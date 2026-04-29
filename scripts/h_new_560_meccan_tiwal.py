#!/usr/bin/env python3
"""H-NEW-560: Meccan-only ṭiwāl cohesion test."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-560-meccan-tiwal-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-560.json"
SEED = 20260519
N_PERMS = 10000
ALPHA_BON = 0.05 / 3

SET_MECCAN_T = list(range(50, 57)) + list(range(67, 78))  # N=18
SET_FULL_T = list(range(50, 78))  # N=28
SET_MEDINAN_T = list(range(57, 67))  # N=10

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
    print(f"=== H-NEW-560 (Meccan-only ṭiwāl) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}")
    assert len(SET_MECCAN_T) == 18 and len(SET_FULL_T) == 28 and len(SET_MEDINAN_T) == 10
    D = load_D()

    rng_m = random.Random(SEED)
    rng_f = random.Random(SEED + 1)
    rng_d = random.Random(SEED + 2)

    dM = mean_pairwise(D, SET_MECCAN_T)
    pM = percentile_in_null(D, dM, 18, N_PERMS, rng_m)
    primary = pM <= 10.0
    print(f"\n--- PRIMARY: Meccan-ṭiwāl {SET_MECCAN_T} N=18 ---")
    print(f"  d̄ = {dM:.4f}, pct = {pM:.2f}%, ≤10%: {primary}")

    dF = mean_pairwise(D, SET_FULL_T)
    pF = percentile_in_null(D, dF, 28, N_PERMS, rng_f)
    mw5 = 15.0 <= pF <= 35.0  # replicate H-550 NULL near 23%
    print(f"\n--- MW-5 REPLICATE: full ṭiwāl Q50-77 N=28 ---")
    print(f"  d̄ = {dF:.4f}, pct = {pF:.2f}%, [15,35]: {mw5}")

    dDn = mean_pairwise(D, SET_MEDINAN_T)
    pDn = percentile_in_null(D, dDn, 10, N_PERMS, rng_d)
    mw6 = pDn <= 15.0
    print(f"\n--- MW-6: Medinan-ṭiwāl Q57-66 N=10 ---")
    print(f"  d̄ = {dDn:.4f}, pct = {pDn:.2f}%, ≤15%: {mw6}")

    agg = primary and mw5 and mw6
    print(f"\n=== AGGREGATE H1: {agg} ===")

    out = {
        "id": "H-NEW-560", "prereg_sha": prereg_sha, "seed": SEED,
        "primary_meccan_tiwal": {"set": SET_MECCAN_T, "n": 18, "d": dM, "percentile": pM, "pass": primary},
        "mw5_full_tiwal": {"set": SET_FULL_T, "n": 28, "d": dF, "percentile": pF, "pass": mw5},
        "mw6_medinan_tiwal": {"set": SET_MEDINAN_T, "n": 10, "d": dDn, "percentile": pDn, "pass": mw6},
        "aggregate_h1_confirmed": agg,
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
