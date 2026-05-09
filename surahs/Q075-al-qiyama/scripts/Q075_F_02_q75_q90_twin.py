#!/usr/bin/env python3
"""
Q075-F-02 — Q 75 ↔ Q 90 structural-twin pair (bare-*lā uqsimu* corpus exclusivity).

Pre-reg: surahs/Q075-al-qiyama/preregs/Q075-F-02-q75-q90-twin-prereg.md

Author: Waiel Al-Shujaa
Date: 2026-05-09
"""
import json
import re
import hashlib
import sys
from pathlib import Path

PREREG_PATH = Path(__file__).resolve().parent.parent / "preregs" / "Q075-F-02-q75-q90-twin-prereg.md"
PREREG_SHA_EXPECTED = "WILL_BE_FILLED_AT_LOCK"
QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
FR_PATH = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"
OUT_PATH = Path(__file__).resolve().parent.parent / "csv" / "Q075-F-02.json"


def main():
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if PREREG_SHA_EXPECTED != "WILL_BE_FILLED_AT_LOCK" and sha != PREREG_SHA_EXPECTED:
        print(f"FATAL: pre-reg SHA mismatch.", file=sys.stderr)
        sys.exit(1)

    with open(QURAN_PATH) as f:
        qd = json.load(f)
    with open(FR_PATH) as f:
        fr = json.load(f)

    # CELL A: enumerate surahs whose v.1 starts with bare لا أقسم (no fa- prefix)
    bare_la_uqsimu_openers = []
    for s in qd:
        v1 = s["verses"][0]["text"]
        # Strip ornaments
        v1_clean = re.sub(r"[۞\s]+", " ", v1).strip()
        if re.match(r"^لا أقسم\b", v1_clean):
            bare_la_uqsimu_openers.append(s["id"])

    cell_a_predicted = [75, 90]
    cell_a_count_predicted = 2
    cell_a_count_observed = len(bare_la_uqsimu_openers)
    cell_a_match = (sorted(bare_la_uqsimu_openers) == sorted(cell_a_predicted))
    cell_a_pass = cell_a_match and (cell_a_count_observed == cell_a_count_predicted)

    # CELL B: FR pair-distance Q 75 <-> Q 90 vs corpus median
    n = 114
    D = [[0.0] * n for _ in range(n)]
    for entry in fr["D_matrix_upper_triangular"]:
        i, j, d = entry[0], entry[1], entry[2]
        D[i - 1][j - 1] = d
        D[j - 1][i - 1] = d
    pair_distance = D[74][89]  # Q 75 = idx 74, Q 90 = idx 89
    corpus_median = fr["distance_matrix_stats"]["median"]
    corpus_mean = fr["distance_matrix_stats"]["mean"]

    # Compute percentile of this pair-distance among all 6441 pair-distances
    all_pairs = [entry[2] for entry in fr["D_matrix_upper_triangular"]]
    pair_percentile = sum(1 for p in all_pairs if p < pair_distance) / len(all_pairs)

    cell_b_pass = (pair_distance < corpus_median)

    # Q 75 nearest 10 neighbors
    q75_dists = [(s + 1, D[74][s]) for s in range(n) if s != 74]
    q75_dists.sort(key=lambda x: x[1])
    q75_nearest_10 = [{"surah": s, "fr_distance": d} for s, d in q75_dists[:10]]
    q90_rank_for_q75 = next((rank + 1 for rank, (s, _) in enumerate(q75_dists) if s == 90), None)

    # Q 90 nearest 10 neighbors
    q90_dists = [(s + 1, D[89][s]) for s in range(n) if s != 89]
    q90_dists.sort(key=lambda x: x[1])
    q90_nearest_10 = [{"surah": s, "fr_distance": d} for s, d in q90_dists[:10]]
    q75_rank_for_q90 = next((rank + 1 for rank, (s, _) in enumerate(q90_dists) if s == 75), None)

    if cell_a_pass and cell_b_pass:
        verdict = "VINDICATED"
    elif cell_a_pass:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    out = {
        "test_id": "Q075-F-02",
        "title": "Q 75 <-> Q 90 structural-twin pair",
        "prereg_sha256": sha,
        "seed": 20260509,
        "cell_a": {
            "predicted_openers": cell_a_predicted,
            "predicted_count": cell_a_count_predicted,
            "observed_openers": bare_la_uqsimu_openers,
            "observed_count": cell_a_count_observed,
            "exact_match": cell_a_match,
            "pass": cell_a_pass,
        },
        "cell_b": {
            "q75_q90_fr_distance": pair_distance,
            "corpus_mean": corpus_mean,
            "corpus_median": corpus_median,
            "pair_distance_percentile_in_corpus": pair_percentile,
            "below_corpus_median": cell_b_pass,
            "pass": cell_b_pass,
        },
        "auxiliary": {
            "q75_nearest_10": q75_nearest_10,
            "q90_nearest_10": q90_nearest_10,
            "q90_rank_in_q75_neighborhood": q90_rank_for_q75,
            "q75_rank_in_q90_neighborhood": q75_rank_for_q90,
        },
        "verdict": verdict,
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Wrote {OUT_PATH}")
    print(f"Verdict: {verdict}")
    print(f"Cell A: predicted={cell_a_predicted}, observed={bare_la_uqsimu_openers}, pass={cell_a_pass}")
    print(f"Cell B: pair_distance={pair_distance:.4f}, median={corpus_median:.4f}, pass={cell_b_pass}")
    print(f"Q 90 is rank {q90_rank_for_q75} in Q 75's neighborhood")
    print(f"Q 75 is rank {q75_rank_for_q90} in Q 90's neighborhood")


if __name__ == "__main__":
    main()
