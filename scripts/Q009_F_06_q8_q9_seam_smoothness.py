#!/usr/bin/env python3
"""
Q009-F-06 — Q 8 → Q 9 seam smoothness from H-NEW-720.

Direction-LOCKED before observation:
  Q 8 → Q 9 rank-smooth ≤ 34 of 113 (top 30% smoothest seams)
  ↔ al-Biqāʿī thematic-couplet VINDICATED.

Seed: 20260509 (no permutation needed; rank-test from precomputed artifact).
"""

import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q009-al-tawba/Q009-F-06-q8-q9-seam-smoothness-prereg.md"
EXPECTED_SHA = "6fd9d94553ada755192702f89e4939f635403853225edf35b10904a78e53f88c"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q009-al-tawba/csv/Q009-F-06-q8-q9-seam-smoothness.json"
SOURCE = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json"


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH\n  expected: {EXPECTED_SHA}\n  actual:   {actual}\n"
        )
        sys.exit(2)


def main():
    verify_prereg()
    with open(SOURCE) as f:
        data = json.load(f)

    pa = data["per_adjacency"]
    sorted_smooth = sorted(pa, key=lambda e: e["delta_raw"])

    q8_q9 = next(e for e in pa if e["s"] == 8)
    q9_q10 = next(e for e in pa if e["s"] == 9)

    rank_smooth_q8q9 = next(i + 1 for i, e in enumerate(sorted_smooth) if e["s"] == 8)
    rank_smooth_q9q10 = next(i + 1 for i, e in enumerate(sorted_smooth) if e["s"] == 9)

    n = len(pa)
    threshold = 34  # top 30% smoothest
    in_top30 = rank_smooth_q8q9 <= threshold

    # Bottom-cheap / top-expensive context
    smoothest_5 = [(e["s"], e["pair"], e["delta_raw"]) for e in sorted_smooth[:5]]
    expensive_5 = [(e["s"], e["pair"], e["delta_raw"]) for e in sorted_smooth[-5:][::-1]]

    if in_top30:
        verdict = "VINDICATED"
    elif rank_smooth_q8q9 <= 80:
        verdict = "NULL"
    else:
        verdict = "FALSIFIED"

    result = {
        "finding_id": "Q009-F-06",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260509,
        "source_artifact": SOURCE,
        "n_adjacencies": n,
        "q8_q9": {
            "pair": q8_q9["pair"],
            "delta_raw": q8_q9["delta_raw"],
            "fraction_residual": q8_q9["fraction_residual"],
            "rank_smooth": rank_smooth_q8q9,
            "rank_pct": round(100 * rank_smooth_q8q9 / n, 2),
        },
        "q9_q10_context": {
            "pair": q9_q10["pair"],
            "delta_raw": q9_q10["delta_raw"],
            "fraction_residual": q9_q10["fraction_residual"],
            "rank_smooth": rank_smooth_q9q10,
            "rank_pct": round(100 * rank_smooth_q9q10 / n, 2),
        },
        "smoothest_5_seams": smoothest_5,
        "most_expensive_5_seams": expensive_5,
        "pre_registered_threshold": {
            "vindicated_if_rank_smooth_q8q9": "<= 34",
            "null_band": "35-80",
            "falsified_if_rank_smooth_q8q9": ">= 81",
        },
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(json.dumps({k: result[k] for k in ("finding_id", "verdict", "q8_q9", "q9_q10_context")}, indent=2, ensure_ascii=False))
    print(f"\nResult written to {OUT_PATH}")


if __name__ == "__main__":
    main()
