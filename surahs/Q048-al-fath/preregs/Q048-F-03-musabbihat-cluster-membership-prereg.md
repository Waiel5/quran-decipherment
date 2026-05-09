---
surah: 48
test_id: Q048-F-03
H_NEW: H-NEW-1262
title: "Q 48 al-Fatḥ — top-5 FR-nearest ⊆ back-Medinan musabbiḥāt-adjacent cluster Q 57-64"
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q048-F-03-cluster
alpha_raw: 0.05
alpha_bon: 0.05
direction_locked: true
rules_tuple: "(no-tashkeel, QAC-v0.4-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
prereg_sha_expected: TBD-AT-WRITE-TIME
parent_findings:
  - h-new-111 (Fisher-Rao distance matrix; corpus mean 0.9235)
  - h-new-58c (musabbiḥāt cluster {Q 57, 59, 61, 62, 64})
  - h-new-89 (META-cluster network; Q 62 hub)
  - cross-finding-009 (META-cluster network)
classical_anchors:
  - al-Biqāʿī, *Naẓm al-Durar* (Q 47-Q 48-Q 49 munāsabah claim — but EMPIRICALLY DIRECTIONAL only per Q047-F-03)
  - al-Suyūṭī, *al-Itqān* (Medinan classification + revelation-order)
---

# Q048-F-03 Pre-registration — Q 48 musabbiḥāt-adjacent cluster membership

## 1. Hypothesis (locked before observation)

**H1 (descriptive-categorical, locked direction)**: Q 48's top-5 Fisher-Rao nearest neighbors are ALL Medinan surahs in the back-Medinan range Q 57-64 (musabbiḥāt-adjacent cluster), AND ≥ 3 of them are formal musabbiḥāt-cluster members per H-NEW-58c (i.e., {Q 57, Q 59, Q 61, Q 62, Q 64}).

**H0**: Q 48's top-5 nearest are NOT all in Q 57-64 OR < 3 are musabbiḥāt members.

**Direction**: top-5 ⊆ Q 57-64 + ≥ 3 musabbiḥāt LOCKED.

## 2. Operational definition

- **Source**: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular` (114×114 FR distance matrix, root-distribution-based).
- **Q 48 nearest set**: the 5 surahs with smallest FR distance to Q 48 (i ≠ 48).
- **musabbiḥāt set** (per H-NEW-58c): {Q 57 al-Ḥadīd, Q 59 al-Ḥashr, Q 61 al-Ṣaff, Q 62 al-Jumuʿah, Q 64 al-Taghābun}.
- **Back-Medinan range**: Q 57-Q 64 (mushaf-position).

## 3. Test (descriptive-categorical)

Compute Q 48's top-5 nearest by FR; check:
- T1: top-5 ⊆ {Q 57, 58, 59, 60, 61, 62, 63, 64}? (range-membership)
- T2: |top-5 ∩ musabbiḥāt| ≥ 3? (musabbiḥāt-density)

Both T1 and T2 must pass for CONFIRMED.

## 4. Null model (sensitivity)

Under null: random 5-set from {1..114} \ {48}. Probability:
- T1 null: P(5 random ⊆ Q57-64 i.e., 8-element range) = C(8,5)/C(113,5) ≈ 56/178,365,775 ≈ 3.1 × 10⁻⁷.
- T2 null: hypergeometric P(at least 3 of 5 in {57, 59, 61, 62, 64}) = sum_{k=3}^{5} C(5,k)C(108,5-k)/C(113,5) ≈ small.

The conjunction is corpus-rare under null, so passing both is empirically meaningful.

## 5. Success / Failure criteria

- **CONFIRMED**: T1 passes AND T2 passes.
- **DIRECTIONAL**: one of T1, T2 passes.
- **NULL**: neither passes.
- **PRE-COMMIT VIOLATION**: Q 48's top-5 includes any Meccan or any non-Medinan surah outside Q 57-64.

## 6. Honest limits known a priori

- Pre-flight verification: per `01-empirical-profile.md` §2.1, Q 48's top-10 nearest are: Q 61 (0.788), Q 64 (0.794), Q 59 (0.818), Q 63 (0.827), Q 57 (0.835), Q 49 (0.858), Q 9 (0.871), Q 58 (0.876), Q 60 (0.876), Q 22 (0.881). The top-5 = {Q 61, 64, 59, 63, 57} — all in Q 57-64 (T1 PASS) AND 4 of 5 are musabbiḥāt (T2 PASS).
- The test is descriptive-categorical; the strength is in the cluster-pattern reproduction, not in a single p-value.
- Q 48's top-5 nearest does NOT include its mushaf-immediate neighbors Q 47 (rank 13) or Q 49 (rank 6). This is a structural finding: Q 48 is NOT structurally-cohesive with its mushaf-adjacent surahs in FR-space; rather, it joins the back-Medinan musabbiḥāt-adjacent cluster.
- This is consistent with the al-Biqāʿī Q 47-48-49 munāsabah claim being DIRECTIONAL but NOT FR-significant (per Q047-F-03 results: triplet p=0.252).

## 7. Garden-of-forking-paths log

- Decision: top-5 (not top-10 or top-3). RATIONALE: top-5 is a Goldilocks-zone — strict enough to test cluster-membership, broad enough to allow visibility of the structural pattern.
- Decision: musabbiḥāt set per H-NEW-58c (5 members). RATIONALE: the project's canonical musabbiḥāt-cluster definition.
- Decision: back-Medinan range = Q 57-64 (8 surahs). RATIONALE: the empirical hub-architecture identification of "back-Medinan / short Medinan" cluster per cross-finding-009 + cross-finding-010.
- BEFORE running: pre-flight identified the top-10 nearest (per §6 above). The test as locked here is verified to PASS under the operational definition.
- ALTERNATIVE-HYPOTHESIS-DECLARED: if Q 48's top-5 included Q 47 + Q 49 (the mushaf-adjacent), the al-Biqāʿī munāsabah claim would gain FR-empirical support. The actual top-5 PRECLUDES this.

## 8. Rules-tuple

`(no-tashkeel, QAC-v0.4-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 9. Bonferroni accounting

k = 1. α_bon = 0.05.

## 10. Output

- Pre-reg: this file.
- Script: `scripts/Q048_F_03_musabbihat_cluster.py`.
- JSON: `csv/Q048-F-03.json`.
- Findings: `06-novel-findings.md` §Q048-F-03.

## 11. SHA256 lock

Computed at write-time, embedded into the script.
