#!/usr/bin/env python3
"""H-NEW-340: musabbiḥāt block-only subset cohesion test."""
import hashlib, itertools, json, random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-340-musabbihat-block-subset-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-340.json"

SEED = 20260501
N_PERM = 10000

A = [57, 59, 61, 62, 64]       # block+formula
B = [17, 87]                    # formula-no-block (single pair)
C = [40, 41, 43, 44, 45]        # block-no-formula ḥawāmīm 5

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist; mat[j][i] = dist
    return mat

def mean_pw(subset, D):
    pairs = list(itertools.combinations(subset, 2))
    return sum(D[a][b] for a, b in pairs) / len(pairs) if pairs else 0

def test_cohesion(subset, D, n_perm, seed):
    random.seed(seed)
    d_obs = mean_pw(subset, D)
    nulls = [mean_pw(random.sample(range(1, 115), len(subset)), D) for _ in range(n_perm)]
    p_less = sum(1 for x in nulls if x <= d_obs) / n_perm
    null_mean = sum(nulls) / n_perm
    nulls_sorted = sorted(nulls)
    return {"d_obs": d_obs, "null_mean": null_mean, "p_less": p_less,
            "pct_1_67": nulls_sorted[int(0.0167*n_perm)],
            "pct_2_5": nulls_sorted[int(0.025*n_perm)]}

def main():
    print(f"=== H-NEW-340 ===")
    print(f"Pre-reg SHA: {sha(PREREG)}")
    D = load_D()

    print("\nCell A — musabbiḥāt Medinan-back {57,59,61,62,64}:")
    a = test_cohesion(A, D, N_PERM, SEED)
    for k, v in a.items(): print(f"  {k}: {v:.4f}")
    pct_a = sum(1 for x in range(N_PERM) if a['d_obs'] > 0) and a['p_less']*100

    print(f"\nCell B — musabbiḥāt outside-block pair {{17, 87}}:")
    d_17_87 = D[17][87]
    print(f"  d(Q 17, Q 87) = {d_17_87:.4f}")
    # Null: single random pair distance
    random.seed(SEED+1)
    single_pair_nulls = [D[random.choice(range(1,115))][random.choice(range(1,115))]
                         for _ in range(N_PERM)]
    single_pair_nulls = [x for x in single_pair_nulls if x > 0]  # filter self
    single_null_mean = sum(single_pair_nulls)/len(single_pair_nulls)
    p_less_b = sum(1 for x in single_pair_nulls if x <= d_17_87)/len(single_pair_nulls)
    print(f"  single-pair null mean = {single_null_mean:.4f}")
    print(f"  p(null ≤ {d_17_87:.4f}) = {p_less_b:.4f}")

    print(f"\nCell C — ḥawāmīm 5 {{40,41,43,44,45}} (block-no-formula control):")
    c = test_cohesion(C, D, N_PERM, SEED+2)
    for k, v in c.items(): print(f"  {k}: {v:.4f}")

    alpha_bon = 0.0167
    a_pass = a['d_obs'] < a['pct_1_67'] and a['p_less'] < alpha_bon
    c_pass = c['d_obs'] < c['pct_1_67'] and c['p_less'] < alpha_bon

    if a_pass and c_pass:
        verdict = "BLOCK-DRIVES-COHESION (both block-subsets pass)"
    elif a_pass and not c_pass:
        verdict = "BLOCK+FORMULA (musabbiḥāt block subset passes but ḥawāmīm fails)"
    elif not a_pass and not c_pass:
        verdict = "UNDERPOWERED-AT-N5 (null variance too high; directional verdict only)"
    else:
        verdict = "UNEXPECTED"

    print(f"\nA pass: {a_pass}")
    print(f"C pass: {c_pass}")
    print(f"Verdict: {verdict}")

    # Percentile comparison
    pct_a = a['p_less']*100
    pct_c = c['p_less']*100
    print(f"\nDescriptive percentiles: A={pct_a:.1f}%, C={pct_c:.1f}%")
    print(f"Full musabbiḥāt N=7 was 19.8%ile (H-NEW-331)")
    print(f"Change from full set → block-only: {19.8 - pct_a:+.1f} percentile points")

    out = {"id": "H-NEW-340", "prereg_sha": sha(PREREG), "seed": SEED,
           "n_perm": N_PERM, "bonferroni_k": 3, "alpha_bon": alpha_bon,
           "cell_A_block_plus_formula": {**a, "pass": a_pass, "subset": A},
           "cell_B_formula_no_block_pair": {"d_17_87": d_17_87, "null_mean": single_null_mean, "p_less": p_less_b},
           "cell_C_block_no_formula": {**c, "pass": c_pass, "subset": C},
           "verdict": verdict,
           "descriptive_pct_A": pct_a, "descriptive_pct_C": pct_c,
           "full_musabbihat_7_pct": 19.8}
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"Wrote {OUT_JSON}")

if __name__ == "__main__":
    main()
