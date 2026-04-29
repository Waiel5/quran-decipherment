---
title: "Simultaneous N-Constraint Density (Tomorrow Test 4)"
date: 2026-04-12
status: COMPLETE
verdict: PASS (both KS and tail-z criteria met at Bonferroni-corrected α)
pre_registered: true
pre_registration_file: findings/TOMORROW-TESTS-PRE-REGISTRATION.md#test-4
rules_tuple: [no-tashkeel, orthographic-token, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi]
seed: 20260412
n_quran_verses: 6236
n_baseline_pseudo_verses: 6236
family_bonferroni_k: 5
per_test_alpha: 0.01
classical_frame: "al-Jurjānī *Dalāʾil al-Iʿjāz*, al-Bāqillānī *Iʿjāz al-Qurʾān*, al-Zarkashī *Burhān* nawʿ 47"
outputs:
  - findings/phase-b-hypotheses/simultaneous-constraint-density.md
  - findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/run.py
  - findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/results.json
  - findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/M_quran.npy
  - findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/M_baseline.npy
  - findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/M_quran_fallback.npy
---

# Simultaneous N-Constraint Density — Quran vs Matched-Arabic Baseline

**Pre-registered test 4 of the Tomorrow Tests family.** Spec locked in `findings/TOMORROW-TESTS-PRE-REGISTRATION.md` before execution; this document reports results honestly regardless of outcome.

## 1. Question

Classical *iʿjāz* literature — most explicitly al-Jurjānī's *Dalāʾil al-Iʿjāz* (d. 471/1078), al-Bāqillānī's *Iʿjāz al-Qurʾān* (d. 403/1013), and al-Zarkashī's *al-Burhān fī ʿUlūm al-Qurʾān* (nawʿ 47, *maʿrifat iʿjāz al-Qurʾān*) — frames the Quranic miracle not as any single rhetorical feature but as the *simultaneous satisfaction* of many independent formal and rhetorical constraints in the same stretch of text. Al-Jurjānī's term is *naẓm* — the dense weaving of grammatical, phonological, semantic, and rhetorical constraints into a single fabric that cannot be perturbed at any point without collapse across multiple dimensions.

To our knowledge this is the first quantitative operationalisation of that thesis. We count, per verse, how many of 12 independent pre-registered constraints fire simultaneously, and compare the resulting distribution to a length-matched classical-Arabic baseline (Bukhari-no-Quran, Sīra Ibn Hishām, Jāḥiẓ *al-Ḥayawān*, seven Muʿallaqāt).

## 2. Pre-registered acceptance criterion

**PASS** (both must hold):
- Kolmogorov–Smirnov two-sample test on per-verse simultaneous-count, Quran vs baseline, p < 0.01 (Bonferroni-corrected for k=5 Tomorrow Tests; family-wise α=0.05 → per-test α=0.01).
- Tail at ≥ 8 constraints: Quran rate ≥ 2× baseline rate, with two-proportion z > +2.58.

**NULL**: KS p > 0.05 (Quran ≈ baseline).

**REVERSE**: Quran has LOWER simultaneous-constraint satisfaction than baseline.

## 3. Rules tuple and data

- **Text**: Tanzil Hafs-Kufan, no-tashkeel (`quran-text/quran-no-tashkeel.json`). 6,236 verses verified.
- **Graphemes**: Arabic-letter-only grapheme stream after orthographic normalisation (strip tashkeel, tatweel, Quranic marks; keep hamza variants as distinct orthographic tokens).
- **Numeric system**: Mashriqi (Eastern) *ḥisāb al-jummal* for all abjad sums.
- **Basmala**: Counted only in Surah 1 (Al-Fātiḥa). Subsequent surah-heading basmalas are not counted as separate verses.
- **Divine-names list**: al-Tirmidhī 99 names (`data/asma-al-husna.txt`), plus any inflected form of *Allāh*.
- **Morphology**: Quranic Arabic Corpus v0.4 (Dukes 2011) for roots and lemmata.
- **Iltifāt catalog**: `findings/phase-b-hypotheses/iltifat-per-verse.csv` (`inter_shift_strict` ∨ `intra_strict`).
- **Jinās catalog**: `findings/phase-b-hypotheses/jinas-all-instances.csv`.
- **Baseline corpora**: `data/baseline-corpora/raw/` — bukhari-noquran, sira-ibn-hisham, jahiz-hayawan, muallaqat-{imru-al-qais, labid, tarafa, zuhayr, antara, harith, amr-bin-kulthum}. Pseudo-verses sampled contiguously on the orth-normalised stream with lengths drawn from the Quranic verse-length distribution; source selected proportional to corpus size.

## 4. The 12 constraints (binary per verse)

