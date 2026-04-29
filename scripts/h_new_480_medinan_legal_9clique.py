#!/usr/bin/env python3
"""H-NEW-480: Medinan social-legal 9-clique cohesion test."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-480-medinan-legal-9clique-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-480.json"
SEED = 20260514
N_PERMS = 10000
ALPHA_BON = 0.05 / 3

SET_A_LEGAL = [2, 3, 4, 5, 24, 33, 48, 49, 64]
SET_B_MUSABBI_MUFASSAL = [50, 54, 57, 59, 61, 64, 67, 76, 78]
SET_C_DIVERSE = [1, 12, 36, 38, 55, 67, 90, 101, 114]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist; mat[j][i] = dist
    return mat

def mean_pairwise(D, subset):
    xs = list(subset)
    vals = [D[a][b] for a, b in combinations(xs, 2)]
    return sum(vals) / len(vals) if vals else 0.0

def percentile_in_null(D, observed, size, n_perms, rng):
    all_surahs = list(range(1, 115))
    below = 0
    for _ in range(n_perms):
        sub = rng.sample(all_surahs, size)
        if mean_pairwise(D, sub) <= observed:
            below += 1
    return 100.0 * below / n_perms

def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-480 (Medinan-legal 9-clique) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\nα_bon: {ALPHA_BON:.4f}")
    D = load_D()

    # Need separate RNG streams for deterministic reproduction
    rng_a = random.Random(SEED)
    rng_b = random.Random(SEED + 1)
    rng_c = random.Random(SEED + 2)

    # PRIMARY
    dA = mean_pairwise(D, SET_A_LEGAL)
    pA = percentile_in_null(D, dA, 9, N_PERMS, rng_a)
    primary_pass = pA <= 10.0
    print(f"\n--- PRIMARY: Set A = {SET_A_LEGAL} (Medinan legal) ---")
    print(f"  d̄(A) = {dA:.4f}, percentile = {pA:.2f}%")
    print(f"  Pre-commit ≤10%: {primary_pass}")

    # Print individual pairwise distances
    print(f"  pairwise distances within A:")
    for a, b in combinations(SET_A_LEGAL, 2):
        print(f"    D({a}, {b}) = {D[a][b]:.4f}")

    # MW-5
    dB = mean_pairwise(D, SET_B_MUSABBI_MUFASSAL)
    pB = percentile_in_null(D, dB, 9, N_PERMS, rng_b)
    mw5_pass = pB <= 25.0
    print(f"\n--- MW-5 POSITIVE: Set B = {SET_B_MUSABBI_MUFASSAL} (musabbiḥāt+mufaṣṣal) ---")
    print(f"  d̄(B) = {dB:.4f}, percentile = {pB:.2f}%")
    print(f"  Pre-commit ≤25%: {mw5_pass}")

    # MW-6
    dC = mean_pairwise(D, SET_C_DIVERSE)
    pC = percentile_in_null(D, dC, 9, N_PERMS, rng_c)
    mw6_pass = 30.0 <= pC <= 70.0
    print(f"\n--- MW-6 NULL: Set C = {SET_C_DIVERSE} (diverse-9) ---")
    print(f"  d̄(C) = {dC:.4f}, percentile = {pC:.2f}%")
    print(f"  Pre-commit [30%, 70%]: {mw6_pass}")

    # Aggregate
    aggregate = primary_pass and mw5_pass and mw6_pass
    print(f"\n=== AGGREGATE ===")
    print(f"PRIMARY: {primary_pass}  MW-5: {mw5_pass}  MW-6: {mw6_pass}")
    print(f"AGGREGATE H1 CONFIRMED: {aggregate}")

    out = {
        "id": "H-NEW-480", "prereg_sha": prereg_sha, "seed": SEED,
        "alpha_bon": ALPHA_BON,
        "primary": {"set": SET_A_LEGAL, "d": dA, "percentile": pA, "threshold": 10.0, "pass": primary_pass},
        "mw5": {"set": SET_B_MUSABBI_MUFASSAL, "d": dB, "percentile": pB, "threshold": 25.0, "pass": mw5_pass},
        "mw6": {"set": SET_C_DIVERSE, "d": dC, "percentile": pC, "range": [30.0, 70.0], "pass": mw6_pass},
        "pairwise_within_A": {f"{a}-{b}": D[a][b] for a,b in combinations(SET_A_LEGAL, 2)},
        "aggregate_h1_confirmed": aggregate,
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
