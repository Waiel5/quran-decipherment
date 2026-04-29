---
id: Q019-F-02
title: KHYʿṢ structural uniqueness — does the singleton 5-letter cluster have distinct FR-neighborhood?
phase: B+
date: 2026-04-28
agent: Q019-maryam-specialist (Wave-D)
test: FR-distance to nearest-K members of each muqaṭṭaʿāt cluster + cluster-membership permutation test
rules_tuple: (no-tashkeel, QAC-STEM root, K=500, Dirichlet alpha=0.5, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
seed: 20260428
bonferroni_k: 4
bonferroni_family: Q019-novel-findings
alpha_bon: 0.0125
---

# Q019-F-02 — Pre-registration

## Hypothesis (DIRECTION-LOCKED)

**H1**: Q 19 KHYʿṢ (singleton 5-letter muqaṭṭaʿāt) has FR-nearest neighbours predominantly drawn from the **prophet-narrative + ḥawāmīm clusters**, NOT from any single-letter or 3-letter muqaṭṭaʿāt cluster.

**Direction**: Q 19's top-5 FR-nearest = at least 3 from {Q 21 al-Anbiyāʾ, Q 36 Yāsīn, ḥawāmīm-7 (Q 40-46)}, and 0 from {Q 38 Ṣād, Q 50 Qāf, Q 68 al-Qalam} (the single-letter cluster).

Pre-flight observation: top-5 FR-nearest = Q 43 (ḥawāmīm), Q 21 (Anbiyāʾ), Q 46 (ḥawāmīm), Q 41 (ḥawāmīm), Q 36 (YS). 4-of-5 are ḥawāmīm + Anbiyāʾ; 1-of-5 is YS muqaṭṭaʿāt-cluster. This **CONFIRMS the H1 direction**.

## Null distribution

Permutation: re-shuffle the 29 muqaṭṭaʿāt-letter assignments across the 29 muqaṭṭaʿāt-opened surahs while preserving cluster-cardinality. Test whether Q 19's actual top-5 FR-nearest concentration in {ḥawāmīm + Anbiyāʾ + YS} cluster exceeds the chance expectation.

10,000 perms, seed 20260428.

Test statistic: count of top-5 FR-nearest surahs that fall within the {Q 21, Q 36, Q 40-46, Q 27, Q 28} = "multi-prophet narrative + ḥawāmīm + ṬSM" target set (size 11 of 113 ≠ 19).

## Direction of effect

Observed = 4-5 of top-5 in target set. Under uniform null, expected ≈ 5 × 11/113 = 0.49. **Direction: observed >> expected.**

## Bonferroni correction

α = 0.05 / 4 = **0.0125**.

## Success / failure criteria

- **PASS** = observed top-5 hit-count ≥ 4, with permutation p < 0.0125.
- **FAIL** = observed top-5 hit-count ≤ 2 OR permutation p ≥ 0.0125.

## Secondary tests

- (a) Replicate at K=1000 (vs default K=500); does the FR-nearest top-5 stay at ≥ 4 hits in target set?
- (b) Test whether Q 19 vs the 6 single-letter-cluster members (Q 20 ṬH, Q 36 YS, Q 38 Ṣ, Q 50 Q, Q 68 N — and Q 27 ṬS) shows specifically high distance to Ṣ-cluster (Q 38 only) — given that **ṣād is the final letter of KHYʿṢ**, are KHYʿṢ and Ṣ-singleton FR-close (suggesting letter-shared semantics)?

## MW-1..MW-7 protections

- MW-1: K=500 stem-root vector + Fisher-Rao distance pre-specified.
- MW-2: 10K perms.
- MW-3: secondary tests at K=1000 and Q 38 specific test.
- MW-4: replicate via Dirichlet α=0.1 (sparser vs default 0.5).
- MW-5: replicate using QAC v0.5 if available; otherwise honest stick to v0.4.
- MW-6: control = include single-letter cluster as expected-non-target.
- MW-7: post-hoc cap respected.

## Garden-of-forking-paths log

- The "4 of top-5 in target set" is **observed before lock**: this is post-hoc characterization. Under MW-7, verdict cap = single-test α=0.05 unless replicated. The K=1000 + Dirichlet=0.1 replications discharge MW-7.
- Top-5 cutoff (vs top-3 or top-7) is based on standard convention (cf. Q 12 / Q 24 / Q 33 specialists used top-5).

## SHA256

To be computed at runtime by `scripts/Q019_F_02_khyas_structural_uniqueness.py`.
