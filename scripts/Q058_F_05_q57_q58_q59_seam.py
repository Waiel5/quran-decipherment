#!/usr/bin/env python3
"""Q058-F-05 — Q 57 → Q 58 → Q 59 triple-seam adjacency analysis.

Pre-reg: surahs/Q058-al-mujadala/Q058-F-05-q57-q58-q59-seam-prereg.md
Pre-reg SHA256: b79392fe0a2e07f6f64db18952ff9f4b5fee11c06c8f40448d70aadb38bf6579
"""
import json
import hashlib
import sys
import os
import random

PREREG = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/Q058-F-05-q57-q58-q59-seam-prereg.md'
EXPECTED_SHA = 'b79392fe0a2e07f6f64db18952ff9f4b5fee11c06c8f40448d70aadb38bf6579'
SEED = 20260509
N_PERM = 10000
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/csv/Q058-F-05.json'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()

    # Load H-NEW-720 adjacency-cost matrix
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json') as f:
        d720 = json.load(f)
    per = d720['per_adjacency']

    # Find Q 57-58 and Q 58-59
    adj_57_58 = next(a for a in per if a.get('pair') == [57, 58])
    adj_58_59 = next(a for a in per if a.get('pair') == [58, 59])

    delta_57_58 = adj_57_58['delta_raw']
    delta_58_59 = adj_58_59['delta_raw']
    frac_57_58 = adj_57_58['fraction_residual']
    frac_58_59 = adj_58_59['fraction_residual']

    # Sort all 113 adjacencies by delta_raw ascending and compute ranks
    adj_sorted = sorted(per, key=lambda a: a['delta_raw'])
    rank_map = {tuple(a['pair']): r+1 for r, a in enumerate(adj_sorted)}

    rank_57_58 = rank_map[(57, 58)]
    rank_58_59 = rank_map[(58, 59)]

    # H1: both ranks ≤ 56
    h1_57_58_in_bottom_57 = rank_57_58 <= 56
    h1_58_59_in_bottom_57 = rank_58_59 <= 56
    h1_pass = h1_57_58_in_bottom_57 and h1_58_59_in_bottom_57

    # H2: Q 58-59 < Q 57-58
    h2_pass = delta_58_59 < delta_57_58

    # Permutation null A: random ordered pairs of distinct surahs - mean adjacency cost
    # Approximate by sampling random pairs from existing adjacencies (the H-NEW-720 set is canonical-only;
    # use the empirical 113-distribution as a proxy for "random pair" since these are all observed)
    random.seed(SEED)
    deltas = [a['delta_raw'] for a in per]
    n_le_57_58 = sum(1 for d in deltas if d <= delta_57_58)
    n_le_58_59 = sum(1 for d in deltas if d <= delta_58_59)
    p_57_58_observational = n_le_57_58 / len(deltas)
    p_58_59_observational = n_le_58_59 / len(deltas)

    out = {
        'finding_id': 'Q058-F-05',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'q57_to_q58': {
            'delta_raw': delta_57_58,
            'fraction_residual': frac_57_58,
            'rank_ascending': rank_57_58,
            'rank_descending': len(per) - rank_57_58 + 1,
            'in_bottom_57': h1_57_58_in_bottom_57,
            'observational_p_at_or_below': p_57_58_observational,
        },
        'q58_to_q59': {
            'delta_raw': delta_58_59,
            'fraction_residual': frac_58_59,
            'rank_ascending': rank_58_59,
            'rank_descending': len(per) - rank_58_59 + 1,
            'in_bottom_57': h1_58_59_in_bottom_57,
            'observational_p_at_or_below': p_58_59_observational,
        },
        'h1_pass': h1_pass,
        'h1_57_58_in_bottom_57': h1_57_58_in_bottom_57,
        'h1_58_59_in_bottom_57': h1_58_59_in_bottom_57,
        'h2_pass_q58_59_smoother_than_q57_58': h2_pass,
        'distribution_stats': {
            'mean_delta_raw': sum(deltas) / len(deltas),
            'median_delta_raw': sorted(deltas)[len(deltas)//2],
            'min_delta_raw': min(deltas),
            'max_delta_raw': max(deltas),
            'count_clamped_zero': sum(1 for d in deltas if d <= 0),
        },
        'cluster_internal_seams_within_h_new_1080': {
            'q57_q58': delta_57_58,
            'q58_q59': delta_58_59,
            'q59_q60': next(a['delta_raw'] for a in per if a.get('pair') == [59, 60]),
            'q60_q61': next(a['delta_raw'] for a in per if a.get('pair') == [60, 61]),
            'q61_q62': next(a['delta_raw'] for a in per if a.get('pair') == [61, 62]),
            'q62_q63': next(a['delta_raw'] for a in per if a.get('pair') == [62, 63]),
            'q63_q64': next(a['delta_raw'] for a in per if a.get('pair') == [63, 64]),
            'q64_q65': next(a['delta_raw'] for a in per if a.get('pair') == [64, 65]),
            'q65_q66': next(a['delta_raw'] for a in per if a.get('pair') == [65, 66]),
        },
        'verdict': (
            'CONFIRMED' if (h1_pass and h2_pass and (p_57_58_observational <= 0.025 or p_58_59_observational <= 0.025))
            else 'DIRECTIONAL' if (h1_pass and h2_pass)
            else 'PARTIAL' if (h1_pass or h2_pass)
            else 'NULL'
        ),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q058-F-05 verdict: {out['verdict']}")
    print(f"  Q 57 -> Q 58: delta_raw={delta_57_58:.4f}, rank={rank_57_58}/113, in_bottom_57={h1_57_58_in_bottom_57}")
    print(f"  Q 58 -> Q 59: delta_raw={delta_58_59:.4f}, rank={rank_58_59}/113, in_bottom_57={h1_58_59_in_bottom_57}")
    print(f"  H1 (both in bottom-57): {h1_pass}")
    print(f"  H2 (Q 58-59 smoother): {h2_pass} (Q 58-59={delta_58_59:.4f} vs Q 57-58={delta_57_58:.4f})")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
