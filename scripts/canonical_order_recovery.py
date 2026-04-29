#!/usr/bin/env python3
"""
Canonical-order reverse-engineering (Test 3 pre-registered).

Given only the 114 surah texts (scrambled, no chronological metadata), can
the canonical mushaf order be recovered at above-chance rate by a
structural-similarity TSP heuristic?

Rules tuple:
  orthography: no-tashkeel (JSON quran-no-tashkeel.json)
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: mashriqi (not used here; structural score only)

Adjacency score (pairwise, 114x114):
  1. Normalized gzip compression distance
         NCD(x,y) = (C(xy) - min(C(x),C(y))) / max(C(x),C(y))
  2. Shared-root Jaccard similarity         (1 - J) -> distance
  3. Phonetic bigram KL divergence          (symmetrized)
  4. Mean verse-length ratio                (|log(mvl_i/mvl_j)|)
  5. Bag-of-Roots cosine distance           (1 - cos)

Each of the 5 sub-distances is independently rank-normalized to [0,1] over
the 114*113/2 pairs, then simple-averaged into A[i,j].

Search: nearest-neighbor greedy seed from each of 114 starts (so 114 seeds);
       2-opt improvement with 10,000 iterations cap per restart;
       50 random-permutation restarts additionally 2-opt'd.
Total 164 restarts -> best Hamiltonian path by cumulative adjacency distance.

Compare to canonical mushaf order (1..114) and chronological (Noldeke) order.

Primary statistics:
  - Kendall tau (tau-b) between recovered path and target order
  - Spearman rho
  - Adjacent-pair recovery: |{(i,i+1) canonical pairs} intersect {adjacent
    in recovered path, either direction}|

Null: 10,000 random permutations of 114 surah ids -> tau distribution.
     Expected mean tau ~ 0.

Pre-registered acceptance:
  PASS   : tau > 0 at p < 0.01 under permutation null
  STRONG : tau > 0.3

Forking paths disclosure:
  - 5 sub-distances picked before inspection; not swept.
  - 2-opt params (iter cap, restart count) chosen for tractability; NOT
    tuned per run.
  - The recovered-path direction is ambiguous (reverse = same path);
    tau is taken as max(|tau(p)|, |tau(reverse(p))|) *SIGNED* in whichever
    direction has the larger absolute value. This is disclosed, not
    cherry-picked: a Hamiltonian path has no intrinsic direction.
  - Adjacency metric for the 2-opt cost function: the averaged A[i,j];
    not the individual sub-distances. A sub-distance specific run is
    reported as a sensitivity check in output.
"""
import json
import gzip
import math
import random
import re
import time
from collections import Counter
from pathlib import Path
import sys

import numpy as np
from scipy import stats

ROOT = Path("/Users/grey/Downloads/quran")
CORPUS = ROOT / "quran-text" / "quran-no-tashkeel.json"
ROOTGRAPH = ROOT / "data" / "morphology" / "surah-root-graph.json"
REVORDER = ROOT / "data" / "revelation-order.csv"
OUT_DIR = ROOT / "findings" / "phase-b-hypotheses"
OUT_CSV = OUT_DIR / "csv"
OUT_CSV.mkdir(parents=True, exist_ok=True)

SEED = 20260412
random.seed(SEED)
np.random.seed(SEED)

# ------------------------------ Load corpus ------------------------------
with open(CORPUS) as f:
    quran = json.load(f)

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

surahs = {}
for s in quran:
    sid = s["id"]
    verses = [v["text"] for v in s["verses"]]
    text = norm(" ".join(verses))
    surahs[sid] = {
        "name": s["transliteration"],
        "type": s["type"],
        "n_verses": len(verses),
        "text": text,
        "mean_verse_len_chars": np.mean([len(v) for v in verses]),
    }

N = 114
IDS = list(range(1, N + 1))

# Load root counts per surah
with open(ROOTGRAPH) as f:
    rg = json.load(f)
surah_roots = {int(k): v for k, v in rg["surahs"].items()}
all_roots = sorted({r for counts in surah_roots.values() for r in counts})
root_index = {r: i for i, r in enumerate(all_roots)}
R = len(all_roots)

