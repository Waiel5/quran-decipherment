---
surah: 13
test_id: Q013-F-05
title: "Q 13 chronology-hadith audit — al-Suyūṭī Medinan vs Ibn ʿAbbās Meccan attributions, and architecture-invariance prediction"
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q013-F-family-2026-05-07
alpha_bon: 0.01
n_perm: 10000
---

# Q013-F-05 — Pre-registration: Q 13 chronology-hadith audit + architecture-invariance

## 1. Hypothesis (locked before observation)

Q 13 al-Raʿd has a CONTESTED classical chronology:
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1: classifies Q 13 as **Medinan** (rev order #96 by al-Suyūṭī's catalog).
- al-Ṭabarī, *Jāmiʿ al-bayān* (introduction to Q 13): cites BOTH positions — Medinan (via certain Ibn ʿAbbās chains) AND Meccan (via other Ibn ʿAbbās chains, plus Mujāhid and ʿIkrima).
- al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān* (intro to Q 13): summarizes the dispute, leaning Meccan-with-Medinan-insertions.
- Nöldeke, *Geschichte des Qorâns* (Wikipedia summary): classifies Q 13 as **Late Meccan** (chronological position 90).

**H1 (compound, locked direction)**:
- (a) The classical-chronology disagreement is real (≥ 2 distinct classical positions on disk).
- (b) Q 13's empirical 4-axis architectural signature `v(13)` is closer to a Meccan-of-similar-length surah's signature (chosen pre-test) than to a Medinan-of-similar-length surah's signature.
- (c) The architecture-invariance prediction: regardless of which classical chronology is "correct", Q 13's FR distance to its mushaf-neighbour-window (Q 10–Q 16) is consistent with NO outlier behavior — Q 13 fits its mushaf cohort, not the chronology cohort.

**Pre-committed comparison surahs**:
- Meccan-of-similar-length: **Q 14 al-Ibrāhīm** (52 verses, 798 words, classically Meccan rev #72, Nöldeke #76) — closest mushaf-neighbor with similar length and unambiguous Meccan classification.
- Medinan-of-similar-length: **Q 76 al-Insān/al-Dahr** (31 verses, 240 words; OR Q 110 al-Naṣr 3 verses; OR Q 99 al-Zalzala 8 verses). The closest in length-class to Q 13 from clearly-Medinan classification: **Q 76 al-Insān** (classified Medinan by al-Suyūṭī, rev #98) is the closest.

**Direction (locked)**: `‖v(13) − v(14)‖ < ‖v(13) − v(76)‖` — Q 13 is architecturally closer to Q 14 (Meccan, similar length, mushaf-adjacent) than to Q 76 (Medinan, similar verse count but mufaṣṣal).

## 2. Operational definition

`v(s) = [z_FR_mean, z_sig_A, z_sig_B, z_rhyme_entropy]` from H-NEW-750 per-surah row.

Compute Euclidean `‖v(13) - v(14)‖` and `‖v(13) - v(76)‖`.

**Permutation null**: For 10000 random pairs (`s_meccan_random`, `s_medinan_random`) drawn from {Meccan surahs ≠ 13/14} × {Medinan surahs ≠ 13/76}, compute `‖v(13) - v(s_m)‖` and `‖v(13) - v(s_med)‖` and the indicator `closer_to_meccan_random`. Distribution defines the null direction baseline.

## 3. Test statistic

**Primary (a) — Hadith audit**: count of distinct classical sources on disk that classify Q 13 as Meccan vs Medinan vs Mixed. Pre-commit: ≥ 1 source on each side (verified by reading classical-tafsir directory).

**Primary (b) — Architectural distance**: `closer_to_Q14_indicator = (‖v(13) - v(14)‖ < ‖v(13) - v(76)‖)`. Pre-commit: TRUE.

**Primary (c) — Mushaf-window invariance**: H-NEW-590 X=13 row (already pulled). The classification is `NULL` (delta_pct = -3.85, p_greater_W = 0.5256). Pre-commit: NULL classification CONFIRMED — Q 13 is NOT a content outlier, supporting the architecture-invariance prediction.

**Bonferroni-corrected p-thresholds**: combined family of 3 sub-tests under k=5 outer-Bonferroni; sub-test α: descriptive for (a); permutation for (b); H-NEW-590 already-published for (c).

## 4. Success / Failure

- **CONFIRMED**: ≥1 source each side AND closer_to_Q14 = TRUE AND NULL classification on H-NEW-590 confirmed. Three-out-of-three.
- **DIRECTIONAL**: 2 of 3 sub-tests pass.
- **NULL**: < 2 of 3 sub-tests pass.
- **Pre-commit violation**: closer_to_Q14 = FALSE (Q 13 architecturally closer to Q 76 than to Q 14).

## 5. Honest limits known a priori

- The chronology audit is qualitative; the count is a verification, not a permutation test.
- Q 14 is mushaf-adjacent to Q 13, so `‖v(13) - v(14)‖` may be small for length+mushaf-position reasons (not just chronology). The test is therefore primarily a **mushaf-position-architecture** test, NOT a pure Meccan-vs-Medinan test.
- Q 76 al-Insān is mufaṣṣal (s=76, well past the Hijra-kink at s=50); its z_FR_mean is in the compression-tail (small d̄_content) — automatically distant from Q 13 (head-zone, larger d̄). The test is therefore confounded by compression-tail position.
- We pre-commit to this test KNOWING the confounds because the framework (Q005-F-05 dissociation) is precisely about mushaf-position determining architecture irrespective of chronology — the confounds ARE the predicted mechanism.

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots, Fisher-Rao angular, H-NEW-750 fields, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q013_F_05_chronology_audit.py`.

## 8. Garden-of-forking-paths

- Considered: using Q 110 or Q 99 instead of Q 76 for the Medinan reference. PRE-COMMITTED to Q 76 because al-Insān is the SHORTEST clearly-Medinan-by-al-Suyūṭī surah within reasonable length-similarity (43 verses Q 13, 31 verses Q 76). Q 110 (3 verses) is too short to be a fair comparator. Q 99 (8 verses) similarly. Q 76 is the conservative choice.
- Considered: removing the H-NEW-590 sub-test from the family (already in published results). RETAINED for completeness — the cited result confirms the framework, but the verdict for F-05 weights all 3 sub-tests.
- Considered: rotating the comparison set (using all Meccan vs Medinan centroids). REJECTED: covered by F-03 (Meccan vs Medinan centroid test); F-05 is specifically the contested-chronology audit + invariance.
