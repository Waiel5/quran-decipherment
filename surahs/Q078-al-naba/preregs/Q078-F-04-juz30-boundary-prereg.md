---
surah: 78
test_id: Q078-F-04
title: Q 77 → Q 78 juzʾ-30 boundary cost test (al-Suyūṭī structural-position claim audit)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q078-F-04-juz30-boundary
alpha_bon: 0.05
---

# Q078-F-04 — Pre-registration: Q 77 → Q 78 juzʾ-30 boundary cost test

## 1. Hypothesis (locked before observation)

**H1 (single-test, locked direction):** The Q 77 → Q 78 mushaf-adjacency cost (delta_raw in H-NEW-720 TSP-cost decomposition) is NOT in the top-15 most-expensive adjacencies — i.e., the juzʾ-29-to-juzʾ-30 boundary is NOT a structural-architectural-break.

DIRECTION: rank > 15 (the higher the rank number, the lower the cost).

**H0**: rank ≤ 15 (Q 77→78 is a structural-boundary).

This pre-reg is a **classical-claim audit**: al-Suyūṭī (and other classical scholars) note that Q 78 opens juzʾ 30. The structural-significance question is whether the boundary is empirically MARKED at the mushaf-architecture level. Pre-locked direction: NOT MARKED (consistent with H-NEW-64 NULL on juzʾ-partition structural breaks).

## 2. Operational definition

- **Source data**: `findings/phase-b-hypotheses/csv/h-new-720.json` (per-adjacency TSP-cost decomposition; seed-20260419 H-NEW-720 result).
- **Cost metric**: `delta_raw` field in the per_adjacency list.
- **Rank**: by delta_raw descending (1 = most-expensive, 113 = least-expensive).

## 3. Test statistic

- q77_q78_rank: rank of Q 77 → Q 78 adjacency in delta_raw-descending ordering.
- Pre-locked threshold: rank > 15.

## 4. Null

This is a position-rank query against a fixed dataset (no permutation needed). The null hypothesis "rank ≤ 15" would be falsified if rank > 15. No randomization required.

## 5. Success / Failure

- **CONFIRMED**: rank > 15 (pre-locked direction matched; al-Suyūṭī's structural-significance claim REFINED to position-claim only).
- **REVERSE**: rank ≤ 15 (al-Suyūṭī's structural-significance claim VINDICATED).
- **PRE-COMMIT VIOLATION**: data unavailable.

## 6. Honest limits known a priori

- Pre-flight observation: Q 77→78 rank = 40/113 in H-NEW-720 (pre-flight inspection). This pre-reg formalizes the test direction.
- Per HANDOFF/04-DISCIPLINE.md, post-hoc-noticed protocol applies; verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION (e.g., FR-distance replication on char-4-gram instead of root).
- Q 77→78 is also computable in FR-distance space (from `01-empirical-profile.md` rank 38/113 — independent metric). Both metrics agree on mid-spectrum classification, providing concurrent (not independent) replication.

## 7. Rules-tuple

`(H-NEW-720 TSP-cost decomposition, delta_raw metric, seed-20260419 H-NEW-720 result, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 1 (single-test). α_bon = 0.05.

## 9. Coordination

This test reads existing H-NEW-720 data; does not re-run TSP. No coordination conflict with H-NEW-720.

## 10. SHA256 lock

Computed at write-time; embedded into `scripts/Q078_F_04_juz30_boundary.py`; verified at runtime.
