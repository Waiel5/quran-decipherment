#!/usr/bin/env python3
"""Q073-F-04 — H-NEW-1301 IMPV-qrA cluster cohesion replication with corrected MW-5 positive control.

Pre-reg: surahs/Q073-al-muzzammil/Q073-F-04-impv-qra-cluster-corrected-pc-prereg.md
Pre-reg SHA256: 996b6babbcdb7a5eaf89f5d8e94f8ff498f8f2d3505865a377143d740422a257
Rules-tuple: (no-tashkeel, QAC v0.4 root tokens, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan; matches H-NEW-111)
"""
import json, hashlib, sys, os, random
import numpy as np

PREREG = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/Q073-F-04-impv-qra-cluster-corrected-pc-prereg.md'
EXPECTED_SHA = '996b6babbcdb7a5eaf89f5d8e94f8ff498f8f2d3505865a377143d740422a257'
SEED = 20260509
N_PERM = 10000

FR_PATH = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'
QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/csv/Q073-F-04.json'

CLUSTER_IMPV_QRA = [17, 69, 73, 96]  # H-NEW-1300 corpus-EXACT
CLUSTER_WAMA_ADRAKA = [69, 74, 77, 82, 83, 86, 90, 97, 101, 104]  # H-NEW-1190


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def mean_pairwise_distance(D, surah_ids):
    """Mean pairwise FR distance for the given surah list (1-indexed)."""
    idxs = [s - 1 for s in surah_ids]
    n = len(idxs)
    total = 0.0
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            total += D[idxs[i], idxs[j]]
            cnt += 1
    return total / cnt if cnt else 0.0


