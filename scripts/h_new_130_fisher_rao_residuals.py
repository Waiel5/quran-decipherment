#!/usr/bin/env python3
"""H-NEW-130 — Fisher-Rao mushaf-geodesic RESIDUALS analysis.

Tests whether the top-15 largest Fisher-Rao consecutive-pair distances
in mushaf order concentrate at a pre-committed structural-boundary set B.

Inputs:
- findings/phase-b-hypotheses/csv/h-new-111.json  (parent D-matrix)
- data/revelation-order.csv                        (Nöldeke phase + period)
- data/hafs-verse-counts.tsv                       (verse counts, MW-5 control)

Outputs:
- findings/phase-b-hypotheses/csv/h-new-130.json
- journal/h-new-130-run-1.md  (written separately)

Seed: 20260417. Deterministic.
Pre-reg: findings/phase-b-hypotheses/h-new-130-prereg.md
"""

from __future__ import annotations

import csv
import hashlib
import json
import random
from math import comb
from pathlib import Path

SEED = 20260417
PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
REVELATION_CSV = PROJECT_ROOT / "data/revelation-order.csv"
HAFS_COUNTS_TSV = PROJECT_ROOT / "data/hafs-verse-counts.tsv"
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130.json"
PREREG_PATH = PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-130-prereg.md"

K_TOP = 15
N_PERMS = 10_000


# ---------------------------------------------------------------------------
# Pre-committed boundary set (PURE function of CSV + classical canon)
# ---------------------------------------------------------------------------

MUQ_SET = {
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
    31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68,
}

MUQ_LETTER = {
    2: "ALM", 3: "ALM",
    7: "ALMS",
    10: "ALR", 11: "ALR", 12: "ALR", 14: "ALR", 15: "ALR",
    13: "ALMR",
    19: "KHYAS",
    20: "TH",
    26: "TSM", 27: "TS", 28: "TSM",
    29: "ALM", 30: "ALM", 31: "ALM", 32: "ALM",
    36: "YS",
    38: "S",
    40: "HM", 41: "HM", 42: "HM+ASQ", 43: "HM", 44: "HM", 45: "HM", 46: "HM",
    50: "Q",
    68: "N",
}

LENGTH_BOUNDARIES = {
    7:  "sab_tiwal_end_7_8",
    9:  "sab_tiwal_alt_9_10",
    48: "mufassal_start_48_49",
    49: "mufassal_alt_49_50",
    66: "short_mufassal_boundary_66_67",
    77: "juz_amma_77_78",
    92: "ultra_short_mufassal_92_93",
}


def load_period_phase() -> tuple[dict[int, str], dict[int, str]]:
    phase: dict[int, str] = {}
    period: dict[int, str] = {}
    with REVELATION_CSV.open() as f:
        for row in csv.DictReader(f):
            m = int(row["mushaf_order"])
            phase[m] = row["noldeke_phase"]
            period[m] = row["period"]
    assert len(phase) == 114
    return period, phase


def build_boundary_set() -> dict[tuple[int, int], list[str]]:
    period, phase = load_period_phase()
    B: dict[tuple[int, int], set[str]] = {}

    def add(i: int, label: str) -> None:
        B.setdefault((i, i + 1), set()).add(label)

    for i, lbl in LENGTH_BOUNDARIES.items():
        add(i, lbl)

    for i in range(1, 114):
        if period[i] != period[i + 1]:
            add(i, f"period_{period[i]}_to_{period[i + 1]}")
        if phase[i] != phase[i + 1]:
            add(i, f"phase_{phase[i]}_to_{phase[i + 1]}")
        a, b = (i in MUQ_SET), ((i + 1) in MUQ_SET)
        if a != b:
            add(i, "muq_presence_change")
        if a and b and MUQ_LETTER[i] != MUQ_LETTER[i + 1]:
            add(i, f"muq_letterset_{MUQ_LETTER[i]}_to_{MUQ_LETTER[i + 1]}")

    return {k: sorted(v) for k, v in sorted(B.items())}


# ---------------------------------------------------------------------------
# D-matrix load + consecutive distances
# ---------------------------------------------------------------------------

def load_d_matrix() -> dict[tuple[int, int], float]:
    with H_NEW_111_JSON.open() as f:
        parent = json.load(f)
    flat = parent["D_matrix_upper_triangular"]
    D: dict[tuple[int, int], float] = {}
    for entry in flat:
        i, j, d = int(entry[0]), int(entry[1]), float(entry[2])
        D[(i, j)] = d
        D[(j, i)] = d
    return D


