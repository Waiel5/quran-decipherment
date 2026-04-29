#!/usr/bin/env python3
"""H-NEW-212 — Alternative chronologies vs Fisher-Rao path length.

Pre-registered tests (Bonferroni k=3, α_bon=0.0167):
  PRIMARY-1 — L_egyptian < L_random (1-sided lower, perm p<0.0167)
  PRIMARY-2 — L_bell     < L_random (1-sided lower, perm p<0.0167)
  PRIMARY-3 — L_blachere < L_random (1-sided lower, perm p<0.0167)

Nöldeke and mushaf reported as descriptive references (not in family).

Reuses distance matrix D from h-new-111.json (Fisher-Rao angular distance
on QAC STEM root top-500 Dirichlet-smoothed L1-normalized probability
vectors). Fresh seed 20260419 (independent of H-NEW-111's 20260417).

Pre-reg SHA-256 emitted to stderr.
Seed 20260419.
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
SEED = 20260419
PERMS = 10000
BONFERRONI_K = 3
ALPHA_BON = 0.05 / BONFERRONI_K  # = 0.01667

PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-212-alt-chronology-fisher-rao-prereg.md'
H111_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-212.json'

# -----------------------------------------------------------------------------
# Pre-reg tamper-evidence
# -----------------------------------------------------------------------------
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
h111_sha = hashlib.sha256(H111_JSON.read_bytes()).hexdigest()
print(f"prereg SHA-256:  {prereg_sha}", file=sys.stderr)
print(f"h-new-111 JSON SHA-256 (D matrix source): {h111_sha}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)
print(f"BONFERRONI_K = {BONFERRONI_K}, α_bon = {ALPHA_BON:.5f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 1. Load D matrix from h-new-111.json
# -----------------------------------------------------------------------------
print("\nLoading D matrix from h-new-111.json ...", file=sys.stderr)
h111 = json.loads(H111_JSON.read_text())
D_up = h111['D_matrix_upper_triangular']
D = [[0.0] * 115 for _ in range(115)]
for i, j, d in D_up:
    D[i][j] = float(d)
    D[j][i] = float(d)
print(f"  loaded {len(D_up)} pairs (expected {114*113//2} = 6441)", file=sys.stderr)
assert len(D_up) == 114 * 113 // 2, f"D upper-triangular has wrong size: {len(D_up)}"

L_mushaf_h111 = float(h111['primary']['L_mushaf'])
L_noldeke_h111 = float(h111['secondary_B']['L_noldeke'])
L_tanzil_h111 = float(h111['secondary_B']['L_tanzil_egyptian_std'])
print(f"  reference L_mushaf (H-NEW-111) = {L_mushaf_h111:.4f}", file=sys.stderr)
print(f"  reference L_noldeke (H-NEW-111) = {L_noldeke_h111:.4f}", file=sys.stderr)
print(f"  reference L_egyptian-std (H-NEW-111) = {L_tanzil_h111:.4f}", file=sys.stderr)


def path_length(order):
    L = 0.0
    for i in range(len(order) - 1):
        L += D[order[i]][order[i + 1]]
    return L


# Sanity: recompute L_mushaf and L_noldeke from D and compare
mushaf_order = list(range(1, 115))
L_mushaf = path_length(mushaf_order)
print(f"  recomputed L_mushaf = {L_mushaf:.4f}  (matches H-NEW-111: "
      f"{abs(L_mushaf - L_mushaf_h111) < 1e-4})", file=sys.stderr)

# -----------------------------------------------------------------------------
# 2. Load Egyptian Standard + Nöldeke orderings from CSV
# -----------------------------------------------------------------------------
mushaf_to_egyptian = {}
mushaf_to_noldeke = {}
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        msid = int(row['mushaf_order'])
        mushaf_to_egyptian[msid] = int(row['revelation_order'])
        mushaf_to_noldeke[msid] = int(row['noldeke_order'])

egyptian_order_list = sorted(range(1, 115), key=lambda sid: mushaf_to_egyptian[sid])
noldeke_order_list = sorted(range(1, 115), key=lambda sid: mushaf_to_noldeke[sid])
L_egyptian = path_length(egyptian_order_list)
L_noldeke = path_length(noldeke_order_list)

# Sanity check vs H-NEW-111 stored values
assert abs(L_egyptian - L_tanzil_h111) < 1e-4, (
    f"L_egyptian recomputed {L_egyptian} != H-NEW-111 {L_tanzil_h111}")
assert abs(L_noldeke - L_noldeke_h111) < 1e-4, (
    f"L_noldeke recomputed {L_noldeke} != H-NEW-111 {L_noldeke_h111}")
print(f"\nL_egyptian = {L_egyptian:.4f}", file=sys.stderr)
print(f"L_noldeke  = {L_noldeke:.4f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 3. Hard-code Bell 1937 and Blachère 1947 chronological ranks
#    Source: French Wikipedia "Sourate" chronology table.
#    Data-quality caveats (per pre-reg garden-of-forking-paths §5-6):
#      - Bell rank for surah 15 coded "M" not numeric in source; imputed
#        to middle Meccan median (Bell rank 52).
#      - Bell ties: s81 & s82 both rank 15 → use mushaf-order secondary.
#      - Blachère ties: s80 & s84 both rank 24 → use mushaf-order secondary.
# -----------------------------------------------------------------------------

# mushaf_number -> bell_rank (int)
BELL_RANK = {
    1: 45, 2: 91, 3: 97, 4: 100, 5: 114, 6: 89, 7: 87, 8: 95, 9: 113, 10: 84,
    11: 75, 12: 77, 13: 90, 14: 76,
    15: 52,  # IMPUTED (coded "M" in source); middle-Meccan median
    16: 73, 17: 72, 18: 68, 19: 58, 20: 55, 21: 65, 22: 107, 23: 64, 24: 105,
    25: 66, 26: 56, 27: 67, 28: 79, 29: 81, 30: 74, 31: 82, 32: 69, 33: 103,
    34: 85, 35: 86, 36: 60, 37: 51, 38: 59, 39: 80, 40: 78, 41: 70, 42: 62,
    43: 61, 44: 53, 45: 71, 46: 88, 47: 96, 48: 108, 49: 112, 50: 54, 51: 48,
    52: 22, 53: 30, 54: 49, 55: 28, 56: 23, 57: 99, 58: 106, 59: 102, 60: 110,
    61: 98, 62: 94, 63: 104, 64: 93, 65: 101, 66: 109, 67: 63, 68: 50, 69: 24,
    70: 32, 71: 52, 72: 62, 73: 33, 74: 2, 75: 27, 76: 34, 77: 25, 78: 26,
    79: 20, 80: 17,
    81: 15, 82: 15,  # TIE (mushaf-order 2ndary sort)
    83: 35, 84: 19, 85: 42, 86: 9, 87: 16, 88: 21, 89: 41, 90: 39, 91: 7,
    92: 14, 93: 4, 94: 5, 95: 10, 96: 1, 97: 29, 98: 92, 99: 11, 100: 13,
    101: 12, 102: 31, 103: 6, 104: 38, 105: 40, 106: 3, 107: 8, 108: 37,
    109: 44, 110: 111, 111: 36, 112: 43, 113: 46, 114: 47,
}

# mushaf_number -> blachere_rank (int)
BLACHERE_RANK = {
    1: 5, 2: 87, 3: 89, 4: 92, 5: 112, 6: 55, 7: 39, 8: 88, 9: 113, 10: 51,
    11: 52, 12: 53, 13: 96, 14: 72, 15: 54, 16: 70, 17: 50, 18: 69, 19: 44,
    20: 45, 21: 73, 22: 103, 23: 74, 24: 102, 25: 42, 26: 47, 27: 48, 28: 49,
    29: 85, 30: 84, 31: 57, 32: 75, 33: 90, 34: 58, 35: 43, 36: 41, 37: 56,
    38: 38, 39: 59, 40: 60, 41: 61, 42: 53, 43: 63, 44: 64, 45: 65, 46: 66,
    47: 95, 48: 111, 49: 106, 50: 34, 51: 67, 52: 76, 53: 23, 54: 37, 55: 97,
    56: 46, 57: 94, 58: 105, 59: 101, 60: 91, 61: 109, 62: 110, 63: 104,
    64: 108, 65: 99, 66: 107, 67: 77, 68: 2, 69: 78, 70: 79, 71: 71, 72: 40,
    73: 3, 74: 4, 75: 31, 76: 98, 77: 33, 78: 80, 79: 81,
    80: 24, 84: 24,  # TIE (mushaf-order 2ndary sort)
    81: 82, 82: 86,
    83: 83, 85: 27, 86: 36, 87: 8, 88: 68, 89: 10, 90: 35, 91: 26, 92: 9,
    93: 11, 94: 12, 95: 28, 96: 1, 97: 25, 98: 100, 99: 93, 100: 14, 101: 30,
    102: 16, 103: 13, 104: 32, 105: 19, 106: 29, 107: 17, 108: 15, 109: 18,
    110: 114, 111: 6, 112: 22, 113: 20, 114: 21,
}

# Integrity
assert len(BELL_RANK) == 114, f"Bell rank dict has {len(BELL_RANK)} entries"
assert len(BLACHERE_RANK) == 114, f"Blachère rank dict has {len(BLACHERE_RANK)} entries"
for sid in range(1, 115):
    assert sid in BELL_RANK, f"missing Bell rank for surah {sid}"
    assert sid in BLACHERE_RANK, f"missing Blachère rank for surah {sid}"

# Sort → ordering. Tie-break: mushaf-order ascending (pre-reg §5).
bell_order_list = sorted(range(1, 115), key=lambda sid: (BELL_RANK[sid], sid))
blachere_order_list = sorted(range(1, 115), key=lambda sid: (BLACHERE_RANK[sid], sid))

L_bell = path_length(bell_order_list)
L_blachere = path_length(blachere_order_list)
print(f"L_bell      = {L_bell:.4f}", file=sys.stderr)
print(f"L_blachere  = {L_blachere:.4f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 4. Run FRESH null: 10,000 uniform permutations with seed 20260419
# -----------------------------------------------------------------------------
print(f"\nFresh null: {PERMS} perms, seed {SEED} ...", file=sys.stderr)
rng = random.Random(SEED)
null_L = []
base = list(range(1, 115))
for p in range(PERMS):
    perm = base[:]
    rng.shuffle(perm)
    null_L.append(path_length(perm))
    if (p + 1) % 2000 == 0:
        print(f"  perm {p+1}/{PERMS}", file=sys.stderr)

null_mean = statistics.mean(null_L)
null_sd = statistics.stdev(null_L)
null_sorted = sorted(null_L)


def q(sl, frac):
    n = len(sl)
    idx = max(0, min(n - 1, int(math.floor(frac * n))))
    return sl[idx]


null_quantiles = {
    'min': null_sorted[0],
    'q001': q(null_sorted, 0.001),
    'q01': q(null_sorted, 0.01),
    'q025': q(null_sorted, 0.025),
    'q05': q(null_sorted, 0.05),
    'q25': q(null_sorted, 0.25),
    'q50': q(null_sorted, 0.50),
    'q75': q(null_sorted, 0.75),
    'q95': q(null_sorted, 0.95),
    'max': null_sorted[-1],
    'mean': null_mean,
    'sd': null_sd,
}

print(f"  null mean={null_mean:.4f} sd={null_sd:.4f}", file=sys.stderr)
print(f"  null min={null_sorted[0]:.4f} q05={null_quantiles['q05']:.4f}",
      file=sys.stderr)


def p_lower(L):
    n_le = sum(1 for x in null_L if x <= L)
    return (n_le + 1) / (PERMS + 1), n_le


# -----------------------------------------------------------------------------
# 5. Apply the null to each ordering
# -----------------------------------------------------------------------------
results = {}
for name, L, order_list in [
    ('mushaf', L_mushaf, mushaf_order),
    ('egyptian_1924', L_egyptian, egyptian_order_list),
    ('noldeke_1860', L_noldeke, noldeke_order_list),
    ('bell_1937', L_bell, bell_order_list),
    ('blachere_1947', L_blachere, blachere_order_list),
]:
    p, n_le = p_lower(L)
    z = (L - null_mean) / null_sd
    results[name] = {
        'L': L,
        'z': z,
        'n_perms_le': n_le,
        'p_one_sided_lower': p,
        'first20_order': order_list[:20],
    }
    print(f"  {name:15s}: L={L:.4f}  z={z:+.3f}  p_1sided={p:.6f}",
          file=sys.stderr)

# -----------------------------------------------------------------------------
# 6. Ranked leaderboard (shortest wins)
# -----------------------------------------------------------------------------
leaderboard = sorted(results.items(), key=lambda kv: kv[1]['L'])
print("\nRanked (shortest first):", file=sys.stderr)
for rank, (name, r) in enumerate(leaderboard, 1):
    tag = ""
    if name == 'mushaf':
        tag = "  <-- mushaf"
    print(f"  {rank}. {name:15s} L={r['L']:.4f}  p={r['p_one_sided_lower']:.6f}{tag}",
          file=sys.stderr)

shortest_name = leaderboard[0][0]
mushaf_rank = next(i for i, (n, _) in enumerate(leaderboard, 1) if n == 'mushaf')
print(f"\n SHORTEST: {shortest_name}", file=sys.stderr)
print(f" MUSHAF RANK: {mushaf_rank} of 5", file=sys.stderr)

# -----------------------------------------------------------------------------
# 7. Bonferroni verdicts for the 3-member test family
# -----------------------------------------------------------------------------
family = ['egyptian_1924', 'bell_1937', 'blachere_1947']
verdicts = {}
any_pass = False
for name in family:
    p = results[name]['p_one_sided_lower']
    passed = p < ALPHA_BON
    verdicts[name] = {
        'p': p,
        'alpha_bon': ALPHA_BON,
        'pass': passed,
    }
    if passed:
        any_pass = True
    print(f"  {name}: p={p:.6f}  α_bon={ALPHA_BON:.5f}  "
          f"{'PASS' if passed else 'NULL'}", file=sys.stderr)

mushaf_still_wins = all(results[n]['L'] > L_mushaf for n in family)
print(f"\nMushaf still wins (shorter than all 3 chronologies)? "
      f"{mushaf_still_wins}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 8. Spearman rank correlations across chronologies (diagnostic)
# -----------------------------------------------------------------------------
def spearman(ranks_a, ranks_b):
    """ranks_a, ranks_b: dicts mushaf_id -> rank. Returns ρ in [-1,1]."""
    sids = sorted(ranks_a.keys())
    a = [ranks_a[s] for s in sids]
    b = [ranks_b[s] for s in sids]
    n = len(sids)
    mean_a = sum(a) / n
    mean_b = sum(b) / n
    num = sum((a[i] - mean_a) * (b[i] - mean_b) for i in range(n))
    da = math.sqrt(sum((a[i] - mean_a) ** 2 for i in range(n)))
    db = math.sqrt(sum((b[i] - mean_b) ** 2 for i in range(n)))
    return num / (da * db) if da * db > 0 else 0.0


chrono_ranks = {
    'mushaf': {sid: sid for sid in range(1, 115)},
    'egyptian_1924': mushaf_to_egyptian,
    'noldeke_1860': mushaf_to_noldeke,
    'bell_1937': BELL_RANK,
    'blachere_1947': BLACHERE_RANK,
}
names = list(chrono_ranks)
rank_matrix = {}
for a in names:
    for b in names:
        if a >= b:
            continue
        rho = spearman(chrono_ranks[a], chrono_ranks[b])
        rank_matrix[f"{a} vs {b}"] = rho
        print(f"  ρ({a}, {b}) = {rho:+.4f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 9. Pairwise path-length diffs (L_c − L_mushaf) in null-SD units
# -----------------------------------------------------------------------------
pairwise_diffs = {}
for name in ['egyptian_1924', 'noldeke_1860', 'bell_1937', 'blachere_1947']:
    d = results[name]['L'] - L_mushaf
    pairwise_diffs[name] = {
        'L_minus_mushaf_raw': d,
        'L_minus_mushaf_in_null_sd': d / null_sd,
    }
    sign = 'LONGER than mushaf' if d > 0 else 'SHORTER than mushaf'
    print(f"  {name}: Δ={d:+.4f} ({d/null_sd:+.3f} SDs)  [{sign}]",
          file=sys.stderr)

# -----------------------------------------------------------------------------
# 10. Write JSON
# -----------------------------------------------------------------------------
def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o

summary = {
    'finding_id': 'h-new-212',
    'title': 'Alternative chronology orderings — Fisher-Rao path length',
    'pre_reg_sha256': prereg_sha,
    'h_new_111_source_sha256': h111_sha,
    'seed': SEED,
    'permutations': PERMS,
    'bonferroni_k': BONFERRONI_K,
    'alpha_bon': ALPHA_BON,
    'date': '2026-04-17',
    'rules_tuple': ('(no-tashkeel, QAC-STEM root tokens, QAC v0.4, '
                    'basmala-counted-only-in-surah-1, Hafs-Kufan, '
                    'D-matrix-inherited-from-H-NEW-111)'),
    'null_quantiles': null_quantiles,
    'results': results,
    'leaderboard_shortest_first': [
        {'rank': i + 1, 'name': n, 'L': r['L'], 'p': r['p_one_sided_lower']}
        for i, (n, r) in enumerate(leaderboard)
    ],
    'shortest_name': shortest_name,
    'mushaf_rank_among_5': mushaf_rank,
    'bonferroni_family_verdicts': verdicts,
    'family_any_pass': any_pass,
    'mushaf_still_wins_over_all_3_chronologies': mushaf_still_wins,
    'chronology_spearman_matrix': rank_matrix,
    'pairwise_path_diffs_vs_mushaf': pairwise_diffs,
    'bell_data_quality_caveat': (
        'Surah 15 imputed rank 52 (coded "M" not numeric in Fr. Wiki); '
        'ties (s81/s82 both rank 15) resolved by mushaf-order secondary'),
    'blachere_data_quality_caveat': (
        'Tie s80/s84 (both rank 24) resolved by mushaf-order secondary'),
    'verdict_primary': (
        'SEE leaderboard + family verdicts'),
}
summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 11. Final stdout summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 72, file=sys.stderr)
print("H-NEW-212 SUMMARY (Fisher-Rao; 3-chronology family; α_bon=0.01667)",
      file=sys.stderr)
print("=" * 72, file=sys.stderr)
print(f"  L_mushaf        = {L_mushaf:.4f}  (reference, not in family)",
      file=sys.stderr)
print(f"  L_noldeke_1860  = {L_noldeke:.4f}  (reference, not in family)",
      file=sys.stderr)
print(f"  L_egyptian_1924 = {L_egyptian:.4f}  p={results['egyptian_1924']['p_one_sided_lower']:.6f}",
      file=sys.stderr)
print(f"  L_bell_1937     = {L_bell:.4f}  p={results['bell_1937']['p_one_sided_lower']:.6f}",
      file=sys.stderr)
print(f"  L_blachere_1947 = {L_blachere:.4f}  p={results['blachere_1947']['p_one_sided_lower']:.6f}",
      file=sys.stderr)
print(f"  null mean/sd = {null_mean:.4f} / {null_sd:.4f}", file=sys.stderr)
print(f"  SHORTEST ordering = {shortest_name}", file=sys.stderr)
print(f"  mushaf rank among 5 = {mushaf_rank}", file=sys.stderr)
print(f"  mushaf still wins over all 3 chronologies: {mushaf_still_wins}",
      file=sys.stderr)
print("=" * 72, file=sys.stderr)