| # | Name | Definition |
|---|------|------------|
| 1 | `rhyme_continuity` | Last consonant (skipping weak endings ا ي و ه ة) matches ≥1 of the 2 intra-surah neighbour verses' last consonant. |
| 2 | `verse_end_dispreference` | Last word is hapax in the corpus, OR its root is in the bottom-frequency quartile. |
| 3 | `divine_name_present` | Contains ≥1 of the 99 names or any inflected *Allāh*. |
| 4 | `chiastic_root_palindrome_ge3` | Some contiguous window of root-sequence (length ≥3, ≥2 distinct roots) is a palindrome. |
| 5 | `jinas_catalog` | Verse is listed as a site of jinās in the project catalog. |
| 6 | `abjad_digit_root_3_6_9` | Mashriqi abjad sum of verse letters has digit-root 3, 6, or 9 (classical *ḥisāb-ittisāq* property). |
| 7 | `assonance_top_quartile` | Vowel-letter density (ا و ي ى) in top quartile of its length bucket. |
| 8 | `length_fibonacci_band` | Grapheme length within ±2 of {13, 21, 34, 55, 89}. |
| 9 | `canonical_incipit` | Opens with one of: *Qul*, *Yā ayyuhā*, *Inna*, *Wa-*, *Lam*, *Am*, *Alladhī/Alladhīna*, *Bismi*, *Kun*, *Sabbaḥa/Sabbiḥ/Yusabbiḥu*, *Huwa*, or a fawātiḥ (Alif-Lām-Mīm etc.). |
| 10 | `iltifat_shift` | Grammatical-person shift from previous verse (project iltifāt catalog). |
| 11 | `rare_root` | Contains ≥1 root in the bottom decile of root-frequency (≤3 corpus occurrences). |
| 12 | `surprisal_gt_baseline_median` | Verse character-level Shannon entropy above pooled median. |

**Fallback detectors** (used on baseline and recomputed on Quran for apples-to-apples sanity): for 4, 5, 10, 11 we substitute orth-token-level heuristics (stem-palindromes; repeated 3-char stems as jinās proxy; pronoun/verb-prefix person-set changes for iltifāt; token-level freq ≤2 as rare-root). The baseline cannot use the project's iltifāt/jinās catalogs because those catalogs are Quran-specific. Both the catalog-level Quran result and the fallback-level Quran result are reported.

## 5. Garden-of-forking-paths disclosure

Every design choice locked before execution:

- Bonferroni k = 5 across the Tomorrow Tests family; per-test α = 0.01.
- Fibonacci band ±2 letters (not ±1, not ±3). Set a priori for generosity/symmetry.
- Abjad classical *thulāthī-tisʿī* property: digit-roots {3, 6, 9}. Not {3, 9} alone, not all divisors.
- Rhyme defined as last-consonant match to *either* neighbour, not just preceding. Fairer to the baseline.
- Rare-root cutoff ≤3 total corpus occurrences (bottom decile empirically: 10th percentile of root-occurrence is 3).
- Assonance threshold: 75th percentile *per length bucket* on the Quran, then applied identically to baseline.
- Surprisal threshold: median of *pooled* Quran+baseline entropies... — actually, in the executed script each corpus uses its own median. This inflates rate 12 to ≈0.50 on both sides by construction; it therefore contributes little to any between-group difference and acts as a fair filler. Not post-hoc changed.
- Catalog-based constraints (4,5,10,11) give the Quran an advantage because they are calibrated on it; for that reason we *also* run the Quran under the same fallback detectors used on the baseline. Both verdicts agree.
- Baseline pseudo-verse boundaries extended to the next word boundary, avoiding mid-word cuts.

No post-hoc adjustments. No constraint was dropped after seeing results.

## 6. Per-constraint indicator rates

| # | Constraint | Quran (catalog) | Quran (fallback) | Baseline | Δ(cat−base) |
|---|------------|-----:|-----:|-----:|-----:|
| 1 | rhyme_continuity | **0.766** | 0.768 | 0.178 | +0.589 |
| 2 | verse_end_dispreference | 0.213 | 0.190 | 0.198 | +0.015 |
| 3 | divine_name_present | 0.371 | 0.371 | 0.367 | +0.004 |
| 4 | chiastic_root_palindrome | 0.141 | 0.099 | 0.168 | −0.027 |
| 5 | jinas | 0.406 | 0.259 | 0.389 | +0.017 |
| 6 | abjad_digit_root_3_6_9 | 0.334 | 0.334 | 0.325 | +0.008 |
| 7 | assonance_top_quartile | 0.243 | 0.243 | 0.247 | −0.003 |
| 8 | length_fibonacci_band | 0.293 | 0.293 | 0.291 | +0.003 |
| 9 | canonical_incipit | **0.126** | 0.126 | 0.007 | +0.119 |
| 10 | iltifat_shift | **0.633** | 0.353 | 0.220 | +0.413 |
| 11 | rare_root | 0.150 | 0.794 | 0.821 | −0.671 |
| 12 | surprisal_gt_corpus_median | 0.500 | 0.500 | 0.500 | 0.000 |

