---
id: H-NEW-237
title: Numerical-residual consolidation — prime-density / cumulative-letter constants / abjad surah-name sum
parent: H-NEW-175
phase: B
date: 2026-04-17
seed: 20260419
rules_tuple:
  orthography: no-tashkeel
  letter_definition: hafs-kufan graphemes (U+0621..064A ∪ U+0671..06D3; tashkeel / recitation marks not counted)
  word_definition: orthographic-token, real-words
  basmala_policy: counted-only-in-surah-1
  abjad_tables: mashriqi (primary) + maghribi (secondary)
  null_seed: 20260419
bonferroni:
  k: 3
  alpha_family: 0.05
  alpha_bon: 0.0167   # 0.05 / 3, per-cell two-sided
direction: NULL expected for each cell (consolidation, not discovery)
verdict: PENDING
status: pre-registered (2026-04-17)
companion_documents:
  - findings/phase-b-hypotheses/mathematical-sequences-audit.md (parent audit, k=160 cumulative family)
  - findings/HONEST-LIMITS-LEDGER.md (refutation catalog — DO NOT re-test)
  - findings/phase-b-hypotheses/h-new-174-175-176-triple-inline.md (H-NEW-175 Benford PASS)
---

# [[h-new-237-numerical-residuals|H-NEW-237]] — Numerical-residual consolidation after Benford PASS

## Rationale

H-NEW-175 delivered Benford's-Law PASS on both letter-per-surah (χ² = 7.44,
p = 0.490) and verse-per-surah (χ² = 7.44, p = 0.490) leading-digit
distributions. Benford PASS rules out *large-scale numerological manufacture*
(the strong Khalifa/Jarrar-style hypothesis). [[h-new-237-numerical-residuals|H-NEW-237]] audits the three
remaining *residual* numerological claim-classes that Benford does not
adjudicate:

- **Cell A** — per-surah verse-count *prime density*: is the 114-long
  sequence of verse counts unusually prime-rich (or prime-poor) relative
  to matched random integer draws?
- **Cell B** — *cumulative letter-count* path: does any prefix sum L₁ + L₂
  + ... + Lₖ (k = 1..114) land within tolerance of a distinguished
  mathematical constant (π·10ⁿ, e·10ⁿ, φ·10ⁿ, π², e², φ², π·e, π·φ, e·φ)
  for some integer n?
- **Cell C** — total *abjad* (gematria) sum of the 114 surah names: does
  the corpus-level surah-name-sum hit a distinguished round integer
  (100 000, 123 456, 7 × 11 × 13 × 17 × ..., famous-constant × 10ⁿ, etc.)
  under either mashriqi OR maghribi tables?

## Classical anchor

- Al-Suyūṭī, *al-Itqān* nawʿ 52, lists many numerical curiosities of the
  Quran (verse totals, letter totals, surah-count divisibility) but treats
  them as decorative/enumerative rather than as structural codes.
- The modern numerological-code genre (Khalifa 1974, Nawfal 1983,
  Hassab-Elnaby c. 1990, al-Kaheel 2000s) is the intellectual lineage
  this audit adjudicates.
- Feedback-memory `feedback_rules_tuple_bidirectional.md` — if any cell
  PASSES, a rule-variant sweep is mandatory before interpretation.

## Cell A — verse-count prime density

### Claim template

The 114 per-surah verse counts V₁..V₁₁₄ (range [3, 286]) contain more
primes than matched random integers in the same range.

### Statistic

`k_primes_observed` = count of V_i that are prime.

### Null

1 000 random samples of 114 integers drawn uniform-IID from the empirical
per-surah V-distribution (resampled from the 114 observed values WITH
replacement). Primary null: the Quran's V-values themselves shuffled
(trivial; K = 0 variation — skipped in favor of analytic baseline below).
Secondary/stronger null: 1 000 draws of 114 integers uniform from the
*range* [min(V)..max(V)] = [3..286]. Both nulls reported; primary test
is the uniform-range null (analytic prime density in [3, 286]).

### Test direction

Two-sided (we are testing for *any* deviation from expected prime density,
not specifically excess or deficit).

### Pass threshold

p_bon ≤ 0.0167 under either null.

### MW-5 cheat

Shuffle surah-indices → verse-counts; prime-count MUST be invariant to
ordering. If it changes, pipeline bug.

### Pre-registered expected verdict

NULL — prior prior work (mathematical-sequences-audit.md §2) shows the
V-distribution contains 32 primes, comfortably inside the analytic
expectation.

## Cell B — cumulative letter-count constants

### Claim template

Some prefix sum Sₖ = L₁ + L₂ + ... + Lₖ (for k ∈ 1..114, where Lᵢ is the
grapheme count of surah i under locked rules) lands within relative
tolerance ε = 0.001 (0.1%) of a distinguished constant × 10ⁿ, where
the constant set is {π, e, φ, π², e², φ², π·e, π·φ, e·φ, π·e·φ} = 10
constants, and n ∈ {0..6} covers the full numerical range.

### Statistic

`min_relative_distance` = minimum over all (k, C, n) of |Sₖ − C·10ⁿ| /
(C·10ⁿ).

### Hit count

`n_hits` = count of (k, C, n) triples where the relative distance ≤ ε.

### Null

