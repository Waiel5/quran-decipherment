---
id: H-NEW-880
title: "Pre-reg — Reverse-engineer the canonical mushaf's architectural recipe (minimal joint-constraint subset producing canonical-class TSP-residual)"
phase: B
date_committed: 2026-04-28
hypothesis_origin:
  - H-NEW-690 (compression-tail-alone is NECESSARY but NOT SUFFICIENT — constrained median 25%, canonical 11%)
  - H-NEW-720 (113 canonical adjacencies are super-additive: Σ Δ = 9.83 vs actual 8.29 → 1.185× cooperative)
  - H-NEW-840 (top architectural surahs: Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17)
  - cross-finding-011 (canonical residual = 10.70%; z = −11.46 vs random)
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260450
---

# [[h-new-880-recipe|H-NEW-880]] — Mushaf Recipe: Minimal Joint-Constraint Set: Pre-Registration


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Hypothesis

[[h-new-690-causal-generative|H-NEW-690]] demonstrated that the compression-tail law (C1) alone moves the constrained-ensemble median TSP-residual from random (≈34.7%) to ≈25%, leaving canonical (≈10.7%) far below the entire constrained ensemble. **The mushaf is doing multiple things at once.** The hypothesis tested here:

> The canonical mushaf's TSP-optimality is the joint product of a small, identifiable set of **independent** architectural constraints. When applied together in a generative simulator, this minimal recipe produces orderings within ε of canonical's 11% residual.

This is a forward test: rather than asking "is canonical exceptional?" we ask "what minimal recipe makes canonical typical?"

## 2. The seven candidate constraints (locked, ordered)

Each constraint is a property an ordering π ∈ S₁₁₄ either satisfies or does not. They are tested in the **locked nesting order** below (each row adds one constraint to the previous):

| Code | Name | Definition | Source |
|:-:|:--|:--|:--|
| **C1** | compression-tail | Window-K=15 mean FR distance: d̄(s) ≈ 0.96 − 0.012·max(0, s−50). Operationalized: R²(two-piece-kink-50 fit) ≥ 0.95 AND β ∈ [−0.015, −0.010]. | [[h-new-660-compression-tail-gradient|H-NEW-660]]/690 |
| **C2** | al-Fātiḥa first | π[0] = 1 (Q 1 at position 1, 1-indexed: position 1). | classical |
| **C3** | Hijra hinge adjacency | positions of Q 56 and Q 57 differ by exactly 1 (i.e., adjacent in ordering). | classical / Nöldeke |
| **C4** | terminal muʿawwidhāt | Q 113 at position 113 AND Q 114 at position 114. | classical |
| **C5** | length-monotonicity within Nöldeke phases | Within each Nöldeke phase {Early Meccan, Middle Meccan, Late Meccan, Medinan}, surahs in the ordering have at most **25 adjacent length-inversions** (canonical baseline: Early=20, Medinan=6, Late=7, Middle=8). Tolerance set just above canonical's worst phase to ensure canonical narrowly satisfies; permits weak monotonicity rather than strict. | [[h-new-840-unified-architectural-score|H-NEW-840]] / classical |
| **C6** | architectural-outlier placement | Q 33 at canonical position 33; Q 9 at canonical position 9; Q 24 at canonical position 24; Q 55 at canonical position 55. | [[h-new-840-unified-architectural-score|H-NEW-840]] |
| **C7** | muqaṭṭaʿāt head-cluster | All 29 muqaṭṭaʿāt-bearing surahs occur within positions 1..**68** in the ordering (canonical baseline: max muqaṭṭaʿāt position is Q 68 al-Qalam at position 68). | classical |

**Note on C6.** C6 is intentionally narrow (4 specific surahs at their canonical positions). Wider variants (all top-10 architectural surahs anchored) are explicitly NOT tested under this pre-reg; if [[h-new-880-recipe|H-NEW-880]] fails, a successor pre-reg may widen C6.

**Note on C7 muqaṭṭaʿāt list (29 surahs).** Locked from classical (al-Suyūṭī, *al-Itqān* §40):
{2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}

