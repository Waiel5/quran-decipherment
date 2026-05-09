#!/usr/bin/env python3
"""
Q049-F-02 — Q 49 etiquette-cluster Fisher-Rao cohesion test.
Pre-reg SHA: 8d8759bad9b42b9ccae37d40532e91767f41e609c6fc2dfdd902cf83214a9c59
Direction: POSITIVE — Q 49 mean FR distance to TARGET-SET = {Q 61, Q 62, Q 63, Q 64, Q 66}
hypothesized to be SIGNIFICANTLY BELOW permutation null over random 5-surah subsets.
Seed: 20260509
N permutations: 10000
"""

import json
import os
import random
import statistics

ROOT = '/Users/grey/Downloads/quran'
PRE_REG_SHA = '8d8759bad9b42b9ccae37d40532e91767f41e609c6fc2dfdd902cf83214a9c59'
SEED = 20260509
N_PERM = 10000
TARGET_SET = {61, 62, 63, 64, 66}
Q_SELF = 49

# Surahs with verse-count in [11, 22] (length-matched comparator pool)
# 22-verse limit chosen to span all 5 TARGET surahs' actual lengths {11, 11, 12, 14, 18}
LENGTH_MATCH_MIN = 11
LENGTH_MATCH_MAX = 22


def main():
    # Load Fisher-Rao matrix
    h111 = json.load(open(os.path.join(ROOT, 'findings', 'phase-b-hypotheses', 'csv', 'h-new-111.json')))
    D_list = h111['D_matrix_upper_triangular']

    # Build symmetric distance dict
    D = {}  # (a, b) -> distance with a < b
    for entry in D_list:
        i, j, d = entry[0], entry[1], entry[2]
        a, b = (i, j) if i < j else (j, i)
        D[(a, b)] = d

    def dist(a, b):
        a, b = (a, b) if a < b else (b, a)
        return D[(a, b)]

    # Load Quran data for verse-count lookup
    data = json.load(open(os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')))
    verse_counts = {s['id']: len(s['verses']) for s in data}

    # Observed: mean FR distance from Q 49 to TARGET_SET
    observed = statistics.mean(dist(Q_SELF, t) for t in TARGET_SET)

    # Q 49 mean to all 113
    all_others = [s for s in range(1, 115) if s != Q_SELF]
    mean_all = statistics.mean(dist(Q_SELF, s) for s in all_others)

    # Permutation null A: uniform sample 5 from all 113
    rng = random.Random(SEED)
    null_a = []
    for _ in range(N_PERM):
        sample = rng.sample(all_others, 5)
        null_a.append(statistics.mean(dist(Q_SELF, t) for t in sample))

    # Permutation null B: length-matched
    length_pool = [s for s in all_others if LENGTH_MATCH_MIN <= verse_counts[s] <= LENGTH_MATCH_MAX]
    null_b = []
    rng_b = random.Random(SEED + 1)
    for _ in range(N_PERM):
        sample = rng_b.sample(length_pool, min(5, len(length_pool)))
        null_b.append(statistics.mean(dist(Q_SELF, t) for t in sample))

    # p-values (one-sided, lower-tail)
    p_a = sum(1 for v in null_a if v <= observed) / N_PERM
    p_b = sum(1 for v in null_b if v <= observed) / N_PERM

    # Verdict
    pass_a = p_a <= 0.05
    pass_b = p_b <= 0.05
    if pass_a and pass_b:
        verdict = 'CONFIRMED-PAIR (PASS-DIRECTED ceiling per garden-of-forking-paths)'
    elif pass_a or pass_b:
        verdict = 'PARTIAL'
    else:
        verdict = 'NULL'

    result = {
        'finding_id': 'Q049-F-02',
        'pre_reg_sha256': PRE_REG_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'target_set': sorted(TARGET_SET),
        'rules_tuple': '(QAC-v0.4-roots-via-h-new-111, no-tashkeel, FR-distance-from-h-new-111)',
        'q49_mean_to_target_set': observed,
        'q49_mean_to_all_113': mean_all,
        'ratio_observed_to_corpus_mean': observed / mean_all,
        'null_a_uniform': {
            'mean': statistics.mean(null_a),
            'stdev': statistics.stdev(null_a),
            'p_one_sided_lower': p_a,
        },
        'null_b_length_matched': {
            'pool_size': len(length_pool),
            'pool_verse_count_range': [LENGTH_MATCH_MIN, LENGTH_MATCH_MAX],
            'mean': statistics.mean(null_b),
            'stdev': statistics.stdev(null_b),
            'p_one_sided_lower': p_b,
        },
        'pass_a_uniform': pass_a,
        'pass_b_length_matched': pass_b,
        'verdict': verdict,
        'verdict_ceiling_note': 'PASS-DIRECTED — TARGET-SET pre-extracted from Q 49 top-5 FR neighbors prior to pre-reg lock; verdict ceiling is PASS-DIRECTED per garden-of-forking-paths until independent replication (e.g., on H-NEW-111b char-4-gram matrix).',
    }

    out_path = os.path.join(ROOT, 'surahs', 'Q049-al-hujurat', 'csv', 'Q049-F-02.json')
    with open(out_path, 'w') as f:
        json.dump(result, f, indent=2)

    print(f'Q049-F-02 verdict: {verdict}')
    print(f'  Q 49 mean FR to TARGET-SET {sorted(TARGET_SET)}: {observed:.4f}')
    print(f'  Q 49 mean FR to all 113:                  {mean_all:.4f}')
    print(f'  Null A (uniform 5-of-113): mean={statistics.mean(null_a):.4f} p_lower={p_a:.4f}')
    print(f'  Null B (length-matched 5 from {len(length_pool)}): mean={statistics.mean(null_b):.4f} p_lower={p_b:.4f}')


if __name__ == '__main__':
    main()
