#!/usr/bin/env python3
"""
H-NEW-213 — Dominant repetition unit per surah

For each of 114 surahs, find the longest word-level n-gram (n in 1..12)
that repeats >=3 times within the surah. Report MaxN, the top n-gram at
that length, and integrate with H-NEW-195 length-residual entropy.

Seed: 20260419 (no stochastic component in primary test; declared for audit).
Rules tuple: see prereg.
"""

from __future__ import annotations

import csv
import json
import math
import os
import random
import re
import sys
from collections import Counter
from pathlib import Path

RNG_SEED = 20260419
random.seed(RNG_SEED)

ROOT = Path("/Users/grey/Downloads/quran")
TEXT_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"
H195_CSV = ROOT / "findings/phase-b-hypotheses/csv/h-new-195-per-surah.csv"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-213.json"
OUT_CSV = ROOT / "findings/phase-b-hypotheses/csv/h-new-213-per-surah.csv"

MIN_COUNT = 3
N_RANGE = range(1, 13)

# Quranic pause marks and ornaments to strip before tokenization.
PAUSE_CHARS = "ۛۖۗۚۙۜ۞ۢ۬ـ"
# Strip any non-Arabic-letter (we keep U+0621..U+064A plus hamza variants
# that appear in no-tashkeel form, and alef-with-hamza etc).
ARABIC_LETTERS_RE = re.compile(r"[\u0621-\u064A]+")


def normalize_verse(text: str) -> list[str]:
    # Remove pause marks
    cleaned = "".join(c for c in text if c not in PAUSE_CHARS)
    # Extract runs of Arabic letters as tokens
    tokens = ARABIC_LETTERS_RE.findall(cleaned)
    return tokens


def dominant_repetition_unit(tokens: list[str], min_count: int, n_max: int):
    """Return (MaxN, top_ngram_tuple, count, all_max_ngrams, highest_count_refrain).

    - MaxN: maximum n such that some n-gram has count >= min_count (primary metric).
    - top_ngram: the highest-count n-gram AT that max length.
    - all_max_ngrams: top-5 qualifying n-grams at MaxN.
    - highest_count_refrain: across n in 2..n_max, the n-gram with the highest
      count (ties → longer n wins, then lexicographic). This surfaces classical
      refrains like Q55 fa-bi-ayyi ālāʾi rabbikumā tukaḏḏibān (4-gram x31)
      even when a longer n-gram at count=3 dominates MaxN.
    """
    max_n = 0
    top_ngram = None
    top_count = 0
    all_top_at_maxn = []
    best_refrain = None  # (ngram, count, n)
    for n in range(1, n_max + 1):
        if len(tokens) < n:
            break
        counts: Counter = Counter()
        for i in range(len(tokens) - n + 1):
            counts[tuple(tokens[i : i + n])] += 1
        qualifying = [(ng, c) for ng, c in counts.items() if c >= min_count]
        if qualifying:
            max_n = n
            qualifying.sort(key=lambda x: (-x[1], x[0]))
            top_ngram, top_count = qualifying[0]
            all_top_at_maxn = qualifying[:5]
            # Track highest-count refrain across n>=2 (exclude unigrams)
            if n >= 2:
                cand_ng, cand_c = qualifying[0]
                if (
                    best_refrain is None
                    or cand_c > best_refrain[1]
                    or (cand_c == best_refrain[1] and n > best_refrain[2])
                ):
                    best_refrain = (cand_ng, cand_c, n)
    return max_n, top_ngram, top_count, all_top_at_maxn, best_refrain


def binomial_tail_p(k: int, n: int, p: float) -> float:
    """Upper-tail exact binomial: P(X >= k | n, p)."""
    from math import comb

    total = 0.0
    for i in range(k, n + 1):
        total += comb(n, i) * (p**i) * ((1 - p) ** (n - i))
    return total