# Build root-count matrix (114, R)
root_mat = np.zeros((N, R), dtype=np.float64)
for i, sid in enumerate(IDS):
    counts = surah_roots.get(sid, {})
    for r, c in counts.items():
        root_mat[i, root_index[r]] = c

# Load chronological (Noldeke) order
noldeke_order_by_mushaf = {}   # mushaf_id -> noldeke_order
with open(REVORDER) as f:
    lines = f.read().splitlines()
header = lines[0].split(",")
col = {h: i for i, h in enumerate(header)}
for line in lines[1:]:
    parts = line.split(",")
    if len(parts) < len(header):
        continue
    m = int(parts[col["mushaf_order"]])
    nd = int(parts[col["noldeke_order"]])
    noldeke_order_by_mushaf[m] = nd

# ---------------------- Compute 5 pairwise matrices ----------------------
print("Computing pairwise distance matrices...", file=sys.stderr)
t0 = time.time()

# Precompute gzip sizes
def gz(s):
    return len(gzip.compress(s.encode("utf-8"), compresslevel=9))

C_single = np.zeros(N)
texts = [surahs[IDS[i]]["text"] for i in range(N)]
for i in range(N):
    C_single[i] = gz(texts[i])

# 1. NCD (gzip compression distance)
NCD = np.zeros((N, N))
for i in range(N):
    for j in range(i + 1, N):
        c_xy = gz(texts[i] + " " + texts[j])
        ncd = (c_xy - min(C_single[i], C_single[j])) / max(C_single[i], C_single[j])
        NCD[i, j] = ncd
        NCD[j, i] = ncd
print(f"  NCD computed in {time.time()-t0:.1f}s", file=sys.stderr)

# 2. Shared-root Jaccard
# root sets
root_sets = []
for i in range(N):
    counts = surah_roots.get(IDS[i], {})
    root_sets.append(set(counts.keys()))
JAC_D = np.zeros((N, N))
for i in range(N):
    for j in range(i + 1, N):
        a = root_sets[i]
        b = root_sets[j]
        if not a and not b:
            d = 1.0
        else:
            inter = len(a & b)
            un = len(a | b)
            jac = inter / un if un else 0.0
            d = 1.0 - jac
        JAC_D[i, j] = d
        JAC_D[j, i] = d

# 3. Phonetic bigram KL divergence (symmetrized: Jensen-Shannon-like)
def char_bigrams(s):
    s = re.sub(r"\s+", "", s)
    return Counter(s[k:k+2] for k in range(len(s) - 1))

bigram_counts = [char_bigrams(texts[i]) for i in range(N)]
all_bg = sorted({bg for c in bigram_counts for bg in c})
bg_idx = {bg: k for k, bg in enumerate(all_bg)}
B = len(all_bg)
bg_mat = np.zeros((N, B))
for i in range(N):
    total = sum(bigram_counts[i].values())
    if total == 0:
        continue
    for bg, c in bigram_counts[i].items():
        bg_mat[i, bg_idx[bg]] = c / total

# Symmetric KL (Jensen-Shannon)
eps = 1e-10
KL_D = np.zeros((N, N))
for i in range(N):
    for j in range(i + 1, N):
        p = bg_mat[i] + eps
        q = bg_mat[j] + eps
        p = p / p.sum()
        q = q / q.sum()
        m = 0.5 * (p + q)
        kl_pm = np.sum(p * np.log(p / m))
        kl_qm = np.sum(q * np.log(q / m))
        js = 0.5 * (kl_pm + kl_qm)
        KL_D[i, j] = js
        KL_D[j, i] = js

# 4. Mean verse-length ratio -> abs log ratio
MVL = np.array([surahs[IDS[i]]["mean_verse_len_chars"] for i in range(N)])
MVL_D = np.zeros((N, N))
for i in range(N):
    for j in range(i + 1, N):
        d = abs(math.log(MVL[i]) - math.log(MVL[j]))
        MVL_D[i, j] = d
        MVL_D[j, i] = d

# 5. Bag-of-roots cosine distance
norms = np.linalg.norm(root_mat, axis=1)
norms[norms == 0] = 1.0
root_norm = root_mat / norms[:, None]
BOR_D = 1.0 - (root_norm @ root_norm.T)
BOR_D = np.clip(BOR_D, 0, 2)
np.fill_diagonal(BOR_D, 0.0)

