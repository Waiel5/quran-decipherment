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


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

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
