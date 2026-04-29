---
date: 2026-04-13
analyst: meta-analyst
task: #127
status: live
inputs:
  - findings/phase-c-structures/h-meta-1-corpus-120.tsv (120-claim corpus)
  - findings/cross-finding/scholar-convergence-tracker.md (per-scholar frequency tables)
methodology:
  - Beta-binomial Jeffreys posterior on rate ratio (Beta(c+0.5, n-c+0.5))
  - 20,000-iteration Monte Carlo posterior sampling
  - Random seed 20260413 (project universal)
  - Three tracks for sensitivity
  - 5 sensitivity analyses
seed: 20260413
n_iter: 20000
---

# Classical-modern reliability ratio — CI refinement

Refinement of the previously-circulated **"~7×"** figure for the ratio of confirmable rates between classical-medieval and modern numerology/apologetic claims about the Quran. The legacy figure was a point estimate without a CI; this deliverable gives a Beta-binomial posterior with credible intervals across three definitional tracks and five sensitivity analyses.

**Headline:** the ~7× point estimate sits at the **21st percentile** of the broad-modern posterior — i.e., it is plausible but on the *low* side of what the data support. The posterior median is approximately **13×** under the broad-modern denominator and **~5×** under the named-modern denominator. The 95% credible interval is wide (3.5×–140× under the broad denominator) because the modern denominator (1 confirmed in 20 trials) is itself poorly constrained.

---

## 1. Why a posterior, not a frequentist CI

The bootstrap approach (resample with replacement) was tried first and found to misbehave for two reasons:

1. **Stratified bootstrap by scholar collapses.** When most strata are size-1 (al-Dānī, al-Jurjānī, al-Bāqillānī, al-Qurṭubī, etc. each have one claim), strata-internal resampling produces the same result every iteration, artificially narrowing the CI. The stratified bootstrap CI for Track B was [13.33, 17.78] — implausibly tight.
2. **Non-stratified bootstrap blows up.** When the modern denominator (1/20) gets resampled to 0/20, the ratio becomes ∞. The non-stratified Track A 95% CI was [1.75, 8.6×10⁸] — uninformative on the upper bound.

The Beta-binomial Jeffreys posterior solves both by:
- Treating each (numerator, denominator) as a Bernoulli process with an honest prior.
- Allowing the denominator's uncertainty to enter the posterior smoothly, including the realistic possibility that the true modern rate could be higher than 0.05 (with low but non-zero prior weight).
- Never producing infinite ratios because Beta(c+0.5, n-c+0.5) has zero density at p=0 even when c=0.

The Jeffreys prior Beta(0.5, 0.5) is the standard non-informative choice for Bernoulli parameters: invariant under reparameterization, mildly U-shaped (slight bias toward extreme values, which is conservative for a "ratio is large" claim), and resolves the c=0 pathology of MLE-based estimators.

---

## 2. Three tracks

| Track | Numerator | Denominator | Conf/N classical | Conf/N modern |
|---|---|---|---|---|
| A | named-classical scholars | named-modern scholars | 28/36 = 0.778 | 1/7 = 0.143 |
| B | named-classical scholars | all modern (named + anonymous numerology rows) | 28/36 = 0.778 | 1/20 = 0.050 |
| C | all classical-medieval (named + unnamed) | all modern | 48/62 = 0.774 | 1/20 = 0.050 |

