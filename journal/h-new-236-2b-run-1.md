# h-new-236-2b-run-1

**Date**: `2026-04-19`  
**Task**: land `H-NEW-236.2b`, the held-out predictability test for the extra scaffold edges  
**Outcome**: **PASS-DIRECTED (weak)**  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-2b-extra-scaffold-predictability-prereg.md`  
**Pre-reg SHA-256**: `b6bfd54250cfb42d37f53c14f00a6b9b7d59e8f89e0b1dcce3d53c3d5516a7cf`

## Scope discipline

Only the five owned files were created:

- `scripts/h_new_236_2b_extra_scaffold_predictability.py`
- `findings/phase-b-hypotheses/h-new-236-2b-extra-scaffold-predictability-prereg.md`
- `findings/phase-b-hypotheses/h-new-236-2b-extra-scaffold-predictability.md`
- `findings/phase-b-hypotheses/csv/h-new-236-2b.json`
- `journal/h-new-236-2b-run-1.md`

No continuity files were edited.

## Locked design executed

- universe: all `113` canonical consecutive edges
- positives: `P = H100 \ H50` imported from `h-new-236-1d.json`
- negatives: `N = E \ H100`
- analysis pool: `63` edges = `50` positive + `13` negative
- features: 9 locked binaries from `h_new_130_fisher_rao_residuals.py` and
  `h_new_236_1b_mufassal_terminal.py`
- model: L2 logistic, `C=1.0`, `class_weight='balanced'`,
  `solver='newton-cholesky'`
- validation: LOOCV
- null: `10,000` label permutations
- descriptive positive control: H-NEW-130 top-15 jump problem on all `113`
  canonical edges with the same feature family and model

## Command run

```bash
python3 scripts/h_new_236_2b_extra_scaffold_predictability.py
```

The run completed cleanly on the first production execution.

## Main numbers

### Primary analysis

| Metric | Value |
|---|---:|
| `AUC_LOOCV` | **0.647692** |
| Accuracy at 0.5 | 0.619048 |
| Balanced accuracy at 0.5 | 0.731538 |
| `p_perm` | **0.030197** |
| `ge_count` | `301 / 10000` |
| Null mean AUC | 0.430961 |
| Null q95 | 0.623077 |
| Null q99 | 0.692308 |

Locked verdict: **PASS-DIRECTED (weak)**.

### Descriptive positive control

| Metric | Value |
|---|---:|
| `AUC_LOOCV` | **0.900680** |
| Accuracy at 0.5 | 0.734513 |
| Balanced accuracy at 0.5 | 0.736395 |

Interpretation:

- the feature family is clearly strong on the earlier H-NEW-130 jump problem
- it only weakly generalizes to the extra-scaffold problem

## What drove the result

The main pool is structurally awkward in a very specific way:

- all `13` negatives are inside `mufassal_short`
- only `23 / 50` positives are there

So `within_mufassal_short` becomes the dominant coefficient:

- `within_mufassal_short = -2.222671`

Positive coefficients still show real boundary-coded signal:

- `classical_length_boundary = +0.418034`
- `muq_presence_change = +0.377077`
- `phase_transition = +0.257314`
- `muq_letterset_change = +0.141846`
- `period_transition = +0.107676`

Net result:

- earlier boundary-shaped additions are recovered reasonably well
- late terminal additions are mostly missed

## Error pattern worth retaining

At threshold `0.5`:

- false positives: only `Q110 -> Q111`
- false negatives: `23`

Those false negatives are mostly the late mufaṣṣal-short tranche:

- `Q78 -> Q79` through `Q92 -> Q93`
- `Q95 -> Q96` through `Q101 -> Q102`
- `Q109 -> Q110`

This is the cleanest explanation for why the AUC is above null but modest.

## Bottom-line interpretation

The extra scaffold is **not random** under the locked feature family, but it is
also **not strongly compressible** by that family.

The same 9 features that very strongly recover H-NEW-130's top-15 jump regime
only weakly recover the `top50 -> top100` increment. That suggests the extra
scaffold contains some classical-boundary regularity while still depending
heavily on late internal adjacency structure that these coarse binaries do not
capture well.