def main():
    verify_sha()

    # Load FR matrix
    fr = json.load(open(FR_PATH))
    n = 114
    D = np.zeros((n, n))
    for i, j, d in fr['D_matrix_upper_triangular']:
        D[i-1, j-1] = d
        D[j-1, i-1] = d

    # Load Quran for length matching
    quran = json.load(open(QURAN_PATH))
    surah_verses = {s['id']: s['total_verses'] for s in quran}

    # === Cluster D_obs ===
    D_obs = mean_pairwise_distance(D, CLUSTER_IMPV_QRA)

    # === Cell A: uniform 4-of-113 (exclude Q 1 per H-NEW-111 canonical) ===
    rng = random.Random(SEED)
    pool_A = [s for s in range(2, 115)]  # exclude Q 1, 2-114
    null_A = []
    for _ in range(N_PERM):
        sample = rng.sample(pool_A, 4)
        null_A.append(mean_pairwise_distance(D, sample))
    null_A_mean = float(np.mean(null_A))
    null_A_5pct = float(np.percentile(null_A, 5))
    p_A = sum(1 for x in null_A if x <= D_obs) / N_PERM

    # === Cell B: length-matched ===
    cluster_verse_counts = [surah_verses[s] for s in CLUSTER_IMPV_QRA]
    min_v, max_v = min(cluster_verse_counts), max(cluster_verse_counts)
    band_lo, band_hi = max(1, min_v // 2), max_v * 2
    pool_B = [s for s in pool_A if band_lo <= surah_verses.get(s, 0) <= band_hi]
    null_B = []
    rng = random.Random(SEED)
    for _ in range(N_PERM):
        if len(pool_B) >= 4:
            sample = rng.sample(pool_B, 4)
            null_B.append(mean_pairwise_distance(D, sample))
    null_B_mean = float(np.mean(null_B)) if null_B else None
    null_B_5pct = float(np.percentile(null_B, 5)) if null_B else None
    p_B = (sum(1 for x in null_B if x <= D_obs) / len(null_B)) if null_B else None

    # === MW-5 PC: 4-of-10 H-NEW-1190 sub-sample, deterministic with seed ===
    rng_pc = random.Random(SEED)
    pc_subsample = sorted(rng_pc.sample(CLUSTER_WAMA_ADRAKA, 4))
    D_pc = mean_pairwise_distance(D, pc_subsample)

    # PC null = same uniform pool_A
    rng = random.Random(SEED + 1)  # offset seed to differ from primary
    null_pc = []
    for _ in range(N_PERM):
        sample = rng.sample(pool_A, 4)
        null_pc.append(mean_pairwise_distance(D, sample))
    p_pc = sum(1 for x in null_pc if x <= D_pc) / N_PERM
    pc_pass = (p_pc <= 0.05)

    # === Sensitivity: PC under 5 alternative seeds ===
    pc_sensitivity = []
    for alt_seed in [20260510, 20260511, 20260512, 20260513, 20260514]:
        rng_alt = random.Random(alt_seed)
        sample_alt = sorted(rng_alt.sample(CLUSTER_WAMA_ADRAKA, 4))
        D_alt = mean_pairwise_distance(D, sample_alt)
        # Simple count against pre-computed null_pc
        p_alt = sum(1 for x in null_pc if x <= D_alt) / N_PERM
        pc_sensitivity.append({
            'seed': alt_seed,
            'sample': sample_alt,
            'D_pc_alt': D_alt,
            'p_pc_alt': p_alt,
            'pass': p_alt <= 0.05,
        })

    # === Verdict ===
    if not pc_pass:
        verdict = "NULL-BROKEN (positive control failed)"
    else:
        h1a_pass = (p_A <= 0.025)
        h1b_pass = (p_B is not None and p_B <= 0.025)
        n_pass = (1 if h1a_pass else 0) + (1 if h1b_pass else 0)
        if n_pass == 2:
            verdict = "CONFIRMED"
        elif n_pass == 1:
            verdict = "DIRECTIONAL"
        else:
            verdict = "NULL (PC valid)"

    out = {
        "test_id": "Q073-F-04",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "cluster_impv_qra": CLUSTER_IMPV_QRA,
        "D_obs": D_obs,
        "cell_A_uniform": {
            "n_perm": N_PERM,
            "null_mean": null_A_mean,
            "null_5pct": null_A_5pct,
            "p_one_sided_le": p_A,
            "pass_alpha_bon_0_025": (p_A <= 0.025),
        },
        "cell_B_length_matched": {
            "n_perm": len(null_B),
            "length_band_low": band_lo,
            "length_band_high": band_hi,
            "pool_size": len(pool_B),
            "null_mean": null_B_mean,
            "null_5pct": null_B_5pct,
            "p_one_sided_le": p_B,
            "pass_alpha_bon_0_025": (p_B is not None and p_B <= 0.025),
        },
        "mw5_positive_control_corrected": {
            "method": "4-of-10 sub-sample of H-NEW-1190 wa-mā adrāka mā 10-surah cluster (FR-cohesive p=0.00068)",
            "subsample_seed": SEED,
            "subsample_surahs": pc_subsample,
            "D_pc": D_pc,
            "p_one_sided_le": p_pc,
            "alpha_threshold": 0.05,
            "pass": pc_pass,
        },
        "mw5_pc_sensitivity": pc_sensitivity,
        "verdict": verdict,
        "comparison_to_h_new_1301": {
            "h_new_1301_verdict": "NULL-BROKEN (HM 4-of-7 PC failed at p=0.336)",
            "h_new_1301_p_A": 0.263,
            "h_new_1301_p_B": 0.129,
            "this_test_p_A": p_A,
            "this_test_p_B": p_B,
            "this_test_p_pc": p_pc,
        },
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Verdict: {verdict}")
    print(f"  D_obs (IMPV-qrA cluster mean pairwise FR) = {D_obs:.5f}")
    print(f"  Cell A: null mean = {null_A_mean:.5f}, 5pct = {null_A_5pct:.5f}, p = {p_A:.4f}")
    p_B_str = f"{p_B:.4f}" if p_B is not None else 'n/a'
    null_B_mean_str = f"{null_B_mean:.5f}" if null_B_mean is not None else 'n/a'
    null_B_5pct_str = f"{null_B_5pct:.5f}" if null_B_5pct is not None else 'n/a'
    print(f"  Cell B: null mean = {null_B_mean_str}, 5pct = {null_B_5pct_str}, p = {p_B_str}")
    print(f"  MW-5 PC corrected: subsample = {pc_subsample}, D_pc = {D_pc:.5f}, p_pc = {p_pc:.4f}, pass = {pc_pass}")
    print(f"  PC sensitivity (5 alt seeds): {sum(1 for s in pc_sensitivity if s['pass'])}/5 pass")
    print(f"Written to: {OUT_PATH}")


if __name__ == '__main__':
    main()
