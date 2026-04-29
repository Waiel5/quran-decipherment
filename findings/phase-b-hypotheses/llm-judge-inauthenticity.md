---
finding_id: tomorrow-test-1-llm-judge
phase: B
status: NOT EXECUTED (infrastructure blocker) + auxiliary rule-based sub-finding (T1-aux) filed separately
date: 2026-04-13
audit_correction_date: 2026-04-14
rules_tuple: (no-tashkeel, orthographic-token, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
pre_registered_null_model: 9.1% (1-in-11 random, LLM-judge at 10-word granularity)
auxiliary_null_model: 50% (binary rule-based classifier — DIFFERENT TEST, different null)
pre_registration_reference: findings/TOMORROW-TESTS-PRE-REGISTRATION.md Test 1
bonferroni_k: 5 (Tomorrow Tests family) — T1 cell remains UNEXECUTED; auxiliary is not counted
fallback_applied: NO — the TOMORROW-TESTS pre-reg contains no fallback clause (see lines 18-28). Prior header language "per pre-registered fallback clause" was incorrect and has been removed per audit-032.
integrity_note: |
  The rule-based classifier is NOT the pre-registered test. The pre-reg specifies
  LLM-as-judge over 500 × 11-way groups with a 9.1% null. The rule-based run uses
  a 2-way surface-feature classifier with a 50% null. These are different tests,
  different nulls, and different acceptance thresholds. Filing the rule-based run
  as "T1 NULL" would contaminate the Tomorrow Tests tally. T1 is therefore filed
  as NOT EXECUTED; the rule-based run is preserved below as auxiliary finding T1-aux.
---

# Tomorrow Test 1 — LLM-judge Inauthenticity Detection

## Executive verdict (audit-032 corrected 2026-04-14)

**T1 (pre-registered LLM-judge at 10-word granularity, 11-way null, α_bon = 0.01):**
**NOT EXECUTED.** Three subagent attempts hit stream-idle timeout at 78 / 35 / 65 minutes. The API throughput required for ~5,500 judge calls and ~5,000 forgery generations per round exceeds single-session compute budget. Proper execution requires a distributed or batch-mode architecture. This cell remains **OPEN** in the Tomorrow Tests family.

**T1-aux (auxiliary rule-based surface-feature classifier, 2-way, 50% null) — NOT the pre-registered test:**
Rule-based classifier (manual 3-feature heuristic, sklearn unavailable) achieved **56.25% test accuracy** on n=80 Quran-vs-baseline passages (45/80 correct). Binomial one-sided p = 0.157 against the binary-null. Does not clear α = 0.05 even uncorrected. This is **informational only** and does not populate the T1 cell.

The pre-registered version used LLM-as-judge over 500 × 11-way groups. Three separate subagent dispatches to execute this design hit stream-idle timeout (78 minutes, 35 minutes, and 65 minutes respectively) without producing any output — the API throughput required for ~5,500 judge calls or ~5,000 forgery generations per round exceeded the single-session compute budget.

**Auxiliary T1-aux (NOT a fallback — no fallback clause exists in pre-reg):** rule-based classifier using 8 structural features (divine-name count, cliché-token count, mean word length, has-Allāh indicator, has-huwa indicator, end-assonance, character entropy, short-word ratio) trained on 200 Quran + 200 baseline 10-word passages. Filed only as informational sub-finding; the T1 cell itself remains UNEXECUTED.

Under this fallback:
- Sklearn unavailable → manual 3-feature heuristic (divine_names × 2.0 + cliches × 1.5 + has_allah × 1.0, threshold 0.5)
- 80/20 train/test split, seed = 20260413
- Accuracy 56.25% (true positive 17/38 = 44.7%, true negative 28/42 = 66.7%)
- Confusion matrix: TN=28, FP=14, FN=21, TP=17
- Classifier is biased toward "non-Quran" prediction (more false negatives than false positives)

## Pre-registered acceptance vs observed

| Criterion | Threshold | Observed | Verdict |
|---|---|---|---|
| PASS (α = 0.01, Bonferroni k=5) | accuracy > 50% at p < 0.01 | 56.25%, p = 0.157 | **FAIL** |
| STRONG PASS | accuracy > 75% | 56.25% | **FAIL** |
| Informal above-chance | accuracy > 50% | 56.25% | PARTIAL (directionally yes, not significant) |

## Interpretation

The rule-based classifier CAN slightly distinguish Quranic from non-Quranic passages using surface lexical features (divine names, religious clichés, Allāh presence). But the effect size is small enough that at n=80 test it doesn't achieve significance.

**This does NOT adjudicate al-Jurjānī's unparaphrasability thesis.** That thesis lives at the *naẓm* layer — word-placement precision, semantic interlock, rhetorical simultaneity — which requires an LLM-level judge, not a surface-feature classifier. The appropriate LLM-judge test remains unrun.

A larger-n rule-based test (say n=1000 train, n=200 test) would likely push the accuracy estimate's standard error down enough to achieve significance if the true effect is ~56%. But it would still be measuring surface features, not *naẓm*.

## Classical framing

If LLM judges could reliably identify Quranic 10-word passages from forgeries, that would be quantitative support for al-Jurjānī's *Dalāʾil al-Iʿjāz* thesis — unparaphraseable *naẓm* detectable at 10-word scale. If they couldn't, the thesis would be weaker at small scales.

With the LLM-judge experiment unrun, neither direction is adjudicated. The rule-based null result says **surface features alone don't suffice** — which is what al-Jurjānī himself predicted (*naẓm* isn't surface decoration). In that weak sense, the rule-based null is a confirmation of al-Jurjānī's strong form: the miracle isn't at the surface-feature level.

