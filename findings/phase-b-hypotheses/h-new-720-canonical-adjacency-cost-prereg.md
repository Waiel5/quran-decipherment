---
id: H-NEW-720
title: "Pre-reg — Full canonical-adjacency residual-cost map (sweep all 113 single-adjacency constraints)"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-670 NULL — 11% TSP-residual is DISTRIBUTED, not concentrated. Need full sweep to characterize the distribution.
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260441
---

# [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Full Canonical-Adjacency Residual-Cost Map: Pre-Registration

## 1. Hypothesis

[[h-new-670-tsp-hijra-constraint|H-NEW-670]] tested 6 adjacencies and showed the 11% TSP-residual (L_mushaf − L_2opt = 8.29 length-units) is DISTRIBUTED across many canonical adjacencies. Q1-Q2 was 7.4%, Hijra-kink (Q56-Q57) was 3.3%, terminal pair (Q113-Q114) was 0.8%. To complete the decomposition, sweep ALL 113 canonical adjacencies (Q s, Q s+1) for s ∈ {1,...,113} and build the full per-adjacency cost landscape.

## 2. Test design

For each canonical adjacency (Q s, Q s+1), s ∈ {1,...,113}:
1. Run constrained 2-opt (pos-tracking, O(1) constraint check) with that pair forced adjacent.
2. Use 50 random starts per pair (vs 200 in [[h-new-670-tsp-hijra-constraint|H-NEW-670]] — reduced for tractability across 113 pairs).
3. Max 2000 iterations per 2-opt convergence.
4. Record:
   - L_2opt|s,s+1 = constrained-best path length.
   - Δ_s = L_2opt|s,s+1 − L_2opt (anchor: 77.466858).
   - Fraction of residual = Δ_s / 8.292798 (L_mushaf − L_2opt).

### Anchors (from [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] / [[h-new-670-tsp-hijra-constraint|H-NEW-670]])
- L_mushaf = 85.759656
- L_2opt = 77.466858
- residual = 8.292798 length-units (10.7% of L_mushaf)

## 3. Pre-committed direction

For all s ∈ {1,...,113}: **Δ_s ≥ 0** (constraint cannot reduce unconstrained optimum). Any negative Δ_s indicates 2-opt convergence noise and will be reported as 0 in cumulative-cost calculations (with the noise magnitude documented).

## 4. Pre-committed thresholds (descriptive structural findings)

This is primarily a DESCRIPTIVE map, not a hypothesis test of a single number. Three structural findings are pre-committed:

- **STRUCTURAL FINDING-A**: Top-3 most-expensive single canonical adjacencies cumulatively account for ≥ 25% of the 8.29-unit residual (sum of three Δ values ≥ 2.07 length-units).
- **STRUCTURAL FINDING-B**: Bottom-30 least-expensive single canonical adjacencies cumulatively cost ≤ 5% of the residual (sum ≤ 0.41 length-units).
- **STRUCTURAL FINDING-C**: A "near-Hijra" cluster (s ∈ [50, 66], i.e., Q50-Q51 through Q66-Q67) carries ≥ 15% of the residual cumulative cost (sum ≥ 1.24 length-units).

Each finding is independently PASS / FAIL. No averaging.

## 5. Bonferroni structure

Bonferroni-3 (three structural findings) → α_bon = 0.05/3 = 0.01667. Note: these structural findings are descriptive thresholds on cumulative sums, not hypothesis tests with permutation null. There is no statistical test against null distribution at the structural-finding level — the thresholds are pre-committed magnitudes. Bonferroni is documented as a methodological discipline (each finding is one of three independent claims) but is not a permutation correction.

If we were to permute the (canonical s ↔ Δ) pairing and test whether the OBSERVED top-3 sum is anomalously high vs. random adjacencies, that would require additional non-canonical-adjacency measurements; that is a follow-up (H-NEW-720.1), NOT this run.

## 6. Methodology rules

- MW-1 instrument-prior: FR-roots distance via [[h-new-111-fisher-rao-mushaf|h-new-111]].json D matrix.
- MW-3 alternative-models: each adjacency tested in same way; cross-comparison is the analysis.
- MW-7 honest-null: report the FULL 113-element distribution; no p-hacking on which subset to call "canonical-cluster".
- ONE-text discipline: ḥafṣ ʿan ʿĀṣim text only.
- Direction-locked: Δ_s ≥ 0.

## 7. Cumulative-sum comparison (descriptive)

Compute Σ Δ_s over s = 1..113 and compare to L_mushaf − L_2opt = 8.293. These are NOT additive (constraints interact), but the comparison is informative:
- If Σ Δ_s ≪ 8.29: constraints "cooperate" — fixing one makes others cheaper, and the mushaf is paying a SUPER-ADDITIVE cost.
- If Σ Δ_s ≈ 8.29: constraints are roughly independent.
- If Σ Δ_s ≫ 8.29: constraints "conflict" — fixing one makes others harder, and the mushaf gets a SUB-ADDITIVE deal.

This is DESCRIPTIVE only; no threshold is pre-committed.

## 8. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-720-canonical-adjacency-cost-prereg.md` (this file)
- Script: `scripts/h_new_720_full_adjacency_cost.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-720.json`
- Findings: `findings/phase-b-hypotheses/h-new-720-canonical-adjacency-cost.md`
- Journal: `journal/h-new-720-run-1.md`

## 9. Performance budget

- 113 pairs × 50 starts × ≤2000 iter ≈ ~10-30 minutes Python.
- If walltime exceeds 30 min, reduce starts to 30 and document the reduction.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
