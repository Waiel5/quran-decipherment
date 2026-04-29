---
id: H-NEW-285
title: "OQ-18 within-zone 5-vs-5 contrast test"
status: PRE-REGISTERED 2026-04-18
spec_locked_at: 2026-04-18
author: codex
seed: 20260418
exact_space_n: 252
bonferroni_family: h-new-285-oq18-within-zone-contrast
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED
rules_tuple: "(QAC v0.4 root sets via data/morphology/surah-root-graph.json; exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25; primary statistic = Delta(S)=mean_pairwise_root_jaccard(S)-mean_pairwise_root_jaccard(Z\\S); one-sided upper-tail)"
prior_work_consulted:
  - findings/phase-b-hypotheses/h-new-281-true-isolate-core-within-zone-jaccard.md
  - findings/phase-b-hypotheses/h-new-168-q16-25-concentrator-mode.md
  - findings/phase-b-hypotheses/h-new-126-isolate-core.md
  - scripts/h_new_281_true_isolate_core_within_zone_jaccard.py
---

# [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] — OQ-18 within-zone 5-vs-5 contrast test

## Question

[[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] showed that the true-isolate core `{Q16, Q21, Q22, Q23, Q25}`
has unusually high internal mean pairwise root-Jaccard inside the fixed
`Q16..Q25` zone. The sharper OQ-18 contrast question is whether that same
target split also beats its exact within-zone complement.

This prereg therefore freezes a single contrast:

> compare the target 5-surah subset `S* = {16,21,22,23,25}` against its
> exact complement `Z\\S* = {17,18,19,20,24}` inside the same ten-surah
> zone.

## Frozen target and search space

- Zone fixed in advance: `Q16..Q25`
- Target subset fixed in advance: `{Q16, Q21, Q22, Q23, Q25}`
- Complement fixed in advance: `{Q17, Q18, Q19, Q20, Q24}`
- Exact null space:
  all `C(10,5) = 252` unordered five-surah subsets of `Q16..Q25`

No surah may be added, dropped, or reweighted after results.

## Data

- Root inventory:
  `data/morphology/surah-root-graph.json`

Each surah is represented as a set of QAC roots present anywhere in
that surah. Counts are ignored for this test.

## Primary statistic

For any five-surah subset `S`, define

`T(S) = mean_{a<b in S} J(root_set_a, root_set_b)`

where

`J(A,B) = |A ∩ B| / |A ∪ B|`.

Then define the contrast statistic

`Delta(S) = T(S) - T(Z\\S)`.

The target statistic is `Delta(S*)` for `S* = {16,21,22,23,25}`.

### Direction

One-sided upper-tail.

Higher `Delta(S)` means the target half of the zone is more internally
cohesive than the opposite half.

## Primary exact null

Enumerate all 252 five-surah subsets of `Q16..Q25`. Compute `Delta(S)`
for every subset.

For the target subset `S*`, define

`p_exact = #{S : Delta(S) >= Delta(S*)} / 252`

and descending rank

`rank_desc = 1 + #{S : Delta(S) > Delta(S*)}`.

The primary cell is counted as a directed pass if:

- `p_exact < 0.05`

Because the target subset was surfaced by prior work rather than from a
blind discovery pipeline, the verdict ceiling is **PASS-DIRECTED**, not
CONFIRMED.

## Why this test matters

This is the narrowest honest follow-up to [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]]:

- [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] asked whether the target 5-set was unusually cohesive on
  its own inside `Q16..Q25`.
- [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] asks whether the target 5-set also outperforms the exact
  complementary 5-set inside the same zone.

That keeps the comparison fully internal to the same fixed zone and
avoids introducing any new corpus-wide or chronology-matched null.

## Garden of forking paths frozen before execution

- zone = exactly `Q16..Q25`
- subset size = exactly 5
- target subset = exactly `{16,21,22,23,25}`
- complement = exactly `Z\\S*`
- representation = surah-level root sets, not counts
- similarity = pairwise set Jaccard
- primary statistic = target minus complement mean Jaccard
- null = full exact enumeration, not Monte Carlo
- direction = upper-tail

## Not allowed after results

- widening the zone beyond `Q16..Q25`
- switching to a different target subset
- switching to a different contrast functional
- count-weighting roots after the fact
- adding a secondary statistic and promoting it to primary
- introducing a fresh matched null inside this same finding

Those would require a new prereg.

## Deliverables

1. `findings/phase-b-hypotheses/h-new-285-oq18-within-zone-contrast-prereg.md`
2. `scripts/h_new_285_oq18_within_zone_contrast.py`
3. `findings/phase-b-hypotheses/csv/h-new-285.json`
4. `findings/phase-b-hypotheses/h-new-285-oq18-within-zone-contrast.md`
5. `journal/h-new-285-run-1.md`
