---
finding_id: h-new-288-1
title: "H-NEW-288.1 Q108 residualized-pool medoid test"
phase: B
status: POOL-MEDOID-SEPARATION (C_res = 4/4; Delta_med = 14)
date: 2026-04-19
specialist: codex
parent_finding: h-new-288
audit_backdrop: h-new-273 / h-new-284 / h-new-288
pre_reg: findings/phase-b-hypotheses/h-new-288-1-q108-residualized-pool-medoid-prereg.md
pre_reg_sha256: cc8fc48139c8ff5686f6b636841fb83fc05d810d78042dad4ee11b803da9d96a
journal: journal/h-new-288-1-run-1.md
seed: 20260419
rules_tuple: "(114 surahs; QAC v0.4 STEM roots; K=500 top roots; literal family = count/N_i plus flat alpha=0.5; residualized family = raw counts plus alpha_i = 0.5 * mean_tokens / N_i; fixed pool P defined from revelation-order.csv and hafs-verse-counts.tsv only; mean pairwise distance medoid ranks computed inside P; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; total variation diagnostic only)"
verdict: POOL-MEDOID-SEPARATION
---

# [[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]] - Q108 residualized-pool medoid test

## Result

This is the first mechanistic follow-up to [[h-new-288-normalization-family-adjudication|H-NEW-288]]. The family split was
already answered there. The live question was why the residualized family
preserves Q108 at all.

Locked pool:

- `P = {surahs with noldeke_phase = Early Meccan and verse_count <= 17}`
- fixed from `data/revelation-order.csv` and `data/hafs-verse-counts.tsv`
- pool size = `22`
- pool surahs:
  `Q1, Q86, Q91, Q93, Q94, Q95, Q97, Q99, Q100, Q101, Q102, Q103,`
  `Q104, Q105, Q106, Q107, Q108, Q109, Q111, Q112, Q113, Q114`

Primary test:

- for each family and metric, compute mean pairwise distance inside the fixed
  pool
- rank pool surahs by ascending mean distance
- Q108 rank `1` means Q108 is the pool medoid

Observed primary result:

- residualized rank-1 count
  `C_res = 4 / 4`
- median rank gap
  `Delta_med = median(R_lit - R_res) = 14`
- overall verdict:
  **POOL-MEDOID-SEPARATION**

## Metric Table

| Metric | Literal `R_lit(Q108)` | Residualized `R_res(Q108)` | Rank gap |
|---|---:|---:|---:|
| Fisher-Rao | 15 | 1 | 14 |
| Jensen-Shannon | 15 | 1 | 14 |
| Euclidean L2 | 15 | 1 | 14 |
| Cosine-angle | 15 | 1 | 14 |

Diagnostic-only metric:

| Metric | Literal rank | Residualized rank | Rank gap |
|---|---:|---:|---:|
| Total variation | 3 | 4 | -1 |

The diagnostic dissenter is exactly the one already isolated by [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] and
[[h-new-288-normalization-family-adjudication|H-NEW-288]], so it does not alter the primary read.

## Top Medoid Clouds

The local geometry changes sharply by family.

Literal family top-5 medoids are stable across the four primary metrics:

- `Q91`, `Q100`, `Q86`, `Q104`, `Q111`

Residualized family top-5 medoids are also stable across the four primary
metrics:

- `Q108`, `Q106`, `Q103`, `Q112`, `Q107`

So the residualized family does not merely make Q108 "less bad." It
re-centers the fixed short Early-Meccan pool around Q108 and a tight terminal
cluster near it.

## Interpretation

This is the mechanism [[h-new-288-normalization-family-adjudication|H-NEW-288]] was missing.

- [[h-new-288-normalization-family-adjudication|H-NEW-288]] said the Q108 hub belongs specifically to the residualized
  smoothing family
- [[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]] now shows *why*: residualized `alpha_i` smoothing turns the
  short Early-Meccan pool into a local cloud whose geometric medoid is Q108
- the literal family centers the same pool somewhere else entirely

So the surviving Q108 hub is not just a normalization-family label. It is a
local medoid effect inside a fixed short Early-Meccan pool.

This also sharpens the relation to [[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]:

- [[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]'s `Q1 + Q108` liturgical-anchor result is real but narrow
- [[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]] shows the broader residualized geometry is not reducible to that
  pair alone
- the stronger story is a short Early-Meccan terminal cloud with Q108 at its
  center

## Scope

- no new normalization family was introduced
- no MST was needed for the primary read
- the pool was fixed from chronology and verse count only
- total variation was kept diagnostic-only by preregistered design

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-288-1-q108-residualized-pool-medoid-prereg.md`
- Script: `scripts/h_new_288_1_q108_residualized_pool_medoid.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-288-1.json`
- Journal: `journal/h-new-288-1-run-1.md`

## Verdict

**POOL-MEDOID-SEPARATION**: inside a fixed short Early-Meccan pool, Q108 is
the residualized-family medoid across all four primary metrics but only rank
15 under the literal family.
