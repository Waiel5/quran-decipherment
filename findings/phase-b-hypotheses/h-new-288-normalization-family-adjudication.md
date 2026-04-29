---
id: H-NEW-288
title: "Normalization-family adjudication for OQ-19"
phase: B
status: PASS-BOUNDED - RESIDUALIZED-FAMILY-DOMINANCE (Delta_C = 4; 4/5 vs 0/5)
date: 2026-04-19
specialist: codex
parents:
  - h-new-278
  - h-new-279
  - h-new-282
  - h-new-284
seed: 20260419
prereg: findings/phase-b-hypotheses/h-new-288-normalization-family-adjudication-prereg.md
script: scripts/h_new_288_normalization_family_adjudication.py
json: findings/phase-b-hypotheses/csv/h-new-288.json
journal: journal/h-new-288-run-1.md
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; MST via Kruskal; no-tashkeel; QAC v0.4; primary metrics = Fisher-Rao / Jensen-Shannon / total variation / Euclidean L2 / cosine-angle)"
verdict: RESIDUALIZED-FAMILY-DOMINANCE — when the five-metric MST panel is held fixed, literal count / N_i normalization gives Q108 top-3 status on 0/5 metrics, while residualized alpha_i smoothing gives top-3 status on 4/5 metrics (Delta_C = 4). The surviving Q108 residue belongs to the residualized smoothing family, not to literal length normalization generically.
---

# [[h-new-288-normalization-family-adjudication|H-NEW-288]] - Normalization-family adjudication for OQ-19

## Headline

This is the cleanest next OQ-19 adjudication after [[h-new-278-length-normalized-mst|H-NEW-278]], [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]],
and [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] because it holds the [[h-new-279-metric-robustness-mst|H-NEW-279]] five-metric panel fixed and
changes only the normalization family.

The result is not close:

- literal `count / N_i` family: `C_lit = 0 / 5`
- residualized `alpha_i = 0.5 * mean_tokens / N_i` family:
  `C_res = 4 / 5`
- separation statistic: `Delta_C = 4`

That lands the pre-registered verdict:

> **RESIDUALIZED-FAMILY-DOMINANCE**

So the surviving Q108 hub residue is **not** a generic
"length-normalized" phenomenon. It belongs specifically to the
residualized smoothing family.

## Inherited anchors

The run is promotable because both inherited anchors reproduced exactly:

- literal-family Fisher-Rao matched [[h-new-278-length-normalized-mst|H-NEW-278]]:
  `Q108 degree = 1`, `Q7 degree = 15`
- residualized-family Fisher-Rao matched [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] / [[h-new-131-1-length-normalized-mst|H-NEW-131.1]]:
  `Q108 degree = 16`, `Q108 rank = 1`

So the family comparison is not being driven by a broken reimplementation.

## Exact family table

### Literal normalization family

This is the [[h-new-278-length-normalized-mst|H-NEW-278]] family rerun across the full five-metric panel:
divide by total surah STEM-root tokens `N_i`, then add flat `alpha=0.5`.

| Metric | Q108 degree | Q108 rank | Top-3? |
|---|---:|---:|---|
| Fisher-Rao | 1 | 40 | no |
| Jensen-Shannon | 1 | 40 | no |
| Total variation | 5 | 5 | no |
| Euclidean L2 | 1 | 43 | no |
| Cosine-angle | 1 | 43 | no |

Primary count:

- `C_lit = 0 / 5`

### Residualized smoothing family

This is the [[h-new-131-1-length-normalized-mst|H-NEW-131.1]] / [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] family: raw counts plus
`alpha_i = 0.5 * mean_tokens / N_i`.

| Metric | Q108 degree | Q108 rank | Top-3? |
|---|---:|---:|---|
| Fisher-Rao | 16 | 1 | yes |
| Jensen-Shannon | 16 | 1 | yes |
| Total variation | 3 | 12 | no |
| Euclidean L2 | 15 | 1 | yes |
| Cosine-angle | 15 | 1 | yes |

Primary count:

- `C_res = 4 / 5`

## Mechanism read

The strongest descriptive fact is local, not just rank-based.

### Literal family mostly reduces Q108 to a leaf

Under literal normalization, `Q108` is a singleton `Q89` leaf in
`4 / 5` metrics:

- Fisher-Rao -> neighbor `Q89`
- Jensen-Shannon -> neighbor `Q89`
- Euclidean L2 -> neighbor `Q89`
- Cosine-angle -> neighbor `Q89`

Only total variation gives Q108 a multi-edge residue, and even there the
result is weak:

- TV neighbors = `{Q113, Q100, Q107, Q106, Q93}`
- TV rank = `5`, still outside the top-3

### Residualized family preserves a stable Q108 neighbor core

Under residualized smoothing, `Q108` keeps a recurring short-surah core:

- `Q106`, `Q111`, `Q112` appear in `5 / 5` metrics
- `Q103`, `Q107`, `Q94`, `Q113`, `Q105`, `Q104`, `Q102`, `Q114`,
  `Q100`, `Q101`, `Q97`, `Q93` appear in `4 / 5` metrics

So the residualized family does not merely preserve a rank label. It
preserves a broad local neighborhood around Q108 that the literal family
mostly destroys.

## Interpretation

This is the cleanest bounded read now available for OQ-19:

- [[h-new-279-metric-robustness-mst|H-NEW-279]] showed Q108 is metric-robust on the baseline simplex
- [[h-new-278-length-normalized-mst|H-NEW-278]] and [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] showed literal normalization families collapse
  the anomaly under Fisher-Rao
- [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] showed a residualized residue survives across `4 / 5`
  metrics
- **[[h-new-288-normalization-family-adjudication|H-NEW-288]] now adjudicates the family conflict directly**

Because the metric panel is held fixed, the separation cannot be blamed
on metric choice. Because [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] already failed, the separation is not
just a denominator-bookkeeping artifact inside the literal family.

The honest update is therefore:

> the surviving Q108 hub residue is **family-specific**. It is carried by
> residualized smoothing, not by literal per-surah length normalization.

## Limits

1. This is still a bounded descriptive family adjudication, not a fresh
   inferential null test.
2. The feature space remains the locked top-500 QAC-STEM root matrix.
3. The result distinguishes the two family heads already on disk; it does
   not prove the residualized family is uniquely canonical in every
   conceivable normalization space.

## Bottom line

`[[h-new-288-normalization-family-adjudication|H-NEW-288]]` gives OQ-19 its cleanest normalization-family answer so far:

**when the metric family is held fixed, Q108 survives only in the
residualized smoothing family (`4/5` metrics) and fails completely in the
literal normalization family (`0/5`).**
