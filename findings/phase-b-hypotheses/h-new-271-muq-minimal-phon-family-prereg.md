---
id: H-NEW-271
title: Minimal phonological family test for the muqaṭṭaʿāt cluster ceiling
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-18
agent: codex
parent_1: H-NEW-165
parent_2: H-NEW-165.2
open_question: OQ-1
seed: 20260419
n_perm: 1000
bonferroni_family: h-new-271-muq-minimal-phon-family
bonferroni_k: 2
alpha: 0.05
alpha_bon: 0.025
rules_tuple: "(canonical 29 muq surahs; H-NEW-165 locked baseline codebook; duplicate binary means/fractions collapsed for single-axis search; RF LOOCV primary; maxT permutation within each arm; seed 20260419)"
direction_primary: "determine whether the H-NEW-165 cluster ceiling can be recovered by any single phonological axis, with or without inherited letter_count"
---

# [[h-new-271-muq-minimal-phon-family|H-NEW-271]] — Minimal phonological family test for the muqaṭṭaʿāt cluster ceiling

## Question

`[[h-new-165-phonological-predictor|H-NEW-165]]` and `[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]` established that the locked phonological
codebook reaches the muq cluster ceiling:

- RF LOOCV top-1 = `19 / 29 = 0.6552`
- all 19 multi-member surahs are classified correctly
- all 10 singleton sets remain LOOCV-structurally unreachable
- the signal is codebook-robust under the bounded `[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]` perturbation family

What remains open is **parsimony**:

> Is the 15-dimensional [[h-new-165-phonological-predictor|H-NEW-165]] codebook materially over-specified, with one
> phonological axis already sufficient, or is a genuinely multi-feature
> combination needed to recover the ceiling?

This finding is a tightly bounded follow-up. It does **not** invent new
features. It asks how much of the already-validated [[h-new-165-phonological-predictor|H-NEW-165]] signal survives
under exact subset restriction.

## Locked feature universe

### Parent full codebook

The parent [[h-new-165-phonological-predictor|H-NEW-165]] feature matrix has 15 columns:

1. `mean_makhraj`
2. `mean_voice`
3. `mean_manner`
4. `mean_emphatic`
5. `mean_pharyngeal`
6. `mean_sonorant`
7. `mean_continuant`
8. `mean_idhlaq`
9. `mean_vowel_carrier`
10. `letter_count`
11. `frac_emphatic`
12. `frac_pharyngeal`
13. `frac_sonorant`
14. `frac_idhlaq`
15. `has_qalqala`

### Duplicate-collapse rule

Four parent columns are exact algebraic duplicates:

- `frac_emphatic == mean_emphatic`
- `frac_pharyngeal == mean_pharyngeal`
- `frac_sonorant == mean_sonorant`
- `frac_idhlaq == mean_idhlaq`

For subset search, these duplicates are **collapsed** so that the search space
counts distinct phonological axes rather than duplicated columns that would only
change RF split opportunity. This is locked before execution.

### Search pool

The deduplicated phonological pool is therefore fixed at 10 axes:

1. `mean_makhraj`
2. `mean_voice`
3. `mean_manner`
4. `mean_emphatic`
5. `mean_pharyngeal`
6. `mean_sonorant`
7. `mean_continuant`
8. `mean_idhlaq`
9. `mean_vowel_carrier`
10. `has_qalqala`

`letter_count` is treated separately as a non-phonological inherited scaffold.
It is **not** counted as a phonological feature in any minimal-family claim.

## Two locked inferential arms

### Arm A — phon-only single-axis models

Test exactly 10 models:

- one model per phonological axis
- no `letter_count`

Purpose:

- strongest parsimony test
- answers whether phonology alone can recover the [[h-new-165-phonological-predictor|H-NEW-165]] ceiling

### Arm B — `letter_count` + one phonological axis

Test all models of the form:

`letter_count + {one phonological axis}`

Purpose:

- asks whether the parent result can be compressed to the inherited
  [[h-new-165-phonological-predictor|H-NEW-165]] scaffold plus exactly one phonological axis
- if this arm succeeds at smaller size than Arm A, the result is still
  parsimonious, but only **conditional on letter-count information**

## Positive controls and descriptive anchors

These are locked and reported before interpretation.

### PC1 — parent reproduction

The exact [[h-new-165-phonological-predictor|H-NEW-165]] full 15-column model must reproduce:

- RF LOOCV top-1 = `19 / 29 = 0.6552`

If not, report `NULL-BROKEN-BASELINE`.

### PC2 — MW-5 inherited sanity

`cheat_surah_id` alone must yield RF LOOCV top-1 `>= 0.45`, matching the
[[h-new-165-phonological-predictor|H-NEW-165]] inherited sanity window.

If not, report `NULL-BROKEN-MW5`.

## Locked primary statistic

Primary classifier: `RandomForestClassifier(n_estimators=200, random_state=20260419)`,
matching the parent [[h-new-165-phonological-predictor|H-NEW-165]] model family.

Primary performance statistic for every subset:

- RF LOOCV top-1 accuracy on the 29 canonical muq surahs

### Ceiling-recovery definition

A subset is said to **recover the muq cluster ceiling** iff:

1. RF LOOCV top-1 = `19 / 29 = 0.655172...`
2. recall = `1.0` for each of the four multi-member classes:
   `ALM`, `ALR`, `HM`, `TSM`

Condition (2) prevents a misleading `19 / 29` that comes from some singleton
hit cancelling out a multi-member miss.

## Locked search protocol

For each arm separately:

1. Evaluate all 10 fixed candidate models in that arm.
2. Record the best top-1 value and any ceiling-recovering winners.
3. Run an arm-wise maxT permutation test over the same 10 fixed candidates.

This maxT construction corrects for the within-arm search over candidate
identity. No broader subset-size search is allowed in this first pass.

## Null model

Permutation null:

- shuffle the 29 class labels
- rerun the exact RF LOOCV pipeline
- compute the **maximum** top-1 accuracy attained by any tested subset in the
  relevant arm family
- repeat `N_PERM = 1000`

Arm-wise p-value:

`p_arm = (1 + # perms with max_top1 >= observed_max_top1) / (N_PERM + 1)`

## Multiple-testing discipline

There are exactly **2 inferential arms**:

1. phon-only
2. `letter_count` + phonological

Bonferroni:

- `alpha_bon = 0.025` per arm

The duplicate-collapse check and the positive controls are **not** inferential
cells in this family.

## Decision rules

### Arm-level pass

An arm is treated as inferentially positive iff:

1. at least one subset in the arm recovers the ceiling, and
2. the arm-wise maxT permutation p-value is `< 0.025`

### Global interpretation

- **SINGLE-PHON-FEATURE-SUFFICIENT**:
  Arm A passes
- **SINGLE-AUGMENT-SUFFICIENT**:
  Arm A fails, Arm B passes
- **MULTI-FEATURE-REQUIRED**:
  neither arm passes

## Expected outcome

Honest expectation before run:

- a genuinely single phonological feature is **unlikely** to recover the full
  ceiling on its own
- `letter_count + one phonological axis` is possible but still not the default
  expectation

The main point of `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]` is not to map the whole subset frontier. It is to
answer the first bounded question cleanly:

> can one axis do it, or is a combination already necessary?

## Files

- Pre-reg: this file
- Script: `scripts/h_new_271_muq_minimal_phon_family.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271.json`
- Findings: `findings/phase-b-hypotheses/h-new-271-muq-minimal-phon-family.md`
- Journal: `journal/h-new-271-run-1.md`
