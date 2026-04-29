---
id: H-NEW-201
title: PageRank on the verse-twin similarity network (downstream of H-NEW-167)
phase: B
status: PRE-REGISTERED
registered: 2026-04-17
seed: 20260419
parent: H-NEW-167 (verse-twin graph, top-1 char-trigram Jaccard)
rules_tuple: (no-tashkeel; whitespace-collapsed; basmala-only-in-Q1)
script: scripts/h_new_201_pagerank_verse_twin.py
data_out: findings/phase-b-hypotheses/csv/h-new-201.json
---

# [[h-new-201-pagerank-verse-twin|H-NEW-201]] — PageRank on the verse-twin similarity graph

## Motivation

[[h-new-167-verse-twin-graph|H-NEW-167]] characterised the **top-1** Jaccard twin graph as
near-forest — clusters-less, triangle-less, disconnected. That top-1
construction forbids hubs beyond the raw refrain count. A **top-k**
weighted directed variant recovers the full locally-dense similarity
structure, and PageRank gives each verse a mass proportional to the
aggregated trust-flow of verses that resemble it. The question: does
PageRank on a similarity graph re-discover classically celebrated
verses — the Fātiḥa, ʾāyat al-kursī, the Throne verse family —
or does it mechanically elevate refrains (as degree did)?

## Method (locked)

### Graph construction

* Text: `quran-text/quran-no-tashkeel.json` (Uthmani, tashkeel
  stripped, whitespace collapsed, basmala-only-in-Q1). Same rules
  tuple as [[h-new-167-verse-twin-graph|H-NEW-167]], same seed 20260419.
* Nodes: all 6,236 verses.
* Similarity: character-trigram **Jaccard** (interior spaces kept).
* Edge rule: for each verse v, find the **top-K = 5** nearest
  neighbours by Jaccard (self excluded). Emit **directed** edges
  v → v_k with weight w_{vk} = Jaccard(v, v_k). Self-loops excluded.
  Edges with w = 0 dropped.
* No symmetrisation. The graph is a weighted directed graph with
  out-degree ≤ 5 per node.

### PageRank

* Compute PageRank with damping α = 0.85, exactly **100 iterations**
  (no early-stop on convergence — report final vector at iter 100).
* Personalisation vector: uniform (1/N).
* Dangling node handling: pure-sink verses redistribute their mass
  uniformly (standard PageRank convention).
* Weights: normalise out-weights to 1 per source node before the
  matrix-vector step.

### Primary tests (Bonferroni k=2, α_family = 0.05, α_test = 0.025)

1. **T1 — Classical celebration of top-10 PageRank verses.**
   Take the 10 highest-PageRank verses. For each, check whether it
   is listed in the project's classical-celebration index
   (`findings/verse-commentaries-top100.md` — the top-100 most-
   commented verses in al-Ṭabarī/al-Rāzī/al-Qurṭubī/Ibn Kathīr).
   Count how many of the top-10 PageRank verses are in the
   classical-top-100. **PASS if ≥ 3 of the top-10 are in the
   classical-top-100** (one-sided binomial under null p = 100/6236
   ≈ 0.01603, Pr(X ≥ 3 | n=10, p=0.01603) ≈ 4.3e-4 < 0.025). If
   the celebration index cannot be loaded unambiguously, the test
   is downgraded to DESCRIPTIVE and reported as such.
2. **T2 — al-Fātiḥa PageRank sum exceeds random 7-verse bundle.**
   Let S_F = sum of PageRank of the 7 Fātiḥa verses (Q 1:1..1:7).
   Sample **10,000** random 7-verse bundles from the 6,236 verses
   without replacement (seed 20260419). **PASS if S_F exceeds the
   97.5-percentile of the null bundle sums (one-sided p < 0.025).**

### Secondary / descriptive (not multiplicity-corrected)

* Full top-20 PageRank list with Arabic preview.
* Q 1's aggregate PageRank rank (rank of S_F among all 6,236-choose-7
  bundles, approximated via the null mean/std).
* Top-10 hubs' overlap with [[h-new-167-verse-twin-graph|H-NEW-167]] top-10 degree hubs (sanity).
* Convergence trace: L1 change at iterations 10, 50, 100.

## Stopping rules

Single seeded run. No re-seeding. No post-hoc k-tuning (K = 5 is
fixed by this pre-reg). Report PageRank to 6 decimal places.

## Garden-of-forking-paths log (written BEFORE run)

* **K = 5 chosen** because: (a) [[h-new-167-verse-twin-graph|H-NEW-167]] used K = 1 and found a
  near-forest; the natural next tier is the smallest K that admits
  cycles and triangles while keeping the graph sparse. (b) Common
  default for kNN semantic graphs in the NLP literature. (c) Powers
  of 2 (K = 4, 8) were considered but 5 matches the 5-grams used in
  [[h-new-66-verse-twins-network|H-NEW-66]] parent tradition. No further tuning.
* **Damping α = 0.85** is the field-standard PageRank value (Brin &
  Page 1998). No other value tested.
* **100 iterations** is the task's locked parameter. Typical PageRank
  converges to 1e-6 in ~50 iterations on graphs this size; 100 is
  overkill and guarantees convergence.
* **Directed edges with weight = Jaccard** (not binary) because
  the task specifies "edge weight = similarity".
* **Classical-top-100** as the celebration reference chosen because
  it is the project's pre-existing, cross-tafsir-aggregated ranking
  (already on disk). Alternatives (al-Suyūṭī's ʾItqān list, Ibn
  ʿArabī's mystical-favorites, Sufi recitation-circuit lists) were
  considered but rejected as harder to enumerate deterministically.
  If verse-commentaries-top100.md is absent or malformed, the test
  downgrades to DESCRIPTIVE.
* **Bonferroni k=2** because exactly two primary tests are locked.
  α_test = 0.025.
* **10,000 bundle resamples** gives Monte-Carlo SE ≤ 0.005 at p = 0.025,
  well within tolerance.

— end pre-reg —
