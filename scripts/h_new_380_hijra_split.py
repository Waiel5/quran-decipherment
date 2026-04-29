#!/usr/bin/env python3
"""H-NEW-380: Hijra-split validation test."""
import hashlib, itertools, json, random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-380-hijra-split-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-380.json"

SEED = 20260505
N_PERM = 10000

MECCAN_HALF = list(range(50, 57))       # Q 50-56
MEDINAN_HALF = list(range(57, 67))      # Q 57-66

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist; mat[j][i] = dist
    return mat
def mean_pw(s, D):
    p = list(itertools.combinations(s, 2))
    return sum(D[a][b] for a,b in p)/len(p) if p else 0
def test(s, D, seed):
    random.seed(seed)
    d_obs = mean_pw(s, D)
    nulls = [mean_pw(random.sample(range(1,115), len(s)), D) for _ in range(N_PERM)]
    p_less = sum(1 for x in nulls if x <= d_obs)/N_PERM
    ns = sorted(nulls)
    return {"d_obs": d_obs, "null_mean": sum(nulls)/N_PERM,
            "p_less": p_less, "pct_2_5": ns[int(0.025*N_PERM)]}

def main():
    print(f"=== H-NEW-380 ===\nPre-reg SHA: {sha(PREREG)}")
    D = load_D()
    print(f"\nCell A — Meccan half {{Q 50-56}} N=7:")
    a = test(MECCAN_HALF, D, SEED)
    for k, v in a.items(): print(f"  {k}: {v:.4f}")
    print(f"\nCell B — Medinan half {{Q 57-66}} N=10:")
    b = test(MEDINAN_HALF, D, SEED+1)
    for k, v in b.items(): print(f"  {k}: {v:.4f}")
    alpha = 0.025
    a_pass = a['d_obs'] < a['pct_2_5'] and a['p_less'] < alpha
    b_pass = b['d_obs'] < b['pct_2_5'] and b['p_less'] < alpha
    if a_pass and b_pass: verdict = "CHRONOLOGY-HOMOGENEITY-CONFIRMED — both halves STRICT PASS"
    elif a_pass or b_pass: verdict = f"PARTIAL — {'Meccan' if a_pass else 'Medinan'} passes only"
    else: verdict = "NULL — neither half strictly passes"
    print(f"\nA Meccan pass: {a_pass}; {a['p_less']*100:.1f}%ile")
    print(f"B Medinan pass: {b_pass}; {b['p_less']*100:.1f}%ile")
    print(f"Combined block (H-370): 50.1%ile NULL")
    print(f"Verdict: {verdict}")
    out = {"id":"H-NEW-380","prereg_sha":sha(PREREG),"seed":SEED,"n_perm":N_PERM,
           "bonferroni_k":2,"alpha_bon":alpha,
           "cell_A_meccan":{**a,"pass":a_pass,"subset":MECCAN_HALF,"n":7},
           "cell_B_medinan":{**b,"pass":b_pass,"subset":MEDINAN_HALF,"n":10},
           "verdict":verdict}
    with open(OUT_JSON,"w") as f: json.dump(out,f,indent=2)
    print(f"Wrote {OUT_JSON}")

if __name__ == "__main__": main()
