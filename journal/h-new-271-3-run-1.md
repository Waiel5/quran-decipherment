---
finding_id: h-new-271-3
run: 1
date: 2026-04-19
specialist: codex
seed: 20260419
verdict: NO-MAXT-3D-RESCUE
---

# H-NEW-271-3 run 1 journal

## Task

Test the bounded 3-D follow-up to `H-NEW-271.2`: keep the best raw pair
`mean_manner + mean_vowel_carrier` fixed, add exactly one further
phonological axis from the remaining locked `H-NEW-271` pool, and check
whether any anchored triple yields a familywise-significant rescue of the
singleton layer against the locked `H-NEW-232` accepted sets.

## Timeline

1. Wrote the preregistered follow-up file
   `h-new-271-3-anchored-3d-singleton-rescue-prereg.md`.
2. Locked the anchor pair to `mean_manner + mean_vowel_carrier` from
   `H-NEW-271.2`.
3. Locked the candidate family to the 8 remaining phonological third-axis
   augmentations.
4. Wrote `scripts/h_new_271_3_anchored_3d_singleton_rescue.py` so it imports
   the locked `H-NEW-271` codebook directly and reuses the `H-NEW-232`
   accepted singleton cluster sets verbatim.
5. Ran the script in the local environment.
6. Observed the locked outputs:
   - best triple = `mean_manner + mean_vowel_carrier + mean_sonorant`
   - best hits = `8 / 10`
   - no triple exceeds `8 / 10`
   - corrected `p_maxT = 0.08691308691308691`
   - verdict = `NO-MAXT-3D-RESCUE`
7. Wrote the findings markdown and JSON artifact.

## Result

The anchored 3-D search does not solve the singleton layer.

Four legal triples tie the raw `8 / 10` level:

- `mean_manner + mean_vowel_carrier + mean_sonorant`
- `mean_manner + mean_vowel_carrier + mean_pharyngeal`
- `mean_manner + mean_vowel_carrier + mean_voice`
- `mean_manner + mean_vowel_carrier + mean_continuant`

The preregistered distance tie-break selects `mean_sonorant` as the canonical
winner, but that is only a descriptive winner. Inferentially, the familywise
maxT p-value remains above threshold.

## Persistent misses

The best anchored triple still misses the same two singleton cases as the best
raw pair in `H-NEW-271.2`:

- `HMASQ -> TSM` instead of `{HM}`
- `N -> HM` instead of `{ALM, ALR}`

Nearest multi-member surah and nearest centroid agree for all 10 singleton
cases under the best triple, so the residual failure is again geometric rather
than a centroid-vs-neighbor artifact.

## Exact comparison

- `H-NEW-271.1`: `5 / 10`, `p = 0.41`
- `H-NEW-271.2` best pair: `8 / 10`, `p_maxT = 0.0899100899100899`
- `H-NEW-271.3` best triple: `8 / 10`, `p_maxT = 0.08691308691308691`

So the 3-D follow-up barely improves the corrected p-value and does not raise
the raw hit ceiling. The singleton layer remains unresolved under this compact,
anchored search.
