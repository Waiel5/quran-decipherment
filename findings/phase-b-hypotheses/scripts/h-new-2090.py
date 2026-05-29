#!/usr/bin/env python3
"""
H-NEW-2090 — Surah-position / verse-count arithmetic-coincidence scan.

Skeptical audit: how many "surah N encodes its verse-count" coincidences are
expected purely by chance? Permutation null shuffles the verse-count multiset
across positions; we count exact arithmetic hits per cell.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2090-surah-arithmetic.md
SHA256 LOCK (computed 2026-05-29):
  5a6599038a283ce0886b9b8ce3f1cb15d99621f05d8546d3c304348918aed77d

Rules-tuple: (Hafs-Kūfan verse-counts, canonical mushaf order 1..114, whole-verse unit)
Null model: random permutation of the 114 verse-counts across the 114 positions.
Seed: 20260509 | n_perm: 10000 | Bonferroni k=8, alpha_bon = 0.05/8 = 0.00625
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

import numpy as np

PROJECT_ROOT = "/Users/grey/Downloads/quran"
PREREG_PATH = os.path.join(
    PROJECT_ROOT,
    "findings/phase-b-hypotheses/prereg-h-new-2090-surah-arithmetic.md",
)
EXPECTED_SHA = "5a6599038a283ce0886b9b8ce3f1cb15d99621f05d8546d3c304348918aed77d"
COUNTS_TSV = os.path.join(PROJECT_ROOT, "data/hafs-verse-counts.tsv")
OUTPUT_JSON = os.path.join(
    PROJECT_ROOT, "findings/phase-b-hypotheses/csv/h-new-2090.json"
)

SEED = 20260509
N_PERM = 10000
BONF_K = 8
ALPHA_BON = 0.05 / BONF_K  # 0.00625

# Cell 7 locked linear grid
GRID_A = (1, 2, 3)
GRID_B = (-2, -1, 0, 1, 2)


def verify_prereg_sha() -> str:
    with open(PREREG_PATH, "rb") as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(
            f"FATAL: prereg SHA mismatch.\n  expected {EXPECTED_SHA}\n  actual   {actual}",
            file=sys.stderr,
        )
        sys.exit(1)
    return actual


def load_counts() -> np.ndarray:
    """Return verse_counts indexed by position (positions[i] == i+1)."""
    positions = []
    counts = []
    with open(COUNTS_TSV, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            positions.append(int(parts[0]))
            counts.append(int(parts[1]))
    assert positions == list(range(1, 115)), "positions must be 1..114 in order"
    counts = np.array(counts, dtype=np.int64)
    assert len(counts) == 114, f"expected 114 surahs, got {len(counts)}"
    assert counts.sum() == 6236, f"verse-count sum must be 6236, got {counts.sum()}"
    return counts


def prime_mask(limit: int) -> np.ndarray:
    """Boolean array sieve[n] == True iff n is prime, for n in 0..limit."""
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return sieve


# ---- Cell coincidence-counters. Each takes verse_counts (vc) indexed 0..113
#      where position N = index+1, and returns (count, hit_positions). ----

POS = np.arange(1, 115, dtype=np.int64)  # positions 1..114


def cell1_identity(vc):  # vc == N
    hits = np.where(vc == POS)[0]
    return len(hits), (hits + 1).tolist()


def cell2_double(vc):  # vc == 2N
    hits = np.where(vc == 2 * POS)[0]
    return len(hits), (hits + 1).tolist()


def cell3_half(vc):  # vc == N/2 (N even)
    even = (POS % 2 == 0)
    hits = np.where(even & (vc == POS // 2))[0]
    return len(hits), (hits + 1).tolist()


def cell4_offby1(vc):  # |vc - N| <= 1
    hits = np.where(np.abs(vc - POS) <= 1)[0]
    return len(hits), (hits + 1).tolist()


_PRIME = prime_mask(286)
_POS_PRIME = np.array([_PRIME[n] for n in POS])  # structural, fixed


def cell5_coprimality(vc):  # both N prime and vc prime
    vc_prime = _PRIME[vc]
    hits = np.where(_POS_PRIME & vc_prime)[0]
    return len(hits), (hits + 1).tolist()


def _digit_reverse(n: int) -> int:
    return int(str(n)[::-1])


_POS_REV = np.array([_digit_reverse(int(n)) for n in POS], dtype=np.int64)


def cell6_reversal(vc):  # vc == digit-reverse(N)
    hits = np.where(vc == _POS_REV)[0]
    return len(hits), (hits + 1).tolist()


def cell7_linear_grid(vc):
    """Pooled exact hits over a in {1,2,3}, b in {-2..2}.
    Returns (#surahs-with-any-hit, sorted hit positions, total grid-hit tally)."""
    any_hit = np.zeros(114, dtype=bool)
    total = 0
    for a in GRID_A:
        for b in GRID_B:
            m = (vc == a * POS + b)
            total += int(m.sum())
            any_hit |= m
    hits = np.where(any_hit)[0]
    return len(hits), (hits + 1).tolist(), total


def cell8_multiple(vc):  # N | vc, vc > 0
    hits = np.where((vc > 0) & (vc % POS == 0))[0]
    return len(hits), (hits + 1).tolist()


def main():
    actual_sha = verify_prereg_sha()
    vc = load_counts()
    rng = np.random.default_rng(SEED)

    # --- observed ---
    obs = {}
    obs["cell1_identity"] = cell1_identity(vc)
    obs["cell2_double"] = cell2_double(vc)
    obs["cell3_half"] = cell3_half(vc)
    obs["cell4_offby1"] = cell4_offby1(vc)
    obs["cell5_coprimality"] = cell5_coprimality(vc)
    obs["cell6_reversal"] = cell6_reversal(vc)
    c7 = cell7_linear_grid(vc)
    obs["cell7_linear_grid"] = (c7[0], c7[1])
    obs_cell7_total = c7[2]
    obs["cell8_multiple"] = cell8_multiple(vc)

    # observed scalar counts for null comparison
    obs_counts = {k: v[0] for k, v in obs.items()}

    # --- permutation null ---
    null_counts = {k: np.empty(N_PERM, dtype=np.int64) for k in obs_counts}
    for i in range(N_PERM):
        perm = rng.permutation(vc)
        null_counts["cell1_identity"][i] = cell1_identity(perm)[0]
        null_counts["cell2_double"][i] = cell2_double(perm)[0]
        null_counts["cell3_half"][i] = cell3_half(perm)[0]
        null_counts["cell4_offby1"][i] = cell4_offby1(perm)[0]
        null_counts["cell5_coprimality"][i] = cell5_coprimality(perm)[0]
        null_counts["cell6_reversal"][i] = cell6_reversal(perm)[0]
        null_counts["cell7_linear_grid"][i] = cell7_linear_grid(perm)[0]
        null_counts["cell8_multiple"][i] = cell8_multiple(perm)[0]

    cells = {}
    for k in obs_counts:
        nd = null_counts[k]
        o = int(obs_counts[k])
        p_one_sided = (1 + int(np.sum(nd >= o))) / (N_PERM + 1)
        cells[k] = {
            "observed_count": o,
            "observed_hit_positions": obs[k][1],
            "null_mean": float(np.mean(nd)),
            "null_median": float(np.median(nd)),
            "null_max": int(np.max(nd)),
            "null_p95": float(np.percentile(nd, 95)),
            "p_one_sided_excess": p_one_sided,
            "bonferroni_significant": bool(p_one_sided < ALPHA_BON),
            "verdict": (
                "EXCESS-over-chance (Bonferroni)" if p_one_sided < ALPHA_BON
                else "chance-consistent"
            ),
        }

    # --- descriptive auxiliaries D1 ---
    sum_vc = int(vc.sum())
    sum_pos = int(POS.sum())  # 1..114
    diff = sum_pos - sum_vc

    def factorize(n):
        f, d = {}, 2
        while d * d <= n:
            while n % d == 0:
                f[d] = f.get(d, 0) + 1
                n //= d
            d += 1
        if n > 1:
            f[n] = f.get(n, 0) + 1
        return {str(k): v for k, v in f.items()}

    d1 = {
        "sum_verse_counts": sum_vc,  # expect 6236
        "sum_positions_1_to_114": sum_pos,  # expect 6555
        "difference_pos_minus_vc": diff,  # 319
        "factor_6236": factorize(6236),
        "factor_6555": factorize(6555),
        "factor_319": factorize(319),
        "note": "Sum invariants are fixed integers, not a distribution. Any relation among them is post-hoc; reported, never promoted (MW-7).",
    }

    # --- D2 position-letter name coincidences (descriptive, MW-7 capped) ---
    d2 = {
        "Q50_Qaf": "Q 50 is Sūrat Qāf; opens with the single letter qāf (abjad 100). Position 50 != 100; no verse-count link (Q 50 has 45 verses). Anecdote only.",
        "Q68_Nun": "Q 68 al-Qalam opens with nūn (abjad 50); position 68 != 50. Anecdote only.",
        "Q42_HM_ASQ": "Q 42 al-Shūrā opens ḤM ʿSQ (contains qāf); position 42, 53 verses. No arithmetic link.",
        "note": "Name/letter coincidences cannot be shuffle-tested; capped at single-test alpha, never promoted.",
    }

    # --- D3 running-sum claim (descriptive) ---
    # Does any cumulative running verse-count from position 1 equal a position index?
    cum = np.cumsum(vc)
    # trivially cum grows fast (>=7 at pos1, 293 at pos2...), never re-equals small N after pos1.
    d3 = {
        "cumulative_at_pos1": int(cum[0]),
        "cumulative_at_pos2": int(cum[1]),
        "running_sum_equals_position_hits": [
            int(i + 1) for i in range(114) if cum[i] == (i + 1)
        ],
        "note": "Running cumulative verse-count equals position only where it cannot meaningfully (pos 1: 7 != 1). No clean instance; descriptive only.",
    }

    n_excess = sum(1 for c in cells.values() if c["bonferroni_significant"])

    result = {
        "id": "H-NEW-2090",
        "prereg_sha256": actual_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": BONF_K,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "Hafs-Kufan verse-counts; canonical order 1..114; whole-verse unit; shuffle-assignment null",
        "cell7_grid": {"a": list(GRID_A), "b": list(GRID_B), "observed_total_grid_hits": obs_cell7_total},
        "cells": cells,
        "n_cells_excess_over_chance_bonferroni": n_excess,
        "descriptive_D1_sums": d1,
        "descriptive_D2_position_letter": d2,
        "descriptive_D3_running_sum": d3,
        "verdict": (
            "NULL — surah-position/verse-count arithmetic coincidences are chance-consistent"
            if n_excess == 0
            else f"NON-NULL — {n_excess} cell(s) exceed chance at Bonferroni alpha"
        ),
    }

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"prereg SHA OK: {actual_sha}")
    print(f"Σ verse-counts = {sum_vc} (expect 6236) | Σ(1..114) = {sum_pos} | diff = {diff}")
    print("--- cells (observed vs null mean | p_excess | verdict) ---")
    for k, c in cells.items():
        print(
            f"  {k:22s} obs={c['observed_count']:3d}  null_mean={c['null_mean']:6.3f}"
            f"  null_max={c['null_max']:3d}  p={c['p_one_sided_excess']:.4f}  {c['verdict']}"
        )
    print(f"Cell-7 grid total exact hits (pooled): {obs_cell7_total}")
    print(f"Cells exceeding chance (Bonferroni): {n_excess}/{BONF_K}")
    print(f"VERDICT: {result['verdict']}")
    print(f"Wrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
