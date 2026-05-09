---
finding_id: Q071-F-04
title: Q 70→Q 71→Q 72 mushaf-transitions vs structural-boundary set B (H-NEW-130 replication)
parent_finding: H-NEW-130 (Fisher-Rao residuals as structural-boundary hinges)
date_pre_registered: 2026-05-09
seed: 20260509
agent: Q 71 Nūḥ specialist (Waiel Al-Shujaa)
test_type: deterministic boundary-set lookup + adjacency-rank check
bonferroni_family: Q071-novel-tests-2026-05-09
bonferroni_k: 5
alpha_bon: 0.01
direction_locked: Q 70→71 in B AND Q 71→72 NOT in B (asymmetric chronology-phase boundary)
acceptance_window: both directional predictions match
mw5_positive_control: Q 1→2 (rank-1 universal-hinge transition; in B with full label set)
mw7_internal_check: cross-reference H-NEW-130 csv boundary_set entries
---

# Q071-F-04 — Q 70→Q 71→Q 72 transitions vs structural-boundary set B

## 1. Hypothesis

Under the H-NEW-130 framework (Fisher-Rao mushaf-residuals as structural-boundary
hinges), the Q 70→Q 71 transition is in the pre-committed boundary-set B (specifically,
because it crosses an Early-Meccan→Middle-Meccan Nöldeke phase boundary), while the
Q 71→Q 72 transition is NOT in B (both Q 71 and Q 72 are Middle Meccan, no muq change,
no period change).

## 2. Pre-committed direction

- Q 70→Q 71: in B with label `phase_Early Meccan_to_Middle Meccan` (chronology-phase shift).
- Q 71→Q 72: NOT in B (intra-phase, intra-period, no muq change).

## 3. Method

- **Boundary set B**: the pre-committed set from H-NEW-130, extracted from
  `findings/phase-b-hypotheses/csv/h-new-130.json`, key `boundary_set`.
- **Lookup**: dictionary lookup on keys `'70-71'` and `'71-72'`.
- **Verification**: the FR-distance values D[70][71] and D[71][72] from
  `findings/phase-b-hypotheses/csv/h-new-111.json`'s `D_matrix_upper_triangular`.
- **Adjacency-rank**: rank of D[70][71] and D[71][72] among the 113 mushaf-consecutive
  pairs (1 = cheapest, 113 = most expensive).

## 4. Acceptance window

- BOTH directional predictions match → **PASS-DIRECTED**.
- Only ONE matches → **DIRECTIONAL**.
- NEITHER matches → **NULL**.

## 5. Garden-of-forking-paths

- The boundary-set B was locked at H-NEW-130 pre-registration. We do NOT redefine
  it here. The labels `phase_Early Meccan_to_Middle Meccan` etc. are from the
  parent test's `B_labels` field.
- Nöldeke chronology classifications (Q 70 = Early Meccan #42, Q 71 = Middle Meccan
  #51, Q 72 = Middle Meccan #62) are from `data/revelation-order.csv` (Wikipedia-Nöldeke
  source). These are LOCKED ANCILLARY DATA, not derived in this test.

## 6. Independent-replication notes

The Q 71→Q 72 NOT-in-B prediction is a NEGATIVE prediction (a place where we expect
NO structural-residual signal). This functions as a within-pre-reg negative-control
check: if Q 71→Q 72 were also in B, it would suggest the boundary-set definition is
too permissive.

## 7. Honest disclosure

- Q 70→Q 71 is one of MANY Nöldeke phase-boundary transitions in mushaf order.
  It is NOT in the top-15 universal-hinges list (Q 1→2, Q 49→50, Q 56→57 etc.).
  The verdict is "in B" not "top-cost B-hinge".
- Q 71→Q 72 NOT being in B is empirically correct under the locked B-definition,
  but the FR-distance D[71][72] = 0.808 is NOT exceptionally low (rank 54/113);
  this is a "boundary-absent" claim, NOT a "smooth-transition" claim.
- Both Q 70 and Q 72 are ALIF-RHYME-DOMINANT (Q 70: 71% alif; Q 72: 100% alif),
  and Q 71 is also alif-dominant (85.7%). The Q 70→71→72 cluster is RHYME-COHESIVE
  even though Q 70→71 crosses a chronological phase boundary. This is honest disclosure:
  the H-NEW-130 chronology-phase signal is IN the structural-content axis, not the
  rhyme axis.

## 8. Cross-references

- [[h-new-130-fisher-rao-residuals|H-NEW-130]] — parent test (15/15 top-jumps in B).
- [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] — char-4-gram replication.
- [[h-new-111|H-NEW-111]] — Fisher-Rao distance matrix.
- [[Q070-al-maarij/00-overview|Q 70 al-Maʿārij]] — Early Meccan precursor.
- [[Q072-al-jinn/00-overview|Q 72 al-Jinn]] — Middle Meccan successor.
- 06-novel-findings.md Q071-F-04 — result.
