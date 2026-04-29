---
finding_id: h-new-271-5
run: 1
date: 2026-04-19
specialist: codex
seed: 20260419
verdict: NO-MAXT-EMPIRICAL-RESCUE
---

# H-NEW-271-5 run 1 journal

## Task

Test whether the compact 2-D singleton-rescue line from `H-NEW-271.2` survives
once the accepted singleton table is upgraded to the stronger `H-NEW-274`
empirical version:

- `YS -> HM`
- `HMASQ -> TSM`

Everything else stays locked to the `H-NEW-271.2` design: same `mean_manner`
anchor, same 9 legal one-feature augmentations, same nearest-centroid geometry,
same familywise maxT null over the 9 candidates.

## Timeline

1. Wrote the preregistered follow-up file
   `h-new-271-5-empirical-table-singleton-rescue-prereg.md`.
2. Wrote `scripts/h_new_271_5_empirical_table_singleton_rescue.py` by
   reusing the `H-NEW-271.2` machinery and changing only the accepted singleton
   table to the locked `H-NEW-274` empirical version.
3. Ran the script in the local environment.
4. Observed the locked outputs:
   - best pair = `mean_manner + mean_sonorant`
   - best hits = `8 / 10`
   - corrected `p_maxT = 0.2077922077922078`
   - verdict = `NO-MAXT-EMPIRICAL-RESCUE`
5. Inspected the best-pair misses:
   - `YS -> TSM` against accepted `{HM}`
   - `N -> HM` against accepted `{ALM, ALR}`
6. Wrote the findings markdown and JSON artifact.

## Result

The stronger empirical singleton table does not rescue compact parsimony.

The main structural shift is not a pass. It is a relocation of the failure:

- `HMASQ` is no longer a blocker under the empirical table
- `YS` becomes a blocker instead
- `N` remains a blocker

Three pairs reach the raw `8 / 10` ceiling under the empirical table:

- `mean_manner + mean_sonorant`
- `mean_manner + mean_vowel_carrier`
- `mean_manner + mean_idhlaq`

The preregistered distance tie-break selects `mean_sonorant` as the canonical
winner, but inferentially the outcome is plainly negative.

## Exact comparison

- `H-NEW-271.2` inherited-table best pair:
  `mean_manner + mean_vowel_carrier`, `8 / 10`, `p_maxT = 0.0899100899100899`
- `H-NEW-271.5` empirical-table best pair:
  `mean_manner + mean_sonorant`, `8 / 10`, `p_maxT = 0.2077922077922078`

So the stronger table does not make compact rescue easier. It leaves the raw
ceiling unchanged and makes the corrected null materially harsher.

## Interpretation

This run matters because it closes a tempting escape route. The compact-rescue
failure is not just an artifact of the weaker inherited singleton table.

Even after adopting the stronger `H-NEW-274` empirical accepted clusters, the
best compact 2-D search still fails clearly. The open OQ-1 pressure point is
therefore narrower again: the residual compact difficulty now sits on `YS` and
`N`, not on `HMASQ`, but it remains genuinely unresolved.
