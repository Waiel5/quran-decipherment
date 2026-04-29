"""H-NEW-89 — Meta-Cluster Network Synthesis.

Pre-reg: findings/phase-b-hypotheses/h-new-89-meta-cluster-network-prereg.md
Family:  2026-04-15-Wave-Meta-Cluster-Network
Bonferroni k=4, α_bon=0.0125.
N_PERM=10,000.
Seed=20260416.

Builds bipartite incidence (114 surahs × 11 cluster systems),
computes degree distribution, identifies structural hubs + isolates,
tests 3 inferential cells against membership-permuted null.

Cluster systems locked from existing findings:
  C1  الم muqaṭṭāʿat       {2, 3, 29, 30, 31, 32}           n=6
  C2  الر muqaṭṭāʿat       {10, 11, 12, 14, 15}              n=5
  C3  ḥm muqaṭṭāʿat        {40, 41, 42, 43, 44, 45, 46}      n=7
  C4  طسم muqaṭṭāʿat       {26, 27, 28}                      n=3
  C5  musabbiḥāt          {57, 59, 61, 62, 64}              n=5
  C6  al-sabʿ al-ṭiwāl    {2, 3, 4, 5, 6, 7, 9}             n=7
  C7  Friday liturgy       {18, 32, 62, 76}                  n=4
  C8  Khawātim al-Ḥashr   {59, 62}                          n=2
  C9  al-muʿawwidhatān    {113, 114}                        n=2
  C10 al-Zahrāwān          {2, 3}                            n=2
  C11 al-mufaṣṣal         {49..114}                         n=66

Metrics:
  M1 — per-surah degree (descriptive ranked list)
  M2 — degree-variance ratio (one-sided: observed > null)
  M3 — hub-zone concentration (two-sided: mean mushaf position of top-11 hubs)
  M4 — isolate-count (two-sided: observed vs null)

Outputs:
  - findings/phase-b-hypotheses/csv/h-new-89.json
  - stdout summary
"""
from __future__ import annotations

import hashlib
import json
import random
import time
from collections import Counter
from pathlib import Path
from statistics import mean, variance

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260416
N_PERM = 10_000
BONFERRONI_K = 4
ALPHA_BON = 0.05 / BONFERRONI_K  # 0.0125
N_SURAHS = 114

# -----------------------------------------------------------------------------
# LOCKED CLUSTER SYSTEMS (from pre-reg)
# -----------------------------------------------------------------------------
CLUSTERS: dict[str, dict] = {
    "C1_alif_lam_mim":       {"label": "الم muqaṭṭāʿat",      "members": frozenset({2, 3, 29, 30, 31, 32})},
    "C2_alif_lam_ra":        {"label": "الر muqaṭṭāʿat",      "members": frozenset({10, 11, 12, 14, 15})},
    "C3_ha_mim":             {"label": "ḥm muqaṭṭāʿat",       "members": frozenset({40, 41, 42, 43, 44, 45, 46})},
    "C4_ta_sin_mim":         {"label": "طسم muqaṭṭāʿat",      "members": frozenset({26, 27, 28})},
    "C5_musabbihat":         {"label": "musabbiḥāt",          "members": frozenset({57, 59, 61, 62, 64})},
    "C6_sab_al_tiwal":       {"label": "al-sabʿ al-ṭiwāl",    "members": frozenset({2, 3, 4, 5, 6, 7, 9})},
    "C7_friday":             {"label": "Friday liturgy",      "members": frozenset({18, 32, 62, 76})},
    "C8_khawatim_extended":  {"label": "Khawātim al-Ḥashr",   "members": frozenset({59, 62})},
    "C9_muawwidhatan":       {"label": "al-muʿawwidhatān",    "members": frozenset({113, 114})},
    "C10_zahrawan":          {"label": "al-Zahrāwān",         "members": frozenset({2, 3})},
    "C11_mufassal":          {"label": "al-mufaṣṣal",         "members": frozenset(range(49, 115))},
}
CLUSTER_NAMES = list(CLUSTERS.keys())
CLUSTER_SIZES = {c: len(CLUSTERS[c]["members"]) for c in CLUSTER_NAMES}

# -----------------------------------------------------------------------------
# INCIDENCE + GRAPH PROJECTION
# -----------------------------------------------------------------------------

def compute_degrees(clusters: dict[str, frozenset]) -> dict[int, int]:
    """For each surah, count how many clusters it belongs to."""
    deg: dict[int, int] = {s: 0 for s in range(1, N_SURAHS + 1)}
    for cname, members in clusters.items():
        for s in members:
            deg[s] += 1
    return deg


