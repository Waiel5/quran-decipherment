---
id: H-NEW-660
title: "Pre-reg — Compression-tail gradient: linear regression of d̄(consecutive-K=15) vs window-start-position"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-630 §5 — descriptive sweep showed terminal-third compresses ~3× over head; quantify gradient
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260433
---

# [[h-new-660-compression-tail-gradient|H-NEW-660]] — Compression-Tail Gradient: Pre-Registration

## 1. Hypothesis

The Quran's mushaf has a monotonically decreasing FR-roots cohesion-distance from head to tail (i.e., cohesion-density INCREASES toward tail). Specifically:

> d̄(window-K=15-start-at-s) ≈ α + β · s, with β < 0.

The compression-tail is a LINEAR gradient (or close to it) over mushaf-position s ∈ [1, 100].

## 2. Test design

For each consecutive K=15 window starting at position s ∈ {1, 2, ..., 100}:
- Compute d̄(window).
- Regress d̄ on s (centered: s̃ = s − 50.5).
- Report slope β, intercept α, R², residual SE.

### Permutation null
Shuffle the 114 surahs to a random order (10000 perms, seed 20260433). Recompute all 100 windows' d̄ on the shuffled mushaf. Refit linear regression. Get null distribution of slope β_null. Empirical p-value of observed |β| ≥ |β_null|.

(Note: shuffling 114 surahs preserves the Fisher-Rao distance matrix structure but breaks the spatial gradient. If the gradient is structural to the canonical mushaf order, p < α.)

### Alternative model fits
Pre-committed alternative-model search (MW-3):
1. Linear: d̄ = α + β·s
2. Quadratic: d̄ = α + β·s + γ·s²
3. Two-piece linear: d̄ = α₀ + β·max(0, s−50) (kink at midpoint)

Report R² for each. Pre-commit: the model with HIGHEST adjusted-R² is reported as the primary fit; permutation-test the primary fit.

## 3. Pre-committed direction

- β < 0 (slope is negative, cohesion-distance decreases with mushaf-position).
- Permutation p ≤ α_corrected.

## 4. Bonferroni structure

3 alternative model fits → Bonferroni-3 → α corrected = 0.05/3 = 0.01667.

## 5. Pass/fail thresholds

- **STRICT PASS**: primary-model β < 0, permutation p ≤ 0.01667, R² ≥ 0.50.
- **DIRECTIONAL**: β < 0, p ≤ 0.05, R² ≥ 0.30.
- **NULL**: β ≥ 0, OR p > 0.05, OR R² < 0.30.

## 6. Predicted ranges

Based on [[h-new-630-supercluster-substructure|H-NEW-630]] §5 descriptive observations (head d̄≈0.92, tail d̄≈0.32):
- Linear slope β ≈ -0.006 per surah (range over 100 windows).
- R² (linear) expected ≈ 0.60-0.85.
- Quadratic gamma may give marginal improvement.
- Two-piece may match linear if gradient is uniform.

## 7. What would FALSIFY

- β ≥ 0: gradient direction wrong → falsifies compression-tail.
- R² < 0.30: gradient is not a primary signal (window-cohesion is dominated by other factors).

## 8. Files

- Script: `scripts/h_new_660_compression_tail_gradient.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-660.json`
- Findings: `findings/phase-b-hypotheses/h-new-660-compression-tail-gradient.md`

## 9. Methodology rules

- MW-1: instrument-prior — FR-roots distance.
- MW-3: alternative-models — linear, quadratic, two-piece.
- MW-7 (post-hoc): not applicable — [[h-new-630-supercluster-substructure|H-NEW-630]] §5 was descriptive, this is a NEW pre-registered formal test.
- PRE-REG-STANDARD-04: hypothesis, null, direction, Bonferroni, success criteria all locked.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