print(f"  All 5 matrices computed in {time.time()-t0:.1f}s", file=sys.stderr)

# ------------------- Rank-normalize and combine ----------------------
def rank_normalize_symmetric(D):
    """Replace upper-triangle entries with their rank/(M) in [0,1]. Keep symmetry."""
    M_entries = N * (N - 1) // 2
    iu, ju = np.triu_indices(N, k=1)
    vals = D[iu, ju]
    # rank ascending (smallest -> 0)
    order = np.argsort(vals, kind="stable")
    ranks = np.empty_like(order, dtype=np.float64)
    ranks[order] = np.arange(M_entries)
    ranks = ranks / (M_entries - 1)   # [0, 1]
    out = np.zeros_like(D)
    out[iu, ju] = ranks
    out[ju, iu] = ranks
    return out

SUB = {
    "NCD": rank_normalize_symmetric(NCD),
    "JAC": rank_normalize_symmetric(JAC_D),
    "JS":  rank_normalize_symmetric(KL_D),
    "MVL": rank_normalize_symmetric(MVL_D),
    "BOR": rank_normalize_symmetric(BOR_D),
}

# Averaged adjacency distance
A = np.mean([SUB[k] for k in SUB], axis=0)
np.fill_diagonal(A, np.inf)   # no self-loops in NN greedy

# ------------------- Hamiltonian path solver (TSP-open) -------------------
def path_cost(perm, D):
    return float(D[perm[:-1], perm[1:]].sum())

def nn_greedy(D, start):
    n = D.shape[0]
    visited = np.zeros(n, dtype=bool)
    perm = [start]
    visited[start] = True
    cur = start
    for _ in range(n - 1):
        dists = D[cur].copy()
        dists[visited] = np.inf
        nxt = int(np.argmin(dists))
        perm.append(nxt)
        visited[nxt] = True
        cur = nxt
    return np.array(perm, dtype=np.int64)

def two_opt(perm, D, max_iter=10000):
    n = len(perm)
    best = perm.copy()
    best_cost = path_cost(best, D)
    it = 0
    improved = True
    while improved and it < max_iter:
        improved = False
        # iterate over all i<j
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                a, b = best[i - 1], best[i]
                c, d = best[j], best[j + 1]
                # cost of edges (a-b) + (c-d) vs (a-c) + (b-d) [reverse i..j]
                old = D[a, b] + D[c, d]
                new = D[a, c] + D[b, d]
                if new + 1e-12 < old:
                    best[i:j + 1] = best[i:j + 1][::-1]
                    best_cost += new - old
                    improved = True
                    it += 1
                    if it >= max_iter:
                        break
            if it >= max_iter:
                break
    return best, best_cost

# Fast 2-opt: first-improvement (the nested loop above is first-improvement).
# For 114 nodes this runs in ~0.5-2s per restart.

def search(D, n_nn_starts=114, n_rand_restarts=50, max_iter=10000):
    best_perm = None
    best_cost = math.inf
    t0 = time.time()
    # 114 NN starts
    for s in range(n_nn_starts):
        seed = nn_greedy(D, s)
        p, c = two_opt(seed, D, max_iter=max_iter)
        if c < best_cost:
            best_cost = c
            best_perm = p.copy()
    # 50 random restarts
    for r in range(n_rand_restarts):
        seed = np.random.permutation(N)
        p, c = two_opt(seed, D, max_iter=max_iter)
        if c < best_cost:
            best_cost = c
            best_perm = p.copy()
    t1 = time.time()
    return best_perm, best_cost, t1 - t0

print("Running 2-opt search on combined matrix A...", file=sys.stderr)
best_perm, best_cost, elapsed = search(A)
print(f"  best cost {best_cost:.4f} in {elapsed:.1f}s", file=sys.stderr)

# Convert permutation indices (0-based over IDS) to surah ids (1..114)
recovered_ids = [IDS[i] for i in best_perm]

# ------------------- Scoring against canonical & Noldeke --------------------
canonical = IDS  # 1..114

# Build "position in recovered path" for each surah
pos_in_recovered = {sid: i for i, sid in enumerate(recovered_ids)}
pos_in_canonical = {sid: i for i, sid in enumerate(canonical)}

