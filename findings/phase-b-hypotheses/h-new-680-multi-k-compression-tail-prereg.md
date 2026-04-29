---
id: H-NEW-680
title: "Pre-reg — Multi-K compression-tail spectrum: does the two-piece-kink-at-s=50 law generalize across K ∈ {7, 11, 22}?"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-660 §10 queued follow-up — single-K=15 yielded R²=0.986 for d̄ ≈ 0.9603 − 0.01237·max(0, s − 50). Test scale-invariance.
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260434
---

# [[h-new-680-multi-k-compression-tail|H-NEW-680]] — Multi-K Compression-Tail Spectrum: Pre-Registration

## 1. Hypothesis

The single-parameter compression-tail law established in [[h-new-660-compression-tail-gradient|H-NEW-660]] at K=15 is **scale-invariant**: at K ∈ {7, 11, 22}, the same two-piece-kink-at-s=50 family wins (vs linear, quadratic), the kink converges near s=50, and the post-kink slope β remains negative.

Formally, for each K ∈ {7, 11, 22}:
> d̄(window-K-start-at-s) ≈ α + β · max(0, s − k*), with β < 0 and k* ∈ [40, 60].

## 2. Locked parameters

- **K values (locked)**: {7, 11, 22}.
- **Window-start range (locked per K)**: s ∈ {1, 2, ..., 114 − K + 1}.
- **Three baseline models per K (locked, MW-3)**:
  1. Linear: d̄ = α + β·(s − s̄)
  2. Quadratic: d̄ = α + β·s + γ·s²
  3. Two-piece-kink (best of grid {25, 50, 75}, then refined): d̄ = α + β·max(0, s − k)
- **Kink-search grid (locked, refinement step)**: {25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75}.
- **Permutations (locked)**: 10000 surah-shuffles per K, seed 20260434.
- **Direction (locked)**: β < 0 expected at all K.

## 3. Bonferroni structure

- **Within each K**: 3 models (linear, quadratic, two-piece) → Bonferroni-3 → α_bon = 0.05/3 = 0.01667.
- **Across the 3 K values**: a second Bonferroni-3 → α_cross = 0.01667/3 = 0.00556.
- For STRICT-PASS the primary-model perm p must clear α_cross = 0.00556 at every K (this is tighter than the within-K α_bon = 0.01667, consistent with feedback_bonferroni_tightening_vs_loosening — tightening is self-verifying).

## 4. Pass/fail thresholds

- **STRICT PASS (scale-invariant law)**: at all 3 K values
  - primary-model R² ≥ 0.50
  - primary-model perm p ≤ α_bon = 0.01667 (within-K), AND p ≤ α_cross = 0.00556 (across-K tightening)
  - best kink ∈ [40, 60]
  - β < 0
- **DIRECTIONAL**: at ≥ 2 of 3 K values primary-model R² ≥ 0.30, p ≤ 0.05, kink ∈ [30, 70], β < 0.
- **NULL / SCALE-DEPENDENT**: any K fails directional, OR best kinks diverge by more than ±20 surahs across K.

If different K yield different best kinks, REPORT THE DIVERGENCE HONESTLY (per task instruction).

## 5. Pre-committed prediction

[[h-new-660-compression-tail-gradient|H-NEW-660]] found kink at s=50 with β=−0.01237 at K=15. Predictions for the 3 K values:

| K | Predicted kink | Predicted R² (two-piece) | Predicted β |
|:-:|:--:|:--:|:--:|
|  7 | s ≈ 50  ± 5 | 0.85 – 0.95 | ≈ −0.012 |
| 11 | s ≈ 50  ± 5 | 0.95 – 0.985 | ≈ −0.012 |
| 22 | s ≈ 50  ± 7 | 0.97 – 0.995 | ≈ −0.012 |

(Larger K should smooth the curve and raise R²; smaller K may show more noise around the same kink.)

## 6. What would FALSIFY scale-invariance

- Best kink at K=7 differs from best kink at K=22 by > 20 surahs.
- At any K, two-piece-kink-at-s=50 is OUTPERFORMED by quadratic by adj-R² Δ > 0.05.
- At any K, β ≥ 0.

## 7. Files

- Script: `scripts/h_new_680_multi_k_compression_tail.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-680.json`
- Findings: `findings/phase-b-hypotheses/h-new-680-multi-k-compression-tail.md`
- Journal: `journal/h-new-680-run-1.md`

## 8. Methodology rules

- MW-1: instrument-prior — FR-roots distance from [[h-new-111-fisher-rao-mushaf|h-new-111]].json (locked).
- MW-3: alternative-models — linear, quadratic, two-piece-kink (the kink itself is grid-searched within the locked grid).
- MW-7 (post-hoc): not applicable — [[h-new-660-compression-tail-gradient|H-NEW-660]] was the primary; this is the multi-K generalization, pre-registered before run.
- PRE-REG-STANDARD-04: K-set, kink-grid, direction, Bonferroni-3 (within) and Bonferroni-3 (across) all locked.
- ONE text — single canonical 114-surah corpus.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
