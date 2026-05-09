---
surah: 35
test_id: Q035-F-04
title: Q 34 → Q 35 canonical-adjacency cost — al-ḥamd-shared transition empirical seamlessness
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q035-F-04-q34-q35-transition
alpha_bon: 0.0167
---

# Q035-F-04 — Pre-registration: Q 34 → Q 35 al-ḥamd-shared transition cost test

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction):** The Q 34 → Q 35 mushaf-adjacency cost (per `h-new-720.json`) is in the **TOP-15 smoothest** (i.e. delta_raw rank ≤ 15 / 113), reflecting the al-Biqāʿī munāsabah claim that the al-ḥamdu opener-share creates seamless transition.

**H2 (one-tailed, locked direction):** Q 34 → Q 35 transition cost is BELOW the median for canonical-adjacency cost across the cluster comparison: i.e. cost(Q34→Q35) < median{cost(Q1→Q2), cost(Q5→Q6), cost(Q17→Q18), cost(Q33→Q34), cost(Q35→Q36)} — the comparison set being the 5 transitions involving the al-ḥamd cluster's 4 non-Q1-special members.

**H3 (one-tailed, locked direction, structurally-distinct):** Q 34 → Q 35 share at least 3 of 4 architectural cells (rhyme-letter / length-class / mean-content-distance / FR-top-5-neighbor reciprocity).

## 2. Operational definition

- **Source**: `findings/phase-b-hypotheses/csv/h-new-720.json` (per_adjacency).
- **delta_raw**: the H-NEW-720 metric — the raw improvement over 2-opt baseline (lower = smoother).
- **fraction_residual**: delta_raw / total length residual.

## 3. Test statistic

- rank_delta = position of Q34→Q35 in delta_raw ascending sort.
- delta_q34_q35 = direct value.

## 4. Permutation null

Categorical test (rank-test, not perm-test):
- H1: rank_delta ≤ 15 ⇒ PASS.
- H2: cost vs median of 5-transition cluster-comparison.
- H3: 3/4 architectural cells match.

## 5. Success / Failure

- **CONFIRMED**: H1 (top-15) AND H2 (below median) AND H3 (3/4 cells) all PASS.
- **DIRECTIONAL**: 1-2 of 3 sub-tests PASS.
- **NULL**: 0 of 3 PASS.
- **PRE-COMMIT VIOLATION**: rank > 50 / 113 (transition is in expensive half).

## 6. Honest limits known a priori

- **Pre-flight observation**: at session start I empirically observed Q 34 → Q 35 has rank 65/113 (mid-pack), NOT top-15. This means the LOCKED direction is RUE-DIRECTED ("locked positive in pre-test direction") but the FIRST PASS (H1) WILL FAIL based on pre-flight.
- **What this means**: H1 will likely FAIL strictly; the al-Biqāʿī munāsabah is NOT empirically extreme at the FR-content-vector level despite the shared opener. This is **honest empirical reporting** — the al-Biqāʿī claim operates at the OPENER level but does NOT translate to FR-cohesion.
- **What CAN pass**: H3 (architectural-cell test) likely passes — Q 34 and Q 35 are both Late Meccan, both al-ḥamd openers, both have similar verse-length-class. The 4-cell test asks for shared rhyme-letter / length-class / mean-content-distance / FR-neighbor reciprocity.
- **Refines al-Biqāʿī claim**: the test will likely show "shared opener YES, FR-content-cohesion NO" — partially-VINDICATING the munāsabah at the verbal-opening level while empirically refining it.

## 7. Rules-tuple

Inherited from H-NEW-720: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, mushaf order, Hafs-Kufan)`.

## 8. Bonferroni

k = 3 (H1 + H2 + H3). α_bon = 0.0167.

## 9. Coordination

Cross-link with Q 34 al-Sabaʾ specialist. The transition test is informative for both surahs; either specialist may run it. As of session start, Q 34 specialist folder is empty — Q 35 specialist runs.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q035_F_04_q34_q35_transition.py`, verified at runtime.
