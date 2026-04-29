---
id: H-NEW-288-4
title: Within-bin token-count projection into the residualized Q108 short-core
phase: B
status: PASS-DIRECTED — inside the fixed H-NEW-273 5-7 verse side, shorter STEM-token count points toward the residualized Q108 short-core under an exact 8! null
date: 2026-04-19
specialist: codex
parents:
  - h-new-288-1
  - h-new-288-2
  - h-new-288-3
pre_reg: findings/phase-b-hypotheses/h-new-288-4-token-count-core-projection-prereg.md
pre_reg_sha256: 9919841e3f508c20da1114df7c6b7983728c43a3e7db2236ba6ace75afd9d418
script: scripts/h_new_288_4_token_count_core_projection.py
output_json: findings/phase-b-hypotheses/csv/h-new-288-4.json
verdict: PASS-DIRECTED — the within-bin token-count projection summary T_tok = -0.661587 lands at p_short = 0.043526 under the exact 8! token-count assignment null, while the analogous verse-count contrast is null (p = 0.2660).
---

# [[h-new-288-4-token-count-core-projection|H-NEW-288.4]] - Within-bin token-count projection into the residualized Q108 short-core

## Headline

This is the first exact local explanation to survive after `[[h-new-288-3-residualized-core-projection|H-NEW-288.3]]`.

`[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]` showed a real opener-versus-refuge split.

`[[h-new-288-3-residualized-core-projection|H-NEW-288.3]]` then showed that the whole `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` speech-act axis does **not**
cleanly project onto the residualized short-core.

The next honest question was whether some narrower local factor orders approach
to that core inside the already-fixed `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` 5-7 verse side.

It does:

**shorter STEM-token count points toward the residualized `Q108` short-core
inside the fixed 5-7 verse side, and it does so exactly-significantly.**

Observed primary summary:

- `T_tok = -0.661587`
- exact lower-tail:
  **`p_short = 0.043526`**
- verdict:
  **`PASS-DIRECTED`**

Descriptive contrast:

- the analogous `verse_count` summary is only `T_verse = -0.262734`
- descriptive `p = 0.2660`

So the surviving local factor is **token count**, not just verse count.

## Locked setup

### Fixed side and fixed core

Reuse exactly:

- `B = {Q1, Q97, Q105, Q107, Q109, Q111, Q113, Q114}`
- `K = {Q108, Q106, Q103, Q112}`

### Fixed residualized family

Reuse exactly the `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` residualized family and primary metrics:

- `Fisher-Rao`
- `Jensen-Shannon`
- `Euclidean L2`
- `cosine-angle`

### Token-count vector

Using the same QAC STEM parse already used by `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`, the observed token
counts on `B` are:

| Surah | Token count |
|---|---:|
| Q1 | 23 |
| Q97 | 21 |
| Q105 | 18 |
| Q111 | 17 |
| Q114 | 16 |
| Q113 | 15 |
| Q107 | 14 |
| Q109 | 12 |

All eight counts are distinct, so the exact null contains:

- `8! = 40320` unique assignments

## Observed result

For each metric, define residualized core closeness:

`C_m(s) = -mean_{t in K} d_res,m(s, t)`

Then compute:

`r_m = Corr(token_count, C_m)`

Observed per-metric correlations:

| Metric | `r_m` |
|---|---:|
| Fisher-Rao | `-0.680337` |
| Jensen-Shannon | `-0.680935` |
| Euclidean L2 | `-0.642560` |
| Cosine-angle | `-0.642516` |

Primary summary:

`T_tok = mean(r_m) = -0.661587`

Interpretation:

- larger token count means farther from the residualized short-core
- smaller token count means closer to that core

## Exact null

Under the exact 40320-state token-count assignment null:

- null mean:
  `~ 0`
- null min:
  `-0.983295`
- null max:
  `0.925635`
- descending rank:
  `38567 / 40320`
- ascending rank:
  `1754 / 40320`
- exact lower-tail:
  **`0.043526`**

That clears the locked one-sided threshold.

## Descriptive verse-count contrast

The obvious cruder alternative is verse count.

Using the same exact pipeline descriptively:

- `T_verse = -0.262734`
- exact lower-tail over the 420 unique verse-count assignments:
  `0.266033`

So the local projection is **not** just "shorter in verse count."
The finer token-count measure is doing the real work.

## Interpretation

This result is important because it sharpens OQ-19 without undoing any earlier
adjudication.

It does **not** say:

- the global Q108 hub is "just length"
- literal normalization was secretly right after all
- the `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` speech-act result was false

It says something narrower and cleaner:

1. the global normalization-family question was already answered by
   `[[h-new-288-normalization-family-adjudication|H-NEW-288]]`
2. the fixed-pool medoid mechanism was already answered by `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`
3. the local opener-versus-refuge split was already answered by `[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]`
4. the whole-axis speech-act projection failed in `[[h-new-288-3-residualized-core-projection|H-NEW-288.3]]`
5. **inside that already-fixed local side, residualized short-core approach is
   still mechanically ordered by token count**

So the new honest reading is that OQ-19 contains both:

- a liturgical split that is not a clean whole-axis projection
- and a local residual-length ordering inside the short 5-7 verse side

That is materially more specific than anything on disk before this run.

## Scope

- no new normalization family
- no new candidate-set search
- no new metric family
- no MST rerun

This is a local explanatory refinement inside the already-landed OQ-19
machinery.

## Honest limits

1. This is still a local mechanical factor, not a full semantic explanation.
2. The result is conditioned on the fixed side `B` and fixed core `K`.
3. It explains part of the opener-versus-refuge split, not the entire global
   Q108 anomaly.

## Bottom line

`[[h-new-288-4-token-count-core-projection|H-NEW-288.4]]` lands the first clean post-`[[h-new-288-3-residualized-core-projection|H-NEW-288.3]]` explanation:

**inside the fixed [[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]] 5-7 verse side, shorter STEM-token count points
toward the residualized `Q108` short-core, and this survives an exact `8!`
assignment null.**

So the opener-versus-refuge split is not purely speech-act/semantic. It also
contains a real local residual-length component.
