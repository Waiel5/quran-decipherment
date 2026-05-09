#!/usr/bin/env python3
"""
Q089-F-04 — Q 89 oath-cluster centrality + 2-tier structure.
Pre-reg SHA256 lock: e7e791dbb40229f42f9db9f628f35d2248bc326ccff2b191c81f5f6084de89f3
Seed: 20260509
"""
import json
import hashlib
import sys
import random
from pathlib import Path
import statistics

PREREG_PATH = Path(__file__).resolve().parent.parent / "preregs" / "Q089-F-04-oath-cluster-centrality-prereg.md"
PREREG_SHA = "e7e791dbb40229f42f9db9f628f35d2248bc326ccff2b191c81f5f6084de89f3"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "csv" / "Q089-F-04.json"
SEED = 20260509
N_PERM = 10000

H_NEW_111_PATH = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"

OATH_CLUSTER = [37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103]
TIER_1 = [85, 86, 89, 91, 92, 93, 95, 100, 103]  # core (per Q037-F-04 proposal)
TIER_2 = [37, 51, 52, 53, 77, 79]


def verify_sha():
    h = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if h != PREREG_SHA:
        sys.exit(f"PREREG SHA MISMATCH: expected {PREREG_SHA}, got {h}")
    print(f"PREREG SHA verified: {h}")


def load_fr_matrix():
    with open(H_NEW_111_PATH) as f:
        d = json.load(f)
    N = 114
    M = [[0.0] * (N + 1) for _ in range(N + 1)]
    for entry in d["D_matrix_upper_triangular"]:
        i, j, dst = entry
        M[i][j] = dst
        M[j][i] = dst
    return M


def main():
    verify_sha()
    random.seed(SEED)

    M = load_fr_matrix()
    N = 114
    target = 89

    # D_oath_q89: mean dist from Q 89 to other 14 oath-cluster members
    others_in_O = [s for s in OATH_CLUSTER if s != target]
    D_oath_q89 = statistics.mean(M[target][s] for s in others_in_O)

    # D_random null: 14-subset randomization
    eligible = [s for s in range(1, N + 1) if s != target]
    null_means = []
    for _ in range(N_PERM):
        R = random.sample(eligible, 14)
        null_means.append(statistics.mean(M[target][s] for s in R))
    n_le = sum(1 for x in null_means if x <= D_oath_q89)
    perm_p = n_le / N_PERM

    # Centrality ranking: each cluster member's mean dist to other 14 cluster members
    centrality = {}
    for s in OATH_CLUSTER:
        others = [s2 for s2 in OATH_CLUSTER if s2 != s]
        centrality[s] = statistics.mean(M[s][o] for o in others)
    rank_ordered = sorted(centrality.items(), key=lambda x: x[1])
    q89_rank = next(i for i, (s, _) in enumerate(rank_ordered, 1) if s == target)

    # H2 — TIER 1 vs TIER 2
    M_t1 = statistics.mean(M[target][s] for s in TIER_1 if s != target)
    M_t2 = statistics.mean(M[target][s] for s in TIER_2)
    h2_pass = M_t1 < M_t2

    # H1 pass
    h1_pass = perm_p <= 0.025

    if h1_pass and h2_pass:
        verdict = "CONFIRMED"
    elif h1_pass or h2_pass:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    # Within-cluster median pairwise FR
    pairwise = []
    for i, a in enumerate(OATH_CLUSTER):
        for b in OATH_CLUSTER[i + 1:]:
            pairwise.append(M[a][b])
    intra_median = statistics.median(pairwise)
    q89_row_median = statistics.median(M[target][s] for s in OATH_CLUSTER if s != target)

    # Q 89's own corpus-mean for context
    corpus_mean = statistics.mean(M[target][s] for s in range(1, N + 1) if s != target)

    out = {
        "test_id": "Q089-F-04",
        "prereg_sha256": PREREG_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "h1": {
            "D_oath_q89": D_oath_q89,
            "null_mean": statistics.mean(null_means),
            "null_min": min(null_means),
            "null_max": max(null_means),
            "perm_p_one_sided": perm_p,
            "alpha_bon": 0.025,
            "pass": h1_pass
        },
        "h2": {
            "M_t1_core_mean": M_t1,
            "M_t2_periphery_mean": M_t2,
            "M_t2_minus_M_t1": M_t2 - M_t1,
            "tier_1_members": TIER_1,
            "tier_2_members": TIER_2,
            "pass": h2_pass
        },
        "centrality": {
            "ranking": [{"rank": i + 1, "surah": s, "mean_dist_to_other_14": d}
                        for i, (s, d) in enumerate(rank_ordered)],
            "q89_rank_within_15": q89_rank,
            "intra_cluster_pairwise_median": intra_median,
            "q89_row_median_to_others": q89_row_median,
            "q89_corpus_mean_dist": corpus_mean
        },
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "verdict": verdict
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(out, f, indent=2)
    print(f"VERDICT: {verdict}")
    print(f"D_oath_q89 = {D_oath_q89:.4f}; null_mean = {statistics.mean(null_means):.4f}; perm_p = {perm_p:.4f}")
    print(f"Q 89 rank within 15-cluster centrality: {q89_rank}/15")
    print(f"M_t1 (core, excl Q89) = {M_t1:.4f}; M_t2 (periphery) = {M_t2:.4f}; diff = {M_t2 - M_t1:.4f}")
    print()
    print("Centrality ranking:")
    for i, (s, d) in enumerate(rank_ordered, 1):
        marker = " <-- Q 89" if s == target else ""
        tier = "T1" if s in TIER_1 else "T2"
        print(f"  rank {i:2d}: Q {s:3d} ({tier}) mean_dist={d:.4f}{marker}")


if __name__ == "__main__":
    main()
