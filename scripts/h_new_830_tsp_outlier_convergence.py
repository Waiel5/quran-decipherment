#!/usr/bin/env python3
"""H-NEW-830: TSP-cost vs outlier-strength architectural convergence.

Tests if H-NEW-720 per-adjacency canonical cost is correlated with H-NEW-590 per-surah outlier-strength.
"""
import hashlib
import json
import math
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_720 = ROOT / "findings/phase-b-hypotheses/csv/h-new-720.json"
H_NEW_590 = ROOT / "findings/phase-b-hypotheses/csv/h-new-590.json"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-830.json"
SEED = 20260449
N_PERMS = 10000


def pearson_r(x, y):
    n = len(x)
    mx, my = sum(x)/n, sum(y)/n
    num = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    dx = math.sqrt(sum((x[i]-mx)**2 for i in range(n)))
    dy = math.sqrt(sum((y[i]-my)**2 for i in range(n)))
    return num/(dx*dy) if dx > 0 and dy > 0 else 0.0


def spearman_rho(x, y):
    def ranks(v):
        sorted_pairs = sorted(enumerate(v), key=lambda p: p[1])
        r = [0]*len(v)
        i = 0
        while i < len(sorted_pairs):
            j = i
            while j+1 < len(sorted_pairs) and sorted_pairs[j+1][1] == sorted_pairs[i][1]:
                j += 1
            avg_rank = (i + j) / 2 + 1
            for k in range(i, j+1):
                r[sorted_pairs[k][0]] = avg_rank
            i = j + 1
        return r
    return pearson_r(ranks(x), ranks(y))


