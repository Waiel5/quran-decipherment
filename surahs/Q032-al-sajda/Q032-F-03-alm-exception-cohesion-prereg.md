---
test_id: Q032-F-03
title: "ALM-exception complement cohesion — Q 29, Q 30, Q 32 vs random 3-tuples"
date_locked: 2026-05-08
seed: 20260508
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q032-F-03-alm-exception
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q032-Q047-retry-specialist
parent_findings:
  - h-new-111 (Fisher-Rao distance matrix, corpus mean 0.9235)
  - H-NEW-53 book-reference test (post-hoc, p=10⁻¹², PASS-DIRECTED) — established that ALM-surahs minus exceptions all reference "the Book"
classical_anchors:
  - al-Suyūṭī, *al-Itqān*, nawʿ 40 (muqaṭṭaʿāt), discussion of ALM-cluster
  - al-Rāzī, *Mafātīḥ al-ghayb* (commentary on Q 32 opening)
---

# Q032-F-03 Pre-registration — ALM-exception complement Q 29 + Q 30 + Q 32 cohesion

## Hypothesis

The ALM-muqaṭṭaʿāt cluster comprises 6 surahs: Q 2, Q 3, Q 29, Q 30, Q 31, Q 32. Of these, Q 2, Q 3, Q 31 carry a clear *book-reference opening* (e.g., Q 2:2 ذلك الكتاب لا ريب فيه; Q 3:3 نزل عليك الكتاب; Q 31:2 تلك آيات الكتاب الحكيم). Q 29, Q 30, Q 32 do NOT include such an explicit "the book" reference at the opening verses — they form an *ALM-exception subset*.

The H-NEW-53 finding (book-reference correlation, p=10⁻¹²) established that ALM-cluster surahs preferentially reference "the Book" early. The 3 exceptions (Q 29, Q 30, Q 32) are an interesting structural sub-class — they share ALM but lack the book-reference signature.

**Question**: Are Q 29 + Q 30 + Q 32 FR-cohesive as a triplet, vs random 3-tuples drawn from the corpus?

## Pre-committed prediction (DIRECTION LOCKED)

**Direction-locked LOW**: mean pairwise FR distance over (Q29-Q30, Q29-Q32, Q30-Q32) is below the corpus median for random 3-tuples.

This is a *positive cohesion* prediction: even though they are book-reference *exceptions*, they share enough content-structural characteristics (e.g., post-Hijra-orientation late-Meccan, story-rich, eschatological) to cluster.

## Test (Bonferroni-1, single test)

**T1**: T_observed = mean(FR_29-30, FR_29-32, FR_30-32). Permutation null: 10000 random 3-tuples (any 3 distinct surahs). Direction-locked LOW: count perms where T_perm ≤ T_observed; p_low = (count + 1) / (n_perm + 1).

α = 0.05 (single test, no Bonferroni cost).

Reference values (pre-computed from h-new-111):
- FR(29, 30) = 0.9153
- FR(29, 32) = 0.9383
- FR(30, 32) = 0.9272
- Mean = 0.9269 (vs corpus mean 0.9235 — VERY CLOSE TO MEAN; this is honest pre-disclosure)

This is borderline; the test will likely produce p_low ≈ 0.50. Pre-commit acknowledged: this test may NULL because the 3 exception-surahs are mid-corpus-mean, not significantly cohesive.

## Direction-of-effect lock

Predicted direction: T_observed ≤ corpus-3-tuple median.
If T_observed > median: NULL — the exception-set is not FR-cohesive; book-reference-absence is not enough to cluster them.

## Success criteria

- VINDICATED: p_low < 0.05 (Q29+Q30+Q32 FR-cohesive at corpus-percentile bottom).
- DIRECTIONAL: 0.05 < p_low < 0.20 (suggestive but not conclusive).
- NULL: p_low ≥ 0.20.

## Garden-of-forking-paths log

- BEFORE running: pre-committed direction is LOW (cohesion). The values pre-loaded from h-new-111 above already suggest weak signal (0.9269 is just slightly below corpus mean 0.9235 — wait, 0.9269 > 0.9235, so actually slightly *above* corpus mean — this is a HONEST disclosure that the prediction may fail).
- CORRECTION: I am pre-committing direction-LOW based on the *theoretical* prediction that ALM-exceptions cluster, not based on the values. The honest expectation is that this test may NULL.
- BEFORE running: chose mean-of-3-pairs over min-of-3-pairs because mean is more robust.
- ALTERNATIVE-HYPOTHESIS-DECLARED: equal-prominence NULL is fully expected and would be reported as such. The book-reference-absence may NOT translate into content-cohesion (the muqaṭṭaʿāt are letter-axis ⊥ content-axis per established FALSIFICATION of al-Biqāʿī's munāsaba claim).
