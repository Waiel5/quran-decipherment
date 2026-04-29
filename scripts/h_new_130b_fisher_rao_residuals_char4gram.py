#!/usr/bin/env python3
"""H-NEW-130b — Fisher-Rao residuals CROSS-FEATURE replication on char-4-gram D-matrix.

Pure feature-space replication of H-NEW-130. Boundary set B, K_top, threshold,
Bonferroni-family are FROZEN from H-NEW-130.

Inputs:
- findings/phase-b-hypotheses/csv/h-new-111b.json  (char-4-gram D-matrix)
- findings/phase-b-hypotheses/csv/h-new-130.json   (QAC-STEM top-15 for cross-feature overlap)
- data/revelation-order.csv                         (Nöldeke phase + period, unchanged)
- data/hafs-verse-counts.tsv                        (MW-5 control)

Outputs:
- findings/phase-b-hypotheses/csv/h-new-130b.json

Seed: 20260417. Deterministic.
Pre-reg: findings/phase-b-hypotheses/h-new-130b-prereg.md
"""

from __future__ import annotations

import csv
import hashlib
import json
import random
from math import comb
from pathlib import Path

# Reuse H-NEW-130's boundary-set construction by importing its module.
import sys
sys.path.insert(0, "/Users/grey/Downloads/quran/scripts")
from h_new_130_fisher_rao_residuals import (
    build_boundary_set,
    load_verse_counts,
    hypergeom_sf,
    secondary_A,  # reused
)

SEED = 20260417
PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111B_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111b.json"
H_NEW_130_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130.json"
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130b.json"
PREREG_PATH = PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-130b-prereg.md"

K_TOP = 15
N_PERMS = 10_000


def load_d_matrix_char4gram() -> dict[tuple[int, int], float]:
    with H_NEW_111B_JSON.open() as f:
        parent = json.load(f)
    flat = parent["D_matrix_upper_triangular"]
    D: dict[tuple[int, int], float] = {}
    for entry in flat:
        i, j, d = int(entry[0]), int(entry[1]), float(entry[2])
        D[(i, j)] = d
        D[(j, i)] = d
    return D


def load_h130_top15() -> tuple[list[tuple[int, int]], set[tuple[int, int]]]:
    with H_NEW_130_JSON.open() as f:
        h130 = json.load(f)
    top15 = [(row["i"], row["j"]) for row in h130["top15_largest_jumps"]]
    return top15, set(top15)


def perm_null_overlap(d_consec: list[float], B_pairs: set[tuple[int, int]],
                      k_obs: int, K_TOP: int, n_perms: int, seed: int) -> dict:
    """Robustness: 10K random 15-pair selections from the 113 pairs."""
    rng = random.Random(seed + 2)
    all_pairs = [(i, i + 1) for i in range(1, 114)]
    n_ge = 0
    n_eq = 0
    for _ in range(n_perms):
        sample = rng.sample(all_pairs, K_TOP)
        overlap = sum(1 for p in sample if p in B_pairs)
        if overlap >= k_obs:
            n_ge += 1
        if overlap == k_obs:
            n_eq += 1
    return {
        "n_perms": n_perms,
        "n_ge_observed": n_ge,
        "p_permutation_upper": (n_ge + 1) / (n_perms + 1),
        "n_eq_observed": n_eq,
        "note": "Should agree with hypergeometric up to MC noise",
    }


