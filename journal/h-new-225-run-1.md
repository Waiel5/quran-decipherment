# H-NEW-225 — Adversarial search run journal (run 1)

**Date**: 2026-04-17
**Specialist**: autonomous
**Seed**: 20260419

## Actions

1. Read parent finding H-NEW-111 + sibling H-NEW-144 to confirm D-matrix provenance.
2. Verified H-NEW-111's JSON contains the 114×114 D-matrix upper-triangular (6441 pairs).
3. Authored pre-reg at `findings/phase-b-hypotheses/h-new-225-adversarial-search-prereg.md` BEFORE running any search (SHA-256: `345e7c87dc6ddd720d568232b09e092db3a0e2e7167f03281003f1e97fe57ee5`).
4. Authored `scripts/h_new_225_adversarial_search.py`.
5. Executed script (seed 20260419, 100 SA restarts, 10K iters each, T0=5.0, cooling 0.995).

## MW-5 positive control

L_mushaf reloaded = 85.759655 vs parent 85.759656. Delta < 1e-5. PASS.

## Garden of forking paths (committed pre-run)

- D-matrix: reused from H-NEW-111 verbatim (no re-extraction).
- SA hyperparameters: T0=5.0, cooling=0.995, 10K iters, 50/50 2-opt-reversal/swap proposal, 2-opt polish.
- 100 seeds: 20260419..20260518.
- Single decision cell (k=1); descriptive α=0.05.

## Result

| Item | Value |
|---|---:|
| L_mushaf | 85.760 |
| L_mushaf_2opt (from canonical start) | 77.973 (81 improving swaps) |
| L_SA_min (100 restarts) | 77.404 (seed 20260465) |
| L_search_min | 77.404 |
| gap_abs | 8.355 |
| gap_rel | **1.1079** |
| mushaf rank (pooled) | 102/102 |
| Verdict | **PASS** |

Mushaf is NOT 2-opt-locally optimal. The FIRST improving swap reverses the path at i=0, j=113 (Δ=−0.789).

H-NEW-111's L_2opt bound (77.467) tightened to 77.404 via SA — self-verifying tightening amendment per project discipline.

## Runtime

~4 minutes total on the single-thread Python implementation.

## Queued follow-ups

- Cross-metric replication (Hellinger / Jensen-Shannon) — H-NEW-225b candidate.
- Concorde-exact or LKH-3 run to settle L_min definitively (environment-blocked; queued).
- H-NEW-225c: same search on char-4gram D-matrix (from H-NEW-111b) — would strengthen the gap-quantification as feature-invariant.

## Files written

- `findings/phase-b-hypotheses/h-new-225-adversarial-search-prereg.md`
- `scripts/h_new_225_adversarial_search.py`
- `findings/phase-b-hypotheses/csv/h-new-225.json`
- `findings/phase-b-hypotheses/h-new-225-adversarial-search.md`
- `journal/h-new-225-run-1.md` (this file)
