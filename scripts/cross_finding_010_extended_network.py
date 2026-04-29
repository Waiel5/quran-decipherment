"""cross-finding-010 — Extended Meta-Cluster Network (11 → 20 systems).

Pre-reg: findings/phase-b-hypotheses/cross-finding-010-extended-network-prereg.md
Family:  cross-finding-010-extended-network
Bonferroni k=3, α_bon=0.0167 (= 0.05 / 3).
N_PERM=10,000.
Seed=20260417.

Pipeline:
  1. Re-compute H-NEW-89's 11-cluster network as MW-5 positive control.
     HARD STOP if Q 62 does not emerge as the unique 4-hub.
  2. Compute extended 20-cluster incidence, degree, hubs, isolates.
  3. Compute 9-new-cluster-only sub-network (C12-C20).
  4. Test (C): Q 62 as hub in new-only sub-network vs membership-
     permuted null at α_bon = 0.0167.

Outputs:
  - findings/phase-b-hypotheses/csv/cross-finding-010.json
  - stdout summary
"""
from __future__ import annotations

import json
import random
import time
from collections import Counter
from pathlib import Path
from statistics import mean, variance

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260417
N_PERM = 10_000
BONFERRONI_K = 3
ALPHA_BON = 0.05 / BONFERRONI_K  # 0.01667
N_SURAHS = 114

# -----------------------------------------------------------------------------
# 20-CLUSTER LOCK  (matches pre-reg)
# -----------------------------------------------------------------------------
ORIGINAL_11: dict[str, dict] = {
    "C1_alif_lam_mim":       {"label": "الم muqaṭṭāʿat",      "members": frozenset({2, 3, 29, 30, 31, 32})},
    "C2_alif_lam_ra":        {"label": "الر muqaṭṭāʿat",      "members": frozenset({10, 11, 12, 14, 15})},
    "C3_ha_mim":             {"label": "ḥm muqaṭṭāʿat",       "members": frozenset({40, 41, 42, 43, 44, 45, 46})},
    "C4_ta_sin_mim":         {"label": "طسم muqaṭṭāʿat",      "members": frozenset({26, 27, 28})},
    "C5_musabbihat_inner":   {"label": "musabbiḥāt inner-5",  "members": frozenset({57, 59, 61, 62, 64})},
    "C6_sab_al_tiwal":       {"label": "al-sabʿ al-ṭiwāl",    "members": frozenset({2, 3, 4, 5, 6, 7, 9})},
    "C7_friday":             {"label": "Friday liturgy",      "members": frozenset({18, 32, 62, 76})},
    "C8_khawatim_extended":  {"label": "Khawātim al-Ḥashr",   "members": frozenset({59, 62})},
    "C9_muawwidhatan":       {"label": "al-muʿawwidhatān",    "members": frozenset({113, 114})},
    "C10_zahrawan":          {"label": "al-Zahrāwān",         "members": frozenset({2, 3})},
    "C11_mufassal":          {"label": "al-mufaṣṣal",         "members": frozenset(range(49, 115))},
}

NEW_9: dict[str, dict] = {
    "C12_oath_openers":      {"label": "oath-opener (H-NEW-85)",
                              "members": frozenset({36, 37, 38, 43, 44, 50, 51, 52, 53, 68,
                                                   77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103})},
    "C13_qul_v1w1":          {"label": "qul v1-w1 openers (H-NEW-74)",
                              "members": frozenset({72, 109, 112, 113, 114})},
    "C14_refrain_density":   {"label": "refrain-density ≥ 0.20 (H-NEW-83)",
                              "members": frozenset({55, 77})},
    "C15_divine_attr_named": {"label": "divine-attribute-named",
                              "members": frozenset({24, 35, 40, 55, 112})},
    "C16_prophet_named":     {"label": "prophet-named (strict)",
                              "members": frozenset({10, 11, 12, 14, 19, 47, 71})},
    "C17_muqattaat_single":  {"label": "muqaṭṭāʿat singletons",
                              "members": frozenset({13, 19, 20, 36, 38, 50, 68})},
    "C18_musabbihat_7":      {"label": "musabbiḥāt classical-7",
                              "members": frozenset({17, 57, 59, 61, 62, 64, 87})},
    "C19_book_ref_muq":      {"label": "book-ref muqaṭṭāʿat subset (H-NEW-53)",
                              "members": frozenset({2, 3, 7, 10, 11, 12, 13, 14, 15, 20,
                                                   26, 27, 28, 31, 32, 36, 38, 40, 41, 43,
                                                   44, 45, 46, 50})},
    "C20_invocation":        {"label": "invocation/refuge surahs",
                              "members": frozenset({1, 112, 113, 114})},
}

