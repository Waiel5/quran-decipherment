---
surah: 13
test_id: Q013-F-03
title: "Chronology-architecture dissociation replication on contested-chronology Q 13"
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q013-F-family-2026-05-07
alpha_bon: 0.01
n_perm: 10000
---

# Q013-F-03 — Pre-registration: chronology-architecture dissociation replication

## 1. Hypothesis (locked before observation)

The Q 5 specialist (`surahs/Q005-al-maida/06-novel-findings.md` Q005-F-05) demonstrated a **chronology-architecture dissociation**: Q 5, classically very-late-Medinan (rev #112), is architecturally a Q 2-twin (early-Medinan-ṭiwāl head cluster) with d_EM = 0.16 < d_LM = 1.44 across 4 axes {z_FR_mean, z_sig_A, z_sig_B, z_rhyme_entropy}. The framework predicts: **a surah's architectural signature is fixed by mushaf-position + length-class + content-vocabulary + rhyme-class, NOT by classical-tradition chronology.**

Q 13 is **classically contested** (al-Suyūṭī Medinan vs Ibn ʿAbbās/Mujāhid/Nöldeke Late Meccan). This makes Q 13 the natural test-case: regardless of which chronology classification is "correct", the framework predicts Q 13's architectural signature is determined by its mushaf position (s=13, head-mushaf zone) and length (43 verses, 928 words, mufaṣṣal-ṭiwāl-class).

**H1 (locked direction)**: Q 13's 4-axis architectural signature `v(Q13) = [z_FR_mean, z_sig_A, z_sig_B, z_rhyme_entropy]` is **CLOSER to the Meccan centroid M = mean(v(Q5), v(Q6), v(Q7))** than to the **Medinan centroid Med = mean(v(Q2), v(Q3), v(Q4))**.

**Reasoning for direction**: Q 13 is at mushaf-position 13, in the head-mushaf zone where the H-NEW-660 compression-tail predicts d̄_content ≈ 0.96 (head-cohort plateau). Q 5/6/7 are mushaf positions 5/6/7 (head-Meccan-ṭiwāl band, despite Q 5/9 being late-Medinan in classical chronology). Q 2/3/4 are mushaf positions 2/3/4 (al-sabʿ al-ṭiwāl head). Both are head-cohort surahs, BUT Q 5 is the empirically-known Q 2-twin per Q005-F-05. The Q 13 prediction is that Q 13 should behave like its mushaf-neighbors Q 6 + Q 7 (longer prophet-narrative + cosmological surahs) MORE than like Q 2/Q 3/Q 4 (al-sabʿ al-ṭiwāl legal). The DIRECTION is "closer to M" specifically because Q 13's content register (cosmology + theology + brief prophet-history) more closely resembles Q 6 al-Anʿām and Q 7 al-Aʿrāf than the legal-Medinan-ṭiwāl Q 2/Q 3/Q 4.

**H0**: Q 13 closer to Med than to M (or equidistant).

**Direction (locked)**: Q 13 → M (closer to Meccan centroid Q5/6/7 mean than to Medinan centroid Q2/3/4 mean).

## 2. Operational definition

Per-surah `v(s) = [z_FR_mean, z_sig_A, z_sig_B, z_rhyme_entropy]`:
- `z_FR_mean` (z-score of `mean_content_distance` from H-NEW-750 across all 114 surahs).
- `z_sig_A` from H-NEW-750 (already z-scored field).
- `z_sig_B` from H-NEW-750 (already z-scored field).
- `z_rhyme_entropy` from H-NEW-750 (already z-scored field).

Note: H-NEW-750 reports `z_rhyme_entropy`, `z_mean_content_distance`, `z_local_cohesion` directly. We compute v(s) from these per-surah fields.

For Q 13: pull v(13) from H-NEW-750.
For M = mean(v(Q5), v(Q6), v(Q7)).
For Med = mean(v(Q2), v(Q3), v(Q4)).

**Distance metric**: Euclidean `‖v(13) - M‖` and `‖v(13) - Med‖`.

**Direction-locked**: Q 13 closer to M (`‖v(13) - M‖ < ‖v(13) - Med‖`).

**Permutation null**: random centroid pairings. From the 113 non-Q-13 surahs, draw 1000 random triplets-A and 1000 random triplets-B (triplets sized 3 each), compute centroids and Q 13's distance to each, and count fraction where `d_A < d_B`. The OBSERVED direction (Q13 closer to M) under H0 has p_chance baseline measured; if observed direction is significantly OVER expected baseline → CONFIRMED.

## 3. Test statistic

**Primary**: indicator `Q13_closer_to_M = (‖v(13) - M‖ < ‖v(13) - Med‖)`. Pre-commit: TRUE.

**Secondary (descriptive)**:
- Magnitude of distance difference `Δ = ‖v(13) - Med‖ - ‖v(13) - M‖` (positive = closer to M).
- 4-axis breakdown (which axis contributes most to the distance ratio).

**Permutation p-value**: fraction of 10000 random centroid pairings where the observed direction holds. CONFIRMED if observed direction holds AND p_chance baseline does NOT exceed 0.5 by a wide margin (i.e. the observed direction is not the trivial one).

## 4. Success / Failure

- **CONFIRMED**: indicator = TRUE AND `Δ > 0` AND p_perm against the null direction-distribution shows the observed direction is NOT the chance-trivial direction.
- **DIRECTIONAL**: indicator = TRUE BUT `Δ ≤ 0.1` (small magnitude).
- **NULL — direction reversed**: indicator = FALSE → pre-commit violation. Report with full prominence per PRE-REG-STANDARD-01.
- **CONFIRMED-DISSOCIATION**: indicator = TRUE AND `Δ` large AND Q 13 is empirically much closer to M than to Med, despite al-Suyūṭī chronology classifying Q 13 as Medinan. This would be the **chronology-architecture dissociation replication**: Q 13's classical-chronology category does not determine its architectural signature; the architecture is determined by mushaf-position + content-class.

## 5. Honest limits known a priori

- The Meccan-centroid M (Q 5/6/7) is constructed for this test. The Q 5 specialist's finding is that Q 5 itself is architecturally a Q 2-twin (i.e. Q 5 is in the "legal-Medinan-ṭiwāl" cell, NOT the "Meccan-ṭiwāl" cell). Therefore the M centroid (Q 5+Q 6+Q 7) is NOT a pure Meccan centroid — it's a head-mushaf-ṭiwāl centroid that includes Q 5 (architecturally Med-like). The pre-committed prediction is robust to this because Q 5 itself is empirically Q 2-twin, so M ≈ (Q 5 + Q 6 + Q 7)/3 and Med ≈ (Q 2 + Q 3 + Q 4)/3 may be MORE similar to each other than the labels suggest.
- An alternative: use Q 6 and Q 7 alone (true Meccan in classical chronology) for M. We pre-commit to Q 5/6/7 to make the prediction conservative — if Q 5 is empirically Q 2-like, then M ≈ Med, and the test is biased AGAINST the H1 direction. If Q 13 STILL is closer to M (even with Q 5 dragging M toward Med), the dissociation is robust.
- A 4-axis Euclidean distance is one of many possible architectural-signature definitions. Alternative axes (verse-length distribution, phoneme density, outlier-strength) might yield different results.
- The triplet-based centroid is a small-sample estimator (N=3 per centroid). Random-triplet permutation null reduces this.

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots, Fisher-Rao angular distance, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. All 4 axes pulled from `findings/phase-b-hypotheses/csv/h-new-750.json` per_surah field.

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q013_F_03_chronology_architecture.py`.

## 8. Garden-of-forking-paths

- Considered: using al-Suyūṭī Medinan classification (rev #96) as the "ground truth" for the chronology centroid. PRE-COMMITTED to architectural-signature test alone — chronology is the contested variable.
- Considered: 5-axis signature including UAS rank. REJECTED: UAS already incorporates outlier-strength + adjacency + |sig_A|; correlated with the existing 4 axes.
- Considered: testing with Nöldeke chronology centroid instead. NOT PRE-REGISTERED — alternative; documented as future replication.
- Considered: removing Q 5 from the M centroid. REJECTED: pre-committed conservative-bias-against-H1 by including Q 5.
