---
surah: 21
test_id: Q021-F-02
title: Prophet-order distance — does Q 21 follow a different prophet-cycle template than Q 6?
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 3
bonferroni_family: Q021-F-02-template-comparison-3-cells
alpha_bon: 0.0167
direction: Q 21 prophet-order CLOSER to {Q 11, Q 26, Q 37} than to Q 6
---

# Q021-F-02 — Pre-registration: prophet-order distance template test

## 1. Hypothesis (locked before observation of distances)

**H1 (one-tailed, locked):** Q 21's first-occurrence prophet-order is **closer** (smaller Kendall-τ inversion-count distance) to the *prophet-cycle surahs* {Q 11, Q 26, Q 37} (Hūd, Shuʿarāʾ, Ṣāffāt) than to **Q 6:83-87**.

**H0:** Q 21's order is no closer to any of {Q 11, Q 26, Q 37} than to Q 6 (i.e., the alternative prophet-cycle-template hypothesis is unsupported).

**Direction (LOCKED):** mean(d(Q 21, Q 11), d(Q 21, Q 26), d(Q 21, Q 37)) < d(Q 21, Q 6).

## 2. Disclosure

The author has computed the first-occurrence prophet-order for Q 21, Q 6, Q 11, Q 26, Q 37 from QAC v0.4 BEFORE locking this pre-reg. The author has NOT yet computed the pairwise distances. Direction is locked at H1 above. The pre-reg and run-script SHA256 lock will be in place before any distance computation.

## 3. Operational definition

For each surah s:
- Extract first-occurrence ordering of prophet-PN-lemmas in mushaf-position order (verse + word index).
- The set of prophets considered = the **intersection** of the two surahs being compared (i.e., a surah's order on the *common* prophet set).
- **Distance metric**: Kendall-τ inversion count on the common subset, divided by max-possible-inversions to give a normalized [0, 1] distance d.
- For a pair (Q 21, Q X) where the common prophet set has size n: d = (# pairs out of order) / (n choose 2).

## 4. Test statistic

| Cell | Quantity |
|:--|:--|
| Cell A | d(Q 21, Q 6) |
| Cell B | d(Q 21, Q 11) |
| Cell C | d(Q 21, Q 26) |
| Cell D | d(Q 21, Q 37) |
| Primary | mean(B, C, D) − A |

H1 predicts primary < 0 (Q 21 is closer to {Q 11, Q 26, Q 37} on average than to Q 6).

**Permutation null**: 10 000 random shuffles of the prophet-order in Q 21 only; under the null, the difference of means is symmetric around 0.

## 5. Success / Failure criteria (Bonferroni k=3)

The Bonferroni family has 3 cells (B, C, D each compared against A). With α = 0.05 / 3 = 0.0167:

- **Strict success (CONFIRMED)**: at least 2 of 3 cells (B, C, D) individually satisfy d(Q 21, X) < d(Q 21, Q 6) AND combined-mean comparison is direction-locked.
- **DIRECTIONAL**: Sign of (mean(B,C,D) − A) is negative AND at least 1 cell passes Bonferroni.
- **NULL**: no cells pass Bonferroni AND sign-of-difference is non-negative.

## 6. Honest limits known a priori

- Q 6's 16-prophet order is mostly inside vv. 83–87 (a single 5-verse list); Q 21's 14-prophet order spans 41 verses. The geometry of "first occurrence" thus reflects different surface structures — Q 6 is essentially a *list*, Q 21 is a *narrative-catalog with episodes*.
- Common-set sizes vary: |Q 21 ∩ Q 6| ≤ 13; |Q 21 ∩ Q 11| ≤ 8; |Q 21 ∩ Q 26| ≤ 5; |Q 21 ∩ Q 37| ≤ 6. Smaller common sets reduce statistical power for pairwise comparisons B / C / D.
- Pairs with common set < 4 are excluded from the comparison (insufficient inversion-count granularity).
- The interpretation "Q 21 follows a different template" is a meaningful-effect-size question, not just a significance question. If the absolute difference (mean(B,C,D) − A) is < 0.05, the substantive claim is weak even if formally significant.

## 7. Rules-tuple

`(QAC-v0.4-PN-LEM-first-occurrence, normalized-Kendall-τ, common-subset-only, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. SHA256 lock

To be computed at runtime by `scripts/Q021_F_02_prophet_order.py`. Embedded in script and verified at execution.