def load_verse_counts() -> dict[int, int]:
    counts: dict[int, int] = {}
    with HAFS_COUNTS_TSV.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) != 2:
                continue
            try:
                s, n = int(parts[0]), int(parts[1])
            except ValueError:
                continue
            counts[s] = n
    return counts


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Primary test: hypergeometric p-value
# ---------------------------------------------------------------------------

def hypergeom_sf(k: int, N: int, K: int, n: int) -> float:
    """P(X >= k) where X ~ Hypergeometric(N, K, n)."""
    total = 0.0
    for x in range(k, n + 1):
        if x > K or n - x > N - K:
            continue
        total += comb(K, x) * comb(N - K, n - x) / comb(N, n)
    return total


# ---------------------------------------------------------------------------
# Secondary A: permutation test on B-vs-notB mean distance
# ---------------------------------------------------------------------------

def secondary_A(d_consec: list[float], B_indices: set[int], n_perms: int) -> dict:
    """
    d_consec[i-1] = distance for pair (i, i+1), i=1..113.
    B_indices = set of i such that (i, i+1) ∈ B.

    T = mean(d on B) − mean(d on notB).
    Null: reshuffle B-label over the 113 pair-slots (preserving |B|).
    """
    pair_count = len(d_consec)
    B_size = len(B_indices)
    assert pair_count == 113
    # Observed T
    B_vals = [d_consec[i - 1] for i in B_indices]
    notB_vals = [d for idx, d in enumerate(d_consec, start=1) if idx not in B_indices]
    T_obs = (sum(B_vals) / len(B_vals)) - (sum(notB_vals) / len(notB_vals))

    rng = random.Random(SEED + 1)
    all_indices = list(range(1, pair_count + 1))
    T_null = []
    for _ in range(n_perms):
        rng.shuffle(all_indices)
        fake_B = set(all_indices[:B_size])
        b = [d_consec[i - 1] for i in fake_B]
        nb = [d_consec[i - 1] for i in all_indices[B_size:]]
        T_null.append((sum(b) / len(b)) - (sum(nb) / len(nb)))

    count_ge = sum(1 for t in T_null if abs(t) >= abs(T_obs))
    p_two_sided = (count_ge + 1) / (n_perms + 1)
    return {
        "T_obs": T_obs,
        "sign": "positive_B_has_larger_distances" if T_obs > 0 else "negative_B_has_smaller_distances",
        "p_two_sided": p_two_sided,
        "n_perms": n_perms,
        "T_null_mean": sum(T_null) / len(T_null),
        "T_null_sd": (sum((t - sum(T_null) / len(T_null)) ** 2 for t in T_null) / len(T_null)) ** 0.5,
    }


# ---------------------------------------------------------------------------
# Secondary B: MW-5 positive-control (sort-by-length discriminativeness)
# ---------------------------------------------------------------------------

