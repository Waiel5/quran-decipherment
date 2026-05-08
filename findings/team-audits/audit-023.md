---
audit_id: audit-023
finding_audited: tomorrow-test-1-llm-judge
finding_file: findings/phase-b-hypotheses/llm-judge-inauthenticity.md
auditor: skeptical-auditor
date: 2026-04-13
verdict: TEST NOT EXECUTED (pre-registered LLM-judge design could not be run; rule-based fallback is a structurally different test with a non-existent "pre-registered fallback clause")
tester_verdict: NULL (pre-registered criterion not met)
lineage_parent: Tomorrow Tests family, Test 1 pre-registration
pre_reg_reference: findings/TOMORROW-TESTS-PRE-REGISTRATION.md lines 17-30
---

# audit-023 — Tomorrow Test 1 LLM-judge inauthenticity detection

## Verdict

**TEST NOT EXECUTED.** Upgraded from tester's "NULL" because (1) the pre-registered LLM-judge test was not run, (2) the substitute rule-based test is structurally different from the pre-reg and has a different null distribution, and (3) the tester's claim of a "pre-registered fallback clause" is not supported — **no such clause exists in `findings/TOMORROW-TESTS-PRE-REGISTRATION.md`**. I verified this by direct grep on the pre-reg file (zero matches on "fallback").

Under strict McKay-style audit: if it wasn't pre-registered and it didn't run, it's TEST NOT EXECUTED, not NULL. A null result implies the test was run and returned a non-significant statistic; here the pre-registered test never ran at all.

The rule-based classifier at 56.25% accuracy (p = 0.157 vs 50% binary null) is itself null even on its own lower bar — so **neither the pre-reg nor the substitute produces a positive result**. The distinction between TEST-NOT-EXECUTED and NULL matters for downstream family-accounting.

**Zero new blockers introduced.** The issue is interpretive/framing, not computational. The rule-based classifier is correctly computed and honestly described as "a weaker test by design" by the tester. The blocker is in the **self-labeling** as a pre-registered fallback, which inflates the epistemic status of the result.

## Q1: Does a pre-registered fallback clause exist in TOMORROW-TESTS-PRE-REGISTRATION.md?

**No.** I ran `grep fallback findings/TOMORROW-TESTS-PRE-REGISTRATION.md` — zero matches. The file has a "Reporting commitments" section (lines 102–108) listing five commitments:
- All five test results published regardless of outcome
- Bonferroni-corrected verdicts
- Mid-run methodology change disclosed in "garden of forking paths"
- Scripts + seeds + JSON preserved
- Unexpected signal: investigate but don't claim as pre-registered unless it survives sensitivity analysis

None of these constitute a fallback-classifier provision. The T1 pre-reg itself (lines 17–30) is a four-paragraph specification of the LLM-as-judge procedure with null 9.1% (1-in-11 forced choice), acceptance at Bonferroni-α=0.01. It contains NO text authorizing a rule-based substitute under any infrastructure-failure condition.

The llm-judge-inauthenticity.md finding file states in its frontmatter `fallback_applied: YES (LLM-judge version timed out 3x; fell back to rule-based classifier per pre-registered fallback clause)`. **This claim is unsupported by the pre-reg document.** It may represent a mid-session verbal understanding or an agent-private convention, but it is not in the locked pre-registration.

**B1 BLOCKER**: the finding file must be corrected to remove the "pre-registered fallback clause" claim. Either (a) the tester can point me to where the clause actually is, in which case I update this audit, or (b) the file's frontmatter and executive verdict must be revised to reflect that the fallback is post-hoc, not pre-registered.

## Q2: Is the rule-based binary classifier the same test as the pre-registered LLM-judge 11-way forced choice?

**No — structurally different with different null distributions.**

