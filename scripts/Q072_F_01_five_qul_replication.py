#!/usr/bin/env python3
"""Q072-F-01 — 5-qul opener cluster {Q 72, 109, 112, 113, 114} FR-cohesion REPLICATION.

Pre-reg: surahs/Q072-al-jinn/preregs/Q072-F-01-five-qul-cluster-fr-cohesion-prereg.md
Pre-reg SHA256: b4faaeeea844cf372b8e101fa2d53994b11c8db25e789728c36bd7a719b4f540

Rules-tuple: (no-tashkeel, QAC stem-roots top-K=500 per H-NEW-111, dirichlet-alpha=0.5,
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi script, mushaf order)
Seed: 20260509  |  Perms: 10000  |  Direction: PASS (predicted p<0.01)
"""
import hashlib
import json
import os
import random
import statistics
import sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q072-al-jinn/preregs/Q072-F-01-five-qul-cluster-fr-cohesion-prereg.md"
EXPECTED_SHA = "b4faaeeea844cf372b8e101fa2d53994b11c8db25e789728c36bd7a719b4f540"

FR_PATH = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q072-al-jinn/csv/Q072-F-01.json"

SEED = 20260509
N_PERM = 10000
ALPHA = 0.05
PREDICTED_P_BOUND = 0.01

CLUSTER = [72, 109, 112, 113, 114]
PC = [69, 97, 101]  # H-NEW-1190 sub-sample MW-5 positive control


def verify_sha():
    actual = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def build_dist_dict(fr_json):
    """Build symmetric pairwise FR-distance dict from D_matrix_upper_triangular."""
    d = {}
    for row in fr_json["D_matrix_upper_triangular"]:
        i, j, v = row
        d[(i, j)] = v
        d[(j, i)] = v
    return d


def cluster_mean(cluster, dist):
    """Mean pairwise FR distance within a surah subset."""
    s = []
    n = len(cluster)
    for ii in range(n):
        for jj in range(ii + 1, n):
            a, b = cluster[ii], cluster[jj]
            s.append(dist[(a, b)])
    return statistics.mean(s)


def perm_null(k, dist, rng, n_perm):
    """Random-k-subset-of-114 null distribution of within-mean FR."""
    surahs = list(range(1, 115))
    null = []
    for _ in range(n_perm):
        sample = rng.sample(surahs, k)
        null.append(cluster_mean(sample, dist))
    return null


def main():
    verify_sha()
    fr = json.load(open(FR_PATH))
    dist = build_dist_dict(fr)

    # Primary cluster
    obs_within = cluster_mean(CLUSTER, dist)

    # All pairwise distances inside cluster (for reporting)
    cluster_pairs = []
    for i, a in enumerate(CLUSTER):
        for b in CLUSTER[i + 1:]:
            cluster_pairs.append({"i": a, "j": b, "d": dist[(a, b)]})

    # Null: random 5-subsets
    rng = random.Random(SEED)
    null_5 = perm_null(5, dist, rng, N_PERM)
    null_mean = statistics.mean(null_5)
    null_sd = statistics.stdev(null_5)
    p_le = sum(1 for x in null_5 if x <= obs_within) / N_PERM
    z = (obs_within - null_mean) / null_sd if null_sd > 0 else 0.0

    # MW-5 PC: H-NEW-1190 sub-sample {69, 97, 101} vs random-3-subset null
    obs_pc = cluster_mean(PC, dist)
    rng_pc = random.Random(SEED + 1)
    null_3 = perm_null(3, dist, rng_pc, N_PERM)
    pc_null_mean = statistics.mean(null_3)
    p_pc = sum(1 for x in null_3 if x <= obs_pc) / N_PERM

    # Q 72's distance to each of the 4-qul sub-cluster (descriptive)
    q72_to_4qul = {f"Q72-Q{s}": dist[(72, s)] for s in [109, 112, 113, 114]}
    q72_to_4qul_mean = statistics.mean(q72_to_4qul.values())

    # Verdict
    primary_pass = p_le <= ALPHA
    primary_strong = p_le <= PREDICTED_P_BOUND
    pc_pass = p_pc <= ALPHA
    direction_correct = obs_within < null_mean

    if not direction_correct:
        verdict = "NULL (pre-commit-violation: direction-reversed)"
    elif primary_strong and pc_pass:
        verdict = "PASS-STRONG (predicted p<0.01 met; PC passes)"
    elif primary_pass and pc_pass:
        verdict = "PASS (p<0.05; PC passes)"
    elif primary_pass and not pc_pass:
        verdict = "DIRECTIONAL (primary passes but MW-5 PC fails)"
    else:
        verdict = "DIRECTIONAL (direction correct, p>0.05)"

    out = {
        "test_id": "Q072-F-01",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha": ALPHA,
        "predicted_p_bound": PREDICTED_P_BOUND,
        "cluster": CLUSTER,
        "cluster_within_mean_fr": obs_within,
        "cluster_pairs": cluster_pairs,
        "q72_to_4qul_distances": q72_to_4qul,
        "q72_to_4qul_mean": q72_to_4qul_mean,
        "null_random5": {
            "mean": null_mean,
            "sd": null_sd,
            "min": min(null_5),
            "max": max(null_5),
            "p_one_sided_le": p_le,
            "z_score": z,
        },
        "mw5_pc": {
            "cluster": PC,
            "name": "H-NEW-1190 sub-sample (wa-ma adraka ma)",
            "obs_within_mean": obs_pc,
            "null_random3_mean": pc_null_mean,
            "p_one_sided_le": p_pc,
            "pass": pc_pass,
        },
        "direction_correct": direction_correct,
        "primary_pass_alpha": primary_pass,
        "primary_pass_predicted_bound": primary_strong,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    json.dump(out, open(OUT_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Q072-F-01 verdict: {verdict}")
    print(f"  obs within-mean = {obs_within:.4f}; null mean = {null_mean:.4f}; sd = {null_sd:.4f}")
    print(f"  p (one-sided ≤) = {p_le:.4f}; z = {z:.3f}")
    print(f"  PC obs = {obs_pc:.4f}; PC null = {pc_null_mean:.4f}; PC p = {p_pc:.4f}")
    print(f"  Q72→{{109,112,113,114}} mean = {q72_to_4qul_mean:.4f}")
    print(f"Written: {OUT_PATH}")


if __name__ == "__main__":
    main()
