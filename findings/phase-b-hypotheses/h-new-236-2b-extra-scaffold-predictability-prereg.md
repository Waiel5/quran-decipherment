# [[h-new-236-2b-extra-scaffold-predictability|H-NEW-236.2b]] - Held-out predictability of the extra scaffold edges: pre-registration

```yaml
finding_id: h-new-236-2b
title: "Held-out predictability of the extra scaffold edges under locked boundary features"
parent: h-new-236-1d
related:
  - h-new-130
  - h-new-236-1b
  - h-new-236-1d
grandparent: h-new-236-1b -> h-new-236-1a -> h-new-236-1 -> h-new-236
date: 2026-04-19
specialist: autonomous (H-NEW-236.2b)
seed: 20260419
rules_tuple: "(113 canonical consecutive edges; H100 and H50 imported directly from h-new-236-1d.json; positive=P=H100\\H50; negative=N=E\\H100; 9 locked binary features from H-NEW-130 / H-NEW-236.1b; LOOCV logistic C=1.0 class_weight=balanced solver=newton-cholesky; 10000 label permutations; descriptive H-NEW-130 top-15 positive control)"
primary_statistic: "AUC_LOOCV on the 63-edge analysis pool"
n_perm: 10000
alpha_primary: 0.05
model:
  family: logistic_regression
  penalty: l2
  C: 1.0
  class_weight: balanced
  solver: newton-cholesky
  max_iter: 1000
validation: LOOCV
```

## 1. Motivation

[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] and [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] established that the landed `M_H` scaffold
reaches strict closure by the time the canonical Fisher-Rao hinge family is
extended from `H50` to `H100`, and that the smallest tested strict pass is
`K = 100`.

That resolves the causal-generative closure question at the simulator layer.
It does **not** yet answer a sharper discriminative question:

> Are the *extra* scaffold edges that must be added beyond top-50
> (`H100 \ H50`) themselves recoverable from a small locked family of
> classical-boundary features under held-out prediction, or are they mostly
> unstructured residue once the earlier top-50 scaffold is removed?

This run isolates exactly that branch.

## 2. Locked universe and labels

Universe:

- all `113` canonical consecutive edges `E = {(Q1,Q2), (Q2,Q3), ..., (Q113,Q114)}`

Imported edge sets:

- `H50` = the top-50 hinge family from
  `findings/phase-b-hypotheses/csv/h-new-236-1d.json`
- `H100` = the top-100 hinge family from the same locked file

Locked labels:

- **Positive set `P`** = `H100 \ H50`
- **Negative set `N`** = `E \ H100`

Therefore:

- `|P| = 50`
- `|N| = 13`
- analysis pool size = `63`

The middle `H50` tranche is deliberately excluded. This is the exact
held-out contrast of interest:

> which canonical edges had to be added beyond the already-landed top-50
> scaffold, as opposed to remaining fully outside the top-100 scaffold?

## 3. Locked feature family

All features are binary and must be sourced cleanly from existing on-disk
builders or landed constants. No freehand relabeling is permitted.

### F1 `classical_length_boundary`

Definition:

- `1` iff the edge slot `i -> i+1` is one of the locked classical length
  boundaries in `h_new_130_fisher_rao_residuals.py` `LENGTH_BOUNDARIES`

Source:

- `scripts/h_new_130_fisher_rao_residuals.py`

### F2 `period_transition`

Definition:

- `1` iff the two adjacent surahs have different `period` labels

Source:

- `scripts/h_new_130_fisher_rao_residuals.py` `load_period_phase()`
- underlying file `data/revelation-order.csv`

### F3 `phase_transition`

Definition:

- `1` iff the two adjacent surahs have different `noldeke_phase` labels

Source:

- same as F2

### F4 `muq_presence_change`

Definition:

- `1` iff exactly one of the two adjacent surahs is in the locked muqaṭṭaʿāt set

Source:

- `scripts/h_new_130_fisher_rao_residuals.py` `MUQ_SET`

### F5 `muq_letterset_change`

Definition:

- `1` iff both adjacent surahs are muqaṭṭaʿāt-opened and their locked
  muq-letter-set labels differ

Source:

- `scripts/h_new_130_fisher_rao_residuals.py` `MUQ_LETTER`

### F6 `within_hawamim`

Definition:

