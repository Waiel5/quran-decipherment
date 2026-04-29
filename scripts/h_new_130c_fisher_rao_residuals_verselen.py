#!/usr/bin/env python3
"""H-NEW-130c — Fisher-Rao residuals THIRD-FEATURE replication (verse-length histogram).

Third feature-space replication after H-NEW-130 (roots, PASS-DIRECTED→CONFIRMED)
and H-NEW-130b (char-4-grams, REPLICATION-CONFIRMED). B frozen, K_top frozen,
threshold frozen.

Inputs:
- findings/phase-b-hypotheses/csv/h-new-111c.json   (verse-length D-matrix)
- findings/phase-b-hypotheses/csv/h-new-130.json    (root top-15)
- findings/phase-b-hypotheses/csv/h-new-130b.json   (char-4-gram top-15)

Seed: 20260417. Deterministic.
Pre-reg: findings/phase-b-hypotheses/h-new-130c-prereg.md
"""

from __future__ import annotations

import csv
import hashlib
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, "/Users/grey/Downloads/quran/scripts")
from h_new_130_fisher_rao_residuals import (
    build_boundary_set,
    load_verse_counts,
    hypergeom_sf,
    secondary_A,
)

SEED = 20260417
PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111C_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111c.json"
H_NEW_130_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130.json"
H_NEW_130B_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130b.json"
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130c.json"
PREREG_PATH = PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-130c-prereg.md"

K_TOP = 15
N_PERMS = 10_000


def load_d_matrix_vlen() -> dict[tuple[int, int], float]:
    with H_NEW_111C_JSON.open() as f:
        parent = json.load(f)
    flat = parent["D_matrix_upper_triangular"]
    D: dict[tuple[int, int], float] = {}
    for entry in flat:
        i, j, d = int(entry[0]), int(entry[1]), float(entry[2])
        D[(i, j)] = d
        D[(j, i)] = d
    return D


def load_top15(path: Path) -> list[tuple[int, int]]:
    with path.open() as f:
        d = json.load(f)
    return [(row["i"], row["j"]) for row in d["top15_largest_jumps"]]


