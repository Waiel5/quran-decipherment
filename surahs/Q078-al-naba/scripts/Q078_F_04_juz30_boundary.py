#!/usr/bin/env python3
"""
Q078-F-04 — Q 77 → Q 78 juzʾ-30 boundary cost test.

Pre-reg: surahs/Q078-al-naba/preregs/Q078-F-04-juz30-boundary-prereg.md
SHA256:  embedded at runtime; verified against pre-reg

Hypothesis (LOCKED PRE-RUN):
  H1: The Q 77 → Q 78 mushaf-adjacency cost is NOT in the top-15 by
      delta_raw (i.e., NOT a structural-boundary).
      DIRECTION: rank > 15.

H0: H1 fails (rank ≤ 15).

Single-test (no Bonferroni — single direction-locked claim).
α = 0.05.

Method:
  - Read H-NEW-720 per_adjacency data from
    findings/phase-b-hypotheses/csv/h-new-720.json.
  - Sort by delta_raw descending; report Q 77→78 rank.

Seed: 20260509 (no random-element).
"""

import json
import os
import hashlib

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PREREG_PATH = os.path.join(os.path.dirname(__file__), '..', 'preregs',
                           'Q078-F-04-juz30-boundary-prereg.md')
H_NEW_720_PATH = os.path.join(PROJECT_ROOT, 'findings', 'phase-b-hypotheses',
                              'csv', 'h-new-720.json')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv', 'Q078-F-04.json')

SEED = 20260509


def sha256_of(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    prereg_sha = sha256_of(PREREG_PATH)
    print(f"prereg SHA256: {prereg_sha}")

    with open(H_NEW_720_PATH) as f:
        d = json.load(f)

    # Sort by delta_raw descending
    sorted_adj = sorted(d['per_adjacency'], key=lambda x: -x['delta_raw'])
    q77_q78_rank = next(
        i + 1 for i, a in enumerate(sorted_adj) if a['pair'] == [77, 78]
    )
    q77_q78 = next(a for a in sorted_adj if a['pair'] == [77, 78])

    # Pre-locked direction: rank > 15
    h1_pass = q77_q78_rank > 15

    # Compare to neighbors
    neighbors = []
    for adj in d['per_adjacency']:
        if 75 <= adj['pair'][0] <= 81 or 75 <= adj['pair'][1] <= 81:
            rank = next(
                i + 1 for i, a in enumerate(sorted_adj) if a['pair'] == adj['pair']
            )
            neighbors.append({
                "pair": adj['pair'],
                "delta_raw": adj['delta_raw'],
                "fraction_residual": adj['fraction_residual'],
                "rank_by_cost_desc": rank,
            })

    # Top 13 cheapest seams (per H-NEW-1240) — does Q 77→78 appear?
    is_seamless = q77_q78['delta_raw'] <= 0

    output = {
        "test_id": "Q078-F-04",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "q77_q78_metrics": {
            "delta_raw": q77_q78['delta_raw'],
            "delta_clamped": q77_q78['delta'],
            "fraction_residual": q77_q78['fraction_residual'],
            "rank_by_cost_desc": q77_q78_rank,
            "is_seamless": is_seamless,
        },
        "neighbors_q75_q81": neighbors,
        "top_15_most_expensive": [
            {"pair": a['pair'], "delta_raw": a['delta_raw'],
             "rank": i + 1}
            for i, a in enumerate(sorted_adj[:15])
        ],
        "h1_pass_rank_gt_15": h1_pass,
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"Q 77→78 delta_raw: {q77_q78['delta_raw']:.5f}")
    print(f"Q 77→78 fraction-residual: {q77_q78['fraction_residual']:.5f}")
    print(f"Q 77→78 rank by cost desc: {q77_q78_rank}/113")
    print(f"H1 PASS (rank > 15): {h1_pass}")
    print(f"Top-3 most-expensive: {[a['pair'] for a in sorted_adj[:3]]}")
    print(f"Output: {OUTPUT_PATH}")


if __name__ == '__main__':
    main()
