---
finding_id: h-new-111b
title: "Fisher-Rao information-geodesic test of mushaf order — character-4-gram replication"
parent_finding: h-new-111
replication_of: h-new-111
specialist: h-new-111b-specialist
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 3
bonferroni_family: h-new-111b-char-4gram-replication
alpha_bon: 0.0167
alpha_raw: 0.05
direction_primary: "L_mushaf < L_random at permutation p < 0.0167 (one-sided lower-tail) — REPLICATING H-NEW-111"
direction_secondary_ratio: "L_mushaf / L_2opt < 1.2 (near-optimal) — REPLICATING H-NEW-111 (1.107 on roots)"
direction_secondary_nold: "L_mushaf ≤ L_nold (mushaf shorter-or-equal to chronology) — REPLICATING H-NEW-111 reversal (one-sided)"
K_char_4grams: 2000
dirichlet_alpha: 0.5
length_control: "MW-1 via L1-normalization of per-surah 4-gram distributions (each p_i sums to 1 regardless of surah length)"
rules_tuple: "(no-tashkeel, char-4-grams with spaces, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)"
perms: 10000
verdict_ceiling_if_pass: "REPLICATION-SUCCESS → combine with H-NEW-111 for CONFIRMED via cross-finding"
verdict_ceiling_if_null: "H-NEW-111 verdict remains PASS-DIRECTED; root-token signal does NOT generalize to char-4-gram feature space"
---

# [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] — Fisher-Rao char-4-gram replication of [[h-new-111-fisher-rao-mushaf|H-NEW-111]]

## Motivation

[[h-new-111-fisher-rao-mushaf|H-NEW-111]] (2026-04-17) reported that the Quran's mushaf ordering of its 114
surahs is Fisher-Rao information-geodesic optimal on the simplex of top-500
root distributions: z = −11.46, p < 10⁻⁴, L_mushaf / L_2opt = 1.107, and
the mushaf is shorter than both Nöldeke and Tanzil chronological orderings.
The verdict is PASS-DIRECTED and the project discipline (see
`HANDOFF/04-DISCIPLINE.md`) forbids promotion to CONFIRMED without
**independent replication on an orthogonal feature space**.

This pre-reg locks that replication: character-4-gram histograms per surah,
on the no-tashkeel canonical text. Char-4-grams are orthogonal to root
tokens because they capture:

- Phonological / graphemic signatures (letter-combination frequencies)
- Function-word repetition (high-freq 4-grams like "الله", "الذين", " من ")
- Morphological fragments (affix-pattern substrings that cross lexeme bounds)
- Span-agnostic surface structure (no lemmatization, no root inversion)

If the mushaf-order geodesicity signal reported in [[h-new-111-fisher-rao-mushaf|H-NEW-111]] is a real
property of the canonical arrangement, it should replicate on this
orthogonal feature — with the same sign (mushaf shorter than random) and
ideally the same reversal (mushaf shorter than chronology).

## Hypothesis

**Primary (H1, REPLICATION of [[h-new-111-fisher-rao-mushaf|H-NEW-111]] primary)**: The total Fisher-Rao
path-length over the mushaf order on char-4-gram distributions,
`L_mushaf = Σ_{i=1..113} D_FR(p_i, p_{i+1})`, is SHORTER than expected
under uniform random permutation of the 114 surahs. One-sided lower-tail.

**Secondary A (REPLICATION of [[h-new-111-fisher-rao-mushaf|H-NEW-111]] secondary A)**: `L_mushaf / L_2opt < 1.2`,
i.e. the mushaf is "near-optimal" in Fisher-Rao TSP sense on char-4-gram
distributions. ([[h-new-111-fisher-rao-mushaf|H-NEW-111]] got 1.107 on roots; we predict a similar ratio.)

**Secondary B (REPLICATION of [[h-new-111-fisher-rao-mushaf|H-NEW-111]] secondary B reversal)**: `L_mushaf ≤ L_nold`,
i.e. the mushaf is at-least-as-coherent as the Nöldeke chronological order
on char-4-gram distributions. One-sided because [[h-new-111-fisher-rao-mushaf|H-NEW-111]] pre-committed
the reversal sign post-result; for this replication, we are testing a
specific directional prediction lifted from the parent. NOTE: this is NOT
a two-sided test. If the sign reverses (chronology shorter than mushaf),
the reversal is NOT ratified in the char-4-gram feature space and cross-
finding confirmation is weakened.

