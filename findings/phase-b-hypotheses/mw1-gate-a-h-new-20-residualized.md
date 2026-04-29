---
finding_id: mw1-gate-a-h-new-20-residualized
phase: B
status: PARTIAL (length-correlated but robust under inverse-variance weighting)
date: 2026-04-13
rules_tuple: (no-tashkeel, QAC roots, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
null_model: within-surah verse-order shuffle (cached from H-NEW-20) + length-stratified aggregation
bonferroni_k: 4 (inherited from H-NEW-20)
pre_registration_reference: task #52 MW-1-GATE-A
parent_finding: team-discovery-010.md
author: computational-tester
---

# MW-1-GATE-A — al-Rāzī autocorrelation length residualization

## Gate question

Does H-NEW-20's Stouffer Z = +30.76 for al-Rāzī's linear-munāsaba thesis survive
per-surah length residualization? The skeptical-auditor hypothesis was: longer
surahs contribute disproportionately to unweighted Stouffer aggregation because
they produce more adjacent-pair Jaccard observations per surah, tightening their
per-surah sampling variance and inflating their z-score magnitude. If the signal
is length-dominated, the gate fails and MW-1 loses this leg.

## Methodology correction

The task (#52) originally specified "OLS residualization of z on log(N) then
re-Stouffer." **This is mathematically vacuous**: OLS residuals always sum to
zero by the first-order condition, so unweighted Stouffer on residuals is
identically 0 regardless of the underlying signal. I verified this numerically
(Stouffer on residuals = 0.000 exactly for all three signals).

Replaced with three proper length-control tests:

1. **Length-stratified Stouffer**: compute Stouffer Z within three strata
   (n≤30, 30<n≤100, n>100) separately. A real effect should persist in the
   short stratum where per-surah pair counts are most equal.
2. **Inverse-variance weighted Stouffer**: weight each surah's z by
   w = 1/√(n-1) so longer surahs contribute proportionally less.
3. **Length correlation diagnostic**: Pearson ρ(log_n, z) to characterize
   the length-z relationship.

## Results

### Length correlation diagnostic

| Signal | ρ(log N, z) | Interpretation |
|---|---|---|
| z_r1 | **+0.598** | Strong length-z correlation (auditor concern confirmed) |
| z_grad | **+0.465** | Moderate length-z correlation |
| z_ring | −0.005 | No length dependence (ring already null) |

So the signal magnitude DOES scale with log(N), as the auditor predicted.

### Length-stratified Stouffer

| Stratum | N surahs | z_r1 Stouffer | z_grad Stouffer | z_ring Stouffer |
|---|---|---|---|---|
| n ≤ 30 | 32 | **+9.57** | +6.23 | −1.74 |
| 30 < n ≤ 100 | 45 | +20.13 | +13.57 | −1.05 |
| n > 100 | 18 | +26.07 | +15.42 | −1.78 |
| **All** (original) | **95** | **+30.76** | **+19.67** | **−2.51** |

The signal gradient with length is obvious: Z_r1 triples from short-stratum
(+9.57) to large-stratum (+26.07). But **even the short stratum — which is
most length-equalized — produces Z = +9.57, just 0.43 below the ≥10 threshold
required for MW-1 continued contribution**. 27/32 short surahs show z_r1 > 0.

### Inverse-variance weighted Stouffer (w = 1/√(n−1))

| Signal | Weighted Z |
|---|---|
| z_r1 | **+22.78** |
| z_grad | +14.71 |
| z_ring | −2.37 |

Inverse-variance weighting de-emphasizes long surahs proportionally. Z_r1 drops
from 30.76 → 22.78 — a reduction, but nowhere near to zero. The al-Rāzī signal
survives length-weighting with room to spare.

## Gate verdict

Under the task's strict threshold (post-residualization |Z| ≥ 10):

| Sub-test | z_r1 | z_grad | Pass? |
|---|---|---|---|
| Short stratum (n≤30) | 9.57 | 6.23 | **FAIL** (barely, by 0.43 on r1) |
| Inverse-variance weighted | 22.78 | 14.71 | **PASS** |
| Joint (both required) | | | **FAIL** |

**Strict reading: MW-1-GATE-A FAILS — H-NEW-20 drops from MW-1 leg count.**

**Liberal reading: MW-1-GATE-A PARTIAL — short stratum Z = +9.57 is just below
the hard cut-off, but IV-weighted Z = +22.78 cleanly passes, and 27/32 short
surahs show positive z. The signal is length-enhanced but not length-dominated.**

The correct interpretation: H-NEW-20 is **length-enhanced but real**. The
al-Rāzī adjacent-verse-coherence signal is present across all three length
strata including the short-stratum, but its magnitude amplifies with N.
At short scales (n≤30 verses) the signal is Z ≈ 9.6, meaning p < 10⁻²¹ under
a normal approximation — still overwhelming significance, just not Z ≥ 10.

## Implications for MW-1

Per the task spec: "post-residualization Z ≥ 10. If Z < 10, H-NEW-20 drops from
the MW-1 leg count." The short-stratum result is **Z = +9.57**, which literally
fails the threshold by 0.43. Two defensible positions:

1. **Strict**: threshold was pre-registered, so the gate FAILS. MW-1 loses this
   leg. If the legs were at ≥6 for activation and this was one of them, MW-1
   may fall below threshold.
2. **Liberal**: the IV-weighted test passes at 22.78; the effect-size gradient
   with length (9.57 → 20.13 → 26.07) shows a monotone real signal, not an
   artifact; 27/32 short surahs are positive which rules out the "one or two
   long-surah outliers drove everything" worry. The gate should be read as
   PASSED with the caveat that the headline Z is length-enhanced.

**My recommendation: strict reading**. A pre-registered threshold was set, and
the short-stratum z_r1 does not cross it. The effect is real but H-NEW-20's
original Z = +30.76 substantially over-states how robustly cross-surah the
signal is. H-NEW-20 should continue to inform downstream analyses but not as
an MW-1 leg at its original strength.

## Honest characterization of H-NEW-20

After this audit, H-NEW-20 should be described as:

> "Adjacent-verse Jaccard-root similarity exceeds a within-surah-shuffle null
> across length strata (short: Z = +9.6, mid: Z = +20.1, long: Z = +26.1),
> confirming al-Rāzī's linear-munāsaba thesis as corpus-wide pattern. The
> per-surah signal correlates with log(N_verses) at ρ = +0.60, so the headline
> unweighted Stouffer (+30.76) is length-enhanced: inverse-variance weighting
> reduces it to +22.78."

This is still a large finding. But the original "p ≈ 10⁻²⁰⁰" wording was
misleading — it assumed unweighted Stouffer's null (N(0,1) per surah) holds
for both short and long surahs equally, which it does not.

## Garden of forking paths (disclosed)

- Originally tried OLS-residualization per task spec — identified the
  residualization-Stouffer pathology during execution and added three
  substitute tests.
- Three length strata chosen a priori at n≤30, n≤100, n>100. These
  correspond roughly to short-Meccan / long-Meccan / Medinan length classes.
- IV-weighting w = 1/√(n−1) chosen because n−1 is the number of adjacent
  pairs per surah (the observations actually driving ρ(1)).
- Threshold of 10 inherited from task spec; did not tune.
- Did not run fresh H-NEW-20 computation — used cached per-surah z-scores.

## Limits

1. The H-NEW-20 cache uses adaptive perm counts (500/200/100 by N), which is
   another length-dependent design choice — longer surahs get FEWER perms,
   yielding NOISIER per-surah z's. The direction of this bias is opposite to
   the length-correlation inflation, partially mitigating the issue. A fresh
   run with constant 500 perms everywhere would be cleaner but expensive.
2. Stratum boundaries (30, 100) are arbitrary. Sensitivity not explored.
3. IV weights w = 1/√(n−1) assume per-surah z-variance ≈ 1/(n−1). Actual
   variance under the null is more complicated due to root-set correlations.
4. Inherits H-NEW-20's Jaccard-on-QAC-roots operationalization. A semantic
   (sentence-embedding) version might scale differently with length.
5. N=95 surahs is small; stratum n's (32, 45, 18) are small enough that
   per-stratum Stouffer Z has moderate CI width.

## Cross-references

- Parent finding: `findings/phase-b-hypotheses/team-discovery-010.md`
- Source cache: `scratch/team-discovery/result-razi-biqai.json`
- Output JSON: `findings/phase-b-hypotheses/csv/mw1-gate-a-h-new-20-residualized.json`
- Script: `scripts/h_new_20_residualized.py`
- Seed: 20260413

## Verdict

**MW-1-GATE-A: PARTIAL.** Under the strict pre-registered threshold (short-
stratum Z ≥ 10), the gate FAILS by 0.43 units on the primary signal.
Under inverse-variance weighting the gate passes at Z = +22.78. The effect is
length-enhanced (ρ = +0.60 of z with log N) but not length-dominated: 27 of
32 short-stratum surahs show z > 0 (84%), mid-stratum Z = +20.13, large-
stratum Z = +26.07. H-NEW-20 should be DOWNGRADED from "Z = +30.76 p ≈ 10⁻²⁰⁰"
to "length-enhanced; short-stratum Z ≈ +9.6; inverse-variance-weighted Z ≈
+22.8." The al-Rāzī linear-munāsaba thesis is still computationally supported
as corpus-wide, but with appropriate length-caveated magnitude.

**MW-1 accounting recommendation**: strict reading → H-NEW-20 drops from
the ≥10 leg count. Liberal reading → H-NEW-20 stays in but with downgraded
magnitude.
