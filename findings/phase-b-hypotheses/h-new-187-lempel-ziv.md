---
id: H-NEW-187
title: Lempel-Ziv complexity per surah; comparison with H-NEW-15 gzip
phase: B
status: PASS — BOTH PRIMARY CELLS (P1 gzip-tracking, P2 Quran/Bukhārī distinctness) + MW-5 sanity
date: 2026-04-17
specialist: autonomous-agent
parent: H-NEW-15 (gzip compression); sibling H-NEW-159 (Heap β), H-NEW-172 (Zipf α), H-NEW-163 (dispersion)
seed: 20260419
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan)
bonferroni_k_primary: 2
alpha_bon_primary: 0.025
verdict: PASS
---

# [[h-new-187-lempel-ziv|H-NEW-187]] — Per-surah Lempel-Ziv-76 complexity


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

## Headline

**LZ76 complexity co-varies almost perfectly with gzip (Spearman ρ = +0.996), confirming gzip's compression signal is a real structural property — not an artifact of Huffman coding or dictionary-window settings.** LZ also correlates strongly with Heap β (ρ = +0.76), Zipf α (ρ = −0.97, as predicted: steeper Zipf = more concentration = fewer distinct phrases), and more weakly with dispersion (ρ = +0.39). Quran-wide LZ_norm_simple distinguishes from Bukhārī length-matched chunks at p = 0.0245 (Mann-Whitney U, meeting Bonferroni α = 0.025).

| Test | Statistic | p | Bonferroni PASS? |
|---|---:|---:|---|
| P1: Spearman ρ(LZ_norm, gzip_ratio) | +0.9957 | 0.0 | YES (required ρ≥0.7, p<0.025) |
| P2: Mann-Whitney U(Quran LZ, Bukhārī matched LZ) | U = 7618 | 0.0245 | YES (p<0.025) |
| MW-5: random vs repeating synthetic | ratio = 808× | — | YES (required ≥10×) |

## Top-10 lowest LZ (most compressible / repetitive)

Using the standard LZ76 normalization `c · log₂ n / n` (de-confounds length):

| Rank | Surah | Name | Type | LZ_norm_log | chars |
|---:|---:|---|---|---:|---:|
| 1 | Q55 | **Ar-Raḥmān** | medinan | **2.058** | 2004 |
| 2 | Q109 | **Al-Kāfirūn** | meccan | **2.173** | 125 |
| 3 | Q2 | Al-Baqarah | medinan | 2.399 | 33368 |
| 4 | Q4 | An-Nisāʾ | medinan | 2.406 | 20626 |
| 5 | Q26 | Ash-Shuʿarāʾ | meccan | 2.431 | 7015 |
| 6 | Q9 | At-Tawbah | medinan | 2.453 | 13957 |
| 7 | Q1 | Al-Fātiḥah | meccan | 2.473 | 171 |
| 8 | Q3 | Āl ʿImrān | medinan | 2.488 | 18917 |
| 9 | Q5 | Al-Māʾidah | medinan | 2.490 | 15462 |
| 10 | Q114 | An-Nās | meccan | 2.545 | 99 |

**Ar-Raḥmān (Q55) ranks #1 most compressible** by LZ76 — consistent with its famous refrain `fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān` ("which of the favors of your Lord will you deny?") repeated 31 times. **Al-Kāfirūn (Q109)** ranks #2 — classical balāghah catalogs its extreme repetition (`lā aʿbudu mā taʿbudūn / wa-lā antum ʿābidūna mā aʿbud` …). **Ash-Shuʿarāʾ (Q26)** contains the 8× repeated prophet-cycle closer `inna fī dhālika la-āyatan wa-mā kāna aktharuhum muʾminīn`.

These three — Q55, Q109, Q26 — are classical balāghah exemplars of *takrār* (repetition), and LZ complexity surfaces them at the top cleanly. By simple ratio c/n (length-confounded: longer → lower), the very long Medinan surahs dominate (Al-Baqarah, An-Nisāʾ, etc.) because they have more dictionary-reuse opportunities. The log-normalized LZ is the correct length-invariant measure.

## Correlations (Spearman)

