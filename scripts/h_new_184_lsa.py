#!/usr/bin/env python3
"""H-NEW-184 — Latent Semantic Analysis of 114 surahs × top-1000 roots.

Seed 20260419. Bonferroni k=3.
"""

import csv
import re
import json
import pathlib
import sys
from collections import Counter, defaultdict

import numpy as np

SEED = 20260419
np.random.seed(SEED)

ROOT = pathlib.Path("/Users/grey/Downloads/quran")
MORPH = ROOT / "data" / "morphology" / "quranic-corpus-morphology-0.4.txt"
REV = ROOT / "data" / "revelation-order.csv"

# ---- 1. Parse morphology file: build (surah -> root -> count) -----------

ROOT_RE = re.compile(r"ROOT:([A-Za-z~`<>\{\}\$\^]+)")
LOC_RE = re.compile(r"\((\d+):(\d+):\d+:\d+\)")

surah_root = defaultdict(Counter)
with open(MORPH, encoding="utf-8") as f:
    for line in f:
        if not line.startswith("("):
            continue
        loc = LOC_RE.match(line)
        if not loc:
            continue
        s = int(loc.group(1))
        m = ROOT_RE.search(line)
        if m:
            surah_root[s][m.group(1)] += 1

print(f"[info] parsed roots for {len(surah_root)} surahs")

# ---- 2. Top-1000 roots by total occurrence -------------------------------

total = Counter()
for s, counts in surah_root.items():
    total.update(counts)

TOP_K = 1000
top_roots = [r for r, _ in total.most_common(TOP_K)]
root_idx = {r: i for i, r in enumerate(top_roots)}
print(f"[info] top-{TOP_K} roots cover {sum(total[r] for r in top_roots)}/{sum(total.values())} tokens = "
      f"{100*sum(total[r] for r in top_roots)/sum(total.values()):.1f}%")

N = 114
K = TOP_K
X = np.zeros((N, K), dtype=np.float64)
for s in range(1, N + 1):
    for r, c in surah_root[s].items():
        j = root_idx.get(r)
        if j is not None:
            X[s - 1, j] = c

# ---- 3. TF-IDF weighting + L2 row-normalize -----------------------------

df = (X > 0).sum(axis=0)  # doc-frequency per root
idf = np.log(N / np.maximum(df, 1))
tf = X  # raw counts
tfidf = tf * idf[None, :]
# L2 normalize per surah
norms = np.linalg.norm(tfidf, axis=1, keepdims=True)
norms[norms == 0] = 1
tfidf_n = tfidf / norms

# ---- 4. Truncated SVD (k=20) --------------------------------------------

U, S, Vt = np.linalg.svd(tfidf_n, full_matrices=False)
# U: 114 × 114, S: 114, Vt: 114 × 1000
k = 20
U_k = U[:, :k]
S_k = S[:k]
V_k = Vt[:k, :]  # k × 1000
print(f"[info] top singular values: {S[:5]}")

# explained variance ratios
ev = (S ** 2) / (S ** 2).sum()
print(f"[info] EV top-3: {ev[:3]} sum={ev[:3].sum():.4f}")
print(f"[info] EV top-10: {ev[:10].sum():.4f}")
print(f"[info] EV top-20: {ev[:20].sum():.4f}")

# ---- 5. Interpret top-3 SVs by root loadings ----------------------------

def top_loadings(v, labels, n=12):
    order = np.argsort(v)
    neg = [(labels[i], float(v[i])) for i in order[:n]]
    pos = [(labels[i], float(v[i])) for i in order[-n:][::-1]]
    return pos, neg

sv_interp = {}
for i in range(3):
    pos, neg = top_loadings(V_k[i], top_roots, n=12)
    sv_interp[f"SV{i+1}"] = {"positive": pos, "negative": neg, "sigma": float(S[i])}
    print(f"\n=== SV{i+1} (σ={S[i]:.3f}) ===")
    print("  POS:", [p[0] for p in pos])
    print("  NEG:", [p[0] for p in neg])

# ---- 6. Project 114 onto SV1..SV3 (scores) ------------------------------

scores = U_k * S_k[None, :]  # N × k

# ---- 7. Meccan/Medinan labels for T1 ------------------------------------

