#!/usr/bin/env python3
"""Q035-F-01 — al-hamdu li-llah cluster FR cohesion + Q35 centrality test.

Pre-reg: surahs/Q035-fatir/preregs/Q035-F-01-hamdu-cluster-prereg.md
Pre-reg SHA256: 18e534a4fedb377109e3290ee4593044eacbc40d0b2c62c793d0f724db5c8e2c
Rules-tuple: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, Hafs-Kufan, mashriqi)

H1: 5-cluster mean FR < random-5-subset null mean (p_lower < 0.025).
H2: Q35's mean FR to other 4 cluster members is in bottom-half (rank <= 2 of 5) of cluster centrality ranking.
Bonferroni k=2, alpha_bon=0.025.
"""
import json, hashlib, sys, os
import numpy as np

PREREG = '/Users/grey/Downloads/quran/surahs/Q035-fatir/preregs/Q035-F-01-hamdu-cluster-prereg.md'
EXPECTED_SHA = '18e534a4fedb377109e3290ee4593044eacbc40d0b2c62c793d0f724db5c8e2c'
SEED = 20260509
N_PERM = 10000
ALPHA_BON = 0.05 / 2


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    rng = np.random.default_rng(SEED)
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json') as f:
        d111 = json.load(f)
    ut = d111['D_matrix_upper_triangular']
    N = 114
    mat = np.zeros((N, N))
    for entry in ut:
        i, j, v = entry
        mat[i-1][j-1] = v
        mat[j-1][i-1] = v

    cluster = [1, 6, 18, 34, 35]
    # Within-cluster mean
    pairs = []
    for i, s1 in enumerate(cluster):
        for s2 in cluster[i+1:]:
            pairs.append(mat[s1-1][s2-1])
    obs_mean = float(np.mean(pairs))

    null_means = []
    for _ in range(N_PERM):
        sample = rng.choice(N, size=5, replace=False)
        p = []
        for i in range(5):
            for j in range(i+1, 5):
                p.append(mat[sample[i]][sample[j]])
        null_means.append(np.mean(p))
    null_means = np.array(null_means)
    p_lower = float((null_means <= obs_mean).mean())
    h1_pass = p_lower < ALPHA_BON

    # H2: Q35's centrality (mean FR to other 4 cluster members)
    centralities = {}
    for s in cluster:
        others = [t for t in cluster if t != s]
        m = np.mean([mat[s-1][t-1] for t in others])
        centralities[s] = float(m)
    sorted_central = sorted(centralities.items(), key=lambda x: x[1])  # ascending = most-central first
    q35_rank = next(rk for rk, (s, _) in enumerate(sorted_central, 1) if s == 35)
    h2_pass = q35_rank <= 2  # bottom-half (i.e., top-2 most central)

    n_pass = sum([h1_pass, h2_pass])
    if n_pass == 2: verdict = 'CONFIRMED'
    elif n_pass == 1: verdict = 'DIRECTIONAL'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q035-F-01',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, Hafs-Kufan, mashriqi)',
        'seed': SEED,
        'n_perm': N_PERM,
        'alpha_bon': ALPHA_BON,
        'h1_cluster_cohesion': {
            'cluster': cluster,
            'observed_mean_fr': obs_mean,
            'null_mean': float(null_means.mean()),
            'null_std': float(null_means.std()),
            'p_lower': p_lower,
            'pass': h1_pass,
        },
        'h2_q35_centrality': {
            'centralities': [{'surah': s, 'mean_fr_to_other_4': c} for s, c in sorted_central],
            'q35_rank': q35_rank,
            'pass': h2_pass,
            'threshold': 'top-2 (bottom-half)',
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'Pre-flight: obs_mean=0.9902 > corpus null mean 0.9226 (cluster is ANTI-cohesive). H1 will FAIL. H2 tests Q35 placement within the cluster; pre-flight Q35 centrality not yet examined here.',
    }

    print('=== Q035-F-01 al-hamdu cluster cohesion ===')
    print(f'H1 cluster mean FR={obs_mean:.4f} vs null mean {null_means.mean():.4f}, p_lower={p_lower:.4f} -> pass={h1_pass}')
    print(f'H2 Q35 centrality rank in cluster: {q35_rank}/5 -> pass={h2_pass}')
    print('Centrality (ascending = most-central first):')
    for rk, (s, c) in enumerate(sorted_central, 1):
        marker = ' <-Q35' if s == 35 else ''
        print(f'  rank {rk}: Q{s} mean_fr={c:.4f}{marker}')
    print(f'\nN pass: {n_pass}/2 -> {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv/Q035-F-01.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
