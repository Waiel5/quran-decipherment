---
finding_id: h-new-301-5
run: 1
date: 2026-04-19
specialist: codex
seed: 20260425
verdict: TARGETED-RESIDUAL-RESCUE
---

# H-NEW-301-5 run 1 journal

## Task

Follow up the landed `H-NEW-271.5` residual compact burden on OQ-1.

That finding showed that under the stronger `H-NEW-274` empirical accepted
table, the compact 2-D failure no longer sat on `HMASQ`. It had narrowed to:

- `YS`
- `N`

The task here was to reuse the exact 55-pair family from `H-NEW-301`, change
only the accepted table to the locked empirical version, and ask a narrower
inferential question:

> does any pair rescue both `YS` and `N` in a way that survives a 55-pair maxT
> null once the statistic is defined honestly for those two rows?

## Timeline

1. Wrote the pre-registration file
   `h-new-301-5-empirical-table-residual-row-rescue-prereg.md`.
2. Wrote `scripts/h_new_301_5_empirical_table_residual_row_rescue.py`.
3. Kept the feature universe fixed to the `H-NEW-301` 11-feature family and
   the exact `C(11,2)=55` pair search.
4. Switched only the accepted singleton table to the locked `H-NEW-274`
   empirical version.
5. Defined the targeted statistic on `YS` and `N`:
   - rescue count over the two rows
   - tie-break by summed positive accepted-vs-rejected centroid margin
6. Ran the 20,000-permutation familywise maxT null.
7. Wrote the JSON artifact and findings markdown.

## Locked outputs

- observed best pair:
  `mean_voice + mean_sonorant`
- observed targeted rescue:
  `2 / 2`
- observed positive-margin sum:
  `4.567826058189053`
- observed full-task hits:
  `8 / 10`
- pairs rescuing both targets:
  `14 / 55`
- highest total hits among 2/2-rescue pairs:
  `9 / 10`
- corrected targeted p-value:
  `0.00004999750012499375`
- count-only diagnostic p-value:
  `0.8431578421078946`
- verdict:
  `TARGETED-RESIDUAL-RESCUE`

## Structural reading

This run produced a sharp split between two very different claims:

1. **Count-only claim**:
   "some pair rescues both `YS` and `N`" is weak. It happens too often under
   the 55-pair search to carry inference on its own.
2. **Margin-based claim**:
   `mean_voice + mean_sonorant` rescues both rows by an extremely large margin
   relative to the familywise null. That is the real signal.

The null made this especially clear:

- `16,863 / 20,000` permutations had some pair with `2 / 2` rescue
- but none matched the observed best positive-margin sum

So the inferential win is not "a 2/2 pair exists." It is "the observed 2/2
winner is geometrically far stronger than the search family usually allows."

## Best-pair behavior

Under `mean_voice + mean_sonorant`:

- `YS` lands effectively exactly on the `HM` centroid
- `N` lands inside the accepted `{ALM, ALR}` set with large separation from
  the nearest rejected centroid

The pair does not solve the full singleton table. It misses:

- `ALMS`
- `S`

That is why this finding should not be misread as a full compact singleton
closure.

## Interpretation

This materially sharpens OQ-1.

Before this run, the honest reading was:

- compact global singleton closure is still missing
- the live empirical-table compact residue is `YS` plus `N`

After this run, the honest reading is:

- compact global singleton closure is still missing
- but the live `YS` / `N` residue itself is now a solved 2-D phonological
  subproblem, carried by `mean_voice + mean_sonorant`

That is the right scope for the result.
