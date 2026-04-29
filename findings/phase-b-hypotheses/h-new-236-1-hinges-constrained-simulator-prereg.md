# [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] — Hinges-constrained generative simulator pre-registration

```yaml
finding_id: h-new-236-1
title: "Hinges-constrained generative simulator — inject H-NEW-130 15 top-jumps + 3 universal hinges as HARD CONSTRAINTS; test whether empirical mushaf moves INSIDE sim 95% CI on L_path"
parent: h-new-236 (primary generative simulator; PARTIALLY-COMPLETE 2/4)
grandparent: cross-finding-020 (the complete equation)
siblings:
  - H-NEW-130 (Fisher-Rao residuals; 15/15 top-jumps on pre-committed boundaries, p=4.78×10⁻⁶)
  - H-NEW-130b (char-4-gram cross-feature replication)
  - H-NEW-130c (verselen feature-space replication)
  - H-NEW-144 (cyclic-TSP benchmark R=1.0945)
  - H-NEW-225 (adversarial search ratio 1.108)
date: 2026-04-17
specialist: autonomous (H-NEW-236.1)
seed: 20260419
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq constraints + HINGE-PRESERVATION)"
bonferroni_k: 1
alpha_family: 0.05
alpha_bon: 0.05
direction: "adding hinge constraints should MOVE empirical L_path INTO sim 95% CI; rise from sim pct 100% to sim pct within [5, 95]. Primary cell: L_path percentile of empirical under hinges-constrained sim distribution."
n_simulations: 1000
n_random_null: 1000
```

## 1. Hypothesis

