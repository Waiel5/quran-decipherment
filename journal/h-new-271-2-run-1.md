---
finding_id: h-new-271-2
run: 1
date: 2026-04-19
specialist: codex
seed: 20260419
verdict: NO-MAXT-RESCUE
---

# H-NEW-271-2 run 1 journal

## Task

Test whether the singleton-layer failure of `H-NEW-271.1` can be rescued by the
smallest allowed augmentation: keep `mean_manner` fixed and add exactly one
other phonological axis from the locked `H-NEW-271` pool.

## Timeline

1. Wrote the preregistered follow-up file
   `h-new-271-2-minimal-singleton-rescue-prereg.md`.
2. Locked the candidate space to the 9 phonological pairs
   `mean_manner + {one other phonological axis}`.
3. Locked the inferential unit to the best-performing pair, with familywise
   maxT correction across all 9 candidates.
4. Wrote `scripts/h_new_271_2_minimal_singleton_rescue.py` so it imports the
   locked `H-NEW-271` codebook directly and reuses the `H-NEW-232` accepted
   singleton cluster sets verbatim.
5. Ran the script in the local environment.
6. Observed the locked outputs:
   - best pair = `mean_manner + mean_vowel_carrier`
   - best hits = `8 / 10`
   - corrected `p_maxT = 0.0899100899100899`
   - verdict = `NO-MAXT-RESCUE`
7. Wrote the findings markdown and JSON artifact.

## Result

The bounded search produced an important raw pattern:

- a unique 2-D pair, `mean_manner + mean_vowel_carrier`, restores the raw
  `H-NEW-232` hit count of `8 / 10`
- `mean_sonorant` and `mean_idhlaq` reach `7 / 10`
- no other pair does better than `6 / 10`

But the raw restoration does not survive the 9-way maxT correction. The
familywise-null 95th percentile is itself `8`, so the observed best pair lands
on an interesting boundary rather than a clean inferential pass.

## Best-pair misses

The winning pair still misses:

- `HMASQ -> TSM` instead of `{HM}`
- `N -> HM` instead of `{ALM, ALR}`

Nearest multi-member surah and nearest centroid agree for all 10 singleton
cases under the winning pair, so the remaining problem is geometric, not a
centroid-vs-neighbor artifact.

## Exact comparison

- `H-NEW-271.1`: `5 / 10`, `p = 0.41`
- `H-NEW-271.2` best pair: `8 / 10`, `p_maxT = 0.0899100899100899`
- `H-NEW-232`: `8 / 10`, `p = 0.024975024975024976`

So the minimal 2-D repair restores the **raw** `H-NEW-232` topology but not the
**corrected** evidential strength. The singleton layer remains unsolved under
this bounded augmentation family.
