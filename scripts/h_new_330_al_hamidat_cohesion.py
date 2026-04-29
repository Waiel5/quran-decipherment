#!/usr/bin/env python3
"""H-NEW-330: al-Ḥāmidāt content-axis cohesion test."""
import hashlib
import itertools
import json
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-330-al-hamidat-cohesion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-330.json"

SEED = 20260429
N_PERM = 10000

HAMIDAT = [1, 6, 18, 34, 35]
HAWAMIM_5 = [40, 41, 43, 44, 45]  # MW-5 control (5 of 7 ḥawāmīm, drop Q 42 HMASQ + Q 46)

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def load_D():
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat

def mean_pairwise(subset, D):
    pairs = list(itertools.combinations(subset, 2))
    if not pairs:
        return 0.0
    return sum(D[a][b] for a, b in pairs) / len(pairs)

def cohesion_test(subset, D, n_perm, seed, exclude=None):
    random.seed(seed)
    d_obs = mean_pairwise(subset, D)
    size = len(subset)
    universe = [s for s in range(1, 115) if s not in (exclude or [])]
    nulls = []
    for _ in range(n_perm):
        sample = random.sample(universe, size)
        nulls.append(mean_pairwise(sample, D))
    p_less = sum(1 for x in nulls if x <= d_obs) / n_perm
    null_mean = sum(nulls) / len(nulls)
    nulls_sorted = sorted(nulls)
    pct_2_5 = nulls_sorted[int(0.025 * n_perm)]
    pct_97_5 = nulls_sorted[int(0.975 * n_perm)]
    return {
        "d_obs": d_obs, "null_mean": null_mean, "p_less": p_less,
        "pct_2_5": pct_2_5, "pct_97_5": pct_97_5,
    }

def main():
    print(f"=== H-NEW-330 ===")
    print(f"Pre-reg SHA: {sha(PREREG)}")
    D = load_D()

    print(f"\nCell A — al-ḥāmidāt {{Q 1, 6, 18, 34, 35}}:")
    cell_a = cohesion_test(HAMIDAT, D, N_PERM, SEED)
    print(f"  d̄_obs = {cell_a['d_obs']:.4f}")
    print(f"  Null mean = {cell_a['null_mean']:.4f}")
    print(f"  2.5%ile = {cell_a['pct_2_5']:.4f}; 97.5%ile = {cell_a['pct_97_5']:.4f}")
    print(f"  p(null ≤ obs) = {cell_a['p_less']:.4f}")

    print(f"\nCell B — MW-5 ḥawāmīm control {{Q 40, 41, 43, 44, 45}}:")
    cell_b = cohesion_test(HAWAMIM_5, D, N_PERM, SEED + 1)
    print(f"  d̄_obs = {cell_b['d_obs']:.4f}")
    print(f"  Null mean = {cell_b['null_mean']:.4f}")
    print(f"  2.5%ile = {cell_b['pct_2_5']:.4f}; 97.5%ile = {cell_b['pct_97_5']:.4f}")
    print(f"  p(null ≤ obs) = {cell_b['p_less']:.4f}")

    alpha_bon = 0.025
    a_pass = cell_a['d_obs'] < cell_a['pct_2_5'] and cell_a['p_less'] < alpha_bon
    b_pass = cell_b['d_obs'] < cell_b['pct_2_5'] and cell_b['p_less'] < alpha_bon

    if a_pass and b_pass:
        verdict = "AL-HAMIDAT-CONTENT-COHESIVE"
    elif not a_pass and b_pass:
        verdict = "NULL (ḥāmidāt not content-cohesive; MW-5 ḥawāmīm control passes so instrument sound)"
    elif a_pass and not b_pass:
        verdict = "INSTRUMENT-SUSPECT"
    else:
        verdict = "NULL (ḥāmidāt not content-cohesive; MW-5 also fails — pipeline may be suspect)"

    print(f"\nCell A pass: {a_pass}")
    print(f"Cell B (MW-5 ḥawāmīm) pass: {b_pass}")
    print(f"Verdict: {verdict}")

    out = {
        "id": "H-NEW-330", "prereg_sha": sha(PREREG), "seed": SEED,
        "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": alpha_bon,
        "cell_A_hamidat": {**cell_a, "pass": a_pass, "subset": HAMIDAT},
        "cell_B_mw5_hawamim": {**cell_b, "pass": b_pass, "subset": HAWAMIM_5},
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {OUT_JSON}")

if __name__ == "__main__":
    main()
