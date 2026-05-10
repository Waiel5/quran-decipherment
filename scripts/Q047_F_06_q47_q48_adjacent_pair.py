#!/usr/bin/env python3
"""
Q047-F-06 — Q 47 ↔ Q 48 adjacent-pair cohesion (in_all_three via H-NEW-130 family) + FR pair-rank.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q047-muhammad/Q047-F-06-q47-q48-adjacent-pair-prereg.md
Pre-reg SHA256: 3b74c07902f7e50f4630a5ca6c48e836e00921f38222f83296082b90fc53dc72

Rules-tuple: (no-tashkeel, QAC-stem-root + char-4gram + verse-length-histogram, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""

import json
import hashlib
import sys
from pathlib import Path

PROJECT = Path('/Users/grey/Downloads/quran')
PREREG = PROJECT / 'surahs/Q047-muhammad/Q047-F-06-q47-q48-adjacent-pair-prereg.md'
EXPECTED_SHA = '3b74c07902f7e50f4630a5ca6c48e836e00921f38222f83296082b90fc53dc72'
OUT = PROJECT / 'surahs/Q047-muhammad/csv/Q047-F-06.json'
SEED = 20260509


def verify_prereg_sha():
    with open(PREREG, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != EXPECTED_SHA:
        sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {h}')
    print(f'[OK] pre-reg SHA verified: {h}')


def fr_idx(i, j, n=114):
    if i > j:
        i, j = j, i
    i -= 1
    j -= 1
    return i * (n - 1) - i * (i - 1) // 2 + (j - i - 1)


def main():
    verify_prereg_sha()
    # Load h-new-130 family
    def load(name):
        p = PROJECT / f'findings/phase-b-hypotheses/csv/{name}.json'
        with open(p, encoding='utf-8') as f:
            return json.load(f)

    h130 = load('h-new-130')
    h130b = load('h-new-130b')
    h130c = load('h-new-130c')

    cmd_root = h130['consecutive_mushaf_distances']
    cmd_char = h130b['consecutive_mushaf_distances_char4gram']
    cmd_verse = h130c['consecutive_mushaf_distances_verselen']

    # Test A: Q 47-Q 48 in bottom-15 (cheapest) consecutive adjacencies in all 3 D-matrices
    def bottom_n(cmd, n=15):
        return [k for k, v in sorted(cmd.items(), key=lambda x: x[1])[:n]]

    def rank_low(cmd, pair):
        ranked = sorted(cmd.items(), key=lambda x: x[1])
        return next(i for i, (k, _) in enumerate(ranked, 1) if k == pair)

    pair = '47-48'
    bot15_root = bottom_n(cmd_root, 15)
    bot15_char = bottom_n(cmd_char, 15)
    bot15_verse = bottom_n(cmd_verse, 15)

    in_bot_root = pair in bot15_root
    in_bot_char = pair in bot15_char
    in_bot_verse = pair in bot15_verse
    in_all_three = in_bot_root and in_bot_char and in_bot_verse

    rank_root = rank_low(cmd_root, pair)
    rank_char = rank_low(cmd_char, pair)
    rank_verse = rank_low(cmd_verse, pair)

    # Test B: Q 47-Q 48 FR pair-rank in bottom quartile (rank ≤ 1610 of 6441)
    h111 = load('h-new-111')
    matrix = h111['D_matrix_upper_triangular']  # list of [i, j, distance]
    sorted_pairs = sorted(matrix, key=lambda x: x[2])
    pair_rank = next(i for i, rec in enumerate(sorted_pairs, 1)
                     if (rec[0] == 47 and rec[1] == 48) or (rec[0] == 48 and rec[1] == 47))
    pair_dist = next(rec[2] for rec in matrix
                     if (rec[0] == 47 and rec[1] == 48) or (rec[0] == 48 and rec[1] == 47))
    total_pairs = len(matrix)
    pair_percentile_low = pair_rank / total_pairs

    test_B_pass = pair_rank <= total_pairs / 4  # bottom quartile
    test_B_strict = pair_rank <= total_pairs * 0.025  # alpha-corrected
    test_A_pass = in_all_three

    # verdict
    if test_A_pass and test_B_strict:
        verdict = 'VINDICATED-FULL'
    elif test_A_pass or test_B_strict:
        verdict = 'VINDICATED-PARTIAL'
    elif test_B_pass:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    # nearest 10 FR neighbors of Q 47
    def dist_47(j):
        for rec in matrix:
            if (rec[0] == 47 and rec[1] == j) or (rec[0] == j and rec[1] == 47):
                return rec[2]
        return None

    neighbors = sorted([(j, dist_47(j)) for j in range(1, 115) if j != 47], key=lambda x: x[1])

    out = {
        'test_id': 'Q047-F-06',
        'pre_reg_sha': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': '(no-tashkeel, QAC-stem-root + char-4gram + verse-length-histogram, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'pair': 'Q47-Q48',
        'test_A_in_all_three_bottom15_cohesive': {
            'h-new-130_root': {
                'Q47-Q48_distance': cmd_root[pair],
                'rank_low': rank_root,
                'in_bottom_15': in_bot_root,
                'bottom_15_set': bot15_root,
            },
            'h-new-130b_char4gram': {
                'Q47-Q48_distance': cmd_char[pair],
                'rank_low': rank_char,
                'in_bottom_15': in_bot_char,
                'bottom_15_set': bot15_char,
            },
            'h-new-130c_verselen': {
                'Q47-Q48_distance': cmd_verse[pair],
                'rank_low': rank_verse,
                'in_bottom_15': in_bot_verse,
                'bottom_15_set': bot15_verse,
            },
            'in_all_three_cohesive_bottom_15': in_all_three,
            'test_A_pass': test_A_pass,
        },
        'test_B_FR_pair_rank': {
            'pair_distance': pair_dist,
            'pair_rank_low_of_6441': pair_rank,
            'total_pairs': total_pairs,
            'percentile_low': pair_percentile_low,
            'bottom_quartile_threshold_rank_1610': total_pairs // 4,
            'bottom_2_5pct_threshold_rank': int(total_pairs * 0.025),
            'test_B_pass_quartile': test_B_pass,
            'test_B_pass_strict_alpha': test_B_strict,
        },
        'Q47_nearest_10_FR_neighbors': [{'surah': j, 'fr': d} for j, d in neighbors[:10]],
        'verdict': verdict,
        'bonferroni_k': 2,
        'alpha_bon': 0.025,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'[OK] wrote {OUT}')
    print(f'  Test A in_all_three (bottom-15 cohesive): {in_all_three}')
    print(f'  Test A ranks: root={rank_root}, char={rank_char}, verse={rank_verse}')
    print(f'  Test B FR-pair rank: {pair_rank}/{total_pairs} ({pair_percentile_low:.4f})')
    print(f'  Test B pass quartile? {test_B_pass}; pass strict? {test_B_strict}')
    print(f'  Verdict: {verdict}')


if __name__ == '__main__':
    main()
