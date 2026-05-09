---
surah: 38
test_id: Q038-F-07
title: Iblīs-narrative 7-pericope root-Jaccard cohesion test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q038-F-07-iblis-narrative-cohesion
alpha_bon: 0.05
---

# Q038-F-07 — Pre-registration: Iblīs-narrative 7-pericope cohesion on root-Jaccard

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** The 7 Iblīs-narrative pericopes — Q 2:34, Q 7:11-25, Q 15:31-44, Q 17:61-65, Q 18:50, Q 20:115-123, Q 38:71-85 — exhibit **TIGHTER** mean pairwise root-Jaccard similarity than length-matched random verse-pericope samples drawn from the corpus.

**Pre-committed direction (LOCKED):** TIGHTER (i.e. mean pairwise root-Jaccard of the 7-pericope set > corpus null mean at 10000 random length-matched draws). This contrasts the prior H-NEW (2026-05-07) showing that Iblīs-narrative is NOT FR-cohesive at the WHOLE-SURAH root-distribution level; the pre-commit here is that the PERICOPE-level signal (narrower window, narrative-only) is positive.

**H0:** The 7-pericope mean pairwise root-Jaccard is no tighter than the corpus null.

## 2. Operational definition

The 7 Iblīs-narrative pericopes are pre-specified by verse range. For each:
- Pericope tokens: union of all words (no-tashkeel orthographic tokens) in the verse range.
- Pericope roots: union of all QAC v0.4 ROOT-field assignments for those tokens (from `data/morphology/quranic-corpus-morphology-0.4.txt`).

Pairwise root-Jaccard between pericope i and pericope j:
- J(i,j) = |roots_i ∩ roots_j| / |roots_i ∪ roots_j|.

Test statistic: mean of all 21 pairwise J values among 7 pericopes.

**Null distribution**: For each of 10000 permutations, draw 7 random verse-pericopes matched in verse-length to the 7 Iblīs pericopes (verse-counts: Q 2:34 = 1 verse; Q 7:11-25 = 15; Q 15:31-44 = 14; Q 17:61-65 = 5; Q 18:50 = 1; Q 20:115-123 = 9; Q 38:71-85 = 15). Compute pairwise root-Jaccard mean under each draw. p = fraction of nulls ≥ observed.

## 3. Test statistic

- Primary: `J_mean = mean of 21 pairwise root-Jaccard values among the 7 Iblīs pericopes`.
- Significance: one-tailed permutation p (greater).
- Bonferroni: k = 1. α = 0.05.

## 4. Success / Failure

- **CONFIRMED**: `J_mean > null mean` AND `p_perm < 0.05`.
- **DIRECTIONAL**: `J_mean > null mean` but `p_perm ≥ 0.05`.
- **NULL**: `J_mean ≤ null mean` OR `p_perm ≥ 0.5`.
- **PRE-COMMIT VIOLATION**: `J_mean < null mean` (strict direction reversal). Published with full prominence.

## 5. Honest limits known a priori

- The 7 pericopes are heterogeneous in length (1 to 15 verses); shared roots Iblīs (إبلس) + ساجد (sjd) + adam (Adam-stem) + amr (amara) + abā (abaỳ) + istakbara are expected as a narrative-cycle signature.
- Even at the whole-surah level, the host surahs {Q 2, 7, 15, 17, 18, 20, 38} were already determined NOT FR-cohesive (2026-05-07 NULL). This pericope-level test is a narrower instrument; positive signal here would indicate that narrative-cycle vocabulary is concentrated in the pericope, not diluted by surrounding content.
- 1-verse pericopes (Q 2:34, Q 18:50) have small root-sets; root-Jaccard variance will be high.
- Length-matched permutation null preserves the verse-count distribution; random pericopes can span surah boundaries (drawn from the flat verse index).
- The chosen instrument (root-Jaccard) is set-based; root-frequency information is discarded. A TF-IDF variant would be a follow-up test if NULL.

## 6. Rules-tuple

`(no-tashkeel, root-tokens via QAC-v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q038_F_07_iblis_pericope_cohesion.py`. Fail-fast on mismatch.