2 000 random permutations of the 114 Lᵢ values (preserves marginal L
distribution, destroys ordering). Compute `min_relative_distance` and
`n_hits` under each permutation; compare to observed.

### Test direction

Two-sided; primary statistic is `n_hits` (one-sided upper tail — more
hits than random).

### Pass threshold

p_bon ≤ 0.0167 on either `min_relative_distance` (lower-tail) or
`n_hits` (upper-tail). We report both; primary is `n_hits` upper-tail.

### MW-5 cheat

Identity permutation (no shuffle) must exactly reproduce observed Sₖ.

### Pre-registered expected verdict

NULL — the prefix-sum path is a 1-D random walk in L-space; the chance
that it hits any specific constant within 0.1% tolerance at any of
~70 valid (C, n) pairs across 114 prefix positions is roughly
`114 × 70 × 2 × 0.001 ≈ 16` expected hits by pure density. Observed hit
count should be Poisson-like around 16 under the permutation null.

## Cell C — 114 surah-name abjad sum

### Claim template

The sum of abjad values (separately under mashriqi and maghribi tables)
of all 114 canonical surah-names lands on a distinguished integer —
defined as one of: {multiple of 19, 786, 114², 114 × 19, 2 × 3 × 19 × N
for small N, factorable as 114 × k, or within 0.1% of C × 10ⁿ for C in
the same 10-constant set as Cell B}.

Surah-names are as in the canonical mushaf (one name per surah;
where the mushaf gives multiple names, we use the name present in
`quran-text/quran-no-tashkeel.json`).

### Statistic

Abjad sum `S_names_mashriqi` and `S_names_maghribi`.

### Null

1 000 permutations of the *letter bag* of all 114 surah names (concatenate
all letters, shuffle, re-partition into 114 strings with same lengths as
the originals). Preserves letter-multiset + per-name-length structure,
destroys name-identity. Under this null the abjad sum is INVARIANT
(sum is order-free); so the real null is: compare observed to a null
where we draw 114 random Arabic "names" of matched-length letter bags
from the general Arabic-letter frequency distribution of the entire
Quran corpus. This is the informative null.

We compute TWO nulls:
- **Null-1 (invariant)**: letter-bag permutation → S_names unchanged
  (this is the MW-5 cheat and a consistency check).
- **Null-2 (informative)**: 1 000 draws of 114 fake names, each with
  length = length of the corresponding actual name, letters drawn IID
  from the corpus-wide letter-frequency distribution.

### Test direction

Two-sided; is observed abjad-sum distinguished vs chance draws?

### Pass threshold

p_bon ≤ 0.0167 under Null-2 on either mashriqi or maghribi table.

### MW-5 cheat

Null-1 must return identical abjad sum (invariance check).

### Pre-registered expected verdict

NULL — no prior claim in the literature specifies the surah-name-sum
target; the test is explorative within the well-defined distinguished-
integer set.

## Rules-variant sensitivity plan

If ANY cell passes at α_bon = 0.0167, we must run the following variants
BEFORE interpreting the result (per feedback_rules_tuple_bidirectional.md):

- Orthography: full-tashkeel, min-tashkeel (3 cells).
- Basmala policy: counted-in-every-surah, counted-nowhere (3 cells).
- Abjad table (Cell C only): mashriqi already primary, maghribi already
  secondary; add the rare Mashriqi-variant-with-shin=300 ordering.

All variant results must be reported together; the per-cell p_bon is
adjusted by the number of variant cells tested.

## Garden-of-forking-paths ledger (BEFORE run)

Decisions locked before script execution:
- Prime density null: use *uniform-range* primary null (not the shuffle-
  from-V null, which is degenerate).
- Cumulative constant set: exactly 10 constants × 7 orders of magnitude =
  70 targets (not arbitrarily extended).
- Tolerance ε for Cell B: 0.001 = 0.1%. Reported also at ε = 0.005
  (0.5%) and ε = 0.0001 (0.01%) for sensitivity, but ε = 0.001 is
  primary.
- Cell C distinguished-integer set: explicitly enumerated above;
  no post-hoc additions.
- Cell C permutation: letter-bag permutation is known to return zero
  variance (invariance check); use letter-frequency IID draws with
  matched name-length vector as the informative null.
- All seeds = 20260419; all permutation counts = 1 000 (A, C) or 2 000 (B).
- If Cell A's observed prime count is *exactly* at null median, we
  do not cherry-pick the tighter tail direction.

## Deliverables

1. `scripts/h_new_237_numerical_residuals.py` — runs all 3 cells.
2. `findings/phase-b-hypotheses/h-new-237-numerical-residuals.md` —
   writeup with pre-committed verdict.
3. `findings/phase-b-hypotheses/csv/h-new-237.json` — full per-cell
   numerics and per-permutation statistics.
4. `journal/h-new-237-run-1.md` — execution log.
5. MASTER-FINDINGS-LEDGER.md entry under Wave-4 (likely NULL-catalog).

## Bonferroni accounting

This pre-reg adds **k = 3** new tests to the project's family. With
cumulative family at ~160 (per mathematical-sequences-audit.md §0),
updated cumulative k ≈ 163. Local family Bonferroni is α = 0.05 / 3 =
0.0167; global-family threshold p = 3.07 × 10⁻⁴.
