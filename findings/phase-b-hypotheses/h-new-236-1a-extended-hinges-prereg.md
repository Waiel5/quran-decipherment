# [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] — Extended hinges-constrained simulator pre-registration

```yaml
finding_id: h-new-236-1a
title: "Extended hinges (top-30 + top-50) constrained generative simulator — test whether extending the hinge set closes the residual 27% L_path gap from H-NEW-236.1"
parent: h-new-236-1 (PARTIAL-CLOSURE; 73% of 4-principle residual closed; remaining R12 concentrates in ḥawāmīm + mufaṣṣal-short)
grandparent: h-new-236 → cross-finding-020 (the complete equation)
siblings:
  - H-NEW-130 (Fisher-Rao residuals; 15/15 top-jumps on pre-committed boundaries, p=4.78×10⁻⁶)
  - H-NEW-130b (char-4-gram cross-feature replication)
  - H-NEW-130c (verselen cross-feature replication)
  - H-NEW-144 (cyclic-TSP benchmark R=1.0945)
  - H-NEW-225 (adversarial search ratio 1.108)
  - H-NEW-236 (primary generative simulator; 2/4 verdict)
date: 2026-04-17
specialist: autonomous (H-NEW-236.1a)
seed: 20260419
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq constraints + TOP-K-HINGE-PRESERVATION for K ∈ {30, 50})"
bonferroni_k: 2
alpha_family: 0.05
alpha_bon: 0.025  # tightening: each hinge-extension cell independently tested
cells:
  - cell_a_top30: extend hinge set to top-30 Fisher-Rao jumps; test whether empirical L_path enters sim 95% CI AND all 4 observables PASS; direction — top-30 should close ≥95% of H-NEW-236.1's residual 1.73 units (i.e. sim-to-empirical gap ≤ 0.087)
  - cell_b_top50: extend hinge set to top-50 Fisher-Rao jumps; test the same; direction — top-50 should close ≥99% of residual (gap ≤ 0.017) and produce empirical INSIDE sim 95% CI AND all 4 observables PASS
n_simulations: 1000
n_random_null: 1000
```

## 1. Hypothesis

