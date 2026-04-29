# H-NEW-287 run journal

Date: 2026-04-19
Operator: codex

## Scope

Run the preregistered exact within-zone three-axis content-composite
test for H-NEW-287 after the H-NEW-286 result was already on disk.

## Locked design

- zone fixed to `Q16..Q25`
- target subset fixed to `{16,21,22,23,25}`
- exact space = all `C(10,5) = 252` five-surah subsets
- composite = mean of z-scored `prophet_narrative_density`,
  `book_reference_density`, and `eschatological_density`
- z-scores computed over all 114 surahs from the existing H-NEW-125
  payload
- primary statistic = `Delta_C(S) = mean_C(S) - mean_C(Z\\S)`
- direction = one-sided upper-tail

## Exact outputs

- target mean composite `C_q` = `0.1467726994971126`
- complement mean composite `C_q` = `0.2854340133477646`
- observed `Delta_C(S*)` = `-0.13866131385065197`
- exact rank = `196 / 252`
- exact upper-tail `p = 0.7777777777777778`
- verdict = `NULL`

Null summary:

- null mean = `0.0`
- null median = `0.0`
- null min = `-0.43812930011736534`
- null max = `0.43812930011736534`

## Continuity note

This is the honest bounded follow-up after H-NEW-285 / 286. The compact
three-axis content composite does not explain the OQ-18 isolate core;
the target split is lower than its complement on the preregistered
upper-tail contrast.

## Files written

- `findings/phase-b-hypotheses/h-new-287-oq18-within-zone-three-axis-content-composite-prereg.md`
- `scripts/h_new_287_oq18_three_axis_content_composite.py`
- `findings/phase-b-hypotheses/csv/h-new-287.json`
- `findings/phase-b-hypotheses/h-new-287-oq18-within-zone-three-axis-content-composite.md`
- `journal/h-new-287-run-1.md`