def degree_variance(deg: dict[int, int]) -> float:
    return variance(list(deg.values()))


def hub_zone_mean(deg: dict[int, int], K: int) -> float:
    """Mean mushaf position of top-K hubs (ties broken by mushaf order)."""
    # Sort by (-degree, mushaf_idx) so ties go to earlier surahs
    sorted_s = sorted(deg.items(), key=lambda kv: (-kv[1], kv[0]))
    top_k = [s for s, d in sorted_s[:K]]
    return mean(top_k)


def isolate_count(deg: dict[int, int]) -> int:
    return sum(1 for d in deg.values() if d == 0)


def get_top_hubs(deg: dict[int, int], K: int) -> list[tuple[int, int]]:
    """Return [(surah_id, degree), ...] for top-K hubs."""
    sorted_s = sorted(deg.items(), key=lambda kv: (-kv[1], kv[0]))
    return sorted_s[:K]


def get_all_isolates(deg: dict[int, int]) -> list[int]:
    return sorted(s for s, d in deg.items() if d == 0)


# -----------------------------------------------------------------------------
# NULL: membership-permuted
# -----------------------------------------------------------------------------

def permuted_null_draw(rng: random.Random) -> dict[str, frozenset]:
    """Each cluster keeps its cardinality; members re-drawn from {1..114}."""
    universe = list(range(1, N_SURAHS + 1))
    out = {}
    for cname in CLUSTER_NAMES:
        k = CLUSTER_SIZES[cname]
        out[cname] = frozenset(rng.sample(universe, k))
    return out


def run_null(n_perm: int, rng: random.Random) -> dict:
    """Run n_perm membership-permuted nulls; return observed stats arrays."""
    null_var = []
    null_hub_mean = []
    null_iso = []
    for _ in range(n_perm):
        draw = permuted_null_draw(rng)
        deg = compute_degrees(draw)
        null_var.append(degree_variance(deg))
        null_hub_mean.append(hub_zone_mean(deg, K=11))
        null_iso.append(isolate_count(deg))
    return {"var": null_var, "hub_mean": null_hub_mean, "iso": null_iso}


def empirical_p_one_sided_upper(obs: float, null_vals: list[float]) -> float:
    """p = (1 + |{null ≥ obs}|) / (1 + N)."""
    n = len(null_vals)
    k = sum(1 for v in null_vals if v >= obs)
    return (1 + k) / (1 + n)


def empirical_p_two_sided(obs: float, null_vals: list[float]) -> float:
    """Two-sided by absolute deviation from null mean."""
    n = len(null_vals)
    null_mean = mean(null_vals)
    obs_dev = abs(obs - null_mean)
    k = sum(1 for v in null_vals if abs(v - null_mean) >= obs_dev)
    return (1 + k) / (1 + n)


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

