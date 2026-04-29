# Journal — H-NEW-204 run 1

**Date**: 2026-04-17
**Specialist**: autonomous agent
**Task**: Reverse-mushaf boundary test
**Seed**: 20260419
**Parent**: H-NEW-111 / H-NEW-130 / cross-finding-011
**Bonferroni k**: 2, α_bon = 0.025

## Question

Under reverse-mushaf ordering (114→113→...→1), do the same boundaries appear as
under forward? Fisher-Rao is a symmetric metric, so the primary test is a
verification (bug-check); the secondary is the novel question of reflective
architectural structure about the mushaf midpoint.

## Tests (pre-registered, Bonferroni k=2)

1. **PRIMARY (symmetry verification).** Top-15 consecutive-pair distance
   pairs (as unordered sets) must be identical between forward and reverse
   orderings. Failure = bug.
2. **SECONDARY (mirror-symmetry).** Spearman rank correlation between
   d(i, i+1) and d(115-i, 114-i) for i=1..56 (excluding self-mirror i=57).
   Permutation null (N=10,000). Two-sided.

## Results

- **PRIMARY: PASS.** max |d_fwd_reversed − d_rev| = 0.0 (exact). Top-15 pair
  sets are identical (as expected for a symmetric metric). No pipeline bug.
- **SECONDARY: NULL.** ρ = −0.0511, p_two_sided = 0.715. Mirror pairs are
  uncorrelated; no reflective architecture about the midpoint.
- **TERTIARY (exploratory, not Bonferroni-counted).** 0 mirror-partner pairs
  within the top-15 forward boundaries (expected under null: 0.93).
- **Magnitude mirror.** d(2, 3) = 0.6309 is the largest forward boundary
  (47% above mean); its mirror partner d(113, 114) = 0.2718 is near mean.
  No symmetric magnitude.

## Interpretation

The mushaf's architectural discontinuity structure is NOT mirror-symmetric
about the midpoint. The Q2→Q3 boundary (largest in the corpus) has no
corresponding boundary at Q113→Q114. This is consistent with the known
asymmetric architecture: long Medinan front-loaded surahs, short Meccan
tail, muqaṭṭāʿāt-bearing surahs concentrated in the early-to-middle range.

The primary verification is valuable as a QA check: had the top-15 sets
differed, it would indicate a bug in D-matrix indexing or the consecutive-
pair extraction logic in H-NEW-130. They are bit-identical, so H-NEW-130's
numbers stand.

## Output

`findings/phase-b-hypotheses/csv/h-new-204.json`
