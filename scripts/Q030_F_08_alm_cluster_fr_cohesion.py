#!/usr/bin/env python3
"""Q030-F-08 — ALM 6-surah cluster Fisher-Rao cohesion (sub-set of muqaṭṭāʿat).

Pre-reg: surahs/Q030-al-rum/Q030-F-08-alm-cluster-fr-cohesion-prereg.md
Pre-reg SHA256: 1a88f47c8101b244f136f25ce8df0dcbe45824cfa842473e364f84e44c78cc85
Rules-tuple: matches H-NEW-111 canonical (no-tashkeel, orthographic-token, QAC root distribution,
              basmala-counted-only-in-Q1, hafs-kufan).
"""
import hashlib, json, os, random, sys
import numpy as np

PREREG = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/Q030-F-08-alm-cluster-fr-cohesion-prereg.md'
EXPECTED_SHA = '1a88f47c8101b244f136f25ce8df0dcbe45824cfa842473e364f84e44c78cc85'
FR_PATH = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'
QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
OUT = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv/Q030-F-08.json'

SEED = 20260509
N_PERM = 10000
ALPHA_BON = 0.025

CLUSTER_ALM = [2, 3, 29, 30, 31, 32]
CLUSTER_WAMA_ADRAKA = [69, 74, 77, 82, 83, 86, 90, 97, 101, 104]  # H-NEW-1190


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def mean_pairwise(D, surahs):
    idxs = [s - 1 for s in surahs]
    n = len(idxs)
    total = 0.0
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            total += D[idxs[i], idxs[j]]
            cnt += 1
    return total / cnt if cnt else 0.0


