---
finding_id: Q067-F-04
title: "Q 67 mulk-stem (m-l-k) lexical concentration — does the al-Mulk-named surah over-concentrate its name-stem?"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 2024
n_perm: 0 (hypergeometric exact)
bonferroni_k: 114
alpha_raw: 0.05
alpha_bonferroni: 4.39e-4
direction: "POSITIVE — Q 67 expected to over-concentrate mlk-stem family; failure = NULL on the name-tracks-vocabulary hypothesis"
---

# Q067-F-04 — m-l-k stem lexical concentration

## Hypothesis

Q 67 al-Mulk over-concentrates the QAC m-l-k root family at a rate distinguishable from uniform random distribution, after Bonferroni correction for testing all 114 surahs — analogous to Q 24 al-Nūr's vindicated light-cluster concentration (Q024-F-01 at p<10⁻⁶).

This tests the **name-tracks-vocabulary** hypothesis at a Q 67 instance. A NULL result would falsify the corpus-wide generalization.

## Mlk-stem definition (LOCKED PRE-REG)

The mlk-stem is the QAC root **mlk**, which encompasses:
- *al-mulk* (the dominion)
- *malik* (king)
- *malakūt* (kingdom)
- *malāʾika* (angels)
- *māla* (own)
- and any other QAC-categorized mlk-tokens

The single QAC root **mlk** is the locked target. No alternative root family will be added or removed after observing the data.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-STEM-roots, QAC v0.4 morphological annotations, basmala-counted-only-in-Q1, Hafs-Kufan)`

## Null distribution

Hypergeometric null: under the assumption that all 49,968 root-tokens of the corpus have equal probability of being any of the corpus's 206 mlk-tokens, how many mlk-tokens would Q 67's 208-token sample receive?

Expected: (208 × 206) / 49,968 ≈ **0.86** tokens.

Under the hypergeometric null with parameters N=49,968, K=206, n=208, k=observed:
- P(X ≥ k_observed) computed via log-combinatorial sum.

## Direction (LOCKED)

The direction is POSITIVE: Q 67 is expected to over-concentrate mlk-stem tokens (>1 standard deviation above expected). A *NULL* result (Q 67 tracking expectation, k_observed close to 0.86) is the NULL finding that **falsifies the name-tracks-vocabulary corpus-generalization**.

## Success criteria

- p_raw < 4.39 × 10⁻⁴ (Bonferroni for 114 surahs): **VINDICATED**, name-tracks-vocabulary holds for Q 67.
- p_raw < 0.05: **DIRECTIONAL**.
- p_raw > 0.05 OR k_observed ≈ expected: **NULL** — the name-tracks-vocabulary hypothesis is FALSIFIED for Q 67.

## Failure criteria

- Q 67 mlk-stem count *less than* expected (0.86): direction-violation, treat as strong NULL.
- Bonferroni α not met but raw α met: DIRECTIONAL only.

## Discriminating control

Q 24 al-Nūr's light-cluster (Q024-F-01) passed at p<10⁻⁶. If Q 67's mlk-stem fails to pass, the name-tracks-vocabulary hypothesis is **rules-tuple-fragile across surahs** — confirmed for Q 24, falsified for Q 67. The corpus-generalization is FALSIFIED.

## Output files

- Pre-reg: this file (`preregs/Q067-F-04-mulk-stem-density-prereg.md`).
- Script: `scripts/Q067_F_04_mulk_stem_density.py`.
- JSON: `csv/Q067-F-04.json`.
- Findings: in `06-novel-findings.md`.