def main():
    print(f"=== H-NEW-830 (TSP-cost × outlier-strength convergence) ===\n")

    with open(H_NEW_720) as f: h720 = json.load(f)
    with open(H_NEW_590) as f: h590 = json.load(f)

    # H-NEW-720 per-adjacency: list of {s, pair=[s, s+1], delta, fraction_residual}
    adj_costs = {entry["s"]: entry["delta_raw"] for entry in h720["per_adjacency"]}
    # adjacency s = pair (s, s+1). So adj_costs[s] = cost of forcing Q s adjacent to Q s+1.

    # H-NEW-590 per-surah: list of {X, delta_pct, classification}
    outlier_strengths = {entry["X"]: entry["delta_pct"] for entry in h590["all_surahs_results"]}

    print(f"Loaded: 113 canonical adjacencies, {len(outlier_strengths)} per-surah outlier strengths.\n")

    # For each surah s ∈ {2, ..., 113} (interior — has left and right neighbors)
    # - left_cost = adj_costs[s-1] (cost of Q s-1 to Q s adjacency)
    # - right_cost = adj_costs[s] (cost of Q s to Q s+1)
    # - max_cost = max(left, right)
    # - sum_cost = left + right
    # - outlier_strength = delta_pct(s)
    # - abs_outlier_strength = |delta_pct(s)|

    surahs = list(range(2, 114))  # interior surahs
    left_costs = []
    right_costs = []
    max_costs = []
    sum_costs = []
    abs_outliers = []
    signed_outliers = []
    for s in surahs:
        l = adj_costs.get(s - 1, 0.0)
        r = adj_costs.get(s, 0.0)
        left_costs.append(l)
        right_costs.append(r)
        max_costs.append(max(l, r))
        sum_costs.append(l + r)
        outlier = outlier_strengths.get(s, 0.0)
        abs_outliers.append(abs(outlier))
        signed_outliers.append(outlier)

    # Correlations
    r_max_abs = pearson_r(max_costs, abs_outliers)
    r_max_signed = pearson_r(max_costs, signed_outliers)
    r_sum_abs = pearson_r(sum_costs, abs_outliers)
    r_sum_signed = pearson_r(sum_costs, signed_outliers)
    rho_max_abs = spearman_rho(max_costs, abs_outliers)
    rho_max_signed = spearman_rho(max_costs, signed_outliers)
    rho_sum_abs = spearman_rho(sum_costs, abs_outliers)
    rho_sum_signed = spearman_rho(sum_costs, signed_outliers)

    print(f"--- CORRELATIONS (n={len(surahs)} interior surahs) ---")
    print(f"  Pearson r(max_neighbor_cost, |outlier_strength|) = {r_max_abs:+.4f}")
    print(f"  Pearson r(sum_neighbor_cost, |outlier_strength|) = {r_sum_abs:+.4f}")
    print(f"  Pearson r(max_neighbor_cost, signed_outlier)     = {r_max_signed:+.4f}")
    print(f"  Pearson r(sum_neighbor_cost, signed_outlier)     = {r_sum_signed:+.4f}")
    print(f"  Spearman ρ(max, |outlier|) = {rho_max_abs:+.4f}")
    print(f"  Spearman ρ(sum, |outlier|) = {rho_sum_abs:+.4f}")
    print(f"  Spearman ρ(max, signed)    = {rho_max_signed:+.4f}")
    print(f"  Spearman ρ(sum, signed)    = {rho_sum_signed:+.4f}")

    # Permutation null on r(max, |outlier|)
    rng = random.Random(SEED)
    null_rs = []
    for _ in range(N_PERMS):
        shuffled = abs_outliers[:]
        rng.shuffle(shuffled)
        null_rs.append(pearson_r(max_costs, shuffled))
    p_max_abs = sum(1 for r in null_rs if r >= r_max_abs) / len(null_rs)
    print(f"\n--- PERMUTATION NULL ({N_PERMS} perms) ---")
    print(f"  p(r_max_abs ≥ observed) = {p_max_abs:.5f}")

    # Top-10 surahs by max_neighbor_cost
    paired = sorted(zip(surahs, max_costs, abs_outliers, signed_outliers), key=lambda t: -t[1])
    print(f"\n--- TOP-10 surahs by max_neighbor_cost ---")
    print(f"  {'Surah':>5}  {'max_cost':>9}  {'|Δ_outlier|':>12}  {'signed_outlier':>15}")
    for s, mc, ao, so in paired[:10]:
        print(f"  Q{s:>3}  {mc:>9.4f}  {ao:>12.2f}  {so:>+15.2f}")

    # Top-10 by |outlier|
    paired_o = sorted(zip(surahs, max_costs, abs_outliers, signed_outliers), key=lambda t: -t[2])
    print(f"\n--- TOP-10 surahs by |outlier_strength| ---")
    print(f"  {'Surah':>5}  {'|Δ_outlier|':>12}  {'signed':>10}  {'max_cost':>9}")
    for s, mc, ao, so in paired_o[:10]:
        print(f"  Q{s:>3}  {ao:>12.2f}  {so:>+10.2f}  {mc:>9.4f}")

    # Verdict
    if r_max_abs >= 0.5 and p_max_abs <= 0.025:
        verdict = f"STRONG CONVERGENCE — TSP-cost and outlier-strength independently identify architecturally-significant surahs (r={r_max_abs:.3f}, p={p_max_abs:.5f})"
    elif r_max_abs >= 0.3 and p_max_abs <= 0.05:
        verdict = f"DIRECTIONAL CONVERGENCE — partial overlap (r={r_max_abs:.3f}, p={p_max_abs:.5f})"
    else:
        verdict = f"NULL — TSP-cost and outlier-strength are independent (r={r_max_abs:.3f}, p={p_max_abs:.5f})"
    print(f"\n=== VERDICT: {verdict} ===")

    out = {
        "id": "H-NEW-830",
        "seed": SEED,
        "surahs": surahs,
        "max_costs": max_costs,
        "sum_costs": sum_costs,
        "abs_outliers": abs_outliers,
        "signed_outliers": signed_outliers,
        "correlations": {
            "pearson_max_abs": r_max_abs,
            "pearson_sum_abs": r_sum_abs,
            "pearson_max_signed": r_max_signed,
            "pearson_sum_signed": r_sum_signed,
            "spearman_max_abs": rho_max_abs,
            "spearman_sum_abs": rho_sum_abs,
        },
        "perm_p_max_abs": p_max_abs,
        "verdict": verdict,
        "top10_by_max_cost": [{"surah": s, "max_cost": mc, "abs_outlier": ao} for s, mc, ao, so in paired[:10]],
        "top10_by_abs_outlier": [{"surah": s, "abs_outlier": ao, "max_cost": mc} for s, mc, ao, so in paired_o[:10]],
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
