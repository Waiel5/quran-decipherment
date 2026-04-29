#!/usr/bin/env python3
"""H-NEW-840: Unified Architectural Significance Score (UAS).

Combines 3 independent architectural metrics from prior findings:
  1. |outlier_strength|  (H-NEW-590) — content-distinctness
  2. max_neighbor_TSP_cost (H-NEW-720) — canonical-adjacency-cost
  3. |iʿjāz_signature_per_surah| (H-NEW-750 sig_A) — content × rhyme anti-twin

Each is z-normalized; UAS = z_outlier + z_tsp_cost + z_iʿjāz.
Top-ranked surahs are the corpus's most architecturally-significant under joint criterion.
"""
import json
import math
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_590 = ROOT / "findings/phase-b-hypotheses/csv/h-new-590.json"
H_NEW_720 = ROOT / "findings/phase-b-hypotheses/csv/h-new-720.json"
H_NEW_750 = ROOT / "findings/phase-b-hypotheses/csv/h-new-750.json"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-840.json"


def zscore(arr):
    m = sum(arr)/len(arr)
    sd = math.sqrt(sum((x-m)**2 for x in arr)/len(arr))
    return [(x-m)/sd for x in arr] if sd > 0 else [0.0]*len(arr)


def main():
    print("=== H-NEW-840 (Unified Architectural Significance Score) ===\n")

    with open(H_NEW_590) as f: h590 = json.load(f)
    with open(H_NEW_720) as f: h720 = json.load(f)
    with open(H_NEW_750) as f: h750 = json.load(f)

    # Per-surah outlier strength (signed delta_pct)
    outlier = {e["X"]: e["delta_pct"] for e in h590["all_surahs_results"]}

    # Per-surah max-neighbor TSP cost (max of left+right canonical-adjacency Δ)
    adj_costs = {e["s"]: e["delta_raw"] for e in h720["per_adjacency"]}
    def max_neighbor_cost(s):
        l = adj_costs.get(s - 1, 0.0)
        r = adj_costs.get(s, 0.0)
        return max(max(l, 0), max(r, 0))  # clip negative (super-additive artefacts)

    # Per-surah iʿjāz signature (sig_A from H-NEW-750)
    ijaz = {e["surah"]: e["sig_A"] for e in h750["per_surah"]}

    # Build aligned arrays
    surahs = list(range(1, 115))
    out_abs = [abs(outlier.get(s, 0.0)) for s in surahs]
    cost_max = [max_neighbor_cost(s) for s in surahs]
    ijaz_abs = [abs(ijaz.get(s, 0.0)) for s in surahs]

    # Z-normalize each
    z_out = zscore(out_abs)
    z_cost = zscore(cost_max)
    z_ijaz = zscore(ijaz_abs)

    # UAS
    uas = [z_out[i] + z_cost[i] + z_ijaz[i] for i in range(len(surahs))]

    # Rank
    ranked = sorted(zip(surahs, uas, out_abs, cost_max, ijaz_abs), key=lambda t: -t[1])

    print(f"{'Rank':>4}  {'Surah':>5}  {'UAS':>7}  {'|outlier|':>10}  {'max_cost':>9}  {'|iʿjāz|':>8}")
    print("-" * 60)
    for rank, (s, u, o, c, i) in enumerate(ranked[:20], 1):
        print(f"  {rank:>2}.  Q{s:>3}  {u:>+7.2f}  {o:>10.2f}  {c:>9.4f}  {i:>8.2f}")
    print(f"\n--- BOTTOM 10 (least architecturally-significant) ---")
    for rank, (s, u, o, c, i) in enumerate(ranked[-10:], len(ranked) - 9):
        print(f"  {rank:>2}.  Q{s:>3}  {u:>+7.2f}  {o:>10.2f}  {c:>9.4f}  {i:>8.2f}")

    # Validate convergence: how many top-10 are flagged by ALL 3 metrics?
    top10_outlier = sorted(zip(surahs, out_abs), key=lambda t: -t[1])[:15]
    top10_cost = sorted(zip(surahs, cost_max), key=lambda t: -t[1])[:15]
    top10_ijaz = sorted(zip(surahs, ijaz_abs), key=lambda t: -t[1])[:15]
    top_uas_set = set(s for s, *_ in ranked[:15])
    top_outlier_set = set(s for s, _ in top10_outlier)
    top_cost_set = set(s for s, _ in top10_cost)
    top_ijaz_set = set(s for s, _ in top10_ijaz)

    print(f"\n--- TOP-15 OVERLAP ANALYSIS ---")
    triple_intersection = top_outlier_set & top_cost_set & top_ijaz_set
    print(f"  Surahs in top-15 of ALL 3 metrics: {sorted(triple_intersection)}")
    pair_oc = top_outlier_set & top_cost_set
    pair_oi = top_outlier_set & top_ijaz_set
    pair_ci = top_cost_set & top_ijaz_set
    print(f"  outlier ∩ cost (top-15): {sorted(pair_oc)}")
    print(f"  outlier ∩ ijaz (top-15): {sorted(pair_oi)}")
    print(f"  cost ∩ ijaz (top-15): {sorted(pair_ci)}")

    # Save
    out = {
        "id": "H-NEW-840",
        "method": "UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)",
        "top_15": [{"rank": i+1, "surah": s, "UAS": u, "abs_outlier": o, "max_cost": c, "abs_ijaz": i_}
                   for i, (s, u, o, c, i_) in enumerate(ranked[:15])],
        "bottom_10": [{"rank": len(ranked)-9+i, "surah": s, "UAS": u, "abs_outlier": o, "max_cost": c, "abs_ijaz": i_}
                      for i, (s, u, o, c, i_) in enumerate(ranked[-10:])],
        "triple_intersection_top15": sorted(triple_intersection),
        "all_uas": [{"surah": s, "UAS": u, "abs_outlier": o, "max_cost": c, "abs_ijaz": i_}
                    for s, u, o, c, i_ in ranked],
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
