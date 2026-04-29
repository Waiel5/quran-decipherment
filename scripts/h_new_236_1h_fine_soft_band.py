#!/usr/bin/env python3
"""H-NEW-236.1h - Fine soft interpolation inside the H-NEW-236.1e near-miss band.

This runner intentionally reuses the exact H-NEW-236.1e soft-penalty
implementation and simulator conventions. The only experimental change is a
finer locked lambda grid strictly inside the H-NEW-236.1e gap between 0.05 and
0.10.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PARENT_SCRIPT = PROJECT_ROOT / "scripts/h_new_236_1e_soft_terminal_penalties.py"
PREREG = (
    PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-236-1h-fine-soft-band-prereg.md"
)
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1h.json"

LAMBDA_GRID = [
    ("cell_a_lambda_0p06", 60_000, 0.06),
    ("cell_b_lambda_0p07", 70_000, 0.07),
    ("cell_c_lambda_0p08", 80_000, 0.08),
    ("cell_d_lambda_0p09", 90_000, 0.09),
]


def load_parent_module():
    spec = importlib.util.spec_from_file_location("h2361e_soft_module", PARENT_SCRIPT)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load parent script from {PARENT_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def prereg_sha256() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def main() -> None:
    parent = load_parent_module()

    print("=" * 78)
    print("H-NEW-236.1h - Fine soft interpolation inside the 236.1e near-miss band")
    print("=" * 78)
    print(
        f"Seed={parent.SEED}; N_SIM={parent.N_SIM}; "
        f"N_RANDOM={parent.N_RANDOM}; SA_ITERS={parent.SA_ITERS}"
    )

    dmat = parent.load_d_matrix()
    baseline = parent.load_h2361a_top50_baseline()
    prereg_hash = prereg_sha256()

    print(f"Pre-reg SHA-256: {prereg_hash}")
    print(
        "Preference weights: "
        f"{len(parent.RHYME_PAIRS_1INDEXED)} rhyme pairs x1 + "
        f"{len(parent.LITURGICAL_PAIRS_1INDEXED)} liturgical pairs x2 "
        f"= total weight {parent.PREFERENCE_TOTAL_WEIGHT}"
    )
    parent.validate_soft_delta(parent.PREFERENCE_WEIGHTS_0INDEXED)
    print("Soft-penalty delta check: OK")

    ranked_edges = parent.canonical_edge_ranking(dmat)
    top50 = [(row["a"], row["b"]) for row in ranked_edges[:50]]
    if top50 != baseline["hinges_1indexed"]:
        raise AssertionError("Top-50 hinge set drift vs H-NEW-236.1a baseline")

    empirical_tour = list(range(114))
    empirical = parent.compute_observables(empirical_tour, dmat)
    empirical.update(parent.preference_metrics(empirical_tour))
    print("\nEmpirical observables:")
    for key in [
        "L_path",
        "W_wrap",
        "L_tiwal",
        "L_hawamim",
        "L_mufassal_short",
        "L_tail_91_114",
        "pref_weighted_satisfied",
        "pref_weighted_satisfied_pct",
    ]:
        print(f"  {key:26s} = {empirical[key]:.6f}")

    print("\nRunning shared random null (MW-5 calibration)...")
    rand_results = []
    for k in range(parent.N_RANDOM):
        rand_results.append(parent.simulate_random(k, dmat))
        if (k + 1) % 250 == 0:
            print(f"  random {k + 1}/{parent.N_RANDOM}")

    cell_specs = [("mw5_positive_control_soft0", 900_000, 0.0)] + LAMBDA_GRID
    cell_outputs = {}
    for cell_name, seed_offset, lambda_penalty in cell_specs:
        print(f"\n-- Running {cell_name} (lambda={lambda_penalty:.3f})...")
        cell_run = parent.run_cell(
            cell_name,
            seed_offset,
            top50,
            dmat,
            lambda_penalty=lambda_penalty,
        )
        analysis = parent.analyze_cell(cell_run, empirical, rand_results, baseline)
        cell_outputs[cell_name] = {
            "lambda_penalty": lambda_penalty,
            "hinges_1indexed": top50,
            "within_hinges_1indexed": cell_run["within_hinges_1indexed"],
            "cross_hinges_1indexed": cell_run["cross_hinges_1indexed"],
            **analysis,
        }
        fa = analysis["full_analysis"]
        print(
            "   "
            f"L_path pct={fa['L_path']['sim_percentile_of_empirical']:6.2f}  "
            f"L_muf pct={fa['L_mufassal_short']['sim_percentile_of_empirical']:6.2f}  "
            f"pref_sat_mean={analysis['preference_summary']['weighted_satisfied_mean']:.2f}/"
            f"{parent.PREFERENCE_TOTAL_WEIGHT}  "
            f"verdict={analysis['cell_verdict']}"
        )

    pc = cell_outputs["mw5_positive_control_soft0"]
    pc_z = pc["block_chi2"]["per_block"]["L_mufassal_short"]["sim_z"]
    parent_z = baseline["mufassal_z"]
    pc_ok = math.isfinite(pc_z) and abs(pc_z - parent_z) <= 2.0

    non_control_cells = [name for name, _, _ in LAMBDA_GRID]
    strict_4of4 = [name for name in non_control_cells if cell_outputs[name]["full_four_pass"]]
    primary_only = [
        name
        for name in non_control_cells
        if cell_outputs[name]["primary_pass"] and not cell_outputs[name]["full_four_pass"]
    ]
    primary_conflict = [
        name
        for name in non_control_cells
        if cell_outputs[name]["cell_verdict"] == "SOFT-PARSIMONY-CONFLICT"
    ]

    if strict_4of4:
        overall_verdict = "FINE SOFT BAND FINDS STRICT CLOSURE"
    elif primary_only:
        overall_verdict = "FINE SOFT BAND FINDS PRIMARY-ONLY CLOSURE"
    elif primary_conflict:
        overall_verdict = "FINE SOFT BAND SHOWS NULL/CONFLICT BOUNDARY ONLY"
    else:
        overall_verdict = "FINE SOFT BAND NULL"

    print(
        f"\nMW-5 positive control: top-50 soft0 mufassal z = {pc_z:+.3f} "
        f"(parent {parent_z:+.3f}; tol |delta|<=2.0 => {'OK' if pc_ok else 'FAIL'})"
    )
    print(f"Strict 4/4 cells: {strict_4of4}")
    print(f"Primary-only cells: {primary_only}")
    print(f"Parsimony-conflict cells: {primary_conflict}")
    print(f"Overall verdict: {overall_verdict}")

    output = {
        "finding_id": "h-new-236-1h",
        "title": "Fine soft interpolation inside the H-NEW-236.1e near-miss band",
        "pre_reg_sha256": prereg_hash,
        "parent": "h-new-236-1e / h-new-236-1d",
        "grandparent": (
            "h-new-236-1b / h-new-236-1c -> h-new-236-1a -> "
            "h-new-236-1 -> h-new-236 -> cross-finding-020"
        ),
        "seed": parent.SEED,
        "n_sim": parent.N_SIM,
        "n_random": parent.N_RANDOM,
        "sa_iters": parent.SA_ITERS,
        "bonferroni_k": len(LAMBDA_GRID),
        "alpha_bon": 0.05 / len(LAMBDA_GRID),
        "rules_tuple": (
            "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, "
            "QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, "
            "stochastic 2-opt with classical-block + Q1-lock + length-stratification "
            "+ M2-muq + TOP-50-HINGE-BASELINE + SOFT-TERMINAL-PREFERENCE-PENALTY, "
            "seed 20260421)"
        ),
        "soft_penalty_spec": {
            "base_family_from": "h-new-236-1e",
            "rhyme_pairs_1indexed": parent.RHYME_PAIRS_1INDEXED,
            "liturgical_pairs_1indexed": parent.LITURGICAL_PAIRS_1INDEXED,
            "pair_weights_1indexed": {
                f"{a}-{b}": w for (a, b), w in parent.PREFERENCE_WEIGHTS_1INDEXED.items()
            },
            "pair_weighting_rule": "rhyme pair = 1, liturgical pair = 2, overlaps additive",
            "total_weight": parent.PREFERENCE_TOTAL_WEIGHT,
            "lambda_grid": [
                {"cell_name": cell_name, "lambda_penalty": lambda_penalty}
                for cell_name, _, lambda_penalty in LAMBDA_GRID
            ],
        },
        "parent_h2361a_top50": baseline,
        "parent_h2361e_band_context": {
            "lambda_0p05_verdict": "SOFT-NULL",
            "lambda_0p05_l_mufassal_short_z": 2.78,
            "lambda_0p10_verdict": "SOFT-PARSIMONY-CONFLICT",
            "lambda_0p10_l_mufassal_short_z": 0.88,
        },
        "mw5_positive_control_pass": pc_ok,
        "mw5_positive_control_mufassal_z": pc_z,
        "empirical": empirical,
        "canonical_edge_ranking_top_60": ranked_edges[:60],
        "random_baseline_summaries": {
            key: parent.summarize_distribution([row[key] for row in rand_results])
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
        "strict_4of4_cells": strict_4of4,
        "primary_only_cells": primary_only,
        "parsimony_conflict_cells": primary_conflict,
        "overall_verdict": overall_verdict,
    }

    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
