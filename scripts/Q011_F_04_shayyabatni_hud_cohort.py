#!/usr/bin/env python3
"""Q011-F-04 — shayyabatnī Hūd 5-surah cohort architectural cohesion.

Pre-reg: surahs/Q011-hud/preregs/Q011-F-04-shayyabatni-hud-cohort-prereg.md
Pre-reg SHA256: d1abe1d46336aef1213c07696cabbcab796bd6eaae92da005ebad1abca5da889
Rules-tuple: (no-tashkeel for FR; min-tashkeel for rhyme-top-letter;
              precomputed sig_A and UAS;
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed: 20260507
"""
import json, hashlib, sys, os, random, math, statistics

PREREG = '/Users/grey/Downloads/quran/surahs/Q011-hud/preregs/Q011-F-04-shayyabatni-hud-cohort-prereg.md'
EXPECTED_SHA = 'd1abe1d46336aef1213c07696cabbcab796bd6eaae92da005ebad1abca5da889'
SEED = 20260507
N_PERM = 10000

COHORT = [11, 56, 77, 78, 81]  # Hūd, Wāqiʿa, Mursalāt, Nabaʾ (ʿAmma), Takwīr


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def reconstruct_fr_matrix(path):
    with open(path) as f:
        d = json.load(f)
    ut = d['D_matrix_upper_triangular']
    M = [[0.0]*114 for _ in range(114)]
    for entry in ut:
        i, j, v = entry
        i0 = int(i) - 1; j0 = int(j) - 1
        M[i0][j0] = float(v); M[j0][i0] = float(v)
    return M


def cohort_pairwise_mean_fr(M, surahs):
    pairs = []
    n = len(surahs)
    for i in range(n):
        for j in range(i+1, n):
            pairs.append(M[surahs[i]-1][surahs[j]-1])
    return sum(pairs)/len(pairs)


def cohort_top_letter_agreement(top_letters, surahs):
    letters = [top_letters[s] for s in surahs]
    counts = {}
    for L in letters:
        counts[L] = counts.get(L, 0) + 1
    return max(counts.values()) / len(letters)


def main():
    verify_sha()
    rng = random.Random(SEED)

    # Load empirical artifacts
    M = reconstruct_fr_matrix('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json')

    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json') as f:
        d750 = json.load(f)
    sig_A = {r['surah']: r['sig_A'] for r in d750['per_surah']}

    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json') as f:
        d840 = json.load(f)
    UAS = {r['surah']: r['UAS'] for r in d840['all_uas']}

    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json') as f:
        d700 = json.load(f)
    top_letters = {r['surah']: r['top_letter'] for r in d700['rhyme']['rhyme_letter_diagnostics']}

    # Cohort observed values
    A_obs = cohort_pairwise_mean_fr(M, COHORT)
    B_obs = statistics.pstdev([sig_A[s] for s in COHORT])
    C_obs = statistics.pstdev([UAS[s] for s in COHORT])
    D_obs = cohort_top_letter_agreement(top_letters, COHORT)

    # Random-5 null: draw from {2..114} (exclude Q 1)
    pool = [s for s in range(2, 115) if s in sig_A and s in UAS and s in top_letters]
    cnt_A = cnt_B = cnt_C = cnt_D = 0
    null_A = []
    null_B = []
    null_C = []
    null_D = []
    for _ in range(N_PERM):
        sample = rng.sample(pool, 5)
        a = cohort_pairwise_mean_fr(M, sample)
        b = statistics.pstdev([sig_A[s] for s in sample])
        c = statistics.pstdev([UAS[s] for s in sample])
        d = cohort_top_letter_agreement(top_letters, sample)
        null_A.append(a); null_B.append(b); null_C.append(c); null_D.append(d)
        if a <= A_obs: cnt_A += 1   # lower = more cohesive
        if b <= B_obs: cnt_B += 1
        if c <= C_obs: cnt_C += 1
        if d >= D_obs: cnt_D += 1   # higher = more agreement

    p_A = (cnt_A + 1) / (N_PERM + 1)
    p_B = (cnt_B + 1) / (N_PERM + 1)
    p_C = (cnt_C + 1) / (N_PERM + 1)
    p_D = (cnt_D + 1) / (N_PERM + 1)

    alpha_bon = 0.0125
    pass_A = p_A <= alpha_bon
    pass_B = p_B <= alpha_bon
    pass_C = p_C <= alpha_bon
    pass_D = p_D <= alpha_bon
    n_pass = sum([pass_A, pass_B, pass_C, pass_D])

    if n_pass >= 3:
        verdict = 'CONFIRMED'
    elif n_pass == 2:
        verdict = 'DIRECTIONAL'
    elif n_pass <= 1:
        verdict = 'NULL'
    if all(p > 0.95 for p in [p_A, p_B, p_C, p_D]):
        verdict = 'NULL — pre-commit-violation candidate (cohort strongly less cohesive)'

    out = {
        'finding_id': 'Q011-F-04',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'cohort': COHORT,
        'cohort_label': 'shayyabatni-Hud Shamail #40 (Q11, Q56, Q77, Q78, Q81)',
        'alpha_bon': alpha_bon,
        'axes': {
            'A_mean_pairwise_FR': {
                'cohort': A_obs, 'null_mean': sum(null_A)/len(null_A),
                'p_lower': p_A, 'pass_alpha_bon': pass_A,
            },
            'B_sig_A_sd': {
                'cohort': B_obs, 'null_mean': sum(null_B)/len(null_B),
                'p_lower': p_B, 'pass_alpha_bon': pass_B,
            },
            'C_UAS_sd': {
                'cohort': C_obs, 'null_mean': sum(null_C)/len(null_C),
                'p_lower': p_C, 'pass_alpha_bon': pass_C,
            },
            'D_top_letter_agreement': {
                'cohort': D_obs, 'null_mean': sum(null_D)/len(null_D),
                'p_upper': p_D, 'pass_alpha_bon': pass_D,
            },
        },
        'n_axes_pass_bonferroni': n_pass,
        'verdict': verdict,
    }
    out_dir = '/Users/grey/Downloads/quran/surahs/Q011-hud/csv'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'Q011-F-04.json'), 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Q011-F-04 verdict: {verdict} ({n_pass}/4 axes pass α_bon={alpha_bon})")
    for k, v in out['axes'].items():
        print(f"  {k}: {v}")


if __name__ == '__main__':
    main()
