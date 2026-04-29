---
surah: 12
test_id: Q012-F-02
title: Per-narrative-phase internal cohesion of Q 12
file_type: pre-registration
date_locked: 2026-04-28
seed: 20260428
---

# Q012-F-02 — Pre-registration: per-phase cohesion

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 12, partitioned into 9–10 narrative phases per `00-overview.md` §8, exhibits **internal cohesion within each phase that exceeds the random-pairing null** for at least 5 of 10 phases (Bonferroni-corrected α=0.005, k=10).

**H0:** Per-phase mean pairwise TF-IDF cosine similarity is no greater than that of a random size-matched verse-set drawn from Q 12.

**Direction:** Within-phase mean cosine > random-permutation null mean (LOCKED).

## 2. Operational definition

**Phase split** (locked from `00-overview.md`):
| # | Label | Verses |
|--|--|--|
| 1 | Opening | 1–3 |
| 2 | Dream | 4–6 |
| 3 | Well/Brothers | 7–18 |
| 4 | Caravan/Egypt sale | 19–22 |
| 5 | ʿAzīz wife/seduction/prison | 23–34 |
| 6 | Prison-dreams + Pharaoh | 35–49 |
| 7 | Elevation | 50–57 |
| 8 | Brothers' visits | 58–82 |
| 9 | Reunion | 83–101 |
| 10 | Epilogue | 102–111 |

**Vector representation**: per-verse TF-IDF on Q 12-internal vocabulary (no-tashkeel, whitespace-tokenized, taʿaġġam markers stripped: ۚ ۖ ۗ ۛ ۙ ۘ).

**Test statistic per phase**: mean pairwise cosine similarity within the phase.

## 3. Null distribution

Permutation null: for each phase of size n_v, draw 10000 random samples of n_v verses from Q 12, compute mean pairwise cosine similarity. Rank actual statistic in the null. (Run uses 1000 perms for speed; flag if marginal.)

p_greater = #(null ≥ actual) / n_perm.

## 4. Bonferroni correction

k = 10 phases tested. α_corrected = 0.05 / 10 = 0.005.

## 5. Success / Failure

- **CONFIRMED (collective)**: ≥ 5 phases pass Bonferroni-corrected α.
- **DIRECTIONAL**: 2–4 phases pass.
- **NULL**: ≤ 1 phase passes; the phase split is not internally coherent.

## 6. Honest limits known a priori

- TF-IDF on a single 111-verse corpus is noisy; verse-pair counts in n=3 phases (Opening, Dream) are too small for power.
- The phase split is a **literary judgment** from the overview, NOT an algorithmic optimum. A different split could yield different cohesion. This test asks: **given the literary phase split, is it internally coherent?**

## 7. Rules-tuple

`(no-tashkeel, whitespace-token, TF-IDF-internal, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. SHA256 lock

Embedded at run-time in `scripts/Q012_F_02_phase_cohesion.py`.
