---
id: H-NEW-165.2
title: Phonological codebook sensitivity sweep for the OQ-1 muq predictor
phase: B
status: PRE-REGISTERED
date: 2026-04-18
agent: codex
parent_1: H-NEW-165
parent_2: H-NEW-232
open_question: OQ-1
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-165-2-codebook-sensitivity
alpha_bon: 0.025
rules_tuple: "(no-tashkeel; canonical 14 muq letter-sets; 4 locked codebooks only; RF primary, logistic secondary; inherited H-232 nearest-centroid propagation check; 1000-permutation nulls; seed 20260419)"
---

# [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] — Phonological codebook sensitivity sweep

## Question

[[h-new-165-phonological-predictor|H-NEW-165]] reported the first positive OQ-1 signal on the phonological axis:
RF LOOCV top-1 = 19/29 = 0.6552, exactly the multi-member structural ceiling.
[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] then extended that geometry to the singleton edge and landed
8/10 nearest-centroid matches at p = 0.02498. Audit-038 accepted the direction
but explicitly required a codebook-sensitivity sweep before any upgrade in
confidence.

This finding asks a narrow robustness question:

**Does the [[h-new-165-phonological-predictor|H-NEW-165]] phonological predictor remain qualitatively load-bearing
under a small locked family of reasonable codebook perturbations, or is it
overly dependent on one exact featureization?**

## Scope discipline

This is a **bounded sensitivity analysis**, not a free ablation search.
Only four codebooks are allowed, locked below before execution. I do **not**
test source-isolated ablations like "al-Khalil-only" here because those would
change the model family itself rather than perturb the existing [[h-new-165-phonological-predictor|H-NEW-165]]
featureization modestly.

## Locked codebook family

All variants keep the [[h-new-165-phonological-predictor|H-NEW-165]] feature family structure:

- 9 per-letter features:
  `makhraj`, `voice`, `manner`, `emphatic`, `pharyngeal`,
  `sonorant`, `continuant`, `idhlaq`, `vowel_carrier`
- 6 aggregate features:
  `letter_count`, `frac_emphatic`, `frac_pharyngeal`,
  `frac_sonorant`, `frac_idhlaq`, `has_qalqala`

Only the underlying letter-to-feature assignments may vary.

### V0 — `baseline_h165_locked`

Exact reproduction target of the [[h-new-165-phonological-predictor|H-NEW-165]] / [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] locked codebook as
implemented in:

- `scripts/h_new_165_phonological_predictor.py`
- `scripts/h_new_232_oq1_singleton.py`

This is a positive-control baseline, not a new hypothesis.

### V1 — `watson_modern_voice`

Keep the full [[h-new-165-phonological-predictor|H-NEW-165]] codebook but replace the `voice` assignment with the
modern voiced/voiceless partition already locked elsewhere in the repo
(`[[h-new-69-half-alphabet-split|H-NEW-69]]`, Watson-2002-aligned grouping). This primarily changes the status of
`ط` relative to the classical jahr/hams coding.

### V2 — `strict_pharyngeal_split`

Keep the full [[h-new-165-phonological-predictor|H-NEW-165]] codebook but make the `pharyngeal` feature strict:

- `pharyngeal = 1` only for the throat letters `{ع, ح}` among the 14 muq letters
- `emphatic` remains the tafkhim/musta'liya-like set used by [[h-new-165-phonological-predictor|H-NEW-165]]

This tests whether the parent result depended on the hybrid
"musta'liya union pharyngeals" feature rather than on a cleaner throat-only
coding.

### V3 — `holes_glottal_ha_ayn`

Keep the full [[h-new-165-phonological-predictor|H-NEW-165]] codebook but move `ح` and `ع` one step deeper in the
`makhraj` ordinal:

- baseline: `makhraj(ح) = makhraj(ع) = 7`
- variant: `makhraj(ح) = makhraj(ع) = 8`

This directly tests the audit-038 concern that an alternate Holes-style
pharyngeal/glottal placement might matter.

## Inherited metrics

For each variant, compute two inherited outcome families.

### Family A — [[h-new-165-phonological-predictor|H-NEW-165]] cluster predictor

Run the [[h-new-165-phonological-predictor|H-NEW-165]] predictor stack verbatim:

