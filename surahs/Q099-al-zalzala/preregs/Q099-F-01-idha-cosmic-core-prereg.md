---
surah: 99
test_id: Q099-F-01
title: Q 99 within H-NEW-1200 14-cluster + 4-CORE idhā-cosmic-opener architectural replication
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q099-F-01-idha-cosmic-core
alpha_bon: 0.025
---

# Q099-F-01 — Pre-registration: Q 99 within H-NEW-1200 14-cluster + 4-CORE idhā-cosmic-opener replication

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** Q 99's mean Fisher-Rao distance to the OTHER 13 H-NEW-1200 cluster members (Q {56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 101, 104}) is LOWER than Q 99's corpus-mean distance.

**H1b (one-tailed, locked direction):** Q 99's mean FR distance to the 3 OTHER architectural-CORE Sub-cluster A members ({Q 81, Q 82, Q 84}) is LOWER than Q 99's mean to the 14-cluster, AND lower than 0.60 (the H-NEW-1200 ledger's pre-stated 0.52-0.57 architectural-core band, with mild slack-tolerance).

**H0 (joint):** Q 99 is not preferentially close to either the 14-cluster or the 4-CORE.

**Direction:** locked POSITIVE Q 99 ∈ cluster-CORE.

## 2. Operational definition

- **Source data**: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.
- **14-cluster members**: Q {56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104} per H-NEW-1200 ledger.
- **4-CORE members**: Q {81, 82, 84, 99} per H-NEW-1200 ledger §10.35.
- **Q 99 corpus-mean distance**: computed from D_matrix as mean over all 113 other surahs.
- **Q 99 cluster-mean distance**: mean over 13 other 14-cluster members.
- **Q 99 4-CORE-mean distance**: mean over 3 other 4-CORE members ({Q 81, Q 82, Q 84}).

## 3. Test statistic

- **T1 (cluster cohesion)**: ratio = cluster_mean / corpus_mean. Direction LOCKED positive (T1 < 1.0 = cohesive).
- **T2 (4-CORE cohesion)**: 4_CORE_mean. Direction LOCKED positive (T2 < 0.60 = matches architectural-core band).

## 4. Permutation null

For T1: random 13-surah subsets of the 113-non-Q99 corpus (10,000 iterations); compute Q 99 mean distance to each subset; p-value = fraction of permuted-subsets with mean ≤ observed cluster-mean.

For T2: random 3-surah subsets of the 113-non-Q99 corpus (10,000 iterations); compute Q 99 mean distance to each subset; p-value = fraction with mean ≤ observed 4-CORE-mean.

n_perm = 10000, seed = 20260509.

## 5. Success / Failure

- **CONFIRMED**: T1 AND T2 both pass at p ≤ α_bon = 0.025.
- **DIRECTIONAL**: 1 of 2 passes.
- **NULL**: 0 of 2 passes.

## 6. Honest limits known a priori

- This test is a REPLICATION of H-NEW-1200 (the 14-cluster cohesion) with Q 99 specifically anchored. The H-NEW-1200 ledger result (p=0.00030 cluster-cohesion) was at the WHOLE-CLUSTER level; this test asks whether Q 99 INDIVIDUALLY shows above-average affinity to the cluster.
- Post-hoc origin acknowledged: the H-NEW-1200 ledger's pre-existing identification of {Q 81, 82, 84, 99} as the architectural-CORE was the basis for the brief's "4 idhā-cosmic-opener pairs at FR ~0.52-0.57" anchor. This test FORMALIZES that observation with a permutation null. The test is INDEPENDENT REPLICATION (Q 99 anchored vs. cluster-aggregate).
- The 14-cluster vs corpus comparison is structurally close to the H-NEW-1200 primary test; mild p-value reduction from independence-deflation expected. Single-test α=0.05 cap available as fallback per HANDOFF/04-DISCIPLINE.md "post-hoc protocol."

## 7. Rules-tuple

`(no-tashkeel, root-Fisher-Rao-content-distance, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (T1 + T2). α_bon = 0.025.

## 9. Coordination

This is a Q 99-specific cluster-membership test. Q 81, Q 82, Q 84 specialists (when developed) will run analogous tests. No duplication.

## 10. SHA256 lock

Computed at write-time, embedded in `scripts/Q099_F_01_idha_cosmic_core.py`, verified at runtime.
