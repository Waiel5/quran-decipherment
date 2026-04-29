---
finding_id: h-new-130c
title: "Fisher-Rao residuals THIRD-FEATURE replication on verse-length-histogram D-matrix"
specialist: specialist-a
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 3
bonferroni_family: h-new-130c-residuals-verselen
alpha_bon: 0.0167
alpha_raw: 0.05
direction_primary: "Under verse-length-histogram D-matrix (from H-NEW-111c), of the top-15 largest Fisher-Rao consecutive-pair distances in mushaf order, ≥12 (80%) coincide with the pre-committed structural-boundary set B (|B|=54 of 113 pairs, IDENTICAL to H-NEW-130/130b). Hypergeometric one-sided upper-tail."
direction_secondary_concentration: "Mean verse-length-histogram Fisher-Rao consecutive-distance at B-pairs > mean at non-B-pairs (two-sided perm null, 10K, sign locked positive)."
direction_secondary_triple_overlap: "3-way top-15 intersection among root (H-NEW-130), char-4-gram (H-NEW-130b), and verse-length (H-NEW-130c) is larger than chance. Descriptive for now; inferential claim: |M_root ∩ M_char ∩ M_vlen| ≥ 3 (under trivial null expected ~0.03)."
K_top_pairs: 15
boundary_set_cardinality: 54
rules_tuple: "(no-tashkeel, whitespace-tokenized verse text, basmala-counted-only-in-surah-1 via text, mushaf order, Hafs-Kufan)"
parent_finding_primary: h-new-130
parent_finding_dmatrix: h-new-111c
verdict_ceiling: "If primary passes AND secondary A passes → TRIPLE-REPLICATION-CONFIRMED (root + char-4-gram + verse-length). If primary fails → REPLICATION-PARTIAL (feature-specific)."
---

# [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] — Fisher-Rao residuals THIRD-FEATURE replication on verse-length-histogram D-matrix

## Motivation

[[h-new-130-fisher-rao-residuals|H-NEW-130]] (roots, PASS-DIRECTED) and [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] (char-4-grams, REPLICATION-CONFIRMED) established that the mushaf's 15 largest Fisher-Rao consecutive-surah jumps coincide with a pre-committed structural-boundary set B at hypergeometric p = 4.78×10⁻⁶ on both feature spaces. [[h-new-130-fisher-rao-residuals|H-NEW-130]] has thereby promoted to CONFIRMED.

This test runs the same analysis on the THIRD feature space: verse-length-histogram Fisher-Rao D-matrix from [[h-new-111c-fisher-rao-verselen|H-NEW-111c]]. [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] showed PARTIAL-PASS at the parent level (primary p < 10⁻⁴, but ratio L/L_2opt = 2.71 — NOT near-optimal; rhythm differs structurally from content). The residual structure may behave differently.

Possible outcomes:
1. **Primary passes k ≥ 12** → TRIPLE-REPLICATION. Exceptionally strong claim: mushaf places structural-boundary jumps at the same 15 hinges regardless of whether we measure content (roots), register (char-4-grams), or rhythm (verse-length).
2. **Primary passes partial (9-11)** → RHYTHM-AXIS-PARTIAL. Most hinges hit B but not all 12; rhythm places some jumps at non-B positions (possibly surah-length-discontinuities internal to the mushaf, independent of content boundaries).
3. **Primary fails (≤8)** → RHYTHM-SPECIFIC RESULT. Boundary-marking is a CONTENT phenomenon, not a RHYTHM phenomenon. Would be a genuinely new finding, consistent with [[h-new-111c-fisher-rao-verselen|H-NEW-111c]]'s verse-length-specific behavior already differing from content.

Publishing all three outcomes with equal prominence.

## Hypothesis

**Primary (H1).** Under [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] verse-length-histogram D-matrix, top-15 Fisher-Rao consecutive-surah jumps ∩ B ≥ 12. Hypergeometric p ≤ 0.0073. One-sided upper-tail.

**Secondary A (H2).** Mean verse-length Fisher-Rao distance at B-pairs > mean at non-B-pairs. Two-sided 10K perm; sign locked positive for PASS.

**Secondary B (H3, descriptive but pre-locked).** 3-way top-15 intersection `|M_root ∩ M_char ∩ M_vlen| ≥ 3`. This is the universal-hinges test: hinges that appear in ALL three feature spaces are "maximally robust". Cardinality-3 threshold is conservative given the null expected ~0.03 for three independent 15-of-113 selections.

