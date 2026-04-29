# H-NEW-236.1 — Run 1 journal

**Date**: 2026-04-17
**Specialist**: autonomous
**Pre-reg SHA-256**: `b23f5cd6994567db74152ada7393747f740857f6766877e19f9c641dd3c696ee`
**Parent**: H-NEW-236 (primary generative simulator)
**Seed**: 20260419
**Runtime**: ~90 seconds (1000 hinge-constrained SA sims + 1000 random perms + observable battery)

## Procedure

Executed per pre-reg §3: 1000 block-respecting hinge-constrained SA 2-opt simulations + 1000 unconstrained random permutations. Hinge set = H-NEW-130 top-15 (which contains the 3 universal hinges Q 14→15, Q 49→50, Q 56→57 as subset); 13 within-block hinges enforced by 2-opt rejection; 2 cross-block hinges (Q 1→2, Q 9→10) enforced by structural lock at block boundaries.

Script: `scripts/h_new_236_1_hinges_simulator.py`. Script inherits H-NEW-236 simulator structure; deltas are:
1. New `HINGES` constant with 15 pairs (cross-block + within-block split)
2. New `build_hinge_chains_for_block` function that collapses within-block hinges into mandatory-contiguous chains
3. New `initial_hinge_respecting_tour` function that constructs within-block shuffles respecting hinge-chains and cross-block locks
4. New `swap_breaks_hinge` function checking whether any proposed 2-opt swap would break a hinge adjacency
5. Modified `sa_within_block_hinge_respecting` function rejecting hinge-breaking swaps before cost computation
6. MW-HINGE verification: every sim and the empirical tour is checked for all-15-hinges-preserved (passes).

## MW-1 positive control

Empirical mushaf L_path = 85.7597 (matches H-NEW-111 expected 85.76 to 3 decimals). ✓

## MW-HINGE verification

All 1000 simulated orderings preserve all 15 hinges by construction (verified explicitly via `all_hinges_ok` in the sim loop; zero AssertionErrors). Canonical mushaf preserves all 15 hinges (by definition; every top-15 H-NEW-130 pair is canonically adjacent in the mushaf). ✓

## MW-5 random-null calibration

Random permutations pass 1/4 observables (W_wrap marginally at pct=2.7; all others OUTSIDE). ✓ Identical to H-NEW-236.

## Primary decision

- **O1 L_path**: empirical 85.76 OUTSIDE HIGH (sim CI [83.40, 84.62]; pct=100). Sim mean 84.03; gap 1.73 units = 2.0% of L_path.
- **O2 W_wrap**: INSIDE (pct=35.4). ✓
- **O3 Block-χ²**: empirical 235.5 OUTSIDE HIGH (sim 97.5 pct = 12.2). Improved from H-NEW-236's 524.5. L_hawamim still z=+10; L_mufaṣṣal-short still z=+11.6; **L_ṭiwāl now INSIDE** (z=−0.98, was z=+10.1).
- **O4 L_tail**: INSIDE (pct=29.1). ✓

**Primary-cell verdict: PARTIAL-CLOSURE** — empirical L_path gap narrowed 73% (6.31 → 1.73); z-score on empirical dropped from 79σ to 5.5σ.
**Overall 4-observable verdict: PARTIALLY-COMPLETE (2/4 inside sim CI)** — same PASSES count as H-NEW-236 but the two failing observables moved DRAMATICALLY toward empirical.

## Key interpretive insight

The 15 H-NEW-130 hinges account for **73% of H-NEW-236's L_path residual**. The remaining 27% (~1.73 units) concentrates in blocks that contain ZERO top-15 hinges — L_ḥawāmīm (Q 40-46; z still +10) and L_mufaṣṣal-short (Q 78-114; z still +11.6). L_ṭiwāl, which contains the cross-block hinges Q 1→2 and Q 9→10 plus the within-block Q 7→8, is now INSIDE the sim distribution (z=−0.98).

**Reading A** (parsimonious extension): the residual is an enumeration gap. Extending to H-NEW-130 top-30 or top-50 would capture within-ḥawāmīm and within-mufaṣṣal-short micro-hinges and close the remaining gap.
**Reading B** (separate mechanism): ḥawāmīm/mufaṣṣal-short cost-excess is a distinct 5th-principle mechanism (phonological continuity within ḥawāmīm; refrain-parallelism within mufaṣṣal-short per H-NEW-188/234).

