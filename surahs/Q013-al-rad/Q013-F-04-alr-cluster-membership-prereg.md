---
surah: 13
test_id: Q013-F-04
title: "ALR-cluster geographic-vs-letter membership — is Q 13 FR-close to ALR-siblings (mushaf-adjacent) despite ALMR letter-set?"
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q013-F-family-2026-05-07
alpha_bon: 0.01
n_perm: 10000
---

# Q013-F-04 — Pre-registration: ALR-cluster membership of Q 13

## 1. Hypothesis (locked before observation)

Q 13 is mushaf-positioned IN-BETWEEN the ALR cluster {Q 10, 11, 12} (left) and {Q 14, 15} (right) — it is geographically-WITHIN the ALR-cluster band, even though its letter-set is ALMR (not ALR). The classical letter-family work [[h-new-610-letter-families]] established ALR-5 NULL on whole-surah FR cohesion (56.25%ile) — i.e., the ALR cluster is united by NAME-CLASS, not by content-cohesion. Q 13 is therefore a **structural ambiguity**: is it FR-close to the ALR siblings (membership-by-mushaf-position despite letter-set difference), or FR-distant (true outsider)?

**H1 (locked direction)**: Q 13's mean FR distance to the 5 ALR siblings (`d̄_Q13→ALR`) is **NOT SIGNIFICANTLY DIFFERENT FROM** the ALR-internal pairwise mean distance (`d̄_ALR-internal`, computed over the 10 unordered pairs of Q 10/11/12/14/15). I.e. Q 13 is "as FR-close" to the ALR siblings as ALR siblings are to each other — empirically a 6th-cluster-member-by-distance.

**Operational test statistic**: `Δ = d̄_Q13→ALR − d̄_ALR-internal`. Pre-commit: |Δ| ≤ 0.05 (small absolute difference at the FR-roots scale where typical pairwise distances are 0.7-1.3).

**Alternative direction (also locked)**: Q 13 IS membership-by-distance even more strongly — `d̄_Q13→ALR < d̄_ALR-internal` (Q 13 is closer to ALR-siblings than they are to each other).

**H0**: Q 13 is significantly FARTHER from ALR-siblings than ALR-siblings are from each other (Δ > 0.05) — i.e. Q 13 is a true outsider.

**Direction (locked)**: Q 13 IS FR-close to ALR cluster (membership-by-distance). Specifically: `d̄_Q13→ALR ≤ d̄_ALR-internal + 0.05`.

## 2. Operational definition

ALR siblings: {Q 10, 11, 12, 14, 15}.

`d̄_Q13→ALR = (1/5) · Σ_{s∈ALR} FR(13, s)`.
`d̄_ALR-internal = (1/10) · Σ_{(a,b) ∈ pairs(ALR)} FR(a, b)` where pairs are the 10 unordered combinations.

Reference null: 10000 random "swap-Q13-out-and-replace" permutations. For each permutation: sample a random non-ALR-non-Q13 surah s' uniformly from {1, ..., 114} \ ({13} ∪ ALR). Compute `d̄_s'→ALR = (1/5) · Σ_{s∈ALR} FR(s', s)`. Distribution of `Δ' = d̄_s'→ALR − d̄_ALR-internal` defines the null.

**Permutation p-value**: fraction of 10000 random `s'` substitutions where `Δ' ≤ Δ_observed` (Q 13 outranks the random surah on FR-closeness).

## 3. Test statistic

**Primary**: `Δ_observed` and corresponding p_perm (fraction of permutations with `Δ' ≤ Δ_observed`).

**Pre-committed acceptance window**:
- p_perm ≤ α_bon = 0.01 → CONFIRMED (Q 13 is significantly FR-closer to ALR cluster than a random non-ALR surah would be).
- 0.01 < p_perm ≤ 0.05 → DIRECTIONAL.
- p_perm > 0.05 → NULL (Q 13 is not FR-distinctively close to ALR siblings).

## 4. Success / Failure

- **CONFIRMED**: Δ ≤ 0.05 AND p_perm ≤ 0.01 → Q 13 is FR-close to ALR cluster as a 6th-member-by-distance, even though letter-set differs.
- **DIRECTIONAL**: Q 13 close but not at α_bon level.
- **NULL**: Q 13 is FR-distant from ALR cluster comparably to a random surah.
- **Pre-commit violation**: Q 13 is FR-DISTANT from ALR cluster (Δ > 0.05 with high confidence).

## 5. Honest limits known a priori

- The ALR cluster is itself NULL on whole-surah cohesion (H-NEW-610). The internal pairwise mean is therefore relatively HIGH (close to corpus typical ~0.95). The threshold |Δ| ≤ 0.05 is a small absolute difference.
- We are testing whether Q 13 fits the cluster's loose pattern, not whether the cluster is internally tight.
- The test does NOT assume ALR is content-cohesive; it asks whether Q 13's distance-to-ALR is comparable to the cluster's own internal-distance (i.e., consistent with cluster-membership).
- An alternative null: random-5-member subsets of all 114 surahs. We pre-commit to single-surah substitution for Q 13 (the more conservative test; substituting a random surah for Q 13 at fixed ALR membership).

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Source: H-NEW-111 D matrix (`findings/phase-b-hypotheses/csv/h-new-111.json`).

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q013_F_04_alr_cluster_membership.py`.

## 8. Garden-of-forking-paths

- Considered: also testing Q 13's distance to ALM cluster (already done in F-01). REJECTED for F-04: F-01 covers ALM; F-04 is specifically about ALR-mushaf-neighbor membership.
- Considered: testing each ALR sibling individually rather than the 5-mean. PRE-COMMITTED to the 5-mean to avoid 5-cell sub-test inflation.
- Considered: weighting by mushaf-distance (Q 12 nearer than Q 15 than Q 10). REJECTED: free parameter.
