---
finding_id: h-classic-45
phase: B
status: COMPLETED
verdict: PASS
effect_strength: strong
tested_by: computational-tester
test_date: 2026-04-14
parent_task: "#96"
pre_reg: findings/phase-b-hypotheses/h-classic-45-prereg.md
pre_reg_compliance: PRE-REG-STANDARD-04 + STANDARD-05
script: scripts/h_classic_45_suyuti_gharib.py
json: findings/phase-b-hypotheses/csv/h-classic-45.json
rules_tuple: (no-tashkeel, root-level via QAC, hafs-kufan, mashriqi)
seed: 20260414
n_perm: 10000
bonferroni_k_outer: 6
bonferroni_family_outer: h-classic-44-49
bonferroni_k_inner: 1
bonferroni_family_inner: h-classic-45-single-primary
alpha_bon: 0.00833
primary_observed_rho: -0.6818
primary_p_lower: 0.000100
primary_passes: true
classical_source: al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on gharīb al-Qurʾān (PENDING physical nawʿ-number verify)
cross_refs:
  - findings/cross-finding/scholar-convergence-tracker.md §2 al-Suyūṭī row
  - findings/cross-finding/scholar-convergence-tracker.md §5 chronology prior
  - H-NEW-17 (task #25, loanword density × Nöldeke, classical-scholar lane, in-progress) — parallel test with independent lexicon class
---

# H-CLASSIC-45 — al-Suyūṭī gharīb al-Qurʾān: early-Meccan gharīb-density elevation

## Verdict

**PASS** — al-Suyūṭī's early-Meccan gharīb-elevation claim is confirmed at hierarchical Bonferroni α_bon = 0.00833 with empirical p = 0.0001 (clears threshold by ~80×).

**Spearman ρ(Nöldeke period, gharīb density per 100 STEM tokens) = −0.6818**, one-sided lower-tail p < 10⁻⁴ under 10,000 label-permutation null (seed 20260414). The signal is strong, robust to threshold variation, and survives length-covariate control.

## Primary result

| Statistic | Value |
|---|---|
| Primary Spearman ρ | **−0.6818** |
| Null mean | −0.0005 |
| Null SD | 0.0947 |
| Observed ρ / null SD | ~7.2σ |
| One-sided lower-tail p | **0.0001** (1 of 10,000 perms as extreme) |
| α_bon (k_outer=6, k_inner=1) | 0.00833 |
| Pass | **YES** |

## Per-Nöldeke-period gharīb density (per 100 STEM-bearing tokens)

| Period | Label | n surahs | mean | sd | median |
|---|---|---|---|---|---|
| 1 | Early Meccan | 48 | **12.65** | 10.59 | ~9 |
| 2 | Middle Meccan | 21 | 5.24 | 1.41 | ~5 |
| 3 | Late Meccan | 21 | 2.87 | 1.17 | ~3 |
| 4 | Medinan | 24 | 2.98 | 1.55 | ~3 |

Nearly perfect monotone decay 1 → 2 → 3 with a small non-significant rebound at period 4 (3 → 4 difference ≈ +0.10 per 100 tokens, within ~1/10 of period-3 sd). The Early-Meccan elevation is not subtle: mean gharīb density is **4.4× higher** in Early Meccan than in Medinan, with a **per-period range of ~9.7 percentage points** at the mean.

The large sd (10.59) on period 1 reflects a genuinely heavy-tailed distribution: some Early-Meccan surahs (e.g., short oath-openers with rare vocabulary) have gharīb density > 25%, while others are closer to the Medinan baseline. This heterogeneity is itself consistent with al-Suyūṭī's claim — he argues the early-Meccan style is marked by **clusters** of gharīb vocabulary, not a uniform elevation.

## Threshold sensitivity (diagnostic, not verdict-entering)

| Threshold (total Quranic occurrences) | n gharīb roots | Spearman ρ |
|---|---|---|
| ≤ 3 | ~500 | −0.5901 |
| **≤ 5 (primary)** | **898** | **−0.6818** |
| ≤ 10 | ~1200 | −0.7336 |

The signal **strengthens** as the threshold broadens. This is a meaningful robustness check: if the effect were driven by statistical noise from a small hapax class, broadening the definition would dilute it. Instead, the broader definition captures more of the population-level lexical shift and the effect grows. This indicates the gharīb chronology signal is **not a hapax-outlier artefact** but a genuine population-level lexicon redistribution across Nöldeke periods.

Per pre-reg lock, threshold 5 is the verdict-entering primary; the sensitivity results are reported for transparency only.

## Length confound analysis

The spec flagged the length confound as known (a). Observed:

- `spearmanr(stem_token_count, gharīb_density) = −0.478` (close to but below the pre-registered |ρ|>0.5 flag threshold — **no formal flag** per the locked rule)
- `spearmanr(stem_token_count, period) = +0.672` (Meccan-1 surahs are substantially shorter than Medinan)

This means length and gharīb density are correlated, AND length and period are correlated — a classic mediator/confound configuration. A post-hoc partial-correlation diagnostic is informative:

- **Partial Spearman ρ(period, density | length) = −0.555** (vs marginal −0.682)

The signal drops by ~19% when length is partialled out, but remains strong and in the predicted direction. A linear regression `density ~ period + log(length)` gives a period coefficient of **−1.64 per period** (approximate t ≈ −2.6) — i.e., holding surah length constant, each step up the Nöldeke chronology reduces gharīb density by about 1.6 gharīb tokens per 100 STEM tokens. The length coefficient is **−2.32 per log-length unit**, so both channels contribute.

**Honest interpretation**: The al-Suyūṭī gharīb-chronology effect is **partially** explained by the fact that Early-Meccan surahs are shorter (and shorter surahs concentrate more rare vocabulary per token), but a substantial period-specific residual remains after length control. The classical claim survives in a modified form: "Early-Meccan surahs have elevated gharīb density, and part of this elevation is mediated by their shortness — which is itself a feature of the early-Meccan oracular style al-Suyūṭī is pointing at." Shortness and gharīb-vocabulary are co-features of the Early-Meccan register, and partialling one out of the other is partly cutting into the signal being measured.

This is the right kind of honest caveat: the marginal correlation overstates the period-specific effect, but the partial correlation remains strong enough to clear α_bon on its own (partial ρ = −0.555 at N=114 is far above any reasonable threshold).

## Meccan-vs-Medinan binary test (diagnostic)

Collapsing periods 1-3 into "Meccan" (n=90) vs period 4 "Medinan" (n=24):

- Meccan mean gharīb density: ~7.8 per 100 STEM tokens
- Medinan mean gharīb density: ~3.0 per 100 STEM tokens
- Mann-Whitney U = 1706, one-sided p = **7 × 10⁻⁶**

The binary version is also strongly significant in the predicted direction. The Meccan group is 2.6× higher than Medinan, driven almost entirely by the Early-Meccan subset.

## Alternative chronology diagnostic (revelation order)

Using the full 114-step Tanzil Egyptian Standard revelation order (1-114) as a higher-resolution alternative to the 4-phase Nöldeke bucketing:

- `spearmanr(revelation_order, density) = −0.4554`
- One-sided lower-tail p = 0.0001

Weaker than the 4-phase Nöldeke version (ρ = −0.455 vs −0.682) because the fine-grained revelation order has more noise within each period. The fact that the 4-phase aggregation gives a cleaner signal is itself mild evidence that the relevant chronological structure is at the **Nöldeke-period level**, not at the per-surah revelation-order level. This is a modest internal corroboration of the Nöldeke phase taxonomy as a meaningful grouping.

## Convergence with prior findings

### Leg 1: H-META-1 confirmable-signature classifier

H-META-1's classifier predicts which claims confirm based on substance-type, era, school, scope, and specificity. al-Suyūṭī sits in the mixed-reliability row on the cross-scholar convergence tracker — his local-specific claims confirm, his universal-symmetry claims fail. This gharīb-chronology claim is **monotone-trend**, which is between the two extremes. The H-META-1 prior was UNCERTAIN rather than PASS-predicted; the strong PASS here is modestly surprising and **adds a confirmable data point to al-Suyūṭī's specific-claim track record**.

### Leg 2: H-NEW-17 (task #25, in-progress, classical-scholar lane)

H-NEW-17 tests loanword density × Nöldeke chronology using the Jeffery 1938 loanwords TSV (218 rows, now delivered per classical-scholar 2026-04-14). H-CLASSIC-45 uses the **corpus-internal** gharīb definition (root occurrence ≤ 5), which is methodologically independent from the Jeffery loanword lexicon. If H-NEW-17 reports a PASS in the same direction (loanwords concentrate in early-Meccan), the two findings will be **parallel confirmations at different lexicon-class operationalizations** — a cross-class convergence that would strongly reinforce the Nöldeke chronology-lexicon signature at the rare-vocabulary level. If H-NEW-17 reports NULL, the two findings **dissociate** the gharīb-hapax channel (which passes) from the loanword-borrowing channel (which does not), which would itself be informative.

### Leg 3: Nöldeke-chronology R-010 macro-refutation is NOT violated

R-010 (task #114, MASTER §3 entry) reports that Nöldeke chronology is **not recoverable from the graph-geometric feature space alone** — the multi-feature similarity graph does not produce the Nöldeke order as an intrinsic sort key. H-CLASSIC-45's PASS is a **single-feature correlation**, not a multi-feature recovery claim, so it does not violate R-010. The two findings sit in different regimes: "a specific lexicon feature tracks chronology" (H-CLASSIC-45 PASS) vs "the full bag of features does not globally reconstruct chronology" (R-010 FAIL). Both can be true simultaneously. See MW-1 GATE-B (task #53 pending) for the substratum regression that formally tests this distinction.

### Leg 4: al-Suyūṭī specific-claim track record

Prior al-Suyūṭī tests in this project:
- **Ḥusn al-ibtidāʾ/al-intihāʾ** (task #3, completed): mixed result, local-pair version PASS at specific surah level
- **Gharīb chronology** (this, H-CLASSIC-45): strong PASS

al-Suyūṭī's Itqān is an aggregation of multiple nawʿ-level claims, and his reliability is specific-claim-dependent rather than author-dependent. The gharīb-chronology result adds the second confirmable-specific data point to his row in the scholar-convergence tracker.

## What this finding does and does not claim

**It claims**:
1. Per-surah gharīb density (roots with ≤5 total Quranic occurrences, measured per 100 STEM tokens) is negatively correlated with Nöldeke period at Spearman ρ = −0.68, p < 10⁻⁴, clearing the hierarchical-Bonferroni threshold α_bon = 0.00833 by orders of magnitude.
2. The effect is robust to threshold variation (ρ ∈ [−0.59, −0.73] across thresholds 3/5/10) and **strengthens** at broader thresholds, indicating a population-level lexical redistribution, not a hapax-outlier artefact.
3. The effect is **partially mediated** by surah length (Meccan surahs are shorter, shorter surahs have higher gharīb density), but the length-partialled correlation remains ρ = −0.55, strong enough to clear α_bon on its own.
4. al-Suyūṭī's Itqān claim that gharīb vocabulary clusters in Early-Meccan revelations is empirically corroborated at the corpus level, under the ≤5-occurrence operationalization of gharīb.

**It does not claim**:
1. That Early-Meccan surahs are *uniformly* gharīb-heavy. The within-period sd on period 1 is large (~10), reflecting real heterogeneity — some Early Meccan surahs have gharīb density > 25%, others are closer to Medinan baseline. The claim is about the **distribution shift**, not uniformity.
2. That the length-confound is negligible. It explains a non-trivial fraction of the marginal correlation. The signal survives length control but is smaller in the conditional analysis.
3. That this test recovers the full Nöldeke chronology. The finer-grained revelation-order version gives ρ = −0.45, weaker than the 4-phase version, showing that the recoverable signal is at the period-grouping level, not the per-surah level.
4. That all rare-vocabulary classes behave this way. This test operationalizes gharīb as corpus-internal hapax-class. The Jeffery loanword class (H-NEW-17) is orthogonal and may or may not concur.
5. That this test reaches al-Suyūṭī's narrow eschatological claim. al-Suyūṭī also predicted gharīb clustering in **eschatological verses**. The current test is at the surah-level with period labels; a verse-level test partitioning eschatological vs other genres is a logical follow-up (H-CLASSIC-45.1 candidate).

## Pre-registration compliance

All ten no-fork protections honored:

1. Gharīb threshold LOCKED ≤5. ✓
2. Density normalization LOCKED per-100-STEM-token. ✓
3. Nöldeke period mapping LOCKED 1/2/3/4. ✓
4. Primary statistic LOCKED Spearman ρ. ✓
5. Null seed LOCKED 20260414, n_perm 10,000. ✓
6. α_bon LOCKED 0.00833 (k_outer=6, k_inner=1). ✓
7. One-sided test LOCKED lower-tail. ✓
8. Denominator LOCKED STEM-bearing tokens. ✓
9. Verdict matrix LOCKED. ✓
10. All 5 diagnostics reported but not verdict-entering. ✓

The length-confound partial-correlation analysis in this narrative is a **post-hoc diagnostic** triggered by the length-density correlation reaching |ρ| = 0.478 (below the locked |ρ| > 0.5 flag threshold, but close enough to warrant honest caveat reporting). It is **not** a change to the primary statistic and does not alter the verdict. The verdict stands as PASS based on the locked marginal Spearman ρ primary.

## Follow-up queue

- **H-CLASSIC-45.1**: Eschatological-verse-level gharīb clustering. al-Suyūṭī's original claim names eschatological revelations (yawm al-qiyāma, Day of Judgment verses) as a specific gharīb-rich locus. Test with verse-level genre labels rather than surah-level period labels. **Medium priority**.
- **H-CLASSIC-45.2**: Cross-lexicon convergence with H-NEW-17 (Jeffery loanwords). Once H-NEW-17 reports, run a joint analysis: do the gharīb-hapax and loanword-borrow channels covary at the surah level, or are they dissociable rare-vocabulary classes? **High priority, gated on H-NEW-17 delivery**.
- **H-CLASSIC-45.3**: Length-residualized partial correlation as formal primary. The post-hoc partial ρ = −0.55 diagnostic is strong enough to be a self-standing test if re-pre-registered with the length-covariate as a proper control. **Low priority** — the marginal primary already passes.

## Files

- Pre-registration: `findings/phase-b-hypotheses/h-classic-45-prereg.md`
- Script: `scripts/h_classic_45_suyuti_gharib.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-classic-45.json`
- Narrative (this file): `findings/phase-b-hypotheses/h-classic-45.md`
