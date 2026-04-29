---
finding_id: Q024-F-01
title: "Q 24 over-concentrates the Quranic light-cluster lexicon"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 2024
n_perm: 10000
bonferroni_k: 114
alpha_raw: 0.05
alpha_bonferroni: 4.39e-4
direction: positive (Q 24 expected to over-concentrate light-cluster)
---

# Q024-F-01 — Light-vocabulary density audit

## Hypothesis

Q 24 al-Nūr ("The Light") over-concentrates the Quranic light-cluster lexicon at a rate distinguishable from uniform random distribution, after Bonferroni correction for testing all 114 surahs.

## Light-cluster definition (LOCKED PRE-REG)

The light-cluster is defined as the set of QAC roots:

```
LIGHT = {nwr, SbH, wqd, srj, qbs, shhb, mskw, zjj, kwkb, $jr, zyt, brk, $kw, drr, DwA, mvl}
```

This is 16 roots, drawn from:
- **Q 24:35 itself**: nwr (light/fire), SbH (lamp), wqd (kindle), zjj (glass), kwkb (star), $jr (tree), zyt (oil/olive), brk (bless), $kw (niche), drr (pearl/brilliant), DwA (illuminate), mvl (parable).
- **Standard Quranic light/fire/lamp lexicon**: srj (lamp, e.g., Q 25:61), qbs (firebrand, Q 27:7), shhb (flame, Q 37:10), mskw (alternative niche-form spelling).

All 16 roots are pre-locked before any computation; no roots will be added or removed after observing the data.

QAC parses both *nūr* (نور, light) and *nār* (نار, fire) under the same root *nwr*. This is the QAC convention and is treated as a single semantic field for this analysis. The decision to use the joint lemmatization is made BEFORE running the test.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots, QAC v0.4 morphological annotations, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`

## Null distribution

Hypergeometric null: under the assumption that all 49,968 root-tokens of the corpus have equal probability of being any of the 16 light-cluster roots (collectively making up the corpus's 512 light-cluster tokens), how many light-cluster tokens would Q 24's 859-token sample receive?

Expected: (859 × 512) / 49,968 ≈ 8.80 tokens.

Under the hypergeometric null with parameters N=49,968, K=512, n=859, k=27:
- P(X ≥ 27) = ?

This is computed via log-combinatorial sum.

## Direction (LOCKED)

The direction is POSITIVE: Q 24 is expected to over-concentrate light-cluster tokens. A *negative* result (Q 24 under-concentrating, or scoring at a non-significant percentile) is a NULL finding. A *positive* result (p_raw < α_Bonferroni) is a CONFIRMATION.

## Success criteria

- p_raw < 4.39 × 10⁻⁴ (Bonferroni for 114 surahs at α_raw = 0.05): **VINDICATED**
- p_raw < 0.05 but > 4.39 × 10⁻⁴: **DIRECTIONAL**
- p_raw > 0.05: **NULL**

## Failure criteria

- Q 24 light-cluster count *less than* expected (8.80): direction-violation, treat as NULL with prominence.
- Bonferroni α not met but raw α met: DIRECTIONAL only; not VINDICATED.

## Replication test

The same test is run on Q 33 al-Aḥzāb as a control: Q 33 should NOT show high light-cluster concentration (it is a Medinan-legal surah without light theme). If Q 33 also passes the test, the test is too liberal; the discrimination is broken. If Q 33 fails (as expected), the test is discriminating.

## Output files

- Pre-reg: this file (`preregs/Q024-F-01-light-vocabulary-density-prereg.md`).
- Script: `scripts/Q024_F_01_light_vocabulary_density.py`.
- JSON: `csv/Q024-F-01.json`.
- Findings: `Q024-F-01-light-vocabulary-density.md` (in `06-novel-findings.md`).
