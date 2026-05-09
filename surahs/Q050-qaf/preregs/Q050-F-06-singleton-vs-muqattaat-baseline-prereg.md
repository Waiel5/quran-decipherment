---
finding_id: Q050-F-06
date_locked: 2026-05-09
phase: B+
direction: LOCKED
seed: 20260509
---

# Q050-F-06 — Pre-registration: Singleton-letter triplet FR-cluster vs 28-muqaṭṭāʿat baseline

## Hypothesis

The 3 singleton-letter muqaṭṭāʿat-opener surahs **{Q 38 Ṣād, Q 50 Qāf, Q 68 Nūn}** have a mean pairwise Fisher-Rao distance (S_obs) on QAC stem-roots that is tighter (lower) than BOTH:

- **(a)** the distribution of S over length-matched random 3-surah triplets sampled from the full 114-surah corpus (replicates Q050-F-04 design as a sanity check).
- **(b)** the distribution of S over 3-surah triplets sampled WITHIN the 26 non-singleton muqaṭṭāʿat surahs (the 29 muqaṭṭāʿat-openers minus the 3 singleton-letter cohort) — i.e., the "28-muqaṭṭāʿat" baseline read as "OTHER muqaṭṭāʿat triplets."

This is a refinement of Q050-F-04 which tested only against (a). The new value-add is null (b): does the singleton-letter cohort look TIGHTER even compared to other muqaṭṭāʿat-opener triplets (controlling for whatever class-level FR signature the muqaṭṭāʿat-cohort may carry)?

## Pre-registered direction

**LOW-S** on both nulls. The triplet's mean pairwise FR < the 50th percentile of the null distribution.

Success criteria (Bonferroni-2, α = 0.025 per cell):

- TIGHT-DUAL: percentile_a < 0.025 AND percentile_b < 0.025 → DUAL-CONFIRMED
- TIGHT-ONE: only one of the two passes Bonferroni-2 → PARTIAL
- DIRECTIONAL-DOUBLE: both percentiles in lower half (< 0.50) but neither passes → DIRECTIONAL
- NULL: neither in lower half OR direction reversed on either → NULL (+ pre-commit violation flag if direction reversed)

## Null specification

- Null (a) — "full-corpus":
  - Draw N = 10000 random 3-surah triplets uniformly without replacement from the 114-surah set, EXCLUDING the {38, 50, 68} triplet itself.
  - For each triplet, compute mean pairwise FR distance from h-new-111.json D_matrix_upper_triangular.
  - Compute percentile_a = (# triplets with S < S_obs) / 10000.

- Null (b) — "muqaṭṭāʿat-only":
  - The 29 muqaṭṭāʿat-opener surahs are: {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68} (canonical, per al-Suyūṭī *al-Itqān* nawʿ on muqaṭṭāʿat).
  - The 26 non-singleton-muqaṭṭāʿat = above minus {38, 50, 68}.
  - Enumerate ALL C(26, 3) = 2,600 triplets within the 26 non-singleton-muqaṭṭāʿat (exhaustive enumeration, not sampling).
  - Compute mean pairwise FR distance for each; build empirical null distribution.
  - Compute percentile_b = (# muqaṭṭāʿat-triplets with S < S_obs) / 2600.

## Data and rules-tuple

- FR matrix: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular` (114×114 upper-triangular, list of [i, j, distance]).
- Rules-tuple: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi) — H-NEW-111 default.
- Bonferroni: k = 2 (two null distributions), α_per_cell = 0.025.
- Seed: 20260509.
- n_perm (null a): 10000.
- n_perm (null b): 2600 exhaustive.

## SHA lock

Compute SHA256 of THIS file after writing; embed in `scripts/Q050_F_06_singleton_vs_muqattaat_baseline.py`. Verify at runtime; fail-fast on mismatch.

## Output

- JSON: `surahs/Q050-qaf/csv/Q050-F-06.json` with:
  - finding_id, prereg_sha256, seed, rules_tuple
  - S_obs (singleton triplet mean pairwise FR)
  - null_a stats: mean, sd, percentile_a, n_perm
  - null_b stats: mean, sd, percentile_b, n_triplets_enumerated
  - verdict (DUAL-CONFIRMED / PARTIAL / DIRECTIONAL / NULL)
  - pre_commit_violation flag

## Honest limits

- This is a refinement of Q050-F-04, which tested only against null (a) and returned NULL (percentile 26.7%). The expected outcome under null (b) — within-muqaṭṭāʿat triplets — is unclear; if muqaṭṭāʿat-as-class have higher mean pairwise FR than random (un-clustered), the singleton-letter cohort might look TIGHTER against them; if muqaṭṭāʿat-as-class have lower mean pairwise FR (already a content-cluster), the singleton-letter cohort might look LESS tight relative to other muqaṭṭāʿat triplets.
- Bonferroni-2 is appropriate because the two tests share data (FR matrix) but use different nulls.
- A direction-reversed result (percentile > 0.50) on either null = pre-commit violation; published as NULL with prominence.
