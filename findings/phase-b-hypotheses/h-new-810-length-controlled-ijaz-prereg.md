---
id: H-NEW-810
title: "Pre-reg — Length-controlled iʿjāz partial correlation: does the content-rhyme anti-twinning of H-NEW-730 survive partialling out verse-length?"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-730 (r(content × rhyme) = -0.864 window-by-window) AND H-NEW-770 (verse-length explains ~76% of content-cohesion variance, r ≈ 0.872 letters_per_verse vs d_content; r ≈ 0.873 words_per_verse vs d_content). Critical robustness check: is iʿjāz a length artefact?
discipline: PRE-REG-STANDARD-04
seed: 20260448
---

# [[h-new-810-length-controlled-ijaz|H-NEW-810]] — Length-Controlled iʿjāz Partial Correlation: Pre-Registration


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

The [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] anti-twinning effect — Pearson r(d_content, d_rhyme) = -0.864 across the K=15 100-window mushaf scan — is NOT entirely an artefact of the verse-length compression-tail ([[h-new-770-verse-length-compression-tail|H-NEW-770]]). When verse-length (letters/verse or words/verse) is partialled out, the iʿjāz signature must remain substantially negative (partial r ≤ -0.5) for the [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] reading to hold.

This is a PURE robustness check. Direction of evidence is bidirectional: failure SHRINKS [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]; success STRENGTHENS it.

## 2. Locked metrics (no recomputation)

All three input series are taken VERBATIM from the parent JSON outputs (already on disk, hashed prereg):

- d_content[100] — `findings/phase-b-hypotheses/csv/h-new-730.json` → `d_content`.
- d_rhyme[100]   — `findings/phase-b-hypotheses/csv/h-new-730.json` → `d_rhyme`.
- d_phoneme[100] — `findings/phase-b-hypotheses/csv/h-new-730.json` → `d_phoneme`.
- letters_per_verse[100] — `findings/phase-b-hypotheses/csv/h-new-770.json` → `metric_letters_per_verse.window_obs`.
- words_per_verse[100]   — `findings/phase-b-hypotheses/csv/h-new-770.json` → `metric_words_per_verse.window_obs`.

All five vectors must have length 100 and identical canonical mushaf ordering (s ∈ {1..100} = window-start surah). Length and ordering are checked at run-start; abort if either fails.

## 3. Three locked partial-correlation tests

Using the standard partial-correlation formula:

```
r(X, Y | Z) = (r_xy − r_xz · r_yz) / sqrt((1 − r_xz²) · (1 − r_yz²))
```

with Pearson r as the base correlation, three tests are run:

1. **T1 — r(d_content, d_rhyme | letters_per_verse)** — does iʿjāz survive removing letter-length effect?
2. **T2 — r(d_content, d_rhyme | words_per_verse)**   — same with word-length effect.
3. **T3 — r(d_content, d_phoneme | letters_per_verse)** — same robustness check on the content × phoneme axis.

## 4. Permutation null (locked)

For each test, generate a null distribution of partial correlations under H₀ (no genuine partial association beyond what length explains). Procedure (10000 perms, seed 20260448):

- Shuffle the rhyme (or phoneme) vector ONLY, keeping content and length aligned with the canonical mushaf order.
- Recompute the partial correlation on (content, shuffled-rhyme | length).
- p_perm = fraction of nulls with partial r ≤ observed (one-sided, since the pre-committed direction is negative).

This shuffle holds the content × length and length × length geometries fixed; only the content-rhyme association is broken. (Identical structure to the [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] perm null, with length added as the conditioning vector.)

Fisher z-transform is reported alongside permutation p for completeness, but the perm-p is gating.

## 5. Pre-committed direction

- T1, T2, T3: partial r EXPECTED to be negative.
- Direction = lower-tail (one-sided): observed partial r ≤ null partial r.

## 6. Bonferroni structure

- 3 partial-r tests → α_bon = 0.05 / 3 = 0.01667.

## 7. Pass / partial / fail thresholds (LOCKED)

For each of T1, T2, T3:

- **PASS-INDEPENDENT** (iʿjāz survives length-control): partial r ≤ -0.5 AND perm p ≤ 0.01667.
- **PARTIAL-DEPENDENT** (mixed): partial r ∈ (-0.5, -0.3].
- **PASS-LENGTH-DRIVEN** (iʿjāz dissolves when length is held fixed): partial r > -0.3.

Aggregate verdict on the iʿjāz axis = the reading of T1 and T2 jointly (content × rhyme, two length proxies). T3 (content × phoneme) is reported alongside and treated symmetrically.

## 8. Pre-committed reasoning rules (BEFORE run)

- If T1 AND T2 both PASS-INDEPENDENT → iʿjāz is structurally present BEYOND length; [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] STRENGTHENS; [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] is robust to the [[h-new-770-verse-length-compression-tail|H-NEW-770]] confound.
- If T1 OR T2 lands in PARTIAL-DEPENDENT → iʿjāz is partially length-mediated; [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] SOFTENS but does not fall.
- If T1 AND T2 both PASS-LENGTH-DRIVEN → iʿjāz is largely a verse-length confound; [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] WEAKENS; [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] must be re-narrated as a length-tail phenomenon. THIS RESULT WILL BE REPORTED HONESTLY.
- T3 mirrors the same logic for the content × phoneme axis.

NULL-equally-prominent rule: at every report stage the null reading (length-driven) is presented with the same prominence as the alternative.

## 9. What would FALSIFY the iʿjāz independence

- Any test with partial r > -0.3 and perm p > 0.01667 falsifies independence on that axis.
- T1 and T2 disagreeing wildly (one pass-independent, one length-driven) flags metric-choice fragility — would trigger MW-7 follow-up.

## 10. Files

- Prereg: `findings/phase-b-hypotheses/h-new-810-length-controlled-ijaz-prereg.md` (this file).
- Script: `scripts/h_new_810_length_controlled_ijaz.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-810.json`
- Findings: `findings/phase-b-hypotheses/h-new-810-length-controlled-ijaz.md`
- Journal: `journal/h-new-810-run-1.md`

## 11. Methodology rules

- MW-1 instrument-prior: metrics are inherited verbatim from parents; no new measurement.
- MW-3 alternative-models: two length proxies (letters/words) cross-checked; phoneme axis as a third axis.
- MW-7 not applicable — fully pre-registered.
- PRE-REG-STANDARD-04: hypothesis, null, direction, Bonferroni-3, pass/partial/fail criteria, honesty-rule on length-driven outcome — all LOCKED BEFORE run.

## 12. Disciplines

- ONE-text discipline: single canonical Hafs Quran corpus. No edition framing.
- HONEST-on-failure: if iʿjāz is length-driven, this prereg commits to reporting that finding cleanly, not softening it.
- Bonferroni-tightening permitted post-hoc; loosening forbidden.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
