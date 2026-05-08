---
test_id: Q022-F-02
title: "Q 22 hybrid Mecca-Medina bimodality at the verse level"
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q022-F-02-bimodality
alpha_bon: 0.025
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q022-al-hajj-specialist
---

# Q022-F-02 Pre-registration — Q 22 hybrid Mecca-Medina bimodality

## Hypothesis

Q 22 al-Ḥajj is classically described as MIXED Meccan/Medinan (al-Suyūṭī, *al-Itqān*, nawʿ 1 — some verses revealed in Mecca, others in Medina). The standard tafsir tradition (al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, intro to Q 22) flags vv. 19-24 as Medinan-Badr-context and vv. 25-30, 39-41 as Medinan-Hijra-context, while vv. 1-18 and 60-78 contain mixed registers.

If Q 22 truly has TWO chronological strata, the per-verse score on a Meccan-vs-Medinan feature axis should be **bimodal**, not unimodal.

## Pre-committed prediction

**Direction-locked**: the distribution of per-verse Meccan-feature-scores in Q 22 is **BIMODAL** (Hartigan's dip statistic significant at p<0.05 against unimodal null), and Silverman's bandwidth test rejects unimodality at p<0.05.

## Feature-axis construction

A simple feature-based "Meccan-likelihood" score per verse, using corpus-wide regularities (NOT a trained classifier — to avoid circularity).

Feature vector per verse v ∈ Q 22:
- f1: verse length (words). Meccan late tend to be SHORTER on average than Medinan; classical scholars note "Meccan: short rhythmic verses; Medinan: long legislative" (al-Suyūṭī *Itqān* nawʿ 1).
- f2: presence of *yā ayyuhā al-nāsu* (universal address) — Meccan-typical.
- f3: presence of *yā ayyuhā alladhīna āmanū* (believer-address) — Medinan-typical.
- f4: presence of legal/ritual keywords (حج، صلاة، زكاة، جهاد، قتال، أذن) — Medinan-skewed.
- f5: presence of eschatological keywords (الساعة، القيامة، اليوم، عذاب، يبعث) — Meccan-skewed.

**Score**: `meccan_score(v) = -z(f1) + f2 - f3 - f4 + f5`
(negative-Medinan + positive-Meccan signals).

## Tests (Bonferroni-2)

1. **T1 — Hartigan's dip test**: dip statistic for the meccan_score distribution across 78 verses against unimodal null. (Implemented via permutation: bootstrap 10000 resamples from a fitted Gaussian KDE matched on mean+var.)
2. **T2 — Silverman's bandwidth test**: critical bandwidth at which KDE has exactly 1 mode; bootstrap 10000 to test if data needs ≥2 modes.

α_bon = 0.025.

## Direction-of-effect lock

Predicted: BIMODAL. If unimodal (dip p>0.05 AND silverman p>0.05), publish as NULL — false the classical hybrid claim under this featurization.

## Garden-of-forking-paths log

- BEFORE running: features f1-f5 chosen from al-Suyūṭī *Itqān* nawʿ 1's qualitative Meccan/Medinan markers, NOT from inspecting Q 22's distribution.
- BEFORE running: standardization is z-score against ALL Q22 verses (within-surah z), not against full corpus, to avoid corpus-mean confound.
- BEFORE running: dip test implemented from Hartigan & Hartigan 1985 stdlib — no library dependency.
- BEFORE running: per-verse score, not per-verse-pair: the unit of bimodality test is the verse (al-Suyūṭī's contested-verses are at verse granularity).

## Success criteria

- VINDICATED: BOTH T1 AND T2 reject unimodality at α_bon=0.025.
- DIRECTIONAL: ONE of T1/T2 rejects.
- NULL: NEITHER rejects.

## Failure mode flag

If meccan_score has zero variance, mark NULL-DATA-GAP.
