---
id: H-NEW-810
title: "Length-controlled iʿjāz partial correlation: rhyme axis is partially length-driven; phoneme axis is length-independent"
status: STRICT-MIXED — PARTIAL-DEPENDENT (rhyme) + PASS-INDEPENDENT (phoneme)
phase: B
date: 2026-04-28
parents:
  - H-NEW-730 (content × rhyme anti-twinning, r = -0.864)
  - H-NEW-770 (verse-length compression-tail, r ≈ 0.87 vs d_content)
prereg_sha: 4f3970eb430bd44d33c89d5577feffd3361866e9f80db6d93000e4e555161bb1
seed: 20260448
verdict: ijaz_axis (rhyme) = PARTIAL-DEPENDENT; phoneme_axis = LENGTH-INDEPENDENT
---

# [[h-new-810-length-controlled-ijaz|H-NEW-810]] — Length-Controlled iʿjāz Partial Correlation


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

## 1. Headline

| Test | Pair | Conditioning | partial r | perm p (1-sided) | classification |
|------|------|--------------|-----------|------------------|----------------|
| T1 | d_content × d_rhyme | letters_per_verse | **-0.4054** | 0.00010 | **PARTIAL-DEPENDENT** |
| T2 | d_content × d_rhyme | words_per_verse   | **-0.4017** | 0.00010 | **PARTIAL-DEPENDENT** |
| T3 | d_content × d_phoneme | letters_per_verse | **-0.8563** | 0.00010 | **PASS-INDEPENDENT** |