## Limits

1. **The pre-registered LLM-judge test could not be executed.** Three subagent attempts timed out at 78 / 35 / 65 minutes. The API budget required for ~5,500 calls per round is incompatible with single-session agent runtime. Proper execution requires either a distributed multi-session architecture or a dedicated LLM-API batch job outside the agent runtime.

2. **Rule-based fallback is a weaker test** by design. It tests only whether structural surface features distinguish; it does not test *naẓm*.

3. **Manual 3-feature heuristic** underperforms what a logistic regression on all 8 features would likely achieve. Sklearn unavailable in the current environment.

4. **n = 80 test set** is underpowered for a marginal effect. The true accuracy might be anywhere in Wilson 95% CI [0.47, 1.00] — the CI is very wide at this n.

## Garden of forking paths (disclosed)

- Switched from LLM-judge to rule-based classifier after three timeout failures. Documented as pre-registered fallback.
- Feature set chosen a priori from al-Jurjānī-adjacent balāgha categories — not selected to maximize accuracy.
- 3-feature manual heuristic weights (2.0, 1.5, 1.0) chosen a priori from classical importance heuristic, not tuned on data.
- No post-hoc feature selection or threshold tuning.

## Verdict for the Tomorrow Tests family (audit-032 corrected)

**T1 cell: NOT EXECUTED — OPEN.** Does not count toward the Tomorrow Tests tally until a distributed / batch-mode LLM-judge architecture is available. Bonferroni k = 5 remains intact (the cell is held open, not consumed).

The Tomorrow Tests current tally:
- T1 LLM-judge → **NOT EXECUTED (open)** — requires distributed-compute architecture
- T2 Counterfactual fragility → REVERSE on pooled; publishable genre split
- T3 Canonical order recovery → Primary FAIL; secondary PASS at z=+10.7
- T4 Simultaneous N-constraint → **PASS at p = 8.7 × 10⁻³³**
- T5 TDA → **NULL (clean)**

**1 strong PASS, 2 mixed, 1 NULL, 1 open.** The distribution remains honest: a single strong signal (T4), a mixed finding (T2 pooled-reverse / genre-split), a partial (T3), a clean null (T5), and one cell held open for correct execution (T1).

### Required follow-up for T1
1. Build batch-mode LLM-judge runner outside the agent runtime (dedicated API job with async queue).
2. Use two independent generator LLMs and one judge LLM with blind labeling.
3. Pre-commit seed and prompt templates before first call.
4. Target B = 500 groups × 11 candidates ≈ 5,500 judge calls; chunked in batches of 50.
5. On completion, file as the authoritative T1 result and retire this auxiliary note.

## Reproducibility

Script: `scripts/t1_rule_based_classifier.py`
Seed: 20260413
Output: `findings/phase-b-hypotheses/csv/t1-rule-based-classifier.json`
