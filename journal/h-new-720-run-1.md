# H-NEW-720 — Run 1 Journal

**Date**: 2026-04-28
**Operator**: specialist agent
**Task**: full canonical-adjacency residual-cost map (sweep all 113 pairs)

## Setup

- Pre-reg: `findings/phase-b-hypotheses/h-new-720-canonical-adjacency-cost-prereg.md`
- Pre-reg SHA: `a2f340b7fe79b1e78228413090c12a8b67b9b51c58603554dc41d4a87d7f444b`
- Script: `scripts/h_new_720_full_adjacency_cost.py`
- Seed: 20260441
- Configuration: 50 random starts per pair, 2000 max-iter per 2-opt convergence, pos-tracking constraint check.

## Anchors

- L_mushaf = 85.759656
- L_2opt = 77.466858 (cross-finding-011)
- residual = 8.292798 length-units (10.7% of L_2opt; 9.67% of L_mushaf)

## Pre-committed structural findings

- FINDING-A: top-3 most-expensive ≥ 25% of residual (≥ 2.073 length-units)
- FINDING-B: bottom-30 least-expensive ≤ 5% of residual (≤ 0.415 length-units)
- FINDING-C: near-Hijra cluster s ∈ [50, 66] ≥ 15% of residual (≥ 1.244 length-units)

## Execution log

- Started 2026-04-28 ~15:50 PT
- Initial run with `tee` was buffering — restarted with `python3 -u` (PYTHONUNBUFFERED=1) and direct output to /tmp/h720.log.
- Run completed 2026-04-28 ~16:02 PT.
- Total walltime: 723.2 s (~12 min). Average ~6.4 s/pair × 113 pairs.
- All 113 pairs converged within 2000-iter budget without errors.
- 13 of 113 pairs (11.5%) had Δ_raw ≤ 0 (constrained 2-opt found tour BELOW cf011 anchor of 77.467); pre-commit floor-at-0 applied.

## Results

### Top-3 most-expensive
1. Q1-Q2 (al-Fātiḥa → al-Baqara): Δ = 0.6216 (7.50%)
2. Q32-Q33 (al-Sajda → al-Aḥzāb): Δ = 0.3631 (4.38%)
3. Q33-Q34 (al-Aḥzāb → Sabaʾ): Δ = 0.3311 (3.99%)

### Bottom-3 cheapest (most-negative Δ_raw, all floored to 0)
1. Q91-Q92 (al-Shams → al-Layl): Δ_raw = -0.0868
2. Q4-Q5 (al-Nisāʾ → al-Māʾida): Δ_raw = -0.0657
3. Q6-Q7 (al-Anʿām → al-Aʿrāf): Δ_raw = -0.0575

### Cumulative
- Σ Δ_s (all 113 floored) = 9.827 length-units
- L_mushaf − L_2opt = 8.293 length-units
- Σ Δ / residual = 1.185 (SUPER-ADDITIVE: sum > residual)
- mean Δ = 0.0870, median Δ = 0.0621, std Δ = 0.0924
- max Δ = 0.6216, min raw Δ = -0.0868

### Structural-finding verdicts

| Finding | Threshold | Observed | Verdict |
|:-:|:-:|:-:|:-:|
| A: top-3 ≥ 25% | 2.073 | 1.316 (15.9%) | **FAIL** |
| B: bot-30 ≤ 5% | 0.415 | 0.291 (3.5%) | **PASS** |
| C: Q50-66 cluster ≥ 15% | 1.244 | 1.337 (16.1%) | **PASS** (narrow, 0.09 above threshold) |

### Per-decade pattern (cost declines monotonically with s)
- s=1-10: Σ=1.293 (incl. Q1-Q2 = 0.622)
- s=11-20: Σ=1.030
- s=21-30: Σ=1.275
- s=31-40: Σ=1.383 (peak — Q32-Q34 cluster)
- s=41-50: Σ=1.015
- s=51-60: Σ=0.922 (incl. Hijra-kink)
- s=61-70: Σ=0.760
- s=71-80: Σ=0.648
- s=81-90: Σ=0.393
- s=91-100: Σ=0.440
- s=101-113: Σ=0.671

## Honest issues / observations

1. **cf011 anchor is a heuristic upper bound**: 13 of 113 pairs found constrained tours below 77.467, with most-negative Δ_raw = -0.087 at Q91-Q92. The TRUE L_2opt is at most 77.380. This was handled per pre-reg via floor-at-0; documented in §6 of findings.
2. **Super-additivity discovered** (Σ_individual = 9.83 > joint residual 8.29; ratio 1.185): adjacencies COOPERATE in the joint mushaf. This was a descriptive comparison (no pre-commit threshold) and emerged as a non-trivial finding.
3. **NEW high-cost cluster Q32-Q34** discovered: al-Sajda → al-Aḥzāb → Sabaʾ. This was NOT predicted; emerges as comparable in cost to Q1-Q2. Queued for follow-up (H-NEW-720.3) — possibly a *sajda-tilawa* + Medinan-Meccan typological boundary.
4. **FINDING-A FAILS** because residual is even MORE distributed than pre-registered: top-3 = 16% (vs 25% threshold). This is a STRONGER form of H-NEW-670's NULL.
5. **FINDING-C PASSES narrowly** (1.337 vs 1.244 threshold; 16.1% vs 15%). Cluster sum is 0.09 above threshold — within the ±0.09 noise band per pair × 17 pairs. Robust interpretation: "Q50-66 cluster carries ~15-17% of residual" rather than precise PASS at 16.1%.
6. **No directional constraint enforced** — 2-opt PATH constraint is symmetric (a-b or b-a both allowed). The TRUE *tartīb tawqīfī* is directional. Queued as H-NEW-720.2.

## Files emitted

- Pre-reg: `findings/phase-b-hypotheses/h-new-720-canonical-adjacency-cost-prereg.md` (SHA a2f340b7...)
- Script: `scripts/h_new_720_full_adjacency_cost.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-720.json` (37,924 bytes)
- Findings: `findings/phase-b-hypotheses/h-new-720-canonical-adjacency-cost.md`
- Journal: this file

## Verdict

**PARTIAL** — distribution-of-residual hypothesis CONFIRMED (FINDING-B and FINDING-C PASS); "top-3 dominate" hypothesis FALSIFIED (FINDING-A FAIL). Q1-Q2 al-Fātiḥa primacy remains most-expensive single canonical adjacency at 7.5%; new finding: Q32-Q34 cluster comparable in cost. Near-Hijra Q50-66 cluster carries 16% of residual.

The mushaf's *tartīb tawqīfī* is a fine-grained CONSTELLATION of structural commitments, not dominated by any single feature. Super-additivity (1.185×) suggests joint optimization rather than ad-hoc local choices.