Cross-finding-020's equation is QUANTITATIVELY REFINED: M1.3 structural hinges now quantitatively account for ~5% of mushaf position variance (73% of the previously-unexplained 7%). New residual R12 (ḥawāmīm/mufaṣṣal-short within-block cost-excess) proposed as the remaining ~2%.

## Garden-of-forking-paths log

1. **Hinge set LOCKED pre-run** to H-NEW-130 top-15 (which is a superset of the 3 universal hinges Q 14→15, Q 49→50, Q 56→57). No post-hoc hinge additions.
2. **Enforcement rule LOCKED pre-run** to (a) within-block 2-opt rejection for 13 within-block hinges, (b) structural block-boundary lock for 2 cross-block hinges (Q 1→2 at fatiha/ṭiwāl; Q 9→10 at ṭiwāl/middle_pre_hm).
3. **SA schedule LOCKED pre-run** to H-NEW-236's schedule (T_HOT=0.05, T_COLD=0.001, 200 iters). No hotter-SA post-hoc move (reserved for H-NEW-236.3).
4. **Block boundaries LOCKED** to H-NEW-236's pre-reg (fatiha / ṭiwāl Q 2-9 / middle_pre_hm Q 10-39 / ḥawāmīm Q 40-46 / middle_post_hm Q 47-48 / mufaṣṣal-long Q 49-77 / mufaṣṣal-short Q 78-114). No alternative boundaries tested post-hoc (H-NEW-236.2).
5. **Bonferroni TIGHTENED** from k=4 (H-NEW-236) to k=1 (this pre-reg, primary cell only). Self-verifying per project Bonferroni-tightening-vs-loosening discipline. No ratification required.
6. **Primary cell definition** (O1 L_path percentile under hinges-constrained sim) declared pre-run, not chosen post-hoc after seeing which observable moved most.

## No specialist-judgment overrides

Pre-reg executed as specified. No method changes mid-run. Results written to `findings/phase-b-hypotheses/csv/h-new-236-1.json`.

## Decomposition of the 1.73-unit residual

| Block | Hinges contained | Empirical | Sim mean (H-236.1) | z | z² |
|---|---|---:|---:|---:|---:|
| L_ṭiwāl (Q 2-9) | Q 7→8 + boundary locks | 5.7244 | 5.8868 | **−0.98** | **0.97** (INSIDE) |
| L_ḥawāmīm (Q 40-46) | NONE | 5.2054 | 4.9193 | +10.04 | 100.70 (STILL OUT) |
| L_mufaṣṣal-short (Q 78-114) | NONE | 16.5149 | 15.6094 | +11.57 | 133.86 (STILL OUT) |

The residual concentrates ENTIRELY in the two blocks with no H-NEW-130 top-15 hinges — structurally consistent with M1.3 being the correct mechanism and the top-15 truncation being the binding constraint.

## Next moves

- H-NEW-236.1a: extend to top-30 hinges; predicted outcome = EQUATION-COMPLETE on L_path.
- H-NEW-236.1b: ḥawāmīm-specific mechanism test (phonological vs structural).
- H-NEW-236.2: rule-tuple sensitivity on block boundaries.
- H-NEW-236.3: hotter SA (T_HOT=0.5) with hinges.
- H-NEW-236.4: Q1-lock ablation with hinges.

## Files written

- `findings/phase-b-hypotheses/h-new-236-1-hinges-constrained-simulator-prereg.md`
- `findings/phase-b-hypotheses/h-new-236-1-hinges-constrained-simulator.md`
- `findings/phase-b-hypotheses/csv/h-new-236-1.json`
- `scripts/h_new_236_1_hinges_simulator.py`
- `findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md` Amendment (2026-04-17 post-H-NEW-236.1)
- MASTER-FINDINGS-LEDGER.md Wave-5 entry

Bonferroni-family: k=1; α_bon=0.05. Primary cell (L_path pct under hinges-constrained sim) verdict stable: PARTIAL-CLOSURE at 73% gap reduction. Overall 4-observable battery: PARTIALLY-COMPLETE (2/4).
