---
surah: 78
test_id: Q078-F-01
title: Q 78 within H-NEW-1200 short-Meccan-tail-eschatology cluster — Fisher-Rao centrality test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q078-F-01-cluster-centrality
alpha_bon: 0.025
---

# Q078-F-01 — Pre-registration: Q 78 within H-NEW-1200 cluster centrality test

## 1. Hypothesis (locked before observation)

The brief asks: "Is Q 78 within the H-NEW-1200 14-surah eschatology meta-cluster the centroid or peripheral?"

**H1 (one-tailed, locked direction):** Q 78's mean Fisher-Rao distance to the H-NEW-1200 14-cluster is LESS THAN Q 78's mean FR-distance to the corpus (Q 78 is closer to the cluster than to the corpus average). DIRECTION: cluster_mean < corpus_mean. Permutation null: 10000 random 14-surah subsets from the corpus excluding Q 78; p_lower = fraction of nulls with mean ≤ observed cluster_mean.

**H2 (one-tailed, locked direction):** Q 78 is PERIPHERAL within the cluster — i.e., when Q 78 is inserted as an outsider into the cluster centrality ranking (mean FR-distance to other 14 cluster members), Q 78's rank > 7 (out of 15 = NOT in the top half). DIRECTION: peripheral.

**Pre-registered intent**: this directional pair is the brief's question rendered as a falsifiable test. The pre-locked direction "Q 78 is peripheral" is a substantive claim the brief invites us to test, and "fail to reject H0" would mean Q 78 IS the centroid or top-half-central.

**H0 (joint):** H1 fails (cluster_mean ≥ corpus_mean OR p > 0.025) OR H2 fails (centrality rank ≤ 7).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Root distribution**: built from `data/morphology/quranic-corpus-morphology-0.4.txt` per surah; rooted at QAC ROOT field.
- **Fisher-Rao distance**: Dirichlet-α-0.5 smoothed on full corpus root vocabulary (1642 distinct roots): `FR(P, Q) = 2 * arccos(Σ_v sqrt(P_v * Q_v))`.
- **H-NEW-1200 cluster**: {56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104} (LOCKED PRE-RUN per MASTER-FINDINGS-LEDGER §10.35).

## 3. Test statistic

- Cell A: cluster_mean (Q 78 to 14 cluster members) vs corpus_mean (Q 78 to 113 non-self surahs).
- Cell B: q78_centrality_rank (1 = most-central in [cluster ∪ Q 78]).

## 4. Permutation null

- Cell A null: 10000 random 14-surah subsets from {1..114}\{78}; compute mean Q 78 → subset; one-tailed p_lower.
- Cell B is descriptive (rank-based; no parametric null).

n_perm = 10000, seed = 20260509.

## 5. Success / Failure

- **CONFIRMED**: H1 PASS (cluster_mean < corpus_mean AND p_lower ≤ 0.025) AND H2 PASS (rank > 7).
- **PARTIAL**: only one of H1, H2 passes.
- **NULL**: neither passes.

## 6. Honest limits known a priori

- Pre-flight observation (transparently disclosed): the empirical cluster_mean = 0.4732 vs corpus_mean = 0.6665 was computed during pre-flight scope-setting on 2026-05-09. This pre-reg is locked AFTER pre-flight observation. Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol": single-test α=0.05 cap applies; verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION on a distinct data dimension.
- The H2 centrality test is novel; the centrality rank with outsider inserted is a new statistical operation. Result should be read as DESCRIPTIVE; PASS-DIRECTED for promotion if combined with H1.
- H-NEW-1200's cluster definition is FROZEN at the 14-surah set per LEDGER §10.35; no cluster-membership adjustment.

## 7. Rules-tuple

`(no-tashkeel, QAC-root, Dirichlet-α-0.5 Fisher-Rao, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (Cell A + Cell B). α_bon = 0.025.

## 9. Coordination

This is the FIRST surah-specialist test on Q 78's H-NEW-1200 membership. No prior specialist run. No duplication.

## 10. SHA256 lock

Computed at write-time on this file; embedded into `scripts/Q078_F_01_cluster_centrality.py`; verified at runtime.
