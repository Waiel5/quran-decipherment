---
finding_id: h-new-271-1
run: 1
date: 2026-04-19
specialist: codex
seed: 20260419
verdict: MULTI-DIM-REQUIRED-AT-SINGLETONS
---

# H-NEW-271-1 run 1 journal

## Task

Follow up on H-NEW-271 by collapsing the locked codebook to the single
`mean_manner` axis and testing whether the singleton-layer nearest-centroid
structure from H-NEW-232 survives.

## Timeline

1. Wrote the preregistered follow-up file `h-new-271-1-manner-singleton-prereg.md`
   with the 6/10 nontrivial bar and the 8/10 H-NEW-232 comparability bar.
2. Wrote `scripts/h_new_271_1_manner_singleton.py` so it loads the locked
   H-NEW-271 codebook directly and collapses the singleton geometry to the
   single `mean_manner` axis.
3. Ran the script.
4. Observed the locked outputs:
   - singleton matches = `5 / 10`
   - null mean = `3.758`
   - permutation tail = `p_perm = 0.41` (`410 / 1000`)
   - verdict = `MULTI-DIM-REQUIRED-AT-SINGLETONS`
5. Wrote the findings markdown and JSON artifact.

## Result

The 1-D collapse preserves a coarse residual TSM pull, but it does not recover
the H-NEW-232 singleton-layer topology. Nearest multi-member surah and nearest
centroid agree for all 10 singletons, so the loss is not due to centroid vs
neighbor ambiguity. The loss is the collapse itself.

## Exact comparison to H-NEW-232

- H-NEW-232: `8 / 10`, `p = 0.02498`
- H-NEW-271-1: `5 / 10`, `p = 0.41`

The singleton layer is therefore not preserved at the H-NEW-232 level under the
1-D `mean_manner` reduction, even though the cluster-layer H-NEW-271 result
remains the correct parent claim.

