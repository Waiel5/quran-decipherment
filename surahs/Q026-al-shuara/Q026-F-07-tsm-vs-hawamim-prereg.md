---
prereg_id: Q026-F-07
title: TSM (Q 26 ↔ {Q 27, Q 28}) FR-distance vs Q 26 ↔ ḥawāmīm {Q 40-46}
date_locked: 2026-05-09
seed: 20260509
rules_tuple: (no-tashkeel, QAC-stem-root probability vector, Fisher-Rao, basmala-counted-only-in-Q1, Hafs-Kufan)
bonferroni_family: Q026-F-06..F-07 (k=2); α_per_test = 0.025
direction_locked_before_observation: yes
---

# Q026-F-07 — TSM-cluster FR proximity vs ḥawāmīm-cluster proximity

## Hypothesis (locked, one-sided)

In the precomputed 114×114 Fisher-Rao distance matrix `h-new-111.json`
(QAC stem-root probability vectors), Q 26 is **closer in mean FR-distance
to its own muqaṭṭaʿ TS-family {Q 27, Q 28} than to the contiguous ḥawāmīm
cluster {Q 40, Q 41, Q 42, Q 43, Q 44, Q 45, Q 46}**.

Direction: **mean d_FR(Q26, {Q27,Q28}) < mean d_FR(Q26, {Q40..Q46})**
(one-sided lower tail on the difference).

This pre-reg tests whether Q 26 sits closer to its 3-letter TSM/TS family
or to the 2-letter ḥawāmīm (HM) family. If TSM-closer: muqaṭṭaʿ letter-set
identity has FR-content correlate at least at the 3-letter scale. If
ḥawāmīm-closer or null: the 3-letter TSM family is FR-orthogonal even
relative to a different letter-family of comparable size — strengthens
the H-NEW-600 multi-NULL streak.

## Method

1. Load `findings/phase-b-hypotheses/csv/h-new-111.json` (114×114 FR
   distance matrix).
2. `d_TSM` = mean( d_FR(Q26,Q27), d_FR(Q26,Q28) ).
3. `d_HM`  = mean over k ∈ {40..46} of d_FR(Q26, Qk).
4. Δ = d_TSM − d_HM. Pre-committed direction: Δ < 0.
5. Null: 10,000 permutations, each draws a random pair (size 2) and a
   random 7-tuple of distinct surahs ≠ 26, computes the analog Δ_null.
   p_perm = fraction of null draws with Δ_null ≤ Δ_obs (one-sided lower tail).

Seed: 20260509.

## Pass criterion

Δ_obs < 0 AND p_perm < α_per_test = 0.025 (one-sided lower tail).

## Fail / NULL criteria

- p_perm ≥ 0.025 → NULL.
- Δ_obs > 0 (TSM-family is FURTHER than ḥawāmīm) → PRE-COMMIT VIOLATION,
  published as such per protocol §1.3.

## Honest limits (pre-stated)

- The HM cluster is contiguous (Q 40-46, 7 surahs) whereas TSM is 3 surahs;
  the test uses MEAN distance (not sum or min) to normalize for set size.
- The null draws random pairs and random 7-tuples without restricting to
  muqaṭṭaʿ-opened surahs. A more conservative null (matched-by-muqaṭṭaʿ-status)
  is a follow-up.
- This is a *content-axis* test on FR-roots, not a *letter-axis* test. The
  muqaṭṭaʿ-content NULL streak (H-NEW-600 + Q026-F-02 + Q026-F-04) predicts
  NULL here too. If TSM-closer wins, it would be a rare PASS for
  muqaṭṭaʿ-family content-cohesion at the 3-letter scale.

## Cross-references

- [[h-new-111]] — 114×114 FR matrix.
- [[h-new-600-letter-families]] — multi-NULL muqaṭṭaʿ-content-cohesion streak.
- [[Q026-F-02]] — TSM 4-axis NULL.
- [[Q026-F-04]] — Mūsā-block muqaṭṭaʿ-twin FALSIFIED.