ALL_20 = {**ORIGINAL_11, **NEW_9}

# -----------------------------------------------------------------------------
# GRAPH METRICS (same signatures as H-NEW-89 for MW-5 compatibility)
# -----------------------------------------------------------------------------

def compute_degrees(clusters: dict[str, frozenset]) -> dict[int, int]:
    deg: dict[int, int] = {s: 0 for s in range(1, N_SURAHS + 1)}
    for members in clusters.values():
        for s in members:
            deg[s] += 1
    return deg


def degree_variance(deg: dict[int, int]) -> float:
    return variance(list(deg.values()))


def hub_zone_mean(deg: dict[int, int], K: int) -> float:
    sorted_s = sorted(deg.items(), key=lambda kv: (-kv[1], kv[0]))
    return mean(s for s, _ in sorted_s[:K])


def isolate_count(deg: dict[int, int]) -> int:
    return sum(1 for d in deg.values() if d == 0)


def get_top_hubs(deg: dict[int, int], K: int) -> list[tuple[int, int]]:
    return sorted(deg.items(), key=lambda kv: (-kv[1], kv[0]))[:K]


def get_isolates(deg: dict[int, int]) -> list[int]:
    return sorted(s for s, d in deg.items() if d == 0)


def surah_degree(deg: dict[int, int], surah_id: int) -> int:
    return deg.get(surah_id, 0)


def max_degree(deg: dict[int, int]) -> int:
    return max(deg.values())


# -----------------------------------------------------------------------------
# MEMBERSHIP-PERMUTED NULL
# -----------------------------------------------------------------------------

def permuted_null_draw(clusters: dict[str, dict], rng: random.Random) -> dict[str, frozenset]:
    universe = list(range(1, N_SURAHS + 1))
    out = {}
    for cname, spec in clusters.items():
        k = len(spec["members"])
        out[cname] = frozenset(rng.sample(universe, k))
    return out


def empirical_p_one_sided_upper(obs: float, null_vals) -> float:
    n = len(null_vals)
    k = sum(1 for v in null_vals if v >= obs)
    return (1 + k) / (1 + n)


def empirical_p_two_sided(obs: float, null_vals) -> float:
    n = len(null_vals)
    m = mean(null_vals)
    obs_dev = abs(obs - m)
    k = sum(1 for v in null_vals if abs(v - m) >= obs_dev)
    return (1 + k) / (1 + n)


# -----------------------------------------------------------------------------
# MW-5 POSITIVE CONTROL (re-run H-NEW-89's 11-cluster network)
# -----------------------------------------------------------------------------

def mw5_positive_control(rng: random.Random) -> dict:
    """Re-run H-NEW-89. HARD STOP if Q 62 is not the unique 4-hub."""
    deg = compute_degrees({k: v["members"] for k, v in ORIGINAL_11.items()})
    q62_deg = deg[62]
    top = get_top_hubs(deg, K=3)
    iso = isolate_count(deg)

    null_iso = []
    for _ in range(N_PERM):
        draw = permuted_null_draw(ORIGINAL_11, rng)
        d = compute_degrees(draw)
        null_iso.append(isolate_count(d))

    p_iso = empirical_p_two_sided(iso, null_iso)

    # Must pass: Q 62 degree == 4, top surah at 4 UNIQUE, iso p ≤ 0.01
    mw5_passes = (
        q62_deg == 4
        and top[0] == (62, 4)
        and top[1][1] <= 3
        and iso == 21
        and p_iso <= 0.001
    )
    return {
        "q62_degree": q62_deg,
        "top_3": top,
        "isolate_count": iso,
        "p_iso_two_sided": p_iso,
        "null_iso_mean": mean(null_iso),
        "mw5_passes": mw5_passes,
    }


