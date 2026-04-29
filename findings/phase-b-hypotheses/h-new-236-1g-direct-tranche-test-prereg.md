# [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] Pre-Registration - Direct isolated-tranche test after [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] / [[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]]

**Finding ID**: [[h-new-236-1g-direct-tranche-test|h-new-236-1g]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Parents**: [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] / [[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]]  
**Grandparent context**: [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] / [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] / [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] / [[h-new-236-generative-simulator|H-NEW-236]] / [[cross-finding-020-the-complete-equation|cross-finding-020]]

## 1. Question

[[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] tightened the hard-hinge parsimony bracket to `(95, 100]`
and isolated a decisive five-edge tranche between the last failing cell
and the first strict pass:

- `(92,93)`
- `(99,100)`
- `(100,101)`
- `(101,102)`
- `(109,110)`

[[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]] then tested a broader cumulative hard-prefix late-tail
repair on top of [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A and found no repair.

The narrow question for [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] is therefore:

> does the exact decisive [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] tranche, or either of its two
> natural subcomponents, repair both global observables when tested
> directly rather than as part of the failed cumulative hard-prefix
> design?

The project answer must be explicit even if the result is still no.

## 2. Locked inherited inputs

### 2.1 Bases

- `Base_A = [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A`
  (`cell_a_top50_plus_j30_top5`)
- `Base_D = [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 baseline`
  (`baseline_h2361a_top50`)

### 2.2 Exact decisive tranche from [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]]

- `T_exact = {(92,93), (99,100), (100,101), (101,102), (109,110)}`

This set must be verified against the [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] `K=95` and `K=100`
cells before simulation. The required check is set equality with:

- `set(K100) - set(K95)`

### 2.3 Pre-locked subcomponents

- `T_core = {(99,100), (100,101), (101,102)}`
- `T_overlap = {(92,93), (109,110)}`

These are fixed before running and may not be changed after results are
seen.

## 3. Locked cells

### Positive control

- `mw5_positive_control_cell_a_base`
- design: `Base_A` only
- purpose: re-run [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A under a fresh seed to verify the
  inherited local-closed / global-overcorrected signature

The positive control passes only if both conditions hold:

1. Same qualitative signature as [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A:
   - `L_mufassal_short` inside simulator 95% CI
   - `Block-chi2` inside simulator 95% CI
   - `L_path` outside simulator 95% CI on the low side
   - `L_tail_91_114` outside simulator 95% CI on the low side
2. Drift thresholds versus parent sim means remain within:
   - `|Delta L_path sim_mean| <= 0.50`
   - `|Delta L_tail_91_114 sim_mean| <= 0.75`
   - `|Delta L_mufassal_short sim_mean| <= 0.50`

### Main cells

1. `cell_a_base_plus_exact_tranche`
   - design: `Base_A + T_exact`
2. `cell_b_base_plus_core_only`
   - design: `Base_A + T_core`
3. `cell_c_base_plus_overlap_pair_only`
   - design: `Base_A + T_overlap`
4. `cell_d_top50_plus_exact_tranche`
   - design: `Base_D + T_exact`

No additional cells may be added in this branch.

## 4. Locked simulator conventions

Reuse the [[h-new-236-generative-simulator|H-NEW-236]] family conventions exactly:

- no-tashkeel
- 114 surahs, Hafs-Kufan order
- basmala counted only in surah 1
- QAC-STEM root tokens
- Fisher-Rao arccos-Bhattacharyya distances per [[h-new-111-fisher-rao-mushaf|H-NEW-111]]
- stochastic 2-opt within classical blocks
- Q1 lock
- length stratification
- M2-muq constraints
- hard hinge preservation for each cell's locked hinge set

Locked run parameters:

- `seed = 20260424`
- `n_sim = 1000`
- `n_random = 1000`
- `sa_iters = 200`

## 5. Locked observables

Report the same observables as the parent family:

- `L_path`
- `W_wrap`
- `L_tiwal`
- `L_hawamim`
- `L_mufassal_short`
- `L_tail_91_114`
- `Block-chi2`

## 6. Locked decision rules

### 6.1 Primary direct-repair criterion

A main cell counts as a direct repair only if all four hold:

- `L_path` inside simulator 95% CI
- `L_tail_91_114` inside simulator 95% CI
- `L_mufassal_short` inside simulator 95% CI
- `Block-chi2` inside simulator 95% CI

### 6.2 Family strict 4/4 criterion

Also record the family strict criterion:

- `L_path` inside
- `W_wrap` inside
- `Block-chi2` inside
- `L_tail_91_114` inside

### 6.3 Multiple-testing discipline

Main family size for inferential interpretation:

- `k = 4`
- `alpha_bon = 0.05 / 4 = 0.0125`

The positive control is required for instrument validity but is not one
of the four inferential cells.

## 7. Planned interpretations

Before running, the interpretations are locked as follows:

1. If `cell_a` passes, the exact [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] decisive tranche works as
   a direct repair on top of the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A base.
2. If `cell_b` passes while `cell_c` fails, the structurally
   independent core carries the repair signal.
3. If `cell_c` passes while `cell_b` fails, the overlap pair carries the
   repair signal.
4. If `cell_d` passes while `cell_a` fails, the tranche works on the
   top-50 base but interacts badly with the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Juz30 top-5
   additions.
5. If none of `cell_a` through `cell_d` passes after a valid positive
   control, the answer is still no: the decisive tranche does not repair
   the global overcorrection when tested directly in the hard-adjacency
   form locked here.

## 8. Planned outputs

- script:
  `scripts/h_new_236_1g_direct_tranche_test.py`
- JSON:
  `findings/phase-b-hypotheses/csv/h-new-236-1g.json`
- finding:
  `findings/phase-b-hypotheses/h-new-236-1g-direct-tranche-test.md`
- journal:
  `journal/h-new-236-1g-run-1.md`
