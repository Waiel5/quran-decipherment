---
id: H-NEW-82
title: Yā-Sīn (Q 36) as the "heart of the Quran" — multi-axis quantitative test
phase: B
status: NULL (Q 36 fails the pre-registered "heart" test on all 6 axes; MW-5 instrument check PASSES)
prereg: h-new-82-yasin-heart-prereg.md
script: scripts/h_new_82_yasin_heart.py
csv: findings/phase-b-hypotheses/csv/h-new-82.json
journal: journal/h-new-82-run-1.md
seed: 20260417
date: 2026-04-15
---

# [[h-new-82-yasin-heart|H-NEW-82]] — Yā-Sīn (Q 36) as "heart of the Quran" (results)

## TL;DR

Across **6 pre-registered operationalisations** of "heart" (mushaf
positional median, verse-count median, letter-count median, lexical
centroid by mean root-Jaccard, eigenvector centrality on the 114-surah
similarity graph, and cosine to the corpus theme-vector centroid), **Q 36
Yā-Sīn ranks #1 on zero axes and top-5 on zero axes**. The pre-registered
PASS threshold (#1 on ≥ 3 axes OR top-5 on ≥ 5 axes) is missed on every
axis. **Verdict: NULL.**

The MW-5 negative control passes cleanly: both Q 1 al-Fātiḥa (6/6 axes
in bottom half) and Q 114 al-Nās (6/6 axes in bottom half) are correctly
demoted by the instrument. The instrument is not biased toward corpus
endpoints; it correctly returns NULL for Q 36 even when the test is
constructed to favour mid-corpus, mid-length, lexically-rich surahs.

The classical hadith claim (Tirmidhī #2887, rated ḍaʿīf jiddan / mawḍūʿ
by al-Albānī) is **not corroborated by any of the 6 statistical axes**.

## Pre-registered axis × Q36 rank table

| axis                              | Q 36 rank | Q 36 score    | rank-1 surah | top-5 surahs                    |
|-----------------------------------|-----------|---------------|--------------|---------------------------------|
| A1 mushaf-position-median         | **43**    | −21.5         | Q 57         | 57, 58, 56, 59, 55              |
| A2 verse-count-median             | **88**    | −43.0         | Q 75         | 75, 78, 47, 80, 13              |
| A3 letter-count-median            | **76**    | −1615.0       | Q 54         | 54, 44, 53, 50, 51              |
| A4 lexical-centroid (mean Jacc.)  | **18**    | 0.1982        | Q 10         | 10, 40, 29, 39, 42              |
| A5 eigenvector-centrality         | **27**    | 0.1259        | Q 10         | 10, 40, 6, 39, 29               |
| A6 theme-centroid (cosine)        | **16**    | 0.9748        | Q 46         | 46, 23, 25, 57, 30              |

Bonferroni α_bon = 0.05 / 6 = 0.00833 (one-sided rank-discrete p ≤ rank /
114). Q 36 needs **rank ≤ ⌊0.00833 · 114⌋ + 1 = 1** to be Bonferroni-
significant. **0 / 6 axes Bonferroni-significant.**

Even at uncorrected α = 0.05 (rank ≤ 5), Q 36 is significant on
**0 / 6 axes**.

Median verse count across 114 surahs = 40. Median letter count (no-
tashkeel chars, no spaces) = 1477. Q 36 has 83 verses (more than 2× the
median) and ~3092 letters (more than 2× the median).

## A5 — bootstrap null on eigenvector centrality

Position-matched null (n = 10,000 random surah indices, observed
centrality at each). Observed Q 36 centrality = 0.12588.
**p = 0.2383** — Q 36 is firmly in the bulk of the centrality
distribution. Centrality #1 (Q 10 Yūnus) is 0.1502, ~19 % above Q 36.

## MW-5 instrument check (pre-locked, PASSES)

Pre-committed: at least one of {Q 1, Q 114} must rank > 57 on at least 4
of 6 axes. Otherwise INSTRUMENT_FAIL_NO_DECLARATION.

| control | A1   | A2  | A3  | A4   | A5   | A6  | n_in_bottom_half | passes |
|---------|------|-----|-----|------|------|-----|------------------|--------|
| Q 1     | 113  | 69  | 59  | 94   | 94   | 89  | **6 / 6**        | yes    |
| Q 114   | 114  | 73  | 69  | 100  | 102  | 99  | **6 / 6**        | yes    |

Both controls are correctly demoted on all six axes. The instrument is
not pathologically over-promoting Q 36's neighbours, mid-mushaf surahs,
or any other obvious confound class.

## PASS criterion verdict

PASS criterion (pre-locked):
- "Q 36 is rank #1 on ≥ 3 axes" — **NOT MET (0 / 6).**
- "Q 36 is top-5 on ≥ 5 axes" — **NOT MET (0 / 6).**

PARTIAL band (top-5 on 3–4 axes): NOT MET (top-5 on 0 / 6 axes).

**Verdict: NULL.**

## Q 36 ranks alongside all candidate "heart" surahs

Diagnostic-only table (not in pre-registered family). Surahs sometimes
nominated as a "heart" candidate in classical or popular sources:

| surah                           | A1   | A2   | A3   | A4   | A5   | A6   |
|---------------------------------|------|------|------|------|------|------|
| Q 36 (Yā-Sīn — the hadith pick) | 43   | 88   | 76   | **18** | 27   | **16** |
| Q 1  (al-Fātiḥa, control)       | 113  | 69   | 59   | 94   | 94   | 89   |
| Q 2  (al-Baqara)                | 111  | 114  | 114  | 45   | 38   | 34   |
| Q 18 (al-Kahf)                  | 79   | 98   | 102  | 42   | 39   | 24   |
| Q 50 (Qāf)                      | 15   | 11   | **4**  | 52   | 52   | 32   |
| Q 55 (al-Raḥmān)                | **5**  | 87   | 11   | 77   | 76   | 76   |
| Q 57 (al-Ḥadīd, positional median) | **1**  | 21   | 45   | 25   | 32   | **4** |
| Q 58 (al-Mujādilah)             | **2**  | 36   | 26   | 48   | 49   | 21   |
| Q 67 (al-Mulk)                  | 20   | 17   | 9    | 55   | 55   | 58   |
| Q 114 (al-Nās, control)         | 114  | 73   | 69   | 100  | 102  | 99   |

Highest-rank cells in **bold**.

Q 36 is most "heart-like" on **A4 (lexical centroid, rank 18)** and
**A6 (theme centroid, rank 16)**. These are the two centrality-of-content
axes — i.e. Q 36 *is* moderately central in vocabulary and theme — but
not dominantly so. Q 10 Yūnus, Q 40 Ghāfir, Q 39 al-Zumar, Q 29 al-
ʿAnkabūt, and Q 42 al-Shūrā all out-rank Q 36 on lexical centrality, and
Q 46 al-Aḥqāf, Q 23 al-Muʾminūn, Q 25 al-Furqān out-rank Q 36 on theme
centrality.

## Substantive interpretation

1. **The hadith claim is not a quantitative claim.** "Qalb al-Qurʾān"
   in the hadith literature is a liturgical / theological designation,
   parallel to "fātiḥat al-kitāb" (the Opener) for Q 1, "ḥādī al-Qurʾān"
   (the Crown) for Q 2, "ʿarūs al-Qurʾān" (the Bride) for Q 55, "qalb
   al-Qurʾān" for Q 36, and "asās al-Qurʾān" (the Foundation) for Q 1.
   These epithets describe ritual function (recitation over the dying,
   nightly recitation, Friday recitation), not statistical position.
   The hadith's chain itself is contested in classical ḥadīth criticism
   (al-Albānī: ḍaʿīf jiddan / mawḍūʿ via Hārūn Abū Muḥammad).

2. **Q 36 IS moderately content-central** (A4 rank 18, A6 rank 16),
   consistent with Q 36's reputation for distilling the central Meccan
   themes (tawḥīd, prophet-rejection, resurrection) in compact form.
   But "moderately central" is not "the heart"; many other Meccan and
   middle-Meccan surahs out-rank Q 36 on these axes.

3. **The actual positional and content centroids of the corpus.**
   - Positional median: **Q 57 al-Ḥadīd** (rank 1: |57 − 57.5| = 0.5).
     Tied at 0.5 with Q 58 al-Mujādilah. (Note: the literal exact median
     of 1..114 is between 57 and 58.) Q 57 al-Ḥadīd contains the famous
     "iron / 26 / al-Ḥadīd" verse cluster sometimes adduced for code-19
     claims. We do not endorse those claims here; the *positional median*
     finding is independent and follows trivially from arithmetic.
   - Lexical centroid (mean root-Jaccard, eigenvector centrality both):
     **Q 10 Yūnus** with Q 40 Ghāfir close behind. Q 10 is a long
     middle-Meccan surah covering tawḥīd, prophet-narratives (Nūḥ, Mūsā,
     Yūnus), the Day of Judgement, and Quranic self-reference; it
     overlaps lexically with most other long Meccan surahs by virtue of
     its breadth. The proximity of Q 40 (Ghāfir) at #2 hints that the
     **al-Ḥawāmīm cluster (Q 40-46)** sits at the lexical and thematic
     core of the mushaf, an observation independently noted in classical
     scholarship under "al-ḥawāmīm dībāj al-Qurʾān" (the brocade of the
     Quran).
   - Theme centroid: **Q 46 al-Aḥqāf**, the last of the al-Ḥawāmīm.

4. **Why Q 10 (Yūnus) and the al-Ḥawāmīm dominate centrality.** The
   eigenvector centrality of a surah on the root-Jaccard graph rewards
   surahs that share many roots with surahs that themselves share many
   roots. Long Meccan surahs covering the broad theological-prophetic
   curriculum (Q 10 Yūnus, Q 40 Ghāfir, Q 39 al-Zumar, Q 29 al-ʿAnkabūt,
   Q 6 al-Anʿām) collectively form a tightly-linked clique. Q 36, while
   thematically central, is shorter (~730 STEM tokens vs Q 10's ~1700)
   and so has a smaller distinct-root set, capping its centrality.

5. **MW-5 says the test is honest.** Q 1 and Q 114 are correctly
   demoted to the bottom half on all 6 axes — they are not promoted by
   any spurious feature of the test design. This is reassuring: the
   NULL verdict on Q 36 is not a measurement artefact.

## What the classical claim *could* be operationalised as

Three operationalisations the prereg explicitly excluded (because they
are not standard surah-level quantitative features) might still salvage
the classical claim:

- **Resurrection-pericope length.** Q 36:51-83 is a sustained
  resurrection scene. A surah-level measure would be "fraction of
  verses devoted to eschatology". Computing this honestly would require
  manually-coded pericope boundaries and was therefore not pre-locked.
- **Recitational frequency in classical practice.** A liturgy-weighted
  centrality (each surah weighted by its frequency in the prophetic
  sunna) might promote Q 36, given its standard recitation over the
  dying. This is a sociological / liturgical centrality, not a textual
  one.
- **Information density per word.** Compression-based or perplexity-
  based measures of how much the surah "summarises" the rest. We have
  `compression_per_surah.csv` from prior runs; it would be a separate
  hypothesis to register.

These are noted as possible follow-ups (H-NEW-82b…) but do not enter
the [[h-new-82-yasin-heart|H-NEW-82]] declaration.

## A6 theme-centroid notes (Q 46 ranks #1)

The theme palette T1–T8 was locked from the project's topical taxonomy
*before* inspecting Q 36's morphology. Q 46 al-Aḥqāf scores cosine =
0.9868 against the corpus theme centroid, narrowly ahead of Q 23
al-Muʾminūn (0.9864) and Q 25 al-Furqān (0.9853). Q 36 is rank 16
(cosine = 0.9748). The distance between rank 1 and rank 16 is small
(< 1.5 % cosine) — the entire top-30 surahs are within 2 % of each
other, indicating that the theme palette is broad enough that most
mid-length Meccan surahs cover most of it. This is a known limitation
of corpus-mean centroid measures on dense embeddings.

## Files

- Pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-82-yasin-heart-prereg.md`
- Script: `/Users/grey/Downloads/quran/scripts/h_new_82_yasin_heart.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-82.json`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-82-run-1.md`

## Verdict

- **Pre-registered PASS criterion**: NULL (0 / 6 axes Bonferroni-
  significant; 0 / 6 axes top-5; 0 / 6 axes rank-1).
- **MW-5 instrument check**: PASS (Q 1 and Q 114 both 6/6 in bottom
  half; instrument is honest).
- **Final verdict**: **NULL** — Q 36 Yā-Sīn is not the structural,
  positional, lexical, network-centrality, or theme-centrality "heart"
  of the Quran on any of the 6 pre-locked axes. The classical hadith
  claim is **not corroborated** by quantitative analysis.

The empirical content centroid of the mushaf is **the al-Ḥawāmīm cluster
(Q 40-46)**, and the empirical positional median is **Q 57 al-Ḥadīd**.
Q 10 Yūnus is the single most lexically-central surah by both mean
similarity and eigenvector centrality.
