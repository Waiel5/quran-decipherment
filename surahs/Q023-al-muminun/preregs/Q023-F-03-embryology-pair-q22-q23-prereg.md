---
finding_id: Q023-F-03
title: Embryology pericope Q 23:12-14 vs Q 22:5 — tighter lexical similarity than length-matched null
date: 2026-05-09
seed: 20260509
n_perms: 10000
status: PRE-REGISTERED
rules_tuple: (no-tashkeel, orthographic-token-Jaccard, basmala-counted-only-in-Q1, Hafs-Kufan)
---

# Q023-F-03 — Embryology pericope pair Q 23:12-14 vs Q 22:5 lexical similarity

## 1. Background

Q 23:12-14 (sulāla → nuṭfa → ʿalaqa → muḍgha → ʿiẓām → laḥm → khalqan ākhar) and Q 22:5 (nuṭfa → ʿalaqa → muḍgha → mukhallaqa → makhlūqa → ṭiflan → ashuddakum → ...) are the corpus's two flagship embryology-passages. Classical mufassirūn (al-Qurṭubī ad loc. Q 23:14) explicitly cross-reference them: "the discussion of nuṭfa and ʿalaqa and muḍgha and the rulings on them have already been treated at the start of al-Ḥajj."

A third related pericope is Q 75:37-40 (nuṭfa min maniyy → ʿalaqa → khalq → dhakar / unthā).

## 2. Hypothesis

**Pre-registered DIRECTION**: Q 23:12-14 and Q 22:5 share lexical content (orthographic tokens) at a rate **HIGHER** than a length-matched corpus null.

Specifically, the **Jaccard similarity** of their orthographic-token sets — computed over no-tashkeel text — is HIGHER than the 95th percentile of pairwise Jaccard similarities for random length-matched verse-pairs from the corpus.

**Length-matching**: Q 23:12-14 = 3 verses (~ 30 tokens). Q 22:5 = 1 verse (~ 70 tokens). The null is constructed by sampling random pairs (V_A, V_B) where V_A is a contiguous 3-verse block from anywhere in the corpus and V_B is a 1-verse block, computing Jaccard, and aggregating over 10000 such pairs.

**Failure direction**: if Q 23:12-14 ↔ Q 22:5 Jaccard is at or BELOW the corpus median Jaccard, publish as NULL. Direction reversed = pre-commit violation per Protocol §1.8.

## 3. Test procedure

1. Extract Q 23:12-14 orthographic tokens (no-tashkeel) from `quran-text/quran-no-tashkeel.json`.
2. Extract Q 22:5 orthographic tokens (same).
3. Compute observed Jaccard similarity: `J_obs = |A ∩ B| / |A ∪ B|`.
4. Length-matched null: sample 10000 (3-verse-contiguous, 1-verse) pairs from the corpus, excluding the target pair; compute Jaccard for each; aggregate.
5. p = (#{J_null ≥ J_obs} + 1) / (N+1) — upper-tailed because direction predicts higher.

Secondary tests:
- Q 23:12-14 vs Q 75:37-40 (3 verses each, length-matched).
- All three pairwise (Q 22:5, Q 23:12-14, Q 75:37-40).

## 4. Decision rules

- **PASS-DIRECTED (CONFIRMED)**: upper-tail p ≤ 0.05. Embryology pair is lexically tighter than null.
- **NULL**: upper-tail p > 0.05.
- **PRE-COMMIT VIOLATION**: J_obs strictly below corpus median → flag.

Bonferroni note: this is **1 of 3 pre-registered tests** in the Q 23 specialist landing; family-corrected α = 0.05/3 = 0.0167.

## 5. MW protections

- **MW-1 (instrument)**: Jaccard on orthographic-no-tashkeel tokens; locked.
- **MW-2 (corpus)**: 10000 permutations.
- **MW-3 (alt models)**: report a content-stem variant (Arabic light-stemmer dropping common prefixes ال / و / ف / ب / ل / ك) for comparison.
- **MW-6 (instrument-control)**: compute Jaccard for a control random pair (Q 23:1-3 vs Q 22:5) — should be near the null median.

## 6. Pre-reg lock

This file is locked at SHA256-of-contents. Embedded in the runner script. Verified at runtime.
