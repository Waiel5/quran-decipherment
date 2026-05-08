---
surah: 21
test_id: Q021-F-04
title: Cosmological-verse neighborhood cohesion — do Q 21:30-33 form a distinct sub-cluster?
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
bonferroni_family: Q021-F-04-cosmological-cluster-single-cell
alpha_bon: 0.05
direction: HIGHER (vv. 30-33 internal-cohesion > permutation null)
---

# Q021-F-04 — Pre-registration: cosmological cluster cohesion

## 1. Hypothesis (locked)

**H1 (one-tailed, locked):** The 4-verse block Q 21:30–33 has internal lexical-cohesion (mean pairwise root-Jaccard or TF-IDF cosine) HIGHER than a permutation null of randomly-selected size-4 verse-blocks from Q 21.

**H0:** Q 21:30–33 has cohesion at or below the permutation-null median.

**Direction (LOCKED):** sim(vv. 30-33) > median(null distribution).

## 2. Operational definition

For Q 21's 112 verses:
- Tokenize each verse to its STEM-root multiset (QAC v0.4).
- Verse-level bag-of-roots vector (binary or count; pre-committed to **count** vector).
- Per-block cohesion = mean pairwise cosine similarity between the 4 verse vectors in vv. 30-33 (= 6 pairs).
- **Permutation null**: 10 000 random size-4 blocks of contiguous verses sampled uniformly from Q 21 verses 1-112 (with replacement of starting position; 1 ≤ start ≤ 109).
- **Permutation null secondary**: 10 000 random size-4 blocks of NON-contiguous (independently-sampled) verses.

## 3. Test statistic

- **Primary**: rank of sim(vv. 30-33) within the 10 000-element contiguous-block null. p_one_sided = (# nulls ≥ observed) / N_null.
- **Secondary**: same against non-contiguous null (a sanity check).

## 4. Success / Failure criteria (Bonferroni k=1, α = 0.05)

- **Strict success (CONFIRMED)**: contiguous-null p ≤ 0.05 AND non-contiguous-null p ≤ 0.05.
- **DIRECTIONAL**: contiguous-null p ≤ 0.10 OR non-contiguous-null p ≤ 0.05 (one of two passing).
- **NULL**: both p > 0.10.

## 5. Honest limits known a priori

- 4-verse blocks have only 6 pairwise comparisons; the cohesion metric is high-variance for small n.
- Q 21 has 112 verses, so the contiguous-null sample space is large. Power should be acceptable for a moderate-effect-size test.
- Cosmological lexicon (sky, earth, mountains, sun, moon, water, light) is *itself* internally cohesive in a vocabulary sense; the test does not separate "cosmological-vocab cluster" from "any thematically-tight 4-verse cluster". A passing result confirms the literary-thematic claim; it does NOT prove the thematic-cluster is *cosmological-iʿjāz-specific*.
- The al-Biqāʿī claim (vv. 30-33 form a *naẓm*-coherent unit) is the classical anchor; Q021-F-04 tests the empirical correlate.

## 6. Rules-tuple

`(QAC-v0.4-STEM-roots-per-verse, count-vector, cosine-similarity, no-tashkeel)`.

## 7. SHA256 lock

To be computed at runtime by `scripts/Q021_F_04_cosmological_cluster.py`. Embedded in script and verified at execution.