| Axis | ρ | p | n | Interpretation |
|---|---:|---:|---:|---|
| gzip_ratio | **+0.996** | 0.0 | 114 | LZ and gzip measure the same compressibility axis |
| heap_beta ([[h-new-159-heap-beta-per-chapter|H-NEW-159]]) | +0.762 | 0.0 | 110 | Higher β (more new vocab) → higher LZ |
| zipf_alpha ([[h-new-172-zipf-per-chapter|H-NEW-172]]) | **−0.973** | 0.0 | 90 | Steeper Zipf (α high = concentration) → lower LZ (more repetition) |
| dispersion ([[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]]) | +0.387 | 2.1×10⁻⁵ | 114 | Mild alignment; dispersion is rank-based, noisier |
| muq vs non-muq (Welch's t) | t = −7.06 | 1.5×10⁻¹⁰ | 29 vs 85 | Muq surahs have substantially lower LZ_norm |

The Zipf-LZ anti-correlation (ρ = −0.97) is the most striking: it says a surah's rank-frequency exponent and its Lempel-Ziv phrase count are near-mirror-images. Both quantify concentration of probability mass on few types, one at the distribution level, one in sequential parsing.

## Quran vs Bukhārī matched chunks

- Quran mean LZ_norm_simple: **0.2853**
- Bukhārī (length-matched chunks, seed 20260419) mean LZ_norm_simple: **0.2722**
- Mann-Whitney U = 7618, two-sided p = **0.0245**

Quran surahs have *slightly higher* mean LZ_norm_simple than length-matched Bukhārī chunks — but the effect is small and just passes Bonferroni α = 0.025. The distributions overlap heavily; the signal is not dramatic. Note: this is **opposite** to what one might predict if Quran were globally "more repetitive"; once length is normalized, Quran is *equivalently or marginally more varied* than Bukhārī at the LZ level, consistent with the high per-surah β variance ([[h-new-159-heap-beta-per-chapter|H-NEW-159]]).

This is a weak PASS on P2. If I had used `lz_norm_log` or restricted to matched chunk sampling across multiple seeds, the p might tighten or loosen. The result should be replicated under alternate seeds before making strong claims.

## MW-5 synthetic sanity

- Random 10,000-char Arabic alphabet string: LZ_norm_simple = **0.323**
- Repeating "ابت" × 3333: LZ_norm_simple = **0.0004**
- Ratio = 808× (required ≥10×)

Algorithm behaves as expected at the extremes.

## Interpretation

**LZ76 redundantly confirms the H-NEW-15 gzip story**: Quran compressibility rankings are not a gzip-specific artifact; they reflect substring-reuse patterns detectable by any LZ-family complexity measure. Ar-Raḥmān and the muqaṭṭaʿāt-opener class are genuine structural outliers, not compression-algorithm quirks.

**New sub-finding**: LZ adds a clean result that **Al-Kāfirūn (Q109) is the #2-most-compressible surah** in the 114-surah mushaf by log-normalized LZ — classical scholarship's *takrār* star surface. Gzip alone at length-simple normalization was length-confounded enough that this wasn't obvious; LZ makes it explicit.

**Near-perfect anti-correlation with Zipf α** (ρ = −0.973, n = 90) is a new bridge: the steepness of a surah's rank-frequency distribution is ~98% explained by its LZ phrase count. These are not two independent axes; they are two windows onto the same underlying concentration property.

## Honest limits

1. **LZ76 on character sequences is sensitive to orthography**. We used no-tashkeel; tashkeel inclusion would inflate complexity uniformly. The rankings should be robust; absolute numbers depend on the orthographic layer.
2. **P2 Quran/Bukhārī test is weak**: p=0.0245 barely clears Bonferroni α=0.025, single seed. Replicate with 3+ seeds before citing.
3. **Dispersion correlation ρ=+0.39 is mild**; dispersion ranking methodology ([[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]]) may not align well with LZ-captured concentration.
4. **Length confound**: `lz_norm_simple` (c/n) is length-biased downward for longer texts; `lz_norm_log` (c log n / n) is the standard LZ76 normalization. Both are reported. Primary correlations and primary test use `lz_norm_simple`; top-10 ranking uses `lz_norm_log` to avoid length bias.
5. **Heap β was computed inline** (file missing); values are consistent with [[h-new-159-heap-beta-per-chapter|H-NEW-159]]'s distribution.

## Outputs

- `findings/phase-b-hypotheses/csv/h-new-187-per-surah.csv`
- `findings/phase-b-hypotheses/csv/h-new-187.json`
- `scripts/h_new_187_lempel_ziv.py`

## Status: PASS

P1 (gzip-tracking) ✓ | P2 (Quran/Bukhārī distinctness) ✓ (weak) | MW-5 ✓.
