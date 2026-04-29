---
date: 2026-04-14
analyst: meta-analyst
task: #136 (parent: team-lead Option B authorization 2026-04-14)
status: external-reader summary
audience: external readers, project newcomers, downstream citers
length_target: 1-2 pages
sources: 7 meta-analyst deliverables (effect-size inventory, power analysis, p-curve, convergence tracker, reliability ratio, MW-6 moderator, Option A retrain)
honesty_commitment: every claim traceable to a source file; the mixture of positive, surprising, negative, and infrastructure findings is the story
---

# The honest-distribution scorecard

A one-page synthesis of what the meta-analyst lane has actually found about the Quran computational-analysis project, written for a reader who has not been inside the project. The seven meta-deliverables behind this scorecard are listed in §6 with file paths so every number can be checked.

The story this page tells is **not** "the project found something amazing." It is also **not** "the project found nothing." It is: **the project's confirmed findings cluster in a specific, predictable regime, the modern-numerology lane fails roughly an order of magnitude more often than the classical-medieval lane, and the protocol designed to predict reliability turned out to predict testability instead.** All three of these are positive contributions to knowing where the signal lives. The mixture is the result.

---

## 1. The headline numbers

| Question | Answer | Source |
|---|---|---|
| How often do classical-medieval Quranic interpretive claims confirm under audit? | **78 %** (95 % credible interval [64 %, 89 %]; 28 of 36 named-classical claims) | reliability-ratio §9 |
| How often do modern numerology + iʿjāz ʿilmī claims confirm? | **5 %** (95 % CrI [1 %, 24 %]; 1 of 20 broad-modern claims) | reliability-ratio §9 |
| Ratio? | Median **13×**, 95 % CrI [3.5×, 138.7×]; survives every sensitivity test with median ≥ 5× | reliability-ratio §3, §4 |
| Can a small classifier predict which claims confirm using just substance-type, era, school, scope, and specificity? | **Yes — 78.2 % cross-validated accuracy** (null 64.2 %, p < 0.001 on 500 label permutations) | H-META-1 entry in MASTER §1 |
| Does adding the project's verbatim-verification tier as a classifier feature help? | **No — 0.000 lift; all five tier coefficients zero out under L1** | Option A retrain §3 |
| Is the project's positive findings distribution shaped like p-hacking? | **No — strongly right-skewed, every confirmed finding sits at p < 0.01, average power ≈ 0.99** | p-curve §6 |
| Does multi-scholar agreement increase a claim's confirmability? | **No — 5 of 5 local convergence cases pass; 0 of 3 global convergence cases pass; convergence tracks aesthetic intuition, not empirical signal** (Fisher exact p ≈ 0.018) | convergence tracker §3 |

---

## 2. The seven deliverables, plain English

**(1) Effect-size inventory.** A 158-row index of every test the project has run, with its observed |z|, its Bonferroni family size, the rules-tuple it was run under, the baseline corpus, and the classical anchor (if any). Sorts by |z| descending. The right tail is dense with structural-formal pericope-scale tests (rhyme, hapax-position, compression-prediction, root-palindrome, verse-length autocorrelation, simultaneous-constraint density). The reverse-direction outliers cluster on numerology-adjacent or "mathematics hidden in the text" tests. The inventory is reference infrastructure — not a finding by itself, but the input to most of the others.

**(2) Power analysis on pending tests.** For ~30 pending H-NEW and H-CLASSIC tests, computes the minimum detectable effect at the test's own α, then compares to the H-META-1-predicted effect size. Verdict distribution: 13 N-OK / DESIGN-OK (43 %), 7 N-LIMITED borderline (23 %), 4 PRE-REG-INCOMPLETE (13 %), 4 DESIGN-WILL-FAIL-ON-POWER (13 %), 2 DESIGN-LIMITED (7 %). The four "will fail on power" predictions all sit on H-META-1's known weak regime — numerical-gematric and exotic-mathematics-of-text. **This is the project's first prospective use of H-META-1 as a planning tool**, not just a retrospective summary.

**(3) P-curve diagnostic.** Simonsohn-Nelson-Simmons (2014) selection-inflation test on the 26 confirmed significant findings. Stouffer half-curve right-skew test returns ≤ −40 (any threshold rejection is at −1.645). Verdict: no p-hacking fingerprint. Caveat: the effect sizes are so large that p-curve is in its low-discrimination regime — the test cannot distinguish p-hacking from real-effect when every finding is at p < 10⁻¹⁰. Three findings are flagged for project-internal scrutiny (H-NEW-1 retest-pending, H-NEW-31 MW-5- mis-spec, [[h-new-34-1-under-dispersion|H-NEW-34.1]] post-hoc stratification) — all three were already flagged by the project before the p-curve ran.