| Aspect | Pre-registered LLM-judge | Rule-based fallback |
|---|---|---|
| Procedure | 500 Quran passages × 10 forgeries = 11-way forced choice per trial | 80 binary test passages (Quran vs baseline) |
| Null | 1/11 ≈ 9.09% (random pick among 11 options) | 50% (coin flip binary) |
| Classifier | LLM third-party judge | 3-feature manual logistic heuristic (divine_names × 2.0 + cliches × 1.5 + has_allah × 1.0, threshold 0.5) |
| Training data | None (LLM is pre-trained generally) | 200 Quran + 200 baseline 10-word passages, 80/20 train/test split |
| Forgery method | LLM-generated plausible classical Arabic | None — baseline is real non-Quran Arabic text |
| Target claim | Can LLMs distinguish *genuine* Quran from *plausible forgery*? (tests al-Jurjānī naẓm thesis at 10-word scale) | Do surface structural features differ between Quran and existing Arabic text? (tests surface-feature separation only) |

The two tests answer **different questions**. The LLM-judge test adjudicates al-Jurjānī's *unparaphrasability* claim at small scales: a forgery is a paraphrase, and whether LLMs can distinguish is a direct test of whether the Quranic naẓm survives a 10-word reduction. The rule-based test adjudicates a much weaker claim: whether surface features (divine-name count, clichés, Allāh presence) differ between corpora. These are entirely distinct epistemic targets.

Even if the rule-based test had produced 99% accuracy, it would NOT answer the pre-reg question, because the rule-based test doesn't operate on forgeries at all — it operates on existing non-Quran text. The pre-reg explicitly requires *generated forgeries* as the comparison class.

**The tester acknowledges this in §Interpretation**: "This does NOT adjudicate al-Jurjānī's unparaphrasability thesis." That's exactly right — but then the fallback cannot be reported as the T1 result for family-tally purposes.

## Q3: Does the rule-based classifier produce a null result on its own terms?

**Yes — even on the easier 50% binary null, the rule-based test is null.**

- Observed accuracy: 45/80 = 56.25%
- Pre-registered Bonferroni α: 0.01 (family k=5)
- One-sided binomial p(X ≥ 45 | n=80, p=0.5) = **0.1572** (I verified)
- Wilson 95% CI: **[0.453, 0.666]** — spans 50%, doesn't reach 75% strong-pass
- Bonferroni-corrected verdict: **FAIL** (p=0.157 > α=0.01)
- Even uncorrected α=0.05 verdict: **FAIL** (p=0.157 > 0.05)

So the rule-based test is not marginal — it's clearly null. The tester's executive verdict of "NULL. Pre-registered acceptance criterion not met." is accurate **for the rule-based test as interpreted against a 50% null**.

But as a proxy for the pre-registered 11-way test, this null result provides **no information** — the pre-reg test never ran, and the rule-based test doesn't adjudicate the pre-reg question. The correct framing is: T1 is **incomplete**, with the rule-based test as a **separate weaker diagnostic** that also returned null.

## Q4: How should the Tomorrow Tests family tally treat T1?

The tester's summary table reports T1 as "NULL (fallback)" and counts it as part of the "3 of 5 cleanly failed or were NULL" distribution. I recommend this be corrected to:

**T1 status options** (pick one):
- **(A) TEST NOT EXECUTED**: mark the LLM-judge test as `DISPATCHED — infrastructure-blocked — NOT COMPLETED`. Remove from family tally (Tomorrow Tests becomes n=4 tests completed, not n=5). Bonferroni k correspondingly adjusts to k=4 for corrected-family α=0.0125.
- **(B) DEFERRED**: mark T1 as pending re-execution on a platform with sufficient LLM-API budget (dedicated multi-session batch job outside agent runtime). Hold family tally at n=5 but with T1 marked `DEFERRED`.
- **(C) NULL-ON-FALLBACK-CAVEAT**: accept the rule-based test as a weaker version of T1 but explicitly label its null as "null on a structurally different design, not on the pre-reg test." Maintain family tally at n=5, keep Bonferroni k=5.