def mannwhitney_u_twosided(x: list[float], y: list[float]):
    """Two-sided Mann-Whitney U (normal approx, tie-corrected)."""
    from math import sqrt

    nx, ny = len(x), len(y)
    if nx == 0 or ny == 0:
        return float("nan"), float("nan"), float("nan")
    combined = [(v, 0) for v in x] + [(v, 1) for v in y]
    combined.sort(key=lambda t: t[0])
    # Assign ranks with tie-averaging
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1.0  # 1-based
        for k in range(i, j + 1):
            ranks[k] = avg_rank
        i = j + 1
    rank_sum_x = sum(r for r, (_, g) in zip(ranks, combined) if g == 0)
    U1 = rank_sum_x - nx * (nx + 1) / 2.0
    U2 = nx * ny - U1
    U = min(U1, U2)
    mu = nx * ny / 2.0
    # tie correction
    tie_term = 0.0
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        t = j - i + 1
        if t > 1:
            tie_term += t**3 - t
        i = j + 1
    N = nx + ny
    sigma2 = (nx * ny / 12.0) * ((N + 1) - tie_term / (N * (N - 1)))
    sigma = sqrt(sigma2) if sigma2 > 0 else float("nan")
    if sigma == 0 or math.isnan(sigma):
        return U, float("nan"), float("nan")
    z = (U1 - mu) / sigma  # signed from x-perspective
    # two-sided p via normal approx
    from math import erf

    p_two = 2.0 * (1.0 - 0.5 * (1.0 + erf(abs(z) / math.sqrt(2))))
    return U1, z, p_two


def spearman_rho(x: list[float], y: list[float]):
    from math import sqrt

    n = len(x)
    if n != len(y) or n < 3:
        return float("nan"), float("nan")

    def rankify(v):
        order = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r

    rx, ry = rankify(x), rankify(y)
    mx, my = sum(rx) / n, sum(ry) / n
    sxy = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    sxx = sum((rx[i] - mx) ** 2 for i in range(n))
    syy = sum((ry[i] - my) ** 2 for i in range(n))
    if sxx == 0 or syy == 0:
        return float("nan"), float("nan")
    rho = sxy / sqrt(sxx * syy)
    # t-approx p two-sided
    if abs(rho) >= 1.0:
        return rho, 0.0
    t = rho * sqrt((n - 2) / (1 - rho * rho))
    # two-sided p via Student-t approximation (use large-n normal)
    from math import erf

    p = 2.0 * (1.0 - 0.5 * (1.0 + erf(abs(t) / math.sqrt(2))))
    return rho, p


