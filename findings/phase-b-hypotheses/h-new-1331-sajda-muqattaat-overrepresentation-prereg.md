---
id: H-NEW-1331
title: Sajda-surahs × muqaṭṭāʿat-opened hypergeometric over-representation
date_locked: 2026-05-09
seed: 20260509
n_perm: not-applicable (hypergeometric exact test + permutation cross-check)
bonferroni_k: 1
bonferroni_family: H-NEW-1331-sajda-muqattaat
alpha_bon: 0.05
direction_of_effect: The 14 sajda-surahs are over-represented for muqaṭṭāʿat-opening relative to corpus baseline (one-tailed hypergeometric / one-tailed permutation)
origin: post-hoc-noticed (descriptive observation surfaced by H-NEW-1330; this pre-reg locks the inference BEFORE computing the exact intersection count)
verdict_ceiling: PASS-DIRECTED (post-hoc origin; INDEPENDENT REPLICATION required for promotion)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  muqattaat_definition: 29-surah-list-per-cross-finding-008
  sajda_surah_definition: classical-Sunnī-14-list (Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96)
  null_model: hypergeometric-with-permutation-cross-check
---

# H-NEW-1331 pre-registration

## Origin

H-NEW-1330 returned NULL for the FR-cohesion test of the 14 sajda-surahs but flagged a descriptive observation: 6/14 (43%) appeared muqaṭṭāʿat-opened vs corpus baseline 29/114 (25%) — 1.7× enrichment. Hypergeometric p≈0.062 (single-tailed) was reported but **not pre-registered**. This pre-reg locks the test as a post-hoc-noticed single-test α=0.05 inference, with the **exact intersection count yet to be verified** at run-time.

## Hypothesis

The 14 sajda-surahs contain a higher fraction of muqaṭṭāʿat-opened surahs than expected by random sampling without replacement from the 114-surah corpus.

## Cluster locked

**Sajda set** (classical Sunnī tradition, 14 surahs): {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96}.

**Muqaṭṭāʿat set** (29 surahs per cross-finding-008): {Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}.

**Run-time computation**: the intersection is computed from the locked sets at runtime. Direction is locked: intersection ≥ expected (= 14 × 29/114 = 3.56).

## Test design

### Cell A (primary, hypergeometric exact)

N = 114 (corpus), K = 29 (muqaṭṭāʿat), n = 14 (sajda), k = |intersection|. Compute one-tailed hypergeometric p = P(X ≥ k | hypergeometric(N, K, n)).

PASS if p ≤ 0.05; NULL otherwise.

### Cell B (cross-check, permutation)

10000 random samples of 14-from-114 (no replacement). Count fraction with intersection-with-muq ≥ k_observed. Direction-locked.

PASS if both Cells A and B agree at α = 0.05.

### Bonferroni

k = 1 (single hypothesis). α = 0.05.

### Garden-of-forking-paths

Origin disclosed as post-hoc-noticed via H-NEW-1330 inline observation. The exact intersection count is computed only at run-time from the sets locked above. Direction is locked: over-representation. The 14-sajda list is the **broadest classical-Sunnī list**; the Imāmī 4-surah list and the Mālikī 13-surah list are NOT in scope (separate pre-regs would be needed).

### Anti-flip

Reverse direction (under-representation) is NOT a reportable PASS. Publish as NULL.

## Connection to existing findings

- **Cross-finding-008** muqaṭṭāʿat as book-introduction markers: this finding tests whether the muqaṭṭāʿat-marker correlates with the sajda-trigger-marker, which would extend the muqaṭṭāʿat's multi-axis-correlation reach (cross-finding-025 prediction).
- **H-NEW-1330** sajda FR-cohesion NULL: the muqaṭṭāʿat over-representation is the only structural-axis signal for the sajda set; if it passes, the sajda set is partially "structured" by muqaṭṭāʿat-correlation while still lacking root-distribution cohesion.
- **Cross-finding-025** marker-thickness threshold: this test directly probes the multi-axis-correlation criterion. If sajda × muqaṭṭāʿat passes, the sajda set has at least one independent structural correlate, but its FR-cohesion failure shows that one axis is not enough.

## Pre-commit attestation

Locked by SHA256. Run script verifies before computing intersection.