## 3. Locked subset-search order (Bonferroni-7)

The seven nested subsets to evaluate, in this exact order:

| # | Subset | Description |
|:-:|:--|:--|
| S1 | {C1} | replicate [[h-new-690-causal-generative|H-NEW-690]] (sanity check) |
| S2 | {C1, C2} | + Fātiḥa anchor |
| S3 | {C1, C2, C3} | + Hijra hinge |
| S4 | {C1, C2, C3, C4} | + terminal muʿawwidhāt |
| S5 | {C1, C2, C3, C4, C5} | + phase-length monotonicity |
| S6 | {C1, C2, C3, C4, C5, C6} | + architectural-outlier anchoring |
| S7 | {C1, C2, C3, C4, C5, C6, C7} | + muqaṭṭaʿāt head-cluster |

**Bonferroni-7:** α_bon = 0.05 / 7 = **0.00714**.

## 4. Sampling procedure (for each subset)

Markov-chain over permutations with hard-constraint rejection:

1. **Initialization.** Start from canonical ordering π_canonical = [1, 2, ..., 114] (which by inspection satisfies C1, C2, C3, C4, and partially the others — needed because finding feasible random starts under C2-C7 is intractable). For S1, the procedure replicates [[h-new-690-causal-generative|H-NEW-690]] from random + greedy-warmup.
2. **Proposal.** At each step, propose π' by random adjacent **2-opt** (reverse a random subsequence of length 2..10), or swap (50/50).
3. **Hard-constraint rejection.** π' is rejected outright if ANY of the active constraints fail.
4. **MH on FR-tour-length.** If π' satisfies all active constraints, accept with probability min(1, exp(−(L(π') − L(π))/T)), T = 1.0.
5. **Burn-in.** 2000 steps. **Sampling.** every 100 steps for 10000 post-burn-in steps → up to 100 samples.
6. **Per-subset budget.** 12000 total proposals max. If runtime > 5 min for any single subset, halve N_steps.

For each subset, report:
- Median TSP-residual of collected samples.
- P25, P75, min, max.
- % of samples at ≤ 11.5%, ≤ 12%, ≤ 13%, ≤ 15%.
- Canonical's percentile in the subset's ensemble.
- Acceptance rate, n samples collected.

## 5. Pre-committed direction & verdicts

For each subset Sk (k = 1..7), classify based on **median TSP-residual of the constrained ensemble**:

- **STRONG-RECIPE** (subset matches canonical): median ≤ 12% → this subset is the minimal generative recipe.
- **DIRECTIONAL** (subset is on the path): 12% < median ≤ 15%.
- **NULL** (subset is insufficient): median > 15%.

The **minimal generative recipe** is the smallest k such that Sk attains STRONG-RECIPE.

If NO subset achieves STRONG-RECIPE: report the smallest k achieving DIRECTIONAL as the **partial recipe**, and quantify the residual gap.

If NO subset achieves DIRECTIONAL beyond S1: the recipe-derivability hypothesis is **FALSIFIED** — the canonical mushaf is NOT algorithmically derivable from the seven candidate constraints jointly.

## 6. Bonferroni structure

Seven subsets tested → **α_bon = 0.05 / 7 = 0.00714**.

For per-subset inferential tests (e.g., one-sided test that subset's median is below [[h-new-690-causal-generative|H-NEW-690]]'s NULL median of ~25%), we use α_bon. Pass/fail thresholds in §5 are **deterministic on percentile counts** of a 100-ordering sample, not p-values; the Bonferroni applies to any auxiliary inferential test.

If any subset Sk attains STRONG-RECIPE, we additionally test (post-hoc, flagged) whether dropping any single constraint from Sk degrades it back to NULL — a **necessity audit** of each component.

## 7. Predicted ranges (honest priors)

