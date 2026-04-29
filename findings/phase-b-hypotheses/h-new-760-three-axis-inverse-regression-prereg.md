---
id: H-NEW-760
title: "Pre-reg — 3-axis inverse regression: predict mushaf position s from window cohesion-profile (d_content, d_rhyme, d_phoneme)"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-660 + H-NEW-700 + H-NEW-730 — three 1-D laws on s; test if their JOINT inverse uniquely determines s
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260443
---

# [[h-new-760-three-axis-inverse-regression|H-NEW-760]] — 3-Axis Inverse Regression Pre-Registration

## 1. Hypothesis

[[h-new-660-compression-tail-gradient|H-NEW-660]] / 680 / 700 / 730 establish three architectural axes:
- d̄_content(s) ≈ 0.96 − 0.012 · max(0, s−50)
- d̄_rhyme(s) ≈ 0.36 + 0.0041 · max(0, s−50)
- d̄_phoneme(s) ≈ 0.001 + 0.00089 · max(0, s−75)

**Hypothesis**: the inverse regression s ~ f(d̄_content, d̄_rhyme, d̄_phoneme) achieves LOOCV R² ≥ 0.95.

If confirmed: the mushaf's window-position is **empirically determined** by its 3-axis cohesion profile. A window's "where in the mushaf it lives" is recoverable from its content/rhyme/phoneme distance profile alone.

## 2. Test design

For 100 K=15 windows (s ∈ {1, ..., 100}):
- Predictors: x1 = d̄_content[s], x2 = d̄_rhyme[s], x3 = d̄_phoneme[s].
- Target: s.

### Models
1. Linear: s ~ a + b1·x1 + b2·x2 + b3·x3.
2. Linear + interactions: s ~ a + b1·x1 + b2·x2 + b3·x3 + b12·x1·x2 + b13·x1·x3 + b23·x2·x3.
3. Quadratic + linear: s ~ a + linear + b1²·x1² + b2²·x2² + b3²·x3².

### Validation
- In-sample R².
- LOOCV R² (drop one window at a time, refit, predict).
- Per-prediction error |s_predicted − s_observed|.

### Permutation null
Shuffle s among 100 windows (10000 perms, seed 20260443). Refit linear model. Get null distribution of LOOCV R².

## 3. Pre-committed direction

- All 3 βs nonzero (each axis contributes).
- β(d̄_content) NEGATIVE (content dispersion → small s; content tight → large s, post-Hijra).
- β(d̄_rhyme) POSITIVE (rhyme uniform → small s; rhyme diverse → large s).
- β(d̄_phoneme) POSITIVE (similar to rhyme).

## 4. Pre-committed thresholds

- **STRICT PASS**: LOOCV R² ≥ 0.95 AND mean abs prediction error ≤ 5 windows.
- **DIRECTIONAL**: LOOCV R² ≥ 0.85 AND mean abs error ≤ 10 windows.
- **NULL**: weaker.

## 5. Bonferroni structure

3 model fits → Bonferroni-3 → α corrected = 0.01667.

## 6. Files

- Script: `scripts/h_new_760_three_axis_inverse_regression.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-760.json`
- Findings: `findings/phase-b-hypotheses/h-new-760-three-axis-inverse-regression.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
