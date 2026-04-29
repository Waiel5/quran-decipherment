---
finding_id: h-meta-1-mw6-retrained-prereg
phase: meta
status: PRE-REGISTERED — locked before script execution
date: 2026-04-13
locked_at: 2026-04-13 (timestamp before any retrain execution)
parent: findings/cross-finding/mw6-reliability-moderator.md
parent_classifier: scripts/h_meta_1_classifier.py
parent_classifier_baseline_json: findings/phase-c-structures/csv/h-meta-1-classifier.json
rules_tuple: (no-tashkeel, orthographic-token & lemma, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
seed: 20260413
n_perm: 500
bonferroni_k: 2
bonferroni_alpha_family: 0.05
bonferroni_alpha_per_test: 0.025
pre_registration_authority: team-lead Option A approval 2026-04-13
---

# H-META-1 + MW-6 Retraining — Pre-Registration

## Why pre-register

The MW-6 reliability moderator (`mw6-reliability-moderator.md`) found that VERIFIED-tier classical claims have a *lower* confirmable rate than SECONDARY-tier (P(VERIFIED > SECONDARY) = 0.048, classical-medieval restriction). The mechanism (per S3 sensitivity) is composition-confounding: VERIFIED tier is over-populated with structural-formal claims that have harder pass-bars.

This raises a question the moderator analysis cannot answer alone: **is the MW-6 tier signal load-bearing in the H-META-1 classifier**, or is it absorbed by the substance_type and specificity features the classifier already uses? Adding MW-6 tier as an explicit feature and re-running the classifier produces falsifiable evidence for or against load-bearing-ness.

This pre-reg locks the predictions before the retrain runs.

## Two pre-registered predictions

### Prediction P1: Accuracy lift

**Statement:** Adding the MW-6 tier feature to the H-META-1 classifier improves the LR L1 5-fold cross-validated accuracy by ≥ 1 percentage point over the baseline.

- **Baseline:** LR L1 mean CV accuracy = **0.7820** (from `h-meta-1-classifier.json`, 5-fold stratified, λ = 0.05, fold-by-fold [0.80, 0.84, 0.79, 0.78, 0.70])
- **Threshold for P1 hit:** retrained LR L1 mean CV accuracy ≥ **0.7920**
- **Threshold for P1 miss:** retrained LR L1 mean CV accuracy < 0.7920

A null retrain (no MW-6 added) should produce 0.7820 ± noise from the same protocol. Any retrained accuracy above 0.7920 is a substantive lift; below is not.

### Prediction P2: Sign of VERIFIED coefficient

**Statement:** In the full-data L1-logistic model trained on all 120 claims with MW-6 tier features added, the coefficient on `mw6_tier=VERIFIED` is **negative** (consistent with the moderator finding that VERIFIED-tier classical claims confirm at a lower rate).

- **P2 hit:** `mw6_tier=VERIFIED` coefficient is non-zero AND negative
- **P2 miss (null absorption):** `mw6_tier=VERIFIED` coefficient is zero (L1 sets it to 0)
- **P2 miss (sign reversal):** `mw6_tier=VERIFIED` coefficient is non-zero AND positive

Note: the L1 penalty (λ = 0.05) may zero out features that don't carry independent signal. A zero coefficient is a *miss* under the strict reading but is not a *contradiction* of the moderator analysis — it would mean MW-6 tier is collinear with substance_type or specificity (which the classifier already has) and adds no marginal signal.

## Decision matrix (committed before run)

| P1 (lift) | P2 (VERIFIED sign) | Interpretation |
|---|---|---|
| HIT | HIT (negative) | **Strong confirmation.** MW-6 is empirically load-bearing in the meta-classifier. Reframe ("testability + provenance") is statistically grounded. Recommend integrator add MW-6 tier as a permanent classifier input. |
| HIT | MISS (positive) | **Investigation triggered.** The moderator analysis and the classifier disagree on direction. Possible cause: era effects (classifier sees all 120 rows, moderator restricted to classical-medieval). Run a third analysis: classifier on classical-medieval rows only, see which way the sign goes. |
| HIT | MISS (zero) | **Partial confirmation.** MW-6 tier as a whole improves the classifier (some other tier indicator is load-bearing — perhaps `mw6_tier=SECONDARY` positive coefficient), but VERIFIED specifically is collinear with substance_type. Reframe still holds; classifier picks up the same composition signal through a different channel. |
| MISS | HIT (negative) | **Procedural-only.** MW-6 protocol predicts moderator-level rates but doesn't add classifier signal beyond what substance_type already captures. MW-6 is empirically-validated as a within-tier moderator but is not a classifier feature. |
| MISS | MISS (positive) | **Strong refutation of the moderator-finding's classifier prediction.** The moderator-finding is real at the corpus level but doesn't propagate to classifier load-bearing-ness — and the direction within the classifier even reverses. Flag for skeptical-auditor review of the moderator's mechanism. |
| MISS | MISS (zero) | **MW-6 is procedural-hygiene only.** Neither the classifier nor any sub-coefficient gains from MW-6 inclusion. The moderator finding remains valid as a tier-conditional rate observation but the protocol's contribution to the classifier is bookkeeping. |

All six outcomes are publishable. The decision matrix is locked here, before the retrain runs, so post-hoc reinterpretation is prohibited.

## Protocol details (locked)

1. **Corpus:** `findings/phase-c-structures/h-meta-1-corpus-120.tsv` (same 120-claim balanced corpus as the original H-META-1, no edits).
2. **MW-6 tier extraction:** Same parser as the moderator script (`scripts/mw6_reliability_moderator.py`): regex `\[([^]]+)\]` on the `claim_source` column, take the first whitespace-delimited token of the bracket content, with `SECONDARY-TRIANGULATED` preserved as a distinct tier. Untagged rows get `UNTAGGED`.
3. **Feature encoding:** MW-6 tier is one-hot encoded (5 levels: VERIFIED, SECONDARY-TRIANGULATED, SECONDARY, PENDING, UNTAGGED). Added to the existing categorical feature set. No interactions with other features in the primary specification.
4. **Models:** LR L1 (λ = 0.05) and shallow tree (depth 3, Gini). Same as baseline.
5. **CV:** 5-fold stratified, seed 20260413. Same as baseline.
6. **Null:** 500-perm label-shuffle on the full feature set (matches the baseline's B=500 from the script source). Empirical p computed against null distribution per model.
7. **Bonferroni:** k = 2 family (LR + tree), α_family = 0.05, α_per_test = 0.025. Same as baseline.
8. **Acceptance for the retrain itself:** baseline thresholds apply (PASS at > 0.70, NO-SIGNATURE at < 0.60, WEAK-SIGNAL between).
9. **Pre-registered comparison:** P1 lift threshold = baseline + 0.01 (one percentage point), evaluated on LR L1 mean CV accuracy.
10. **Output:** `findings/cross-finding/h-meta-1-mw6-retrained.md` with full results table, P1/P2 evaluation against this pre-reg, decision-matrix routing, and one of the six interpretation paths above.

## What the retrain MUST NOT do

- No threshold tuning of λ to optimize accuracy
- No post-hoc feature selection beyond L1
- No re-binning of MW-6 tiers after seeing results
- No restriction of the corpus after seeing results
- No selective reporting of LR-only or tree-only if both run

If the retrain produces a result that doesn't fit any of the six decision-matrix cells (e.g. an error, a zero accuracy, an empty L1 weight vector), the run is reported as-is with the failure mode disclosed and a follow-up routed to skeptical-auditor.

## Garden-of-forking-paths log (anticipated)

The following decisions were pre-committed and locked here:

- **One-hot vs ordinal MW-6 encoding.** Choice: one-hot. Rationale: tiers are not linearly ordered in confirmable rate (PENDING > SECONDARY-TRIANGULATED > SECONDARY > VERIFIED > UNTAGGED is the moderator ordering, and PENDING has the highest rate despite being the "lowest verification status"). Ordinal encoding would impose a monotonic constraint the data does not support.
- **UNTAGGED handling.** Choice: treat as a distinct level, not as missing. Rationale: UNTAGGED is dominantly project / contemporary-academic claims and carries strong informational signal about substance composition.
- **Era restriction.** Choice: NO restriction. The H-META-1 classifier runs on the full 120-claim corpus by design, and restricting to classical-medieval would change the comparison from "does adding MW-6 help the existing classifier" to "does the moderator finding replicate." The latter is already done in the moderator analysis.
- **Interaction terms.** Choice: NONE in the primary specification. Adding `mw6_tier × substance_type` interactions would be a separate hypothesis not pre-registered here.

## Reproducibility

After the retrain runs, the following artifacts must exist for the result to be considered valid:

- `scripts/h_meta_1_mw6_retrained.py` (the retraining script)
- `findings/cross-finding/csv/h-meta-1-mw6-retrained.json` (results JSON)
- `findings/cross-finding/h-meta-1-mw6-retrained.md` (writeup with P1/P2 evaluation)
- This pre-reg file unchanged (do not edit after seeing results)

If any of those four files differs from this commitment after the run, treat as a protocol violation and escalate to skeptical-auditor.
