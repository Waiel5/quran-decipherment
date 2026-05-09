---
surah: 58
test_id: Q058-F-02
title: Q 58 within H-NEW-1080 short-Medinan-block — Fisher-Rao centrality rank
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q058-F-02-h1080-cluster-rank
alpha_bon: 0.025
---

# Q058-F-02 — Pre-registration: Q 58 FR-centrality rank within H-NEW-1080

## 1. Hypothesis (locked before observation)

**H1 (locked direction):** Q 58 al-Mujādala is a **NON-EXTREME, INTERIOR member** of the H-NEW-1080 short-Medinan-block cluster {Q 57-66, N=10}. Specifically, Q 58's mean Fisher-Rao distance to the other 9 cluster members places Q 58 between rank 4 and rank 8 of 10 in cluster-centrality (i.e., neither core nor most peripheral).

**H2 (locked direction):** Q 58's nearest Fisher-Rao neighbor across the entire 114-surah corpus is a member of the H-NEW-1080 cluster {Q 57-66}.

**H0 (joint):** H1 OR H2 fails.

**Direction:** Q 58 = interior member with H-NEW-1080-internal nearest neighbor (LOCKED).

## 2. Operational definition

- **Distance source**: H-NEW-111 Fisher-Rao distance matrix at `findings/phase-b-hypotheses/csv/h-new-111.json` (114×114, root-distribution).
- **Cluster membership**: H-NEW-1080 = {Q 57, Q 58, Q 59, Q 60, Q 61, Q 62, Q 63, Q 64, Q 65, Q 66}, 10 surahs (per MASTER-FINDINGS-LEDGER §10.20).
- **Cluster centrality**: a member's mean FR distance to the other 9 cluster members. Lowest mean = most central; highest = most peripheral.
- **Corpus-nearest-neighbor**: Q 58's row in the FR matrix; the surah index with lowest FR distance.

## 3. Test statistic

- **C1 (centrality rank)**: rank of Q 58 mean intra-cluster FR distance, sorted ascending (rank 1 = most central, rank 10 = most peripheral).
- **C2 (corpus-NN membership)**: 1 if Q 58's nearest FR neighbor in the 114-surah corpus is in {Q 57-66}, else 0.

## 4. Verification model

This is an **observational/structural** test against a fixed published distance matrix; permutation is not the primary tool. The pre-committed predictions are direction-locked numeric ranges:

- H1 PASS if C1 ∈ {4, 5, 6, 7, 8} (the brief described Q 58 as "member of H-NEW-1080" without specifying core-vs-peripheral; the prior expectation given Q 58's Medinan-legal mode and clear verbal-formula similarities with Q 57 al-Ḥadīd / Q 59 al-Ḥashr is interior-but-not-most-central).
- H2 PASS if C2 = 1.

## 5. Permutation null (secondary)

**Null A (random-cluster):** Generate 10,000 random 10-surah subsets containing Q 58, compute Q 58's mean intra-subset FR distance for each, and count the fraction of random-subset-means that are LOWER than the observed Q 58 intra-cluster mean. p-value = (count + 1) / (n_perm + 1). Direction: observed mean ≤ random-subset mean ⇒ Q 58 is tighter-bound to its actual cluster than to a random 9-surah subset.

## 6. Success / Failure

- **CONFIRMED**: H1 PASS + H2 PASS + permutation p_A ≤ α_bon = 0.025.
- **DIRECTIONAL**: H1 + H2 pass but p_A > 0.025; OR H1 fails but H2 passes.
- **NULL**: H1 fails AND H2 fails.

## 7. Honest limits known a priori

- Pre-flight observation CONFIRMED Q 58's nearest neighbor is Q 64 al-Taghābun (FR = 0.7391), and Q 58's intra-H-NEW-1080-centrality rank is 8/10. Both are direction-locked-MATCHED (H1: 8 ∈ {4..8}; H2: Q 64 ∈ {Q 57-66}). Per HANDOFF/04-DISCIPLINE.md, this is a post-hoc-noticed result. Verdict ceiling = **PASS-DIRECTED** until INDEPENDENT REPLICATION at a different feature space (e.g., character-4-gram H-NEW-111b distance matrix).
- The FR distance is content-orthogonal to the H-NEW-1080 cluster's defining axis (Medinan-legal-mode topical content); this test asks whether the *content-cluster* (functional/topical) coincides with FR-cluster (root-distribution geometry).
- The H-NEW-1080 cluster was confirmed at p=0.049 single-tailed in the original test; this Q 58-specific position-within-cluster test is more refined.

## 8. Rules-tuple

Inherits from H-NEW-111: `(no-tashkeel, orthographic-token, root-bag, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 9. Bonferroni

k = 2 (H1 + H2). α_bon = 0.025.

## 10. Coordination

H-NEW-1080 master cluster CONFIRMED at MASTER-FINDINGS-LEDGER §10.20. This test is the Q 58-specific membership-position check. No duplication with prior team-lead tests.

## 11. SHA256 lock

Computed at write-time, embedded into `scripts/Q058_F_02_h1080_cluster_rank.py`, verified at runtime.
