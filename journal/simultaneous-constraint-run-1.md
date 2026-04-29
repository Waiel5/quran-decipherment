---
date: 2026-04-12
test: Tomorrow Test 4 — Simultaneous N-Constraint Density
status: COMPLETE
verdict: PASS (KS p = 8.7e-33; tail k>=8 ratio 2.88x, z=+6.73)
seed: 20260412
---

# Run log — Simultaneous-constraint density

## Inputs confirmed
- 6,236 Quranic verses loaded from `quran-text/quran-no-tashkeel.json`.
- 196 divine-name surface forms (99 canonical + definite-article variants).
- Iltifāt catalog: 3,945 verses flagged (inter-shift-strict OR intra-strict).
- Jinās catalog: 2,531 verses with at least one jinās instance.
- Morphology: 6,214 verses with ≥1 tagged root; 1,642 distinct roots in root-stats.
- Baseline pool: 10 Arabic corpora (bukhari-noquran, sira-ibn-hisham, jahiz-hayawan, 7 muʿallaqāt) totalling ~10.8 MB raw.

## Computation
- All 12 constraints computed per verse for the Quran (catalog-enriched) and Quran (fallback-only) and for 6,236 length-matched pseudo-verses sampled from the baseline pool (seed 20260412).
- Assonance and surprisal thresholds: within-corpus, length-bucket-stratified for assonance; median-of-corpus for surprisal (each corpus uses its own median → ≈0.5 marginal by construction).
- KS two-sample test on per-verse simultaneous-count distribution.
- Two-proportion z on tail rate at k ≥ 8 (pre-registered cut).
- Sensitivity: independence-null via column-shuffle of Quranic M matrix.

## Results
| Metric | Quran (catalog) | Quran (fallback) | Baseline |
|---|---|---|---|
| mean constraints/verse | 4.176 | 4.351 | 3.710 |
| median | 4 | 4 | 4 |
| tail ≥ 8 count | 141 | 170 | 49 |
| tail ≥ 8 rate | 2.26% | 2.73% | 0.79% |

- KS (catalog vs baseline): D = 0.1092, p = 8.7e-33
- KS (fallback vs baseline): D = 0.1591, p = 3.0e-69
- Tail z (catalog): +6.73, ratio 2.88× (both ≥ pre-registered thresholds)
- Tail z (fallback): +8.25, ratio 3.47×
- Independence null (Quran, column-shuffled): tail≥8 = 1.52%; observed 2.26% → positive co-occurrence of constraints (49% excess)

## Verdict
PASS. Both pre-registered acceptance criteria met at Bonferroni-corrected α = 0.01.

## Notes
- Most of the signal is driven by rhyme-continuity, iltifāt, and canonical-incipit marginals. Abjad digit-root, assonance, Fibonacci-length, divine-name, verse-end dispreference, and surprisal are all at baseline.
- Palindrome rate is *lower* in Quran than baseline under the fallback detector — recorded as honest null.
- Adversarial baseline (rhymed saj' like Khuṭab Quss, rhymed maqāmāt) would narrow the gap; future work.

## Artefacts
- Script: `findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/run.py`
- Results: `findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/results.json`
- Matrices: `M_quran.npy`, `M_quran_fallback.npy`, `M_baseline.npy` (each 6236×12 int8)
- Writeup: `findings/phase-b-hypotheses/simultaneous-constraint-density.md`
