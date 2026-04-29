---
finding_id: Q009-F-03
prereg_date: 2026-04-28
prereg_type: pre-existing-empirical re-audit (instrument-control)
status: PRE-REGISTERED
---

# Q009-F-03 — Q 9 → Q 10 canonical-adjacency cost audit (pre-registration)

## 1. Hypothesis (DIRECTION-LOCKED)

**H1**: The Q 9 → Q 10 (al-Tawba → Yūnus) canonical-adjacency cost in the FR-TSP residual decomposition (H-NEW-720) is in the **top-10 most-expensive of 113 adjacencies**, AND its cost is driven by the chronology-block boundary (Q 9 = Medinan-late = revelation-order #113; Q 10 = Meccan = revelation-order #51 with ALR muqaṭṭaʿāt cluster Q 10-15).

**Direction**: rank-from-top ≤ 10 (high cost). LOCKED.

## 2. Null hypothesis

**H0**: Random adjacency would give rank ≤ 10 with probability 10/113 ≈ 8.85%.

## 3. Rules-tuple

- adjacency-cost source: `findings/phase-b-hypotheses/csv/h-new-720.json` per_adjacency entries.
- "cost" = `fraction_residual` field.
- ranking: descending of fraction_residual; 1 = most expensive.

## 4. Pre-committed thresholds

Read directly from h-new-720.json — no random component; this is a sanity check.

| Outcome | Verdict |
|:--|:--|
| Q9-Q10 rank ≤ 10 | VINDICATED |
| Q9-Q10 rank 11-30 | DIRECTIONAL |
| Q9-Q10 rank > 30 | FALSIFIED |

## 5. Driver test

Compute three diagnostic statistics:
- **Tashkeel control**: re-compute Q 9 → Q 10 FR distance with `quran-min-tashkeel.json` rhyme-final letter distribution. Does the high cost replicate?
- **Chronology variant**: re-compute with revelation-order metric (replacing canonical adjacency with chronological adjacency). If the cost vanishes, the high canonical cost is **chronology-induced**.
- **muqaṭṭaʿāt control**: compare Q 9-Q 10 cost to Q 6-Q 7 (Q 6 al-Anʿām → Q 7 al-Aʿrāf, where Q 7 starts with المص muqaṭṭaʿāt cluster). If both are top-decile, this generalizes "introducing a new muqaṭṭaʿāt cluster is expensive."

## 6. Pre-commit locked.
