---
id: H-NEW-286.3
title: "OQ-18 Q17 bridge identity test"
status: PRE-REGISTERED 2026-04-19
spec_locked_at: 2026-04-19
author: codex
seed: 20260419
exact_space_n: 5
bonferroni_family: h-new-286-3-q17-bridge-identity-test
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: "DESCRIPTIVE-ONLY (the exact outsider family has 5 candidates, so the minimum attainable one-sided upper fraction is 1/5 = 0.20)"
rules_tuple: "(QAC v0.4 root sets via data/morphology/surah-root-graph.json; binary concept/object-vs-other label reused from findings/phase-b-hypotheses/csv/h-new-126.json Cell B and H-NEW-286; fixed zone = Q16..Q25; fixed core = {Q16,Q21,Q22,Q23,Q25}; outsider family = {Q17,Q18,Q19,Q20,Q24}; candidate bridge score Delta_bridge(b)=mean_jaccard(core-core ∪ bridge-core)-mean_jaccard(all other zone pairs); exact outsider-family rank/upper fraction over the 5 admissible bridges; one-sided upper-tail reported descriptively because min attainable exact upper fraction = 0.20)"
prior_work_consulted:
  - findings/phase-b-hypotheses/h-new-281-true-isolate-core-within-zone-jaccard.md
  - findings/phase-b-hypotheses/h-new-285-oq18-within-zone-contrast.md
  - findings/phase-b-hypotheses/h-new-286-oq18-within-zone-name-class-contrast.md
  - findings/phase-b-hypotheses/h-new-286-1-oq18-pairwise-name-class-localization.md
  - findings/phase-b-hypotheses/h-new-286-2-q17-conditional-bridge-test.md
  - findings/phase-b-hypotheses/csv/h-new-126.json
  - findings/phase-b-hypotheses/csv/h-new-286-2.json
  - scripts/h_new_286_1_oq18_pairwise_name_class_localization.py
  - scripts/h_new_286_2_oq18_q17_conditional_bridge_test.py
---

# [[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]] — OQ-18 Q17 bridge identity test

## Question

[[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] showed that once `Q17` is excluded from the positive side,
the locked nucleus `{Q16,Q21,Q22,Q23,Q25}` becomes the unique optimum of
the [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] pairwise-localization statistic. That establishes
`Q17` as the sole outsider whose inclusion can still improve the parent
5-surah assignment.

The next bounded question is even narrower:

> around the fixed nucleus `{Q16,Q21,Q22,Q23,Q25}`, is `Q17` the unique
> best outsider bridge among the outsider family `{Q17,Q18,Q19,Q20,Q24}`
> under a fixed core-plus-bridge edge model?

This is not a fresh full-space search. The core and outsider family are
already fixed by [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] / [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]].

## Frozen objects

- zone fixed in advance: `Q16..Q25`
- core fixed in advance:
  `{Q16,Q21,Q22,Q23,Q25}`
- outsider family fixed in advance:
  `{Q17,Q18,Q19,Q20,Q24}`
- observed candidate of interest fixed in advance:
  `Q17`

The core is reused exactly from [[h-new-126-isolate-core|H-NEW-126]] / [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] / [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]].
The outsider family is the exact complement of that core inside the
fixed `Q16..Q25` zone.

## Data representation

- root inventory:
  `data/morphology/surah-root-graph.json`

Each surah is represented as its set of QAC roots, matching
[[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] / [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] / [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] / [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]].

For each unordered pair `(a,b)` in `Q16..Q25`, define

`J(a,b) = |R_a ∩ R_b| / |R_a ∪ R_b|`.

## Primary statistic

For a candidate outsider bridge `b` in `{Q17,Q18,Q19,Q20,Q24}`, define
the fixed predicted-high edge set as:

- all core-core pairs inside `{Q16,Q21,Q22,Q23,Q25}`; and
- all bridge-core pairs `(b,c)` with `c` in the core

Call this set `H_b`.

The remaining zone pairs are `L_b`.

Define the candidate score

`Delta_bridge(b) = mean_{e in H_b} J(e) - mean_{e in L_b} J(e)`.

Interpretation:

- higher `Delta_bridge(b)` means candidate `b` better realizes the
  hypothesized "stable nucleus plus one outsider bridge" mask
- the core-core contribution is held fixed across candidates
- only bridge identity is allowed to vary

## Exact outsider-family comparison

The exact admissible space is the outsider family itself:

`B = {Q17,Q18,Q19,Q20,Q24}`

So the exact comparison space has size

`|B| = 5`.

For the observed candidate `Q17`, report:

- descending rank among the 5 candidates
- count of candidates with `Delta_bridge(b) >= Delta_bridge(Q17)`
- one-sided exact upper fraction

`p_exact_family = #{b in B : Delta_bridge(b) >= Delta_bridge(Q17)} / 5`.

## Inferential limit frozen before execution

Because the family contains only 5 candidates, the minimum attainable
one-sided exact upper fraction is

`1 / 5 = 0.20`.

Therefore:

- this design can support an **exact descriptive rank statement**
- it **cannot** support an inferential pass at `alpha = 0.05`

That is not a failure of execution. It is a property of the bounded
candidate family itself, and it is frozen here before any results are
viewed.

So the pre-committed honesty rule is:

- if `Q17` is rank `1 / 5`, report it as **descriptively unique-best**
- the inferential verdict remains **NULL**
- no language stronger than descriptive unique-best is allowed

## Descriptive context

These are descriptive only and do not change the verdict:

- mean bridge-to-core Jaccard for each outsider candidate
- bridge-core edge table for each outsider candidate
- best one-swap [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] replacement of the core for each outsider,
  recomputed on the same root-Jaccard machinery

These are included only to show whether multiple bounded summaries agree
on the same outsider identity.

## Why this test matters

[[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] answered a conditional full-subset question:

> once `Q17` is barred, does any rival to the core remain?

[[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]] asks the complementary identity question:

> when the core is held fixed and only the outsider bridge is allowed to
> vary, does `Q17` outrank the outsider family?

This is the narrowest direct test of the phrase "Q17 is the unique best
outsider bridge around the locked nucleus."

## Garden of forking paths frozen before execution

- zone = exactly `Q16..Q25`
- core = exactly `{Q16,Q21,Q22,Q23,Q25}`
- outsider family = exactly `{Q17,Q18,Q19,Q20,Q24}`
- representation = surah-level root sets, not counts
- pair score = set Jaccard
- predicted-high mask = core-core pairs union bridge-core pairs
- candidate score = `Delta_bridge(b)` exactly as defined above
- exact comparison space = the 5 outsider candidates only
- direction = upper-tail
- no enlargement of the candidate family
- no switch to a different bridge statistic after viewing outputs

## Not allowed after results

- adding more outsider candidates from outside `Q16..Q25`
- changing the core membership
- changing the predicted-high mask
- promoting a secondary descriptive summary to the primary score
- pretending `p = 0.20` can support an inferential pass

Those would require a new prereg.

## Deliverables

1. `findings/phase-b-hypotheses/h-new-286-3-q17-bridge-identity-test-prereg.md`
2. `scripts/h_new_286_3_oq18_bridge_identity_test.py`
3. `findings/phase-b-hypotheses/csv/h-new-286-3.json`
4. `findings/phase-b-hypotheses/h-new-286-3-q17-bridge-identity-test.md`
5. `journal/h-new-286-3-run-1.md`
