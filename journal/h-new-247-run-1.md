# h-new-247-run-1 — Palindromic surah-pair symmetry test

**Specialist**: h-new-247-specialist
**Date**: 2026-04-17
**Task**: H-NEW-247 (Wave-5) — test whether surahs at positions k and 115-k
are structurally paired across 4 feature spaces.
**Parent**: cross-finding-013 (mushaf topological ring, CONFIRMED)
**Sibling**: h-new-204 (reverse-mushaf boundary Spearman, NULL)

## Orientation

- Read cross-finding-013 in full (three-layer ring architecture: Layer 1
  geodesic path, Layer 2 wrap-around, Layer 3 structured hinges).
- Read h-new-204 JSON (primary symmetry verification PASS; secondary
  mirror-Spearman NULL at ρ = -0.051, p = 0.72).
- Identified parent D-matrix (K=500 QAC-STEM roots) in
  `findings/phase-b-hypotheses/csv/h-new-111.json`
  (D_matrix_upper_triangular, 6441 entries, sha256
  4c366c4...5d7f33fc).
- Identified canonical 29 muqaṭṭaʿāt list from existing scripts.

## Pre-registration

- 4 cells, Bonferroni k=4, α_bon = 0.0125.
- Cell (a): mean FR over 57 pairs, one-sided lower.
- Cell (b): mean shared top-50 roots, one-sided upper.
- Cell (c): muq-concordance count, one-sided upper.
- Cell (d): Spearman(log n_v(k), log n_v(115-k)), one-sided upper.
- Seed 20260419, N_perms = 1000.
- Direction: POSITIVE palindromic effect expected on all 4 cells.
- Pre-reg sha256 emitted at run:
  `721e241bd0eb33480594f6732ae051af44b1c50a577a94b3f9e28864ab3c2b2a`

Pre-reg filed BEFORE execution; no amendments.

## Execution

Single run, deterministic under seed 20260419. Runtime ~10s.

## Results

| Cell | Observed | Null mean | z | p | Verdict |
|:-:|---:|---:|---:|---:|:-:|
| (a) FR | 1.0467 | 0.9231 | +6.39 | 1.000 | NULL (anti) |
| (b) shared roots | 8.72 | 11.00 | −5.04 | 1.000 | NULL (anti) |
| (c) muq concord | 28 | 35.42 | −2.61 | 1.000 | NULL (anti) |
| (d) log-len Spearman | −0.466 | 0.0004 | −3.52 | 1.000 | NULL (anti) |

**0/4 PASS**. All four cells register significant anti-palindromic
effects — palindromic pairs are LESS structurally similar than random.

## Key observations

- **Q 1 ↔ Q 114** is the FR-closest palindromic pair at d=0.388 (the
  known cross-finding-013 wrap-around); the next palindromic pair
  (Q 49 ↔ Q 66) is at corpus mean 0.81. No palindromic structure
  beyond the single terminal edge.
- **Both-muq pairs: 0 / 57**. All 29 muq surahs sit in Q 1-68; only
  3 of 29 are past Q 50. Palindromic partners are almost all short
  non-muq back-half surahs.
- **Length-reflection Spearman = −0.466**: long-first-half surahs
  pair with short-back-half surahs (maximally anti-similar on
  length). This is the mechanistic driver of the anti-palindromic
  direction across all length-sensitive cells.

## Sensitivity

Leave-Q1-out: all 4 observed stats drift slightly further from PASS
direction. The 0/4 result is a global property, not a terminal-pair
artifact.

## MW-5 control

Random-pair z-scores center at 0 by construction (confirmed via
null_mean ≈ observed_null_mean for null draw self-statistics). Null
is not broken.

## Interpretation

The mushaf is a ring (CONFIRMED by cross-finding-013) but is NOT a
palindromically folded ring. The wrap-around edge (Q 1 ↔ Q 114) is
a single short edge completing an otherwise non-symmetric cycle. No
Layer 4 (folded ring) exists.

Consistent with H-NEW-204 boundary-mirror Spearman NULL. Strengthens
"no reflective symmetry about midpoint" at the surah-level across 4
feature spaces.

## Honest limits

- N=57 is small; 1000 perms is Bonferroni-adequate but not sub-α=0.001
  resolution.
- Palindromic k↔115-k is ONE symmetry; block-wise and other folds
  not tested.
- Length covariance dominates cells (a), (b), (d); cell (c) is the
  only length-independent cell and shows the weakest (but still
  significant) anti-signal.

## Deliverables shipped

- Pre-reg: `findings/phase-b-hypotheses/h-new-247-palindromic-symmetry-prereg.md`
- Script: `scripts/h_new_247_palindromic.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-new-247.json`
- Findings: `findings/phase-b-hypotheses/h-new-247-palindromic-symmetry.md`
- Journal: this file.
- MASTER-LEDGER: Wave-5 entry pending (added post-journal).

## Audit notes

- Bonferroni k=4 applied per pre-reg; no post-hoc k-adjustment.
- Directional primary pre-committed (POSITIVE on all 4 cells); the
  anti-direction observed is reported honestly as NULL on the
  pre-registered direction, with descriptive mention of the
  anti-direction magnitude. No "rescue" via two-sided re-test.
- No inflated-independence claim; cells share length-covariance
  substrate.
- Classical anchors cited: al-Suyūṭī (Itqān) and Farāhī-Iṣlāḥī
  (Niẓām al-Qurʾān) as SECONDARY-TRIANGULATED — neither proposes
  palindromic pairing; our NULL aligns with their actual positions.
  No verbatim quotation from unverified sources.
