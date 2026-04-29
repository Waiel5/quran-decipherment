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
seed: 20260419
rules_tuple: "(114 surahs; QAC v0.4 STEM roots; K=500 top roots; literal family = count/N_i plus flat alpha=0.5; residualized family = raw counts plus alpha_i = 0.5 * mean_tokens / N_i; fixed pool P defined from revelation-order.csv and hafs-verse-counts.tsv only; mean pairwise distance medoid ranks computed inside P; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; total variation diagnostic only)"
verdict: POOL-MEDOID-SEPARATION
---

# H-NEW-288.1 - run log

## Command

```bash
python3 scripts/h_new_288_1_q108_residualized_pool_medoid.py
```

## Exact outputs

| Quantity | Value |
|---|---:|
| Pool size | 22 |
| `C_res` | 4 / 4 |
| `Delta_med` | 14 |
| Verdict | POOL-MEDOID-SEPARATION |

Primary metrics:

| Metric | Literal `R_lit(Q108)` | Residualized `R_res(Q108)` | Rank gap |
|---|---:|---:|---:|
| Fisher-Rao | 15 | 1 | 14 |
| Jensen-Shannon | 15 | 1 | 14 |
| Euclidean L2 | 15 | 1 | 14 |
| Cosine-angle | 15 | 1 | 14 |

Diagnostic metric:

| Metric | Literal rank | Residualized rank | Rank gap |
|---|---:|---:|---:|
| Total variation | 3 | 4 | -1 |

## Fixed pool

`Q1, Q86, Q91, Q93, Q94, Q95, Q97, Q99, Q100, Q101, Q102, Q103, Q104, Q105, Q106, Q107, Q108, Q109, Q111, Q112, Q113, Q114`

## Top-5 medoids by family

Fisher-Rao:

- literal:
  `Q91, Q100, Q86, Q104, Q111`
- residualized:
  `Q108, Q106, Q103, Q112, Q107`

Jensen-Shannon:

- literal:
  `Q91, Q100, Q86, Q104, Q111`
- residualized:
  `Q108, Q106, Q103, Q112, Q107`

Euclidean L2:

- literal:
  `Q91, Q100, Q86, Q104, Q111`
- residualized:
  `Q108, Q106, Q103, Q112, Q107`

Cosine-angle:

- literal:
  `Q91, Q100, Q86, Q104, Q111`
- residualized:
  `Q108, Q106, Q103, Q112, Q107`

## Notes

- The primary read is metric-stable: the same four primary metrics give the
  same `15 -> 1` Q108 rank shift.
- The diagnostic total-variation dissent reproduces the already-known H-NEW-284
  and H-NEW-288 pattern rather than contradicting the primary mechanism.
- The result explains the H-NEW-288 family split as local geometry inside a
  fixed short Early-Meccan cloud rather than as an abstract normalization
  label effect.

## Artifacts

- Prereg: `findings/phase-b-hypotheses/h-new-288-1-q108-residualized-pool-medoid-prereg.md`
- Script: `scripts/h_new_288_1_q108_residualized_pool_medoid.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-288-1.json`
- Finding: `findings/phase-b-hypotheses/h-new-288-1-q108-residualized-pool-medoid.md`
