# H-NEW-236 — Run 1 journal

**Date**: 2026-04-17
**Specialist**: autonomous
**Pre-reg SHA-256**: `38f79ef5d4346afa5cd366480b61fc538dc85c25079f6e3f95322db65dbf2c0c`
**Seed**: 20260419
**Runtime**: ~45 seconds (1000 SA sims + 1000 random permutations + observables)

## Procedure
Executed per pre-reg §2: 1000 block-respecting SA 2-opt simulations (within-block swaps only, Q1 locked) + 1000 unconstrained random permutations. Observables per pre-reg §3: O1 L_path, O2 W_wrap, O3 block-χ² (sum of z² across 3 blocks), O4 L_tail Q 91-114.

## MW-1 positive control
Empirical mushaf L_path = 85.760 (matches H-NEW-111 expected 85.76 to 3 decimals). ✓

## MW-5 random-null calibration
Random permutations pass 1/4 observables (W_wrap marginally at pct=2.7; all others OUTSIDE). As predicted. ✓ Random L_path mean 104.31; empirical 85.76 at pct=0. Random L_tail mean 21.23; empirical 8.64 at pct=0. Observables have discriminating power.

## Primary decision
- **O1 L_path**: empirical 85.76 OUTSIDE HIGH (sim CI [79.28, 79.63]; pct=100). Sim mean 79.45; gap 6.31 units = 7.9%.
- **O2 W_wrap**: INSIDE (pct=31.8). ✓
- **O3 Block-χ²**: empirical 524.5 OUTSIDE HIGH (sim 97.5 pct = 14.2). Extreme failure driven by L_ḥawāmīm z=+17.4.
- **O4 L_tail**: INSIDE (pct=28.3). ✓

**Verdict: PARTIALLY-COMPLETE (2/4 inside sim CI); model INSUFFICIENT as specified.**

## Key interpretive insight
The failures concentrate on within-block L_path metrics. Pure 2-opt SA within classical blocks finds orderings ~7.9% SHORTER than the canonical mushaf. The mushaf is NOT the within-block FR-minimum — it accepts extra path length to preserve content-boundary integrity. This is the M1 "structural-hinges" sub-claim (H-NEW-130/130b's 15 top-jumps), which the simulator did NOT inject. The 6.31-unit gap matches cross-finding-020's ~7% residual estimate.

## Garden-of-forking-paths log
1. The locked SA hyperparameters (T_HOT=0.05, T_COLD=0.001, 200 iters) converge to tight local minima (sim std=0.09 on L_path). A HOTTER procedure would widen sim CI; this was NOT tried post-hoc to preserve pre-reg discipline.
2. Block boundaries locked as pre-reg § specifies: fatiha=Q1; tiwal=Q2-9; middle_pre_hm=Q10-39; hawamim=Q40-46; middle_post_hm=Q47-48; mufassal_long=Q49-77; mufassal_short=Q78-114. Alternative boundaries (Q 49-66 vs Q 50-77) not tested post-hoc; queued as H-NEW-236.2.
3. The block-χ² collapse of 3 block costs into one statistic was SPECIFIED in pre-reg to keep Bonferroni k=4 (rather than k=6). This is a TIGHTENING choice (combining 3 into 1 via sum-of-squared-z's loses orthogonal-information but preserves false-positive control); legitimate per project Bonferroni-tightening discipline.
4. The "INSIDE 95% CI" test was two-sided for O1/O2/O4 and one-sided (upper tail only) for O3 (χ²-like statistic). Specified in pre-reg §3.

## No specialist-judgment overrides
Pre-reg executed as specified. No method changes mid-run. Results written to `findings/phase-b-hypotheses/csv/h-new-236.json`.

## Next moves
- H-NEW-236.1: inject H-NEW-130 15 top-jumps as hinge constraints.
- H-NEW-236.2: rule-tuple sensitivity sweep on block boundaries.
- H-NEW-236.3: hotter SA (T_HOT=0.5) to widen within-block distribution.
- H-NEW-236.4: Q1-lock ablation.

## Files written
- `findings/phase-b-hypotheses/h-new-236-generative-simulator.md`
- `findings/phase-b-hypotheses/csv/h-new-236.json`
- `scripts/h_new_236_generative_simulator.py`

Bonferroni-family: k=4; α_bon=0.0125. All 4 observables evaluated under locked procedure; sim-passes=2/4; rand-passes=1/4. Primary verdict stable under Bonferroni tightening (all OUTSIDE failures are >10σ).
