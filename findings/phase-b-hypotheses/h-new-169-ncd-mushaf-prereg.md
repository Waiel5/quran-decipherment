---
id: H-NEW-169
title: Mushaf order is information-theoretic geodesic-optimal under NCD (cross-finding-011 third-axis replication)
phase: B
status: PRE-REGISTERED
date: 2026-04-17
seed: 20260419
bonferroni_k: 2
parent: cross-finding-011
rules_tuple: (114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-Surah-1, canonical mushaf order, Normalized Compression Distance via lzma)
---

# [[h-new-169-ncd-mushaf|H-NEW-169]] — NCD matrix of 114 surahs (third-axis [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] replication)

## Background

[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] CONFIRMED that the mushaf ordering is Fisher-Rao
information-geodesic optimal under TWO feature spaces:
- QAC-STEM roots (K=500): z = −11.46, ratio L/L_2opt = 1.107
- Character-4-grams (K_char=2000): z = −11.41, ratio = 1.114

These two features are content-orthogonal but both parametric: they
embed surahs in a simplex and compute Riemannian geodesics on the
Fisher manifold.

[[h-new-169-ncd-mushaf|H-NEW-169]] tests a THIRD entirely different (non-parametric,
information-theoretic) axis: Normalized Compression Distance (NCD)
computed from the lzma compressor.

## Method

1. Surahs loaded from `quran-text/quran-no-tashkeel.json` as
   space-joined verse strings. Basmala counted only in Surah 1 (per
   rules-tuple).
2. NCD(x, y) = (C(xy) − min(C(x), C(y))) / max(C(x), C(y))
   where C(s) = len(lzma.compress(s.encode('utf-8'))) using the
   xz preset 9 | EXTREME for best compression (default python
   `lzma.compress` with preset=9|lzma.PRESET_EXTREME).
3. 114×114 symmetrized NCD matrix: D[i,j] = (NCD(i,j) + NCD(j,i)) / 2.
   Diagonal forced to 0.
4. Primary: L_mushaf = Σᵢ D[i, i+1] (113 consecutive edges).
5. Null: 10,000 uniform random permutations of 114 surahs (seed =
   20260419, python random.Random with Fisher-Yates via
   `random.shuffle`). Compute L_perm for each.
6. p_primary = (#{L_perm ≤ L_mushaf} + 1) / (N_perm + 1).

## Tests (Bonferroni k=2, α_bon = 0.025)

### PRIMARY — mushaf path shorter than random
  H0: L_mushaf ~ uniform over L_perm
  H1: L_mushaf < L_perm (1-sided lower)
  PASS iff p_primary < 0.025

### SECONDARY A — near-TSP-optimality under NCD
  Compute greedy-NN-from-each-start (114 starts) + 2-opt refinement
  on each; take the best as L_2opt_best (approximate TSP upper bound
  on the open-path optimum).
  Report ratio_open = L_mushaf / L_2opt_best.
  Expected direction: ratio < 1.5 (i.e., mushaf within 50% of TSP-2opt
  upper bound).

### Also reported (not α-spent)

- Cycle length L_cycle = L_mushaf + D[114, 1] (wrap-around).
- Cycle TSP upper bound L_cycle_2opt via best greedy+2-opt cycle.
- ratio_cycle = L_cycle / L_cycle_2opt.
- MW-5 positive control: greedy-NN-from-surah-1 synthetic ordering
  should have path length dominated by the 2-opt solution and
  substantially shorter than random mean.

## Decision rule for [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]

- If PRIMARY passes in the same direction as FR-roots and FR-char4gram
  (L_mushaf < random) → [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] gains a THIRD independent
  confirmation (NCD is compression-theoretic, non-parametric,
  non-simplex), and its CONFIRMED status is reinforced via multi-axis
  convergence.
- If PRIMARY fails or reverses → [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] remains confirmed
  on FR-axis only, and NCD joins verse-length as a feature-specific
  non-replication.
- Bonferroni k = 2 (primary + secondary A).

## Locked parameters

- SEED = 20260419
- N_PERMS = 10000
- Compressor: python stdlib `lzma` with
  `lzma.compress(..., preset=9 | lzma.PRESET_EXTREME)`
  (LZMA2 default format, max compression).
- NCD symmetrization: arithmetic mean of NCD(x,y), NCD(y,x).
- Text encoding: utf-8, verses space-joined, no tashkeel.
- Basmala retained in Surah 1 verse 1 and nowhere else (per rules-tuple).

## Garden-of-forking-paths log (pre-run)

Free parameters explicitly locked before execution:
- compressor choice → lzma preset 9|EXTREME (as task spec says "Use
  lzma for better compression")
- NCD formula → (C(xy) − min(C(x),C(y))) / max(C(x),C(y)) [Cilibrasi-Vitányi 2005]
- symmetrization → mean (not min, not concat both directions separately)
- concatenation separator → single byte 0x00 (explicit boundary)
- surah text preparation → verse strings joined with single space
  (matches FR-char4gram preprocessing for comparability across axes)
- null model → uniform random permutations of exactly the 114 surah
  IDs (positional null; does not resample verses)
- seed → 20260419 (distinct from parent 20260417; prevents any
  accidental correlated sampling)

Post-hoc changes to any of the above would invalidate the test.
