---
surah: 48
test_id: Q048-F-04
H_NEW: H-NEW-1263
title: "Q 48 + Q 30 forward-prophecy structural-pair FR-cohesion test (the 'iʿjāz al-ghayb' pair claim)"
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q048-F-04-prophecy-pair
alpha_raw: 0.05
alpha_bon: 0.05
direction_locked: true
rules_tuple: "(no-tashkeel, QAC-v0.4-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
prereg_sha_expected: TBD-AT-WRITE-TIME
parent_findings:
  - h-new-111 (Fisher-Rao distance matrix)
  - cross-finding-008 (muqaṭṭāʿat as book-introduction markers — Q 30 is a member)
  - cross-finding-015 (classical-doctrine validation pattern)
classical_anchors:
  - al-Suyūṭī, *al-Itqān*, nawʿ 65 (iʿjāz al-Qurʾān; iʿjāz al-ghayb sub-section)
  - al-Khaṭṭābī, *Bayān iʿjāz al-Qurʾān* (theological iʿjāz framework)
  - al-Bāqillānī, *Iʿjāz al-Qurʾān* (structural iʿjāz framework)
---

# Q048-F-04 Pre-registration — Q 48 + Q 30 forward-prophecy pair FR-cohesion test

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction)**: The classical *iʿjāz al-ghayb* pair claim — that Q 48 al-Fatḥ (with v.27 Conquest-of-Mecca prophecy) and Q 30 al-Rūm (with vv. 2-4 Romans-then-victory prophecy) form a structurally-coherent pair of forward-looking falsifiable temporal predictions — is empirically supported at the FR-distance level.

**Operationalization**: FR(Q 48, Q 30) ≤ corpus mean FR (≈ 0.9235), with the pair NOT in Q 48's top-50 farthest neighbors.

**H0**: FR(Q 48, Q 30) is at-or-above corpus mean, indicating the pair is NOT structurally cohesive at FR-distance.

**Direction**: pair-LOW LOCKED.

## 2. Operational definition

- **Source**: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.
- **Q 48 ↔ Q 30 distance**: lookup FR(Q 48, Q 30) from the matrix.
- **Corpus mean FR**: 0.9235 (per project records; verified at runtime by computing the mean of all C(114,2) pair distances).
- **Top-50 farthest from Q 48**: rank Q 48's 113 neighbors by FR; take the 50 farthest.

## 3. Test

T1: FR(Q 48, Q 30) ≤ corpus mean FR (0.9235).
T2: Q 30 NOT in Q 48's top-50 farthest (i.e., Q 30 rank ≤ 63 in Q 48-nearest list).

CONFIRMED if both pass.

## 4. Null model (sensitivity)

Under null: a random pair from the 114×114 matrix has FR ~ corpus mean by definition. The probability of a random pair being below corpus mean is ≈ 0.5 (by symmetry); the probability of being below mean AND not in top-50 farthest of one element is ≈ 0.5 × (63/113) ≈ 0.28.

Empirically meaningful test only if the FR is well below mean (e.g., bottom-quartile ≤ 0.86) and the rank is well in the nearest-half (e.g., rank ≤ 30).

## 5. Success / Failure criteria

- **CONFIRMED**: FR ≤ 0.86 AND rank ≤ 30/113.
- **DIRECTIONAL**: FR ≤ 0.92 AND rank ≤ 56.
- **NULL**: FR > 0.92 OR rank > 56.

## 6. Honest limits known a priori

- The test is asking whether a **classical thematic-content claim** ("Q 48 and Q 30 are paired in *iʿjāz al-ghayb*") is supported by an **empirical structural metric** (FR distance).
- Pre-flight verification (computed before pre-reg lock): FR(Q 48, Q 30) ≈ 1.025 (high; well above corpus mean 0.92). Q 30 rank in Q 48-nearest ≈ 88/113 — Q 30 is FAR from Q 48 in FR-space.
- This means the test is **EXPECTED TO RETURN NULL** at the FR-cohesion level. The classical *iʿjāz al-ghayb* pair claim is THEMATIC, NOT FR-cluster.
- Pre-registering this NULL prediction satisfies project discipline: the project tests classical claims for empirical support and reports NULLs with equal prominence.
- The test is post-hoc-noticed; per HANDOFF/04-DISCIPLINE.md post-hoc protocol, single-test α=0.05 cap.

## 7. Garden-of-forking-paths log

- Decision: use FR (root-distribution Fisher-Rao) as the cohesion metric. RATIONALE: project's primary structural-distance metric.
- Decision: pre-flight value FR(Q48, Q30) ≈ 1.025 KNOWN before lock. The pre-reg LOCKS the prediction direction (LOW = cohesion-supporting), with the expected outcome being NULL (because the actual value is HIGH).
- ALTERNATIVE-HYPOTHESIS-DECLARED: if Q 48 + Q 30 are FR-close, the classical *iʿjāz al-ghayb* pair claim gains FR-cluster support; if FAR (the empirical case), the pair is THEMATIC-only.
- This pre-reg is a canonical example of using PRE-REGISTRATION DISCIPLINE to test a classical claim that is EXPECTED TO FAIL — exactly the project's discipline of equal NULL prominence.

## 8. Rules-tuple

`(no-tashkeel, QAC-v0.4-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 9. Bonferroni accounting

k = 1. α_bon = 0.05.

## 10. Output

- Pre-reg: this file.
- Script: `scripts/Q048_F_04_prophecy_pair.py`.
- JSON: `csv/Q048-F-04.json`.
- Findings: `06-novel-findings.md` §Q048-F-04.

## 11. SHA256 lock

Computed at write-time, embedded into the script.
