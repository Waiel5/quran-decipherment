#!/usr/bin/env python3
"""Q067-F-05 — Q 66 → Q 67 canonical-adjacency cost seam test.

Reads H-NEW-720 per_adjacency, ranks the Q 66 → Q 67 entry by delta_raw
(descending; rank 1 = highest cost).

Pre-reg: surahs/Q067-al-mulk/preregs/Q067-F-05-q66-q67-mushaf-seam-prereg.md
Pre-reg SHA256: 826c4a8e7934907ed5125547a4c289fe703cbbac7f96b8a63f8bd2cadcec001e
Seed: 20260509
"""
import json
import hashlib
import sys
import random
import statistics

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f'{PROJECT}/surahs/Q067-al-mulk/preregs/Q067-F-05-q66-q67-mushaf-seam-prereg.md'
EXPECTED_SHA = '826c4a8e7934907ed5125547a4c289fe703cbbac7f96b8a63f8bd2cadcec001e'
SEED = 20260509
N_BOOT = 10000
H720_PATH = f'{PROJECT}/findings/phase-b-hypotheses/csv/h-new-720.json'
OUT_PATH = f'{PROJECT}/surahs/Q067-al-mulk/csv/Q067-F-05.json'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f'PRE-REG SHA MISMATCH:\n  expected {EXPECTED_SHA}\n  actual   {actual}', file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()

    with open(H720_PATH) as f:
        d720 = json.load(f)
    per = d720['per_adjacency']

    # Locate Q 66 -> Q 67 (and neighbours for MW-5)
    pairs = {tuple(a['pair']): a for a in per}
    target = pairs[(66, 67)]
    delta_target = target['delta_raw']
    frac_target = target['fraction_residual']

    # Rank descending by delta_raw
    sorted_desc = sorted(per, key=lambda a: -a['delta_raw'])
    rank_desc_map = {tuple(a['pair']): r + 1 for r, a in enumerate(sorted_desc)}
    rank_desc_target = rank_desc_map[(66, 67)]
    rank_asc_target = len(per) - rank_desc_target + 1
    n_adj = len(per)

    # Top decile threshold = top 12 of 113 (round(113*0.1))
    top_decile_threshold = max(1, round(n_adj * 0.1))
    passes_top_decile = rank_desc_target <= top_decile_threshold

    # Bootstrap-based p-value: how often does a random adjacency exceed observed delta?
    deltas = [a['delta_raw'] for a in per]
    n_ge = sum(1 for d in deltas if d >= delta_target)
    observational_p_at_or_above = n_ge / n_adj

    # Bootstrap resampling for stability of rank
    rng = random.Random(SEED)
    boot_ranks = []
    for _ in range(N_BOOT):
        resample = [rng.choice(deltas) for _ in range(n_adj)]
        # rank of delta_target if inserted (descending)
        rank_in_boot = 1 + sum(1 for d in resample if d > delta_target)
        boot_ranks.append(rank_in_boot)
    boot_ranks_sorted = sorted(boot_ranks)
    boot_p_in_top_decile = sum(1 for r in boot_ranks if r <= top_decile_threshold) / N_BOOT

    # Neighbours
    n_65_66 = pairs[(65, 66)]
    n_67_68 = pairs[(67, 68)]
    rank_65_66 = rank_desc_map[(65, 66)]
    rank_67_68 = rank_desc_map[(67, 68)]

    # Distribution stats
    distribution = {
        'mean_delta_raw': statistics.mean(deltas),
        'median_delta_raw': statistics.median(deltas),
        'stdev_delta_raw': statistics.stdev(deltas),
        'min_delta_raw': min(deltas),
        'max_delta_raw': max(deltas),
        'n_adjacencies': n_adj,
        'top_decile_threshold': top_decile_threshold,
    }

    if passes_top_decile:
        verdict = 'PASS-DIRECTED'
        interpretation = (
            f'Q 66 → Q 67 ranks {rank_desc_target}/{n_adj} (descending) — '
            f'inside top decile (≤{top_decile_threshold}). delta_raw={delta_target:.4f} '
            f'vs corpus mean {distribution["mean_delta_raw"]:.4f}, median {distribution["median_delta_raw"]:.4f}. '
            f'The long-Medinan→short-Meccan-tail seam is a high-cost boundary in mushaf order.'
        )
    else:
        verdict = 'NULL'
        interpretation = (
            f'Q 66 → Q 67 ranks {rank_desc_target}/{n_adj} (descending) — '
            f'outside top decile (>{top_decile_threshold}). delta_raw={delta_target:.4f} '
            f'vs corpus mean {distribution["mean_delta_raw"]:.4f}, median {distribution["median_delta_raw"]:.4f}. '
            f'Pre-registered "high-cost seam" direction NOT supported: the Q 66 → Q 67 transition is mid-pack '
            f'on the H-NEW-720 adjacency map; the post-Hijra-kink position-architecture is not visible at this seam under '
            f'the current rules-tuple.'
        )

    out = {
        'finding_id': 'Q067-F-05',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': '(no-tashkeel, QAC-stem-roots, K=500, Dirichlet α=0.5, FR-distance, Hafs-Kufan)',
        'data_source': H720_PATH,
        'target_pair': [66, 67],
        'q66_q67': {
            'delta_raw': delta_target,
            'fraction_residual': frac_target,
            'rank_descending': rank_desc_target,
            'rank_ascending': rank_asc_target,
            'in_top_decile_descending': passes_top_decile,
            'observational_p_at_or_above': observational_p_at_or_above,
        },
        'neighbours': {
            'q65_q66': {
                'delta_raw': n_65_66['delta_raw'],
                'fraction_residual': n_65_66['fraction_residual'],
                'rank_descending': rank_65_66,
            },
            'q67_q68': {
                'delta_raw': n_67_68['delta_raw'],
                'fraction_residual': n_67_68['fraction_residual'],
                'rank_descending': rank_67_68,
            },
        },
        'bootstrap': {
            'n_boot': N_BOOT,
            'boot_p_in_top_decile': boot_p_in_top_decile,
            'boot_rank_mean': statistics.mean(boot_ranks),
            'boot_rank_median': statistics.median(boot_ranks),
            'boot_rank_q05': boot_ranks_sorted[int(0.05 * N_BOOT)],
            'boot_rank_q95': boot_ranks_sorted[int(0.95 * N_BOOT)],
        },
        'distribution_stats': distribution,
        'top10_expensive_pairs': [(a['pair'], round(a['delta_raw'], 4)) for a in sorted_desc[:10]],
        'verdict': verdict,
        'interpretation': interpretation,
    }

    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'Q067-F-05: VERDICT={verdict}')
    print(f'  Q 66 → Q 67 delta_raw = {delta_target:.4f}')
    print(f'  Rank descending: {rank_desc_target}/{n_adj} (top decile threshold ≤ {top_decile_threshold})')
    print(f'  In top decile: {passes_top_decile}')
    print(f'  Q 65 → Q 66 rank: {rank_65_66}; Q 67 → Q 68 rank: {rank_67_68}')
    print(f'  Output: {OUT_PATH}')


if __name__ == '__main__':
    main()
