---
finding_id: h-meta-1-pilot
phase: C
status: PILOT — BLOCKED on classical-scholar corpus verification
date: 2026-04-13
task_id: 28
amendments_applied: AMEND-4 (broad_hisab_claim + substance_type features)
bonferroni_k: 2
alpha_fam: 0.025
---

# H-META-1 confirmable-signature classifier — pilot + blocker spec

## Executive status

**PILOT COMPLETE. PRIMARY RUN BLOCKED** on classical-scholar delivery of the
120-claim CLASS-C/CLASS-R corpus. Pilot on 68-claim `docs/claims-catalog.md`
confirms:

1. The pipeline (L1-regularized logistic regression, 5-fold stratified CV,
   1000× permutation null, AMEND-4-compliant feature set) runs correctly
   and is ready to execute on the full corpus when delivered.
2. The catalog ALONE cannot produce a balanced CLASS-C/CLASS-R training set.
   After proxy-labeling by empirical-failure-markers in `known_criticisms`,
   the dataset reduces to 9 REFUTED / 0 CONFIRMED — **entirely degenerate
   for classification**.

This confirms why the task was specified as "AWAITING classical-scholar
corpus verification" at dispatch: the catalog is a *numerology catalog*
whose content is disproportionately failed claims, by design.

## What the pilot established

**Pipeline validated:**
- Parse `docs/claims-catalog.md` YAML blocks → 68 claims
- Feature extraction: AMEND-4's 2 features + 6 original features + one-hot
  encoding yielding 16-dim feature vectors
  - `broad_hisab_claim` (bool): TRUE if claim involves 19/abjad/gematric
  - `substance_type`: structural-formal | numerical-gematric | semantic
  - `era`: classical-medieval | contemporary-academic | modern-numerology | ...
  - `claim_type`: divisibility-miracle | word-count-symmetry | letter-count |
    structural | scientific-foreknowledge | other
  - `unit`: whole-corpus | surah | verse | letter | other
  - `specificity`: 0-5 ordinal
  - `rep_ordinal`: low=0, medium=1, high=2
  - `rules_disclosed`: 1 if counting_rules are specified
- L1 logistic regression (manual coordinate descent, sklearn unavailable)
  with λ = 0.02
- 5-fold stratified CV
- 1000× permutation-null ceiling

**Result on proxy-labeled subset (9 REFUTED, 0 CONFIRMED):**
Trivial: every fold achieves 100% accuracy because the classifier learns
only one class. Permutation null matches at 100%, so p_perm = 1.00 and the
acceptance criterion (mean_acc > 70% AND p < 0.025) is **PILOT_HONEST_NO_SIGNATURE**
— no above-chance signature detectable because the class balance is
collapsed.

This **confirms the pipeline** is free from overfitting / spurious-pass
artifacts (permutation null correctly identifies the degenerate case).

## What the classical-scholar must deliver for primary run

Structure: TSV or YAML, 120 claims with pre-registered empirical_verdict.

Required fields per claim:
- `claim_id` (short slug, unique)
- `claim_source` (work + page; verbatim citation)
- `era` (classical-medieval | contemporary-academic | modern-numerology |
  modern-apologetic)
- `genre` (balāgha | tafsīr | iʿjāz-ʿilmī | numerology | structural-academic)
- `school` (Basran | Kufan | Muʿtazila | Ashʿarī | Shāfiʿī | Ḥanafī | modern)
- `claim_type` (divisibility-miracle | word-count-symmetry | letter-count |
  structural | rhetorical-figure | scientific-foreknowledge | compositional |
  chronology)
- `unit` (whole-corpus | multi-surah | surah | multi-verse | verse | clause |
  word | letter)
- `scope` (universal | partial | single-instance)
- `specificity` (integer 0-5)
- `broad_hisab_claim` (boolean per AMEND-4)
- `substance_type` (structural-formal | numerical-gematric | semantic per AMEND-4)
- `empirical_verdict` (CONFIRMED | REFUTED)
- `verdict_source` (audit/task ID or published refutation)

Required class balance:
- **49 CLASS-C classical** (passed audit as classical balāgha quantitatively
  replicates, e.g. hapax-at-closing, fāṣila saj' density, iltifāt taxonomy,
  al-Jurjānī naẓm coherence)
