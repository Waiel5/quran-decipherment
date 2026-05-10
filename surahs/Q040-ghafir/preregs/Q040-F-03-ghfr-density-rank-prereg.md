---
id: Q040-F-03
title: Q 40 *ghfr*-root density corpus rank
date_locked: 2026-05-09
phase: B
status: pre-registered
---

# Q040-F-03 — *ghfr*-root density corpus rank

## Hypothesis (DIRECTION-LOCKED, before observation)

**H1**: Q 40 (named *Ghāfir*, "The Forgiver", from Q 40:3 *ghāfir al-dhanb wa-qābil al-tawb*) is in the **top-5** of all 114 surahs by *ghfr*-root density (root-tokens per 1000 orthographic tokens, no-tashkeel).

Direction: rank(Q 40) ≤ 5.

## Theoretical motivation

The surah's primary classical name *Ghāfir* derives from Q 40:3, which is one of the most cited divine-attribute verses in classical theology (al-Suyūṭī *al-Itqān*, nawʿ 17 on surah-names; al-Bāqillānī on Qurʾān names). If the name reflects lexical density (parallel to Q 23 al-Muʾminūn = top-1 *ʾmn*; Q 58 al-Mujādila = high *jdl*), Q 40 should be in the top-5 of *ghfr*-density. The pre-registered direction is the naming-density hypothesis.

## Pre-committed protocol

- Source root index: `data/morphology/root-index.json` key `gfr`.
- Per-surah count: number of attestations of root `gfr` where attestation[0] == s.
- Per-surah token denominator: total whitespace-split tokens across all verses, source `quran-text/quran-no-tashkeel.json`.
- Density: count / tokens × 1000.
- Rank: descending by density; ties broken by higher raw count, then lower surah number.

## Verdicts

| Outcome | Verdict |
|:--|:--|
| rank(Q 40) ≤ 5 | DIRECTIONAL VINDICATION |
| 5 < rank(Q 40) ≤ 20 | PARTIAL (naming-density-weak) |
| rank(Q 40) > 20 | NULL — naming-density does not drive ranking |

If NULL: the surah's naming reflects narrative-thematic (Q 40:3 divine-attribute verse) NOT lexical-density framing — a substantive contrast with Q 23 *Muʾminūn* and Q 58 *Mujādila*.

## Honest limits

1. Short surahs with 1 token of *ghfr* and small token denominators (e.g., Q 110, 20 tokens, 1 *ghfr*) can mathematically dominate the per-1000 rate. The pre-reg accepts this as the operational definition; secondary descriptive ranks (raw count, length-thresholded) reported but not pre-committed.
2. Root key `gfr` from QAC v0.4; lemma vs stem-root sensitivity acknowledged (§1.4).

*Locked 2026-05-09.*
