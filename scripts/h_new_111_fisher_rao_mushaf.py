#!/usr/bin/env python3
"""H-NEW-111 — Fisher-Rao information-geodesic test of mushaf order.

Pre-registered tests (Bonferroni k=3, α_bon=0.0167):
  PRIMARY   — L_mushaf < L_random at permutation p<0.0167 (1-sided lower-tail)
  SECONDARY A — L_mushaf / L_2opt ratio (descriptive; <2.0 = "geodesic-like")
  SECONDARY B — L_nold vs L_mushaf under same null (2-sided exploratory)

MW-1: length control via L1-normalization of per-surah root distributions.
MW-5: greedy-NN-from-surah-1 synthetic ordering serves as positive control.

Pre-reg SHA-256 emitted to stderr.
Seed 20260417.
"""
import csv
import hashlib
import json
import math
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
PERMS = 10000

# Locked parameters (see pre-reg)
K_TOP = 500
DIRICHLET_ALPHA = 0.5

# Paths
QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'

# Pre-reg hash (tamper-evidence)
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"K_TOP = {K_TOP}", file=sys.stderr)
print(f"DIRICHLET_ALPHA = {DIRICHLET_ALPHA}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Parse QAC: per-surah STEM root tokens
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_surah_roots = defaultdict(list)  # sid -> list of root strings
global_root_counts = Counter()

with open(QAC_FILE, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        sid = int(m.group(1))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        root = rm.group(1)
        per_surah_roots[sid].append(root)
        global_root_counts[root] += 1

n_surahs = len(per_surah_roots)
total_tokens = sum(len(v) for v in per_surah_roots.values())
print(f"surahs with ≥1 root token: {n_surahs}", file=sys.stderr)
print(f"total STEM root tokens: {total_tokens}", file=sys.stderr)
print(f"global distinct roots: {len(global_root_counts)}", file=sys.stderr)

assert n_surahs == 114, f"Expected 114 surahs, got {n_surahs}"

# ---------------------------------------------------------------------------
# 2. Select top-K roots (locked K=500)
# ---------------------------------------------------------------------------
top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {r: i for i, r in enumerate(top_roots)}
print(f"top-K roots selected: {len(top_roots)}", file=sys.stderr)
print(f"  top-5: {top_roots[:5]}", file=sys.stderr)
print(f"  cumulative coverage: {sum(global_root_counts[r] for r in top_roots) / total_tokens:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 3. Build per-surah count vectors + Dirichlet smooth + L1-normalize
# ---------------------------------------------------------------------------
# shape: 114 rows × K columns; rows indexed 1..114
counts = [[0.0] * K_TOP for _ in range(115)]  # 1-indexed, row 0 unused
for sid in range(1, 115):
    roots = per_surah_roots.get(sid, [])
    for r in roots:
        idx = top_root_index.get(r)
        if idx is not None:
            counts[sid][idx] += 1.0

# Track fraction of tokens in top-K per surah (sanity/coverage)
per_surah_topk_coverage = {}
for sid in range(1, 115):
    tot = len(per_surah_roots.get(sid, []))
    in_topk = int(sum(counts[sid]))
    per_surah_topk_coverage[sid] = in_topk / tot if tot > 0 else 0.0

# Dirichlet smoothing α=0.5 on every cell, then L1 normalize
prob = [[0.0] * K_TOP for _ in range(115)]
for sid in range(1, 115):
    row = counts[sid]
    smoothed = [c + DIRICHLET_ALPHA for c in row]
    s = sum(smoothed)
    if s == 0:
        raise RuntimeError(f"Zero sum after smoothing at surah {sid}")
    prob[sid] = [v / s for v in smoothed]
    # sanity
    assert abs(sum(prob[sid]) - 1.0) < 1e-9

# Precompute sqrt-probability vectors (for Bhattacharyya)
sqrt_prob = [[math.sqrt(p) for p in prob[sid]] for sid in range(115)]

# ---------------------------------------------------------------------------
# 4. Fisher-Rao distance matrix D[i,j] = 2·arccos(Σ sqrt(p_i*p_j))
# ---------------------------------------------------------------------------
def fr_distance(i, j):
    if i == j:
        return 0.0
    bc = 0.0
    si = sqrt_prob[i]
    sj = sqrt_prob[j]
    for k in range(K_TOP):
        bc += si[k] * sj[k]
    # numerical clamp
    if bc > 1.0:
        bc = 1.0
    elif bc < -1.0:
        bc = -1.0
    return 2.0 * math.acos(bc)

print("\nBuilding 114×114 Fisher-Rao distance matrix...", file=sys.stderr)
D = [[0.0] * 115 for _ in range(115)]  # 1-indexed
for i in range(1, 115):
    for j in range(i + 1, 115):
        d = fr_distance(i, j)
        D[i][j] = d
        D[j][i] = d
    if i % 20 == 0:
        print(f"  row {i}/114", file=sys.stderr)

# Quick sanity stats
all_d = [D[i][j] for i in range(1, 115) for j in range(i + 1, 115)]
print(f"  D range: [{min(all_d):.4f}, {max(all_d):.4f}]", file=sys.stderr)
print(f"  D mean: {statistics.mean(all_d):.4f}, median: {statistics.median(all_d):.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 5. Path-length helper
# ---------------------------------------------------------------------------
def path_length(order):
    """order: list of surah IDs (1..114). Returns Σ D[order[i], order[i+1]]."""
    L = 0.0
    for i in range(len(order) - 1):
        L += D[order[i]][order[i + 1]]
    return L

# Mushaf = 1..114
mushaf_order = list(range(1, 115))
L_mushaf = path_length(mushaf_order)
print(f"\nL_mushaf = {L_mushaf:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. Null: 10,000 uniform random permutations
# ---------------------------------------------------------------------------
print(f"\nNull: {PERMS} random permutations...", file=sys.stderr)
rng = random.Random(SEED)
null_L = []
for p in range(PERMS):
    perm = mushaf_order[:]
    rng.shuffle(perm)
    null_L.append(path_length(perm))
    if (p + 1) % 2000 == 0:
        print(f"  perm {p+1}/{PERMS}", file=sys.stderr)

null_L_sorted = sorted(null_L)
n_le_mushaf = sum(1 for L in null_L if L <= L_mushaf)
p_primary = (n_le_mushaf + 1) / (PERMS + 1)
print(f"  null L mean={statistics.mean(null_L):.4f} sd={statistics.stdev(null_L):.4f}", file=sys.stderr)
print(f"  null L min={min(null_L):.4f} max={max(null_L):.4f}", file=sys.stderr)
print(f"  #{{L_perm ≤ L_mushaf}} = {n_le_mushaf}", file=sys.stderr)
print(f"  p_primary (1-sided lower) = {p_primary:.6f}", file=sys.stderr)

def q(sorted_list, frac):
    n = len(sorted_list)
    idx = max(0, min(n - 1, int(math.floor(frac * n))))
    return sorted_list[idx]

null_quantiles = {
    'min': null_L_sorted[0],
    'q001': q(null_L_sorted, 0.001),
    'q01': q(null_L_sorted, 0.01),
    'q025': q(null_L_sorted, 0.025),
    'q05': q(null_L_sorted, 0.05),
    'q25': q(null_L_sorted, 0.25),
    'q50': q(null_L_sorted, 0.50),
    'q75': q(null_L_sorted, 0.75),
    'q95': q(null_L_sorted, 0.95),
    'max': null_L_sorted[-1],
    'mean': statistics.mean(null_L),
    'sd': statistics.stdev(null_L),
}

# z-score vs null
z_mushaf = (L_mushaf - null_quantiles['mean']) / null_quantiles['sd']
print(f"  z(L_mushaf) = {z_mushaf:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. Secondary A — approximate TSP: greedy NN from each start + 2-opt on best
# ---------------------------------------------------------------------------
print("\nSecondary A: greedy-NN + 2-opt TSP approximation...", file=sys.stderr)

def greedy_nn(start):
    unvisited = set(range(1, 115))
    unvisited.remove(start)
    path = [start]
    cur = start
    while unvisited:
        nxt = min(unvisited, key=lambda v: D[cur][v])
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

# 2-opt local improvement on best
def two_opt(path, max_passes=50):
    """Standard 2-opt for open path."""
    path = path[:]
    n = len(path)
    improved = True
    passes = 0
    while improved and passes < max_passes:
        improved = False
        passes += 1
        best_delta = 0.0
        best_ij = None
        for i in range(0, n - 2):
            a = path[i]
            b = path[i + 1]
            for j in range(i + 2, n):
                c = path[j]
                d = path[j + 1] if j + 1 < n else None
                # old edges: (a,b), (c,d)   (if d None, only (a,b))
                # new edges after reversing path[i+1..j]: (a,c), (b,d)
                if d is None:
                    delta = D[a][c] - D[a][b]
                else:
                    delta = (D[a][c] + D[b][d]) - (D[a][b] + D[c][d])
                if delta < best_delta - 1e-12:
                    best_delta = delta
                    best_ij = (i, j)
        if best_ij is not None:
            i, j = best_ij
            path[i + 1:j + 1] = list(reversed(path[i + 1:j + 1]))
            improved = True
    return path, passes

opt_path, n_passes = two_opt(best_path)
L_2opt = path_length(opt_path)
print(f"  2-opt: L={L_2opt:.4f} ({n_passes} passes)", file=sys.stderr)

# Also do 2-opt on all 114 greedy starts (cheap, 114 × small) to tighten bound
L_2opt_best = L_2opt
opt_path_best = opt_path[:]
print("  running 2-opt on all 114 greedy starts for a tighter upper bound...", file=sys.stderr)
for L_g, start, p in greedy_paths:
    if L_g > L_2opt_best * 1.5:
        # skip paths far from best; 2-opt can't rescue them enough
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
# 8. Secondary B — Nöldeke chronological order
# ---------------------------------------------------------------------------
print("\nSecondary B: Nöldeke chronological path...", file=sys.stderr)
noldeke_mushaf_to_noldeke = {}  # mushaf_sid -> noldeke_order
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        msid = int(row['mushaf_order'])
        nol = int(row['noldeke_order'])
        noldeke_mushaf_to_noldeke[msid] = nol

# Sanity: all 114
assert len(noldeke_mushaf_to_noldeke) == 114
# Build noldeke order: list of mushaf sids sorted by noldeke_order
noldeke_order_list = sorted(range(1, 115), key=lambda sid: noldeke_mushaf_to_noldeke[sid])
L_nold = path_length(noldeke_order_list)
print(f"  L_nold = {L_nold:.4f}", file=sys.stderr)

n_le_nold = sum(1 for L in null_L if L <= L_nold)
n_ge_nold = sum(1 for L in null_L if L >= L_nold)
p_nold_lower = (n_le_nold + 1) / (PERMS + 1)
p_nold_upper = (n_ge_nold + 1) / (PERMS + 1)
p_nold_two_sided = 2.0 * min(p_nold_lower, p_nold_upper)
if p_nold_two_sided > 1.0:
    p_nold_two_sided = 1.0
print(f"  p_nold 1-sided lower = {p_nold_lower:.6f}", file=sys.stderr)
print(f"  p_nold 2-sided = {p_nold_two_sided:.6f}", file=sys.stderr)
print(f"  sign: L_mushaf ({L_mushaf:.4f}) - L_nold ({L_nold:.4f}) = {L_mushaf - L_nold:+.4f}", file=sys.stderr)
if L_mushaf < L_nold:
    print("  ==> mushaf is SHORTER (more coherent) than chronology", file=sys.stderr)
else:
    print("  ==> chronology is SHORTER (more coherent) than mushaf", file=sys.stderr)

# Revelation order (Tanzil) path: different from Nöldeke in some rows
tanzil_rev_order_list = sorted(range(1, 115),
                               key=lambda sid: next(
                                   r for r in _rev_rows if int(r['mushaf_order']) == sid
                               ) if False else None) if False else None  # placeholder replaced below

# Actually just load once properly:
_rev_rows = []
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        _rev_rows.append(row)
mushaf_to_tanzil = {int(r['mushaf_order']): int(r['revelation_order']) for r in _rev_rows}
tanzil_order_list = sorted(range(1, 115), key=lambda sid: mushaf_to_tanzil[sid])
L_tanzil = path_length(tanzil_order_list)
n_le_tanzil = sum(1 for L in null_L if L <= L_tanzil)
print(f"  L_tanzil(Egyptian-Std revelation) = {L_tanzil:.4f} (1-sided lower p = {(n_le_tanzil+1)/(PERMS+1):.6f})", file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. MW-5 positive control: greedy-NN from surah 1 should crush the null
# ---------------------------------------------------------------------------
print("\nMW-5 positive control: greedy-NN from surah 1...", file=sys.stderr)
pos_ctrl_path = greedy_nn(1)
L_pos = path_length(pos_ctrl_path)
n_le_pos = sum(1 for L in null_L if L <= L_pos)
p_pos = (n_le_pos + 1) / (PERMS + 1)
print(f"  L_positive_control = {L_pos:.4f}  (p = {p_pos:.6f})", file=sys.stderr)
mw5_broken = p_pos >= 0.001
if mw5_broken:
    print("  !! MW-5 POSITIVE CONTROL FAILED — null is BROKEN !!", file=sys.stderr)
else:
    print("  MW-5 positive control PASSES (p < 0.001)", file=sys.stderr)

# ---------------------------------------------------------------------------
# 10. Bonus: length-sorted permutation (ascending by n_verses) — sanity anchor
# ---------------------------------------------------------------------------
surah_nverses = {}
quran = json.loads(QURAN_JSON.read_text())
for s in quran:
    surah_nverses[s['id']] = len(s['verses'])
len_sorted = sorted(range(1, 115), key=lambda sid: surah_nverses[sid])
L_lensort = path_length(len_sorted)
len_sorted_desc = sorted(range(1, 115), key=lambda sid: -surah_nverses[sid])
L_lensort_desc = path_length(len_sorted_desc)

# ---------------------------------------------------------------------------
# 11. Write JSON
# ---------------------------------------------------------------------------
def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o

# Flatten D to upper-triangular list for JSON (saves space vs full matrix)
D_upper = []
for i in range(1, 115):
    for j in range(i + 1, 115):
        D_upper.append([i, j, D[i][j]])

summary = {
    'finding_id': 'h-new-111',
    'title': 'Fisher-Rao information-geodesic test of mushaf order',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'rules_tuple': '(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)',
    'locked_params': {
        'K_top_roots': K_TOP,
        'dirichlet_alpha': DIRICHLET_ALPHA,
        'permutations': PERMS,
        'distance': 'Fisher-Rao angular = 2·arccos(Σ sqrt(p_i·p_j))',
        'length_control': 'L1-normalized probability vectors (MW-1)',
    },
    'corpus_stats': {
        'n_surahs': n_surahs,
        'total_stem_root_tokens': total_tokens,
        'global_distinct_roots': len(global_root_counts),
        'top_K_coverage_fraction': sum(global_root_counts[r] for r in top_roots) / total_tokens,
    },
    'per_surah_topk_coverage': {str(k): v for k, v in sorted(per_surah_topk_coverage.items())},
    'distance_matrix_stats': {
        'n_pairs': len(all_d),
        'min': min(all_d),
        'max': max(all_d),
        'mean': statistics.mean(all_d),
        'median': statistics.median(all_d),
    },
    'primary': {
        'L_mushaf': L_mushaf,
        'null_quantiles': null_quantiles,
        'z_score': z_mushaf,
        'n_perms_le_mushaf': n_le_mushaf,
        'p_primary_one_sided_lower': p_primary,
        'alpha_bon': 0.0167,
        'pass_primary': p_primary < 0.0167,
    },
    'secondary_A': {
        'L_greedy_best': L_greedy_best,
        'L_2opt_best': L_2opt_best,
        'best_2opt_start_or_path_first': opt_path_best[0],
        'ratio_mushaf_over_2opt': ratio_mushaf_opt,
        'interpretation': (
            'near-optimal (<1.2)' if ratio_mushaf_opt < 1.2
            else 'geodesic-like (<2.0)' if ratio_mushaf_opt < 2.0
            else 'NOT geodesic-like (≥2.0)'
        ),
    },
    'secondary_B': {
        'L_noldeke': L_nold,
        'L_tanzil_egyptian_std': L_tanzil,
        'p_nold_one_sided_lower': p_nold_lower,
        'p_nold_two_sided': p_nold_two_sided,
        'delta_mushaf_minus_nold': L_mushaf - L_nold,
        'sign_interpretation': (
            'mushaf SHORTER than chronology' if L_mushaf < L_nold
            else 'chronology SHORTER than mushaf'
        ),
        'p_tanzil_one_sided_lower': (n_le_tanzil + 1) / (PERMS + 1),
    },
    'mw5_positive_control': {
        'method': 'greedy-NN from surah 1',
        'L': L_pos,
        'p_one_sided_lower': p_pos,
        'threshold': 0.001,
        'pass': not mw5_broken,
    },
    'sanity_anchors': {
        'L_length_sorted_ascending': L_lensort,
        'L_length_sorted_descending': L_lensort_desc,
    },
    'verdict_primary': 'PASS' if (p_primary < 0.0167 and not mw5_broken) else ('NULL' if not mw5_broken else 'INSTRUMENT-BROKEN'),
    'verdict_ceiling': 'PASS (not CONFIRMED; requires independent replication on distinct feature set)',
    'example_path_2opt_first20': opt_path_best[:20],
    'example_path_noldeke_first20': noldeke_order_list[:20],
    'D_matrix_upper_triangular': D_upper,
}

summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote summary JSON: {OUT_JSON}", file=sys.stderr)

# Final stdout summary
print("\n" + "=" * 70, file=sys.stderr)
print(f"PRIMARY: L_mushaf = {L_mushaf:.4f}", file=sys.stderr)
print(f"         null: mean={null_quantiles['mean']:.4f}, min={null_quantiles['min']:.4f}, q05={null_quantiles['q05']:.4f}", file=sys.stderr)
print(f"         z = {z_mushaf:.3f}", file=sys.stderr)
print(f"         p = {p_primary:.6f}   (α_bon = 0.0167)", file=sys.stderr)
print(f"         verdict: {'PASS' if p_primary < 0.0167 else 'NULL'}", file=sys.stderr)
print(f"SECONDARY A: L_mushaf / L_2opt = {ratio_mushaf_opt:.4f}", file=sys.stderr)
print(f"SECONDARY B: L_nold = {L_nold:.4f}, p_2sided = {p_nold_two_sided:.6f}", file=sys.stderr)
print(f"             sign: {'mushaf SHORTER' if L_mushaf < L_nold else 'chronology SHORTER'}", file=sys.stderr)
print(f"MW-5: pos-ctrl p = {p_pos:.6f}   {'BROKEN' if mw5_broken else 'PASS'}", file=sys.stderr)
print("=" * 70, file=sys.stderr)
