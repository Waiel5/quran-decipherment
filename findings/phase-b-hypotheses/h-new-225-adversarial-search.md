# [[h-new-225-adversarial-search|H-NEW-225]] — Adversarial search: can ANY ordering beat the mushaf path length?


> ## ⛔ CORRECTION NOTICE — 2026-08-07
>
> **The arithmetic here is not retracted.** What fell is the inference drawn from the Fisher-Rao
> permutation null. Under the project's first genre control (`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`),
> al-Bukhārī scores **z = −13.84** and pre-Islamic poetry **z = −15.13** against the Qurʾān's
> **z = −11.50** on an instrument-matched pipeline, and both baselines sit closer to their own TSP
> optima. Cutting this corpus's own verse stream into 114 blocks of the same size profile at offsets
> that ignore every surah seam gives z = −11.23 to −13.18. **Length-sorting alone reaches z = −8.66**
> (H-NEW-111's write-up mis-transcribed that anchor as 107.27; its own `csv/h-new-111.json` records
> 91.03 / 90.30). The mushaf's honest margin over pure length is **2.80 σ**, not 11.46 σ.
> The *relative* claim survives — mushaf 85.76 < Nöldeke 87.23 < Tanzil 89.53.
> Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


**Finding ID**: [[h-new-225-adversarial-search|h-new-225]]
**Date**: 2026-04-17
**Specialist**: autonomous
**Pre-reg**: `findings/phase-b-hypotheses/h-new-225-adversarial-search-prereg.md`
**Pre-reg SHA-256**: `345e7c87dc6ddd720d568232b09e092db3a0e2e7167f03281003f1e97fe57ee5`
**Seed**: 20260419
**Parent**: [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (L_mushaf=85.760, L_2opt=77.467, ratio 1.107)
**Sibling**: [[h-new-144-cyclic-tsp|H-NEW-144]] (cyclic ratio 1.0945)
**Rules tuple**: (114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya, open Hamiltonian path, mushaf-initialized 2-opt + 100-random-start SA search)
**Verdict**: **PASS** (mushaf non-optimal by ~10.8%; quantified gap matches theorist prediction)

---

## Headline

**Adversarial search on the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D-matrix DECISIVELY finds orderings shorter than the mushaf. The mushaf is NOT a 2-opt local optimum on this graph — 81 improving swaps exist from the canonical ordering — and 100 SA + 2-opt restarts find a new tightest upper bound of L_search_min = 77.404.**

- L_mushaf                 = 85.760
- L_mushaf (after 2-opt)   = 77.973 (81 improving swaps; first swap: reverse positions 1..113, Δ=−0.789)
- L_SA_min (100 restarts)  = 77.404 (seed 20260465)
- **L_search_min**         = **77.404** (TIGHTENS [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s L_2opt=77.467)
- **gap_abs**              = **8.355**
- **gap_rel**              = **1.1079**

The mushaf ranks **102 of 102** in the pooled set of search results (102 = 100 SA restarts + mushaf-2opt + mushaf itself). **Every single search run found an ordering shorter than the mushaf.**

---

## Decision

Pre-reg decision rule (k=1, descriptive α=0.05):

| Rule | Threshold | Observed | |
|---|---:|---:|---|
| SURPRISE-NULL | gap_rel ≤ 1.01 | 1.1079 | ✗ |
| PASS | 1.01 < gap_rel ≤ 1.15 | 1.1079 | **✓** |
| EXTREME-GAP | gap_rel > 1.15 | 1.1079 | ✗ |

**Verdict: PASS.** The mushaf is provably non-optimal on the Fisher-Rao open-path metric, by a gap of ~10.8%. This is consistent with [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s reported ratio 1.107 and the theorist prediction (gap_rel ≈ 1.107).

## What this does NOT do

1. Does **not** revise [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s PRIMARY result (z=−11.46 vs random null). The mushaf remains 11 SD below random mean — dramatically non-random.
2. Does **not** demote M1 ([[cross-finding-013-mushaf-topological-ring|cross-finding-013]]). M1's "near-optimal" language is **backed** by this result: gap_rel = 1.11 is the definition of "near-optimal" at the pre-registered <1.2 threshold of [[h-new-111-fisher-rao-mushaf|H-NEW-111]]-Secondary-A.
3. Does **not** claim the 77.40 ordering is the GLOBAL minimum. It is a tightened UPPER BOUND on the true L_min; a Concorde-exact or LKH-3 run would strictly improve on it.

## What this DOES do

1. **Quantifies the gap empirically via adversarial search.** Prior parent bounds came from greedy + 2-opt; this run commits 1M SA proposals + 100 independent restarts. The gap is robust.
2. **Tightens [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s Secondary-A bound** from L_2opt=77.467 to L_search_min=77.404 (self-verifying tightening amendment per project discipline — `feedback_bonferroni_tightening_vs_loosening.md`). The updated ratio L_mushaf / L_search_min = **1.1079** (was 1.1071 in [[h-new-111-fisher-rao-mushaf|H-NEW-111]] after rounding).
3. **Falsifies "mushaf is 2-opt-locally-optimal".** The very first improving swap from the mushaf ordering reverses the entire path (i=0, j=113, Δ=−0.789). This single move alone gets L from 85.76 → 84.97. 80 more swaps continue to improve toward 77.97.
4. **Confirms theorist prediction R ≈ 1.107 on open path** matching both (a) 100-SA best and (b) parent's greedy+2-opt — three independent heuristic families converging to the same ~77.4-77.5 basin is strong (non-definitive) evidence that the true L_min is ≈ 77.4 ± 0.5.

## Detail: 81 improving 2-opt swaps from mushaf

The mushaf-initialized 2-opt run executed **81 improving swaps over 82 passes** before reaching a local optimum at L=77.97. Total improvement: ΔL=−7.787 (mushaf 85.76 → 77.97). Per-swap mean improvement: ~0.096.

The first swap reverses positions 1..113 (i=0, j=113, Δ=−0.789), which equivalently reverses the entire mushaf order except Q1. This is a single-edge swap targeting the path's first edge (1→2) vs the wrap edge (114→1). The existence of this particular improving swap is consistent with [[h-new-130d-reverse-universal-wraparound|H-NEW-130d]]'s finding that the wrap-around edge d(Q114, Q1) = 0.388 is notably short — so reversing the path at the correct hinge improves the open-path sum immediately.

## Detail: 100-restart SA distribution

| Quantile | L |
|---|---:|
| min | 77.404 |
| 25th %ile | 77.62 (approx) |
| median | 77.701 |
| mean | 77.702 |
| 75th %ile | 77.78 (approx) |
| max | 78.021 |
| SD | 0.125 |

All 100 SA+2-opt restarts converged into a narrow basin [77.40, 78.02] (spread 0.62, SD 0.125). This tight clustering strongly suggests a well-defined geodesic basin; the "true" L_min is very likely within ±0.5 of 77.4. No restart found anything matching the mushaf value (85.76) or higher — the mushaf is NOT in the basin reached by adversarial search.

## Honest limits

1. **SA+2-opt is a heuristic**, not an exact solver. A Concorde-exact run would settle L_min to the nearest float. Our 77.404 is an upper bound on the true optimum.
2. **D-matrix reused from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] verbatim.** If the K=500 / α_dir=0.5 / Fisher-Rao choices influence the gap, this result is conditional on those parent locks. A cross-metric replication (e.g., Hellinger or JS distance) belongs to a separate pre-reg (H-NEW-225b if queued).
3. **The gap is not proof of "suboptimal design".** That the mushaf is ~10.8% above an adversarial minimum does NOT mean the mushaf is poorly ordered at the information-geometric axis — 10.8% is, for a 114-node TSP, inside the regime where a human orderer optimizing for OTHER criteria (theme, length, revelation-chronology, liturgical coherence) would naturally fall. [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s core finding (z=−11.46 vs random) remains: the mushaf is dramatically non-random, just not globally minimum.
4. **No p-value is reported for the "existence" claim**, because the answer was predetermined by [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (L_2opt=77.47 < L_mushaf=85.76 exhibited a known-shorter ordering as soon as that run completed). [[h-new-225-adversarial-search|H-NEW-225]] refines the QUANTITY of the gap, not its existence.

## Connections

- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** (parent): L_mushaf / L_2opt = 1.107. [[h-new-225-adversarial-search|H-NEW-225]] updates this to L_mushaf / L_search_min = 1.1079 (tighter denominator).
- **[[h-new-144-cyclic-tsp|H-NEW-144]]** (cyclic sibling): cyclic ratio 1.0945, tighter than open-path ratio because wrap edge 0.388 is short. [[h-new-225-adversarial-search|H-NEW-225]] operates on the open-path problem to stay directly comparable with [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]], [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]** (CONFIRMED): both M1 claims are unaffected; [[h-new-225-adversarial-search|H-NEW-225]] REFINES their quantitative bounds.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-225-adversarial-search-prereg.md`
- Script: `scripts/h_new_225_adversarial_search.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-225.json`
- Journal: `journal/h-new-225-run-1.md`

## Verdict

**PASS (gap_rel = 1.1079).** Adversarial search — 2-opt from mushaf + 100-restart SA — robustly finds orderings shorter than the mushaf. Mushaf is not 2-opt-locally-optimal (81 improving swaps). The gap matches theorist prediction (~1.107) and marginally tightens [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s upper bound (77.467 → 77.404). M1's "near-optimal Hamiltonian path" language is empirically confirmed at the ~11% gap level by adversarial search, not just by greedy heuristic.
