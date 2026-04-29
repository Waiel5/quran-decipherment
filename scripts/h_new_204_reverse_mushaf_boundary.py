#!/usr/bin/env python3
"""H-NEW-204 — Reverse-mushaf boundary test.

QUESTION: Under reverse-mushaf order (114→113→...→1), do the same boundaries
appear as under forward order? Fisher-Rao is a symmetric metric, so:

  (A) The SET of consecutive-pair distances {d(i, i+1) : i=1..113} is
      IDENTICAL under reversal. Top-15 concentration stats MUST match
      H-NEW-130 exactly. (This is a verification / no-bug check.)

  (B) The interesting question is: is there REFLECTIVE structure?
      Define the mirror partner of pair (i, i+1) as (115-i, 114-i).
      If architectural structure is mirror-symmetric about the mushaf midpoint,
      d(i, i+1) should be CORRELATED with d(115-i, 114-i). If the top-15
      boundaries mirror-partner each other more than chance, that's novel.

Pre-reg tests (Bonferroni k=2):
  PRIMARY (verification): top-15 under reverse == top-15 under forward as SETS.
    This MUST pass by symmetry; failure indicates a bug.
  SECONDARY (novel): Spearman-style permutation test on mirror correlation
    between d(i, i+1) and d(115-i, 114-i) across i=1..56 (excluding midpoint
    pair 57-58 which is self-mirror).

Seed: 20260419. Deterministic.
Output: findings/phase-b-hypotheses/csv/h-new-204.json
"""

from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path

SEED = 20260419
PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
H_NEW_130_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130.json"
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-204.json"

K_TOP = 15
N_PERMS = 10_000
BONFERRONI_K = 2
ALPHA = 0.05
ALPHA_BON = ALPHA / BONFERRONI_K  # 0.025


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


def load_forward_boundary_set() -> dict[str, list[str]]:
    """Re-use the pre-committed B set from H-NEW-130."""
    with H_NEW_130_JSON.open() as f:
        parent_130 = json.load(f)
    return parent_130["boundary_set"]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def spearman_rho(x: list[float], y: list[float]) -> float:
    """Spearman rank correlation."""
    n = len(x)
    assert n == len(y)

    def ranks(v: list[float]) -> list[float]:
        sorted_idx = sorted(range(n), key=lambda k: v[k])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[sorted_idx[j + 1]] == v[sorted_idx[i]]:
                j += 1
            avg_rank = (i + j) / 2.0 + 1.0  # average of 1-based ranks
            for k in range(i, j + 1):
                r[sorted_idx[k]] = avg_rank
            i = j + 1
        return r

    rx, ry = ranks(x), ranks(y)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((rx[k] - mx) * (ry[k] - my) for k in range(n))
    dx = (sum((rx[k] - mx) ** 2 for k in range(n))) ** 0.5
    dy = (sum((ry[k] - my) ** 2 for k in range(n))) ** 0.5
    if dx == 0 or dy == 0:
        return 0.0
    return num / (dx * dy)


