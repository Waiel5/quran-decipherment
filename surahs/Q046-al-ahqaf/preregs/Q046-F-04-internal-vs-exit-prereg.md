---
prereg_id: Q046-F-04
title: Q 45→Q 46 (internal HM-B) vs Q 46→Q 47 (HM exit) adjacency-cost asymmetry
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T03:30:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q046-F-04 — internal vs exit adjacency cost

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The Q 45 → Q 46 canonical-adjacency cost (intra-HM-B internal) is **HIGHER** than the Q 46 → Q 47 cost (HM exit boundary), measured as `delta` in `h-new-720.json`.

Rationale: classical assumption (and the user-prompt's framing) treats HM-EXIT as the dominant cost driver; this pre-reg tests whether the empirical INTERNAL cost is higher — a counter-intuitive finding if confirmed.

## 2. Null

**H0**: Q 45→Q 46 cost = Q 46→Q 47 cost (or Q 45→Q 46 < Q 46→Q 47).

## 3. Operationalization

- Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json`, field `per_adjacency`.
- delta(Q 45→Q 46) extracted at `pair == [45, 46]`.
- delta(Q 46→Q 47) extracted at `pair == [46, 47]`.

## 4. Direction lock

Pre-committed direction: **delta(Q 45→Q 46) > delta(Q 46→Q 47)**.

If reversed: **NULL with pre-commit violation flag**.

## 5. Bonferroni

Single test (k=1).

## 6. Success / failure criteria

- **VINDICATED**: Q 45→46 > Q 46→47 by ≥ 5%.
- **DIRECTIONAL**: Q 45→46 > Q 46→47 but margin < 5%.
- **NULL/violation**: Q 45→46 ≤ Q 46→47.

## 7. Seed

N/A (deterministic).

## 8. Output

JSON to `csv/Q046-F-04.json` with: both costs, ranks, ratio, interpretation note.

## 9. Notes

If H1 vindicates, this **counter-intuitively refines** the user-prompt's "boundary cost" framing: the HM-exit transition is empirically EASIER than the internal HM-B step. Mechanism: HM-B is a high-internal-coherence cluster; the exit is to a content-distinct but FR-structurally-cheap-to-access neighbor.