# -----------------------------------------------------------------------------
# PRODUCTS A / B / C
# -----------------------------------------------------------------------------

def product_A_degree_distribution(clusters: dict[str, dict]) -> dict:
    """Updated 20-cluster degree distribution + hub list."""
    deg = compute_degrees({k: v["members"] for k, v in clusters.items()})
    hist = Counter(deg.values())
    top = get_top_hubs(deg, K=15)
    return {
        "per_surah_degree": dict(sorted(deg.items())),
        "degree_histogram": {str(d): c for d, c in sorted(hist.items())},
        "top_15_hubs": [
            {
                "rank": r,
                "surah": s,
                "degree": d,
                "clusters": [c for c, spec in clusters.items() if s in spec["members"]],
                "cluster_labels": [spec["label"] for c, spec in clusters.items() if s in spec["members"]],
            }
            for r, (s, d) in enumerate(top, 1)
        ],
        "q62_degree": deg[62],
        "q62_clusters": [c for c, spec in clusters.items() if 62 in spec["members"]],
        "q62_cluster_labels": [spec["label"] for c, spec in clusters.items() if 62 in spec["members"]],
        "new_hubs_at_degree_4_plus": [
            {"surah": s, "degree": d}
            for s, d in deg.items()
            if d >= 4 and s != 62
        ],
        "max_degree": max(deg.values()),
        "degree_variance": degree_variance(deg),
    }


def product_B_isolate_count(clusters: dict[str, dict], baseline_isolates: list[int]) -> dict:
    """Updated isolate count + Q 16-25 tracking."""
    deg = compute_degrees({k: v["members"] for k, v in clusters.items()})
    iso = get_isolates(deg)
    q16_25 = [s for s in iso if 16 <= s <= 25]

    exited = sorted(set(baseline_isolates) - set(iso))
    entered = sorted(set(iso) - set(baseline_isolates))

    return {
        "total_isolates": len(iso),
        "isolate_surahs": iso,
        "q16_25_isolates": q16_25,
        "q16_25_isolate_count": len(q16_25),
        "baseline_isolates_count_H89": len(baseline_isolates),
        "isolates_EXITED_from_H89": exited,
        "isolates_ENTERED_vs_H89": entered,
    }


def product_C_new_only_independence(rng: random.Random) -> dict:
    """New-cluster-only sub-network (C12-C20 only). Test Q 62 hub p."""
    deg = compute_degrees({k: v["members"] for k, v in NEW_9.items()})
    q62_deg = deg[62]
    top = get_top_hubs(deg, K=15)
    iso = get_isolates(deg)
    max_deg = max_degree(deg)

    # Null: permute each of C12-C20 with its size preserved, measure max degree
    null_max_deg = []
    null_q62_deg = []
    for _ in range(N_PERM):
        draw = permuted_null_draw(NEW_9, rng)
        d = compute_degrees(draw)
        null_max_deg.append(max_degree(d))
        null_q62_deg.append(d[62])

    # Two-sided p-value on Q 62's observed degree vs null Q 62 degree distribution
    p_q62 = empirical_p_two_sided(q62_deg, null_q62_deg)
    # Two-sided p-value on overall max degree (structural hub emergence)
    p_max = empirical_p_two_sided(max_deg, null_max_deg)

    # Bonferroni-3-corrected threshold
    q62_bon_pass = p_q62 <= ALPHA_BON
    max_bon_pass = p_max <= ALPHA_BON

    return {
        "new_only_per_surah_degree": dict(sorted(deg.items())),
        "new_only_top_15_hubs": [
            {
                "rank": r,
                "surah": s,
                "degree": d,
                "clusters": [c for c, spec in NEW_9.items() if s in spec["members"]],
                "cluster_labels": [spec["label"] for c, spec in NEW_9.items() if s in spec["members"]],
            }
            for r, (s, d) in enumerate(top, 1)
        ],
        "new_only_q62_degree": q62_deg,
        "new_only_q62_clusters": [c for c, spec in NEW_9.items() if 62 in spec["members"]],
        "new_only_q62_cluster_labels": [spec["label"] for c, spec in NEW_9.items() if 62 in spec["members"]],
        "new_only_max_degree": max_deg,
        "new_only_n_isolates": len(iso),
        "null_max_deg_mean": mean(null_max_deg),
        "null_q62_deg_mean": mean(null_q62_deg),
        "p_q62_two_sided": p_q62,
        "p_max_deg_two_sided": p_max,
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "q62_bon_pass": q62_bon_pass,
        "max_bon_pass": max_bon_pass,
    }


