---
finding_id: Q024-F-03
title: "al-ifk passage (Q 24:11-20) cohesion vs random control + Q 24:35 structural-midpoint test"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 2024
n_random_spans: 2000
direction_ifk: positive (al-ifk expected more cohesive than random)
direction_midpoint: positive (Q 24:35 expected to contain word and letter median of Q 24)
---

# Q024-F-03 — al-ifk cohesion + Q 24:35 structural midpoint

## Hypothesis A (al-ifk cohesion)

The al-ifk passage Q 24:11-20 has higher mean pairwise root-Jaccard cohesion than 80% of random 5-10-verse intra-surah spans drawn from the rest of the corpus.

## Hypothesis B (structural midpoint)

Q 24:35 contains both:
- The median word of Q 24 (no-tashkeel-orthographic, mushaf-marks-stripped, basmala-not-counted-since-not-in-Q24).
- The median letter of Q 24 (same rules-tuple, no spaces).

## Rules-tuple

`(no-tashkeel, QAC-stem-roots for cohesion test, no-tashkeel-orthographic for word/letter counts, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`

## Cohesion metric

For verses i, j with QAC root-counter R_i, R_j:
- Jaccard(i, j) = |R_i ∩ R_j| / |R_i ∪ R_j|
Where set-intersection/union is on the keys (distinct roots).

Passage cohesion = mean over all C(n, 2) verse-pairs in the passage.

## Random control

Random 5-10-verse contiguous intra-surah spans drawn uniformly from the corpus. n=2000 random samples, seed=2024.

## Direction-locked

- Direction A: al-ifk cohesion > 80th percentile of random control. Confirms.
- Direction A: al-ifk cohesion in [50, 80] — DIRECTIONAL (no Bonferroni claim).
- Direction A: al-ifk cohesion < 50 — NULL.

- Direction B: Q 24:35 contains both word-median AND letter-median — CONFIRMED.
- Direction B: contains one but not the other — DIRECTIONAL.
- Direction B: contains neither — NULL.

## Output

- Pre-reg: this file.
- Script: `scripts/Q024_F_03_ifk_cohesion_midpoint.py`.
- JSON: `csv/Q024-F-03.json`.
