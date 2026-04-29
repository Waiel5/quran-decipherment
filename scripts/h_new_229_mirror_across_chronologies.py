#!/usr/bin/env python3
"""H-NEW-229 — Mirror-pair structure across chronologies.

Does the ±58 Nöldeke chronology-reversal mirror at Q 49→50 and Q 56→57
(H-NEW-142) exist under other chronologies (Bell, Egyptian, Blachère)?

Primary descriptive test (per pre-reg): under each chronology C, does
the specific {Q 49→50, Q 56→57} pair-pair exhibit:
  (a) EQUAL |Δ_C| at both pairs (strict ±0),
  (b) OPPOSITE signs,
  (c) Magnitude ≥ median |Δ_C| across all 113 pairs.

Secondary: largest mirrored |Δ_C| per chronology and its location.

Bonferroni k=1. Seed 20260419. No randomization actually used in this
descriptive test; seed retained for reproducibility.
"""
import csv
import hashlib
import json
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
BONFERRONI_K = 1

PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-229-mirror-pair-structure-across-chronologies-prereg.md'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
H212_SCRIPT = ROOT / 'scripts/h_new_212_alt_chronology_fisher_rao.py'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-229.json'

# Pre-reg tamper-evidence
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
h212_sha = hashlib.sha256(H212_SCRIPT.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"H-NEW-212 source SHA-256 (Bell/Blachère dicts): {h212_sha}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"BONFERRONI_K = {BONFERRONI_K}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 1. Load Egyptian + Nöldeke chronologies from CSV
# -----------------------------------------------------------------------------
mushaf_to_egyptian = {}
mushaf_to_noldeke = {}
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        msid = int(row['mushaf_order'])
        mushaf_to_egyptian[msid] = int(row['revelation_order'])
        mushaf_to_noldeke[msid] = int(row['noldeke_order'])

assert len(mushaf_to_egyptian) == 114
assert len(mushaf_to_noldeke) == 114

# -----------------------------------------------------------------------------
# 2. Bell 1937 + Blachère 1947 from H-NEW-212 (inherited).
#    NOTE: the inherited dicts from H-NEW-212 have raw ranks with ties
#    (Bell: s81/s82 both 15; Blachère: s80/s84 both 24). These are the
#    RAW source ranks. Below we resolve ties deterministically (mushaf-order
#    ascending, per inherited pre-reg §5) and also re-rank to dense 1..114.
# -----------------------------------------------------------------------------

# mushaf_number -> bell_rank (raw, with ties allowed; s15 imputed 52)
BELL_RANK_RAW = {
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
    81: 15, 82: 15,  # TIE
    83: 35, 84: 19, 85: 42, 86: 9, 87: 16, 88: 21, 89: 41, 90: 39, 91: 7,
    92: 14, 93: 4, 94: 5, 95: 10, 96: 1, 97: 29, 98: 92, 99: 11, 100: 13,
    101: 12, 102: 31, 103: 6, 104: 38, 105: 40, 106: 3, 107: 8, 108: 37,
    109: 44, 110: 111, 111: 36, 112: 43, 113: 46, 114: 47,
}

BLACHERE_RANK_RAW = {
    1: 5, 2: 87, 3: 89, 4: 92, 5: 112, 6: 55, 7: 39, 8: 88, 9: 113, 10: 51,
    11: 52, 12: 53, 13: 96, 14: 72, 15: 54, 16: 70, 17: 50, 18: 69, 19: 44,
    20: 45, 21: 73, 22: 103, 23: 74, 24: 102, 25: 42, 26: 47, 27: 48, 28: 49,
    29: 85, 30: 84, 31: 57, 32: 75, 33: 90, 34: 58, 35: 43, 36: 41, 37: 56,
    38: 38, 39: 59, 40: 60, 41: 61, 42: 53, 43: 63, 44: 64, 45: 65, 46: 66,
    47: 95, 48: 111, 49: 106, 50: 34, 51: 67, 52: 76, 53: 23, 54: 37, 55: 97,
    56: 46, 57: 94, 58: 105, 59: 101, 60: 91, 61: 109, 62: 110, 63: 104,
    64: 108, 65: 99, 66: 107, 67: 77, 68: 2, 69: 78, 70: 79, 71: 71, 72: 40,
    73: 3, 74: 4, 75: 31, 76: 98, 77: 33, 78: 80, 79: 81,
    80: 24, 84: 24,  # TIE
    81: 82, 82: 86,
    83: 83, 85: 27, 86: 36, 87: 8, 88: 68, 89: 10, 90: 35, 91: 26, 92: 9,
    93: 11, 94: 12, 95: 28, 96: 1, 97: 25, 98: 100, 99: 93, 100: 14, 101: 30,
    102: 16, 103: 13, 104: 32, 105: 19, 106: 29, 107: 17, 108: 15, 109: 18,
    110: 114, 111: 6, 112: 22, 113: 20, 114: 21,
}

assert len(BELL_RANK_RAW) == 114
assert len(BLACHERE_RANK_RAW) == 114


def resolve_ties_to_dense_ranks(raw_ranks):
    """Given mushaf_id -> raw_rank (with possible ties), return a fresh
    mushaf_id -> dense_rank in 1..114. Ties broken by mushaf_id ascending
    (inherited H-NEW-212 pre-reg §5)."""
    sorted_sids = sorted(raw_ranks.keys(), key=lambda s: (raw_ranks[s], s))
    return {sid: i + 1 for i, sid in enumerate(sorted_sids)}


# Egyptian and Nöldeke in the CSV are already dense 1..114.
# Confirm this invariant.
egyptian_vals = sorted(mushaf_to_egyptian.values())
noldeke_vals = sorted(mushaf_to_noldeke.values())
assert egyptian_vals == list(range(1, 115))
assert noldeke_vals == list(range(1, 115))

bell_dense = resolve_ties_to_dense_ranks(BELL_RANK_RAW)
blachere_dense = resolve_ties_to_dense_ranks(BLACHERE_RANK_RAW)
assert sorted(bell_dense.values()) == list(range(1, 115))
assert sorted(blachere_dense.values()) == list(range(1, 115))

CHRONOS = {
    'noldeke_1860': mushaf_to_noldeke,
    'egyptian_1924': mushaf_to_egyptian,
    'bell_1937': bell_dense,
    'blachere_1947': blachere_dense,
}

# -----------------------------------------------------------------------------
# 3. Compute Δ_C for all 113 consecutive mushaf pairs
# -----------------------------------------------------------------------------
def compute_deltas(chrono_map):
    """Returns list of (pair_label, i_from, i_to, signed_delta, abs_delta)."""
    out = []
    for i in range(1, 114):  # 1..113
        a = chrono_map[i]
        b = chrono_map[i + 1]
        signed = b - a
        out.append((f"Q{i}->Q{i+1}", i, i + 1, signed, abs(signed)))
    return out


# -----------------------------------------------------------------------------
# 4. Per chronology: descriptive stats, top-6, mirror structure around Q 49→50 / Q 56→57
# -----------------------------------------------------------------------------
def find_mirrored_magnitudes(deltas):
    """Return sorted list of dicts for each |Δ| that has both + and − signs."""
    by_mag = {}
    for lbl, a, b, s, m in deltas:
        by_mag.setdefault(m, []).append((lbl, s))
    mirrored = []
    for m in sorted(by_mag.keys(), reverse=True):
        signs = set(sign_of(s) for _, s in by_mag[m] if s != 0)
        if len(signs) == 2:  # both + and − present
            mirrored.append({
                'abs_delta': m,
                'pairs': by_mag[m],
            })
    return mirrored


def sign_of(x):
    return '+' if x > 0 else ('-' if x < 0 else '0')


results_per_chrono = {}
for name, chrono_map in CHRONOS.items():
    deltas = compute_deltas(chrono_map)

    # All 113 deltas
    by_abs_desc = sorted(deltas, key=lambda t: (-t[4], t[1]))
    top6 = by_abs_desc[:6]

    # Median |Δ| across 113 pairs
    all_abs = [t[4] for t in deltas]
    median_abs = statistics.median(all_abs)
    mean_abs = statistics.mean(all_abs)

    # Specific Q 49→50 (i=49) and Q 56→57 (i=56)
    d_49 = next(t for t in deltas if t[1] == 49)  # Q49->Q50
    d_56 = next(t for t in deltas if t[1] == 56)  # Q56->Q57

    abs_equal = (d_49[4] == d_56[4])
    opposite_signs = (d_49[3] * d_56[3] < 0)
    above_median = (d_49[4] >= median_abs and d_56[4] >= median_abs)
    # Primary test all three
    primary_pass = abs_equal and opposite_signs and above_median

    # Secondary: largest mirrored |Δ|
    mirrored = find_mirrored_magnitudes(deltas)
    largest_mirror = mirrored[0] if mirrored else None

    # Tertiary: does Q 49→50 & Q 56→57 pair match at |Δ| ≥ 50?
    q49_q56_mirror_ge50 = (abs_equal and opposite_signs and d_49[4] >= 50)

    results_per_chrono[name] = {
        'top6_by_abs_desc': [
            {
                'pair': lbl,
                'i_from': a,
                'i_to': b,
                'signed_delta': s,
                'abs_delta': m,
            } for lbl, a, b, s, m in top6
        ],
        'median_abs_delta': median_abs,
        'mean_abs_delta': mean_abs,
        'Q49_to_Q50': {
            'signed_delta': d_49[3],
            'abs_delta': d_49[4],
        },
        'Q56_to_Q57': {
            'signed_delta': d_56[3],
            'abs_delta': d_56[4],
        },
        'primary_test': {
            'abs_equal': abs_equal,
            'opposite_signs': opposite_signs,
            'above_median': above_median,
            'PASS': primary_pass,
        },
        'tertiary_Q49_Q56_mirror_ge50': q49_q56_mirror_ge50,
        'n_distinct_mirrored_abs_magnitudes': len(mirrored),
        'largest_mirrored_abs_delta': largest_mirror['abs_delta'] if largest_mirror else None,
        'largest_mirror_pairs': largest_mirror['pairs'] if largest_mirror else None,
        'all_mirrored_magnitudes_desc_abs': [
            {'abs_delta': mm['abs_delta'],
             'pairs': mm['pairs']}
            for mm in mirrored[:10]  # top 10 for brevity
        ],
    }

    print(f"\n=== {name} ===", file=sys.stderr)
    print(f"  median |Δ| = {median_abs}, mean |Δ| = {mean_abs:.2f}", file=sys.stderr)
    print(f"  top-6 by |Δ|:", file=sys.stderr)
    for t in top6:
        print(f"    {t[0]}  signed={t[3]:+d}  |Δ|={t[4]}", file=sys.stderr)
    print(f"  Q49→Q50: signed={d_49[3]:+d}  |Δ|={d_49[4]}", file=sys.stderr)
    print(f"  Q56→Q57: signed={d_56[3]:+d}  |Δ|={d_56[4]}", file=sys.stderr)
    print(f"  primary PASS = {primary_pass}  "
          f"(abs_equal={abs_equal}, opposite_signs={opposite_signs}, "
          f"above_median={above_median})", file=sys.stderr)
    if largest_mirror:
        print(f"  largest mirrored |Δ| = {largest_mirror['abs_delta']} "
              f"at pairs {largest_mirror['pairs']}", file=sys.stderr)
    else:
        print(f"  NO MIRROR in this chronology.", file=sys.stderr)

# -----------------------------------------------------------------------------
# 5. Cross-chronology decision
# -----------------------------------------------------------------------------
passed = [n for n, r in results_per_chrono.items() if r['primary_test']['PASS']]
nol_pass = results_per_chrono['noldeke_1860']['primary_test']['PASS']
other_pass = [n for n in passed if n != 'noldeke_1860']

if nol_pass and not other_pass:
    verdict = ('NOLDEKE_ARTIFACT — mirror passes only under Nöldeke; '
               'not a robust architectural feature of the mushaf under alternative chronologies.')
elif nol_pass and len(other_pass) >= 1:
    if len(passed) == 4:
        verdict = ('UNIVERSAL_ARCHITECTURAL_FEATURE — primary passes under '
                   'all four chronologies.')
    else:
        verdict = (f'ROBUST_ARCHITECTURAL_FEATURE — primary passes under '
                   f'Nöldeke and {len(other_pass)} other chronology(ies): '
                   f'{other_pass}')
elif not nol_pass:
    verdict = ('UNEXPECTED — primary fails under Nöldeke; finding-config '
               'error (should not happen if data correct). Investigate.')
else:
    verdict = 'INDETERMINATE'

print(f"\nVERDICT: {verdict}", file=sys.stderr)
print(f"  Passed: {passed}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 6. Emit JSON
# -----------------------------------------------------------------------------
summary = {
    'finding_id': 'h-new-229',
    'title': 'Mirror-pair structure across chronologies',
    'date': '2026-04-17',
    'pre_reg_sha256': prereg_sha,
    'h212_source_sha256': h212_sha,
    'seed': SEED,
    'bonferroni_k': BONFERRONI_K,
    'rules_tuple': ('(113 consecutive mushaf pairs; signed Δ = rank(i+1) - rank(i); '
                    'strict mirror (±0 tolerance); above-median magnitude requirement; '
                    'Bell/Blachère ties resolved by mushaf-order ascending inherited '
                    'from H-NEW-212 pre-reg §5; Bell surah 15 rank imputed 52)'),
    'chronologies_tested': list(CHRONOS.keys()),
    'results_per_chronology': results_per_chrono,
    'chronologies_passing_primary': passed,
    'verdict': verdict,
    'references': {
        'parent_finding_h_new_142': 'findings/phase-b-hypotheses/h-new-142-universal-hinges-chrono-rhetorical.md',
        'parent_finding_h_new_158': 'findings/phase-b-hypotheses/h-new-158-mirror-pair-uniqueness.md',
        'inherited_chronology_script_h_new_212': 'scripts/h_new_212_alt_chronology_fisher_rao.py',
    },
}


def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    if isinstance(o, tuple):
        return [round_floats(v, n) for v in o]
    return o


OUT_JSON.write_text(json.dumps(round_floats(summary), indent=2, ensure_ascii=False))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
print(f"Pre-reg SHA-256: {prereg_sha}", file=sys.stderr)
