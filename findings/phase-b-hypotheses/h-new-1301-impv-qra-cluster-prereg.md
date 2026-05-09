---
id: H-NEW-1301
title: IMPV-qrA 4-surah cluster Fisher-Rao cohesion {Q 17, 69, 73, 96}
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-1301-impv-qra-cluster
alpha_bon: 0.05
direction_of_effect: The 4 IMPV-qrA surahs {Q 17, 69, 73, 96} have a mean intra-cluster Fisher-Rao distance lower than 95% of length-matched random 4-surah samples (intra-cluster mean ≤ 5th percentile of permutation null)
origin: post-hoc-noticed (inventory revealed by H-NEW-1300; this pre-reg locks BEFORE loading h-new-111.json FR matrix into analysis context)
verdict_ceiling: PASS-DIRECTED (post-hoc origin → single-test α=0.05 cap; INDEPENDENT REPLICATION required for promotion)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: standard-mashriqi
  null_model: random-4-surah-samples-from-114-with-no-replacement-no-length-matching-as-primary-with-length-matched-as-secondary
---

# H-NEW-1301 pre-registration

## Origin

H-NEW-1300 returned NULL by strict pre-reg (Q 96 tied with Q 73 at rank 1 of IMPV-qrA count). The descriptive observation: only 4 surahs in the entire Quran contain IMPV-qrA (out of 114) — Q 17 al-Isrāʾ, Q 69 al-Ḥāqqa, Q 73 al-Muzzammil, Q 96 al-ʿAlaq. This is a **post-hoc-noticed** clustering. This pre-reg locks the FR-cohesion question before any FR-matrix value is loaded into the run-script context.

## Hypothesis

The 4 IMPV-qrA surahs {17, 69, 73, 96} form a structurally cohesive group in Fisher-Rao root-distribution distance (h-new-111.json instrument).

## Test design

### Cell A (primary)

Compute mean pairwise Fisher-Rao distance among {17, 69, 73, 96} = 6 pairs. Compare to permutation null: 10000 random 4-surah samples drawn uniformly without replacement from {1,…,114} excluding Q 1 (per H-NEW-89 sui-generis isolate). Compute p_perm = fraction of random samples with mean intra-cluster ≤ observed.

**Direction-locked**: intra-cluster mean ≤ permutation null 5th percentile.

**Decision**: PASS-DIRECTED if p_perm ≤ 0.05; NULL otherwise.

### Cell B (secondary, length-matched control)

Same test but restrict permutation null to 4-surah samples whose total verse-count is within ±20% of the observed cluster's total verse-count. (Q 17 = 111v; Q 69 = 52v; Q 73 = 20v; Q 96 = 19v; total ≈ 202 verses.) This addresses the obvious length-confound (Q 17 is long-Meccan; Q 73, 96 are short-mufaṣṣal-Meccan). The cluster spans the corpus length spectrum — length-matched null is the relevant control.

### Bonferroni

Cells A + B = 2 cells (primary + length-matched control). k=2. α_bon = 0.025 per cell.

### Acceptance windows

- Cell A passes: p_perm_A ≤ 0.025 → PASS-DIRECTED (cell A only)
- Cell B passes: p_perm_B ≤ 0.025 → PASS-DIRECTED (cell B only)
- Both pass → PASS-DIRECTED
- Cell A passes but Cell B fails → DESCRIPTIVE-ONLY (length-confound suspected)
- Both fail → NULL

### Garden-of-forking-paths

Origin disclosed: H-NEW-1300 NULL revealed the 4-surah cluster post-hoc. No FR-matrix value loaded yet. Direction locked here. No alternative cells will be added post-observation. The cluster identity {17, 69, 73, 96} is locked from the H-NEW-1300 IMPV-qrA segment inventory; no membership-rule alternative will be tested ad hoc.

### Anti-flip

Reverse direction (cluster mean ≥ 95th percentile = anti-cohesion) is not a reportable PASS from this pre-reg. If observed, publish as NULL with reverse-direction note for follow-up.

### MW-5 positive control

Use a cluster known to be structurally cohesive: the muqaṭṭāʿat-opened حم cluster {40, 41, 42, 43, 44, 45, 46} (CONFIRMED structurally tight per cross-finding-008). Sub-sample 4 of 7 randomly (seed 20260509+1); intra-cluster mean must fall ≤ 5th percentile of the random-4-surah null. If positive control FAILS, test instrument is broken; report NULL-BROKEN.

## Connection to existing findings

- H-NEW-1300 sourced the 4-surah inventory.
- Cross-finding-008 / 016 muqaṭṭāʿat-as-book-introduction at *kitāb* axis: Q 17, 69, 73, 96 each invoke *kitāb* in a thematically distinct register; this pre-reg tests whether *kitāb* + *iqraʾ* lexis correlates with FR cohesion.
- H-NEW-89 + H-NEW-1220 FR-centroid ranking: Q 17, 73, 96 are mufaṣṣal-region; Q 69 is Late-Meccan tail. Length confound is the primary null hypothesis (controlled in Cell B).

## Pre-commit attestation

This pre-reg is locked by SHA256 hash. Run script verifies SHA before loading the FR matrix.