def main():
    verify_sha()

    # Load FR matrix
    fr = json.load(open(FR_PATH))
    N = 114
    D = np.zeros((N, N))
    for i, j, d in fr['D_matrix_upper_triangular']:
        D[i - 1, j - 1] = d
        D[j - 1, i - 1] = d

    # Load Quran for length matching
    quran = json.load(open(QURAN_PATH))
    surah_verses = {s['id']: s['total_verses'] for s in quran}

    # Observed cluster mean
    D_obs = mean_pairwise(D, CLUSTER_ALM)
    cluster_verses_total = sum(surah_verses[s] for s in CLUSTER_ALM)
    K = len(CLUSTER_ALM)

    # All 15 within-ALM pair distances (descriptive)
    pair_distances = []
    for i in range(K):
        for j in range(i + 1, K):
            a, b = CLUSTER_ALM[i], CLUSTER_ALM[j]
            pair_distances.append({'a': a, 'b': b, 'd': float(D[a - 1, b - 1])})
    pair_distances.sort(key=lambda x: x['d'])

    # === Cell A: uniform 6-of-113 (exclude Q 1, matching H-NEW-111 canonical null) ===
    pool_A = [s for s in range(2, N + 1)]
    rng = random.Random(SEED)
    null_A = []
    for _ in range(N_PERM):
        sample = rng.sample(pool_A, K)
        null_A.append(mean_pairwise(D, sample))
    null_A_mean = float(np.mean(null_A))
    null_A_5pct = float(np.percentile(null_A, 5))
    null_A_50pct = float(np.percentile(null_A, 50))
    p_A = sum(1 for x in null_A if x <= D_obs) / N_PERM
    pass_A = p_A <= ALPHA_BON

    # === Cell B: length-matched (total within ±20%) ===
    lo = cluster_verses_total * 0.80
    hi = cluster_verses_total * 1.20
    rng = random.Random(SEED)
    null_B = []
    null_B_attempts = 0
    max_attempts = N_PERM * 200
    while len(null_B) < N_PERM and null_B_attempts < max_attempts:
        sample = rng.sample(pool_A, K)
        null_B_attempts += 1
        total = sum(surah_verses[s] for s in sample)
        if lo <= total <= hi:
            null_B.append(mean_pairwise(D, sample))
    if null_B:
        null_B_mean = float(np.mean(null_B))
        null_B_5pct = float(np.percentile(null_B, 5))
        p_B = sum(1 for x in null_B if x <= D_obs) / len(null_B)
    else:
        null_B_mean = null_B_5pct = p_B = None
    pass_B = (p_B is not None and p_B <= ALPHA_BON)

    # === MW-5 PC: 6-of-10 H-NEW-1190 sub-sample, deterministic with SEED ===
    rng_pc = random.Random(SEED)
    pc_subsample = sorted(rng_pc.sample(CLUSTER_WAMA_ADRAKA, K))
    D_pc = mean_pairwise(D, pc_subsample)

    rng = random.Random(SEED + 1)
    null_pc = []
    for _ in range(N_PERM):
        sample = rng.sample(pool_A, K)
        null_pc.append(mean_pairwise(D, sample))
    p_pc = sum(1 for x in null_pc if x <= D_pc) / N_PERM
    pc_pass = p_pc <= 0.05

    # === Sensitivity: PC under 5 alternative seeds ===
    pc_sensitivity = []
    for alt_seed in [20260510, 20260511, 20260512, 20260513, 20260514]:
        rng_alt = random.Random(alt_seed)
        sample_alt = sorted(rng_alt.sample(CLUSTER_WAMA_ADRAKA, K))
        D_alt = mean_pairwise(D, sample_alt)
        p_alt = sum(1 for x in null_pc if x <= D_alt) / N_PERM
        pc_sensitivity.append({
            'seed': alt_seed, 'sample': sample_alt,
            'D_pc_alt': float(D_alt), 'p_pc_alt': p_alt,
            'pass': p_alt <= 0.05,
        })

    # Verdict per acceptance windows
    if not pc_pass:
        verdict = 'NULL-BROKEN (positive control failed)'
    else:
        if pass_A and pass_B:
            verdict = 'PASS-DIRECTED'
        elif pass_A and not pass_B:
            verdict = 'DESCRIPTIVE-ONLY (length-confound)'
        elif (not pass_A) and pass_B:
            verdict = 'PARTIAL'
        else:
            verdict = 'NULL (PC valid)'

    out = {
        'test_id': 'Q030-F-08',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED, 'n_perm': N_PERM, 'alpha_bon': ALPHA_BON,
        'cluster_alm': CLUSTER_ALM,
        'D_obs_mean_pairwise_FR': float(D_obs),
        'within_cluster_pair_distances_sorted': pair_distances,
        'cluster_verses_total': cluster_verses_total,
        'cell_A_uniform': {
            'n_perm': N_PERM,
            'null_mean': null_A_mean,
            'null_5pct': null_A_5pct,
            'null_50pct': null_A_50pct,
            'p_one_sided_le': p_A,
            'pass_alpha_bon_0_025': pass_A,
        },
        'cell_B_length_matched': {
            'length_band_low': lo, 'length_band_high': hi,
            'n_accepted_samples': len(null_B),
            'null_mean': null_B_mean, 'null_5pct': null_B_5pct,
            'p_one_sided_le': p_B,
            'pass_alpha_bon_0_025': pass_B,
        },
        'mw5_positive_control': {
            'method': '6-of-10 sub-sample of H-NEW-1190 wa-mā adrāka mā (FR-cohesive p=0.00068)',
            'subsample_seed': SEED,
            'subsample_surahs': pc_subsample,
            'D_pc': float(D_pc),
            'p_one_sided_le': p_pc,
            'alpha_threshold': 0.05,
            'pass': pc_pass,
        },
        'mw5_pc_sensitivity': pc_sensitivity,
        'verdict': verdict,
        'comparison_to_h_new_1395_HM7': {
            'h_new_1395_verdict': 'NULL (CONFIRMED-NULL) — HM 7-cluster not FR-cohesive',
            'h_new_1395_D_obs': 0.8672,
            'h_new_1395_null_uniform_mean': 0.9230,
            'this_test_D_obs': float(D_obs),
            'this_test_p_A': p_A,
            'this_test_p_B': p_B,
        },
        'a_priori_prediction': 'NULL-leaning per cross-finding-025 marker-thickness rule',
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q030-F-08 results:")
    print(f"  Cluster: ALM = {CLUSTER_ALM}")
    print(f"  D_obs (mean pairwise FR) = {D_obs:.5f}")
    print(f"  Cluster total verses = {cluster_verses_total}; length band = [{lo:.0f}, {hi:.0f}]")
    print(f"  Cell A: null_mean={null_A_mean:.5f}, null_5pct={null_A_5pct:.5f}, p={p_A:.4f}, pass={pass_A}")
    if null_B_mean is not None:
        print(f"  Cell B: n_accepted={len(null_B)}, null_mean={null_B_mean:.5f}, null_5pct={null_B_5pct:.5f}, p={p_B:.4f}, pass={pass_B}")
    else:
        print(f"  Cell B: insufficient length-matched samples (n={len(null_B)})")
    print(f"  MW-5 PC: subsample={pc_subsample}, D_pc={D_pc:.5f}, p_pc={p_pc:.4f}, pass={pc_pass}")
    print(f"  PC sensitivity: {sum(1 for s in pc_sensitivity if s['pass'])}/5 passes under alternate seeds")
    print(f"  Verdict: {verdict}")
    print(f"Written: {OUT}")


if __name__ == '__main__':
    main()
