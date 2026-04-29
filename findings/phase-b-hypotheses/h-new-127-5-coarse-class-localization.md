---
finding_id: h-new-127-5
title: "H-NEW-127.5 coarse-class one-vs-rest localization of locked compression structure"
phase: B
status: NULL (0 familywise-significant coarse classes; best = legal, |Δ| = 7.608650, p_maxT = 0.401280)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-4
pre_reg: findings/phase-b-hypotheses/h-new-127-5-coarse-class-localization-prereg.md
pre_reg_sha256: b124c2d260060c3caa0698441655960f81e74c8734f890d6b740f188731e0f2f
journal: journal/h-new-127-5-run-1.md
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; coarse label axis = first hyphen-delimited token of sinai_genre; 18 fixed one-vs-rest coarse-class cells; two-sided localization statistic T_c = |mean(z_s in c) - mean(z_s outside c)|; outer label-shuffle null preserves coarse class counts; familywise maxT correction across all 18 cells; 114 surahs)"
verdict: NULL
---

# [[h-new-127-5-coarse-class-localization|H-NEW-127.5]] - coarse-class one-vs-rest localization of locked compression structure

## Result

This bounded follow-up localized the positive [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] coarse-prefix
omnibus with 18 fixed one-vs-rest tests:

- observable reused exactly: `z_s = -gzip_z`
- class axis reused exactly: first hyphen-delimited token of locked
  `sinai_genre`
- per-cell statistic: `T_c = |mean(z_s in c) - mean(z_s outside c)|`
- outer null: coarse-prefix label shuffle preserving the exact 18 class counts
- familywise control: single-step maxT across all 18 cells

Exact localization result:

- familywise verdict: **NULL**
- familywise-significant coarse classes: **none**
- familywise-null mean maxT: `7.732622326915629`
- familywise-null sd maxT: `2.57387060549878`
- familywise-null `q95`: `12.81451653787599`
- familywise-null `q99`: `13.722123868712181`

Best observed cells:

- `legal`: positive `Δ = 7.608650012785614`, raw `p = 0.00004999750012499375`,
  corrected `p_maxT = 0.40127993600319983`
- `admonition`: negative `Δ = -6.723773984605927`, raw
  `p = 0.04704764761761912`, corrected `p_maxT = 0.5643717814109295`
- `hybrid`: positive `Δ = 5.24708599869908`, corrected
  `p_maxT = 0.8614069296535173`
- `oath`: negative `Δ = -4.930663319191329`, raw `p = 0.000199990000499975`,
  corrected `p_maxT = 0.9031548422578871`

## Interpretation

The [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] omnibus does not collapse, but it also does not localize to a
single familywise-protected coarse class. The coarse-prefix compression
structure is therefore better read as **distributed stratification across many
classes** rather than as a one-cell effect.

The descriptive extremes are still clear:

- strongest positive coarse class by mean `z_s`: `legal`
- strongest negative coarse class by mean `z_s`: `admonition`

But under the preregistered 18-cell maxT null, even the strongest positive cell
is ordinary enough to miss the `0.05` familywise bar.

## One-Vs-Rest Localization Table

| Coarse class | `n` | Mean `z_s` | Mean rest | `Δ` | Raw `p` | maxT `p` | FWE |
|---|---:|---:|---:|---:|---:|---:|---|
| legal | 13 | 7.845357 | 0.236707 | 7.608650 | 0.000050 | 0.401280 | no |
| admonition | 2 | -5.501453 | 1.222321 | -6.723774 | 0.047048 | 0.564372 | no |
| hybrid | 1 | 6.305419 | 1.058333 | 5.247086 | 0.261887 | 0.861407 | no |
| oath | 16 | -3.134281 | 1.796383 | -4.930663 | 0.000200 | 0.903155 | no |
| prophetic | 1 | -3.660324 | 1.146525 | -4.806849 | 0.314834 | 0.928104 | no |
| creedal | 1 | -3.506909 | 1.145167 | -4.652077 | 0.389931 | 0.960302 | no |
| address | 3 | -3.403308 | 1.226189 | -4.629496 | 0.108095 | 0.961152 | no |
| apotropaic | 2 | -3.404142 | 1.184869 | -4.589010 | 0.195640 | 0.962252 | no |
| eschatological | 15 | -2.592464 | 1.664485 | -4.256948 | 0.001700 | 0.984951 | no |
| scripture | 15 | 4.458118 | 0.596215 | 3.861903 | 0.004300 | 0.994850 | no |
| hymnic | 4 | -1.588095 | 1.202267 | -2.790362 | 0.276236 | 0.999900 | no |
| hymn | 2 | 3.449974 | 1.062474 | 2.387500 | 0.508575 | 1.000000 | no |
| narrative | 18 | 2.845644 | 0.777869 | 2.067775 | 0.102045 | 1.000000 | no |
| liturgical | 1 | -0.849270 | 1.121649 | -1.970919 | 0.774161 | 1.000000 | no |
| exhortative | 5 | 2.224889 | 1.052959 | 1.171929 | 0.615269 | 1.000000 | no |
| historical | 3 | 2.235459 | 1.073790 | 1.161670 | 0.703215 | 1.000000 | no |
| polemical | 10 | 0.388717 | 1.189548 | -0.800831 | 0.499675 | 1.000000 | no |
| tripartite | 2 | 1.158047 | 1.090718 | 0.067328 | 0.993200 | 1.000000 | no |

## Descriptive Ranking By Mean `z_s`

| Rank | Coarse class | `n` | Mean `z_s` |
|---:|---|---:|---:|
| 1 | legal | 13 | 7.845357 |
| 2 | hybrid | 1 | 6.305419 |
| 3 | scripture | 15 | 4.458118 |
| 4 | hymn | 2 | 3.449974 |
| 5 | narrative | 18 | 2.845644 |
| 6 | historical | 3 | 2.235459 |
| 7 | exhortative | 5 | 2.224889 |
| 8 | tripartite | 2 | 1.158047 |
| 9 | polemical | 10 | 0.388717 |
| 10 | liturgical | 1 | -0.849270 |
| 11 | hymnic | 4 | -1.588095 |
| 12 | eschatological | 15 | -2.592464 |
| 13 | oath | 16 | -3.134281 |
| 14 | address | 3 | -3.403308 |
| 15 | apotropaic | 2 | -3.404142 |
| 16 | creedal | 1 | -3.506909 |
| 17 | prophetic | 1 | -3.660324 |
| 18 | admonition | 2 | -5.501453 |

## Scope

- All 114 surahs were included.
- The compression scores were not recomputed.
- The coarse classes were not modified beyond the [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] first-token rule.
- Localization was two-sided and familywise-corrected across the full 18-cell
  search family.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-5-coarse-class-localization-prereg.md`
- Script: `scripts/h_new_127_5_oq20_coarse_class_localization.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-5.json`
- Journal: `journal/h-new-127-5-run-1.md`

## Verdict

**NULL**: the coarse-prefix omnibus in [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] does not localize to any
single coarse class under the preregistered 18-way one-vs-rest maxT correction.
