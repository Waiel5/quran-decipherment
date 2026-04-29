# [[h-new-236-generative-simulator|H-NEW-236]] — Generative simulator pre-registration

```yaml
finding_id: h-new-236
title: "Generative simulator — sample 1,000 4-principle-constrained orderings, compare to empirical mushaf on 4 observables"
parent: cross-finding-020 (the complete equation; 4-principle + 5-mode + 2-class)
siblings:
  - cross-finding-018 (4-principle reduced model)
  - H-NEW-144 (cyclic-TSP benchmark R=1.0945)
  - H-NEW-225 (adversarial search ratio 1.108)
  - H-NEW-230 (block-decomposition; Q 91-114 tail carries mushaf's advantage)
  - H-NEW-192 (mushaf position decomposition; 76%+20%+4%)
date: 2026-04-17
specialist: autonomous (H-NEW-236)
seed: 20260419
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq constraints)"
bonferroni_k: 4
alpha_family: 0.05
alpha_bon: 0.0125
direction: "empirical mushaf should lie within 95% simulated-distribution CI on ALL 4 observables"
n_simulations: 1000
n_random_null: 1000
```

## 1. Hypothesis

**H0 (null of equation-completeness)**: the 4-principle model (M1 Fisher-Rao geodesic + M2 Late-Meccan muqaṭṭāʿat clustering + M3 prosodic hard-constraint / Q 1 lock + M5 length-stratification with classical blocks) is a COMPLETE generative equation for the 114-surah mushaf ordering. If so, the empirical mushaf should lie WITHIN the 95% CI of simulated orderings on all 4 observables.

**H1 (null of equation-failure)**: the 4-principle model is INCOMPLETE. The empirical mushaf lies OUTSIDE the 95% CI on ≥1 of 4 observables.

## 2. Generative procedure

For each of 1,000 simulated orderings:

1. **(a) Compositional-feature seeding**: each of 114 surahs carries its classical-block membership:
   - **Block-Fātiḥa** (Q 1; singleton; Class B per [[h-new-155-q1-sui-generis|H-NEW-155]])
   - **Block-ṭiwāl** (Q 2-9; 7 longest + Q 9 associated — al-sabʿ al-ṭiwāl per [[h-new-67-sab-tiwal-mathani|H-NEW-67]])
   - **Block-middle** (Q 10-48; the pre-mufaṣṣal mid-mushaf)
   - **Block-ḥawāmīm** (Q 40-46; muqaṭṭāʿat ḥā-mīm cluster; overlaps with Block-middle)
   - **Block-mufaṣṣal-long** (Q 49-77; approximate long-mufaṣṣal per classical al-Suyūṭī)
   - **Block-mufaṣṣal-short** (Q 78-114; short-mufaṣṣal)

2. **(e) P3/Q-1 hard constraint**: Q 1 al-Fātiḥa locked at position 1 (2-class refinement; prayer-frame).

3. **(c) M5 length-stratification**: enforce block-rank partial ordering:
   - Block-Fātiḥa at position 1
   - Block-ṭiwāl in positions 2-9 (allow interior permutation within block)
   - Block-middle in positions 10-48
   - Block-ḥawāmīm stays inside Block-middle (positions 40-46 nominal)
   - Block-mufaṣṣal-long in positions 49-77
   - Block-mufaṣṣal-short in positions 78-114

4. **(d) M2 muq-clustering**: muqaṭṭāʿat-opened surahs should remain clustered consistent with their Late-Meccan / early-Medinan chronology bins. Since the classical-block partition already achieves this (alif-lām-mīm cluster concentrates at Q 2-7 front-ṭiwāl; ḥā-mīm cluster at Q 40-46 middle; short-muq singletons Q 50/68/38 in mufaṣṣal-long), we treat M2 as ABSORBED into the block constraints. No separate re-assignment required.

5. **(b) M1 Fisher-Rao minimization (2-opt relaxation)**: within the block-partition, perform stochastic 2-opt on the Fisher-Rao D-matrix. Swaps that violate block-partition (move a surah outside its block) are rejected. Stochastic: accept a proposal with probability 1 if ΔL < 0, else with probability exp(−ΔL/T) (simulated-annealing) with T decreasing from 0.05 to 0.001 over 200 iterations per simulation. Each simulation starts from a random within-block permutation (seed = 20260419 + k).

