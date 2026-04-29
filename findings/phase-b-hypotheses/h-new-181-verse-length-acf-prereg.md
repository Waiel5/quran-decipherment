# [[h-new-181-verse-length-acf|H-NEW-181]] — Per-surah verse-length autocorrelation (pre-registration)

**Finding ID**: [[h-new-181-verse-length-acf|h-new-181]]-prereg
**Date**: 2026-04-17
**Agent**: autonomous-test-H-NEW-181
**Parents**: H-NEW-35 (corpus-wide verse-length ACF(1) z=+13.13), [[h-new-166-multi-scale-hurst|H-NEW-166]] (multifractal, within-surah/between-surah crossover at n≈50–100)
**Seed**: 20260419 (matches [[h-new-166-multi-scale-hurst|H-NEW-166]] / [[h-new-178-alpha-beta-manifold|H-NEW-178]] for cross-axis correlation reproducibility)
**Status**: PRE-REGISTERED BEFORE DATA ANALYSIS

## Background

H-NEW-35 aggregates verse-length autocorrelation across all 114 surahs, yielding a single +13σ signal at lag 1. [[h-new-166-multi-scale-hurst|H-NEW-166]] establishes that the long-memory structure is scale-dependent, with a rolling-Hurst regime change near n ≈ 50–100 verses — interpreted as a crossover from within-surah verse-level refrain/pericope rhythm to between-surah macro-structure.

This per-surah audit asks: **which surahs contribute the within-surah rhythmic signature?** Classical Balāghah (al-Sakkākī *Miftāḥ* pp. 527–540 on *īqāʿ*; al-Suyūṭī *Itqān* Nawʿ 59 on *fawāṣil*) suggests short oath-laden Meccan surahs and muqaṭṭāʿat-prefixed chapters have distinctive *fāṣila* rhythms — they should cluster at the top of a per-surah ACF ranking.

## Rules tuple

- Orthography: `no-tashkeel`
- Verse length metric: **letter-count** per verse (matches H-NEW-35 primary: `[\u0621-\u064A]`)
- Verse numbering: hafs-kufan (6236 verses)
- Basmala policy: basmala counted only in surah 1 (H-NEW-35 convention)
- Minimum surah length: **N ≥ 20 verses** (task spec) → pre-expect ~90 surahs included
- RNG seed: 20260419

## Method

### Per-surah statistics

For each surah with N ≥ 20 verses, on the verse-length sequence L[1..N]:

1. **ACF(k) for k ∈ {1,…,10}**: `ρ(k) = Corr(L[1..N-k], L[k+1..N])` using Pearson.
2. **PACF(k) for k ∈ {1,…,5}**: Durbin-Levinson recursion (ψ_kk values).
3. **Ljung-Box Q(m)** with m = 10:
   `Q = N(N+2) · Σ_{k=1..10} ρ(k)² / (N−k)`
   Reference null: Q ~ χ²(10) under white noise.
   Report `p_LB = 1 − F_χ²₁₀(Q)`.

### Ranking

- **Top-10 most rhythmic**: by Ljung-Box Q (primary), cross-checked against max |ρ(k)| for k=1..5 and against ρ(1) alone.
- **Bottom-10 anti-rhythmic**: lowest Q / highest p_LB (plus any surahs where ρ(1) < −0.2 → alternating-length structure).

### Ljung-Box null calibration via phase-shuffle

For each included surah, draw N_PERM = 2000 random permutations of L[1..N], compute Q per permutation, derive empirical p-value `p_perm = (1 + #{Q_shuf ≥ Q_obs}) / (1 + N_PERM)`. Use this as the honest p since χ²(10) is asymptotic and many surahs are short.

### Pre-registered Bonferroni-2 plan

**Family** `[[h-new-181-verse-length-acf|h-new-181]]-per-surah-rhythm` with k=2:

1. **Primary (leg A)**: Does the **top-10** most-rhythmic set (by permutation p_LB) show **enrichment for muqaṭṭāʿat OR classical-Meccan** vs the non-top-10 complement? Fisher exact 2-sided test on 2×2 (top-10 vs rest) × (muq-or-Meccan vs neither). α_bon = 0.025. Pre-expected direction: muq OR Meccan > baseline rate.
2. **Secondary (leg B)**: Does per-surah Ljung-Box Q correlate with (a) [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] dispersion (per-surah) AND/OR (b) [[h-new-178-alpha-beta-manifold|H-NEW-178]] α/β-residual (distance from linear α = −3.526β + 3.689)? Spearman ρ, 2-sided. α_bon = 0.025. No pre-committed sign — exploratory covariate check.