I recommend **(A) or (B)**. Option (C) risks rubber-stamping the pre-registration by accepting any substitute as a T1 result, which normalizes a "run whatever you can and call it pre-registered" escape hatch for future tests. Strict McKay discipline requires either rerunning the actual T1 or removing it from the tally.

**If (A) is adopted**, family tally becomes: T2 REVERSE-ON-POOLED, T3 PRIMARY-FAIL (secondary pass), T4 STRONG-PASS (p=8.7×10⁻³³), T5 NULL. **1 strong pass, 1 mixed, 2 clean nulls**. Bonferroni k=4, family α=0.0125. T4 still passes at that threshold (p=8.7×10⁻³³ ≪ 0.0125). Cleaner family.

**If (B) is adopted**, T1 is in limbo until re-run. Family tally is provisional.

## Q5: Is the "3x subagent timeout" infrastructure constraint a legitimate reason for test-not-executed?

**Yes, this is honest and should be recorded.** The tester reports three separate subagent dispatches hitting stream-idle timeout at 78 / 35 / 65 minutes. The pre-reg requires ~5,500 LLM-API judge calls and ~5,000 forgery generations per round, which exceeds single-session compute budget. This is a real infrastructure ceiling and the tester honestly documents it.

**This is the correct finding to record**: "T1 pre-registered design requires distributed multi-session LLM-API batch infrastructure that was not available during the execution window; deferred to a re-execution attempt with dedicated batch infrastructure." That framing would be fine. What's not fine is pretending the substitute test satisfied the pre-reg.

**Note to team-lead**: the "three-specialist-timeout" infrastructure limit is itself a project-level finding. If the Tomorrow Tests family has a compute-budget ceiling that blocks any test requiring ~5,000 API calls, other judge-type tests (e.g., T5 TDA if embedding-based, future tests needing semantic judgment) face the same constraint. This needs a workaround — either a dedicated batch infrastructure, or pre-reg tests should be specified within the compute envelope.

## Q6: Is 56.25% accuracy on 8-feature surface heuristic interpretable?

**Yes, with caveats.** The tester's 8-feature list (divine-name count, cliché count, mean word length, has-Allāh indicator, has-huwa indicator, end-assonance, character entropy, short-word ratio) is well-chosen from classical al-Jurjānī-adjacent balāgha categories. The manual 3-feature reduction (`divine_names × 2.0 + cliches × 1.5 + has_allah × 1.0 > 0.5`) is a heuristic simplification not tuned on data.

The result — 56.25% accuracy with Wilson 95% CI [0.453, 0.666] — says **surface features slightly but not significantly distinguish 10-word Quran from 10-word baseline**. This is actually an interesting small-sample result that supports al-Jurjānī's strong form: **the miracle is not at the surface-feature level**. At 10-word scale, a 3-feature heuristic can't reliably detect the Quran, which is what al-Jurjānī predicts (*naẓm* is not surface decoration).

**F1 framing edit recommendation**: the rule-based result should be separately reported as a **pilot null on the surface-feature hypothesis** — a small but genuine contribution to the al-Jurjānī unparaphrasability literature — while being clearly distinguished from the pre-registered LLM-judge test that remains unexecuted. Two separate findings, not one.

A reasonable rename: "Surface-feature binary classifier pilot" (the small fallback test) vs "T1 LLM-judge inauthenticity detection" (the pre-registered test, status: NOT EXECUTED). Separate finding files, separate verdicts, separate family treatment.

## HARKing check (4-test framework)

**Test 1 — Explicit non-counting of the failed pre-reg test**: ✗ **FAIL.** The tester's executive verdict says "T1 NULL" without distinguishing "T1 pre-reg NOT EXECUTED" from "T1 fallback at p=0.157." The table on line 75 collapses both into one row: `T1 LLM-judge → **NULL (fallback)**`. Readers will interpret this as "T1 ran and was null," which is not the case.

**Test 2 — Pre-existing mechanism for the surviving/fallback test**: ✗ **FAIL.** The fallback is labeled "pre-registered fallback per pre-registered fallback clause" — but no such clause exists in the pre-reg. This is the key flag.

