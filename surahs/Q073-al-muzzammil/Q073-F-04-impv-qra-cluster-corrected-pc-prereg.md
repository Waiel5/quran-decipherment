---
surah: 73
test_id: Q073-F-04
title: H-NEW-1301 IMPV-qrA cluster cohesion replication with corrected MW-5 positive control
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q073-F-04-impv-qra-cluster-replication
alpha_bon: 0.025
---

# Q073-F-04 — Pre-registration: H-NEW-1301 IMPV-qrA cluster cohesion replication with corrected MW-5 positive control

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction):** The 4-surah IMPV-qrA cluster {Q 17, Q 69, Q 73, Q 96} (per H-NEW-1300 corpus-EXACT inventory) is **Fisher-Rao-cohesive** at the surah-aggregate root-distribution level, with mean intra-cluster pairwise FR distance lower than 95% of length-matched random 4-surah samples.

**H1a (Cell A, uniform null):** intra-cluster FR mean ≤ 5th percentile of random 4-of-113 (excluding Q 1) sample.

**H1b (Cell B, length-matched null):** intra-cluster FR mean ≤ 5th percentile of random 4-of-N length-matched sample (length-window: ±50% of cluster's mean verse-count = (111 + 52 + 20 + 19) / 4 = 50.5).

**MW-5 positive control (corrected):** the gold-standard *wa-mā adrāka mā* 10-surah cluster (H-NEW-1190, p=0.00068) MUST detect cohesion under the SAME instrument. **Sub-sample method**: take 4-of-10 from the H-NEW-1190 cluster {Q 69, 74, 77, 82, 83, 86, 90, 97, 101, 104}; randomly sample 4 with seed=20260509; the resulting sub-sample's intra-cluster FR mean MUST be in the bottom 5% of length-matched random 4-of-N samples.

**H0:** Either H1a OR H1b NULL, OR MW-5 PC fails (NULL-BROKEN).

**Direction:** cluster cohesion + instrument-validity (LOCKED).

## 2. Operational definition

- **Source data**: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`. Rules-tuple: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, mushaf order, Hafs-Kūfan).
- **Cluster definition**: {Q 17, Q 69, Q 73, Q 96} per H-NEW-1300.
- **Length matching (Cell B)**: matched on verse-count band ±50% of cluster mean (50.5). Cluster verse counts: Q 17 = 111, Q 69 = 52, Q 73 = 20, Q 96 = 19. The cluster ranges 19-111 verses — a >5× range. Length-window operationalization: each null sample drawn requires that all 4 surahs lie within {min/2, max*2} = {10, 222} verse-band. (Wider window than H-NEW-1301's ±20% to account for the heterogeneity of the actual cluster.)

**MW-5 positive control method (CORRECTED from H-NEW-1301)**:
- H-NEW-1301 used the HM cluster {41, 42, 43, 44} 4-of-7 sample, which FAILED. The HM cluster is letter-set-cohesive but NOT root-distribution-FR-cohesive (per H-NEW-1301's diagnosis).
- The corrected PC uses the H-NEW-1190 *wa-mā adrāka mā* 10-surah cluster, which IS confirmed FR-cohesive at p=0.00068.
- **Sub-sample**: deterministically sample 4 surahs from {69, 74, 77, 82, 83, 86, 90, 97, 101, 104} using seed=20260509. The 4-surah subset must show cohesion at p_pc ≤ 0.05 under the SAME 4-of-113-uniform null instrument.

## 3. Test statistic

- D_obs = mean pairwise FR distance for {17, 69, 73, 96}.
- p_A = fraction of random 4-of-113 (excluding Q 1) samples with D ≤ D_obs.
- p_B = fraction of random length-matched 4 samples with D ≤ D_obs.
- D_pc = mean pairwise FR for the 4-of-10 H-NEW-1190 sub-sample.
- p_pc = fraction of random 4-of-113 samples with D ≤ D_pc.

## 4. Permutation null

- Cell A: n_perm = 10000, seed = 20260509. Uniform random 4-of-113 (exclude Q 1 per the canonical exclusion in h-new-111).
- Cell B: n_perm = 10000. Random 4-of-N length-matched (verse-count in [10, 222]).
- MW-5 PC: n_perm = 10000. Same uniform null as Cell A; PC sub-sample is fixed (seed=20260509 4-of-10 draw from H-NEW-1190 cluster).

## 5. Success / Failure

- **CONFIRMED**: H1a AND H1b both pass at α_bon = 0.025; MW-5 PC passes (p_pc ≤ 0.05).
- **DIRECTIONAL**: 1 of 2 cells passes; MW-5 PC passes.
- **NULL**: both cells NULL; MW-5 PC passes — the substantive finding is genuinely no cluster cohesion.
- **NULL-BROKEN**: MW-5 PC fails — instrument cannot detect known signal; verdict cannot be issued.

## 6. Honest limits known a priori

- This is a **planned replication** of H-NEW-1301 with a SINGLE METHODOLOGICAL CHANGE: the corrected MW-5 positive control. All other parameters (rules-tuple, FR distance, n_perm, alpha) match H-NEW-1301 exactly to enable direct comparison.
- The substantive expectation, given H-NEW-1301's NULL on both cells, is that the cluster IS NOT cohesive at the surah-aggregate FR-root level. This pre-reg replicates that NULL with a working instrument so we can definitively say "the IMPV-qrA cluster is NOT FR-cohesive on root-distribution" (rather than "test was broken").
- The 4-of-10 PC sub-sample is **deterministic** under seed=20260509. Sensitivity check: report p_pc under 5 alternative seeds to confirm the PC is robust.
- **MW-5 PRINCIPLE STRICT INTERPRETATION**: per HANDOFF/04-DISCIPLINE.md, if MW-5 PC fails the verdict is NULL-BROKEN regardless of substantive outcome. The "lesson published" disposition from H-NEW-1301 will be promoted to a substantive verdict here ONLY if MW-5 PC PASSES.

## 7. Pre-commit attestation

- Pre-reg locked BEFORE running the FR-distance computations on either cluster. Cluster membership and PC source are documented anchors (not run-time observations).
- The seed for the 4-of-10 PC sample is **fixed** at 20260509; this draws a deterministic sub-sample. The sub-sample is computed at runtime, not observed before lock.

## 8. Decision rule

1. Load h-new-111.json D matrix.
2. Compute D_obs for {17, 69, 73, 96}.
3. Run Cell A null (10K perms uniform 4-of-113 exclude Q 1).
4. Run Cell B null (10K perms length-matched).
5. Draw deterministic 4-of-10 PC sub-sample (seed=20260509).
6. Compute D_pc for sub-sample; run PC null (10K perms uniform 4-of-113).
7. Apply MW-5 verdict gate, then primary-cell verdict.

## 9. Bonferroni declaration

- bonferroni_k = 2 (Cell A, Cell B).
- bonferroni_family = Q073-F-04-impv-qra-cluster-replication.
- alpha_bon = 0.05 / 2 = 0.025 per cell.
- MW-5 PC threshold: 0.05 (single-test, instrument-control level).

## 10. Connection to existing findings

- **H-NEW-1300** (NULL by strict pre-reg): the corpus-EXACT 4-surah inventory.
- **H-NEW-1301** (NULL-BROKEN per HANDOFF instrument-discipline): the original test which this replicates with corrected PC.
- **H-NEW-1190** (CONFIRMED FR-cohesive p=0.00068): provides the corrected MW-5 PC.
- **MW-5 principle** (HANDOFF/04-DISCIPLINE.md §6): every permutation null must pass a positive-control on a known-signal corpus.
