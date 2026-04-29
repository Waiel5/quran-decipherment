---
prereg_id: Q043-F-01
title: Q 43:1-2 ↔ Q 44:1-2 verbatim-identical first-two-verse opening uniqueness test
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T02:30:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q043-F-01 — Q 43-Q 44 verbatim-identical opening pair

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The pair (Q 43:1, Q 43:2) and (Q 44:1, Q 44:2) are verbatim-identical at the no-tashkeel orthographic level, AND no other adjacent surah-pair in the entire Qurʾān shares verbatim-identical first-two-verse opening.

## 2. Operationalization

- Tashkeel: no-tashkeel.
- Source: `quran-text/quran-no-tashkeel.json`.
- For each adjacent surah pair (Q 1-Q 2, Q 2-Q 3, ..., Q 113-Q 114), check if (s_i v.1, s_i v.2) == (s_{i+1} v.1, s_{i+1} v.2) verbatim.

## 3. Direction lock

Pre-committed: only the Q 43-Q 44 pair has this property.

## 4. Bonferroni

Single test (k=1).

## 5. Verdict criteria

- VINDICATED if exactly the Q 43-Q 44 pair satisfies the verbatim-identical opening condition.
- NULL if other pairs also share or if Q 43-Q 44 does not.

## 6. Seed

`20260428`.

## 7. Output

JSON to `csv/Q043-F-01.json`.

## 8. Rationale

al-Biqāʿī (*Naẓm al-durar* ad Q 44:1) treats the Q 43-Q 44 verbatim-twin opening as deliberate liturgical-pairing. This pre-reg formalizes the test.
