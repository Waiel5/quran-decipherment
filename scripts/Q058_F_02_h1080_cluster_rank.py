#!/usr/bin/env python3
"""Q058-F-02 — Q 58 within H-NEW-1080 short-Medinan-block FR centrality rank.

Pre-reg: surahs/Q058-al-mujadala/Q058-F-02-h1080-cluster-rank-prereg.md
Pre-reg SHA256: d28198ad222fdee67c61a73b9b1055f130259122d4c689cbece9f02b74fea2ee
"""
import json
import hashlib
import sys
import os
import random

PREREG = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/Q058-F-02-h1080-cluster-rank-prereg.md'
EXPECTED_SHA = 'd28198ad222fdee67c61a73b9b1055f130259122d4c689cbece9f02b74fea2ee'
SEED = 20260509
N_PERM = 10000
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/csv/Q058-F-02.json'

CLUSTER = list(range(57, 67))  # H-NEW-1080: Q 57-66


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def load_fr_matrix():
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json') as f:
        d = json.load(f)
    n = 114
    D = [[0.0] * n for _ in range(n)]
    for entry in d['D_matrix_upper_triangular']:
        i, j, dist = entry
        D[i-1][j-1] = dist
        D[j-1][i-1] = dist
    return D


def main():
    verify_sha()
    D = load_fr_matrix()
    n = 114

    # H1: cluster centrality rank
    cluster_means = []
    for a in CLUSTER:
        md = sum(D[a-1][b-1] for b in CLUSTER if b != a) / (len(CLUSTER) - 1)
        cluster_means.append((a, md))
    cluster_means_sorted = sorted(cluster_means, key=lambda x: x[1])
    q58_centrality_rank = next(r+1 for r, (sid, _) in enumerate(cluster_means_sorted) if sid == 58)
    q58_intra_mean = next(md for sid, md in cluster_means if sid == 58)

    h1_pass = q58_centrality_rank in {4, 5, 6, 7, 8}

    # H2: corpus-NN ∈ {Q 57-66}
    q58_idx = 57
    neighbors = sorted([(j+1, D[q58_idx][j]) for j in range(n) if j != q58_idx], key=lambda x: x[1])
    nn_sid, nn_dist = neighbors[0]
    h2_pass = nn_sid in CLUSTER

    # Permutation null A: random 10-subsets containing Q 58
    random.seed(SEED)
    others = [s for s in range(1, 115) if s != 58]
    n_lower = 0
    for _ in range(N_PERM):
        sub = random.sample(others, 9) + [58]
        sub_mean = sum(D[58-1][b-1] for b in sub if b != 58) / 9
        if sub_mean <= q58_intra_mean:
            n_lower += 1
    p_null_A = (n_lower + 1) / (N_PERM + 1)

    # Top-15 nearest neighbors output
    top_15 = [{'rank': r, 'sid': sid, 'fr': dist} for r, (sid, dist) in enumerate(neighbors[:15], 1)]
    farthest_5 = [{'sid': sid, 'fr': dist} for sid, dist in neighbors[-5:]]

    # All cluster intra-pairs
    intra_pairs = []
    for i, a in enumerate(CLUSTER):
        for b in CLUSTER[i+1:]:
            intra_pairs.append({'a': a, 'b': b, 'fr': D[a-1][b-1]})
    intra_pairs_sorted = sorted(intra_pairs, key=lambda x: x['fr'])

    out = {
        'finding_id': 'Q058-F-02',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'cluster_definition': CLUSTER,
        'cluster_size': len(CLUSTER),
        'q58_centrality_rank': q58_centrality_rank,
        'q58_intra_cluster_mean_fr': q58_intra_mean,
        'cluster_centrality_ranking': [{'rank': r+1, 'sid': sid, 'mean_fr': md} for r, (sid, md) in enumerate(cluster_means_sorted)],
        'h1_pass': h1_pass,
        'h1_predicted_range': '[4, 8]',
        'q58_corpus_nearest_neighbor': {'sid': nn_sid, 'fr': nn_dist},
        'q58_corpus_nearest_in_cluster': h2_pass,
        'h2_pass': h2_pass,
        'q58_top_15_corpus_neighbors': top_15,
        'q58_farthest_5_corpus': farthest_5,
        'q58_mean_dist_to_all_113': sum(d for _, d in neighbors) / len(neighbors),
        'cluster_intra_pairs_sorted': intra_pairs_sorted,
        'cluster_mean_pairwise_fr': sum(p['fr'] for p in intra_pairs) / len(intra_pairs),
        'permutation_null_A': {
            'n_random_subset_means_lower_or_equal': n_lower,
            'p_value': p_null_A,
            'description': 'fraction of random 10-subsets containing Q 58 with mean FR <= observed cluster mean',
        },
        'verdict': (
            'CONFIRMED' if (h1_pass and h2_pass and p_null_A <= 0.025)
            else 'DIRECTIONAL' if (h1_pass and h2_pass)
            else 'PARTIAL' if (h1_pass or h2_pass)
            else 'NULL'
        ),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q058-F-02 verdict: {out['verdict']}")
    print(f"  H1 cluster centrality rank: {q58_centrality_rank}/10 (pass={h1_pass}, range={out['h1_predicted_range']})")
    print(f"  H2 corpus-NN: Q {nn_sid} (FR={nn_dist:.4f}); in_cluster={h2_pass}")
    print(f"  Perm-null A p-value: {p_null_A:.4f}")
    print(f"  Q 58 mean intra-cluster FR: {q58_intra_mean:.4f}")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
