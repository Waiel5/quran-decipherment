---
id: H-NEW-89
title: Meta-Cluster Network Synthesis — graph projection across 8+ surah cluster systems
phase: B
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (BEFORE running graph computation)
agent: h-new-89-specialist
parent_findings:
  - H-NEW-58c (musabbiḥāt cluster, p=0.0001)
  - H-NEW-67 (al-sabʿ al-ṭiwāl, p=0.0001 length axis)
  - H-NEW-68 (Friday cluster, pre-registered)
  - H-NEW-63 (Khawātim al-Ḥashr extended, OBSERVED-FACT)
  - H-NEW-53/56/57 (muqaṭṭāʿat as book-introduction markers, p≤10⁻¹²)
  - cross-finding-008 (muqaṭṭāʿat synthesis)
  - H-NEW-58b (auto-discovered cluster taxonomy)
bonferroni_family: 2026-04-15-Wave-Meta-Cluster-Network
bonferroni_k: 4 (4 graph-metric cells)
alpha_bon: 0.0125 (= 0.05 / 4)
seed: 20260416
n_perm: 10000
rules_tuple: (no-tashkeel; whitespace-tokenized; cluster-membership taken from existing locked finding files)
---

# [[h-new-89-meta-cluster-network|H-NEW-89]] — Meta-Cluster Network Synthesis (Pre-registration)

## Question

Across 8+ classically-attested surah cluster systems already locked in
the project's findings, build a bipartite (surah × cluster) incidence
matrix and project to a unipartite surah-graph. Then ask:

1. Which surahs are in the MOST clusters (structural hubs)?
2. Which surahs are in NO clusters (structural isolates)?
3. Is the observed degree distribution (clusters-per-surah) more skewed
   than a random null with matching cluster sizes?
4. Are hub surahs concentrated in any specific Quran zone (front,
   middle, back)?

## Locked cluster-system list (8 systems, fixed before computation)

The following 8 cluster systems are LOCKED from existing findings.
All membership lists are taken verbatim from the cited files. NO
post-hoc additions or removals are permitted.

### C1 — Muqaṭṭāʿat الم cluster (n=6)
Surahs: {2, 3, 29, 30, 31, 32}
Source: [[h-new-56-five-exceptions|H-NEW-56]] MUQATTAAT_SURAHS list (locked); cross-finding-008.

### C2 — Muqaṭṭāʿat الر cluster (n=5)
Surahs: {10, 11, 12, 14, 15}
Source: [[h-new-58b-shared-prefix-pairs|H-NEW-58b]] top-15 + [[h-new-56-five-exceptions|H-NEW-56]] list (al-Suyūṭī Itqān). Note:
Q 13 (المر) is included in the broader الر-family by classical
convention but uses al-mr not just الر. Per pre-reg discipline of
the LOCKED cluster, we include only pure الر openers.

### C3 — Muqaṭṭāʿat ḥm cluster (n=7)
Surahs: {40, 41, 42, 43, 44, 45, 46}
Source: [[h-new-58b-shared-prefix-pairs|H-NEW-58b]] top-15 + [[h-new-56-five-exceptions|H-NEW-56]] list. The 7 ḥawāmīm.

### C4 — Muqaṭṭāʿat طسم cluster (n=3)
Surahs: {26, 27, 28}
Source: [[h-new-58b-shared-prefix-pairs|H-NEW-58b]] top-15 + [[h-new-56-five-exceptions|H-NEW-56]] list. The 3 طسم/طس family
(Q 27 is طس only but classically grouped).

### C5 — Musabbiḥāt cluster (n=5)
Surahs: {57, 59, 61, 62, 64}
Source: [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] (PASS at p=0.0001). The 5-surah inner cluster.

### C6 — al-sabʿ al-ṭiwāl cluster (n=7)
Surahs: {2, 3, 4, 5, 6, 7, 9}
Source: [[h-new-67-sab-tiwal-mathani|H-NEW-67]] (PASS p=0.0001 on length). Q 9 reading chosen
(Q 9 = al-Tawba; Q 10 = al-Yūnus is the alternative, both pass).
PRE-REGISTRATION CHOICE: use Q 2-9 reading (al-Suyūṭī's primary
reading per Itqān). Logged in garden-of-forking-paths.

### C7 — Friday-liturgy cluster (n=4)
Surahs: {18, 32, 62, 76}
Source: [[h-new-68-friday-cluster|H-NEW-68]] pre-registration (locked classical liturgical set).

### C8 — Khawātim al-Ḥashr extended (n=2 surahs)
Surahs: {59, 62}
Source: [[h-new-63-khawatim-echo-extended|H-NEW-63]] (OBSERVED-FACT: Q 59:22-24 + Q 62:1 share 3 Khawātim
divine names). Cluster operationalized at SURAH level — only the 2
surahs containing Khawātim divine names co-occur in a single verse.

### C9 — al-Muʿawwidhatān (n=2)
Surahs: {113, 114}
Source: classical paired-prayer; [[h-new-58-surah-pair-twinning|H-NEW-58]] MW-5 referent; [[h-new-58b-shared-prefix-pairs|H-NEW-58b]]
PASS at Bonferroni-4 on shared char-prefix.

### C10 — al-Zahrāwān (n=2)
Surahs: {2, 3}
Source: classical pairing; [[h-new-58-surah-pair-twinning|H-NEW-58]] PASS at any-pair null on
root-jaccard p=0.0006.

