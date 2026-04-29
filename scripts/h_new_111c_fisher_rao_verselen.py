#!/usr/bin/env python3
"""H-NEW-111c — Fisher-Rao on verse-length histograms (2nd replication of H-NEW-111).

Pre-registered tests (Bonferroni k=3, α_bon=0.0167):
  PRIMARY     — L_mushaf < L_random at permutation p<0.0167 (1-sided lower)
  SECONDARY A — L_mushaf / L_2opt ratio (<1.2 = "near-optimal")
  SECONDARY B — L_nold/L_tanzil vs L_mushaf (2-sided p; sign)

Bin edges LOCKED BEFORE RUN: [1, 5, 10, 15, 25, 40, 60, 100, inf] — 8 bins.

MW-1 (note): per-surah L1-normalization removes TOTAL verse count, but we
deliberately do not residualize the verse-length signal itself — that IS
our feature. See pre-reg garden-of-forking-paths for the honest caveat that
the mushaf's known long-to-short mufaṣṣal ordering makes this replication
LESS orthogonal to length than char-4-grams (h-new-111b).

MW-5: greedy-NN-from-surah-1 positive control on the same distance matrix.

Seed 20260417.
"""
import csv
import hashlib
import json
import math
import random
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
PERMS = 10000

# Locked bin edges (SEE PRE-REG)
BIN_EDGES = [1, 5, 10, 15, 25, 40, 60, 100, math.inf]  # 8 bins
N_BINS = len(BIN_EDGES) - 1
DIRICHLET_ALPHA = 0.5

QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-111c-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111c.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"BIN_EDGES = {BIN_EDGES}", file=sys.stderr)
print(f"N_BINS = {N_BINS}", file=sys.stderr)
print(f"DIRICHLET_ALPHA = {DIRICHLET_ALPHA}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)


def bin_index(length):
    """Return 0-based bin index for a given verse token count."""
    for i in range(N_BINS):
        lo = BIN_EDGES[i]
        hi = BIN_EDGES[i + 1]
        if lo <= length < hi:
            return i
    # if length < lowest bin (shouldn't happen — lowest is 1)
    return 0 if length < BIN_EDGES[0] else N_BINS - 1


# ---------------------------------------------------------------------------
# 1. Load Quran + per-surah verse-length vectors
# ---------------------------------------------------------------------------
quran = json.loads(QURAN_JSON.read_text())
assert len(quran) == 114, f"expected 114 surahs, got {len(quran)}"

per_surah_nverses = {}
per_surah_counts = {}  # sid -> [c1..c8]
total_verses = 0
all_lengths = []

for s in quran:
    sid = s['id']
    verses = s['verses']
    per_surah_nverses[sid] = len(verses)
    total_verses += len(verses)
    counts = [0] * N_BINS
    for v in verses:
        toklen = len(v['text'].split())
        all_lengths.append(toklen)
        counts[bin_index(toklen)] += 1
    per_surah_counts[sid] = counts

print(f"total verses: {total_verses}", file=sys.stderr)
print(f"verse-length stats: min={min(all_lengths)}, max={max(all_lengths)},"
      f" mean={statistics.mean(all_lengths):.2f}, median={statistics.median(all_lengths):.1f}",
      file=sys.stderr)

# Global bin occupancy (sanity)
global_counts = [0] * N_BINS
for sid in range(1, 115):
    for b in range(N_BINS):
        global_counts[b] += per_surah_counts[sid][b]
print("global bin occupancy:", file=sys.stderr)
for b in range(N_BINS):
    lo, hi = BIN_EDGES[b], BIN_EDGES[b + 1]
    frac = global_counts[b] / total_verses
    print(f"  bin {b+1} [{lo}, {hi}): {global_counts[b]} verses ({frac:.3f})",
          file=sys.stderr)

assert total_verses == 6236, f"expected 6236 verses, got {total_verses}"

# ---------------------------------------------------------------------------
# 2. Smooth + L1-normalize → per-surah probability vectors
# ---------------------------------------------------------------------------
prob = [None] * 115  # 1-indexed
for sid in range(1, 115):
    smoothed = [c + DIRICHLET_ALPHA for c in per_surah_counts[sid]]
    s = sum(smoothed)
    prob[sid] = [v / s for v in smoothed]
    assert abs(sum(prob[sid]) - 1.0) < 1e-9

sqrt_prob = [None] + [[math.sqrt(v) for v in prob[sid]] for sid in range(1, 115)]

# ---------------------------------------------------------------------------
# 3. Fisher-Rao distance matrix
# ---------------------------------------------------------------------------
def fr_distance(i, j):
    if i == j:
        return 0.0
    si = sqrt_prob[i]
    sj = sqrt_prob[j]
    bc = 0.0
    for k in range(N_BINS):
        bc += si[k] * sj[k]
    if bc > 1.0:
        bc = 1.0
    elif bc < -1.0:
        bc = -1.0
    return 2.0 * math.acos(bc)


print("\nBuilding 114×114 Fisher-Rao distance matrix (8-dim simplex)...", file=sys.stderr)
D = [[0.0] * 115 for _ in range(115)]
for i in range(1, 115):
    for j in range(i + 1, 115):
        d = fr_distance(i, j)
        D[i][j] = d
        D[j][i] = d

all_d = [D[i][j] for i in range(1, 115) for j in range(i + 1, 115)]
print(f"  D range: [{min(all_d):.4f}, {max(all_d):.4f}]", file=sys.stderr)
print(f"  D mean: {statistics.mean(all_d):.4f}, median: {statistics.median(all_d):.4f}",
      file=sys.stderr)

# ---------------------------------------------------------------------------
# 4. Path length helper
# ---------------------------------------------------------------------------
def path_length(order):
    L = 0.0
    for i in range(len(order) - 1):
        L += D[order[i]][order[i + 1]]
    return L


mushaf_order = list(range(1, 115))
L_mushaf = path_length(mushaf_order)
print(f"\nL_mushaf = {L_mushaf:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 5. Null: 10,000 uniform random permutations
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
null_mean = statistics.mean(null_L)
null_sd = statistics.stdev(null_L)
z_mushaf = (L_mushaf - null_mean) / null_sd
print(f"  null mean={null_mean:.4f}, sd={null_sd:.4f}", file=sys.stderr)
print(f"  null min={min(null_L):.4f}, max={max(null_L):.4f}", file=sys.stderr)
print(f"  #{{L_perm ≤ L_mushaf}} = {n_le_mushaf}", file=sys.stderr)
print(f"  z = {z_mushaf:.4f}", file=sys.stderr)
print(f"  p_primary = {p_primary:.6f}", file=sys.stderr)


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
    'mean': null_mean,
    'sd': null_sd,
}

# ---------------------------------------------------------------------------
# 6. Secondary A — greedy-NN + 2-opt TSP upper bound
# ---------------------------------------------------------------------------
print("\nSecondary A: greedy-NN + 2-opt...", file=sys.stderr)

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


def two_opt(path, max_passes=50):
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
print(f"  2-opt on best: L={L_2opt:.4f} ({n_passes} passes)", file=sys.stderr)

L_2opt_best = L_2opt
opt_path_best = opt_path[:]
print("  2-opt on all 114 greedy starts for tighter bound...", file=sys.stderr)
for L_g, start, p in greedy_paths:
    if L_g > L_2opt_best * 1.5:
        continue
    p2, _ = two_opt(p)
    Lp = path_length(p2)
    if Lp < L_2opt_best:
        L_2opt_best = Lp
        opt_path_best = p2[:]
        print(f"    improved: start={start}, L={Lp:.4f}", file=sys.stderr)

print(f"  final L_2opt_best = {L_2opt_best:.4f}", file=sys.stderr)
ratio_mushaf_opt = L_mushaf / L_2opt_best
print(f"  L_mushaf / L_2opt_best = {ratio_mushaf_opt:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. Secondary B — Nöldeke + Tanzil
# ---------------------------------------------------------------------------
print("\nSecondary B: Nöldeke / Tanzil chronological paths...", file=sys.stderr)
rev_rows = []
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rev_rows.append(row)
mushaf_to_nold = {int(r['mushaf_order']): int(r['noldeke_order']) for r in rev_rows}
mushaf_to_tanzil = {int(r['mushaf_order']): int(r['revelation_order']) for r in rev_rows}
assert len(mushaf_to_nold) == 114 and len(mushaf_to_tanzil) == 114

noldeke_order_list = sorted(range(1, 115), key=lambda sid: mushaf_to_nold[sid])
tanzil_order_list = sorted(range(1, 115), key=lambda sid: mushaf_to_tanzil[sid])
L_nold = path_length(noldeke_order_list)
L_tanzil = path_length(tanzil_order_list)

n_le_nold = sum(1 for L in null_L if L <= L_nold)
n_ge_nold = sum(1 for L in null_L if L >= L_nold)
p_nold_lower = (n_le_nold + 1) / (PERMS + 1)
p_nold_upper = (n_ge_nold + 1) / (PERMS + 1)
p_nold_two_sided = min(1.0, 2.0 * min(p_nold_lower, p_nold_upper))
n_le_tanzil = sum(1 for L in null_L if L <= L_tanzil)
p_tanzil_lower = (n_le_tanzil + 1) / (PERMS + 1)

print(f"  L_nold = {L_nold:.4f} (1-sided p={p_nold_lower:.6f}, 2-sided p={p_nold_two_sided:.6f})",
      file=sys.stderr)
print(f"  L_tanzil = {L_tanzil:.4f} (1-sided p={p_tanzil_lower:.6f})", file=sys.stderr)
print(f"  sign: L_mushaf - L_nold = {L_mushaf - L_nold:+.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. MW-5 positive control
# ---------------------------------------------------------------------------
print("\nMW-5 positive control: greedy-NN from surah 1...", file=sys.stderr)
pos_ctrl_path = greedy_nn(1)
L_pos = path_length(pos_ctrl_path)
n_le_pos = sum(1 for L in null_L if L <= L_pos)
p_pos = (n_le_pos + 1) / (PERMS + 1)
mw5_broken = p_pos >= 0.001
print(f"  L_pos = {L_pos:.4f}, p = {p_pos:.6f}", file=sys.stderr)
print(f"  {'BROKEN' if mw5_broken else 'PASS'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. Sanity anchors — length-sorted orderings (critical for honesty)
# ---------------------------------------------------------------------------
# sort by total verses ascending / descending
len_sorted_asc = sorted(range(1, 115), key=lambda sid: per_surah_nverses[sid])
len_sorted_desc = sorted(range(1, 115), key=lambda sid: -per_surah_nverses[sid])
L_lensort_asc = path_length(len_sorted_asc)
L_lensort_desc = path_length(len_sorted_desc)
# sort by mean verse length
mean_vlen = {}
for s in quran:
    sid = s['id']
    tl = [len(v['text'].split()) for v in s['verses']]
    mean_vlen[sid] = sum(tl) / len(tl)
mean_vlen_sorted_asc = sorted(range(1, 115), key=lambda sid: mean_vlen[sid])
mean_vlen_sorted_desc = sorted(range(1, 115), key=lambda sid: -mean_vlen[sid])
L_mvlen_asc = path_length(mean_vlen_sorted_asc)
L_mvlen_desc = path_length(mean_vlen_sorted_desc)

print(f"\nSanity anchors:", file=sys.stderr)
print(f"  L_length_sorted_asc (#verses) = {L_lensort_asc:.4f}", file=sys.stderr)
print(f"  L_length_sorted_desc (#verses) = {L_lensort_desc:.4f}", file=sys.stderr)
print(f"  L_mean-verse-len_asc = {L_mvlen_asc:.4f}", file=sys.stderr)
print(f"  L_mean-verse-len_desc = {L_mvlen_desc:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 10. JSON output
# ---------------------------------------------------------------------------
def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o


D_upper = []
for i in range(1, 115):
    for j in range(i + 1, 115):
        D_upper.append([i, j, D[i][j]])

summary = {
    'finding_id': 'h-new-111c',
    'title': 'Fisher-Rao on verse-length histograms — 2nd replication of H-NEW-111',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'parent_finding': 'h-new-111',
    'parent_replication_lane': 'second orthogonal replication (first is h-new-111b on char-4-grams)',
    'rules_tuple': '(no-tashkeel, whitespace-tokenized verse text, basmala-counted-only-in-surah-1 via text, mushaf order, Hafs-Kufan)',
    'locked_params': {
        'bin_edges': [x if math.isfinite(x) else 'inf' for x in BIN_EDGES],
        'n_bins': N_BINS,
        'dirichlet_alpha': DIRICHLET_ALPHA,
        'permutations': PERMS,
        'distance': 'Fisher-Rao angular = 2·arccos(Σ sqrt(p_i·p_j))',
    },
    'corpus_stats': {
        'n_surahs': 114,
        'total_verses': total_verses,
        'verse_length_min': min(all_lengths),
        'verse_length_max': max(all_lengths),
        'verse_length_mean': statistics.mean(all_lengths),
        'verse_length_median': statistics.median(all_lengths),
    },
    'global_bin_occupancy': {
        f"bin_{b+1}_[{BIN_EDGES[b]},{BIN_EDGES[b+1] if math.isfinite(BIN_EDGES[b+1]) else 'inf'})": global_counts[b]
        for b in range(N_BINS)
    },
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
        'p_tanzil_one_sided_lower': p_tanzil_lower,
        'delta_mushaf_minus_nold': L_mushaf - L_nold,
        'sign_interpretation': (
            'mushaf SHORTER than chronology' if L_mushaf < L_nold
            else 'chronology SHORTER than mushaf'
        ),
    },
    'mw5_positive_control': {
        'method': 'greedy-NN from surah 1',
        'L': L_pos,
        'p_one_sided_lower': p_pos,
        'threshold': 0.001,
        'pass': not mw5_broken,
    },
    'sanity_anchors_length_confound': {
        'L_length_sorted_asc_nverses': L_lensort_asc,
        'L_length_sorted_desc_nverses': L_lensort_desc,
        'L_mean_verselen_sorted_asc': L_mvlen_asc,
        'L_mean_verselen_sorted_desc': L_mvlen_desc,
        'note': (
            'Critical discriminator: if L_mushaf is close to L_length_sorted_desc, '
            'the replication is mechanically confounded by Uthmanic length-sorting. '
            'If L_mushaf is meaningfully below all four length-sorted anchors, the '
            'rhythmic coherence goes beyond pure length-sorting.'
        ),
    },
    'verdict_primary': 'PASS' if (p_primary < 0.0167 and not mw5_broken) else ('NULL' if not mw5_broken else 'INSTRUMENT-BROKEN'),
    'verdict_ceiling': 'PASS-DIRECTED (replication lane of h-new-111; parent promotes to CONFIRMED only if both h-new-111b AND h-new-111c pass)',
    'example_path_2opt_first20': opt_path_best[:20],
    'example_path_noldeke_first20': noldeke_order_list[:20],
    'D_matrix_upper_triangular': D_upper,
}

summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote summary JSON: {OUT_JSON}", file=sys.stderr)

print("\n" + "=" * 70, file=sys.stderr)
print(f"H-NEW-111c — Fisher-Rao on verse-length histograms (8 bins)", file=sys.stderr)
print(f"PRIMARY: L_mushaf = {L_mushaf:.4f}", file=sys.stderr)
print(f"         null mean={null_mean:.4f} sd={null_sd:.4f} min={min(null_L):.4f}", file=sys.stderr)
print(f"         z = {z_mushaf:.3f}", file=sys.stderr)
print(f"         p = {p_primary:.6f}  (α_bon=0.0167)", file=sys.stderr)
print(f"         verdict: {'PASS' if p_primary < 0.0167 else 'NULL'}", file=sys.stderr)
print(f"SECONDARY A: L_mushaf / L_2opt = {ratio_mushaf_opt:.4f}", file=sys.stderr)
print(f"SECONDARY B: L_nold={L_nold:.4f}, L_tanzil={L_tanzil:.4f}, "
      f"p_nold_2-sided={p_nold_two_sided:.6f}", file=sys.stderr)
print(f"             sign: {'mushaf SHORTER' if L_mushaf < L_nold else 'chronology SHORTER'}", file=sys.stderr)
print(f"MW-5: p = {p_pos:.6f}  {'BROKEN' if mw5_broken else 'PASS'}", file=sys.stderr)
print(f"CONFOUND CHECK: L_length_sorted_desc_nverses = {L_lensort_desc:.4f}", file=sys.stderr)
print(f"                L_mean_verselen_sorted_desc = {L_mvlen_desc:.4f}", file=sys.stderr)
print(f"                L_mean_verselen_sorted_asc = {L_mvlen_asc:.4f}", file=sys.stderr)
print("=" * 70, file=sys.stderr)
