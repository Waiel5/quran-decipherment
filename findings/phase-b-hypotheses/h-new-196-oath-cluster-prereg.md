---
finding_id: h-new-196-oath-cluster
phase: B
status: PRE-REG
date: 2026-04-17
author: h-new-196-autonomous
parent: h-new-85-oath-openers (21-surah oath set)
seed: 20260419
rules_tuple: (no-tashkeel, hafs-kufan, canonical-114, H-NEW-85-locked-oath-set, K_TOP=500, DIRICHLET_ALPHA=0.5, Fisher-Rao metric)
null_models: permutation null — 10,000 random draws of 21 distinct surah-IDs from {1..114}
bonferroni_k: 2
bonferroni_family: h-new-196-oath-cluster
alpha_bon: 0.025
---

# [[h-new-196-oath-cluster|H-NEW-196]] — Oath-opening surah structural cohesion

## Background

[[h-new-85-oath-openers|H-NEW-85]] CONFIRMED the 21 classical oath-opener surahs (from [[h-new-61-opening-words|H-NEW-61]]
OATH_PARTICLE class) as mechanically verified by QAC walker. The locked
set (contradicts some looser classical enumerations; we adopt [[h-new-85-oath-openers|H-NEW-85]]'s
mechanically-verified list):

  Q 36, 37, 38, 43, 44, 50, 51, 52, 53, 68, 77, 79, 85, 86, 89, 91, 92,
  93, 95, 100, 103  (n=21, all Meccan)

[[h-new-85-oath-openers|H-NEW-85]] further confirmed Q 91 al-Shams is the unique structural maximum
(7 oath-verses, 8 head-NPs, 4 category-diversity).

TASK-STATED alternate list (Q 37, 51, 52, 53, 56, 68, 75-79, 81, 84, 85,
86, 89, 90, 91, 92, 95, 100, 103) includes non-waw-qasam openers
(Q 56, 75, 78, 90 open with non-waw particles) and the [[h-new-85-oath-openers|H-NEW-85]]-verified
list excludes them. We pre-commit to [[h-new-85-oath-openers|H-NEW-85]]'s locked set (authority:
mechanical QAC-walker verification) AND report the alternate-list
replication as a secondary sensitivity.

## Hypothesis

**H1 (cluster cohesion, PRIMARY)**: The 21 oath-opener surahs form a
significantly TIGHTER cluster in Fisher-Rao information space than
random 21-surah samples. Formally, let D be the 114×114 Fisher-Rao
distance matrix (top-500 stem roots, Dirichlet α=0.5, [[h-new-111-fisher-rao-mushaf|H-NEW-111]]
parameterization). Let M(S) = mean pairwise D[i,j] for i,j ∈ S. Test
whether M(oath-21) < M(random-21) at one-sided permutation p < α_bon.

**H2 (mode assignment, SECONDARY)**: The 21 oath-opener surahs
disproportionately cluster into a specific compositional mode (defined
as a k-means clustering of surahs in Fisher-Rao-embedded space, k=5,
seed=20260419). Test χ² vs uniform-5 expected distribution. Note:
H-NEW-191 (5-mode clustering) does not exist as a prior finding;
this hypothesis operationalizes "5 modes" as k=5 k-means on the
top-500-root compositional representation.

## Pre-committed analyses

1. **Cell V (Verify)**: Scan v1 of all 114 surahs for wa-prefix (و/وال)
   qasam pattern; cross-check with [[h-new-85-oath-openers|H-NEW-85]]'s 21 oath list. Record
   overlap and divergence vs both task-stated and [[h-new-85-oath-openers|H-NEW-85]] locked lists.

2. **Cell H1 (Cluster cohesion PRIMARY)**:
   - Compute M(oath-21) = mean pairwise Fisher-Rao D
   - Permutation null: 10,000 random 21-surah samples, compute M(rand-21)
   - p_H1 = (#{M(rand) ≤ M(oath)} + 1) / (N + 1)
   - PASS if p_H1 < 0.025 (Bonferroni for k=2)
   - Also report 1%, 5%, 50%, 95%, 99% quantiles of null

3. **Cell H2 (Mode assignment SECONDARY)**:
   - Project surahs to their L1-normalized top-500-root probability vector
   - k-means, k=5, init=k-means++-like (deterministic with seed 20260419)
   - Count oath-21 per mode; χ² vs expected = 21/5 = 4.2 per mode
   - PASS if p_H2 < 0.025

4. **Cell S (Sensitivity)**: Repeat H1 with the task-stated alternate
   21-surah list (Q 37, 51, 52, 53, 56, 68, 75, 76, 77, 78, 79, 81, 84,
   85, 86, 89, 90, 91, 92, 95, 100, 103 — if 22 items, we use the
   22-item set for this sensitivity only). Descriptive only.

## Features

For Cell H2 per-surah compositional features (supplementary to
root-probability vector): verse_count, mean_verse_length_chars,
oath_cluster_length_verses, oath_head_np_count, category_diversity.

## Verdict table (pre-committed, k=2)

| Cell | Test | PASS if |
|---|---|---|
| V | 21-list verification | ≥19/21 match [[h-new-85-oath-openers|H-NEW-85]] locked |
| H1 | M(oath) < M(random-21) | p_perm < 0.025 |
| H2 | χ² mode-assignment | p_χ² < 0.025 |

Bonferroni α_bon = 0.05 / 2 = 0.025.

## Interpretation

If H1 PASS + H2 PASS: oath-opener surahs form a mechanically distinct
compositional cluster — the waw-qasam rhetorical gear correlates with
substantive compositional similarity.

If H1 PASS + H2 NULL: oath-openers are a tight CLOUD but not a SINGLE
mode — they share a common sub-topology in Fisher-Rao space without
concentrating on one centroid.

If H1 NULL + H2 PASS: oath-openers locate a mode but aren't tighter
than random — they occupy a sub-region, not a sub-neighborhood.

If both NULL: the waw-oath is purely a SURFACE rhetorical marker with
no compositional footprint (consistent with [[h-new-85-oath-openers|H-NEW-85]] Cells 4+5 NULL —
length and jawāb-theme don't separate oath-openers either).

## Files

- Script: `scripts/h_new_196_oath_cluster.py`
- JSON results: `findings/phase-b-hypotheses/data/h-new-196.json`
- Findings: `findings/phase-b-hypotheses/h-new-196-oath-cluster.md`
