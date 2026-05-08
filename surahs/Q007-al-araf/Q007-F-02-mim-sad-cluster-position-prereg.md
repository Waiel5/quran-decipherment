---
surah: 7
test_id: Q007-F-02
title: المص muqaṭṭaʿ-content-axis position vs الم and الر cluster centroids
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q007-F-01..F-04 (Q 7 surah-local pre-registered family)
alpha_bon: 0.0125
direction_locked: BETWEEN — Q 7 root-bag is BETWEEN الم and الر cluster centroids (closer to ALR than to ALM, OR closer to ALM than to ALR by ≤ 0.05 FR-units)
rules_tuple: (no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q007-F-02 — Pre-registration: المص muqaṭṭaʿ content-axis position

## 1. Background

Q 7 is the SOLE 4-letter muqaṭṭaʿ المص opener (alif-lām-mīm-ṣād). It contains both:
- The 3-letter prefix الم (shared with Q 2, 3, 29, 30, 31, 32 — the ALM-6 cluster)
- An overlap with الر (shared with Q 10, 11, 12, 14, 15 — the ALR-5 cluster) only in the alif-lām opener; the mīm-ṣād suffix is unique.

Classical reading (al-Biqāʿī *Naẓm al-Durar*, al-Suyūṭī *al-Itqān* nawʿ 40) is that المص is structurally a "transitional" letter-set: it shares the alif-lām-mīm prefix of the ALM cluster AND the alif-lām of the ALR cluster, with an additional ṣād. The empirical question: does Q 7's CONTENT-AXIS root-bag profile reflect this orthographic mix?

Project priors (loadcells challenging this claim):
- H-NEW-600 (full-29 muqaṭṭaʿ-content-cohesion): NULL — letter-axis is ⊥ content-axis.
- H-NEW-610 (ALM-6 cohesion): NULL.
- H-NEW-610 (ALR-5 cohesion): NULL.
- Q026-F-02 (TSM-3 cohesion): NULL.
- Q026-F-04 (TSM-twin Mūsā-block): FALSIFIED.

So the prior expectation is **H1 fails** at the cluster-cohesion level. **However**, this test is at the cross-cluster *POSITION* level: not whether ALM and ALR are cohesive, but whether Q 7 sits *between* them. This is a different statistical question.

## 2. Hypothesis (locked before observation)

**H1 (one-tailed, "BETWEEN" direction)**: Q 7's mean Fisher-Rao distance to the ALM-cluster centroid (mean of d(7, Q∈{2,3,29,30,31,32})) and to the ALR-cluster centroid (mean of d(7, Q∈{10,11,12,14,15})) places Q 7 *between* them in this sense:

- BOTH d_ALM(Q7) AND d_ALR(Q7) are below the corpus-wide mean of d(s, ALM-centroid) and d(s, ALR-centroid) respectively, computed across all 114 surahs.
- Q 7 ranks in the top-15/114 (≤ 13.2% percentile) on the COMBINED proximity score = mean(d_ALM, d_ALR), strictly below both individual cluster-internal means (so Q 7 is "in the neighborhood" of both clusters).

**Pre-committed BETWEEN-NESS criterion**:
- Q 7 RANK on `(d_ALM + d_ALR)/2` (lower = closer to mid-ground): top-15/114, AND
- |d_ALM − d_ALR| ≤ 0.10 (Q 7 is roughly equidistant to both centroids).

**H0**: Q 7's letter-mixing in the muqaṭṭaʿ does NOT predict content-axis position; Q 7's combined-proximity rank is no better than median (rank ≥ 57/114) OR Q 7 is strongly biased toward one cluster (|d_ALM − d_ALR| > 0.10).

## 3. Test statistic

Compute on h-new-111.json (114×114 Fisher-Rao distance matrix on QAC stem-roots, locked).

- d_ALM(s) = mean(D[s][q] for q ∈ {2,3,29,30,31,32}, q ≠ s)
- d_ALR(s) = mean(D[s][q] for q ∈ {10,11,12,14,15}, q ≠ s)
- combined(s) = (d_ALM(s) + d_ALR(s)) / 2
- rank Q 7 on combined ascending (lower = closer to both centroids).

Permutation null (10,000 perms, seed 20260507): randomly select 11-surah subsets of muqaṭṭaʿ-29 (matching ALM-6 ∪ ALR-5 size = 11) and recompute Q 7's combined rank. (Tests whether Q 7's between-ness is special to the *ALM ∪ ALR* set vs random muqaṭṭaʿ-subsets.)

## 4. Success / Failure

- **CONFIRMED**: Q 7 rank ≤ 15/114 on combined AND |d_ALM − d_ALR| ≤ 0.10 AND p_perm ≤ 0.0125.
- **DIRECTIONAL**: Q 7 rank ≤ 30/114 OR p_perm ≤ 0.05.
- **NULL**: Q 7 rank > 57/114 OR |d_ALM − d_ALR| > 0.20.
- **PRE-COMMIT VIOLATION**: Q 7 rank > 100/114 (Q 7 is FARTHER from both centroids than typical surahs — a strong anti-clustering result).

## 5. Honest limits

1. The H-NEW-600 / H-NEW-610 NULL streak (5 replications) is a strong prior that this WILL fail. The pre-reg is honest about this expectation.
2. Q 7 might trivially be "close" to both clusters because it shares CONTENT (prophet-narrative) with ALR cluster (Q 10, 11, 12, 14, 15 are all prophet-narrative), and Q 7's neighbors in the mushaf (Q 6, Q 8) are also prophet-narrative-rich. The "BETWEEN-ness" might reflect content-overlap, not muqaṭṭaʿ-letter logic.
3. Therefore, the meaningful test is the COMBINED test: rank ≤ 15 AND equidistance.

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots, FR-distance-from-h-new-111, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q007_F_02_mim_sad_position.py`.
