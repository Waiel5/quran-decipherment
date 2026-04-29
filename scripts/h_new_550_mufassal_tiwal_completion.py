#!/usr/bin/env python3
"""H-NEW-550: mufaṣṣal-ṭiwāl (Q 50-77) cohesion — tripartite completion."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-550-mufassal-tiwal-completion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-550.json"
SEED = 20260518
N_PERMS = 10000
ALPHA_BON = 0.05 / 3

SET_T = list(range(50, 78))  # 28 surahs Q 50-77
SET_AWSAT = list(range(78, 93))  # 15 surahs
SET_DIVERSE = [1, 2, 3, 12, 18, 19, 20, 22, 24, 26, 28, 30, 33, 36, 37, 38, 40, 42, 45, 47, 48, 49, 79, 85, 90, 96, 99, 110]

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
    print(f"=== H-NEW-550 (mufaṣṣal-ṭiwāl completion) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\nα_bon: {ALPHA_BON:.4f}")
    assert len(SET_T) == 28 and len(SET_AWSAT) == 15 and len(SET_DIVERSE) == 28
    D = load_D()

    rng_t = random.Random(SEED)
    rng_a = random.Random(SEED + 1)
    rng_d = random.Random(SEED + 2)

    dT = mean_pairwise(D, SET_T)
    pT = percentile_in_null(D, dT, 28, N_PERMS, rng_t)
    primary = pT <= 5.0
    gradient_ok = 0.70 <= dT <= 0.90
    print(f"\n--- PRIMARY: T=Q50-77 (ṭiwāl, N=28) ---")
    print(f"  d̄(T) = {dT:.4f}, pct = {pT:.2f}%, ≤5%: {primary}")
    print(f"  gradient [0.70, 0.90]: {gradient_ok}")

    dA = mean_pairwise(D, SET_AWSAT)
    pA = percentile_in_null(D, dA, 15, N_PERMS, rng_a)
    mw5 = pA <= 1.0
    print(f"\n--- MW-5 REPLICATION: awsāṭ Q78-92 (N=15) ---")
    print(f"  d̄ = {dA:.4f}, pct = {pA:.2f}%, ≤1%: {mw5}")

    dDiv = mean_pairwise(D, SET_DIVERSE)
    pDiv = percentile_in_null(D, dDiv, 28, N_PERMS, rng_d)
    mw6 = 30.0 <= pDiv <= 70.0
    print(f"\n--- MW-6 DIVERSE-28 ---")
    print(f"  d̄ = {dDiv:.4f}, pct = {pDiv:.2f}%, [30,70]: {mw6}")

    agg = primary and mw5 and mw6
    print(f"\n=== AGGREGATE ===")
    print(f"PRIMARY: {primary}  MW-5: {mw5}  MW-6: {mw6}")
    print(f"AGGREGATE H1 CONFIRMED: {agg}")
    print(f"\nTripartite gradient: ṭiwāl={dT:.4f} > awsāṭ={dA:.4f} > qiṣār (~0.37)")

    out = {
        "id": "H-NEW-550", "prereg_sha": prereg_sha, "seed": SEED,
        "alpha_bon": ALPHA_BON,
        "primary": {"set": SET_T, "n": 28, "d": dT, "percentile": pT, "threshold": 5.0, "pass": primary, "gradient_ok": gradient_ok},
        "mw5_awsat": {"set": SET_AWSAT, "n": 15, "d": dA, "percentile": pA, "threshold": 1.0, "pass": mw5},
        "mw6_diverse": {"set": SET_DIVERSE, "n": 28, "d": dDiv, "percentile": pDiv, "range": [30.0, 70.0], "pass": mw6},
        "aggregate_h1_confirmed": agg,
        "tripartite_gradient": {"tiwal_d": dT, "awsat_d": dA, "qisar_d_from_h500": 0.3729},
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
