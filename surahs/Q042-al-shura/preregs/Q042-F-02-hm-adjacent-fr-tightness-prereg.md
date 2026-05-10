---
prereg_id: Q042-F-02
title: Q 41 ↔ Q 42 is the TIGHTEST adjacent ḥawāmīm pair by FR-distance
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T00:15:00-05:00
status: PRE-REG-LOCKED
---

# Pre-registration: Q042-F-02 — Q 41 ↔ Q 42 as tightest adjacent ḥawāmīm pair

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: Among the six mushaf-adjacent pairs inside the
ḥawāmīm-7 cluster (Q 40-41, Q 41-42, Q 42-43, Q 43-44, Q 44-45, Q 45-46),
**Q 41 ↔ Q 42** is the **TIGHTEST** (lowest FR-distance) pair.

**Rationale**: Both Q 41 and Q 42 share the *double-HM-opener-with-tanzīl-incipit*
formula (Q 41:2 *tanzīlun min al-raḥmāni al-raḥīm* and Q 42 carries the full
ḤMʿsq super-opener) and are mushaf-adjacent inside HM-A. The brief predicts
their root-distribution FR-distance should be the minimum of the six.

## 2. Null

**H0**: Q 41 ↔ Q 42 is NOT the minimum-FR adjacent ḥawāmīm pair.

## 3. Operationalization

- Distance source: `findings/phase-b-hypotheses/csv/h-new-111.json` (114×114
  FR distance matrix on QAC stem-roots; upper-triangular `D_matrix_upper_triangular`).
- Adjacent ḥawāmīm pairs (k=6, all mushaf-adjacent within Q 40-46):
  {(40,41), (41,42), (42,43), (43,44), (44,45), (45,46)}.
- Direction: minimum-rank-of-six.

## 4. Direction lock

Pre-committed: Q 41 ↔ Q 42 ranks #1 (lowest FR-distance) among the six.

## 5. Success / failure / Bonferroni

- Single test, k=1. No multiple-comparison.
- **VINDICATION**: Q 41 ↔ Q 42 is rank #1 of six.
- **PRE-COMMIT VIOLATION → NULL**: any other rank.

## 6. Seed

`20260509`.

## 7. Output

JSON to `csv/Q042-F-02.json` with the six adjacent FR-distances + observed rank
of Q 41 ↔ Q 42 + verdict.

## 8. Why pre-register a directional prediction we may lose

The brief's intuition (shared double-HM opener formula + content adjacency
should produce minimum root-FR-distance among adjacent HM pairs) is testable
and falsifiable. Direction-of-effect is locked here; any rank > 1 publishes as
NULL with full prominence (Protocol §1.3, §1.8). The result is informative
either way — if Q 41 ↔ Q 42 is not tightest, it indicates the *tanzīl-incipit*
shared formula does NOT linearly predict FR root-tightness within HM-7.