Reference (no control):
- Original r(d_content, d_rhyme) = **-0.8643** ([[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]).
- Original r(d_content, d_phoneme) = **-0.8933** ([[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]).

**The content × rhyme anti-twinning shrinks from r = -0.864 to partial r ≈ -0.40 once verse-length is held fixed — a 53% reduction in magnitude. The content × phoneme anti-twinning is virtually unchanged (-0.893 → -0.856, a 4% reduction).** Both length proxies (letters/verse, words/verse) give the same answer for T1 and T2 to two decimal places, so the result is not a metric-choice artefact.

Bonferroni-3 α = 0.01667. All three perm p-values = 0.00010 (lower-bound of 10000-perm grid). All three tests reject H₀ at α_bon, but only T3 satisfies the pre-locked partial-r threshold (≤ -0.5) for PASS-INDEPENDENT.

## 2. Implication: is iʿjāz length-confounded or length-independent?

The two iʿjāz axes behave differently:

- **Rhyme axis ([[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] content × rhyme anti-twinning) is PARTIALLY length-mediated.** The headline -0.864 is *not* a pure length artefact (partial r = -0.40 is still significant and substantial), but a majority of the squared anti-correlation does dissolve once length is held fixed. r²: 0.747 → 0.164. About **78% of the explanatory power of the rhyme axis is verse-length co-variation**; about **22% is rhyme-specific anti-twinning that cannot be reduced to length**.
- **Phoneme axis (content × d_phoneme) is LENGTH-INDEPENDENT.** Partial r = -0.856 is essentially identical to the marginal r = -0.893. The phoneme-distinctness anti-twinning operates on a channel orthogonal to verse-length.

This is the kind of result that a pre-reg is built for: the marginal pictures of "rhyme" and "phoneme" looked very similar (-0.864 vs -0.893), yet under length-control they decouple by half an order of magnitude in r². The classical-balagha intuition that *fawāṣil* (verse-end rhyme) is length-coupled — short verses ride a tight rhyme grid; long verses meander — finds quantitative support here.

## 3. Effect on [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]

[[cross-finding-026-iʿjāz-architecture|cross-finding-026]] read [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] as evidence that *content saturation* and *acoustic patterning* anti-twin window-by-window across the Quran — an "iʿjāz signature" of two-channel design. Under [[h-new-810-length-controlled-ijaz|H-NEW-810]]:

- The rhyme strand of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] **WEAKENS but does not collapse**. The architectural reading should be re-narrated as: *content-cohesion and rhyme-distinctness both ride the verse-length compression-tail; once that tail is removed, a residual but real anti-twinning of magnitude r ≈ -0.40 remains*. This residual is genuine (perm p < α_bon) but it is a smaller signal than the marginal -0.86 suggested.
- The phoneme strand of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] **STRENGTHENS**. Phoneme-distinctness anti-twins with content-cohesion at r ≈ -0.86 *independently of verse-length*. This is a non-trivial architectural fact: the Quran's window-by-window phoneme distribution covaries inversely with content saturation in a way that the ḥijāzī-mufaṣṣal length-tail does not predict.

Honest summary: **the iʿjāz claim survives, but the rhyme axis is now mostly length-driven; the phoneme axis is the cleaner architectural signal.** [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] should be amended to reflect this asymmetry.

## 4. Honest limits

1. **Pre-locked threshold of -0.5 is somewhat arbitrary.** Partial r = -0.40 sits in the PARTIAL-DEPENDENT band by 0.10 — within the noise of any single 100-window perm null. The conclusion would not change if we tightened to -0.6 (still partial-dependent) or loosened to -0.35 (still partial-dependent), but a reader who anchors on "partial r is significantly negative at p < 10⁻³" can legitimately read this as a softer iʿjāz claim, not a refutation.
2. **Verse-length is itself a coarse proxy.** Letters/verse and words/verse are the [[h-new-770-verse-length-compression-tail|H-NEW-770]] metrics; they do not capture syllable count, foot count, or phrase-boundary structure. A finer-grained length axis (e.g., mean verse-final consonantal weight) might absorb still more of the rhyme-axis signal — or it might not.
3. **The window scheme is fixed at K=15, s ∈ {1..100}.** Any artefact in the window choice is inherited from [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] / [[h-new-770-verse-length-compression-tail|H-NEW-770]]. Sliding-K robustness is queued for follow-up.
4. **Permutation-p saturates at 0.00010 (1/(N_perm+1)).** Effects are real-significant; we are not detecting a finer p-resolution because we did not need to.
5. **The phoneme anti-twinning's length-independence does not establish that no other confound exists.** Letter-count is one of many possible confounds (e.g., surah period, register, narrative density). [[h-new-810-length-controlled-ijaz|H-NEW-810]] only certifies that *length* does not absorb the phoneme axis.
6. **One-text discipline preserved.** Single Hafs corpus throughout.

## 5. Cross-references

- **[[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]** (parent) — provided d_content, d_rhyme, d_phoneme; this finding partials its result.
- **[[h-new-770-verse-length-compression-tail|H-NEW-770]]** (parent) — provided letters_per_verse and words_per_verse window vectors.
- **[[cross-finding-026-iʿjāz-architecture|cross-finding-026]]** — should be amended: rhyme-axis iʿjāz becomes "partial after length"; phoneme-axis iʿjāz strengthens.
- **[[h-new-660-compression-tail-gradient|H-NEW-660]]** — content-cohesion compression-tail; verse-length sits between [[h-new-660-compression-tail-gradient|H-NEW-660]] and [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] as the apparent mediator on the rhyme axis.
- Wave-1 2026-04-17 4-region architecture — the asymmetry between rhyme (length-mediated) and phoneme (length-independent) suggests the architecture has at least two separate axes, not one collapsed iʿjāz channel.

## 6. Queued follow-ups

1. **H-NEW-820** (queued): residual iʿjāz at r = -0.40 — is the residual structured? Window-by-window scatter of (d_content × d_rhyme) regressed on length-residuals; cluster by mushaf region.
2. **H-NEW-830** (queued): is the *phoneme* anti-twinning mediated by something else (e.g., consonantal-cluster density, vowel-length distribution)? T3's robustness to length does not establish robustness to other axes.
3. **[[h-new-840-unified-architectural-score|H-NEW-840]]** (queued): syllable- and foot-level length metrics as a finer length proxy. Does T1 collapse further to partial r ≈ 0 under syllabic-length control?
4. **H-NEW-850** (queued): sliding-K robustness — repeat T1, T2, T3 at K ∈ {10, 20, 25} to confirm the rhyme-vs-phoneme asymmetry is not K=15-specific.

## 7. Final statement

The Quran's content × rhyme anti-twinning is **partially** an artefact of the verse-length compression-tail: about three-quarters of its r² dissolves under length-control, leaving a residual r ≈ -0.40 that is significant but markedly weaker than the headline -0.86. The Quran's content × phoneme anti-twinning is **not** an artefact of verse-length: r ≈ -0.86 survives length-partial almost untouched. The iʿjāz signature is therefore real but asymmetric — phoneme-distinctness is the cleaner architectural channel; rhyme-distinctness is largely length-mediated with a smaller residual layer. [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]'s iʿjāz reading should be amended accordingly. Reported HONESTLY per the prereg's commitment.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
