---
id: H-NEW-167
title: Graph-theoretic properties of the verse-twin network (downstream of H-NEW-66)
phase: B
status: PRE-REGISTERED
registered: 2026-04-17
seed: 20260419
parent: H-NEW-66 (verse-twin network, top-1 char-5-gram intersection)
rules_tuple: (no-tashkeel; whitespace-collapsed; basmala-only-in-Q1; recitation-marks stripped)
script: scripts/h_new_167_verse_twin_graph.py
data_out: findings/phase-b-hypotheses/csv/h-new-167.json
---

# [[h-new-167-verse-twin-graph|H-NEW-167]] — Graph-theoretic properties of the verse-twin network

## Motivation

[[h-new-66-verse-twins-network|H-NEW-66]] established an undirected verse-twin network on eligible
verses (min 5 words) with a 3.76× intra-surah enrichment. That paper
reported descriptive stats (max degree, largest component size,
mutual-edge count) but did **not** characterise the graph as a
graph — is it small-world? scale-free? assortative? The present
hypothesis tests those structural claims and compares to an
Erdős–Rényi null with matched node/edge count.

## Method (locked)

### Graph construction

* Text: `quran-text/quran-no-tashkeel.json` (Uthmani, tashkeel
  stripped, whitespace collapsed).
* Nodes: all 6,236 verses (no minimum-length filter; a verse with
  fewer than 3 characters is collapsed to itself as a singleton
  node but its twin-edge is still computed on the available trigrams).
* Similarity: character-trigram **Jaccard** over the set of
  length-3 character windows (windows **include** interior spaces;
  basmala of Q1 only included once as a verse token per project
  convention; text already whitespace-collapsed).
* Edge rule: for each verse v, find the **top-1** argmax Jaccard
  twin v' ≠ v across the whole corpus (self excluded). No
  adjacency exclusion. Ties broken by lower (surah, ayah) index.
* The directed "top-1" map is **symmetrised** into an undirected
  simple graph: edge {v, v'} exists iff v'∈top1(v) **or** v∈top1(v').
  Degree = undirected degree.

### Primary tests (Bonferroni-3, α_family = 0.05, α_test = 0.0167)

1. **Scale-free (power-law fit).** Fit p(k) ∝ k^(-γ) via MLE on
   the undirected degree distribution with k ≥ k_min (Clauset-
   Shalizi-Newman method, k_min selected by KS-minimisation).
   PASS if the Kolmogorov–Smirnov goodness-of-fit p-value
   (via 500 bootstrap replicates from the fitted power-law)
   exceeds 0.0167 (i.e., power-law is **not rejected**) AND γ ∈ (1.5, 4).
2. **Clustering > ER.** Average clustering coefficient C_obs vs.
   500 Erdős-Rényi graphs G(n=6236, m=|E|) sampled with seed
   20260419. PASS if C_obs exceeds the 98.33 percentile of the
   ER null (one-sided, α = 0.0167).
3. **Small-world (Watts-Strogatz σ).** σ = (C_obs/C_ER_mean) /
   (L_obs/L_ER_mean), where L is the mean shortest-path length
   on the largest connected component (for fair comparison, both
   graphs are restricted to their largest components before L is
   computed). PASS if σ ≥ 2.

### Secondary (descriptive, not multiplicity-corrected)

* Component-size histogram; largest connected component; number of
  isolates.
* Degree assortativity (Newman 2002 r-coefficient).
* Top-10 hubs by undirected degree.

## Stopping rules

Single seeded run. No re-seeding on failure. No k_min grid-search
beyond the CSN procedure. Report γ, KS-p, C_obs, C_ER, L_obs,
L_ER, σ verbatim.

## Mechanical-witness MW-5

Generate a synthetic planted-community graph (5 blocks of ≈1000
nodes each, high intra-block edge density, low inter-block), match
its edge count, run the same three tests. Such a graph is
well-known to exhibit (a) heavy-tailed degree via hub-per-block
spuriously looks power-law-ish but typically fails the CSN KS
test; however the clustering and small-world tests should clearly
PASS. The MW is considered passed if clustering-and-small-world
both PASS; the power-law arm is informational.

## Garden-of-forking-paths log (written before run)

* Chose Jaccard over multiset-intersection because the task
  explicitly asked "fast char-trigram Jaccard". Jaccard is also
  length-normalised, so short verses do not become structural
  isolates.
* Chose symmetrisation via OR (rather than mutual-only AND) because
  the task says "undirected" and typical verse-twin networks in
  the NLP literature symmetrise the kNN graph with OR.
* Chose k_min = CSN procedure rather than fixed k_min = 2 because
  CSN is the field standard.
* Bonferroni-3 chosen over tighter thresholds because exactly
  three primary tests are locked. Any additional descriptive
  statistics are reported without claim.

— end pre-reg —
