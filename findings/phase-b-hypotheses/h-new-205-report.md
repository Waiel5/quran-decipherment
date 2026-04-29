---
id: H-NEW-205
title: "Fisher-Rao M1 geodesic at VERSE level: B7 (Late-Meccan) vs OTHER"
phase: B
status: NULL
date: 2026-04-17
seed: 20260419
bonferroni_k: 2
alpha_bon: 0.025
pre_reg_sha256: a41140db44e9a97e5157d85343827249b4194d1966b9b67f0a0397436c162aeb
---

# [[h-new-205-report|H-NEW-205]] — Fisher-Rao verse-level M1 geodesic NOT stronger within B7

## Question
Is the verse-level Fisher-Rao canonical geodesic *more anomalously short* within the 14 B7 Late-Meccan surahs (Q 2, 3, 6, 7, 8, 13, 35, 46, 47, 57, 61, 62, 64, 98; [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] modal peak) than within the other 100 surahs? If yes, M1 would be LM-localized; if no, M1 is period-invariant.

## Method
QAC STEM roots → top-K=300 → Dirichlet(α=0.5) → Fisher-Rao angular distance. For each surah n≥5, compute verse-level canonical path length vs 10,000 permutation null → z-score and L_canon/L_2opt ratio. MWU one-sided (B7 < OTHER) on both, Bonferroni-2 (α=0.025). Seed 20260419. 109 included (5 short surahs excluded; none in B7).

## Results
- median z: B7 = **−1.85**, OTHER = **−2.39** (B7 LESS anomalous; direction opposite to hypothesis)
- median ratio: B7 = 1.146, OTHER = 1.175
- Test 1 (MWU z): p_perm = 0.470 → FAIL
- Test 2 (MWU ratio): p_perm = 0.103 → FAIL

## Verdict
**NULL.** M1 verse-level geodesic is NOT B7-localized. In fact the point estimate for the z-score test runs *opposite* the prediction.

## Implication
M1 (structured Fisher-Rao Hamiltonian path) is orthogonal to P1★ (Late-Meccan scripture-announcement apparatus). The two principles are independent axes, consistent with [[cross-finding-018-four-principle-reduced-model|cross-finding-018]]'s four-principle reduced model and [[h-new-141-pattern-b-within-late-meccan|H-NEW-141]]'s finding that the LM apparatus is a bundle phenomenon, not a latent factor. M1 survives as a period-invariant topological property of the mushaf content space.

Artifacts:
- `scripts/h_new_205_verse_fisher_rao_b7.py`
- `findings/phase-b-hypotheses/h-new-205-prereg.md`
- `findings/phase-b-hypotheses/csv/h-new-205.json`
