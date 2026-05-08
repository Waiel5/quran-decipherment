---
surah: 38
test_id: Q038-F-03
title: Singleton-letter self-reference — letter ص rate within Q 38 vs corpus baseline (cross-validated with Q 50 ق, Q 68 ن)
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 3
bonferroni_family: Q038-F-03-singleton-self-letter
alpha_bon: 0.01667
---

# Q038-F-03 — Pre-registration: singleton-letter self-reference rate

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Each of the three singleton-muqaṭṭaʿāt surahs amplifies its own opening letter at a rate **higher** than the corpus-wide letter-rate baseline:
- Q 38 letter ص rate > corpus ص rate.
- Q 50 letter ق rate > corpus ق rate.
- Q 68 letter ن rate > corpus ن rate.

The hypothesis is rooted in the classical *al-mubāsharatu fī al-iftitāḥ* tradition (al-Suyūṭī, *al-Itqān*, nawʿ 40, on the harmony between the muqaṭṭaʿ and the surah's letter-distribution; al-Khaṭṭābī's *bayān iʿjāz al-Qurʾān* on tongue-of-letter affinity).

**H0:** Each singleton's own-letter rate is no higher than the corpus baseline rate (or is equal).

**Direction (LOCKED, IN ADVANCE OF VIEWING DATA):** HIGHER. All three singletons should exceed corpus baseline on their own letter.

## 2. Operational definition

For each singleton surah s and its associated letter L:
- `rate_s_L = (# of L letters in body of s) / (# of all letters in body of s)`.
- `rate_corpus_L = (# of L letters in entire corpus excluding s) / (# letters in entire corpus excluding s)`.
- `Δ_L = rate_s_L − rate_corpus_L`.
- `ratio_L = rate_s_L / rate_corpus_L`.

**Body of s** = the surah verse-text under no-tashkeel, excluding the leading muqaṭṭaʿ letter itself (so the test is whether the BODY of the surah amplifies the letter, not whether the muqaṭṭaʿ glyph trivially boosts the count).

**Permutation null**: For each singleton, draw 10000 random size-matched substrings (matched in letter-count) from the rest of the corpus and compute the mean letter-rate. The pre-registered direction is `rate_s_L > permutation_mean_rate_L` for each of 3 singletons.

## 3. Test statistic

- Primary: per-singleton `Δ_L` (raw rate-difference, %-points).
- Significance: per-singleton permutation-p (one-tailed greater).
- Bonferroni-3 family threshold: α_bon = 0.05/3 = 0.01667.

## 4. Success / Failure

- **Strict success (CONFIRMED)**: All 3 singletons exceed corpus baseline AND all 3 pass α_bon = 0.01667.
- **Directional**: 2 of 3 pass.
- **NULL**: < 2 pass; or any singleton has rate BELOW corpus baseline (pre-commit violation triggers).
- **Pre-commit violation**: any singleton has its own letter at LOWER rate than corpus baseline. Published with full prominence.

## 5. Honest limits known a priori

- Letter ن is highly frequent in Arabic (~8% corpus baseline); a small absolute difference can be statistically significant due to large N. ص and ق are mid-frequency (~0.6% and ~2%).
- Body-of-surah is short for Q 50 (1.5K letters) and Q 68 (1.3K letters); permutation baseline noise is non-trivial.
- The classical tradition is ambiguous whether the letter-amplification is meant as a thematic-structural signal or as a trivial-orthographic accident. The empirical test is descriptive, not interpretive.
- This is a **DIRECTION-LOCKED PRE-COMMIT**. If results show the OPPOSITE direction (singleton DEPLETES its own letter), the test is published as a NULL with **explicit pre-commit violation** flag.

## 6. Rules-tuple

`(no-tashkeel, character-graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

To be computed at run-time. Embedded in `scripts/Q038_F_03_self_letter.py`.
