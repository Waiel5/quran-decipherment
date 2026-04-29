# H-NEW-285 run journal

Date: 2026-04-18
Operator: codex

## Scope

Run the preregistered exact within-zone 5-vs-5 contrast test for
H-NEW-285 after the H-NEW-281 result was already on disk.

## Locked design

- zone fixed to `Q16..Q25`
- target subset fixed to `{16,21,22,23,25}`
- complement fixed to `{17,18,19,20,24}`
- exact space = all `C(10,5) = 252` five-surah subsets
- primary statistic = `Delta(S) = mean_pairwise_root_jaccard(S) - mean_pairwise_root_jaccard(Z\\S)`
- direction = one-sided upper-tail

## Key outputs

- target mean pairwise root-Jaccard = `0.34138556942690185`
- complement mean pairwise root-Jaccard = `0.30516838491368325`
- observed delta = `0.03621718451321859`
- exact rank = `12 / 252`
- exact upper-tail `p = 0.047619047619047616`
- verdict = `PASS-DIRECTED`

Null summary:

- null mean = `0`
- null median = `0`
- null min = `-0.04970470738489352`
- null max = `0.04970470738489352`

## Continuity note

This is a bounded refinement of H-NEW-281, not a new corpus-wide search.
The exact within-zone contrast is positive, but only marginally above
the 0.05 threshold.
