#!/usr/bin/env python3
"""Q096-F-04 — Sajda-tilāwa 14-surah cluster Fisher-Rao cohesion.

Pre-reg: Q096-F-04-sajda-cluster-prereg.md
SHA256:  6620cbef4068e0c62f4fc33066f677209777f4bcb8388c3933b65142ce259898
Seed:    20260509
"""
import hashlib
import json
import random
from itertools import combinations
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
PREREG = REPO / "surahs/Q096-al-alaq/preregs/Q096-F-04-sajda-cluster-prereg.md"
EXPECTED_SHA = "6620cbef4068e0c62f4fc33066f677209777f4bcb8388c3933b65142ce259898"
H111 = REPO / "findings/phase-b-hypotheses/csv/h-new-111.json"
OUT = REPO / "surahs/Q096-al-alaq/csv/q096-f-04.json"
SEED = 20260509

# Locked cluster identity (Sunni-conservative 14-surah base)
SAJDA_14 = [7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96]


def verify_sha():
    sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        raise SystemExit(f"PREREG SHA mismatch: {sha} != {EXPECTED_SHA}")


def load_fr_matrix():
    with open(H111) as f:
        d = json.load(f)
    ut = d["D_matrix_upper_triangular"]
    N = 114
    D = [[0.0] * N for _ in range(N)]
    for entry in ut:
        i, j, dist = entry
        D[i - 1][j - 1] = dist
        D[j - 1][i - 1] = dist
    return D


def mean_intra(D, surahs):
    pairs = list(combinations(surahs, 2))
    return sum(D[a - 1][b - 1] for a, b in pairs) / len(pairs)


def run():
    D = load_fr_matrix()
    obs_mean_A = mean_intra(D, SAJDA_14)

    # Cell A — uniform random 14-surah samples from {1, ..., 114}
    random.seed(SEED)
    n_perm = 10000
    null_means_A = []
    for _ in range(n_perm):
        sample = random.sample(range(1, 115), 14)
        null_means_A.append(mean_intra(D, sample))
    n_le_A = sum(1 for m in null_means_A if m <= obs_mean_A)
    p_A = n_le_A / n_perm
    null_p5_A = sorted(null_means_A)[int(0.05 * n_perm)]

    # Cell B — exclude Q 1
    random.seed(SEED + 1)
    pool_B = [s for s in range(1, 115) if s != 1]
    null_means_B = []
    for _ in range(n_perm):
        sample = random.sample(pool_B, 14)
        null_means_B.append(mean_intra(D, sample))
    n_le_B = sum(1 for m in null_means_B if m <= obs_mean_A)  # SAJDA_14 doesn't include Q 1
    p_B = n_le_B / n_perm
    null_p5_B = sorted(null_means_B)[int(0.05 * n_perm)]

    # MW-5 positive control: musabbiḥāt 5-cluster
    musab = [57, 59, 61, 62, 64]
    obs_mean_pc = mean_intra(D, musab)
    random.seed(SEED + 2)
    null_means_pc = []
    for _ in range(n_perm):
        sample = random.sample(range(1, 115), 5)
        null_means_pc.append(mean_intra(D, sample))
    n_le_pc = sum(1 for m in null_means_pc if m <= obs_mean_pc)
    p_pc = n_le_pc / n_perm

    pass_a = p_A <= 0.025
    pass_b = p_B <= 0.025
    pass_pc = p_pc <= 0.05

    if not pass_pc:
        verdict = "NULL-BROKEN (positive control failed)"
    elif pass_a and pass_b:
        verdict = "PASS-DIRECTED (both cells)"
    elif pass_a:
        verdict = "PARTIAL (Cell A only — sensitive to Q 1 exclusion)"
    elif pass_b:
        verdict = "WEIRD (Cell B only — flag for review)"
    else:
        verdict = "NULL"

    out = {
        "id": "Q096-F-04",
        "title": "Sajda-tilāwa 14-cluster Fisher-Rao cohesion",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": n_perm,
        "cluster": SAJDA_14,
        "obs_mean_intra_FR": obs_mean_A,
        "cell_A_uniform_random": {
            "null_mean": sum(null_means_A) / len(null_means_A),
            "null_p5": null_p5_A,
            "p_perm": p_A,
            "alpha_bon": 0.025,
            "pass": pass_a,
        },
        "cell_B_exclude_q1": {
            "null_mean": sum(null_means_B) / len(null_means_B),
            "null_p5": null_p5_B,
            "p_perm": p_B,
            "alpha_bon": 0.025,
            "pass": pass_b,
        },
        "mw5_positive_control_musabbihat": {
            "cluster": musab,
            "obs_mean_intra_FR": obs_mean_pc,
            "p_perm": p_pc,
            "pass": pass_pc,
        },
        "bonferroni_k": 2,
        "alpha_bon_per_cell": 0.025,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT}")
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    verify_sha()
    run()
