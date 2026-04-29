---
id: H-NEW-288-2
title: Q1 liturgical-separation test inside the residualized Q108 pool
phase: B
status: PASS-DIRECTED — Q1 is the unique maximum of the fixed H-NEW-273 score times metric-consistent residualized ejection inside the exact H-NEW-288.1 pool
date: 2026-04-19
specialist: codex
parents:
  - h-new-273
  - h-new-288
  - h-new-288-1
pre_reg: findings/phase-b-hypotheses/h-new-288-2-q1-liturgical-separation-prereg.md
pre_reg_sha256: 0e94e5eb699aeb052eb34d8eae98ef259b87cfc75610a44772e1d28835b705be
script: scripts/h_new_288_2_q1_liturgical_separation.py
output_json: findings/phase-b-hypotheses/csv/h-new-288-2.json
verdict: PASS-DIRECTED — inside the fixed short Early-Meccan pool from H-NEW-288.1, Q1 is the unique maximum of L_sep(s)=S_H273(s) * C_sep(s), where C_sep(s) counts the four primary metrics on which residualized smoothing moves s farther from Q108 than literal normalization does. Exact upper-tail over the 21 admissible surahs is p = 1/21 = 0.047619.
---

# [[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]] - Q1 liturgical-separation test inside the residualized Q108 pool

## Headline

This is the first direct integration test between:

- the narrow `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` Q1↔Q108 speech-act foothold, and
- the broader `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` residualized medoid mechanism

The result is not that the two findings collapse into one mechanism.

It is the opposite, but in a bounded way:

**inside the exact `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` short Early-Meccan pool, `Q1` is the unique
maximum of the fixed liturgical-separation score**

`L_sep(s) = S_H273(s) * C_sep(s)`

with:

- `S_H273(s) = sqrt(divine_share_{Alh,rbb,rHm}(s) * imperative_density(s))`
- `C_sep(s) = # of the four primary metrics on which residualized smoothing
  moves `s` farther from `Q108` than literal normalization does`

Observed target:

- `L_sep(Q1) = 0.834183`
- exact descending rank:
  **`1 / 21`**
- exact upper-tail:
  **`p = 0.047619`**

Verdict:

- **`PASS-DIRECTED`**

So the live OQ-19 picture is now sharper:

> the `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` Q1↔Q108 foothold is real, but it is **not** simply the same
> thing as the residualized-family medoid cloud from `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`.
> `Q1` is specifically the strongest high-liturgical short surah that the
> residualized family pushes away from `Q108`.

## Locked result

### Fixed pool and families

Inherited exactly from `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`:

- pool `P = {Early Meccan surahs with verse_count <= 17}`
- candidate family `P \\ {Q108}` with **21** admissible surahs
- literal family = `count / N_i` plus flat `alpha = 0.5`
- residualized family = raw counts plus
  `alpha_i = 0.5 * mean_tokens / N_i`
- primary metrics:
  `Fisher-Rao`, `Jensen-Shannon`, `Euclidean L2`, `cosine-angle`

### Primary target Q1

For `Q1`, the distance-rank movement relative to `Q108` is perfectly
consistent across the four primary metrics:

| Metric | Literal rank to Q108 | Residualized rank to Q108 | Delta |
|---|---:|---:|---:|
| Fisher-Rao | 14 | 17 | +3 |
| Jensen-Shannon | 14 | 17 | +3 |
| Euclidean L2 | 14 | 17 | +3 |
| Cosine-angle | 14 | 17 | +3 |

So:

- `C_sep(Q1) = 4 / 4`
- `S_H273(Q1) = 0.208546`
- `L_sep(Q1) = 0.834183`

Exact bounded candidate-family result:

- descending rank:
  **`1 / 21`**
- exact upper-tail:
  **`1 / 21 = 0.047619`**

That clears the locked directional threshold.

## Top exact separation candidates

The only positive-scoring separation candidates are:

| Rank | Surah | `S_H273` | `C_sep` | `L_sep` |
|---|---:|---:|---:|---:|
| 1 | **Q1** | **0.208546** | **4** | **0.834183** |
| 2 | Q94 | 0.125000 | 4 | 0.500000 |
| 3 | Q93 | 0.098688 | 4 | 0.394751 |

Everything else is zero because either:

- the surah has no positive `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` speech-act score, or
- it is not consistently pushed away from `Q108`

So the pass is not being driven by generic distance-rank churn. It is driven by
the fact that the strongest inherited speech-act surah among the consistently
ejected candidates is specifically `Q1`.

## Descriptive contrast

The strongest descriptive counterpoint is `Q112`, which matters because
`[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` already named `Q1 + Q112` as the best non-target competitor pair.

For `Q112`:

| Metric | Literal rank to Q108 | Residualized rank to Q108 | Delta |
|---|---:|---:|---:|
| Fisher-Rao | 20 | 3 | -17 |
| Jensen-Shannon | 20 | 3 | -17 |
| Euclidean L2 | 20 | 3 | -17 |
| Cosine-angle | 20 | 3 | -17 |

So descriptively:

- `C_app(Q112) = 4 / 4`
- `S_H273(Q112) = 0.223607`
- `L_app(Q112) = 0.894427`

and `Q112` is the unique top descriptive **approach** candidate.

The same descriptive direction holds for:

- `Q114`
- `Q113`

which are the two refuge surahs already used as the non-passing contrast in
`[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]`.

That gives the OQ-19 integration problem a concrete internal split:

- `Q1` is the strongest high-liturgical **ejected** surah
- `Q112`, `Q114`, and `Q113` are the strongest high-liturgical
  **approaching** surahs

## Interpretation

This is the first bounded result that tells us how `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` and
`[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` fit together.

The honest reading is:

1. `[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` did not identify a generic "all short liturgical surahs merge
   with Q108" mechanism.
2. `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]` did not erase the `Q1↔Q108` foothold either.
3. Instead, the residualized-family cloud **bifurcates** the liturgical side:
   it pulls `Q112/113/114` toward `Q108`, while `Q1` becomes the strongest
   high-score surah pushed away from `Q108`.

So the opener surah is now boundedly separated from the refuge/Ikhlas side
inside the residualized short-surah cloud.

That is exactly the kind of integration result OQ-19 was missing.

## Scope

- no new normalization family was introduced
- no new metric family was introduced
- no new liturgical score was invented
- the pool is exactly the one fixed by `[[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]]`

This is a clean cross-finding integration test, not another generic rerun.

## Honest limits

1. The candidate family has only 21 members, so the pass sits at the minimum
   attainable exact upper-tail (`1 / 21`).
2. The finding is directional because both the target `Q1` and the score
   `S_H273` are inherited from earlier OQ-19 work.
3. The descriptive `Q112/113/114` approach pattern was not a second primary
   cell.
4. This does not yet explain *why* the opener behaves differently; it only
   shows that the difference is real inside the fixed residualized pool.

## Bottom line

`[[h-new-288-2-q1-liturgical-separation|H-NEW-288.2]]` lands the first direct OQ-19 integration pass:

**`Q1` is the unique strongest high-`[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]`-score surah that the
residualized `Q108` family consistently pushes away rather than drawing in.**

So the narrow `Q1↔Q108` liturgical foothold and the broader residualized
medoid mechanism are now boundedly linked as **complementary but non-identical**
structures.
