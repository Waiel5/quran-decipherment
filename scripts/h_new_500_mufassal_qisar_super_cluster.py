#!/usr/bin/env python3
"""H-NEW-500: mufaṣṣal-qiṣār 22-surah super-cluster cohesion test."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-500-mufassal-qisar-super-cluster-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-500.json"
SEED = 20260516
N_PERMS = 10000
ALPHA_BON = 0.05 / 3

SET_Q = list(range(93, 115))  # 22 surahs
SET_QI = list(range(103, 115))  # 12 surahs inner
SET_Cm = [26, 27, 28, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 50, 51, 52, 54, 55, 56, 67, 68, 71]  # 22 Meccan-mid

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
    print(f"=== H-NEW-500 (mufaṣṣal-qiṣār super-cluster) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\nα_bon: {ALPHA_BON:.4f}")
    assert len(SET_Q) == 22 and len(SET_QI) == 12 and len(SET_Cm) == 22
    D = load_D()

    rng_q = random.Random(SEED)
    rng_qi = random.Random(SEED + 1)
    rng_cm = random.Random(SEED + 2)

    dQ = mean_pairwise(D, SET_Q)
    pQ = percentile_in_null(D, dQ, 22, N_PERMS, rng_q)
    primary = pQ <= 5.0
    print(f"\n--- PRIMARY: Q={SET_Q} (mufaṣṣal-qiṣār Q93-114, N=22) ---")
    print(f"  d̄(Q) = {dQ:.4f}, pct = {pQ:.2f}%, ≤5%: {primary}")

    dQI = mean_pairwise(D, SET_QI)
    pQI = percentile_in_null(D, dQI, 12, N_PERMS, rng_qi)
    mw5 = pQI <= 1.0
    print(f"\n--- MW-5: QI={SET_QI} (inner-12, Q103-114) ---")
    print(f"  d̄(QI) = {dQI:.4f}, pct = {pQI:.2f}%, ≤1%: {mw5}")

    dCm = mean_pairwise(D, SET_Cm)
    pCm = percentile_in_null(D, dCm, 22, N_PERMS, rng_cm)
    mw6 = 30.0 <= pCm <= 70.0
    print(f"\n--- MW-6: Cm={SET_Cm} (Meccan-mid-22) ---")
    print(f"  d̄(Cm) = {dCm:.4f}, pct = {pCm:.2f}%, [30,70]: {mw6}")

    agg = primary and mw5 and mw6
    print(f"\n=== AGGREGATE ===")
    print(f"PRIMARY: {primary}  MW-5: {mw5}  MW-6: {mw6}")
    print(f"AGGREGATE H1 CONFIRMED: {agg}")

    out = {
        "id": "H-NEW-500", "prereg_sha": prereg_sha, "seed": SEED,
        "alpha_bon": ALPHA_BON,
        "primary": {"set": SET_Q, "n": 22, "d": dQ, "percentile": pQ, "threshold": 5.0, "pass": primary},
        "mw5": {"set": SET_QI, "n": 12, "d": dQI, "percentile": pQI, "threshold": 1.0, "pass": mw5},
        "mw6": {"set": SET_Cm, "n": 22, "d": dCm, "percentile": pCm, "range": [30.0, 70.0], "pass": mw6},
        "aggregate_h1_confirmed": agg,
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