def main() -> None:
    t0 = time.time()
    rng = random.Random(SEED)

    # OBSERVED
    observed_clusters = {cname: CLUSTERS[cname]["members"] for cname in CLUSTER_NAMES}
    deg_obs = compute_degrees(observed_clusters)
    obs_var = degree_variance(deg_obs)
    obs_hub_mean = hub_zone_mean(deg_obs, K=11)
    obs_iso = isolate_count(deg_obs)
    top_hubs = get_top_hubs(deg_obs, K=11)
    all_isolates = get_all_isolates(deg_obs)

    # Degree histogram
    deg_hist = Counter(deg_obs.values())

    # NULL
    print(f"running {N_PERM} membership-permuted nulls (seed {SEED})...", flush=True)
    nulls = run_null(N_PERM, rng)

    # P-values
    p_var = empirical_p_one_sided_upper(obs_var, nulls["var"])  # one-sided upper
    p_hub = empirical_p_two_sided(obs_hub_mean, nulls["hub_mean"])  # two-sided
    p_iso = empirical_p_two_sided(obs_iso, nulls["iso"])  # two-sided

    null_var_mean = mean(nulls["var"])
    null_hub_mean_m = mean(nulls["hub_mean"])
    null_iso_mean = mean(nulls["iso"])

    # Per-cluster pairwise co-membership (informative cross-cluster intersection matrix)
    pair_intersect = {}
    for i, ci in enumerate(CLUSTER_NAMES):
        for cj in CLUSTER_NAMES[i + 1 :]:
            k = len(observed_clusters[ci] & observed_clusters[cj])
            if k > 0:
                pair_intersect[f"{ci} ∩ {cj}"] = {
                    "intersection_size": k,
                    "members": sorted(observed_clusters[ci] & observed_clusters[cj]),
                }

    # OUTPUTS
    bonferroni_pass_var = p_var <= ALPHA_BON
    bonferroni_pass_hub = p_hub <= ALPHA_BON
    bonferroni_pass_iso = p_iso <= ALPHA_BON

    sig_count = sum([bonferroni_pass_var, bonferroni_pass_hub, bonferroni_pass_iso])
    if sig_count >= 2:
        verdict = "PASS"
    elif sig_count == 1:
        verdict = "MARGINAL"
    else:
        verdict = "NULL"

    # Summary printout
    print("\n=== H-NEW-89 — META-CLUSTER NETWORK RESULT ===")
    print(f"# clusters:   {len(CLUSTER_NAMES)}")
    print(f"# surahs:     {N_SURAHS}")
    print(f"N_PERM:       {N_PERM}")
    print(f"seed:         {SEED}")
    print(f"α_bon:        {ALPHA_BON}")
    print(f"elapsed:      {time.time() - t0:.1f}s")
    print()
    print("--- Degree histogram (clusters-per-surah) ---")
    for d in sorted(deg_hist.keys()):
        count = deg_hist[d]
        bar = "█" * min(50, count)
        print(f"  degree {d}: {count:>3} surahs {bar}")
    print()
    print("--- Top-11 hub surahs (highest cluster-degree) ---")
    for rank, (s, d) in enumerate(top_hubs, 1):
        # Which clusters does surah s belong to?
        cl_list = [c for c in CLUSTER_NAMES if s in observed_clusters[c]]
        cl_str = ", ".join(CLUSTERS[c]["label"] for c in cl_list)
        print(f"  {rank:>2}. Q{s:<3} degree={d}  [{cl_str}]")
    print()
    print(f"--- Isolate surahs (degree 0): {len(all_isolates)} total ---")
    print(f"  {sorted(all_isolates)}")
    print()
    print("--- Inferential cells ---")
    print(f"M2 variance ratio:     obs={obs_var:.4f}  null-mean={null_var_mean:.4f}  p1-sided={p_var:.5f}  {'✓' if bonferroni_pass_var else '✗'}")
    print(f"M3 hub-zone mean:      obs={obs_hub_mean:.2f}  null-mean={null_hub_mean_m:.2f}  p2-sided={p_hub:.5f}  {'✓' if bonferroni_pass_hub else '✗'}")
    print(f"M4 isolate count:      obs={obs_iso}  null-mean={null_iso_mean:.2f}  p2-sided={p_iso:.5f}  {'✓' if bonferroni_pass_iso else '✗'}")
    print()
    print(f"--- Verdict: {verdict} ({sig_count} / 3 inferential cells significant at α_bon={ALPHA_BON}) ---")

    # JSON output
    out = {
        "id": "H-NEW-89",
        "date": "2026-04-15",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "clusters_locked": {
            cname: {
                "label": CLUSTERS[cname]["label"],
                "members": sorted(CLUSTERS[cname]["members"]),
                "size": CLUSTER_SIZES[cname],
            }
            for cname in CLUSTER_NAMES
        },
        "observed": {
            "degree_by_surah": deg_obs,
            "degree_histogram": {str(d): c for d, c in sorted(deg_hist.items())},
            "top_11_hubs": [
                {
                    "rank": r,
                    "surah": s,
                    "degree": d,
                    "clusters": [c for c in CLUSTER_NAMES if s in observed_clusters[c]],
                    "cluster_labels": [CLUSTERS[c]["label"] for c in CLUSTER_NAMES if s in observed_clusters[c]],
                }
                for r, (s, d) in enumerate(top_hubs, 1)
            ],
            "isolates": all_isolates,
            "n_isolates": len(all_isolates),
            "degree_variance": obs_var,
            "hub_zone_mean_top11": obs_hub_mean,
            "isolate_count": obs_iso,
        },
        "cluster_pairwise_intersections": pair_intersect,
        "null_stats": {
            "variance": {"mean": null_var_mean, "obs": obs_var, "p_one_sided_upper": p_var, "bon_pass": bonferroni_pass_var},
            "hub_zone_mean": {"mean": null_hub_mean_m, "obs": obs_hub_mean, "p_two_sided": p_hub, "bon_pass": bonferroni_pass_hub},
            "isolate_count": {"mean": null_iso_mean, "obs": obs_iso, "p_two_sided": p_iso, "bon_pass": bonferroni_pass_iso},
        },
        "verdict": verdict,
        "n_inferential_cells_significant": sig_count,
    }
    out_path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "h-new-89.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
