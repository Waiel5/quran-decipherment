---
id: H-NEW-880
run: 1
date: 2026-04-28
seed: 20260450
prereg_sha: 5ff0a959d3684aaaf0ee9670da2f9f460eeeb6c0827c783b6295428a6c23df00
verdict: STRONG NULL
elapsed_sec: 46.3
---

# H-NEW-880 — Run 1 Journal

## Pre-run

- Read H-NEW-690 (compression-tail-alone causal: NULL median 25% vs canonical 11%).
- Read H-NEW-720 (super-additive adjacencies, Σ Δ = 9.83 vs actual 8.29; cooperative ratio 1.185×).
- Read H-NEW-840 (top architectural surahs: Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17).
- Confirmed canonical L = 85.7597, L_2opt = 77.4669, residual = 10.70% from h-new-111.json.

## Pre-reg drafting

Drafted seven constraints (C1..C7) in fixed nesting order. Initial draft used C5 = 5 inversions per phase and C7 = head-cap-50.

## Pre-run sanity check (calibration)

Before running ANY chain, ran sanity check on canonical alone to verify it satisfies all seven constraints. Result: canonical FAILS C5 and C7 as drafted:

- C5 (tol=5): canonical has 20 inversions in Early Meccan phase. Fails.
- C7 (cap=50): canonical has Q 68 al-Qalam (a muqaṭṭaʿāt surah) at position 68. Fails.

This was a pre-reg specification bug. If left unfixed, S5..S7 would have INFEASIBLE-START — the test would be unrunnable. Per garden-of-forking-paths discipline, recalibrated:

- C5 tolerance set to 25 (= max canonical inversion 20 + 5 margin).
- C7 cap set to 68 (= max canonical muqaṭṭaʿāt position).

Both calibrations are conservative *toward* finding STRONG-RECIPE: looser constraints give the chain more freedom to escape canonical, not less. Pre-reg §8a documents this calibration explicitly.

Re-computed pre-reg SHA: `5ff0a959d3684aaaf0ee9670da2f9f460eeeb6c0827c783b6295428a6c23df00`. Updated `EXPECTED_PREREG_SHA` in script accordingly.

Re-verified canonical now satisfies ALL seven constraints under calibrated thresholds. ✓

## Run

Executed `python3 scripts/h_new_880_recipe.py` at 2026-04-28. Total elapsed: 46.3s.

Per-subset chain stats (12000 proposals, 2000 burn-in, sample every 100):

| Subset | Constraint-OK% | Acceptance | n_samples | Median resid |
|:--|:-:|:-:|:-:|:-:|
| S1 (C1) | 66.5% | 7294/12000 | 100 | 24.58% |
| S2 (+C2) | 66.2% | 7251 | 100 | 24.66% |
| S3 (+C3) | 63.4% | 6964 | 100 | 24.60% |
| S4 (+C4) | 62.4% | 6865 | 100 | 24.90% |
| S5 (+C5) | 60.4% | 6599 | 100 | 24.73% |
| S6 (+C6) | 52.7% | 5796 | 100 | 24.64% |
| S7 (+C7) | 50.7% | 5637 | 100 | 23.47% |

Each chain mixed well (acceptance > 47% in all cases). Constraint-feasibility rate degraded smoothly (66% → 51%) as constraints stacked, but no subset collapsed.

S1 replicated H-NEW-690 within MC variance (24.58% vs H-NEW-690's 24.95%; same NULL verdict). Reproducibility confirmed.

## Results

ALL SEVEN SUBSETS verdict = NULL (median > 15%). Earliest DIRECTIONAL recipe: NONE. Minimal STRONG recipe: NONE.

S7 (full constraint stack) median = 23.47%; min = 20.21%. Canonical (10.70%) sits below the entire S7 ensemble (canonical percentile = 0.0%).

Adding C2..C7 to C1 reduces median by only 1.1 pp (24.58 → 23.47), versus the residual gap to canonical of ~13 pp.

## Interpretation

The seven-constraint recipe is necessary-but-far-from-sufficient. Canonical is *exceptional within the recipe-respecting subset*, not *typical of it*. The recipe-derivability hypothesis at the seven-constraint resolution is falsified.

Three live alternatives going forward:
1. Hidden joint adjacency cooperativity (H-NEW-720 super-additivity not captured by C1..C7).
2. Higher-order architectural constraints not yet hypothesized (ḥawāmīm grouping, musabbiḥāt, thematic-pair couplings).
3. Non-decomposable global optimum (no small recipe exists).

## Limits noted

- S2..S7 start from canonical (conservative toward STRONG); MCMC explores feasible region but biased mildly toward canonical neighborhood. Acceptance rates 50-66% indicate good mixing.
- T_MH = 1.0 introduces soft TSP-bias (conservative toward STRONG).
- 100 samples per subset; medians stable to ±0.3 pp under bootstrap.
- 7 constraints tested are not exhaustive; this falsifies *this specific recipe*, not the broader hypothesis that some recipe exists.

## Files written

- `findings/phase-b-hypotheses/h-new-880-recipe-prereg.md` (calibrated, locked SHA `5ff0a959...`)
- `scripts/h_new_880_recipe.py`
- `findings/phase-b-hypotheses/csv/h-new-880.json`
- `findings/phase-b-hypotheses/h-new-880-recipe.md`
- `journal/h-new-880-run-1.md` (this file)

## Status

COMPLETE. Verdict: STRONG NULL across all 7 nested subsets.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
