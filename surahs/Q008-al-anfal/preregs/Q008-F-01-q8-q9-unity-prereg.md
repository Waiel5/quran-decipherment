---
surah: 8
test_id: Q008-F-01
title: Empirical adjudication of the Ibn ʿAbbās "Q 8 + Q 9 = one surah" classical claim
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q008-F-01-q8-q9-unity
alpha_bon: 0.01667
---

# Q008-F-01 — Pre-registration: Q 8 + Q 9 unity test

## 1. Hypothesis (locked before observation)

The classical Ibn ʿAbbās tradition (preserved by al-Tirmidhī ≈ #3086 via Yazīd al-Fārisī → Ibn ʿAbbās → ʿUthmān; cataloged in al-Suyūṭī *al-Itqān* nawʿ 18 *fī ʿadad suwar al-Qurʾān*) holds that Q 8 al-Anfāl + Q 9 al-Tawba originally constitute ONE surah, with the canonical basmala-omission as the textual signal of unity. The classical claim has a STRONG reading (literal one-surah identity) and a WEAK reading (al-Biqāʿī thematic-legal continuity).

**Direction of test**: under the STRONG reading, Q 8 + Q 9 should be empirically MORE-SIMILAR than typical adjacent pairs in the corpus, on multiple axes. Specifically:
- **H1 (locked direction):** d_FR(Q 8, Q 9) is in the BOTTOM DECILE of adjacent-pair Fisher-Rao distances (rank ≤ 11 of 113).
- **H2 (locked direction):** Q 8 → Q 9 mushaf canonical-adjacency cost (delta_raw) is in the SEAMLESS-CLAMPED-ZERO set (delta_raw ≤ 0; corpus has 13 such pairs).
- **H3 (locked direction):** root-Jaccard(Q 8, Q 9) is the corpus-MAX of all-pair Jaccard ranks (rank 1 of 6,441 pairs).

**H0 (joint):** Q 8 + Q 9 are TYPICAL Medinan-pair, with all 3 axes returning rank > strict-threshold.

**Pre-commit violation flag**: If d_FR(Q 8, Q 9) > corpus median (≥0.816), the STRONG reading is at-least-partially refuted at axis A.

## 2. Operational definition

- **Source data**: pre-computed FR matrix from `findings/phase-b-hypotheses/csv/h-new-111.json` (`D_matrix_upper_triangular`); pre-computed adjacency-cost from `findings/phase-b-hypotheses/csv/h-new-720.json`; root-distribution from `data/morphology/root-index.json`.
- **Axis A — FR distance**: d_FR(s, t) is the pre-registered Fisher-Rao distance between root-distributions of surah s and surah t. The 113 adjacent-pair distribution is computed from `D_matrix_upper_triangular` for all (s, s+1) with s ∈ {1, ..., 113}.
- **Axis B — adjacency cost**: delta_raw and fraction_residual from H-NEW-720 per_adjacency entry for s = 8 (i.e., Q 8 → Q 9 transition).
- **Axis C — root-Jaccard**: J(s, t) = |R_s ∩ R_t| / |R_s ∪ R_t| where R_s is the set of QAC roots attested in surah s (per `data/morphology/root-index.json`).
- **Adjacent-pair baseline**: 113 pairs (s, s+1).
- **All-pair baseline**: 6,441 pairs (114 choose 2).

## 3. Test statistic

For each axis, compute Q 8 + Q 9's rank within the relevant baseline.

- Axis A: rank_le_FR = number of adjacent pairs with d_FR ≤ d_FR(Q 8, Q 9). One-tailed p = rank_le_FR / 113.
- Axis B: classification ∈ {seamless-clamped-zero, modest-cost, expensive}.
- Axis C: rank_J_adj = rank in adjacent pairs by Jaccard descending; rank_J_all = rank in all 6,441 pairs.

## 4. Permutation null

Each axis already has its empirical reference distribution baked in (the 113 adjacent-pair distribution; the 13-clamped-zero set; the 6,441 all-pair Jaccard distribution). No additional permutation null is needed beyond the rank-test.

For Axis A, additional null: 10,000 random adjacent-pair selections within the 113-set, computing d_FR of each. Test: how often does a random adjacent pair have d_FR ≤ d_FR(Q 8, Q 9)?
- For Axis C, additional null: 10,000 random surah-pairs, Jaccard distribution.

## 5. Success / Failure

- **CONFIRMED (STRONG-Ibn-ʿAbbās)**: H1 + H2 + H3 all pass at α_bon = 0.01667 (Bonferroni-3).
- **DIRECTIONAL**: H1 (rank ≤ 11) AND H2 (clamped-zero) pass; H3 fails.
- **NULL (FALSIFIES STRONG-Ibn-ʿAbbās)**: any of H1 / H2 / H3 fails.
- **PRE-COMMIT VIOLATION**: d_FR(Q 8, Q 9) > corpus-adjacent-median (>0.816) — direction-reversed; the STRONG-reading is empirically inconsistent.

## 6. Honest limits known a priori

- The empirical-anchor extraction during pre-flight observed d_FR(Q 8, Q 9) = 0.911 BEFORE the formal pre-reg lock (per the existing `00-overview.md` and H-NEW-890 T1 finding). The H-NEW-890 T1 result is already in the project's empirical record at NULL. Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol":
  - This pre-reg is a FORMAL re-statement of an already-tested hypothesis.
  - Single-test α=0.05 cap applies for the post-hoc noticing.
  - Verdict ceiling = **PASS-DIRECTED for falsification** (the falsification is an empirically-observed signal that this pre-reg formalizes).
- The Bonferroni-3 (across the 3 axes) uses α_bon = 0.01667; for the rank-tests this is structurally-already-incorporated into the test statistic.
- **Falsification of STRONG reading does NOT FALSIFY the WEAK reading** (al-Biqāʿī thematic-continuity); see `05-classical-claims-audit.md` Claim 1 for the distinction.

## 7. Rules-tuple

`(no-tashkeel, FR-on-roots, mushaf-canonical-adjacency-cost, root-Jaccard, basmala-counted-only-in-Q1, Hafs-Kufan, all-pair-baseline, adjacent-pair-baseline)`.

## 8. Bonferroni

k = 3 (3 axes); α_bon = 0.01667.

## 9. Coordination

This is the Q 8 specialist's primary empirical-adjudication test. Q 9 specialist (Q009-al-tawba) has Q009-F-03 on the Q 9 → Q 10 boundary; no duplication.

## 10. SHA256 lock

Computed at write-time from this file's text content (excluding this section); embedded into `scripts/Q008_F_01_q8_q9_unity.py`; verified at runtime.
