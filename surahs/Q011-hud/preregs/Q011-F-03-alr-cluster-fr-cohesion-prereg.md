---
surah: 11
test_id: Q011-F-03
title: Q 11 FR-distance to ALR-siblings vs comparable-length non-ALR
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_family: Q011-F-03
bonferroni_k: 1
alpha_bon: 0.05
n_perm: 10000
---

# Q011-F-03 — Pre-registration: Q 11 FR pull-in to ALR-cluster

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, direction LOCKED):** Q 11's mean Fisher-Rao content distance
to its 4 other ALR-cluster siblings {Q 10, Q 12, Q 14, Q 15} is **strictly
less than** its mean FR distance to the **20 nearest-length non-ALR comparable
surahs** (5 most below + 5 most above Q 11's verse-count, then taken pairwise
× 2; see §2 for exact construction).

**H0:** Q 11's mean FR distance to ALR siblings ≥ mean FR distance to the 20
length-matched non-ALR surahs.

**Direction:** ALR pull-in is real — Q 11 is closer to its letter-family
siblings than to length-comparable random non-ALR surahs (LOCKED).

## 2. Operational definition

- **FR distance**: read pre-computed 114×114 Fisher-Rao distance matrix from
  `findings/phase-b-hypotheses/csv/h-new-111.json` (`D_matrix_upper_triangular`).
  Reconstruct symmetric matrix.
- **ALR siblings of Q 11**: {Q 10, Q 12, Q 14, Q 15} (the 4 other ALR surahs;
  Q 13 is ALMR, so excluded under the strict-ALR membership of H-NEW-97).
- **Comparable-length non-ALR set**: all surahs s ∈ {1..114} \ {10, 11, 12, 13, 14, 15}
  (excludes the 6 muqaṭṭaʿāt-ALR-or-ALMR cluster) sorted by absolute difference
  in verse count |n_s − 123|; take the **20 nearest**.
- **Test statistic**: `T = mean_FR(Q 11, ALR-siblings) − mean_FR(Q 11, 20 length-matched non-ALR)`.
  Negative T = Q 11 closer to ALR siblings (DIRECTION-MATCHED).
- **Permutation null**: 10,000 random partitions of the 24 candidate surahs
  (4 ALR + 20 length-matched) into a "fake ALR" group of 4 and a "fake length-matched"
  group of 20; compute T_perm under each draw; p-value = fraction of draws with
  T_perm ≤ T_obs.
- **Seed 20260507**.

## 3. Test statistic

T (continuous, signed). p-value (one-tailed lower).

## 4. Success / Failure

| Outcome | Verdict |
|:--|:--|
| T < 0 AND p ≤ 0.05 | **CONFIRMED** |
| T < 0 AND 0.05 < p ≤ 0.10 | DIRECTIONAL |
| T ≥ 0 OR p > 0.10 | NULL |
| T strongly POSITIVE (p ≥ 0.95) | Pre-commit violation; NULL with full prominence |

## 5. Bonferroni context

- 1 primary cell. α=0.05.
- This test is the empirical follow-up to H-NEW-600's whole-surah ALR-5
  cohesion NULL (56.25 %ile) and to Q 11's 00-overview.md §9 post-hoc t-test
  observation that Q 11 has the strongest ALR pull-in among the 5 ALR members.
  Status: confirmatory of the post-hoc observation under a stronger length-matched
  permutation null — this elevates the Q 11 §9 post-hoc to PASS-DIRECTED if the
  permutation passes.

## 6. Honest limits known a priori

- The H-NEW-600 *whole-surah-cohesion* test failed for ALR-5 in aggregate.
  Q011-F-03 is the **per-surah** version: it tests whether Q 11 specifically
  is pulled in. Even if Q011-F-03 PASSES, the H-NEW-600 corpus-level NULL is
  not undone — these are different scales of the same axis.
- Length-matching is by verse count |n_s − 123|, not by token count or by
  rhyme/phoneme density. A length-controlled non-ALR comparator could be
  constructed differently; this is the standard verse-count match.
- Excluding Q 13 from "ALR-cluster" matches H-NEW-97 strict definition. If
  one includes Q 13 (ALMR), the cluster becomes {Q 10, 12, 13, 14, 15} and
  the test shifts marginally; this is robust under either definition (ALR-strict
  is the locked one).

## 7. Rules-tuple

`(no-tashkeel, FR-distance from h-new-111, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. SHA256 lock

Computed at run-time. Embedded in `scripts/Q011_F_03_alr_cluster_fr_cohesion.py`.
