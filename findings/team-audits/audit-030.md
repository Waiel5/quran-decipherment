---
audit_id: audit-030
date: 2026-04-14
target: findings/phase-c-structures/h-new-meta-3-prereg.md
target_finding: H-NEW-META-3 (third-null specification, task #118)
target_author: hypothesis-generator
stage: pre-execution pre-registration cleanliness audit
verdict: PASSED WITH TWO PRE-EXECUTION NOTES (non-blocking)
harking_test_result: 4/4 CLEAN PASS
mw5_compliance: N/A (this is a pre-reg, not a result)
mw6_compliance: PASS (this pre-reg is a null-calibration protocol, not a positive-claim protocol; MW-6 auditor self-mandate tightening does not apply to interval-gate calibration)
mw7_relevance: N/A
related_audits: audit-023 (H-META-2 BOTH_DISQUALIFIED precedent), audit-025 (PRE-REG-STANDARD-04 origin)
---

# Audit-030 — H-NEW-META-3 third-null specification pre-registration

## Executive verdict

**PASSED WITH TWO PRE-EXECUTION NOTES.** Execution of task #118 is **green-lit**. The two notes below are documentation items for the script header; neither blocks dispatch.

This is the cleanest pre-registration the project has produced. Every element of PRE-REG-STANDARD-04 is satisfied, the calibration-window discipline is locked before null design (not after), the three candidate nulls cover distinct methodological traditions (stratified permutation / block-bootstrap / parametric), the joint-verdict table is complete across all four (Gate 1 × Gate 2) cells, the tie-breaker is pre-committed with a conservative preference, and the failure protocol is pre-committed without loophole.

## HARKing 4-test framework verdict

**Test 1 — non-counting failed sub-tests:** CLEAN PASS. All three candidate nulls are counted, including the "all three fail → META-NULL-REINFORCED" publishable failure mode. No hidden exclusion.

**Test 2 — pre-existing mechanism:** CLEAN PASS. The root-cause diagnosis (§Background lines 28-34) is a structural-reasoning argument about which invariants each null preserves. The three candidates are derived from this diagnosis — they are not retrofitted to match a predetermined winner.

**Test 3 — pre-registered directional evidence:** CLEAN PASS. This is an interval calibration (not a significance test) so "directional" is reframed as "pre-committed calibration window." Window [0.005, 0.02] was locked before null design per hypothesis-generator's claim, and the joint verdict table is symmetric (PASS routes to eligibility; PARTIAL routes to provisional; FAIL routes to disqualification; all with equal prominence).

**Test 4 — refusal to rename/retrofit:** CLEAN PASS. The META-NULL-REINFORCED failure verdict is pre-committed: if all three candidates disqualify, H-NEW-1 / H-NEW-1-v2 remain caveated indefinitely, and a H-NEW-META-4 follow-up is registered as a separate task, not a retrofit of the current test. No renaming, no drift.

## Clean-pass verification of hypothesis-generator's four requested checks

### (1) Garden-of-forking-paths risk

The §"Garden of forking paths" disclosure (lines 151-157) correctly pre-specifies:
- Three candidates from distinct traditions (not single-tradition monoculture)
- Block size 8 for Null-D locked a priori (not tuned post-hoc)
- Stratification cells for Null-C locked as (surah_id × length-decile × rhyme-cluster), not optimized
- Poisson rate form for Null-E locked, not selected post-hoc
- Tie-breaker protocol pre-committed (Null-C preferred over Null-D and Null-E in case of tie)

**One item not disclosed but worth adding to the script header at execution time (Note 1, non-blocking):** the EXACT length-decile boundaries. Are the deciles computed over:
(a) the full 6,236-verse Quran corpus,
(b) each surah independently (which produces variable boundaries per surah), or
(c) the pooled Quran + Mutanabbī + Jāḥiẓ corpus (normalization-matched)?

This is not a defect of the pre-reg — the pre-reg says "length-decile (1-10)" which is adequate — but the tester should document the chosen computation in the script header with a "pre-committed 2026-04-14" timestamp before execution so that a future audit of the result cannot retroactively argue that the deciles were chosen to pass Gate 1. I recommend (a) — pooled Quran-level deciles — but any choice is acceptable as long as it's locked before running.

### (2) Winner-selection tie-breaker back-door risk

The tie-breaker (lines 126-131) is:
1. Smallest mean absolute deviation |recovered_z − planted_σ| averaged across 6 power-cells
2. If still tied, prefer Null-C (stratified permutation) as most conservative

**Verdict: NOT a back-door.** The concern would be if Null-C preference created a selection bias toward under-powered nulls (since Null-C is likeliest to lose power in small stratification cells). But tie-break step 1 resolves on Gate 2 magnitude, not on Gate 1 Type-I rate. If Null-C is under-powered, its mean-absolute-deviation on planted signals will be larger, and step 1 will select a competitor before step 2 fires. Step 2 only activates on true numerical ties, which are vanishingly unlikely across 6 continuous-valued power cells. **Tie-breaker is robust.**

### (3) META-NULL-REINFORCED failure verdict loophole check

Lines 132-138 pre-commit:
1. META-NULL-REINFORCED verdict (no rename to "inconclusive" or "deferred")
2. Equal-prominence failure publication
3. H-NEW-1 / H-NEW-1-v2 z-magnitudes remain caveated indefinitely
4. H-NEW-META-4 files as separate task (not a retrofit of H-NEW-META-3)

**Verdict: NO LOOPHOLE.** All four commitments are properly closed. The "radically different null design" provision (line 138) is correctly framed as a NEW task requiring its OWN pre-registration, not as a fallback within the current pre-reg. This is the exact opposite of the audit-023 T1 fallback-clause abuse pattern.

One sub-check: line 138 provision (b) describes conformal prediction or Bayesian posterior predictive check as examples. These are GENERATIVE EXAMPLES, not a pre-committed H-NEW-META-4 spec. If H-NEW-META-3 disqualifies all three, H-NEW-META-4 must be its own independent pre-reg — with its own cleanliness audit. That protocol is implicit in the "separate H-NEW-META-4" language. **Clean.**

### (4) Power-cell Bonferroni adjustment question

Hypothesis-generator asked: "Does the power-cell definition (6 cells × 3 candidates = 18 checks) need a Bonferroni-adjusted magnitude threshold, or is strict-per-cell sign+magnitude sufficient?"

**Answer: strict-per-cell sign+magnitude IS sufficient, AND it is actually MORE CONSERVATIVE than a Bonferroni-adjusted magnitude test.** Reasoning:

- A Bonferroni-adjusted test would loosen the per-cell threshold (e.g., from |Δ| < 2σ to |Δ| < 2σ × √18) to maintain family-wise error rate on a composite HO.
- Strict-per-cell sign+magnitude is an **intersection test** (all 6 cells must PASS for one candidate to pass Gate 2). Intersection tests are MORE conservative than union tests, not less — they require ALL 18 checks to pass, which Bonferroni would not enforce.
- The intersection-test structure means: false positives are bounded by the product of individual cell error rates, which is vanishingly small (2σ² raised to power 6 is ~0.05⁶ ≈ 10⁻⁸).
- The actual statistical concern in the opposite direction: intersection tests are PROHIBITIVELY HARSH on the candidate. Relaxing from 2σ to 3σ (the pre-specified relaxed fallback) is the correct mitigation — it acknowledges that 6-cell intersection is a stringent gate.

**The strict/relaxed dual-threshold structure is exactly right.** Do not Bonferroni-adjust. Do not relax to single-cell-only testing. Keep the 6-cell intersection at strict 2σ, with pre-specified 3σ relaxed fallback. **Clean as currently specified.**

## Additional scrutiny items (auditor-initiated)

### Rules-tuple and seed discipline

- Rules tuple (line 6, 149): (no-tashkeel, orthographic-token, hafs-kufan, mashriqi) — matches H-META-2 for direct comparability. CLEAN.
- Seed 20260414 (line 14, 145): deliberately different from H-META-2's 20260413 to ensure fresh rhyme-set draws. CLEAN.
- Corpora (line 142): Mutanabbī-Dīwān and Jāḥiẓ-Ḥayawān — same as H-META-2 for direct head-to-head comparison. CLEAN.
- Independence claim (line 143): "Neither corpus has been inspected for this test's result; only their aggregate H-META-2 over-rejection rates were seen." This is the crucial independence statement. I accept it at face value; future result audit will cross-reference against the JSON outputs.

### Pre-registered calibration-first discipline (PRE-REG-STANDARD-04)

The critical claim in this pre-reg is:
> "Calibration window [0.005, 0.02] for Type-I and strict/relaxed magnitude tolerances for sign-correctness were locked BEFORE the three candidate nulls were designed (the design was downstream of the gates, not upstream)."

This ordering (gates → designs, not designs → gates) is the entire point of PRE-REG-STANDARD-04. **I accept hypothesis-generator's claim at face value** based on the following internal consistency checks:
- The window [0.005, 0.02] is the SAME window as H-META-2, i.e., it was carried forward from a pre-existing standard, not freshly negotiated during this pre-reg.
- The 6 power cells (2 corpora × 3 σ levels) are IDENTICAL to H-META-2's power cells — they were not expanded to 9 cells (which would have allowed post-hoc relaxation) or contracted to 4 cells (which would have allowed post-hoc strengthening).
- The 3σ relaxed fallback is not novel — it's the standard "within-3-sigma = soft PASS" convention used in physical-sciences replication tests.

**All three consistency checks support gates-locked-before-design.** Verdict stands.

### Bonferroni structure discipline

- k=3 locked in frontmatter (line 10). CLEAN.
- α_bon = 0.0167 computed correctly: 0.05 / 3 = 0.01666... ≈ 0.0167. CLEAN.
- Important clarification (line 13): "calibration is an interval test, not a significance test" — this is structurally correct. The Bonferroni applies to the downstream INTERPRETIVE decision (which candidate becomes the default null for H-NEW-1 retest), not to the PASS/FAIL of calibration itself. The calibration window [0.005, 0.02] stays fixed regardless of k. **This is the right way to frame it.**

## Pre-execution notes (non-blocking, for script header documentation)

**Note 1 — length-decile computation basis.** The pre-reg states "length-decile (1-10)" without specifying whether deciles are computed over the full Quran corpus, per-surah, or pooled with baseline. Tester should document the choice in the script header with a "pre-committed 2026-04-14" timestamp BEFORE running. I recommend pooled Quran-level computation but any consistent choice is acceptable. This prevents a future audit from arguing that decile boundaries were chosen to pass Gate 1.

**Note 2 — Null-E Poisson goodness-of-fit diagnostic.** The pre-reg mentions "goodness-of-fit diagnostic (log-likelihood vs observed)" (line 78) but does not specify a pre-committed numerical threshold for "good fit vs. mis-fit." Tester should add a pre-committed threshold BEFORE running — e.g., "log-likelihood within 10% of saturated model" or "χ² p-value > 0.05 for the Poisson fit vs. observed histogram." Without a pre-committed threshold, a post-hoc "Null-E mis-fit" claim could be used to dismiss an unfavorable Null-E result after the fact. Recommended threshold: **Poisson χ² p-value > 0.05 for the fit of the rate model vs. the observed residual-surprise histogram, pre-committed in script header**. If this threshold fails for Null-E, Null-E is DISQUALIFIED on goodness-of-fit grounds, reported as such, but the other two candidates still run.

**Both notes are documentation items, not pre-reg defects.** The pre-reg can be filed and execution can proceed; the tester adds the script-header documentation before running.

## Forward watches (for result-stage audit of H-NEW-META-3)

When the result file lands, the auditor (me) will check:

1. **Gate 1 rate computation.** Does the reported Type-I rate match the |z| > 2.576 two-sided threshold at nominal α=0.01? Is it computed as (number of draws with |z| > 2.576) / 1000 exactly, with no smoothing?

2. **Gate 2 strict-vs-relaxed verdict routing.** If any candidate falls between strict (|Δ| < 2σ) and relaxed (|Δ| < 3σ), the verdict MUST be "PROVISIONALLY CALIBRATED" — not "CALIBRATED." Check the routing code for off-by-one.

3. **Winner tie-breaker.** If 2+ candidates pass, verify tie-break step 1 computes mean absolute deviation correctly (arithmetic mean of |Δ| across 6 cells, not RMSE or median).

4. **META-NULL-REINFORCED verdict honoring.** If all three fail, the writeup must state "META-NULL-REINFORCED" verbatim (not "inconclusive," not "deferred") and explicitly state that H-NEW-1 and H-NEW-1-v2 remain caveated indefinitely.

5. **No fallback-clause language.** The writeup must not contain "per pre-registered fallback clause" language unless it refers to the strict/relaxed magnitude fallback (which IS pre-registered here). The absence of a "if timeout → rule-based fallback" style clause (the T1 LLM-judge abuse pattern) is CORRECTLY NOT PRESENT in this pre-reg. Tester must not add one at execution time.

6. **Rules-tuple documentation in JSON output.** The JSON output `findings/phase-c-structures/csv/h-new-meta-3.json` must include the rules_tuple and seed in its metadata block for replicability.

## Recommendation

- **Dispatch task #118 execution to computational-tester** with both pre-execution notes attached as script-header requirements.
- **Hypothesis-generator task #118 status:** AUDITOR-CLEARED, pre-reg clean. Move task #118 from in_progress to completed when execution dispatch happens.
- **Result-stage audit reserved as audit-031** (earliest; or later audit-0XX depending on which filings arrive first).
- **MW-6 instance tracking:** this pre-reg is a null-calibration protocol, not a positive-claim protocol. It is **not** a MW-6 instance (MW-6 auditor self-mandate tightening applies to protocols specifying new tests with directional predictions). Not counted.

## Classical-framing layer

Not applicable — this is a methodology audit, not a classical-doctrine audit. Classical-scholar involvement not required.

## Closing note on project-level significance

If Null-C, Null-D, or Null-E clears both gates, this is a **methodologically load-bearing result**: it would be the project's first calibrated null for the Markov-surprise family and would enable the H-NEW-1 retest that potentially restores the z-magnitude from caveated to robust. That's a very high-stakes outcome hinging on a clean execution of this pre-reg.

If ALL THREE fail, META-NULL-REINFORCED is ALSO load-bearing in the opposite direction: it permanently caveats H-NEW-1 and justifies retiring the Markov-surprise family (or escalating to conformal/Bayesian designs in H-NEW-META-4).

**Either outcome is publishable and consequential.** The pre-reg is honest about this — §Downstream consequence (lines 169-171) correctly notes that H-NEW-META-3 only establishes calibrated-null infrastructure and does NOT adjudicate H-NEW-1's z-magnitude. That's the right scope.

Filed under skeptical-auditor/audit-030.
