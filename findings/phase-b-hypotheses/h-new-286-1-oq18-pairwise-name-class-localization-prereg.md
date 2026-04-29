---
id: H-NEW-286.1
title: "OQ-18 pairwise name-class localization"
status: PRE-REGISTERED 2026-04-19
spec_locked_at: 2026-04-19
author: codex
seed: 20260419
exact_space_n: 252
bonferroni_family: h-new-286-1-oq18-pairwise-name-class-localization
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED
rules_tuple: "(QAC v0.4 root sets via data/morphology/surah-root-graph.json; binary concept/object-vs-other label reused from findings/phase-b-hypotheses/csv/h-new-126.json Cell B and H-NEW-286; fixed zone = Q16..Q25; exact enumeration over all C(10,5)=252 positive-label assignments preserving the 5/5 split; primary statistic = Delta_pair(L)=mean_jaccard(++)-mean_jaccard(other pairs); one-sided upper-tail)"
prior_work_consulted:
  - findings/phase-b-hypotheses/h-new-126-isolate-core.md
  - findings/phase-b-hypotheses/h-new-281-true-isolate-core-within-zone-jaccard.md
  - findings/phase-b-hypotheses/h-new-285-oq18-within-zone-contrast.md
  - findings/phase-b-hypotheses/h-new-286-oq18-within-zone-name-class-contrast.md
  - findings/phase-b-hypotheses/csv/h-new-126.json
  - scripts/h_new_285_oq18_within_zone_contrast.py
  - scripts/h_new_286_oq18_within_zone_name_class_contrast.py
---

# [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] — OQ-18 pairwise name-class localization

## Question

[[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] showed that inside the fixed `Q16..Q25` zone, the exact
concept/object-named set `{Q16, Q21, Q22, Q23, Q25}` is the categorical
5-surah split picked out by the [[h-new-126-isolate-core|H-NEW-126]] name map. That establishes the
class boundary, but it does not yet show whether this same boundary
localizes the **pairwise overlap structure** seen in [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] / [[h-new-285-oq18-within-zone-contrast|H-NEW-285]].

This prereg therefore asks:

> when the ten surahs in `Q16..Q25` are represented by the same root-set
> Jaccard instrument used in [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] / [[h-new-285-oq18-within-zone-contrast|H-NEW-285]], does the positive
> concept/object label pick out the unusually high-overlap **pairs**, not
> just the best 5-set in aggregate?

## Frozen zone and label map

- Zone fixed in advance: `Q16..Q25`
- Positive label fixed in advance:
  `concept/object-named = {Q16, Q21, Q22, Q23, Q25}`
- Negative label fixed in advance:
  `{Q17, Q18, Q19, Q20, Q24}`

The binary label is reused exactly from the on-disk [[h-new-126-isolate-core|H-NEW-126]] Cell B map
as already frozen by [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]].

## Data representation

- Root inventory:
  `data/morphology/surah-root-graph.json`

Each surah is represented as the set of QAC roots present anywhere in
that surah. Counts are ignored, matching [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] / [[h-new-285-oq18-within-zone-contrast|H-NEW-285]].

For each unordered pair `(a,b)` in `Q16..Q25`, define

`J(a,b) = |R_a ∩ R_b| / |R_a ∪ R_b|`.

## Primary statistic

For any 5-positive assignment `L` over the ten surahs, let:

- `++(L)` be the 10 unordered pairs where both surahs are positive
- `other(L)` be the remaining 35 unordered pairs

Then define

`Delta_pair(L) = mean_{(a,b) in ++(L)} J(a,b) - mean_{(a,b) in other(L)} J(a,b)`.

The observed assignment is

`L* = {Q16, Q21, Q22, Q23, Q25}`.

### Direction

One-sided upper-tail.

Higher `Delta_pair(L)` means the positive label isolates the high-overlap
pair mass more strongly.

## Primary exact null

Enumerate all `C(10,5) = 252` assignments of exactly 5 positive labels
over `Q16..Q25`. For each assignment `L`, compute `Delta_pair(L)`.

For the observed label assignment `L*`, define

`p_exact = #{L : Delta_pair(L) >= Delta_pair(L*)} / 252`

and descending rank

`rank_desc = 1 + #{L : Delta_pair(L) > Delta_pair(L*)}`.

The primary cell is counted as a directed pass if:

- `p_exact < 0.05`

Because the observed positive set was surfaced by prior work rather than
from a blind discovery pipeline, the verdict ceiling is
**PASS-DIRECTED**, not CONFIRMED.

## Descriptive quantities

These are descriptive only and do not change the verdict:

- mean Jaccard across `++` pairs
- mean Jaccard across `+-` pairs
- mean Jaccard across `--` pairs
- mean Jaccard across `other = (+-) U (--)`
- observed pair table for all 45 within-zone pairs

## Why this test matters

This is the narrowest honest pair-level follow-up to [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]]:

- [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] showed the target 5-set is internally cohesive.
- [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] showed the target 5-set beats its exact complement.
- [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] showed the same 5-set is exactly the concept/object class.
- [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] asks whether that same class boundary localizes the
  pairwise overlap concentration itself.

If this passes, the name-class mechanism is not merely set-level. It
reaches down to the pair structure. If it fails, the mechanism remains
real at the 5-set level but does not cleanly explain the pair table.

## Garden of forking paths frozen before execution

- zone = exactly `Q16..Q25`
- positive label = exactly [[h-new-126-isolate-core|H-NEW-126]] / [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] concept/object set
- negative label = the remaining five surahs in the zone
- representation = surah-level root sets, not counts
- pair score = set Jaccard
- primary statistic = mean `++` pair Jaccard minus mean non-`++` pair
  Jaccard
- null = full exact enumeration, not Monte Carlo
- direction = upper-tail

## Not allowed after results

- widening the zone beyond `Q16..Q25`
- changing the positive label set
- excluding mixed pairs from `other` after the fact
- swapping in a different pair statistic or weighting scheme
- promoting any descriptive split to primary

Those would require a new prereg.

## Deliverables

1. `findings/phase-b-hypotheses/h-new-286-1-oq18-pairwise-name-class-localization-prereg.md`
2. `scripts/h_new_286_1_oq18_pairwise_name_class_localization.py`
3. `findings/phase-b-hypotheses/csv/h-new-286-1.json`
4. `findings/phase-b-hypotheses/h-new-286-1-oq18-pairwise-name-class-localization.md`
5. `journal/h-new-286-1-run-1.md`
