#!/usr/bin/env python3
"""H-NEW-360: mufaṣṣal-awsāṭ cohesion test (N=11)."""
import hashlib, itertools, json, random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-360-mufassal-awsat-cohesion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-360.json"

SEED = 20260503
N_PERM = 10000

AWSAT = list(range(67, 78))  # Q 67-77
MW5_MID_NULL = [30, 32, 35, 37, 40, 45, 49, 54, 56, 58, 60]  # mid-mushaf unrelated random

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
    print(f"=== H-NEW-360 ===")
    print(f"Pre-reg SHA: {sha(PREREG)}")
    D = load_D()

    print(f"\nCell A — mufaṣṣal-awsāṭ {{Q 67-77}}:")
    a = test(AWSAT, D, SEED)
    for k, v in a.items(): print(f"  {k}: {v:.4f}")

    print(f"\nCell B — MW-5 mid-mushaf random scatter (negative control):")
    b = test(MW5_MID_NULL, D, SEED+1)
    for k, v in b.items(): print(f"  {k}: {v:.4f}")

    alpha_bon = 0.025
    a_pass = a['d_obs'] < a['pct_2_5'] and a['p_less'] < alpha_bon
    b_null_like = 0.4 < b['p_less'] < 0.6  # expect ≈50%ile

    if a_pass:
        verdict = "STRICT-PASS — mufaṣṣal-awsāṭ content-cohesive at α=0.025"
    else:
        verdict = "NULL — mufaṣṣal-awsāṭ not strictly significant"

    print(f"\nA (awsāṭ) pass: {a_pass}")
    print(f"A percentile: {a['p_less']*100:.1f}%")
    print(f"B negative control (expected ~50%ile): {b['p_less']*100:.1f}%")
    print(f"Verdict: {verdict}")

    print(f"\nSeries hierarchy comparison:")
    print(f"  Q 107-114 terminal (H-350)   : 0.0%ile  STRICT PASS")
    print(f"  Musabbiḥāt-block (H-340)     : 8.1%ile  directional")
    print(f"  al-Ṭiwāl Q 2-9 (H-350)       : 17.3%ile directional")
    print(f"  Mufaṣṣal-awsāṭ Q 67-77 (H-360): {a['p_less']*100:.1f}%ile  {verdict.split()[0]}")

    out = {"id": "H-NEW-360", "prereg_sha": sha(PREREG), "seed": SEED,
           "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": alpha_bon,
           "cell_A_awsat": {**a, "pass": a_pass, "subset": AWSAT, "n": len(AWSAT)},
           "cell_B_mw5_mid": {**b, "null_like": b_null_like, "subset": MW5_MID_NULL},
           "verdict": verdict}
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__":
    main()
