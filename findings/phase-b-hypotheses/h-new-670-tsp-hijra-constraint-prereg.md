---
id: H-NEW-670
title: "Pre-reg — Constrained-TSP test: does forcing Q 56/57 adjacency raise tour-length close to L_mushaf?"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-660 §4 + cross-finding-011 — partial explanation of 11% TSP-residual is the Hijra-kink preservation cost
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260440
---

# [[h-new-670-tsp-hijra-constraint|H-NEW-670]] — Constrained-TSP / Hijra-Adjacency Cost: Pre-Registration


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

[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] found the canonical mushaf is 11% from FR-TSP-optimal:
- L_mushaf = 85.76
- L_2opt = 77.47
- ratio = 1.107

[[h-new-660-compression-tail-gradient|H-NEW-660]] found that the Hijra-boundary kink at Q 56/57 is structurally locked in the canonical mushaf (R²=0.986 single-parameter law).

**Hypothesis**: A non-trivial fraction of the 11% TSP-residual is the COST of preserving the Q 56-Q 57 adjacency. If we constrain TSP to require Q 56-Q 57 adjacency, the constrained-optimal tour-length L_2opt|56-57 will be CLOSER to L_mushaf than the unconstrained L_2opt.

## 2. Test design

For Hamiltonian PATH (open, length-113-edge):
- **L_2opt** (unconstrained): 77.47 ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] anchor).
- **L_2opt|adj56-57**: best 2-opt tour subject to Q 56 and Q 57 being immediately adjacent in the path.
- **L_mushaf**: 85.76 ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] anchor).

### Implementation
- Contract Q 56-Q 57 into a single "super-node" with two endpoints (the orientation is preserved).
- Build a 113-node distance matrix where the super-node has its two flanking-edge weights to other surahs (one for "Q 56 is the touchpoint", one for "Q 57 is the touchpoint").
- Run 2-opt from multiple random starts (≥100), pick the best.
- Optionally: also run 2-opt with Q 56 IMMEDIATELY-FOLLOWED-BY Q 57 in mushaf-order direction.

### Comparison metrics
- **Δ_constraint**: L_2opt|56-57 − L_2opt = excess length forced by the constraint.
- **Fraction-of-residual-explained**: (L_2opt|56-57 − L_2opt) / (L_mushaf − L_2opt).
- **Constrained-residual**: (L_mushaf − L_2opt|56-57) / L_mushaf — what's left to explain after Hijra-kink.

## 3. Pre-committed direction

- L_2opt|56-57 ≥ L_2opt (constraint cannot reduce optimum).
- Fraction-of-residual-explained ≥ 0 (always true; question is magnitude).

## 4. Pre-committed thresholds

- **STRONG-PASS**: Fraction-of-residual-explained ≥ 0.50. The Hijra-kink alone explains ≥50% of the 11% TSP-residual.
- **DIRECTIONAL**: Fraction-of-residual-explained ∈ [0.20, 0.50]. Substantial.
- **MARGINAL**: Fraction-of-residual-explained ∈ [0.05, 0.20]. Hijra-kink is one of multiple factors.
- **NULL**: Fraction-of-residual-explained < 0.05. Hijra-kink does not explain the residual.

## 5. Bonferroni structure

Single test (one constraint, one comparison) → no Bonferroni correction needed.

## 6. Methodology rules

- MW-1: instrument-prior — FR-roots distance via [[h-new-111-fisher-rao-mushaf|h-new-111]].json D matrix.
- MW-3: alternative-models — also compute L_2opt|adj13-14 (random-Meccan-adjacency) and L_2opt|adj1-2 (Q 1-Q 2) as CONTROLS. If those non-Hijra adjacencies have similar Δ, the Hijra-kink claim is weakened.
- PRE-REG-STANDARD-04: hypothesis, null, direction, success criteria all locked.

## 7. Pre-committed control

- **Control adjacency 1**: Q 1-Q 2 (mushaf-canonical adjacency, but not at Hijra-boundary). Expected Δ similar (mushaf preserves it too).
- **Control adjacency 2**: random non-canonical adjacency, e.g., Q 13-Q 80 (forced random pair). Expected Δ ≥ Hijra-kink Δ (random pair is harder constraint).

The Hijra-kink claim is strongest if Δ(Q56-57) is materially larger than Δ(Q1-Q2) but smaller than random-pair Δ.

## 8. Files

- Script: `scripts/h_new_670_tsp_hijra_constraint.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-670.json`
- Findings: `findings/phase-b-hypotheses/h-new-670-tsp-hijra-constraint.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
