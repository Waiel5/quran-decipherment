---
id: H-NEW-2090
title: Surah-position / verse-count arithmetic-coincidence scan — chance vs design
date_locked: 2026-05-29
seed: 20260509
n_perm: 10000
bonferroni_k: 8
bonferroni_family: H-NEW-2090-surah-arithmetic (8 arithmetic-coincidence cells, see below)
alpha_bon: 0.00625
direction_of_effect: NULL EXPECTED. The number of surah-position/verse-count exact arithmetic coincidences does NOT exceed the chance expectation under random re-assignment of verse-counts to positions. No arithmetic design is predicted in the surah/verse-count pairing.
origin: Popular devotional and numerological claims assert that surah numbers encode their verse-counts (e.g. "Q 36 Yāsīn = 36", surah-position N has N verses, or simple functions 2N / N±k). This pre-reg locks an EXHAUSTIVE skeptical scan of all such position↔verse-count arithmetic relations, with a permutation null, to quantify how many "coincidences" are expected purely by chance.
verdict_ceiling: NULL-OR-PASS. Default expectation is NULL (chance). A cell is promoted to PASS-DIRECTED only if its observed coincidence-count exceeds the permutation null at α_bon = 0.00625 (one-sided, more-coincidences-than-chance). Any single famous anecdote (e.g. Q 36) is MW-7-capped post-hoc unless it falls out of a pre-registered cell.
rules_tuple:
  verse_counts: Hafs-Kūfan, from data/hafs-verse-counts.tsv (114 rows, sum = 6236)
  surah_position: canonical mushaf order 1..114
  counting_unit: whole verses (āyāt), Hafs-Kūfan numbering
  basmala_policy: NOT counted as a separate verse except as v.1 of Q 1 (standard Hafs-Kūfan numbering already reflected in hafs-verse-counts.tsv)
  reading_tradition: Hafs-Kūfan default
  null_model: shuffle the 114 verse-counts across the 114 positions (random permutation), preserving the multiset of verse-counts; recompute every cell's coincidence-count per permutation
  primality_def: standard integer primality (n>1 with no divisors other than 1 and n)
---

# H-NEW-2090 pre-registration — surah-position / verse-count arithmetic-coincidence scan

## Origin

A recurring family of popular claims asserts that the canonical mushaf order arithmetically "encodes" verse-counts:

- "Surah Yāsīn is Q 36 and 36 = ..." style position-anchoring claims.
- Surah at position N is said (in some devotional lists) to have N verses, or 2N, or N±k.
- Position-letter coincidences: Q 50 is Sūrat Qāf (qāf = abjad 100), Q 42 al-Shūrā opens with the qāf-bearing muqaṭṭaʿāt cluster ḤM-ʿSQ, etc.
- Sum relationships: Σ verse-counts = 6236; Σ surah-numbers (1..114) = 6555; these are sometimes paired with the 6555 = Σ(1..114) "summation miracle" (Khalifa-adjacent claims).

These are exactly the kind of post-hoc arithmetic coincidence that the project's MW-2 (corpus-prior) and MW-6 (instrument-control) walls exist to discipline. The skeptical null is that any handful of exact hits is what one expects when scanning 114 integer pairs across many candidate arithmetic relations. This pre-reg quantifies that expectation with a permutation null.

## Hypothesis

**H0 (locked default, NULL EXPECTED)**: For each arithmetic relation in the pre-registered family, the observed number of exact surah-position/verse-count coincidences is consistent with the chance expectation under random re-assignment of the verse-count multiset to positions. No arithmetic design.

**Reverse / alternative (would require evidence)**: At least one cell shows an observed coincidence-count that exceeds the permutation null at α_bon = 0.00625 (one-sided, excess direction). This is NOT predicted.

## Tests / cells (the Bonferroni family, k = 8)

Each cell counts exact hits over the 114 surahs and is tested one-sided (observed ≥ null) against the 10000-permutation null. Direction LOCKED: we only ask whether there are MORE coincidences than chance (a design signature). Fewer-than-chance is not a meaningful "anti-design" claim and is reported descriptively.

- **Cell 1 — identity**: verse_count(N) == N. (the "surah N has N verses" claim)
- **Cell 2 — double**: verse_count(N) == 2·N.
- **Cell 3 — half**: verse_count(N) == N / 2 (only integer N even).
- **Cell 4 — off-by-one band**: |verse_count(N) − N| ≤ 1 (near-identity; permissive).
- **Cell 5 — verse-count prime AND position prime**: count of N where both N and verse_count(N) are prime (cross-tab co-primality). Null preserves which positions are prime; shuffles which verse-count lands there.
- **Cell 6 — reversal**: verse_count(N) equals the digit-reversal of N (e.g. N=12 ↔ 21), a common numerology move.
- **Cell 7 — small linear family |vc − (a·N + b)| == 0** for the small grid a∈{1,2,3}, b∈{−2,−1,0,1,2}: total exact hits across the grid (a single pooled count; the grid is the multiple-comparison hazard this cell internalizes). The famous "Q 36" anecdote, if real, must surface here.
- **Cell 8 — verse_count(N) is a multiple of N** (N | verse_count(N), verse_count>0): divisibility coincidence.

## Auxiliary descriptive checks (NOT in the Bonferroni family; reported, not null-tested)

