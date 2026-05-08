---
finding_id: Q026-F-03
title: Anti-poetry coda (Q 26:224-227) lexical distinctness vs surah body
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q026-F-01..F-05
alpha_bon: 0.01
acceptance_window: see §6
---

# Q026-F-03 — Anti-poetry coda lexical distinctness

## 1. Hypothesis (locked before observation)

**H1**: The 4-verse coda Q 26:224-227 (the *al-shuʿarāʾ* coda) is the *most-distinctive* 4-verse window in Q 26 by root-cosine distance from the surah-mean root distribution.

**H0**: The coda is no more distinctive than a random 4-verse window in Q 26.

## 2. Operational definition

- Surah Q 26 = 227 verses → 224 sliding 4-verse windows W_i = (v_i, v_{i+1}, v_{i+2}, v_{i+3}), i = 1..224.
- Per-window TF vector over QAC roots; the surah-mean TF vector is computed from all 227 verses.
- `dist(W_i)` = 1 − cosine(TF(W_i), TF(surah-mean)).
- The coda window is W_224 = (v224, v225, v226, v227).

## 3. Test statistic

- `rank_coda` = rank of dist(W_224) among 224 windows (1 = max-distinctive).
- `pct_coda` = (rank_coda − 1) / (224 − 1) ; pct = 0 means MOST distinct.

## 4. Direction (LOCKED)

- Coda is most-distinct: rank_coda = 1 (top-1 of 224).
- One-sided lower-tail; α_bon = 0.01.

## 5. Permutation null

Seed 20260507. 10000 perms — random shuffles of root-tokens to verses preserving verse-token-counts; recompute the coda window vs all 224 windows; count of `rank_coda_perm ≤ 1` ; p_perm = (1 + count) / (1 + 10000).

## 6. Acceptance

- **CONFIRMED** = rank_coda = 1 AND p_perm < 0.01.
- **DIRECTIONAL** = rank_coda ≤ 5 AND p_perm < 0.05.
- **NULL** = rank_coda > 11 (top-5%).
- **PRE-COMMIT VIOLATION** = rank_coda > 200 (anti-prediction).

## 7. Rules-tuple

`(no-tashkeel, QAC-stem-roots, sliding-4-verse-windows, Hafs-Kufan, Mashriqi)`. Source for QAC roots: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.

## 8. Anti-hallucination

QAC root file path stated above; verse-text from `quran-text/quran-no-tashkeel.json`.

## 9. Honest a-priori limits

- The coda is short (4 verses, ~56 words). Sparse vectors give noisier cosine. We use Laplace smoothing (+1) on the surah-mean vector.
- We are testing one window of one surah — n=1 effective. Permutation null protects against false-positive but does not give a corpus-wide rate.
- Classical claim (al-Bāqillānī Iʿjāz al-Qurʾān): the coda is rhetorically distinct as anti-poetry-statement. This test is the empirical counterpart to that classical claim. Lexical distinctness is necessary but not sufficient evidence; the genre-claim itself is testable in F-05.
- The coda contains the unique surah-name-token *الشعراء* (which appears nowhere else in Q 26 — single instance v 224). Surah-name tokens by definition spike in their own corner; the test is whether the broader 4-verse window's full TF still ranks #1 of 224.
