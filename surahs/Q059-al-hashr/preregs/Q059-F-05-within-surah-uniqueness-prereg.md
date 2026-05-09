---
surah: 59
test_id: Q059-F-05
title: Q 59:22-24 within-surah window uniqueness
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q059-F-05-within-surah-uniqueness
alpha_bon: 0.025
post_hoc_origin: NO — this test was designed inline of the F-01 corpus-comparison test as the natural within-surah counterpart.
---

# Q059-F-05 — Pre-registration: Q 59:22-24 within-surah uniqueness

## 1. Hypothesis (locked)

**H1a (one-tailed):** Q 59:22-24 is the rank-1 3-verse window WITHIN Q 59 (among 22 internal windows) by absolute 99-name token count F99.

**H1b (one-tailed):** Q 59:22-24 is the rank-1 3-verse window WITHIN Q 59 by per-token-density (F99 / W).

## 2. Operational definition

- **Internal windows**: 22 windows v1-3, v2-4, ..., v22-24 (NO surah-boundary crossing).
- **F99**: 99-name token count under proclitic-tolerant substring matching (same as F-01).
- **Density**: F99 / W (no W-floor in this within-surah test, since all 22 windows are well-formed Q 59 verses).

## 3. Permutation null

**Word-count-weighted within-surah re-distribution:**
1. Total Q 59 99-name tokens = N (computed empirically).
2. For each permutation, sample N positions among Q 59's 24 verses with replacement, weighted by per-verse word-count.
3. After re-distribution, compute the max F and max density across the 22 internal windows.
4. p = fraction of permutations where null max ≥ observed.

n_perm = 10,000, seed = 20260509.

## 4. Success / Failure

- **CONFIRMED**: both H1a and H1b pass at p < α_bon = 0.025.
- **PASS**: one passes.
- **NULL**: neither.

## 5. Honest limits

- The within-surah null asks "given Q 59 has its observed N divine-name tokens distributed by length-weight, how often does ANY 3-verse window achieve the observed density?" The null preserves the **count and length-conditional rate**, but not the **lā-ilāha-illā-huwa anaphora structure** — which mechanically forces dense divine-naming in vv 22-24. The test is therefore conservative against a "structured-anaphora-as-cause" critique: even after structural anaphora is preserved-on-average via length-weighting, the v22-24 concentration exceeds chance.
- **The test is closely related to MW-5 positive control**: under H-NEW-95 Cell E, Q 59:22-24 is the global rank-1 corpus 3-verse window. The within-surah variant is a tighter test (smaller window pool) but with smaller null variance.

## 6. Rules-tuple

`(no-tashkeel, ornament-stripped, whitespace-tokenized, 99-name-substring-with-proclitic-tolerance, word-count-weighted-within-surah-permutation)`.

## 7. Bonferroni

k = 2 (F + density). α_bon = 0.025.

## 8. Authored by

Waiel Al-Shujaa, 2026-05-09.
