---
finding_id: h-new-130b
title: "Fisher-Rao residuals CROSS-FEATURE replication on char-4-gram D-matrix"
specialist: specialist-a
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 3
bonferroni_family: h-new-130b-residuals-char4gram
alpha_bon: 0.0167
alpha_raw: 0.05
direction_primary: "Under char-4-gram D-matrix (from H-NEW-111b), of the top-15 largest Fisher-Rao consecutive-pair distances in mushaf order, ≥12 (80%) coincide with the pre-committed structural-boundary set B (|B|=54 of 113 pairs, IDENTICAL to H-NEW-130). One-sided upper-tail hypergeometric. Also report permutation-null p on 10K random 15-pair selections as a robustness check."
direction_secondary_concentration: "Sum of mushaf-consecutive char-4-gram distances at B-pairs / sum at non-B-pairs is larger than expected under random B-label assignment (10K perms). Two-sided. Sign-locked positive for PASS."
direction_secondary_replication: "Top-15 largest-jump SETS overlap between H-NEW-130 (QAC-STEM) and H-NEW-130b (char-4-gram) is larger than random-pair expectation. This is the explicit CROSS-FEATURE replication cell."
K_top_pairs: 15
boundary_set_cardinality: 54
rules_tuple: "(no-tashkeel, char-4-grams with spaces, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)"
parent_feature_tuple: "(no-tashkeel, QAC-STEM roots, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)"
perms_for_secondary: 10000
verdict_ceiling: "CONFIRMED (primary claim) if H-NEW-130b replicates at k>=12 on char-4-gram D-matrix; otherwise REPLICATION-PARTIAL or REPLICATION-FAILED"
parent_finding_primary: h-new-130
parent_finding_dmatrix: h-new-111b
---

# [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] — Fisher-Rao residuals CROSS-FEATURE replication on char-4-gram D-matrix

## Motivation

[[h-new-130-fisher-rao-residuals|H-NEW-130]] (PASS-DIRECTED, 2026-04-17) established that all 15 of the 15
largest Fisher-Rao consecutive-surah distances in the mushaf coincide
with a pre-committed structural-boundary set B, under the **QAC-STEM
root-distribution** Fisher-Rao D-matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]. Per project
discipline, novel-test verdicts are PASS-DIRECTED until independent
replication on a distinct feature space.

