---
finding_id: h-new-151
title: "Single-letter muqaṭṭāʿat sub-cluster under char-4-gram — replication of H-NEW-146 Cell C"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 1
bonferroni_family: h-new-151-single-letter-muq-char4gram
alpha_bon: 0.05
alpha_raw: 0.05
parent_findings: [h-new-146 (Cell C p=0.031 single-letter-muq sub-cluster), h-new-111b (char-4-gram FR D-matrix)]
rules_tuple: "(114 surahs Hafs-Kūfan; char-4-gram features per H-NEW-111b; Fisher-Rao arccos-Bhattacharyya; pairwise distance comparison)"
pre_reg_standard: PRE-REG-STANDARD-04
---

# [[h-new-151-single-letter-muq-char4gram|H-NEW-151]] — Single-letter muqaṭṭāʿat sub-cluster under char-4-gram

## Motivation

[[h-new-146-q50-qaf-hub|H-NEW-146]] Cell C found that the three single-letter muq surahs
(Q 38 ص, Q 50 ق, Q 68 ن) are mutually 14% closer in Fisher-Rao root
distance (0.850 within-singletons vs 0.992 Q-50-to-other-muq), with
permutation p = 0.031 — a near-miss at Bonferroni-3 in that study.

**Does the sub-cluster replicate under a DIFFERENT feature space
(char-4-gram per [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]])?**

Independent replication on a structurally different feature space would
strengthen the single-letter-muq sub-class claim.

## Hypothesis

**H_0**: Mean Fisher-Rao char-4-gram distance among the three pairs
{(38,50), (38,68), (50,68)} is NOT different from mean distance of
target_sid to other 28 muq surahs.

**H_1**: The mean within-singleton distance is significantly SHORTER
(the three single-letter-muq form a structural sub-cluster).

This is a single-test replication (Bonferroni k=1, α_bon=0.05).

## Method

### Data

- Fisher-Rao D-matrix from `findings/phase-b-hypotheses/csv/h-new-111b.json`
  (char-4-gram feature space, K=500 char-4-grams, Dirichlet α=0.5)
- Single-letter muq: Q 38, Q 50, Q 68
- Other 26 muq: Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29,
  30, 31, 32, 36, 40, 41, 42, 43, 44, 45, 46

### Test

1. Compute mean FR-char4gram distance over the 3 pairs
   {(38,50), (38,68), (50,68)}: `d_within`
2. Compute mean FR-char4gram distance over all pairs
   {singleton, non-singleton}: `d_between` (26 non-singletons × 3 singletons = 78 pairs)
3. Observed statistic: `delta = d_within - d_between`
4. **Null**: shuffle which 3 of 29 muq surahs are the "singletons",
   recompute delta. 10,000 permutations.
5. **1-sided lower-tail p**: fraction of shuffles with delta ≤ observed.

**PASS**: p < 0.05 (single-test; replication of [[h-new-146-q50-qaf-hub|H-NEW-146]] Cell C is a
focused 1-test, direction pre-committed = negative delta).

### Direction-lock

DIRECTION IS LOCKED NEGATIVE (within-singleton shorter than between).
This matches [[h-new-146-q50-qaf-hub|H-NEW-146]] Cell C observed direction. 1-sided test.

## Garden of forking paths

- **Char-4-gram feature space** chosen because it's the existing
  cross-feature replication space from [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] and was validated
  ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] confirmed Fisher-Rao mushaf-geodesic under
  char-4-gram, z=-11.41).
- **Alternatives rejected pre-result**: verse-length FR ([[h-new-111c-fisher-rao-verselen|H-NEW-111c]] —
  found to be feature-space-weak); Hellinger/JS/TV metrics (redundant
  with FR for ranking purposes, tested in [[h-new-131-q108-supernode|H-NEW-131]]); surface-word FR
  (not pre-computed as a corpus-wide D-matrix).
- **3-pair within vs 78-pair between**: the natural pairing for n=3
  vs n=26. Alternatives rejected: "any singleton to mean of
  non-singletons" (loses the symmetry).
- **1-sided with pre-locked direction**: matches [[h-new-146-q50-qaf-hub|H-NEW-146]] direction.
  Replication tests SHOULD be 1-sided when direction is already
  established by parent test.
- **10K permutations**: matches parent test.

## Pre-committed acceptance matrix

| Result | Verdict |
|---|---|
| p < 0.05 | REPLICATED — single-letter muq sub-cluster confirmed across feature spaces |
| 0.05 ≤ p < 0.10 | PARTIAL — consistent direction but weak |
| p ≥ 0.10 | NULL — char-4-gram does not replicate root sub-cluster |

## Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_151_single_letter_muq_char4gram.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-151.json`
- Findings: `findings/phase-b-hypotheses/h-new-151-single-letter-muq-char4gram.md`
- Journal: `journal/h-new-151-run-1.md`

Null and pass published with equal prominence. Runtime <1 min.
