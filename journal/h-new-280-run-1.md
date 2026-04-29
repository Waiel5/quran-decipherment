---
finding_id: h-new-280
run: 1
date: 2026-04-18
specialist: codex
seed: 20260418
---

# H-NEW-280 run 1 journal

## Timeline

1. Read `HANDOFF/05-OPEN-QUESTIONS.md` at OQ-20.
2. Read the immediate parent/context files:
   `findings/phase-b-hypotheses/h-new-127-verse-fisher-rao-fractal.md`,
   `scripts/h_new_127_verse_fisher_rao.py`,
   `scripts/h_new_83_rahman_refrain_extension.py`,
   and `findings/per-verse-annotations.csv`.
3. Confirmed the audit-salvage scope from OQ-20:
   keep Q55 refrain positions fixed and permute only non-refrain verses.
4. Wrote pre-reg:
   `findings/phase-b-hypotheses/h-new-280-q55-refrain-constrained-fr-null-prereg.md`.
5. Wrote script:
   `scripts/h_new_280_q55_refrain_constrained_fr_null.py`.
6. Executed the script and wrote JSON:
   `findings/phase-b-hypotheses/csv/h-new-280.json`.
7. Wrote findings note:
   `findings/phase-b-hypotheses/h-new-280-q55-refrain-constrained-fr-null.md`.
8. Wrote this journal.

## Locked result

- Refrain positions verified exactly:
  `[13, 16, 18, 21, 23, 25, 28, 30, 32, 34, 36, 38, 40, 42, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77]`
- Non-refrain verses shuffled: `47`
- `L_canon = 13.639165`
- Constrained-null mean `= 13.693339`
- Constrained-null SD `= 0.118168`
- `z = -0.458439`
- One-sided lower-tail `p = 0.312168783122`
- Primary decision rule (`p < 0.05`) -> `NULL`
- Anti-geodesic under constrained null? `No`

## Comparison to H-NEW-127

The main point of this run is the change in null behavior:

- H-NEW-127 unconstrained null mean for Q55: `11.252899`
- H-NEW-280 constrained null mean for Q55: `13.693339`

So preserving the refrain schedule moves the null center upward by about
`2.44044`, which is exactly the correction this bounded follow-up was
meant to test. The earlier anti-geodesic reversal disappears, but the
result does not become a positive pass.

## Notes

- I kept the feature space identical to H-NEW-127:
  `K=300`, `alpha=0.5`, QAC STEM roots, Fisher-Rao angular distance.
- I did not add 2-opt, block nulls, alternate metrics, or a new family
  of surahs. That would have broadened the task beyond the user's scope.
- The only instrument check was that the exact normalized refrain-match
  positions agreed with the H-NEW-83 list. They did.

## Deviations from pre-reg

None.

## Files touched

- Created: `findings/phase-b-hypotheses/h-new-280-q55-refrain-constrained-fr-null-prereg.md`
- Created: `scripts/h_new_280_q55_refrain_constrained_fr_null.py`
- Created: `findings/phase-b-hypotheses/csv/h-new-280.json`
- Created: `findings/phase-b-hypotheses/h-new-280-q55-refrain-constrained-fr-null.md`
- Created: `journal/h-new-280-run-1.md`
