#!/usr/bin/env python3
"""H-NEW-630b: descriptive supplementary — confirm Q 100-114 is the GLOBALLY DENSEST 15-surah window in the mushaf.

Sweep all consecutive 15-surah windows; rank by d̄. Also check all consecutive 22-surah windows for B's claim.
Descriptive only; no pre-reg required (sweeps are in MASTER-FINDINGS-LEDGER methodology).
"""
import json
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"


def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def mean_pairwise(D, subset):
    return sum(D[a][b] for a, b in combinations(subset, 2)) / max(1, len(list(combinations(subset, 2))))


def main():
    D = load_D()
    print("=== H-NEW-630b: Globally densest consecutive-K windows ===\n")

    for K in [11, 15, 22]:
        windows = []
        for start in range(1, 115 - K + 1):
            sub = list(range(start, start + K))
            d = mean_pairwise(D, sub)
            windows.append((d, start, start + K - 1))
        windows.sort()
        print(f"--- K={K} consecutive surahs (top 10 densest of {len(windows)} windows) ---")
        for rank, (d, lo, hi) in enumerate(windows[:10], 1):
            print(f"  #{rank}: Q {lo}-{hi}  d̄={d:.4f}")
        print()

    print("--- Specific windows of interest ---")
    interesting = [
        ("Q 67-77", list(range(67, 78))),
        ("Q 78-99", list(range(78, 100))),
        ("Q 100-114", list(range(100, 115))),
        ("Q 78-89", list(range(78, 90))),
        ("Q 86-92", list(range(86, 93))),
        ("Q 93-99", list(range(93, 100))),
        ("Q 107-114", list(range(107, 115))),
        ("Q 109-114 (muʿawwidhāt+)", list(range(109, 115))),
        ("Q 1-7 (Fātiḥa+)", list(range(1, 8))),
    ]
    for label, sub in interesting:
        d = mean_pairwise(D, sub)
        print(f"  {label}: d̄={d:.4f}, N={len(sub)}")


if __name__ == "__main__":
    main()
