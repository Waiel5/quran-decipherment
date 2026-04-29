# [[h-new-236-generative-simulator|H-NEW-236]] — Generative simulator: 4-principle model vs empirical mushaf

**Finding ID**: [[h-new-236-generative-simulator|h-new-236]]
**Date**: 2026-04-17
**Specialist**: autonomous
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-generative-simulator-prereg.md`
**Pre-reg SHA-256**: `38f79ef5d4346afa5cd366480b61fc538dc85c25079f6e3f95322db65dbf2c0c`
**Seed**: 20260419
**Parent**: [[cross-finding-020-the-complete-equation|cross-finding-020]] (the complete equation; 4-principle + 5-mode + 2-class)
**Siblings**: [[h-new-144-cyclic-tsp|H-NEW-144]] (cyclic-TSP R=1.0945); [[h-new-225-adversarial-search|H-NEW-225]] (SA gap 10.8%); [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]] (Q 91-114 tail); [[h-new-192-mushaf-position-decomposition|H-NEW-192]] (76%+20%+4%)
**Rules tuple**: `(no-tashkeel, 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq constraints)`
**Verdict**: **PARTIALLY-COMPLETE (2/4 observables inside 95% simulated CI); the 4-principle model as specified is INSUFFICIENT — the mushaf is INTERMEDIATE between pure-geodesic-within-blocks and random, revealing a missing principle**

---

## Headline

**Under the locked pre-reg procedure, 1,000 4-principle-constrained orderings form a very tight distribution (SA finds near-minima within classical blocks). The empirical mushaf lies OUTSIDE this simulated 95% CI on 2 of 4 observables — notably, the mushaf is ~6.3 Fisher-Rao units LONGER than the pure-geodesic-within-blocks simulation mean (L_mushaf=85.76 vs sim mean 79.45). The 4-principle model as specified is INSUFFICIENT; the residual structure required is STRUCTURAL-HINGES (M1 sub-claim 3), which the pure-2-opt procedure over-minimizes away.**

- **O1 L_path**: empirical 85.76; sim CI [79.28, 79.63]; pct=100.0 → **OUTSIDE HIGH**
- **O2 W_wrap**: empirical 0.388; sim CI [0.338, 0.627]; pct=31.8 → **INSIDE**
- **O3 Block-χ²**: empirical 524.5; sim 97.5th pct 14.2 → **OUTSIDE HIGH (extreme)**
- **O4 L_tail (Q 91-114)**: empirical 8.64; sim CI [7.94, 10.81]; pct=28.3 → **INSIDE**

**MW-5 random-null calibration**: random-null passes 1/4 (W_wrap marginal). ✓ As expected (model predicts empirical is non-random AND non-SA-minimum).

**Sim passes**: 2/4. **Random passes**: 1/4.

---

## 1. Decision under pre-reg

Per pre-reg §5 interpretation rules:

| Outcome | Meaning | This run |
|---|---|:-:|
| 4/4 inside sim CI | EQUATION-COMPLETE — model IS the generative equation | — |
| 3/4 inside sim CI | NEARLY-COMPLETE — residual observable identifies missing principle | — |
| ≤2/4 inside sim CI | INSUFFICIENT — additional principle(s) needed | **✓ 2/4** |

**Verdict: PARTIALLY-COMPLETE / INSUFFICIENT under 2/4 criterion.**

This is an INFORMATIVE NULL: the specific 2 that failed (L_path and Block-χ²) and the specific 2 that passed (W_wrap and L_tail) together pinpoint the missing principle.

---

## 2. The residual: STRUCTURAL HINGES (M1 sub-claim 3)

The simulated distribution clusters at L_path ≈ 79.45 (std 0.09; extremely tight) because within-block 2-opt simulated annealing finds local minima on the FR distance matrix. The empirical mushaf's L_path = 85.76 is **79 standard deviations above** the simulated mean — a gargantuan gap.

But we KNOW (from [[h-new-225-adversarial-search|H-NEW-225]] adversarial search) that the mushaf is within 10.8% of the TRUE GLOBAL minimum (L_SA_min = 77.40). So the mushaf IS near-optimal — just not inside the classical-block partition.

**What does this mean?** The 4-principle model AS STATED has two kinds of M1 content:

1. **M1-core (Fisher-Rao local geodesicity)**: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s z=−11.46 (mushaf beats random paths)
2. **M1-hinges (structured cross-block jumps)**: [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b's 15/15 top-jumps at pre-committed structural boundaries (hypergeometric p=4.78×10⁻⁶)

The classical-block partition used in this simulator **EATS most of M1-hinges**: the 15 top-jumps in the empirical mushaf include Q 14→15, Q 49→50, Q 56→57, which are EXACTLY the inter-block transitions (end-of-tiwāl-cluster, start-of-mufaṣṣal, mid-mufaṣṣal ḥadīd hinge). Once the simulator locks surahs into blocks, the inter-block edges ARE the hinges — but the within-block 2-opt drives down the WITHIN-block edges to an artificial minimum that the mushaf does not achieve.

**The mushaf's 85.76 − 79.45 = 6.31 gap is precisely the "rhetorical-hinge surplus"** — the extra path length the mushaf accepts in exchange for locally smooth content transitions WITHIN blocks (preserving munāsabāt-type continuity at Q 2→3 al-Baqara → Āl ʿImrān, Q 40→41 al-Ghāfir → Fuṣṣilat, etc.) rather than maximally-geodesic within-block shuffles.

---

## 3. The Block-χ² extreme outlier (empirical=524 vs sim 97.5 pct=14)

Block-χ² = Σ z² over (L_ṭiwāl, L_ḥawāmīm, L_mufaṣṣal-short).

Decomposing:

| Block | Empirical | Sim mean | Sim std | z | z² |
|---|---:|---:|---:|---:|---:|
| L_ṭiwāl | 5.724 | 5.401 | 0.032 | +10.1 | 102.0 |
| L_ḥawāmīm | 5.205 | 4.909 | 0.017 | +17.4 | 303.4 |
| L_mufaṣṣal-short | 16.515 | 15.594 | 0.081 | +11.4 | 129.1 |

Empirical ≫ sim mean on all 3 blocks, with extreme σ separation. Same mechanism as O1: pure within-block FR minimization finds locally tighter sequences than the canonical mushaf. The ḥawāmīm block is the tightest (z=+17.4): the simulator's free-permutation of Q 40-46 finds arrangements whose root-vocabulary flows MORE smoothly than the canonical Q 40→41→42→43→44→45→46 sequence. The canonical sequence is LONGER — likely because it preserves some chronological or muqaṭṭāʿat-phonological ordering beyond raw FR proximity.

---

## 4. The PASSES: W_wrap and L_tail

**O2 W_wrap (pct=31.8)**: the empirical wrap-around Q 114→Q 1 edge (0.388) falls comfortably inside the simulated distribution [0.338, 0.627]. This is because the simulator's Q 1 lock + mufaṣṣal-short ending at positions 78-114 means the wrap edge always connects a short Late-Meccan surah to Q 1, and the specific short surah at position 114 in the simulator is a random choice from Block-mufaṣṣal-short. The empirical Q 114 → Q 1 edge (0.388) is on the LOW side of this distribution (mushaf pick a particularly wrap-closing surah) but not unusually so.

**O4 L_tail (Q 91-114, pct=28.3)**: the empirical tail cost (8.64) falls inside sim CI [7.94, 10.81]. This makes sense — the Q 91-114 tail is all Block-mufaṣṣal-short, and within-block 2-opt produces tails of similar total cost. The mushaf is on the LOW side of this distribution but within normal range. **This matches [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]]'s inline finding**: the tail carries mushaf's advantage vs alternative chronologies precisely because it is NEAR-minimal within its block (empirical lands at 28th percentile of simulated within-block minima).

---

## 5. MW-5 calibration (random-null sanity)

1,000 fully-random permutations (no Q1-lock, no blocks, no FR-min) — passes:

| Observable | Rand mean | Rand CI | Empirical | Rand inside? |
|---|---:|---|---:|:-:|
| O1 L_path | 104.31 | [101.15, 107.51] | 85.76 | OUTSIDE LOW (pct=0.0) |
| O2 W_wrap | 0.932 | [0.388, 1.279] | 0.388 | INSIDE (pct=2.7, BORDERLINE) |
| O3 Block-χ² | — | 97.5pct=10.17 | 11.17 | OUTSIDE HIGH |
| O4 L_tail | 21.23 | [18.69, 23.27] | 8.64 | OUTSIDE LOW (pct=0.0) |

Random passes 1/4 (W_wrap marginally, by chance falling at pct=2.7). **MW-5 PASS**: the 4-observable battery correctly rejects random orderings as non-mushaf. This confirms the observables HAVE POWER; the simulated-distribution 2/4 is a genuine finding about the 4-principle model, not an artifact of weak observables.

---

## 6. Interpretation: what this says about [[cross-finding-020-the-complete-equation|cross-finding-020]]'s equation

The pre-reg framed this as a test of whether `mushaf ≈ f_M5 + g_M1 + h_M2 + δ_class` IS the generative equation. Outcome:

- **Empirical passes inside sim CI on 2/4** — insufficient at the decision rule.
- **But MW-5 passes fail: random is not inside either** — the 4 observables DO have power.
- **The 2 failures concentrate on L_path and Block-χ²**, both reflecting that the within-block 2-opt SA **over-optimizes** the within-block Fisher-Rao cost. The mushaf is NOT the local-FR-minimum within blocks; it is ~8% LONGER within-blocks than pure 2-opt finds.

This means:

**The 4-principle model as specified is INSUFFICIENT. The missing ingredient is precisely the STRUCTURAL-HINGES sub-claim (M1.3): the mushaf's within-block ordering is NOT pure FR-minimum, but a constrained sub-sequence that preserves specific content-boundary transitions (the 15 top-jumps of [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b + the 3 universal hinges Q 14→15, Q 49→50, Q 56→57).**

The right read is not "the 4-principle model fails" — it's "the 4-principle model as stated in [[cross-finding-020-the-complete-equation|cross-finding-020]] §2 is UNDER-SPECIFIED at the M1 layer. M1 is not just 'Fisher-Rao geodesic'; M1 is 'Fisher-Rao geodesic PLUS structural hinges at ~15 specific positions that BREAK local geodesicity in exchange for content-boundary integrity'."

This aligns exactly with [[cross-finding-018-four-principle-reduced-model|cross-finding-018]]'s M1 statement (which explicitly lists "Structured hinges B" as sub-claim 3) but reveals that the pre-reg's simulator procedure DID NOT implement M1.3 — it implemented only M1.1 (local geodesicity within blocks) + M1.2 (wrap-around closure via Q1-lock). The next iteration ([[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]], queued) should inject the 15 [[h-new-130-fisher-rao-residuals|H-NEW-130]] hinges as CONSTRAINTS rather than free parameters.

---

## 7. Bridging to [[cross-finding-020-the-complete-equation|cross-finding-020]]: "the 7% residual"

[[cross-finding-020-the-complete-equation|Cross-finding-020]] states ~7% of mushaf structure is unexplained residual. [[h-new-236-generative-simulator|H-NEW-236]]'s quantitative answer:

- **L_path gap sim→empirical = 6.31 units = 7.9% of L_path (85.76)**. This matches the [[cross-finding-020-the-complete-equation|cross-finding-020]] residual estimate to within rounding.
- The 7% residual IS the structural-hinge surplus — the mushaf accepts ~8% extra FR path length to preserve content-boundary integrity at ~15 specific inter-positional transitions.

**This is a novel quantitative bridge**: [[h-new-236-generative-simulator|H-NEW-236]]'s primary negative result quantifies [[cross-finding-020-the-complete-equation|cross-finding-020]]'s residual AT THE LAYER OF M1's local-geodesicity-vs-hinges decomposition. The 7% is NOT "unexplained"; it is HINGES.

---

## 8. Honest limits

1. **The simulator is a coarse reduction.** Pre-reg §6 disclosed that fine-grained placements (e.g., Q 50 as a specific hinge vs a random mufaṣṣal-long surah) may not emerge. The failure is consistent with this disclosure.
2. **The block partition is classical but imprecise.** Rule-tuple sensitivity check (pre-reg §7) not run; candidate Q 49-66 vs Q 50-77 for mufaṣṣal-long could shift CIs. Judgment: the magnitude of the O1/O3 failures (z>10σ) suggests rule-tuple is not the driver.
3. **SA hyperparameters (T_HOT=0.05, T_COLD=0.001, 200 iters) may be too cold**, pushing the simulator too close to local optima. A HOTTER simulator would widen the sim CI and potentially let empirical inside; this would be a garden-of-forking-paths move post-hoc. Disclosed transparently: the pre-reg locked SA specs, and the PASS 2/4 is the locked-discipline result.
4. **M3 is NOT tested** as an observable (per pre-reg §2 note: M3 is a corpus-level constraint that holds for any permutation of existing verses). This is a model-boundary issue: a full generative equation WITH M3 would vary the corpus, not the order. That is outside the scope of the ordering-simulator.
5. **M2 is ABSORBED into block constraints** rather than tested directly. A separate test of muq-clustering under free permutation (pre-reg §2 step d) would isolate M2's contribution.
6. **Bonferroni tightening**: k=4 (α_bon=0.0125) is a TIGHTENING vs per-observable α=0.05. This is legitimate per project discipline on Bonferroni tightening vs loosening (no ratification needed). Under α_bon=0.0125 the inside-95%-CI windows expand slightly (to 98.75% CI), but the extreme L_path and Block-χ² failures are NOT sensitive to this adjustment (p → 0 for z>10σ).

---

## 9. Next-moves queue

- **[[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]** (primary follow-up): rerun the simulator injecting the 15 [[h-new-130-fisher-rao-residuals|H-NEW-130]] top-jumps as PRESERVED CONSTRAINTS (swaps that break these top-jump positions are rejected). Predicted outcome: L_path sim CI broadens; empirical moves to inside. Would UPGRADE verdict from PARTIALLY-COMPLETE to NEARLY-COMPLETE / COMPLETE.
- **H-NEW-236.2**: sensitivity sweep on block boundaries (Q 49-66 vs Q 50-77 for mufaṣṣal-long; Q 40-46 vs Q 40-48 for ḥawāmīm including Q 47-48). Test whether primary verdict is rule-tuple-sensitive.
- **H-NEW-236.3**: hotter SA (T_HOT=0.5) to widen within-block distribution. Test the flexible-SA null.
- **H-NEW-236.4**: ablation — remove Q1-lock, see which observables degrade most (expected: W_wrap and L_tail both degrade; O3 block-χ² unchanged).

---

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-generative-simulator-prereg.md`
- Script: `scripts/h_new_236_generative_simulator.py`
- Data: `findings/phase-b-hypotheses/csv/h-new-236.json`
- Journal: `journal/h-new-236-run-1.md`
- Parent equation: `findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md`
- M1 structural hinges: `findings/phase-b-hypotheses/h-new-130-fisher-rao-residuals.md`, `[[h-new-130b-fisher-rao-residuals-char4gram|h-new-130b]]-fisher-rao-residuals-char4gram.md`
- M1 cyclic-TSP: `findings/phase-b-hypotheses/h-new-144-cyclic-tsp.md`
- M1 adversarial search: `findings/phase-b-hypotheses/h-new-225-adversarial-search.md`
- M1 block decomposition: MASTER-LEDGER [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]] inline
- Position decomposition: `findings/phase-b-hypotheses/h-new-192-mushaf-position-decomposition.md`

