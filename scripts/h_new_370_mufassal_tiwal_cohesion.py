#!/usr/bin/env python3
"""H-NEW-370: mufaṣṣal-ṭiwāl cohesion test (N=17)."""
import hashlib, itertools, json, random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-370-mufassal-tiwal-cohesion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-370.json"

SEED = 20260504
N_PERM = 10000

TIWAL_MUF = list(range(50, 67))  # Q 50-66, 17 surahs
MW5_TERMINAL17 = list(range(98, 115))  # Q 98-114, 17 surahs

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
    print(f"=== H-NEW-370 ===")
    print(f"Pre-reg SHA: {sha(PREREG)}")
    D = load_D()

    print(f"\nCell A — mufaṣṣal-ṭiwāl {{Q 50-66}} N=17:")
    a = test(TIWAL_MUF, D, SEED)
    for k, v in a.items(): print(f"  {k}: {v:.4f}")

    print(f"\nCell B — MW-5 terminal-17 {{Q 98-114}} N=17 (expected high cohesion):")
    b = test(MW5_TERMINAL17, D, SEED+1)
    for k, v in b.items(): print(f"  {k}: {v:.4f}")

    alpha_bon = 0.025
    a_pass = a['d_obs'] < a['pct_2_5'] and a['p_less'] < alpha_bon
    b_pass = b['d_obs'] < b['pct_2_5'] and b['p_less'] < alpha_bon

    if a_pass and b_pass:
        verdict = "BOTH-STRICT-PASS — mufaṣṣal-ṭiwāl cohesive AND terminal control cohesive"
    elif a_pass:
        verdict = "ṬIWĀL-PASS; terminal control underwhelming"
    elif b_pass:
        verdict = "ONLY-TERMINAL-PASSES; ṭiwāl not cohesive"
    else:
        verdict = "BOTH-FAIL — hierarchy hypothesis weakened"

    print(f"\nA (mufaṣṣal-ṭiwāl Q 50-66) pass: {a_pass}; {a['p_less']*100:.1f}%ile")
    print(f"B (terminal Q 98-114) pass: {b_pass}; {b['p_less']*100:.1f}%ile")
    print(f"Verdict: {verdict}")

    print(f"\nSeries hierarchy after H-NEW-370:")
    print(f"  Q 107-114 qiṣār-subset (H-350) : 0.0%ile STRICT")
    print(f"  Q 67-77 awsāṭ (H-360)          : 7.1%ile directional")
    print(f"  Q 50-66 mufaṣṣal-ṭiwāl (H-370) : {a['p_less']*100:.1f}%ile {'PASS' if a_pass else 'directional'}")
    print(f"  Q 2-9 ṭiwāl-proper (H-350)     : 17.3%ile directional")

    out = {"id": "H-NEW-370", "prereg_sha": sha(PREREG), "seed": SEED,
           "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": alpha_bon,
           "cell_A_mufassal_tiwal": {**a, "pass": a_pass, "subset": TIWAL_MUF, "n": len(TIWAL_MUF)},
           "cell_B_mw5_terminal17": {**b, "pass": b_pass, "subset": MW5_TERMINAL17, "n": len(MW5_TERMINAL17)},
           "verdict": verdict}
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__":
    main()
