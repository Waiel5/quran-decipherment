---
id: H-NEW-288-4
title: Within-bin token-count projection into the residualized Q108 short-core
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-19
agent: codex
parent_1: H-NEW-288-1
parent_2: H-NEW-288-2
parent_3: H-NEW-288-3
open_question: OQ-19 local factor behind the opener-versus-refuge split inside the residualized Q108 neighborhood
bonferroni_family: h-new-288-4-token-count-core-projection
bonferroni_k: 1
alpha: 0.05
alpha_bon: 0.05
rules_tuple: "(fixed H-NEW-273 5-7 verse side B = {Q1,Q97,Q105,Q107,Q109,Q111,Q113,Q114}; fixed H-NEW-288.1 residualized short-core K = {Q108,Q106,Q103,Q112}; residualized probability family reused exactly from H-NEW-288.1; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; token count N_tok(s) = total QAC STEM-root tokens from the same parse used by H-NEW-288.1; per metric core-closeness C_m(s) = -mean_{t in K} d_res,m(s,t); primary summary T_tok = mean_m Corr(N_tok, C_m) over B; exact null by permuting the observed token-count vector across B, yielding 8! = 40320 unique assignments; one-sided lower-tail for shorter-closer direction)"
direction_primary: "determine whether residualized short-core approach inside the fixed H-NEW-273 side is mechanically ordered by local stem-token count even after the broader normalization-family question has already been answered"
---

# [[h-new-288-4-token-count-core-projection|H-NEW-288.4]] - Within-bin token-count projection into the residualized Q108 short-core

## Question

`[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]` showed a real local opener-versus-refuge split.

`[[h-new-288-3-residualized-core-projection|H-NEW-288.3]]` then showed that this split does not become a clean whole-axis
projection of the `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` speech-act score.

The next honest OQ-19 question is therefore narrower:

> inside that fixed 5-7 verse side, is there any concrete local ordering factor
> that predicts approach to the residualized `Q108` short-core?

This finding tests the smallest mechanical candidate:

- total QAC STEM-root token count inside the already-fixed 5-7 verse side

## Fixed sets and family

Reuse exactly:

- `B = {Q1,Q97,Q105,Q107,Q109,Q111,Q113,Q114}`
- `K = {Q108,Q106,Q103,Q112}`
- residualized family from `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`
- primary metrics
  `{Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle}`

No new normalization family and no new candidate-set search are permitted.

## Token-count vector

For each `s in B`, define:

`N_tok(s) = total number of QAC STEM-root tokens`

using the same morphology parse already reused by `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`.

Observed vector on `B`:

`{23, 21, 18, 14, 12, 17, 15, 16}`

All eight values are distinct.

## Core-closeness statistic

For each metric `m`, define:

`C_m(s) = -mean_{t in K} d_res,m(s, t)`

Higher `C_m(s)` means closer to the residualized short-core.

## Primary summary

For each metric `m`, compute:

`r_m = Corr(N_tok, C_m)`

Primary summary:

`T_tok = mean_m r_m`

Interpretation:

- negative `T_tok` means shorter token count points toward the residualized
  short-core

## Exact null

Hold the four residualized closeness tables fixed.

Permute the observed token-count vector across the eight surahs in `B`.

Because all eight token counts are distinct, the null contains exactly:

`8! = 40320`

assignments.

Primary one-sided lower-tail:

`p_short = (1 + #{pi : T_tok(pi) <= T_obs}) / (1 + 40320)`

Also report:

- per-metric correlations
- null mean, minimum, maximum
- descending and ascending ranks

## Descriptive contrast

Run the same pipeline descriptively on `verse_count` inside `B`.

This is descriptive only. It is not a second inferential cell.

## Decision rule

- `PASS-DIRECTED` iff `p_short < 0.05`
- `NULL` otherwise

## Why this test

This is the smallest honest post-`[[h-new-288-3-residualized-core-projection|H-NEW-288.3]]` move because:

1. it does not reopen the global length-normalization family conflict
2. it stays entirely inside the fixed residualized family and fixed 5-7 verse
   side
3. it asks whether there is a local residual-length ordering even after the
   broader speech-act projection failed

## Honest limits

1. This is a local mechanical factor test, not a full semantic explanation.
2. A pass would show only that token count partly orders the residualized
   neighborhood inside `B`, not that Q108's global anomaly is "just length."
3. The verse-count contrast is descriptive only.

## Deliverables

- Script: `scripts/h_new_288_4_token_count_core_projection.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-288-4.json`
- Findings: `findings/phase-b-hypotheses/h-new-288-4-token-count-core-projection.md`
- Journal: `journal/h-new-288-4-run-1.md`
