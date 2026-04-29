# Journal — H-NEW-262 run 1

**Date**: 2026-04-18  
**Command**: `python3 scripts/h_new_262_muqattaat_positional_code.py`

## Scope control

This run was redirected twice before landing:

1. `H-NEW-131` was already occupied in the repo.
2. `H-NEW-261` was also already occupied in the repo.
3. Final landed ID: `H-NEW-262`.

I kept ownership strictly to the five H-NEW-262 files requested and did
not edit any `h-new-131*` or `h-new-261*` artifacts.

## Goal

Test a formal same-letter positional hypothesis:

> for each muqaṭṭaʿat letter, are its normalized within-verse positions
> later inside the 29 muq-opened surahs than inside the 85
> non-muq-opened surahs?

This is deliberately narrower than H-NEW-113. H-NEW-113 compared the
14-letter muq set against the 14-letter complement set across the whole
corpus. H-NEW-262 compares **the same letter to itself** across the two
surah partitions.

## Design choices

- Canonical loader: `analysis.tools.loader.load_quran("no-tashkeel")`
- Same 28-letter normalization as H-NEW-113
- No opener stripping: I kept the canonical verses intact and only
  normalized characters
- Primary family: 14 one-sided Mann-Whitney U tests
- Direction: later positions in muq-opened surahs
- Bonferroni: `0.05 / 14 = 0.0035714286`
- KS kept as descriptive only

I did a small scratch comparison of candidate summary statistics while
settling the design. That pushed the final production spec toward
one-sided Mann-Whitney as the primary and KS as descriptive. So this is
best read as an honestly locked production analysis, not a pristine
blind first-look prereg.

## Result

- Positive control: **PASS**
- Overall verdict: **MIXED-LETTER-SPECIFIC**
- Pre-registered Bonferroni-14 survivors: **`ي`, `ن`**
- Exploratory reverse-direction Bonferroni-14 survivors: **`ر`, `ه`, `ق`**

Most important numbers:

- `ن`: mean `0.5376` vs `0.5131`, `Δ = +0.02446`, `RR_bin10 = 1.245`,
  `p = 4.08e-12`
- `ي`: mean `0.5296` vs `0.5199`, `Δ = +0.00973`, `RR_bin10 = 1.028`,
  `p = 3.47e-03`
- `م` just missed: `p = 4.13e-03`
- Sign balance across the 14 letters: `7` positive deltas, `7` negative
- Descriptive Stouffer aggregation in the pre-registered direction:
  `Z = -0.97`, `p = 0.834`

That is the key shape of the run:

- there really are letter-level differences
- but they are not moving together in one signed direction
- `ن` is the one clearly robust positive letter
- `ي` survives narrowly

## Positive control values

The instrument behaved exactly as expected on pooled-corpus bin-10
density:

- `ن = 0.1556` (`> 0.13`)
- `ر = 0.1598` (`> 0.13`)
- `ي = 0.1551` (`> 0.13`)
- `ا = 0.0680` (`< 0.10`)
- `ل = 0.0783` (`< 0.10`)

That was important because the main family result is mixed. The null and
near-nulls are credible only because the position-binning instrument is
clearly alive.

## Interpretation note

If I had seen only `ن`, I would have called this a clean letter-specific
success. What changed the overall verdict was the full family pattern:

- only `2 / 14` survive in the pre-registered direction
- `3` others survive in the opposite direction
- the family-wide sign balance is exactly neutral

So the right landing is not "the muq letters systematically move later
inside muq-opened surahs". The right landing is "some specific letters,
especially `ن`, do."

## Deliverables

- `scripts/h_new_262_muqattaat_positional_code.py`
- `findings/phase-b-hypotheses/h-new-262-muqattaat-positional-code-prereg.md`
- `findings/phase-b-hypotheses/h-new-262-muqattaat-positional-code.md`
- `findings/phase-b-hypotheses/csv/h-new-262.json`
- `journal/h-new-262-run-1.md`
