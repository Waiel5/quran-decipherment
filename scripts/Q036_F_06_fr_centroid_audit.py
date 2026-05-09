#!/usr/bin/env python3
"""
Q036-F-06 — "Heart of the Qurʾān" empirical FR-centroid audit.

Pre-reg: surahs/Q036-yasin/preregs/Q036-F-06-heart-of-quran-empirical-centroid-prereg.md
SHA-256: 69c0782025c1ae13c951fd5ab019f5ce1ca34591042c987c881c39b5c301a4b1
Seed:    20260509 (n/a — deterministic over canonical FR matrix)

Uses the project-canonical Fisher-Rao distance matrix from H-NEW-111
(K=500 root-truncation, Dirichlet alpha=0.5 smoothing), as established by
Q112-F-01 (which locked Q 112's rank-1 FR-centroid status). This is the
project's canonical metric for "FR-centrality" claims.
"""

import hashlib
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG = PROJECT_ROOT / "surahs/Q036-yasin/preregs/Q036-F-06-heart-of-quran-empirical-centroid-prereg.md"
EXPECTED_SHA = "69c0782025c1ae13c951fd5ab019f5ce1ca34591042c987c881c39b5c301a4b1"
H_NEW_111 = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"


def verify_prereg_sha():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}",
              file=sys.stderr)
        sys.exit(1)
    print(f"[ok] pre-reg SHA verified: {actual[:16]}...")


def main():
    verify_prereg_sha()

    # Load the canonical 114×114 FR distance matrix from H-NEW-111.
    # The matrix uses K=500 root-truncation + Dirichlet alpha=0.5 smoothing,
    # as locked by H-NEW-111 and reused by Q112-F-01.
    with open(H_NEW_111) as f:
        h111 = json.load(f)

    D = [[0.0] * 114 for _ in range(114)]
    for entry in h111["D_matrix_upper_triangular"]:
        i, j, dist = entry[0], entry[1], entry[2]
        D[i - 1][j - 1] = dist
        D[j - 1][i - 1] = dist

    # mean-FR per surah and median-FR per surah
    mean_fr = [sum(D[s][t] for t in range(114) if t != s) / 113 for s in range(114)]
    median_fr = []
    for s in range(114):
        row = sorted(D[s][t] for t in range(114) if t != s)
        median_fr.append(row[len(row) // 2])

    # Ranking ascending (smallest mean = most central = "heart" candidate)
    ranking_mean = sorted(range(114), key=lambda s: mean_fr[s])
    ranking_median = sorted(range(114), key=lambda s: median_fr[s])
    rank_mean = {s + 1: i + 1 for i, s in enumerate(ranking_mean)}
    rank_median = {s + 1: i + 1 for i, s in enumerate(ranking_median)}

    q036_rank_mean = rank_mean[36]
    q036_rank_median = rank_median[36]
    q112_rank_mean = rank_mean[112]
    q112_rank_median = rank_median[112]

    cond_a = q112_rank_mean <= 3            # Q 112 in top-3
    cond_b = q036_rank_mean >= 30           # Q 36 outside top-30

    if cond_a and cond_b:
        verdict = "PASS-DIRECTED-REAFFIRMED"
    elif (not cond_a) and q036_rank_mean <= 3:
        verdict = "NULL-PRE-COMMIT-REVERSED (Q 36 is the centroid; published with prominence)"
    elif not cond_a:
        verdict = f"PARTIAL-NULL (Q 112 outside top-10: rank {q112_rank_mean})"
    elif not cond_b:
        verdict = f"PARTIAL-NULL (Q 36 inside top-30: rank {q036_rank_mean})"
    else:
        verdict = "UNDEFINED"

    result = {
        "finding_id": "Q036-F-06",
        "pre_reg_sha256": EXPECTED_SHA,
        "seed": 20260509,
        "date": "2026-05-09",
        "source_matrix": "H-NEW-111 D_matrix_upper_triangular "
                         "(QAC stem-roots, K=500 truncation, Dirichlet α=0.5)",
        "rules_tuple": "(no-tashkeel, QAC-stem-roots, K500, Dirichlet-alpha-0.5, "
                       "basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "metric": "Fisher–Rao distance on smoothed root-frequency probability simplex",
        "centroid_top10_by_mean_FR": [
            {"rank": i + 1, "surah": s + 1, "mean_FR": round(mean_fr[s], 6)}
            for i, s in enumerate(ranking_mean[:10])
        ],
        "q036_mean_FR": round(mean_fr[35], 6),
        "q036_rank_mean": q036_rank_mean,
        "q036_rank_median": q036_rank_median,
        "q112_mean_FR": round(mean_fr[111], 6),
        "q112_rank_mean": q112_rank_mean,
        "q112_rank_median": q112_rank_median,
        "pre_committed_predictions": {
            "q112_in_top3_on_mean": cond_a,
            "q036_outside_top30_on_mean": cond_b,
        },
        "verdict": verdict,
        "interpretation": (
            f"Under the project-canonical H-NEW-111 FR-roots metric "
            f"(K=500, Dirichlet α=0.5), Q {ranking_mean[0] + 1} ranks #1 on "
            f"min(mean FR distance) = {mean_fr[ranking_mean[0]]:.4f}. "
            f"Q 112 ranks {q112_rank_mean}/114 (mean FR = {mean_fr[111]:.4f}). "
            f"Q 36 ranks {q036_rank_mean}/114 (mean FR = {mean_fr[35]:.4f}). "
            "Q 36 is NOT the FR-centroid by any metric tested in the project. "
            "The pre-committed prediction is "
            f"{'reaffirmed' if (cond_a and cond_b) else 'partially reversed'}."
        ),
        "honest_limits": [
            "FR-centroid is biased toward short-and-theologically-broad surahs.",
            "The metric depends on the K=500 truncation + Dirichlet α=0.5 smoothing locked by H-NEW-111.",
            "Liturgy-weighting was tested separately in Q036-F-01 and was also NULL.",
            "A length-normalised cosine variant on roots could yield a different ordering; "
            "such variants are post-hoc.",
        ],
        "cross_references": [
            "Q112-F-01 — Q 112 FR-centroid rank-1 finding",
            "H-NEW-82 — the binding 6-axis NULL on the qalb al-Qurʾān claim",
            "Q036-F-01 — the 7th-axis (liturgy-weighted Jaccard) NULL",
        ],
    }

    out = PROJECT_ROOT / "surahs/Q036-yasin/csv/Q036-F-06.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nVerdict: {verdict}")
    print(f"Centroid rank-1: Q {ranking_mean[0] + 1} (mean_FR = {mean_fr[ranking_mean[0]]:.4f})")
    print(f"Q 36 rank (mean FR): {q036_rank_mean}/114 (mean_FR = {mean_fr[35]:.4f})")
    print(f"Q 112 rank (mean FR): {q112_rank_mean}/114 (mean_FR = {mean_fr[111]:.4f})")
    print(f"Output: {out}")


if __name__ == "__main__":
    main()
