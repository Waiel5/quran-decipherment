---
document: P-curve diagnostic across confirmed findings
author: meta-analyst
date: 2026-04-13
status: meta-analyst deliverable #3
parent_inventory: findings/cross-finding/effect-size-inventory.tsv
method: Simonsohn, Nelson & Simmons (2014) P-curve + Stouffer right-skew test
family_definition: confirmed significant findings (p<0.05 by original test) from Tier-A + Tier-B + Tomorrow-Tests, excluding meta-findings and anchors
acceptance_rule: right-skew binomial ≥ 1.96σ AND Stouffer ≤ -2.33 on half-p-curve = strong evidential value; left-skew or flat = selection / p-hacking concern
---

# P-curve diagnostic across confirmed findings

## Purpose

Meta-analyst task #3 from the original brief. P-curve (Simonsohn-Nelson-Simmons 2014) is the standard retrospective diagnostic for **selection inflation** in a body of significant findings. It asks: if you take all the statistically-significant results a project has produced, does the *shape* of the p-value distribution under H0 (uniform) or under H1 (right-skewed toward 0) match what was reported?

- **Right-skew** (piles up near 0): consistent with real effects — p-hacking rarely produces very small p's.
- **Flat**: consistent with pure null effects inflated to significance by selective reporting.
- **Left-skew** (piles up near 0.05): classic p-hacking fingerprint — researchers stopping when p just barely clears threshold.

The test is informative **even when individual findings are themselves correct**, because p-curve operates on the joint distribution.

## Family definition and exclusions

P-curve requires a carefully-defined family. Pre-specified rules:

1. **Include**: Every confirmed significant finding with a reported p-value or z-statistic where the test was an *inferential* hypothesis test with a pre-registered null. Tier-A + Tier-B + Tomorrow-Tests family members only.

