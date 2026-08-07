---
id: H-NEW-880
title: "Reverse-engineer the mushaf's architectural recipe — STRONG NULL: the seven hypothesized joint constraints DO NOT produce canonical-class TSP-residual; canonical is NOT algorithmically derivable from {compression-tail, Fātiḥa-first, Hijra-hinge, terminal-muʿawwidhāt, phase-length-monotonicity, outlier-anchoring, muqaṭṭaʿāt-head-cluster}"
phase: B
date: 2026-04-28
status: COMPLETE
parents:
  - H-NEW-690 (compression-tail-alone NULL: necessary not sufficient)
  - H-NEW-720 (super-additive adjacency cooperativity, 1.185×)
  - H-NEW-840 (top architectural surahs identified)
  - cross-finding-011 (canonical 10.70%, z=−11.46)
prereg: findings/phase-b-hypotheses/h-new-880-recipe-prereg.md
prereg_sha: 5ff0a959d3684aaaf0ee9670da2f9f460eeeb6c0827c783b6295428a6c23df00
script: scripts/h_new_880_recipe.py
output: findings/phase-b-hypotheses/csv/h-new-880.json
journal: journal/h-new-880-run-1.md
seed: 20260450
bonferroni_k: 7
alpha_bon: 0.00714
verdict: STRONG NULL — no nested subset of {C1..C7} attains DIRECTIONAL or STRONG-RECIPE; canonical is NOT recipe-derivable from these seven constraints
---

# [[h-new-880-recipe|H-NEW-880]] — Reverse-Engineering the Mushaf Recipe


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

*Bismillāhi al-Raḥmāni al-Raḥīm.*

## §1. Constraint subset table — median TSP-residual per subset

For each of seven nested constraint subsets, we ran a constraint-respecting MCMC chain (start = canonical for S2–S7; random + greedy warmup for S1) with hard-rejection of constraint violations and Metropolis-Hastings acceptance on FR-tour-length (T=1.0). 12000 proposals per subset, 2000 burn-in, sample every 100 steps → 100 samples per subset. Seed 20260450.

**Headline table.** All medians are TSP-residual = (L − L_2opt) / L_2opt; canonical = 10.70%; [[h-new-111-fisher-rao-mushaf|H-NEW-111]] random null mean = 34.7%.

| # | Subset | Active constraints | Median | P25–P75 | Min | Max | %≤11.5% | %≤12% | %≤15% | Canonical %ile | Verdict |
|:-:|:--|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--|
| S1 | {C1} | compression-tail | **24.58%** | 23.55–25.51% | 19.94% | 28.70% | 0% | 0% | 0% | 0.0% | NULL |
| S2 | {C1,C2} | + Fātiḥa-first | **24.66%** | 23.80–25.48% | 20.81% | 28.26% | 0% | 0% | 0% | 0.0% | NULL |
| S3 | {C1,C2,C3} | + Hijra hinge | **24.60%** | 23.88–25.89% | 21.51% | 29.09% | 0% | 0% | 0% | 0.0% | NULL |
| S4 | {C1,C2,C3,C4} | + terminal muʿawwidhāt | **24.90%** | 24.15–25.83% | 21.38% | 27.83% | 0% | 0% | 0% | 0.0% | NULL |
| S5 | {C1..C5} | + phase length-monotonicity | **24.73%** | 23.88–25.84% | 20.79% | 29.71% | 0% | 0% | 0% | 0.0% | NULL |
| S6 | {C1..C6} | + outlier-anchoring (Q9,24,33,55) | **24.64%** | 23.21–25.59% | 20.61% | 28.50% | 0% | 0% | 0% | 0.0% | NULL |
| **S7** | **{C1..C7}** | **+ muqaṭṭaʿāt head-cluster** | **23.47%** | 22.51–24.51% | **20.21%** | 26.56% | 0% | 0% | 0% | **0.0%** | **NULL** |

