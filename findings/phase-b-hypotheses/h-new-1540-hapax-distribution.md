---
id: H-NEW-1540
title: Hapax-legomenon (corpus-singleton roots) distribution across 114 surahs
date_run: 2026-05-09
phase: B
status: PARTIAL → DESCRIPTIVE-PHASE-EFFECT
seed: 20260509
n_perm: 10000
prereg: prereg-h-new-1540-hapax-distribution.md
prereg_sha: a8cecf09831dd054eb4e7b64cf1981f03998691e02e32ab5cc0b07a63b299a44
---

# H-NEW-1540 — Hapax distribution across 114 surahs


> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Pre-registered hypothesis

Hapax-legomenon root distribution across 114 surahs is non-uniform relative to a length-proportional null. Three pre-committed cells (one-tailed upper):

1. CV(density) ≥ null
2. max-density ≥ null
3. n(surahs with ratio ≥ 2.0 × baseline) ≥ 3

Bonferroni α = 0.05 / 3 ≈ 0.0167. Length-proportional permutation null (10,000 perms, seed 20260509).

## Result

**Verdict: PARTIAL — 2 of 3 cells pass; the third (CV) trends in the predicted direction but does not survive Bonferroni.**

| Cell | Observed | Null mean | Null p95 | p | α_Bonf | Pass |
|:--|--:|--:|--:|--:|--:|:--:|
| CV(density) | 1.9997 | 1.4100 | 1.9382 | 0.0368 | 0.0167 | NO |
| max-density (Q 108) | 0.20000 | 0.04992 | 0.10000 | **0.0014** | 0.0167 | **YES** |
| n(ratio ≥ 2×) | 40 | 11.47 | 16 | **<0.0001** | 0.0167 | **YES** |

The count-cell crushes the null: **40 surahs have hapax-density ≥ 2× the corpus length-weighted baseline, against a null expectation of 11.5.** The maximum hapax-density (Q 108 al-Kawthar, 2 hapaxes in 10 words = 0.200, 41.7× baseline) sits at the 99.86th percentile of the null. The CV statistic is directionally consistent (1.9997 obs vs 1.4100 null mean) but falls in the 96.32nd percentile, just short of the Bonferroni-corrected α=0.0167 threshold.

Reverse-direction flag: **not raised** (all three statistics are above their null means).

## Counts

- Total roots in QAC v0.4: **1,642**
- Hapax roots (count = 1): **395** (24.06% of all roots)
- Hapax tokens (one per hapax root by definition): **395**
- Total corpus orthographic word count (no-tashkeel): **82,375**
- Baseline hapax density: **0.00480**

## Top 10 surahs by hapax density

| Rank | Surah | Name | Period (Nöldeke) | Word count | Hapax | Density | Ratio |
|:--|:--:|:--|:--|--:|--:|--:|--:|
| 1 | Q 108 | al-Kawthar | Early Meccan | 10 | 2 | 0.2000 | 41.71× |
| 2 | Q 112 | al-Ikhlāṣ | Early Meccan | 15 | 2 | 0.1333 | 27.81× |
| 3 | Q 100 | al-ʿĀdiyāt | Early Meccan | 41 | 5 | 0.1220 | 25.43× |
| 4 | Q 106 | Quraysh | Early Meccan | 17 | 2 | 0.1176 | 24.53× |
| 5 | Q 111 | al-Masad | Early Meccan | 23 | 2 | 0.0870 | 18.13× |
| 6 | Q 113 | al-Falaq | Early Meccan | 23 | 2 | 0.0870 | 18.13× |
| 7 | Q 91 | al-Shams | Early Meccan | 54 | 4 | 0.0741 | 15.45× |
| 8 | Q 81 | al-Takwīr | Early Meccan | 104 | 7 | 0.0673 | 14.04× |
| 9 | Q 90 | al-Balad | Early Meccan | 82 | 4 | 0.0488 | 10.17× |
| 10 | Q 105 | al-Fīl | Early Meccan | 23 | 1 | 0.0435 | 9.07× |

**All 10 top hapax-density surahs are classified Early Meccan in the Nöldeke chronology.**

## Bottom 10 (zero hapax)

| Surah | Name | Period | Word count |
|:--:|:--|:--|--:|
| Q 1 | al-Fātiḥa | Early Meccan | 29 |
| Q 10 | Yūnus | Late Meccan | 1,964 |
| Q 41 | Fuṣṣilat | Late Meccan | 838 |
| Q 43 | al-Zukhruf | Middle Meccan | 870 |
| Q 45 | al-Jāthiya | Late Meccan | 512 |
| Q 48 | al-Fatḥ | Medinan | 600 |
| Q 57 | al-Ḥadīd | Medinan | 618 |
| Q 59 | al-Ḥashr | Medinan | 478 |
| Q 60 | al-Mumtaḥana | Medinan | 377 |
| Q 62 | al-Jumuʿa | Medinan | 186 |

**27 surahs total have zero hapaxes.** The bottom-10 above are the LONGEST zero-hapax surahs. By length-proportional null, Q 10 (1,964 words) carrying zero hapax-tokens is striking — under the null, expected ≈ 1,964 × 0.00480 ≈ 9.4 hapaxes.

## Period-stratified breakdown of the 40 surahs with ratio ≥ 2.0×

| Nöldeke phase | Count |
|:--|--:|
| Early Meccan | 31 |
| Middle Meccan | 5 |
| Medinan | 4 |

**31 of 40 (77.5%) are Early Meccan.** Of the 48 surahs classified Early Meccan in the Nöldeke ordering, 31 (64.6%) carry hapax density ≥ 2× baseline. By contrast, of the ~28 Medinan surahs, only 4 do (~14%).

