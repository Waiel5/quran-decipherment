---
id: H-NEW-206
title: Semi-supervised surah taxonomy via multi-feature clustering
phase: B
status: PRE-REGISTERED
date: 2026-04-17
seed: 20260419
bonferroni_k: 2
direction: two-sided (selection of best k)
---

# [[h-new-206-semi-supervised-taxonomy|H-NEW-206]] — Semi-supervised surah taxonomy

## Purpose

Given the 50+ surah-level features uncovered over Phase B, do the 114 surahs form
a small number of structurally distinct **classes** beyond the binary
Meccan/Medinan or ternary Early-Meccan / Middle-Meccan / Late-Meccan / Medinan
(Nöldeke) labels? If yes, do those classes align with **classical balāgha
taxonomies** (ṭiwāl / mi'ūn / mathānī / mufaṣṣal; musabbiḥāt; ḥawāmīm; al-R
cluster; etc.)?

## Feature set (per-surah, 114 × p)

1. Zipf α (from [[h-new-187-lempel-ziv|h-new-187]]-per-surah.csv)
2. Heap β (from [[h-new-187-lempel-ziv|h-new-187]]-per-surah.csv)
3. Lexical dispersion ([[h-new-168-q16-q25-dispersion|H-NEW-168]] variant, from [[h-new-187-lempel-ziv|h-new-187]]-per-surah.csv)
4. PC1, PC2, PC3 of Hellinger-sqrt word-distribution matrix (re-computed fresh,
   H-NEW-176 methodology, top-500 words)
5. [[h-new-125-chronology-content|H-NEW-125]] axis subset (computed per-surah): mean_verse_length, allah_density,
   qul_density, prophet_density, eschatological_density, book_reference_density,
   divine_name_density, legal_term_density, loanword_proxy_density
6. Per-surah multifractal width Δα ([[h-new-166-multi-scale-hurst|H-NEW-166]]-style MF-DFA on verse-length
   sequence within the surah; computed only for surahs with n_verses ≥ 30 —
   smaller surahs get width=NaN, imputed to the grand median)
7. LZ complexity normalized ([[h-new-187-lempel-ziv|h-new-187]] lz_norm_log)
8. First-root inclusio flag ([[h-new-156-first-root-inclusio|h-new-156]] per_surah_results)
9. Surah length (n_verses)
10. muq_cardinality (0 for non-muq; letter-count for 29 muq surahs)
11. Nöldeke rank (from zipf-per-surah.csv noldeke_order)

All features are z-scored. Missing values (e.g., Zipf α for tiny surahs) are
median-imputed on the surah column.

## Clustering algorithms

- k-means: k ∈ {3, 4, 5, 6, 7, 8, 10} with n_init=50, seed=20260419
- HDBSCAN: min_cluster_size ∈ {3, 5, 7}, other params at defaults

## Model selection

Primary metric: silhouette score (sklearn.metrics.silhouette_score, Euclidean).
- For k-means: report silhouette and Calinski-Harabasz per k.
- For HDBSCAN: report n_clusters_found and silhouette of the non-noise points.

**Best-k**: highest silhouette over k-means runs.

## Multiple-testing

Pre-registered Bonferroni k=2. Interpretation: the two principal inferences
- (a) "≥1 clustering has silhouette > 0.2 at the best k"
- (b) "cluster labels correlate with muqaṭṭāʿat membership beyond chance
  (χ²)"
each get α=0.025 instead of 0.05.

The specific k-choice and the cluster-name interpretation are DESCRIPTIVE, not
inferential — they carry standard apophenia-risk cautions.

## Hub surah report

For each of the [[cross-finding-009-meta-cluster-network|cross-finding-009]] hub surahs — Q 2, Q 3, Q 59, Q 62 (front-back
hub pair) and Q 18, Q 36, Q 50, Q 68 (secondary hubs) — report cluster
membership.

## Classical balāgha taxonomy target names

Non-exhaustive checklist to compare against cluster centroids:

- **al-Sabʿ al-ṭiwāl** (the seven long): Q 2, 3, 4, 5, 6, 7, 9 (+ Yūnus by some)
- **al-Mi'ūn** (100-verse tier): Q 10-17 roughly
- **al-Mathānī** (doublers, post-Mi'ūn): Q 18-49
- **al-Mufaṣṣal** (frequent-breaks): Q 49-114, subdivided ṭiwāl/awsāṭ/qiṣār
- **al-Ḥawāmīm** (ḥā-mīm openers): Q 40-46
- **al-Musabbiḥāt** (tasbīḥ openers): Q 17, 57, 59, 61, 62, 64, 87
- **al-ʿItāq al-awwal** (earliest Meccan): late-30s surahs

## Output files

- `/findings/phase-b-hypotheses/h-new-206-work/feature_matrix.csv`
- `/findings/phase-b-hypotheses/h-new-206-work/cluster_assignments.csv`
- `/findings/phase-b-hypotheses/h-new-206-work/cluster_centers.csv`
- `/findings/phase-b-hypotheses/h-new-206-work/silhouette_scores.json`
- `/findings/phase-b-hypotheses/h-new-206-work/hub_cluster_report.json`
- `/findings/phase-b-hypotheses/csv/h-new-206.json`
- `/findings/phase-b-hypotheses/h-new-206-semi-supervised-taxonomy.md`
- `/journal/h-new-206-run-1.md`

## Seed

20260419 (locked).