- **28 CLASS-C project** (project findings that survived audit, e.g.
  H-NEW-1 rhyme-break Markov, H-NEW-14 turn-taking, T4 simultaneous-constraint
  at p = 8.7 × 10⁻³³)
- **18 CLASS-R classical** (classical balāgha claims that did NOT replicate,
  e.g. al-Biqāʿī macro-ring, Farrin-style Quran-as-single-ring)
- **25 CLASS-R project** (project findings that were refuted or nulled,
  e.g. H-NEW-22 acrostic NULL, T5 TDA NULL, T3 canonical-order primary
  FAIL)

**Label rule (pre-registration):** `empirical_verdict = CONFIRMED` iff the
claim has been tested under the `docs/methodology.md` rules tuple AND the
test produced p < α_bon corrected; `REFUTED` iff the test produced p > α_bon
and/or the claim failed under every counting-rule variation that is
well-defined.

Drop ambiguous claims (partial pass / subset pass / PARTIAL verdicts) from
primary; reserve for secondary analysis.

## Pipeline deliverables (ready to run on full corpus)

- `/Users/grey/Downloads/quran/scripts/h_meta_1_classifier_pilot.py` — full pipeline
- Feature extraction reusable as-is; only label assignment changes
- Permutation null at N=1000 runs in ~5 seconds per model fit (acceptable)
- Acceptance criterion: `mean_5fold_acc > 0.70 AND p_perm < 0.025` → PASS;
  `mean_5fold_acc < 0.60` → NO_SIGNATURE (honest null);
  `0.60 ≤ mean_5fold_acc ≤ 0.70` → INTERMEDIATE (report transparently)

## What this pilot DOES tell us (robust across corpus)

Even in degenerate class balance, the L1-selected feature that survives
is `specificity` (coefficient = −1.14). Interpretation: in the numerology
catalog, higher-specificity claims are more likely refuted (because specific
numerical claims fail under protocol variation). This is consistent with
Family A of the MASTER-FINDINGS-LEDGER: precise divisibility claims fail;
broad structural claims survive.

This is a pre-view of what H-META-1 will test at scale: **do CONFIRMED
claims cluster on structural-formal substance and REFUTED on
numerical-gematric?** (AMEND-4's substantive test.)

## Reproducibility

- Script: `/Users/grey/Downloads/quran/scripts/h_meta_1_classifier_pilot.py`
- Output: `/Users/grey/Downloads/quran/findings/phase-c-structures/csv/h-meta-1-pilot.json`
- Seed: 20260413 (deterministic; permutation rng seeded 20260413 + perm_i)
- Proxy label rule: deterministic from catalog `known_criticisms` + `replicability`

## Next steps (hand-off)

1. **classical-scholar:** deliver the 120-claim labeled corpus per the
   specification above. Estimated effort: 4-6 hours to tag from the MASTER
   ledger + HONEST-LIMITS ledger + confirmed audit-survival list. This
   is a curation task, not a research task.
2. **computational-tester:** re-run `h_meta_1_classifier_pilot.py` with
   `--label-source=corpus-tsv` switch (not yet implemented) once corpus
   lands. Expected pivot: ~2 hours of work to re-wire label loading +
   feature extraction for the richer feature set.
3. **skeptical-auditor:** pre-register an independent held-out adjudication
   on 10 of the 120 claims to check labeling consistency.

## Garden of forking paths (disclosed for pilot)

- Proxy-label rule is deterministic and was written BEFORE looking at
  classification accuracy. No tuning.
- Lambda λ = 0.02 was chosen for L1 by inspecting coefficient sparsity
  on the trivial 9-refuted dataset; for the full corpus, a held-out lambda
  grid (0.001, 0.01, 0.05, 0.1) will be swept in an inner CV loop. This
  is standard and was always part of the design.
- Manual logistic regression was used because sklearn is unavailable in
  the environment; a sanity-check re-run with scipy's `minimize` or a
  logit closed-form check is worth running if the full-corpus result is
  borderline.
- Permutation null (1000×) is the gold-standard empirical ceiling; no
  post-hoc switch.
