---
id: H-NEW-690
title: "Causal generative test of the compression-tail law — NULL: compression-tail is NECESSARY but NOT SUFFICIENT for mushaf-class TSP-optimality"
phase: B
date: 2026-04-28
status: COMPLETE
parents:
  - H-NEW-660 (compression-tail law, R²=0.986, β=−0.0124)
  - cross-finding-011 (canonical mushaf is 11% above 2-opt TSP, z=−11.46)
prereg: findings/phase-b-hypotheses/h-new-690-causal-generative-prereg.md
prereg_sha: 21d56df2bcf132dd219846ce7152df2e089e876a85dc5b089e8a30257efadfda
script: scripts/h_new_690_causal_generative.py
output: findings/phase-b-hypotheses/csv/h-new-690.json
journal: journal/h-new-690-run-1.md
seed: 20260437
bonferroni_k: 3
alpha_bon: 0.0167
verdict: NULL (compression-tail is NECESSARY but NOT SUFFICIENT)
---

# [[h-new-690-causal-generative|H-NEW-690]] — Causal Generative Test of the Compression-Tail Law

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

*Bismillāhi al-Raḥmāni al-Raḥīm.*

## §1. Headline

**Verdict: NULL.** Compression-tail-alone is **NOT** sufficient to generate orderings with mushaf-class TSP-residuals.

The constrained ensemble (n=90 sampled orderings that respect the [[h-new-660-compression-tail-gradient|H-NEW-660]] two-piece-kink-50 law: R² ≥ 0.95, β ∈ [−0.015, −0.010]) has:

| Statistic | Constrained ensemble | Canonical mushaf | Random permutations* |
|---|---|---|---|
| FR-tour-length L | median 96.79 (range 94.32–99.51) | **85.76** | mean 104.35 (sd 1.62) |
| Residual (L − L_2opt) / L_2opt | median **24.95%** (range 21.76% – 28.45%) | **10.70%** | mean **34.70%** |
| Canonical's percentile | **0.0%** (canonical is below the entire ensemble) | — | < 0.001% |

\* Random-permutation null from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (n=10000); L_2opt = 77.466858 from same.

**Histogram of residuals across 90 sampled constrained orderings:**

```
21.76% – 22.43% : 8 ████████
22.43% – 23.10% : 4 ████
23.10% – 23.77% : 11 ███████████
23.77% – 24.43% : 13 █████████████
24.43% – 25.10% : 15 ███████████████
25.10% – 25.77% : 15 ███████████████
25.77% – 26.44% : 12 ████████████
26.44% – 27.11% : 8 ████████
27.11% – 27.78% : 3 ███
27.78% – 28.45% : 1 █
```

Pre-registered pass thresholds:
- STRONG GENERATIVE (≥ 50% of ensemble at residual ≤ 11.5%): **0/90 = 0.0%** → FAIL.
- DIRECTIONAL (≥ 25% at residual ≤ 12%): **0/90 = 0.0%** → FAIL.
- NULL (< 10% at residual ≤ 13%): **0/90 = 0.0%** → **PASS**.

The verdict is unambiguous and meets the NULL pre-registered threshold by a wide margin.

## §2. Comparison: canonical vs constrained ensemble vs pure-TSP-optimum

Three reference points on the FR-tour-length axis:

| Anchor | L | Residual to L_2opt | Description |
|---|---|---|---|
| L_2opt (target) | 77.47 | 0.00% | 2-opt TSP upper bound on the FR-roots metric |
| L_canonical (mushaf) | **85.76** | **10.70%** | Canonical Quran order ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]) |
| Constrained-ensemble median | 96.79 | **24.95%** | Median of orderings respecting compression-tail law |
| Constrained-ensemble best | 94.32 | 21.76% | Lowest TSP residual found in 90 samples |
| Random-perm mean | 104.35 | 34.70% | [[h-new-111-fisher-rao-mushaf|H-NEW-111]] null mean |

**Key observation.** The compression-tail constraint moves residual from random's ~34.7% to ~24.95% — a *partial* compression of ~ (34.7 − 25.0) / (34.7 − 10.7) ≈ **40%** of the way from random to canonical. So the compression-tail law accounts for roughly 2/5 of the canonical mushaf's TSP-optimality, leaving ~3/5 unexplained.

