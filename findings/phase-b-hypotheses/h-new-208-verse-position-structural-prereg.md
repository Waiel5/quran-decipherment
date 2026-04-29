# [[h-new-208-verse-position-structural|H-NEW-208]] — Verse-position within-surah structural analysis (pre-registration)

**Date filed:** 2026-04-17
**Seed:** 20260419
**Bonferroni k:** 3 (primary family)
**Status:** PRE-REG (written before running `scripts/h_new_208_verse_position_structural.py`)

## Motivation

[[h-new-90-kahf-narrative-structure|H-NEW-90]] Q 18 al-Kahf found a word-midpoint convergence at v50 (sitting in
interlude-B, 45-59). We now ask whether "position within surah" as a normalized
coordinate has structural signature across all 114 surahs, and whether
MIDPOINT verses in particular carry distinguishable features.

For every verse `(s, v)` with `v_id ∈ 1..V_s`, define
`p(s,v) = (v - 0.5) / V_s ∈ (0, 1)` (continuous midpoint-of-cell).

## Primary tests (Bonferroni k=3, α_bon = 0.05/3 = 0.01667, two-tailed)

**T1 Verse-length signature at 5 position bands.**
Bands B = {FIRST: v=1}, {Q1: p ≈ 0.25, nearest-v}, {MID: p ≈ 0.5, nearest-v},
{Q3: p ≈ 0.75, nearest-v}, {LAST: v=V_s}.
For each band collect verse-length (no-tashkeel grapheme count excluding
recitation-marks per methodology §8). Test: is there a band-effect
(Kruskal-Wallis H across 5 bands, all 114 surahs, one verse per surah per
band)?
- PASS: p < 0.01667.

**T2 Divine-name density at 5 position bands.**
Using `findings/phase-b-hypotheses/divine-names-by-verse.csv` `num_names`
column. Same 5 bands. Kruskal-Wallis across bands.
- PASS: p < 0.01667.

**T3 MIDPOINT specialness — is MID band distinguishable from non-MID?**
Pool FIRST+Q1+Q3+LAST vs MID. Two-sample Mann-Whitney U on verse-length
(primary feature, to avoid double-dipping T1). Report effect direction.
- PASS: p < 0.01667 AND |rank-biserial r| ≥ 0.10.

## Secondary (descriptive, not α-counted)

**S1** Per-surah: which surahs have a MIDPOINT verse whose verse-length OR
divine-name count is ≥ 2σ from the surah mean? Report list (ranked). These
are candidates for "structural midpoint" surahs; Q 18 v55 (the nearest-v to
p=0.5 in Q 18, V=110) is a lookup to cross-check the [[h-new-90-kahf-narrative-structure|H-NEW-90]] finding.

**S2** Correlation of normalized position vs verse-length (Spearman ρ, all
6236 verses). Sign/magnitude of any end-loading or front-loading global trend.

**S3** Sensitivity: re-run T1-T3 excluding Q1-Q9 (short first decile may
dominate) and excluding surahs with V_s < 20 (bands collapse).

## Data

- Corpus: `quran-text/quran-no-tashkeel.json` (primary; locked by methodology).
- Verse-length: grapheme count after filtering the recitation-mark codepoints
  used elsewhere in project (`\u06D6-\u06ED`, `\u0640` tatweel, combining
  marks `\u064B-\u065F\u0670`).
- Divine-name count: `findings/phase-b-hypotheses/divine-names-by-verse.csv`
  `num_names` column (1981 rows = all verses carrying ≥1 divine name; verses
  absent from CSV are treated as `num_names = 0`).

## Banding rule (LOCKED)

For surah with V verses:
- FIRST = v = 1
- Q1 = v closest to round(0.25 * V + 0.5)    (ties → lower v)
- MID = v closest to round(0.50 * V + 0.5)
- Q3 = v closest to round(0.75 * V + 0.5)
- LAST = v = V

When V < 5 the surah is **excluded** from T1/T2/T3 (insufficient band
separation). 114 − (surahs with V<5) surahs used.

## Falsifiers

- T1, T2, T3 all non-significant → hypothesis dies. Verse position is not a
  structural predictor.
- T3 significant but MID is "flatter" (lower verse-length, fewer names) than
  non-MID → MIDPOINT is a *lull*, not a climax. Direction matters, report.
- S1 empty (no surah has a ≥2σ MID) → "structural midpoint" is not a
  surah-level phenomenon even if global T3 passes.

## Pre-commit

Script: `scripts/h_new_208_verse_position_structural.py`.
Seed 20260419 used only for S1 ranked-tie breaking and any permutation-null
sanity checks if we add them as a descriptive robustness (not counted in α).