## 3. Observables

For each simulated + empirical ordering, compute:

**O1. Fisher-Rao path length L_path** = Σ_{i=1}^{113} D[π(i), π(i+1)]
**O2. Wrap-around edge W** = D[π(114), π(1)]
**O3. Per-block tour cost** reported as 3 numbers (L_ṭiwāl, L_ḥawāmīm, L_mufaṣṣal-short) [combined into multivariate one-observable via Mahalanobis rank]
**O4. Q 91-114 tail cost** = Σ_{i=91}^{113} D[π(i), π(i+1)] (the mushaf's winning edge per [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]])

**Bonferroni family**: k=4 (one test per observable); α_bon = 0.0125.
**Decision rule per observable**:
- INSIDE 95% CI (simulated percentile 2.5-97.5): observable PASS (empirical within model distribution)
- OUTSIDE on LOW side (empirical < 2.5th pct): model over-constrains; empirical is MORE optimal than generative
- OUTSIDE on HIGH side (empirical > 97.5th pct): model under-constrains; empirical is WORSE than generative on this axis

## 4. MW sanity controls

- **MW-1 (positive control)**: empirical mushaf L_path and W match prior literature values (L_path = 85.76 ± 0.5 per [[h-new-111-fisher-rao-mushaf|H-NEW-111]]; wrap_edge ≈ 0.37 per [[h-new-137-wrap-around-closure|H-NEW-137]]/138).
- **MW-5 (random-null calibration)**: draw 1,000 UNCONSTRAINED random permutations of 114 surahs (Q 1 free to float). This RANDOM-NULL should FAIL ≥3 of 4 observables (model predicts empirical is NON-RANDOM). If random-null mistakenly PASSES on most observables, the observables themselves lack power.

## 5. Interpretation rules (locked pre-run)

- **All 4 within 95% CI**: EQUATION-COMPLETE. The 4-principle model IS the generative equation for mushaf-equivalents.
- **3/4 within 95% CI**: NEARLY-COMPLETE. The missing observable identifies the residual principle. Report which and interpret.
- **≤2/4 within 95% CI**: INSUFFICIENT. Additional principle(s) required.

## 6. Honest limits

- The generative procedure is a COARSE reduction. Fine-grained single-surah placements (e.g., Q 50 as a specific Qāf hinge, Q 114 as absolute tail) may or may not emerge.
- The 2-opt Fisher-Rao minimization uses within-block swaps only — this is a structural simplification of the full 4-term optimization of [[cross-finding-020-the-complete-equation|cross-finding-020]] §2.3. A full joint optimization with λ weights fit to data would be tighter but would leak mushaf information via the weight-fitting step.
- M3 (prosodic niche) is a corpus-level HARD CONSTRAINT that holds for any permutation of existing verses (verse-length distribution is permutation-invariant). It is therefore NOT directly testable as an ordering observable; we treat M3 as satisfied by construction.
- Bonferroni tightening is applied (k=4). If loosening were required it would not be (per project discipline on Bonferroni tightening vs loosening).

## 7. Rule-tuple sensitivity

Block boundaries are classical but imprecise. Sensitivity analysis (if time): re-run with alternative block boundaries — mufaṣṣal-long could be Q 49-66 or Q 50-77 depending on al-Suyūṭī vs al-Bāqillānī. If primary decision reverses under alternative blocks, disclose as rule-tuple-sensitive.

## 8. Deliverables

- `scripts/h_new_236_generative_simulator.py`
- `findings/phase-b-hypotheses/h-new-236-generative-simulator.md` (findings + observable percentiles + equation-complete verdict + residual analysis)
- `findings/phase-b-hypotheses/csv/h-new-236.json` (per-simulation results)
- MASTER-LEDGER Wave-4 entry
- `journal/h-new-236-run-1.md`

Pre-reg locked 2026-04-17. Execution follows.