[[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] repeats the test on the **char-4-gram** Fisher-Rao D-matrix
from [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]. [[cross-finding-011-mushaf-fisher-rao-confirmed|Cross-finding-011]] established that the parent geodesic
claim (mushaf L/L_2opt ≈ 1.11) replicates across both feature spaces
with z-matching to within 0.4%. [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] asks whether the *residual
boundary-concentration* structure also replicates.

If k ≥ 12 / 15 is reproduced on char-4-grams: [[h-new-130-fisher-rao-residuals|H-NEW-130]] promotes to
CONFIRMED. If not: partial-replication or failed-replication,
reported with equal prominence.

## Hypothesis

**Primary (H1).** Under [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] char-4-gram D-matrix, of the 15
largest Fisher-Rao consecutive-surah distances in mushaf order,
a significantly larger fraction coincides with the pre-committed
structural-boundary set B than the hypergeometric null expectation.
Primary pass: |M ∩ B| ≥ 12.

**Secondary A (H2, descriptive-concentration).** Mean char-4-gram
Fisher-Rao consecutive-distance at B-pairs is larger than mean at
non-B-pairs under a two-sided permutation null (10K perms). Sign
locked positive for PASS.

**Secondary B (H3, cross-feature top-15 overlap).** The top-15 sets
from [[h-new-130-fisher-rao-residuals|H-NEW-130]] (roots) and [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] (char-4-grams) overlap more
than chance would predict. Hypergeometric test with N=113, K=15
(mushaf root top-15), n=15 (mushaf char-4-gram top-15). PASS at
overlap ≥ 6 (hypergeom p = 0.00031 under null K=15, n=15, N=113).

## Pre-committed structural-boundary set B

**IDENTICAL to [[h-new-130-fisher-rao-residuals|H-NEW-130]].** |B| = 54 of 113 consecutive-surah pairs.
Computed deterministically from the same 5 boundary-types (classical
length, Meccan↔Medinan, Nöldeke phase, muqaṭṭāʿat presence,
muqaṭṭāʿat letter-set). The boundary-set is DATA-FROZEN from [[h-new-130-fisher-rao-residuals|H-NEW-130]]
with no modification; this is a pure feature-space replication.

Full list re-computed by the same `build_boundary_set()` function as
in `scripts/h_new_130_fisher_rao_residuals.py`. No new boundary-types
are added.

## Method (locked before results viewed)

### Data

- D-matrix: load `D_matrix_upper_triangular` from
  `findings/phase-b-hypotheses/csv/h-new-111b.json` (char-4-gram
  Fisher-Rao, parent-frozen).
- Boundary set B: re-computed by the same function used in [[h-new-130-fisher-rao-residuals|H-NEW-130]];
  independent of D-matrix.
- [[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 set: loaded from
  `findings/phase-b-hypotheses/csv/h-new-130.json` for Secondary B
  cross-feature overlap test.

### Primary test

1. Compute `d_i = D_char[i, i+1]` for `i = 1..113`.
2. Rank pairs by `d_i` descending. Take top-15 set `M_char`.
3. Compute `|M_char ∩ B|`.
4. **Null 1 (hypergeometric)**: `p = P(X ≥ |M_char ∩ B|)` under
   Hypergeometric(N=113, K=54, n=15). Exact, no simulation.
5. **Null 2 (permutation robustness, per team-lead request)**:
   10,000 random 15-pair selections without replacement from the 113
   pairs; count fraction with overlap ≥ observed. Should match the
   hypergeometric exactly (different RNG confirms no computational
   bug).
6. **PASS**: `p_primary_hg < α_bon = 0.0167`. This corresponds to
   `|M_char ∩ B| ≥ 12`.

### Secondary A — concentration

Same structure as [[h-new-130-fisher-rao-residuals|H-NEW-130]] Secondary A, but on char-4-gram distances.
T = mean(d_char on B) − mean(d_char on notB); 10K perms; sign locked
positive.

### Secondary B — cross-feature top-15 overlap

1. Load [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s top-15 set `M_root` from [[h-new-130-fisher-rao-residuals|h-new-130]].json.
2. Compute overlap `|M_char ∩ M_root|`.
3. **Null**: hypergeometric with N=113, K=|M_root|=15, n=|M_char|=15.
   `p = P(X ≥ overlap)` one-sided upper-tail.
4. **PASS**: `p_secondary_B < α_bon = 0.0167`. This corresponds to
   overlap ≥ 5 (exact hypergeom).

### MW-5 positive control (inherited discriminativeness)

Re-run the sort-by-length synthetic-ordering discriminativeness check
on the char-4-gram D-matrix. Top-15 under synthetic ordering must
differ from mushaf's top-15 char-4-gram set; if identical, instrument
broken.

### MW-1 length control

Inherited from [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] (char-4-gram distributions are L1-normalized
at the per-surah simplex level, removing total surah-length scale).

## Pre-committed acceptance windows

- **PRIMARY PASS**: `|M_char ∩ B| ≥ 12` (hypergeom p ≤ 0.0073).
- **PRIMARY REPLICATION-PARTIAL**: `|M_char ∩ B| ∈ {9, 10, 11}` — raw
  significant (p < 0.05) but Bonferroni-not-significant; report as
  partial.
- **PRIMARY REPLICATION-FAILED**: `|M_char ∩ B| ≤ 8`. Publish as
  REPLICATION-FAILED with equal prominence; [[h-new-130-fisher-rao-residuals|H-NEW-130]] stays
  PASS-DIRECTED-ROOT-ONLY.
- **SECONDARY A PASS**: p < 0.0167 with T > 0.
- **SECONDARY B PASS**: overlap ≥ 5 (hypergeom p ≤ 0.015).
- **CROSS-FINDING PROMOTION**: [[h-new-130-fisher-rao-residuals|H-NEW-130]] primary + [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] primary
  both PASS → [[h-new-130-fisher-rao-residuals|H-NEW-130]] upgrades to CONFIRMED, draft [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]
  (or addendum to [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]).

## Garden of forking paths

### Inherited discipline

- Boundary set B is FROZEN from [[h-new-130-fisher-rao-residuals|H-NEW-130]]. No changes allowed; this is
  pure feature-space replication.
- K_top = 15 is FROZEN. No changes.
- α_bon = 0.0167 is FROZEN (Bonferroni-3 family).
- Threshold ≥ 12 is FROZEN (same 80% threshold as [[h-new-130-fisher-rao-residuals|H-NEW-130]], derived
  from the hypergeometric tail at α_bon=0.0167).

### Novel elements for this replication

- **Secondary B (cross-feature top-15 overlap)** is new at [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]];
  it is only meaningful for a replication test. Its Bonferroni slot
  is the same 3-family as primary + secondary A. No inflation.
- **Permutation-null robustness cell for primary** is new (per
  team-lead request). Two nulls on the same primary test is
  redundant-by-design (they should agree); this is robustness, not
  a new inferential cell, so no additional Bonferroni penalty.

### What's NOT allowed

- Re-picking K_top to optimize replication. FORBIDDEN.
- Adjusting |B| post-replication-check. FORBIDDEN.
- Adding new boundary-types. FORBIDDEN.
- Sign-flipping. PRE-REG-STANDARD-01 applies.

## Failure modes and how they will be reported

| Scenario | Report |
|---|---|
| Primary ≥12, Secondary A pass, Secondary B ≥5 | **REPLICATION-CONFIRMED**; [[h-new-130-fisher-rao-residuals|H-NEW-130]] promotes to CONFIRMED; draft [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] |
| Primary ≥12, Secondary A pass, Secondary B <5 | REPLICATION-PARTIAL: B-concentration replicates but specific top-15 set differs; still enough to elevate [[h-new-130-fisher-rao-residuals|H-NEW-130]] if primary replicates |
| Primary 9-11 (raw-sig but Bonferroni-NS) | REPLICATION-PARTIAL: direction right, magnitude weakened |
| Primary ≤8 | REPLICATION-FAILED; [[h-new-130-fisher-rao-residuals|H-NEW-130]] stays PASS-DIRECTED-ROOT-ONLY; publish with equal prominence |
| MW-5 breaks (synthetic top-15 == mushaf top-15 on char-4-grams) | INSTRUMENT-BROKEN; primary inadmissible |
| Any secondary fails with sign-flip | EXPLORATORY-REVERSE, not demote primary |

## Post-hoc-noticed disclosure

Pre-reg written BEFORE char-4-gram D-matrix D_char[i,i+1] per-pair
distances are viewed. I have viewed aggregate-level char-4-gram
D-matrix statistics only via [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]'s published summary (mean,
min, max, median) while reading its JSON schema to locate the
`D_matrix_upper_triangular` field. No per-pair distance has been
ranked or inspected.

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_130b_fisher_rao_residuals_char4gram.py`
   (seed 20260417, deterministic).
3. JSON `findings/phase-b-hypotheses/csv/h-new-130b.json`.
4. Findings `findings/phase-b-hypotheses/h-new-130b-fisher-rao-residuals-char4gram.md`.
5. Journal `journal/h-new-130b-run-1.md`.
6. If primary+secondary pass: [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] or [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]
   addendum.
