#!/usr/bin/env python3
"""H-NEW-205 — Fisher-Rao verse-level M1 geodesic: B7 vs OTHER.

Is the verse-level Fisher-Rao canonical path *more anomalously short*
within the 14 Late-Meccan B7 surahs (per cross-finding-012 modal peak)
than within the remaining ~100 surahs?

Parent: H-NEW-111 (surah-level PASS), H-NEW-127 (verse-level PASS in 5 surahs).
See pre-reg: findings/phase-b-hypotheses/h-new-205-prereg.md

Primary: Bonferroni k=2, α_bon = 0.025.
  Test 1: one-sided MWU on z-scores (H1: B7 < OTHER, more negative)
  Test 2: one-sided MWU on L_canon/L_2opt (H1: B7 < OTHER, closer to 1)

Locked parameters (inherited from H-NEW-111/127):
  K_top_roots = 300
  dirichlet_alpha = 0.5 (Jeffreys)
  distance = Fisher-Rao angular = 2·arccos(Σ sqrt(p_i·p_j))
  PERMS = 10,000
  seed = 20260419 (per task dispatch)

Pre-reg SHA-256 emitted to stderr.
"""
import hashlib
import json
import math
import random
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PERMS = 10000

K_TOP = 300
DIRICHLET_ALPHA = 0.5
ALPHA_BON = 0.025
BON_K = 2
N_FLOOR = 5  # minimum verses for inclusion