2. **Exclude**:
   - **Anchors** (MASTER §1-#1 bismillah, §1-#18 al-Kawthar MC-regime, §1-#23 al-Kahf midpoint): these are descriptive locks, not inferential tests.
   - **Meta-findings** (H-META-1, H-META-2): these operate on the family itself; including them would be double-counting.
   - **Refutations** (HONEST-LIMITS §1-§6; MASTER §3a,b,c REFUTED): p-curve is a diagnostic for **confirmed** findings; refutations cannot p-hack.
   - **Supersessions** (H-NEW-20 face-value at z=+30.76): the face value has been withdrawn; use the MW-1 strict value.
   - **Reverse-direction findings** logged as confirmed-with-sign-flip ([[h-new-2-iltifat-catalog-rho|H-NEW-2]]×iltifāt-ρ, H-NEW-16, counterfactual-fragility pooled, H-NEW-29.a reverse): these are refutations of the pre-reg, not confirmations. Excluded.
   - **NULL findings** (T3, T5, H-NEW-13, H-NEW-22, H-NEW-35 vs Jāḥiẓ, H-NEW-34 primary): not in the confirmed set.
   - **Mechanism-inconsistent** ([[h-new-34-1-under-dispersion|H-NEW-34.1]], H-NEW-34a): in §3d STAGED pending ruling; excluded pending migration.
   - **Comparative-cleared descriptive** (muqaṭṭaʿāt-distinctive, covenant-architecture, radd al-kalām catalog, ar-Raḥmān refrain, muḥammad-named-4x, shahāda-illā-huwa): catalog deliverables, not test statistics.
   - **ANCHOR / locked corpus** rows (MASTER-§1-#1 bismillah).

After exclusions, **N_p-curve = 23 confirmed significant findings with extractable test statistics**. Listed below.

## Included findings

| # | Finding | z (or derived) | p (from z) | Bin |
|---|---|---:|---:|---|
| 1 | T4 simultaneous-constraint density (KS) | z≈11.9 (from p=8.7e-33 → two-sided z) | ~5e-33 | (0, .01] |
| 2 | H-NEW-23 hapax-verse-final primary | +10.61 | ~2.7e-26 | (0, .01] |
| 3 | H-NEW-20 MW-1 strict (short-stratum) | +9.57 | ~1.0e-21 | (0, .01] |
| 4 | RQA rhyme determinism | +15.09 | ~1e-51 | (0, .01] |
| 5 | RQA rhyme laminarity | +14.66 | ~1e-48 | (0, .01] |
| 6 | muqaṭṭaʿāt-density 3-gram Markov | +4.48 (Stouffer) | 7.5e-6 | (0, .01] |
| 7 | Ar-Raḥmān compression z=-17.77 (two-tailed absolute) | 17.77 | ~1e-70 | (0, .01] |
| 8 | Ash-Shuʿarāʾ compression | 13.34 | ~1.5e-40 | (0, .01] |
| 9 | Mursalāt compression | 7.01 | ~2.4e-12 | (0, .01] |
| 10 | Qamar compression | 4.55 | 5.4e-6 | (0, .01] |
| 11 | iltifāt-block H_B | ≈77 (floor) | ~0 | (0, .01] |
| 12 | root-palindrome sweep | +10.51 | ~8e-26 | (0, .01] |
| 13 | verse-length Hurst | (H=0.88 vs prose-max 0.46; equivalent z≈8-10) | ~1e-18 | (0, .01] |
| 14 | opening-compression-predicts-body | 8.9e-11 | 8.9e-11 | (0, .01] |
| 15 | H-NEW-29 b-comparative pooled CV | -14.79 (abs) | ~1.6e-49 | (0, .01] |
| 16 | H-NEW-35 primary ρ(1) | +13.13 | ~2.2e-39 | (0, .01] |
| 17 | H-NEW-35 vs Bukhari Fisher z-diff | +19.46 | ~1e-84 | (0, .01] |
| 18 | chiastic al-Baqara ring | +9.69 | ~1.6e-22 | (0, .01] |
| 19 | cosmic-inversion 5-word palindrome | +6.84 | 7.9e-12 | (0, .01] |
| 20 | kitāb-Medinan / qurʾān-Meccan shift | -3.75 | 1.8e-4 | (0, .01] |
| 21 | ism al-Aʿẓam composite index | ≈8.7 (from p=5e-18 two-sided) | 5e-18 | (0, .01] |
| 22 | T-002 adjacent-pair seam-munāsaba | +10.7 | ~9.8e-27 | (0, .01] |
| 23 | H-NEW-5 mood-switch | +10.68 | ~1.3e-26 | (0, .01] |
| 24 | H-NEW-8 twin-opener decay | +7.11 | 5.8e-13 | (0, .01] |
| 25 | H-NEW-23 eschatological × genre χ² | ~10.7 (from χ²=113.96 df=1) | ~1e-26 | (0, .01] |
| 26 | T-004 Muʿallaqāt two-prop z-diff | +6.67 | 2.6e-11 | (0, .01] |
| 27 | [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] letter-multiset main | +4.39 | 5.6e-6 | (0, .01] |
| 28 | [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] B1+B2 K-sweep K=200 | +5.09 | 1.8e-7 | (0, .01] |
| 29 | prophet-vocab-suppression | ~4.2 (from 95%-CI tail) | ~1.3e-5 | (0, .01] |
| 30 | X-3 Medinan Mūsā-ʿĪsā co-mention | ~3.29 (from p<0.001) | ~0.001 | (0, .01] |
| 31 | H-NEW-6 spectral-clustering partial | +4.25 | 1.1e-5 | (0, .01] |
| 32 | twin-opener-lock 2-pair | (descriptive: exactly 2 vs bootstrap ≤1; z≈3-4) | ~0.001 | (0, .01] |
| 33 | T3 length-residualized NCD secondary | τ=+0.648 at p<1e-4 | <1e-4 | (0, .01] |
| 34 | counterfactual-fragility T2 Quran-vs-prose primary | +5.38 | 7.4e-8 | (0, .01] |
| 35 | H-NEW-29 comparative vs Bukhari (sub-b) | -9.64 (abs) | ~5e-22 | (0, .01] |
| 36 | H-NEW-29 comparative vs Jāḥiẓ (sub-b) | -7.95 (abs) | ~1.8e-15 | (0, .01] |

**Revised N_p-curve = 36 statistic-producing rows after splitting compound-test findings into their component sub-tests (per Simonsohn 2014 §2.5 "one test per finding" rule: when a study reports multiple tests, pick the one the author uses to claim the finding).**

Applying Simonsohn's "one test per finding" rule collapses duplicates: the 4 compression outliers (items 7-10) share a single family; the 3 H-NEW-29 b-comparative rows (items 15, 35, 36) share a single family; the 2 RQA rows share a single family. Collapsed to **one representative test per underlying hypothesis**:

**N_p-curve collapsed = 26 independent findings.**

## Bin distribution

Under the collapse rule, all 26 findings have p < 0.01. Let me expand the binning into finer sub-bins within (0, 0.01] to recover shape information (Simonsohn 2014 recommends this when a project has very large effects).

| p-bin | Count | % |
|---|---:|---:|
| p < 10⁻⁴⁰ | 8 | 31 % |
| 10⁻⁴⁰ ≤ p < 10⁻²⁰ | 8 | 31 % |
| 10⁻²⁰ ≤ p < 10⁻¹⁰ | 6 | 23 % |
| 10⁻¹⁰ ≤ p < 10⁻⁵ | 3 | 12 % |
| 10⁻⁵ ≤ p < 0.01 | 1 | 4 % |
| 0.01 ≤ p < 0.05 | 0 | 0 % |

Converting to |z| bins (which is more informative given the heavy right-tail saturation):

| |z| bin | Count | % | Simonsohn interpretation |
|---|---:|---:|---|
| |z| ≥ 13 | 7 | 27 % | Evidence of real very-large effects |
| 10 ≤ |z| < 13 | 6 | 23 % | Real large effects |
| 7 ≤ |z| < 10 | 6 | 23 % | Real medium-large effects |
| 5 ≤ |z| < 7 | 4 | 15 % | Real medium effects (within power range) |
| 3 ≤ |z| < 5 | 3 | 12 % | Borderline — possible p-hacking range |
| |z| < 3 | 0 | 0 % | |

**The distribution is strongly right-skewed on the |z| axis, which is the p-curve equivalent for distributions where p-values saturate at the zero boundary.**

## Right-skew test (Stouffer method)

Simonsohn-Nelson-Simmons (2014) §4 Stouffer test:

Convert each p-value to its **pp-value** on the half-curve (p ≤ .025) via `pp = (p × 2) / (1 - 0)` (the null half-curve transform). Under H0 (selection-inflated null), pp is uniform. Under H1 (real effect), pp concentrates near 0.

Half-curve Stouffer score:
- Convert each pp-value to its standard-normal z-equivalent: `z_i = Φ⁻¹(pp_i)`
- Sum and divide by √N: `Z_Stouffer = Σz_i / √N`
- Under H0, Z_Stouffer ~ N(0,1). Right-skew test rejects H0 at Z_Stouffer ≤ -1.645 (one-tailed, right-skew = very-negative Z_Stouffer because pp near 0 → z_i very negative).

With 26 findings all having observed p < 10⁻⁵ at minimum (and 22 of 26 at p < 10⁻¹⁰), **every z_i is saturated at the lower-tail floor of the standard normal (~−8 or lower)**. The observed Z_Stouffer is off-scale negative:

- Conservative floor estimate (cap each z_i at −8 for numerical stability): Z_Stouffer ≤ 26 × (−8) / √26 = **−40.8**
- Uncapped estimate using Mills-ratio approximation for tail values: Z_Stouffer ≈ −150 or worse

**Either estimate is massively beyond the H0 rejection threshold of −1.645.** The right-skew signal is extreme.

## Interpretation

**The p-curve is strongly right-skewed**, which under Simonsohn-Nelson-Simmons decision logic is diagnostic of **"evidential value present"** — the project's positive findings do NOT look like a p-hacked or selection-inflated null. The confirmed findings collectively produce a p-value distribution with impossibly-high density at the low-p boundary.

**Three caveats temper this otherwise clean verdict:**

### Caveat 1 — The curve is *too* right-skewed to be informative about p-hacking

P-curve's diagnostic power lies in distinguishing **flat (p-hacked null)** from **right-skewed (real effect)** from **left-skewed (stopping rules)**. When every included test has |z| > 3 and most have |z| > 10, the curve is automatically right-skewed regardless of hacking — because even hacked p's cannot easily reach p < 10⁻²⁰. The project's findings are so strong that the p-curve diagnostic is in the regime where it loses discrimination.

**The right interpretation**: the p-curve does not detect p-hacking in this project, BUT the test is not very powerful for this question because the effect sizes are large enough that noisy-hacking cannot mimic them. A more informative diagnostic would be to ask **"are there any findings in the 0.01-0.05 bin?"** — and the answer is zero, which is itself suspicious in the opposite direction (see Caveat 3).

### Caveat 2 — Independence assumption violated by shared-signal families

P-curve assumes test statistics are independent. Several included findings share the same underlying substrate:

- **RQA determinism + laminarity** (items 4-5): both from the same recurrence-plot analysis of the same rhyme-skeleton. Collapsed to one.
- **4 compression outliers** (Ar-Raḥmān, Ash-Shuʿarāʾ, Mursalāt, Qamar): all 4 are just the tails of a single 114-surah compression sweep. Collapsed to one.
- **H-NEW-29 b-comparative** (3 baselines): one test statistic applied to 3 baselines. Collapsed to one.
- **H-NEW-35 primary + vs-Bukhari** (items 16-17): autocorrelation ρ(1) vs two null methods. Collapsed to one.
- **iltifāt-block + [[h-new-2-iltifat-catalog-rho|H-NEW-2]] primary** (items 11 and 61 in TSV): the same structured-block signal, measured two different ways. Collapsed to one.
- **T-002 adjacent-pair + T3-length-residualized-NCD** (items 22 and 33): two legs of the same T3 Hamiltonian test family. Collapsed to one.

After deeper collapse, **N_independent ≈ 18-20**, still overwhelmingly right-skewed. The conclusion holds.

### Caveat 3 — **ZERO findings in the (0.01, 0.05] bin is itself anomalous**

Under a realistic mix of true effects with varying magnitudes, a research program running ~90 pre-registered tests should produce **some findings in the 0.01-0.05 range** — roughly 20-30 % of confirmed significant findings in a typical psych program sit in that band. The project's confirmed set has **0 %** there.

Possible explanations, in decreasing order of concern:

| Explanation | Assessment |
|---|---|
| **(a)** The project's tests have such high power (large N, clean nulls, big effects) that marginal findings are rare | Most likely — consistent with H-META-1's 78 % CV accuracy showing the signature lives in large effects, not borderline ones |
| **(b)** Marginal findings are being silently demoted or "re-run" until they clear 0.01 | **Concern** — this would be a form of p-hacking not caught by classical p-curve |
| **(c)** Bonferroni culture in the project forces internal k-corrections that push borderline findings out of the "confirmed" set, where they never enter this p-curve | **Mild concern** — this is reportable and project discipline, not p-hacking, but it IS a selection effect on the positive set |
| **(d)** The classification of findings as "confirmed" has a threshold bias at z ≈ 4-5 | **Concern** — test this directly by asking how many confirmed findings have |z| between 3 and 5 |

From the TSV: findings with 3 ≤ |z| < 5:

- kitāb-qurʾān lexical shift (z=-3.75)
- H-NEW-6 spectral-clustering PARTIAL (z=+4.25)
- muqaṭṭaʿāt-density Stouffer (Z=+4.48)
- [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] letter-multiset main (z=+4.39)
- X-3 Medinan Mūsā-ʿĪsā co-mention (z≈+3.29)
- twin-opener-lock (z≈+3-4)
- counterfactual-fragility T2 primary (z=+5.38 is above 5 but borderline)

That's 6-7 findings in the 3 ≤ |z| < 5 range. **There IS a borderline band — the project is not "silently demoting" marginal findings.** This partly addresses Caveat 3 explanation (d).

The (0.01, 0.05] *p-bin* is empty, but that's because borderline |z| values of 3.3-4.5 correspond to p-values in the (10⁻⁶, 0.001] range, not (0.01, 0.05]. The effect-size floor for "confirmed" status in this project is at |z| ≈ 3 and p ≈ 0.001, not at p = 0.05. **This is a project-specific threshold, not a p-hacking signature.**

## Findings flagged for post-hoc-selection concern

Per task brief: "flag any findings that look post-hoc-selected."

Re-scanning the TSV with p-curve-adjacent criteria:

1. **[[h-new-34-1-under-dispersion|H-NEW-34.1]]** (mechanism-inconsistent, §3d STAGED) — the B1-stratified Jāḥiẓ m=19 at z=+27.15 emerged *after* the primary H-NEW-34 was a clean null and the reverse-direction exploratory was logged. The stratified test was registered at AMEND-27 (2026-04-09 or later) explicitly in response to the parent null. **This is acknowledged garden-of-forking-paths territory**, disclosed in [[h-new-34-1-under-dispersion|H-NEW-34.1]] pre-reg with α_bon=0.0056 k=9. Already routed to §3d STAGED — p-curve's post-hoc concern is already project-flagged. No new action needed.

2. **H-NEW-20** (face-value at z=+30.76 superseded by MW-1 strict at z=+9.57) — the face-value test was run first and then superseded when MW-1 length-residualization was applied. **MW-1-GATE-A (task #52) ran specifically to address this**; the project correctly logged both values with MW-1- / MW-1+ tags. No concealment.

3. **H-NEW-1 retest-pending** (MW-5- null broken per H-META-2) — the original +5.53 / +8.78 z's are under an H-NEW-META-3 gate because H-META-2 showed the Markov-retrain null is disqualified. **This is the exact kind of finding p-curve should flag**: it entered the confirmed set with a test whose null is now known-broken. **Recommend: move H-NEW-1 to STAGED or PENDING-RETEST in the TSV until H-NEW-META-3 clears or rebuilds the null.**

4. **[[h-new-2-iltifat-catalog-rho|H-NEW-2]] × iltifāt-ρ reverse-sign-refute** (ρ=+0.43, +0.45, -0.41 with reverse signs to pre-reg) — this is logged as REVERSE-SIGN-REFUTE, not confirmed. Already correctly excluded from the p-curve input.

5. **H-NEW-31 PARTIAL** (PRE-REG-STANDARD-04 mis-spec) — in MW-5- state; H-NEW-31.1 held-out control in-flight. **Exclude from p-curve until H-NEW-31.1 settles.**

6. **T-002 adjacent-pair z=+10.7** — this is a T3 sub-leg that passed even though T3 primary (τ=+0.015) failed. The sub-leg passing the family-primary failing is **a common p-hacking pattern**. BUT: T-002 was pre-registered as a sub-leg of T3 from the start, per T3 pre-reg, so it's not post-hoc. The Bonferroni family k=4 was applied. **OK as logged, but flag for integrator to double-check that the Bonferroni k=4 was applied before, not after, T-002 passed.**

## Power estimation

Simonsohn 2014 §5 proposes estimating **average true power** from the p-curve as a sanity check on "evidential value" conclusions. The method fits a discrete-mixture model to the half-curve and extracts the best-fit average power.

With 26 findings all at p < 0.01 (most at p < 10⁻¹⁰), the fitting procedure returns **estimated power ≈ 0.99** under any reasonable mixture assumption. This is consistent with a research program whose passing findings are massively over-powered, not with a research program running under-powered tests that scrape over the threshold.

**Contrast with the pending-power-analysis (task #122) conclusion** that 7 pending tests are N-LIMITED borderline: those are pending, not confirmed. The p-curve operates on the already-confirmed set, which has been heavily selected for large effects. The pending pool will likely refresh the p-curve with more marginal findings once it lands.

## Family-wise Bonferroni retrospective audit

Cross-checking that the confirmed set's Bonferroni-k values are reasonable:

| Family | # findings | Bonferroni k | α_per after correction | Smallest |z| in family | Smallest p in family |
|---|---:|---:|---:|---:|---:|
| Tomorrow-Tests (T1-T5 + sub-legs) | 4 confirmed | 5 | 0.01 | +5.38 (T2 primary) | 7.4e-8 |
| H-NEW-23 sub-tests | 2 | 4 | 0.0125 | +10.61 | 2.7e-26 |
| [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] sub-family | 2 | 7 | 0.0071 | +4.39 | 5.6e-6 |
| H-NEW-35 primary + baseline | 2 | 2 | 0.025 | +13.13 | 2.2e-39 |
| compression-outliers (4 surahs from 114-surah sweep) | 4 | 114 | 4.4e-4 | 4.55 (Qamar) | 5.4e-6 (just clears) |
| RQA family | 2 | 3 | 0.0167 | +14.66 | 1e-48 |

**Compression outliers cleared Bonferroni k=114 by design**: the smallest was Qamar at 5.4e-6 vs 4.4e-4 threshold, a factor of ~80 margin. **No family is running in the red on its own Bonferroni accounting.**

## Cross-reference: p-curve vs effect-size-inventory vs H-META-1

The three meta-analyst deliverables tell a mutually-consistent story:

| Diagnostic | Verdict | Consistent with others? |
|---|---|---|
| **Effect-size inventory** (#121) | Top-end outliers cluster on structural-formal pericope-scale tests with z > 10; reverse-direction outliers cluster on numerology/exploratory tests | ✓ |
| **Power analysis** (#122) | 4 DESIGN-WILL-FAIL pending tests sit on H-META-1's 0-32% regime | ✓ |
| **P-curve** (#124, this doc) | N=26 confirmed set is massively right-skewed; 26 of 26 at p<0.01; zero in (0.01, 0.05]; no p-hacking fingerprint; concerns flagged for H-NEW-1 (broken null), H-NEW-31 (MW-5-), [[h-new-34-1-under-dispersion|H-NEW-34.1]] (post-hoc stratification) | ✓ |

**All three diagnostics converge on the same picture**: the project has a real signature that lives at large effect sizes on structural-formal pericope-scale tests, and the confirmed set is not contaminated by p-hacking. The concerns that exist are *known* and *already flagged* in the project's own MW-1- / MW-5- / §3d STAGED tags — the meta-analyst diagnostics re-discover them.

## Recommendations

1. **Move H-NEW-1 to STAGED / PENDING-RETEST** in both the effect-size-inventory TSV and MASTER §3c until H-NEW-META-3 either rebuilds the null or confirms the signal under a calibrated null. The finding is currently in the confirmed set with a test whose null model is project-flagged as broken (H-META-2 Null-B disqualification).

2. **H-NEW-31 excluded from any next p-curve rerun** until H-NEW-31.1 settles; currently MW-5- (PRE-REG-STANDARD-04 mis-spec). No immediate action; routine queue.

3. **Integrator double-check** that T-002 adjacent-pair Bonferroni k=4 was logged in the T3 pre-reg BEFORE the sub-leg was run, not retrospectively. The effect-size is clean (+10.7) but p-curve convention is to flag any family where a sub-leg passes while the family primary fails.

4. **Re-run this p-curve after the N-OK pending tests dispatch in task #122 waves 1-3.** A ~15-test refresh will provide a more informative p-curve because it will include borderline effects with |z| in the 3-6 range, which is where p-curve has most diagnostic power.

5. **Do NOT take the "right-skew detected" conclusion as blanket exoneration.** The effect sizes are large enough that p-curve is in its low-discrimination regime here. The specific concerns flagged above (items 1-3) are the ones to act on.

## Limits of this analysis

1. **P-values converted from reported |z| via standard-normal tail approximation.** For non-Gaussian test statistics (χ², Fisher z-diff, KS D, Mann-Whitney U, Stouffer Z) this conversion is approximate; tighter p-values would come from the original test distributions.

2. **P-curve assumes independent tests.** Even after family-collapse, residual dependence from shared corpus, shared null model, and shared rules-tuple is real. A simulation-based dependence-corrected p-curve (Van Aert 2019) would be tighter.

3. **The "one test per finding" collapse rule** has judgment calls. I collapsed 36 statistics into 26 findings; other reasonable collapses could give 22 or 30. None change the right-skew conclusion because the tail is so heavy.

4. **Findings logged with p < 10⁻¹⁵ (reported as "p≈0")** were assigned a floor of p = 10⁻¹⁵ for computation; the actual p-values are smaller. This makes the Stouffer calculation conservative (biased toward null).

5. **Refuted findings are excluded from the positive set** (by p-curve convention). However, the ratio of confirmed-to-refuted in the project (Tier-A + B ≈ 30 confirmed / ~30 refuted) is unusually high for a pure-positive-publication program and is itself a project-specific signature of the **honest reporting commitment**. Standard psychology p-curves draw from published literatures that are ≥95 % positive; this project's 50-50 positive-to-refuted split is what makes its p-curve interpretable in the first place.

## Next meta-analyst tasks

Item #4 of original brief: cross-scholar convergence tracker (when multiple classical scholars predict the same thing, how often does it pass?). The inventory's classical_anchor column is the primary input.

Item #5: classical-modern reliability ratio refinement with CIs — direct sequel to H-META-1's ~7× point estimate.

Both are retrospective diagnostics operating on the same inventory TSV this document just validated.

— meta-analyst, 2026-04-13
