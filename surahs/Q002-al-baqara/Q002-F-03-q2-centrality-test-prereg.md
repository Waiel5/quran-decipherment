---
test_id: Q002-F-03
title: Q 2 gravitational centrality in the FR distance matrix
target_claim: al-Biqāʿī (*Naẓm al-Durar*, intro and Q 2 sections) — al-Baqara is the "scaffold" of the entire Quran's structure; Q 2's removal should perturb the corpus geometry more than removal of any other surah.
date_locked: 2026-04-28
phase: B+
status: PRE-REGISTERED
seed: 20260428
---

# Pre-registration — Q002-F-03: Q 2 centrality / leave-one-out centroid shift

## 1. Hypothesis (LOCKED)

**H1**: Among all 114 surahs, the Q 2 leave-one-out centroid shift in FR distance space is in the top-5 (i.e. rank ≤ 5).

**H0**: rank > 5.

**Direction (LOCKED)**: HIGH (Q 2 is more "central" — its removal shifts the geometry MORE than 95% of others).

## 2. Operationalisation

- **Distance matrix**: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular` (114×114, FR on QAC stem-roots).
- **Centroid (medoid)**: surah whose mean distance to all others is minimum.
- **Leave-one-out shift**: for each surah X, recompute the medoid on the 113-surah subset; record the change in mean-distance vector (Σ |Δd_i| over the remaining 113 surahs).
- **Rank Q 2** in descending order of shift magnitude.

## 3. Alternative metric (MW-3)

Also compute "total gravitational pull" of each surah X = Σ_j (1/D[X,j]) (lower distance = stronger pull). Rank Q 2.

## 4. Success criteria

- **VINDICATED**: Q 2 in top-5 on EITHER metric.
- **DIRECTIONAL**: top-15.
- **NULL**: rank > 15 on both.
- **PRE-COMMIT VIOLATION**: Q 2 in bottom-half (rank > 57).

## 5. Bonferroni

Family α = 0.01 across the Q 2 5-test family. Top-5 of 114 = 4.4% (raw α). Within family-α since the rank-criterion is conservative.

## 6. MW-5 replication

Re-rank using sum-of-distances mean instead of medoid; both should agree.

## 7. Output paths

- Script: `/Users/grey/Downloads/quran/scripts/Q002_F_03_centrality.py`
- JSON: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/csv/Q002-F-03.json`
- Findings: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/Q002-F-03-centrality.md`

*Locked 2026-04-28.*
