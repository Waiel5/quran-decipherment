#!/usr/bin/env python3
"""Q030-F-04 — Q 29 ↔ Q 30 architectural-twin signature (FR distance within ALM cluster).

Pre-reg: surahs/Q030-al-rum/Q030-F-04-architectural-twin-prereg.md
Pre-reg SHA256: c92548471c002b18f89b5fbf232c38167e88cc545709143946de55bb32902383
Rules-tuple: re-uses h-new-111 locked artifact (FR-roots distance matrix)
"""
import json, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/Q030-F-04-architectural-twin-prereg.md'
EXPECTED_SHA = 'c92548471c002b18f89b5fbf232c38167e88cc545709143946de55bb32902383'
H111 = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'

ALM = [2, 3, 29, 30, 31, 32]


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    with open(H111) as f:
        d = json.load(f)
    rows = d['D_matrix_upper_triangular']
    N = 114
    D = [[0.0] * N for _ in range(N)]
    for row in rows:
        i, j, dist = row
        if isinstance(i, str): i = int(i)
        if isinstance(j, str): j = int(j)
        D[i - 1][j - 1] = float(dist)
        D[j - 1][i - 1] = float(dist)

    # ALM-cluster pairwise distances
    pairs_alm = []
    for i in range(len(ALM)):
        for j in range(i + 1, len(ALM)):
            a, b = ALM[i], ALM[j]
            pairs_alm.append({'a': a, 'b': b, 'd': D[a - 1][b - 1]})

    pairs_sorted = sorted(pairs_alm, key=lambda x: x['d'])
    q29_q30 = next(p for p in pairs_alm if {p['a'], p['b']} == {29, 30})
    rank_alm = next(i for i, p in enumerate(pairs_sorted, 1) if {p['a'], p['b']} == {29, 30})
    median_alm = sorted([p['d'] for p in pairs_alm])[len(pairs_alm) // 2]
    mean_alm = sum(p['d'] for p in pairs_alm) / len(pairs_alm)

    # Corpus-wide percentile of d(29,30)
    corpus_pairs = []
    for i in range(N):
        for j in range(i + 1, N):
            corpus_pairs.append(D[i][j])
    n_below = sum(1 for d in corpus_pairs if d < q29_q30['d'])
    pct_corpus = 100 * n_below / len(corpus_pairs)

    # Mushaf-adjacency control: rank d(29,30) in {d(s,s+1) for s=1..113}
    adjacency = []
    for s in range(1, N):
        adjacency.append({'pair': (s, s + 1), 'd': D[s - 1][s]})
    adj_sorted = sorted(adjacency, key=lambda x: x['d'])
    rank_adj = next(i for i, p in enumerate(adj_sorted, 1) if p['pair'] == (29, 30))
    median_adj = sorted([p['d'] for p in adjacency])[len(adjacency) // 2]

    # Verdict
    if rank_alm <= 3:
        primary_verdict = 'STRONG-DIRECTED'
    elif rank_alm <= 7:
        primary_verdict = 'DIRECTED'
    else:
        primary_verdict = 'NULL'

    if pct_corpus <= 5:
        secondary_verdict = 'STRONG-DIRECTIONAL'
    elif pct_corpus <= 25:
        secondary_verdict = 'WEAK-DIRECTIONAL'
    elif pct_corpus > 50:
        secondary_verdict = 'NULL'
    else:
        secondary_verdict = 'WEAK-DIRECTIONAL'

    out = {
        'finding_id': 'Q030-F-04',
        'prereg_sha': EXPECTED_SHA,
        'data_source': 'h-new-111 (FR-roots distance matrix)',
        'd_q29_q30': q29_q30['d'],
        'within_ALM_cluster': {
            'pairs_sorted_ascending': pairs_sorted,
            'rank_q29_q30_in_15': rank_alm,
            'median_alm': median_alm,
            'mean_alm': mean_alm,
            'rank_p_one_sided': rank_alm / 15,
        },
        'corpus_wide': {
            'n_pairs': len(corpus_pairs),
            'pct_below_q29q30': pct_corpus,
        },
        'mushaf_adjacency_control': {
            'rank_q29_q30_in_113_adjacencies': rank_adj,
            'median_adjacency': median_adj,
            'pct_in_adjacency': 100 * (rank_adj - 1) / len(adjacency),
        },
        'primary_verdict': primary_verdict,
        'secondary_verdict': secondary_verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv/Q030-F-04.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q030-F-04 results:")
    print(f"  d(Q29, Q30) FR-roots = {q29_q30['d']:.6f}")
    print(f"  Rank within ALM-15-pairs: {rank_alm}/15 (median {median_alm:.6f})")
    print(f"  Corpus-wide percentile: {pct_corpus:.2f}% (n={len(corpus_pairs)})")
    print(f"  Mushaf-adjacency rank (1=closest): {rank_adj}/113")
    print(f"  Primary verdict: {primary_verdict}")
    print(f"  Secondary verdict: {secondary_verdict}")


if __name__ == '__main__':
    main()