**Why three tracks?** The "modern lane" can be defined narrowly (only post-1900 named scholars: Khalifa, Al-Kaheel, al-Nursī, Hassab-Elnaby, Farrin, Cuypers, Neuwirth/Wild) or broadly (also include anonymous modern-numerology rows like rahma=114, Yūsuf-sjn=12, the iʿjāz ʿilmī cluster, Fibonacci-in-Quran, Pascal's-triangle-in-Quran, Catalan-42, etc.). Each definition is defensible:

- **Narrow (Track A)** is what you want if you're asking "for any one named modern figure, how often are they right?"
- **Broad (Track B/C)** is what you want if you're asking "for the entire post-1900 Quranic numerology + iʿjāz ʿilmī literature considered as a class, how often does it confirm under audit?"

The legacy "~7×" figure was reported without specifying which denominator it used, so this deliverable computes both.

---

## 3. Posterior distributions on the ratio

Beta(c₁+0.5, n₁−c₁+0.5) / Beta(c₂+0.5, n₂−c₂+0.5), 20,000 Monte Carlo samples each.

### Track A — named-classical vs named-modern

| Quantity | Value |
|---|---|
| Median ratio | **4.82** |
| 68% CrI | [2.41, 12.94] |
| 90% CrI | [1.74, 31.38] |
| 95% CrI | [1.53, 52.11] |
| P(ratio ≥ 1) | 0.999 |
| P(ratio ≥ 5) | 0.483 |
| P(ratio ≥ 10) | 0.221 |
| P(ratio ≥ 20) | 0.092 |

Track A is the most conservative track (excludes the 13 anonymous modern-numerology project rows). Even here the ratio is almost certainly ≥1, with median nearly 5× and a non-trivial 22% posterior mass on ≥10×.

### Track B — named-classical vs broad-modern (recommended primary)

| Quantity | Value |
|---|---|
| Median ratio | **13.27** |
| 68% CrI | [6.20, 36.31] |
| 90% CrI | [4.17, 86.15] |
| 95% CrI | [3.53, 138.69] |
| P(ratio ≥ 1) | 1.000 |
| P(ratio ≥ 5) | 0.909 |
| P(ratio ≥ 10) | 0.634 |
| P(ratio ≥ 20) | 0.332 |

Track B is the recommended primary track because it matches how the modern numerology literature is actually consumed — readers encounter the rahma=114 / Catalan / Big-Bang-in-Q claims as a class, not as individually-named-author predictions. The right denominator is "all such claims tested."

The 90% CrI is **[4.17, 86.15]**. The median 13.3 is the headline figure.

### Track C — all-classical vs broad-modern

| Quantity | Value |
|---|---|
| Median ratio | **13.35** |
| 68% CrI | [6.30, 37.17] |
| 90% CrI | [4.27, 87.12] |
| 95% CrI | [3.61, 143.40] |

Track C is essentially identical to Track B because adding the 26 anonymous classical CONFIRMED + REFUTED rows (which split 22/4) leaves the rate at ≈0.774, indistinguishable from the named-only 0.778. The classical pool is internally homogeneous on the confirm-rate axis.

---

## 4. Sensitivity analyses

| Analysis | Adjusted classical c/n | Median ratio | 95% CrI |
|---|---|---:|---|
| Primary Track B | 28/36 = 0.778 | 13.27 | [3.53, 138.69] |
| **S1** drop al-Suyūṭī + al-Zarkashī | 17/22 = 0.773 | 13.09 | [3.55, 134.14] |
| **S2** keep only canonical 4 (Suyūṭī, Zarkashī, Biqāʿī, Rāzī) | 15/22 = 0.682 | 11.45 | [3.00, 123.58] |
| **S3** halve classical CONFIRMED (selection-bias correction) | 14/22 = 0.636 | 10.74 | [2.82, 113.92] |
| **S4** hypothetical extra modern CONFIRMED (+1) | 28/36 vs 2/21 | 7.48 | [2.75, 38.39] |
| **S5** hypothetical 2 extra modern CONFIRMED (+2) | 28/36 vs 3/22 | 5.39 | [2.34, 19.16] |

### What sensitivity tells us

- **Dropping the top 2 contributors (S1)** barely moves the median (13.27 → 13.09). The ratio is not driven by al-Suyūṭī/al-Zarkashī alone; it survives their removal.
- **Restricting to canonical 4 scholars (S2)** drops the classical rate to 0.682 (al-Biqāʿī's macro-ring failures dilute the canonical pool), but the median ratio still sits at **11.5×**, comfortably above the legacy ~7×.
- **Aggressive selection-bias correction (S3)** — even halving the classical CONFIRMED count (a brutal correction representing "half of the project's classical confirmations are partly artifacts of which classical claims were *selected* for testing") leaves the median at **10.74×**. The ratio is robust to substantial selection-bias correction.
- **Hypothetical additional modern confirms (S4, S5)** — adding 1 hypothetical modern confirmation drops the median to **7.5×**; adding 2 drops it to **5.4×**. This is the right way to interpret "what if Khalifa or Al-Kaheel were partly right after all?" Even granting that, the ratio is still ≥5×.

The robustness profile is: **the ratio survives every sensitivity analysis with a median ≥5×**, and the median is most sensitive to *modern denominator increases* (S4, S5) rather than *classical numerator decreases* (S1, S2, S3).

---

## 5. Where does the legacy "~7×" figure sit?

In the Track B posterior:
- **7×** is at the **20.6th percentile** — i.e., the data assign 79% posterior probability to a ratio ≥7.
- **10×** is at the 36.9th percentile.
- **13×** is at the 50th percentile (the median).
- **15×** is at the 55.4th percentile.
- **20×** is at the 66.7th percentile.

**Verdict on the legacy figure:** the "~7×" point estimate was *plausible but conservative*. It was a defensible round number for outreach communication because it avoided the higher numbers that depend on rare-event modern denominator estimates, but it understates the central tendency. The honest revision is **"approximately 13× under the broad-modern denominator, with 95% credible interval [3.5, 140]."**

The wide upper bound is unavoidable: with 1/20 modern confirmations, the true modern rate could be as low as 0.005 or as high as 0.24, and the upper-bound ratios reflect the *low* end of that modern range divided by the *high* end of the classical range.

---

## 6. Recommended formulations for downstream use

### For integrator narrative (synthesis files)

> Across the 120-claim H-META-1 corpus, classical-medieval Quranic interpretive claims confirm under project rules at **~78%** (95% CrI [64%, 89%]) while the modern numerology and iʿjāz ʿilmī literature confirms at **~5%** (95% CrI [1%, 24%]). The point estimate of the rate ratio is **~13×**, with 95% credible interval [3.5×, 140×]. The previously-circulated "~7×" figure is plausible but on the low end of this interval.

### For skeptical-auditor pre-reg discussions

> The classical-modern reliability gap has high posterior probability ≥5× (P=0.91 under Track B; P=0.48 under Track A). Quoting "~5×" is conservative; "~10×" is the central tendency; quoting bounds higher than 30× requires acknowledging the modern denominator is poorly constrained.

### For external reporting (avoid overclaim)

> The reliability ratio sits in the range **5×–15×** under multiple definitional tracks and survives selection-bias correction down to 10×. It would take 2 additional modern confirmations from the existing testing pipeline to drop the central estimate below 6×.

---

## 7. Methodological caveats (non-skip)

1. **Selection bias unresolved.** The 0.778 classical rate is conditional on which classical claims were chosen for the H-META-1 corpus. The corpus was constructed by classical-scholar with awareness of which claims were testable; this biases the classical numerator upward. The true population rate of unselected classical claims is unknown. *Direction of bias:* the reported ratio is an upper bound on the true population ratio. Sensitivity S3 attempts to model this with a 50% haircut and still gets ≥10×.

2. **Modern-lane denominator dominated by anonymous rows.** 19 of 20 broad-modern rows are REFUTED, with Neuwirth/Wild as the lone CONFIRMED. The wide 95% CrI upper bound (138×) reflects honest uncertainty about the true modern rate, not a methodology failure. Reporting the CrI is essential.

3. **Independence assumption violated.** Tests are not independent — they share corpora, baselines, methods. Beta-binomial posterior assumes Bernoulli independence. The true CI is wider than reported. Appropriate corrective: treat the credible interval as a *lower bound on uncertainty*, not as a tight envelope.

4. **The ratio is a comparative summary, not a fundamental constant.** It depends on the corpus composition. If the project tests 100 more obscure modern numerology claims and 0 more classical claims, the ratio will go up. If it tests 100 more bombastic classical claims that were selected on aesthetic grounds, the ratio will go down. The number is an *audit summary* of what has been tested, not a discovery about the texts themselves.

5. **Ratio framing risks misinterpretation.** Ratios are intuitive for comparative claims but lose information about *absolute* rates. The classical rate ~0.78 and the modern rate ~0.05 are individually more interesting than their ratio. Recommended: when reporting the ratio, *always* report both absolute rates alongside.

6. **MW-6 verbatim-confidence not used as a moderator.** This deliverable does not condition on PENDING vs VERIFIED nawʿ tags. A tighter analysis would test whether VERIFIED-only classical claims have a different rate than PENDING ones. That would be a follow-up task in this thread.

---

## 8. Pointer back to inputs

- Per-scholar tables: `findings/cross-finding/scholar-convergence-tracker.md`
- Underlying claim-level data: `findings/phase-c-structures/h-meta-1-corpus-120.tsv`
- Effect-size index: `findings/cross-finding/effect-size-inventory.tsv`
- Power-analysis context: `findings/cross-finding/pending-power-analysis.md`
- P-curve diagnostic: `findings/cross-finding/p-curve-diagnostic.md`

The five cross-finding deliverables (effect-size-inventory, pending-power-analysis, p-curve-diagnostic, scholar-convergence-tracker, classical-modern-reliability-ratio) now form the meta-analyst standing reference set. Closes meta-analyst standing queue items 1-5 from initial brief.

---

## 9. Headline numbers (for citation by other agents)

| Question | Answer |
|---|---|
| Classical confirmable rate | 0.778 (95% CrI [0.64, 0.89]), 28/36 named-classical |
| Modern broad confirmable rate | 0.050 (95% CrI [0.01, 0.24]), 1/20 broad-modern |
| Reliability ratio (Track B median) | **13.3×** (95% CrI [3.5×, 138.7×]) |
| Reliability ratio (Track A median, conservative) | **4.8×** (95% CrI [1.5×, 52.1×]) |
| P(ratio ≥ 5 under Track B) | 0.91 |
| P(ratio ≥ 10 under Track B) | 0.63 |
| Sensitivity-robust lower bound on median | ≥5× across all S-tests |

**One-line summary:** classical Quranic interpretive claims are roughly an order of magnitude more often confirmable under audit than modern numerology and iʿjāz ʿilmī claims, with a posterior credible-interval lower bound of ~3.5× and median ~13×.
