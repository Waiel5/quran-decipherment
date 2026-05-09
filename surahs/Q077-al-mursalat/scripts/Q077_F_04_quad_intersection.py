#!/usr/bin/env python3
"""Q077-F-04 — Q 77 quadruple-cluster-intersection corpus-uniqueness.

Pre-reg: surahs/Q077-al-mursalat/preregs/Q077-F-04-quad-cluster-intersection-prereg.md
SHA256: 76565f698cb2703cbc153c66fa20e20ab212405429b0186ab0bab836ce824f91

Cell A: |O ∩ A ∩ E ∩ R| == 1 AND Q 77 ∈ ∩₄.
Cell B: |O ∩ A ∩ E| == 2.
Cell C: Monte Carlo perm-null with cluster cardinalities (15, 10, 14, 5).
"""

import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q077-al-mursalat/preregs/Q077-F-04-quad-cluster-intersection-prereg.md"
EXPECTED_SHA = "76565f698cb2703cbc153c66fa20e20ab212405429b0186ab0bab836ce824f91"
OUT = ROOT / "surahs/Q077-al-mursalat/csv/Q077-F-04.json"
SEED = 20260509
N_PERM = 10_000

# Locked cluster definitions (from MASTER-FINDINGS-LEDGER §10.34, §10.35, §10.38, §10.40)
OATH = {37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}  # H-NEW-1070
ADRAKA = {69, 74, 77, 82, 83, 86, 90, 97, 101, 104}  # H-NEW-1190
ESCHAT = {56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104}  # H-NEW-1200
REFRAIN = {26, 37, 54, 55, 77}  # H-NEW-1230


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:12]}…")


def main() -> None:
    verify_prereg()

    out = {
        "id": "Q077-F-04",
        "title": "Q 77 quadruple-cluster-intersection corpus-uniqueness",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "rules_tuple": "(cluster-membership-set-theoretic, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
    }

    # Compute all set intersections
    quad_intersection = OATH & ADRAKA & ESCHAT & REFRAIN
    triple_OAE = OATH & ADRAKA & ESCHAT
    triple_OAR = OATH & ADRAKA & REFRAIN
    triple_OER = OATH & ESCHAT & REFRAIN
    triple_AER = ADRAKA & ESCHAT & REFRAIN

    # Cell A: 4-way intersection
    cell_A_size = len(quad_intersection)
    cell_A_q77_in = 77 in quad_intersection
    cell_A_pass = cell_A_size == 1 and cell_A_q77_in

    # Cell B: O ∩ A ∩ E intersection
    cell_B_pass = triple_OAE == {77, 86}

    out["intersections"] = {
        "quad_OAER": sorted(quad_intersection),
        "triple_OAE": sorted(triple_OAE),
        "triple_OAR": sorted(triple_OAR),
        "triple_OER": sorted(triple_OER),
        "triple_AER": sorted(triple_AER),
        "pair_OA": sorted(OATH & ADRAKA),
        "pair_OE": sorted(OATH & ESCHAT),
        "pair_OR": sorted(OATH & REFRAIN),
        "pair_AE": sorted(ADRAKA & ESCHAT),
        "pair_AR": sorted(ADRAKA & REFRAIN),
        "pair_ER": sorted(ESCHAT & REFRAIN),
    }

    out["cell_A"] = {
        "target": "|O ∩ A ∩ E ∩ R| == 1 AND Q 77 ∈ ∩₄",
        "obs_size": cell_A_size,
        "q77_in_quad": cell_A_q77_in,
        "obs_set": sorted(quad_intersection),
        "pass": cell_A_pass,
    }

    out["cell_B"] = {
        "target": "|O ∩ A ∩ E| == 2 AND set == {77, 86}",
        "obs_set": sorted(triple_OAE),
        "obs_size": len(triple_OAE),
        "pass": cell_B_pass,
    }

    # Cell C: Monte Carlo null
    rng = random.Random(SEED)
    sizes = [15, 10, 14, 5]  # |O|, |A|, |E|, |R|
    pop = list(range(1, 115))

    n_perm_with_quad_hit = 0
    quad_hit_counts: list[int] = []
    for _ in range(N_PERM):
        sets = [set(rng.sample(pop, k)) for k in sizes]
        intersection = sets[0] & sets[1] & sets[2] & sets[3]
        n_intersect = len(intersection)
        quad_hit_counts.append(n_intersect)
        if n_intersect >= 1:
            n_perm_with_quad_hit += 1

    p_perm = n_perm_with_quad_hit / N_PERM
    cell_C_pass = p_perm <= 0.05

    out["cell_C"] = {
        "target": "p_perm(any-surah-in-4-way-random-intersect) ≤ 0.05",
        "n_perm": N_PERM,
        "cluster_sizes": sizes,
        "n_perm_with_quad_hit": n_perm_with_quad_hit,
        "p_perm_one_tailed": p_perm,
        "perm_null_mean_intersect_size": sum(quad_hit_counts) / N_PERM,
        "max_intersect_size_observed_in_perm": max(quad_hit_counts),
        "pass": cell_C_pass,
    }

    # Combined verdict
    n_pass = sum([cell_A_pass, cell_B_pass, cell_C_pass])
    if n_pass == 3:
        verdict = "PASS-DIRECTED FULL"
    elif n_pass == 2:
        verdict = "PASS-DIRECTED PARTIAL (2/3)"
    elif n_pass == 1:
        verdict = "PARTIAL (1/3)"
    else:
        verdict = "NULL"

    out["verdict_summary"] = {
        "n_cells_pass": n_pass,
        "verdict": verdict,
        "cells": {
            "A_quad_intersect_unique": cell_A_pass,
            "B_triple_OAE_77_86": cell_B_pass,
            "C_perm_null": cell_C_pass,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nVerdict: {verdict}")
    print(f"Cell A (4-way intersect == {{77}}): {sorted(quad_intersection)} pass={cell_A_pass}")
    print(f"Cell B (3-way O∩A∩E == {{77, 86}}): {sorted(triple_OAE)} pass={cell_B_pass}")
    print(f"Cell C (perm null p): {p_perm:.5f}, pass={cell_C_pass}")
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
