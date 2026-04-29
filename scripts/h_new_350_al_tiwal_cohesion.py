#!/usr/bin/env python3
"""H-NEW-350: al-Ṭiwāl block cohesion test (N=8)."""
import hashlib, itertools, json, random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-350-al-tiwal-cohesion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-350.json"

SEED = 20260502
N_PERM = 10000

TIWAL = [2, 3, 4, 5, 6, 7, 8, 9]
MW5_LAST8 = [107, 108, 109, 110, 111, 112, 113, 114]

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

def test(subset, D, seed):
    random.seed(seed)
    d_obs = mean_pw(subset, D)
    nulls = [mean_pw(random.sample(range(1, 115), len(subset)), D) for _ in range(N_PERM)]
    p_less = sum(1 for x in nulls if x <= d_obs) / N_PERM
    null_mean = sum(nulls) / N_PERM
    sorted_nulls = sorted(nulls)
    return {"d_obs": d_obs, "null_mean": null_mean, "p_less": p_less,
            "pct_2_5": sorted_nulls[int(0.025*N_PERM)],
            "pct_97_5": sorted_nulls[int(0.975*N_PERM)]}

def main():
    print(f"=== H-NEW-350 ===")
    print(f"Pre-reg SHA: {sha(PREREG)}")
    D = load_D()

    print(f"\nCell A — al-ṭiwāl {{Q 2-9}}:")
    a = test(TIWAL, D, SEED)
    for k, v in a.items(): print(f"  {k}: {v:.4f}")

    print(f"\nCell B — MW-5 mufaṣṣal-qiṣār last-8 {{Q 107-114}}:")
    b = test(MW5_LAST8, D, SEED+1)
    for k, v in b.items(): print(f"  {k}: {v:.4f}")

    alpha_bon = 0.025
    a_pass = a['d_obs'] < a['pct_2_5'] and a['p_less'] < alpha_bon
    b_pass = b['d_obs'] < b['pct_2_5'] and b['p_less'] < alpha_bon

    if a_pass and b_pass:
        verdict = "BLOCK-CAUSAL-STRICT-PASS — both blocks strictly significant"
    elif a_pass:
        verdict = "TIWAL-STRICT-PASS; MW-5 less-extreme"
    elif not a_pass and b_pass:
        verdict = "ONLY-MW-5-passes; ṭiwāl fails"
    else:
        verdict = "BOTH-UNDERPOWERED — directional only"

    print(f"\nA (ṭiwāl) pass: {a_pass}")
    print(f"B (last-8 MW-5) pass: {b_pass}")
    print(f"Verdict: {verdict}")

    # Descriptive percentiles
    print(f"\nDescriptive percentiles: A (ṭiwāl) = {a['p_less']*100:.1f}%, B (last-8) = {b['p_less']*100:.1f}%")
    print(f"Compare to H-NEW-340 A (musabbiḥāt block 5) = 8.1%, C (ḥawāmīm 5) = 23.6%")

    out = {"id": "H-NEW-350", "prereg_sha": sha(PREREG), "seed": SEED,
           "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": alpha_bon,
           "cell_A_tiwal": {**a, "pass": a_pass, "subset": TIWAL, "n": len(TIWAL)},
           "cell_B_mw5_last8": {**b, "pass": b_pass, "subset": MW5_LAST8, "n": len(MW5_LAST8)},
           "verdict": verdict}
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__":
    main()
