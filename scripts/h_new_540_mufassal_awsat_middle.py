#!/usr/bin/env python3
"""H-NEW-540: mufaṣṣal-awsāṭ middle-cluster cohesion test."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-540-mufassal-awsat-middle-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-540.json"
SEED = 20260517
N_PERMS = 10000
ALPHA_BON = 0.05 / 3

SET_A = list(range(78, 93))  # 15 surahs, Q 78-92 mufaṣṣal-awsāṭ
SET_REPL = list(range(93, 115))  # 22 surahs mufaṣṣal-qiṣār (MW-5 replication)
SET_Cm = [26, 28, 37, 39, 41, 43, 45, 50, 52, 54, 56, 67, 68, 71, 75]  # 15 Meccan-mid

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
    print(f"=== H-NEW-540 (mufaṣṣal-awsāṭ middle) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\nα_bon: {ALPHA_BON:.4f}")
    assert len(SET_A) == 15 and len(SET_REPL) == 22 and len(SET_Cm) == 15
    D = load_D()

    rng_a = random.Random(SEED)
    rng_r = random.Random(SEED + 1)
    rng_c = random.Random(SEED + 2)

    dA = mean_pairwise(D, SET_A)
    pA = percentile_in_null(D, dA, 15, N_PERMS, rng_a)
    primary = pA <= 5.0
    print(f"\n--- PRIMARY: A={SET_A} (mufaṣṣal-awsāṭ Q 78-92, N=15) ---")
    print(f"  d̄(A) = {dA:.4f}, pct = {pA:.2f}%, ≤5%: {primary}")

    dR = mean_pairwise(D, SET_REPL)
    pR = percentile_in_null(D, dR, 22, N_PERMS, rng_r)
    mw5 = pR <= 1.0
    print(f"\n--- MW-5 REPLICATION: qiṣār Q 93-114 (N=22) ---")
    print(f"  d̄ = {dR:.4f}, pct = {pR:.2f}%, ≤1%: {mw5}")

    dCm = mean_pairwise(D, SET_Cm)
    pCm = percentile_in_null(D, dCm, 15, N_PERMS, rng_c)
    mw6 = 30.0 <= pCm <= 70.0
    print(f"\n--- MW-6 NULL: Meccan-mid-15 {SET_Cm} ---")
    print(f"  d̄ = {dCm:.4f}, pct = {pCm:.2f}%, [30,70]: {mw6}")

    agg = primary and mw5 and mw6
    print(f"\n=== AGGREGATE ===")
    print(f"PRIMARY: {primary}  MW-5: {mw5}  MW-6: {mw6}")
    print(f"AGGREGATE H1 CONFIRMED: {agg}")
    print(f"\nComparison: awsāṭ pct={pA:.2f}% vs qiṣār pct={pR:.2f}%")

    out = {
        "id": "H-NEW-540", "prereg_sha": prereg_sha, "seed": SEED,
        "alpha_bon": ALPHA_BON,
        "primary": {"set": SET_A, "n": 15, "d": dA, "percentile": pA, "threshold": 5.0, "pass": primary},
        "mw5_replication": {"set": SET_REPL, "n": 22, "d": dR, "percentile": pR, "threshold": 1.0, "pass": mw5},
        "mw6": {"set": SET_Cm, "n": 15, "d": dCm, "percentile": pCm, "range": [30.0, 70.0], "pass": mw6},
        "aggregate_h1_confirmed": agg,
        "awsat_vs_qisar_percentile_gap": pA - pR,
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
