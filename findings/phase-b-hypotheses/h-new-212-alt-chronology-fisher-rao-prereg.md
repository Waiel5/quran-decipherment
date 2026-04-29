---
finding_id: h-new-212
title: Alternative chronology orderings — Fisher-Rao path length comparison
status: pre-registered
bonferroni_family: h-new-212
bonferroni_k: 3
alpha_bon: 0.0167
seed: 20260419
date_prereg: 2026-04-17
parent_lineage: H-NEW-111 (Fisher-Rao mushaf-order test)
---

# [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] — Alternative chronologies under Fisher-Rao

## Motivation

[[h-new-111-fisher-rao-mushaf|H-NEW-111]] established the mushaf order has Fisher-Rao path length L_mushaf that
is SHORTER than random (informative-geodesic signal). The chronology baseline
compared was the **Egyptian Standard 1924** ordering (`revelation_order` in
`data/revelation-order.csv`, which tracks the Cairo 1924 edition). The claim
"mushaf beats chronology" is thus currently one-chronology-deep.

[[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] asks: under other published academic chronologies (Nöldeke-Schwally
1860/1909, Bell 1937, Blachère 1947), does the mushaf still dominate?  Is any
alternative chronology Fisher-Rao-shorter than mushaf?

## Pre-registered chronologies

1. **Egyptian Standard 1924** (Cairo reformed edition tartīb al-nuzūl) — data
   source: `data/revelation-order.csv` column `revelation_order`.
2. **Nöldeke 1860 / Geschichte des Qorāns** (Schwally 1909 revision, 4-phase
   surah ordering within phases) — data source: `data/revelation-order.csv`
   column `noldeke_order` (Wikipedia cross-ref confirmed).
3. **Bell 1937** (Richard Bell, *The Qur'ān translated with a critical
   re-arrangement of the Surahs*, Edinburgh UP) — data source: French
   Wikipedia "Sourate" table (hard-coded below; cross-verified with CARM,
   Understanding Islam where possible). CAVEAT: Bell primarily dated at the
   pericope level, not the whole-surah level; the table gives first-date of
   surah as Bell's surah-level assignment. Surahs 15 (coded "M" not numeric),
   81/82 (both rank 15), 80/84 (both Blachère rank 24): treated as ties,
   resolved by mushaf-order secondary sort. Noted as data-quality caveat.
4. **Blachère 1947** (Régis Blachère, *Le Coran: Traduction selon un essai de
   reclassement des sourates*, Paris) — data source: French Wikipedia
   "Sourate" table.

## Hypothesis family (Bonferroni k=3)

Acknowledged test family:

- **PRIMARY-1** — L_egyptian vs null (1-sided lower). Is L_egyptian < random?
- **PRIMARY-2** — L_bell vs null (1-sided lower). Is L_bell < random?
- **PRIMARY-3** — L_blachere vs null (1-sided lower). Is L_blachere < random?

Bonferroni k=3, α_bon = 0.0167 per test.

Nöldeke is ALREADY published via [[h-new-111-fisher-rao-mushaf|H-NEW-111]] Secondary B (L_nold reported,
p_2sided reported). It is REUSED here as a reference but NOT in the test
family (no multiple-comparison cost, per rules-tuple of this pre-reg).

## Primary question: which ordering is SHORTEST?

Descriptive ranking of {L_mushaf, L_egyptian, L_noldeke, L_bell, L_blachere,
L_random_mean, L_2opt_lower_bound} — **pre-committed sign-flip prohibition**:
no post-hoc rationalisation of which chronology "wins". Report all four with
full null-calibrated p-values; the shortest is declared the shortest, full
stop.

## Secondary (no Bonferroni cost; descriptive only)

- Rank-correlation (Spearman ρ) between each chronology pair (including
  mushaf-as-index-1..114) — diagnostic of how much the four chronologies
  agree with each other.
- Pairwise path-length differences (L_egyptian − L_mushaf, etc.) reported
  with raw-diff and as fraction of null SD (null_sd from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]).

## MW protections

- **MW-1 length control**: inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (L1-normalized probability
  vectors; all four chronologies traverse the same 114 points under the same
  distance matrix D).
- **MW-5 positive control**: inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (greedy-NN-from-surah-1;
  if the null is broken there, this run is INSTRUMENT-BROKEN and no verdict
  is issued).

## Locked parameters (frozen at pre-reg sign)

- seed: 20260419 (fresh null draws, independent from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s 20260417)
- permutations: 10000
- K_TOP roots: 500 (inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]])
- DIRICHLET_ALPHA: 0.5 (inherited)
- distance matrix D: loaded from `findings/phase-b-hypotheses/csv/h-new-111.json`
  `D_matrix_upper_triangular` (SHA-256 of [[h-new-111-fisher-rao-mushaf|h-new-111]].json will be logged).

## Acceptance window

For each chronology c ∈ {egyptian, bell, blachere}:
- PASS if p_c (1-sided lower) < α_bon = 0.0167
- NULL otherwise

Family PASS: at least one chronology passes AND mushaf (reference; not in
family) remains shorter than all passing chronologies.

"Does mushaf still win?" = YES if **no** chronology has L_c ≤ L_mushaf.

## Garden of forking paths (logged BEFORE run)

1. Chose 4 chronologies (Egyptian, Nöldeke, Bell, Blachère) — standard
   academic set. Nöldeke dropped from family because of [[h-new-111-fisher-rao-mushaf|H-NEW-111]] precedence.
2. Chose fresh seed 20260419 (independent from 20260417) for null draws.
3. Chose 1-sided lower-tail (predicted direction: chronology if real = short).
4. Chose to reuse [[h-new-111-fisher-rao-mushaf|H-NEW-111]] distance matrix rather than recompute (saves
   30+ min; adds SHA-256-dependency audit).
5. Tie-breaking for duplicate ranks: mushaf-order ascending (documented; any
   duplicate-rank pair in Bell/Blachère from French-Wikipedia table).
6. Surah 15 in Bell table coded as "M" not numeric: imputed at rank
   midpoint of its Nöldeke bucket (middle Meccan; Bell rank ≈ 52).
   Documented imputation.

## Output

- JSON: `findings/phase-b-hypotheses/csv/h-new-212.json`
- Analysis MD: `findings/phase-b-hypotheses/h-new-212-alt-chronology-fisher-rao.md`
