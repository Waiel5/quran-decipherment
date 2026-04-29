---
id: H-NEW-690
title: "Pre-reg — Causal generative test of the compression-tail law (does compression-tail-alone produce mushaf-class TSP-residuals?)"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-660 (compression-tail law, R²=0.986) + cross-finding-011 (canonical mushaf is 11% above 2-opt TSP optimum, z=-11.46)
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260437
---

# [[h-new-690-causal-generative|H-NEW-690]] — Causal Generative Test of the Compression-Tail Law: Pre-Registration

## 1. Hypothesis

The compression-tail law ([[h-new-660-compression-tail-gradient|H-NEW-660]]) is a strong descriptive characterisation of canonical mushaf order. **Causal question:** is it sufficient to *generate* orderings whose Fisher-Rao TSP-residual matches canonical mushaf's ~11% ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]])?

If we constrain a generative simulator to produce orderings that respect the compression-tail law (and only that), do those orderings end up with mushaf-class FR-tour-lengths?

Three competing causal claims:
- **STRONG GENERATIVE.** Compression-tail is the dominant generative principle of mushaf-order; constrained ensemble should match or beat 11%.
- **DIRECTIONAL.** Compression-tail is a contributing principle but not sufficient; constrained ensemble is closer to 11% than random but does not match.
- **NULL.** Compression-tail is a mere statistical *consequence* of mushaf order, not its cause. Constrained ensemble has no special TSP-residual relationship.

## 2. Test design

### 2.1 Compression-tail constraint definition

For an ordering π ∈ S₁₁₄ (a permutation of {1, ..., 114}), define:
- For each window-start s ∈ {1, ..., 100}, the K=15 window contains surahs π[s−1], π[s], ..., π[s+13] (1-indexed s, 0-indexed array slice).
- Compute mean pairwise Fisher-Rao distance d̄(π, s) using the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D matrix.
- Fit two-piece-kink-50: d̄ = α + β · max(0, s − 50). Get (α, β, R²).

**Constraint:** ordering π RESPECTS the compression-tail law if:
- R² ≥ 0.95 AND
- β ∈ [−0.015, −0.010]

The [[h-new-660-compression-tail-gradient|H-NEW-660]] canonical fit gives R²=0.986, β=−0.0124, so the canonical mushaf passes this constraint comfortably.

### 2.2 Sampling procedure

Markov-chain Monte Carlo over permutations:
1. Initialize π₀ = a random permutation (seed 20260437).
2. At each step t:
   - Propose π' by swapping two random positions in π_t.
   - Compute (R²(π'), β(π'), L_FR(π')) where L_FR is the FR-tour-length (sum of consecutive distances).
   - Accept iff π' satisfies the compression-tail constraint AND with Metropolis-Hastings probability min(1, exp(−(L_FR(π') − L_FR(π_t)) / T)) where T=1.0 (encourages low TSP but does not enforce it).
   - If π_t does not yet satisfy the constraint (warm-up), accept any proposal that gets us strictly closer to constraint satisfaction (greedy on R² then on |β−(−0.0125)|), then switch to the MH rule once feasible.
3. Run for 10000 steps. Save 100 sampled orderings (every 100 steps after a 1000-step burn-in).
4. If the chain cannot find a feasible starting point in 5000 burn-in proposals, fall back to: start from canonical π_canonical = identity (which satisfies the constraint by construction), and run from there.

### 2.3 Locked simulation parameters
- Steps: 10000 (with 1000 burn-in).
- Saved orderings: 100, sampled every 100 steps post-burn-in.
- MH temperature: T=1.0 in FR-tour-length units (typical L scale ~85-105).
- Seed: 20260437.

If runtime exceeds 30 minutes, reduce to 2000 steps with 200 burn-in and 100 samples every 18 steps; document this in findings.

### 2.4 Comparison values (locked from prior work)

