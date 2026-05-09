#!/usr/bin/env python3
"""Q034-F-01 — al-ḥamdu li-llāh opener cluster {Q 1, 6, 18, 34, 35} FR cohesion test.

Pre-reg: surahs/Q034-saba/preregs/Q034-F-01-hamd-cluster-fr-cohesion-prereg.md
Pre-reg SHA256: 26500022e51a2fe82807fa6308393f9a2b45d1101e2be99797e080f96fb8063a
Rules-tuple: (no-tashkeel, orthographic-token + QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

H1: within-cluster mean FR < random-5-tuple null mean.
H2: drop-Q1 4-cluster mean FR < random-4-tuple null mean.
H3: length-residualized 5-cluster mean < 0.
Bonferroni k=3, alpha_bon=0.01667.
"""
import json, hashlib, sys, os, math
import numpy as np

PREREG = '/Users/grey/Downloads/quran/surahs/Q034-saba/preregs/Q034-F-01-hamd-cluster-fr-cohesion-prereg.md'
EXPECTED_SHA = '26500022e51a2fe82807fa6308393f9a2b45d1101e2be99797e080f96fb8063a'
SEED = 20260509
N_PERM = 10000
ALPHA_BON = 0.05 / 3

def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    rng = np.random.default_rng(SEED)

    # Load FR matrix
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json') as f:
        d111 = json.load(f)
    ut = d111['D_matrix_upper_triangular']
    N = 114
    mat = np.zeros((N, N))
    for entry in ut:
        i, j, v = entry
        mat[i-1][j-1] = v
        mat[j-1][i-1] = v

    # Cluster
    cluster5 = [1, 6, 18, 34, 35]
    cluster4 = [6, 18, 34, 35]

    # H1: 5-cluster within mean
    pairs5 = []
    for i, s1 in enumerate(cluster5):
        for s2 in cluster5[i+1:]:
            pairs5.append(mat[s1-1][s2-1])
    obs5 = float(np.mean(pairs5))

    null5 = []
    for _ in range(N_PERM):
        sample = rng.choice(N, size=5, replace=False)
        pairs = []
        for i in range(5):
            for j in range(i+1, 5):
                pairs.append(mat[sample[i]][sample[j]])
        null5.append(np.mean(pairs))
    null5 = np.array(null5)
    p1_lower = float((null5 <= obs5).mean())

    h1_pass = p1_lower < ALPHA_BON

    # H2: 4-cluster (drop Q1) within mean
    pairs4 = []
    for i, s1 in enumerate(cluster4):
        for s2 in cluster4[i+1:]:
            pairs4.append(mat[s1-1][s2-1])
    obs4 = float(np.mean(pairs4))

    null4 = []
    for _ in range(N_PERM):
        sample = rng.choice(N, size=4, replace=False)
        pairs = []
        for i in range(4):
            for j in range(i+1, 4):
                pairs.append(mat[sample[i]][sample[j]])
        null4.append(np.mean(pairs))
    null4 = np.array(null4)
    p2_lower = float((null4 <= obs4).mean())

    h2_pass = p2_lower < ALPHA_BON

    # H3: length-residualized
    verse_counts = {}
    with open('/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv') as f:
        for line in f:
            sid, vc = line.strip().split('\t')
            verse_counts[int(sid)] = int(vc)

    all_pair_idx = []
    all_dists = []
    all_log_diffs = []
    for i in range(N):
        for j in range(i+1, N):
            all_pair_idx.append((i+1, j+1))
            all_dists.append(mat[i][j])
            all_log_diffs.append(abs(math.log(verse_counts[i+1]) - math.log(verse_counts[j+1])))

    all_dists = np.array(all_dists)
    all_log_diffs = np.array(all_log_diffs)

    b1, b0 = np.polyfit(all_log_diffs, all_dists, 1)
    residuals_all = all_dists - (b0 + b1 * all_log_diffs)

    def res_for_pair(s1, s2):
        target = (s1, s2) if s1 < s2 else (s2, s1)
        for k, (a, b) in enumerate(all_pair_idx):
            if (a, b) == target:
                return float(residuals_all[k])
        return None

    cluster_residuals = []
    for i, s1 in enumerate(cluster5):
        for s2 in cluster5[i+1:]:
            cluster_residuals.append(res_for_pair(s1, s2))
    mean_residual = float(np.mean(cluster_residuals))

    # H3 null: residuals of random 5-tuples
    null_resids = []
    for _ in range(N_PERM):
        sample = rng.choice(N, size=5, replace=False)
        rs = []
        for i in range(5):
            for j in range(i+1, 5):
                a, b = sample[i]+1, sample[j]+1
                rs.append(res_for_pair(a, b))
        null_resids.append(np.mean(rs))
    null_resids = np.array(null_resids)
    p3_lower = float((null_resids <= mean_residual).mean())

    h3_pass = mean_residual < 0 and p3_lower < ALPHA_BON

    n_pass = sum([h1_pass, h2_pass, h3_pass])
    if n_pass == 3: verdict = 'CONFIRMED'
    elif n_pass == 2: verdict = 'DIRECTIONAL'
    elif n_pass == 1: verdict = 'DIRECTIONAL-WEAK'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q034-F-01',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-token + QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'seed': SEED,
        'n_perm': N_PERM,
        'alpha_bon': ALPHA_BON,
        'h1_5cluster_cohesion': {
            'cluster': cluster5,
            'observed_mean_fr': obs5,
            'null_mean': float(null5.mean()),
            'null_std': float(null5.std()),
            'p_lower': p1_lower,
            'pass': h1_pass,
        },
        'h2_4cluster_drop_q1': {
            'cluster': cluster4,
            'observed_mean_fr': obs4,
            'null_mean': float(null4.mean()),
            'null_std': float(null4.std()),
            'p_lower': p2_lower,
            'pass': h2_pass,
        },
        'h3_length_residualized': {
            'regression_b0': float(b0),
            'regression_b1': float(b1),
            'cluster_mean_residual': mean_residual,
            'null_mean_residual': float(null_resids.mean()),
            'p_lower': p3_lower,
            'pass': h3_pass,
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'Empirical-anchor extraction prior to lock observed observed_mean_fr=0.9902 (above corpus mean 0.9226). Direction-locked at COHESIVE under DISCIPLINE; expected NULL based on pre-observation. Verdict ceiling DESCRIPTIVE-EMPIRICAL.',
    }

    print('=== Q034-F-01 al-ḥamdu li-llāh cluster FR cohesion ===')
    print(f'H1 5-cluster: obs={obs5:.4f} vs null mean {null5.mean():.4f} std {null5.std():.4f}')
    print(f'  p_lower={p1_lower:.4f} → pass={h1_pass}')
    print(f'H2 4-cluster (drop Q1): obs={obs4:.4f} vs null mean {null4.mean():.4f}')
    print(f'  p_lower={p2_lower:.4f} → pass={h2_pass}')
    print(f'H3 length-residualized: cluster mean residual={mean_residual:.4f}')
    print(f'  null mean={null_resids.mean():.4f}, p_lower={p3_lower:.4f} → pass={h3_pass}')
    print(f'\nN pass: {n_pass}/3 → {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q034-saba/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q034-saba/csv/Q034-F-01.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
