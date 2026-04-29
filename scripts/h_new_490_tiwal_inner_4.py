#!/usr/bin/env python3
"""H-NEW-490: al-sabʿ al-ṭiwāl inner-4 cohesion pre-registered confirmation."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-490-tiwal-inner-4-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-490.json"
SEED = 20260515
N_PERMS = 10000
ALPHA_BON = 0.05 / 3

SET_T = [2, 3, 4, 5]
SET_M = [57, 59, 61, 64]
SET_N = [1, 55, 67, 112]

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
    print(f"=== H-NEW-490 (ṭiwāl-inner-4) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\nα_bon: {ALPHA_BON:.4f}")
    D = load_D()

    rng_t = random.Random(SEED)
    rng_m = random.Random(SEED + 1)
    rng_n = random.Random(SEED + 2)

    dT = mean_pairwise(D, SET_T)
    pT = percentile_in_null(D, dT, 4, N_PERMS, rng_t)
    primary = pT <= 10.0
    print(f"\n--- PRIMARY: T={SET_T} (ṭiwāl-inner-4) ---")
    print(f"  d̄(T) = {dT:.4f}, pct = {pT:.2f}%, ≤10%: {primary}")
    print(f"  pairwise:")
    for a, b in combinations(SET_T, 2):
        print(f"    D({a},{b}) = {D[a][b]:.4f}")

    dM = mean_pairwise(D, SET_M)
    pM = percentile_in_null(D, dM, 4, N_PERMS, rng_m)
    mw5 = pM <= 10.0
    print(f"\n--- MW-5: M={SET_M} (musabbiḥāt-4) ---")
    print(f"  d̄(M) = {dM:.4f}, pct = {pM:.2f}%, ≤10%: {mw5}")

    dN = mean_pairwise(D, SET_N)
    pN = percentile_in_null(D, dN, 4, N_PERMS, rng_n)
    mw6 = 30.0 <= pN <= 70.0
    print(f"\n--- MW-6: N={SET_N} (diverse-4) ---")
    print(f"  d̄(N) = {dN:.4f}, pct = {pN:.2f}%, [30,70]: {mw6}")

    agg = primary and mw5 and mw6
    print(f"\n=== AGGREGATE ===")
    print(f"PRIMARY: {primary}  MW-5: {mw5}  MW-6: {mw6}")
    print(f"AGGREGATE H1 CONFIRMED: {agg}")

    out = {
        "id": "H-NEW-490", "prereg_sha": prereg_sha, "seed": SEED,
        "alpha_bon": ALPHA_BON,
        "primary": {"set": SET_T, "d": dT, "percentile": pT, "threshold": 10.0, "pass": primary},
        "mw5": {"set": SET_M, "d": dM, "percentile": pM, "threshold": 10.0, "pass": mw5},
        "mw6": {"set": SET_N, "d": dN, "percentile": pN, "range": [30.0, 70.0], "pass": mw6},
        "pairwise_T": {f"{a}-{b}": D[a][b] for a,b in combinations(SET_T, 2)},
        "pairwise_M": {f"{a}-{b}": D[a][b] for a,b in combinations(SET_M, 2)},
        "pairwise_N": {f"{a}-{b}": D[a][b] for a,b in combinations(SET_N, 2)},
        "aggregate_h1_confirmed": agg,
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
