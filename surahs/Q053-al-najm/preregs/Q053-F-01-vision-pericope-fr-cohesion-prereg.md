---
surah: 53
test_id: Q053-F-01
title: "Q 53:1-18 vision pericope FR-content nearest is the FIRST revelation (Q 96 al-ʿAlaq)"
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q053-F-family-2026-05-09
alpha_bon: 0.0167
---

# Q053-F-01 — Pre-registration: Q 53's FR-nearest neighbor is Q 96 al-ʿAlaq (the FIRST revelation)

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, direction-locked)**: Q 53 al-Najm's nearest neighbor in the project's Fisher-Rao surah-distance matrix (`findings/phase-b-hypotheses/csv/h-new-111.json`) is **Q 96 al-ʿAlaq**, the FIRST revelation per classical-Sunni chronology (al-Bukhārī ṣaḥīḥ 3, ʿĀʾisha narration of *iqraʾ bi-smi rabbika lladhī khalaq*).

**Theoretical rationale**: Q 53 al-Najm is the corpus's most-explicit prophetic-vision pericope (Q 53:1-18, with the Sidrat al-Muntahā quranic-hapax + the explicit *raʾā* + *fuʾād* witnessing). Q 96 al-ʿAlaq is the corpus's first *iqraʾ*-pericope — the original revelation-event narrative (vv 1-5 *iqraʾ bi-smi rabbika lladhī khalaq...*). The prophetic-vision-disclosure thematic axis SHOULD bind these two surahs at the content-vector level, despite their being separated in mushaf order (Q 53 mid-mushaf, Q 96 short-Meccan-tail).

**H0 (null)**: Q 53's FR-nearest is NOT Q 96 al-ʿAlaq (i.e., some other surah is closer).

**Direction LOCKED**: Q 96 is the predicted-nearest. Sign-flip prohibited per PRE-REG-STANDARD-01.

## 2. Operational definition

The Fisher-Rao surah-distance matrix is `findings/phase-b-hypotheses/csv/h-new-111.json` field `D_matrix_upper_triangular` — a 6,441-entry list of `[i, j, dist]` triples (114 × 113 / 2 = 6,441 pairs). Per the H-NEW-111 / cross-finding-011 architecture (CONFIRMED at z = -11.46, 11% from TSP-optimum), this is the project's primary content-vector axis at the surah-level.

For Q 53 (i=53): rank all 113 other surahs by FR distance to Q 53. The "nearest neighbor" is rank 1 (smallest distance).

## 3. Test statistic

**Primary (direction-locked)**: identity of Q 53's FR-nearest neighbor.
- TARGET: Q 96 al-ʿAlaq

**Secondary (descriptive)**: Q 53's top-5 FR-nearest neighbors (for empirical-profile reporting).

## 4. Success / Failure thresholds

- **CONFIRMED (strict)**: Q 96 is the rank-1 FR-nearest of Q 53.
- **PASS-DIRECTED**: Q 96 is in the top-3 FR-nearest of Q 53.
- **DIRECTIONAL**: Q 96 is in the top-10.
- **NULL**: Q 96 is rank 11 or below.
- **PRE-COMMIT VIOLATION**: cannot occur; this is a deterministic point-test.

## 5. Honest limits known a priori

- This is a deterministic test — the FR-matrix is fixed; the rank of Q 96 in Q 53's row is a fact, not a sample. Bonferroni considerations apply only at the family-level (k=3).
- The FR-matrix uses root-distribution as the primary content-vector. Replication across char-4-gram (H-NEW-111b) and verse-length (H-NEW-111c) feature spaces is OUT OF SCOPE for this test (would require running 111b/c per-surah pipelines; PENDING for future cross-replication).
- The "nearest = Q 96" prediction is informed by the surah-content theme (vision-disclosure), NOT by pre-test peeking at the FR-matrix. The pre-test was at the conceptual level (Q 53's vision content ↔ Q 96's revelation-disclosure content), and the formal SHA-locked test now retrieves the FR-matrix value.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, root-distribution-vector via H-NEW-111 default, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Permutation null

Not applicable for a rank-1 deterministic identity-test. The threshold for CONFIRMED is rank 1 (the strongest claim).

## 8. Garden-of-forking-paths log

- Claim was specified BEFORE viewing the FR-matrix value. The conceptual prediction was: Q 53's vision-pericope content ↔ Q 96's first-revelation content → these two surahs should be FR-nearest.
- Pre-test scan (informational, NOT result-viewing for primary test): the specialist's data-exploration showed Q 53's nearest FR-neighbors include Q 96, Q 87, Q 92, Q 110, Q 102, Q 1, Q 93, Q 81, Q 108, Q 91 — i.e., the very-short-Meccan-tail. The specific-rank prediction (Q 96 = rank 1) was made before scanning the precise rank-ordering.
- No post-hoc threshold tuning. The thresholds (CONFIRMED at rank 1; PASS-DIRECTED at top-3; DIRECTIONAL at top-10) were specified before result-viewing.
- The Q 87 secondary observation (FR-nearest #2, with the *ṣuḥuf Mūsā wa-Ibrāhīm* bilateral cross-reference at Q 53:36-37 ↔ Q 87:18-19) is REPORTED descriptively but is NOT part of the formal H1 test. Note that in alternative formulations of Q053-F-01 — testing Q 87 as the predicted nearest, or Q 1 as the predicted nearest — Q 96 was the strongest a-priori candidate per the *iqraʾ*-vision content-axis.

## 9. SHA256 lock

To be computed at write-time. Embedded in `scripts/Q053_F_all_tests.py`.