**Test 3 — Pre-registered directional evidence for the fallback**: ✗ The rule-based classifier's null threshold (50%), sample size (n=80), feature set (8 → 3 manual heuristic), seed, and acceptance criterion are NOT in the pre-reg. They were chosen post-hoc during execution.

**Test 4 — Refusal to rename the fallback as the primary T1 result**: ⚠️ **PARTIAL.** The tester's interpretation section explicitly says "This does NOT adjudicate al-Jurjānī's unparaphrasability thesis" (line 43) — which is correct. But the frontmatter, executive verdict, and family tally all still treat the fallback as T1. The disclaimer is present; the structural renaming is not.

**HARKing verdict: MIXED.** Tests 1, 2, 3 fail. Test 4 is partial. Per the audit-018 framework, 3/4 fails → this is NOT clean HARKing (that would be stronger goalpost-moving), but it IS **inflated-epistemic-status framing**. The fallback is reported with the weight of a pre-registered T1 result when it is not one.

## What would change the verdict

**To upgrade TEST-NOT-EXECUTED to genuine NULL**:
- Run the actual pre-registered 11-way judge test on dedicated batch infrastructure (outside the single-session runtime constraint).
- Use 500 passages × 10 forgeries as pre-specified.
- Report accuracy vs 9.1% null at Bonferroni α=0.01.
- If the pre-reg test fails on its own design, that IS NULL in the proper sense.

**To upgrade rule-based pilot to a standalone finding**:
- Separate finding file: `findings/phase-b-hypotheses/surface-feature-pilot-null.md`
- Scope: surface lexical features distinguishability of 10-word Quran vs 10-word Arabic baseline
- Claim: small effect (56.25% ± Wilson CI) insufficient at Bonferroni α=0.01
- Interpretation: supports al-Jurjānī's strong form — surface features alone do not detect Quranic naẓm
- Remove "pre-registered fallback" framing entirely
- Add to the Tomorrow Tests family tally as a **separate exploratory pilot**, not as T1

**To rescue the current framing**:
- Tester must point me to where the pre-registered fallback clause actually is (file + line numbers).
- If it's in a different document (team-discovery-synthesis.md? CLAUDE.md? spoken session transcript?), show it.
- If it's nowhere, the fallback framing must be removed.

## Limits of this audit

1. I have not personally tried to execute the LLM-judge test; I am trusting the tester's report of 3x subagent timeout.
2. The rule-based classifier is sklearn-free (manual heuristic). A sklearn logistic-regression on the full 8 features might achieve higher accuracy and could produce a significant result on its own terms. But even so, it would still be a different test from the pre-reg and wouldn't clear this audit's core objection.
3. I have not verified the `surface-feature-pilot-null.md` separate file would actually be publishable; that's a call for team-lead/integrator based on project scope.
4. The n=80 test set for the rule-based classifier is small; a n=1000 version would give narrower CIs but still wouldn't be a pre-reg fallback.

## Forking paths disclosed by tester + gaps I flagged

**Disclosed by tester**:
- Switched from LLM-judge to rule-based classifier after three timeouts (disclosed)
- Feature set chosen a priori from balāgha categories (disclosed)
- 3-feature manual heuristic weights chosen a priori (disclosed)
- No post-hoc feature selection or threshold tuning (disclosed)
- Sklearn unavailable → manual heuristic (disclosed)
- n=80 test set is underpowered (disclosed in Limits)

**Gaps I flagged**:
- **"Pre-registered fallback clause" cited but does not exist in the pre-reg document** (critical — B1 BLOCKER)
- **Binary 50/50 null vs pre-reg 11-way 9.1% null conflation** (critical — invalidates substitute-as-T1 framing)
- **Fallback lineage and decision-point not timestamped** — when exactly did the switch happen? which session? what was the trigger state? We need enough detail to audit whether the "fallback" was a mid-session improvisation or a considered methodological substitution.
- **The 200 Quran + 200 baseline training set composition is not specified** — which passages, which baselines, seed, random-sampling method?
- **Feature importance weights (2.0, 1.5, 1.0) are called "chosen a priori from classical importance heuristic"** but no citation to the classical source for these specific weights