| Subset | Predicted median (prior) | Rationale |
|:-:|:-:|:--|
| S1 | 24-26% | replicates [[h-new-690-causal-generative|H-NEW-690]] |
| S2 | 22-25% | C2 fixes 1 of 114 positions; small effect expected |
| S3 | 20-25% | C3 fixes 1 adjacency; small effect |
| S4 | 18-23% | C4 fixes 2 positions at end; small effect |
| S5 | 14-20% | length-monotonicity is a strong global constraint |
| S6 | 12-18% | C6 fixes 4 outlier positions; [[h-new-720-canonical-adjacency-cost|H-NEW-720]] super-additivity suggests joint effect |
| S7 | 10-15% | C7 head-anchors muqaṭṭaʿāt; predicted to close the gap |

If S7's median ≤ 12%: the recipe is **closed** (canonical is algorithmically derivable from these seven constraints).
If S7's median > 15%: there is a substantive **architectural residual** unexplained by these seven constraints.

## 8. What would FALSIFY the recipe-closure hypothesis

If the median residual of the largest tested subset (S7) is > 15%, then the seven constraints are jointly insufficient and additional unidentified architectural principles must exist.

## 8a. Pre-run calibration log (garden-of-forking-paths discipline)

This pre-reg was first drafted with C5 tolerance = 5 inversions and C7 cap = position 50. Pre-run sanity check (executed BEFORE chain runs, on canonical only) revealed canonical does NOT satisfy these as drafted: canonical has 20 inversions in Early Meccan phase and Q 68 al-Qalam (a muqaṭṭaʿāt surah) sits at canonical position 68. As drafted, S5–S7 would have INFEASIBLE-START (the chain cannot even initialize from canonical), making the test unrunnable.

**Calibration:** C5 tolerance set to 25 (max canonical inversion + 5); C7 cap set to position 68 (max canonical muqaṭṭaʿāt position). These are the **minimum** values that admit canonical as feasible. The constraints are now operationalized as "as monotonic as canonical" and "as head-clustered as canonical" — i.e., they encode canonical-level structure rather than stricter idealized structure. This is conservative for the recipe-derivation hypothesis: looser constraints mean the chain has MORE freedom to escape canonical, not less.

This calibration was performed BEFORE any chain runs (verified by SHA recalculation; new SHA replaces draft SHA in script `EXPECTED_PREREG_SHA`).

## 9. Honest computational limits (locked before run)

- The constraint graph for C2-C7 is highly restrictive. Acceptance rate may collapse below 1% under S6 and S7. If acceptance rate < 0.5% for any subset, we report the chain as **non-mixing** and flag results as preliminary.
- Starting from canonical biases the chain toward canonical; this is a conservative bias for testing *minimality* of the recipe (the chain has every opportunity to escape canonical and rarely does — this itself is informative).
- The MH temperature T=1.0 introduces a soft TSP-bias. As in [[h-new-690-causal-generative|H-NEW-690]] this is **conservative toward STRONG**: passing under this bias does NOT prove the recipe constraints alone produce canonical-class residual without TSP guidance.
- 100-sample ensembles per subset: bootstrap CIs reported.
- We do NOT exhaustively test all 2^7 = 128 subsets; only the 7 nested subsets as locked.

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-880-recipe-prereg.md`
- Script: `scripts/h_new_880_recipe.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-880.json`
- Findings: `findings/phase-b-hypotheses/h-new-880-recipe.md`
- Journal: `journal/h-new-880-run-1.md`

## 11. Methodology rules

- MW-1: instrument-prior — FR-roots D matrix from [[h-new-111-fisher-rao-mushaf|h-new-111]].json (locked).
- MW-3: alternative-models — only the seven locked constraints; wider C6 variants NOT tested under this pre-reg.
- MW-7: post-hoc — per-component necessity audit only if a STRONG-RECIPE is found, flagged as post-hoc.
- PRE-REG-STANDARD-04: hypothesis, constraint set, simulation params, success criteria all locked.
- HONEST-NULL: NULL is reported with EQUAL prominence to STRONG/DIRECTIONAL.
- Bonferroni: 7-fold across seven subsets, α_bon = 0.00714.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