# -----------------------------------------------------------------------------
# FULL INCIDENCE MATRIX
# -----------------------------------------------------------------------------

def build_incidence_matrix(clusters: dict[str, dict]) -> dict:
    """(surah, cluster) -> 0/1 dict.  Also return per-cluster membership lists."""
    names = list(clusters.keys())
    matrix = {}
    for s in range(1, N_SURAHS + 1):
        matrix[s] = {c: int(s in clusters[c]["members"]) for c in names}
    return {
        "cluster_order": names,
        "cluster_labels": {c: clusters[c]["label"] for c in names},
        "cluster_sizes": {c: len(clusters[c]["members"]) for c in names},
        "cluster_members": {c: sorted(clusters[c]["members"]) for c in names},
        "per_surah_incidence": {str(s): matrix[s] for s in range(1, N_SURAHS + 1)},
    }


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

def main() -> None:
    t0 = time.time()
    rng = random.Random(SEED)

    # MW-5 positive control (uses a separate RNG branch to avoid biasing later)
    print("=" * 78)
    print("MW-5 positive control — re-running H-NEW-89 (11-cluster)")
    print("=" * 78)
    mw5_rng = random.Random(SEED + 1000)
    mw5 = mw5_positive_control(mw5_rng)
    print(f"  Q 62 degree: {mw5['q62_degree']} (expected 4)")
    print(f"  top-3 hubs:  {mw5['top_3']}")
    print(f"  isolate count: {mw5['isolate_count']} (expected 21)")
    print(f"  p_iso two-sided: {mw5['p_iso_two_sided']:.6f} (expected ≤ 0.001)")
    print(f"  null iso mean: {mw5['null_iso_mean']:.2f} (expected ≈ 32.6)")
    print(f"  MW-5 PASSES: {mw5['mw5_passes']}")
    if not mw5["mw5_passes"]:
        raise SystemExit("MW-5 POSITIVE CONTROL FAILED — stopping. "
                         "The pipeline does not recover H-NEW-89.")

    # Product A — updated degree distribution (20-cluster)
    print("\n" + "=" * 78)
    print("Product (A) — 20-cluster degree distribution")
    print("=" * 78)
    prod_A = product_A_degree_distribution(ALL_20)
    print(f"  Q 62 degree (20-cluster):  {prod_A['q62_degree']}")
    print(f"  Q 62 cluster memberships:  {prod_A['q62_cluster_labels']}")
    print(f"  Max degree:                {prod_A['max_degree']}")
    print(f"  Top-15 hubs:")
    for row in prod_A["top_15_hubs"]:
        print(f"    #{row['rank']:>2}  Q{row['surah']:<3}  degree={row['degree']}  "
              f"[{', '.join(row['cluster_labels'])}]")
    print(f"  New hubs at degree ≥ 4 (excluding Q 62):")
    for row in prod_A["new_hubs_at_degree_4_plus"]:
        print(f"    Q{row['surah']:<3} degree={row['degree']}")

    # Product B — isolate count (20-cluster)
    print("\n" + "=" * 78)
    print("Product (B) — 20-cluster isolate count")
    print("=" * 78)
    baseline_H89 = [1, 8, 13, 16, 17, 19, 20, 21, 22, 23, 24, 25, 33, 34, 35, 36, 37, 38, 39, 47, 48]
    prod_B = product_B_isolate_count(ALL_20, baseline_H89)
    print(f"  Total isolates:   {prod_B['total_isolates']} (H-NEW-89 baseline 21)")
    print(f"  Isolate surahs:   {prod_B['isolate_surahs']}")
    print(f"  Q 16-25 isolates: {prod_B['q16_25_isolates']} "
          f"({prod_B['q16_25_isolate_count']}/10 — baseline 8/10)")
    print(f"  Isolates EXITED from H-NEW-89:   {prod_B['isolates_EXITED_from_H89']}")
    print(f"  Isolates ENTERED vs H-NEW-89:    {prod_B['isolates_ENTERED_vs_H89']}")

    # Product C — new-cluster-only independence test
    print("\n" + "=" * 78)
    print("Product (C) — 9-new-cluster-only independence test")
    print("=" * 78)
    cell_c_rng = random.Random(SEED + 2000)
    prod_C = product_C_new_only_independence(cell_c_rng)
    print(f"  Q 62 degree (new-only):      {prod_C['new_only_q62_degree']}")
    print(f"  Q 62 clusters (new-only):    {prod_C['new_only_q62_cluster_labels']}")
    print(f"  Max degree (new-only):       {prod_C['new_only_max_degree']}")
    print(f"  Null Q 62 deg mean:          {prod_C['null_q62_deg_mean']:.3f}")
    print(f"  Null max deg mean:           {prod_C['null_max_deg_mean']:.3f}")
    print(f"  p (Q 62 degree) two-sided:   {prod_C['p_q62_two_sided']:.5f}  "
          f"{'✓' if prod_C['q62_bon_pass'] else '✗'}  (α_bon={ALPHA_BON:.4f})")
    print(f"  p (max degree) two-sided:    {prod_C['p_max_deg_two_sided']:.5f}  "
          f"{'✓' if prod_C['max_bon_pass'] else '✗'}")
    print(f"  Top-15 hubs (new-only):")
    for row in prod_C["new_only_top_15_hubs"]:
        print(f"    #{row['rank']:>2}  Q{row['surah']:<3}  degree={row['degree']}  "
              f"[{', '.join(row['cluster_labels'])}]")

    # VERDICT
    sig_count_C = sum([prod_C["q62_bon_pass"], prod_C["max_bon_pass"]])
    if sig_count_C >= 1:
        verdict_C = "PASS"
    else:
        verdict_C = "NULL"

    print("\n" + "=" * 78)
    print(f"  VERDICT: cross-finding-010 Cell C = {verdict_C} "
          f"({sig_count_C} / 2 sub-tests pass α_bon)")
    print("=" * 78)
    print(f"  (Cells A + B are descriptive; see above.)")

    # Full incidence matrix
    incidence = build_incidence_matrix(ALL_20)

    # Write JSON
    out = {
        "id": "cross-finding-010",
        "title": "Extended Meta-Cluster Network (20-cluster)",
        "date": "2026-04-17",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": BONFERRONI_K,
        "bonferroni_family": "cross-finding-010-extended-network",
        "alpha_bon": ALPHA_BON,
        "elapsed_sec": time.time() - t0,
        "clusters_locked": {
            cname: {
                "label": spec["label"],
                "members": sorted(spec["members"]),
                "size": len(spec["members"]),
                "is_original_H89": cname in ORIGINAL_11,
            }
            for cname, spec in ALL_20.items()
        },
        "mw5_positive_control": mw5,
        "product_A_degree_distribution": prod_A,
        "product_B_isolate_count": prod_B,
        "product_C_new_only_independence_test": prod_C,
        "incidence_matrix": incidence,
        "verdict_cell_C": verdict_C,
    }

    out_path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "cross-finding-010.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\nwrote {out_path}")
    print(f"elapsed: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
