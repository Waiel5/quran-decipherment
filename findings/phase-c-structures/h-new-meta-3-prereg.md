---
finding_id: h-new-meta-3-prereg
phase: C-meta
status: PRE-REGISTERED, execution pending computational-tester pickup
date: 2026-04-14
rules_tuple: (no-tashkeel, orthographic-token, hafs-kufan, mashriqi)
parent_finding: h-meta-2 BOTH_DISQUALIFIED (2026-04-13)
target_family: Markov-surprise family (H-NEW-1, H-NEW-1-v2 and downstream)
pre_registration_reference: THIS FILE (locked 2026-04-14 before null design, per PRE-REG-STANDARD-04)
bonferroni_k: 3
bonferroni_family: three candidate nulls (Null-C, Null-D, Null-E) calibrated in parallel
alpha_unadjusted: 0.05 family-wise
alpha_bon: 0.0167 per candidate (for the PASS/FAIL gate itself — calibration is an interval test, not a significance test)
seed: 20260414
null_publishable: true
positive_publishable: true
one_sided_justification: N/A — calibration is a two-tailed interval gate
---

# H-NEW-META-3 — Third-Null Specification for Markov-Surprise Family

## Background

**H-META-2 result (2026-04-13, task #43):** BOTH_DISQUALIFIED.
- **Null-A** (label-permutation on break/conform × fixed Markov surface): Type-I rate 0.651–0.693 at nominal α=0.01 on two independent classical-Arabic corpora. Target calibration window [0.005, 0.02]. Over-rejection factor ~35×–70×. On planted σ=1.0 signals, recovered |z| deviates from planted by 3.1σ (Jāḥiẓ) to 6.2σ (Mutanabbī).
- **Null-B** (Markov re-trained under character-permutation surrogate): Type-I rate 0.62–0.72. Over-rejection factor ~32×–72×. On planted σ=1.0 signals, recovered |z| SIGN-FLIPS on Jāḥiẓ (+4.8σ when planted +1σ → null-B recovers −4.1σ direction error) while being close on Mutanabbī.

**Root cause diagnosis (hypothesis-generator 2026-04-14):**

1. Both nulls destroy *structural dependencies* that the Markov test statistic uses. Null-A leaves Markov surface fixed but shuffles class labels — if class membership is correlated with any *hidden confound* (verse length, surah position, rhyme-cluster register), the exchangeability assumption fails. Null-B re-estimates the Markov model under character permutation — but character permutation breaks the joint distribution of (word-internal structure, verse-final context), introducing artifactual transitions the original data never produced.

2. The common failure mode is **preservation of the wrong invariants**: neither null preserves the joint marginal structure of (verse-length, surah-id, class) simultaneously. Null-A preserves verse-length and surah-id but shuffles class; Null-B preserves class but shuffles characters. Neither preserves the *conditional* structure.

3. The fix is a null that preserves the **matched-pair structure**: each verse is exchangeable only with other verses from the same surah, of similar length, and the same rhyme-class. Exchangeability at that level is what the break/conform test actually needs.

## Candidate null specifications (three designs, pre-registered)

### Null-C: Stratified matched-pair permutation

**Design:** For each verse v in the observed corpus, define its stratum as (surah_id, length-decile (1-10), rhyme-cluster-id). Permute the break/conform class label only WITHIN stratum. This preserves:
- Surah of origin (eliminates surah-level confound)
- Verse-length rank (eliminates length-confound)
- Rhyme cluster membership (eliminates rhyme-register confound)

**Markov model:** trained once on the observed data, frozen. Not re-trained under permutation.

**Test statistic:** same as H-NEW-1-v2 (residual-mean-difference between break/conform classes at verse-end).

**Null draws:** B = 1000 permutations per calibration run.

**Weakness:** may lose power if stratification cells become too small (e.g., a stratum of size 1 or 2 allows no effective permutation). Power-test must confirm planted-signal recovery.

### Null-D: Block-bootstrap on surah-segments

**Design:** Partition each surah into contiguous blocks of 8 consecutive verses (pre-registered block size). For each calibration draw, resample blocks with replacement from within the same surah. Recompute the test statistic on the resampled data. This preserves:
- Local autocorrelation structure within a block (8-verse window)
- Surah identity
- Marginal distribution of verse-length and rhyme

**Markov model:** trained once per bootstrap draw on the resampled blocks.

**Test statistic:** same residual-mean-difference.

**Null draws:** B = 1000 bootstrap draws per calibration run.

**Weakness:** may over-preserve structure if the break/conform split has block-scale spatial correlation, inflating dependency and depressing Type-I rate below nominal.

### Null-E: Rate-matched parametric

**Design:** Fit a Poisson rate model for residual-Markov-surprise conditional on (length, rhyme-cluster, surah_id) under the null hypothesis H0: class has no effect. Generate synthetic corpora from the fitted rate model. Compute test statistic on each synthetic corpus.

**Markov model:** not explicitly modeled — subsumed into the residual-surprise rate parameter.

**Test statistic:** same residual-mean-difference, computed on synthetic corpora drawn from the parametric H0.

**Null draws:** B = 1000 parametric draws per calibration run.

**Weakness:** parametric mis-specification risk — if the Poisson-rate model mis-fits, calibration can fail in either direction. Requires goodness-of-fit diagnostic (log-likelihood vs observed).

---

## Calibration gates (PRE-REGISTERED, locked 2026-04-14 before execution)

All three candidates are tested against the **same two-gate standard** as H-META-2:

### Gate 1: Type-I independence calibration

**Protocol:** On EACH of Mutanabbī-Dīwān and Jāḥiẓ-Ḥayawān (same independent corpora as H-META-2 for direct comparability), run the candidate null with **B = 1000 random rhyme-set draws** (same 5-letter subset-from-28 construction as H-META-2). For each draw, compute |z| and check against nominal α=0.01 two-sided threshold (|z| > 2.576). Report rate of rejection.

**Gate 1 PASS:** Rate ∈ **[0.005, 0.02]** on BOTH corpora. (Same window as H-META-2.)

**Gate 1 FAIL:** Rate outside [0.005, 0.02] on EITHER corpus.

### Gate 2: Sign-and-magnitude calibration on planted signals

**Protocol:** For each corpus (Mutanabbī and Jāḥiẓ) and each planted effect size σ ∈ {0.5, 1.0, 2.0}, plant the same surprise-boost signal as H-META-2 Test B (p_flip chosen to achieve target σ at break-class verse-ends). Compute the candidate null's recovered z for each cell.

**Gate 2 PASS (strict):**
- SIGN: recovered z has same sign as planted effect in ALL 6 cells (2 corpora × 3 σ levels)
- MAGNITUDE: |recovered_z − planted_σ| < 2σ in ALL 6 cells (calibrated-within-2-sigma)

**Gate 2 PASS (relaxed fallback, pre-specified):**
- SIGN: correct in ALL 6 cells
- MAGNITUDE: |recovered_z − planted_σ| < 3σ in ALL 6 cells

**Gate 2 FAIL:** Any sign-flip or magnitude deviation > 3σ in any of the 6 cells.

### Joint verdict table

| Gate 1 | Gate 2 | Verdict |
|---|---|---|
| PASS | PASS-strict | **CALIBRATED — ELIGIBLE as default null for H-NEW-1 retest** |
| PASS | PASS-relaxed | **PROVISIONALLY CALIBRATED — eligible for H-NEW-1 retest with magnitude-flag footnote** |
| PASS | FAIL | **DISQUALIFIED (Type-I OK but power mis-calibrated)** |
| FAIL | * | **DISQUALIFIED (Type-I mis-calibrated)** |

### Bonferroni structure

- **k = 3** (Null-C, Null-D, Null-E tested in parallel)
- Family-wise α = 0.05
- Per-candidate α_bon = 0.0167

Note: the calibration window [0.005, 0.02] is an INTERVAL gate, not a significance gate. The Bonferroni k=3 applies to the downstream interpretive decision of which candidate becomes the default null. If MULTIPLE candidates pass both gates, they are ALL eligible; the downstream choice among them is ranked by Gate-2 closest-magnitude match as tie-breaker.

### Winner-selection protocol (if 2+ candidates PASS)

If both Null-C and Null-D pass, or all three pass, the tie-breaker is:

1. **Smallest mean absolute deviation** |recovered_z − planted_σ| averaged across all 6 power-cells
2. In case of ties at step 1, prefer Null-C (stratified permutation) as the more conservative choice — it requires fewer modeling assumptions than Null-D (block-bootstrap) or Null-E (parametric)

### Failure protocol (if ALL THREE candidates fail)

If Null-C, Null-D, and Null-E all disqualify:
1. Report H-NEW-META-3 as **META-NULL-REINFORCED** — the Markov-surprise family is pathologically resistant to calibration
2. Publish the failure with equal prominence to any potential success
3. H-NEW-1 and H-NEW-1-v2 z-magnitude claims remain caveated indefinitely under the H-META-2 STAGED subsection
4. Hypothesis-generator files a follow-up task to either (a) abandon the Markov-surprise family entirely, or (b) propose a 4th radically different null design (e.g., conformal prediction, Bayesian posterior predictive check) as a separate H-NEW-META-4

## Independent-corpus integrity

- Mutanabbī-Dīwān and Jāḥiẓ-Ḥayawān are the SAME corpora as H-META-2, used for direct comparability
- Neither corpus has been inspected for this test's result; only their aggregate H-META-2 over-rejection rates were seen
- Both corpora are independent of the Quran and were used in H-META-2 pre-registered BEFORE null-spec execution
- **Seed 20260414** is different from H-META-2's seed 20260413, ensuring the 1000 rhyme-set draws are fresh
- 6 power cells use the same planted-σ levels {0.5, 1.0, 2.0} for direct head-to-head comparison with Null-A and Null-B from H-META-2

## Rules tuple
(no-tashkeel, orthographic-token, hafs-kufan, mashriqi) — locked, matching H-META-2.

## Garden of forking paths (disclosed in advance)

- Three candidate nulls chosen a priori from distinct methodological traditions (stratified permutation; block-bootstrap; parametric H0) to avoid monoculture failure
- Block size 8 for Null-D pre-specified, not tuned
- Stratification cells for Null-C pre-specified as (surah_id × length-decile × rhyme-cluster), not optimized
- Poisson rate form for Null-E pre-specified, not selected from alternatives post-hoc
- Tie-breaker protocol (Null-C preferred if tied) pre-specified

## Expected runtime

Computational-tester estimate: ~40-60 minutes single-threaded Python for all three candidates × 2 corpora × (1000 calibration + 6 power cells).

## Output artifacts

- Script: `scripts/h_new_meta_3_third_null.py`
- JSON: `findings/phase-c-structures/csv/h-new-meta-3.json`
- Findings file: `findings/phase-c-structures/h-new-meta-3-third-null.md`

## Downstream consequence

If any candidate PASSES, it becomes the default null for a H-NEW-1 / H-NEW-1-v2 retest. That retest is SEPARATE from H-NEW-META-3 and will be its own task, with its own pre-registration. H-NEW-META-3 only establishes the calibrated-null infrastructure; it does NOT adjudicate H-NEW-1's z-magnitude.

## Approvals

- **Team-lead 2026-04-14:** Standing request for H-NEW-META-3 third-null design (audit of H-META-2 BOTH_DISQUALIFIED). Win condition pre-registered: Type-I rate in [0.005, 0.02] on both corpora AND sign-correct on all planted σ levels. This pre-reg satisfies both conditions.
- **Hypothesis-generator 2026-04-14:** Designed three candidate nulls (C/D/E) per team-lead's calibration specification.
- **PRE-REG-STANDARD-04 compliance:** Bonferroni k=3 + α_bon=0.0167 locked in frontmatter at proposal time. Calibration window [0.005, 0.02] locked in text body. Sign-magnitude gates pre-specified before script execution.
- **Team-lead 2026-04-14:** APPROVED for execution pending skeptical-auditor cleanliness clear.
- **Computational-tester 2026-04-14:** Signed off on candidate-set design (Null-C/D/E), σ=4.0 omission (direct H-META-2 comparability), and META-NULL-REINFORCED failure protocol.
- **Skeptical-auditor 2026-04-14 (audit-030):** PASSED WITH TWO PRE-EXECUTION NOTES (non-blocking). HARKing 4/4 CLEAN PASS. PRE-REG-STANDARD-04 compliance PASS. All four hypothesis-generator cleanliness checks cleared: garden-of-forking-paths disclosed, tie-breaker not a back-door, META-NULL-REINFORCED has no loophole, power-cell Bonferroni-adjustment NOT required (strict-per-cell is more conservative than Bonferroni). Full audit memo at `findings/team-audits/audit-030.md`.

---

## Execution-time documentation requirements addendum (pre-committed 2026-04-14, BEFORE script runs)

This addendum is a pre-execution amendment, timestamped and locked BEFORE computational-tester runs any code. Per audit-030, both items are non-blocking documentation requirements that must be captured in the script header at execution time.

### Addendum Note 1 — Length-decile computation basis (PRE-COMMITTED 2026-04-14)

Length-deciles for Null-C stratification shall be computed on the **pooled Quran corpus (full 6,236-verse Quran)**, NOT per-surah independently and NOT pooled across (Quran + Mutanabbī + Jāḥiẓ). Rationale: option (a) pooled-Quran-level is the auditor's recommended default, is corpus-internal (no cross-corpus mixing of length distributions), and prevents any future result audit from arguing deciles were chosen post-hoc to pass Gate 1.

Script header must include this commitment verbatim with the timestamp "pre-committed 2026-04-14 per audit-030 Note 1" BEFORE the first script run. No post-hoc decile-basis change is permitted without a formal amendment filed in TEAM-AMENDMENTS-LOG.md.

### Addendum Note 2 — Null-E Poisson goodness-of-fit threshold (PRE-COMMITTED 2026-04-14)

Null-E's goodness-of-fit diagnostic is operationalized as:

**Poisson χ² test p-value > 0.05 for rate-model fit vs observed residual-surprise histogram.**

- Procedure: bin the observed residual-Markov-surprise distribution into k bins (k pre-committed = 10, Sturges-rule ceiling for n~6k observations), compute expected counts under fitted Poisson rate model, compute χ² statistic, and χ² p-value with df = k − p_params − 1 where p_params = number of fitted parameters in the rate model.
- **Threshold**: p_value > 0.05 → Null-E passes GoF (eligible to run Gate 1 + Gate 2)
- **Threshold**: p_value ≤ 0.05 → **Null-E DISQUALIFIED on goodness-of-fit grounds** (reported in output JSON as `null_e_gof_disqualified: true`)
- **Downstream handling if Null-E GoF-disqualified**: Null-C and Null-D still run to completion; Gate 1/Gate 2 adjudication proceeds normally for the two remaining candidates; Bonferroni k=3 still applies as locked (NOT reduced to k=2 post-hoc — this preserves pre-reg discipline).

Script header must include this threshold commitment verbatim with the timestamp "pre-committed 2026-04-14 per audit-030 Note 2" BEFORE the first script run.

### Addendum commitment-lock

Both addendum notes are pre-committed 2026-04-14 and locked BEFORE script execution, matching the PRE-REG-STANDARD-04 discipline. Computational-tester must copy both notes verbatim into the script header docstring before running any candidate null. Violation of either note at result-stage audit (audit-031) constitutes a pre-reg violation.
