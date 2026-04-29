---
id: H-NEW-273
title: "Q1<->Q108 twin liturgical-anchor test — exact matched-null on divine-reference x imperative density"
phase: B
status: PRE-REGISTERED-FOR-FORMAL-RUN
date: 2026-04-18
specialist: codex
seed: 20260418
bonferroni_k: 1
alpha_raw: 0.05
alpha_bon: 0.05
bonferroni_family: h-new-273-q1-q108-twin-liturgical-anchor
parent_backdrop:
  - h-new-131-1 (Q108 robust high-degree MST hub after length-normalization)
  - h-new-137 (Q1 nearest-neighbor linkage to Q108..114 at root level)
  - h-new-138 (wrap-around closure replicates on char-4-gram and verse-length)
scope_note: "Metric family chosen after bounded local scoping of candidate liturgical operationalizations; this file locks the first landed formal run only."
rules_tuple: "(QAC v0.4 STEM roots via surah-root-graph.json; imperative density via findings/phase-b-hypotheses/csv/imperatives-per-surah.csv; divine-reference root set locked to {Alh,rbb,rHm}; surah score S(s)=sqrt(D(s)*I(s)) where D(s)=share of root tokens in {Alh,rbb,rHm} and I(s)=imperative tokens per verse; pair score T(a,b)=S(a)+S(b); exact matched null over unordered Early-Meccan pairs with verse bins {5-7,3-4}; Hafs-Kufan; basmala-counted-only-in-surah-1)"
---

# [[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]] — Q1<->Q108 twin liturgical-anchor test

## Question

Can the `Q1 <-> Q108` "twin liturgical-anchor" idea be stated in one
bounded, falsifiable way without re-running the already-landed
wrap-around-distance tests?

This run answers that with a single pair score:

- `Q1 al-Fatihah` should contribute a strong **divine-reference** profile.
- `Q108 al-Kawthar` should contribute a strong **imperative liturgical**
  profile.
- The pair should jointly sit unusually high among short Early-Meccan
  matched pairs if the twin-anchor reading is real on this axis.

## Locked operationalization

For each surah `s`, define:

- `D(s)` = fraction of all QAC STEM-root tokens in surah `s` whose root is in
  the fixed divine-reference set `{Alh, rbb, rHm}`.
- `I(s)` = imperative density = `IMPV tokens / verses` from the existing
  repo-wide imperative extractor.
- `S(s)` = `sqrt(D(s) * I(s))`.

Interpretation:

- `S(s)` is high only when a surah has both non-trivial divine-reference
  mass and non-trivial imperative density.
- The geometric mean prevents a surah from scoring high by only one side.

For the target pair, define:

- `T(Q1,Q108) = S(Q1) + S(Q108)`

## Null

Use an **exact matched null**, not a permutation sample.

Enumerate all unordered surah pairs satisfying all three conditions:

1. both surahs are `Early Meccan` by `revelation-order.csv`
2. one surah lies in the verse-count bin `5-7`
3. one surah lies in the verse-count bin `3-4`

This matches the coarse shape of the target:

- Q1 = 7 verses, Early Meccan
- Q108 = 3 verses, Early Meccan

Primary p-value:

- exact upper-tail
- `p = (1 + # {null pairs with T >= T_obs}) / (1 + N_null)`

Decision rule:

- `PASS-NARROW` if exact upper-tail `p < 0.05`
- otherwise `NULL`

No family correction beyond `k = 1`; this is a single landed cell.

## Why this operationalization is acceptable

This test is deliberately narrow:

- it does not ask whether Q1 and Q108 are nearest neighbors overall
- it does not ask whether they explain the mushaf architecture
- it does not ask whether liturgy caused structure

It asks only whether the pair is unusually strong on **one explicit
speech-act axis**:

- divine reference
- imperative liturgical force

## Descriptive contrast (not part of the decision rule)

If compute permits, report the same score for `Q113 + Q114` under its own
matched Early-Meccan `5-7` + `5-7` null as an honesty contrast.

This is **not** a ratifying positive control for the main verdict. It is
only a check on whether the landed metric behaves like a general
liturgical-pair detector or like a narrower Q1/Q108-specific construct.

## Deliverables

- Script: `scripts/h_new_273_q1_q108_twin_liturgical_anchor.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-273.json`
- Findings: `findings/phase-b-hypotheses/h-new-273-q1-q108-twin-liturgical-anchor.md`
- Journal: `journal/h-new-273-run-1.md`
