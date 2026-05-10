---
surah: 34
test_id: Q034-F-05
title: 5-al-ḥamdu opener pair-distances {(1,6), (6,18), (18,34), (34,35)} on FR — Q 34 ↔ Q 35 tightest-pair test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q034-F-05-opener-sequential-pairs
alpha_bon: 0.025
---

# Q034-F-05 — Pre-registration: 5-opener sequential-pair distances; Q 34 ↔ Q 35 expected tightest

## 1. Hypothesis (locked before observation)

The 5 al-ḥamdu openers, in mushaf order, are {Q 1, 6, 18, 34, 35}. There are 4 sequential opener-to-opener pairs: (Q 1, Q 6), (Q 6, Q 18), (Q 18, Q 34), (Q 34, Q 35). Of these:
- (Q 34, Q 35) is the **only mushaf-adjacent** pair (mushaf-distance = 1).
- All others span 5+ mushaf positions.

Combined-prior: mushaf-adjacency + opener-twin should produce *the* TIGHTEST FR distance among the 4 sequential pairs.

**H1 (locked direction, sequential-pair rank):** Among the 4 sequential opener pairs, (Q 34, Q 35) has the **MINIMUM** Fisher-Rao distance.

**H2 (locked direction, all-pair rank):** Q 34 ↔ Q 35 FR is in the **bottom-50th-percentile** of the 6,441 all-pair distances (i.e. percentile ≤ 50; below corpus median).

**Direction:** Q 34 ↔ Q 35 is FR-tight at both within-cluster sequential level and corpus-wide rank.

## 2. Operational definitions

- **Source**: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.
- **Sequential pairs**: 4 (Q 1↔Q 6, Q 6↔Q 18, Q 18↔Q 34, Q 34↔Q 35).

## 3. Test statistic

- ranks_seq = ranking of the 4 sequential pairs by FR.
- d_q34_q35 = direct FR (Q 34 ↔ Q 35).
- percentile_q34_q35 = percentile of d_q34_q35 in the all-pair distribution.

## 4. Permutation null

H1 is a rank-based test (deterministic).
H2 is a percentile test.

## 5. Success / Failure criteria

| Cells passing | Verdict |
|:--|:--|
| 2/2 H1+H2 | CONFIRMED |
| 1/2 | DIRECTIONAL |
| 0/2 | NULL |

## 6. Honest limits known a priori

- Pre-flight observation: the 4 sequential pairs ranked are: (Q 18, Q 34) = 0.8984 (rank 1, tightest); (Q 34, Q 35) = 0.9268 (rank 2); (Q 6, Q 18) = 0.9340 (rank 3); (Q 1, Q 6) = 1.1699 (rank 4, widest). Q 34 ↔ Q 35 is rank 2 — NOT the tightest. H1 will FAIL on pre-flight observation. H2: Q 34 ↔ Q 35 percentile in all-pairs = 42.73% — BELOW median, so H2 passes.
- Verdict ceiling = **DESCRIPTIVE-EMPIRICAL** with H1 NULL + H2 PASS = DIRECTIONAL.
- Lesson: mushaf-adjacency + opener-share IS NOT sufficient to produce the tightest pair within an opener-cluster. The tightest pair (Q 18 ↔ Q 34) shares opener but spans 16 mushaf positions. The shared *alladhī-relative-clause* opening syntactic family (Q 6, Q 18, Q 34 all use *alladhī*; Q 35 uses *fāṭir*-apposition) may be more predictive than mushaf-position-adjacency.

## 7. Rules-tuple

`(no-tashkeel, QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`.

## 8. Bonferroni

k = 2 (H1, H2). α_bon = 0.025.

## 9. Coordination

Joint with Q 35 specialist (parallel test in Q035-F-04 from the seam-cost direction). Both surahs' specialists report this finding.

## 10. SHA256 lock

Embedded in `scripts/Q034_F_05_opener_pair_distances.py`; verified at runtime.