def secondary_B_mw5(D: dict[tuple[int, int], float],
                    verse_counts: dict[int, int],
                    top15_mushaf: list[tuple[int, int]],
                    B_pairs: set[tuple[int, int]]) -> dict:
    # Sort surahs by descending verse count (ties broken by surah number, deterministic)
    order = sorted(range(1, 115), key=lambda s: (-verse_counts[s], s))
    d_consec_synth = [D[(order[i], order[i + 1])] for i in range(len(order) - 1)]
    assert len(d_consec_synth) == 113

    ranked = sorted(range(113), key=lambda k: -d_consec_synth[k])[:K_TOP]
    top15_synth = [(order[k], order[k + 1]) for k in ranked]
    top15_synth_set = set(top15_synth)
    top15_mushaf_set = set(top15_mushaf)

    intersect = top15_mushaf_set & top15_synth_set
    synth_hits_B = len(top15_synth_set & B_pairs)

    return {
        "synthetic_ordering": "descending_verse_count",
        "top15_synth": top15_synth,
        "n_pairs_shared_with_mushaf_top15": len(intersect),
        "identical_top15": top15_synth_set == top15_mushaf_set,
        "synth_hits_against_B": synth_hits_B,
        "pass_discriminativeness": top15_synth_set != top15_mushaf_set,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    random.seed(SEED)

    # Pre-committed boundary set
    B_dict = build_boundary_set()
    B_pairs = set(B_dict.keys())
    B_indices = {i for (i, _j) in B_pairs}
    assert len(B_indices) == len(B_pairs)  # each pair (i, i+1) has unique i

    # Load D-matrix (parent)
    D = load_d_matrix()
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
    p_primary = hypergeom_sf(obs_k, N, K_size, n)

    threshold_pass = 12  # pre-committed
    primary_pass = obs_k >= threshold_pass

    # Secondary A: B vs notB mean-distance
    sec_A = secondary_A(d_consec, B_indices, N_PERMS)

    # Secondary B / MW-5: sort-by-length control
    verse_counts = load_verse_counts()
    assert len(verse_counts) >= 114
    sec_B = secondary_B_mw5(D, verse_counts, top_K_pairs, B_pairs)

    # Assemble top-15 table with distances and B-labels
    top15_table = []
    for (i, j) in top_K_pairs:
        top15_table.append({
            "i": i,
            "j": j,
            "distance": d_consec[i - 1],
            "in_B": (i, j) in B_pairs,
            "B_labels": B_dict.get((i, j), []),
        })
    top15_table.sort(key=lambda x: -x["distance"])

    # Verdict
    primary_verdict = "PASS" if primary_pass else "NULL"
    if not sec_B["pass_discriminativeness"]:
        primary_verdict = "INSTRUMENT-BROKEN (MW-5 fails; M'=M_mushaf)"
    sec_A_pass = (sec_A["p_two_sided"] < 0.0167) and (sec_A["T_obs"] > 0)

    # Findings JSON
    output = {
        "finding_id": "h-new-130",
        "title": "Fisher-Rao mushaf-geodesic residuals analysis",
        "pre_reg_path": str(PREREG_PATH),
        "pre_reg_sha256": sha256_file(PREREG_PATH),
        "parent_finding": "h-new-111 / cross-finding-011",
        "seed": SEED,
        "date": "2026-04-17",
        "rules_tuple": "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)",
        "bonferroni_k": 3,
        "bonferroni_family": "h-new-130-residuals",
        "alpha_bon": 0.0167,
        "boundary_set": {f"{i}-{j}": labels for (i, j), labels in B_dict.items()},
        "boundary_set_size": K_size,
        "boundary_set_fraction_of_113": K_size / 113,
        "consecutive_mushaf_distances": {
            f"{i}-{i + 1}": d_consec[i - 1] for i in range(1, 114)
        },
        "top15_largest_jumps": top15_table,
        "primary": {
            "observed_M_intersect_B": obs_k,
            "threshold_pass": threshold_pass,
            "null_model": "hypergeometric(N=113, K=|B|=54, n=15)",
            "null_expected_overlap": n * K_size / N,
            "p_primary_one_sided_upper": p_primary,
            "alpha_bon": 0.0167,
            "pass_primary": primary_pass,
            "verdict": primary_verdict,
        },
        "secondary_A_concentration": sec_A | {
            "alpha_bon": 0.0167,
            "pass_secondary_A": sec_A_pass,
        },
        "secondary_B_mw5_control": sec_B,
        "top15_pairs_intersect_B_list": sorted(list(M_intersect_B)),
        "top15_pairs_not_in_B_list": sorted(list(top_K_set - B_pairs)),
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # Human-readable summary
    print("=" * 70)
    print("H-NEW-130 — Fisher-Rao residuals")
    print("=" * 70)
    print(f"|B| = {K_size} of 113 ({K_size / 113:.1%})")
    print(f"Expected |M ∩ B| under null (hypergeom mean): {n * K_size / N:.3f}")
    print(f"Observed |M ∩ B|: {obs_k}")
    print(f"Primary p (one-sided upper, hypergeom): {p_primary:.5f}")
    print(f"Threshold pass (>=12): {primary_pass}")
    print(f"Primary verdict: {primary_verdict}")
    print()
    print("Top-15 largest-jump consecutive pairs (descending distance):")
    for row in top15_table:
        mark = "B" if row["in_B"] else "-"
        labels = (" " + ", ".join(row["B_labels"])) if row["B_labels"] else ""
        print(f"  Q{row['i']:3d} → Q{row['j']:3d}  d={row['distance']:.4f}  [{mark}]{labels}")
    print()
    print(f"Secondary A: T = {sec_A['T_obs']:.5f}, p_two_sided = {sec_A['p_two_sided']:.5f}")
    print(f"  Sign: {sec_A['sign']}")
    print(f"  Pass: {sec_A_pass}")
    print()
    print("Secondary B / MW-5 (sort-by-length discriminativeness):")
    print(f"  Identical top-15 as mushaf? {sec_B['identical_top15']}")
    print(f"  Shared pairs with mushaf top-15: {sec_B['n_pairs_shared_with_mushaf_top15']}")
    print(f"  Synthetic-ordering hits against B: {sec_B['synth_hits_against_B']}")
    print(f"  Pass discriminativeness: {sec_B['pass_discriminativeness']}")
    print()
    print(f"Output JSON: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