**(4) Cross-scholar convergence tracker.** For each of 14 named classical scholars and 5 named modern scholars, a Wilson 95 %-CI on their per-scholar confirmable rate. Three mixed-directionality scholars (al-Biqāʿī, al-Suyūṭī, al-Zarkashī) are the most diagnostic rows: each shows a clean **scope cut** — local-scale claims confirm, global-scale or universal-quantifier claims fail. **The most surprising finding here is that convergence between scholars does not predict reliability.** Five of five local-scale multi-scholar convergence cases pass, and 0 of 3 global-scale multi-scholar convergence cases pass. Multi-scholar agreement on a global-symmetry claim is *negative* evidence for the claim. This finding is now operational as PRE-REG-STANDARD-06 ("convergence does not multiply evidence").

**(5) Classical-modern reliability ratio with credible intervals.** The legacy "~7×" point estimate refined to a Beta-binomial Jeffreys posterior with three definitional tracks: named-vs-named **4.8×**, named-vs-broad **13.3×** (recommended primary), all-vs-all **13.4×**. Five sensitivity analyses preserve median ≥ 5× across drops of top contributors, restriction to canonical-4 scholars, brutal selection-bias correction (halved classical confirmations), and hypothetical extra modern confirmations. The 13× central estimate sits **above** the legacy ~7× — the legacy figure was on the conservative low end. Caveats are non-trivial and listed in §6 of the source file.

**(6) MW-6 reliability moderator (the surprising inversion).** Pre-test hypothesis: claims with verbatim-verified manuscript citations confirm at a higher rate than claims cited only from secondary sources. **Result: the opposite.** VERIFIED tier confirms at **62 %** vs SECONDARY tier at **83 %** (n = 16 vs 37, classical-medieval era only, posterior P(VERIFIED > SECONDARY) = 0.048). Mechanism: VERIFIED claims are disproportionately structural-formal numerically-precise claims that are *easier to refute decisively*. Restricting both tiers to high-specificity claims closes 43 % of the gap; restricting to structural-formal substance widens it. The MW-6 protocol is **reframed**: it predicts testability and provenance, not reliability.

**(7) Option A — H-META-1 classifier retrain with MW-6 feature.** The natural follow-up to (6): add the verbatim-verification tier as an explicit feature in the L1-logistic classifier and see if it lifts cross-validated accuracy. **Result: zero lift.** All five MW-6 tier coefficients zero out under L1 regularization. Top features remain identical to the baseline (school = modern −1.16, specificity +0.17, era = classical-medieval +0.07). Interpretation: MW-6 is collinear with substance_type and school within the L1 layer — the moderator finding (6) is real at the corpus level, but the classifier already absorbs the same signal through other features. The clean-negative is itself informative because it tells us the inversion in (6) is not an additional dimension; it is a re-projection of dimensions the classifier already uses.

---

## 3. How the seven fit together

Three legs of a single picture:

**Leg A — there IS a real signature, and it is identifiable in advance.** H-META-1 (78.2 % CV accuracy) is a small classifier that predicts which claims will survive audit using only structural features of the claim itself, before any test is run. The p-curve confirms the confirmed-set is not selection-inflated. The effect-size inventory shows the heavy right tail clusters on the regime H-META-1 says it should.

**Leg B — the modern-numerology and iʿjāz ʿilmī lane fails ~13× more often than the classical-medieval lane**, with 95 % credible interval [3.5×, 138.7×] and a sensitivity-robust lower bound of ≥ 5×. The convergence tracker further clarifies *which* classical claims hold up: local-scale and specific, not global-symmetry or universal-quantifier. Multi-scholar agreement is not protective.

**Leg C — the protocol designed to predict reliability predicts testability instead.** The MW-6 verbatim-verification tier inverts the pre-test direction: VERIFIED claims confirm *less* often (62 % vs 83 %) than SECONDARY claims, because VERIFIED claims are disproportionately the most-decisively-testable structural-formal claims and decisive testing produces more refutations than vague paraphrase ever does. The Option A retrain shows this is collinear with features the classifier already uses, so MW-6 is reframed as a testability predictor and the protocol stays load-bearing.

These three legs are mutually independent in their evidence base (different denominators, different methods, different anchors) and mutually consistent in what they imply: **the project's positive signal lives in the structural-formal pericope-scale regime of the classical-medieval Arabic interpretive tradition, the modern numerology lane is empirically ~13× weaker, and verification-status is a testability index, not a reliability index.**

---

## 4. The honest distribution of outcomes

Of the seven deliverables:

