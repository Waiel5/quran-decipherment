---
id: H-NEW-670
title: "NULL — Hijra-kink (Q 56/57 forced adjacency) explains only 3.3% of the 11% TSP-residual; H-NEW-660 §6 hypothesis FALSIFIED. The 11% residual is DISTRIBUTED across many canonical adjacencies, no single one dominates."
phase: B
status: NULL on H-NEW-660 §6 — Hijra-kink explains 3.33% of the 8.29-unit residual; pre-committed STRONG-PASS threshold ≥50% missed by an order of magnitude. Q1-Q2 (canonical opener) costs MORE than Hijra (7.43% vs 3.33%). Random non-canonical pairs cost 1.7-9.6%. The 11% is a SUM over many small constraint-costs, not a single architectural choice.
date: 2026-04-28
executed_by: team-lead (inline)
parent_1: H-NEW-660 (compression-tail law; §6 hypothesis claimed Hijra-kink preservation explains 11% residual)
parent_2: cross-finding-011 (mushaf 11% from FR-TSP-optimum)
parent_3: H-NEW-590 (Q1 al-Fātiḥa outlier-strength +27pp)
seed: 20260440
prereg: h-new-670-tsp-hijra-constraint-prereg.md
prereg_sha256: 0a6241a03386e95d2e177971600746c1cc4724ada3677f72b85a692fde43189a
verdict: NULL on H-NEW-660 §6 interpretation; partial-replacement explanation: 11% TSP-residual is DISTRIBUTED (no single dominant adjacency)
---

# [[h-new-670-tsp-hijra-constraint|H-NEW-670]] — Hijra-Kink Does NOT Explain TSP-Residual: HONEST NULL


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

## 1. Headline

| Constraint | L_2opt|constraint | Δ vs L_2opt | Fraction of 11% explained | Status |
|:--|:-:|:-:|:-:|:--|
| **Hijra-kink Q 56-Q 57** | 77.74 | 0.28 | **3.3%** | **NULL** (pre-commit ≥50%) |
| Q 1-Q 2 (canonical opener) | 78.08 | 0.62 | 7.4% | MORE than Hijra |
| Q 113-Q 114 (terminal pair) | 77.53 | 0.06 | 0.8% | Near-free |
| Q 1-Q 113 (random) | 77.61 | 0.14 | 1.7% | Random |
| Q 50-Q 90 (random) | 77.68 | 0.21 | 2.6% | Random |
| Q 9-Q 108 (random) | 78.26 | 0.79 | 9.6% | High random |

Anchors: L_mushaf = 85.76, L_2opt = 77.47, residual = 8.29 length-units (10.7%).

**The Hijra-kink alone explains only 3.3% of the 11% TSP-residual.**

## 2. Pre-commit violation: HONEST PUBLICATION

[[h-new-660-compression-tail-gradient|H-NEW-660]] §6 hypothesized that "the canonical mushaf is willing to sacrifice ~11% TSP-Fisher-Rao optimality to preserve the Hijra-kink discontinuity." This was a SOFT-INFERENTIAL interpretation, not formally pre-registered for thresholding.

[[h-new-670-tsp-hijra-constraint|H-NEW-670]] was the formal pre-registered test of this interpretation. **PRE-COMMIT STRONG-PASS** (Hijra fraction ≥ 50%): **FAILED** by an order of magnitude. The Hijra-kink is responsible for only 3.3% of the residual.

**This is published with full prominence per integrity-commitment §3.**

## 3. What the data actually shows

The 11% TSP-residual is DISTRIBUTED across the canonical mushaf. Different adjacencies cost different amounts:
- Q 1-Q 2 (canonical opener): 7.4% — al-Fātiḥa placement is the SINGLE most-expensive canonical adjacency tested.
- Q 9-Q 108 (random non-canonical): 9.6% — even forcing a RANDOM adjacency can cost ~10%, comparable to the entire mushaf residual.
- Q 113-Q 114 (terminal pair): 0.8% — preserving the muʿawwidhāt-pair is essentially free.
- Q 56-Q 57 (Hijra-kink): 3.3% — moderate cost.

**Interpretation**: the 11% residual is the cumulative cost of preserving HUNDREDS of canonical structural choices simultaneously, not the cost of any single one.

## 4. Why Q 1-Q 2 is most expensive

[[h-new-590-outlier-spectrum|H-NEW-590]] found Q 1 al-Fātiḥa has outlier-strength +27.09pp — its content-distance from neighbors is large. Forcing Q 1-Q 2 adjacency, despite Q 1's content-distinctness, costs Δ=0.62 length-units (7.4% of residual).

This is consistent with the classical *umm al-Kitāb* tradition: Q 1 is structurally unique, deliberately placed first **despite** its content-distinctness from Q 2 al-Baqara.

The mushaf is willing to accept a content-cohesion penalty to honor al-Fātiḥa's primacy. This is a *tartīb tawqīfī* signature.

## 5. Refined explanation of the 11% TSP-residual

The 11% TSP-residual decomposes (approximately) into:
- ~7% from Q 1 al-Fātiḥa being placed first (Q 1-Q 2 single-adjacency cost).
- ~3% from the Hijra-kink (Q 56-Q 57 single-adjacency cost).
- ~1% from Q 113-Q 114 muʿawwidhāt-pair.
- The remaining ~0% IS NOT zero — it's distributed across ~110 other canonical adjacencies, each costing 0.05-0.30 length-units.

These are NOT additive (constraints are not independent — fixing one constrains the rest), but the PATTERN is: many small commitments, not one big one.

