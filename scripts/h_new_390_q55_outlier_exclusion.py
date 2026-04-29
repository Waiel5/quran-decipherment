#!/usr/bin/env python3
"""H-NEW-390: Q 55 outlier-exclusion test."""
import hashlib, itertools, json, random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-390-q55-outlier-exclusion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-390.json"

SEED = 20260506
N_PERM = 10000

EXCLUDE_Q55 = [50, 51, 52, 53, 54, 56]   # Meccan Q 50-56 minus Q 55
FULL_MECCAN = [50, 51, 52, 53, 54, 55, 56]  # for reference

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
    print(f"=== H-NEW-390 ===\nPre-reg SHA: {sha(PREREG)}")
    D = load_D()

    # Show Q 55's per-surah distance to each other Meccan member
    print(f"\nQ 55's FR distance to other Meccan-half members:")
    for s in [50, 51, 52, 53, 54, 56]:
        print(f"  d(Q 55, Q {s}) = {D[55][s]:.4f}")

    print(f"\nCell A — Meccan half WITHOUT Q 55 {{Q 50, 51, 52, 53, 54, 56}} N=6:")
    a = test(EXCLUDE_Q55, D, SEED)
    for k, v in a.items(): print(f"  {k}: {v:.4f}")

    # Descriptive: full Meccan half for comparison
    d_full = mean_pw(FULL_MECCAN, D)
    print(f"\nFull Meccan half {{Q 50-56}} N=7: d̄={d_full:.4f} at 70.1%ile (H-NEW-380)")
    print(f"Delta from removing Q 55: d̄ change = {d_full - a['d_obs']:+.4f}")
    print(f"Percentile change: 70.1% → {a['p_less']*100:.1f}%  ({(70.1-a['p_less']*100):+.1f}pp)")

    alpha = 0.025
    a_pass = a['d_obs'] < a['pct_2_5'] and a['p_less'] < alpha
    delta_pct = 70.1 - a['p_less']*100

    if a_pass:
        verdict = "Q55-IS-PRIMARY-DISRUPTOR — exclusion passes strict α"
    elif delta_pct >= 50:
        verdict = "Q55-IS-STRONG-DISRUPTOR — exclusion drops percentile ≥50pp"
    elif delta_pct >= 20:
        verdict = "Q55-IS-MODERATE-DISRUPTOR — partial improvement"
    else:
        verdict = "Q55-NOT-KEY-DISRUPTOR — register-heterogeneity independent"

    print(f"\nA pass: {a_pass}; percentile: {a['p_less']*100:.1f}%")
    print(f"Delta vs H-NEW-380: {delta_pct:+.1f}pp")
    print(f"Verdict: {verdict}")

    out = {"id": "H-NEW-390", "prereg_sha": sha(PREREG), "seed": SEED, "n_perm": N_PERM,
           "bonferroni_k": 2, "alpha_bon": alpha,
           "cell_A_exclude_Q55": {**a, "pass": a_pass, "subset": EXCLUDE_Q55, "n": 6},
           "full_meccan_d_obs": d_full, "full_meccan_pct": 70.1,
           "delta_pct_from_Q55_removal": delta_pct,
           "q55_distances_to_others": {f"Q_{s}": D[55][s] for s in [50,51,52,53,54,56]},
           "verdict": verdict}
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"Wrote {OUT_JSON}")

if __name__ == "__main__": main()
