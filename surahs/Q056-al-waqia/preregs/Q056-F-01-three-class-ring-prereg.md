---
test_id: Q056-F-01
title: Q 56 al-Wāqiʿa — 3-class RING ARCHITECTURE: lexical correspondence between vv 10-56 (Day-of-Judgment 3-class block) and vv 88-94 (death-moment 3-class block)
date: 2026-05-07
phase: B+
status: PRE-REGISTERED
investigator: Q056-al-waqia-specialist
seed: 20260507
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q056-F-01-ring-coherence
alpha_bon: 0.01667
direction: Locked: corresponding-pair lexical-overlap MUST EXCEED non-corresponding-pair lexical-overlap
acceptance: corresponding-pair Jaccard > non-corresponding-pair Jaccard at p_bon < 0.0167 in ≥ 2 of 3 cells
failure: 0/3 or 1/3 cells pass; OR direction reverses
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q056-F-01 Pre-Registration — 3-class RING ARCHITECTURE

## Hypothesis

Q 56 has a unique 3-class human-classification architecture:

**Block A (vv 10-56 = Day of Judgment, full descriptions):**
- A.1 Sābiqūn al-muqarrabūn (vv 10-26)
- A.2 Aṣḥāb al-Yamīn (vv 27-40)
- A.3 Aṣḥāb al-Shimāl (vv 41-56)

**Block B (vv 88-94 = death-moment, abbreviated):**
- B.1 al-muqarrabūn (vv 88-89)
- B.2 aṣḥāb al-yamīn (vv 90-91)
- B.3 al-mukadhdhibūn al-ḍāllūn (vv 92-94)

**Pre-committed direction:** the lexical-overlap (Jaccard on no-tashkeel orthographic tokens) between corresponding-pair (A.1↔B.1, A.2↔B.2, A.3↔B.3) is HIGHER than between non-corresponding cross-pairs (A.1↔B.2, A.1↔B.3, A.2↔B.1, A.2↔B.3, A.3↔B.1, A.3↔B.2).

## Null distribution

For each of 3 corresponding-pair Jaccard values, permute the assignment of B.1/B.2/B.3 labels across {88-89, 90-91, 92-94} (3! = 6 permutations only) — too few. Instead, use **token-level permutation**: randomly shuffle the tokens of vv 10-56 across the 3 A-blocks (preserving block size) and re-compute correspondence-Jaccard, 10000× (seed 20260507). Report Bonferroni-3 p-values.

## Tests (3-cell family, α_bon = 0.05/3 = 0.01667)

- F-01.a: J(A.1, B.1) > 95th percentile of permuted-J(A.1, B-class-1)
- F-01.b: J(A.2, B.2) > 95th percentile of permuted-J(A.2, B-class-2)
- F-01.c: J(A.3, B.3) > 95th percentile of permuted-J(A.3, B-class-3)

## Stop-conditions

- Direction-reversal in any cell (corresponding < permuted-mean) → publish as PARTIAL/NULL with prominence
- Tie or non-significance after Bonferroni → NULL with prominence

## Rules-tuple sensitivity

Primary: orthographic tokens (no-tashkeel). Secondary check: re-run on QAC root-tokens (morphology). Both must agree for "ROBUST" tag.
