#!/usr/bin/env python3
"""
Q112-F-01: Q 112 al-Ikhlāṣ FR-centroid status.

Pre-registered: empirical lock on *thuluth al-Qurʾān* via FR-roots distance.
Pre-reg SHA: 6e4cdfbec48ea9067bfc805077b042ca859e346582b63d3e1d245e7946d2f0f0
Pre-reg path: /Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/Q112-F-01-fr-centroid-prereg.md
Date: 2026-04-28
Seed: 20260428
"""

import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/Q112-F-01-fr-centroid-prereg.md"
PREREG_SHA_EXPECTED = "6e4cdfbec48ea9067bfc805077b042ca859e346582b63d3e1d245e7946d2f0f0"
H_NEW_111 = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/csv/Q112-F-01.json"

def verify_sha():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA_EXPECTED:
        print(f"FATAL: pre-reg SHA mismatch! expected {PREREG_SHA_EXPECTED}, got {sha}", file=sys.stderr)
        sys.exit(1)
    print(f"[OK] pre-reg SHA verified: {sha}")

def main():
    verify_sha()
    with open(H_NEW_111) as f:
        d111 = json.load(f)
    # Reconstruct 114x114 distance matrix from upper-triangular
    D = [[0.0]*114 for _ in range(114)]
    for elt in d111["D_matrix_upper_triangular"]:
        i, j, dist = elt[0], elt[1], elt[2]
        D[i-1][j-1] = dist
        D[j-1][i-1] = dist
    # Mean distance to 113 others, per surah
    mean_d = []
    for s in range(114):
        total = sum(D[s][j] for j in range(114) if j != s)
        mean_d.append(total / 113)
    # Rank ascending (lower = more central)
    ranked = sorted(range(114), key=lambda s: mean_d[s])
    rank_of_112 = ranked.index(111) + 1  # surah 112 = index 111
    top10 = [(s+1, mean_d[s]) for s in ranked[:10]]
    result = {
        "preregistration_id": "Q112-F-01",
        "prereg_sha": PREREG_SHA_EXPECTED,
        "seed": 20260428,
        "rules_tuple": ["no-tashkeel","QAC-stem-roots","K500","Dirichlet-alpha-0.5","Hafs-Kufan","Mashriqi","basmala-counted-only-in-Q1"],
        "n_surahs": 114,
        "Q112_rank": rank_of_112,
        "Q112_mean_d": mean_d[111],
        "top_10_centroids": [{"rank": i+1, "surah": s, "mean_d": d} for i, (s, d) in enumerate(top10)],
        "H1_pass": rank_of_112 <= 10,
        "H1_strong_pass": rank_of_112 == 1,
        "alpha_bon": 0.0125,
        "p_value_under_uniform_null": rank_of_112 / 114,
        "verdict_H1": "VINDICATED" if rank_of_112 <= 10 else "NULL",
        "verdict_H1_strong": "VINDICATED" if rank_of_112 == 1 else ("DIRECTIONAL" if rank_of_112 <= 10 else "NULL"),
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[OK] Q112_rank = {rank_of_112}/114")
    print(f"[OK] Q112_mean_d = {mean_d[111]:.6f}")
    print(f"[OK] verdict_H1 = {result['verdict_H1']}")
    print(f"[OK] verdict_H1_strong = {result['verdict_H1_strong']}")
    print(f"[OK] output -> {OUT_PATH}")

if __name__ == "__main__":
    main()
