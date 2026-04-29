#!/usr/bin/env python3
"""H-NEW-630: Q 67-114 super-cluster sub-structure test (flat vs hierarchical)."""
import hashlib
import json
import random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-630-supercluster-substructure-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-630.json"
SEED = 20260432
N_PERMS = 10000

CLUSTER_A = list(range(67, 78))   # Q 67-77 (N=11)
CLUSTER_B = list(range(78, 100))  # Q 78-99 (N=22)
CLUSTER_C = list(range(100, 115)) # Q 100-114 (N=15)
SUPER = CLUSTER_A + CLUSTER_B + CLUSTER_C  # 48 surahs


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def mean_pairwise(D, subset):
    return sum(D[a][b] for a, b in combinations(subset, 2)) / max(1, len(list(combinations(subset, 2))))


def mean_cross(D, X, Y):
    pairs = [(a, b) for a in X for b in Y]
    return sum(D[a][b] for a, b in pairs) / len(pairs)


def percentile_in_null(D, observed, size, n_perms, rng):
    all_surahs = list(range(1, 115))
    below = 0
    for _ in range(n_perms):
        sub = rng.sample(all_surahs, size)
        if mean_pairwise(D, sub) <= observed:
            below += 1
    return 100.0 * below / n_perms


def cross_null(D, observed, size_x, size_y, n_perms, rng):
    """Null: pick random size_x and size_y disjoint subsets, compute cross-d̄."""
    all_surahs = list(range(1, 115))
    below = 0
    for _ in range(n_perms):
        pool = rng.sample(all_surahs, size_x + size_y)
        X = pool[:size_x]; Y = pool[size_x:]
        if mean_cross(D, X, Y) <= observed:
            below += 1
    return 100.0 * below / n_perms


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-630 (Q 67-114 super-cluster sub-structure) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\n")
    D = load_D()
    rng = random.Random(SEED)

    # Within-cluster d̄ + percentiles
    dA = mean_pairwise(D, CLUSTER_A)
    dB = mean_pairwise(D, CLUSTER_B)
    dC = mean_pairwise(D, CLUSTER_C)
    pA = percentile_in_null(D, dA, len(CLUSTER_A), N_PERMS, random.Random(SEED + 1))
    pB = percentile_in_null(D, dB, len(CLUSTER_B), N_PERMS, random.Random(SEED + 2))
    pC = percentile_in_null(D, dC, len(CLUSTER_C), N_PERMS, random.Random(SEED + 3))

    print(f"--- WITHIN-CLUSTER ---")
    print(f"  A (Q67-77, N=11): d̄={dA:.4f}, %ile={pA:.2f}")
    print(f"  B (Q78-99, N=22): d̄={dB:.4f}, %ile={pB:.2f}")
    print(f"  C (Q100-114, N=15): d̄={dC:.4f}, %ile={pC:.2f}")

    # Between-cluster cross d̄
    dAB = mean_cross(D, CLUSTER_A, CLUSTER_B)
    dAC = mean_cross(D, CLUSTER_A, CLUSTER_C)
    dBC = mean_cross(D, CLUSTER_B, CLUSTER_C)
    pAB = cross_null(D, dAB, len(CLUSTER_A), len(CLUSTER_B), N_PERMS, random.Random(SEED + 4))
    pAC = cross_null(D, dAC, len(CLUSTER_A), len(CLUSTER_C), N_PERMS, random.Random(SEED + 5))
    pBC = cross_null(D, dBC, len(CLUSTER_B), len(CLUSTER_C), N_PERMS, random.Random(SEED + 6))

    print(f"\n--- BETWEEN-CLUSTER ---")
    print(f"  A-B (cross): d̄={dAB:.4f}, %ile={pAB:.2f}")
    print(f"  A-C (cross): d̄={dAC:.4f}, %ile={pAC:.2f}")
    print(f"  B-C (cross): d̄={dBC:.4f}, %ile={pBC:.2f}")

    # Hierarchy: mean Δ = mean(between - within) over 3 cross-pairs
    delta_AB = dAB - (dA + dB) / 2
    delta_AC = dAC - (dA + dC) / 2
    delta_BC = dBC - (dB + dC) / 2
    mean_delta = (delta_AB + delta_AC + delta_BC) / 3
    print(f"\n--- HIERARCHY ---")
    print(f"  Δ(A-B) = {delta_AB:.4f}")
    print(f"  Δ(A-C) = {delta_AC:.4f}")
    print(f"  Δ(B-C) = {delta_BC:.4f}")
    print(f"  mean Δ = {mean_delta:.4f}  (positive = hierarchical)")

    # Permutation null for mean Δ: shuffle cluster labels among 48 super-cluster members
    print(f"\n--- PERMUTATION NULL ({N_PERMS} perms) ---")
    rng_perm = random.Random(SEED + 100)
    null_deltas = []
    sizes = [len(CLUSTER_A), len(CLUSTER_B), len(CLUSTER_C)]
    for _ in range(N_PERMS):
        shuffled = SUPER[:]
        rng_perm.shuffle(shuffled)
        idx = 0
        Cs = []
        for sz in sizes:
            Cs.append(shuffled[idx:idx + sz])
            idx += sz
        dA_n = mean_pairwise(D, Cs[0])
        dB_n = mean_pairwise(D, Cs[1])
        dC_n = mean_pairwise(D, Cs[2])
        dAB_n = mean_cross(D, Cs[0], Cs[1])
        dAC_n = mean_cross(D, Cs[0], Cs[2])
        dBC_n = mean_cross(D, Cs[1], Cs[2])
        delta_n = ((dAB_n - (dA_n + dB_n)/2) + (dAC_n - (dA_n + dC_n)/2) + (dBC_n - (dB_n + dC_n)/2)) / 3
        null_deltas.append(delta_n)

    p_delta = sum(1 for d in null_deltas if d >= mean_delta) / len(null_deltas)
    print(f"  Empirical p(mean Δ ≥ observed) = {p_delta:.5f}")

    # Verdict
    alpha_bon = 0.05 / 7
    within_strict = pA <= 0.71 and pB <= 0.71 and pC <= 0.71
    within_directional = pA <= 5.0 and pB <= 5.0 and pC <= 5.0
    hierarchy_strict = mean_delta > 0.05 and p_delta <= alpha_bon
    hierarchy_directional = mean_delta > 0 and p_delta <= 0.05

    if within_strict and hierarchy_strict:
        verdict = "STRICT-HIERARCHICAL"
    elif within_directional and hierarchy_directional:
        verdict = "DIRECTIONAL-HIERARCHICAL"
    elif within_directional and not hierarchy_directional:
        verdict = "FLAT-COHESION (super-cluster confirmed; no internal hierarchy)"
    elif mean_delta < 0:
        verdict = "ANTI-HIERARCHICAL (between < within — implausible flag)"
    else:
        verdict = "MIXED"

    print(f"\n=== VERDICT: {verdict} ===")
    print(f"  Bonferroni-7 α = {alpha_bon:.5f}")

    out = {
        "id": "H-NEW-630",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "clusters": {"A_Q67-77": CLUSTER_A, "B_Q78-99": CLUSTER_B, "C_Q100-114": CLUSTER_C},
        "within": {
            "A": {"d": dA, "percentile": pA, "n": len(CLUSTER_A)},
            "B": {"d": dB, "percentile": pB, "n": len(CLUSTER_B)},
            "C": {"d": dC, "percentile": pC, "n": len(CLUSTER_C)},
        },
        "between": {
            "AB": {"d": dAB, "percentile": pAB},
            "AC": {"d": dAC, "percentile": pAC},
            "BC": {"d": dBC, "percentile": pBC},
        },
        "hierarchy": {
            "delta_AB": delta_AB,
            "delta_AC": delta_AC,
            "delta_BC": delta_BC,
            "mean_delta": mean_delta,
            "perm_p": p_delta,
            "alpha_bon": alpha_bon,
        },
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
