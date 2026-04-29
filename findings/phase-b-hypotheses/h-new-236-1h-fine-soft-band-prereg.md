# [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] - Fine soft interpolation inside the [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] near-miss band: pre-registration

```yaml
finding_id: h-new-236-1h
title: "Fine soft interpolation inside the H-NEW-236.1e near-miss band - is there a narrow soft-only sweet spot between lambda 0.05 and 0.10?"
parent: h-new-236-1e / h-new-236-1d
grandparent: h-new-236-1b / h-new-236-1c -> h-new-236-1a -> h-new-236-1 -> h-new-236 -> cross-finding-020
date: 2026-04-18
specialist: autonomous (H-NEW-236.1h)
seed: 20260421
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + TOP-50-HINGE-BASELINE + SOFT-TERMINAL-PREFERENCE-PENALTY, seed 20260421)"
bonferroni_k: 4
alpha_family: 0.05
alpha_bon: 0.0125
cells:
  - cell_a_lambda_0p06
  - cell_b_lambda_0p07
  - cell_c_lambda_0p08
  - cell_d_lambda_0p09
n_simulations: 1000
n_random_null: 1000
```

## 1. Motivation

[[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] tested the same soft terminal preference family now under study
here and found a sharp boundary:

- `lambda = 0.05` kept empirical `L_path` and `L_tail_91_114` inside the
  simulator family, but left `L_mufassal_short` just outside high
  (`z = +2.78`, percentile `99.9`)
- `lambda = 0.10` moved empirical `L_mufassal_short` inside, but broke both
  `L_path` and `L_tail_91_114`

That leaves an honest narrow next question:

> Is there a real soft-only sweet spot hidden between `0.05` and `0.10`, or is
> the apparent near-miss just the boundary of the same old parsimony-conflict
> regime?

[[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] increases the value of this question because it tightened the hard
hinge bracket to `(95, 100]`, making any lower-cost soft rescue especially
important if it exists at all.

## 2. Hypothesis

**H0:** on a locked fine lambda grid fully inside `(0.05, 0.10)`, no cell
achieves even the primary closure target. The soft route remains bounded by
`SOFT-NULL` on the weak side and `SOFT-PARSIMONY-CONFLICT` on the strong side.

**H1:** at least one pre-committed lambda inside the narrow band moves empirical
`L_mufassal_short` inside the simulator 95% CI while keeping empirical `L_path`
inside the simulator 95% CI. If this happens, [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] missed a genuine
soft-only sweet spot.

Primary pass criterion per cell:

- empirical `L_mufassal_short` inside sim 95% CI
- empirical `L_path` inside sim 95% CI

Strict full pass criterion per cell:

- primary pass criterion satisfied
- plus `W_wrap` inside sim 95% CI
- plus `Block-chi2` inside sim 95% CI
- plus `L_tail_91_114` inside sim 95% CI

## 3. Locked preference family

This run reuses the exact [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] soft penalty family with no expansion of
the preference sets.

### 3.1 Rhyme-class preference pairs

Canonical adjacent pairs in Q 78-114 whose two surahs share the same assigned
rhyme-class:

- `80-81`
- `81-82`
- `84-85`
- `85-86`
- `87-88`
- `88-89`
- `91-92`
- `92-93`
- `93-94`
- `94-95`
- `95-96`
- `104-105`
- `105-106`
- `106-107`

Each broken rhyme pair contributes weight `1`.

### 3.2 Liturgical preference pairs

The same four [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] / [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] liturgical pairs are retained:

- `87-88`
- `93-94`
- `109-110`
- `113-114`

Each broken liturgical pair contributes weight `2`.

### 3.3 Overlap rule

As in [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]], weights are additive on overlap:

- `87-88` has total weight `3`
- `93-94` has total weight `3`

Total weighted preference mass remains `22`.

## 4. Soft objective

Let:

- `L_path(tour)` be the ordinary path length under the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] Fisher-Rao matrix
- `B_pref(tour)` be the weighted count of broken terminal preference pairs