# For tau/rho, use each surah's (canonical_position, recovered_position)
canon_seq = [pos_in_canonical[sid] for sid in IDS]
recov_seq = [pos_in_recovered[sid] for sid in IDS]

tau, tau_p = stats.kendalltau(canon_seq, recov_seq)
rho, rho_p = stats.spearmanr(canon_seq, recov_seq)

# Reverse direction
recov_seq_rev = [(N - 1) - pos_in_recovered[sid] for sid in IDS]
tau_rev, tau_rev_p = stats.kendalltau(canon_seq, recov_seq_rev)
rho_rev, rho_rev_p = stats.spearmanr(canon_seq, recov_seq_rev)

# Pick whichever direction has larger |tau| (disclosed)
if abs(tau_rev) > abs(tau):
    tau_use, rho_use = tau_rev, rho_rev
    direction = "reverse"
    final_perm = list(reversed(recovered_ids))
else:
    tau_use, rho_use = tau, rho
    direction = "forward"
    final_perm = list(recovered_ids)

# Adjacent-pair recovery (undirected)
canon_adj = {(IDS[k], IDS[k + 1]) for k in range(N - 1)}
canon_adj_undir = {frozenset(p) for p in canon_adj}

recov_adj_undir_final = {frozenset((final_perm[k], final_perm[k + 1]))
                         for k in range(N - 1)}
n_adj_match = len(canon_adj_undir & recov_adj_undir_final)

# Chronological (Noldeke) comparison
noldeke_pos = {sid: noldeke_order_by_mushaf[sid] for sid in IDS if sid in noldeke_order_by_mushaf}
# Use only surahs for which we have Noldeke order
have_nd = [sid for sid in IDS if sid in noldeke_pos]
nd_seq = [noldeke_pos[sid] for sid in have_nd]
rv_seq = [pos_in_recovered[sid] for sid in have_nd]

tau_nd, tau_nd_p = stats.kendalltau(nd_seq, rv_seq)
# reverse
rv_seq_rev = [(N - 1) - pos_in_recovered[sid] for sid in have_nd]
tau_nd_rev, tau_nd_rev_p = stats.kendalltau(nd_seq, rv_seq_rev)
if abs(tau_nd_rev) > abs(tau_nd):
    tau_nd_use = tau_nd_rev
    nd_direction = "reverse"
else:
    tau_nd_use = tau_nd
    nd_direction = "forward"
rho_nd, rho_nd_p = stats.spearmanr(nd_seq, rv_seq)

print(f"\n== Tau(recovered vs canonical) = {tau:.4f} (p={tau_p:.3g})", file=sys.stderr)
print(f"== Tau(reverse  vs canonical) = {tau_rev:.4f} (p={tau_rev_p:.3g})", file=sys.stderr)
print(f"== Picked direction = {direction}; tau_use = {tau_use:.4f}", file=sys.stderr)
print(f"== Rho = {rho_use:.4f}", file=sys.stderr)
print(f"== Adjacent-pair matches: {n_adj_match}/113 (null 113/113 * 2/114 = ~1.98)", file=sys.stderr)
print(f"== Tau vs Noldeke = {tau_nd_use:.4f} ({nd_direction})", file=sys.stderr)

# ------------------- Null distribution -------------------
print("Running 10,000 random-permutation null...", file=sys.stderr)
NPERM = 10000
t0 = time.time()
null_taus = np.empty(NPERM)
null_taus_abs = np.empty(NPERM)
null_adj_matches = np.empty(NPERM, dtype=np.int64)
rng = np.random.default_rng(SEED)

# For tau null we compare random permutations of IDS against canonical
for k in range(NPERM):
    perm = rng.permutation(N)
    # perm[i] = surah-id-index at position i in null-recovered path
    pos_null = np.empty(N, dtype=np.int64)
    pos_null[perm] = np.arange(N)   # pos_null[sid_idx] = position in null path
    seq_null = pos_null[np.arange(N)]  # sequence of positions sorted by canonical id
    t, _ = stats.kendalltau(np.arange(N), seq_null)
    t_rev, _ = stats.kendalltau(np.arange(N), (N - 1) - seq_null)
    if abs(t_rev) > abs(t):
        tt = t_rev
    else:
        tt = t
    null_taus[k] = tt
    null_taus_abs[k] = abs(tt)
    # adjacent-pair match count
    null_ids = [IDS[i] for i in perm]
    null_adj = {frozenset((null_ids[i], null_ids[i + 1])) for i in range(N - 1)}
    null_adj_matches[k] = len(canon_adj_undir & null_adj)