### C11 — al-mufaṣṣal classical division (n=66)
Surahs: {49, 50, 51, ..., 114}
Source: al-Suyūṭī Itqān. The largest classical cluster.
LOCKED at Q 49-114 per the project's [[h-new-45-2-dead-zone|H-NEW-45.2]] dead-zone test.

Total: 11 cluster systems. (The task specifies "8+" — locking 11
gives full coverage of classically attested clusters in the project's
existing findings. Each cluster's source is a LOCKED finding-file
reference.)

## Locked metrics (pre-registered before graph projection)

### M1 — Per-surah cluster-degree
For each surah s ∈ {1, ..., 114}, count the number of clusters
containing s. Range: 0 to 11. Hub = top-decile (top 11 surahs by
degree). Isolate = degree 0.

### M2 — Degree-distribution skewness (one-sided test)
Compute the empirical distribution of {degree(s) : s ∈ 1..114}.
Compare its variance to a null where cluster MEMBERSHIPS are randomly
permuted (each cluster keeps its cardinality but the SURAH IDs are
re-drawn uniformly from {1..114}). Under the null, expected variance
≈ Σ |C_i| (1 - |C_i|/114) / 114. Observed variance / null mean
variance gives a concentration ratio. p = empirical fraction of
N=10K null draws with variance ≥ observed.

### M3 — Hub-zone concentration (one-sided test)
Compute the mean mushaf position (1..114) of the top-K hubs (K=11,
top-decile by degree). Compare against the null mean from N=10K
random K-surah samples. Two-sided test: hubs are unusually
front-clustered OR back-clustered.

### M4 — Isolate count (one-sided)
Count |{s : degree(s) = 0}|. Compare to expected count under
membership-permuted null. Test direction: observed count is unusually
HIGH (more isolates than random) or LOW.

## Bonferroni declaration
Family k=4 (M2, M3, M4, plus M1 hub identification as descriptive).
α_bon = 0.05/4 = 0.0125. M1 produces a ranked list (descriptive); 
M2/M3/M4 are inferential cells.

PASS criterion: ≥ 2 of 3 inferential cells significant at α_bon.

## Null distribution
Membership-permuted null:
- For each cluster C_i with cardinality |C_i|, draw a random 
  |C_i|-subset of {1..114} (without replacement within cluster).
- Compute new incidence matrix and recompute all metrics.
- Repeat 10,000 times with seed 20260416.
- Empirical p = (1 + |{null ≥ observed}|) / (1 + N).

## Garden-of-forking-paths (locked before run)

Choices fixed BEFORE seeing graph numbers:

1. **11 clusters** (not 8 minimum): include Khawātim, Muʿawwidhatān,
   Zahrāwān, mufaṣṣal as classical small/large clusters. Already-
   tested clusters from the project's findings receive priority.
2. **Top-decile hubs** (K=11): not top-5 or top-K-by-degree-≥-N.
   Top-decile is a standard order-statistic quantile.
3. **Membership-permuted null**, NOT degree-preserving rewiring:
   simpler and matches the [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] / [[h-new-67-sab-tiwal-mathani|H-NEW-67]] cluster-cohesion
   framework. Cluster cardinalities preserved; surah IDs re-drawn.
4. **Q 9 reading for al-sabʿ al-ṭiwāl** (not Q 10): al-Suyūṭī's
   primary classical reading. Q 10 alternative would change C6
   membership; we lock the primary reading and disclose.
5. **Pure الر** for C2 (Q 13 المر excluded): conservative cluster
   definition. If Q 13 were included, only Q 13's degree would
   change.
6. **mufaṣṣal at Q 49-114** (not Q 49-114 or Q 50-114 alternatives):
   matches [[h-new-45-2-dead-zone|H-NEW-45.2]] dead-zone test definition.
7. **Variance** as M2 metric (not Gini, not entropy): variance is
   the canonical concentration metric and matches the 
   membership-permuted null exactly.

## Anti-HARK pre-commitments

- All 4 metrics (M1 ranking + M2/M3/M4 inferential) reported regardless
  of significance.
- Top-11 hubs and all isolates reported with full degree list.
- If 0 cells significant: NULL. If 1 cell: MARGINAL. If 2+: PASS.
- Honest framing: cluster-membership is largely DETERMINISTIC from
  classical tradition — this test asks whether the JOINT structure
  of cluster systems is more concentrated than random, NOT whether
  the individual clusters are real (they are, by construction).

## Cross-finding implications (anticipated)

If PASS on any cell, this will be the project's first explicit
META-cluster synthesis — i.e., demonstrating that the Quran's
recognized cluster systems (muqaṭṭāʿat, musabbiḥāt, ṭiwāl, etc.)
are not orthogonal to each other but converge on specific HUB
surahs. Candidate [[cross-finding-009-meta-cluster-network|cross-finding-009]].

Q 62 al-Jumuʿah is a strong PRIOR hub candidate (musabbiḥāt + Friday
+ Khawātim-extended + mufaṣṣal = 4 clusters minimum).

Q 2 al-Baqara is another PRIOR hub candidate (الم + ṭiwāl + Zahrāwān
= 3 clusters).

These PRIORS are noted but do not constitute post-hoc bias since
they are explicitly disclosed BEFORE the run.

## Data + outputs

- Input: hard-coded cluster membership lists (above)
- Script: `scripts/h_new_89_meta_cluster_network.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-89.json`
- Findings: `findings/phase-b-hypotheses/h-new-89-meta-cluster-network.md`
- Cross-finding (if warranted): `findings/cross-finding/cross-finding-009-meta-cluster-network.md`

## Status
PRE-REGISTERED 2026-04-15 BEFORE script execution.
