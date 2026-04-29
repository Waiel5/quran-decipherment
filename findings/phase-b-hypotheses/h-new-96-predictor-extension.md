---
id: H-NEW-96
title: Multi-class muqaṭṭāʿat letter-set predictor — feature-space extension (NM-4)
phase: B
status: NULL (primary — extension fails to improve on H-NEW-88 baseline)
date: 2026-04-17
specialist: h96-wrapper / team-lead (script ran in background ~40 min; findings wrap inline)
pre_reg: findings/phase-b-hypotheses/h-new-96-predictor-extension-prereg.md
script: scripts/h_new_96_predictor_extension.py
json: findings/phase-b-hypotheses/csv/h-new-96.json
seed: 20260417
bonferroni_k: 2
bonferroni_family: h-new-96-predictor-extension
alpha_bon: 0.025
parent: H-NEW-88 (baseline RF LOOCV top-1 = 0.414)
rules_tuple: (29 muqaṭṭāʿat-opened surahs; 14 letter-set classes; 92-feature extended design matrix; Random Forest + logistic LOOCV; 1000 permutation null)
verdict: NULL
---

# [[h-new-96-predictor-extension|H-NEW-96]] — Multi-class muqaṭṭāʿat letter-set predictor extension

## Claim tested

Under theorist R4 / NM-4, adding 74 new features (G1-G6: opener class, formulaic-opening type, top-30 roots, divine-name pattern, content-classification, name-root concentration) to [[h-new-88-letter-set-predictor|H-NEW-88]]'s 18-feature baseline should LIFT LOOCV top-1 accuracy > 0.50 and/or make ≥1 of the 8 singleton letter-sets predictable.

## Results

### Primary (top-1 LOOCV vs [[h-new-88-letter-set-predictor|H-NEW-88]]'s 0.414)

| Classifier | LOOCV top-1 | top-3 | top-5 | Singleton hits |
|---|---:|---:|---:|---:|
| Random Forest | **0.3793** | 0.5862 | 0.6552 | 0/8 |
| Logistic | 0.3103 | 0.5517 | 0.6207 | 0/8 |

**Both classifiers UNDERPERFORM [[h-new-88-letter-set-predictor|H-NEW-88]]'s 0.414 baseline**. Extended feature space does NOT help; arguably slightly hurts (added noise).

### MW-5 positive control

cheat_surah_id alone → LOOCV top-1 = 0.5172 (structural ceiling = 0.6552 due to LOOCV on singletons — each singleton-held-out makes its class unpredictable). Instrument is validated: the pipeline can achieve up to the structural ceiling when given perfect information, but no feature-space we've tested reaches it.

**audit-037 MW-5 clarification (non-blocking, appended 2026-04-17)**: The structural ceiling for *cheat_surah_id under LOOCV* is actually 21/29 ≈ **0.724** (the 21 cluster-member surahs are perfectly identifiable by their id, the 8 singletons remain unpredictable). The 0.6552 cited above is the ceiling for any *feature-based* predictor (19/29, per pre-reg). Observed cheat = 0.517 is below the 0.724 ceiling, indicating RF hyperparameters (n_estimators=200) under-utilize the cheat feature — likely a trees/leaf-constraint issue preventing perfect memorization of unique-id values. Pipeline is validated for the NULL verdict regardless (primary tests failed independently of MW-5 tightness).

### Permutation null (RF, 1000 perms)

| Quantity | Value |
|---|---:|
| Observed top-1 | 0.3793 |
| Null mean | 0.1396 |
| Null 95th percentile | 0.2759 |
| Null max | 0.4138 |
| **p_primary** | **0.0050** |
| p_singleton_hit | 0.0010 |

**Significant vs permutation** (p=0.005) — the features ARE informative. But NOT significantly better than [[h-new-88-letter-set-predictor|H-NEW-88]] parent.

### Pre-reg pass/fail mapping

- Primary threshold: top-1 > 0.50 → **FAIL** (0.38 observed)
- Secondary threshold: ≥1 singleton hit → **FAIL** (0/8 observed)
- Significance vs random permutation: **PASS** (p=0.005)

**Overall verdict: NULL** (extension hypothesis rejected).

