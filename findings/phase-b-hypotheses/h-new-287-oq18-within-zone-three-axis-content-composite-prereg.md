---
id: H-NEW-287
title: "OQ-18 within-zone three-axis content composite"
status: PRE-REGISTERED 2026-04-19
spec_locked_at: 2026-04-19
author: codex
seed: 20260419
exact_space_n: 252
bonferroni_family: h-new-287-oq18-within-zone-three-axis-content-composite
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED
rules_tuple: "(H-NEW-125 per-surah axis values reused from findings/phase-b-hypotheses/csv/h-new-125.json; per-surah C_q = mean(z(prophet_narrative_density), z(book_reference_density), z(eschatological_density)) with z-scores computed over all 114 surahs; exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25; primary statistic = Delta_C(S)=mean_{q in S} C_q - mean_{q in Z\\S} C_q; one-sided upper-tail)"
prior_work_consulted:
  - findings/phase-b-hypotheses/h-new-125-chronology-content-prereg.md
  - findings/phase-b-hypotheses/h-new-281-true-isolate-core-within-zone-jaccard.md
  - findings/phase-b-hypotheses/h-new-285-oq18-within-zone-contrast.md
  - findings/phase-b-hypotheses/h-new-286-oq18-within-zone-name-class-contrast.md
  - findings/phase-b-hypotheses/csv/h-new-125.json
---

# [[h-new-287-oq18-within-zone-three-axis-content-composite|H-NEW-287]] — OQ-18 within-zone three-axis content composite

## Question

[[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] showed that the target core `{Q16, Q21, Q22, Q23, Q25}` is
locally cohesive inside the fixed `Q16..Q25` zone under exact
root-Jaccard nulls. [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] then showed the same split also beats its
exact complement inside the zone. [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] added a categorical
name-class foothold.

[[h-new-287-oq18-within-zone-three-axis-content-composite|H-NEW-287]] asks whether a compact content composite built only from
already-locked [[h-new-125-chronology-content|H-NEW-125]] axes can explain the same target split:

> inside `Q16..Q25`, is the target subset `S* = {16,21,22,23,25}`
> unusually high on a three-axis content composite made from prophet
> narrative, book-reference, and eschatological density?

This is a bounded follow-up, not a search over alternate axes or
weights.

## Frozen target and search space

- Zone fixed in advance: `Q16..Q25`
- Target subset fixed in advance: `{Q16, Q21, Q22, Q23, Q25}`
- Exact null space: all `C(10,5) = 252` unordered five-surah subsets of
  `Q16..Q25`

No surah may be added, dropped, or reweighted after results.

## Data

The composite reuses the existing [[h-new-125-chronology-content|H-NEW-125]] per-surah axis definitions:

- `prophet_narrative_density`
- `book_reference_density`
- `eschatological_density`

Each axis is z-scored over all 114 surahs using the already-computed
[[h-new-125-chronology-content|H-NEW-125]] per-surah values in `findings/phase-b-hypotheses/csv/h-new-125.json`.

For each surah `q`, define:

`C_q = mean(z(prophet_narrative_density), z(book_reference_density), z(eschatological_density))`

The composite is centered over the full corpus; the zone test only uses
the resulting per-surah `C_q` values.

## Primary statistic

For any five-surah subset `S`, define

`Delta_C(S) = mean_{q in S} C_q - mean_{q in Z\\S} C_q`

where `Z = {16..25}`.

The target statistic is `Delta_C(S*)` for
`S* = {16,21,22,23,25}`.

### Direction

One-sided upper-tail.

Higher `Delta_C(S)` means the target half of the zone is more elevated
on the compact three-axis content composite than the opposite half.

## Primary exact null

Enumerate all 252 five-surah subsets of `Q16..Q25`. Compute `Delta_C(S)`
for every subset.

For the target subset `S*`, define

`p_exact = #{S : Delta_C(S) >= Delta_C(S*)} / 252`

and descending rank

`rank_desc = 1 + #{S : Delta_C(S) > Delta_C(S*)}`.

The primary cell is counted as a directed pass if:

- `p_exact < 0.05`

Because the target subset was surfaced by prior work rather than from a
blind discovery pipeline, the verdict ceiling is **PASS-DIRECTED**, not
CONFIRMED.

## Why this test matters

This is the narrowest honest content-axis follow-up to [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] /
[[h-new-285-oq18-within-zone-contrast|H-NEW-285]] / [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]]:

- [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] asked whether the target 5-set is unusually cohesive on its
  own inside `Q16..Q25`.
- [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] asked whether the target 5-set also outperforms the exact
  complementary 5-set inside the same zone.
- [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] checked a categorical label mechanism directly.
- [[h-new-287-oq18-within-zone-three-axis-content-composite|H-NEW-287]] asks whether a compact, pre-locked three-axis content
  composite built from [[h-new-125-chronology-content|H-NEW-125]] axis definitions explains the same
  split.

## Garden of forking paths frozen before execution

- zone = exactly `Q16..Q25`
- subset size = exactly 5
- target subset = exactly `{16,21,22,23,25}`
- axes = exactly `prophet_narrative_density`, `book_reference_density`,
  `eschatological_density`
- z-scoring = full-corpus 114-surah standardization
- composite = unweighted mean of the 3 z-scores
- null = full exact enumeration, not Monte Carlo
- direction = upper-tail

## Not allowed after results

- widening the zone beyond `Q16..Q25`
- switching to a different target subset
- changing the three locked axes
- adding a fourth axis or reweighting the three axes after the fact
- introducing a fresh matched null inside this same finding

Those would require a new prereg.

## Deliverables

1. `findings/phase-b-hypotheses/h-new-287-oq18-within-zone-three-axis-content-composite-prereg.md`
2. `scripts/h_new_287_oq18_three_axis_content_composite.py`
3. `findings/phase-b-hypotheses/csv/h-new-287.json`
4. `findings/phase-b-hypotheses/h-new-287-oq18-within-zone-three-axis-content-composite.md`
5. `journal/h-new-287-run-1.md`
