#!/usr/bin/env python3
"""H-NEW-282: Q 42 HMASQ mushaf-block vs phonological-cluster tension.

Pre-reg: findings/phase-b-hypotheses/h-new-290-q42-block-vs-phonology-tension-prereg.md
Seed: 20260422
"""

import hashlib
import json
import math
import random
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG_MD = ROOT / "findings/phase-b-hypotheses/h-new-290-q42-block-vs-phonology-tension-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-290.json"

SEED = 20260422
N_PERM = 1000


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_fr_matrix():
    """Load 114×114 Fisher-Rao distance matrix from h-new-111.json upper-triangular."""
    with open(H_NEW_111_JSON) as f:
        d = json.load(f)
    ut = d["D_matrix_upper_triangular"]
    mat = [[0.0] * 115 for _ in range(115)]  # 1-indexed [1..114]
    for i, j, dist in ut:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def main():
    random.seed(SEED)
    prereg_sha = sha256_file(PREREG_MD)

    print("=" * 75)
    print("H-NEW-282: Q 42 HMASQ — mushaf-block vs phonological-cluster tension")
    print("=" * 75)
    print(f"Pre-reg SHA-256: {prereg_sha}")
    print(f"Seed: {SEED}")
    print()

    D = load_fr_matrix()
    print("Fisher-Rao matrix loaded (114×114 from h-new-111.json).")
    print()

    # Target pivots
    Q42 = 42
    Q41, Q43 = 41, 43  # mushaf-block neighbors (both HM)
    Q26, Q28 = 26, 28  # TSM cluster members
    Q40, Q44, Q45, Q46 = 40, 44, 45, 46  # other HM block
    # All HM cluster (exclude Q 42)
    HM_BLOCK = [40, 41, 43, 44, 45, 46]
    TSM_CLUSTER = [26, 28]

    # === CELL A: Head-to-head comparison ===
    print("=" * 50)
    print("CELL A — Head-to-head comparison")
    print("=" * 50)

    d_block_41 = D[Q42][Q41]
    d_block_43 = D[Q42][Q43]
    d_phon_26 = D[Q42][Q26]
    d_phon_28 = D[Q42][Q28]

    d_block_mean = (d_block_41 + d_block_43) / 2
    d_phon_mean = (d_phon_26 + d_phon_28) / 2
    delta = d_block_mean - d_phon_mean

    print(f"d(Q 42, Q 41) = {d_block_41:.4f}  (block-left)")
    print(f"d(Q 42, Q 43) = {d_block_43:.4f}  (block-right)")
    print(f"d(Q 42, Q 26) = {d_phon_26:.4f}  (TSM)")
    print(f"d(Q 42, Q 28) = {d_phon_28:.4f}  (TSM)")
    print(f"d̄_block = {d_block_mean:.4f}")
    print(f"d̄_phon  = {d_phon_mean:.4f}")
    print(f"Δ = d̄_block − d̄_phon = {delta:+.4f}")
    print(f"  (negative → BLOCK wins; positive → PHONOLOGY wins)")

    # Null for Cell A: random pairs from all non-Q-42 surahs
    non_q42 = [i for i in range(1, 115) if i != Q42]
    nulls_delta = []
    for _ in range(N_PERM):
        # Draw 2 random surahs for "block-like" and 2 for "phon-like"
        sample_block = random.sample(non_q42, 2)
        sample_phon = random.sample(non_q42, 2)
        null_block_mean = (D[Q42][sample_block[0]] + D[Q42][sample_block[1]]) / 2
        null_phon_mean = (D[Q42][sample_phon[0]] + D[Q42][sample_phon[1]]) / 2
        nulls_delta.append(null_block_mean - null_phon_mean)

    nulls_delta.sort()
    null_mean = sum(nulls_delta) / len(nulls_delta)
    null_sd = math.sqrt(sum((x - null_mean) ** 2 for x in nulls_delta) / (len(nulls_delta) - 1))

    # Two-sided p under H_0
    ge_extreme = sum(1 for x in nulls_delta if abs(x) >= abs(delta))
    p_two = ge_extreme / N_PERM

    # One-sided p under pre-committed direction
    if delta < 0:
        p_one_block = sum(1 for x in nulls_delta if x <= delta) / N_PERM
        p_one_phon = 1 - p_one_block
    else:
        p_one_phon = sum(1 for x in nulls_delta if x >= delta) / N_PERM
        p_one_block = 1 - p_one_phon

    print(f"Null mean Δ: {null_mean:+.4f} (sd {null_sd:.4f})")
    print(f"p_two-sided (H_0 rejection): {p_two:.4f}")
    print(f"p_one-sided block: {p_one_block:.4f}")
    print(f"p_one-sided phon:  {p_one_phon:.4f}")

    alpha_bon = 0.01667
    if delta < 0 and p_one_block < alpha_bon:
        cell_a = "BLOCK-DOMINANCE (direction-locked)"
    elif delta > 0 and p_one_phon < alpha_bon:
        cell_a = "PHON-DOMINANCE (direction-locked)"
    else:
        cell_a = "H_0 (indistinguishable)"
    print(f"Cell A verdict: {cell_a}")
    print()

    # === CELL B: Ranked-neighbor test ===
    print("=" * 50)
    print("CELL B — Ranked-neighbor test")
    print("=" * 50)

    # Rank all 113 non-Q-42 surahs by FR distance to Q 42
    ranked = sorted(non_q42, key=lambda s: D[Q42][s])
    ranks = {s: idx + 1 for idx, s in enumerate(ranked)}

    block_ranks = [ranks[s] for s in HM_BLOCK]
    phon_ranks = [ranks[s] for s in TSM_CLUSTER]

    block_median = sorted(block_ranks)[len(block_ranks) // 2]
    phon_median = sorted(phon_ranks)[len(phon_ranks) // 2]

    print(f"HM-block-neighbor ranks (Q 40, 41, 43, 44, 45, 46): {block_ranks}")
    print(f"TSM-cluster ranks (Q 26, 28): {phon_ranks}")
    print(f"HM-block median rank: {block_median}")
    print(f"TSM-cluster median rank: {phon_median}")
    print()
    print(f"Q 41 (left neighbor): rank {ranks[Q41]}")
    print(f"Q 43 (right neighbor): rank {ranks[Q43]}")
    print(f"Q 26 (TSM): rank {ranks[Q26]}")
    print(f"Q 28 (TSM): rank {ranks[Q28]}")

    # Lower rank = closer = wins
    if block_median < phon_median:
        cell_b = f"BLOCK-DOMINANCE (block median {block_median} < phon median {phon_median})"
    elif phon_median < block_median:
        cell_b = f"PHON-DOMINANCE (phon median {phon_median} < block median {block_median})"
    else:
        cell_b = f"TIED"

    # Permutation for Cell B: random 6-set rank median vs random 2-set rank median
    null_medians_block = []
    null_medians_phon = []
    for _ in range(N_PERM):
        sample6 = random.sample(non_q42, 6)
        sample2 = random.sample(non_q42, 2)
        null_medians_block.append(sorted([ranks[s] for s in sample6])[3])
        null_medians_phon.append(sorted([ranks[s] for s in sample2])[1])

    # One-sided: is observed block-median significantly LOWER than null?
    p_block_rank = sum(1 for x in null_medians_block if x <= block_median) / N_PERM
    p_phon_rank = sum(1 for x in null_medians_phon if x <= phon_median) / N_PERM

    print(f"Cell B verdict: {cell_b}")
    print(f"p(block_median ≤ observed): {p_block_rank:.4f}")
    print(f"p(phon_median ≤ observed): {p_phon_rank:.4f}")
    print()

    # === CELL C: Centroid-distance ===
    print("=" * 50)
    print("CELL C — HMASQ to block-centroid distance (root-content)")
    print("=" * 50)

    # Mean FR distance from Q 42 to HM block and to TSM cluster
    d_to_hm_mean = sum(D[Q42][s] for s in HM_BLOCK) / len(HM_BLOCK)
    d_to_tsm_mean = sum(D[Q42][s] for s in TSM_CLUSTER) / len(TSM_CLUSTER)

    print(f"Mean d(Q 42, HM block Q 40/41/43/44/45/46) = {d_to_hm_mean:.4f}")
    print(f"Mean d(Q 42, TSM cluster Q 26/28)          = {d_to_tsm_mean:.4f}")
    print(f"Ratio HM/TSM = {d_to_hm_mean / d_to_tsm_mean:.4f}")

    if d_to_hm_mean < d_to_tsm_mean:
        cell_c = "HM-centroid closer (block-content dominance at centroid level)"
    else:
        cell_c = "TSM-centroid closer (phonology-content agreement at centroid level)"
    print(f"Cell C verdict: {cell_c}")
    print()

    # === MW-5 positive control on Q 43 (control HM surah) ===
    print("=" * 50)
    print("MW-5 positive control — Q 43 (should show BLOCK-DOMINANCE)")
    print("=" * 50)

    Q43_control = 43
    # For Q 43, block-neighbors are Q 42 (HMASQ, but still HM-block), Q 44 (HM)
    # Phon-TSM cluster members: Q 26, Q 28
    d_ctrl_block = (D[Q43_control][42] + D[Q43_control][44]) / 2
    d_ctrl_phon = (D[Q43_control][26] + D[Q43_control][28]) / 2
    ctrl_delta = d_ctrl_block - d_ctrl_phon

    print(f"Q 43 d̄_block = {d_ctrl_block:.4f}")
    print(f"Q 43 d̄_phon  = {d_ctrl_phon:.4f}")
    print(f"Q 43 Δ = {ctrl_delta:+.4f}")
    print(f"Expected: Δ < 0 (block dominance for canonical HM surah)")
    if ctrl_delta < 0:
        mw5 = "PASS (Q 43 shows block-dominance as expected)"
    else:
        mw5 = "FAIL (Q 43 does NOT show block-dominance — instrument suspect!)"
    print(f"MW-5: {mw5}")

    # === Combined verdict ===
    print()
    print("=" * 50)
    print("COMBINED VERDICT")
    print("=" * 50)

    cells_block = sum(1 for v in [cell_a, cell_b, cell_c]
                      if "BLOCK" in v or "HM-centroid" in v)
    cells_phon = sum(1 for v in [cell_a, cell_b, cell_c]
                     if "PHON" in v or "TSM-centroid" in v)

    if cells_block >= 2 and cells_phon == 0:
        verdict = "BLOCK-DOMINANCE (2-3 of 3 cells)"
    elif cells_phon >= 2 and cells_block == 0:
        verdict = "PHON-DOMINANCE (2-3 of 3 cells)"
    elif cells_block >= 1 and cells_phon >= 1:
        verdict = "MIXED (multi-principled Q 42 placement)"
    else:
        verdict = "H_0 (indistinguishable)"

    print(f"Cells supporting BLOCK: {cells_block}/3")
    print(f"Cells supporting PHON:  {cells_phon}/3")
    print(f"OVERALL VERDICT: {verdict}")

    # Write JSON
    out = {
        "id": "H-NEW-282",
        "title": "Q 42 HMASQ mushaf-block vs phonological-cluster tension",
        "prereg_sha256": prereg_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": 3,
        "alpha_bon": alpha_bon,
        "cell_A": {
            "d_block_41": d_block_41,
            "d_block_43": d_block_43,
            "d_phon_26": d_phon_26,
            "d_phon_28": d_phon_28,
            "d_block_mean": d_block_mean,
            "d_phon_mean": d_phon_mean,
            "delta": delta,
            "null_mean": null_mean,
            "null_sd": null_sd,
            "p_two_sided": p_two,
            "p_one_block": p_one_block,
            "p_one_phon": p_one_phon,
            "verdict": cell_a,
        },
        "cell_B": {
            "block_neighbor_ranks": {str(s): ranks[s] for s in HM_BLOCK},
            "tsm_cluster_ranks": {str(s): ranks[s] for s in TSM_CLUSTER},
            "block_median_rank": block_median,
            "phon_median_rank": phon_median,
            "p_block_rank": p_block_rank,
            "p_phon_rank": p_phon_rank,
            "verdict": cell_b,
        },
        "cell_C": {
            "d_to_hm_mean": d_to_hm_mean,
            "d_to_tsm_mean": d_to_tsm_mean,
            "ratio_hm_over_tsm": d_to_hm_mean / d_to_tsm_mean,
            "verdict": cell_c,
        },
        "mw5": {
            "control_surah": Q43_control,
            "d_ctrl_block": d_ctrl_block,
            "d_ctrl_phon": d_ctrl_phon,
            "ctrl_delta": ctrl_delta,
            "verdict": mw5,
        },
        "overall_verdict": verdict,
        "cells_supporting_block": cells_block,
        "cells_supporting_phon": cells_phon,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