- `1` iff both surahs lie inside the locked `hawamim` block

Source:

- `scripts/h_new_236_1b_mufassal_terminal.py` `BLOCKS_1INDEXED["hawamim"]`

### F7 `within_mufassal_short`

Definition:

- `1` iff both surahs lie inside the locked `mufassal_short` block

Source:

- `scripts/h_new_236_1b_mufassal_terminal.py` `BLOCKS_1INDEXED["mufassal_short"]`

### F8 `same_rhyme_class`

Definition:

- `1` iff both surahs share the same locked mufaṣṣal-short rhyme class

Source:

- `scripts/h_new_236_1b_mufassal_terminal.py`
  `RHYME_CLASSES_MUFASSAL_SHORT`

Operational note:

- outside that locked rhyme map, this feature is `0`

### F9 `liturgical_pair`

Definition:

- `1` iff the edge is one of the four locked liturgical pairs

Source:

- `scripts/h_new_236_1b_mufassal_terminal.py` `M_L_PAIRS_1INDEXED`

## 4. Locked model and validation

Primary model:

- scikit-learn `LogisticRegression`
- `penalty = L2`
- `C = 1.0`
- `class_weight = "balanced"`
- `solver = "newton-cholesky"` (deterministic)
- `max_iter = 1000`

Preprocessing:

- none beyond binary feature matrix assembly
- no scaling, no feature selection, no interaction terms

Validation:

- leave-one-out cross-validation on the locked 63-edge pool

Primary statistic:

- `AUC_LOOCV` computed from the 63 held-out probabilities

## 5. Permutation null

Primary inferential null:

- shuffle the 63 labels `10,000` times
- each shuffle preserves the observed class count `50 / 13`
- rerun the exact same LOOCV pipeline each time
- compute `AUC_LOOCV` each time

Primary p-value:

- `p = (1 + count(null_auc >= observed_auc)) / 10001`

## 6. Positive control (descriptive only)

A descriptive only calibration branch will be run on the already-landed
[[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 jump problem:

- universe = all 113 canonical consecutive edges
- positives = [[h-new-130-fisher-rao-residuals|H-NEW-130]] `top15_largest_jumps`
- negatives = the remaining 98 canonical consecutive edges
- same 9 locked binary features
- same logistic model
- same LOOCV pipeline

This positive control does **not** consume inferential alpha in this run.
Its role is descriptive:

> do these nine features clearly recover the earlier [[h-new-130-fisher-rao-residuals|H-NEW-130]] jump problem
> even if they fail to recover the extra-scaffold tranche?

## 7. Locked interpretation rules

Primary inferential decision:

- `PASS-DIRECTED` iff `p_perm < 0.05`
- `NULL` otherwise

Descriptive AUC strength bands:

- `AUC >= 0.80` -> `strong`
- `0.65 <= AUC < 0.80` -> `moderate`
- `0.55 <= AUC < 0.65` -> `weak`
- `AUC < 0.55` -> `near-null`

Result wording combines both:

- `PASS-DIRECTED (strong/moderate/weak)`
- or `NULL (strong/moderate/weak descriptive lift only)`

This avoids pre-committing a second arbitrary effect-size gate beyond the
permutation test while still forcing an honest descriptive read.

## 8. Honest limits

1. The analysis pool is intentionally asymmetric (`50 / 13`). Balanced class
   weighting handles threshold bias, but variance is still higher on the
   minority negative class.
2. Excluding `H50` is conceptually correct for the question asked, but it also
   means this is **not** a classifier over all 113 canonical edges.
3. Several features are inherited from overlapping prior mechanisms
   (`same_rhyme_class`, `liturgical_pair`, `within_mufassal_short`), so
   coefficients should be read descriptively rather than as independent causal
   claims.
4. Some features are rare or even absent in the negative class by
   construction. Regularized logistic regression can still fit them, but their
   coefficients may be unstable in magnitude even when their sign is stable.
5. LOOCV on 63 samples is small-N. The permutation null is the primary guard
   against over-reading a moderate AUC.

## 9. Files

- Pre-reg: this file
- Script: `scripts/h_new_236_2b_extra_scaffold_predictability.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-2b.json`
- Finding: `findings/phase-b-hypotheses/h-new-236-2b-extra-scaffold-predictability.md`
- Journal: `journal/h-new-236-2b-run-1.md`
