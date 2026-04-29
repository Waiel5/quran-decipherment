---
id: H-NEW-630
title: "Pre-reg — Q 67-114 super-cluster sub-structure test"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-580 §4 — Q 67-114 identified as corpus-densest cohesion super-cluster (6 non-overlapping windows ≤8%ile); test whether it has hierarchical internal structure
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260432
---

# [[h-new-630-supercluster-substructure|H-NEW-630]] — Q 67-114 super-cluster sub-structure: Pre-Registration

## 1. Context

[[h-new-580-five-factor-regression|H-NEW-580]] §4 identified Q 67-114 as a 48-surah super-cluster with corpus-extreme content cohesion (6 non-overlapping windows tested ≤8%ile in FR-roots distance). Two hypotheses are possible:

- **H1-flat**: Q 67-114 is a SINGLE uniform-cohesion zone; arbitrary partitioning shows comparable d̄ within and between sub-blocks.
- **H1-hierarchical**: Q 67-114 contains internal sub-clusters with within-block cohesion stronger than between-block.

[[h-new-630-supercluster-substructure|H-NEW-630]] distinguishes these.

## 2. Sub-cluster partitioning (locked)

Three hypothesized sub-clusters mapped to classical *al-mufaṣṣal* sub-divisions:

- **A: Q 67-77** (N=11) — mufaṣṣal-awsāṭ (al-Zarkashī's "middle mufaṣṣal").
- **B: Q 78-99** (N=22) — mufaṣṣal-qiṣār upper half (eschat-creedal Meccan core).
- **C: Q 100-114** (N=15) — mufaṣṣal-qiṣār lower half (terminal-tail).

This partitioning follows al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān* mufaṣṣal subdivision tradition; al-Suyūṭī *al-Itqān* concurs.

## 3. Test design

For each pair (i, j) ∈ A∪B∪C:
- Within-cluster d̄: mean pairwise FR distance among surahs within A, within B, within C.
- Between-cluster d̄: mean pairwise FR distance for pairs with one member in cluster X and one in cluster Y.

### Primary tests
1. **PRIMARY-A**: d̄(within-A) vs full-corpus N=11 random null.
2. **PRIMARY-B**: d̄(within-B) vs full-corpus N=22 random null.
3. **PRIMARY-C**: d̄(within-C) vs full-corpus N=15 random null.
4. **PRIMARY-AB**: d̄(between-A,B) vs random-cross-block null (size 11×22 pair-mean).
5. **PRIMARY-AC**: d̄(between-A,C) vs null.
6. **PRIMARY-BC**: d̄(between-B,C) vs null.

### Discriminating test
**MW-5 hierarchical**: If hierarchical, expect:
- d̄(within-X) < d̄(between-X,Y) for each pair (within tighter than between).

Compute Δ = d̄(between) − d̄(within). All 3 within-blocks have a unique Δ to each of the other 2 blocks. Average over 3 within-clusters of mean(Δ_to_other_two). Positive Δ = hierarchical.

### Permutation null for hierarchy
Shuffle the 48 cluster-labels among the 48 surahs (10000 perms, seed 20260432). Compute null distribution of mean Δ. Empirical p-value of observed Δ.

## 4. Pre-committed predictions

If H1-hierarchical:
- All 3 within-cluster %iles ≤ 5.
- Mean Δ > 0 with permutation p ≤ 0.0167 (Bonferroni-3).
- Specific between-pair: A-C is FARTHEST (longest mushaf separation), so d̄(A-C) should be largest.

If H1-flat:
- Within and between are comparable; mean Δ ≈ 0.
- All 6 d̄ values cluster around the same magnitude.

## 5. Bonferroni structure

- 6 primary tests + 1 hierarchy test = 7 tests.
- α corrected = 0.05 / 7 = 0.00714.

## 6. Pass/fail thresholds

- **STRICT PASS (hierarchical)**: All 3 within-%iles ≤ 0.71 (Bonferroni); permutation p(mean Δ) ≤ 0.00714; mean Δ > 0.05 (in FR distance units).
- **DIRECTIONAL**: All 3 within-%iles ≤ 5.0; permutation p ≤ 0.05; mean Δ > 0.
- **FLAT**: any of: ≥1 within-%ile > 5; mean Δ ≤ 0.
- **NULL**: opposite direction (mean Δ < 0).

## 7. Methodology rules

- MW-1: instrument-prior — FR-roots distance.
- MW-2: corpus-prior — 10000-perm percentile.
- MW-5: hierarchical replication test.
- PRE-REG-STANDARD-04: hypotheses, null, direction, Bonferroni, success criteria all locked.

## 8. Direction of effect (locked)

- All 3 within-cluster d̄ values: SMALLER than full-corpus null (low %ile expected).
- All 3 between-cluster d̄ values: similar to within-cluster IF flat; larger IF hierarchical.
- Mean Δ: POSITIVE if hierarchical.

## 9. Files

- Script: `scripts/h_new_630_supercluster_substructure.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-630.json`
- Findings: `findings/phase-b-hypotheses/h-new-630-supercluster-substructure.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
