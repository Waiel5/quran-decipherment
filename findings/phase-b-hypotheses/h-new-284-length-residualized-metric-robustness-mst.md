---
finding_id: h-new-284
title: "Length-residualized metric-robustness MST follow-up for OQ-19"
phase: B
status: PASS-BOUNDED - METRIC-ROBUST RESIDUE (C_LR = 4/5)
date: 2026-04-18
specialist: codex
parents:
  - h-new-131.1
  - h-new-279
  - h-new-282
seed: 20260418
prereg: findings/phase-b-hypotheses/h-new-284-length-residualized-metric-robustness-mst-prereg.md
script: scripts/h_new_284_length_residualized_metric_robustness_mst.py
json: findings/phase-b-hypotheses/csv/h-new-284.json
journal: journal/h-new-284-run-1.md
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; length-residualized Dirichlet alpha_i = alpha_base * (mean_surah_tokens / surah_i_tokens); alpha_base=0.5; Fisher-Rao / Jensen-Shannon / total variation / Euclidean L2 / cosine-angle; MST via Kruskal; no-tashkeel; QAC v0.4)"
---

# [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] - Length-residualized metric-robustness MST follow-up for OQ-19

## Headline

[[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] reruns the [[h-new-279-metric-robustness-mst|H-NEW-279]] locked 5-metric family on the
[[h-new-131-1-length-normalized-mst|H-NEW-131.1]] Cell B length-residualized simplex. The surviving Q108
residue is still metric-robust by the inherited bounded rule:
`C_LR = 4/5`.

That is the cleanest honest adjudication:

- the length-equalized residue survives on 4 of 5 metrics
- it fails only on total variation
- there is no native null here, so the claim stays descriptive

## Exact outputs

Length-residualized simplex:

- mean surah STEM-root tokens = `438.3157894736842`
- Q108 total STEM-root tokens = `7`
- Q108 top-500 tokens = `4`
- Q108 top-500 coverage = `0.5714285714285714`
- Q108 effective alpha_i = `31.30827067669173`
- Q2 effective alpha_i = `0.05642582253780693`
- alpha_i range = `[0.05642582253780693, 31.30827067669173]`

Per-metric Q108 results:

| Metric | Q108 degree | Q108 rank | Top-3? |
|---|---:|---:|---|
| Fisher-Rao | 16 | 1 | yes |
| Jensen-Shannon | 16 | 1 | yes |
| Total variation | 3 | 12 | no |
| Euclidean L2 | 15 | 1 | yes |
| Cosine-angle | 15 | 1 | yes |

Primary statistic:

- `C_LR = 4/5`

Consensus top-3 appearances across the 5 metrics:

- `Q7 = 5`
- `Q108 = 4`
- `Q64 = 4`

## Decision

The pre-committed rule from the prereg was:

- `C_LR >= 4` -> metric-robust residue
- `C_LR in {2,3}` -> partial metric-robust residue
- `C_LR <= 1` -> not robust after length equalization

[[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] lands at `C_LR = 4/5`, so the verdict is:

> Q108 remains a metric-robust residue after length equalization, but
> the robustness is bounded rather than universal.

## Interpretation

This is narrower than [[h-new-279-metric-robustness-mst|H-NEW-279]] and cleaner than [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]].

- [[h-new-131-1-length-normalized-mst|H-NEW-131.1]] Cell B already showed the residue survives explicit length
  residualization at Fisher-Rao degree 16.
- [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] shows that this residue is not Fisher-Rao-only: it survives
  on JS, Euclidean L2, and cosine-angle as well.
- Total variation is the one metric that breaks the top-3 standing.

So the surviving residue is real, but it is not fully metric-invariant.
The correct bounded reading is:

> length equalization reduces the original super-hub, but does not erase
> Q108's top-tier status across the locked metric family.

## Caveat

No native null or p-value is claimed here. The five metric outcomes are
dependent, so this is a bounded descriptive robustness adjudication, not
a fresh inferential test.
