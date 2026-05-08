#!/usr/bin/env python3
"""muʿawwidhāt cluster cohesion test."""
import hashlib, json, os, sys, random
import numpy as np

PREREG = "/Users/grey/Downloads/quran/surahs/muawwidhat-cluster-cohesion-prereg.md"
PREREG_SHA = "8ff693166ff9ae19696c8aa8a33e853a8d9aa0f4bc8bc08da1cafd1805556d13"
OUT = "/Users/grey/Downloads/quran/surahs/muawwidhat-cluster-cohesion.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA: print("FATAL", file=sys.stderr); sys.exit(1)
    print(f"[OK] SHA verified: {sha}")

def main():
    verify()
    with open("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json") as f:
        d111 = json.load(f)
    D = np.zeros((114,114))
    for elt in d111["D_matrix_upper_triangular"]:
        i, j, dist = elt[0], elt[1], elt[2]
        D[i-1][j-1] = dist
        D[j-1][i-1] = dist
    # observed: muawwidhat-3 cluster
    cluster = [112, 113, 114]
    pairs = [(112,113),(112,114),(113,114)]
    obs_mean = np.mean([D[a-1][b-1] for a,b in pairs])
    # null: 10000 random 3-subsets
    rng = random.Random(20260428)
    n_perm = 10000
    null_means = []
    all_surahs = list(range(1, 115))
    for _ in range(n_perm):
        sample = rng.sample(all_surahs, 3)
        a, b, c = sample
        m = np.mean([D[a-1][b-1], D[a-1][c-1], D[b-1][c-1]])
        null_means.append(m)
    null_means = np.array(null_means)
    p = (null_means <= obs_mean).sum() / n_perm
    # also strict-pair muʿawwidhatān: just Q113-Q114
    obs_113_114 = D[112][113]
    # null: random pairs
    n_perm_pair = 10000
    null_pair = []
    for _ in range(n_perm_pair):
        a, b = rng.sample(all_surahs, 2)
        null_pair.append(D[a-1][b-1])
    null_pair = np.array(null_pair)
    p_pair = (null_pair <= obs_113_114).sum() / n_perm_pair
    result = {
        "preregistration_id": "muawwidhat-cluster-F-01",
        "prereg_sha": PREREG_SHA,
        "n_perm": n_perm,
        "muawwidhat_3_cluster": cluster,
        "muawwidhat_3_pairs": [list(p) for p in pairs],
        "muawwidhat_3_pair_distances": {f"{a}-{b}": float(D[a-1][b-1]) for a,b in pairs},
        "muawwidhat_3_mean_pairwise_distance": float(obs_mean),
        "null_mean_3subset_distribution": {
            "mean": float(null_means.mean()),
            "std": float(null_means.std()),
            "min": float(null_means.min()),
            "p1": float(np.percentile(null_means, 1)),
            "p5": float(np.percentile(null_means, 5)),
            "median": float(np.median(null_means)),
        },
        "permutation_p_3subset": float(p),
        "muawwidhatān_strict_pair": [113, 114],
        "muawwidhatān_strict_distance": float(obs_113_114),
        "null_pair_distribution": {
            "mean": float(null_pair.mean()),
            "p1": float(np.percentile(null_pair, 1)),
            "p5": float(np.percentile(null_pair, 5)),
        },
        "permutation_p_strict_pair": float(p_pair),
        "verdict_3cluster": "VINDICATED" if p <= 0.01 else "DIRECTIONAL" if p <= 0.05 else "NULL",
        "verdict_strict_pair": "VINDICATED" if p_pair <= 0.01 else "DIRECTIONAL" if p_pair <= 0.05 else "NULL",
    }
    with open(OUT, "w") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\n=== Muʿawwidhāt-3 cluster {cluster} ===")
    for a,b in pairs:
        print(f"   D[{a},{b}] = {D[a-1][b-1]:.4f}")
    print(f"   Mean pairwise: {obs_mean:.4f}")
    print(f"   Null mean (10000 random 3-subsets): {null_means.mean():.4f}, p1: {np.percentile(null_means,1):.4f}")
    print(f"   Permutation p: {p:.6f}")
    print(f"   Verdict 3-cluster: {result['verdict_3cluster']}")
    print(f"\n=== Muʿawwidhatān strict {[113,114]} ===")
    print(f"   D[113,114] = {obs_113_114:.4f}")
    print(f"   Null mean (10000 random pairs): {null_pair.mean():.4f}; p1: {np.percentile(null_pair,1):.4f}")
    print(f"   Permutation p: {p_pair:.6f}")
    print(f"   Verdict strict pair: {result['verdict_strict_pair']}")
    print(f"[OK] -> {OUT}")

if __name__=="__main__": main()
