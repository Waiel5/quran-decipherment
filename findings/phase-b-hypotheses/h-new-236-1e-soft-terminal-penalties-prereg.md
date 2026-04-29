# [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] - Soft terminal penalties on the top-50 scaffold: pre-registration

```yaml
finding_id: h-new-236-1e
title: "Soft terminal penalties on the top-50 hinge scaffold - can a weighted M_R/M_L preference recover L_mufassal_short without breaking L_path?"
parent: h-new-236-1b / h-new-236-1c
grandparent: h-new-236-1a -> h-new-236-1 -> h-new-236 -> cross-finding-020
date: 2026-04-18
specialist: autonomous (H-NEW-236.1e)
seed: 20260421
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + TOP-50-HINGE-BASELINE + SOFT-TERMINAL-PREFERENCE-PENALTY, seed 20260421)"
bonferroni_k: 3
alpha_family: 0.05
alpha_bon: 0.0166666667
cells:
  - cell_a_lambda_0p05
  - cell_b_lambda_0p10
  - cell_c_lambda_0p20
n_simulations: 1000
n_random_null: 1000
```

## 1. Motivation

[[h-new-236-1a-extended-hinges|H-NEW-236.1a]] established the top-50 hinge scaffold:

- `L_path` moved inside the simulator 95% CI
- `L_hawamim` closed
- the last clear miss remained `L_mufassal_short`

[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] then tested hard terminal mechanisms:

- hard `M_R` rhyme-class adjacency closed `L_mufassal_short`
- hard `M_L` liturgical-pair adjacency closed `L_mufassal_short`
- but both broke `L_path`

That leaves one clean follow-up:

> Maybe the terminal mechanism is real, but it is not a hard adjacency rule.
> Maybe it is a softer preference that nudges the optimizer toward the canonical
> terminal order without fully over-constraining the global path.

This pre-reg tests exactly that and nothing broader.

## 2. Hypothesis

**H0:** under the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 hinge scaffold, adding a soft terminal
preference penalty does not move empirical `L_mufassal_short` inside the
simulator 95% CI while also keeping empirical `L_path` inside the simulator
95% CI. The hard-cell parsimony conflict from [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] survives the
softening.

**H1:** at least one pre-committed penalty weight lambda does move empirical
`L_mufassal_short` inside the simulator 95% CI while keeping empirical
`L_path` inside the simulator 95% CI. If this happens, the terminal mechanism
is better modeled as a weighted preference than as a hard adjacency law.

Primary pass criterion per cell:

- empirical `L_mufassal_short` inside sim 95% CI
- empirical `L_path` inside sim 95% CI

Strict full pass criterion per cell:

- primary pass criterion satisfied
- plus `W_wrap` inside sim 95% CI
- plus `Block-chi2` inside sim 95% CI
- plus `L_tail_91_114` inside sim 95% CI

## 3. Locked preference set

The hard top-50 hinge scaffold is unchanged from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]].

The new ingredient is a soft penalty over the terminal preference set derived
from the [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] `M_R` and `M_L` cells.

### 3.1 Rhyme-class preference pairs

Use the same pre-committed rhyme-class assignment as [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]. The
canonical adjacent pairs in Q 78-114 whose two surahs share the same assigned
rhyme-class are:

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

Use the same four pre-committed liturgical pairs as [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]:

- `87-88`
- `93-94`
- `109-110`
- `113-114`

Each broken liturgical pair contributes weight `2`.

### 3.3 Overlap rule

If a pair appears in both sets, the weights are additive. Therefore:

- `87-88` has total weight `3`
- `93-94` has total weight `3`

Total weighted preference mass:

- rhyme contribution = `14`
- liturgical contribution = `8`
- total = `22`

## 4. Soft objective

Let:

- `L_path(tour)` be the ordinary path length under the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] Fisher-Rao matrix
- `B_pref(tour)` be the weighted count of broken terminal preference pairs

Then the simulated annealing objective is:

`E_lambda(tour) = L_path(tour) + lambda * B_pref(tour)`

Interpretation:

- `lambda = 0` recovers the top-50 baseline code path
- `lambda -> infinity` would behave like a hard adjacency regime
- this run uses a small locked lambda grid between those extremes

## 5. Locked lambda grid

The grid is fixed before execution:

- `cell_a_lambda_0p05`
- `cell_b_lambda_0p10`
- `cell_c_lambda_0p20`

Why this grid:

- max possible penalty mass is `22`
- at `lambda = 0.05`, full miss costs `1.10` FR units
- at `lambda = 0.10`, full miss costs `2.20` FR units
- at `lambda = 0.20`, full miss costs `4.40` FR units

This spans weak / medium / strong soft pressure while remaining clearly below
the hard-constraint limit.

No extra cells, no adaptive lambda search, no family split after seeing
results.

## 6. Generative procedure

Start from the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] / [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] simulator family.

Locked details:

1. Base scaffold: the top-50 canonical Fisher-Rao consecutive edges from
   [[h-new-236-1a-extended-hinges|H-NEW-236.1a]].
2. No new hard terminal hinges are added.
3. No sub-block restriction is added.
4. The only new term is the soft preference penalty defined in sections 3-4.
5. SA schedule unchanged:
   - `T_HOT = 0.05`
   - `T_COLD = 0.001`
   - `SA_ITERS = 200`
6. `N_sim = 1000` per lambda cell.
7. `N_random = 1000` shared random null.
8. Positive control:
   - run a `lambda = 0` top-50 cell through the same soft-penalty code path
   - it must reproduce the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 `L_mufassal_short z` within a
     broad tolerance of `|delta z| <= 2.0`

## 7. Observables

Primary target observables:

- `L_mufassal_short`
- `L_path`

Continuity observables:

- `W_wrap`
- `Block-chi2`
- `L_tail_91_114`

Additional soft-mechanism diagnostics:

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

- if any cell reaches `SOFT-CLOSES-STRICT-4OF4`, the soft mechanism strictly closes
- else if any cell reaches `SOFT-CLOSES-PRIMARY`, the soft mechanism closes the
  declared primary target but not the full equation
- else if all surviving signal is `SOFT-PARSIMONY-CONFLICT`, the hard-cell
  conflict survives softening
- else the soft mechanism is null

## 9. Bonferroni discipline

`k = 3` lambda cells, so:

- `alpha_bon = 0.05 / 3 = 0.0166666667`

The `lambda = 0` positive-control cell is not part of the inferential family.

## 10. Honest limits

1. This tests one specific softening only: weighted broken-pair count. It does
   not test richer prosodic penalties, late-tail-only penalties, or any
   learned objective.
2. The weights `1` and `2` are a modeling choice locked pre-run. They encode
   liturgical pairs as stronger than generic rhyme continuity, but not
   infinitely stronger.
3. The preference set is entirely inside Q 78-114. If the true remaining
   mechanism depends on a later-tail split, on nonlocal terminal spacing, or on
   interactions with Q 49-77, this run can miss it.
4. The soft penalty still acts through a path-level optimizer. If the terminal
   mechanism is not reducible to path optimization plus a local penalty, this
   instrument may fail even if a real terminal mechanism exists.
5. The lambda grid is intentionally small. If the true sweet spot lies between
   these values, this run will only bracket it.

## 11. Deliverables

- `scripts/h_new_236_1e_soft_terminal_penalties.py`
- `findings/phase-b-hypotheses/h-new-236-1e-soft-terminal-penalties.md`
- `findings/phase-b-hypotheses/csv/h-new-236-1e.json`
- `journal/h-new-236-1e-run-1.md`

Pre-reg locked 2026-04-18. Execution follows.
