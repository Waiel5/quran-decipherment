---
finding_id: h-new-130
title: "Fisher-Rao mushaf-geodesic RESIDUALS — do the largest consecutive-surah jumps coincide with known structural boundaries?"
specialist: specialist-a
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 3
bonferroni_family: h-new-130-residuals
alpha_bon: 0.0167
alpha_raw: 0.05
direction_primary: "Of the top-15 largest Fisher-Rao consecutive-pair distances in mushaf order, ≥12 (80%) coincide with the pre-committed structural-boundary set B (|B|=54 of 113 pairs). Under the hypergeometric null (N=113, K=54, n=15), ≥12 corresponds to p = 0.0073 — less than α_bon = 0.0167. One-sided upper-tail."
direction_secondary_concentration: "Sum of mushaf-consecutive distances at B-pairs divided by sum at non-B-pairs is larger than expected under random-label assignment. Two-sided permutation test against 10,000 random relabelings of which 54 of 113 pairs carry the B-label."
direction_secondary_mw5: "Synthetic SORT-BY-SURAH-LENGTH ordering produces a DIFFERENT top-15-largest-jump set, and therefore a DIFFERENT |M ∩ B| value, from the mushaf ordering. If identical, boundary-hit metric is non-discriminative and primary is inadmissible."
K_top_pairs: 15
boundary_set_cardinality: 54
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)"
perms_for_secondary: 10000
verdict_ceiling: "PASS-DIRECTED (novel test, child of H-NEW-111; awaits independent replication on a distinct feature space such as char-4-gram D-matrix)"
parent_finding: h-new-111 / cross-finding-011
---

# [[h-new-130-fisher-rao-residuals|H-NEW-130]] — Fisher-Rao mushaf-geodesic RESIDUALS analysis

## Motivation