## Pre-committed structural-boundary set B

**IDENTICAL to [[h-new-130-fisher-rao-residuals|H-NEW-130]] and [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]].** |B| = 54 of 113 pairs. Loaded via the same `build_boundary_set()` function in `scripts/h_new_130_fisher_rao_residuals.py`. No modification.

## Method (locked before results viewed)

### Data
- D-matrix: `D_matrix_upper_triangular` from `findings/phase-b-hypotheses/csv/h-new-111c.json`.
- Boundary set B: `build_boundary_set()` from [[h-new-130-fisher-rao-residuals|H-NEW-130]] script (import, not copy).
- Reference top-15 sets: `findings/phase-b-hypotheses/csv/h-new-130.json` (roots) and `[[h-new-130b-fisher-rao-residuals-char4gram|h-new-130b]].json` (char-4-gram).

### Primary test
1. `d_i = D_vlen[i, i+1]` for i=1..113.
2. Rank descending, take top-15 `M_vlen`.
3. `|M_vlen ∩ B|`.
4. Null: hypergeometric(113, 54, 15). p = P(X ≥ observed).
5. PASS at k ≥ 12.

### Secondary A — concentration
Same as [[h-new-130-fisher-rao-residuals|H-NEW-130]]: T = mean_B − mean_notB; 10K perm null; sign locked positive.

### Secondary B — 3-way top-15 intersection
1. Load root top-15, char-4-gram top-15.
2. Compute `M_root ∩ M_char ∩ M_vlen`.
3. Report cardinality and list. Pre-committed threshold ≥ 3 for "universal-hinge" claim.

### MW-5 discriminativeness
Synthetic sort-by-verse-count ordering on verse-length D-matrix. Top-15 under synth must differ from M_vlen. Identical → INSTRUMENT-BROKEN.

### MW-1 length control
This feature space is ABOUT verse-length distribution, so "length" is the SIGNAL, not the confound. Length is not residualized; the D-matrix is between per-surah histograms of verse-length bins, L1-normalized. Discuss in findings how this changes the MW-1 framing: here MW-1 is built-in differently (distribution-shape, not total-length).

## Acceptance windows

- **PRIMARY PASS (k ≥ 12)** → TRIPLE-REPLICATION-CONFIRMED
- **PRIMARY PARTIAL (9 ≤ k ≤ 11)** → RHYTHM-PARTIAL
- **PRIMARY FAIL (k ≤ 8)** → RHYTHM-AXIS-DIFFERS; publish with equal prominence
- **SECONDARY A PASS**: p < 0.0167, T > 0
- **SECONDARY B UNIVERSAL-HINGES**: |triple-intersection| ≥ 3 (publish the list regardless)

## Garden of forking paths

- B FROZEN from [[h-new-130-fisher-rao-residuals|H-NEW-130]]. No modification.
- K_top = 15 FROZEN.
- Threshold ≥ 12 FROZEN.
- Bonferroni-3 family.
- 3-way intersection is a DESCRIPTIVE cell; its ≥3 threshold is pre-committed as a "universal-hinges" label trigger, not an inferential p-value.

## Failure modes

| Scenario | Report |
|---|---|
| Primary ≥12, Sec A pass, Sec B ≥3 | TRIPLE-REPLICATION-CONFIRMED + universal-hinges identified |
| Primary ≥12, Sec A pass, Sec B <3 | REPLICATION-CONFIRMED but no universal-hinges (unexpected; would mean each feature picks different top-15) |
| Primary 9-11 | RHYTHM-PARTIAL |
| Primary ≤8 | REPLICATION-FAILED on verse-length axis; [[h-new-130-fisher-rao-residuals|H-NEW-130]] CONFIRMED status unchanged (already CONFIRMED on two feature spaces); document as feature-specific partial generalization |
| MW-5 fails | INSTRUMENT-BROKEN |

## Post-hoc-noticed disclosure

Pre-reg written BEFORE inspecting per-pair distances d_vlen[i, i+1]. I've seen only aggregate [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] stats (mean, min, max, median) from its JSON schema, and the ratio L/L_2opt = 2.71 published in its findings file. No individual consecutive-pair verse-length distance has been viewed.

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_130c_fisher_rao_residuals_verselen.py`.
3. JSON `findings/phase-b-hypotheses/csv/h-new-130c.json`.
4. Findings `findings/phase-b-hypotheses/h-new-130c-fisher-rao-residuals-verselen.md`.
5. Journal `journal/h-new-130c-run-1.md`.