**The canonical mushaf is at residual 10.70%, *below* the entire constrained ensemble** (best constrained sample: 21.76%). Canonical is not merely a "good" representative of compression-tail-respecting orderings — it is *exceptional* even within that subset.

## §3. Where does the canonical mushaf sit in the constrained-ensemble distribution?

**Canonical's percentile in the constrained ensemble: 0.0%** (canonical L = 85.76 is below the minimum sampled L = 94.32).

A trajectory diagnostic from canonical confirms this: starting from canonical (residual 10.70%), a Metropolis-Hastings chain on FR-tour-length (subject to staying inside the compression-tail-feasible set) drifts upward rapidly:

| Step | L | Residual | R² | Notes |
|---|---|---|---|---|
| 0 | 85.76 | 10.70% | 0.9860 | canonical start |
| 10 | 87.02 | 12.34% | 0.9830 | already past 12% |
| 50 | 90.66 | 17.03% | 0.9534 | well above 15% |
| 100 | 91.63 | 18.28% | 0.9676 | |
| 500 | 96.02 | 23.95% | 0.9567 | reached typical-set |
| 1000 | 94.41 | 21.87% | 0.9518 | mixing in plateau |
| 5000 | 95.97 | 23.89% | 0.9549 | stable plateau |

The constrained ensemble's typical residual is ~24–25%; canonical sits at 10.7%. **The compression-tail constraint defines a "valley" of orderings, but canonical is at a special lower-elevation point INSIDE that valley.** Compression-tail is an envelope, not the architecture itself.

## §4. Implication: NECESSARY, SUFFICIENT, or NEITHER?

**Compression-tail is NECESSARY but NOT SUFFICIENT for canonical mushaf-architecture.**

- **Necessary** (in the sense of marginal contribution): the constrained ensemble's residual (~25%) is lower than the random-permutation residual (~35%) by a large and clear margin. Imposing the compression-tail law alone reduces typical residual by ~10 percentage points, accounting for ~40% of the canonical's TSP-optimality gap to random.
- **Not sufficient**: 0 of 90 constrained orderings reach mushaf-class residual (≤ 13%). The chain rapidly walks away from canonical even when started there. A randomly-drawn ordering from the constrained subset has expected residual ~24-25%, more than DOUBLE canonical's 10.7%.

This is consistent with the broader Phase-B finding ([[cross-finding-018-four-principle-reduced-model|cross-finding-018]], [[cross-finding-021-mushaf-information-theoretic-optimality|cross-finding-021]]) that **mushaf-architecture is multi-principle**: compression-tail is one of several joint constraints (Nöldeke ordering, Mufaṣṣal/Ṭiwāl/Awsāṭ groupings, muqaṭṭaʿāt placement, root-bridge architecture, etc.) that together yield the canonical's exceptional TSP-residual. None of them alone explains the full 11%.

**A correctly-stated causal claim:** the compression-tail law is a *consequence-constraint* of the mushaf — any ordering that satisfies it has lower-than-random tour length, but the strict 11% optimum requires *additional* architecture (rhythm, content axes, MWA-rules, surah-grouping conventions) layered on top.

## §5. Honest limits

1. **MCMC mixing.** The chain warmup failed to reach feasibility from a random start within 5000 greedy descent attempts; we fell back to canonical-start (pre-registered fallback). This means the chain's typical-set is reached *from* canonical, not toward it from elsewhere. However, the trajectory diagnostic shows rapid escape from canonical (within 50 steps), and three independent seeds (99991, 4242, 12345) all converge to median residuals of 24-26% — so the typical-set value is robust to seed.

2. **Sample count is 90, not 100.** The sampler indexed `next_sample_step = n_burn + sample_every` (i.e., first sample at step 1100), so over 10000 steps we collected 90 samples instead of 100. This is a minor bookkeeping deviation and does not affect the verdict (which is at 0% / 0% / 0% and far from any pre-registered threshold). Documented honestly here.

3. **Constraint definition is post-hoc-tuned.** R² ≥ 0.95 and β ∈ [−0.015, −0.010] were chosen tightly around [[h-new-660-compression-tail-gradient|H-NEW-660]]'s canonical fit (R²=0.986, β=−0.0124). A loosened constraint (e.g., R² ≥ 0.80, β ∈ [−0.02, −0.005]) might yield a wider ensemble with more variation. We pre-locked the tight version because the question is "respects-the-law-as-fitted", and the law-as-fitted is the [[h-new-660-compression-tail-gradient|H-NEW-660]] result. Loosening would test "respects-some-version-of-compression-tail" — a different question.