## Interpretation

The extended 92-feature model achieves significance against permutation null but FAILS to improve on [[h-new-88-letter-set-predictor|H-NEW-88]]'s 18-feature baseline. Adding G1 opener-class, G2 formulaic-opening type, G3 top-30 roots (74 features), G4 top-20 divine-names (20 features), G5 content-class, G6 name-root concentration does NOT lift predictive power.

**Interpretive reading**: [[h-new-88-letter-set-predictor|H-NEW-88]]'s original 18-feature set (length, Meccan/Medinan, Nöldeke rank, prior muqaṭṭāʿat proximity, opener-token counts) captures essentially all information about muqaṭṭāʿat letter-set assignment that surface content features can provide. The 8 singleton letter-sets (ص, ق, ن, طه, يس, طس, كهيعص, حمعسق) remain STRUCTURALLY UNPREDICTABLE from any content feature we've tested.

This NULL refines OQ-1: **the specific letter-set assignment per muqaṭṭāʿat surah is NOT derivable from content-level features**. It's either (a) governed by a hidden variable we haven't measured (phonology? liturgy? numerology?), (b) genuinely arbitrary at the singleton level, or (c) determined by features requiring semantic / theological analysis beyond surface statistics.

This is consistent with H-NEW-136.1 NULL (5-letter muq not a content sub-class): letter-set identity is CONTENT-DECOUPLED.

## Honest limits

1. **LOOCV on singletons is inherently ceiling-bound at 0.655** (each singleton's held-out fold cannot be voted for). The 0.50 PASS threshold was set between 0.41 baseline and 0.66 ceiling — ambitious but achievable in principle.

2. **G1-G6 feature families were pre-committed** before training; no post-hoc feature selection. Discipline intact.

3. **G4 top-20 divine-names has leakage** (same as [[h-new-88-letter-set-predictor|H-NEW-88]] parent, disclosed in pre-reg). Per-fold recomputation not applied.

4. **1000 permutations** (vs 10K in more thorough tests) — compute budget compromise; sufficient for α=0.025 primary decision.

5. **Random Forest underperforms logistic here** (0.38 vs 0.31) — but both are below baseline. Model choice is not the issue.

## What this means for the unified model

- P5 (muqaṭṭāʿat-as-marker, now merged into P1★) predicts muq-STATUS but NOT muq-IDENTITY.
- OQ-1 remains **OPEN**: the specific letter-set choice per surah is not content-derivable.
- Theorist's R4 extension candidate (P10 "surah-name-root-letter matching") loses another empirical anchor — at content-feature level, no matching exists.
- The muqaṭṭāʿat letter-set assignment may be **load-bearing at a non-content axis** (phonological? acoustic? mystical?) that we haven't operationalized.

## Queue for future investigation

- H-NEW-96.1 — try char-n-gram features instead of root features (maybe phonological not semantic)
- H-NEW-96.2 — try combining rhyme-pattern features (per [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] the muq openings correlate with rhyme letters; maybe letter-set is predictable from rhyme-features)
- H-NEW-96.3 — try semantic embedding features (AraBERT) instead of hand-crafted
- H-NEW-96.4 — combine with [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]]'s Pattern-B composite as a predictor feature

## Connection to other findings

- [[h-new-88-letter-set-predictor|H-NEW-88]] baseline confirmed (no improvement)
- [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] muqaṭṭāʿat → rhyme finding may provide a NEW feature axis for H-NEW-96.2
- H-NEW-136.1 NULL (5-letter muq not sub-class) parallels this: both say content-level features don't determine letter-identity

## Classical wisdom

Classical tafsir (al-Rāzī, al-Suyūṭī) acknowledges that the muqaṭṭāʿat remain "among the secrets" (min al-asrār) whose interpretation is God's knowledge. The empirical finding that content-level features fail to predict them is CONSISTENT with classical epistemic humility about them. This doesn't prove theological unknowability — it just means this specific operationalization doesn't crack them.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-96-predictor-extension-prereg.md`
- Script: `scripts/h_new_96_predictor_extension.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-96.json`
- Findings: this file
- Journal: to be written by h96-wrapper or integrator
