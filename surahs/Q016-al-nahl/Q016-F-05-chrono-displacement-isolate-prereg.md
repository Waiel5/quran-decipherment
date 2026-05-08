---
finding_id: Q016-F-05
title: Chronology-vs-mushaf displacement and true-isolate status across the 5 isolates
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q016-al-nahl-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q016-F-05-isolate-displacement
bonferroni_k: 2
alpha_bon: 0.025
direction: one-sided UPPER on Spearman ρ(|chrono_rank − mushaf_rank|, isolate_status_indicator) — POSITIVE correlation predicted
success_criterion: Spearman ρ ≥ 0; permutation p ≤ α_bon = 0.025 on at least one of 2 chronology systems (Tanzil vs Nöldeke)
failure_criterion: ρ ≤ 0 in BOTH chronology systems
rules_tuple: "(Hafs-Kufan, mushaf-position, Tanzil/Nöldeke chronologies)"
script: surahs/Q016-al-nahl/scripts/Q016_F_05_chrono_displacement.py
output_json: surahs/Q016-al-nahl/csv/Q016-F-05.json
parent_oq: Why does the true-isolate set {Q 16, 21, 22, 23, 25} share invisibility to cluster-systems?
---

# Q016-F-05 — Chrono-vs-mushaf displacement of the 5 isolates (pre-reg)

## 1. Hypothesis

**H1 (one-tailed):** The 5 true-isolate surahs {Q 16, 21, 22, 23, 25} have **systematically larger chronology-vs-mushaf displacement** |chrono_rank − mushaf_rank| than non-isolates. Operationally: across all 114 surahs, the binary indicator `is_isolate` (1 for {16,21,22,23,25}, 0 otherwise) **positively correlates** with |chrono_rank − mushaf_rank|.

**H0:** No correlation; isolate-status is independent of chronology-displacement.

**Direction:** Spearman ρ > 0 (LOCKED).

## 2. Why this is the right test

The 5 isolates {Q 16, 21, 22, 23, 25} are **invisible to all 20 cluster-systems** in cross-finding-010, including Nöldeke 4-period chronology + the Suyūṭī mushaf-grouping. One natural mechanism: an isolate is invisible to *both* chronology and mushaf because it has a *high displacement between them* — it lives in a different "location" under chronology than under mushaf, so it doesn't co-cluster with chronology-neighbors OR mushaf-neighbors.

Q 16 itself: mushaf-rank 16, Tanzil-chrono-rank 70, Nöldeke-rank 73. **|displacement| = 54 (Tanzil) / 57 (Nöldeke).** The other isolates: Q 21 = 73-21 = 52; Q 22 = 103-22 = 81 (extreme); Q 23 = 74-23 = 51; Q 25 = 42-25 = 17. **Mean |displacement| of isolates = 51.0 (Tanzil)** vs corpus-mean (rough) ≈ 30.

## 3. Operational definition

**Inputs**:
- `data/revelation-order.csv` provides Tanzil revelation-order (column 1) and Nöldeke order (column 6) for each mushaf-position (column 2).
- `is_isolate(s)` = 1 if s ∈ {16, 21, 22, 23, 25}; 0 otherwise.

**Statistics** (Bonferroni k = 2 family):
- F-05a: Spearman ρ(|tanzil_rank − mushaf_rank|, is_isolate) across 114 surahs.
- F-05b: Spearman ρ(|noldeke_rank − mushaf_rank|, is_isolate) across 114 surahs.

**Permutation null**: 10000 random samples of 5 surahs (instead of the actual 5 isolates), each time recompute the Spearman ρ; empirical p = fraction of null samples with ρ ≥ observed ρ.

## 4. Acceptance / failure

- **CONFIRMED**: BOTH F-05a and F-05b reject H0 at α_bon = 0.025.
- **DIRECTIONAL**: 1 of 2 rejects.
- **NULL**: Neither rejects.
- **Pre-commit violation**: ρ < 0 in both — isolates have *lower* displacement than non-isolates, contradicting the mechanism.

## 5. Honest limits

- N = 114 surahs but only 5 are isolates → low statistical power for Spearman. The permutation-null on the 5-out-of-114 sampling distribution accounts for this.
- Spearman ρ on a binary x continuous is mathematically equivalent to a 2-sample comparison (Mann-Whitney U). We report both.
- Tanzil-chronology and Nöldeke-chronology are the two project-canonical sources; they correlate but are not identical.

## 6. Why this matters for Q 16 specifically

If the test passes, then the *mechanism* of Q 16's true-isolate status is partly explained: Q 16 is mushaf-position-16 (head ṭiwāl, bordering ALR-cluster) but chronology-position-70 (late Meccan, post-Hijra-conditional). Its content profile is late-Meccan niʿmah-catalog rhetoric, but its mushaf-neighbors are mid-Meccan ALR muqaṭṭaʿāt prophet-narratives. The mismatch makes Q 16 invisible to BOTH a chronology-clusterer AND a mushaf-clusterer.

## 7. Garden-of-forking-paths log

- **Why Spearman not Pearson?** is_isolate is binary; Spearman handles tied ranks; chrono-displacement is integer.
- **Why the absolute value?** Direction-of-displacement (early-revelation surah placed late OR late-revelation surah placed early) is symmetric for the cluster-invisibility mechanism — both directions move the surah away from its chronology-neighbors.
- **Why 2 chronology systems not 1?** Tanzil + Nöldeke disagree slightly. Bonferroni k=2 ensures the conclusion is robust.

## 8. MW protections

- MW-1: ranks are pre-defined from `data/revelation-order.csv`.
- MW-2: 10000-permutation null on 5-out-of-114 random sampling.
- MW-3: Tanzil + Nöldeke = 2 chronology variants.
- MW-5 (positive-control): replace {16,21,22,23,25} with {1,2,3,4,5} (the head ṭiwāl) — these should NOT show high displacement; if they do, instrument broken. Also: replace with {110,111,112,113,114} (the terminal qiṣār) — these were revealed early but placed late, so they should show high displacement (this is a REVERSE-positive-control that confirms displacement is meaningful).
- MW-6: 5-out-of-114 random sampling = corpus-prior.
- MW-7: direction is pre-registered upper-tail.

## 9. Files

- Pre-reg: `surahs/Q016-al-nahl/Q016-F-05-chrono-displacement-isolate-prereg.md`
- Script: `surahs/Q016-al-nahl/scripts/Q016_F_05_chrono_displacement.py`
- Output: `surahs/Q016-al-nahl/csv/Q016-F-05.json`

*PRE-REG LOCKED 2026-05-07.*