4. **MH temperature T=1.0 is conservative TOWARD finding STRONG.** With T=1.0 the chain favors lower-L states (those closer to canonical-class). Even with this bias, the chain stabilizes at ~25% residual, NOT near 10.7%. A higher temperature (more random) would only push residuals *higher*, strengthening the NULL.

5. **One feature space (FR-roots).** This test uses the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] root-axis distance matrix only. [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] (char-4-gram) and [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] (verselen) gave different but consistent ranking results in [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]. Replicating [[h-new-690-causal-generative|H-NEW-690]] on those two axes would test whether compression-tail's insufficiency is universal across feature spaces — pre-registered as a follow-up below.

6. **No Bonferroni concern triggered.** The pre-registered Bonferroni-3 (linear/quadratic/two-piece) was set up to control multiple-constraint testing. We tested only the two-piece form per task brief; Bonferroni adjustment would only further loosen significance thresholds, which does not change the deterministic 0/90 verdict.

## §6. Cross-references

**Parents:**
- `findings/phase-b-hypotheses/h-new-660-compression-tail-gradient.md` — established the compression-tail law (R²=0.986, β=−0.0124).
- `findings/phase-b-hypotheses/cross-finding-011-mushaf-fisher-rao-confirmed.md` — established canonical's L_mushaf=85.76 ≈ 1.107 · L_2opt.

**Sister findings (other architectural principles):**
- `findings/phase-b-hypotheses/h-new-130-fisher-rao-residuals.md` (root-axis residuals: where the 11% concentrates).
- `findings/phase-b-hypotheses/cross-finding-018-four-principle-reduced-model.md` — multi-principle architecture.
- `findings/phase-b-hypotheses/cross-finding-021-mushaf-information-theoretic-optimality.md` — broader optimality framing.

**Conceptual neighbors:**
- `findings/phase-b-hypotheses/h-new-490-tiwal-inner-4.md` — Ṭiwāl / Awsāṭ / Mufaṣṣal as orthogonal grouping principle.
- `findings/phase-b-hypotheses/h-new-226-mushaf-order-scholarly-review.md` — classical scholarship on mushaf order.

## §7. Queued follow-ups

1. **H-NEW-690b** — Replicate on [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] (char-4-gram) and [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] (verselen) feature spaces. Does compression-tail's insufficiency hold across all three feature spaces?
2. **H-NEW-690c** — Add a SECOND constraint (e.g., Nöldeke chronological banding, or muqaṭṭaʿāt cluster). Does compression-tail + 1 more principle close the gap to 11%? This decomposes the multi-principle architecture quantitatively.
3. **H-NEW-690d** — Loosened-constraint variant: R² ≥ 0.85, β ∈ [−0.02, −0.005]. Confirms the law-shape is what matters (not just the loose direction).
4. **H-NEW-690e** — Cooler MH temperature (T=0.1) to test how close to canonical the constrained subset *can* get with strong TSP bias. Estimates the constrained-subset's TSP-frontier (best achievable residual under compression-tail).

## §8. Final statement

The compression-tail law ([[h-new-660-compression-tail-gradient|H-NEW-660]]) is a **consequence-envelope** of mushaf order, not its cause. Within that envelope, canonical is exceptional: it sits at residual 10.7%, while the typical compression-tail-respecting ordering sits at ~25%. Compression-tail accounts for ~40% of canonical's TSP-optimality; the remaining ~60% is carried by additional architectural principles (root-bridges, surah-groupings, ordering conventions) documented elsewhere in the project.

**This is good news for the multi-principle thesis** ([[cross-finding-018-four-principle-reduced-model|cross-finding-018]], [[cross-finding-021-mushaf-information-theoretic-optimality|cross-finding-021]]): the canonical mushaf is not reducible to a single low-dimensional descriptive law, but is a layered optimum across multiple orthogonal axes. [[h-new-690-causal-generative|H-NEW-690]] quantifies one layer's contribution and shows it is real but partial.

The NULL verdict here is honest, robust (3 alternate seeds), and constructive: it sharpens what the compression-tail finding does — and does not — claim about generative cause.

*wa-Allāhu aʿlam.*
