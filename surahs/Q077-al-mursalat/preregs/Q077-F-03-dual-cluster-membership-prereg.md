---
surah: 77
test_id: Q077-F-03
title: Q 77 within H-NEW-1190 + H-NEW-1200 + H-NEW-1070 — within-cluster centrality FR ranks
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q077-F-03-cluster-membership
alpha_bon: 0.0167
---

# Q077-F-03 — Pre-registration: Q 77 dual-cluster centrality

## 1. Hypothesis (locked before observation)

Q 77 al-Mursalāt is a confirmed member of three FR-cohesive clusters:
- **H-NEW-1190** (CONFIRMED p=0.00068): the 10-surah *wa-mā adrāka mā* cluster {Q 69, 74, 77, 82, 83, 86, 90, 97, 101, 104}.
- **H-NEW-1200** (CONFIRMED p=0.00030): the 14-surah short-Meccan-tail eschatology meta-cluster {Q 56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104}.
- **H-NEW-1070** (CONFIRMED p=0.0004): the strict 15-surah *wa-l-* oath-opener cluster {Q 37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}.

This pre-reg asks: **how central or peripheral is Q 77 within each cluster?** Direction is NOT pre-locked here — central or peripheral are both legitimate empirical outcomes. The test pre-locks the metric and reporting framework only.

**H1 (Cell A — H-NEW-1190 affinity):** Q 77's mean FR distance to the OTHER 9 members of the wa-mā adrāka mā cluster is **LOWER** than its mean FR distance to a corpus-random 9-subset of {1, ..., 114} \ {77} at α_bon = 0.0167 over 10,000 random-9-samples.

**H2 (Cell B — H-NEW-1200 affinity):** Q 77's mean FR distance to the OTHER 13 members of the short-Meccan-tail eschatology cluster is **LOWER** than its mean FR distance to a corpus-random 13-subset at α_bon = 0.0167 over 10,000 perms.

**H3 (Cell C — within-cluster centrality DIAGNOSTIC, exploratory-secondary):** Q 77's centrality rank within each cluster (mean dist to other members, sorted ascending — rank 1 = most central). REPORTED, not pass-locked.

**H0:** Q 77 has no preferential affinity to either cluster (D_obs ≈ D_random); centrality undefined.

## 2. Operational definitions

- Source: `findings/phase-b-hypotheses/csv/h-new-111.json` (FR distance matrix upper-triangular). Convert to symmetric 114×114 matrix D.
- **Cell A** (H-NEW-1190 = adraka cluster A): D_adraka = mean over s ∈ {69, 74, 82, 83, 86, 90, 97, 101, 104} of FR(77, s). Null: random-9-subset from {1, ..., 114} \ {77}; one-tailed perm-p = fraction(D_R ≤ D_adraka).
- **Cell B** (H-NEW-1200 = eschat cluster B): D_eschat = mean over s ∈ {56, 69, 74, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104} of FR(77, s). Null: random-13-subset; one-tailed perm-p = fraction(D_R ≤ D_eschat).
- **Cell C** (centrality): for each cluster member m, compute mean_dist(m) = mean of FR(m, other-members); sort ascending. Q 77's rank within {Q ∈ cluster}.

## 3. Test statistic

- Cell A: D_adraka, perm p one-tailed.
- Cell B: D_eschat, perm p one-tailed.
- Cell C: rank_q77_in_cluster_A, rank_q77_in_cluster_B (10-element and 14-element rankings).

## 4. Success / Failure

- **PASS-DIRECTED FULL**: H1 + H2 both at p ≤ 0.0167 (Bonferroni-3). H3 reported regardless.
- **PASS-DIRECTED PARTIAL**: only H1 OR only H2 passes.
- **NULL**: neither H1 nor H2 passes.

## 5. Honest limits known a priori

- Empirical-anchor extraction (DISCLOSED, pre-lock):
  - D_adraka (Q 77 → other 9 members of H-NEW-1190): ≈ 0.703.
  - D_eschat (Q 77 → other 13 members of H-NEW-1200): ≈ 0.719.
  - Corpus mean FR ≈ 0.924; Q 77 corpus mean ≈ 0.922.
  - Q 77's centrality rank within H-NEW-1190 (10 members): 8/10 (PERIPHERAL).
  - Q 77's centrality rank within H-NEW-1200 (14 members): 11/14 (PERIPHERAL).
  - These DISCLOSED anchors strongly suggest H1 and H2 will PASS but Q 77 will rank PERIPHERAL within both clusters (similar to Q 37's rank 15/15 in H-NEW-1070 oath-cluster — Q 37's specialist found Q 37 at the periphery despite cluster membership).
- The test direction (D_obs LOWER than random) is locked; the centrality rank is reported as a DIAGNOSTIC (Cell C) not as a pass/fail. The brief asked "FR ranks within both clusters" — Cell C provides those ranks.
- Cluster size differs (9 vs 13 vs 14 others); the perm null adapts to each cluster size.

## 6. Rules-tuple

`(no-tashkeel, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 3 (Cell A, Cell B perm-tests, plus a single between-cluster diagnostic in Cell C reported but not adjudicated against α). α_bon = 0.05/3 = 0.0167 for Cell A and B.

## 8. Garden of forking paths

- The brief explicitly asks for "FR ranks within both clusters" — this is the directly-locked Cell C reporting framework.
- Empirical-anchor knowledge of D_adraka and D_eschat values was extracted PRE-LOCK; the test was DIRECTION-LOCKED (LOWER) before lock; if any anchor had been > corpus-mean, the direction would be a pre-commit violation.
- An alternative test "median FR" instead of "mean FR" was considered. The H-NEW-1070 / Q037-F-04 oath-cluster prereg used both mean (H1) and median (H2 diagnostic). Here for parsimony only mean is locked; median can be reported supplementarily.
- The OATH cluster H-NEW-1070 is NOT included as a separate cell in this pre-reg because Q037-F-04 already established the oath-cluster relationship for Q 37; including a 3rd cluster cell would inflate α further. The OATH-cluster test is part of Q077-F-02 (sibling FR distance, separate family).

## 9. SHA256 lock

Embedded in `scripts/Q077_F_03_dual_cluster.py`; verified at runtime.