- **D1** — sum invariants: Σ verse-counts (expect 6236), Σ(1..114) (expect 6555), difference 319, and whether 6236 / 6555 / 319 have any flagged numerological factorizations. Reported as locked arithmetic facts only.
- **D2** — position-letter coincidences (Q 50 Qāf, Q 68 Nūn, etc.): catalogued descriptively. These are NAME-based, not amenable to the verse-count shuffle null, so they are reported as anecdote-with-caveat under MW-7 (single-test α ceiling, no promotion).
- **D3** — the "running-sum" claim: starting from surah k, does the running cumulative verse-count hit a position-indexed target? Catalogued descriptively if any clean instance appears; MW-7-capped.

## Direction lock

LOCKED before computation:
- Every cell's pass-direction is EXCESS (observed > null) at one-sided α_bon = 0.00625.
- NULL is the expected outcome for all 8 cells.
- A cell with observed coincidence-count at or below the null median is reported as confirming chance.
- No cell may be re-interpreted as "design" via fewer-than-chance, digit-shuffling, or post-hoc relation-hunting. Cells 1–8 and the Cell-7 grid are the COMPLETE pre-registered relation set; no relation added after the SHA-lock counts toward a PASS.

## A-priori expectation (honest)

Over 114 surahs with verse-counts ranging 3..286, exact identity hits (Cell 1) are expected to be small (0–3). Verse-counts cluster heavily at small values (3..30 dominate the back half of the mushaf), while positions run 1..114, so identity hits concentrate where small verse-counts meet small positions — but the back-half surahs have small verse-counts at LARGE positions, suppressing identity. Expected Cell-1 hits ≈ 1–2, fully chance-consistent. Cell-7's 15-cell linear grid will produce several hits by construction (that is the point — it shows the "Q 36"-type anecdote is a grid artifact). Co-primality (Cell 5) is expected near its chance base-rate (~25% of positions prime × ~density of prime verse-counts). The whole exercise is predicted to be NULL: the famous coincidences are cherry-picked survivors of a large implicit search.

## Methodology

### Step 1 — load locked verse-counts
- Source: `/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv` (114 rows, tab-separated `position<TAB>verse_count`).
- Assert sum == 6236 and n == 114 (fail-fast).

### Step 2 — compute observed coincidence-counts for Cells 1–8
- Deterministic integer arithmetic; no rounding.
- Cell 5 uses a primality sieve up to max(114, max verse-count) = 286.
- Cell 7 pools exact hits over the locked a∈{1,2,3} × b∈{−2..2} grid (15 (a,b) pairs); a surah counts once if ANY (a,b) gives an exact hit (de-duplicated per surah) AND, separately, total grid-hit tally is recorded.

### Step 3 — permutation null (seed 20260509, 10000 perms)
- For each permutation: shuffle the 114-element verse-count vector across positions; recompute each cell's coincidence-count.
- Cell 5 holds the prime-position mask FIXED (positions 1..114 primality is structural) and shuffles only which verse-count lands at each position.
- One-sided p = (1 + #{perm coincidence ≥ observed}) / (n_perm + 1).
- Report null mean, null median, observed, raw p, Bonferroni-corrected significance flag at α_bon = 0.00625.

### Step 4 — descriptive auxiliaries D1–D3
- Locked arithmetic facts only; no null test; MW-7 cap.

## Outputs

- `findings/phase-b-hypotheses/csv/h-new-2090.json` — per-cell observed, null mean/median, p, Bonferroni flag; the exact-hit surah lists; D1–D3 descriptive block.
- `findings/phase-b-hypotheses/h-new-2090-surah-arithmetic.md` — full finding writeup.
- `findings/phase-b-hypotheses/scripts/h-new-2090.py` — locked-SHA runner.

## Honest limits

- **Implicit multiple comparison**: the universe of "simple arithmetic relations" between two integers is effectively unbounded. Cells 1–8 + the Cell-7 grid are a deliberately broad but FINITE pre-registered sample; they cannot exhaust the numerologist's search space, but they show that even a generous pre-registered net catches only chance-level hits. This is the correct skeptical posture.
- **Permutation null preserves the verse-count multiset** (it shuffles assignment, not values), which is the right null for "is the PAIRING designed" — it does not test whether the multiset of verse-counts is itself unusual (a separate question, out of scope here).
- **Position-letter coincidences (D2)** cannot be shuffle-tested and are explicitly anecdote-capped.
- **Sum invariants (D1)** are single fixed integers, not a distribution; any "relationship" among 6236 / 6555 / 319 is post-hoc and reported as such, never promoted.

## Cross-finding connections

- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 17** (ʿadad al-suwar wa-l-āyāt): the classical enumeration; the 6236-verse total is corpus-locked (MASTER-FINDINGS-LEDGER §1).
- **Popular "6,666 verses" tradition** — already FALSIFIED in the ledger; this test extends the skeptical audit to position↔count arithmetic.
- **al-Khalifa muqaṭṭaʿāt / 19-summation claims** — decisively rejected in Wave-K (cross-finding-022); D1's 6555-summation is the same genre and is reported descriptively only.
- **muqaṭṭaʿāt letter-axis ⊥ content-axis** (FALSIFIED 4×): reinforces that surah-position is not a content-encoding channel; arithmetic-position coincidences are expected to be null by the same logic.

## Pre-registration discipline

- Cells 1–8, the Cell-7 (a,b) grid, the null model, the seed, and α_bon = 0.05/8 are all locked in this file.
- SHA256 of this locked file is computed at the end of pre-registration and embedded in the runner; verified fail-fast at runtime.
- Direction is locked: EXCESS-over-chance only; NULL expected.
- Seed 20260509, 10000 permutations.
