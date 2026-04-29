---
id: H-NEW-276
title: Deep-null resolution of the H-NEW-263 hub question
phase: B
status: NO-HUB-SURVIVES-DEEP-NULL
prereg: findings/phase-b-hypotheses/h-new-276-q27-hub-resolution-prereg.md
script: scripts/h_new_276_q27_hub_resolution.py
json: findings/phase-b-hypotheses/csv/h-new-276.json
journal: journal/h-new-276-run-1.md
date: 2026-04-18
agent: codex
seed: 20260694
n_perm: 10000
accepted_swaps_per_perm: 500
hub_threshold: 2
parent: H-NEW-263
---

# [[h-new-276-q27-hub-resolution|H-NEW-276]] — Deep-null resolution of the [[h-new-263-divine-name-surah-network|H-NEW-263]] hub question

## Headline

The deep-null follow-up strengthens the negative side of [[h-new-263-divine-name-surah-network|H-NEW-263]].

- observed top hub candidate remains **Q27**
- observed `Zmax = 2.043820`
- deep-null family-wise `p_exist = 0.135986`
- inherited threshold `alpha = 0.025` is **not** met
- overall verdict = **NO-HUB-SURVIVES-DEEP-NULL**

So the correct reading of the divine-name surah-overlap network is now
even cleaner:

> the network structure is real, but no single surah survives as a
> family-wise divine-name hub once Cell B is rerun under the deeper
> fixed-margin null.

## What changed relative to [[h-new-263-divine-name-surah-network|H-NEW-263]]

[[h-new-263-divine-name-surah-network|H-NEW-263]] had already landed:

- Cell A structural concentration = **PASS**
- Cell B hub existence = **FAIL** with `p_exist = 0.04319`

[[h-new-276-q27-hub-resolution|H-NEW-276]] keeps the observed construction completely fixed and changes
only one thing:

- permutations increase from `300` to `10000`

Under that deeper null, the negative Cell B conclusion survives and
becomes less borderline:

| Run | `Zmax` | `p_exist` | Verdict |
|---|---:|---:|---|
| [[h-new-263-divine-name-surah-network|H-NEW-263]] | `2.1972` | `0.04319` | fail at `0.025` |
| [[h-new-276-q27-hub-resolution|H-NEW-276]] | `2.0438` | `0.13599` | fail at `0.025` |

The hub story did not get stronger when the null got deeper. It got
weaker.

## Q27 candidate focus

Q27 still leads the ranked table, but only as a nominal candidate.

| Field | Value |
|---|---:|
| Surah | `Q27` |
| observed `strength_ge2` | `232` |
| null mean | `178.0261` |
| null SD | `26.4083` |
| z | `2.043820` |
| raw upper-tail `p_raw` | `0.00449955` |
| family-wise `p_adj_fwer` | `0.135986` |
| rank | `1` |

This is the important distinction:

- **raw candidate signal exists**
- **family-wise hub existence still fails**

So Q27 is the leading descriptive candidate, not a certified hub.

## Top-ranked surahs under the deep null

Top 5 by hub z-score:

| Rank | Surah | `strength_ge2` | z | `p_adj_fwer` |
|---:|---:|---:|---:|---:|
| 1 | 27 | 232 | `2.0438` | `0.1360` |
| 2 | 45 | 147 | `1.8434` | `0.5119` |
| 3 | 41 | 194 | `1.5930` | `0.8895` |
| 4 | 29 | 205 | `1.4975` | `0.9593` |
| 5 | 30 | 204 | `1.4669` | `0.9714` |

No candidate is remotely close to the inherited Bonferroni threshold
after family-wise adjustment.

## Interpretation

[[h-new-276-q27-hub-resolution|H-NEW-276]] resolves the lingering ambiguity in the [[h-new-263-divine-name-surah-network|H-NEW-263]] Cell B
story.

### What now looks settled

1. **Cell A was the real signal.**
   The divine-name repertoire network is structurally non-random at the
   global level.
2. **Cell B was never a near-miss hub discovery in a stable sense.**
   The deeper null moves the result farther away from significance.
3. **Q27 remains the best descriptive lead, not the evidential center
   of gravity.**
   It tops the z-score list, but the family-wise case does not hold.

### What this means for the parent claim

The [[h-new-263-divine-name-surah-network|H-NEW-263]] wording should now be read with more confidence:

- **PASS-STRUCTURE-NO-HUB** is the correct conclusion
- not "almost hub"
- not "Q27 probably hub with more permutations"

The deeper null cuts off that escalation path.

## Honest limits

1. This follow-up re-tests only the inherited Cell B hub question.
2. It does not reopen Cell A, the `W >= 2` threshold, or the projection
   construction.
3. A different hub statistic could still be proposed in a new pre-reg,
   but this exact [[h-new-263-divine-name-surah-network|H-NEW-263]] hub cell is now well-resolved in the
   negative direction.

## Bottom line

The divine-name surah-overlap network is real as a **distributed
structure**, not as a **single-hub** architecture.

Deepening the null to `10000` permutations leaves Q27 in first place
descriptively but pushes the family-wise hub claim farther from the
decision boundary.
