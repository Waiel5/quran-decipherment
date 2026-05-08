---
test_id: Q056-F-03
title: META-OATH (oath-about-an-oath-being-great) corpus rate — Q 56:75-76 as a structurally rare device
date: 2026-05-07
phase: B+
status: PRE-REGISTERED
investigator: Q056-al-waqia-specialist
seed: 20260507
n_perm: 0
bonferroni_k: 1
bonferroni_family: Q056-F-03-meta-oath
alpha_bon: 0.05
direction: Locked: META-OATH device occurs in ≤ 3 surahs corpus-wide (rare)
acceptance: ≥ 1 and ≤ 3 surahs contain the META-OATH pattern (oath-formula immediately followed by self-referential clause about the oath being great or sworn-by)
failure: > 3 surahs OR 0 surahs
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q056-F-03 Pre-Registration — META-OATH device rate

## Hypothesis

Q 56:75-76 contains the device:
> *fa-lā uqsimu bi-mawāqiʿ al-nujūm* (75) — oath-formula
> *wa-innahu la-qasamun law taʿlamūna ʿaẓīm* (76) — META-OATH ("and indeed it is a mighty oath if you knew")

The classical scholarship (al-Bāqillānī, *Iʿjāz al-Qurʾān*; al-Suyūṭī, *al-Itqān*, nawʿ on *aqsām al-Qurʾān*) treats v 76 as exceptional self-referential commentary on the oath itself.

**Pre-committed:** the same META-OATH structure (oath-formula + immediate following verse asserting the oath's magnitude using *qasamun* / *qasam* / *yamīn* / equivalent) occurs in ≤ 3 surahs in the corpus.

## Method

1. Identify all *qasam*-formula triggers in the corpus: verses opening with *wa-* + by-noun or *lā uqsimu bi-* / *uqsimu bi-* / *fa-lā uqsimu*.
2. For each trigger, examine the immediately-following verse.
3. Flag a META-OATH if the next verse contains *qasamun* OR *la-qasamun* OR equivalent self-referential predicate about the oath.
4. Count surahs containing ≥ 1 META-OATH.

## Acceptance / failure

- 1 ≤ count ≤ 3 surahs: VINDICATED (rare device)
- count > 3: NULL (more common than expected)
- count = 0: pre-commit violation (Q 56 itself must count) → debug pipeline
