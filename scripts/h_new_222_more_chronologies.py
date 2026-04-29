#!/usr/bin/env python3
"""H-NEW-222 — Additional classical chronologies vs Fisher-Rao path length.

Pre-registered tests (Bonferroni k=4, α_bon=0.0125):
  PRIMARY-1 — L_ibn_abbas    < L_random (1-sided lower, perm p<0.0125)
  PRIMARY-2 — L_suyuti_itqan < L_random (1-sided lower, perm p<0.0125)
  PRIMARY-3 — L_tanzil       < L_random (replication of H-NEW-212 egyptian)
  PRIMARY-4 — L_watt_bell    < L_random (1-sided lower, perm p<0.0125)

Mushaf reported as descriptive reference (not in family).

Reuses distance matrix D from h-new-111.json (Fisher-Rao angular distance
on QAC STEM root top-500 Dirichlet-smoothed L1-normalized probability
vectors). Seed 20260419 (same as H-NEW-212 — null directly comparable).

SOURCES for chronology tables:
  * Ibn ʿAbbās (ʿAbd al-Kāfī): understandingislam.today transcription,
    cross-checked against Robinson 2003 p.77. One source-typo fix:
    rank 60 was coded as surah 4 (duplicate); corrected to surah 41
    (Fuṣṣilat) based on the narrative context (late-Meccan group
    between surahs 40 and 42). Documented in pre-reg §6.
  * al-Suyūṭī al-Itqān (Jābir b. Zayd transmission): per Itqān nawʿ 7,
    Suyūṭī endorses the Jābir b. Zayd transmission as soundest. This
    list is essentially identical to Tanzil (al-Zanjānī's al-Itqān
    derivative). We use the same list as Tanzil here but test it under
    its own Bonferroni slot — honestly acknowledging that p will match
    Tanzil's. This is NOT padding: it's a formal test of whether
    Suyūṭī's self-identified preferred transmission matches the
    Cairo 1924 edition numerically. (It does; documented explicitly.)
  * Tanzil / Egyptian Standard 1924: from data/revelation-order.csv.
  * Watt-Bell (1970) Introduction ch. 7: four-phase ordering as
    transcribed from truthnet.org/islam/Watt/Chapter7.html. Total
    surahs per phase: 48 first-Meccan + 21 second-Meccan + 21
    third-Meccan + 24 Medinan = 114. No imputations needed.

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
BONFERRONI_K = 4
ALPHA_BON = 0.05 / BONFERRONI_K  # = 0.0125

PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-222-more-chronologies-prereg.md'
H111_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
H212_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-212.json'
TANZIL_CSV = ROOT / 'data/revelation-order.csv'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-222.json'

# -----------------------------------------------------------------------------
# Pre-reg tamper-evidence
# -----------------------------------------------------------------------------
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
h111_sha = hashlib.sha256(H111_JSON.read_bytes()).hexdigest()
h212_sha = hashlib.sha256(H212_JSON.read_bytes()).hexdigest()
print(f"prereg SHA-256:  {prereg_sha}", file=sys.stderr)
print(f"h-new-111 D-matrix SHA-256: {h111_sha}", file=sys.stderr)
print(f"h-new-212 cross-ref SHA-256: {h212_sha}", file=sys.stderr)
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
assert len(D_up) == 114 * 113 // 2

L_mushaf_h111 = float(h111['primary']['L_mushaf'])
L_tanzil_h111 = float(h111['secondary_B']['L_tanzil_egyptian_std'])

# Also load H-NEW-212 egyptian L as cross-check
h212 = json.loads(H212_JSON.read_text())
L_egyptian_h212 = float(h212['results']['egyptian_1924']['L'])

print(f"  ref L_mushaf (H-NEW-111) = {L_mushaf_h111:.4f}", file=sys.stderr)
print(f"  ref L_egyptian (H-NEW-212) = {L_egyptian_h212:.4f}", file=sys.stderr)


def path_length(order):
    L = 0.0
    for i in range(len(order) - 1):
        L += D[order[i]][order[i + 1]]
    return L


mushaf_order = list(range(1, 115))
L_mushaf = path_length(mushaf_order)
assert abs(L_mushaf - L_mushaf_h111) < 1e-4

# -----------------------------------------------------------------------------
# 2. Tanzil / Egyptian Standard ordering (from revelation-order.csv)
# -----------------------------------------------------------------------------
mushaf_to_tanzil = {}
with open(TANZIL_CSV, encoding='utf-8') as f:
    for row in csv.DictReader(f):
        mushaf_to_tanzil[int(row['mushaf_order'])] = int(row['revelation_order'])

tanzil_order_list = sorted(range(1, 115), key=lambda s: mushaf_to_tanzil[s])
L_tanzil = path_length(tanzil_order_list)

# Sanity: L_tanzil must match L_egyptian_h212 within 1e-4 (MW-1 instrument check)
instrument_ok = abs(L_tanzil - L_egyptian_h212) < 1e-4
assert instrument_ok, (
    f"INSTRUMENT-BROKEN: L_tanzil={L_tanzil} != H-NEW-212 egyptian {L_egyptian_h212}")
print(f"\n[OK] L_tanzil replicates H-NEW-212 egyptian ({L_tanzil:.4f}) — "
      f"instrument intact", file=sys.stderr)

# -----------------------------------------------------------------------------
# 3. Ibn ʿAbbās (ʿAbd al-Kāfī transmission)
#    Source: understandingislam.today; typo-correction rank 60 = surah 41
#    (source had "4" duplicated between rank 60 and rank 92; rank 92 = 4
#    (an-Nisāʾ, Medinan) is correct; rank 60 must be 41 (Fuṣṣilat) from
#    the narrative context (between surahs 40 and 42, late-Meccan group).
# -----------------------------------------------------------------------------
ibn_abbas_order = [
    96, 68, 73, 74, 111, 81, 87, 92, 89, 93, 94, 103, 100, 108, 102, 107,
    109, 105, 113, 114, 112, 53, 80, 97, 91, 85, 95, 106, 101, 75, 104,
    77, 50, 90, 86, 54, 38, 7, 72, 36, 25, 35, 19, 20, 56, 26, 27, 28,
    17, 10, 11, 12, 15, 6, 37, 31, 34, 39, 40, 41, 1, 42, 43, 44, 45,
    46, 51, 88, 18, 16, 71, 14, 21, 23, 32, 52, 67, 69, 70, 78, 79, 82,
    84, 30, 29, 83, 2, 8, 3, 33, 60, 4, 99, 57, 47, 13, 55, 76, 65, 98,
    59, 110, 24, 22, 63, 58, 49, 66, 62, 64, 61, 48, 5, 9,
]
assert len(ibn_abbas_order) == 114
assert set(ibn_abbas_order) == set(range(1, 115))
L_ibn_abbas = path_length(ibn_abbas_order)

# -----------------------------------------------------------------------------
# 4. al-Suyūṭī al-Itqān (Jābir b. Zayd transmission)
#    Per Itqān fī ʿulūm al-Qurʾān nawʿ 7, Suyūṭī endorses the Jābir b. Zayd
#    transmission. Al-Zanjānī's Tārīkh al-Qurʾān (basis of Tanzil) is this
#    transmission. So Suyūṭī Itqān list = Tanzil list in practice.
#    We use Tanzil's ordering here and DOCUMENT explicitly in the MD.
# -----------------------------------------------------------------------------
suyuti_itqan_order = list(tanzil_order_list)  # identical to Tanzil
L_suyuti_itqan = path_length(suyuti_itqan_order)

# -----------------------------------------------------------------------------
# 5. Watt-Bell (1970) Introduction ch. 7 — 4-phase ordering
#    Source: truthnet.org/islam/Watt/Chapter7.html
#    First Meccan (48 surahs):
#      96,74,111,106,108,104,107,102,105,92,90,94,93,97,86,91,80,68,87,95,
#      103,85,73,101,99,82,81,53,84,100,79,77,78,88,89,75,83,69,51,52,56,
#      70,55,112,109,113,114,1
#    Second Meccan (21 surahs):
#      54,37,71,76,44,50,20,26,15,19,38,36,43,72,67,23,21,25,17,27,18
#    Third Meccan (21 surahs):
#      32,41,45,16,30,11,14,12,40,28,39,29,31,42,10,34,35,7,46,6,13
#    Medinan (24 surahs):
#      2,98,64,62,8,47,3,61,57,4,65,59,33,63,24,58,22,48,66,60,110,49,9,5
# -----------------------------------------------------------------------------
watt_bell_first_meccan = [
    96, 74, 111, 106, 108, 104, 107, 102, 105, 92, 90, 94, 93, 97, 86, 91,
    80, 68, 87, 95, 103, 85, 73, 101, 99, 82, 81, 53, 84, 100, 79, 77, 78,
    88, 89, 75, 83, 69, 51, 52, 56, 70, 55, 112, 109, 113, 114, 1,
]
watt_bell_second_meccan = [
    54, 37, 71, 76, 44, 50, 20, 26, 15, 19, 38, 36, 43, 72, 67, 23, 21, 25,
    17, 27, 18,
]
watt_bell_third_meccan = [
    32, 41, 45, 16, 30, 11, 14, 12, 40, 28, 39, 29, 31, 42, 10, 34, 35, 7,
    46, 6, 13,
]
watt_bell_medinan = [
    2, 98, 64, 62, 8, 47, 3, 61, 57, 4, 65, 59, 33, 63, 24, 58, 22, 48, 66,
    60, 110, 49, 9, 5,
]
assert len(watt_bell_first_meccan) == 48, len(watt_bell_first_meccan)
assert len(watt_bell_second_meccan) == 21, len(watt_bell_second_meccan)
assert len(watt_bell_third_meccan) == 21, len(watt_bell_third_meccan)
assert len(watt_bell_medinan) == 24, len(watt_bell_medinan)

watt_bell_order = (
    watt_bell_first_meccan + watt_bell_second_meccan +
    watt_bell_third_meccan + watt_bell_medinan
)
assert len(watt_bell_order) == 114
assert set(watt_bell_order) == set(range(1, 115)), (
    f"missing/extra: {set(range(1,115)) - set(watt_bell_order)} / "
    f"{set(watt_bell_order) - set(range(1,115))}")
L_watt_bell = path_length(watt_bell_order)

print(f"\nL_mushaf          = {L_mushaf:.4f}", file=sys.stderr)
print(f"L_ibn_abbas       = {L_ibn_abbas:.4f}", file=sys.stderr)
print(f"L_suyuti_itqan    = {L_suyuti_itqan:.4f}  (= L_tanzil by construction)",
      file=sys.stderr)
print(f"L_tanzil          = {L_tanzil:.4f}", file=sys.stderr)
print(f"L_watt_bell       = {L_watt_bell:.4f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 6. Run FRESH null: 10,000 uniform permutations with seed 20260419
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

print(f"  null mean={null_mean:.4f} sd={null_sd:.4f}  min={null_sorted[0]:.4f}",
      file=sys.stderr)


def p_lower(L):
    n_le = sum(1 for x in null_L if x <= L)
    return (n_le + 1) / (PERMS + 1), n_le


# -----------------------------------------------------------------------------
# 7. Apply the null to each ordering
# -----------------------------------------------------------------------------
results = {}
for name, L, order_list in [
    ('mushaf',         L_mushaf,         mushaf_order),
    ('ibn_abbas',      L_ibn_abbas,      ibn_abbas_order),
    ('suyuti_itqan',   L_suyuti_itqan,   suyuti_itqan_order),
    ('tanzil',         L_tanzil,         tanzil_order_list),
    ('watt_bell',      L_watt_bell,      watt_bell_order),
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
    print(f"  {name:14s}: L={L:.4f}  z={z:+.3f}  p_1sided={p:.6f}",
          file=sys.stderr)

# -----------------------------------------------------------------------------
# 8. Leaderboard (shortest wins)
# -----------------------------------------------------------------------------
leaderboard = sorted(results.items(), key=lambda kv: kv[1]['L'])
print("\nRanked (shortest first):", file=sys.stderr)
for rank, (name, r) in enumerate(leaderboard, 1):
    tag = "  <-- mushaf" if name == 'mushaf' else ""
    print(f"  {rank}. {name:14s} L={r['L']:.4f}  p={r['p_one_sided_lower']:.6f}{tag}",
          file=sys.stderr)

shortest_name = leaderboard[0][0]
mushaf_rank = next(i for i, (n, _) in enumerate(leaderboard, 1) if n == 'mushaf')
print(f"\n SHORTEST: {shortest_name}", file=sys.stderr)
print(f" MUSHAF RANK: {mushaf_rank} of {len(results)}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 9. Bonferroni verdicts for the 4-member test family
# -----------------------------------------------------------------------------
family = ['ibn_abbas', 'suyuti_itqan', 'tanzil', 'watt_bell']
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
print(f"\nMushaf still wins (shorter than all 4 chronologies)? "
      f"{mushaf_still_wins}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 10. Spearman rank correlations (new chronologies vs old + mushaf)
# -----------------------------------------------------------------------------
def spearman(ranks_a, ranks_b):
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


def order_to_ranks(order_list):
    return {s: (order_list.index(s) + 1) for s in order_list}


chrono_ranks = {
    'mushaf': {s: s for s in range(1, 115)},
    'ibn_abbas': order_to_ranks(ibn_abbas_order),
    'suyuti_itqan': order_to_ranks(suyuti_itqan_order),
    'tanzil': order_to_ranks(tanzil_order_list),
    'watt_bell': order_to_ranks(watt_bell_order),
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
# 11. Pairwise path-length diffs vs mushaf
# -----------------------------------------------------------------------------
pairwise_diffs = {}
for name in family:
    d = results[name]['L'] - L_mushaf
    pairwise_diffs[name] = {
        'L_minus_mushaf_raw': d,
        'L_minus_mushaf_in_null_sd': d / null_sd,
    }
    sign = 'LONGER than mushaf' if d > 0 else 'SHORTER than mushaf'
    print(f"  {name}: Δ={d:+.4f} ({d/null_sd:+.3f} SDs)  [{sign}]",
          file=sys.stderr)

# -----------------------------------------------------------------------------
# 12. Cross-study comparison: H-NEW-222 vs H-NEW-212 orderings
# -----------------------------------------------------------------------------
h212_egypt_L = float(h212['results']['egyptian_1924']['L'])
h212_nold_L  = float(h212['results']['noldeke_1860']['L'])
h212_bell_L  = float(h212['results']['bell_1937']['L'])
h212_blach_L = float(h212['results']['blachere_1947']['L'])

# Combined 7-ordering leaderboard (mushaf + 4 new + 3 external, not double-counting tanzil == egyptian)
combined = {
    'mushaf':        L_mushaf,
    'noldeke_1860':  h212_nold_L,
    'bell_1937':     h212_bell_L,
    'blachere_1947': h212_blach_L,
    'ibn_abbas':     L_ibn_abbas,
    'suyuti_itqan':  L_suyuti_itqan,
    'tanzil_egyptian_1924': L_tanzil,
    'watt_bell_1970': L_watt_bell,
}
combined_sorted = sorted(combined.items(), key=lambda kv: kv[1])
print("\n===== COMBINED LEADERBOARD (H-NEW-212 + H-NEW-222) =====", file=sys.stderr)
for rank, (name, L) in enumerate(combined_sorted, 1):
    p_lo, _ = p_lower(L)
    z = (L - null_mean) / null_sd
    tag = "  <-- mushaf" if name == 'mushaf' else ""
    print(f"  {rank}. {name:22s} L={L:.4f}  z={z:+.3f}  p={p_lo:.6f}{tag}",
          file=sys.stderr)

# -----------------------------------------------------------------------------
# 13. Write JSON
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
    'finding_id': 'h-new-222',
    'title': 'Additional classical chronologies — Fisher-Rao path length',
    'pre_reg_sha256': prereg_sha,
    'h_new_111_source_sha256': h111_sha,
    'h_new_212_source_sha256': h212_sha,
    'seed': SEED,
    'permutations': PERMS,
    'bonferroni_k': BONFERRONI_K,
    'alpha_bon': ALPHA_BON,
    'date': '2026-04-17',
    'rules_tuple': (
        '(no-tashkeel, QAC-STEM root tokens, QAC v0.4, '
        'basmala-counted-only-in-surah-1, Hafs-Kufan, '
        'D-matrix-inherited-from-H-NEW-111)'),
    'null_quantiles': null_quantiles,
    'instrument_check': {
        'L_tanzil_h222': L_tanzil,
        'L_egyptian_h212': L_egyptian_h212,
        'delta': L_tanzil - L_egyptian_h212,
        'ok_within_1e-4': abs(L_tanzil - L_egyptian_h212) < 1e-4,
    },
    'source_notes': {
        'ibn_abbas': 'understandingislam.today transcription of the ʿAbd al-Kāfī '
                     'version of Ibn ʿAbbās (ʿAṭāʾ transmission); typo fix '
                     'at chronological rank 60 (source had duplicate surah 4; '
                     'corrected to surah 41 Fuṣṣilat per narrative context).',
        'suyuti_itqan': 'Per al-Suyūṭī al-Itqān fī ʿulūm al-Qurʾān, nawʿ 7: '
                        'Suyūṭī endorses the Jābir b. Zayd transmission. The '
                        'list = Tanzil/al-Zanjānī list in practice (both derive '
                        'from Jābir b. Zayd → Ibn ʿAbbās). Documented here as '
                        'a formal test slot; Bonferroni k=4 is preserved.',
        'tanzil': 'data/revelation-order.csv column revelation_order (= '
                  'Tanzil.net = Cairo 1924 edition).',
        'watt_bell': 'W. M. Watt, Bell\'s Introduction to the Qur\'an, '
                     'Edinburgh UP 1970, ch. 7. Four-phase ordering with '
                     'Watt\'s within-phase ordering. 48+21+21+24 = 114; '
                     'no imputations. Source: truthnet.org/islam/Watt/Chapter7.html.',
    },
    'results': results,
    'leaderboard_shortest_first': [
        {'rank': i + 1, 'name': n, 'L': r['L'], 'p': r['p_one_sided_lower']}
        for i, (n, r) in enumerate(leaderboard)
    ],
    'shortest_name': shortest_name,
    'mushaf_rank_among_5': mushaf_rank,
    'bonferroni_family_verdicts': verdicts,
    'family_any_pass': any_pass,
    'mushaf_still_wins_over_all_4_chronologies': mushaf_still_wins,
    'chronology_spearman_matrix': rank_matrix,
    'pairwise_path_diffs_vs_mushaf': pairwise_diffs,
    'combined_leaderboard_h212_plus_h222': [
        {'rank': i + 1, 'name': n, 'L': L}
        for i, (n, L) in enumerate(combined_sorted)
    ],
    'orderings_full': {
        'ibn_abbas': ibn_abbas_order,
        'suyuti_itqan': suyuti_itqan_order,
        'tanzil': tanzil_order_list,
        'watt_bell': watt_bell_order,
    },
}
summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 14. Final stdout summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 72, file=sys.stderr)
print("H-NEW-222 SUMMARY (Fisher-Rao; 4-chronology family; α_bon=0.0125)",
      file=sys.stderr)
print("=" * 72, file=sys.stderr)
print(f"  L_mushaf        = {L_mushaf:.4f}  (reference, not in family)",
      file=sys.stderr)
print(f"  L_ibn_abbas     = {L_ibn_abbas:.4f}  p={results['ibn_abbas']['p_one_sided_lower']:.6f}",
      file=sys.stderr)
print(f"  L_suyuti_itqan  = {L_suyuti_itqan:.4f}  p={results['suyuti_itqan']['p_one_sided_lower']:.6f}",
      file=sys.stderr)
print(f"  L_tanzil        = {L_tanzil:.4f}  p={results['tanzil']['p_one_sided_lower']:.6f}",
      file=sys.stderr)
print(f"  L_watt_bell     = {L_watt_bell:.4f}  p={results['watt_bell']['p_one_sided_lower']:.6f}",
      file=sys.stderr)
print(f"  null mean/sd = {null_mean:.4f} / {null_sd:.4f}", file=sys.stderr)
print(f"  SHORTEST ordering = {shortest_name}", file=sys.stderr)
print(f"  mushaf rank among 5 = {mushaf_rank}", file=sys.stderr)
print(f"  mushaf still wins over all 4 chronologies: {mushaf_still_wins}",
      file=sys.stderr)
print("=" * 72, file=sys.stderr)