The overall finding passes Bonferroni-2 if **both** legs pass at α=0.025. A single-leg pass is reported as PARTIAL.

### Baseline rate (for leg A)

Across included surahs (N ≥ 20), the "muq OR Meccan" baseline rate is pre-computed BEFORE the top-10 is frozen, so the Fisher 2×2 is well-defined. Muqaṭṭāʿat: 29 standard surahs (2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68). Meccan/Medinan from `data/revelation-order.csv`.

### Cross-axis correlation spec

- [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] dispersion source: `csv/h-new-168-per-surah-dispersion.csv` (114 rows).
- [[h-new-178-alpha-beta-manifold|H-NEW-178]] α/β source: `csv/h-new-172-per-surah.csv` (93 rows).
- [[h-new-178-alpha-beta-manifold|H-NEW-178]] (α,β) residual: distance from the fit line α = −3.526β + 3.689 (absolute residual on α).

Report Spearman ρ per axis with Bonferroni-within-leg-B=2, so effective α for each axis = 0.0125 (but the Bonferroni-2 family treats leg B as a single "any-axis" test: pass if **either** axis clears 0.025 after Bonferroni-within-leg).

## Garden-of-forking-paths log (pre-data-touch)

Choices fixed **before** analysis:
- Metric = letter-count per verse (matches H-NEW-35); no swap to word-count.
- Min surah length = 20 (task spec, not optimized).
- Q with m=10 (task spec: lags 1–10).
- PACF Durbin-Levinson recursion (standard).
- Null: phase-shuffle within-surah, 2000 permutations (task spec for H-NEW-35 used 1000; I use 2000 per surah because per-surah p-values need tighter resolution).
- Top/bottom-10 cardinality = 10 (task spec).
- Muqaṭṭāʿat list = canonical 29 (no alternatives considered).
- Meccan = `period == 'Meccan'` in revelation-order.csv (Nöldeke-standard, single source).
- Fisher exact = scipy.stats.fisher_exact 2-sided (not Boschloo / mid-p).
- Spearman ρ = scipy.stats.spearmanr 2-sided.
- α/β residual = orthogonal distance to α = −3.526β + 3.689 on α-axis (not perpendicular distance); this matches how [[h-new-178-alpha-beta-manifold|H-NEW-178]] residualizes.
- Bonferroni family k=2 (leg A + leg B), α_bon=0.025 per leg.
- Leg B passes on "any-axis" rule (at Bonferroni-within α=0.0125 per axis); does NOT require BOTH axes.
- No optional stopping: all 2000 permutations run for all qualifying surahs regardless of early pass/fail.

### Decision table

| Leg A (muq-or-Meccan enrichment) | Leg B (any axis correlation) | Verdict |
|---|---|---|
| p < 0.025 | p_best < 0.025 | PASS |
| p < 0.025 | p_best ≥ 0.025 | PARTIAL-A |
| p ≥ 0.025 | p_best < 0.025 | PARTIAL-B |
| p ≥ 0.025 | p_best ≥ 0.025 | NULL |

## Artifacts (planned)

- `scripts/h_new_181_per_surah_acf.py` — analysis script
- `findings/phase-b-hypotheses/csv/h-new-181.json` — full numerical output
- `findings/phase-b-hypotheses/csv/h-new-181-per-surah.csv` — per-surah table
- `findings/phase-b-hypotheses/h-new-181-verse-length-acf.md` — finding report

## Checklist

- [x] Rules tuple pre-registered
- [x] Lag set (1..10 ACF, 1..5 PACF), N_PERM=2000, seed all pre-declared
- [x] Bonferroni family k=2 pre-declared with α_bon=0.025 per leg
- [x] Direction for leg A pre-committed (muq OR Meccan > rest); leg B 2-sided exploratory
- [x] Top/bottom cardinality = 10 pre-declared
- [x] Muqaṭṭāʿat list and Meccan source pre-declared
- [x] Garden-of-forking-paths log written before any data touch
- [ ] Analysis executed
- [ ] Honest verdict published
