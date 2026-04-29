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
