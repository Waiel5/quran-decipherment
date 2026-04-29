# H-NEW-268 run 1 — Q18 Al-Kahf four-narrative structural spacing test

**Date**: 2026-04-18  
**Task**: land H-NEW-268 as a bounded, pre-registered test of the four
main Al-Kahf narratives using existing corpus resources only.

## Orientation

Read and reused:

- `journal/h-new-90-kahf-narrative-structure-run-1.md`
- `journal/kahf-deep-run-1.md`
- `findings/per-verse-annotations.csv`
- `findings/verse-signature-atlas.csv`
- `quran-text/quran-no-tashkeel.json`

Key design decision: avoid a second broad "parallelism" claim after
H-NEW-90. Restrict this run to **spacing geometry** over the same four
locked narrative ranges.

## Pre-registration

Locked block boundaries:

1. 18:9-26
2. 18:32-44
3. 18:60-82
4. 18:83-98

Locked null:

- fixed block lengths `(18, 13, 23, 16)`
- fixed order
- uniform exact enumeration over all placements inside a 110-verse surah
- residual 40 verses distributed across 5 gap slots
- total state space `C(44,4) = 135,751`

Locked Bonferroni family:

- A: `d1 = d3`
- B: `d2 > max(d1, d3)`
- C: `d1 = d3 < d2`

Bonferroni `k = 3`, `alpha_bon = 0.01667`.

MW-5 positive control:

- planted gap slots `(0, 5, 35, 0, 0)`
- expected tuple `(23, 48, 23)`

Pre-reg SHA-256 captured by script:

- `1fa0d98c3a2c9ac7df4827bf47ba0ea1fa747740364be8db15412b3801be7d62`

## Execution

- Wrote prereg
- Implemented exact-enumeration script
- Verified Q18 verse count from `quran-no-tashkeel.json` = 110
- Pulled block word/letter totals from `verse-signature-atlas.csv`
- Enumerated all 135,751 placements exactly
- Wrote JSON and findings

Runtime was effectively instantaneous.

## Results

Observed narrative starts:

- `(9, 32, 60, 83)`

Observed start-gap tuple:

- **(23, 28, 23)**

Observed gap slots:

- `(8, 5, 15, 0, 12)`

Primary family:

| Cell | Exact p | Bonferroni pass? |
|---|---:|---:|
| A — outer equality | 0.03233 | no |
| B — middle widest | 0.13341 | no |
| C — joint palindromic-expansion | **0.00802** | **yes** |

Descriptive:

- exact observed tuple frequency: `21 / 135,751 = 0.0001547`
- null mean `|d1-d3|`: `9.53`
- null mean `d2`: `21.0`

Overall verdict:

- **DIMENSION-SPECIFIC** (`1/3` cells pass)

## MW-5

Planted tuple:

- `(23, 48, 23)`

Results:

- A true
- B true
- C true
- exact tuple frequency `1 / 135,751 = 7.37e-06`

Positive control passed cleanly.

## Interpretation

The result is narrow but real. Al-Kahf's four main narratives are not
established here as a full-blown four-way symmetric macro-ring; instead,
their **start positions** show a statistically rare `23, 28, 23`
spacing pattern under the ordered-placement null.

This fits the literary intuition better than a lexical-overlap test:

- the outer spacing is exactly balanced,
- the middle span is broader,
- the balance is achieved by interlude placement rather than equal block
  sizes.

This also sits cleanly next to H-NEW-90:

- H-NEW-90: lexical parallelism weak / mostly null
- H-NEW-268: spacing geometry has a real, bounded hit

## Honest limits

- Verse-index spacing only; no content features in the test.
- Boundary-dependent.
- Uniform placement null is deliberately simple.
- The geometry is visible once boundaries are fixed, so this should not
  be oversold as hidden-code evidence.
- Only 1/3 cells passed, so the correct label remains
  **DIMENSION-SPECIFIC**.

## Deliverables

- `scripts/h_new_268_kahf_four_narratives.py`
- `findings/phase-b-hypotheses/h-new-268-kahf-four-narratives-prereg.md`
- `findings/phase-b-hypotheses/h-new-268-kahf-four-narratives.md`
- `findings/phase-b-hypotheses/csv/h-new-268.json`
- `journal/h-new-268-run-1.md`
