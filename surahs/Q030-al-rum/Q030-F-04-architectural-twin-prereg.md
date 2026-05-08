---
surah: 30
test_id: Q030-F-04
title: Q 29 ↔ Q 30 architectural-twin signature (Fisher-Rao distance within ALM cluster)
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
alpha_bon: 0.05
hypothesis_anchor: cross-finding-008 (Q29+Q30 are the 2 ALM-exceptions); Q005-F-05 (chronology-architecture dissociation framework)
verdict_ceiling: PASS-DIRECTED (single-test cap; replication queue: independent operationalization on rhyme/phoneme)
---

# Q030-F-04 — Pre-registration: Q 29 ↔ Q 30 architectural-twin signature

## 1. Hypothesis (LOCKED before observation)

**H1 (one-tailed):** Within the ALM-cluster (Q 2, 3, 29, 30, 31, 32 — i.e., the 6 surahs opening with الم muqaṭṭāʿat), the Fisher-Rao stem-root distance d(Q 29, Q 30) is **STRICTLY BELOW the median of all 15 within-ALM-cluster pairwise distances**.

**H0:** d(Q 29, Q 30) is at or above the median.

**Direction:** d(Q 29, Q 30) < median(d_ALM-15-pairs) — LOCKED.

## 2. Rationale

Cross-finding-008 establishes Q 29 + Q 30 as the 2 ALM-cluster exceptions to the muqaṭṭaʿāt + book-reference pattern. Both are also Late Meccan (Nöldeke phase 3) and adjacent in the mushaf (Q 29 immediately precedes Q 30). If their book-reference-exception status corresponds to a SHARED architectural signature (not just shared exception-status), the Fisher-Rao roots-distance between them should be small relative to the other ALM pairs.

This test is the **architectural twin** counterpart to the Q005-F-05 chronology-architecture-dissociation framework. Q005-F-05 found that Q 5 (late chronology) is architecturally Q 2-like (early). Here we ask whether Q 29 and Q 30 (both late chronology, both ALM-exceptions) are architecturally close to each other.

## 3. Test statistic

- **Primary**: rank of d(Q 29, Q 30) in the sorted list of 15 within-ALM pairwise distances. Pass = rank ≤ 7 (BELOW median = strict lower half of 15).
- **Secondary**: percentile of d(Q 29, Q 30) in the 6441 corpus-wide pairs.

## 4. Bonferroni

k=1. α_bon = 0.05.

For the primary statistic (rank ≤ 7 of 15 under uniform null), the exact one-tailed p = 7/15 ≈ 0.467 — a single comparison cannot achieve α_bon=0.05 by rank-position alone.

**THEREFORE the primary acceptance criterion is reframed at pre-reg time as DIRECTIONAL-only**: rank ≤ 7 = "matches direction"; rank ≤ 3 = "extreme-direction"; rank > 7 = "direction-violated, NULL".

The secondary statistic (corpus-wide percentile, n=6441) CAN achieve α=0.05 at percentile ≤ 5%.

## 5. Success / Failure

| Outcome | Primary verdict |
|:--|:--|
| Rank 1-3 of 15 within ALM | **STRONG-DIRECTED** |
| Rank 4-7 of 15 within ALM | **DIRECTED** (matches H1) |
| Rank 8-15 of 15 within ALM | **NULL / direction-violated** |

| Secondary outcome | Verdict |
|:--|:--|
| corpus percentile ≤ 5% | **STRONG-DIRECTIONAL with α=0.05 lock** |
| corpus percentile 5-25% | **WEAK-DIRECTIONAL** |
| corpus percentile > 50% | **NULL** |

## 6. Data source

`/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` — 114×114 Fisher-Rao distance matrix on QAC stem-roots (already locked under [[h-new-111|H-NEW-111]] mushaf-information-geodesic-optimal finding, run-date 2026-04-14, seed 20260417).

## 7. SHA256 lock

This test re-uses pre-existing locked artifacts (h-new-111). The pre-reg locks the EXTRACTION procedure on top of the existing matrix. Script verifies its own SHA before running.

## 8. Honest a-priori limits

- The h-new-111 matrix is a single distance metric (FR on QAC stem-roots). Alternative metrics (rhyme, phoneme, verse-length-distribution) could give different verdicts. This test commits to FR-roots; alternative-metric replication is a follow-up.
- The "ALM-cluster" of 6 surahs is the relevant within-letter-family comparison. Within-cluster homogeneity is itself an architectural feature of the Quran (cross-finding-006), so we expect ALM pairs to be on average closer than a random 6-surah sample.
- Q 29-Q 30 are mushaf-adjacent (s=29, s=30). The compression-tail law (H-NEW-660) predicts modest content-cohesion at this position. A small d(Q29,Q30) could be partly explained by mushaf-position rather than ALM-exception-twin status. **An adjacency control is queued as Q030-F-04-secondary**: compute d(Q s, Q s+1) for s∈{1..113} and rank d(29, 30) in that adjacency-ladder.
