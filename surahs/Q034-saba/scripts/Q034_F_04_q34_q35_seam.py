#!/usr/bin/env python3
"""Q034-F-04 — Q 34 -> Q 35 mushaf-adjacency seam LOW-cost test.

Pre-reg: surahs/Q034-saba/preregs/Q034-F-04-q34-q35-seam-prereg.md
Pre-reg SHA256: 6f2d39c93528655fb7bf01f93b458cfab3bdedfdd61a27289127b13d1c415333
Rules-tuple: (no-tashkeel, QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

H1: rank of Q34->Q35 in delta_raw ascending is <= 20 / 113 (top-20 smoothest).
H2: cost(Q34->Q35) < median of {cost(Q1->Q2), cost(Q5->Q6), cost(Q17->Q18), cost(Q33->Q34), cost(Q34->Q35)}.
H3: FR(Q34, Q35) < median of 10 intra-cluster pairs.
Bonferroni k=3, alpha_bon=0.01667.
"""
import json, hashlib, sys, os, statistics

PREREG = '/Users/grey/Downloads/quran/surahs/Q034-saba/preregs/Q034-F-04-q34-q35-seam-prereg.md'
EXPECTED_SHA = '6f2d39c93528655fb7bf01f93b458cfab3bdedfdd61a27289127b13d1c415333'
SEED = 20260509
ALPHA_BON = 0.05 / 3


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    # Load adjacency data
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json') as f:
        d720 = json.load(f)
    pa = d720['per_adjacency']

    # Find rank of Q34->Q35 in ascending delta_raw
    pa_sorted = sorted(pa, key=lambda e: e['delta_raw'])
    rank_seam = None
    delta_q34_q35 = None
    for rk, e in enumerate(pa_sorted, 1):
        if e['pair'] == [34, 35]:
            rank_seam = rk
            delta_q34_q35 = e['delta_raw']
            break

    h1_pass = rank_seam is not None and rank_seam <= 20

    # H2: 5 openers' transition-to-mushaf-successor cost
    # opener -> successor: 1->2, 6->7, 18->19, 34->35
    # NOTE: brief says "the 5 transitions involving the al-hamd cluster's 4 non-Q1-special members"
    # Use opener-into-next-surah: Q1->Q2, Q6->Q7, Q18->Q19, Q34->Q35
    # And the predecessor-of-Q35: Q34->Q35 (counted once)
    # Pre-reg specifies: {Q1->Q2, Q5->Q6, Q17->Q18, Q33->Q34, Q34->Q35}
    targets = [[1,2], [5,6], [17,18], [33,34], [34,35]]
    costs = {}
    for e in pa:
        for t in targets:
            if e['pair'] == t:
                costs[tuple(t)] = e['delta_raw']
    cost_values = list(costs.values())
    median_5 = statistics.median(cost_values) if cost_values else None
    h2_pass = (delta_q34_q35 is not None) and (median_5 is not None) and (delta_q34_q35 < median_5)

    # H3: FR(Q34, Q35) vs median of 10 intra-cluster pairs
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json') as f:
        d111 = json.load(f)
    ut = d111['D_matrix_upper_triangular']
    N = 114
    mat = [[0.0]*N for _ in range(N)]
    for entry in ut:
        i, j, v = entry
        mat[i-1][j-1] = v
        mat[j-1][i-1] = v
    cluster = [1, 6, 18, 34, 35]
    intra_dists = []
    for i, s1 in enumerate(cluster):
        for s2 in cluster[i+1:]:
            intra_dists.append((s1, s2, mat[s1-1][s2-1]))
    median_intra = statistics.median([d for _,_,d in intra_dists])
    d_q34_q35 = mat[33][34]
    h3_pass = d_q34_q35 < median_intra

    n_pass = sum([h1_pass, h2_pass, h3_pass])
    if n_pass == 3: verdict = 'CONFIRMED'
    elif n_pass == 2: verdict = 'DIRECTIONAL'
    elif n_pass == 1: verdict = 'DIRECTIONAL-WEAK'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q034-F-04',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'seed': SEED,
        'alpha_bon': ALPHA_BON,
        'h1_seam_rank': {
            'delta_q34_q35': delta_q34_q35,
            'rank': rank_seam,
            'top20_threshold': 20,
            'pass': h1_pass,
        },
        'h2_opener_median_cost': {
            'targets': [{'pair': list(k), 'delta_raw': v} for k, v in costs.items()],
            'median_5': median_5,
            'delta_q34_q35': delta_q34_q35,
            'pass': h2_pass,
        },
        'h3_intra_cluster_fr_median': {
            'cluster': cluster,
            'intra_pairs': [{'pair': [s1, s2], 'fr': d} for s1, s2, d in intra_dists],
            'median_intra': median_intra,
            'd_q34_q35': d_q34_q35,
            'pass': h3_pass,
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'Pre-flight: rank_seam=65/113 (NOT top-20); H1 will FAIL with full prominence. H3 likely passes (Q34-Q35 below intra-median 0.97). Net verdict probably DIRECTIONAL-WEAK or NULL — honest empirical refinement of al-Biqaʾi nażm claim.',
    }

    print('=== Q034-F-04 Q34->Q35 seam test ===')
    print(f'H1: delta_q34_q35={delta_q34_q35:.4f}, rank={rank_seam}/113, threshold=top-20 -> pass={h1_pass}')
    print(f'H2: median_5={median_5:.4f}, q34-q35={delta_q34_q35:.4f} -> pass={h2_pass}')
    print(f'H3: median_intra={median_intra:.4f}, d_q34_q35={d_q34_q35:.4f} -> pass={h3_pass}')
    print(f'\nN pass: {n_pass}/3 -> {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q034-saba/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q034-saba/csv/Q034-F-04.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
