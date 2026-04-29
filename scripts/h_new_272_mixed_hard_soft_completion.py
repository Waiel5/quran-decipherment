#!/usr/bin/env python3
"""H-NEW-272 - Mixed hard-soft completion on the OQ-15 parsimony frontier.

Pre-reg:
  findings/phase-b-hypotheses/h-new-272-mixed-hard-soft-completion-prereg.md

Parents:
  - H-NEW-236.1h: lambda=0.07 soft-only primary pass, strict tail miss
  - H-NEW-236.1g: exact decisive tranche and overlap pair isolated in hard-only form

Design:
  Keep the H-NEW-236.1h soft sweet spot locked at lambda=0.07 and test only
  two hard complements: the exact 95->100 decisive tranche and the smallest
  overlap subset extracted in H-NEW-236.1g.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import h_new_236_1e_soft_terminal_penalties as family

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG = (
    PROJECT_ROOT
    / "findings/phase-b-hypotheses/h-new-272-mixed-hard-soft-completion-prereg.md"
)
H2361H_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1h.json"
H2361G_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1g.json"
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-272.json"

FINDING_ID = "h-new-272"
DATE = "2026-04-18"
LAMBDA_FIXED = 0.07
PARENT_LAMBDA07_CELL = "cell_b_lambda_0p07"
POSITIVE_CONTROL_NAME = "mw5_positive_control_lambda0p07_soft_only"

EXACT_DECISIVE_TRANCHE_1INDEXED = [
    (92, 93),
    (99, 100),
    (100, 101),
    (101, 102),
    (109, 110),
]
OVERLAP_PAIR_1INDEXED = [
    (92, 93),
    (109, 110),
]

CELL_SPECS = [
    (POSITIVE_CONTROL_NAME, "soft_only_parent_reproduction", [], 70_000),
    (
        "cell_a_lambda0p07_plus_exact_tranche",
        "top50_soft0p07_plus_exact_95_100_tranche",
        EXACT_DECISIVE_TRANCHE_1INDEXED,
        170_000,
    ),
    (
        "cell_b_lambda0p07_plus_overlap_pair",
        "top50_soft0p07_plus_overlap_pair",
        OVERLAP_PAIR_1INDEXED,
        270_000,
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
    with H2361H_JSON.open() as f:
        data_h = json.load(f)
    with H2361G_JSON.open() as f:
        data_g = json.load(f)

    parent_lambda07 = data_h["cells"][PARENT_LAMBDA07_CELL]
    if parent_lambda07["cell_verdict"] != "SOFT-CLOSES-PRIMARY":
        raise AssertionError("Parent lambda=0.07 cell drifted away from SOFT-CLOSES-PRIMARY")

    exact_from_parent = [tuple(pair) for pair in data_g["exact_decisive_tranche_1indexed"]]
    overlap_from_parent = [tuple(pair) for pair in data_g["overlap_pair_1indexed"]]
    if exact_from_parent != EXACT_DECISIVE_TRANCHE_1INDEXED:
        raise AssertionError("Exact decisive tranche drift vs H-NEW-236.1g")
    if overlap_from_parent != OVERLAP_PAIR_1INDEXED:
        raise AssertionError("Overlap pair drift vs H-NEW-236.1g")

    baseline = family.load_h2361a_top50_baseline()
    rank_map = {
        (row["a"], row["b"]): row["rank"] for row in family.canonical_edge_ranking(dmat)
    }

    def edge_meta(edges: list[tuple[int, int]]) -> list[dict]:
        return [
            {
                "edge_1indexed": [a, b],
                "global_rank": rank_map[(a, b)],
                "distance": float(dmat[a - 1][b - 1]),
                "overlaps_soft_preference_family": (a, b) in family.PREFERENCE_WEIGHTS_1INDEXED,
                "soft_weight_if_any": family.PREFERENCE_WEIGHTS_1INDEXED.get((a, b), 0),
            }
            for a, b in edges
        ]

    return {
        "baseline_top50_hinges_1indexed": baseline["hinges_1indexed"],
        "parent_lambda0p07_cell_name": PARENT_LAMBDA07_CELL,
        "parent_lambda0p07": {
            "cell_verdict": parent_lambda07["cell_verdict"],
            "primary_pass": parent_lambda07["primary_pass"],
            "full_four_pass": parent_lambda07["full_four_pass"],
            "sim_passes": parent_lambda07["sim_passes"],
            "full_analysis": {
                key: parent_lambda07["full_analysis"][key]
                for key in ["L_path", "W_wrap", "L_mufassal_short", "L_tail_91_114"]
            },
            "block_chi2": parent_lambda07["block_chi2"],
            "preference_summary": parent_lambda07["preference_summary"],
        },
        "exact_decisive_tranche_verified": {
            "edges_1indexed": [list(pair) for pair in EXACT_DECISIVE_TRANCHE_1INDEXED],
            "edge_meta": edge_meta(EXACT_DECISIVE_TRANCHE_1INDEXED),
        },
        "overlap_pair_verified": {
            "edges_1indexed": [list(pair) for pair in OVERLAP_PAIR_1INDEXED],
            "edge_meta": edge_meta(OVERLAP_PAIR_1INDEXED),
        },
    }


def positive_control_check(control: dict, parent: dict) -> dict:
    obs_keys = ["L_path", "W_wrap", "L_mufassal_short", "L_tail_91_114"]
    drifts = {
        key: (
            control["full_analysis"][key]["sim_mean"]
            - parent["full_analysis"][key]["sim_mean"]
        )
        for key in obs_keys
    }
    max_abs_drift = max(abs(v) for v in drifts.values())
    verdict_ok = control["cell_verdict"] == parent["cell_verdict"]
    drift_ok = max_abs_drift <= 1e-9
    return {
        "parent_cell_name": PARENT_LAMBDA07_CELL,
        "control_cell_name": POSITIVE_CONTROL_NAME,
        "parent_verdict": parent["cell_verdict"],
        "control_verdict": control["cell_verdict"],
        "verdict_match": verdict_ok,
        "sim_mean_drifts": drifts,
        "max_abs_sim_mean_drift": max_abs_drift,
        "positive_control_pass": bool(verdict_ok and drift_ok),
    }


def classify_mixed_verdict(analysis: dict) -> str:
    if analysis["full_four_pass"]:
        return "MIXED-COMPLETES-STRICT"
    if analysis["primary_pass"]:
        return "MIXED-PRESERVES-PRIMARY-ONLY"
    if analysis["mufassal_inside_sim_95ci"] and not analysis["l_path_inside_sim_95ci"]:
        return "MIXED-PARSIMONY-CONFLICT"
    if analysis["l_path_inside_sim_95ci"] and not analysis["mufassal_inside_sim_95ci"]:
        return "MIXED-LOCAL-FAIL"
    return "MIXED-BROKEN"


def main() -> None:
    print("=" * 78)
    print("H-NEW-272 - Mixed hard-soft completion on the OQ-15 parsimony frontier")
    print("=" * 78)
    print(
        f"Seed={family.SEED}; N_SIM={family.N_SIM}; "
        f"N_RANDOM={family.N_RANDOM}; SA_ITERS={family.SA_ITERS}"
    )
    print(f"Fixed lambda={LAMBDA_FIXED:.2f}")

    dmat = family.load_d_matrix()
    baseline = family.load_h2361a_top50_baseline()
    parents = load_parent_context(dmat)
    prereg_hash = prereg_sha256()

    print(f"Pre-reg SHA-256: {prereg_hash}")
    print(
        "Preference weights: "
        f"{len(family.RHYME_PAIRS_1INDEXED)} rhyme pairs x1 + "
        f"{len(family.LITURGICAL_PAIRS_1INDEXED)} liturgical pairs x2 "
        f"= total weight {family.PREFERENCE_TOTAL_WEIGHT}"
    )
    family.validate_soft_delta(family.PREFERENCE_WEIGHTS_0INDEXED)
    print("Soft-penalty delta check: OK")

    empirical_tour = list(range(114))
    empirical = family.compute_observables(empirical_tour, dmat)
    empirical.update(family.preference_metrics(empirical_tour))
    print("\nEmpirical observables:")
    for key in [
        "L_path",
        "W_wrap",
        "L_mufassal_short",
        "L_tail_91_114",
        "pref_weighted_satisfied",
        "pref_weighted_satisfied_pct",
    ]:
        print(f"  {key:26s} = {empirical[key]:.6f}")

    print("\nRunning shared random null...")
    rand_results = []
    for idx in range(family.N_RANDOM):
        rand_results.append(family.simulate_random(idx, dmat))
        if (idx + 1) % 250 == 0:
            print(f"  random {idx + 1}/{family.N_RANDOM}")

    base_hinges = [tuple(pair) for pair in baseline["hinges_1indexed"]]
    parent_lambda07 = parents["parent_lambda0p07"]
    cell_outputs = {}

    for cell_name, design_label, added_edges, seed_offset in CELL_SPECS:
        hinges = dedup_hinges(base_hinges + added_edges)
        overlap_with_soft = [
            list(pair) for pair in added_edges if pair in family.PREFERENCE_WEIGHTS_1INDEXED
        ]
        print(
            f"\n-- Running {cell_name} "
            f"(added={added_edges}; overlap_soft={overlap_with_soft}; |hinges|={len(hinges)})..."
        )
        cell_run = family.run_cell(
            cell_name,
            seed_offset=seed_offset,
            hinges_1indexed=hinges,
            dmat=dmat,
            lambda_penalty=LAMBDA_FIXED,
        )
        analysis = family.analyze_cell(cell_run, empirical, rand_results, baseline)
        mixed_verdict = classify_mixed_verdict(analysis)
        cell_outputs[cell_name] = {
            "design_label": design_label,
            "seed_offset": seed_offset,
            "lambda_penalty": LAMBDA_FIXED,
            "added_hard_edges_1indexed": [list(pair) for pair in added_edges],
            "added_hard_edge_count": len(added_edges),
            "hard_edges_overlapping_soft_family_1indexed": overlap_with_soft,
            "hinges_1indexed": hinges,
            "within_hinges_1indexed": cell_run["within_hinges_1indexed"],
            "cross_hinges_1indexed": cell_run["cross_hinges_1indexed"],
            "mixed_verdict": mixed_verdict,
            "drift_vs_parent_lambda0p07": {
                "L_path_sim_mean": (
                    analysis["full_analysis"]["L_path"]["sim_mean"]
                    - parent_lambda07["full_analysis"]["L_path"]["sim_mean"]
                ),
                "W_wrap_sim_mean": (
                    analysis["full_analysis"]["W_wrap"]["sim_mean"]
                    - parent_lambda07["full_analysis"]["W_wrap"]["sim_mean"]
                ),
                "L_mufassal_short_sim_mean": (
                    analysis["full_analysis"]["L_mufassal_short"]["sim_mean"]
                    - parent_lambda07["full_analysis"]["L_mufassal_short"]["sim_mean"]
                ),
                "L_tail_91_114_sim_mean": (
                    analysis["full_analysis"]["L_tail_91_114"]["sim_mean"]
                    - parent_lambda07["full_analysis"]["L_tail_91_114"]["sim_mean"]
                ),
                "weighted_pref_satisfied_mean": (
                    analysis["preference_summary"]["weighted_satisfied_mean"]
                    - parent_lambda07["preference_summary"]["weighted_satisfied_mean"]
                ),
            },
            **analysis,
        }
        fa = analysis["full_analysis"]
        print(
            "   "
            f"mixed={mixed_verdict:30s} "
            f"path_in={fa['L_path']['sim_inside_95ci']} "
            f"muf_in={fa['L_mufassal_short']['sim_inside_95ci']} "
            f"tail_in={fa['L_tail_91_114']['sim_inside_95ci']} "
            f"wrap_in={fa['W_wrap']['sim_inside_95ci']} "
            f"block_in={analysis['block_chi2']['sim_inside_95ci']}"
        )

    positive_control = positive_control_check(
        cell_outputs[POSITIVE_CONTROL_NAME],
        parent_lambda07,
    )
    print(
        "\nPositive control lambda=0.07: "
        f"{'PASS' if positive_control['positive_control_pass'] else 'FAIL'} "
        f"(max_abs_sim_mean_drift={positive_control['max_abs_sim_mean_drift']:.12f})"
    )

    inferential_cells = [
        "cell_a_lambda0p07_plus_exact_tranche",
        "cell_b_lambda0p07_plus_overlap_pair",
    ]
    strict_4of4_cells = [
        name for name in inferential_cells if cell_outputs[name]["full_four_pass"]
    ]
    primary_only_cells = [
        name
        for name in inferential_cells
        if cell_outputs[name]["primary_pass"] and not cell_outputs[name]["full_four_pass"]
    ]

    if not positive_control["positive_control_pass"]:
        overall_verdict = "INSTRUMENT-BROKEN"
        interpretation = (
            "the mixed-code positive control did not reproduce the parent "
            "lambda=0.07 sweet-spot cell"
        )
    elif strict_4of4_cells:
        overall_verdict = "MIXED-HARD-SOFT-COMPLETION-CONFIRMED"
        interpretation = (
            "at least one locked hard complement converts the real lambda=0.07 "
            "soft sweet spot into strict completion"
        )
    elif primary_only_cells:
        overall_verdict = "MIXED-HARD-SOFT-COMPLETION-NOT-ENOUGH"
        interpretation = (
            "the tested hard complements preserve only primary closure and do not "
            "complete the tail residual"
        )
    else:
        overall_verdict = "MIXED-HARD-SOFT-COMPLETION-FAILS"
        interpretation = (
            "the tested hard complements do not complete the soft sweet spot and "
            "do not preserve the parent primary pass"
        )

    print(f"Strict 4/4 cells: {strict_4of4_cells}")
    print(f"Primary-only cells: {primary_only_cells}")
    print(f"Overall verdict: {overall_verdict}")

    output = {
        "finding_id": FINDING_ID,
        "title": "Mixed hard-soft completion at the OQ-15 parsimony frontier",
        "date": DATE,
        "pre_reg_sha256": prereg_hash,
        "parents": ["h-new-236-1h", "h-new-236-1g"],
        "grandparent": (
            "h-new-236-1e / h-new-236-1d -> h-new-236-1a -> "
            "h-new-236-1 -> h-new-236 -> cross-finding-020"
        ),
        "seed": family.SEED,
        "n_sim": family.N_SIM,
        "n_random": family.N_RANDOM,
        "sa_iters": family.SA_ITERS,
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "rules_tuple": (
            "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, "
            "QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, "
            "stochastic 2-opt with classical-block + Q1-lock + length-stratification "
            "+ M2-muq + TOP-50-HINGE-BASELINE + SOFT-TERMINAL-PREFERENCE-PENALTY "
            "lambda=0.07 + LOCKED-HARD-COMPLEMENT, seed 20260421)"
        ),
        "fixed_lambda_penalty": LAMBDA_FIXED,
        "soft_preference_family": {
            "rhyme_pairs_1indexed": family.RHYME_PAIRS_1INDEXED,
            "liturgical_pairs_1indexed": family.LITURGICAL_PAIRS_1INDEXED,
            "pair_weights_1indexed": {
                f"{a}-{b}": w
                for (a, b), w in family.PREFERENCE_WEIGHTS_1INDEXED.items()
            },
            "total_weight": family.PREFERENCE_TOTAL_WEIGHT,
        },
        "empirical": empirical,
        "parent_context": parents,
        "positive_control_lambda0p07": positive_control,
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
        "strict_4of4_cells": strict_4of4_cells,
        "primary_only_cells": primary_only_cells,
        "overall_verdict": overall_verdict,
        "interpretation": interpretation,
    }

    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