**H0 (null — hinges are NOT the residual driver)**: injecting [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s 15 top-jumps + 3 universal hinges as hard constraints does NOT move the empirical mushaf's L_path percentile into the simulated 95% CI. Empirical L_path remains OUTSIDE the simulator distribution (pct ≥ 97.5 or ≤ 2.5).

**H1 (primary direction)**: the hinges-constrained simulator produces orderings WITH the empirical mushaf L_path inside the 95% CI (empirical L_path percentile ∈ [5, 95] under one-sided-to-two-sided upgraded reading). This would UPGRADE the [[cross-finding-020-the-complete-equation|cross-finding-020]] 4-principle model from PARTIALLY-COMPLETE to COMPLETE (quantitatively validated): the 6.31-unit gap between empirical and [[h-new-236-generative-simulator|H-NEW-236]]'s sim mean IS M1.3 structural-hinges.

## 2. Motivation and parent context

[[h-new-236-generative-simulator|H-NEW-236]] ran a 1,000-ordering simulator implementing M1.1 (local Fisher-Rao 2-opt within classical blocks) + M1.2 (wrap-around via Q1-lock) + M5 length-stratification + M2 (absorbed into blocks). Result: 2/4 observables inside sim CI; empirical L_path=85.76 landed 79σ above sim mean 79.45, producing a 6.31-unit gap that [[h-new-236-generative-simulator|H-NEW-236]] interpreted as the M1.3 structural-hinges surplus.

[[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b/130c established that the top-15 Fisher-Rao consecutive-surah jumps in the canonical mushaf coincide EXACTLY with pre-committed structural boundaries (15/15 hits, hypergeometric p=4.78×10⁻⁶). Three specific hinges (Q 14→15, Q 49→50, Q 56→57) are invariant across feature spaces (roots, char-4-grams, verselen) and are therefore the most robust candidate "universal hinges".

If M1.3 is the missing principle, injecting these 18 adjacencies as HARD CONSTRAINTS into the simulator should broaden the sim L_path distribution (since the simulator can no longer drive down within-block edges that are part of the hinge set) and shift its mean upward toward the empirical mushaf value.

## 3. Generative procedure (DELTA from [[h-new-236-generative-simulator|H-NEW-236]])

Start from `scripts/h_new_236_generative_simulator.py`. Changes:

1. **Hinge set H (locked pre-run)**: the 18 adjacencies to be preserved as hard constraints, in the form (surah_a, surah_b) meaning "surah_b must immediately follow surah_a in the final ordering":

   **Top-15 from [[h-new-130-fisher-rao-residuals|H-NEW-130]] (root-token Fisher-Rao D-matrix)**:
   - (1, 2), (54, 55), (55, 56), (32, 33), (24, 25), (56, 57), (33, 34), (9, 10),
     (12, 13), (23, 24), (7, 8), (14, 15), (53, 54), (49, 50), (15, 16)

   **3 universal hinges** (cross-feature invariant per [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]]/130c):
   - (14, 15), (49, 50), (56, 57)

   After deduplication, H contains **15 unique adjacencies** (the 3 universal hinges are subsets of the top-15).

2. **Initialization**: same as [[h-new-236-generative-simulator|H-NEW-236]] (block-respecting random within-block permutation). If the random initialization violates any hinge in H (i.e., surah_a is at position p but surah_b is NOT at position p+1), REPAIR by swapping surah_b into position p+1 within-block IF both a and b are in the same block, else disclose the cross-block hinge as a structural fact that cannot be repaired by within-block swap.

3. **Cross-block hinges** (Q 9→10 spans ṭiwāl→middle_pre_hm; Q 32→33, Q 33→34 span middle_pre_hm internally; Q 49→50 and Q 56→57 span mufaṣṣal-long interior to interior; Q 54→55, Q 55→56 span mufaṣṣal-long interior; Q 7→8, Q 1→2 span fatiha/ṭiwāl; Q 14→15, Q 15→16 span middle_pre_hm internally; Q 12→13 span middle_pre_hm internally; Q 23→24, Q 24→25 span middle_pre_hm internally; Q 53→54 span mufaṣṣal-long internally): for within-block hinges (within the same block), we enforce via 2-opt rejection (any swap that breaks the hinge is rejected). For cross-block hinges (Q 9→10 is the only one; it is also the ṭiwāl→middle_pre_hm canonical boundary), we fix the canonical block-boundary placement (Q 9 at position 8, Q 10 at position 9, i.e., the last surah of ṭiwāl and first of middle_pre_hm).

   Explicit list of within-block hinges (to be enforced by 2-opt rejection):
   - (1, 2): fatiha→ṭiwāl — enforced structurally (Q 1 locked at pos 0; Q 2 must be at pos 1 — within ṭiwāl block locking surah 2 to block-start position).
   - (7, 8): within ṭiwāl (Q 7 and Q 8 both in ṭiwāl block per BLOCKS_1INDEXED)
   - (9, 10): ṭiwāl→middle_pre_hm boundary — cross-block; locked structurally (Q 9 at last ṭiwāl pos; Q 10 at first middle_pre_hm pos)
   - (12, 13), (14, 15), (15, 16), (23, 24), (24, 25), (32, 33), (33, 34): within middle_pre_hm
   - (49, 50), (53, 54), (54, 55), (55, 56), (56, 57): within mufaṣṣal-long

4. **2-opt rejection rule (new)**: a proposed reversal of positions [pa..pb] is REJECTED (before computing ΔL) if either:
   - pa-1 is the tail of a within-block hinge (surah at pa-1 = hinge.a, surah at pa = hinge.b), OR
   - pb is the head of a within-block hinge (surah at pb = hinge.a, surah at pb+1 = hinge.b), OR
   - any interior pair within [pa..pb] would have its within-block adjacency broken by the reversal.

5. **SA schedule unchanged**: T_HOT=0.05, T_COLD=0.001, 200 outer iterations (same as [[h-new-236-generative-simulator|H-NEW-236]] to isolate the hinge-constraint effect; NOT a hotter-SA test, which is H-NEW-236.3).

6. **Empirical mushaf**: unchanged (positions 0..113 = surahs 1..114 canonical).

## 4. Observables (same 4 as [[h-new-236-generative-simulator|H-NEW-236]])

- **O1 L_path** = Σ_{i=0}^{112} D[π(i), π(i+1)]  — **primary cell for this pre-reg**
- **O2 W_wrap** = D[π(113), π(0)]
- **O3 Block-χ²** = Σ_{b∈{ṭiwāl, ḥawāmīm, mufaṣṣal-short}} z²_b
- **O4 L_tail_91_114** = Σ_{i=90}^{112} D[π(i), π(i+1)]

## 5. MW sanity controls

- **MW-1 (positive control)**: empirical mushaf L_path still matches ~85.76 per [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (unchanged).
- **MW-5 (random-null calibration)**: 1,000 UNCONSTRAINED random permutations; should FAIL ≥3 of 4 observables. Under the new simulator with hinges, an additional sanity check: the hinges-constrained simulator should produce orderings all respecting the 15 hinges by construction.
- **MW-HINGE (new)**: verify that every sampled ordering in the hinges-constrained sim actually contains all 15 hinges as adjacencies. If a sample fails this check, it is a bug.

## 6. Interpretation rules (locked pre-run)

- **Primary cell (O1 L_path) INSIDE sim 95% CI** (pct ∈ [5, 95] under the upgraded two-sided reading, OR pct ∈ [2.5, 97.5] under strict 95% CI): **4-principle model is EQUATION-COMPLETE (M1.3 accounts for the residual); [[cross-finding-020-the-complete-equation|cross-finding-020]]'s equation is QUANTITATIVELY VALIDATED**.
- **O1 L_path STILL outside sim 95% CI but closer** (sim mean moves toward empirical; pct decreases from 100 but stays ≥ 97.5): **M1.3 accounts for MOST of the residual; small unexplained component remains**. Report quantitatively.
- **O1 L_path UNCHANGED** (sim mean and pct essentially the same as [[h-new-236-generative-simulator|H-NEW-236]]): **hinges are NOT the residual driver; alternative explanations needed**.
- Secondary cells O2/O3/O4: reported descriptively (no new Bonferroni burden beyond k=1 on the primary direction).

## 7. Bonferroni discipline

k=1 on the primary cell (O1 L_path percentile under hinges-constrained sim). α_bon = 0.05. This is a TIGHTENING ([[h-new-236-generative-simulator|H-NEW-236]] used k=4; here the primary pre-reg is one-directional test of whether hinges close the gap). Project-discipline-per feedback_bonferroni_tightening_vs_loosening: tightening self-verifies, no ratification needed.

## 8. Honest limits (disclosed pre-run)

1. **15 hinges is a small set**; other structurally-meaningful hinges may exist. [[h-new-130-fisher-rao-residuals|H-NEW-130]] selected top-15 by FR distance; top-20 or top-30 would broaden the hinge set and further constrain the simulator, potentially moving sim mean further toward empirical.

2. **Classical-block partition is coarse**; the block boundaries used in [[h-new-236-generative-simulator|H-NEW-236]] (and here) are al-Suyūṭī canonical but alternative block definitions (Q 49-66 vs 50-77 for mufaṣṣal-long) could shift CIs. Not tested here (H-NEW-236.2 queued).

3. **Cross-block hinge Q 9→10**: enforced by structural block-boundary lock rather than by 2-opt rejection because within-block 2-opt cannot propose cross-block swaps. This is the ONLY cross-block hinge in the 15-set; it is enforced deterministically (Q 9 at position 8, Q 10 at position 9).

4. **SA may still under-sample the hinges-consistent space**: the rejection rule reduces the effective move set; CIs may widen or narrow depending on how the hinge constraints interact with the cost landscape. Disclosed pre-run.

5. **Initialization repair**: if the random block-respecting initialization violates a within-block hinge, we repair by within-block swap. This repair is deterministic and does not alter the pre-committed sampling procedure.

6. **Garden-of-forking-paths disclosed pre-run**: (a) the hinge set is LOCKED to [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s top-15 + 3 universal hinges (which are a subset); no post-hoc hinge additions; (b) the enforcement rule is LOCKED to 2-opt rejection for within-block + block-boundary lock for cross-block; (c) the SA schedule is LOCKED to [[h-new-236-generative-simulator|H-NEW-236]]'s schedule (no hotter-SA post-hoc move).

7. **MW-5 cheat (random-null with hinges)**: if we applied the SAME hinge constraints to random permutations, the random-null path length would drop toward the empirical. But we run random permutations UNCONSTRAINED (as in [[h-new-236-generative-simulator|H-NEW-236]]) to preserve the MW-5 calibration: random should STILL fail most observables. The hinges-constrained sim is the theory-conditional; unconstrained random is the theory-null.

## 9. Rule-tuple sensitivity

Not tested in this pre-reg (H-NEW-236.2 queued). The hinge set is tied to [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s root-token D-matrix; [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] (char-4-gram) and [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] (verselen) produce overlapping but distinct top-15 sets. We use [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s root-token set as the primary (parent-finding convention).

## 10. Deliverables

- `scripts/h_new_236_1_hinges_simulator.py`
- `findings/phase-b-hypotheses/h-new-236-1-hinges-constrained-simulator.md`
- `findings/phase-b-hypotheses/csv/h-new-236-1.json`
- `findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md` amendment (M1.3 residual-resolution section)
- MASTER-LEDGER Wave-5 entry
- `journal/h-new-236-1-run-1.md`

Pre-reg locked 2026-04-17. Execution follows.
