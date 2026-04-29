---
prereg_id: Q046-F-01
title: Q 46 → Q 47 canonical-adjacency cost rank under triple-discontinuity
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T03:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q046-F-01 — Q 46 → Q 47 boundary cost rank

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The Q 46 → Q 47 canonical-adjacency cost in `h-new-720.json` ranks within the top-25/113 (i.e., upper-22%) of canonical adjacencies, reflecting the triple discontinuity: (i) ḥawāmīm exit (HM → no-HM), (ii) Meccan → Medinan chronology jump, (iii) common-noun-name → person-name shift.

## 2. Null

**H0**: Q 46 → Q 47 cost rank is uniformly distributed in [1, 113].

## 3. Operationalization

- Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json`, field `per_adjacency`.
- Cost: `delta` field (= L_constrained − L_2opt residual contribution).
- Rank: descending sort by `delta`; rank 1 = highest cost.
- Adjacency identified by `pair == [46, 47]`.

## 4. Direction lock

Pre-committed direction: **Q 46-Q 47 rank ≤ 25** (top-22%, i.e., HIGH cost as the user-prompt assertion).

If observed rank > 25: **DIRECTIONAL FAILURE — refined to moderate**; published with full prominence per [[INVESTIGATION-PROTOCOL]] §1.3.

## 5. Bonferroni

This is a single test (k=1) within this prereg. No multiplicity correction.

## 6. Success / failure criteria

- **VINDICATED**: rank ≤ 10 (top-10).
- **DIRECTIONAL VINDICATION**: rank ≤ 25.
- **REFINED-MODERATE**: rank in [26, 56].
- **NULL/REFUTED**: rank > 56 (below median).

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q046-F-01.json` with: rank, delta-cost, fraction-of-residual, top-10 reference, comparison to Q 45→Q 46.

## 9. Notes

The user-prompt's framing characterised Q 46→Q 47 as "HIGH canonical-adjacency-cost transition per h-new-720" — this pre-reg makes that framing FALSIFIABLE at rank-threshold 25. Mechanism candidates: (i) HM exit, (ii) Meccan→Medinan, (iii) name-class shift.
