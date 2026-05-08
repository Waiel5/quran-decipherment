---
surah: 7
test_id: Q007-F-04
title: Adam-narrative inner-structure twin — Q 7:11–25 vs Q 2:30–39 vs Q 20:115–126
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q007-F-01..F-04
alpha_bon: 0.0125
direction_locked: positive — Q 7:11–25 ↔ Q 2:30–39 root-cosine similarity > Q 7:11–25 ↔ Q 20:115–126
rules_tuple: (no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q007-F-04 — Pre-registration: Adam-narrative twin

## 1. Hypothesis (locked before observation)

The Quran narrates Adam's creation, the prostration of angels and Iblīs's refusal, the garden-trial, the descent (`hubūṭ`), and the divine guidance-promise in three principal blocks:

| Block | Verses | Length | Style |
|:---|:---|:-:|:---|
| Q 2:30–39 | 10 verses | mid-length | Medinan, "extended-Adam" |
| Q 7:11–25 | 15 verses | longer | Late-Meccan, "extended-Adam" |
| Q 20:115–126 | 12 verses | shorter | Mid-Meccan, "brief-Adam" (per al-Rāzī) |

**H1 (one-tailed):** Q 7:11–25 and Q 2:30–39 are the **extended-Adam pair**; Q 7 ↔ Q 2 root-cosine similarity is HIGHER than Q 7 ↔ Q 20 root-cosine similarity AND HIGHER than Q 2 ↔ Q 20.

Equivalently:
- d(Q 7-Adam, Q 2-Adam) < d(Q 7-Adam, Q 20-Adam)
- d(Q 7-Adam, Q 2-Adam) < d(Q 2-Adam, Q 20-Adam)
- (Margin) min(d(Q 7,Q 20), d(Q 2,Q 20)) − d(Q 7,Q 2) > 0

**H0**: The three Adam-blocks are roughly equidistant (margin near zero or negative).

## 2. Operational definition

For each of the 3 blocks, build TF over QAC stem-roots (sum of all root-tokens within the block's verses; `data/morphology/root-index.json`).

Pairwise root-cosine distance: d_cos = 1 − cos(V_i, V_j).

(MW-1: same operationalization as Q026-F-04 for cross-test consistency.)

## 3. Test statistic

**Primary**: pre-committed margin = min(d(7,20), d(2,20)) − d(7,2). Direction LOCKED positive (Q 7 ↔ Q 2 closer than either to Q 20).

**Permutation null** (10,000 perms, seed 20260507): randomly partition the union vocabulary into 3 blocks preserving block sizes; compute null margin distribution.

p_perm_one_sided = fraction of perms with null_margin ≥ observed.

## 4. Success / Failure

- **CONFIRMED**: margin > 0 AND p_perm ≤ 0.0125.
- **DIRECTIONAL**: margin > 0 AND p_perm ≤ 0.05.
- **NULL**: margin ≤ 0 OR p_perm > 0.05.
- **PRE-COMMIT VIOLATION**: margin < 0 AND p_perm ≥ 0.95 (i.e., Q 7 is closer to Q 20 than to Q 2 — strong direction-flip).

## 5. Honest limits

1. **Block sizes differ** (Q 7: 15 verses, Q 2: 10 verses, Q 20: 12 verses). Cosine on TF is invariant to total mass but NOT invariant to vocabulary-set richness; longer blocks have more "stuff." We do NOT length-normalize beyond cosine; the choice is locked.
2. **Q 26-F-04 PRE-COMMIT-VIOLATED** the analogous Mūsā-twin test. If the same operationalization fails here too, the empirical direction would be that **muqaṭṭaʿ-letter-family-based content-similarity prediction is unreliable across the corpus**, even for narrative-twin pairs. We are testing here a DIFFERENT axis: not muqaṭṭaʿ-family but length-class (extended vs brief).
3. **Q 2:30–39 contains the angel-prostration scene; Q 20:115–126 is briefer**. Q 7's extended Adam-Iblīs dialogue (vv 12–18) might match Q 2's angel-dialogue (vv 30–34) more than Q 20's brief recap. Direction is locked positive accordingly.
4. **The Adam-narrative is also in Q 15:26–43, Q 17:61–65, Q 18:50–51, Q 38:71–85**. These are NOT in the H1 test (we lock the 3 most-extended in the standard scholarly grouping). They could be added in a follow-up replication.

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots, root-cosine-distance, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q007_F_04_adam_twin.py`.