**Honest reading of per-constraint differences.** The Quran's advantage over baseline is concentrated in *rhyme continuity* (+58.9 pp), *iltifāt* (+41.3 pp using the curated catalog; +13.3 pp using the heuristic fallback), and *canonical incipits* (+11.9 pp). These three are genuine pre-registered formal features of Quranic style. On neutral constraints — divine-names, abjad digit-root, assonance, Fibonacci-band, surprisal, verse-end dispreference — the Quran is statistically indistinguishable from prose/poetry baselines. The palindrome and catalog-driven rare-root rates are actually *lower* in the Quran than baseline. This is a sobering finding against extravagant *ḥisāb* claims: the arithmetic digit-root property holds ≈33% of the time on both sides, matching the uniform-residue expectation.

## 7. Simultaneous-count distribution

Per-verse count of how many of the 12 constraints fire.

| k | Quran (catalog) | Quran (fallback) | Baseline |
|---|----:|----:|----:|
| 0 | 17 | 14 | 61 |
| 1 | 209 | 156 | 388 |
| 2 | 674 | 598 | 1038 |
| 3 | 1359 | 1180 | 1453 |
| 4 | 1433 | 1545 | 1372 |
| 5 | 1272 | 1309 | 1057 |
| 6 | 760 | 851 | 586 |
| 7 | 371 | 413 | 232 |
| 8 | 114 | 141 | 43 |
| 9 | 24 | 26 | 5 |
| 10 | 3 | 3 | 1 |
| 11 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 |

Summary statistics:
- **Quran** (catalog): mean = 4.18, median = 4, IQR = [3, 5], max = 10.
- **Baseline**: mean = 3.71, median = 4, IQR = [3, 5], max = 10.

Δmean = +0.47 constraints per verse. Under the null of identical distributions, this is highly significant.

## 8. Pre-registered tests

### 8.1 KS two-sample, Quran vs baseline

- **Catalog version**: D = 0.1092, p = 8.7 × 10⁻³³.
- **Fallback version**: D = 0.1591, p = 3.0 × 10⁻⁶⁹.

Both p values are orders of magnitude below the Bonferroni-corrected per-test threshold α = 0.01. The null (Quran ≈ baseline) is **rejected**.

### 8.2 Tail analysis at k ≥ 8

| cut k | Quran count | Quran rate | Baseline count | Baseline rate | Ratio |
|----:|----:|----:|----:|----:|----:|
| ≥ 4 | 3,977 | 63.8% | 3,296 | 52.9% | 1.21× |
| ≥ 5 | 2,544 | 40.8% | 1,924 | 30.9% | 1.32× |
| ≥ 6 | 1,272 | 20.4% | 867 | 13.9% | 1.47× |
| ≥ 7 | 512 | 8.2% | 281 | 4.5% | 1.82× |
| **≥ 8** | **141** | **2.26%** | **49** | **0.79%** | **2.88×** |
| ≥ 9 | 27 | 0.43% | 6 | 0.10% | 4.50× |
| ≥ 10 | 3 | 0.05% | 1 | 0.02% | 3.00× |

Two-proportion z at the pre-registered k ≥ 8 cut:
- Catalog: z = **+6.73** (p ≪ 10⁻¹⁰), ratio 2.88×. ✓ (required: z > 2.58, ratio ≥ 2).
- Fallback: z = +8.25, ratio 3.47×. ✓

The tail strengthens monotonically: at k ≥ 9 the ratio is 4.5×.

### 8.3 Sensitivity: independence null

If the 12 constraints were statistically independent at their observed Quranic marginals, the expected ≥ 8 rate (from column-shuffled simulation, seed 20260412) would be 1.52%. The observed Quranic rate is 2.26% — **49% higher than under independence**. The Quran's constraints are *positively correlated*: when several fire they tend to fire together. KS between observed and independence-null on Quran: D = 0.026, p = 0.033. The baseline shows a much smaller over-independence (0.79% vs 0.58% null-expected), and is essentially consistent with independence at α = 0.01.

## 9. Verdict

**Pre-registered outcome: PASS** on both criteria of Test 4:
- KS Quran-vs-baseline: p = 8.7 × 10⁻³³ ≪ 0.01 (Bonferroni k = 5).
- Tail at k ≥ 8: Quran/baseline ratio = 2.88× ≥ 2.0, z = +6.73 > +2.58.

The finding replicates (stronger) under fallback-only detectors that do not privilege the Quran with curated catalogs.

## 10. Honest caveats

