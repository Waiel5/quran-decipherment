#!/usr/bin/env python3
"""
Q043-F-07 — HM 7-cluster within-pair FR-distance ranking of Q 43.
Pre-reg SHA256: 4b7630a63ef47d4dfc559611070a5b166144593a1872d5fecfc1a866ea7bd654
Seed: 20260509; n_perm: 10000; Bonferroni-3 → α = 0.0167.
Direction: median D[Q43, HM_others] < median D[Q43, random size-6 non-HM].
"""
import hashlib
import json
import os
import random
import statistics
import sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/preregs/Q043-F-07-hm-cluster-pair-distance-prereg.md"
EXPECTED_SHA = "4b7630a63ef47d4dfc559611070a5b166144593a1872d5fecfc1a866ea7bd654"
FR_PATH = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/csv/Q043-F-07.json"
SEED = 20260509
N_PERM = 10000
ALPHA = 0.05 / 3
N_SURAHS = 114
TARGET = 43
HM = [40, 41, 42, 43, 44, 45, 46]

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
    print(f"[OK] Pre-reg SHA verified.")

def main():
    verify()
    hnew = json.load(open(FR_PATH))
    D = [[0.0]*N_SURAHS for _ in range(N_SURAHS)]
    for entry in hnew["D_matrix_upper_triangular"]:
        i, j, d = entry
        D[i-1][j-1] = d
        D[j-1][i-1] = d

    hm_others = [s for s in HM if s != TARGET]
    observed_pairs = [(s, D[TARGET-1][s-1]) for s in hm_others]
    observed_median = statistics.median([p[1] for p in observed_pairs])

    pool = [s for s in range(1, N_SURAHS+1) if s not in HM]
    rng = random.Random(SEED)
    null_medians = []
    n_size = len(hm_others)
    for _ in range(N_PERM):
        sample = rng.sample(pool, n_size)
        med = statistics.median([D[TARGET-1][s-1] for s in sample])
        null_medians.append(med)
    null_medians_sorted = sorted(null_medians)
    n_le = sum(1 for v in null_medians if v <= observed_median)
    p_one_sided = n_le / N_PERM
    null_median = statistics.median(null_medians)
    null_p25 = null_medians_sorted[int(0.25 * N_PERM)]
    null_p75 = null_medians_sorted[int(0.75 * N_PERM)]

    if observed_median < null_median and p_one_sided < ALPHA:
        verdict = "PASS-DIRECTED — Q 43 tighter to HM than to random"
    elif observed_median < null_median:
        verdict = "DIRECTIONAL"
    elif observed_median > null_median:
        verdict = "PRE-COMMIT-VIOLATION — observed direction reversed; published as NULL"
    else:
        verdict = "NULL"

    out = {
        "prereg_id": "Q043-F-07",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA,
        "target_surah": TARGET,
        "hm_cluster": HM,
        "hm_others": hm_others,
        "observed_pairs": [{"hm": s, "fr_distance": d} for s, d in observed_pairs],
        "observed_median": observed_median,
        "null_median": null_median,
        "null_p25": null_p25,
        "null_p75": null_p75,
        "p_one_sided_lower": p_one_sided,
        "pass_alpha": p_one_sided < ALPHA,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"observed_median = {observed_median:.4f}")
    print(f"null_median     = {null_median:.4f}  (p25={null_p25:.4f}, p75={null_p75:.4f})")
    print(f"p_one_sided     = {p_one_sided:.4f}")
    print(f"VERDICT: {verdict}")

if __name__ == "__main__":
    main()