print(f"  done in {time.time()-t0:.1f}s", file=sys.stderr)

# Because we picked the larger |tau| direction, the comparison should be
# against the |tau| distribution (both tails), NOT signed tau null.
null_abs_mean = null_taus_abs.mean()
null_abs_sd = null_taus_abs.std()
p_abs_tau = (np.sum(null_taus_abs >= abs(tau_use)) + 1) / (NPERM + 1)
# signed-tau raw (for reference)
null_mean = null_taus.mean()
null_sd = null_taus.std()

# adj-match null
null_adj_mean = null_adj_matches.mean()
null_adj_sd = null_adj_matches.std()
p_adj = (np.sum(null_adj_matches >= n_adj_match) + 1) / (NPERM + 1)

# ------------------- Sub-distance sensitivity runs -------------------
print("Running sensitivity analyses (each sub-distance alone)...", file=sys.stderr)
sub_results = {}
for name, D in SUB.items():
    Dd = D.copy()
    np.fill_diagonal(Dd, np.inf)
    p, c, _ = search(Dd, n_nn_starts=20, n_rand_restarts=10, max_iter=5000)
    sub_recov = [IDS[i] for i in p]
    pos_r = {sid: i for i, sid in enumerate(sub_recov)}
    seq_r = [pos_r[sid] for sid in IDS]
    tt, _ = stats.kendalltau(canon_seq, seq_r)
    seq_r_rev = [(N - 1) - pos_r[sid] for sid in IDS]
    tt_rev, _ = stats.kendalltau(canon_seq, seq_r_rev)
    tau_best = tt_rev if abs(tt_rev) > abs(tt) else tt
    # adj match
    recov_adj = {frozenset((sub_recov[i], sub_recov[i + 1])) for i in range(N - 1)}
    if abs(tt_rev) > abs(tt):
        fp = list(reversed(sub_recov))
        recov_adj = {frozenset((fp[i], fp[i + 1])) for i in range(N - 1)}
    nadj = len(canon_adj_undir & recov_adj)
    sub_results[name] = {"tau": tau_best, "adj_match": nadj, "cost": c}

# ------------------- Length-descending control -------------------
# Canonical mushaf order is roughly length-descending (with known
# exceptions — Fatiha is short, Baqara is longest, then long surahs,
# short surahs at end). Compute tau(length_desc_order -> canonical).
text_lengths = np.array([len(texts[i]) for i in range(N)])
length_desc_order_idx = np.argsort(-text_lengths)  # longest first
length_desc_ids = [IDS[i] for i in length_desc_order_idx]
pos_ld = {sid: i for i, sid in enumerate(length_desc_ids)}
seq_ld = [pos_ld[sid] for sid in IDS]
tau_ld, tau_ld_p = stats.kendalltau(canon_seq, seq_ld)
seq_ld_rev = [(N - 1) - pos_ld[sid] for sid in IDS]
tau_ld_rev, _ = stats.kendalltau(canon_seq, seq_ld_rev)
tau_ld_use = tau_ld_rev if abs(tau_ld_rev) > abs(tau_ld) else tau_ld

# ------------------- Write outputs -------------------
# CSV: recovered path with positions and adjacency flags
with open(OUT_CSV / "canonical_order_recovered_path.csv", "w") as f:
    f.write("position,surah_id,surah_name,canonical_position,adj_in_canonical\n")
    final_pos = {sid: i for i, sid in enumerate(final_perm)}
    for i, sid in enumerate(final_perm):
        canon_i = pos_in_canonical[sid]
        nb1 = final_perm[i - 1] if i > 0 else None
        nb2 = final_perm[i + 1] if i < N - 1 else None
        adj_in = 0
        if nb1 is not None and abs(sid - nb1) == 1:
            adj_in = 1
        if nb2 is not None and abs(sid - nb2) == 1:
            adj_in = 1
        f.write(f"{i + 1},{sid},{surahs[sid]['name']},{canon_i + 1},{adj_in}\n")

