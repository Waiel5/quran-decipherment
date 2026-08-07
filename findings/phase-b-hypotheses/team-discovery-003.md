---
finding_id: H-NEW-3
title: Canonical surah length-sequence has structure beyond "descending sort with noise" — specifically, lag-1 autocorrelation of log-ratios and Al-Fatiha's outlier position
date: 2026-04-12
rules_tuple:
  orthography: no-tashkeel
  word_definition: not-applicable (length = letter-graphemes)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
null_model:
  primary_naive: uniform permutation of 114 lengths (refuted as uninformative — see below)
  primary_real: Kendall-τ-matched permutation of descending-sorted lengths (controls for the fact that canonical order is already roughly descending)
acceptance_criterion: Bonferroni-corrected p < 0.005, z ≥ 3.0 under the τ-matched null
verdict: PARTIAL — two of four sub-claims survive a τ-matched null; two reduce to the known fact that canonical order is roughly descending.
---


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
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Claim

Three sub-tests on the 114 canonical surah letter-lengths:
(i) Kendall's τ of canonical order vs length (quantifies "descending-sortedness").
(ii) Simple-integer-ratio clustering in consecutive L(k+1)/L(k) values.
(iii) Bimodality in |log L(k+1)/L(k)| distribution.
(iv) Lag-1 autocorrelation of log ratios.

## The trap that came first

**Under a uniform permutation null** (all 114 surahs randomly reshuffled), observed statistics are spectacular:
- Kendall τ to descending: observed −0.837, null ≈ 0, SD 0.063 → z = −13.2
- Integer-ratio hits (targets {1/1, 2/1, 3/2, 4/3, 5/4, 3/1} at ±5% tolerance): observed 57/113, null mean 19.3, SD 3.9 → z = 9.6
- Lag-1 ACF log-ratios: observed −0.25, null −0.49, SD 0.066 → z = 3.6
- Bimodality coefficient: observed 0.76, null ≈ lower

**All four of these collapse to the single known fact**: canonical order is strongly descending by length. Once lengths are sorted descending, consecutive ratios ≈ 1, which trivially hits the "1/1" target, and log-ratio ACF is strongly negative. These z-scores are *one fact stated four ways.*

## The honest test: τ-matched null

I constrained the null to permutations whose Kendall τ to descending is within 0.03 of the observed τ (−0.837). Generated 2,000 such permutations via adjacent-swap walks from sorted descending.

**Under the τ-matched null:**

| Statistic | Observed | Null mean ± SD | z | p_ge (1-sided) |
|-----------|----------|-----------------|---|---------|
| Integer-ratio hits | 57 | 52.4 ± 4.88 | 0.94 | 0.21 |
| Lag-1 ACF log-ratios | −0.251 | −0.494 ± 0.073 | +3.34 | — |
| Bimodality coeff | 0.761 | 0.564 ± 0.047 | +4.16 | 0.0 |

- **Integer-ratio clustering**: NOT significant once descending-sort is controlled. Refutes "simple-ratio resonance" claim.
- **Lag-1 ACF less negative than null**: SIGNIFICANT (z = +3.34). Observed consecutive log-ratios are less anti-correlated than in comparable near-descending permutations. Physical meaning: when two consecutive surahs are both in a "size-plateau" region (similar lengths), the next transition is also small — consecutive ratios cluster in "plateau runs" rather than alternating.
- **Bimodality**: SIGNIFICANT (z = +4.16). But see below.

## Outlier sensitivity (disclosed forking path)

The bimodality is **dominated by surah 1 → 2**: |log(26249/143)| = 5.21, a ratio of ~183× (Al-Fatiha → Al-Baqara). Excluding this single transition:
- BC drops from 0.761 to **0.590** (right at the bimodality threshold 0.555, no longer strongly bimodal).

Therefore, the "bimodality" finding is really: **Al-Fatiha is anomalously short and then the Quran launches into the long Medinan surahs.** This is a well-known feature of the mushaf — Al-Fatiha is a liturgical opener, qualitatively different from the seven long surahs. It's a single structural fact, not a distribution-wide bimodal pattern.

The lag-1 ACF finding, by contrast, is NOT driven by a single outlier (verified by a leave-one-out sensitivity walk: all 113 leave-one-out versions retain z > 2.5 vs τ-matched null).

## Verdict: PARTIAL

**What survives:**
- Lag-1 autocorrelation of log-ratios is significantly less negative than τ-matched null (z = +3.34). Canonical order has "plateau runs" of similar-length surahs — the descending sort is applied in clusters, not monotonically-random.

**What is refuted:**
- Integer-ratio clustering does NOT exceed τ-matched null (z = 0.94). The apparent "simple-ratio hits" are just the consequence of descending sort making adjacent lengths similar.

**What is a single outlier, not a pattern:**
- The bimodality result (z = +4.16 naively) is driven by Al-Fatiha's anomalous shortness. Excluding it, BC falls to borderline.

## Garden of forking paths disclosure

### Choices made after seeing the data
- Introduced τ-matched null AFTER seeing that the uniform-permutation null was confounded with descending-sort. This is a correction to the null model, not to the statistic.
- Did leave-one-out sensitivity on BC after noticing Al-Fatiha outlier.

### Alternative rule tuples considered
- Could have used word-count or verse-count instead of letter-graphemes. Kendall τ for verse count is −0.68, weaker (more noise). Letter-count is the strictest length measure.

### Sibling hypotheses
- Revelation-order (tartib nuzuli) length-ratios: NOT tested. Would be a distinct claim.
- Surah-length as function of revelation chronology: separate test.

### Why this one and not those
- This is the exact statistic specified in the pre-registered hypothesis. Not rescuing by switching metrics.

## Seed
`random.seed(20260413)`. Raw: `scratch/team-discovery/result-003.json`, `result-003-v2.json` (τ-matched null).
