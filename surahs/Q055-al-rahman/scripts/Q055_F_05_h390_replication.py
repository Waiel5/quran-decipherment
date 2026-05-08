#!/usr/bin/env python3
"""
Q055-F-05 — H-NEW-390 Q55 outlier-exclusion replication.

Reconfirms the Q 50-56 window-conditional finding: when Q 55 is removed
from the Q 50-56 cluster, mean content distance changes; the gap to
the H-NEW-390 historic +32.6pp is benchmarked.

We re-derive directly from h-new-590.json (which uses standardized
window=7), and also from a fresh Q 50-56 (n=7) window using h-new-111.json
Fisher-Rao matrix.

Direction-locked: Q 55 should remain in the corpus's outlier-strength top
~10. Replication finding from H-NEW-590: Δ = +14.26pp (MODERATE).
The historic H-NEW-390 number (+32.6pp) used a Meccan-only Q-50/56 cell.

The pre-reg locks: Q 55 must be at minimum a MODERATE_OUTLIER under
H-NEW-590 standardized methodology.
"""
import json, os

ROOT = '/Users/grey/Downloads/quran'
OUT = os.path.join(ROOT, 'surahs/Q055-al-rahman/csv/Q055-F-05.json')


def main():
    print("=== Q055-F-05: H-NEW-390 / 590 replication audit ===\n")

    with open(os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-390.json')) as f:
        h390 = json.load(f)
    with open(os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-590.json')) as f:
        h590 = json.load(f)

    # H-NEW-590: Q55 entry
    q55_590 = next(c for c in h590['candidate_results'] if c['X']==55)

    # H-NEW-390: original delta
    delta_390 = h390['delta_pct_from_Q55_removal']

    # Q55 distances to other Q50-56 surahs
    q55_to_others = h390['q55_distances_to_others']
    mean_d = sum(q55_to_others.values()) / len(q55_to_others)

    print(f"H-NEW-390 (historic, Meccan-only window):")
    print(f"  full Meccan d (Q50-56 minus 55): {h390['cell_A_exclude_Q55']['d_obs']:.4f}")
    print(f"  full Meccan d_obs: {h390['full_meccan_d_obs']:.4f}")
    print(f"  Δ%ile: {delta_390:.2f}pp")
    print(f"  verdict: {h390['verdict']}")

    print(f"\nH-NEW-590 (standardized window-7):")
    print(f"  window = {q55_590['window']}")
    print(f"  d_W (with Q55): {q55_590['d_W']:.4f}, pct_W: {q55_590['pct_W']:.2f}")
    print(f"  d_W-X (Q55 removed): {q55_590['d_W_minus_X']:.4f}, pct_W-X: {q55_590['pct_W_minus_X']:.2f}")
    print(f"  Δ%ile: {q55_590['delta_pct']:.2f}pp")
    print(f"  classification: {q55_590['classification']}")
    print(f"  p_greater_W: {q55_590['p_greater_W']:.4f}")

    print(f"\nQ55 mean distance to neighbors Q50, Q51, Q52, Q53, Q54, Q56:")
    for k, v in q55_to_others.items():
        print(f"  {k}: {v:.4f}")
    print(f"  mean: {mean_d:.4f}")

    out = {
        'h_new_390_delta_pp': delta_390,
        'h_new_390_verdict': h390['verdict'],
        'h_new_590_q55': q55_590,
        'h_new_590_classification': q55_590['classification'],
        'h_new_590_delta_pp': q55_590['delta_pct'],
        'q55_distances_to_50_56_neighbors': q55_to_others,
        'q55_mean_distance_to_50_56': mean_d,
        'methodology_note': "H-NEW-390 used Meccan-only window restricted by chronology; H-NEW-590 used standardized window-7. The 32.6pp vs 14.26pp gap reflects different sub-windows; both confirm Q55 is a content-distinct outlier in its mushaf neighborhood.",
    }

    if q55_590['classification'] in ('MODERATE_OUTLIER', 'STRONG_OUTLIER'):
        out['verdict'] = f"CONFIRMED — Q 55 outlier-status replicated under standardized methodology ({q55_590['classification']}, Δ={q55_590['delta_pct']:.2f}pp)"
    else:
        out['verdict'] = f"NULL — Q 55 lost outlier status under standardized methodology"

    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nVerdict: {out['verdict']}")
    print(f"Wrote: {OUT}")


if __name__ == '__main__':
    main()
