---
surah: 32
test_id: Q032-F-04
title: ALM-4 mid-Meccan sub-cluster {Q 29, 30, 31, 32} Fisher-Rao cohesion (tighter than ALM-6 per Q030-F-08 PARTIAL)
file_type: pre-registration
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 2
alpha_bon: 0.025
verdict_ceiling: PASS-DIRECTED (single planned replication required for promotion to CONFIRMED)
classical_anchor: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 — the 6 ALM-openers split between Medinan (Q 2, 3) and Late-Meccan (Q 29, 30, 31, 32). Q030-F-08 tested the full ALM-6 and returned PARTIAL (uniform NULL p=0.418; length-matched PASS p=0.0225). The ALM-4 (mid-Meccan subset) is hypothesized to be tighter than ALM-6 because chronologically and length-class uniform.
direction_of_effect: LOCKED — mean intra-cluster Fisher-Rao distance of the 4 surahs {Q 29, 30, 31, 32} is below the 5th percentile of permutation-null samples of size 4 from non-Q1 surahs.
rules_tuple:
  orthography: no-tashkeel
  word_definition: QAC stem-roots
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  cluster_definition: 4-surahs {Q 29, 30, 31, 32} — the ALM-openers all in al-Suyūṭī "Late Meccan" chronological band, sharing 3-letter muqaṭṭaʿ + mufaṣṣal-ṭiwāl length class
  null_model: random-4-surah-samples (uniform from 113-surah pool excluding Q 1)
  null_model_B: random-4-surah-samples length-matched to the ALM-4 word-count band
  instrument: H-NEW-111 D_matrix_upper_triangular (Fisher-Rao on QAC stem-root TF distributions, top-500 roots)
---

# Q032-F-04 — Pre-registration: ALM-4 mid-Meccan cluster Fisher-Rao cohesion

## 1. Origin

al-Suyūṭī (*al-Itqān*, nawʿ 1) places Q 29-32 in the Late Meccan chronological band (revelation orders 85, 84, 57, 75 respectively per `data/revelation-order.csv`); Q 2 and Q 3 are Medinan (revelation orders 87, 89). All 6 share the ALM 3-letter muqaṭṭaʿ opener.

Q030-F-08 tested ALM-6 {Q 2, 3, 29, 30, 31, 32} for FR-cohesion and returned PARTIAL: Cell A (uniform null) NULL with p=0.418 (T_obs = 0.926, corpus pairwise mean = 0.923); Cell B (length-matched null among large-band surahs) PASS-DIRECTED with p=0.0225. The PARTIAL verdict arose because Q 2 (286 verses) and Q 3 (200 verses) are 6–9× longer than Q 29-32 (29-69 verses) and have distinct vocabulary in late-Medinan legal/communal idioms.

This pre-reg tests the **smaller, chronologically-tighter ALM-4 sub-cluster** {Q 29, 30, 31, 32}. The hypothesis is that REMOVING Q 2 + Q 3 (the Medinan-late outliers) tightens the cluster.

## 2. Hypothesis

**H1:** The 4 Late-Meccan ALM surahs {Q 29, Q 30, Q 31, Q 32} form a Fisher-Rao cohesive cluster on the H-NEW-111 root-distribution instrument.

**H0:** The ALM-4 cluster is NOT FR-cohesive (mean intra-cluster distance no lower than random length-matched 4-of-113 samples).

**Direction:** intra-cluster mean ≤ permutation null 5th percentile (LOCKED).

## 3. Cluster definition

C = {Q 29 al-ʿAnkabūt, Q 30 al-Rūm, Q 31 Luqmān, Q 32 al-Sajda}.

- Q 29:1, Q 30:1, Q 31:1, Q 32:1 — each is the 3-letter token alif-lām-mīm (الم), verified against QAC `morphology/quranic-corpus-morphology-0.4.txt` location-tuples (29:1:1:1), (30:1:1:1), (31:1:1:1), (32:1:1:1).
- All four are al-Suyūṭī Late-Meccan; revelation orders 85/84/57/75; verse counts 69/60/34/30 — verse-count IQR 30-69.

## 4. Test design

### Cell A — uniform null

Compute mean pairwise FR among the 4 cluster surahs (C(4,2) = 6 pairs). Permutation null: 10,000 random 4-of-113 samples from corpus excluding Q 1.

**Direction-locked**: intra-cluster mean ≤ permutation null 5th percentile.

PASS if p_perm ≤ 0.025 (Bonferroni-2); NULL otherwise.

### Cell B — length-matched null

Permutation null: 10,000 random 4-of-X samples where X = surahs with word-count within IQR [543, 815] (the length band of the ALM-6 cluster, retained from Q030-F-08 for cross-test comparability). This is the same length-matching as Q030-F-08 Cell B.

**Direction-locked**: intra-cluster mean ≤ permutation null 5th percentile.

PASS if p_perm ≤ 0.025.

## 5. Bonferroni and significance

**Bonferroni-k = 2** (Cell A uniform + Cell B length-matched). α_bon = 0.025 per cell. The pre-reg follows the Q030-F-08 two-cell template exactly for cross-test comparability.

## 6. A priori expectation (locked PRIOR to running)

Per Q030-F-08 Cell B-uniform PASS (p=0.0225, the ALM-6 set was tighter than length-matched-large-band random), and per cross-finding-025 marker-thickness rule (clusters share multiple independent structural features → FR-cohesive), the ALM-4 sub-cluster carries:
- (1) shared 3-letter ALM muqaṭṭaʿ
- (2) shared al-Suyūṭī Late-Meccan chronology
- (3) shared mufaṣṣal-ṭiwāl length class
- (4) shared cosmological-eschatological-prophetic-narrative content register (per `Q030-al-rum/02-content-analysis.md`, `Q031-luqman/02-content-analysis.md`, `Q032-al-sajda/00-overview-comprehensive.md`)

Four independent shared features satisfy cross-finding-025's marker-thickness threshold. The PRIOR expectation is PASS-DIRECTED with the uniform-null cell as the cleaner test (since Q 2/Q 3 removal also removes the length-mismatch confound of Q030-F-08).

## 7. Honest limits

- Removing Q 2 and Q 3 narrows the test to 4 surahs; the smaller cluster has higher permutation-null variance.
- Q 7 (ALMS, 4-letter) and Q 13 (ALMR, 4-letter) are excluded as orthographically distinct openers despite sharing the alif-lām-mīm prefix.
- The chronological band of Q 29-32 is contested in fine detail (Nöldeke places Q 29 at #81 Middle Meccan; Tanzil aligns with al-Suyūṭī). Both sources agree Q 29-32 are pre-Hijra and post-early-Meccan.

## 8. Pre-commit violations

If the mean intra-cluster FR distance EXCEEDS the null 50th percentile (i.e. moves in the WRONG direction), the finding is published as NULL — DIRECTION REVERSED with full prominence per PRE-REG-STANDARD-01.
