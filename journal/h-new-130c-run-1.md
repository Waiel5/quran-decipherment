# Journal — H-NEW-130c run 1

**Date**: 2026-04-17
**Specialist**: specialist-a
**Task**: T-L — H-NEW-130c verse-length third-feature replication
**Seed**: 20260417

## Sequence

1. TaskList + TaskGet #19 confirmed T-L spec.
2. Inspected h-new-111c.json — same flat `D_matrix_upper_triangular` schema.
3. Wrote pre-reg with identical frozen elements (B, K=15, threshold ≥12). Added secondary B as 3-way intersection for universal-hinges identification (new cell specific to 3rd feature).
4. Wrote script as thin wrapper reusing H-NEW-130 helpers via import.
5. Executed seed 20260417.

## Results

- **Primary**: 13/15 hit B on verse-length D-matrix. p = 1.16×10⁻³. PASS.
- **Secondary A**: T = +0.385 (strongest of 3), p = 1×10⁻⁴. PASS.
- **Secondary B (3-way intersection)**: 3 universal hinges. PASS threshold ≥3.
- **MW-5**: discriminative (0 overlap with synth sort-by-length).

## Universal hinges

{(14, 15), (49, 50), (56, 57)} appear in top-15 of roots, char-4-grams, AND verse-length.

## 2 non-B rhythm top-15 pairs

Q 73→74 and Q 96→97 are in verse-length top-15 but not in B. Both within short-mufaṣṣal, both Early-Meccan, both muq-free. Rhythm-specific discontinuities — not false positives, but signals that verse-length axis has SOME structure beyond the 5 pre-committed boundary types.

## Verdict

TRIPLE-REPLICATION-CONFIRMED. H-NEW-130 CONFIRMED status reinforced.

## Files

- Pre-reg, script, JSON, findings all written.
- Next: T-L.1 (reverse mushaf), L.2 (universal-hinges catalog — already in the JSON output), L.3 (wrap-around interaction), L.4 (cross-corpus).
