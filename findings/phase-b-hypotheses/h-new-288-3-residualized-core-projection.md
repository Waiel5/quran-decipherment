---
id: H-NEW-288-3
title: Residualized short-core projection test for the H-NEW-273 speech-act score
phase: B
status: NULL — the H-NEW-273 speech-act axis trends away from the residualized short-core, but not strongly enough to certify either a same-mechanism or complementary-projection reading
date: 2026-04-19
specialist: codex
parents:
  - h-new-273
  - h-new-288-1
  - h-new-288-2
pre_reg: findings/phase-b-hypotheses/h-new-288-3-residualized-core-projection-prereg.md
pre_reg_sha256: 33da1364997438ae5ec04d6c6ce621c66cefd4a329a65996b78b03d70bad6228
script: scripts/h_new_288_3_residualized_core_projection.py
output_json: findings/phase-b-hypotheses/csv/h-new-288-3.json
verdict: NULL — observed T_proj = -0.485885 with p_same = 0.8902 and p_comp = 0.1157 under the exact 336-assignment score-permutation null. The speech-act axis points directionally away from the residualized short-core, but the projection is not exact-significant.
---

# [[h-new-288-3-residualized-core-projection|H-NEW-288.3]] - Residualized short-core projection test for the [[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]] speech-act score

## Headline

This is the direct follow-up to `[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]`.

After `[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]`, the right OQ-19 question was no longer whether `Q1` is a
special case inside the residualized pool. That was already positive. The next
question was whether the **whole** `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` speech-act axis points into the
residualized `Q108` short-core, away from it, or neither cleanly enough to
certify.

The answer is:

- **directionally away**
- but **not exact-significant**

Observed primary summary:

- `T_proj = -0.485885`
- `p_same = 0.890208`
- `p_comp = 0.115727`
- verdict:
  **`NULL`**

So the new OQ-19 opener/refuge split from `[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]` does **not** scale
cleanly into a certified projection of the full `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` speech-act axis
onto the residualized short-core.

## Locked setup

### Speech-act side

Exact `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` 5-7 verse Early-Meccan side:

`B = {Q1, Q97, Q105, Q107, Q109, Q111, Q113, Q114}`

Exact `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` score:

`S(s) = sqrt(divine_share_{Alh,rbb,rHm}(s) * imperative_density(s))`

Observed scores:

| Surah | `S(s)` |
|---|---:|
| Q1 | **0.208546** |
| Q114 | 0.144352 |
| Q113 | 0.115470 |
| Q97 | 0.000000 |
| Q105 | 0.000000 |
| Q107 | 0.000000 |
| Q109 | 0.000000 |
| Q111 | 0.000000 |

### Residualized short-core side

Fixed from `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`:

`K = {Q108, Q106, Q103, Q112}`

### Metric family

Exact `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` primary metrics:

- `Fisher-Rao`
- `Jensen-Shannon`
- `Euclidean L2`
- `cosine-angle`

## Observed result

For each metric, define residualized core closeness:

`C_m(s) = - mean_{t in K} d_res,m(s, t)`

and then compute:

`r_m = Corr(S, C_m)`

Observed per-metric correlations:

| Metric | `r_m` |
|---|---:|
| Fisher-Rao | `-0.483185` |
| Jensen-Shannon | `-0.483064` |
| Euclidean L2 | `-0.488655` |
| Cosine-angle | `-0.488634` |

Primary summary:

`T_proj = mean(r_m) = -0.485885`

So the directional tendency is consistent:

- higher `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` score corresponds to being **farther** from the
  residualized short-core, not closer

## Exact null

Hold the residualized closeness tables fixed.

Permute the observed `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` score multiset across `B`.

Because five entries are zero, the exact null contains:

- `8! / 5! = 336` unique assignments

Null summary:

- exact null mean:
  `~ 0`
- null min:
  `-0.922873`
- null max:
  `0.741133`

Directional exact tails:

- `p_same = 0.890208`
- `p_comp = 0.115727`

Exact ranks:

- descending rank:
  `299 / 336`
- ascending rank:
  `38 / 336`

So the negative direction is real descriptively, but it does **not** clear the
exact complementary-projection threshold.

## Interpretation

This result matters because it blocks two overclaims at once.

It does **not** support:

1. a strong same-mechanism reading in which the `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` speech-act axis
   simply points into the residualized short-core
2. a strong complementary-projection reading in which that speech-act axis
   cleanly points away from the short-core as a whole

The honest OQ-19 update is narrower:

- `[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]` gave a **real local split**:
  `Q1` is the strongest high-liturgical ejected surah, while
  `Q112/113/114` move toward `Q108`
- `[[h-new-288-3-residualized-core-projection|H-NEW-288.3]]` shows that this local split does **not** upgrade into a clean
  global projection of the whole `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` speech-act axis across the exact
  5-7 verse side

So the two branches are in contact, but not in a way that is well-described by
one ordered score-to-core projection.

## Scope

- no new normalization family
- no new metric family
- no MST rerun
- no new speech-act score

This is a direct post-`[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]` axis-level discriminator and should be read
as such.

## Honest limits

1. The exact test has only eight surahs and 336 unique assignments, so power is
   limited.
2. The short-core `K` is inherited from `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`; this is not a new core
   discovery.
3. Because the result is null, it sharpens the frontier but does not provide a
   new explanatory mechanism by itself.

## Bottom line

`[[h-new-288-3-residualized-core-projection|H-NEW-288.3]]` closes the strongest immediate overreach after `[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]`:

**the [[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]] speech-act axis trends away from the residualized `Q108`
short-core, but not strongly enough to certify a full complementary-projection
story.**

So OQ-19 now contains:

- a narrow exact Q1↔Q108 foothold
- a fixed-pool residualized medoid mechanism
- a real local opener/refuge split
- but **no** clean global projection of the speech-act axis onto that short-core
