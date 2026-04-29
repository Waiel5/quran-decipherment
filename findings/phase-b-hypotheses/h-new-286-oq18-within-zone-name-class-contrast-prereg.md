---
id: H-NEW-286
title: "OQ-18 within-zone name-class contrast"
status: PRE-REGISTERED 2026-04-18
spec_locked_at: 2026-04-18
author: codex
seed: 20260418
exact_space_n: 252
bonferroni_family: h-new-286-oq18-within-zone-name-class-contrast
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED
rules_tuple: "(QAC v0.4 surah-name map reused from findings/phase-b-hypotheses/csv/h-new-126.json Cell B; binary label = concept/object-named vs other; exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25; primary statistic = Delta_name(S)=mean_{q in S} I[label(q)=concept/object]-mean_{q in Z\\S} I[label(q)=concept/object]; one-sided upper-tail)"
prior_work_consulted:
  - findings/phase-b-hypotheses/h-new-126-isolate-core.md
  - findings/phase-b-hypotheses/h-new-281-true-isolate-core-within-zone-jaccard.md
  - findings/phase-b-hypotheses/h-new-285-oq18-within-zone-contrast.md
  - findings/phase-b-hypotheses/csv/h-new-126.json
---

# [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] — OQ-18 within-zone name-class contrast

## Question

[[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] showed that the pre-identified core `{Q16, Q21, Q22, Q23, Q25}`
is unusually cohesive inside the fixed `Q16..Q25` zone under exact
root-Jaccard nulls. [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] then showed that the same split also beats
its exact within-zone complement on the same root-Jaccard instrument.

[[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] asks the narrower name-class question:

> inside `Q16..Q25`, does the target subset `S* = {16,21,22,23,25}` isolate
> the entire concept/object-named class when the surah names are collapsed
> to a binary label?

This is a bounded follow-up, not a search over all surah-name groupings.

## Frozen target and search space

- Zone fixed in advance: `Q16..Q25`
- Target subset fixed in advance: `{Q16, Q21, Q22, Q23, Q25}`
- Exact null space:
  all `C(10,5) = 252` unordered five-surah subsets of `Q16..Q25`

No surah may be added, dropped, or reweighted after results.

## Binary label

The label is collapsed to:

- `concept/object-named`
- `other`

The concept/object set is reused from the on-disk [[h-new-126-isolate-core|H-NEW-126]] Cell B map:
`{16, 21, 22, 23, 25}`.

Within `Q16..Q25`, every surah not in that set is labeled `other`.

## Primary statistic

For any five-surah subset `S`, define

`Delta_name(S) = mean_{q in S} I[label(q)=concept/object] - mean_{q in Z\\S} I[label(q)=concept/object]`

where `Z = {16..25}`.

The target statistic is `Delta_name(S*)` for
`S* = {16,21,22,23,25}`.

### Direction

One-sided upper-tail.

Higher `Delta_name(S)` means the target half of the zone is more
concentrated in concept/object-named surahs than the opposite half.

## Primary exact null

Enumerate all 252 five-surah subsets of `Q16..Q25`. Compute
`Delta_name(S)` for every subset.

For the target subset `S*`, define

`p_exact = #{S : Delta_name(S) >= Delta_name(S*)} / 252`

and descending rank

`rank_desc = 1 + #{S : Delta_name(S) > Delta_name(S*)}`.

The primary cell is counted as a directed pass if:

- `p_exact < 0.05`

Because the target subset was surfaced by prior work rather than from a
blind discovery pipeline, the verdict ceiling is **PASS-DIRECTED**, not
CONFIRMED.

## Why this test matters

This is the cleanest name-class follow-up to [[h-new-126-isolate-core|H-NEW-126]] / [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] /
[[h-new-285-oq18-within-zone-contrast|H-NEW-285]]:

- [[h-new-126-isolate-core|H-NEW-126]] established that the target 5-set is concept/object-named.
- [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] asked whether the same 5-set is internally cohesive inside
  `Q16..Q25` under root-Jaccard.
- [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] asked whether the same 5-set beats its complement under the
  same within-zone root-Jaccard contrast.
- [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] checks the categorical name-class mechanism directly, with
  the same fixed zone and the same exact 5-of-10 search space.

## Garden of forking paths frozen before execution

- zone = exactly `Q16..Q25`
- subset size = exactly 5
- target subset = exactly `{16,21,22,23,25}`
- binary label = concept/object-named vs other
- label source = [[h-new-126-isolate-core|H-NEW-126]] Cell B map
- null = full exact enumeration, not Monte Carlo
- direction = upper-tail

## Not allowed after results

- widening the zone beyond `Q16..Q25`
- switching to a different target subset
- splitting the labels into more than two categories
- count-weighting the labels after the fact
- introducing a new matched null inside this same finding

Those would require a new prereg.

## Deliverables

1. `findings/phase-b-hypotheses/h-new-286-oq18-within-zone-name-class-contrast-prereg.md`
2. `scripts/h_new_286_oq18_within_zone_name_class_contrast.py`
3. `findings/phase-b-hypotheses/csv/h-new-286.json`
4. `findings/phase-b-hypotheses/h-new-286-oq18-within-zone-name-class-contrast.md`
5. `journal/h-new-286-run-1.md`
