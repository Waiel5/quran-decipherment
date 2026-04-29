---
finding_id: Q055-F-05
title: H-NEW-390 / H-NEW-590 outlier-exclusion replication for Q 55
phase: B+
date_locked: 2026-04-28
seed: 20260428
script: surahs/Q055-al-rahman/scripts/Q055_F_05_h390_replication.py
---

# Q055-F-05 — H-NEW-390 replication pre-registration

## Hypothesis

Q 55 must be replicated as an outlier in its mushaf-neighborhood under both
- H-NEW-390 (Meccan-only Q 50-56 window-conditional, +32.6pp historic)
- H-NEW-590 (standardized window-7 outlier-spectrum)

## Direction (LOCKED)

- Q 55 classification under H-NEW-590 ∈ {MODERATE_OUTLIER, STRONG_OUTLIER}
- Q 55 Δ-pp under H-NEW-590 > 0 (strict positive direction)
- Q 55 Δ-pp under H-NEW-390 > 0

Counter-direction (Q 55 NOT classified as ≥ MODERATE_OUTLIER under H-NEW-590) = NULL.

## Methodology

Re-derive directly from the canonical project artifacts:
- `findings/phase-b-hypotheses/csv/h-new-390.json`
- `findings/phase-b-hypotheses/csv/h-new-590.json`

No new computation; we audit consistency between H-NEW-390 (window-conditional, Meccan-only) and H-NEW-590 (standardized window-7).

## Note on the +32.6pp vs +14.26pp gap

H-NEW-390 used a Meccan-only Q-50-56 cell (n=7, no chronological mixing), giving +32.6pp upon Q 55 removal.
H-NEW-590 uses standardized window=7 around s, giving +14.26pp.
The gap is methodological: the more chronologically-homogeneous Meccan-only cell amplifies Q 55's content-distinctness against its surrounding mufaṣṣal-Meccan tier.
Both tests confirm Q 55 is an outlier; the magnitude shifts with windowing.