**H0 (null — residual R12 is NOT captured by extending hinges)**: Extending the hinge set to [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s top-30 or top-50 jumps does NOT materially close the remaining 1.73-unit L_path gap identified in [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]. The ḥawāmīm and mufaṣṣal-short within-block cost-excess (z²=100.7 and 133.9 respectively) persists; the residual 27% gap is NOT pure hinge-truncation but reflects a different mechanism.

**H1 cell A (top-30 closure)**: Extending to top-30 hinges closes ≥ 95% of [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]'s residual 1.73-unit gap on L_path (new gap ≤ 0.087 units). Empirical L_path percentile enters the sim 95% CI. L_ḥawāmīm z² drops below 5 (from 100.7). All 4 observables PASS.

**H1 cell B (top-50 closure)**: Extending to top-50 hinges closes ≥ 99% of residual (new gap ≤ 0.017 units). All 4 observables PASS. Both L_ḥawāmīm and L_mufaṣṣal-short z² drop below 5.

Per the protocol interpretation rules:
- **Top-30 closure → EQUATION-COMPLETE at top-30**. [[cross-finding-020-the-complete-equation|Cross-finding-020]]'s causal-generative layer CONFIRMED.
- **Top-30 partial, top-50 complete → EQUATION-COMPLETE at top-50**.
- **Top-50 still outside → residual R12 is NOT pure hinge-truncation; deeper mechanism needed (5th principle / M1.4)**.

## 2. Motivation and parent context

[[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] established that injecting [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s top-15 jumps as hard constraints closes 73% of the 4-principle simulator's L_path residual (gap 6.31 → 1.73 units; z-score 79σ → 5.5σ). The remaining 27% (1.73 units) concentrates in:
- **L_ḥawāmīm** (Q 40-46): z = +10.04, z² = 100.7
- **L_mufaṣṣal-short** (Q 78-114): z = +11.57, z² = 133.9

Both blocks contain **ZERO [[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 hinges** — the first ḥawāmīm internal edge (Q 42→43) is rank 16; the first mufaṣṣal-short internal edge (Q 78→79) is rank 73.

**Cell A predicts**: Top-30 adds Q 42→43 (rank 16, within-ḥawāmīm) and Q 46→47 (rank 17, ḥawāmīm→middle_post_hm boundary). This should close L_ḥawāmīm's within-block cost-excess.

**Cell B predicts**: Top-50 adds 4 more ḥawāmīm internal edges (Q 41→42 rank 47; Q 43→44 rank 43; Q 44→45 rank 48; Q 40→41 rank 50). With Q 45→46 at rank 58 (just outside), top-50 should fully constrain ḥawāmīm's internal ordering. However, top-50 includes **zero mufaṣṣal-short internal edges** (earliest is Q 78→79 at rank 73). So top-50 is predicted to close ḥawāmīm but NOT mufaṣṣal-short.

**Theoretical implication**: If top-50 closes ḥawāmīm but not mufaṣṣal-short, the residual R12 is NOT purely hinge-truncation but has a block-specific driver (mufaṣṣal-short has a different mechanism — possibly phonological-rhyme continuity per [[h-new-234-q55-unified-profile|H-NEW-234]]/188, or refrain-parallelism).

## 3. Pre-computation (locked pre-run)

Top-50 Fisher-Rao consecutive-edge ranks in canonical mushaf (computed from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D-matrix, SHA-verified via [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]'s load_d_matrix function). Top-30 = rows 1-30; top-50 = rows 1-50.

**Block distribution by rank**:

| Rank range | within-tiwal | within-middle_pre_hm | within-ḥawāmīm | within-middle_post_hm | within-mufaṣṣal_long | within-mufaṣṣal_short | cross-block |
|:---|---:|---:|---:|---:|---:|---:|---:|
| Top-15 | 1 | 7 | 0 | 0 | 5 | 0 | 2 |
| Top-16-30 | 0 | 12 | 1 | 0 | 2 | 0 | 0 |
| Top-31-50 | 2 | 8 | 4 | 1 | 4 | 0 | 2 |
| Top-50 total | 3 | 27 | 5 | 1 | 11 | 0 | 4 |

**Critical observation locked pre-run**: mufaṣṣal-short has ZERO internal edges in the top-50. The first mufaṣṣal-short internal edge is Q 78→79 (rank 73). Consequently, top-50 CANNOT directly constrain mufaṣṣal-short internal ordering. If L_mufaṣṣal-short z² fails to drop under top-50, this is NOT surprising under the hinge-truncation hypothesis — it would require extending the hinge set to rank 73+ (more than half of all 113 edges constrained).

**Honest disclosure pre-run**: the "top-50 closes mufaṣṣal-short" prediction is WEAK. If top-50 closes ḥawāmīm but not mufaṣṣal-short, we interpret this as PARTIAL-GENERATIVE: hinges capture ḥawāmīm's structure but mufaṣṣal-short has a non-hinge mechanism.

## 4. Generative procedure (DELTA from [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]])

Start from `scripts/h_new_236_1_hinges_simulator.py`. Changes:

1. **Hinge set H_K (locked pre-run)** — two cells:
   - **H_30**: top-30 Fisher-Rao consecutive-edge pairs in canonical mushaf (see §3 table).
   - **H_50**: top-50 pairs.

2. **Cross-block vs within-block classification (locked pre-run)**:
   - **Cross-block hinges** (enforced by initialization structural lock):
     - Q 1→2, Q 9→10 (same as [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]])
     - Q 46→47 (added in top-30): ḥawāmīm→middle_post_hm boundary — Q 46 at last ḥawāmīm position (45 in 0-indexed); Q 47 at first middle_post_hm position (46).
     - Q 48→49 (added in top-50, rank 46): middle_post_hm→mufaṣṣal_long boundary — Q 48 at last middle_post_hm position (47); Q 49 at first mufaṣṣal_long position (48).
   - **Within-block hinges** (enforced by 2-opt rejection): all others.

3. **Chain construction**: identical to [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]'s `build_hinge_chains_for_block`. All top-30 and top-50 within-block hinges are consecutive in canonical mushaf, so they form contiguous runs within their blocks (e.g., within ḥawāmīm under top-50: Q40→41→42→43→44→45 is a chain of length 6, leaving only Q46 as a standalone singleton; under the cross-block Q46→47 lock, Q46 is at block-end).

4. **SA schedule unchanged**: T_HOT=0.05, T_COLD=0.001, 200 iterations. Same rationale as [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] (isolate the hinge-extension effect; NOT a hotter-SA test).

5. **N_sim=1000; N_random=1000; seed=20260419** (identical to [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] for direct comparability).

6. **MW-HINGE**: verify all 1000 orderings respect all K hinges by construction (separately per cell).

## 5. Observables (same 4 as [[h-new-236-generative-simulator|H-NEW-236]] and [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]])

- **O1 L_path** = Σ_{i=0}^{112} D[π(i), π(i+1)] — **PRIMARY cell** per each K
- **O2 W_wrap** = D[π(113), π(0)]
- **O3 Block-χ²** = Σ_{b∈{ṭiwāl, ḥawāmīm, mufaṣṣal-short}} z²_b
- **O4 L_tail_91_114** = Σ_{i=90}^{112} D[π(i), π(i+1)]

## 6. Interpretation rules (locked pre-run)

For each cell K ∈ {30, 50}:

| Outcome | Verdict |
|---|:---|
| Empirical L_path INSIDE sim 95% CI AND all 4 obs PASS | **EQUATION-COMPLETE at top-K**: CF-020 causal-generative layer CONFIRMED; report closure % |
| Empirical INSIDE [5, 95] relaxed AND 4/4 PASS | **NEARLY-COMPLETE at top-K** |
| Empirical OUTSIDE but gap < 0.5 units from sim mean | **NEAR-PARTIAL-CLOSURE**: hinges capture most residual; small unexplained component |
| Empirical OUTSIDE with gap ≥ 0.5 units | **RESIDUAL-R12-PERSISTS**: hinge-truncation is NOT the mechanism; 5th-principle / M1.4 needed |

**Progression test**: compare top-15 → top-30 → top-50 closure %. If each extension roughly proportionally closes more of the gap, the extrapolation suggests the residual is enumeration-bounded. If extensions plateau (top-30 and top-50 similar), the residual is mechanism-bounded (block-internal structure not captured by FR top-K ranking).

## 7. Bonferroni discipline

**k=2** (top-30 and top-50 as separate cells); α_bon = 0.025 per cell. This TIGHTENS vs [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]'s k=1. Per project-discipline: TIGHTENING self-verifies, no ratification needed.

## 8. Honest limits (disclosed pre-run)

1. **Top-50 approaches the saturation limit**: with 113 consecutive edges in canonical mushaf, constraining 50 of them means 44% of the path is hinge-locked. The "generative" claim weakens as K grows: at K=113, the simulator would be a perfect reproduction trivially. The strength of [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]'s top-15 result was that 13% of edges sufficed to close 73% of the residual.

2. **If top-50 produces EQUATION-COMPLETE**: this is meaningful but qualified. It means "constraining the 50 largest FR jumps + 4-principle model + classical blocks → mushaf-equivalent orderings." Classical-anchor reading: the 50 hinges ARE al-Biqāʿī's munāsabāt (pre-committed content-boundary pivots).

3. **Mufaṣṣal-short prediction**: top-50 contains ZERO mufaṣṣal-short internal edges. L_mufaṣṣal-short z² is predicted to remain elevated under top-50, refuting the strict hinge-truncation hypothesis for that block. This is disclosed pre-run.

4. **Classical-block boundaries**: unchanged from [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] (al-Suyūṭī ṭiwāl/mufaṣṣal). Rule-tuple sensitivity queued as H-NEW-236.2.

5. **Initialization repair**: if random initialization violates any hinge, repair by within-block swap. Deterministic; does not alter sampling procedure.

6. **Garden-of-forking-paths disclosed pre-run**:
   - The two cells (K=30, K=50) are LOCKED; no intermediate K swept post-hoc.
   - The hinge set for each K is LOCKED to top-K FR consecutive-edge ranking on the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] root-token D-matrix (same parent D-matrix as [[h-new-130-fisher-rao-residuals|H-NEW-130]]).
   - Enforcement rule LOCKED: cross-block = initialization lock; within-block = 2-opt rejection.
   - SA schedule LOCKED (same as [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]).

7. **MW-5 calibration preserved**: unconstrained random permutations are run at N=1000 for MW-5 sanity (unchanged from [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]).

## 9. Deliverables

- `scripts/h_new_236_1a_extended_hinges.py`
- `findings/phase-b-hypotheses/h-new-236-1a-extended-hinges.md`
- `findings/phase-b-hypotheses/csv/h-new-236-1a.json`
- `findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md` §12.7 (new generative-verdict section)
- MASTER-LEDGER Wave-5 entry
- `journal/h-new-236-1a-run-1.md`

Pre-reg locked 2026-04-17. Execution follows.