period = {}
with open(REV, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        period[int(row["mushaf_order"])] = row["period"]
y = np.array([1 if period.get(i + 1) == "Medinan" else 0 for i in range(N)])
print(f"[info] Medinan count: {y.sum()} / {N}")

def auc(scores1d, y):
    order = np.argsort(scores1d)
    y_sorted = y[order]
    n1 = y.sum(); n0 = (1 - y).sum()
    if n1 == 0 or n0 == 0:
        return 0.5
    ranks = np.arange(1, len(y) + 1)
    sum_ranks_pos = ranks[y_sorted == 1].sum()
    return (sum_ranks_pos - n1 * (n1 + 1) / 2) / (n1 * n0)

auc_sv1 = auc(scores[:, 0], y)
auc_sv1_flip = max(auc_sv1, 1 - auc_sv1)
print(f"[T1] AUC SV1 vs Medinan: {auc_sv1:.4f} (flip={auc_sv1_flip:.4f})")
auc_sv2 = auc(scores[:, 1], y); auc_sv2f = max(auc_sv2, 1 - auc_sv2)
auc_sv3 = auc(scores[:, 2], y); auc_sv3f = max(auc_sv3, 1 - auc_sv3)
print(f"[info] AUC SV2: {auc_sv2f:.4f}  AUC SV3: {auc_sv3f:.4f}")

# ---- 8. LSA-M1 mushaf-neighbour test ------------------------------------

# Cosine similarity in LSA k=20 space
sim = U_k @ U_k.T  # since U orthonormal; use scores instead for cosine in weighted space
# Use L2-normalized scores (weighted by σ)
sc_norm = scores / np.linalg.norm(scores, axis=1, keepdims=True)
cos = sc_norm @ sc_norm.T
np.fill_diagonal(cos, -np.inf)

nn = np.argmax(cos, axis=1)  # nearest-neighbour index
adj = np.sum(np.abs(nn - np.arange(N)) == 1)
print(f"[T2] LSA-NN adjacency: {adj}/{N}")

# Permutation null: each surah gets a random mushaf position; count how many
# nearest-neighbour pairs are |pos_i - pos_nn[i]| == 1 under the random assignment.
rng = np.random.default_rng(SEED)
null = np.zeros(10000, dtype=int)
for b in range(10000):
    perm_pos = rng.permutation(N)  # pos[i] = new mushaf position of surah i
    # original nn pair is (i, nn[i]); under permutation they get positions perm_pos[i] and perm_pos[nn[i]]
    null[b] = np.sum(np.abs(perm_pos - perm_pos[nn]) == 1)
pval_T2 = (null >= adj).mean()
print(f"[T2] null mean: {null.mean():.2f}  std: {null.std():.2f}  p={pval_T2:.4f}  (99.5 pctile={np.percentile(null,99.5):.1f})")

# ---- T3: top-3 SV EV vs null (column-permutation) -----------------------

ev3 = ev[:3].sum()
B = 200
null_ev3 = np.zeros(B)
rng2 = np.random.default_rng(SEED + 1)
for b in range(B):
    Xp = tfidf_n.copy()
    for j in range(K):
        Xp[:, j] = rng2.permutation(Xp[:, j])
    Sp = np.linalg.svd(Xp, compute_uv=False)
    evp = (Sp ** 2) / (Sp ** 2).sum()
    null_ev3[b] = evp[:3].sum()
z_T3 = (ev3 - null_ev3.mean()) / null_ev3.std()
print(f"[T3] EV top-3 obs: {ev3:.4f}  null: {null_ev3.mean():.4f}±{null_ev3.std():.4f}  z={z_T3:.2f}")

# ---- Extreme surahs per SV ----------------------------------------------

extremes = {}
for i in range(3):
    order = np.argsort(scores[:, i])
    extremes[f"SV{i+1}"] = {
        "low": [(int(order[j] + 1), float(scores[order[j], i])) for j in range(6)],
        "high": [(int(order[-j - 1] + 1), float(scores[order[-j - 1], i])) for j in range(6)],
    }
    print(f"\n  SV{i+1} low: {extremes[f'SV{i+1}']['low']}")
    print(f"  SV{i+1} high: {extremes[f'SV{i+1}']['high']}")

# ---- Nearest-neighbour pairs sample -------------------------------------

nn_pairs = [(i + 1, int(nn[i]) + 1, float(cos[i, nn[i]])) for i in range(N)]
# Print top-10 tightest pairs
tight = sorted(nn_pairs, key=lambda t: -t[2])[:15]
print("\n[info] tightest NN pairs:")
for a, b, c in tight:
    print(f"  Q{a:>3} <-> Q{b:>3}  cos={c:.4f}  mushaf|Δ|={abs(a-b)}")

# ---- Save results --------------------------------------------------------

out = {
    "seed": SEED,
    "N": N, "K": K,
    "ev": ev[:20].tolist(),
    "ev_top3": float(ev3),
    "sigma_top5": S[:5].tolist(),
    "sv_interp": sv_interp,
    "extremes": extremes,
    "T1_auc_sv1": auc_sv1_flip,
    "T1_auc_sv2": auc_sv2f,
    "T1_auc_sv3": auc_sv3f,
    "T2_lsa_nn_adj": int(adj),
    "T2_null_mean": float(null.mean()),
    "T2_null_std": float(null.std()),
    "T2_pval": float(pval_T2),
    "T2_null_99_5pct": float(np.percentile(null, 99.5)),
    "T3_z": float(z_T3),
    "T3_null_mean": float(null_ev3.mean()),
    "T3_null_std": float(null_ev3.std()),
    "nn_map": [int(x) + 1 for x in nn],
    "tight_pairs_top15": tight,
}
OUTJ = ROOT / "findings" / "phase-b-hypotheses" / "h-new-184-lsa-results.json"
with open(OUTJ, "w") as f:
    json.dump(out, f, indent=2)
print(f"\n[wrote] {OUTJ}")
