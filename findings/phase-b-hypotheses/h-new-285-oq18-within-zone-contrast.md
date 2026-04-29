---
id: H-NEW-285
title: OQ-18 within-zone 5-vs-5 contrast test
phase: B
status: PASS-DIRECTED
date: 2026-04-18
agent: codex
parent_1: H-NEW-281
open_question: OQ-18
seed: 20260418
prereg: findings/phase-b-hypotheses/h-new-285-oq18-within-zone-contrast-prereg.md
script: scripts/h_new_285_oq18_within_zone_contrast.py
json: findings/phase-b-hypotheses/csv/h-new-285.json
journal: journal/h-new-285-run-1.md
rules_tuple: "(QAC v0.4 root sets via surah-root-graph.json; exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25; primary statistic = Delta(S)=mean_pairwise_root_jaccard(S)-mean_pairwise_root_jaccard(Z\\S); one-sided upper-tail)"
---

# [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] — OQ-18 within-zone 5-vs-5 contrast test

## Headline

[[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] showed that the true-isolate core
`{Q16, Q21, Q22, Q23, Q25}` is unusually cohesive inside `Q16..Q25`.
[[h-new-285-oq18-within-zone-contrast|H-NEW-285]] tightened that into a direct 5-vs-5 contrast:

`Delta(S*) = mean_pairwise_root_jaccard(S*) - mean_pairwise_root_jaccard(Z\\S*)`

where `S* = {16,21,22,23,25}` and `Z\\S* = {17,18,19,20,24}`.

The result is positive and exact, but only marginally so.

- target mean pairwise root-Jaccard = **`0.34138556942690185`**
- complement mean pairwise root-Jaccard = **`0.30516838491368325`**
- observed `Delta(S*)` = **`0.03621718451321859`**
- exact rank = **`12 / 252`**
- exact one-sided upper-tail `p` = **`0.047619047619047616`**
- verdict = **PASS-DIRECTED**

## Interpretation

This keeps the comparison entirely internal to the fixed `Q16..Q25`
zone and asks whether the target split beats its exact complement. It
does, but just barely.

So the honest read is:

- the target half remains locally strong under the exact within-zone
  contrast
- the evidence clears `0.05`, but not by much
- this is a directed pass, not a robust separation

## Exact null summary

- null space size = `252`
- null mean = `0`
- null median = `0`
- null min = `-0.04970470738489352`
- null max = `0.04970470738489352`

## Bottom line

The true-isolate core still outruns its within-zone complement on mean
pairwise root-Jaccard, but only marginally. That is enough for
`PASS-DIRECTED` under the preregistered exact upper-tail null, and no
more.
