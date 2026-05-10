#!/usr/bin/env python3
"""Q034-F-05 — 5-opener sequential-pair FR distances; Q34<->Q35 tightest pair test.

Pre-reg: surahs/Q034-saba/preregs/Q034-F-05-opener-pair-distances-prereg.md
Pre-reg SHA256: 83414986ef57bbeeff090b9e57ec0f0ee0ccabe82a6a67c43b835cccbfd928e3
Rules-tuple: (no-tashkeel, QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

H1: Among the 4 sequential opener-pairs ((1,6),(6,18),(18,34),(34,35)), (34,35) has the MINIMUM FR.
H2: D[Q34,Q35] percentile <= 50 (bottom half of corpus pairs).
Bonferroni k=2, alpha_bon=0.025.
"""
import json, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q034-saba/preregs/Q034-F-05-opener-pair-distances-prereg.md'
EXPECTED_SHA = '83414986ef57bbeeff090b9e57ec0f0ee0ccabe82a6a67c43b835cccbfd928e3'
SEED = 20260509
ALPHA_BON = 0.05 / 2


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json') as f:
        d111 = json.load(f)
    ut = d111['D_matrix_upper_triangular']
    N = 114
    mat = [[0.0]*N for _ in range(N)]
    for entry in ut:
        i, j, v = entry
        mat[i-1][j-1] = v
        mat[j-1][i-1] = v

    seq_pairs = [(1,6), (6,18), (18,34), (34,35)]
    seq_dists = [(a, b, mat[a-1][b-1]) for a, b in seq_pairs]
    seq_sorted = sorted(seq_dists, key=lambda x: x[2])
    tightest_pair = (seq_sorted[0][0], seq_sorted[0][1])
    h1_pass = tightest_pair == (34, 35)
    rank_q34_q35_in_seq = next((rk for rk, (a, b, _) in enumerate(seq_sorted, 1) if (a, b) == (34, 35)), None)

    # H2: all-pair percentile
    all_pairs = []
    for i in range(N):
        for j in range(i+1, N):
            all_pairs.append(mat[i][j])
    all_sorted = sorted(all_pairs)
    d_q34_q35 = mat[33][34]
    rank_q34_q35 = sum(1 for p in all_sorted if p < d_q34_q35) + 1
    percentile = 100.0 * rank_q34_q35 / len(all_sorted)
    h2_pass = percentile <= 50

    n_pass = sum([h1_pass, h2_pass])
    if n_pass == 2: verdict = 'CONFIRMED'
    elif n_pass == 1: verdict = 'DIRECTIONAL'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q034-F-05',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'seed': SEED,
        'alpha_bon': ALPHA_BON,
        'h1_sequential_minimum': {
            'pairs': [{'pair': [a, b], 'fr': d} for a, b, d in seq_dists],
            'sorted_ranking': [{'rank': rk, 'pair': [a, b], 'fr': d} for rk, (a, b, d) in enumerate(seq_sorted, 1)],
            'tightest_pair': list(tightest_pair),
            'q34_q35_rank_in_sequential': rank_q34_q35_in_seq,
            'pass': h1_pass,
        },
        'h2_all_pair_percentile': {
            'd_q34_q35': d_q34_q35,
            'rank_of_6441': rank_q34_q35,
            'percentile': percentile,
            'threshold': 50,
            'pass': h2_pass,
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'Pre-flight: Q18-Q34 is the tightest sequential pair (FR=0.8984), Q34-Q35 is rank 2 (FR=0.9268). H1 FAILS. H2 PASSES (Q34-Q35 percentile 42.73%). Net verdict = DIRECTIONAL.',
    }

    print('=== Q034-F-05 opener-pair distances ===')
    print('Sequential pair ranking:')
    for rk, (a, b, d) in enumerate(seq_sorted, 1):
        print(f'  rank {rk}: Q{a}<->Q{b} = {d:.4f}')
    print(f'H1: tightest pair = Q{tightest_pair[0]}<->Q{tightest_pair[1]}; pass(==34<->35)? {h1_pass}')
    print(f'H2: D[Q34,Q35]={d_q34_q35:.4f}, percentile={percentile:.2f}%, threshold<=50% -> pass={h2_pass}')
    print(f'\nN pass: {n_pass}/2 -> {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q034-saba/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q034-saba/csv/Q034-F-05.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