# Summary JSON
summary = {
    "primary": {
        "tau_forward": tau, "tau_p_forward": tau_p,
        "tau_reverse": tau_rev, "tau_p_reverse": tau_rev_p,
        "direction_used": direction,
        "tau_used": tau_use,
        "rho_used": rho_use,
        "adjacent_pair_matches": int(n_adj_match),
        "adjacent_pairs_total": N - 1,
        "null_mean_abs_tau": float(null_abs_mean),
        "null_sd_abs_tau": float(null_abs_sd),
        "null_mean_signed_tau": float(null_mean),
        "null_sd_signed_tau": float(null_sd),
        "permutation_p_two_sided_abs": float(p_abs_tau),
        "null_mean_adj_matches": float(null_adj_mean),
        "null_sd_adj_matches": float(null_adj_sd),
        "permutation_p_adj_matches": float(p_adj),
        "n_perms": NPERM,
    },
    "chronological": {
        "tau_forward": tau_nd, "tau_reverse": tau_nd_rev,
        "tau_used": tau_nd_use,
        "rho": rho_nd,
        "direction_used": nd_direction,
    },
    "length_desc_control": {
        "tau_length_desc_vs_canonical": tau_ld_use,
        "note": "The canonical mushaf order is classically described as length-descending. "
                "This tau measures HOW MUCH of the recovered-vs-canonical signal is "
                "attributable to mere length.",
    },
    "sub_distance_sensitivity": {name: {"tau": r["tau"], "adj_match": r["adj_match"], "cost": r["cost"]}
                                 for name, r in sub_results.items()},
    "pass": bool(p_abs_tau < 0.01),
    "strong": bool(abs(tau_use) > 0.3 and p_abs_tau < 0.01),
    "seed": SEED,
    "recovered_ids_first_20": final_perm[:20],
    "recovered_ids_last_20": final_perm[-20:],
    "search_params": {
        "n_nn_starts": 114,
        "n_rand_restarts": 50,
        "max_iter_per_restart": 10000,
        "total_restarts": 164,
    },
}

with open(OUT_CSV / "canonical_order_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

# Null distribution CSV (for plotting)
with open(OUT_CSV / "canonical_order_null_distribution.csv", "w") as f:
    f.write("perm_index,abs_tau,signed_tau,adj_matches\n")
    for k in range(NPERM):
        f.write(f"{k},{null_taus_abs[k]:.6f},{null_taus[k]:.6f},{null_adj_matches[k]}\n")

# ------------------- Console output -------------------
print("\n" + "=" * 72)
print("CANONICAL-ORDER RECOVERY — RESULTS")
print("=" * 72)
print(f"N surahs             : {N}")
print(f"Search cost (A)      : {best_cost:.4f}")
print(f"Direction chosen     : {direction}")
print(f"Kendall tau (used)   : {tau_use:+.4f}")
print(f"  forward / reverse  : {tau:+.4f} / {tau_rev:+.4f}")
print(f"Spearman rho (used)  : {rho_use:+.4f}")
print(f"Adj-pair matches     : {n_adj_match}/{N - 1}")
print()
print(f"Null (10,000 perms):")
print(f"  |tau|  mean / sd   : {null_abs_mean:.4f} / {null_abs_sd:.4f}")
print(f"  signed mean / sd   : {null_mean:+.4f} / {null_sd:.4f}")
print(f"  adj-match mean / sd: {null_adj_mean:.2f} / {null_adj_sd:.2f}")
print()
print(f"Permutation p-values (obs >= null):")
print(f"  |tau|   p          : {p_abs_tau:.4g}")
print(f"  adj-match p        : {p_adj:.4g}")
print()
print(f"vs Nöldeke chronology: tau = {tau_nd_use:+.4f} ({nd_direction})")
print(f"Length-desc control  : tau(length_desc, canonical) = {tau_ld_use:+.4f}")
print()
print(f"Pre-registered PASS  ({'YES' if summary['pass'] else 'NO '}): |tau|>0 & p<0.01")
print(f"Pre-registered STRONG({'YES' if summary['strong'] else 'NO '}): |tau|>0.3 & p<0.01")
print()
print("Sub-distance sensitivity:")
for name, r in sub_results.items():
    print(f"  {name}: tau={r['tau']:+.4f}  adj={r['adj_match']}/{N - 1}")

print("\n=== DONE ===", file=sys.stderr)