## Method (locked before running)

### Corpus

- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
  (Hafs-Kūfan, 114 surahs, 6,236 verses, no tashkeel).
- Verified: basmala appears only as verse 1:1 in this JSON; Surahs 2–114
  do NOT include basmala as their verse 0. This matches the rules-tuple
  "basmala-counted-only-in-surah-1".

### Feature construction

1. For each surah i, concatenate all verse texts with a single space
   between adjacent verses: `text_i = " ".join(v['text'] for v in surah_i.verses)`.
   Exterior boundaries are NOT padded.
2. Extract all character 4-grams via sliding window, stride 1, over `text_i`:
   `grams_i = [text_i[k:k+4] for k in range(len(text_i) - 3)]`.
   **Includes spaces** (so function-word boundaries like " من " contribute).
3. Build global 4-gram frequency counter across all 114 concatenated texts.
4. **Select top-K_char = 2000** 4-grams by global frequency. LOCKED in this
   pre-reg before any computation. Ties at the boundary broken by lexicographic
   order (deterministic).

### Distribution construction (MW-1 length control)

5. For each surah i, build count vector c_i over the top-K_char 4-grams.
6. Dirichlet smoothing α = 0.5 on every cell: `c_i[k] + α`.
7. L1-normalize: `p_i[k] = (c_i[k] + α) / Σ_k (c_i[k] + α)`. Each p_i is
   a probability vector on the (K_char - 1)-simplex. Length drops out:
   two surahs with the same 4-gram PROPORTIONS get distance 0 regardless
   of absolute length.

### Fisher-Rao angular distance

`D[i,j] = 2 · arccos( Σ_k sqrt(p_i[k] · p_j[k]) )`

Clipped to [0, π]. Symmetric, zero on diagonal.

### Primary test

- `L_mushaf = Σ_{i=1..113} D[i, i+1]` (consecutive-surah distances in
  mushaf order 1 → 2 → ... → 114).
- **Null**: 10,000 uniformly random permutations, **seed = 20260417**
  (same seed as [[h-new-111-fisher-rao-mushaf|H-NEW-111]] for comparability, though the D matrix is
  independent). Recompute `L_perm = Σ D[π(i), π(i+1)]`.
- `p_primary = (#{L_perm ≤ L_mushaf} + 1) / (PERMS + 1)` (one-sided
  lower-tail; +1 conservatism).

### Secondary A: geodesic-optimality ratio

- Greedy nearest-neighbor TSP from each of 114 possible start-surahs, then
  2-opt local improvement on each; report best.
- `L_2opt_best`, then ratio `L_mushaf / L_2opt_best`. Descriptive.

### Secondary B: Nöldeke chronology vs mushaf

- Load `/Users/grey/Downloads/quran/data/revelation-order.csv`, build
  Nöldeke permutation σ by sorting mushaf surah IDs on `noldeke_order`.
- `L_nold = Σ D[σ(i), σ(i+1)]`.
- Report also `L_tanzil` on `revelation_order` column.
- Compare to same 10,000-perm null: `p_nold_lower = (#{L_perm ≤ L_nold} + 1) / (PERMS+1)`.
- Sign: does `L_mushaf < L_nold` replicate the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] reversal?

### MW-5 positive control

Greedy-NN ordering from surah 1 must fire at p < 10⁻⁴ under the same null.
If it does not, the null is BROKEN and primary result is inadmissible.

## Pre-committed acceptance window

- **PRIMARY PASS** (Bonferroni 3, α_bon = 0.0167): `p_primary < 0.0167`.
- **SECONDARY A**: ratio `L_mushaf / L_2opt < 1.2` → "near-optimal REPLICATED";
  `< 1.5` → "geodesic-like"; `< 2.0` → "weaker geodesic-like"; else "NOT replicated".
- **SECONDARY B**: `p_nold_lower < 0.0167` AND `L_mushaf ≤ L_nold`
  → "chronology-reversal REPLICATED". If sign flips, reversal NOT replicated.

