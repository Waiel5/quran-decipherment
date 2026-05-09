---
surah: 75
test_id: Q075-F-04
title: Q 75 affinity to H-NEW-1200 short-Meccan-tail eschatology cluster — augmentation FR-cohesion test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q075-F-04-q75-h-new-1200
alpha_bon: 0.025
direction: Locked — Q 75 belongs to the H-NEW-1200 eschatology cluster; adding Q 75 STRENGTHENS or matches cluster cohesion at z<-5.0
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q075-F-04 — Pre-registration: Q 75 affinity to H-NEW-1200 cluster

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** Q 75's mean FR-distance to the H-NEW-1200 14-cluster {Q 56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104} is **below** Q 75's mean FR-distance to the rest of the corpus (i.e., Q 75 is content-attracted to the eschatology cluster).

**H1b (one-tailed, locked direction):** Adding Q 75 to the H-NEW-1200 cluster (forming a 15-surah extended cluster) **does not weaken** cohesion: the 15-surah z-score is at-or-better than the 14-surah baseline z-score. Pre-committed threshold: 15-cluster z ≤ −5.0 (matching baseline z≈-5.23).

**H0 (joint):** Either (i) Q 75 mean to cluster ≥ Q 75 mean to non-cluster, OR (ii) 15-cluster z > −5.0.

**Direction:** Q 75 BELONGS in the eschatology cluster (LOCKED).

## 2. Operational definition

### Source artifacts
- `findings/phase-b-hypotheses/csv/h-new-111.json`

### H-NEW-1200 cluster (locked from MASTER-FINDINGS-LEDGER §10.35)
{Q 56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104}

### Cell A — Q 75's positional affinity
- Compute Q 75's mean FR distance to each of the 14 cluster members → mean_Q75_to_cluster.
- Compute Q 75's mean FR distance to all NON-cluster surahs (excluding Q 75 itself, 99 surahs) → mean_Q75_to_others.
- Test: mean_Q75_to_cluster < mean_Q75_to_others (one-sided, paired comparison).
- Z-score: (mean_Q75_to_cluster - mean_Q75_to_others) / SE_paired.

### Cell B — 15-cluster cohesion vs 14-baseline
- Replicate H-NEW-1200 14-cluster baseline: pairwise FR mean over C(14,2)=91 pairs; permutation null over 10⁴ random 14-surah subsets.
- Add Q 75 to form 15-cluster: pairwise FR mean over C(15,2)=105 pairs; permutation null over 10⁴ random 15-surah subsets.
- Compare z-scores; pre-committed: 15-cluster z ≤ −5.0.

### Permutation null seed: 20260509, n_perm = 10000.

## 3. Success / Failure

- **CONFIRMED**: Both Cell A passes (one-sided p < α_bon = 0.025) AND Cell B passes (15-cluster z ≤ −5.0).
- **PASS-DIRECTED**: One cell passes; direction LOCKED matches.
- **NULL**: Direction matches but p > 0.5 in both cells.
- **PRE-COMMIT VIOLATION**: Direction reverses (Q 75 is FAR from cluster).

## 4. Honest limits

- This is essentially asking whether Q 75 belongs to a cluster it was not originally part of. The original H-NEW-1200 cluster was defined by (a) *idhā*-cosmic-event-openers (5 surahs) and (b) *wa-mā adrāka mā* (10 surahs) — Q 75 has NEITHER pattern at v.1, but its CONTENT is heavily eschatological (Q 75 = highest *qiyāmah*-density surah; see Q075-F-05). The test asks whether content-similarity drives FR-clustering even without surface-pattern membership.
- This is a **cluster-augmentation test**, not a cluster-discovery test. Pre-reg lock is on direction.
- N=15 is small; perm null bound ≈ 1/n_perm = 0.0001.

## 5. Rules-tuple

Default. (no-tashkeel, etc.)

## 6. Bonferroni

k = 2 (Cell A, Cell B). α_bon = 0.025.

## 7. Coordination

H-NEW-1200 is the parent finding (CONFIRMED p=0.00030). Q075-F-04 is an augmentation test to assess Q 75's position relative to that cluster.

## 8. SHA256 lock

Computed at write-time, embedded into `scripts/Q075_F_04_h_new_1200_affinity.py`, verified at runtime.