1. RF LOOCV top-1, top-3, top-5
2. logistic LOOCV top-1, top-3, top-5
3. RF permutation null with `n_perm = 1000`
4. 8-task singleton LOOCV hits
5. MW-5 `cheat_surah_id` positive control

### Family B — [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] singleton propagation

Using the same variant codebook, rerun the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] nearest-centroid protocol:

1. build the same 29 x 15 design matrix
2. z-score using the 19 multi-member rows only
3. compute the 4 centroids
4. score the 10 singleton nearest-centroid matches against the exact same
   pre-committed accepted-cluster table used in [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]
5. run the 1000-permutation shuffled-label null

## Positive controls

### PC1 — baseline reproduction

The baseline variant must reproduce the parent findings exactly or to rounding:

- [[h-new-165-phonological-predictor|H-NEW-165]] RF top-1 = `19/29 = 0.6552`
- [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] singleton nearest-centroid matches = `8/10`

If this fails, the entire experiment is `NULL-BROKEN-PIPELINE`.

### PC2 — MW-5 inherited sanity

For each variant, `cheat_surah_id` must yield RF LOOCV top-1 >= 0.45, matching
the inherited [[h-new-165-phonological-predictor|H-NEW-165]] sanity window.

## Preserved vs degraded definitions

These are locked before execution.

### Variant-level [[h-new-165-phonological-predictor|H-NEW-165]] status

- `primary_retained`:
  RF top-1 > 0.50 AND RF permutation p < 0.025
- `primary_preserved`:
  `primary_retained` AND RF top-1 >= `18/29 = 0.6207`
  Rationale: at most one LOOCV hit below the 19/29 [[h-new-165-phonological-predictor|H-NEW-165]] ceiling result.
- `collapsed_below_h88`:
  RF top-1 <= 0.4138 OR RF permutation p >= 0.05

### Variant-level [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] propagation status

- `singleton_retained`:
  nearest-centroid matches >= 7/10 AND permutation p < 0.025
- `singleton_degraded`:
  nearest-centroid matches <= 6/10 OR permutation p >= 0.05

### Combined per-variant verdict

- `PRESERVED-BOTH`:
  `primary_preserved` AND `singleton_retained`
- `PRESERVED-PRIMARY-ONLY`:
  `primary_preserved` AND NOT `singleton_retained`
- `DEGRADED-BUT-RETAINS-PRIMARY`:
  `primary_retained` but not `primary_preserved`
- `DEGRADED`:
  not `primary_retained`

## Overall verdict rule

Let the 3 perturbed variants be V1-V3 only; V0 is the positive-control baseline.

- `ROBUST`:
  baseline reproduction passes, all 3 perturbed variants retain the primary
  signal, and at least 2 of 3 also preserve singleton propagation
- `ROBUST-PRIMARY-EDGE-SENSITIVE`:
  baseline reproduction passes, all 3 perturbed variants retain the primary
  signal, but fewer than 2 of 3 preserve singleton propagation
- `MIXED`:
  baseline reproduction passes, but only 1-2 of 3 perturbed variants retain the
  primary signal
- `FRAGILE`:
  baseline reproduction fails, or 0 of 3 perturbed variants retain the primary
  signal

## Garden-of-forking-paths constraints

1. Only the four codebooks above are allowed.
2. No extra distance metrics are allowed.
3. No feature dropping, feature weighting, or model tuning is allowed.
4. RF and logistic hyperparameters are inherited verbatim from [[h-new-165-phonological-predictor|H-NEW-165]].
5. The [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] accepted-cluster table is inherited verbatim; no re-annotation.
6. No post-hoc threshold edits are allowed.
7. The purpose is robustness bounding, not discovering a "best" codebook.

## Expected outcome

Honest expectation before execution:

- the [[h-new-165-phonological-predictor|H-NEW-165]] primary signal should survive modest perturbations
- the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] singleton geometry is more likely to move, because the parent
  p-value sat exactly on the corrected edge

So the modal expectation is **ROBUST or ROBUST-PRIMARY-EDGE-SENSITIVE**, not a
clean collapse.

## Files

- Pre-reg: this file
- Script: `scripts/h_new_165_2_codebook_sensitivity.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-165-2.json`
- Finding: `findings/phase-b-hypotheses/h-new-165-2-codebook-sensitivity.md`
- Journal: `journal/h-new-165-2-run-1.md`
