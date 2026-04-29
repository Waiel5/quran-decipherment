#!/usr/bin/env python3
"""H-NEW-331: al-Musabbiḥāt content-axis cohesion test."""
import hashlib, itertools, json, random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-331-al-musabbihat-cohesion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-331.json"

SEED = 20260430
N_PERM = 10000

MUSABBIHAT = [17, 57, 59, 61, 62, 64, 87]
HAWAMIM_6 = [40, 41, 43, 44, 45, 46]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def load_D():
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist; mat[j][i] = dist
    return mat

def mean_pairwise(subset, D):
    pairs = list(itertools.combinations(subset, 2))
    return sum(D[a][b] for a, b in pairs) / len(pairs) if pairs else 0

def cohesion_test(subset, D, n_perm, seed):
    random.seed(seed)
    d_obs = mean_pairwise(subset, D)
    size = len(subset)
    nulls = [mean_pairwise(random.sample(range(1, 115), size), D) for _ in range(n_perm)]
    p_less = sum(1 for x in nulls if x <= d_obs) / n_perm
    null_mean = sum(nulls) / n_perm
    nulls_sorted = sorted(nulls)
    return {"d_obs": d_obs, "null_mean": null_mean, "p_less": p_less,
            "pct_2_5": nulls_sorted[int(0.025*n_perm)],
            "pct_97_5": nulls_sorted[int(0.975*n_perm)]}

def main():
    print(f"=== H-NEW-331 ===")
    print(f"Pre-reg SHA: {sha(PREREG)}")
    D = load_D()

    print(f"\nCell A — al-musabbiḥāt {{Q 17, 57, 59, 61, 62, 64, 87}}:")
    cell_a = cohesion_test(MUSABBIHAT, D, N_PERM, SEED)
    for k, v in cell_a.items(): print(f"  {k}: {v:.4f}")

    print(f"\nCell B — MW-5 ḥawāmīm 6-subset {{40, 41, 43, 44, 45, 46}}:")
    cell_b = cohesion_test(HAWAMIM_6, D, N_PERM, SEED+1)
    for k, v in cell_b.items(): print(f"  {k}: {v:.4f}")

    alpha_bon = 0.025
    a_pass = cell_a['d_obs'] < cell_a['pct_2_5'] and cell_a['p_less'] < alpha_bon
    b_pass = cell_b['d_obs'] < cell_b['pct_2_5'] and cell_b['p_less'] < alpha_bon

    if a_pass and b_pass:
        verdict = "MUSABBIHAT-CONTENT-COHESIVE"
    elif not a_pass and b_pass:
        verdict = "NULL (musabbiḥāt not cohesive; MW-5 passes — instrument sound)"
    elif a_pass and not b_pass:
        verdict = "INSTRUMENT-SUSPECT"
    else:
        verdict = "NULL (musabbiḥāt not cohesive; MW-5 underpowered)"

    print(f"\nCell A pass: {a_pass}")
    print(f"Cell B (MW-5 ḥawāmīm-6) pass: {b_pass}")
    print(f"Verdict: {verdict}")

    out = {"id": "H-NEW-331", "prereg_sha": sha(PREREG), "seed": SEED,
           "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": alpha_bon,
           "cell_A_musabbihat": {**cell_a, "pass": a_pass, "subset": MUSABBIHAT},
           "cell_B_mw5_hawamim": {**cell_b, "pass": b_pass, "subset": HAWAMIM_6},
           "verdict": verdict}
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"Wrote {OUT_JSON}")

if __name__ == "__main__":
    main()
