"""H-NEW-46 — Muqaṭṭaʿāt vs Surah Length.

Pre-reg: findings/phase-b-hypotheses/h-new-46-muqattaat-vs-surah-length-prereg.md

Question: do muqaṭṭaʿāt-opened surahs concentrate in LONG surahs (verse-count)
above what uniform random 29-from-114 selection would predict?

Seed: 20260416
Bonferroni k = 4, α_bon = 0.0125
N_PERM = 100,000

4 test cells:
  1. Mean verse-count enrichment (one-sided upper; eyeball-noticed)
  2. Median verse-count enrichment (two-sided)
  3. Top-29 representation (one-sided upper)
  4. Bottom-29 suppression (one-sided lower)

+ MW-5 positive control: 29-longest plant should give cell 1 p < 1e-4.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import statistics
import sys
import time
from typing import List, Tuple

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))

from tools.loader import load_quran  # noqa: E402

SEED = 20260416
N_PERM = 100_000
BON_K = 4
ALPHA_BON = 0.05 / BON_K
N_SURAHS = 114
K = 29  # muqaṭṭaʿāt-opened count

# Locked observed set (from pre-reg)
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
              36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
assert len(MUQ_SURAHS) == 29


def load_verse_counts() -> List[int]:
    """Return list of 114 verse counts indexed by surah_id - 1."""
    surahs = load_quran("no-tashkeel")
    assert len(surahs) == N_SURAHS
    counts = [0] * N_SURAHS
    for s in surahs:
        # Use literal verse list length, not declared total_verses, for honesty.
        counts[s.id - 1] = len(s.verses)
    # Sanity: 286 (Q 2) longest under hafs-kufan.
    assert counts[1] == 286, f"expected Q 2 to have 286 verses, got {counts[1]}"
    return counts


def cell_stats(S: set, verse_counts: List[int],
               top29_set: set, bot29_set: set) -> dict:
    """Compute the 4 cell stats for a sample S of 29 surah ids (1..114)."""
    lens = [verse_counts[i - 1] for i in S]
    return {
        "mean_len": statistics.fmean(lens),
        "median_len": statistics.median(lens),
        "top29_count": sum(1 for i in S if i in top29_set),
        "bot29_count": sum(1 for i in S if i in bot29_set),
    }


def run_null(rng: random.Random, n_perm: int, verse_counts: List[int],
             top29_set: set, bot29_set: set) -> Tuple[List[dict], float]:
    t0 = time.time()
    out = []
    all_surahs = list(range(1, N_SURAHS + 1))
    for i in range(n_perm):
        S = set(rng.sample(all_surahs, K))
        out.append(cell_stats(S, verse_counts, top29_set, bot29_set))
        if (i + 1) % 20000 == 0:
            print(f"  null {i+1}/{n_perm}  elapsed={time.time()-t0:.0f}s")
    return out, time.time() - t0


def empirical_p(obs: float, null_list: List[float],
                direction: str) -> dict:
    """direction in {'upper','lower','two_sided'}"""
    n = len(null_list)
    as_or_more_upper = sum(1 for x in null_list if x >= obs) + 1
    as_or_more_lower = sum(1 for x in null_list if x <= obs) + 1
    p_upper = as_or_more_upper / (n + 1)
    p_lower = as_or_more_lower / (n + 1)
    mu = sum(null_list) / n
    sd = (sum((x - mu) ** 2 for x in null_list) / n) ** 0.5
    base = {"null_mean": mu, "null_std": sd,
            "p_upper": p_upper, "p_lower": p_lower}
    if direction == "upper":
        base["p"] = p_upper
    elif direction == "lower":
        base["p"] = p_lower
    elif direction == "two_sided":
        base["p"] = 2 * min(p_upper, p_lower)
        if base["p"] > 1.0:
            base["p"] = 1.0
    else:
        raise ValueError(direction)
    return base


def mw5_positive_control(verse_counts: List[int], top29_set: set,
                         bot29_set: set, rng: random.Random,
                         n_perm: int = 10_000) -> dict:
    """Plant the 29 LONGEST surahs as the 'fake muqaṭṭaʿāt set'. Cell 1
    (mean) should reject at p < 1e-4 immediately."""
    planted = set(top29_set)
    obs = cell_stats(planted, verse_counts, top29_set, bot29_set)
    all_surahs = list(range(1, N_SURAHS + 1))
    null_means = []
    for _ in range(n_perm):
        S = set(rng.sample(all_surahs, K))
        lens = [verse_counts[i - 1] for i in S]
        null_means.append(sum(lens) / len(lens))
    p = (sum(1 for x in null_means if x >= obs["mean_len"]) + 1) / (n_perm + 1)
    return {"planted_mean_len": obs["mean_len"],
            "p_positive_control_cell1": p,
            "detect_at_lt_1e_minus_4": p < 1e-4}


def main():
    print("[H-NEW-46] loading verse counts ...")
    verse_counts = load_verse_counts()
    sorted_idx_by_len = sorted(range(1, N_SURAHS + 1),
                               key=lambda i: (-verse_counts[i - 1], i))
    top29_set = set(sorted_idx_by_len[:29])
    # bottom-29 chosen ascending; ties broken by surah-id ascending so the
    # set is deterministic. Worth printing tie-band size for transparency.
    sorted_idx_asc = sorted(range(1, N_SURAHS + 1),
                            key=lambda i: (verse_counts[i - 1], i))
    bot29_set = set(sorted_idx_asc[:29])

    print(f"  top-29 longest contains {sum(1 for i in MUQ_SURAHS if i in top29_set)} muq")
    print(f"  bot-29 shortest contains {sum(1 for i in MUQ_SURAHS if i in bot29_set)} muq")

    print("[H-NEW-46] observed ...")
    obs = cell_stats(MUQ_SURAHS, verse_counts, top29_set, bot29_set)
    print(f"  observed: {obs}")

    print("[H-NEW-46] MW-5 positive control (cell 1) ...")
    rng_pc = random.Random(SEED + 1)
    pc = mw5_positive_control(verse_counts, top29_set, bot29_set, rng_pc, n_perm=10_000)
    print(f"  positive control: {pc}")
    if not pc["detect_at_lt_1e_minus_4"]:
        print("  WARNING: positive control did NOT clear p<1e-4 — pipeline suspect")

    print(f"[H-NEW-46] null n_perm={N_PERM} ...")
    rng = random.Random(SEED)
    nulls, runtime = run_null(rng, N_PERM, verse_counts, top29_set, bot29_set)

    null_mean = [n["mean_len"] for n in nulls]
    null_median = [n["median_len"] for n in nulls]
    null_top = [n["top29_count"] for n in nulls]
    null_bot = [n["bot29_count"] for n in nulls]

    cell1 = empirical_p(obs["mean_len"], null_mean, "upper")
    cell2 = empirical_p(obs["median_len"], null_median, "two_sided")
    cell3 = empirical_p(obs["top29_count"], null_top, "upper")
    cell4 = empirical_p(obs["bot29_count"], null_bot, "lower")

    cells = {
        "cell1_mean_one_sided_upper": cell1,
        "cell2_median_two_sided": cell2,
        "cell3_top29_one_sided_upper": cell3,
        "cell4_bot29_one_sided_lower": cell4,
    }
    sig = {k: (v["p"] < ALPHA_BON) for k, v in cells.items()}
    n_sig = sum(sig.values())

    if not pc["detect_at_lt_1e_minus_4"]:
        verdict = "NULL-BROKEN"
    elif n_sig == 0:
        verdict = "NULL"
    elif n_sig == 1:
        verdict = "EXPLORATORY"
    elif n_sig in (2, 3):
        verdict = "PARTIAL-PASS"
    elif n_sig == 4:
        verdict = "STRONG-PASS"
    else:
        verdict = "UNDEFINED"

    preg_path = os.path.join(REPO, "findings/phase-b-hypotheses/"
                             "h-new-46-muqattaat-vs-surah-length-prereg.md")
    with open(preg_path, "rb") as f:
        preg_sha = hashlib.sha256(f.read()).hexdigest()

    out = {
        "hypothesis_id": "H-NEW-46",
        "run_date": "2026-04-15",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_family": "2026-04-16-Wave-Muqattaat-Extended",
        "bonferroni_k": BON_K,
        "alpha_bon": ALPHA_BON,
        "prereg_sha256": preg_sha,
        "muq_surahs_locked": sorted(MUQ_SURAHS),
        "verse_counts": verse_counts,
        "top29_longest": sorted(top29_set),
        "bot29_shortest": sorted(bot29_set),
        "observed": obs,
        "positive_control": pc,
        "cells": cells,
        "significant_at_alpha_bon": sig,
        "n_significant": n_sig,
        "verdict": verdict,
        "runtime_seconds": runtime,
    }

    out_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-46.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[H-NEW-46] wrote {out_path}")
    print(f"[H-NEW-46] VERDICT: {verdict}  (n_sig={n_sig}/4)")
    for k, r in cells.items():
        print(f"  {k}: p={r['p']:.6f}  null_mean={r['null_mean']:.3f}  null_std={r['null_std']:.3f}  sig={sig[k]}")


if __name__ == "__main__":
    main()