def main() -> None:
    random.seed(SEED)

    B_dict = build_boundary_set()
    B_pairs = set(B_dict.keys())

    D = load_d_matrix_vlen()
    d_consec = [D[(i, i + 1)] for i in range(1, 114)]
    assert len(d_consec) == 113

    ranked = sorted(range(1, 114), key=lambda i: -d_consec[i - 1])
    top_K_indices = ranked[:K_TOP]
    top_K_pairs = [(i, i + 1) for i in top_K_indices]
    top_K_set = set(top_K_pairs)

    # Primary
    M_intersect_B = top_K_set & B_pairs
    obs_k = len(M_intersect_B)
    N, K_size, n = 113, len(B_pairs), K_TOP
    p_primary = hypergeom_sf(obs_k, N, K_size, n)
    primary_pass = obs_k >= 12

    # Secondary A
    B_indices = {i for (i, _j) in B_pairs}
    sec_A = secondary_A(d_consec, B_indices, N_PERMS)
    sec_A_pass = (sec_A["p_two_sided"] < 0.0167) and (sec_A["T_obs"] > 0)

    # Secondary B: 3-way intersection
    root_top15 = set(load_top15(H_NEW_130_JSON))
    char_top15 = set(load_top15(H_NEW_130B_JSON))
    triple = top_K_set & root_top15 & char_top15
    root_vlen = top_K_set & root_top15
    char_vlen = top_K_set & char_top15
    triple_pass = len(triple) >= 3

    # MW-5 discriminativeness
    verse_counts = load_verse_counts()
    order = sorted(range(1, 115), key=lambda s: (-verse_counts[s], s))
    d_synth = [D[(order[i], order[i + 1])] for i in range(len(order) - 1)]
    synth_ranked = sorted(range(113), key=lambda k: -d_synth[k])[:K_TOP]
    synth_top15_set = set((order[k], order[k + 1]) for k in synth_ranked)
    mw5_pass = synth_top15_set != top_K_set
    synth_hits_B = len(synth_top15_set & B_pairs)

    # Table
    top15_table = []
    for (i, j) in top_K_pairs:
        top15_table.append({
            "i": i, "j": j, "distance": d_consec[i - 1],
            "in_B": (i, j) in B_pairs,
            "B_labels": B_dict.get((i, j), []),
            "in_h130_root_top15": (i, j) in root_top15,
            "in_h130b_char_top15": (i, j) in char_top15,
            "in_all_three": (i, j) in triple,
        })
    top15_table.sort(key=lambda x: -x["distance"])

    # Verdict
    if not mw5_pass:
        verdict = "INSTRUMENT-BROKEN"
    elif obs_k >= 12:
        verdict = "TRIPLE-REPLICATION-CONFIRMED" if (sec_A_pass and triple_pass) else "REPLICATION-CONFIRMED"
    elif obs_k >= 9:
        verdict = "RHYTHM-PARTIAL (9-11 hits; raw-sig, Bonferroni-NS)"
    else:
        verdict = "RHYTHM-AXIS-DIFFERS (primary fails on verse-length feature)"

    output = {
        "finding_id": "h-new-130c",
        "title": "Fisher-Rao residuals THIRD-FEATURE replication on verse-length-histogram D-matrix",
        "pre_reg_path": str(PREREG_PATH),
        "pre_reg_sha256": hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest(),
        "parent_finding_primary": "h-new-130",
        "parent_finding_dmatrix": "h-new-111c",
        "seed": SEED,
        "date": "2026-04-17",
        "rules_tuple": "(no-tashkeel, whitespace-tokenized verse text, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)",
        "bonferroni_k": 3,
        "bonferroni_family": "h-new-130c-residuals-verselen",
        "alpha_bon": 0.0167,
        "boundary_set_size": K_size,
        "consecutive_mushaf_distances_verselen": {
            f"{i}-{i + 1}": d_consec[i - 1] for i in range(1, 114)
        },
        "top15_largest_jumps": top15_table,
        "primary_hypergeometric": {
            "observed_M_intersect_B": obs_k,
            "threshold_pass": 12,
            "null_model": "hypergeometric(N=113, K=54, n=15)",
            "null_expected_overlap": n * K_size / N,
            "p_primary_one_sided_upper": p_primary,
            "alpha_bon": 0.0167,
            "pass_primary": primary_pass,
        },
        "secondary_A_concentration": sec_A | {
            "alpha_bon": 0.0167,
            "pass_secondary_A": sec_A_pass,
        },
        "secondary_B_three_way_intersection": {
            "root_top15": sorted(list(root_top15)),
            "char_top15": sorted(list(char_top15)),
            "vlen_top15": sorted(list(top_K_set)),
            "root_and_vlen": sorted(list(root_vlen)),
            "char_and_vlen": sorted(list(char_vlen)),
            "triple_intersection_universal_hinges": sorted(list(triple)),
            "triple_cardinality": len(triple),
            "threshold_pass": 3,
            "pass_universal_hinges": triple_pass,
        },
        "mw5_discriminativeness": {
            "synthetic_ordering": "descending_verse_count",
            "synth_top15": sorted(list(synth_top15_set)),
            "n_shared_with_vlen_top15": len(synth_top15_set & top_K_set),
            "synth_hits_against_B": synth_hits_B,
            "pass_discriminativeness": mw5_pass,
        },
        "verdict": verdict,
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print("H-NEW-130c — verse-length histogram D-matrix")
    print("=" * 70)
    print(f"Observed |M ∩ B|: {obs_k} of 15")
    print(f"Primary hypergeom p: {p_primary:.5e}")
    print(f"Threshold ≥12 passed: {primary_pass}")
    print()
    print("Top-15 largest-jump pairs (verse-length):")
    for row in top15_table:
        b_mark = "B" if row["in_B"] else "-"
        r_mark = "R" if row["in_h130_root_top15"] else "-"
        c_mark = "C" if row["in_h130b_char_top15"] else "-"
        triple_mark = "★" if row["in_all_three"] else " "
        labels = (" " + ", ".join(row["B_labels"])) if row["B_labels"] else ""
        print(f"  {triple_mark} Q{row['i']:3d} → Q{row['j']:3d}  d={row['distance']:.4f}  [{b_mark}{r_mark}{c_mark}]{labels}")
    print()
    print(f"Secondary A: T = {sec_A['T_obs']:+.5f}, p = {sec_A['p_two_sided']:.5f}")
    print(f"  Sign: {sec_A['sign']}; pass: {sec_A_pass}")
    print()
    print(f"Secondary B (3-way intersection):")
    print(f"  Triple (root ∩ char ∩ vlen): {len(triple)} pairs → {sorted(list(triple))}")
    print(f"  Pass threshold ≥3: {triple_pass}")
    print()
    print(f"MW-5: synth top-15 identical to vlen top-15? {not mw5_pass}; synth hits B: {synth_hits_B}")
    print()
    print(f"VERDICT: {verdict}")
    print(f"Output: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