Then the SA objective is unchanged:

`E_lambda(tour) = L_path(tour) + lambda * B_pref(tour)`

This run changes only the lambda resolution.

## 5. Locked fine lambda grid

The inferential grid is fixed before execution:

- `cell_a_lambda_0p06`
- `cell_b_lambda_0p07`
- `cell_c_lambda_0p08`
- `cell_d_lambda_0p09`

Why this grid:

- it lies strictly inside the [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] gap between `0.05` and `0.10`
- it samples the whole interval at uniform `0.01` increments
- it is the smallest obvious locked family that can falsify the "narrow sweet
  spot" story without turning this into an adaptive search

No extra cells, no interpolation after seeing results, no preference-set
expansion.

## 6. Generative procedure

Everything is inherited unchanged from [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] except the lambda grid.

Locked details:

1. Base scaffold: the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 canonical Fisher-Rao consecutive edges.
2. No new hard terminal hinges are added.
3. No new soft preference pairs are added.
4. SA schedule unchanged:
   - `T_HOT = 0.05`
   - `T_COLD = 0.001`
   - `SA_ITERS = 200`
5. `N_sim = 1000` per lambda cell.
6. `N_random = 1000` shared random null.
7. Positive control:
   - run a `lambda = 0` top-50 cell through the same soft-code path
   - it must reproduce the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 `L_mufassal_short z` within
     `|delta z| <= 2.0`

## 7. Observables

Primary target observables:

- `L_mufassal_short`
- `L_path`

Continuity observables:

- `W_wrap`
- `Block-chi2`
- `L_tail_91_114`

Additional diagnostics:

- weighted preference satisfaction
- rhyme-pair satisfaction count
- liturgical-pair satisfaction count

## 8. Interpretation rules

Per cell:

| Outcome | Verdict |
|---|---|
| `L_mufassal_short` inside and `L_path` inside and full 4/4 pass | `SOFT-CLOSES-STRICT-4OF4` |
| `L_mufassal_short` inside and `L_path` inside but not full 4/4 | `SOFT-CLOSES-PRIMARY` |
| `L_mufassal_short` inside but `L_path` outside | `SOFT-PARSIMONY-CONFLICT` |
| `L_mufassal_short` outside but `L_path` inside | `SOFT-NULL` |
| both outside | `SOFT-BROKEN` |

Overall decision:

- if any cell reaches `SOFT-CLOSES-STRICT-4OF4`, the fine-band sweep finds a
  genuine soft-only strict closure
- else if any cell reaches `SOFT-CLOSES-PRIMARY`, the fine-band sweep finds a
  soft-only primary closure
- else if the surviving signal remains a mixture of `SOFT-NULL` and
  `SOFT-PARSIMONY-CONFLICT`, the near-miss interpretation survives but no sweet
  spot lands
- else the fine-band sweep is null

## 9. Bonferroni discipline

`k = 4` lambda cells, so:

- `alpha_bon = 0.05 / 4 = 0.0125`

The `lambda = 0` positive-control cell is not part of the inferential family.

## 10. Honest limits

1. This is not a new mechanism family. It is a resolution increase inside the
   exact [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] family.
2. A negative result here does not prove that no softer terminal mechanism
   exists. It only rules against this specific weighted rhyme/liturgical family
   on this narrow band.
3. A positive result would still not solve hard-hinge parsimony by itself. It
   would only show that the [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] coarse grid skipped a viable lambda.
4. Because [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] points to a late-tail hard tranche containing edges
   outside the soft preference family, this sweep may still fail even if the
   true terminal mechanism is real.

## 11. Deliverables

- `scripts/h_new_236_1h_fine_soft_band.py`
- `findings/phase-b-hypotheses/h-new-236-1h-fine-soft-band.md`
- `findings/phase-b-hypotheses/csv/h-new-236-1h.json`
- `journal/h-new-236-1h-run-1.md`

Pre-reg locked 2026-04-18. Execution follows.
