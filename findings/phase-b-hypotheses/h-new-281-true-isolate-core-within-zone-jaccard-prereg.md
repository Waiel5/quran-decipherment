---
id: H-NEW-281
title: "true-isolate core within-zone exact Jaccard test"
status: PRE-REGISTERED 2026-04-18
spec_locked_at: 2026-04-18
author: codex
seed: 20260418
exact_space_n: 252
bonferroni_family: h-new-281-true-isolate-core-within-zone-jaccard
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED
rules_tuple: "(QAC v0.4 root sets via data/morphology/surah-root-graph.json; exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25; primary statistic = mean pairwise root-set Jaccard; one-sided upper-tail)"
prior_work_consulted:
  - HANDOFF/05-OPEN-QUESTIONS.md
  - findings/phase-b-hypotheses/h-new-126-isolate-core.md
  - findings/phase-b-hypotheses/h-new-168-q16-q25-dispersion.md
  - scripts/h_new_126_isolate_core.py
  - scripts/h_new_168_q16_q25_dispersion.py
---

# [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] — true-isolate core within-zone exact Jaccard test

## Question

[[h-new-126-isolate-core|H-NEW-126]] showed that the true-isolate core
`{Q16, Q21, Q22, Q23, Q25}` has unusually high mean pairwise
root-Jaccard against a **global random-5 non-core null**. [[h-new-168-q16-q25-dispersion|H-NEW-168]] then
showed that the wider `Q16..Q25` zone is itself an internally-similar
concentrator community.

This follow-up asks the sharper bounded question:

> **within the already-coherent `Q16..Q25` zone itself, does the
> pre-identified true-isolate core still sit unusually high on internal
> root overlap?**

That is the relevant mechanism test for OQ-18. If the core is merely a
random 5-of-10 slice from a broadly coherent zone, it should not stand
out strongly against the other 251 exact five-surah subsets of the same
zone.

## Frozen target and search space

- Zone fixed in advance: `Q16..Q25`
- Target subset fixed in advance from prior work:
  `{Q16, Q21, Q22, Q23, Q25}`
- Exact null space:
  **all** `C(10,5) = 252` unordered five-surah subsets of `Q16..Q25`

No surah may be added, dropped, or reweighted after results.

## Data

- Root inventory:
  `data/morphology/surah-root-graph.json`

Each surah is represented as a **set** of QAC roots present anywhere in
that surah. Counts are ignored for this test, matching [[h-new-126-isolate-core|H-NEW-126]]'s
pairwise root-set Jaccard instrument.

## Primary statistic

For a five-surah subset `S`, define

`T(S) = mean_{a<b in S} J(root_set_a, root_set_b)`

where

`J(A,B) = |A ∩ B| / |A ∪ B|`.

There are 10 unordered pairs inside each five-surah subset, so `T(S)` is
the mean of those 10 pairwise Jaccards.

### Direction

**One-sided upper-tail**.

Higher `T(S)` means the subset is more internally coherent in root-set
space.

## Primary exact null

Enumerate all 252 subsets of size 5 from `Q16..Q25`. Compute `T(S)` for
every subset.

For the target subset `S* = {16,21,22,23,25}`, define

`p_exact = #{S : T(S) >= T(S*)} / 252`

and descending rank

`rank_desc = 1 + #{S : T(S) > T(S*)}`.

The primary cell is counted as a directed pass if:

- `p_exact < 0.05`

Because the target subset was surfaced by prior work rather than from a
blind discovery pipeline, the verdict ceiling is **PASS-DIRECTED**, not
CONFIRMED.

## Secondary descriptive statistic

As a subordinate descriptive supplement only, also compute for each
five-surah subset:

`U(S) = |intersection of the 5 surah root sets|`

This is the **shared-root spine count**: how many roots appear in all
five surahs of the subset.

This secondary quantity is reported descriptively, including its exact
rank inside the same 252-subset space, but it does **not** drive the
family verdict and carries no separate pass/fail label.

## Why this test matters

This exact within-zone null addresses the main honest caveat from
[[h-new-126-isolate-core|H-NEW-126]]:

- the earlier global null could partly reward the core simply for living
  inside a long, internally-similar Late-Meccan / mixed zone
- the present test holds the zone fixed and asks whether the exact
  five-surah core is special **relative to alternate 5-of-10 splits from
  the same zone**

So this is a mechanism-sharpening test, not a generic replication.

## Garden of forking paths frozen before execution

- zone = exactly `Q16..Q25`
- subset size = exactly 5
- target subset = exactly `{16,21,22,23,25}`
- representation = surah-level root **sets**, not counts
- similarity = pairwise set Jaccard
- primary statistic = mean over the 10 within-subset pairs
- null = full exact enumeration, not Monte Carlo
- direction = upper-tail
- secondary supplement = shared-root spine count only

## Not allowed after results

- widening the zone beyond `Q16..Q25`
- switching the target to a different 5-surah subset
- swapping Jaccard for cosine, TF-IDF, embeddings, or Fisher-Rao
- count-weighting roots after the fact
- promoting the secondary shared-root spine statistic to the primary
- introducing a fresh matched-length or chronology-matched null inside
  this same finding

Those would require a new prereg.

## Post-hoc-noticed disclosure

The zone and target subset are both prior-known from [[h-new-126-isolate-core|H-NEW-126]] /
[[h-new-168-q16-q25-dispersion|H-NEW-168]] / [[cross-finding-010-extended-network|cross-finding-010]]. This finding therefore tests a
**post-hoc surfaced target under a new bounded exact null**. That is why
the verdict ceiling is limited to **PASS-DIRECTED**.

## Deliverables

1. `findings/phase-b-hypotheses/h-new-281-true-isolate-core-within-zone-jaccard-prereg.md`
2. `scripts/h_new_281_true_isolate_core_within_zone_jaccard.py`
3. `findings/phase-b-hypotheses/csv/h-new-281.json`
4. `findings/phase-b-hypotheses/h-new-281-true-isolate-core-within-zone-jaccard.md`
5. `journal/h-new-281-run-1.md`