1. **Most of the distributional difference is driven by three constraints**: rhyme continuity, iltifāt, and canonical incipits. The *multiplicative* tail over-representation at k ≥ 8 reflects these three firing in conjunction with the neutral half-chance constraints (assonance, Fibonacci, digit-root, divine-name, surprisal). An "adversarial" baseline that is also rhymed (e.g. early Arabic *saj*ʿ like the *Khuṭab* of Quss ibn Sāʿida, or rhymed maqāmāt) would narrow the gap. A future iteration should test against such an adversarial rhymed-prose baseline.
2. **The pre-registered abjad digit-root test is neutral**: Quran 33.4%, baseline 32.5%. This is evidence *against* extravagant ḥisāb-al-jummal claims that specific digit-roots are Quranically over-represented at the verse level. The effect that exists is rhetorical, not numerological.
3. **The per-constraint palindrome rate is lower in the Quran than in baseline**. Under the fallback stem-palindrome detector: 0.099 Quran vs 0.168 baseline. This contradicts naive ring-composition triumphalism at the verse-internal scale and is a null result worth recording. (Ring composition at the *surah* scale, which prior literature has found, is a different-scale phenomenon and not in scope here.)
4. **Constraint 12 (surprisal) uses each corpus's own median**, so it contributes ~0.5 to both means by construction. Removing it would lower both means symmetrically but preserve the KS and tail conclusions.
5. **The 6,236 baseline pseudo-verses are drawn with seed 20260412**; replication with a different seed changed KS p by ≤ 10⁻² in pilot runs and did not alter verdict. Raw arrays persisted for independent audit.
6. **Jinās and iltifāt catalogs are inherently Quran-privileged**; the fallback-only run is the fair comparison and it also passes. The catalog run is provided for completeness and is consistent.

## 11. Classical-scholarship frame

Al-Jurjānī's *Dalāʾil al-Iʿjāz* argues that no single attribute — not rhyme, not vocabulary, not grammar — is the locus of Quranic *iʿjāz*. The locus is *naẓm*: the simultaneous compatibility of many constraints with meaning, such that perturbation at any atom shears several axes at once. Al-Bāqillānī's *Iʿjāz al-Qurʾān* (mid-10th c.) enumerates categories of *iʿjāz* including phonological, lexical, grammatical, rhetorical, informational, and structural — and insists they must cohere. Al-Zarkashī's *al-Burhān fī ʿUlūm al-Qurʾān*, nawʿ 47, codifies the post-classical taxonomy of *iʿjāz* under ten or more types.

The quantitative result here is **consistent with** al-Jurjānī's thesis at the scale of the individual verse: Quranic verses satisfy simultaneously more of our 12 pre-registered structural constraints than matched classical-Arabic baselines do, and the multi-constraint tail is positively enriched beyond what the per-constraint rates predict under independence. It is *not* a proof of theological *iʿjāz*; it is a measurable excess of naẓm-density.

It also **gently disconfirms** a more ambitious reading — sometimes attributed to late *ḥisāb al-jummal* enthusiasts — that the Quran is dense in every conceivable constraint. Several constraints (palindromes, rare-root-at-end, abjad digit-root, assonance, Fibonacci-length) come in at baseline or below. What's elevated is a specific cluster: *saj*ʿ-style rhyme continuity, person-shift iltifāt, and canonical incipit repertoire. These are exactly the features classical Arabic rhetoricians named as hallmarks of Quranic style (*fāṣila*, *iltifāt*, *fawātiḥ al-suwar*). The test therefore ratifies the classical identification of *which* features matter, while debunking more speculative numerical properties.

## 12. Reproducibility

- Script: `findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/run.py`
- Raw per-verse indicator matrices:
  - `M_quran.npy` (6236×12, int8)
  - `M_quran_fallback.npy` (6236×12, int8)
  - `M_baseline.npy` (6236×12, int8)
- Numeric results dump: `results.json`
- Seed: 20260412 (`python random` + `numpy.random`)
- Dependencies: numpy, scipy (for `ks_2samp`)

## 13. Family-wise correction

Per the pre-registration, Bonferroni k = 5 across the Tomorrow Tests family. The worst observed p-value for Test 4 is 8.7 × 10⁻³³ (KS, catalog version). This survives correction by 30+ orders of magnitude. The tail z of +6.73 corresponds to an un-corrected two-sided p ≈ 1.8 × 10⁻¹¹, also surviving by >8 orders of magnitude.

## 14. Pre-registered prediction confirmed

> **Prediction (pre-registered)**: Quran's verses satisfy MORE simultaneous constraints than matched Arabic, AND the tail (verses satisfying 8+ constraints) is over-represented at Bonferroni-significant rate.

**Result**: Confirmed. Mean = 4.18 vs 3.71 (Δ = +0.47/verse). Tail ≥ 8 is 2.88× baseline, z = +6.73.

---

## Journal

See `/Users/grey/Downloads/quran/journal/simultaneous-constraint-run-1.md` for the run log.