## Garden of forking paths (REPLICATION-specific)

- **This is NOT a fishing expedition.** [[h-new-111-fisher-rao-mushaf|H-NEW-111]] is the parent finding;
  every parameter here is either LOCKED BY PARENT or LOCKED BY REPLICATION-
  INTENT. I have not viewed results on char-4-grams before locking this
  pre-reg.
- **K_char = 2000**: larger than K_roots = 500 because the 4-gram vocabulary
  is larger (tens of thousands) and 2000 captures most of the high-frequency
  mass while keeping computation tractable. 2000 is locked in YAML front-
  matter above. Alternatives rejected pre-result: K ∈ {500, 1000, 5000}.
  Rationale for 2000 specifically: it is the standard "top vocab" size for
  char-n-gram language-identification work (Cavnar-Trenkle 1994 used 300,
  but modern char-LID uses 1k–5k; 2000 is the geometric midpoint).
- **α = 0.5 (Jeffreys)**: SAME as [[h-new-111-fisher-rao-mushaf|H-NEW-111]] for comparability. Not retuned.
- **Distance**: Fisher-Rao angular, SAME as [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
- **Null**: 10,000 uniform permutations, seed 20260417, SAME as [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
- **Direction**: one-sided lower-tail for primary AND secondary B, because
  the parent finding PRE-COMMITS the direction we are testing to REPLICATE.
  This is the correct posture for a replication study (McShane & Gal 2017).
- **Length control**: L1-normalization of each p_i (MW-1). Identical to parent.
- **Text preprocessing**: "No-tashkeel text only" (per task brief). The JSON
  file at `quran-no-tashkeel.json` is already no-tashkeel. Verse concatenation
  uses a single space separator so that 4-grams spanning verse boundaries
  have one space in them (mirrors natural recitation spacing). No sentence-
  boundary padding added — tested that adding boundary tokens doesn't
  materially change high-freq 4-gram ranks (N/A pre-locked).
- **Feature-space orthogonality claim**: root-tokens ([[h-new-111-fisher-rao-mushaf|H-NEW-111]]) live in
  QAC morphological annotation space; char-4-grams live in surface-text
  grapheme space. The two feature spaces share information only through the
  underlying text — if a signal appears in BOTH, that is genuine replication
  evidence; if it appears in only one, the signal is feature-specific.

## Failure modes and how they would be reported

- **Positive control fails** → INSTRUMENT-BROKEN, primary result in abeyance;
  [[h-new-111-fisher-rao-mushaf|H-NEW-111]] verdict is not affected.
- **Primary p ≥ 0.0167** → **NULL (replication failed)**: the mushaf-order
  geodesicity does NOT generalize to char-4-gram space. [[h-new-111-fisher-rao-mushaf|H-NEW-111]] remains
  PASS-DIRECTED (no downgrade), but the cross-finding combined-evidence
  case weakens. Publish with equal prominence.
- **Primary passes but ratio ≥ 1.5** → partial replication: mushaf is
  shorter-than-random on char-4-grams, but LESS near-optimal than on
  roots. Report both numbers; cross-finding evidence is mixed.
- **Primary passes AND ratio < 1.2 AND L_mushaf ≤ L_nold** → full three-cell
  replication. Combine with [[h-new-111-fisher-rao-mushaf|H-NEW-111]] for CONFIRMED via cross-finding entry.
- **Primary passes AND L_mushaf > L_nold** → PARTIAL replication;
  geodesicity replicates but chronology reversal does NOT — suggests the
  reversal in [[h-new-111-fisher-rao-mushaf|H-NEW-111]] might be a root-feature artifact.

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_111b_fisher_rao_char_4gram.py` (seed 20260417,
   deterministic).
3. JSON `findings/phase-b-hypotheses/csv/h-new-111b.json` with distance
   matrix (upper triangular), L_mushaf, L_random quantiles, L_2opt, L_nold,
   L_tanzil, p-values.
4. Findings `findings/phase-b-hypotheses/h-new-111b-fisher-rao-char-4gram.md`.
5. Journal `journal/h-new-111b-run-1.md`.
