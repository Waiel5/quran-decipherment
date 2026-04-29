---
id: H-NEW-274
title: "Empirical-vs-classical a-priori reassignment test for Q36 YS and Q42 HMASQ — PASS-HOLDOUT-STRONGER"
phase: B
status: PASS-HOLDOUT-STRONGER
date: 2026-04-18
executed_by: codex
parent_1: H-NEW-232
parent_2: H-NEW-252
parent_3: H-NEW-165.2
prereg: h-new-274-empirical-vs-classical-singleton-reassignment-prereg.md
prereg_sha256: 5a64d6c614eb75d843831fd8243d037b020865d3845f614b1d3a5e4ecd59312d
rules_tuple: "(discovery source locked to h-new-232.json only; empirical replacements locked to YS->HM and HMASQ->TSM from discovery nearest centroids; holdout spaces locked to h-new-252 joint 17-dim and h-new-165.2 V1/V2/V3; paired 40-cell classical-vs-empirical comparison; exact one-sided discordant-cell binomial test; alpha_primary=0.025)"
verdict: PASS-HOLDOUT-STRONGER
---

# [[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]] — empirical-vs-classical singleton reassignment

## Headline

**PASS-HOLDOUT-STRONGER.**

Using `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` as the only discovery source, I replaced just two classical
accepted-cluster entries:

- `Q36 YS: {ALM, ALR} -> {HM}`
- `Q42 HMASQ: {HM} -> {TSM}`

Then I scored the inherited classical table versus this single empirical
replacement table on four locked holdout spaces:

- `[[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]]` joint phonology + `(alpha, beta)` space
- `[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]` Watson modern voice recode
- `[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]` strict pharyngeal split
- `[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]` Holes glottal ha/ayn recode

The result is clean:

- **Classical holdout score: 32 / 40**
- **Empirical holdout score: 40 / 40**
- **Delta: +8 cells**
- **Improved cells: 8**
- **Worsened cells: 0**
- **Exact one-sided discordant-cell p = 0.00390625**

Under the pre-registered materiality rule (`delta >= 6`, `worsened = 0`,
`p < 0.025`), the empirical reassignment table is materially stronger.

## Why this is not circular

The comparison is discovery/holdout split, not a trivial rescore of the same
artifact:

- discovery-only source for the replacement pair: `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]`
- primary evaluation: 4 holdout spaces only

I deliberately did **not** evaluate broader replacement-table families in this
first pass. This finding is narrowly about whether the single empirical
replacement pair outperforms the inherited classical pair.

## Holdout results

| Holdout space | Classical | Empirical | Delta | Q36 YS nearest | Q42 HMASQ nearest |
|---|---:|---:|---:|---|---|
| [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] joint 17-dim | 8/10 | 10/10 | +2 | HM | TSM |
| [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] Watson voice | 8/10 | 10/10 | +2 | HM | TSM |
| [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] strict pharyngeal | 8/10 | 10/10 | +2 | HM | TSM |
| [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] Holes glottal | 8/10 | 10/10 | +2 | HM | TSM |

Every holdout space reproduces the same pattern:

- `YS` lands at `HM`
- `HMASQ` lands at `TSM`
- every other singleton stays unchanged

So the entire gain comes from the two disputed rows, repeated in all four
holdout geometries.

## Primary test

Unit of analysis: singleton-space cell.

- 4 holdout spaces x 10 singleton rows = **40 cells**
- discordant cells = **8**
- empirical-improved cells = **8**
- classical-improved cells = **0**

Under the pre-registered one-sided exact binomial on discordant cells:

- `p = 1 / 2^8 = 0.00390625`

This is well inside the locked `alpha_primary = 0.025`.

## Distance-margin check

The empirical pair is not winning by a zero-margin tie. In every holdout space,
the empirical cluster is geometrically closer than the classical alternative.

### Q36 YS empirical margin

Defined as `min(d(ALM), d(ALR)) - d(HM)`.

| Holdout space | Margin |
|---|---:|
| [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] joint 17-dim | 1.7886 |
| [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] Watson voice | 0.9912 |
| [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] strict pharyngeal | 1.0655 |
| [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] Holes glottal | 0.9645 |

- mean margin = **1.2025**
- min margin = **0.9645**
- all 4 holdouts positive

### Q42 HMASQ empirical margin

Defined as `d(HM) - d(TSM)`.

| Holdout space | Margin |
|---|---:|
| [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] joint 17-dim | 1.9368 |
| [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] Watson voice | 3.1794 |
| [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] strict pharyngeal | 2.8535 |
| [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] Holes glottal | 2.8558 |

- mean margin = **2.7064**
- min margin = **1.9368**
- all 4 holdouts positive

## Interpretation

The cleanest reading is narrow and strong:

- the inherited classical singleton-account table is already good at `8/10`
- the remaining two disagreements are not feature-fragile accidents
- replacing those two disputed entries with the empirical nearest-cluster
  assignments yields a strictly stronger holdout account

So the pressure point is no longer the feature geometry. The pressure point is
the **interpretation table** layered on top of that geometry.

This does **not** mean the broader classical tradition collapses. It means that,
for the singleton nearest-centroid account defined by [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] and stress-tested
by [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] / [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]], the tighter table is:

- `YS -> HM`
- `HMASQ -> TSM`

## Descriptive context

Although discovery was excluded from the primary test, it points in the same
direction:

- `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` classical score = **8/10**
- `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` empirical replacement score = **10/10**

Across discovery + holdouts together:

- classical total = **40/50**
- empirical total = **50/50**

This 50/50 number is descriptive only; the verdict is driven by the 4 holdout
spaces.

## Honest limits

1. This is a **bounded meta-test** of two competing accepted-cluster tables, not
   a new raw-feature discovery.
2. The four holdout spaces are alternate formulations on the same 29 muq
   surahs, not independent corpora.
3. The empirical replacement table is discovery-derived from `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]`, so
   the strongest claim available here is holdout replication across related
   geometries.
4. I did not search broader replacement-table families in this first pass,
   because the clean two-row test was already decisive.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-274-empirical-vs-classical-singleton-reassignment-prereg.md`
- Script: `scripts/h_new_274_empirical_vs_classical_singleton_reassignment.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-274.json`
- Journal: `journal/h-new-274-run-1.md`