def main() -> None:
    random.seed(SEED)

    D = load_d_matrix()

    # Forward consecutive distances: d_fwd[k] = D(k+1, k+2), k=0..112
    d_fwd = [D[(i, i + 1)] for i in range(1, 114)]
    assert len(d_fwd) == 113

    # Reverse-mushaf ordering: order = [114, 113, ..., 1]
    rev_order = list(range(114, 0, -1))
    # Consecutive distances under reverse ordering:
    # d_rev[k] = D(rev_order[k], rev_order[k+1]) = D(114-k, 113-k)
    d_rev = [D[(rev_order[k], rev_order[k + 1])] for k in range(113)]
    assert len(d_rev) == 113

    # (A) Symmetry verification: d_fwd reversed should equal d_rev
    fwd_reversed = list(reversed(d_fwd))
    sym_diff = max(abs(a - b) for a, b in zip(fwd_reversed, d_rev))
    symmetric_ok = sym_diff < 1e-12

    # (A-cont) Top-15 pair SETS under forward vs reverse
    top15_fwd_indices = sorted(range(1, 114), key=lambda i: -d_fwd[i - 1])[:K_TOP]
    top15_fwd_pairs = sorted([(i, i + 1) for i in top15_fwd_indices])
    # Under reverse order, position k (0-indexed) corresponds to pair
    # (rev_order[k], rev_order[k+1]) = (115-k-1, 114-k-1) = (114-k, 113-k)
    # But the UNORDERED pair {a, b} with a<b is the same as the forward pair.
    top15_rev_positions = sorted(range(113), key=lambda k: -d_rev[k])[:K_TOP]
    top15_rev_pairs = sorted([
        tuple(sorted((rev_order[k], rev_order[k + 1])))
        for k in top15_rev_positions
    ])

    primary_pass = top15_fwd_pairs == top15_rev_pairs and symmetric_ok

    # (B) Mirror-symmetry test:
    # Pair i = (i, i+1), mirror partner = (115-i, 114-i) for i in 1..56
    # (i=57 is the self-mirror pair (57,58) -> mirror is also (57,58))
    # (i=114-i+1 means partner index i' = 114-i. For i<=56 i'>=58; for i=57, i'=57.)
    # We take i in 1..56 and pair it with i' = 114-i (so i'>=58).
    mirror_pairs = []
    for i in range(1, 57):
        j = 114 - i  # partner pair index (the "i" of the partner pair, j to j+1)
        assert j >= 58
        mirror_pairs.append((d_fwd[i - 1], d_fwd[j - 1], i, j))

    x = [m[0] for m in mirror_pairs]
    y = [m[1] for m in mirror_pairs]
    rho_obs = spearman_rho(x, y)

    # Permutation null: shuffle y, recompute rho
    rng = random.Random(SEED + 1)
    rho_null = []
    y_perm = list(y)
    for _ in range(N_PERMS):
        rng.shuffle(y_perm)
        rho_null.append(spearman_rho(x, y_perm))

    count_ge = sum(1 for r in rho_null if abs(r) >= abs(rho_obs))
    p_mirror_two_sided = (count_ge + 1) / (N_PERMS + 1)
    mirror_pass = p_mirror_two_sided < ALPHA_BON

    # Also check: do top-15 forward boundaries have mirror partners in top-15?
    top15_fwd_i_values = set(top15_fwd_indices)
    mirror_hits = 0
    mirror_hit_list = []
    for i in top15_fwd_i_values:
        if i == 57:
            continue  # self-mirror, skip
        partner_i = 114 - i
        if partner_i in top15_fwd_i_values and i < partner_i:
            mirror_hits += 1
            mirror_hit_list.append(((i, i + 1), (partner_i, partner_i + 1)))

    # Null for mirror_hits: randomly pick 15 of 113 indices, count mirror-pairs
    rng2 = random.Random(SEED + 2)
    all_i = list(range(1, 114))
    null_mirror_hits = []
    for _ in range(N_PERMS):
        sample = set(rng2.sample(all_i, K_TOP))
        cnt = 0
        for i in sample:
            if i == 57:
                continue
            partner = 114 - i
            if partner in sample and i < partner:
                cnt += 1
        null_mirror_hits.append(cnt)
    p_mirror_hits = (sum(1 for c in null_mirror_hits if c >= mirror_hits) + 1) / (N_PERMS + 1)

    # Magnitude mirror: |d(2,3) - d(113,114)| / (max-min), etc.
    # Largest top-forward boundary was Q2->Q3 (from H-NEW-130 findings). Let's
    # check d(2,3) vs d(113,114) specifically.
    d_2_3 = D[(2, 3)]
    d_113_114 = D[(113, 114)]
    abs_diff_extremes = abs(d_2_3 - d_113_114)
    mean_d = sum(d_fwd) / len(d_fwd)
    relative_diff_extremes = abs_diff_extremes / mean_d if mean_d else float("inf")

    output = {
        "finding_id": "h-new-204",
        "title": "Reverse-mushaf boundary test: symmetry verification + mirror-symmetry test",
        "parent_finding": "h-new-111 / h-new-130 / cross-finding-011",
        "parent_d_matrix_sha256": sha256_file(H_NEW_111_JSON),
        "parent_130_sha256": sha256_file(H_NEW_130_JSON),
        "seed": SEED,
        "date": "2026-04-17",
        "rules_tuple": "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order REVERSED, Hafs-Kufan)",
        "bonferroni_k": BONFERRONI_K,
        "bonferroni_family": "h-new-204-reverse-mushaf",
        "alpha_bon": ALPHA_BON,
        "n_perms": N_PERMS,
        "primary_symmetry_verification": {
            "description": "Under reverse mushaf order, top-15 largest consecutive-pair Fisher-Rao distances should be IDENTICAL (as sets) to forward order (Fisher-Rao is symmetric).",
            "max_abs_diff_fwd_reversed_vs_rev": sym_diff,
            "symmetry_ok_tol_1e-12": symmetric_ok,
            "top15_fwd_pairs": top15_fwd_pairs,
            "top15_rev_pairs": top15_rev_pairs,
            "sets_identical": top15_fwd_pairs == top15_rev_pairs,
            "pass_primary": primary_pass,
            "interpretation": "PASS = metric is symmetric (expected). FAIL = bug in pipeline.",
        },
        "secondary_mirror_symmetry": {
            "description": "Spearman correlation between d(i, i+1) and d(115-i, 114-i) for i in 1..56 tests reflective architectural structure about the mushaf midpoint.",
            "n_mirror_pairs": len(mirror_pairs),
            "mirror_partner_indices": [(m[2], m[3]) for m in mirror_pairs[:5]],
            "rho_obs_spearman": rho_obs,
            "p_two_sided_perm": p_mirror_two_sided,
            "alpha_bon": ALPHA_BON,
            "pass_secondary_mirror": mirror_pass,
            "sign": "positive_mirror_corr" if rho_obs > 0 else "negative_mirror_corr",
            "null_rho_mean": sum(rho_null) / len(rho_null),
            "null_rho_sd": (sum((r - sum(rho_null) / len(rho_null)) ** 2 for r in rho_null) / len(rho_null)) ** 0.5,
        },
        "tertiary_top15_mirror_hits": {
            "description": "Count of mirror-partner pairs within top-15 forward boundaries (exploratory, not Bonferroni-counted).",
            "mirror_hits_observed": mirror_hits,
            "mirror_hit_pairs": mirror_hit_list,
            "p_one_sided_perm": p_mirror_hits,
            "null_expected": sum(null_mirror_hits) / len(null_mirror_hits),
        },
        "magnitude_mirror_check": {
            "d_2_3": d_2_3,
            "d_113_114": d_113_114,
            "abs_diff": abs_diff_extremes,
            "mean_consecutive_d": mean_d,
            "relative_diff_to_mean": relative_diff_extremes,
        },
        "verdict": {
            "primary_symmetry": "PASS" if primary_pass else "FAIL-BUG",
            "secondary_mirror": "PASS" if mirror_pass else "NULL",
            "interpretation": (
                "Primary PASS confirms Fisher-Rao metric symmetry (no bug). "
                "Secondary mirror test is the novel question: is there reflective "
                "architectural structure about the mushaf midpoint? "
                "NULL = boundaries are not systematically mirror-placed."
            ),
        },
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print("H-NEW-204 — Reverse-mushaf boundary test")
    print("=" * 70)
    print(f"Seed: {SEED}, Bonferroni k={BONFERRONI_K}, alpha_bon={ALPHA_BON}")
    print()
    print("PRIMARY (symmetry verification):")
    print(f"  max |d_fwd_reversed - d_rev| = {sym_diff:.2e}")
    print(f"  top-15 sets identical: {top15_fwd_pairs == top15_rev_pairs}")
    print(f"  verdict: {'PASS' if primary_pass else 'FAIL-BUG'}")
    print()
    print("SECONDARY (mirror-symmetry):")
    print(f"  Spearman rho between d(i,i+1) and d(115-i,114-i), i=1..56: {rho_obs:.4f}")
    print(f"  p_two_sided (perm, n={N_PERMS}): {p_mirror_two_sided:.5f}")
    print(f"  null rho mean={sum(rho_null)/len(rho_null):.4f}")
    print(f"  verdict: {'PASS' if mirror_pass else 'NULL'}")
    print()
    print("TERTIARY (top-15 mirror-partner hits, exploratory):")
    print(f"  observed: {mirror_hits}")
    print(f"  expected under null: {sum(null_mirror_hits)/len(null_mirror_hits):.3f}")
    print(f"  p_one_sided: {p_mirror_hits:.5f}")
    print(f"  mirror-partner pairs: {mirror_hit_list}")
    print()
    print(f"Magnitude mirror: d(2,3)={d_2_3:.4f}, d(113,114)={d_113_114:.4f}")
    print(f"  abs diff = {abs_diff_extremes:.4f}, rel to mean = {relative_diff_extremes:.2%}")
    print()
    print(f"Output: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