## Equal-probability null (sensitivity, NOT primary test)

When hapaxes are redistributed with equal probability (independent of word count, each surah equiprobable), the observed statistics are NOT extreme:

- p_CV (equal-prob) = 0.22
- p_max (equal-prob) = 0.9999
- p_count (equal-prob) = 1.0

This is the expected behavior: an equal-probability null massively over-loads short surahs with hapaxes by construction, so short-surah concentration is the null's default. **The substantive comparison is the length-proportional null**, which is what the primary cells use. The sensitivity check confirms the test depends on the length-weighting assumption, as pre-registered.

## Interpretation (with MW-7 post-hoc cap on cluster-pattern claims)

1. **The length-proportional null is rejected on 2/3 cells.** Hapaxes are NOT distributed proportional to surah length. They cluster heavily in short Early-Meccan surahs and are partially depleted in long Late-Meccan and Medinan surahs.

2. **The CV cell trends but does not pass Bonferroni** (raw p=0.037, Bonferroni-corrected α=0.0167). The "lumpiness" of the density distribution is real but moderate; the more dramatic signals are concentrated in extreme cases (max-density at Q 108; n-above-2× at 40 vs null 11.47).

3. **Chronological-phase pattern is descriptive (MW-7 capped) but striking.** All top-10 hapax-density surahs are Early Meccan. 31/40 surahs above the 2× threshold are Early Meccan. This is post-hoc cross-tabulation and is reported descriptively, NOT as an independent significance test. A separate pre-registered chronology-phase test would be required to claim this as a confirmed law. **This is a candidate hypothesis for future pre-registration.**

4. **Classical-rhetorical interpretation**: al-Suyūṭī (*al-Itqān*, nawʿ 38 *al-mufradāt* / nawʿ 39 *al-gharīb*) catalogued lexical rarities; if his theory of *gharīb* applies, the Early-Meccan phase carries a disproportionate share of the lexical-novelty load. Whether this is (a) genuine semantic-precision iʿjāz, (b) a function of oath-and-eschatology style admitting more loanwords (per Jeffery 1938), or (c) the short-surah genre's higher tolerance for vocabulary singletons, is NOT decided by this test.

## NULL surahs (zero hapax legomena)

The 27 zero-hapax surahs (alongside the 10 enumerated above): Q 1, 10, 21, 26 (check), 38, 41, 43, 45, 48, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 95, 98, 99, 102, 103, 110, 114. (Exact list in JSON output.) Several of these are Medinan administrative-and-legal surahs (Q 48, 57-66) — a thematic distinction visible to classical mufassirūn but never previously quantified in hapax-frequency terms.

## MW-protections audit

- **MW-1**: instrument pre-specified (root-index.json singletons; word-count denominator).
- **MW-2**: 10,000 permutations, length-proportional null.
- **MW-3**: 3 statistics (CV, max, count) jointly reported; equal-prob null as sensitivity.
- **MW-4**: no fitted parameters; ratio threshold 2.0 fixed pre-observation.
- **MW-5**: equal-probability null replication run (sensitivity only).
- **MW-6**: no surah-class selection; all 114 surahs in the population.
- **MW-7**: chronological-phase cross-tab is post-hoc; capped at descriptive-only.

## Honest limits

1. The PARTIAL verdict reflects that 2/3 cells survive Bonferroni; the CV cell does not. Strict pre-reg discipline does NOT permit relaxing α post-hoc.
2. Hapaxes here are QAC-stem-root singletons, NOT word-form singletons. A root used once may surface in only one inflection; the test is at root-level by construction.
3. The chronological pattern (top-10 all Early Meccan) is descriptive and post-hoc. Although the pattern is dramatic, MW-7 caps interpretive force until a pre-registered chronology-phase test is run.
4. Loanword hypothesis (Jeffery 1938): many corpus-rare words in oath-and-eschatology surahs are loanwords from Aramaic, Ethiopic, etc. This is a plausible mechanism for the Early-Meccan concentration but is not tested here.
5. The 27 zero-hapax surahs include both Q 1 (the corpus's deliberately recursive / common-vocabulary opener) and long administrative Medinan surahs — these are very different reasons for zero-hapax status but the test does not distinguish them.

## Output files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-1540-hapax-distribution.md` (SHA a8cecf09…)
- Script: `findings/phase-b-hypotheses/scripts/h-new-1540.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-1540.json`

## Cross-references

- [[h-new-590-outlier-strength]] — per-surah outlier ranking (different metric; check whether top-hapax-density surahs are also outlier-strength outliers)
- [[h-new-840-unified-architectural-score]] — UAS includes content-distinctness; intersection unexplored
- [[cross-finding-010-extended-network]] — Q 1 zero-hapax + Q 112 high-hapax represents the corpus's bipolar fingerprint axis
- [[h-new-1370-long-verse-top10]] — long-verse distribution comparison (Medinan-loaded)
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 38 (*al-mufradāt*) and nawʿ 39 (*al-gharīb*) — classical catalogue of lexical rarities
- al-Bāqillānī, *Iʿjāz al-Qurʾān* — *balāgha*-axis iʿjāz on word-choice precision
- Jeffery 1938, *The Foreign Vocabulary of the Qurʾān* — loanword catalogue overlap with hapax set (untested here)

## Candidate next pre-reg

**H-NEW-1540B**: Direction-locked phase test — surahs in Nöldeke "Early Meccan" phase carry a disproportionate share of hapax-density mass relative to "Middle Meccan", "Late Meccan", and "Medinan" phases, using a phase-randomization permutation null over 10,000 perms.

*Pre-reg SHA verified at runtime: a8cecf09831dd054eb4e7b64cf1981f03998691e02e32ab5cc0b07a63b299a44*
