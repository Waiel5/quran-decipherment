#!/usr/bin/env python3
"""H-NEW-236.1g - Direct isolated-tranche test.

Pre-reg:
  findings/phase-b-hypotheses/h-new-236-1g-direct-tranche-test-prereg.md

Parents:
  - H-NEW-236.1d: decisive K=95->100 tranche
  - H-NEW-236.1f: cumulative late-tail hard-prefix repair failed

Design:
  Test the exact decisive tranche, its core, and its overlap pair
  directly instead of nesting them inside the failed cumulative prefix.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import h_new_236_1f_tail_repair_scaffold as family

SEED = 20260424
N_SIM = 1000
N_RANDOM = 1000
SA_ITERS = 200

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H2361C_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1c.json"
H2361D_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1d.json"
H2361F_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1f.json"
PREREG = (
    PROJECT_ROOT
    / "findings/phase-b-hypotheses/h-new-236-1g-direct-tranche-test-prereg.md"
)
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1g.json"

CELL_A_NAME = "cell_a_top50_plus_j30_top5"
TOP50_KEY = "baseline_h2361a_top50"
TOP95_NAME = "cell_top95"
TOP100_NAME = "cell_top100"

EXACT_DECISIVE_TRANCHE_1INDEXED = [
    (92, 93),
    (99, 100),
    (100, 101),
    (101, 102),
    (109, 110),
]
CORE_TRANCHE_1INDEXED = [
    (99, 100),
    (100, 101),
    (101, 102),
]
OVERLAP_PAIR_1INDEXED = [
    (92, 93),
    (109, 110),
]

CELL_SPECS = [
    (
        "mw5_positive_control_cell_a_base",
        "h2361c_cell_a_base_only",
        CELL_A_NAME,
        [],
        0,
    ),
    (
        "cell_a_base_plus_exact_tranche",
        "h2361c_cell_a_base_plus_exact_decisive_tranche",
        CELL_A_NAME,
        EXACT_DECISIVE_TRANCHE_1INDEXED,
        100_000,
    ),
    (
        "cell_b_base_plus_core_only",
        "h2361c_cell_a_base_plus_core_only",
        CELL_A_NAME,
        CORE_TRANCHE_1INDEXED,
        200_000,
    ),
    (
        "cell_c_base_plus_overlap_pair_only",
        "h2361c_cell_a_base_plus_overlap_pair_only",
        CELL_A_NAME,
        OVERLAP_PAIR_1INDEXED,
        300_000,
    ),
    (
        "cell_d_top50_plus_exact_tranche",
        "h2361a_top50_base_plus_exact_decisive_tranche",
        TOP50_KEY,
        EXACT_DECISIVE_TRANCHE_1INDEXED,
        400_000,
    ),
]


def prereg_sha256() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def dedup_hinges(hinges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    seen: set[tuple[int, int]] = set()
    out: list[tuple[int, int]] = []
    for pair in hinges:
        if pair in seen:
            continue
        seen.add(pair)
        out.append(pair)
    return out


def load_parent_context(dmat: list[list[float]]) -> dict:
    with H2361C_JSON.open() as f:
        data_c = json.load(f)
    with H2361D_JSON.open() as f:
        data_d = json.load(f)
    with H2361F_JSON.open() as f:
        data_f = json.load(f)

    cell_a = data_c["cells"][CELL_A_NAME]
    top50 = data_c[TOP50_KEY]
    cell_top95 = data_d["cells"][TOP95_NAME]
    cell_top100 = data_d["cells"][TOP100_NAME]

    cell_a_hinges = [tuple(pair) for pair in cell_a["hinges_1indexed"]]
    top50_hinges = [tuple(pair) for pair in top50["hinges_1indexed"]]
    top95_hinges = {tuple(pair) for pair in cell_top95["hinges_1indexed"]}
    top100_hinges = {tuple(pair) for pair in cell_top100["hinges_1indexed"]}

    tranche_from_1d = top100_hinges - top95_hinges
    if tranche_from_1d != set(EXACT_DECISIVE_TRANCHE_1INDEXED):
        raise AssertionError(
            "H-NEW-236.1d K=95->100 delta does not match the locked decisive tranche"
        )

    if set(CORE_TRANCHE_1INDEXED) | set(OVERLAP_PAIR_1INDEXED) != set(
        EXACT_DECISIVE_TRANCHE_1INDEXED
    ):
        raise AssertionError("Core + overlap pair must equal the exact decisive tranche")
    if set(CORE_TRANCHE_1INDEXED) & set(OVERLAP_PAIR_1INDEXED):
        raise AssertionError("Core and overlap pair must be disjoint")

    rank_map = {
        (row["a"], row["b"]): row["rank"]
        for row in family.canonical_edge_ranking(dmat)
    }
    decisive_tranche_edge_ranks = [
        {
            "edge_1indexed": [a, b],
            "global_rank": rank_map[(a, b)],
            "distance": float(dmat[a - 1][b - 1]),
            "in_core": [a, b] in [[x, y] for x, y in CORE_TRANCHE_1INDEXED],
            "in_overlap_pair": [a, b] in [[x, y] for x, y in OVERLAP_PAIR_1INDEXED],
        }
        for a, b in EXACT_DECISIVE_TRANCHE_1INDEXED
    ]

    return {
        "cell_a_hinges_1indexed": cell_a_hinges,
        "top50_hinges_1indexed": top50_hinges,
        "cell_a_parent_metrics": {
            "L_path": cell_a["full_analysis"]["L_path"],
            "L_tail_91_114": cell_a["full_analysis"]["L_tail_91_114"],
            "L_mufassal_short": cell_a["full_analysis"]["L_mufassal_short"],
            "Block_chi2": cell_a["block_chi2"],
            "sim_passes": cell_a["sim_passes"],
            "cell_verdict": cell_a["cell_verdict"],
        },
        "top50_parent_metrics": {
            "l_path_gap": top50["l_path_gap"],
            "block_chi2": top50["block_chi2"],
            "mufassal_gap": top50["mufassal_gap"],
            "mufassal_sim_mean": top50["mufassal_sim_mean"],
        },
        "top95_parent_metrics": {
            "L_path": cell_top95["full_analysis"]["L_path"],
            "L_tail_91_114": cell_top95["full_analysis"]["L_tail_91_114"],
            "L_mufassal_short": cell_top95["full_analysis"]["L_mufassal_short"],
            "Block_chi2": cell_top95["block_chi2"],
            "pass_strict_4of4": cell_top95["pass_strict_4of4"],
        },
        "top100_parent_metrics": {
            "L_path": cell_top100["full_analysis"]["L_path"],
            "L_tail_91_114": cell_top100["full_analysis"]["L_tail_91_114"],
            "L_mufassal_short": cell_top100["full_analysis"]["L_mufassal_short"],
            "Block_chi2": cell_top100["block_chi2"],
            "pass_strict_4of4": cell_top100["pass_strict_4of4"],
        },
        "positive_control_from_h2361f": data_f["positive_control_k0"],
        "decisive_tranche_verified_from_h2361d": {
            "k95_minus_k100_set_match": True,
            "k95_hinge_count": len(top95_hinges),
            "k100_hinge_count": len(top100_hinges),
            "exact_tranche_1indexed": [list(pair) for pair in EXACT_DECISIVE_TRANCHE_1INDEXED],
            "core_1indexed": [list(pair) for pair in CORE_TRANCHE_1INDEXED],
            "overlap_pair_1indexed": [list(pair) for pair in OVERLAP_PAIR_1INDEXED],
            "edge_ranks": decisive_tranche_edge_ranks,
        },
    }


def analyze_cell(cell_run: dict, empirical: dict, rand_results: list[dict], added_edges: list[tuple[int, int]]) -> dict:
    sim_results = cell_run["sim_results"]
    full_analysis = {}
    for obs_name in [
        "L_path",
        "W_wrap",
        "L_tiwal",
        "L_hawamim",
        "L_mufassal_short",
        "L_tail_91_114",
    ]:
        full_analysis[obs_name] = family.observable_analysis(
            empirical[obs_name],
            [row[obs_name] for row in sim_results],
            [row[obs_name] for row in rand_results],
        )

    block_stat = family.block_chi2(empirical, sim_results, rand_results)
    l_path_inside = full_analysis["L_path"]["sim_inside_95ci"]
    l_tail_inside = full_analysis["L_tail_91_114"]["sim_inside_95ci"]
    l_muf_inside = full_analysis["L_mufassal_short"]["sim_inside_95ci"]
    block_inside = block_stat["sim_inside_95ci"]
    w_wrap_inside = full_analysis["W_wrap"]["sim_inside_95ci"]

    primary_direct_repair_pass = bool(
        l_path_inside and l_tail_inside and l_muf_inside and block_inside
    )
    strict_4of4_pass = bool(l_path_inside and w_wrap_inside and block_inside and l_tail_inside)

    if strict_4of4_pass and primary_direct_repair_pass:
        verdict = "DIRECT-TRANCHE-STRICT-PASS"
    elif primary_direct_repair_pass:
        verdict = "DIRECT-TRANCHE-PRIMARY-PASS"
    elif l_muf_inside and block_inside and (not l_path_inside or not l_tail_inside):
        verdict = "LOCAL-CLOSED-GLOBAL-FAIL"
    elif (l_path_inside or l_tail_inside) and not (l_muf_inside and block_inside):
        verdict = "GLOBAL-PARTIAL-LOCAL-FAIL"
    else:
        verdict = "NO-REPAIR"

    primary_passes = sum([l_path_inside, l_tail_inside, l_muf_inside, block_inside])
    family_passes = sum([l_path_inside, w_wrap_inside, block_inside, l_tail_inside])

    return {
        "added_edges_1indexed": [list(pair) for pair in added_edges],
        "added_edge_count": len(added_edges),
        "full_analysis": full_analysis,
        "block_chi2": block_stat,
        "l_path_gap_vs_sim_mean": empirical["L_path"] - full_analysis["L_path"]["sim_mean"],
        "l_tail_gap_vs_sim_mean": empirical["L_tail_91_114"] - full_analysis["L_tail_91_114"]["sim_mean"],
        "mufassal_gap_vs_sim_mean": empirical["L_mufassal_short"]
        - full_analysis["L_mufassal_short"]["sim_mean"],
        "primary_direct_repair_pass": primary_direct_repair_pass,
        "strict_4of4_pass": strict_4of4_pass,
        "primary_passes": primary_passes,
        "family_passes": family_passes,
        "cell_verdict": verdict,
        "sim_summaries": {
            key: family.summarize_distribution([row[key] for row in sim_results])
            for key in [
                "L_path",
                "W_wrap",
                "L_tiwal",
                "L_hawamim",
                "L_mufassal_short",
                "L_tail_91_114",
            ]
        },
        "sa_summary": cell_run["sa_summary"],
        "valid_pairs_count": cell_run["valid_pairs_count"],
        "sim_samples": cell_run["sim_results"][:25],
    }


def main() -> None:
    family.SEED = SEED
    family.N_SIM = N_SIM
    family.N_RANDOM = N_RANDOM

    print("=" * 78)
    print("H-NEW-236.1g - Direct isolated-tranche test")
    print("=" * 78)
    print(f"Seed={SEED}; N_SIM={N_SIM}; N_RANDOM={N_RANDOM}; SA_ITERS={SA_ITERS}")

    dmat = family.load_d_matrix()
    prereg_hash = prereg_sha256()
    parents = load_parent_context(dmat)

    print(f"Pre-reg SHA-256: {prereg_hash}")
    print("Locked decisive tranche:")
    for edge in EXACT_DECISIVE_TRANCHE_1INDEXED:
        print(f"  Q {edge[0]}->{edge[1]}")

    empirical_tour = list(range(114))
    empirical = family.compute_observables(empirical_tour, dmat)
    print("\nEmpirical observables:")
    for key, value in empirical.items():
        print(f"  {key:22s} = {value:.6f}")

    print("\nRunning shared random null...")
    rand_results = []
    for idx in range(N_RANDOM):
        rand_results.append(family.simulate_random(idx, dmat))
        if (idx + 1) % 250 == 0:
            print(f"  random {idx + 1}/{N_RANDOM}")

    base_map = {
        CELL_A_NAME: parents["cell_a_hinges_1indexed"],
        TOP50_KEY: parents["top50_hinges_1indexed"],
    }

    cell_outputs = {}
    for cell_name, design_label, base_name, added_edges, seed_offset in CELL_SPECS:
        hinges = dedup_hinges(base_map[base_name] + added_edges)
        print(
            f"\n-- Running {cell_name} "
            f"(base={base_name}; added={added_edges}; |hinges|={len(hinges)})..."
        )
        cell_run = family.run_cell(
            cell_name,
            seed_offset=seed_offset,
            hinges_1indexed=hinges,
            dmat=dmat,
        )
        analysis = analyze_cell(cell_run, empirical, rand_results, added_edges)
        cell_outputs[cell_name] = {
            "design_label": design_label,
            "base_name": base_name,
            "hinges_1indexed": cell_run["hinges_1indexed"],
            "within_hinges_1indexed": cell_run["within_hinges_1indexed"],
            "cross_hinges_1indexed": cell_run["cross_hinges_1indexed"],
            **analysis,
        }
        fa = analysis["full_analysis"]
        print(
            f"   verdict={analysis['cell_verdict']:31s} "
            f"path_in={fa['L_path']['sim_inside_95ci']} "
            f"tail_in={fa['L_tail_91_114']['sim_inside_95ci']} "
            f"muf_in={fa['L_mufassal_short']['sim_inside_95ci']} "
            f"block_in={analysis['block_chi2']['sim_inside_95ci']} "
            f"wrap_in={fa['W_wrap']['sim_inside_95ci']}"
        )

    positive_control = family.positive_control_check(
        cell_outputs["mw5_positive_control_cell_a_base"],
        parents["cell_a_parent_metrics"],
    )
    print(
        "\nPositive control cell_a_base: "
        f"{'PASS' if positive_control['positive_control_pass'] else 'FAIL'} "
        f"(same_signature={positive_control['same_signature_pass']}; "
        f"drift_pass={positive_control['drift_pass']})"
    )

    main_cells = [
        "cell_a_base_plus_exact_tranche",
        "cell_b_base_plus_core_only",
        "cell_c_base_plus_overlap_pair_only",
        "cell_d_top50_plus_exact_tranche",
    ]
    primary_repair_cells = [
        name for name in main_cells if cell_outputs[name]["primary_direct_repair_pass"]
    ]
    strict_4of4_cells = [
        name for name in main_cells if cell_outputs[name]["strict_4of4_pass"]
    ]

    best_local_closed_cell = None
    best_local_closed_score = None
    for name in main_cells:
        cell = cell_outputs[name]
        if not (
            cell["full_analysis"]["L_mufassal_short"]["sim_inside_95ci"]
            and cell["block_chi2"]["sim_inside_95ci"]
        ):
            continue
        score = abs(cell["l_path_gap_vs_sim_mean"]) + abs(cell["l_tail_gap_vs_sim_mean"])
        if best_local_closed_score is None or score < best_local_closed_score:
            best_local_closed_score = score
            best_local_closed_cell = name

    if not positive_control["positive_control_pass"]:
        overall_verdict = "INSTRUMENT-FAIL-POSITIVE-CONTROL"
        interpretation = "no evidential read; base cell did not reproduce H-NEW-236.1c Cell A"
    elif primary_repair_cells:
        overall_verdict = "DIRECT-ISOLATED-TRANCHE-REPAIR-CONFIRMED"
        interpretation = (
            "at least one isolated direct tranche design repairs both global observables "
            "without reopening the local terminal block"
        )
    else:
        overall_verdict = "NO-DIRECT-ISOLATED-TRANCHE-REPAIR"
        interpretation = (
            "the decisive H-NEW-236.1d tranche and its locked subcomponents do not repair "
            "the H-NEW-236.1c overcorrection in the hard-adjacency forms tested here"
        )

    print(f"\nPrimary repair cells: {primary_repair_cells}")
    print(f"Strict 4/4 cells:    {strict_4of4_cells}")
    print(f"Best local-closed:   {best_local_closed_cell}")
    print(f"Overall verdict:     {overall_verdict}")

    output = {
        "finding_id": "h-new-236-1g",
        "title": "Direct isolated-tranche test after H-NEW-236.1d / H-NEW-236.1f",
        "date": "2026-04-18",
        "pre_reg_sha256": prereg_hash,
        "parents": ["h-new-236-1d", "h-new-236-1f"],
        "grandparent": "h-new-236-1c / h-new-236-1a -> h-new-236-1 -> h-new-236 -> cross-finding-020",
        "seed": SEED,
        "n_sim": N_SIM,
        "n_random": N_RANDOM,
        "sa_iters": SA_ITERS,
        "bonferroni_k": 4,
        "alpha_bon": 0.05 / 4.0,
        "rules_tuple": (
            "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, "
            "QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, "
            "stochastic 2-opt with classical-block + Q1-lock + length-stratification "
            "+ M2-muq constraints + direct isolated tranche tests on H-NEW-236.1c Cell A "
            "or H-NEW-236.1a top-50 base, seed 20260424)"
        ),
        "empirical": empirical,
        "exact_decisive_tranche_1indexed": [list(pair) for pair in EXACT_DECISIVE_TRANCHE_1INDEXED],
        "core_tranche_1indexed": [list(pair) for pair in CORE_TRANCHE_1INDEXED],
        "overlap_pair_1indexed": [list(pair) for pair in OVERLAP_PAIR_1INDEXED],
        "parent_context": parents,
        "positive_control_cell_a_base": positive_control,
        "random_baseline_summaries": {
            key: family.summarize_distribution([row[key] for row in rand_results])
            for key in [
                "L_path",
                "W_wrap",
                "L_tiwal",
                "L_hawamim",
                "L_mufassal_short",
                "L_tail_91_114",
            ]
        },
        "cells": cell_outputs,
        "primary_repair_cells": primary_repair_cells,
        "strict_4of4_cells": strict_4of4_cells,
        "best_local_closed_cell": best_local_closed_cell,
        "best_local_closed_score_abs_path_plus_tail_gap": best_local_closed_score,
        "overall_verdict": overall_verdict,
        "interpretation": interpretation,
    }

    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
