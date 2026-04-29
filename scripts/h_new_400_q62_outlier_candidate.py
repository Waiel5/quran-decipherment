#!/usr/bin/env python3
"""H-NEW-400: Q 62 al-Jumuʿa outlier-candidate test."""
import hashlib, itertools, json, random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-400-q62-outlier-candidate-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-400.json"

SEED = 20260507
N_PERM = 10000

EXCLUDE_Q62 = [57, 59, 61, 64]        # musabbiḥāt-block minus Q 62
FULL_BLOCK = [57, 59, 61, 62, 64]     # H-NEW-340 baseline

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
    return {"d_obs": d_obs, "null_mean": sum(nulls)/N_PERM, "p_less": p_less,
            "pct_2_5": sorted(nulls)[int(0.025*N_PERM)]}

def main():
    print(f"=== H-NEW-400 ===\nPre-reg SHA: {sha(PREREG)}")
    D = load_D()

    print(f"\nQ 62 pairwise distances to other musabbiḥāt-block members:")
    for s in [57, 59, 61, 64]:
        print(f"  d(Q 62, Q {s}) = {D[62][s]:.4f}")

    print(f"\nCell A — exclusion {{Q 57, 59, 61, 64}} N=4:")
    a = test(EXCLUDE_Q62, D, SEED)
    for k, v in a.items(): print(f"  {k}: {v:.4f}")

    # Baseline comparison
    d_full = mean_pw(FULL_BLOCK, D)
    print(f"\nFull H-NEW-340 block {{Q 57, 59, 61, 62, 64}} N=5: d̄={d_full:.4f} at 8.1%ile")
    print(f"Delta d̄: {d_full - a['d_obs']:+.4f}")
    print(f"Percentile change: 8.1% → {a['p_less']*100:.1f}%  ({(8.1 - a['p_less']*100):+.1f}pp)")

    alpha = 0.025
    a_pass = a['d_obs'] < a['pct_2_5'] and a['p_less'] < alpha
    delta_pct = 8.1 - a['p_less']*100

    if a_pass:
        verdict = "Q62-IS-OUTLIER STRICT-PASS"
    elif delta_pct >= 5:
        verdict = f"Q62-CANDIDATE-OUTLIER (+{delta_pct:.1f}pp improvement)"
    elif delta_pct <= -5:
        verdict = f"Q62-IS-COHESION-ANCHOR (removing Q 62 WORSENS cohesion by {-delta_pct:.1f}pp)"
    else:
        verdict = f"Q62-NOT-OUTLIER (negligible change {delta_pct:+.1f}pp)"

    print(f"\nA pass: {a_pass}; percentile: {a['p_less']*100:.1f}%")
    print(f"Delta vs H-NEW-340: {delta_pct:+.1f}pp")
    print(f"Verdict: {verdict}")

    out = {"id": "H-NEW-400", "prereg_sha": sha(PREREG), "seed": SEED, "n_perm": N_PERM,
           "bonferroni_k": 2, "alpha_bon": alpha,
           "cell_A_exclude_Q62": {**a, "pass": a_pass, "subset": EXCLUDE_Q62, "n": 4},
           "full_block_d_obs": d_full, "full_block_pct": 8.1,
           "delta_pct_from_Q62_removal": delta_pct,
           "q62_distances_to_block_members": {f"Q_{s}": D[62][s] for s in [57,59,61,64]},
           "verdict": verdict}
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"Wrote {OUT_JSON}")

if __name__ == "__main__": main()
