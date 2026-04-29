---
id: H-NEW-205
title: "Fisher-Rao M1 geodesic at VERSE level within Late-Meccan B7 vs outside"
phase: B
status: PRE-REGISTERED (2026-04-17)
date: 2026-04-17
author: autonomous-agent (grey-dispatched)
parent_findings:
  - H-NEW-111 (surah-level Fisher-Rao M1 geodesic; PASS-DIRECTED)
  - H-NEW-127 (verse-level Fisher-Rao within 5 locked surahs; PASS-DIRECTED)
  - cross-finding-012 (Late-Meccan scripture-announcement apparatus, modal peak bin B7)
  - cross-finding-016 (LM apparatus synthesis)
  - H-NEW-141 (Pattern-B independent within Late-Meccan — NULL)
rules_tuple: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf verse order, Hafs-Kūfan, 114 surahs)
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-205
alpha_bon: 0.025
---

# [[h-new-205-report|H-NEW-205]] pre-registration — Is the verse-level M1 geodesic STRONGER within Late-Meccan B7 than outside?

## Motivation

- M1 is "structured Hamiltonian path/cycle in Fisher-Rao content space" (theorist merger of P2+P8 under [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]).
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] CONFIRMED at surah level; [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] CONFIRMED at verse level within 5 locked surahs (Q 2/7/12/36/55), showing z_score < −6 for all five.
- [[cross-finding-012-late-meccan-scripture-announcement|Cross-finding-012]] identified B7 (Nöldeke ranks 86–99, 14 surahs straddling the Hijra) as the modal peak for the scripture-announcement apparatus.
- [[h-new-141-pattern-b-within-late-meccan|H-NEW-141]] showed that Pattern-B axes are INDEPENDENT within Late-Meccan — the apparatus is a bundle phenomenon at inter-period scale.
- Open question: does the M1 geodesic effect *also* peak at B7, or is it orthogonal to the LM apparatus? If M1 is strictly content-topological (P2 merger), it should be approximately period-invariant; if it is functionally entangled with the scripture-announcement apparatus, B7 surahs should show a STRONGER verse-level geodesic.

This finding is a specific, falsifiable decomposition of M1.

## Hypothesis

H1: Verse-level Fisher-Rao canonical path is *more* anomalously short (more negative z) within the 14 B7 surahs than within the remaining 100 surahs.

## Design

### Data
- QAC v0.4 STEM root tokens per (surah, verse).
- Top-K=300 roots globally (locked; identical to [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] locked parameter, inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] pre-reg).
- Dirichlet α=0.5 smoothing (Jeffreys).
- Fisher-Rao angular distance d(p,q) = 2·arccos(Σ √(p_i q_i)).

### Per-surah statistic
For each surah s with n(s) ≥ 5 verses:
- Build n×n Fisher-Rao distance matrix D_s over verse probability vectors.
- L_canon(s) = Σᵢ D_s[i, i+1] on mushaf (i=1..n−1) verse order.
- Null: 10,000 random permutations of verse order; compute L_perm distribution (per-surah RNG seeded by SEED + sid·1000003).
- z(s) = (L_canon(s) − null_mean(s)) / null_sd(s).
- p(s) = one-sided lower-tail empirical p-value.
- L_2opt(s) via greedy-NN from every start + 2-opt refinement.
- ratio(s) = L_canon(s) / L_2opt(s).

Surahs with n < 5 are excluded from both groups (insufficient permutation support); the excluded short surahs are documented for transparency.

### Groups
- GROUP_B7 = {Q 2, 3, 6, 7, 8, 13, 35, 46, 47, 57, 61, 62, 64, 98} (14 surahs; per [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] modal peak bin).
- GROUP_OTHER = all remaining surahs (expected ≈100 after exclusion of n<5 surahs, which are all very short late-Meccan/pre-hijra; these are NOT in B7 by construction so exclusion only reduces OTHER).

### Primary tests (Bonferroni k=2, α_bon = 0.025)

**Test 1 (primary-z)**: One-sided Mann-Whitney U (WMW) on z-scores.
H1: z(B7) distributionally less than z(OTHER) — i.e., B7 z-scores are more negative (more anomalous geodesic).
Report: U, U_prob, n1, n2, median_z_B7, median_z_OTHER, Hodges-Lehmann shift.
PASS iff p_MWU_one_sided < 0.025.

**Test 2 (primary-ratio)**: One-sided MWU on L_canon/L_2opt ratio.
H1: ratio(B7) distributionally greater than ratio(OTHER) — B7 surahs have canonical path further above the optimum (stronger structure). NOTE: if M1 is strong, L_canon is CLOSE to optimum, meaning ratio is CLOSE to 1. So if B7 has stronger M1, ratio(B7) should be *smaller* (closer to 1), not larger. Correct direction: ratio(B7) < ratio(OTHER).
H1 (corrected): ratio(B7) distributionally LESS THAN ratio(OTHER).
PASS iff p_MWU_one_sided < 0.025.

### Verdict table (joint)

| Test 1 (z) | Test 2 (ratio) | Family verdict |
|---|---|---|
| PASS | PASS | CONFIRMED — B7 has stronger verse-level M1 |
| PASS | FAIL | PARTIAL (z but not ratio) |
| FAIL | PASS | PARTIAL (ratio but not z) |
| FAIL | FAIL | NULL — M1 is not B7-localized |

### Garden-of-forking-paths log (before data contact)

- Alternative group definition (B6+B7, 8-bin {B5,B6,B7}): NOT used. Primary is strict B7 (the modal peak).
- Alternative n-floor (n≥10): considered; rejected because it would remove all 6-verse etc. short surahs which are NOT in B7 anyway, so choice does not affect B7 group. Used n≥5 (smallest surah with permutation support).
- Alternative test (t-test on z): not used — MWU robust to non-normality of z distribution.
- Alternative distance (Euclidean on sqrt(p)): not used — Fisher-Rao angular is the locked M1 metric.
- Direction of ratio test clarified above (should be B7 < OTHER, not >).

### Permutations & seeds
- PERMS = 10,000
- Master SEED = 20260419 (assigned by task)
- Per-surah RNG = Random(SEED + sid·1000003)

### Output artifacts
- `findings/phase-b-hypotheses/csv/h-new-205.json`: full per-surah stats + both tests + verdict.
- `findings/phase-b-hypotheses/h-new-205-report.md`: <200-word report.
- `scripts/h_new_205_verse_fisher_rao_b7.py`: the executed script.

## Falsifiers

- If p_MWU_one_sided(z) > 0.50 AND p_MWU_one_sided(ratio) > 0.50, [[h-new-205-report|H-NEW-205]] is NULL-STRONG and M1 is period-invariant (independent of the LM apparatus).
- If BOTH primary tests PASS Bonferroni-2, M1 and P1★ (LM apparatus) are jointly-localized, which has significant implications for the reduced-principle model.
