#!/usr/bin/env python3
"""H-NEW-570: muqaṭṭaʿāt-29 content-cluster test."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-570-muqattaat-content-cluster-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-570.json"
SEED = 20260520
N_PERMS = 10000
ALPHA_BON = 0.05 / 3

SET_MUQ = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]  # 29
SET_HM = [40, 41, 42, 43, 44, 45, 46]  # 7 ḥawāmīm
SET_NONMUQ = [1, 4, 5, 6, 8, 9, 16, 17, 18, 21, 22, 23, 24, 25, 33, 34, 35, 37, 39, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57]  # 29 non-muq

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
    print(f"=== H-NEW-570 (muqaṭṭaʿāt-29 content-cluster) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}")
    assert len(SET_MUQ) == 29 and len(SET_HM) == 7 and len(SET_NONMUQ) == 29
    D = load_D()

    rng_m = random.Random(SEED)
    rng_h = random.Random(SEED + 1)
    rng_n = random.Random(SEED + 2)

    dM = mean_pairwise(D, SET_MUQ)
    pM = percentile_in_null(D, dM, 29, N_PERMS, rng_m)
    primary = pM <= 10.0
    print(f"\n--- PRIMARY: muq-29 ---")
    print(f"  d̄ = {dM:.4f}, pct = {pM:.2f}%, ≤10%: {primary}")

    dH = mean_pairwise(D, SET_HM)
    pH = percentile_in_null(D, dH, 7, N_PERMS, rng_h)
    mw5 = pH <= 5.0
    print(f"\n--- MW-5: ḥawāmīm-7 {SET_HM} ---")
    print(f"  d̄ = {dH:.4f}, pct = {pH:.2f}%, ≤5%: {mw5}")

    dN = mean_pairwise(D, SET_NONMUQ)
    pN = percentile_in_null(D, dN, 29, N_PERMS, rng_n)
    mw6 = 30.0 <= pN <= 70.0
    print(f"\n--- MW-6: non-muq-29 ---")
    print(f"  d̄ = {dN:.4f}, pct = {pN:.2f}%, [30,70]: {mw6}")

    agg = primary and mw5 and mw6
    print(f"\n=== AGGREGATE H1: {agg} ===")

    out = {
        "id": "H-NEW-570", "prereg_sha": prereg_sha, "seed": SEED,
        "primary": {"set": SET_MUQ, "n": 29, "d": dM, "percentile": pM, "pass": primary},
        "mw5_hm7": {"set": SET_HM, "n": 7, "d": dH, "percentile": pH, "pass": mw5},
        "mw6_nonmuq29": {"set": SET_NONMUQ, "n": 29, "d": dN, "percentile": pN, "pass": mw6},
        "aggregate_h1_confirmed": agg,
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
