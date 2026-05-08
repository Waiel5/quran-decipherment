---
test_id: Q047-F-03
title: "Q 47-Q 48-Q 49 architectural triplet cohesion — three consecutive Medinan surahs"
date_locked: 2026-05-08
seed: 20260508
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q047-F-03-triplet
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q032-Q047-retry-specialist
parent_findings:
  - h-new-111 (FR distance matrix; corpus mean 0.9235)
  - h-new-720 (canonical adjacency: Q47-Q48 delta=0.033 (CHEAP), Q48-Q49 delta=0.083)
  - cross-finding-026 (mushaf TSP-residual 11%)
classical_anchors:
  - al-Suyūṭī, *al-Itqān*, nawʿ 18 (tartīb tawqīfī)
  - al-Biqāʿī, *Naẓm al-Durar* (munāsabāt between Muḥammad–Fatḥ–Ḥujurāt)
---

# Q047-F-03 Pre-registration — Q 47-Q 48-Q 49 triplet cohesion

## Hypothesis

Q 47 (Muḥammad), Q 48 (al-Fatḥ), Q 49 (al-Ḥujurāt) are three consecutive Medinan surahs:
- Q 47 — pre/Hudaybiyya war-instruction (per al-Bukhārī tafsīr-bāb context)
- Q 48 — explicit Hudaybiyya/al-Fatḥ revelation (al-Bukhārī Hudaybiyya cycle)
- Q 49 — post-Hudaybiyya social/communal etiquette (Banū Tamīm delegation)

al-Biqāʿī (*Naẓm al-Durar*) reads them as a *thematic ring*: war → conquest → community-formation. The h-new-720 data shows Q 47-Q 48 has the cheapest adjacency cost in this region (delta=0.033, very cohesive); Q 48-Q 49 is also cheap (delta=0.083).

**Hypothesis**: The 3-tuple {Q 47, Q 48, Q 49} has a mean pairwise FR significantly below random 3-tuple permutation null.

## Pre-committed prediction (DIRECTION LOCKED)

**Direction-locked LOW**: T_observed = mean(FR_47-48, FR_47-49, FR_48-49) < corpus 3-tuple median.

Reference values (pre-computed from h-new-111):
- FR(47, 48) = 0.8893
- FR(48, 49) = 0.8584
- FR(47, 49) = will compute

Expected T_observed ≈ 0.87, which is below corpus mean 0.9235 — this triplet should clear the test.

## Test (Bonferroni-1)

**T1**: T_observed = mean of 3 pairwise FRs. Permutation null: 10000 random 3-tuples (any 3 distinct surahs from 114). p_low = (count perms with T_perm ≤ T_observed + 1) / (n_perm + 1).

α = 0.05 (single test).

## Direction-of-effect lock

Predicted: T_observed ≤ corpus-3-tuple-median.
If T_observed > median: NULL — Q 47-Q 48-Q 49 is not FR-cohesive as a triplet.

## Success criteria

- VINDICATED: p_low < 0.05 AND triplet-rank in bottom-quartile of consecutive triplets (rank ≤ 28 of 112).
- DIRECTIONAL: p_low < 0.10.
- NULL: p_low ≥ 0.10.

## Garden-of-forking-paths log

- BEFORE running: chose 3 consecutive Medinan surahs (Q 47-Q 48-Q 49) following the Q022-F-05 (Q 21-Q 22-Q 23) protocol exactly for replication validity.
- BEFORE running: predicted LOW based on h-new-720 cheap-adjacency observation (Q 47-Q 48 delta=0.033 is among the cheapest in corpus).
- ALTERNATIVE-HYPOTHESIS-DECLARED: if mean FR ≈ corpus-mean, the consecutive-Medinan-class doesn't sufficiently dominate to produce cohesion (each surah contributes its own structural-content axis).
- BEFORE running: chose mean-of-3 over min-of-3 (more robust); chose consecutive-triplet rank as descriptive statistic.
