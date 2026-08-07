---
id: H-NEW-890
title: "Numerical and sequence re-audit in light of 2026-04-28 architectural findings"
phase: B
status: PRE-REGISTERED
date: 2026-04-28
parent_findings:
  - H-NEW-660 (compression-tail R²=0.986, two-piece kink at s=50)
  - H-NEW-700 (phonological dispersion-tail, sign-inverted twin)
  - H-NEW-750 (per-surah iʿjāz signature; anti-twin r=-0.86)
  - H-NEW-810 (length-controlled iʿjāz, super-additivity 1.185×)
  - H-NEW-111 (Fisher-Rao mushaf-order optimality, z=-11.46)
seed: 20260428
bonferroni_k: 5
alpha_bon: 0.01
---

# [[h-new-890-numerical-reaudit|H-NEW-890]] — Pre-Registration


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

## Motivation

The 2026-04-28 architectural findings (compression-tail R²=0.986, dual-axis super-additivity 1.185×, sign-inverted phonological twin r=-0.86, FR-distance optimality z=-11.46) are *quantitative*. Classical *ʿilm al-ḥarf* and *ḥisāb al-jummal* literature contains many *qualitative* numerical claims — that surahs Q 8 and Q 9 form one unit; that the bismillah's letter count or the "nineteen" of Q 74:30 organize the mushaf; that 6236 / 114 are structurally meaningful; that Q 1 al-Fātiḥa is the seed-vector around which the rest of the mushaf orbits.

Most such claims have been adjudicated previously in the project ledger (see `mathematical-sequences-audit.md`, `numerical-coincidences.md`, `numerical-sequences.md`) and the verdict was largely NULL. This re-audit asks the narrower, *architecturally informed* question: do any of these classical claims become testable predictions in light of the new structural findings?

We pre-commit to five tests, each with a falsifiable null and a Bonferroni-5 correction (α_bon = 0.01).

## Pre-committed Tests

### Test 1 — Q 8 + Q 9 functional-unity test (Tawba/Anfāl)

**Classical claim**: Some classical commentators noted Q 9 lacks the bismillah and questioned whether Q 8–Q 9 form a single composition (the "two-as-one" surah). Combined verse count: 75 + 129 = 204.

**Architectural prediction**: If the two are functionally one, the FR-roots cosine-distance d_FR(Q 8, Q 9) should sit at the *low end* of the all-adjacent-pairs distribution.

**Statistic**: Empirical rank of d_FR(8, 9) among the 113 adjacent-pair distances {d_FR(i, i+1) : i ∈ [1, 113]}.

**Null**: d_FR(8, 9) is a typical adjacent-pair distance — its rank is uniformly distributed on {1, …, 113}.

**One-sided test**: smaller-than-expected. Empirical p = rank/113.

**PASS**: p < 0.01 (Bonferroni-5).
**NULL**: p ≥ 0.01.

### Test 2 — Compression-tail genericity (cross-textual control)

**Classical claim**: The mushaf's structural minimalism is part of *iʿjāz al-Qurʾān*. A 1-D compression-tail law (R²=0.986 with single kink-50 parameter) is information-theoretically minimal; if it is a property of *any* edited collection of pieces, the claim of distinctiveness collapses.

**Architectural prediction**: An ARTIFICIAL mushaf-analog built from a non-Quranic Arabic corpus, sliced into 114 "pseudo-surahs" matched to the actual verse-count distribution, should NOT produce an equivalent compression-tail (i.e. its kink-50 fit should yield R² ≪ 0.986 *or* an undefined sign).

**Statistic**: Refit the same two-piece-kink-at-s=50 linear model on a per-pseudo-surah gzip-compression-ratio sequence built from `bukhari-noquran.txt` (and `jahiz-hayawan.txt` if size permits), sliced into 114 contiguous chunks of lengths matching `hafs-verse-counts.tsv` (rescaled to chunk-byte-budget).

**Null**: The non-Quranic kink-50 R² is in the same range (R² ≥ 0.90) and same sign (β < 0) as the Quranic compression-tail.

**Two-sided test on R² and one-sided test on β-sign**.

**PASS-DISTINCTIVE**: Quranic R² > non-Quranic R² by ≥ 0.20 *AND* non-Quranic β has opposite or null sign; honest if reversed.
**NULL-GENERIC**: non-Quranic also produces R² ≥ 0.90 with β < 0.

### Test 3 — Verse-count divisibility-by-19 test

**Classical claim**: Rashad-Khalifa-style "Code 19" claims that the count of 19 (number of letters in *bism Allāh al-Raḥmān al-Raḥīm* in *some* spellings, words in Q 96:1-5 in some countings, and the explicit "nineteen" of Q 74:30) is structurally pervasive. We test the claim **per surah**: how many of the 114 surahs have a verse count divisible by 19?

