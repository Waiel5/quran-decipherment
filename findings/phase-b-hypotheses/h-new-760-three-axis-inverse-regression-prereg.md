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


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
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