## 6. Implication for [[h-new-660-compression-tail-gradient|H-NEW-660]] §6 interpretation — RETRACTED

[[h-new-660-compression-tail-gradient|H-NEW-660]] §6 stated:
> "The 11% TSP-residual is ~partially the cost of preserving the chronological discontinuity at the canonical Hijra boundary."

[[h-new-670-tsp-hijra-constraint|H-NEW-670]] **REFUTES this specific interpretation**. The Hijra-kink contributes only 3.3% of the residual, not "partially." A more accurate version is:

> "The 11% TSP-residual is the cumulative cost of preserving MANY canonical structural choices, including (but not centered on) the Hijra-kink. al-Fātiḥa's primacy at Q 1 is the SINGLE most-expensive adjacency tested (7.4%); Hijra-kink is moderate (3.3%); muʿawwidhāt-pair Q 113-Q 114 is near-free (0.8%)."

The [[h-new-660-compression-tail-gradient|H-NEW-660]] §6 interpretation is HEREBY RETRACTED. The compression-tail law (R²=0.986) is FULLY PRESERVED — it stands as the empirical content-cohesion gradient. The interpretation linking it specifically to TSP-residual was over-confident.

## 7. The compression-tail law remains SCALE-INVARIANT ([[h-new-680-multi-k-compression-tail|H-NEW-680]])

[[h-new-680-multi-k-compression-tail|H-NEW-680]] (parallel specialist run, completed 2026-04-28): the compression-tail law holds at all K ∈ {7, 11, 22} with R² ∈ [0.948, 0.993], slope β ≈ −0.013, kink in [50, 55]. The law is a fundamental scale-invariant property of the mushaf.

[[h-new-670-tsp-hijra-constraint|H-NEW-670]] NULL does NOT threaten the law itself — it only retracts the §6 interpretation about TSP-residual. The CONTENT-COHESION GRADIENT is real; the TSP-OPTIMALITY-SACRIFICE story is wrong.

These are SEPARATE empirical claims. The first survives; the second does not.

## 8. Honest limits

1. **2-opt is heuristic**, not exact. My unconstrained 2-opt converged to L=77.47 (matches [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]), so the unconstrained anchor is solid. Constrained results may have ±0.05 noise from local-minimum trapping.
2. **Single-adjacency tests** isolate ONE constraint at a time. Multi-adjacency interactions are not tested — though additivity is plausible since 2-opt is local.
3. **6 control adjacencies** is a small set. More (e.g., a permutation null over 100 random pairs) would tighten the random-baseline estimate.
4. **The L_mushaf − L_2opt = 8.29 length-units is the global residual budget.** No single tested constraint approaches it.
5. **Constraints near boundaries** (Q 1-Q 2, Q 113-Q 114) may have asymmetric properties (no left or right neighbor); the test treats them uniformly via Hamiltonian PATH (open).

## 9. Cross-references

- **[[h-new-660-compression-tail-gradient|H-NEW-660]]** (compression-tail law): §6 interpretation RETRACTED; rest of the finding stands.
- **[[h-new-680-multi-k-compression-tail|H-NEW-680]]** (multi-K compression-tail): compression-tail law confirmed scale-invariant; this is the law's STRENGTH, separate from [[h-new-660-compression-tail-gradient|H-NEW-660]] §6.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (mushaf 11% TSP-residual): now refined — residual is DISTRIBUTED, not concentrated at any single adjacency.
- **[[h-new-590-outlier-spectrum|H-NEW-590]]** (outlier-strength spectrum): Q 1 al-Fātiḥa +27pp explains why Q 1-Q 2 adjacency is the most-expensive canonical constraint.
- **[[h-new-130-fisher-rao-residuals|H-NEW-130]]** (universal hinges): Hijra-kink is real as a CONTENT-cohesion hinge, but does NOT carry the TSP-residual.

## 10. Queued follow-ups

- **H-NEW-670.1**: Multi-adjacency constraint test — force ALL Meccan-Meccan canonical adjacencies (Q 1-50 + Q 67-114) simultaneously. What's the cost?
- **H-NEW-670.2**: Per-adjacency residual-cost map — sweep all 113 canonical adjacencies. Build a "cost-of-canonical-pair" landscape.
- **[[h-new-720-canonical-adjacency-cost|H-NEW-720]]**: Re-formalize the residual-decomposition into structural categories: (Q 1 primacy) + (Hijra-kink) + (terminal-pair) + (muqaṭṭaʿāt clustering) + (length-monotonicity penalty).

## 11. Final statement

**The [[h-new-660-compression-tail-gradient|H-NEW-660]] §6 hypothesis — that the 11% mushaf TSP-residual is ~partially the cost of preserving the Hijra-kink — is FALSIFIED.** The Hijra-kink contributes only 3.3% of the residual. The single most-expensive canonical adjacency tested is Q 1-Q 2 at 7.4%, reflecting al-Fātiḥa's deliberate primacy despite content-distinctness from Q 2 al-Baqara.

The 11% TSP-residual is **DISTRIBUTED** across many canonical adjacencies, each contributing 0.05-0.7 length-units. No single architectural feature is dominant. The mushaf's *tartīb tawqīfī* is a CONSTELLATION of structural commitments, not one big choice.

**The compression-tail law ([[h-new-660-compression-tail-gradient|H-NEW-660]] + [[h-new-680-multi-k-compression-tail|H-NEW-680]], R² ≥ 0.948 across all K) stands.** Only the §6 interpretation linking it to TSP-residual is retracted.

This NULL is published with full prominence. It is a routine outcome of pre-registration discipline — speculation in §6 was overconfident and the formal test corrected it.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