**Statistic**: k = #{i : 1 ≤ i ≤ 114, n_verses[i] mod 19 == 0}.

**Random expectation under uniform residue**: E[k] = 114/19 = 6.0.

**Null distribution**: Generated by randomly sampling 114 verse-counts (with replacement) from a baseline integer distribution; we use the *empirical* distribution of verse counts (multinomial bootstrap, n_iter = 10⁵) to preserve range/skew. Then compute k_null. This is conservative (the actual mushaf is a single observation, but bootstrapping gives a calibrated null at the same support).

**Two-sided test**: p = (#{k_null ≥ k_obs} + #{k_null ≤ k_obs ∧ if k_obs > E})/n_iter, properly two-tailed.

**PASS**: p < 0.01.
**NULL**: p ≥ 0.01.

### Test 4 — 6236 / 114 divisibility patterns

**Statistic**: 6236 = 4 × 1559 = 2² × 1559. 1559 is prime. 114 = 2 × 3 × 19. The mean verse-count per surah is 6236 / 114 = 54.70…

**Test**: Check whether the *count* of surahs whose verse-count is *factor of 6236* (i.e. divides 6236 evenly: divisors are 1, 2, 4, 1559, 3118, 6236) is unusual. Trivially small (only Q 1 has n=7, none of {1,2,4,1559,3118,6236} occur as actual surah lengths except possibly 1, which doesn't appear). This is documented as a sanity check, not a primary statistical test. We report the descriptive result without permutation.

**Result type**: Descriptive. Counted as **NULL** by default unless a structural pattern emerges.

(Note: this test is explicitly weakest of the five; included for completeness per task spec; we are honest that it is unlikely to produce signal.)

### Test 5 — Allah-density vs FR-distance to Q 1 al-Fātiḥa

**Classical claim**: Q 1 al-Fātiḥa is the *umm al-kitāb* (mother of the book) and contains a high concentration of divine names per verse. If it is the seed-vector around which the mushaf orbits, then surahs *closer* to Q 1 (in FR-roots-distance) should have *higher* Allah-density.

**Architectural prediction**: Spearman ρ(Allah-density per surah, d_FR(s, 1)) < 0 (negative correlation: closer surahs = denser).

**Statistic**:
- Allah-density per surah s := (# Allah-tokens in s) / n_verses(s) using the regex `الله` on the no-tashkeel text.
- d_FR(s, 1) from the [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] / [[h-new-111-fisher-rao-mushaf|h-new-111]] distance matrix.
- Spearman ρ over the 113 surahs s ≠ 1.

**Null**: ρ = 0 (no relationship).

**One-sided test**: Spearman p-value (negative direction) via SciPy.

**PASS**: p < 0.01.
**NULL**: p ≥ 0.01.

## Multiple-comparison plan

Five primary tests; α_bon = 0.05 / 5 = 0.01. Reported alongside uncorrected p for transparency.

## Rules-tuple

- Corpus: Hafs ʿan ʿĀṣim, no-tashkeel form (`quran-no-tashkeel.json`).
- Verse counts: `data/hafs-verse-counts.tsv`.
- FR-distances: `findings/phase-b-hypotheses/csv/h-new-111.json` D matrix.
- Divine names: `findings/phase-b-hypotheses/divine-names-by-verse.csv` (Allah-only count via regex on no-tashkeel JSON, NOT the names CSV — the CSV may exclude the bismillah's Allah token; we re-derive from raw text).
- Baseline corpus for Test 2: `data/baseline-corpora/raw/bukhari-noquran.txt`.
- Seed: 20260428. n_iter = 10⁵ for all permutation tests.

## Honest-limits clauses

1. **Test 1** has only ONE adjacent pair of interest; the empirical p is exactly rank/113 and is NOT corrected for any post-hoc selection (the choice of Q 8/Q 9 is pre-committed from classical literature).
2. **Test 2** uses Bukhari (hadith) which is structurally different from the Quran (multi-author corpus); the kink-50 model may simply not fit, which would produce a low R² that we interpret as DISTINCTIVE — but we'll report Bukhari's *best* simple model R² as a sanity check.
3. **Test 3** "19" claim originates with a single 20th-century author (Rashad Khalifa) whose work has been comprehensively refuted; we test it for completeness, expecting NULL.
4. **Test 4** is descriptive only.
5. **Test 5** depends on the Allah-token count being approximately Poisson-distributed across the 6236 verses (n_Allah ≈ 2700 in Hafs, ~0.43 per verse). Surahs of very small n_verses will have noisy density estimates, and we'll report Spearman (rank-based, robust) not Pearson.

## Pre-commit hash

This file's SHA256 will be recorded after writing and before running the script. The script computes its own input prereg hash for output JSON.
