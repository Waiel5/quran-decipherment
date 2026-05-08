#!/usr/bin/env python3
"""Q037-F-04 — Q 37 oath-cluster membership extension on H-NEW-1070.

Pre-reg: surahs/Q037-al-saffat/Q037-F-04-oath-cluster-membership-prereg.md
Pre-reg SHA256: d4e9e449d1655a0632f8d19b18b13710a447c372f2a5bae0d41e7e04e2d2bda1
Rules-tuple: (no-tashkeel, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, hashlib, sys, os, random, statistics

PREREG = '/Users/grey/Downloads/quran/surahs/Q037-al-saffat/Q037-F-04-oath-cluster-membership-prereg.md'
EXPECTED_SHA = 'd4e9e449d1655a0632f8d19b18b13710a447c372f2a5bae0d41e7e04e2d2bda1'
SEED = 20260508
N_PERM = 10000

OATH_15 = {37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    rng = random.Random(SEED)

    d = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'))
    ut = d['D_matrix_upper_triangular']
    N = 114
    mat = [[0.0]*N for _ in range(N)]
    for entry in ut:
        i, j, v = entry
        mat[i-1][j-1] = v
        mat[j-1][i-1] = v

    others = OATH_15 - {37}  # 14 surahs
    D_oath = sum(mat[36][s-1] for s in others) / len(others)

    # Permutation null: random 14-subset from {1..114} \ {37}
    pool = [s for s in range(1, 115) if s != 37]
    null_means = []
    for _ in range(N_PERM):
        R = rng.sample(pool, 14)
        D_R = sum(mat[36][s-1] for s in R) / 14
        null_means.append(D_R)
    p_perm = sum(1 for x in null_means if x <= D_oath) / N_PERM

    # Within-cluster median diagnostic
    intra_pairs = []
    for s1 in OATH_15:
        for s2 in OATH_15:
            if s1 < s2:
                intra_pairs.append(mat[s1-1][s2-1])
    M_intra = statistics.median(intra_pairs)

    q37_to_others = [mat[36][s-1] for s in others]
    M_q37 = statistics.median(q37_to_others)

    h1_pass = p_perm <= 0.025
    h2_pass = M_q37 <= M_intra

    if h1_pass and h2_pass:
        verdict = 'CONFIRMED'
    elif h1_pass or h2_pass:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'
    # Pre-commit-violation: D_oath > corpus mean
    full_mean = sum(mat[36][s-1] for s in range(N) if s+1 != 37) / (N-1)
    if D_oath > full_mean + 0.05:
        verdict = 'PRE-COMMIT-VIOLATION'

    # Rank Q 37 within the 15 cluster: who has the smallest sum-of-distances to the other 14?
    cluster_centrality = {}
    for s in OATH_15:
        d_sum = sum(mat[s-1][o-1] for o in OATH_15 if o != s)
        cluster_centrality[s] = d_sum / 14
    ranked = sorted(cluster_centrality.items(), key=lambda x: x[1])
    q37_rank_in_cluster = next(i for i,(s,_) in enumerate(ranked, 1) if s==37)

    out = {
        'finding_id': 'Q037-F-04',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'oath_cluster': sorted(list(OATH_15)),
        'D_oath_q37_to_other_14': D_oath,
        'D_random_null_mean': sum(null_means)/len(null_means),
        'D_random_null_min': min(null_means),
        'D_random_null_max': max(null_means),
        'p_perm_one_tailed': p_perm,
        'corpus_mean_q37_to_113': full_mean,
        'M_intra_cluster_median': M_intra,
        'M_q37_to_others_median': M_q37,
        'cluster_centrality_ranking': ranked,
        'q37_rank_in_cluster_centrality': q37_rank_in_cluster,
        'q37_distances_to_oath_members': {str(s): mat[36][s-1] for s in sorted(others)},
        'h1_pass': h1_pass,
        'h2_pass': h2_pass,
        'alpha_bon': 0.025,
        'verdict': verdict,
        'honest_limits': 'H-NEW-1070 corpus-level cluster-cohesion was confirmed at p=0.0004; Q 37-individual extension here may show cluster cohesion is driven by Q 51-103 with Q 37 at the periphery.',
    }

    print('=== Q037-F-04 OATH-CLUSTER MEMBERSHIP ===')
    print(f'D_oath (Q 37 to other 14): {D_oath:.4f}')
    print(f'D_random null mean: {sum(null_means)/len(null_means):.4f}')
    print(f'p_perm (D_oath ≤ random): {p_perm:.4f}')
    print(f'corpus-mean (Q 37 to 113): {full_mean:.4f}')
    print(f'\nWithin-cluster pairwise median: {M_intra:.4f}')
    print(f'Q 37 row median to others: {M_q37:.4f}')
    print(f'\nQ 37 rank within 15-cluster centrality (lowest mean = rank 1): {q37_rank_in_cluster}/15')
    print('Cluster centrality ranking:')
    for rk, (s, d_) in enumerate(ranked, 1):
        print(f'  {rk:2d}. Q{s:3d}: mean dist to other 14 = {d_:.4f}')
    print(f'\nH1 perm-p ≤ 0.025: {h1_pass}')
    print(f'H2 M_q37 ≤ M_intra: {h2_pass}')
    print(f'Verdict: {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv/Q037-F-04.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
