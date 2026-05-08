#!/usr/bin/env python3
"""
Q032-F-03 — ALM-exception complement: Q 29 + Q 30 + Q 32 cohesion vs random 3-tuples.
Pre-reg SHA verified at runtime; fail-fast on mismatch.
Seed: 20260508. n_perm = 10000.
"""
import json, math, random, hashlib, os, sys

EXPECTED_SHA = '85ef2873698bffbba5dbd5884336e7db0724745176e59d6fec39bae743d202ba'
PREREG_PATH = '/Users/grey/Downloads/quran/surahs/Q032-al-sajda/Q032-F-03-alm-exception-cohesion-prereg.md'
H111 = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q032-al-sajda/csv/Q032-F-03.json'

def verify_sha():
    with open(PREREG_PATH, 'rb') as f:
        got = hashlib.sha256(f.read()).hexdigest()
    if got != EXPECTED_SHA:
        print(f'SHA MISMATCH: expected {EXPECTED_SHA}, got {got}')
        sys.exit(1)
    print(f'Pre-reg SHA verified: {got}')

def main():
    verify_sha()
    d = json.load(open(H111))
    N = 114
    D = [[0.0]*N for _ in range(N)]
    for i,j,v in d['D_matrix_upper_triangular']:
        D[i-1][j-1] = v
        D[j-1][i-1] = v

    # ALM-exception triplet: Q 29, Q 30, Q 32
    triplet = [29, 30, 32]
    pairs = [(29,30), (29,32), (30,32)]
    fr_vals = [D[a-1][b-1] for a,b in pairs]
    T_obs = sum(fr_vals)/3

    # Permutation null: 10000 random 3-tuples from N
    rng = random.Random(20260508)
    n_perm = 10000
    le = 0
    perm_means = []
    for _ in range(n_perm):
        idx = rng.sample(range(N), 3)
        a,b,c = idx
        T = (D[a][b] + D[a][c] + D[b][c]) / 3
        perm_means.append(T)
        if T <= T_obs:
            le += 1
    p_low = (le + 1) / (n_perm + 1)
    perm_sorted = sorted(perm_means)
    median_perm = perm_sorted[len(perm_sorted)//2]
    p25 = perm_sorted[int(0.25*len(perm_sorted))]
    p10 = perm_sorted[int(0.10*len(perm_sorted))]

    # Consecutive-3-tuple comparison: where does Q29-Q30-Q31 (the natural ALM-cluster) sit?
    # And how does the EXCEPTION sub-set compare to other ALM combinations?
    alm_full = [2, 3, 29, 30, 31, 32]
    from itertools import combinations
    alm_3tuples = list(combinations(alm_full, 3))
    alm_means = []
    for trio in alm_3tuples:
        a,b,c = trio
        T = (D[a-1][b-1] + D[a-1][c-1] + D[b-1][c-1]) / 3
        alm_means.append((trio, T))
    alm_means.sort(key=lambda x: x[1])

    if p_low < 0.05:
        verdict = 'VINDICATED'
    elif p_low < 0.20:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'test_id': 'Q032-F-03',
        'pre_reg_sha': EXPECTED_SHA,
        'seed': 20260508,
        'n_perm': n_perm,
        'rules_tuple': '(no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'triplet': triplet,
        'pairwise_FR': {f'Q{a}-Q{b}': D[a-1][b-1] for a,b in pairs},
        'T_observed_mean_FR': T_obs,
        'corpus_3tuple_perm_median': median_perm,
        'corpus_3tuple_perm_p25': p25,
        'corpus_3tuple_perm_p10': p10,
        'p_low_T_le_T_obs': p_low,
        'alm_full_set': alm_full,
        'alm_all_3tuples_ranked_by_FR_mean': [
            {'triplet': list(t), 'mean_FR': v} for t,v in alm_means
        ],
        'verdict': verdict,
        'bonferroni_k': 1,
        'alpha_bon': 0.05,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'Q032-F-03 verdict: {verdict}')
    print(f'  T_obs (Q29+Q30+Q32) = {T_obs:.4f}')
    print(f'  perm median         = {median_perm:.4f}')
    print(f'  p_low               = {p_low:.4f}')

if __name__ == '__main__':
    main()
