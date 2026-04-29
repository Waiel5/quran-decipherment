---
id: H-NEW-400
title: "Q 62 al-Jumuʿa outlier-candidate test — does the classical 4-cluster meta-hub surah disrupt cohesion like Q 55?"
phase: B
status: PRE-REGISTERED 2026-04-21
date: 2026-04-21
agent: team-lead (inline; ID 400 to skip codex sequential)
parent_1: H-NEW-340 (musabbiḥāt-block-subset {57, 59, 61, 62, 64} at 8.1%ile)
parent_2: H-NEW-390 (Q 55 outlier-exclusion +32.6pp improvement)
parent_3: NEXT-AGENT-PROMPT (Q 62 flagged as "4-cluster meta-hub")
seed: 20260507
bonferroni_k: 2
bonferroni_family: h-new-400-q62-outlier-candidate
alpha_bon: 0.025
n_perm: 10000
rules_tuple: "(musabbiḥāt-block MINUS Q 62 = {Q 57, 59, 61, 64} N=4; baseline = H-NEW-340 {Q 57, 59, 61, 62, 64} at 8.1%ile N=5; FR from H-NEW-111; 10000-perm null; seed 20260507)"
direction: "Cell A exclusion-subset d̄ < null 2.5%ile AND p<α_bon; Cell B comparison-delta: removing Q 62 improves percentile by ≥5pp (modest threshold given N=4 tiny)"
verdict: PENDING
---

# [[h-new-400-q62-outlier-candidate|H-NEW-400]] — Q 62 al-Jumuʿa outlier-candidate test

## 1. Question

[[h-new-390-q55-outlier-exclusion|H-NEW-390]] confirmed Q 55 al-Raḥmān as moderate cohesion-disruptor (+32.6pp). Is Q 62 al-Jumuʿa — classically designated "4-cluster meta-hub" per NEXT-AGENT-PROMPT and featured in 4 classical groupings (musabbiḥāt, Medinan-back, community-legal, Friday-prayer) — ALSO an outlier-disruptor?

If YES: the outlier-factor generalizes to multiple surahs; the cohesion model has ≥2 known outlier-candidates.

If NO: Q 55's outlier status is singular; Q 62's "meta-hub" status may not translate to outlier-disruption in content-axis.

## 2. Hypothesis

**H1 (Q 62 is 2nd outlier)**: removing Q 62 from [[h-new-340-musabbihat-block-subset|H-NEW-340]]'s musabbiḥāt-block {Q 57, 59, 61, 62, 64} improves cohesion by ≥5pp.

**H0 (Q 62 is not outlier)**: removal produces negligible change (~0pp ± 5pp).

Pre-committed direction: ≥5pp improvement for H1.

## 3. Protocol

1. FR matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
2. Exclusion subset: {Q 57, 59, 61, 64} N=4.
3. Compute d̄.
4. Null: 10000 random 4-surah draws.
5. Compare vs [[h-new-340-musabbihat-block-subset|H-NEW-340]] baseline {Q 57, 59, 61, 62, 64} N=5 at 8.1%ile.
6. Q 62's pairwise FR distances to other musabbiḥāt-block members reported descriptively.

## 4. Bonferroni + honest limits

k=2, α_bon=0.025.

At N=4, null variance is extreme; strict α unlikely. Descriptive delta is primary insight.

## 5. Pre-committed predictions

If Q 62 is an outlier: pairwise distances from Q 62 to Q 57/59/61/64 should be notably higher than intra-{57,59,61,64} distances. Removing Q 62 pulls d̄ down ~0.05-0.10; percentile drops ~5-10pp.

If Q 62 is NOT outlier: distances are uniform; removal barely moves percentile.

Modal expectation: Q 62 is LIKELY NOT a content-outlier (it's mainline musabbiḥāt Medinan-community surah). Predicted: H_0 — minimal change. Pre-committed direction for H_1 includes the null alternative as possibility.

## 6. Classical anchor

- Q 62 al-Jumuʿa opens with *yusabbiḥu li-Llāhi...*; Q 62:9-11 contains the classical Friday prayer institution
- Ibn Kathīr *Tafsīr* Q 62 on the uniqueness of Friday prayer
- al-Biqāʿī *Naẓm al-Durar* Q 61→62→63 munāsabāt

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_400_q62_outlier_candidate.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-400.json`
- Findings: `findings/phase-b-hypotheses/h-new-400-q62-outlier-candidate.md`

Pre-reg locked 2026-04-21.