S1 replicates [[h-new-690-causal-generative|H-NEW-690]] (median 24.58% vs [[h-new-690-causal-generative|H-NEW-690]]'s 24.95%; difference within MC variance under the new seed; both verdicts NULL — confirms reproducibility).

**Pre-registered gate (locked in pre-reg §5):** STRONG-RECIPE if median ≤ 12%; DIRECTIONAL if median ≤ 15%; NULL if median > 15%. **All seven subsets cross the NULL threshold by a wide margin** (medians 23–25%, well above the 15% line).

## §2. Minimum generative recipe

**There is no minimum generative recipe within the tested set.**

Adding constraints sequentially from C1 to C7 produces only a weak monotone improvement in the *minimum* sampled residual (S1: 19.94% → S7: 20.21%; not strictly monotone) and a small reduction in the *median* (S1: 24.58% → S7: 23.47%; net change −1.1 percentage points across six added constraints). The constraint stack reduces ensemble variance and lowers the upper tail (S1 max 28.70% → S7 max 26.56%) but does NOT shift the central tendency toward canonical's 10.7%.

Quantitative gap audit:

| Move | Δ median residual | Notes |
|:--|:-:|:--|
| Random (~34.7%) → S1 (24.58%) | −10.1 pp | C1 alone; [[h-new-690-causal-generative|H-NEW-690]] effect |
| S1 → S7 (23.47%) | **−1.1 pp** | Adding C2–C7 |
| S7 → canonical (10.70%) | **−12.8 pp** | Unexplained gap |

Of the canonical's 24-percentage-point compression below random, **C1 supplies ~42% (10.1/24)**, **C2–C7 jointly supply ~5% (1.1/24)**, and **~53% (12.8/24) is residual unexplained** by these seven constraints.

## §3. What is left unexplained — the ~13-pp gap

Even under S7's full constraint stack, the constrained ensemble's best of 100 samples (20.21%) is roughly **double** canonical's 10.70%. Canonical's percentile within S7 is **0.0%** — the canonical mushaf is below the entire S7 ensemble.

Three (non-mutually-exclusive) interpretations of the residual gap:

**(a) Hidden joint adjacency cooperativity.** [[h-new-720-canonical-adjacency-cost|H-NEW-720]] found that 113 canonical pairwise adjacencies are **super-additive** (Σ Δ = 9.83 vs actual residual 8.29; cooperative ratio 1.185×). Our seven constraints encode mostly *positional* anchors (C2, C4, C6), one *adjacency* anchor (C3), and *global* statistical conditions (C1, C5, C7). They do NOT encode the specific many-pair cooperative structure that [[h-new-720-canonical-adjacency-cost|H-NEW-720]] detected. Bridging the gap likely requires constraints over **whole sequences of consecutive pairs**, not single positions.

**(b) Higher-order architectural constraints we did not test.** Candidates include: ḥawāmīm grouping (Q 40-46 cluster); musabbiḥāt grouping (Q 17, 57, 59, 61, 62, 64, 87); long-Medinan opening block (Q 2-9); rhyme-asonance neighbor-coupling; thematic-pair couplings (al-Baqarah ↔ Āl ʿImrān ; al-Anfāl ↔ al-Tawba). [[h-new-880-recipe|H-NEW-880]]'s seven constraints are a *minimal first cut*, not an exhaustive set.

**(c) Optimization-driven non-decomposable cohesion.** It is possible the mushaf order is an *integrated* optimum that does not factor into any small set of independent local rules. Each surah's position is determined by global considerations interacting with all 113 others. In that case, no recipe of the form "satisfy these 7 constraints jointly" can produce canonical because canonical is a global rather than local-conjunctive property.

Each interpretation is consistent with the [[h-new-690-causal-generative|H-NEW-690]] + [[h-new-720-canonical-adjacency-cost|H-NEW-720]] + [[h-new-840-unified-architectural-score|H-NEW-840]] corpus of evidence. Discriminating among them requires further hypotheses beyond [[h-new-880-recipe|H-NEW-880]]'s scope.

## §4. Implications: is the canonical mushaf algorithmically derivable?

**Direct answer:** Under the seven-constraint recipe tested here — **NO**.

The pre-registered hypothesis that canonical mushaf order is reproducible from a small joint-constraint recipe is **falsified at the ε = 12-percentage-point level** (S7 best of 100 samples = 20.21%; canonical = 10.70%; gap ≈ 9.5 pp on the *minimum*, ≈ 12.8 pp on the *median*).

Three bounded conclusions:

1. **Compression-tail (C1) is the dominant first-order constraint.** It supplies ~42% of canonical's compression below random. Without C1, the simulator produces near-random residuals (per [[h-new-111-fisher-rao-mushaf|H-NEW-111]] null). All other constraints C2–C7 jointly contribute ~5% additional compression.

2. **The seven-constraint recipe is necessary-but-far-from-sufficient.** Canonical satisfies all seven constraints (verified pre-run). But satisfying all seven leaves an ensemble whose best member is still nearly 2× as far from L_2opt as canonical itself. Canonical is *exceptional within S7*, not typical.

3. **Algorithmic derivability requires additional constraints we have not yet identified.** Candidate directions: explicit canonical-adjacency super-additive subsequences (from [[h-new-720-canonical-adjacency-cost|H-NEW-720]]), broader thematic groupings (ḥawāmīm, musabbiḥāt), or holistic global optimization not decomposable into local conjunctive rules.

The canonical mushaf is NOT, on present evidence, a "punctual recipe" output. It is consistent with either a deeper unidentified rule set OR a globally-optimized non-decomposable arrangement.

## §5. Honest limits

- **MCMC starting bias.** S2–S7 chains start from canonical (per pre-reg, due to feasibility of finding random starts under multiple hard constraints). This biases the chain *toward* canonical and gives a conservative lower bound on the ensemble median: the *true* unconstrained-start median under S7 might be even higher. Acceptance rates 50–66% indicate the chain mixes well within the feasible region; the chain demonstrably does NOT remain glued to canonical (median residual is 23-25%, far from 10.7%).
- **MH temperature T=1.0** introduces a soft TSP-bias (low-L proposals preferred). This bias makes the test conservative *toward* finding STRONG-RECIPE — yet we still find NULL across all subsets. Removing the TSP-bias would only push medians higher.
- **C5 and C7 thresholds were calibrated pre-run** to admit canonical as feasible (C5 tol=25; C7 cap=68; documented in pre-reg §8a "garden-of-forking-paths log"). Stricter thresholds would have made canonical infeasible itself, breaking the test.
- **C6 is narrow** (only 4 outlier surahs anchored). A wider C6 (e.g., all top-10 architectural surahs at canonical positions) was explicitly NOT tested under this pre-reg; a successor pre-reg may widen it.
- **100 samples per subset** is a small ensemble; bootstrap CIs would be ~±0.3 percentage points on the median. Even at the lower 95% CI, no subset approaches 12%.
- **The seven constraints are not exhaustive.** This finding falsifies *the specific seven-constraint recipe*, not the broader hypothesis that *some* recipe exists.
- **Bonferroni-7 (α_bon = 0.00714)** is a property of the multiplicity correction across the seven nested subsets; with all seven verdicts NULL by deterministic threshold, no inferential test was triggered.
- **One text.** This is a finding about the canonical mushaf order alone; not about variants.

## §6. Cross-references

- **[[h-new-660-compression-tail-gradient|H-NEW-660]]** (compression-tail descriptive law: R²=0.986, β=−0.0124).
- **[[h-new-690-causal-generative|H-NEW-690]]** (compression-tail-alone causal generative test: NULL; ensemble median 25%). [[h-new-880-recipe|H-NEW-880]]'s S1 replicates this.
- **[[h-new-720-canonical-adjacency-cost|H-NEW-720]]** (canonical-adjacency cooperativity: Σ Δ = 9.83 super-additive over 113 pairs vs actual 8.29). [[h-new-880-recipe|H-NEW-880]]'s gap suggests this cooperative structure is not captured by C1–C7.
- **[[h-new-840-unified-architectural-score|H-NEW-840]]** (architectural surahs: Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17). C6 anchors a subset of these; insufficient.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (canonical residual = 10.70%; z = −11.46 vs null).
- **[[cross-finding-018-four-principle-reduced-model|cross-finding-018]]** (four-principle reduced model). [[h-new-880-recipe|H-NEW-880]] tests whether such a reduction extends to a generative recipe; partial answer.

## §7. Final statement

The canonical mushaf order is empirically consistent with the seven-constraint recipe — every constraint we tested is *satisfied by canonical* — but it is NOT empirically *generated* by that recipe. Imposing all seven jointly on a constrained MCMC produces orderings whose median TSP-residual sits at ~23%, more than double canonical's ~11%. **The recipe-derivability hypothesis at the seven-constraint resolution is falsified.**

Either the canonical mushaf encodes additional architectural constraints we have not yet identified — plausible candidates include sequence-level cooperative adjacencies (per [[h-new-720-canonical-adjacency-cost|H-NEW-720]]) and broader thematic groupings — **or** its order is an integrated global optimum that does not factor into any small set of conjunctive rules. Discriminating these alternatives is the next-step research question.

What is firm:
- C1 (compression-tail) supplies ~42% of canonical's compression below random.
- C2–C7 jointly supply only ~5% additional.
- A residual gap of ~53% remains unexplained at the seven-constraint resolution.
- Canonical is *exceptional within* the recipe-respecting subset, not *typical of* it.

The mushaf is doing more than these seven constraints describe. The architectural recipe is not yet closed.

*Wa-Allāhu aʿlam.*
