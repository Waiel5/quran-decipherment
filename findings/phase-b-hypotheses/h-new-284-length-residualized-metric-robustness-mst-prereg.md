---
finding_id: h-new-284
title: "Length-residualized metric-robustness MST follow-up for OQ-19"
specialist: codex
date_prereg: 2026-04-18
seed: 20260418
parent_backdrop:
  - h-new-131.1 (length-residualized smoothing; Cell B PASS at degree 16)
  - h-new-279 (locked 5-metric hub-robustness family)
  - h-new-282 (top-500 denominator rescue fails)
scope_note: "This run holds the H-NEW-131.1 Cell B residualized simplex fixed, then reruns the H-NEW-279 locked primary metric family only. No new feature space, no new denominator family, no new null-hunting."
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; length-residualized Dirichlet alpha_i = alpha_base * (mean_surah_tokens / surah_i_tokens); alpha_base=0.5; MST via Kruskal; no-tashkeel; QAC v0.4)"
primary_metric_family:
  - fisher_rao
  - jensen_shannon
  - total_variation
  - euclidean_l2
  - cosine_angle
primary_statistic: "C_LR = number of metrics in the locked family for which rank(Q108) <= 3"
family_role: "bounded descriptive adjudication; no p-value or native null is claimed because the metric ranks are dependent and the point is robustness of the surviving residue, not a fresh inferential test"
decision_rule: "C_LR >= 4 => metric-robust residue; C_LR in {2,3} => partial metric-robust residue; C_LR <= 1 => not robust after length equalization"
justification: "H-NEW-279 already used the same 5-metric family and a 4/5 majority rule for bounded robustness on the fixed alpha=0.5 simplex. H-NEW-131.1 Cell B showed the length-residualized simplex still preserves a real Q108 hub residue (degree 16), so H-NEW-284 keeps the same bounded majority standard and only asks whether that residue survives metric variation."
deliverables:
  - script: scripts/h_new_284_length_residualized_metric_robustness_mst.py
  - json: findings/phase-b-hypotheses/csv/h-new-284.json
  - findings: findings/phase-b-hypotheses/h-new-284-length-residualized-metric-robustness-mst.md
  - journal: journal/h-new-284-run-1.md
---

# [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] - Length-residualized metric-robustness MST follow-up for OQ-19

## Question

[[h-new-131-1-length-normalized-mst|H-NEW-131.1]] Cell B showed that a per-surah length-residualized smoothing
scheme still leaves Q108 with a real Fisher-Rao MST residue. [[h-new-279-metric-robustness-mst|H-NEW-279]]
showed that Q108 is metric-robust on the fixed alpha=0.5 simplex across
the locked 5-metric family.

The remaining question is narrower:

> after length equalization, does the surviving Q108 residue remain
> metric-robust across the same locked family?

## Locked setup

1. Build the same `114 x 500` top-QAC-STEM-root count matrix used in the
   [[h-new-131-q108-supernode|H-NEW-131]] / [[h-new-279-metric-robustness-mst|H-NEW-279]] line.
2. Apply the [[h-new-131-1-length-normalized-mst|H-NEW-131.1]] Cell B residualization:
   `alpha_i = alpha_base * (mean_surah_tokens / surah_i_tokens)`.
3. L1-normalize each residualized row to the simplex.
4. Rerun the [[h-new-279-metric-robustness-mst|H-NEW-279]] primary metric family only:
   Fisher-Rao, Jensen-Shannon, total variation, Euclidean L2,
   cosine-angle.
5. Build each complete-graph MST by Kruskal and compute competition
   rank for Q108.

## Primary statistic

`C_LR = number of metrics in the locked family for which rank(Q108) <= 3`

This is the only statistic used for the main adjudication.

## Decision rule

This is a bounded descriptive rule, not a null test:

- `C_LR >= 4` -> metric-robust residue
- `C_LR in {2, 3}` -> partial metric-robust residue
- `C_LR <= 1` -> not robust after length equalization

The threshold is intentionally inherited from [[h-new-279-metric-robustness-mst|H-NEW-279]]'s 4/5 majority
standard for bounded metric robustness. There is no native null for the
post-residualization rank table, so no p-value will be claimed.

## Deliverables

- Script: `scripts/h_new_284_length_residualized_metric_robustness_mst.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-284.json`
- Findings: `findings/phase-b-hypotheses/h-new-284-length-residualized-metric-robustness-mst.md`
- Journal: `journal/h-new-284-run-1.md`
