---
id: H-NEW-287
title: OQ-18 within-zone three-axis content composite
phase: B
status: NULL
date: 2026-04-19
agent: codex
parent_1: H-NEW-286
open_question: OQ-18
seed: 20260419
prereg: findings/phase-b-hypotheses/h-new-287-oq18-within-zone-three-axis-content-composite-prereg.md
script: scripts/h_new_287_oq18_three_axis_content_composite.py
json: findings/phase-b-hypotheses/csv/h-new-287.json
journal: journal/h-new-287-run-1.md
rules_tuple: "(H-NEW-125 per-surah axis values reused from h-new-125.json; per-surah C_q = mean(z(prophet_narrative_density), z(book_reference_density), z(eschatological_density)) with z-scores computed over all 114 surahs; exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25; primary statistic = Delta_C(S)=mean_{q in S} C_q-mean_{q in Z\\S} C_q; one-sided upper-tail)"
---

# [[h-new-287-oq18-within-zone-three-axis-content-composite|H-NEW-287]] — OQ-18 within-zone three-axis content composite

## Summary

Using only the three already-locked [[h-new-125-chronology-content|H-NEW-125]] content axes
`prophet_narrative_density`, `book_reference_density`, and
`eschatological_density`, the target OQ-18 split does not outperform its
within-zone complement.

The composite is built as:

`C_q = mean(z(prophet_narrative_density), z(book_reference_density), z(eschatological_density))`

with each z-score computed over all 114 surahs. Inside `Q16..Q25`, the
target 5-set lands well below the exact upper-tail threshold.

## Result

Primary statistic:

`Delta_C(S) = mean_{q in S} C_q - mean_{q in Z\\S} C_q`

Observed at `S* = {16,21,22,23,25}`:

- target mean composite `C_q` = `0.1467726994971126`
- complement mean composite `C_q` = `0.2854340133477646`
- observed `Delta_C(S*)` = `-0.13866131385065197`
- exact upper-tail `p = 0.7777777777777778`
- exact descending rank = `196 / 252`
- verdict = `NULL`

## Exact null summary

- null space size = `252`
- null mean = `0.0`
- null median = `0.0`
- null min = `-0.43812930011736534`
- null max = `0.43812930011736534`

## Interpretation

This is a clean negative result for the compact three-axis composite.
The target OQ-18 core is not the high-composite half of the zone; the
complement is. So this composite does not provide the explanatory
mechanism that [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] and [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] already narrowed toward.

That makes the honest conclusion simple: the compact [[h-new-125-chronology-content|H-NEW-125]] content
axes are relevant background structure, but this particular 3-axis mean
is not the mechanism for the OQ-18 isolate core.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-287-oq18-within-zone-three-axis-content-composite-prereg.md`
- Script: `scripts/h_new_287_oq18_three_axis_content_composite.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-287.json`
- Journal: `journal/h-new-287-run-1.md`