Parent finding [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (confirmed via [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]) established that
the canonical mushaf ordering of 114 surahs has Fisher-Rao path length
`L_mushaf = 85.76`, within 11% of an approximate TSP-optimum
`L_2opt = 77.47`. The ratio `L_mushaf / L_2opt = 1.107` means ~11% of the
path length is "in excess" of what a pure information-geodesic traversal
would require.

**Question.** Where is that excess? If the 11% gap is distributed uniformly
across all 113 consecutive pairs, the mushaf is near-optimal everywhere.
But if the gap concentrates at a small number of LARGE-JUMP pairs, those
pairs may represent INTENTIONAL structural hinges — points where the
mushaf deliberately leaves the local-continuity geodesic to mark a
transition between sections (end of sabʿ al-ṭiwāl, start of mufaṣṣal,
Meccan→Medinan, muqaṭṭāʿat letter-set change).

This is a test of whether the mushaf's non-geodesic residual is
*structurally interpretable* or *noise*.

## Hypothesis

**Primary (H1).** Of the 15 largest Fisher-Rao consecutive-pair distances
in mushaf order, a significantly larger fraction coincides with the
pre-committed structural-boundary set B than the hypergeometric null
expectation.

**Secondary A (H2, descriptive-concentration).** Mean Fisher-Rao
consecutive-distance at B-pairs is larger than mean at non-B-pairs
under a two-sided permutation null.

**Secondary B (MW-5 discriminativeness).** Synthetic SORT-BY-LENGTH
ordering produces a DIFFERENT top-15 jump-set than mushaf, and therefore
a DIFFERENT intersection with B. If identical, the test is
non-discriminative.

## Pre-committed structural-boundary set B

|B| = 54 of 113 consecutive-surah pairs. Computed deterministically from
orthodox classical and philological sources BEFORE any Fisher-Rao
distance was viewed in this analysis. The full list is reproduced from
the pre-commit computation (script output archived in
`journal/h-new-130-run-1.md`).

### Boundary types included

1. **Classical length-category boundaries (Ibn Nadīm / Zarkashī / Suyūṭī):**
   - Q 7→8 (end of al-sabʿ al-ṭiwāl, canonical)
   - Q 9→10 (alternative sabʿ boundary, by basmala-absence argument)
   - Q 48→49 (mufaṣṣal start, canonical)
   - Q 49→50 (alternative mufaṣṣal start)
   - Q 66→67 (short-mufaṣṣal boundary, per some classical schemes)
   - Q 77→78 (juzʾ ʿamma / short-mufaṣṣal start, traditional)
   - Q 92→93 (ultra-short-mufaṣṣal start, classical)

2. **Meccan ↔ Medinan period transitions** (from `data/revelation-order.csv`
   `period` column, applied to mushaf-adjacent pairs)

3. **Nöldeke phase sub-transitions** (`noldeke_phase` column applied to
   mushaf-adjacent pairs): Early/Middle/Late Meccan ↔ Medinan

4. **muqaṭṭāʿat presence transitions** (muq-surah ↔ non-muq-surah at i → i+1)

5. **muqaṭṭāʿat letter-set transitions** (both i and i+1 are muq-surahs
   but different letter-set, e.g., ALR → ALMR at Q 12→13)

### Full list (54 pairs)

See `scripts/h_new_130_fisher_rao_residuals.py`, function `build_boundary_set()`,
which is a PURE function of the input CSV + hardcoded canon. The script
writes the full list to `csv/h-new-130.json` under `boundary_set`.

## Method (locked before results viewed)

### Data

- D-matrix: load `D_matrix_upper_triangular` from
  `findings/phase-b-hypotheses/csv/h-new-111.json`. Parent-finding-frozen;
  no re-computation.
- Surah length: sum of verses from `data/hafs-verse-counts.tsv` (or
  equivalent). Used only for MW-5 positive control.
- Period / phase: `data/revelation-order.csv`.

### Primary test

1. Compute `d_i = D[i, i+1]` for `i = 1..113` from D-matrix.
2. Rank pairs by `d_i` descending. Take top-15 set `M`.
3. Compute `|M ∩ B|`.
4. **Null**: hypergeometric with `N = 113`, `K = 54`, `n = 15`.
   `p_primary = P(X ≥ |M ∩ B|)` (one-sided upper-tail).
5. **PASS**: `p_primary < α_bon = 0.0167`. This corresponds to
   `|M ∩ B| ≥ 12` (exact hypergeometric p = 0.00732).

### Secondary A — concentration

1. Let `S_B = Σ_{i ∈ B} d_i / |B|`, `S_notB = Σ_{i ∉ B} d_i / (113 − |B|)`.
2. Test statistic `T = S_B − S_notB`. If mushaf intentionally places
   "big jumps" at B, `T > 0`.
3. Null: 10,000 random re-labelings where 54 of 113 pair-indices are
   randomly assigned to a "B-label" set; recompute `T_perm`.
4. `p_secondary_A = #{|T_perm| ≥ |T|} / 10000` (two-sided).
5. Bonferroni-adjusted pass: `p_secondary_A < 0.0167`.

### Secondary B — MW-5 positive / discriminativeness control

1. Construct a synthetic ordering: surahs sorted by verse-count descending.
   Under this ordering, compute `d'_i = D[σ(i), σ(i+1)]` using the SAME
   D-matrix, rank to get top-15 set `M'`.
2. If `M' = M` (identical top-15 jump-pairs), the metric is
   non-discriminative and the primary claim is INADMISSIBLE. Report
   INSTRUMENT-BROKEN.
3. If `M' ≠ M`, check whether `|M' ∩ B|` differs from `|M ∩ B|` by at
   least 1. This is a sanity check on the "B coincidence is structural"
   claim: a random-ish ordering should hit B at near the null mean.

### MW-1 length control

Built into parent ([[h-new-111-fisher-rao-mushaf|H-NEW-111]]) D-matrix via L1-normalization; inherited.
No additional length residualization needed at [[h-new-130-fisher-rao-residuals|H-NEW-130]] level.

## Pre-committed acceptance windows

- **PRIMARY PASS**: `|M ∩ B| ≥ 12` (hypergeometric p ≤ 0.0073 < α_bon = 0.0167).
- **PRIMARY FAIL (NULL)**: `|M ∩ B| ≤ 11`. Publish as NULL with equal prominence.
- **SECONDARY A PASS**: `p_secondary_A < 0.0167` with sign `T > 0`.
- **SECONDARY A-REVERSE**: `p_secondary_A < 0.0167` with sign `T < 0`.
  Report as SIGN-REVERSAL-EXPLORATORY; cannot promote under
  PRE-REG-STANDARD-01.
- **SECONDARY B (MW-5)**: `M' ≠ M` required for primary admissibility.

## Garden of forking paths

### Divergence from team-lead method-spec (specialist-judgment override)

The team-lead task prompt specified `direction_primary: ≥60% of top-15
largest-jump pairs coincide with pre-committed boundary (vs null ~10%)`.
Before any Fisher-Rao data was viewed in this analysis, I computed the
pre-committed boundary set B from classical + philological sources and
found `|B| = 54 of 113 pairs = 47.8%`. The null expected overlap is
therefore `n · K / N = 15 · 54 / 113 = 7.17 of 15 = 47.8%`, NOT 10%.

- The "≥60% vs null 10%" framing embeds a factually incorrect null; I
  am overriding the threshold per the specialist-judgment-overrides
  protocol (`HANDOFF/04-DISCIPLINE.md`, MEMORY
  `feedback_specialist_judgment_overrides_team_lead_method.md`), which
  allows this override when (a) I have direct empirical evidence the
  team-lead spec is wrong, (b) the alternative is locked BEFORE
  results are viewed, and (c) I disclose the divergence.
- The corrected threshold `≥12 of 15 (80%)` yields hypergeometric
  p = 0.0073 under the correct null, which is the right stringency
  for `α_bon = 0.0167`.
- This is a **tightening** amendment (80% > 60%), so per the
  Bonferroni-asymmetry rule (MEMORY
  `feedback_bonferroni_tightening_vs_loosening.md`), it self-verifies
  without ratification. I am DMing the auditor regardless, for
  transparency and because the null MODEL changed (not just threshold).

### Why not expand |B|?

One could add more candidate boundaries (e.g., every 10-surah decade,
every juzʾ boundary, every ruku boundary). I am NOT doing this because:
- The 54-pair set is already 48% of all pairs; larger would make B
  near-trivial and uninformative.
- Juzʾ / ruku boundaries are later copyist/liturgical conventions, not
  intrinsic to the mushaf's structural architecture.
- PRE-REG-STANDARD-03 (feature-space-locked) prohibits post-hoc expansion
  regardless of result direction.

### Why not shrink |B|?

I am not dropping any of the 5 boundary-types. A narrower "only classical
length boundaries" would bias toward finding hits on known-highlighted
transitions; a narrower "only Meccan-Medinan" would ignore the
muqaṭṭāʿat architecture that [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] explicitly interprets as
book-marking. All five types are pre-justified by classical or
philological tradition; including all is the honest ex-ante choice.

### Why K = 15 top-jump?

Team-lead-specified and I am accepting. A smaller K would reduce power;
a larger K would dilute (by construction, as K → 113 the intersection
trivially → |B|). K=15 is in the sweet-spot of "top ~13% largest jumps"
and Bonferroni-safe.

### Why hypergeometric (not permutation) for primary?

Exact: the sampling (top-15 by distance) selects 15 pairs from 113, and
under the null "top-15 choice is unrelated to B-membership",
membership follows exactly the hypergeometric. No simulation needed,
no monte-carlo noise. This is the correct null.

## Failure modes and how they will be reported

| Scenario | Report |
|---|---|
| `|M ∩ B| ≥ 12` AND `p_secondary_A < 0.0167, T > 0` AND MW-5 OK | **PASS-DIRECTED** (novel test, awaits cross-feature replication) |
| `|M ∩ B| ≥ 12` but secondary A fails | PASS-PRIMARY-ONLY; qualified |
| `|M ∩ B| ≤ 11` (primary fail) | **NULL**: mushaf's large-jump residuals DO NOT concentrate at pre-committed structural boundaries. Publish with equal prominence. |
| `T < 0` significantly | SIGN-REVERSAL-EXPLORATORY; B-pairs have systematically SMALLER distances than non-B-pairs. File as new H-NEW-130.1 if interesting. |
| MW-5 fails (`M' = M`) | INSTRUMENT-BROKEN; primary inadmissible. |

## Post-hoc-noticed disclosure

This hypothesis was NOT eyeballed. It arose from abstract residual-analysis
logic (if the parent shows 11% sub-optimality, examine where). I did
NOT view consecutive-pair distances or rank them before writing this
pre-reg. The D-matrix is from the parent finding and was previously
viewed only at aggregate statistics (mean, min, max, median), not per-pair.

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_130_fisher_rao_residuals.py` (seed 20260417,
   deterministic).
3. JSON `findings/phase-b-hypotheses/csv/h-new-130.json` with
   top-15-jump list, `|M ∩ B|`, p-values, MW-5 synthetic-control output,
   full boundary-set listing.
4. Findings `findings/phase-b-hypotheses/h-new-130-fisher-rao-residuals.md`.
5. Journal `journal/h-new-130-run-1.md`.
