---
finding_id: h-new-284
run: 1
date: 2026-04-18
specialist: codex
seed: 20260418
---

# H-NEW-284 run 1 journal

## Timeline

1. Read the H-NEW-131.1 Cell B residualization line and the H-NEW-279
   locked 5-metric family.
2. Wrote the H-NEW-284 prereg to lock the length-residualized simplex
   and the inherited majority rule on `C_LR`.
3. Wrote `scripts/h_new_284_length_residualized_metric_robustness_mst.py`
   to reuse the Cell B simplex and rerun the locked metric family.
4. Executed the script.
5. Observed the exact outputs:
   - mean surah tokens = `438.3157894736842`
   - Q108 effective alpha_i = `31.30827067669173`
   - Fisher-Rao: `Q108 degree 16`, rank `1`
   - Jensen-Shannon: `Q108 degree 16`, rank `1`
   - Total variation: `Q108 degree 3`, rank `12`
   - Euclidean L2: `Q108 degree 15`, rank `1`
   - Cosine-angle: `Q108 degree 15`, rank `1`
   - `C_LR = 4/5`
   - verdict = `METRIC-ROBUST RESIDUE`
6. Wrote the JSON artifact.
7. Wrote this findings file and journal.

## Notes

- The only breaker is total variation.
- The result is bounded, not inferential. There is no native null for the
  dependent metric-rank table, so I kept the claim descriptive.
- The surviving residue is still strong enough to remain top-3 on 4 of 5
  metrics after length equalization.
