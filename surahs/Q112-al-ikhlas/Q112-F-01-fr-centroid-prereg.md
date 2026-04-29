---
preregistration_id: Q112-F-01
title: Q 112 al-Ikhlāṣ Fisher–Rao centroid status — empirical lock on *thuluth al-Qurʾān*
date: 2026-04-28
phase: B+
seed: 20260428
status: PRE-REGISTERED-LOCKED
---

# Q112-F-01 — Pre-registration: Q 112 al-Ikhlāṣ FR-centroid status

## Hypothesis (H1)

Q 112 al-Ikhlāṣ has rank ≤ 10 in mean Fisher–Rao distance to the other 113 surahs (i.e., is in the corpus's 10 most-FR-central surahs). This is the empirical correlate of the classical *thuluth al-Qurʾān* claim (al-Bukhārī #5013-15) under the al-Rāzī interpretation that Q 112 covers one of the Quran's three main content-axes.

## Null hypothesis (H0)

Q 112 ranks 11-114 (i.e., is NOT in the top-10 FR-centroids). Under the null of "Q 112 is an unremarkable terminal-short surah", we would expect it to land at random in the rank distribution.

**Stronger pre-registered claim (H1-strong)**: Q 112 ranks 1 (corpus-unique FR-centroid).

## Data

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` — 114×114 Fisher–Rao distance matrix on QAC stem-roots (K=500, Dirichlet α=0.5).

## Method

1. Reconstruct the full 114×114 distance matrix `D` from the upper-triangular list in h-new-111.json.
2. For each surah s ∈ [1, 114], compute mean_d(s) = (Σ_{j≠s} D[s, j]) / 113.
3. Rank surahs by mean_d ascending (lower = more central / closer to corpus mean).
4. Locate Q 112's rank.

## Direction

LOCKED before observation: Q 112 expected to be in **top-10** (H1) or **rank-1** (H1-strong), corresponding to "FR-central / theological-content-density-high".

## Success criteria

- H1 PASSES if Q 112 rank ≤ 10.
- H1-strong PASSES if Q 112 rank = 1.
- H1 FAILS (NULL) if Q 112 rank ≥ 11.

## Bonferroni correction

Family of pre-registered Q 112 tests is 4 (Q112-F-01 through Q112-F-04). Bonferroni-corrected threshold for any individual finding's "law-strength" claim: α = 0.05 / 4 = 0.0125. The rank-1-of-114 result, if obtained, has p-value 1/114 = 0.00877 < 0.0125 (under the null of uniform rank), so Bonferroni-corrected significant.

## Multiple-models check (MW-3)

- Primary: FR-roots K=500 (h-new-111).
- Secondary check: same metric on K=200 and K=1000 vocabulary truncations would be ideal but not on disk; documented as honest-limit.

## Replication (MW-5)

- The h-new-111 matrix is the project's canonical FR distance matrix. No additional seed-replication available without re-computing root-tokens.

## Honest pre-commit clause

If Q 112 ranks ≥ 11, this is published as NULL with full prominence. The *thuluth al-Qurʾān* claim survives as a theological-tradition claim but loses its FR-roots empirical correlate.

## Run script

`scripts/Q112_F_01_fr_centroid.py` (pre-registered SHA: this file's SHA-256 will be computed and embedded into the script header).

## Pre-reg SHA-256

Computed at lock-time, inserted here:
```
PREREG_SHA: (computed from this file at runtime; verified in script header)
```
