---
prereg_id: Q026-F-06
title: 7-prophet narrative root-Jaccard cohesion within Q 26 vs random Meccan sub-blocks
date_locked: 2026-05-09
seed: 20260509
rules_tuple: (no-tashkeel, QAC-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
bonferroni_family: Q026-F-06..F-07 (k=2); α_per_test = 0.025
direction_locked_before_observation: yes
---

# Q026-F-06 — 7-prophet narrative root-Jaccard cohesion vs random sub-blocks

## Hypothesis (locked, one-sided)

The 7 prophet-pericopes inside Q 26 (Mūsā 10-68, Ibrāhīm 69-104, Nūḥ 105-122,
Hūd 123-140, Ṣāliḥ 141-159, Lūṭ 160-175, Shuʿayb 176-191) form a more
lexically-cohesive 7-block decomposition by mean pairwise root-Jaccard than
7 equally-sized sub-blocks drawn from comparable Meccan narrative surahs
(Q 7, Q 11, Q 21, Q 38, Q 51 — all prophet-cycle surahs of overlapping
narrative subject matter).

Direction: **Q 26 mean pairwise Jaccard > random-block mean pairwise Jaccard**
(one-sided upper tail).

## Method

1. Build per-block QAC root-set for each of the 7 Q 26 prophet-pericopes
   (set of distinct ROOT codes in QAC v0.4 covering those verses).
2. Compute mean pairwise Jaccard over the C(7,2)=21 pairs → `J_Q26_obs`.
3. Null: 10,000 permutations, each draws 7 contiguous sub-blocks of length
   {59,36,18,18,19,16,16} (the empirical Q 26 cycle lengths) from the
   pooled verse-pool of {Q 7, Q 11, Q 21, Q 38, Q 51} (random surah, random
   start within bounds, with replacement across surahs) and computes the
   same mean pairwise Jaccard.
4. p_perm = fraction of null draws with mean-Jaccard ≥ `J_Q26_obs`.

Seed: 20260509. Random module: `random.Random(20260509)`.

## Pass criterion

p_perm < α_per_test = 0.025 (one-sided upper tail) AND
`J_Q26_obs` ≥ null_mean + 1 SD.

## Fail / NULL criteria

- p_perm ≥ 0.025 → NULL.
- Observed direction reversed (`J_Q26_obs` < null_mean) → PRE-COMMIT VIOLATION,
  published as such per protocol §1.3.

## Honest limits (pre-stated)

- Random-block draw with replacement across 5 source surahs may include
  multiple draws from the same surah; this is acceptable as a null that
  preserves narrative-Meccan vocabulary distribution.
- Root-Jaccard ignores frequency weights; a TF-cosine variant might give
  different result — not pre-registered here.
- The 5-surah baseline pool is deliberately narrative-Meccan to control
  for genre. A broader corpus-wide null would inflate cohesion of Q 26
  prophet-blocks trivially.

## Cross-references

- [[Q026-F-01]] — refrain-cycle structure (CONFIRMED).
- [[Q026-F-04]] — Mūsā-block twin (FALSIFIED).
- [[h-new-1320]] — refrain triplet architecture.