def main() -> None:
    random.seed(SEED)

    # Frozen boundary set
    B_dict = build_boundary_set()
    B_pairs = set(B_dict.keys())

    # char-4-gram D-matrix
    D = load_d_matrix_char4gram()
    d_consec = [D[(i, i + 1)] for i in range(1, 114)]
    assert len(d_consec) == 113

    # Rank pairs
    ranked_by_distance = sorted(range(1, 114), key=lambda i: -d_consec[i - 1])
    top_K_indices = ranked_by_distance[:K_TOP]
    top_K_pairs = [(i, i + 1) for i in top_K_indices]
    top_K_set = set(top_K_pairs)

    # Primary: hypergeometric
    M_intersect_B = top_K_set & B_pairs
    obs_k = len(M_intersect_B)
    N, K_size, n = 113, len(B_pairs), K_TOP
    p_primary_hg = hypergeom_sf(obs_k, N, K_size, n)

    threshold_pass = 12
    primary_pass = obs_k >= threshold_pass

    # Permutation-null robustness (team-lead-requested)
    perm_robustness = perm_null_overlap(d_consec, B_pairs, obs_k, K_TOP, N_PERMS, SEED)

    # Secondary A: B-vs-notB mean-distance concentration
    B_indices = {i for (i, _j) in B_pairs}
    sec_A = secondary_A(d_consec, B_indices, N_PERMS)
    sec_A_pass = (sec_A["p_two_sided"] < 0.0167) and (sec_A["T_obs"] > 0)

    # Secondary B: cross-feature top-15 overlap with H-NEW-130
    h130_top15, h130_top15_set = load_h130_top15()
    cross_overlap_pairs = top_K_set & h130_top15_set
    cross_overlap_k = len(cross_overlap_pairs)
    p_cross_overlap = hypergeom_sf(cross_overlap_k, 113, K_TOP, K_TOP)
    cross_pass = p_cross_overlap < 0.0167  # i.e., overlap >= 5 per pre-reg

    # MW-5 positive control: sort-by-verse-count on char-4-gram D-matrix
    verse_counts = load_verse_counts()
    order = sorted(range(1, 115), key=lambda s: (-verse_counts[s], s))
    d_synth = [D[(order[i], order[i + 1])] for i in range(len(order) - 1)]
    synth_ranked = sorted(range(113), key=lambda k: -d_synth[k])[:K_TOP]
    synth_top15 = [(order[k], order[k + 1]) for k in synth_ranked]
    synth_top15_set = set(synth_top15)
    mw5_pass_discrim = synth_top15_set != top_K_set
    synth_hits_B = len(synth_top15_set & B_pairs)

    # Top-15 table with B labels
    top15_table = []
    for (i, j) in top_K_pairs:
        top15_table.append({
            "i": i,
            "j": j,
            "distance": d_consec[i - 1],
            "in_B": (i, j) in B_pairs,
            "B_labels": B_dict.get((i, j), []),
            "in_h130_top15": (i, j) in h130_top15_set,
        })
    top15_table.sort(key=lambda x: -x["distance"])

    # Verdict
    if not mw5_pass_discrim:
        primary_verdict = "INSTRUMENT-BROKEN (synthetic sort-by-length top-15 == char-4-gram top-15)"
    elif obs_k >= 12:
        primary_verdict = "REPLICATION-CONFIRMED (>= 12 of 15 hit B)"
    elif obs_k >= 9:
        primary_verdict = "REPLICATION-PARTIAL (raw-sig, Bonferroni-NS)"
    else:
        primary_verdict = "REPLICATION-FAILED (< 9 of 15 hit B)"

    # Pre-reg SHA
    pre_reg_sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()

    output = {
        "finding_id": "h-new-130b",
        "title": "Fisher-Rao residuals CROSS-FEATURE replication on char-4-gram D-matrix",
        "pre_reg_path": str(PREREG_PATH),
        "pre_reg_sha256": pre_reg_sha,
        "parent_finding_primary": "h-new-130",
        "parent_finding_dmatrix": "h-new-111b",
        "seed": SEED,
        "date": "2026-04-17",
        "rules_tuple": "(no-tashkeel, char-4-grams with spaces, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)",
        "bonferroni_k": 3,
        "bonferroni_family": "h-new-130b-residuals-char4gram",
        "alpha_bon": 0.0167,
        "boundary_set_size": K_size,
        "boundary_set_fraction_of_113": K_size / 113,
        "consecutive_mushaf_distances_char4gram": {
            f"{i}-{i + 1}": d_consec[i - 1] for i in range(1, 114)
        },
        "top15_largest_jumps": top15_table,
        "primary_hypergeometric": {
            "observed_M_intersect_B": obs_k,
            "threshold_pass": threshold_pass,
            "null_model": "hypergeometric(N=113, K=|B|=54, n=15)",
            "null_expected_overlap": n * K_size / N,
            "p_primary_one_sided_upper": p_primary_hg,
            "alpha_bon": 0.0167,
            "pass_primary": primary_pass,
        },
        "primary_permutation_robustness": perm_robustness,
        "secondary_A_concentration": sec_A | {
            "alpha_bon": 0.0167,
            "pass_secondary_A": sec_A_pass,
        },
        "secondary_B_cross_feature_overlap": {
            "n_shared_top15_with_h130_root": cross_overlap_k,
            "shared_pairs": sorted(list(cross_overlap_pairs)),
            "null_model": "hypergeometric(N=113, K=15, n=15)",
            "null_expected_overlap": K_TOP * K_TOP / 113,
            "p_one_sided_upper": p_cross_overlap,
            "alpha_bon": 0.0167,
            "pass_cross_feature": cross_pass,
        },
        "mw5_discriminativeness": {
            "synthetic_ordering": "descending_verse_count",
            "synth_top15": synth_top15,
            "n_shared_with_char4gram_top15": len(synth_top15_set & top_K_set),
            "synth_hits_against_B": synth_hits_B,
            "pass_discriminativeness": mw5_pass_discrim,
        },
        "verdict_primary": primary_verdict,
        "verdict_overall_replication": (
            "CONFIRMED" if (primary_pass and sec_A_pass and cross_pass and mw5_pass_discrim)
            else ("PASS-PRIMARY-ONLY" if primary_pass and mw5_pass_discrim
                  else primary_verdict)
        ),
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # Console summary
    print("=" * 70)
    print("H-NEW-130b — Fisher-Rao residuals, char-4-gram D-matrix")
    print("=" * 70)
    print(f"|B| = {K_size} of 113 (frozen from H-NEW-130)")
    print(f"Null expected |M ∩ B|: {n * K_size / N:.3f}")
    print(f"Observed |M ∩ B|: {obs_k}")
    print(f"Primary hypergeom p: {p_primary_hg:.5e}")
    print(f"Permutation-robustness p (10K): {perm_robustness['p_permutation_upper']:.5f}")
    print(f"Threshold pass (>=12): {primary_pass}")
    print(f"Primary verdict: {primary_verdict}")
    print()
    print("Top-15 largest-jump pairs (char-4-gram):")
    for row in top15_table:
        b_mark = "B" if row["in_B"] else "-"
        r_mark = "R" if row["in_h130_top15"] else "-"
        labels = (" " + ", ".join(row["B_labels"])) if row["B_labels"] else ""
        print(f"  Q{row['i']:3d} → Q{row['j']:3d}  d={row['distance']:.4f}  [{b_mark}{r_mark}]{labels}")
    print()
    print(f"Secondary A: T = {sec_A['T_obs']:+.5f}, p = {sec_A['p_two_sided']:.5f}")
    print(f"  Sign: {sec_A['sign']}")
    print(f"  Pass: {sec_A_pass}")
    print()
    print(f"Secondary B (cross-feature overlap with H-NEW-130 root top-15):")
    print(f"  Overlap: {cross_overlap_k} of 15")
    print(f"  Hypergeom p: {p_cross_overlap:.5e}")
    print(f"  Pass: {cross_pass}")
    print()
    print(f"MW-5 discriminativeness:")
    print(f"  Synthetic-sort top-15 identical to char-4-gram? {not mw5_pass_discrim}")
    print(f"  Synth top-15 hits B: {synth_hits_B}")
    print(f"  Pass: {mw5_pass_discrim}")
    print()
    print(f"OVERALL REPLICATION: {output['verdict_overall_replication']}")
    print(f"Output JSON: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
