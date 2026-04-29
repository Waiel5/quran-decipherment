# [[h-new-210-mirror-verses|H-NEW-210]] Pre-Registration — Levenshtein Mirror-Verses

**Finding ID**: [[h-new-210-mirror-verses|h-new-210]]
**Date**: 2026-04-17
**Seed**: 20260419
**Bonferroni k**: 1 (single primary test)
**Corpus**: `quran-text/quran-no-tashkeel.json` (verse-level, 6236 verses)

## Hypothesis

The canonical mutashābih-al-lafẓ tradition catalogs verse pairs that are nearly-identical in wording across different surahs. If classical catalogs reflect real textual structure, a character-level Levenshtein distance < 30% of mean length should surface the same pairs and cluster at documented classical positions (e.g. Q 2:136 ↔ Q 3:84, Q 4:43 ↔ Q 5:6, intra-Q 55 al-Raḥmān refrain).

## Distinction from prior work

- `mutashabih-pairs.csv` / [[h-new-158-mirror-pair-uniqueness|H-NEW-158]] / [[h-new-160-delta-43-mirror|H-NEW-160]] use **token-overlap ratio** (set-based Jaccard-like).
- [[h-new-210-mirror-verses|H-NEW-210]] uses **Levenshtein edit distance** (character-level, order-sensitive).
These are orthogonal metrics; agreement would cross-validate.

## Primary pre-registered test

- **T1**: Compute Levenshtein distance d(v_i, v_j) for all cross-surah verse pairs (s_i ≠ s_j). Retain pairs with d/mean_len(v_i, v_j) < 0.30 AND min_len ≥ 10 chars (exclude trivial ~5-char doxologies).
- Rank top-50 by d/mean_len ascending (tie-break by -mean_len, i.e. prefer longer pairs).
- **Pre-registered cluster check**: of top-50, how many fall at the three classical hotspots?
  1. Prophet-catalog doublet (Q 2:136 ↔ Q 3:84 or neighbors ±2 verses).
  2. Ablution-doublet (Q 4:43 ↔ Q 5:6 or neighbors ±2).
  3. Al-Raḥmān refrain (any Q 55 ↔ Q 55 pair — actually intra-surah; we count Q 55:13 style refrains that also appear outside Q 55 if any).

**Null**: permute verse-to-surah assignments preserving verse lengths (seed 20260419, 1000 permutations) and compute fraction of permuted top-50 that land in the three hotspot windows. Compare observed vs null distribution.

## Decision rule

- SUPPORT if ≥3 distinct top-50 pairs land in the classical hotspot windows AND p < 0.05 (Bonferroni-adjusted α = 0.05/1 = 0.05).
- NULL-CONSISTENT otherwise.

## Deliverables

- `[[h-new-210-mirror-verses|h-new-210]]-prereg.md` (this file)
- `[[h-new-210-mirror-verses|h-new-210]]-mirror-verses.md` (findings report)
- `[[h-new-210-mirror-verses|h-new-210]]-top50.csv` (top-50 pairs with surah/verse/distance/ratio)
- `h_new_210_mirror_verses.py` (script)

## Garden of forking paths — locked BEFORE run

- Corpus: no-tashkeel JSON only (single fixed choice).
- Distance metric: standard Levenshtein on raw Arabic chars (spaces retained, no normalization beyond no-tashkeel).
- Threshold: 0.30 (chosen once — matches classical "near-identical" threshold ~70% agreement).
- Min length: 10 chars.
- Top-K: 50.
- Cross-surah only (no intra-surah pairs in primary; intra-surah reported separately as secondary descriptive).
- Permutation: length-stratified shuffle of surah labels, 1000 iters.