- L_canonical (mushaf) = 85.759656 (from [[h-new-111-fisher-rao-mushaf|h-new-111]].json).
- L_2opt (2-opt TSP upper bound) = 77.466858 (from [[h-new-111-fisher-rao-mushaf|h-new-111]].json).
- Canonical residual = (L_canonical − L_2opt) / L_2opt = 0.10705 = **10.71%**.
- Reference random-permutation null mean L ≈ 104.35 (from [[h-new-111-fisher-rao-mushaf|h-new-111]].json), random-residual mean ≈ 34.7%.

## 3. Pre-committed direction & verdicts

- **STRONG GENERATIVE**: ≥ 50% of 100 sampled orderings have TSP-residual ≤ 11.5%.
  → Compression-tail-alone reproduces mushaf-class TSP-optimality.
- **DIRECTIONAL**: ≥ 25% of sampled orderings have TSP-residual ≤ 12% (and STRONG fails).
  → Compression-tail is a contributing principle.
- **NULL**: < 10% of sampled orderings have TSP-residual ≤ 13%.
  → Compression-tail is a consequence, not a cause; mushaf has additional generative structure.
- **AMBIGUOUS**: any pattern between DIRECTIONAL and NULL (e.g., 10-25% at ≤13% but <25% at ≤12%) — report as INCONCLUSIVE; do not over-claim.

## 4. Bonferroni structure

We could in principle test linear/quadratic/two-piece forms of the constraint (3 forms). Per task brief, use only two-piece for simplicity; Bonferroni-3 → α_bon = 0.01667.

The pass/fail thresholds above are deterministic on percentile counts of a 100-ordering sample, not p-values; the Bonferroni applies to any auxiliary inferential test (e.g., one-sided z-test of "constrained-ensemble residual is below random-ensemble residual" — pre-locked to use α_bon=0.01667).

## 5. Predicted ranges (honest priors)

If compression-tail is causally dominant: median residual of constrained ensemble ≈ 8-13%.
If it's a partial signal: median residual ≈ 15-22%.
If it's a mere consequence: median residual ≈ 25-35% (random-class).

## 6. What would FALSIFY each claim

- STRONG: any sample shows median residual > 12% → falsified.
- DIRECTIONAL: median > 18% → falsified.
- NULL: median ≤ 14% → falsified (i.e., compression-tail does carry some generative signal).

## 7. Honest limits (locked before run)

- The two-piece-kink-50 constraint is one of many possible constraints derivable from [[h-new-660-compression-tail-gradient|H-NEW-660]]. We chose it because it is [[h-new-660-compression-tail-gradient|H-NEW-660]]'s *primary* model. Other constraints (linear, quadratic) might give different ensembles. We do NOT claim our constraint is unique.
- The MCMC may fail to mix well over the constrained subset of S₁₁₄; if acceptance rate < 1%, we report this and treat ensemble as non-representative.
- The MH temperature T=1.0 introduces a soft TSP-bias that makes the test conservative *toward* finding STRONG. If even with this bias we fail to reach STRONG, the negative result is robust.
- 100 saved orderings is a small sample; bootstrap CIs on percentiles will be reported.

## 8. Files

- Script: `scripts/h_new_690_causal_generative.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-690.json`
- Findings: `findings/phase-b-hypotheses/h-new-690-causal-generative.md`
- Journal: `journal/h-new-690-run-1.md`

## 9. Methodology rules

- MW-1: instrument-prior — FR-roots D matrix from [[h-new-111-fisher-rao-mushaf|h-new-111]].json (locked).
- MW-3: alternative-models — only two-piece per task brief; lin/quad implicitly Bonferroni-corrected.
- MW-7: post-hoc — N/A (this is a NEW pre-registered causal test).
- PRE-REG-STANDARD-04: hypothesis, constraint, simulation params, success criteria all locked.
- HONEST-NULL: NULL is reported with EQUAL prominence to STRONG/DIRECTIONAL.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
