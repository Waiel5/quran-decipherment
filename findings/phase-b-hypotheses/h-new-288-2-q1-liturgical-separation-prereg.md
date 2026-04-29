---
id: H-NEW-288-2
title: Q1 liturgical-separation test inside the residualized Q108 pool
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-19
agent: codex
parent_1: H-NEW-273
parent_2: H-NEW-288
parent_3: H-NEW-288-1
open_question: OQ-19 integration of the narrow Q1↔Q108 liturgical foothold with the residualized-family medoid mechanism
bonferroni_family: h-new-288-2-q1-liturgical-separation
bonferroni_k: 1
alpha: 0.05
alpha_bon: 0.05
rules_tuple: "(fixed H-NEW-288.1 pool P = {Early Meccan surahs with verse_count <= 17}; candidate family = P \\ {Q108}; literal and residualized probability families reused exactly from H-NEW-288.1; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; H-NEW-273 surah score reused exactly as S(s)=sqrt(divine_share_{Alh,rbb,rHm}(s) * imperative_density(s)); for each candidate s and primary metric m, compute rank_lit^m(s) and rank_res^m(s) by ascending distance to Q108 inside P \\ {Q108}; define C_sep(s)=#{m : rank_res^m(s) > rank_lit^m(s)} and L_sep(s)=S(s) * C_sep(s); exact candidate-family upper-tail over the 21 admissible surahs)"
direction_primary: "determine whether Q1 is the strongest high-H-NEW-273-score surah that is consistently pushed away from Q108 when the family shifts from literal normalization to residualized smoothing"
---

# [[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]] - Q1 liturgical-separation test inside the residualized Q108 pool

## Question

`[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` and `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` now both stand:

- `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` gives one real but narrow Q1↔Q108 speech-act foothold
- `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` shows that the broader residualized OQ-19 mechanism is a
  fixed-pool medoid effect centered on `Q108`

The live OQ-19 question is therefore no longer whether either component exists.
It is how they fit together.

This finding asks the narrowest integration question that stays inside the
already-landed machinery:

> Inside the exact `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` short Early-Meccan pool, is `Q1` the strongest
> high-`[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]`-score surah that residualized smoothing consistently pushes
> *away* from `Q108`, rather than drawing *toward* the residualized medoid
> cloud?

If yes, then the narrow Q1↔Q108 liturgical foothold is not simply the same
mechanism as the residualized medoid cloud. It marks a bounded, opener-specific
separation.

## Locked ingredients

### Fixed pool

Reuse `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` exactly:

`P = {surahs with noldeke_phase = Early Meccan and verse_count <= 17}`

So the admissible candidate family is:

`P \\ {Q108}`

with 21 surahs.

### Fixed OQ-19 geometry

Reuse `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` exactly:

- literal family = `count / N_i` plus flat `alpha = 0.5`
- residualized family = raw counts plus
  `alpha_i = 0.5 * mean_tokens / N_i`
- primary metrics only:
  `Fisher-Rao`, `Jensen-Shannon`, `Euclidean L2`, `cosine-angle`

No new normalization family, no new feature space, and no new metric family are
permitted.

### Fixed liturgical score

Reuse the `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` per-surah speech-act score exactly:

`S(s) = sqrt(D(s) * I(s))`

where:

- `D(s)` = share of QAC STEM-root tokens in `{Alh, rbb, rHm}`
- `I(s)` = imperative density per verse

No new divine lexicon, no new imperative weighting, and no new speech-act
composite are permitted.

## Per-surah family-shift statistic

For each candidate surah `s in P \\ {Q108}` and each primary metric `m`:

1. Compute the ascending distance rank of `s` to `Q108` under the literal
   family:

   `rank_lit^m(s)`

2. Compute the ascending distance rank of `s` to `Q108` under the residualized
   family:

   `rank_res^m(s)`

3. Record whether residualized smoothing pushes `s` farther from `Q108`:

   `1[rank_res^m(s) > rank_lit^m(s)]`

Define the consistent-separation count:

`C_sep(s) = #{m : rank_res^m(s) > rank_lit^m(s)}`

So `C_sep(s)` ranges from `0` to `4`.

Interpretation:

- `C_sep(s) = 4` means the surah moves farther from `Q108` on every primary
  metric under residualized smoothing
- `C_sep(s) = 0` means it never moves farther and may instead be pulled closer

## Primary statistic

Define the liturgical-separation score:

`L_sep(s) = S(s) * C_sep(s)`

The target is fixed:

`s* = Q1`

Observed primary statistic:

`L_sep(Q1)`

## Exact null

This is an exact bounded candidate-family test, not a permutation.

Evaluate `L_sep(s)` for every surah in:

`P \\ {Q108}`

Primary upper-tail:

`p_exact = #{s : L_sep(s) >= L_sep(Q1)} / 21`

Also report:

- descending rank
- top candidate table by `L_sep`
- the per-metric literal and residualized ranks for `Q1`

## Secondary descriptive contrast

Because `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` named `Q112` as the strongest non-target pair competitor
with `Q1`, report descriptively:

- `C_app(s) = #{m : rank_res^m(s) < rank_lit^m(s)}`
- `L_app(s) = S(s) * C_app(s)`

This is descriptive only. It is not a second inferential cell.

## Decision rule

The ceiling is directional because both the pool and the speech-act score are
inherited from already-landed OQ-19 work:

- `PASS-DIRECTED` iff `p_exact < 0.05`
- `NULL` otherwise

## Why this test

This is the cleanest next OQ-19 integration probe because:

1. it reuses only landed ingredients from `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` and `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`
2. it asks a genuinely new question without reopening family adjudication
3. it distinguishes "same mechanism" from "bounded opener-specific separation"
   directly
4. the admissible candidate family is exact and small enough to interpret
   cleanly

## Honest limits

1. This is a directed integration test, not a discovery-clean new family.
2. The exact candidate family has only 21 members, so the minimum attainable
   upper-tail is `1 / 21 = 0.047619`.
3. The statistic is specifically about *distance-rank movement* relative to
   `Q108`, not about whole-graph MST structure.
4. A pass would show bounded liturgical separation, not a full causal account
   of Q108's hub status.

## Deliverables

- Script: `scripts/h_new_288_2_q1_liturgical_separation.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-288-2.json`
- Findings: `findings/phase-b-hypotheses/h-new-288-2-q1-liturgical-separation.md`
- Journal: `journal/h-new-288-2-run-1.md`
