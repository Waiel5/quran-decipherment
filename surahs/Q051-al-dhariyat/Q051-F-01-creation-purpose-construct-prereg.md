---
surah: 51
test_id: Q051-F-01
title: Q 51:1-4 4-element fa-coordinated oath cohesion vs Q 51 baseline + sibling cluster (Q 37, 77, 100)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q051-F-01-oath-trio-cohesion
alpha_bon: 0.0167
---

# Q051-F-01 — Pre-registration: Q 51:1-4 4-element oath cohesion + sibling intra-set cohesion

## 1. Hypothesis (locked before observation)

The 4 verses Q 51:1-4 form a *fa-coordinated* oath-cluster (active-feminine-plural-participle + cognate-accusative) that is one of the corpus's signature multi-element oath openers (per al-Suyūṭī *al-Itqān* nawʿ 67, the strict-15 H-NEW-1070 cluster, and the Q 37 / Q 77 / Q 100 4+-element fa-coordinated sub-genre).

**H1 (locked direction):** Cohesion of Q 51:1-4 (mean pairwise token-cosine) is HIGHER than mean pairwise token-cosine of random 4-spans of Q 51 verses.

**H2 (locked direction):** The morphological-template parallelism (active-feminine-plural-participle + cognate-accusative) at Q 51:1-4 is corpus-EXACT verb-form-pattern, NOT shared with random 4-verse Q 51 spans.

**H3 (locked direction):** Cohesion of Q 51:1-4 is HIGHER than cohesion of Q 51:5-8 (the immediately-following 4-verse span, which contains the jawāb al-qasam).

**H0:** No directional cohesion difference between the trio and random Q 51 spans.

**Direction:** all three locked POSITIVE (Q 51:1-4 cohesion > random > comparator).

## 2. Operational definitions

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Token cohesion** C(span): mean pairwise cosine on token-bag (orthographic-tokens within each verse).
- **Root cohesion**: same operation on QAC-roots (from `data/morphology/root-index.json`).
- **Permutation null (H1)**: random 4-verse spans drawn from Q 51's 60-verse pool (without replacement; non-contiguous OK), 10,000 trials.
- **Q 51:5-8 comparator (H3)**: literal vv. 5-8.

## 3. Test statistic

- C(Q 51:1-4) at token-bag level + at QAC-root level.
- Null distribution mean + p_one-tailed.
- C(Q 51:5-8) for direct H3 comparison.

## 4. Permutation null

For H1: 10,000 random 4-verse spans from Q 51, compute C; p = fraction of nulls with C ≥ C(Q 51:1-4).

## 5. Success / Failure

- **CONFIRMED**: H1 perm-p ≤ α_bon = 0.0167 AND H2 morphological-template observed AND H3 C(1-4) > C(5-8).
- **DIRECTIONAL**: 1-2 of {H1, H2, H3} pass.
- **NULL**: All 3 fail.
- **PRE-COMMIT VIOLATION**: C(1-4) at the token level falls BELOW null mean by ≥ 1 SD (a sign-flip).

## 6. Honest limits known a priori

- The 4 verses share zero orthographic tokens pairwise (per inspection at empirical-anchor extraction — disclosed). The token-cosine cohesion will be ≈ 0; the morphological-template cohesion will be 4/4 = 100%.
- Per Q037-F-03 sibling experience: the morphological-template captures the iʿjāz, the lexical-token level does NOT. Pre-commit anticipates a likely PRE-COMMIT VIOLATION on H1 at lexical level.
- Direction-locked POSITIVE; the test is run honestly with that anticipation.
- The al-Bāqillānī 4-cosmic-stage reading is semantically-integrative; it is not directly testable at the orthographic-token level.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token-bag, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī, QAC-root)`.

## 8. Bonferroni

k = 3 (H1 token-cosine, H2 morphological-template descriptive, H3 C(1-4) vs C(5-8)). α_bon = 0.0167.

## 9. Coordination

This is a Q 51-specific test of the 4-element oath cohesion. It is a sibling test to Q037-F-03 (Q 37:1-3 trio) and to corpus-wide H-NEW-1070 (15-cluster cohesion). Independent feature space (token + root) compared to H-NEW-1070's FR matrix. No duplication.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q051_F_01_oath_cohesion.py`, verified at runtime.