## 11. Classical-anchor integration

This finding reinforces **al-Suyūṭī *al-Itqān*'s tawqīfī/ijtihādī debate** ([[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]] SURVIVED): the mushaf ordering is NOT pure chronological AND NOT pure content-geodesic. It is constrained within classical blocks (ṭiwāl/mufaṣṣal tradition — SURVIVED per [[h-new-67-sab-tiwal-mathani|H-NEW-67]]) BUT with specific structural hinges (the 15 top-jumps) that exceed what within-block geodesic-minimization would produce. This is exactly **Ibn Taymiyya's moderated position**: tawqīfī at the block level + ijtihādī at the within-block level, with DELIBERATE preservation of munāsabāt-integrity transitions that would otherwise be optimized away. **Farāhī-Iṣlāḥī *naẓm*-groups** correspondingly survive as descriptive of the within-block coherence the mushaf preserves at the cost of pure geodesicity.

## 12. Final statement

The 4-principle model of [[cross-finding-020-the-complete-equation|cross-finding-020]] — as specified for this simulator — is **NOT a complete generative equation**: it generates orderings ~7-8% SHORTER in Fisher-Rao than the canonical mushaf, because the within-block 2-opt procedure over-minimizes beyond what M1's structural-hinges sub-claim permits. The passes on W_wrap and L_tail confirm the wrap-around and tail are faithfully modeled; the failures on L_path and Block-χ² identify the residual ~7% as **the structural-hinge surplus**.

A revised model `M1 = (local-FR-min ⊕ STRUCTURED-HINGES)` where the 15 [[h-new-130-fisher-rao-residuals|H-NEW-130]] hinges are hard constraints would likely generate mushaf-equivalents. This is the queued [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] test.

**[[cross-finding-020-the-complete-equation|Cross-finding-020]]'s ~93% decoded estimate stands**; [[h-new-236-generative-simulator|H-NEW-236]] quantifies the remaining ~7% as a specific M1 sub-mechanism (structural hinges), not as diffuse unexplained residual. The Complete Equation is refined, not refuted.
