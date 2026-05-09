---
surah: 39
test_id: Q039-F-01
title: Q 39 — Tanzīl-cluster (H-NEW-1100) Late-Meccan Nöldeke-peak co-localization
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q039-novel-tests
alpha_bon: 0.0125
direction: tanzil_cluster_late_meccan_concentrated
---

# Q039-F-01 — Pre-registration: Tanzīl-opener cluster Late-Meccan Nöldeke-peak co-localization

## 1. Hypothesis (locked before observation)

The H-NEW-1100 *tanzīl al-kitāb min Allāh* opener-formula 6-surah cluster {Q 32, 39, 40, 41, 45, 46} is corpus-EXACT at the FORM level (per MASTER-LEDGER §10.24). cross-finding-012 (Late-Meccan Scripture-Announcement Apparatus) established that 5 Pattern-B axes jointly concentrate at modal Nöldeke bin B7 (ranks 86-99, Hijra-straddling). The tanzīl-opener IS Pattern-B "scripture-announcement-content".

**Question pre-registered:** Are the 6 tanzīl-cluster surahs more chronologically concentrated (under Nöldeke ranks) than corpus-random 6-subsets? If yes, the H-NEW-1100 opener-form is empirically a Late-Meccan-phase signature, vindicating cross-finding-012's Pattern-B grouping at corpus-EXACT precision for this specific opener-form cluster.

**H1 (direction-locked):** The 6-surah tanzīl-cluster has a LOWER variance-of-Nöldeke-rank (i.e., is more chronologically concentrated) than corpus-random 6-subsets at α_bon = 0.0125 (one-tailed lower-tail).

**H2 (direction-locked, secondary):** The 6-surah tanzīl-cluster has a HIGHER mean Nöldeke rank (i.e., is later in chronology) than corpus-random 6-subsets at α_bon = 0.0125 (one-tailed upper-tail).

**Pre-commit violation conditions:**
- H1 reverse: variance-Nöldeke ≥ corpus-random 75th percentile → publish as NULL with `EXPLORATORY-REVERSE` tag (PRE-REG-STANDARD-01); cluster is chronologically DISPERSED, not concentrated.
- H2 reverse: mean Nöldeke rank below corpus-random 25th percentile → cluster is EARLY rather than Late Meccan; falsifies cross-finding-012 reading at this sub-axis.

**H0:** The tanzīl cluster's chronological distribution is corpus-typical.

## 2. Operational definitions

- Nöldeke ranks: from `data/revelation-order.csv` column `noldeke_order` (1 = earliest, 114 = latest).
- Tanzīl-cluster (H-NEW-1100): T = {32, 39, 40, 41, 45, 46}, n=6.
- Var-statistic: `np.var(noldeke_ranks_in_T, ddof=0)`.
- Mean-statistic: `np.mean(noldeke_ranks_in_T)`.
- Null distribution: 10,000 random 6-subsets of {1,...,114}, seed 20260509.
- One-tailed test on each H1, H2.

## 3. Empirical anchors (locked, verified pre-reg)

From `data/revelation-order.csv`:
- Q 32 al-Sajda: Nöldeke 70 (Late Meccan)
- Q 39 al-Zumar: Nöldeke 80 (Late Meccan)
- Q 40 Ghāfir: Nöldeke 78 (Late Meccan)
- Q 41 Fuṣṣilat: Nöldeke 71 (Late Meccan)
- Q 45 al-Jāthiya: Nöldeke 72 (Late Meccan)
- Q 46 al-Aḥqāf: Nöldeke 88 (Late Meccan)

All 6 fall within Nöldeke ranks [70, 88], a range-span of 18 of 114 (15.8%) — visibly concentrated. Variance ≈ 47.5; mean ≈ 76.5. Mean rank 76.5 is firmly within the Pattern-B B6/B7 zone (cross-finding-012).

The empirical-anchor inspection above is DISCLOSED: the lowering-variance direction is locked because the values are visibly clustered. This does NOT fit the post-hoc protocol — the inspection happens AFTER pre-reg framing of the specific hypothesis (Late-Meccan-concentration was the cross-finding-012 prediction). Single-test α=0.0125 used regardless.

## 4. Success / Failure

- **CONFIRMED-DIRECTED**: H1 perm-p ≤ 0.0125 AND H2 perm-p ≤ 0.0125 (both: low variance + high mean).
- **PASS-DIRECTED**: H1 OR H2 passes at α_bon = 0.0125, not both.
- **NULL**: Both fail.
- **PRE-COMMIT VIOLATION**: Either reverses (variance high or mean low) → `EXPLORATORY-REVERSE`.

## 5. Honest limits

- N=6 is small; statistical power is moderate. Two-tailed test would be unstable; one-tailed direction-locked is appropriate but conservative.
- The H-NEW-1100 cluster was DISCOVERED by formal-pattern (opener form), not by chronology. Co-localization at chronology is a claim of *cross-axis correlation*, not redundancy.
- cross-finding-012 has shared latent factor with Pattern-B per audit-036 A3 — this test is SUPPORTING / CO-DEPENDENT with cross-finding-012, not independent evidence.

## 6. Bonferroni & rules-tuple

- Family `Q039-novel-tests`, k=4 (Q039-F-01..F-04), α_bon = 0.05/4 = 0.0125.
- Rules-tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, mashriqi).
- Seed 20260509.

## 7. SHA-locked

This pre-reg's SHA-256 is computed and stored in run script `Q039_F_01_tanzil_cluster.py`; runtime verification at start.
