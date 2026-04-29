---
id: H-NEW-286.2
title: "OQ-18 Q17 conditional bridge test"
status: PRE-REGISTERED 2026-04-19
spec_locked_at: 2026-04-19
author: codex
seed: 20260419
exact_space_n: 126
bonferroni_family: h-new-286-2-q17-conditional-bridge-test
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED
rules_tuple: "(QAC v0.4 root sets via data/morphology/surah-root-graph.json; binary concept/object-vs-other label reused from findings/phase-b-hypotheses/csv/h-new-126.json Cell B and H-NEW-286; fixed zone = Q16..Q25; target nucleus = {Q16,Q21,Q22,Q23,Q25}; primary statistic reused exactly from H-NEW-286.1: Delta_pair(S)=mean_jaccard(++)-mean_jaccard(other pairs); primary null = exact enumeration over all C(9,5)=126 five-positive assignments drawn from Q16..Q25 with Q17 excluded from the positive side; one-sided upper-tail)"
prior_work_consulted:
  - findings/phase-b-hypotheses/h-new-281-true-isolate-core-within-zone-jaccard.md
  - findings/phase-b-hypotheses/h-new-285-oq18-within-zone-contrast.md
  - findings/phase-b-hypotheses/h-new-286-oq18-within-zone-name-class-contrast.md
  - findings/phase-b-hypotheses/h-new-286-1-oq18-pairwise-name-class-localization.md
  - findings/phase-b-hypotheses/csv/h-new-126.json
  - findings/phase-b-hypotheses/csv/h-new-286-1.json
  - scripts/h_new_286_1_oq18_pairwise_name_class_localization.py
---

# [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] — OQ-18 Q17 conditional bridge test

## Question

[[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] showed that the locked concept/object nucleus
`{Q16, Q21, Q22, Q23, Q25}` does localize the pairwise root-overlap
table inside `Q16..Q25`, but not perfectly: the observed assignment was
only rank `8 / 252`, and the top seven relabelings all included `Q17`.

That makes the next bounded question very narrow:

> if `Q17` is removed from the admissible positive side, does the locked
> nucleus become the exact optimum of the same pairwise-localization
> statistic?

This is a branch-specific follow-up to the [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] `Q17` leak
observation. It is not a fresh discovery scan.

## Frozen zone, target, and condition

- Zone fixed in advance: `Q16..Q25`
- Target nucleus fixed in advance:
  `{Q16, Q21, Q22, Q23, Q25}`
- Conditioning rule fixed in advance:
  `Q17` is forbidden from the positive side

The target subset is reused exactly from [[h-new-126-isolate-core|H-NEW-126]] / [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] /
[[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]].

## Data representation

- Root inventory:
  `data/morphology/surah-root-graph.json`

Each surah is represented as its set of QAC roots, matching [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] /
[[h-new-285-oq18-within-zone-contrast|H-NEW-285]] / [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]].

For each unordered pair `(a,b)` in `Q16..Q25`, define

`J(a,b) = |R_a ∩ R_b| / |R_a ∪ R_b|`.

## Primary statistic

For any admissible 5-positive assignment `S`, let:

- `++(S)` be the 10 unordered pairs with both surahs in `S`
- `other(S)` be the remaining 35 unordered pairs

Define the reused [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] statistic:

`Delta_pair(S) = mean_{(a,b) in ++(S)} J(a,b) - mean_{(a,b) in other(S)} J(a,b)`.

The observed assignment is

`S* = {Q16, Q21, Q22, Q23, Q25}`.

### Direction

One-sided upper-tail.

Higher `Delta_pair(S)` means the candidate positive side isolates the
high-overlap pair mass more strongly.

## Primary exact null

Enumerate all 5-surah subsets of `Q16..Q25` that exclude `Q17`. This
creates an exact conditioned space of

`C(9,5) = 126`

admissible assignments.

For each admissible subset `S`, compute `Delta_pair(S)`.

For the observed nucleus `S*`, define

`p_exact = #{S : Delta_pair(S) >= Delta_pair(S*)} / 126`

and descending rank

`rank_desc = 1 + #{S : Delta_pair(S) > Delta_pair(S*)}`.

The primary cell is counted as a directed pass if:

- `p_exact < 0.05`

Because the `Q17` condition was chosen from the [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] residual
observation rather than from a blind prospective design, the verdict
ceiling remains **PASS-DIRECTED**.

## Descriptive context

These are descriptive only and do not change the verdict:

- the same `Delta_pair` distribution in the complementary stratum where
  `Q17` is required to be positive
- count of full-space assignments above `S*` split by `Q17` included vs
  excluded
- outsider-to-nucleus bridge summaries for `{Q17, Q18, Q19, Q20, Q24}`
  under the same root-Jaccard instrument
- best one-swap replacement of the locked nucleus for each outsider

These quantities help interpret whether `Q17` is merely one strong
outsider or the unique residual leak, but they are not family drivers.

## Why this test matters

This is the sharpest bounded follow-up to the [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] observation.

- [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] already established that the pairwise mechanism is real.
- It also isolated the exact failure mode: every stricter improvement
  over the locked nucleus involved `Q17`.
- [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] asks the direct consequence of that observation:
  once `Q17` is barred, is there any residual rival left?

If this passes, the honest reading is that the name-class nucleus is
stable everywhere in the zone except for a single bridge/leak at `Q17`.

## Garden of forking paths frozen before execution

- zone = exactly `Q16..Q25`
- target subset = exactly `{Q16,Q21,Q22,Q23,Q25}`
- conditioned exclusion = exactly `Q17`
- representation = surah-level root sets, not counts
- pair score = set Jaccard
- primary statistic = unchanged from [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]]
- null = full exact enumeration of the `Q17`-excluded 126-state space
- direction = upper-tail

## Not allowed after results

- swapping the conditioned surah from `Q17` to a different outsider
- adding a second exclusion or inclusion condition
- changing the pair statistic or weighting scheme
- promoting a descriptive outsider ranking to primary
- widening beyond the exact `Q16..Q25` zone

Those would require a new prereg.

## Deliverables

1. `findings/phase-b-hypotheses/h-new-286-2-q17-conditional-bridge-test-prereg.md`
2. `scripts/h_new_286_2_oq18_q17_conditional_bridge_test.py`
3. `findings/phase-b-hypotheses/csv/h-new-286-2.json`
4. `findings/phase-b-hypotheses/h-new-286-2-q17-conditional-bridge-test.md`
5. `journal/h-new-286-2-run-1.md`
