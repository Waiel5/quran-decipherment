# H-NEW-281 run journal

Date: 2026-04-18
Operator: codex

## Scope

Local harvest of the exact within-zone OQ-18 test after the JSON result
landed on disk but the finding/journal prose files had not yet been
written.

## Locked design

- zone fixed to `Q16..Q25`
- target subset fixed to `{16,21,22,23,25}`
- exact space = all `C(10,5) = 252` five-surah subsets
- primary statistic = mean pairwise root-set Jaccard
- direction = one-sided upper-tail

## Key outputs

- observed primary statistic = `0.34138556942690185`
- exact rank = `8 / 252`
- exact upper-tail `p = 0.031746031746031744`
- verdict = `PASS-DIRECTED`

Secondary descriptive context:

- shared-root spine count = `80`
- secondary rank = `11 / 252`

## Continuity note

This finding directly answers the open H-NEW-168 follow-up question:
the true-isolate core is unusually cohesive even inside its own
Q16-25 zone, not only against a global random-5 comparison.