def main():
    with open(TEXT_JSON, "r", encoding="utf-8") as f:
        surahs = json.load(f)
    assert len(surahs) == 114

    # Known reference sets
    OATH_CLUSTER = {
        37, 51, 52, 53, 68, 74, 75, 77, 79, 80, 81, 84, 85, 86, 89, 90, 91, 92, 93, 95, 100, 103
    }  # per H-NEW-85-style set (task-stated 21-oath list approx)
    SHORT_CREEDAL = {108, 109, 112, 113, 114}
    MUSABBIHAT = {17, 57, 59, 61, 62, 64, 87}

    results = []
    for s in surahs:
        sid = s["id"]
        name = s["name"]
        translit = s.get("transliteration", "")
        stype = s.get("type", "")
        verse_texts = [v["text"] for v in s["verses"]]
        tokens: list[str] = []
        for vt in verse_texts:
            tokens.extend(normalize_verse(vt))
        L = len(tokens)
        if L == 0:
            results.append(
                {
                    "surah_id": sid,
                    "name": name,
                    "transliteration": translit,
                    "type": stype,
                    "length_tokens": 0,
                    "MaxN": 0,
                    "top_ngram": "",
                    "top_count": 0,
                    "top5_at_maxn": [],
                }
            )
            continue
        max_n, top_ng, top_c, top5, best_ref = dominant_repetition_unit(tokens, MIN_COUNT, 12)
        results.append(
            {
                "surah_id": sid,
                "name": name,
                "transliteration": translit,
                "type": stype,
                "length_tokens": L,
                "MaxN": max_n,
                "top_ngram": " ".join(top_ng) if top_ng else "",
                "top_count": top_c,
                "top5_at_maxn": [
                    {"ngram": " ".join(ng), "count": c} for ng, c in top5
                ],
                "highest_count_refrain": (
                    {
                        "ngram": " ".join(best_ref[0]),
                        "count": best_ref[1],
                        "n": best_ref[2],
                    }
                    if best_ref
                    else None
                ),
            }
        )

    # H1 primary test: fraction MaxN >= 3
    n_refrain = sum(1 for r in results if r["MaxN"] >= 3)
    n_total = len(results)
    frac = n_refrain / n_total
    p_binom = binomial_tail_p(n_refrain, n_total, 0.10)

    # Load H-NEW-195 residuals
    h195_residuals = {}
    if H195_CSV.exists():
        with open(H195_CSV, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # Find id column and residual column from headers
            fieldnames = reader.fieldnames or []
            id_col = None
            for candidate in ("sid", "surah", "surah_id", "id"):
                if candidate in fieldnames:
                    id_col = candidate
                    break
            resid_col = None
            for col in fieldnames:
                if "residual" in col.lower():
                    resid_col = col
                    break
            for row in reader:
                if id_col is None or resid_col is None:
                    continue
                try:
                    sid = int(row[id_col])
                    h195_residuals[sid] = float(row[resid_col])
                except (TypeError, ValueError):
                    continue
    # H2 secondary: residual(refrain) vs residual(non-refrain)
    refrain_res = [h195_residuals[r["surah_id"]] for r in results if r["MaxN"] >= 3 and r["surah_id"] in h195_residuals]
    nonrefrain_res = [h195_residuals[r["surah_id"]] for r in results if r["MaxN"] < 3 and r["surah_id"] in h195_residuals]
    if refrain_res and nonrefrain_res:
        U1, z, p_mwu = mannwhitney_u_twosided(refrain_res, nonrefrain_res)
        median_refrain = sorted(refrain_res)[len(refrain_res) // 2]
        median_nonref = sorted(nonrefrain_res)[len(nonrefrain_res) // 2]
    else:
        U1, z, p_mwu = float("nan"), float("nan"), float("nan")
        median_refrain = median_nonref = float("nan")

    # Spearman rho between MaxN and H-NEW-195 residual
    pair_maxn, pair_res = [], []
    for r in results:
        if r["surah_id"] in h195_residuals:
            pair_maxn.append(r["MaxN"])
            pair_res.append(h195_residuals[r["surah_id"]])
    rho, p_rho = spearman_rho(pair_maxn, pair_res) if pair_maxn else (float("nan"), float("nan"))

    # Cross-reference overlaps
    refrain_ids = {r["surah_id"] for r in results if r["MaxN"] >= 3}
    overlap_oath = sorted(refrain_ids & OATH_CLUSTER)
    overlap_creedal = sorted(refrain_ids & SHORT_CREEDAL)
    overlap_musabbihat = sorted(refrain_ids & MUSABBIHAT)

    # Distribution of MaxN
    maxn_dist = Counter(r["MaxN"] for r in results)

    # Top 20 surahs by MaxN (then by count)
    ranked = sorted(results, key=lambda r: (-r["MaxN"], -r["top_count"], r["surah_id"]))
    top20 = [
        {
            "surah_id": r["surah_id"],
            "name": r["name"],
            "transliteration": r["transliteration"],
            "MaxN": r["MaxN"],
            "top_ngram": r["top_ngram"],
            "top_count": r["top_count"],
            "length_tokens": r["length_tokens"],
            "highest_count_refrain": r["highest_count_refrain"],
        }
        for r in ranked[:20]
    ]

    # Top 20 by highest-count refrain (showcase classical refrain surahs)
    by_count = sorted(
        (r for r in results if r["highest_count_refrain"]),
        key=lambda r: (-r["highest_count_refrain"]["count"], -r["highest_count_refrain"]["n"], r["surah_id"]),
    )
    top20_by_count = [
        {
            "surah_id": r["surah_id"],
            "transliteration": r["transliteration"],
            "refrain": r["highest_count_refrain"],
            "MaxN": r["MaxN"],
            "length_tokens": r["length_tokens"],
        }
        for r in by_count[:20]
    ]

    summary = {
        "id": "H-NEW-213",
        "seed": RNG_SEED,
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "rules_tuple": "(Hafs-Kūfan; no-tashkeel; pause-marks stripped; word = whitespace-split Arabic-letter runs; min_count=3; n=1..12)",
        "n_surahs": n_total,
        "primary_H1": {
            "n_refrain_maxN_ge_3": n_refrain,
            "n_total": n_total,
            "fraction": frac,
            "H0_p": 0.10,
            "p_binomial_upper": p_binom,
            "alpha_bon": 0.025,
            "verdict": "PASS" if p_binom < 0.025 else "FAIL",
        },
        "secondary_H2_vs_H195": {
            "n_refrain_with_residual": len(refrain_res),
            "n_nonrefrain_with_residual": len(nonrefrain_res),
            "median_residual_refrain": median_refrain,
            "median_residual_nonrefrain": median_nonref,
            "MWU_U1": U1,
            "MWU_z": z,
            "MWU_p_two_sided": p_mwu,
            "alpha_bon": 0.025,
            "direction_predicted": "refrain_lower_residual",
            "direction_observed": (
                "refrain_lower_residual"
                if not math.isnan(median_refrain) and median_refrain < median_nonref
                else "refrain_higher_residual"
                if not math.isnan(median_refrain)
                else "NA"
            ),
            "verdict": (
                "PASS"
                if (not math.isnan(p_mwu))
                and p_mwu < 0.025
                and (median_refrain < median_nonref)
                else "FAIL"
            ),
        },
        "spearman_MaxN_vs_H195_residual": {
            "n": len(pair_maxn),
            "rho": rho,
            "p_two_sided": p_rho,
        },
        "MaxN_distribution": dict(sorted(maxn_dist.items())),
        "top20_by_MaxN": top20,
        "top20_by_highest_count_refrain": top20_by_count,
        "cross_reference_overlaps": {
            "refrain_set_size": len(refrain_ids),
            "overlap_with_oath_cluster": overlap_oath,
            "overlap_with_short_creedal": overlap_creedal,
            "overlap_with_musabbihat": overlap_musabbihat,
        },
        "H_NEW_191_cluster_4_note": (
            "H-NEW-191 'cluster-4 refrain-stylistic' does not exist as a saved "
            "finding in this project (confirmed by grep; h-new-196-oath-cluster "
            "prereg explicitly states H-NEW-191 'does not exist in this project "
            "yet'). H-NEW-213 therefore operationalizes the refrain-stylistic "
            "axis directly via MaxN>=3, rather than reverse-inferring membership "
            "from a non-existent cluster assignment. The set here (refrain_ids) "
            "is the empirical refrain-structured set."
        ),
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    # Full per-surah CSV
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "surah_id",
                "name",
                "transliteration",
                "type",
                "length_tokens",
                "MaxN",
                "top_ngram",
                "top_count",
                "h195_residual",
                "highest_count_refrain_ngram",
                "highest_count_refrain_count",
                "highest_count_refrain_n",
            ]
        )
        for r in results:
            hcr = r["highest_count_refrain"]
            w.writerow(
                [
                    r["surah_id"],
                    r["name"],
                    r["transliteration"],
                    r["type"],
                    r["length_tokens"],
                    r["MaxN"],
                    r["top_ngram"],
                    r["top_count"],
                    h195_residuals.get(r["surah_id"], ""),
                    hcr["ngram"] if hcr else "",
                    hcr["count"] if hcr else "",
                    hcr["n"] if hcr else "",
                ]
            )

    print(f"H-NEW-213 complete.")
    print(f"  MaxN>=3 count: {n_refrain}/{n_total} = {frac:.3f}")
    print(f"  H1 p (binomial, H0=0.10): {p_binom:.4g} -> {summary['primary_H1']['verdict']}")
    print(f"  H2 MWU p (residual refrain vs non): {p_mwu:.4g} -> {summary['secondary_H2_vs_H195']['verdict']}")
    print(f"  Spearman MaxN vs residual: rho={rho:.3f} p={p_rho:.4g}")
    print(f"  MaxN distribution: {dict(sorted(maxn_dist.items()))}")
    print(f"  Top 5: {[(t['surah_id'], t['MaxN'], t['top_count']) for t in top20[:5]]}")
    print(f"  Outputs: {OUT_JSON} ; {OUT_CSV}")


if __name__ == "__main__":
    main()
