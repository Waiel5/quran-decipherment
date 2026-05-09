---
surah: 34
test_id: Q034-F-01
title: al-ḥamdu li-llāh opener cluster {Q 1, 6, 18, 34, 35} Fisher-Rao cohesion test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q034-F-01-hamd-cluster
alpha_bon: 0.01667
---

# Q034-F-01 — Pre-registration: al-ḥamdu li-llāh opener cluster FR cohesion (OQ-3 candidate)

## 1. Hypothesis (locked before observation)

The 5 surahs whose first non-basmala verse begins with *al-ḥamdu li-llāh* — {Q 1, Q 6, Q 18, Q 34, Q 35} — are conjectured (per HANDOFF/05-OPEN-QUESTIONS OQ-3 candidate) to form a **second book-introduction-marker class** analogous to the muqaṭṭāʿat (cross-finding-006/008). The test direction is locked: **the cluster is FR-cohesive at the group level**.

**H1 (locked direction, primary cohesion test):** The within-cluster mean Fisher-Rao distance over root-distributions on the 5 surahs ({Q 1, 6, 18, 34, 35}, 10 pairs) is **LOWER** than the random-5-tuple permutation null mean (n_perm = 10,000). Direction-locked: lower = cohesive. Pass at α = 0.05/3 = 0.01667 single-tailed.

**H2 (locked direction, drop-Q1 sensitivity test):** Q 1 al-Fātiḥa is a known sui-generis isolate (per H-NEW-89; cross-finding-009). Even excluding Q 1, the 4-cluster {Q 6, 18, 34, 35} mean within-pair FR is LOWER than the random-4-tuple permutation null mean. Pass at α = 0.01667.

**H3 (locked direction, length-residualized cohesion):** After residualizing pairwise FR distances on |log(verse-count_i) - log(verse-count_j)| (controlling for the length-confound at the primary-test level per MW-1), the 5-cluster mean residual is **NEGATIVE** (i.e., closer-than-expected for given length-difference). Pass at α = 0.01667.

## 2. Operational definitions

### Data
- FR matrix: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular` (decoded to symmetric 114×114 matrix).
- Verse counts: `data/hafs-verse-counts.tsv`.
- Cluster identification: 5 surahs whose first verse (excluding basmala) is exactly *al-ḥamdu li-llāh* — verified by regex match on `quran-text/quran-no-tashkeel.json`.

### H1: within-cluster mean FR
- Cluster = {Q 1, Q 6, Q 18, Q 34, Q 35}; |cluster| = 5; |pairs| = 10.
- Observed = mean of D[s_i, s_j] over the 10 pairs.
- Null: 10,000 random 5-element subsets of {1..114}; compute mean of 10 pairs from each.
- p_lower = (n_null_with_mean ≤ observed) / 10,000.

### H2: 4-cluster drop-Q1 sensitivity
- Cluster' = {Q 6, Q 18, Q 34, Q 35}; |cluster'| = 4; |pairs| = 6.
- Same null protocol, n_perm = 10,000 random 4-element subsets.

### H3: length-residualized
- For each of the 6,441 surah-pairs, regress D[i,j] linearly on |log(VC_i) - log(VC_j)| where VC = verse-count.
- Compute the residual for each cluster pair.
- Observed = mean of cluster residuals.
- Pass: observed < 0 (negative = closer than expected for length difference).

## 3. Test statistic

- H1: within-cluster mean FR (lower = cohesive).
- H2: drop-Q1 4-cluster mean FR (lower = cohesive).
- H3: length-residualized mean (negative = cohesive after length control).

## 4. Success / Failure criteria

| Cells passing | Verdict |
|:--|:--|
| 3/3 H1+H2+H3 | CONFIRMED |
| 2/3 | DIRECTIONAL |
| 1/3 | DIRECTIONAL-WEAK |
| 0/3 | NULL (cluster is NOT FR-cohesive at the group level) |

## 5. Honest limits known a priori

- Q 1 al-Fātiḥa is corpus-isolated by H-NEW-89 cluster-membership taxonomy (umm al-kitāb / sui generis). Including Q 1 in any cluster-cohesion test creates a known confound; H2 drops it as the explicit sensitivity check.
- The al-ḥamdu li-llāh phrase is a DOXOLOGICAL FORMULA, not a content-fingerprint. The cohesion hypothesis is OPTIMISTIC and should be tested honestly — null would be more theoretically satisfying than confirmation in the sense that confirmation would require explaining WHY a praise-formula creates content-similarity.
- The corpus all-pair mean FR is ~0.92; cluster means above this would indicate the cluster is in fact ANTI-cohesive (more spread than random matches). This would constitute a strong NULL (cluster does NOT function as a content-cluster).
- Garden-of-forking-paths disclosure: I observed (during empirical-anchor extraction) that the 5-cluster mean is 0.9902 (above corpus mean 0.9226) BEFORE locking this pre-reg. Per HANDOFF/04-DISCIPLINE.md, I am locking the directional test (cohesive) anyway and accepting that the empirical observation will likely be NULL. Single-test α=0.05 cap applies; verdict ceiling is **DESCRIPTIVE-EMPIRICAL** under transparent post-hoc disclosure.
- The cohesion-test direction is locked NOT because I expect a positive result, but because OQ-3 candidate's pre-existing hypothesis is "cluster is cohesive" and the discipline requires testing that hypothesis honestly.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token + QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`.

## 7. Bonferroni

k = 3 (H1, H2, H3). α_bon = 0.05/3 = 0.01667 per test.

## 8. SHA256 lock

Embedded in `scripts/Q034_F_01_hamd_cluster_fr_cohesion.py`; verified at runtime.

## 9. Independent replication path

If H1+H2+H3 pass (DIRECTIONAL or stronger), independent replication via:
- char-4-gram FR replication (using H-NEW-111b matrix, when available)
- verse-length-distribution replication (using H-NEW-111c)
- broader heaven-and-earth opener cluster (4 of 5: Q 6, 18 indirectly, 34, 35) as orthogonal definition
