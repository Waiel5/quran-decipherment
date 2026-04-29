---
id: H-NEW-410
title: "Full 114-surah local-content-outlier spectrum via mean-FR-distance-to-neighbors ranking"
phase: B
status: PRE-REGISTERED 2026-04-21
date: 2026-04-21
agent: team-lead (inline; ID 410 skip codex range)
parent_1: H-NEW-390 (Q 55 outlier +32.6pp)
parent_2: H-NEW-400 (Q 62 NOT outlier)
seed: 20260508
bonferroni_k: 1
bonferroni_family: h-new-410-outlier-spectrum
alpha_bon: 0.05
rules_tuple: "(114 surahs; FR from H-NEW-111; for each surah k, compute mean pairwise FR to its 4 mushaf-nearest neighbors at positions k±1, k±2 — excluding out-of-range neighbors; rank all 114 by mean distance; top-10 constitutes empirical outlier spectrum)"
direction: "Descriptive ranking; pre-committed: Q 55 expected in top-5; Q 62 expected NOT in top-10 (per H-NEW-390/400); Q 1 expected in top-10 (per H-NEW-155 sui-generis classification)"
verdict: PENDING
---

# [[h-new-410-outlier-spectrum|H-NEW-410]] — Full 114-surah local-outlier spectrum

## 1. Question

[[h-new-390-q55-outlier-exclusion|H-NEW-390]] confirmed Q 55 al-Raḥmān as content-outlier (+32.6pp disruption). [[h-new-400-q62-outlier-candidate|H-NEW-400]] confirmed Q 62 al-Jumuʿa is NOT an outlier. **What is the FULL empirical outlier spectrum across all 114 surahs?**

For each surah, compute mean Fisher-Rao distance to its 4 mushaf-nearest neighbors (k±1, k±2). Surahs with HIGH mean-distance-to-neighbors are LOCAL CONTENT OUTLIERS — their content register differs from adjacent surahs.

This yields a DATA-DRIVEN outlier ranking across the corpus, independent of classical-designation bias.

## 2. Protocol

1. Load [[h-new-111-fisher-rao-mushaf|H-NEW-111]] FR distance matrix (114×114).
2. For k in 1..114:
   - neighbors = {k-2, k-1, k+1, k+2} ∩ [1, 114] (exclude self; exclude out-of-range)
   - mean_dist[k] = average FR distance from k to its neighbors
3. Rank all 114 surahs by mean_dist descending (highest = most outlier-like).
4. Report top-10 outliers with per-neighbor distances.
5. Verify Q 55 position; verify Q 62 position.

## 3. Pre-committed predictions

- **Q 55 al-Raḥmān**: Top-5 (per [[h-new-390-q55-outlier-exclusion|H-NEW-390]] +32.6pp block-disruption effect)
- **Q 62 al-Jumuʿa**: NOT in top-10 (per [[h-new-400-q62-outlier-candidate|H-NEW-400]] below-null distances)
- **Q 1 al-Fātiḥa**: Top-10 (per [[h-new-155-q1-sui-generis|H-NEW-155]] sui-generis-liturgical classification + [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]] content-distant status)
- **Q 112 al-Ikhlāṣ**: uncertain ([[h-new-350-al-tiwal-cohesion|H-NEW-350]] shows it's IN the terminal tail 0%ile cohesion)

## 4. Bonferroni + descriptive scope

This is a RANKING task, not inferential. k=1 (single descriptive test); α = 0.05 single-test cap per MW-7. No inferential claim at each individual surah; interpretation applies to the top-K set as descriptive outlier-spectrum.

## 5. Honest limits

1. ±2 neighbor window is arbitrary — broader window (±3 or ±5) could re-rank.
2. Boundary surahs (Q 1, Q 2, Q 113, Q 114) have fewer neighbors (only 2-3 in window).
3. Classical outlier-recognitions vary — some scholars flag different surahs.
4. FR-roots only.

## 6. Classical anchor

Outlier-recognition layer in classical tradition:
- al-Tirmidhī #3291: *ʿarūs al-Qurʾān* for Q 55
- al-Tabrisī *Majmaʿ al-Bayān* Q 1 as unique-prayer
- al-Zamakhsharī *Kashshāf* Q 55 singular cosmic-mercy
- al-Suyūṭī *Itqān* Q 112 as theological-central "third of Quran"

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_410_outlier_spectrum.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-410.json`
- Findings: `findings/phase-b-hypotheses/h-new-410-outlier-spectrum.md`

Pre-reg locked 2026-04-21.
