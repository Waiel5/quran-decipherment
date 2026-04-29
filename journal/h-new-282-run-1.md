# H-NEW-282 run journal

Date: 2026-04-18
Operator: codex

## Scope

Local harvest of the bounded OQ-19 denominator-adjudication follow-up
after the JSON landed on disk but the finding/journal prose files had
not yet been written.

## Locked comparison

- baseline:
  raw top-500 counts + flat `alpha = 0.5`
- H-278 comparator:
  divide by total stem-root token mass
- H-282 candidate:
  divide by top-500 feature-space token mass

All runs use:

- K = 500 top QAC-STEM roots
- Fisher-Rao angular distance
- Kruskal MST
- no-tashkeel
- Hafs-Kufan

## Key outputs

- baseline `Q108 = 24`, `Q7 = 10`
- H-278 `Q108 = 1`, `Q7 = 15`
- H-282 `Q108 = 1`, `Q7 = 18`
- H-282 top-3 = `Q7, Q9, Q25`
- H-282 verdict = `FAIL-COLLAPSE`

## Continuity note

This finding strengthens the H-278 interpretation:
the Q108 collapse under normalization is not rescued by switching the
denominator from total stem-root mass to top-500 coverage mass.