# B7 surahs per cross-finding-012 (Nöldeke ranks 86-99)
GROUP_B7 = [2, 3, 6, 7, 8, 13, 35, 46, 47, 57, 61, 62, 64, 98]
GROUP_B7_SET = set(GROUP_B7)

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-205-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-205.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"K_TOP = {K_TOP}", file=sys.stderr)
print(f"ALPHA_BON = {ALPHA_BON} (Bonferroni-{BON_K})", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)
print(f"GROUP_B7 = {GROUP_B7}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Parse QAC
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_verse_roots = defaultdict(list)
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
        vid = int(m.group(2))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        root = rm.group(1)
        per_verse_roots[(sid, vid)].append(root)
        global_root_counts[root] += 1

total_tokens = sum(len(v) for v in per_verse_roots.values())
print(f"total STEM root tokens: {total_tokens}", file=sys.stderr)
print(f"global distinct roots: {len(global_root_counts)}", file=sys.stderr)

top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {r: i for i, r in enumerate(top_roots)}
topk_cov = sum(global_root_counts[r] for r in top_roots) / total_tokens
print(f"top-K={K_TOP} coverage: {topk_cov:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 2. Build per-surah verse probability vectors
# ---------------------------------------------------------------------------
quran_raw = json.loads(QURAN_JSON.read_text())
surah_verse_probs = {}  # sid -> (n_verses × K_TOP) numpy float64 sqrt-prob matrix

for sdata in quran_raw:
    sid = sdata['id']
    verses = sdata['verses']
    n_v = len(verses)
    counts = np.zeros((n_v, K_TOP), dtype=np.float64)
    for i, v in enumerate(verses):
        vid = v['id']
        for r in per_verse_roots.get((sid, vid), []):
            idx = top_root_index.get(r)
            if idx is not None:
                counts[i, idx] += 1.0
    # Dirichlet smooth + L1 normalize
    smoothed = counts + DIRICHLET_ALPHA
    row_sums = smoothed.sum(axis=1, keepdims=True)
    probs = smoothed / row_sums
    sqprobs = np.sqrt(probs)
    surah_verse_probs[sid] = sqprobs

# ---------------------------------------------------------------------------
# 3. Fisher-Rao utilities (numpy)
# ---------------------------------------------------------------------------
def build_distance_matrix(sqprobs):
    # sqprobs: (n, K) float64
    # Bhattacharyya coefficient B[i,j] = sum_k sqprobs[i,k]*sqprobs[j,k]
    B = sqprobs @ sqprobs.T
    B = np.clip(B, -1.0, 1.0)
    D = 2.0 * np.arccos(B)
    # Numerical: diag may be tiny nonzero
    np.fill_diagonal(D, 0.0)
    return D

def path_length(D, order):
    # order: 1-D int array
    return float(D[order[:-1], order[1:]].sum())

def greedy_nn(D, start):
    n = D.shape[0]
    visited = np.zeros(n, dtype=bool)
    visited[start] = True
    path = [start]
    cur = start
    for _ in range(n - 1):
        d_row = D[cur].copy()
        d_row[visited] = np.inf
        nxt = int(np.argmin(d_row))
        path.append(nxt)
        visited[nxt] = True
        cur = nxt
    return np.array(path, dtype=np.int64)

def two_opt(D, path, max_passes=50):
    path = path.copy()
    n = len(path)
    for _pass in range(max_passes):
        improved = False
        best_delta = 0.0
        best_ij = None
        # Vectorized search over i, j
        for i in range(0, n - 2):
            a = path[i]
            b = path[i + 1]
            # j in [i+2, n-1]
            js = np.arange(i + 2, n)
            c = path[js]
            has_d = js + 1 < n
            d_idx = np.where(has_d, np.minimum(js + 1, n - 1), 0)
            d = path[d_idx]
            delta = np.where(
                has_d,
                (D[a, c] + D[b, d]) - (D[a, b] + D[c, d]),
                D[a, c] - D[a, b],
            )
            local_min_pos = int(np.argmin(delta))
            if delta[local_min_pos] < best_delta - 1e-12:
                best_delta = float(delta[local_min_pos])
                best_ij = (i, int(js[local_min_pos]))
        if best_ij is None:
            break
        i, j = best_ij
        path[i + 1:j + 1] = path[i + 1:j + 1][::-1]
        improved = True
    return path

# ---------------------------------------------------------------------------
# 4. Per-surah run
# ---------------------------------------------------------------------------
per_surah = {}
t0 = time.time()
n_done = 0

for sid in range(1, 115):
    sqprobs = surah_verse_probs[sid]
    n = sqprobs.shape[0]
    if n < N_FLOOR:
        per_surah[sid] = {
            'n_verses': n,
            'excluded': True,
            'reason': f'n<{N_FLOOR}',
        }
        continue

    D = build_distance_matrix(sqprobs)
    canon = np.arange(n, dtype=np.int64)
    L_canon = path_length(D, canon)

    # Null via PERMS random permutations
    rng = random.Random(SEED + sid * 1000003)
    # Seed numpy RNG deterministically; but for reproducibility with
    # stdlib random, we use rng.shuffle via python list indexes;
    # better: build np.random.Generator with deterministic seed
    np_seed = (SEED + sid * 1000003) & 0xFFFFFFFF
    nprng = np.random.default_rng(np_seed)
    null_L = np.empty(PERMS, dtype=np.float64)
    # Pre-extract matrix for speed: use flat indexing
    for p_i in range(PERMS):
        perm = nprng.permutation(n)
        null_L[p_i] = D[perm[:-1], perm[1:]].sum()

    null_mean = float(null_L.mean())
    null_sd = float(null_L.std(ddof=1))
    null_min = float(null_L.min())
    null_max = float(null_L.max())
    z = (L_canon - null_mean) / null_sd if null_sd > 0 else 0.0
    n_le = int((null_L <= L_canon).sum())
    p_val = (n_le + 1) / (PERMS + 1)

    # 2-opt from a handful of greedy starts (to estimate optimum)
    # For speed, limit to 10 starts (best greedy + 9 more); refine each.
    n_starts = min(n, 20) if n <= 120 else 8
    greedy_results = []
    # deterministic start sampling
    start_rng = random.Random(np_seed)
    all_starts = list(range(n))
    start_rng.shuffle(all_starts)
    tried = set()
    for st in all_starts[:n_starts]:
        if st in tried:
            continue
        tried.add(st)
        gp = greedy_nn(D, st)
        greedy_results.append((path_length(D, gp), gp))
    greedy_results.sort(key=lambda x: x[0])
    L_greedy_best = greedy_results[0][0]

    L_2opt_best = float('inf')
    for L_g, gp in greedy_results[:min(len(greedy_results), 5)]:
        opt = two_opt(D, gp)
        L_opt = path_length(D, opt)
        if L_opt < L_2opt_best:
            L_2opt_best = L_opt

    ratio = L_canon / L_2opt_best if L_2opt_best > 0 else float('inf')

    per_surah[sid] = {
        'n_verses': n,
        'excluded': False,
        'in_B7': sid in GROUP_B7_SET,
        'L_canon': L_canon,
        'null_mean': null_mean,
        'null_sd': null_sd,
        'null_min': null_min,
        'null_max': null_max,
        'z_score': z,
        'n_perms_le_canon': n_le,
        'p_value_one_sided_lower': p_val,
        'L_greedy_best': L_greedy_best,
        'L_2opt_best': L_2opt_best,
        'ratio_canon_over_2opt': ratio,
    }
    n_done += 1
    if n_done % 10 == 0:
        elapsed = time.time() - t0
        print(f"  [{n_done:3d} surahs done, {elapsed:.1f}s]  Q{sid:3d} n={n:3d} z={z:+.2f} ratio={ratio:.3f}",
              file=sys.stderr)

print(f"\nAll per-surah done in {time.time()-t0:.1f}s", file=sys.stderr)

# ---------------------------------------------------------------------------
# 5. MWU (one-sided) B7 vs OTHER on z-scores and on ratios
# ---------------------------------------------------------------------------
def mwu_one_sided_less(xs, ys, n_boot_perm=100000, seed=20260419):
    """Return (U_stat, n1, n2, p_less, p_greater, hl_shift).
    p_less: H1: xs distributionally less than ys.
    p_greater: H1: xs > ys.
    HL shift: median of x_i - y_j (positive means xs > ys).
    Uses exact rank-based MWU via scipy-style formula, with permutation
    p-value as a secondary check (seeded, deterministic).
    """
    xs = np.asarray(xs, dtype=np.float64)
    ys = np.asarray(ys, dtype=np.float64)
    n1 = len(xs)
    n2 = len(ys)
    # Rank-sum (handles ties by average rank)
    combined = np.concatenate([xs, ys])
    order = np.argsort(combined, kind='mergesort')
    ranks = np.empty_like(combined)
    # Average ranks over ties
    sorted_vals = combined[order]
    # Find tie groups
    i = 0
    while i < len(sorted_vals):
        j = i
        while j + 1 < len(sorted_vals) and sorted_vals[j + 1] == sorted_vals[i]:
            j += 1
        avg_rank = 0.5 * ((i + 1) + (j + 1))
        ranks[order[i:j + 1]] = avg_rank
        i = j + 1
    R1 = ranks[:n1].sum()
    U1 = R1 - n1 * (n1 + 1) / 2.0
    U2 = n1 * n2 - U1
    # Normal approximation with tie correction
    mean_U = n1 * n2 / 2.0
    # tie correction
    _, counts = np.unique(combined, return_counts=True)
    T = sum(t**3 - t for t in counts)
    N = n1 + n2
    var_U = (n1 * n2 / 12.0) * ((N + 1) - T / (N * (N - 1)))
    if var_U > 0:
        # Continuity correction
        z_less = (U1 - mean_U + 0.5) / math.sqrt(var_U)
        z_greater = (U1 - mean_U - 0.5) / math.sqrt(var_U)
        # p_less = P(U1 <= observed under H0); want lower if xs tend < ys
        # But U1 is LARGE when xs > ys; so:
        # H1: xs < ys  -> expect U1 SMALL  -> p = Phi(z_less)
        # H1: xs > ys  -> expect U1 LARGE  -> p = 1-Phi(z_greater)
        from math import erf, sqrt as msqrt
        def phi(z):
            return 0.5 * (1 + erf(z / msqrt(2)))
        p_less = phi(z_less)
        p_greater = 1 - phi(z_greater)
    else:
        p_less = float('nan')
        p_greater = float('nan')

    # Permutation p-value (exact under H0: labels exchangeable), seeded
    pr = np.random.default_rng(seed)
    labels = np.array([1] * n1 + [0] * n2)
    obs_U1 = U1
    perm_U1 = np.empty(n_boot_perm, dtype=np.float64)
    for b in range(n_boot_perm):
        perm_labels = pr.permutation(labels)
        x_perm = combined[perm_labels == 1]
        y_perm = combined[perm_labels == 0]
        # Compute U1 for permuted
        R1p = ranks[perm_labels == 1].sum()
        U1p = R1p - n1 * (n1 + 1) / 2.0
        perm_U1[b] = U1p
    p_less_perm = ((perm_U1 <= obs_U1).sum() + 1) / (n_boot_perm + 1)
    p_greater_perm = ((perm_U1 >= obs_U1).sum() + 1) / (n_boot_perm + 1)

    # Hodges-Lehmann shift
    diffs = xs[:, None] - ys[None, :]
    hl = float(np.median(diffs))

    return {
        'U1': float(U1),
        'U2': float(U2),
        'n1': n1,
        'n2': n2,
        'R1': float(R1),
        'p_less_normal': float(p_less),
        'p_greater_normal': float(p_greater),
        'p_less_permutation': float(p_less_perm),
        'p_greater_permutation': float(p_greater_perm),
        'hl_shift_xs_minus_ys': hl,
        'median_xs': float(np.median(xs)),
        'median_ys': float(np.median(ys)),
        'mean_xs': float(np.mean(xs)),
        'mean_ys': float(np.mean(ys)),
    }

# Assemble groups
included = [sid for sid in range(1, 115)
            if not per_surah[sid].get('excluded', False)]
excluded = [sid for sid in range(1, 115)
            if per_surah[sid].get('excluded', False)]
b7_included = [sid for sid in included if sid in GROUP_B7_SET]
other_included = [sid for sid in included if sid not in GROUP_B7_SET]

z_B7 = [per_surah[sid]['z_score'] for sid in b7_included]
z_OTHER = [per_surah[sid]['z_score'] for sid in other_included]
ratio_B7 = [per_surah[sid]['ratio_canon_over_2opt'] for sid in b7_included]
ratio_OTHER = [per_surah[sid]['ratio_canon_over_2opt'] for sid in other_included]

print(f"\nIncluded: {len(included)} surahs ({len(b7_included)} B7, {len(other_included)} OTHER)",
      file=sys.stderr)
print(f"Excluded (n<{N_FLOOR}): {excluded}", file=sys.stderr)

print(f"\nz-score medians: B7={np.median(z_B7):+.3f}  OTHER={np.median(z_OTHER):+.3f}",
      file=sys.stderr)
print(f"ratio medians:   B7={np.median(ratio_B7):.4f}  OTHER={np.median(ratio_OTHER):.4f}",
      file=sys.stderr)

# Test 1: z-scores, H1 B7 < OTHER (more negative)
print("\n--- Test 1: MWU on z (H1: B7 < OTHER) ---", file=sys.stderr)
test1 = mwu_one_sided_less(z_B7, z_OTHER, n_boot_perm=20000, seed=SEED)
for k, v in test1.items():
    print(f"  {k}: {v}", file=sys.stderr)
test1_pass = test1['p_less_permutation'] < ALPHA_BON

# Test 2: ratios, H1 B7 < OTHER (closer to 1, stronger M1)
print("\n--- Test 2: MWU on ratio (H1: B7 < OTHER) ---", file=sys.stderr)
test2 = mwu_one_sided_less(ratio_B7, ratio_OTHER, n_boot_perm=20000, seed=SEED + 1)
for k, v in test2.items():
    print(f"  {k}: {v}", file=sys.stderr)
test2_pass = test2['p_less_permutation'] < ALPHA_BON

# ---------------------------------------------------------------------------
# 6. Family verdict
# ---------------------------------------------------------------------------
if test1_pass and test2_pass:
    verdict = 'CONFIRMED'
elif test1_pass and not test2_pass:
    verdict = 'PARTIAL_Z_ONLY'
elif test2_pass and not test1_pass:
    verdict = 'PARTIAL_RATIO_ONLY'
else:
    verdict = 'NULL'
print(f"\n=== H-NEW-205 VERDICT: {verdict} ===", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. Write summary
# ---------------------------------------------------------------------------
def round_floats(o, n=6):
    if isinstance(o, float):
        if math.isnan(o) or math.isinf(o):
            return str(o)
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o

summary = {
    'finding_id': 'h-new-205',
    'title': 'Fisher-Rao M1 geodesic at VERSE level: B7 (Late-Meccan) vs OTHER',
    'parent_findings': ['h-new-111', 'h-new-127', 'cross-finding-012', 'cross-finding-016', 'h-new-141'],
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'rules_tuple': '(no-tashkeel, QAC-STEM root tokens, QAC v0.4, mushaf verse order, Hafs-Kūfan, 114 surahs)',
    'locked_params': {
        'K_top_roots': K_TOP,
        'dirichlet_alpha': DIRICHLET_ALPHA,
        'permutations': PERMS,
        'distance': 'Fisher-Rao angular = 2·arccos(Σ sqrt(p_i·p_j))',
        'bonferroni_k': BON_K,
        'alpha_bon': ALPHA_BON,
        'n_floor': N_FLOOR,
        'group_b7': GROUP_B7,
    },
    'corpus_stats': {
        'total_stem_root_tokens': total_tokens,
        'global_distinct_roots': len(global_root_counts),
        'top_K_coverage_fraction': topk_cov,
        'n_surahs_included': len(included),
        'n_surahs_excluded_short': len(excluded),
        'excluded_surahs': excluded,
        'n_b7_included': len(b7_included),
        'n_other_included': len(other_included),
    },
    'per_surah': {str(sid): per_surah[sid] for sid in range(1, 115)},
    'group_summary': {
        'z_B7_median': float(np.median(z_B7)),
        'z_B7_mean': float(np.mean(z_B7)),
        'z_B7_min': float(np.min(z_B7)),
        'z_B7_max': float(np.max(z_B7)),
        'z_OTHER_median': float(np.median(z_OTHER)),
        'z_OTHER_mean': float(np.mean(z_OTHER)),
        'z_OTHER_min': float(np.min(z_OTHER)),
        'z_OTHER_max': float(np.max(z_OTHER)),
        'ratio_B7_median': float(np.median(ratio_B7)),
        'ratio_B7_mean': float(np.mean(ratio_B7)),
        'ratio_OTHER_median': float(np.median(ratio_OTHER)),
        'ratio_OTHER_mean': float(np.mean(ratio_OTHER)),
    },
    'test_1_mwu_z_one_sided_less': test1,
    'test_1_pass_bon2': test1_pass,
    'test_2_mwu_ratio_one_sided_less': test2,
    'test_2_pass_bon2': test2_pass,
    'verdict': verdict,
}
summary = round_floats(summary)
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote {OUT_JSON}", file=sys.stderr)

# Console summary
print("\n" + "=" * 70, file=sys.stderr)
print(f"H-NEW-205 verse-level M1 geodesic: B7 vs OTHER", file=sys.stderr)
print(f"  n_B7 = {len(b7_included)}  n_OTHER = {len(other_included)}  (excluded short: {len(excluded)})",
      file=sys.stderr)
print(f"  median z:     B7 = {np.median(z_B7):+.3f}    OTHER = {np.median(z_OTHER):+.3f}", file=sys.stderr)
print(f"  median ratio: B7 = {np.median(ratio_B7):.4f}   OTHER = {np.median(ratio_OTHER):.4f}", file=sys.stderr)
print(f"  Test 1 (MWU z one-sided less): p_perm = {test1['p_less_permutation']:.4f}  "
      f"{'PASS' if test1_pass else 'FAIL'} (α_bon={ALPHA_BON})", file=sys.stderr)
print(f"  Test 2 (MWU ratio one-sided less): p_perm = {test2['p_less_permutation']:.4f}  "
      f"{'PASS' if test2_pass else 'FAIL'} (α_bon={ALPHA_BON})", file=sys.stderr)
print(f"  VERDICT: {verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)
