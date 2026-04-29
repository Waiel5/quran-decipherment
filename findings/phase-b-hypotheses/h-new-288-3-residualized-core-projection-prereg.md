---
id: H-NEW-288-3
title: Residualized short-core projection test for the H-NEW-273 speech-act score
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-19
agent: codex
parent_1: H-NEW-273
parent_2: H-NEW-288-1
parent_3: H-NEW-288-2
open_question: OQ-19 projection of the H-NEW-273 speech-act axis onto the residualized Q108 short-core after the opener/refuge split
bonferroni_family: h-new-288-3-residualized-core-projection
bonferroni_k: 1
alpha: 0.05
alpha_bon: 0.05
rules_tuple: "(fixed H-NEW-273 5-7 verse Early-Meccan side B = {Q1,Q97,Q105,Q107,Q109,Q111,Q113,Q114}; fixed H-NEW-288.1 residualized short-core K = {Q108,Q106,Q103,Q112}; residualized probability family reused exactly from H-NEW-288.1; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; H-NEW-273 surah score reused exactly as S(s)=sqrt(divine_share_{Alh,rbb,rHm}(s) * imperative_density(s)); per metric core-closeness C_m(s) = -mean_{t in K} d_res,m(s,t); primary summary T_proj = mean_m Corr(S, C_m) over B; exact null by permuting the observed H-NEW-273 score multiset across B, yielding 8!/5! = 336 unique assignments; dual directional exact p_same and p_comp)"
direction_primary: "determine whether the H-NEW-273 speech-act score projects toward the residualized short-core, away from it, or neither cleanly enough to certify"
---

# [[h-new-288-3-residualized-core-projection|H-NEW-288.3]] - Residualized short-core projection test for the [[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]] speech-act score

## Question

`[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]` showed that `Q1` is the strongest high-liturgical short surah
consistently pushed away from `Q108` once the family shifts from literal
normalization to residualized smoothing.

That still leaves one narrower OQ-19 question:

> does the exact `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` speech-act axis project as a whole toward the
> residualized `Q108` short-core, away from it, or not cleanly enough either
> way?

This finding does not reopen generic family adjudication or generic linkage.
It tests the exact post-`[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]` frontier.

## Fixed objects

### Speech-act side

Reuse the exact `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` 5-7 verse Early-Meccan side:

`B = {Q1, Q97, Q105, Q107, Q109, Q111, Q113, Q114}`

Reuse the exact `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` surah score:

`S(s) = sqrt(divine_share_{Alh,rbb,rHm}(s) * imperative_density(s))`

Observed score multiset on `B`:

`{0.2085456889, 0.1443520003, 0.1154700538, 0, 0, 0, 0, 0}`

### Residualized short-core side

Reuse the fixed residualized short-core from `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`:

`K = {Q108, Q106, Q103, Q112}`

This keeps the test inside the already-landed residualized family.

### Metric family

Reuse the exact `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` primary metrics:

- `Fisher-Rao`
- `Jensen-Shannon`
- `Euclidean L2`
- `cosine-angle`

No new metric family, no MST, and no new normalization family are permitted.

## Core-closeness statistic

For each surah `s in B` and each primary metric `m`, define residualized
short-core closeness:

`C_m(s) = - mean_{t in K} d_res,m(s, t)`

Higher `C_m(s)` means `s` is closer to the residualized `Q108` short-core.

## Primary summary

For each metric `m`, compute:

`r_m = Corr_{s in B}(S(s), C_m(s))`

Primary summary statistic:

`T_proj = mean_m r_m`

Interpretation:

- positive `T_proj` means the speech-act score points into the residualized
  short-core
- negative `T_proj` means the speech-act score points away from that core

## Exact null

Hold the four residualized closeness tables fixed.

Permute the observed `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` score multiset across the eight surahs in `B`.
Because five scores are zero, this yields exactly:

`8! / 5! = 336`

unique assignments.

For each assignment `pi`, recompute:

`T_proj(pi)`

Report both directional exact tails:

- `p_same = (1 + #{pi : T_proj(pi) >= T_obs}) / 337`
- `p_comp = (1 + #{pi : T_proj(pi) <= T_obs}) / 337`

Also report:

- per-metric `r_m`
- exact null mean, minimum, maximum
- descending and ascending ranks

## Decision rule

This is a directional discriminator, not a one-direction-only test.

Verdict table:

- `PASS-SAME-MECHANISM` iff `p_same < 0.05`
- `PASS-COMPLEMENTARY` iff `p_comp < 0.05`
- `NULL` otherwise

## Why this test

This is the cleanest immediate follow-up after `[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]` because:

1. it uses only landed OQ-19 ingredients
2. it respects the new opener/refuge split instead of ignoring it
3. it tests the axis-level projection question directly rather than by another
   local rank anecdote
4. the null is exact and finite

## Honest limits

1. This is an exact test on only eight surahs, so power is limited.
2. The core `K` is inherited from `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`; this is not a new core search.
3. A null result still matters because it directly blocks both strong
   same-mechanism and strong complementary-projection overclaims.

## Deliverables

- Script: `scripts/h_new_288_3_residualized_core_projection.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-288-3.json`
- Findings: `findings/phase-b-hypotheses/h-new-288-3-residualized-core-projection.md`
- Journal: `journal/h-new-288-3-run-1.md`
