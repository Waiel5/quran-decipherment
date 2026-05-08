#!/usr/bin/env python3
"""
Q047-F-03 — Q 47-Q 48-Q 49 architectural triplet cohesion.
Pre-reg SHA verified at runtime; fail-fast on mismatch.
Seed: 20260508. n_perm = 10000. Bonferroni-1.
"""
import json, hashlib, os, sys, random

EXPECTED_SHA = '998eebaf6c77085b6fc50fbc5a0f86a156dfbf9d992291846b0359beaff08fe6'
PREREG_PATH = '/Users/grey/Downloads/quran/surahs/Q047-muhammad/Q047-F-03-q47-q48-q49-triplet-prereg.md'
H111 = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q047-muhammad/csv/Q047-F-03.json'

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

    triplet = [47, 48, 49]
    pairs = [(47,48), (47,49), (48,49)]
    fr_vals = [D[a-1][b-1] for a,b in pairs]
    T_obs = sum(fr_vals)/3

    # Permutation null: 10000 random 3-tuples
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

    # Consecutive-3-tuple ranking — where does Q47-Q48-Q49 sit?
    consec = []
    for s in range(1, 113):
        a, b, c = s, s+1, s+2
        if c > N: break
        T_c = (D[a-1][b-1] + D[a-1][c-1] + D[b-1][c-1]) / 3
        consec.append((s, T_c))
    consec.sort(key=lambda x: x[1])
    rank_consec = next(i+1 for i,(s,t) in enumerate(consec) if s == 47)
    consec_total = len(consec)

    # Verdict
    if p_low < 0.05 and rank_consec <= 28:
        verdict = 'VINDICATED'
    elif p_low < 0.10:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'test_id': 'Q047-F-03',
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
        'rank_among_consecutive_triplets': rank_consec,
        'consecutive_triplets_total': consec_total,
        'percentile_among_consecutive': rank_consec / consec_total,
        'top_10_cheapest_consecutive_triplets': [{'start_surah': s, 'mean_FR': round(t,4)} for s,t in consec[:10]],
        'verdict': verdict,
        'bonferroni_k': 1,
        'alpha_bon': 0.05,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'Q047-F-03 verdict: {verdict}')
    print(f'  T_obs (Q47+Q48+Q49) = {T_obs:.4f}')
    print(f'  perm median         = {median_perm:.4f}')
    print(f'  p_low               = {p_low:.4f}')
    print(f'  consec rank         = {rank_consec}/{consec_total}')

if __name__ == '__main__':
    main()