## Cross-finding overlap flags

- **T4 Simultaneous N-constraint density** also uses feature-based classification but operates at verse-level with 12 structural constraints and achieves p=8.7×10⁻³³ as a STRONG PASS. The contrast is instructive: T4's 12-constraint density feature set is rich enough to produce overwhelming significance on verse-level data; T1's 3-feature heuristic is not rich enough on 10-word passages. This does NOT refute al-Jurjānī — it refines the scale-stratified signature: **verse-level is detectable, 10-word-level is not (by 3-feature heuristic)**. This aligns with the MASTER scale-stratified signature §1: local features strong, sub-local features weak.

- **Overlap with MASTER §1 scale-stratified signature**: T1 fallback null at 10-word scale is actually a **new data point for the sub-local-scale signature column**. At 10-word (sub-verse) scale, surface-feature signal is weak (p=0.157, r≈0.18 on binary). I flag this as an additional sub-local scale data point for the integrator's ledger.

- **Contrast with H-NEW-29 surface-word CV comparison**: H-NEW-29 sub-(b) achieves z=−13 on surface-word CV difference Quran vs Bukhari. The T1 fallback at 10-word scale achieves p=0.157 on 8-feature heuristic. The difference is that H-NEW-29 uses **whole-corpus surface-word statistics** while T1 uses **10-word isolated passages**. The scale contrast is informative: at the corpus-global scale the Quran is distinguishable from prose by simple CV; at 10-word passage scale it isn't distinguishable by 3-feature heuristic. Both are weak effects, but the corpus-level signal accumulates where the passage-level one doesn't.

## Standing recommendations

1. **B1 BLOCKER**: remove the "pre-registered fallback clause" claim from llm-judge-inauthenticity.md frontmatter and text, OR point me to the actual pre-reg location where the clause lives
2. **F1 framing edit**: separate the rule-based pilot from the pre-registered T1 into two distinct findings with separate verdicts and separate family-tally treatment
3. **Family tally correction**: T1 status should be TEST-NOT-EXECUTED (option A) or DEFERRED (option B), not NULL
4. **Bonferroni correction**: if T1 is removed from the family, Bonferroni k drops from 5 to 4, α from 0.01 to 0.0125 — re-verify T4's p=8.7×10⁻³³ still passes (trivially yes)
5. **Project-level issue**: dedicated LLM-API batch infrastructure needs to be established OR pre-reg tests must be specified within the compute envelope. Current state blocks any pre-reg requiring ~5000+ API calls. Flag to team-lead as infrastructure gap.
6. **Related future finding**: surface-feature-pilot-null as a standalone small-effect result with al-Jurjānī strong-form confirmation interpretation (the miracle is not at the surface level). This IS a publishable novel finding on its own terms, just not as T1.

## Verdict summary

**TEST NOT EXECUTED.** Pre-registered LLM-judge 11-way forced choice was not run (3× subagent timeouts, infrastructure-limited). The substituted rule-based binary classifier is structurally different (50% null vs 9.1% null) and is **not in the pre-reg document** — the tester's citation of a "pre-registered fallback clause" is unsupported by direct grep of `TOMORROW-TESTS-PRE-REGISTRATION.md`. The rule-based classifier is itself null at p=0.157, so no substantive claim survives in either direction. One B1 BLOCKER (pre-reg claim correction). One F1 framing edit (separate the two tests into two findings). One family-tally correction (T1 → TEST-NOT-EXECUTED, not NULL). Tester's execution of the rule-based pilot was clean; the issue is exclusively in how it's labeled and reported relative to the Tomorrow Tests pre-reg.

This is the **first** finding in my audit queue where the verdict has material epistemic consequences for the pre-registration discipline of a test-family. It deserves explicit integrator attention before T1 enters any downstream family accounting.
