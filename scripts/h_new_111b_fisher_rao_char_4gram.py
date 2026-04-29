#!/usr/bin/env python3
"""H-NEW-111b — Fisher-Rao char-4-gram replication of H-NEW-111.

Orthogonal-feature replication of H-NEW-111 (root-token Fisher-Rao geodesicity).

Pre-registered tests (Bonferroni k=3, α_bon=0.0167):
  PRIMARY   — L_mushaf < L_random at permutation p<0.0167 (1-sided lower-tail)
  SECONDARY A — L_mushaf / L_2opt ratio (REPLICATE near-optimal <1.2)
  SECONDARY B — L_mushaf ≤ L_nold (REPLICATE chronology reversal, 1-sided lower)

MW-1: length control via L1-normalization of per-surah 4-gram distributions.
MW-5: greedy-NN-from-surah-1 synthetic ordering serves as positive control.

K_char = 2000 locked before running (see pre-reg).
Seed 20260417 (same as H-NEW-111 for comparability).
"""
import csv
import hashlib
import json
import math
import random
import statistics
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
PERMS = 10000

# Locked parameters (see pre-reg)
K_CHAR = 2000
NGRAM_N = 4
DIRICHLET_ALPHA = 0.5

# Paths
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-111b-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111b.json'

# Pre-reg hash (tamper-evidence)
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"K_CHAR = {K_CHAR}", file=sys.stderr)
print(f"NGRAM_N = {NGRAM_N}", file=sys.stderr)
print(f"DIRICHLET_ALPHA = {DIRICHLET_ALPHA}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Load no-tashkeel Quran and build per-surah concatenated text
# ---------------------------------------------------------------------------
quran = json.loads(QURAN_JSON.read_text(encoding='utf-8'))
assert len(quran) == 114, f"Expected 114 surahs, got {len(quran)}"

# Confirm surah 1 verse 1 is basmala (counted only there) and surah 2
# starts with الم (not basmala) — matches rules-tuple.
assert quran[0]['verses'][0]['text'].startswith('بسم'), \
    "Surah 1 v1 should be basmala"
assert not quran[1]['verses'][0]['text'].startswith('بسم'), \
    "Surah 2 v1 should NOT be basmala (basmala-counted-only-in-surah-1)"

per_surah_text = {}  # sid -> str
per_surah_nverses = {}
for s in quran:
    sid = s['id']
    verses = [v['text'] for v in s['verses']]
    # single space between verses (mirrors standard recitation spacing)
    per_surah_text[sid] = ' '.join(verses)
    per_surah_nverses[sid] = len(verses)

assert len(per_surah_text) == 114

total_chars = sum(len(t) for t in per_surah_text.values())
print(f"surahs: {len(per_surah_text)}", file=sys.stderr)
print(f"total chars (no-tashkeel, space-joined): {total_chars}", file=sys.stderr)
print(f"mean surah chars: {total_chars / 114:.1f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 2. Extract char-4-grams per surah and globally
# ---------------------------------------------------------------------------
def char_ngrams(text, n):
    if len(text) < n:
        return []
    return [text[k:k+n] for k in range(len(text) - n + 1)]

per_surah_grams = {}  # sid -> Counter
global_gram_counts = Counter()

for sid, text in per_surah_text.items():
    grams = char_ngrams(text, NGRAM_N)
    c = Counter(grams)
    per_surah_grams[sid] = c
    global_gram_counts.update(c)

total_grams = sum(global_gram_counts.values())
print(f"total char-{NGRAM_N}-gram tokens (sliding): {total_grams}", file=sys.stderr)
print(f"distinct char-{NGRAM_N}-grams: {len(global_gram_counts)}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 3. Select top-K_char 4-grams (LOCKED K_CHAR = 2000)
# ---------------------------------------------------------------------------
# Ties broken lexicographically for determinism
sorted_grams = sorted(
    global_gram_counts.items(),
    key=lambda kv: (-kv[1], kv[0])
)
top_grams = [g for g, _ in sorted_grams[:K_CHAR]]
top_gram_index = {g: i for i, g in enumerate(top_grams)}

cumulative_topk_mass = sum(global_gram_counts[g] for g in top_grams)
print(f"top-K={K_CHAR} 4-grams selected", file=sys.stderr)
print(f"  top-5: {[(g, global_gram_counts[g]) for g in top_grams[:5]]}", file=sys.stderr)
print(f"  freq cutoff at K-th: {global_gram_counts[top_grams[-1]]}", file=sys.stderr)
print(f"  cumulative coverage: {cumulative_topk_mass / total_grams:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 4. Build per-surah count matrix [114 × K_CHAR], Dirichlet smooth, L1-norm
# ---------------------------------------------------------------------------
counts = np.zeros((115, K_CHAR), dtype=np.float64)  # 1-indexed, row 0 unused
per_surah_topk_coverage = {}
for sid in range(1, 115):
    c = per_surah_grams[sid]
    total_in_surah = sum(c.values())
    in_topk = 0
    for g, n in c.items():
        idx = top_gram_index.get(g)
        if idx is not None:
            counts[sid, idx] += n
            in_topk += n
    per_surah_topk_coverage[sid] = in_topk / total_in_surah if total_in_surah > 0 else 0.0

# Dirichlet α=0.5 smoothing + L1 normalization
smoothed = counts[1:] + DIRICHLET_ALPHA          # shape (114, K)
row_sums = smoothed.sum(axis=1, keepdims=True)
prob = smoothed / row_sums                        # shape (114, K); rows sum to 1

# Sanity
assert prob.shape == (114, K_CHAR)
np.testing.assert_allclose(prob.sum(axis=1), 1.0, atol=1e-12)

# ---------------------------------------------------------------------------
# 5. Fisher-Rao distance matrix via sqrt-probability inner product
# ---------------------------------------------------------------------------
# D[i,j] = 2 * arccos( Σ_k sqrt(p_i[k] * p_j[k]) )
# = 2 * arccos( (sqrt(p_i) · sqrt(p_j)) )
print("\nBuilding 114x114 Fisher-Rao distance matrix...", file=sys.stderr)
sqrt_prob = np.sqrt(prob)                          # (114, K)
bc = sqrt_prob @ sqrt_prob.T                       # (114, 114) Bhattacharyya coeff
np.clip(bc, -1.0, 1.0, out=bc)
D_mat = 2.0 * np.arccos(bc)                        # (114, 114), in [0, pi]
# Numerical floor on diagonal
np.fill_diagonal(D_mat, 0.0)

# 1-indexed wrapper (row 0 / col 0 unused) for parity with parent
D = np.zeros((115, 115), dtype=np.float64)
D[1:, 1:] = D_mat

# Stats
iu = np.triu_indices(114, k=1)
all_d = D_mat[iu]
print(f"  D range: [{all_d.min():.4f}, {all_d.max():.4f}]", file=sys.stderr)
print(f"  D mean: {all_d.mean():.4f}, median: {np.median(all_d):.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. Path length helper
# ---------------------------------------------------------------------------
def path_length(order):
    """order: list of surah IDs (1..114)."""
    a = np.asarray(order, dtype=np.int64)
    return float(D[a[:-1], a[1:]].sum())

mushaf_order = list(range(1, 115))
L_mushaf = path_length(mushaf_order)
print(f"\nL_mushaf = {L_mushaf:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. Null: 10,000 uniform random permutations
# ---------------------------------------------------------------------------
print(f"\nNull: {PERMS} random permutations (seed={SEED})...", file=sys.stderr)
rng = random.Random(SEED)
null_L = np.empty(PERMS, dtype=np.float64)
perm = mushaf_order[:]
for p in range(PERMS):
    rng.shuffle(perm)
    null_L[p] = path_length(perm)
    if (p + 1) % 2000 == 0:
        print(f"  perm {p+1}/{PERMS}", file=sys.stderr)

n_le_mushaf = int((null_L <= L_mushaf).sum())
p_primary = (n_le_mushaf + 1) / (PERMS + 1)

null_mean = float(null_L.mean())
null_sd = float(null_L.std(ddof=1))
print(f"  null L mean={null_mean:.4f} sd={null_sd:.4f}", file=sys.stderr)
print(f"  null L min={null_L.min():.4f} max={null_L.max():.4f}", file=sys.stderr)
print(f"  #{{L_perm <= L_mushaf}} = {n_le_mushaf}", file=sys.stderr)
print(f"  p_primary (1-sided lower) = {p_primary:.6f}", file=sys.stderr)

def q(arr, frac):
    return float(np.quantile(arr, frac))

null_quantiles = {
    'min': float(null_L.min()),
    'q001': q(null_L, 0.001),
    'q01': q(null_L, 0.01),
    'q025': q(null_L, 0.025),
    'q05': q(null_L, 0.05),
    'q25': q(null_L, 0.25),
    'q50': q(null_L, 0.50),
    'q75': q(null_L, 0.75),
    'q95': q(null_L, 0.95),
    'max': float(null_L.max()),
    'mean': null_mean,
    'sd': null_sd,
}

z_mushaf = (L_mushaf - null_mean) / null_sd
print(f"  z(L_mushaf) = {z_mushaf:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. Secondary A — approximate TSP: greedy NN from each start + 2-opt
# ---------------------------------------------------------------------------
print("\nSecondary A: greedy-NN + 2-opt TSP approximation...", file=sys.stderr)

def greedy_nn(start):
    unvisited = set(range(1, 115))
    unvisited.remove(start)
    path = [start]
    cur = start
    while unvisited:
        nxt = min(unvisited, key=lambda v: D[cur, v])
        path.append(nxt)
        unvisited.remove(nxt)
        cur = nxt
    return path

greedy_paths = []
for start in range(1, 115):
    p = greedy_nn(start)
    greedy_paths.append((path_length(p), start, p))
greedy_paths.sort(key=lambda x: x[0])
L_greedy_best = greedy_paths[0][0]
best_start = greedy_paths[0][1]
best_path = greedy_paths[0][2][:]
print(f"  greedy best: start={best_start}, L={L_greedy_best:.4f}", file=sys.stderr)

def two_opt(path, max_passes=50):
    """Standard 2-opt for open path (no return to start)."""
    path = path[:]
    n = len(path)
    passes = 0
    while passes < max_passes:
        passes += 1
        best_delta = 0.0
        best_ij = None
        for i in range(0, n - 2):
            a = path[i]
            b = path[i + 1]
            d_ab = D[a, b]
            for j in range(i + 2, n):
                c = path[j]
                if j + 1 < n:
                    d = path[j + 1]
                    delta = (D[a, c] + D[b, d]) - (d_ab + D[c, d])
                else:
                    delta = D[a, c] - d_ab
                if delta < best_delta - 1e-12:
                    best_delta = delta
                    best_ij = (i, j)
        if best_ij is None:
            break
        i, j = best_ij
        path[i + 1:j + 1] = list(reversed(path[i + 1:j + 1]))
    return path, passes

opt_path, n_passes = two_opt(best_path)
L_2opt = path_length(opt_path)
print(f"  2-opt: L={L_2opt:.4f} ({n_passes} passes)", file=sys.stderr)

# Try 2-opt on all 114 greedy starts for tighter upper bound
L_2opt_best = L_2opt
opt_path_best = opt_path[:]
print("  running 2-opt on all 114 greedy starts...", file=sys.stderr)
for L_g, start, p in greedy_paths:
    if L_g > L_2opt_best * 1.5:
        continue
    p2, _ = two_opt(p)
    Lp = path_length(p2)
    if Lp < L_2opt_best:
        L_2opt_best = Lp
        opt_path_best = p2[:]
        print(f"    improved: start={start}, L={Lp:.4f}", file=sys.stderr)

print(f"  final L_min (approx, 2-opt): {L_2opt_best:.4f}", file=sys.stderr)
ratio_mushaf_opt = L_mushaf / L_2opt_best
print(f"  L_mushaf / L_min ≈ {ratio_mushaf_opt:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. Secondary B — Nöldeke chronology + Tanzil revelation order
# ---------------------------------------------------------------------------
print("\nSecondary B: Nöldeke chronological path...", file=sys.stderr)
rev_rows = []
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rev_rows.append(row)

mushaf_to_noldeke = {int(r['mushaf_order']): int(r['noldeke_order']) for r in rev_rows}
mushaf_to_tanzil = {int(r['mushaf_order']): int(r['revelation_order']) for r in rev_rows}
assert len(mushaf_to_noldeke) == 114

noldeke_order_list = sorted(range(1, 115), key=lambda sid: mushaf_to_noldeke[sid])
tanzil_order_list = sorted(range(1, 115), key=lambda sid: mushaf_to_tanzil[sid])

L_nold = path_length(noldeke_order_list)
L_tanzil = path_length(tanzil_order_list)
print(f"  L_nold   = {L_nold:.4f}", file=sys.stderr)
print(f"  L_tanzil = {L_tanzil:.4f}", file=sys.stderr)

n_le_nold = int((null_L <= L_nold).sum())
n_le_tanzil = int((null_L <= L_tanzil).sum())
p_nold_lower = (n_le_nold + 1) / (PERMS + 1)
p_tanzil_lower = (n_le_tanzil + 1) / (PERMS + 1)

# Pre-registered direction: one-sided lower (L_mushaf ≤ L_nold replication)
sign_mushaf_minus_nold = L_mushaf - L_nold
replicates_reversal = (L_mushaf <= L_nold)
print(f"  p_nold   (1-sided lower) = {p_nold_lower:.6f}", file=sys.stderr)
print(f"  p_tanzil (1-sided lower) = {p_tanzil_lower:.6f}", file=sys.stderr)
print(f"  sign: L_mushaf - L_nold = {sign_mushaf_minus_nold:+.4f}", file=sys.stderr)
print(f"  reversal replicated: {replicates_reversal}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 10. MW-5 positive control: greedy-NN from surah 1
# ---------------------------------------------------------------------------
print("\nMW-5 positive control: greedy-NN from surah 1...", file=sys.stderr)
pos_ctrl_path = greedy_nn(1)
L_pos = path_length(pos_ctrl_path)
n_le_pos = int((null_L <= L_pos).sum())
p_pos = (n_le_pos + 1) / (PERMS + 1)
print(f"  L_positive_control = {L_pos:.4f}  (p = {p_pos:.6f})", file=sys.stderr)
MW5_THRESHOLD = 1e-4
mw5_broken = p_pos >= MW5_THRESHOLD
if mw5_broken:
    print(f"  !! MW-5 POSITIVE CONTROL FAILED at p >= {MW5_THRESHOLD} — null broken !!", file=sys.stderr)
else:
    print(f"  MW-5 positive control PASSES (p < {MW5_THRESHOLD})", file=sys.stderr)

# ---------------------------------------------------------------------------
# 11. Sanity anchors: length-sorted orderings
# ---------------------------------------------------------------------------
len_sorted_asc = sorted(range(1, 115), key=lambda sid: per_surah_nverses[sid])
L_lensort_asc = path_length(len_sorted_asc)
len_sorted_desc = sorted(range(1, 115), key=lambda sid: -per_surah_nverses[sid])
L_lensort_desc = path_length(len_sorted_desc)

# ---------------------------------------------------------------------------
# 12. Write JSON summary
# ---------------------------------------------------------------------------
def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o

# Flatten D to upper-triangular list
D_upper = []
for i in range(1, 115):
    for j in range(i + 1, 115):
        D_upper.append([i, j, float(D[i, j])])

# Primary verdict
pass_primary = bool(p_primary < 0.0167) and (not mw5_broken)
# Secondary A replication
if ratio_mushaf_opt < 1.2:
    sa_interp = 'near-optimal REPLICATED (<1.2)'
elif ratio_mushaf_opt < 1.5:
    sa_interp = 'geodesic-like (<1.5) — partial replication'
elif ratio_mushaf_opt < 2.0:
    sa_interp = 'weaker geodesic-like (<2.0)'
else:
    sa_interp = 'NOT geodesic-like (>=2.0) — replication failed'

# Secondary B replication
sb_pass = bool(p_nold_lower < 0.0167 and L_mushaf <= L_nold)

# Overall replication verdict
if not mw5_broken and pass_primary and ratio_mushaf_opt < 1.2 and sb_pass:
    overall = 'FULL REPLICATION'
elif not mw5_broken and pass_primary and ratio_mushaf_opt < 1.5:
    overall = 'PARTIAL REPLICATION (primary + secondary A; secondary B status separate)'
elif not mw5_broken and pass_primary:
    overall = 'PRIMARY-ONLY REPLICATION'
elif not mw5_broken:
    overall = 'REPLICATION FAILED (null)'
else:
    overall = 'INSTRUMENT-BROKEN'

summary = {
    'finding_id': 'h-new-111b',
    'title': 'Fisher-Rao char-4-gram replication of H-NEW-111',
    'parent_finding': 'h-new-111',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'rules_tuple': '(no-tashkeel, char-4-grams with spaces, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)',
    'locked_params': {
        'K_char_4grams': K_CHAR,
        'ngram_n': NGRAM_N,
        'dirichlet_alpha': DIRICHLET_ALPHA,
        'permutations': PERMS,
        'distance': 'Fisher-Rao angular = 2*arccos(sum sqrt(p_i*p_j))',
        'length_control': 'L1-normalized probability vectors (MW-1)',
        'bonferroni_k': 3,
        'alpha_bon': 0.0167,
    },
    'corpus_stats': {
        'n_surahs': 114,
        'total_chars': total_chars,
        'total_char_4grams_sliding': total_grams,
        'distinct_char_4grams': len(global_gram_counts),
        'top_K_coverage_fraction': cumulative_topk_mass / total_grams,
        'freq_at_K': global_gram_counts[top_grams[-1]],
        'top5_4grams': [[g, global_gram_counts[g]] for g in top_grams[:5]],
    },
    'per_surah_topk_coverage': {str(k): v for k, v in sorted(per_surah_topk_coverage.items())},
    'distance_matrix_stats': {
        'n_pairs': int(len(all_d)),
        'min': float(all_d.min()),
        'max': float(all_d.max()),
        'mean': float(all_d.mean()),
        'median': float(np.median(all_d)),
    },
    'primary': {
        'L_mushaf': L_mushaf,
        'null_quantiles': null_quantiles,
        'z_score': z_mushaf,
        'n_perms_le_mushaf': n_le_mushaf,
        'p_primary_one_sided_lower': p_primary,
        'alpha_bon': 0.0167,
        'pass_primary': pass_primary,
    },
    'secondary_A': {
        'L_greedy_best': L_greedy_best,
        'L_2opt_best': L_2opt_best,
        'ratio_mushaf_over_2opt': ratio_mushaf_opt,
        'interpretation': sa_interp,
        'parent_ratio_on_roots': 1.107,
    },
    'secondary_B': {
        'L_noldeke': L_nold,
        'L_tanzil_egyptian_std': L_tanzil,
        'p_nold_one_sided_lower': p_nold_lower,
        'p_tanzil_one_sided_lower': p_tanzil_lower,
        'delta_mushaf_minus_nold': sign_mushaf_minus_nold,
        'replicates_reversal_sign': replicates_reversal,
        'pass_secondary_B_one_sided': sb_pass,
        'sign_interpretation': (
            'mushaf SHORTER-OR-EQUAL than chronology (reversal REPLICATED)' if replicates_reversal
            else 'chronology SHORTER than mushaf (reversal NOT replicated)'
        ),
    },
    'mw5_positive_control': {
        'method': 'greedy-NN from surah 1',
        'L': L_pos,
        'p_one_sided_lower': p_pos,
        'threshold': MW5_THRESHOLD,
        'pass': bool(not mw5_broken),
    },
    'sanity_anchors': {
        'L_length_sorted_ascending': L_lensort_asc,
        'L_length_sorted_descending': L_lensort_desc,
    },
    'verdict_primary': 'PASS' if pass_primary else ('NULL' if not mw5_broken else 'INSTRUMENT-BROKEN'),
    'replication_verdict': overall,
    'cross_finding_note': (
        'If replication is FULL, combine with H-NEW-111 for CONFIRMED via cross-finding entry. '
        'If replication fails, H-NEW-111 remains PASS-DIRECTED (no downgrade); signal is root-feature-specific.'
    ),
    'example_path_2opt_first20': opt_path_best[:20],
    'example_path_noldeke_first20': noldeke_order_list[:20],
    'D_matrix_upper_triangular': D_upper,
}

summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote summary JSON: {OUT_JSON}", file=sys.stderr)

# Final stderr summary
print("\n" + "=" * 72, file=sys.stderr)
print(f"PRIMARY: L_mushaf = {L_mushaf:.4f}", file=sys.stderr)
print(f"         null: mean={null_mean:.4f}, min={null_L.min():.4f}, q05={null_quantiles['q05']:.4f}", file=sys.stderr)
print(f"         z = {z_mushaf:.3f}", file=sys.stderr)
print(f"         p = {p_primary:.6f}   (α_bon = 0.0167)", file=sys.stderr)
print(f"         verdict: {'PASS' if pass_primary else 'NULL'}", file=sys.stderr)
print(f"SECONDARY A: L_mushaf / L_2opt = {ratio_mushaf_opt:.4f}  ({sa_interp})", file=sys.stderr)
print(f"             parent (roots) ratio = 1.107", file=sys.stderr)
print(f"SECONDARY B: L_nold = {L_nold:.4f}, p_1sided = {p_nold_lower:.6f}", file=sys.stderr)
print(f"             Δ = L_mushaf - L_nold = {sign_mushaf_minus_nold:+.4f}", file=sys.stderr)
print(f"             replicates reversal: {replicates_reversal}", file=sys.stderr)
print(f"MW-5: pos-ctrl p = {p_pos:.6f}   {'BROKEN' if mw5_broken else 'PASS'}", file=sys.stderr)
print(f"REPLICATION VERDICT: {overall}", file=sys.stderr)
print("=" * 72, file=sys.stderr)