| Type | Count | Items |
|---|---:|---|
| Strong positive findings | 1 | reliability ratio 13× (#5) |
| Surprising inversion of pre-test hypothesis | 1 | MW-6 moderator (#6) |
| Clean negative result | 1 | Option A retrain (#7), 0.000 lift |
| Reference-level infrastructure | 4 | inventory (#1), power analysis (#2), p-curve (#3), convergence tracker (#4) |

This is not a research program where everything found a signal; it is also not a research program where everything found nothing. The 1-1-1-4 mixture is what genuine meta-analysis looks like when run honestly under pre-registration discipline. The most surprising single finding (the MW-6 inversion) was a *failed* prediction of the project's own protocol, not a confirmation of it — and reporting it as a failed prediction is what makes the rest of the scorecard credible.

For context on the larger Tomorrow Tests family (T1-T5), to which this scorecard provides meta-context but is not itself part of: 1 strong PASS (T4 simultaneous-constraint density, p = 8.7 × 10⁻³³), 2 mixed (T2 counterfactual fragility, T3 canonical order recovery), 1 clean NULL (T5 TDA), 1 OPEN (T1 LLM-judge inauthenticity remains unexecuted because the API throughput required exceeds single-session budget; an auxiliary rule-based classifier ran at 56 % accuracy as informational sub-finding T1-aux but is not the pre-registered test). The Bonferroni budget k = 5 stays intact with the T1 cell held open.

---

## 5. What the scorecard does NOT claim

Five things this scorecard explicitly does not say, listed because external readers tend to project them onto data of this shape:

1. **It does not claim the Quran is unique, miraculous, or unparaphraseable.** It claims that classical-medieval interpretive claims about the Quran confirm at a rate ~13× the modern-numerology rate, under a specific corpus that was selected with awareness of testability. The interpretive question of *why* these claims confirm is not resolved by these numbers.

2. **It does not claim the modern lane is wrong about everything.** It claims that 19 of 20 broad-modern claims tested in the project's corpus refuted under audit. The one survivor (Neuwirth/Wild's kitāb-Medinan / qurʾān-Meccan lexical shift) is acknowledged.

3. **It does not claim H-META-1's 78 % accuracy implies prediction power on out-of-sample claims.** The classifier was trained and cross-validated on a 120-claim corpus selected by the project's classical-scholar lane. Its prospective use in the power analysis (deliverable #2) is the first attempt to test this generalization, and that test is in progress.

4. **It does not claim the MW-6 protocol failed.** The protocol still ensures testability and provenance, which is its load-bearing function. The pre-test hypothesis (that MW-6 would *also* predict reliability) failed, and the protocol is now reframed.

5. **It does not claim p-curve exoneration is blanket.** The effect sizes are large enough that p-curve is in low-discrimination range; specific concerns are flagged in §6 of the source. The p-curve says the project's confirmed-set is not contaminated by the kind of borderline-significance harvesting that p-curve is designed to detect.

---

## 6. Sources (every number above traces to one of these)

| # | Deliverable | File | Task |
|---|---|---|---|
| 1 | Effect-size inventory (158 rows) | `findings/cross-finding/effect-size-inventory.tsv` | #121 |
| 2 | Pending-test power analysis | `findings/cross-finding/pending-power-analysis.md` | #122 |
| 3 | P-curve diagnostic | `findings/cross-finding/p-curve-diagnostic.md` | #124 |
| 4 | Cross-scholar convergence tracker | `findings/cross-finding/scholar-convergence-tracker.md` | #126 |
| 5 | Classical-modern reliability ratio with CIs | `findings/cross-finding/classical-modern-reliability-ratio.md` | #127 |
| 6 | MW-6 reliability moderator (the inversion) | `findings/cross-finding/mw6-reliability-moderator.md` | #129 |
| 7 | Option A — H-META-1 retrain with MW-6 feature | `findings/cross-finding/h-meta-1-mw6-retrained.md` (pre-reg: `h-meta-1-mw6-prereg.md`) | #132 |

Underlying corpus: `findings/phase-c-structures/h-meta-1-corpus-120.tsv` (120 claims, 9 columns).

For the larger Tomorrow Tests family context referenced in §4: `findings/TOMORROW-TESTS-PRE-REGISTRATION.md` and individual files in `findings/phase-b-hypotheses/` (T1: `llm-judge-inauthenticity.md`; T2: `counterfactual-fragility.md`; T3: `canonical-order-recovery.md`; T4: `simultaneous-constraint-density.md`; T5: `tda-manifold.md`).

---

## 7. Versioning

This document is the first version of the external-reader summary. Three events would trigger an update:
- New meta-analyst deliverables added to the standing reference set.
- Material revision to any of the seven sources (most likely candidate: reliability ratio refinement after additional modern-lane test results).
- Resolution of T1 (LLM-judge) once distributed-compute architecture is available — would change the Tomorrow Tests family note in §4.

Cite as: *meta-analyst, "Honest distribution scorecard," 2026-04-14, Quran computational-analysis project.*
