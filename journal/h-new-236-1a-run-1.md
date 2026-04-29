# H-NEW-236.1a — Run 1 journal

**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg SHA-256**: `cf373a6a7b27847cfb0d9c4f6ccf42e934cf942e5e3b704505f55c65144183fe`  
**Parent**: H-NEW-236.1  
**Seed**: 20260419  
**Runtime**: ~2 minutes (1000 shared random permutations + 1000 top-30 sims + 1000 top-50 sims)

## Procedure

Executed per pre-reg:

1. Read `h-new-236-1a-extended-hinges-prereg.md`.
2. Reused the H-NEW-236.1 simulator structure rather than inventing a new generator.
3. Wrote `scripts/h_new_236_1a_extended_hinges.py` to derive the canonical Fisher-Rao consecutive-edge ranking directly from `csv/h-new-111.json`.
4. Locked two cells exactly as pre-registered:
   - Cell A = top-30 canonical consecutive edges
   - Cell B = top-50 canonical consecutive edges
5. Split each cell's hinge set into:
   - cross-block hinges enforced by block-boundary lock
   - within-block hinges enforced by chain-construction + 2-opt rejection
6. Reused H-NEW-236 / 236.1 observables:
   - O1 `L_path`
   - O2 `W_wrap`
   - O3 `Block-chi2`
   - O4 `L_tail_91_114`
7. Reused the same SA schedule as H-NEW-236.1:
   - `T_HOT = 0.05`
   - `T_COLD = 0.001`
   - `SA_ITERS = 200`
8. Shared MW-5 random baseline across both cells (1000 permutations).

## Mid-run issue and fix

First run crashed during Cell B analysis because one block's simulator
variance collapsed to zero and the Block-chi2 code divided by zero.

Cause:
- Under top-50, the ḥawāmīm block becomes fully hinge-locked, so
  `sim_std(L_hawamim) = 0.0`.

Fix:
- Added `safe_z(...)` to treat zero-variance blocks correctly:
  - `z = 0` if empirical equals the degenerate mean
  - `z = +/-inf` only if empirical differs from a degenerate mean

This changed only the reporting layer, not the simulator.

## Results summary

### Cell A — top-30

- `L_path` gap vs sim mean = **-0.000133**
- Residual closure vs H-NEW-236.1 = **100.01%**
- `L_path` inside sim 95% CI at **pct = 48.1**
- Overall = **3/4 pass**
- Failing observable = **Block-chi2**

Block decomposition:
- `L_tiwal` CLOSED
- `L_hawamim` CLOSED
- `L_mufassal_short` remains **z = +10.90**

### Cell B — top-50

- `L_path` gap vs sim mean = **+0.062169**
- Residual closure vs H-NEW-236.1 = **96.41%**
- `L_path` inside sim 95% CI at **pct = 59.1**
- Overall = **3/4 pass**
- Failing observable = **Block-chi2**

Block decomposition:
- `L_tiwal` CLOSED
- `L_hawamim` CLOSED EXACTLY (`std = 0`, empirical = mean)
- `L_mufassal_short` remains **z = +10.66**

## Key interpretation

The run changes the causal-generative state materially:

1. **The global path-length problem is solved.**
   Both top-30 and top-50 place the empirical mushaf inside the
   simulator distribution on `L_path`.

2. **The remaining causal miss is local, not global.**
   The only surviving failure is Block-chi2, driven almost entirely by
   `L_mufassal_short`.

3. **H-NEW-236.1's Reading A is partly vindicated.**
   Extending the hinge list does solve the unresolved ḥawāmīm region.
   It does not solve mufaṣṣal-short.

4. **Top-30 is the best global fit.**
   Top-50 does not improve the surviving miss because it still contains
   zero internal mufaṣṣal-short edges; instead it slightly overconstrains
   other regions.

## Garden-of-forking-paths log

1. The hinge sets were **derived from disk state**, not typed manually:
   canonical consecutive edges sorted by H-NEW-111 Fisher-Rao distance.
2. The only post-start code change was the zero-variance `safe_z` patch in
   the reporting layer after the first run exposed a deterministic divide-by-zero.
3. No pre-reg thresholds, hinge memberships, SA temperatures, or block
   definitions were changed after viewing results.
4. Shared random baseline across cells was retained because the null is
   cell-independent under the pre-regged design.

## Next move recommendation

The queue should now prioritise:

- **H-NEW-236.1b or equivalent**: targeted mufaṣṣal-short mechanism test

not another broad top-K sweep. The unresolved region is isolated enough
that a block-specific follow-up is now more informative than a larger
generic hinge expansion.

## Files produced

- `scripts/h_new_236_1a_extended_hinges.py`
- `findings/phase-b-hypotheses/csv/h-new-236-1a.json`
- `findings/phase-b-hypotheses/h-new-236-1a-extended-hinges.md`
- This journal
