---
id: H-NEW-730
title: "Pre-reg — Content × Rhyme architectural anti-correlation: window-by-window Pearson r"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-660 (content compresses) + H-NEW-700 (rhyme disperses) — both at R²≥0.79 on same Hijra-kink; test if they are anti-correlated at window-level
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260442
---

# [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] — Content/Rhyme Anti-Correlation: Pre-Registration


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

[[h-new-660-compression-tail-gradient|H-NEW-660]] found content-cohesion COMPRESSES toward the mushaf terminus (β = −0.01237, R²=0.986). [[h-new-700-phonological-compression-tail|H-NEW-700]] found phonological-rhyme DISPERSES on the same Hijra-kink (β = +0.00412, R²=0.789). 

**Hypothesis**: at window-level, the two metrics are NEGATIVELY correlated. Specifically:

> Pearson r(d̄_content_window, d̄_rhyme_window) ≤ −0.60.

If confirmed, this empirically locks the **iʿjāz architecture**: theological convergence simultaneous with sonic divergence is a window-by-window structural anti-twin signature.

## 2. Test design

For each K=15 window starting at s ∈ {1, ..., 100}:
- d̄_content[s] = mean pairwise FR-roots distance (load from [[h-new-660-compression-tail-gradient|h-new-660]] or recompute).
- d̄_rhyme[s] = mean pairwise rhyme-cosine distance (load from [[h-new-700-phonological-compression-tail|h-new-700]].json key `rhyme.d_observed`).
- Compute Pearson r and Spearman ρ.

### Permutation null
Shuffle d̄_rhyme positions (10000 perms, seed 20260442). Recompute Pearson r each time. Empirical p-value of |r_observed| ≥ |r_null|.

### Cross-window check
Identify the windows where:
- Both d̄_content LOW and d̄_rhyme HIGH (max iʿjāz signature: cohesive content + diverse rhyme) — terminal-tail expected.
- Both d̄_content HIGH and d̄_rhyme LOW (anti-iʿjāz: dispersed content + uniform rhyme) — head ṭiwāl expected.

## 3. Pre-committed direction

- Pearson r < 0 (negative correlation).
- |r| ≥ 0.60.
- Permutation p ≤ 0.025 (Bonferroni-2 — Pearson + Spearman).

## 4. Pre-committed thresholds

- **STRICT PASS**: r ≤ −0.60, p ≤ 0.025, |Spearman ρ| ≤ −0.55.
- **DIRECTIONAL**: r ≤ −0.40, p ≤ 0.05.
- **NULL**: r > −0.40 OR p > 0.05.

## 5. Bonferroni structure

Pearson + Spearman → Bonferroni-2 → α_corrected = 0.025.

## 6. What would FALSIFY

- r > 0: content and rhyme co-compress (would falsify the iʿjāz anti-twin).
- |r| < 0.40: weak relationship.

## 7. Methodology rules

- MW-1: instrument-prior — both metrics use existing project methodology.
- MW-3: alternative-models — Spearman in addition to Pearson.
- MW-7: not applicable (this is a primary pre-registered test).
- PRE-REG-STANDARD-04: hypothesis, null, direction, success criteria locked.

## 8. Files

- Script: `scripts/h_new_730_content_rhyme_anticorrelation.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-730.json`
- Findings: `findings/phase-b-hypotheses/h-new-730-content-rhyme-anticorrelation.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
