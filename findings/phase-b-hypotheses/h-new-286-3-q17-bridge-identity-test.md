---
id: H-NEW-286.3
title: OQ-18 Q17 bridge identity test
phase: B
status: DESCRIPTIVE-ONLY
date: 2026-04-19
agent: codex
parent_1: H-NEW-286.2
open_question: OQ-18
seed: 20260419
prereg: findings/phase-b-hypotheses/h-new-286-3-q17-bridge-identity-test-prereg.md
script: scripts/h_new_286_3_oq18_bridge_identity_test.py
json: findings/phase-b-hypotheses/csv/h-new-286-3.json
journal: journal/h-new-286-3-run-1.md
rules_tuple: "(QAC v0.4 root sets via surah-root-graph.json; fixed zone = Q16..Q25; fixed core = {Q16,Q21,Q22,Q23,Q25}; outsider family = {Q17,Q18,Q19,Q20,Q24}; candidate bridge score Delta_bridge(b)=mean_jaccard(core-core ∪ bridge-core)-mean_jaccard(all other zone pairs); exact outsider-family rank/upper fraction over the 5 admissible bridges; one-sided upper-tail reported descriptively because the minimum attainable exact upper fraction is 1/5 = 0.20)"
---

# [[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]] — OQ-18 Q17 bridge identity test

## Headline

[[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] already showed that `Q17` is the only outsider whose
inclusion can improve the locked OQ-18 nucleus
`{Q16,Q21,Q22,Q23,Q25}` under the parent pairwise-localization
statistic.

[[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]] asks the sharper identity question:

> if the nucleus is held fixed and only the outsider bridge is allowed
> to vary across `{Q17,Q18,Q19,Q20,Q24}`, is `Q17` the unique best
> bridge candidate?

Under the fixed core-plus-bridge mask, the answer is **yes
descriptively**:

- `Q17` is the **unique rank-1 outsider bridge**
- exact outsider-family rank = **`1 / 5`**
- exact upper fraction = **`1 / 5 = 0.20`**

But that same bounded family size means the result is **not
inferentially pass-capable**. The minimum attainable exact upper
fraction in a 5-candidate family is already `0.20`, so no outsider can
reach `p < 0.05`.

The honest verdict is therefore:

- **descriptive conclusion**: `Q17` is the unique best outsider bridge
- **inferential verdict**: **NULL**

## Fixed model

Core fixed from [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] / [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]]:

- `{Q16,Q21,Q22,Q23,Q25}`

Outsider family fixed from the zone complement:

- `{Q17,Q18,Q19,Q20,Q24}`

For each candidate bridge `b`, the predicted-high edge set is:

- all 10 core-core pairs
- all 5 bridge-core pairs `(b,c)`

Primary score:

`Delta_bridge(b) = mean_jaccard(predicted_high) - mean_jaccard(all other zone pairs)`

So this is a fixed-nucleus, fixed-zone, bridge-identity comparison on
the same QAC-root / Jaccard machinery used in [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] / 285 / 286.1 /
286.2.

## Exact result

Observed candidate of interest: `Q17`

- mean Jaccard across predicted-high edges = `0.3415968263411155`
- mean Jaccard across all other zone pairs = `0.3076007721081613`
- observed `Delta_bridge(Q17) = 0.03399605423295421`

Exact outsider-family comparison:

- admissible candidates = `5`
- descending rank of `Q17` = `1 / 5`
- candidates `>=` observed = `1`
- exact upper fraction = `1 / 5 = 0.2`
- family mean = `0.020715104447297218`
- family median = `0.021176192972585384`
- family min = `0.007457427166184971`
- family max = `0.03399605423295421`

Because `1 / 5 = 0.20` is already the minimum possible upper fraction,
this design cannot yield an inferential pass at `alpha = 0.05`. That
limit was frozen in the prereg before execution.

## Candidate ranking

| Bridge candidate | `Delta_bridge(b)` | mean bridge-to-core Jaccard |
|---|---:|---:|
| `Q17` | `0.03399605423295421` | `0.3420193401695428` |
| `Q20` | `0.02382721893190054` | `0.32168166956743544` |
| `Q18` | `0.021176192972585384` | `0.3163796176488051` |
| `Q24` | `0.01711862893286098` | `0.30826448956935626` |
| `Q19` | `0.007457427166184971` | `0.2889420860360043` |

The margin from the top candidate to the runner-up is:

- `Q17 - Q20 = 0.01016883530105367`

So `Q17` is not merely tied for first. It is the unique top bridge
candidate under the locked mask.

## Descriptive robustness

The same outsider ordering appears on the bounded secondary summaries.

### 1. Mean bridge-to-core Jaccard

The bridge-to-core means are already rank-ordered

`Q17 > Q20 > Q18 > Q24 > Q19`

with the same top candidate `Q17`.

### 2. [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] one-swap continuity

Best single-swap replacement of the core under the parent
`Delta_pair` statistic:

- `Q17` replacing `Q21` gives `{Q16,Q17,Q22,Q23,Q25}` with
  `Delta_pair = 0.0346190439274357`, a gain of
  `+0.005751184903178219` over the [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] core reference
- `Q20`, `Q18`, `Q24`, and `Q19` all remain below the core reference

So the fixed core-plus-bridge mask and the earlier single-swap
diagnostic point to the same identity claim:

- only `Q17` improves the bounded nucleus
- `Q17` is the strongest outsider-to-core bridge

## Interpretation

This is the cleanest bounded statement available now for the Q17 branch:

- [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] showed the residual leak is concentrated at `Q17`
- [[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]] shows that, once the nucleus is fixed, `Q17` is the
  unique best outsider bridge inside the exact outsider family

What [[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]] does **not** do is produce a new inferential pass.
The family is too small for that. A 5-candidate exact comparison can
only ever return upper fractions `{1.0, 0.8, 0.6, 0.4, 0.2}`. So even
the strongest possible outcome remains descriptive.

That is why the correct read is:

- **identity claim**: `Q17` is the unique best outsider bridge
- **significance claim**: unavailable under this bounded exact design

## Bottom line

`Q17` is the unique rank-1 outsider bridge around the locked OQ-18
nucleus `{Q16,Q21,Q22,Q23,Q25}` under the fixed core-plus-bridge
Jaccard model.

Exact result:

- rank `1 / 5`
- exact upper fraction `0.20`

Verdict:

- **DESCRIPTIVE-ONLY**
- inferentially **NULL**

So [[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]] sharpens the narrative from [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] without
over-claiming: the bounded outsider family supports **unique-best
identity**, not a new inferential pass.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-286-3-q17-bridge-identity-test-prereg.md`
- Script: `scripts/h_new_286_3_oq18_bridge_identity_test.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-286-3.json`
- Journal: `journal/h-new-286-3-run-1.md`
