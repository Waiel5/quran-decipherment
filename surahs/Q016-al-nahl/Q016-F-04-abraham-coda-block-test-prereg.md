---
finding_id: Q016-F-04
title: Abraham-as-imam-of-nations coda Q 16:120–123 — block-homogeneity vs surah-mean
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q016-al-nahl-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q016-F-04-coda-block
bonferroni_k: 2
alpha_bon: 0.025
direction: one-sided LOWER on cosine(coda-vector, Q16-mean-vector minus coda) — i.e. coda is LESS similar to surah-rest than a random 4-verse window in Q 16
success_criterion: cosine(coda, surah_minus_coda) < observed-mean of 10000 random 4-verse windows in Q 16; permutation p ≤ α_bon = 0.025 (passes one of 2 sub-tests)
failure_criterion: cosine ≥ surah-mean; both sub-tests NULL
rules_tuple: "(no-tashkeel, QAC-root-set or orthographic-token-set, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
script: surahs/Q016-al-nahl/scripts/Q016_F_04_abraham_coda.py
output_json: surahs/Q016-al-nahl/csv/Q016-F-04.json
parent_oq: al-Biqāʿī seam-detection — does Q 16:120–123 form a distinct sub-block?
---

# Q016-F-04 — Abraham coda block-homogeneity (pre-reg)

## 1. Hypothesis

**H1 (one-tailed):** The 4-verse Abraham coda Q 16:120–123 is structurally **HETEROGENEOUS** with the rest of Q 16 — its content-vector is less similar to the surah-mean (minus coda) than a random 4-verse window inside Q 16. Equivalently: the coda forms a distinct sub-block.

**H0:** The coda is no more distant from the surah-rest than any random 4-verse window inside Q 16.

**Direction:** cosine(coda, surah_minus_coda) < cosine of random-4-verse-window inside Q 16 (LOWER = LOCKED).

## 2. Operational definition (2-cell battery)

For each of two content-representations, build:

**Cell A — QAC-root-set** (Jaccard distance):
- coda vector = unique QAC roots in Q 16:120–123 (any morphological form)
- surah-rest vector = unique QAC roots in Q 16 \ {120–123}
- statistic = Jaccard similarity = |coda ∩ rest| / |coda ∪ rest|

**Cell B — orthographic-token Bag-of-Words** (cosine):
- TF vector over orthographic tokens (no-tashkeel)
- statistic = cosine similarity

**Per cell**: compute the same statistic for 10000 random 4-verse contiguous windows inside Q 16 (with windows-disjoint-from-coda when computing rest-vector); empirical p = fraction of null windows with statistic ≤ coda's statistic.

## 3. Acceptance / failure

- **CONFIRMED**: BOTH cells reject H0 at α_bon = 0.025.
- **DIRECTIONAL**: 1 cell rejects.
- **NULL**: Neither cell rejects; coda is structurally homogeneous with the surah body.
- **Pre-commit violation**: cosine(coda, rest) > corpus median of random windows (coda is MORE typical than random — pre-commit violation per PRE-REG-STANDARD-01).

## 4. Honest limits

- 4-verse windows include short ones; the coda is 4 short verses (~30 tokens). The null is matched on window-length (4 contiguous verses).
- Q 16 has 128 verses, so there are 125 candidate 4-verse contiguous windows; we use 10000 random-with-replacement draws.
- The Abraham coda might be heterogeneous in *some* representations but not others (likely passes Cell-A on roots — Abraham, ḥanīf, ummah are rare roots — but might fail Cell-B if function-words dominate).

## 5. Garden-of-forking-paths log

- **Why 4-verse not 5 or 3?** Q 16:120–123 = 4 verses, the canonical Abraham-coda boundary in al-Biqāʿī's munāsaba mapping (vol. 11). Locked to the classical extent.
- **Why two cells?** Roots vs tokens are the two project-canonical content-axes; passing both is the strict bar.
- **Why one-sided LOWER?** The classical claim is that the coda is *distinct* from the surah body; any direction of difference would be evidence, but the *predicted* direction is heterogeneity (= lower-similarity).

## 6. MW protections

- MW-1: representations + statistics locked.
- MW-2: 10000 random within-surah windows.
- MW-3: 2-cell battery is the model-variant control.
- MW-5: Q 12:4 in Q 12 (the dream-verse, classically a content-distinct prologue) — its 1-verse-window content-vector should also reject H0 on Cell-A (positive control). If it doesn't, instrument is broken.
- MW-6: within-surah random-window null.
- MW-7: 4-verse threshold and direction are pre-registered.

## 7. Files

- Pre-reg: `surahs/Q016-al-nahl/Q016-F-04-abraham-coda-block-test-prereg.md`
- Script: `surahs/Q016-al-nahl/scripts/Q016_F_04_abraham_coda.py`
- Output: `surahs/Q016-al-nahl/csv/Q016-F-04.json`

*PRE-REG LOCKED 2026-05-07.*
