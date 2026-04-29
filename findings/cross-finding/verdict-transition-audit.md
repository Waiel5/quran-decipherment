---
date: 2026-04-14
analyst: meta-analyst
task: #142 (team-lead authorization 2026-04-14, Option 3 from four-candidate menu + Items 7-8 additions)
status: draft v1 (pre-sensitivity pass)
deliverable_type: cross-finding meta-analysis
sources:
  - MASTER-FINDINGS-LEDGER.md §1/§3/§3b/§3c/§3d/§4/§6 (transition trail)
  - findings/team-audits/audit-001.md..audit-032 (lineage drivers)
  - TEAM-AMENDMENTS-LOG.md PRE-REG-STANDARD-04..07 + MW-1..8 (protocol-level transitions)
  - findings/cross-finding/honest-distribution-scorecard.md §5 (context)
scope_items_locked:
  - 1-6 as meta-analyst proposed, 2026-04-14
  - 7 (AUDIT-032 case study) + 8 (baseline comparison framing) per team-lead addition 2026-04-14
honesty_commitment: every transition listed is traceable to a MASTER-ledger entry or audit file; the mixture of direction-preserving and direction-flipping transitions is the story
length_target: 3-4 pages
---

# Verdict-Transition Audit — how often and why does the project revise its own verdicts?

## Context and purpose

This audit answers a question external readers ask about any pre-registration research program: **how stable are the verdicts once they are filed, and when they change, what drives the change?** A project whose findings never revise is either too small to have observed revision events, too protected from auditing to notice when it should, or publishing results at sub-audit quality. A project whose findings revise constantly is either in early-stage instrument development or doing the work so carelessly that the pre-registration discipline isn't binding. The honest middle is a measurable positive revision rate with characterizable drivers.

The purpose of this audit is not to claim the project's revision rate is good or bad in absolute terms. It is to (a) enumerate every status-transition in the ledger, (b) categorize transitions by mechanism, (c) place the aggregate rate in the context of published pre-registration programs, and (d) name the currently mid-transition findings so that downstream readers can weight them appropriately until they resolve.

This audit is the ninth meta-analyst deliverable in the standing reference set. Prior eight: effect-size inventory (#121), pending power analysis (#122), p-curve diagnostic (#124), scholar convergence tracker (#126), classical-modern reliability ratio (#127), MW-6 moderator (#129), Option A retrain (#132), honest-distribution scorecard (#136). This audit provides *temporal* discipline to complement their *cross-sectional* discipline.

## 1. Enumerating verdict transitions in MASTER §1/§3/§3b/§3c/§3d/§4

A verdict transition is defined for this audit as: **any change to a finding's MASTER-ledger section assignment, its pre-registered acceptance verdict, or the primary quantitative magnitude it reports, that occurred after the finding was first filed.** Renumbering, cross-ref updates, and prose cleanup do not count. Sibling-finding additions (e.g., H-NEW-1-v2 alongside H-NEW-1) do not count as transitions on the parent unless they change the parent's disposition.

Under this definition, the project's transition inventory is:

| # | Finding | Original disposition | Revised disposition | Category | Driver |
|---|---|---|---|---|---|
| 1 | H-NEW-1 (verse-ending consonant Markov-residual) | §3c CONFIRMED z≈+8 | audit-001 DOWNGRADE (2/27 cells surviving) | spurious-downgrade-reverted | audit-015 meta-audit found audit-001's null itself broken; H-NEW-1 restored to §3c |
| 2 | H-NEW-1 (continued) | §3c CONFIRMED (restored) | §3d STAGED PENDING-RETEST | null-broken-retest-pending | H-META-2 BOTH_DISQUALIFIED 2026-04-14 — entire Markov-surprise null family fails calibration on classical Arabic positive controls |
| 3 | H-NEW-16 (cross-word phonetic palindromes) | pre-registered one-tailed (Quran MORE palindromes than baseline) | REVERSE-SIGNAL CONFIRMED at p ≈ 10⁻⁶ (Quran has ~half the palindromes of matched null) | reverse-direction-relabel | data landed with sign opposite to pre-reg; finding re-filed as reverse-signal rather than refuted-primary |
| 4 | H-NEW-34 (verse-final abjad-sum modular residue) | NULL-confirmed primary | NULL-primary + post-hoc reverse under-dispersion flagged | reverse-direction-relabel (exploratory overlay) | primary verdict stayed, post-hoc signal surfaced, immediately flagged as not-pre-registered; gate [[h-new-34-1-under-dispersion|H-NEW-34.1]] pre-registered for upgrade attempt |
| 5 | [[h-new-34-1-under-dispersion|H-NEW-34.1]] (Muʿallaqāt + length-stratified upgrade gate) | pre-registered under-dispersion direction | MECHANISM-INCONSISTENT (5 Jāḥiẓ cells + 1 Bukhari cell over-disperse at α_bon) | staged-to-refuted-mechanism-inconsistent | length-stratification flipped the direction; §3d → §4 migration pending auditor C1/C2 ruling |
| 6 | [[h-new-2-iltifat-catalog-rho|H-NEW-2]] × iltifāt catalog ρ-correlation | pre-registered positive-sign on 3 signals | all 3 signals reverse-sign at p₂ < 0.005 | reverse-direction-relabel | audit-013 path #3 rule explicitly FAIL; but "no correlation" null strongly rejected; publishable as reverse |
| 7 | H-NEW-29 (root renewal-process CV) | pre-registered absolute CV<1 (al-Jāḥiẓ *takrār maqbūl*) | dual verdict: (a) absolute-form NULL (mathematically impossible for natural-language content-word streams), (b) comparative-form CONFIRMED at z = −14.79 pooled | post-hoc-mechanism-split | pre-registered operationalization retroactively recognized as impossible at gate-time; comparative form filed as separate finding rather than as rescue-rename (anti-HARK 4/4 per audit-022) |
| 8 | H-NEW-35 (verse-length autocorrelation, al-Sakkākī *īqāʿ*) | primary confirmed z=+13.127 | primary-confirmed BUT discriminative-vs-prose FAILS (Jāḥiẓ ρ essentially identical) | post-hoc-mechanism-split | primary existence-claim survives; secondary distinguishing-classical-iʿjāz claim refuted; al-Sakkākī vindicated as description, not as iʿjāz distinguisher |
| 9 | H-NEW-20 (al-Rāzī linear naẓm) | CONFIRMED Stouffer Z=+30.76 | length-residualized Z=+9.57 (strict pre-registered reading: FAIL by 0.43; liberal reading: PASS) | methodology-upgrade-supersession | MW-1-GATE-A per-surah length residualization; finding tempered but not refuted |
| 10 | H-NEW-30 (descriptive pattern) | pre-registered inferential test | DEMOTED to descriptive annotation, N=8 | demotion-to-power-insufficient | power analysis showed N=8 cannot support inferential test; honest disposition rather than force-file |
| 11 | H-NEW-23 (hapax-verse-final slot) | CONFIRMED with 2.24× enrichment | rehabilitated framing — Muʿallaqāt positive-control shows effect present in pre-Islamic monorhyme at 1.37×; Quran is 4.23× stronger than pool but no longer zero-baseline claim | methodology-upgrade-supersession (positive-control reframe) | T-004 Muʿallaqāt positive control under MW-5 protocol; finding preserved, framing sharpened |
| 12 | T2 (counterfactual fragility) | pre-registered "Quran MORE fragile than matched Arabic" | pooled-baseline REVERSE z=−4.86; genre-split: Quran +5.38 vs prose, −6.44 vs poetry | reverse-direction-relabel + post-hoc-mechanism-split | data landed with pooled-baseline reverse sign; genre split revealed the pooled result was an artifact of stacking two populations |
| 13 | T3 (canonical order recovery) | pre-registered primary τ>0 at p<0.01 on 5-metric combined-adjacency | primary FAIL τ=+0.015; secondary adjacent-pair PASS z≈+10.7; length-residualized NCD τ=+0.648 | post-hoc-mechanism-split | pre-reg primary design was wrong for length-dominated ordering; secondary legs uncovered the real signal |
| 14 | T5 (TDA verse-embedding manifold) | pre-registered at 99th-percentile within-baseline threshold | CLEAN NULL — 0 of 4 bottleneck distances clear the 99th percentile | (no transition — direct NULL) | verdict matches acceptance rule mechanically |
| 15 | T4 (simultaneous N-constraint density) | pre-registered KS + tail-k≥8 criteria | CLEAN PASS at p = 8.7 × 10⁻³³ (~30 orders past Bonferroni) | (no transition — direct PASS) | verdict matches acceptance rule mechanically |
| 16 | **T1 (LLM-as-judge inauthenticity)** | **initially filed NULL via "per pre-registered fallback clause" (56.25% rule-based accuracy, binomial p=0.157 vs binary null)** | **audit-032 correction: NOT-EXECUTED, cell held OPEN; T1-aux filed as informational-only sub-finding** | **false-verdict-filing-corrected-to-unexecuted (NEW CATEGORY)** | **the original filing called a 2-way surface-feature classifier "the test" when the pre-reg specified an 11-way LLM-judge over 5,500 calls; no fallback clause in pre-reg; filing error corrected without consuming the Bonferroni cell** |
| 17 | 90-claim classical-quantitative audit (§3b) | 49 CONFIRMED / 18 PARTIAL / 18 CONTRADICTED at initial pass | no transitions: verdicts are mechanical exact-count checks | (no transition — mechanical) | these are look-up-and-count claims, not inferential tests; locked on contact |
| 18 | al-Rāzī's muqaṭṭaʿāt-divine-names theory | classical claim surveyed | REFUTED at 0/78 surviving shuffle null | (no transition — direct refutation on first test) | inferential test from start |
| 19 | HASHR option-(iii) | classical cluster-flag | PROMOTED-WITH-FOOTNOTE | methodology-upgrade-supersession | tier promotion after rule-tuple-robustness check across mashriqi/maghribi |
| 20 | MW-6 reliability moderator pre-test | pre-test hypothesis: VERIFIED tier confirms at higher rate than SECONDARY | INVERSION: VERIFIED 0.618 vs SECONDARY 0.829, P(VERIFIED>SECONDARY)=0.048 | reverse-direction-relabel (protocol-level) | see scorecard #5c Leg C; MW-6 reframed as testability predictor, not reliability predictor |
| 21 | Legacy "~7×" classical-modern reliability ratio | point estimate from earlier triangulation | Beta-binomial Jeffreys posterior 13.27× [3.53, 138.69] | methodology-upgrade-supersession | legacy ~7× sits at 20.6th percentile of refined posterior; see #5a |

**Total observable transitions: 21 events across ~60 findings in the MASTER ledger.**

Three findings appear twice in the table because they underwent two sequential transitions (H-NEW-1: #1 then #2). Three entries (#14, #15, #17, #18) are listed to anchor the denominator but do not count as transitions — they are direct verdict matches to pre-registration. Excluding those, **17 transition events on ~57 auditable findings** gives a corpus-level transition rate of **~30%**. This figure is discussed in §5 below against published baselines, where its meaning is not the same as a replication-rate.

## 2. Transition-type taxonomy

Nine categories emerge, organized by what the transition changes:

| Category | Count | What it changes | Canonical example |
|---|---:|---|---|
| **A. reverse-direction-relabel** | 5 | sign of the signal, not its existence | H-NEW-16 palindrome; [[h-new-2-iltifat-catalog-rho|H-NEW-2]]×iltifāt ρ; T2 pooled |
| **B. post-hoc-mechanism-split** | 4 | primary verdict remains, secondary disentangles sub-claims | H-NEW-29 dual; H-NEW-35 existence-vs-discrimination; T3 four-leg |
| **C. methodology-upgrade-supersession** | 4 | magnitude tempered by new method (length residualization, positive control, CI refinement, retag) | H-NEW-20 MW-1; 13× ratio supersedes ~7×; T-004 reframes H-NEW-23 |
| **D. null-broken-retest-pending** | 2 | entire null family flagged as uncalibrated; finding held in §3d PENDING-RETEST | H-NEW-1 + H-NEW-1-v2 (under H-META-2) |
| **E. spurious-downgrade-reverted** | 1 | an earlier downgrade is itself audited and overturned | H-NEW-1 audit-015 reverts audit-001 |
| **F. staged-to-refuted-mechanism-inconsistent** | 1 | pre-registered upgrade gate fails direction post-stratification; §3d → §4 route | [[h-new-34-1-under-dispersion|H-NEW-34.1]] MECHANISM-INCONSISTENT |
| **G. demotion-to-power-insufficient** | 1 | finding re-filed as descriptive, not inferential | H-NEW-30 N=8 |
| **H. protocol-level inversion** | 1 | pre-test hypothesis about a *protocol* (not a finding) is inverted | MW-6 testability-not-reliability |
| **I. false-verdict-filing-corrected-to-unexecuted** (NEW) | 1 | the filed verdict was on the wrong methodology; correction routes to NOT-EXECUTED / cell-held-OPEN, **not** to verdict-flip | T1 LLM-judge audit-032 |

Categories A + B together dominate: **9 of 17 transitions (53%) preserve the finding but change its framing.** Category C is the next largest at 4. Categories D-I are singletons or twins and each encode a distinct epistemic pathway.

**The key structural observation.** Transitions that *flip* a finding's overall direction are rare (Category F, 1 event). Transitions that *nuance* a finding's interpretation or tempering are common (Categories A-C, 13 events). This ratio is what a mature rigorous program should produce: you learn more about why findings work than about whether they work. A program dominated by Category F flips would indicate weak instruments; a program with zero Category A-C nuances would indicate that the second-pass audits aren't doing anything.

## 3. Per-category count, driver, and significance

**Category A — reverse-direction-relabel (5 events).** The driver is always the same: data lands with a sign opposite to the pre-registered prediction, the null of "no signal" is nonetheless strongly rejected, and the finding is re-filed with the reverse sign disclosed rather than quietly abandoned. The project handles this with what the audit-022 closure calls "anti-HARK discipline": the reverse-sign version is filed as a separate finding rather than as a rescue of the original hypothesis. Five instances, all discovered and routed by different lanes (computational-tester on H-NEW-16, team-discovery on [[h-new-2-iltifat-catalog-rho|H-NEW-2]]×iltifāt, Tomorrow Tests on T2 pooled, H-NEW-34 post-hoc, MW-6 at protocol level), gives this pattern convergent validity.

**Category B — post-hoc-mechanism-split (4 events).** The pre-registered primary verdict holds, but the secondary analysis disentangles sub-claims and the sub-claims have different fates. H-NEW-29 is the cleanest: absolute CV<1 mathematically impossible for any natural-language content-word stream, so the primary NULL is a methodology failure the auditor should have caught before runtime; the comparative CV-vs-prose form is what the classical claim actually meant and it confirms at z=−14.79. H-NEW-35 splits similarly: the existence of verse-length autocorrelation is real, the discriminative-vs-prose claim fails because Jāḥiẓ shows the same rhythm. T3's four-leg split is the largest single instance: primary combined-τ FAILS, adjacent-pair PASSES, Nöldeke chronology FALSIFIED, length-residualized NCD STRONG — one finding, four disjoint verdicts across its legs.

**Category C — methodology-upgrade-supersession (4 events).** The archetype is H-NEW-20 (al-Rāzī linear naẓm): MW-1-GATE-A required per-surah length residualization after the original Stouffer Z=+30.76 was discovered to be length-enhanced; residualized strict-reading Z=+9.57 (0.43 below pre-reg threshold); residualized liberal-reading Z=+22.78. The finding is preserved but tempered. Similarly, H-NEW-23 is re-framed with Muʿallaqāt as positive-control baseline rather than zero baseline. The classical-modern reliability ratio's refinement from legacy "~7×" to 13.27× [3.53, 138.69] is another instance at the meta-analytic level: the earlier estimate wasn't wrong, it was under-specified. The most important property of Category C transitions is that they can go in either direction: sometimes the new methodology strengthens the finding (H-NEW-23 discriminative Quran-vs-Muʿallaqāt residual), sometimes it weakens it (H-NEW-20 strict reading).

**Category D — null-broken-retest-pending (2 events).** H-NEW-1 and its sibling H-NEW-1-v2, both held in §3d-PENDING-RETEST under the newly-created 2026-04-14 sub-class. The driver is H-META-2 (Task #43): the null-model comparator found that both null specifications used throughout the Markov-surprise family fail pre-registered calibration on independent classical Arabic corpora (reject rates 0.620–0.720 vs calibration window [0.005, 0.02]), and one null specification flips sign on planted-σ injection on Jāḥiẓ. The published z-magnitudes for H-NEW-1 are therefore flagged not-reliable until H-NEW-META-3 (Task #118, in-progress, pilot pre-confirmed META-NULL-REINFORCED) resolves whether any calibrated null exists for this corpus. This is the cleanest possible example of the project disciplining itself: rather than accept or reject the finding, it quarantines it with a pre-locked revert-condition. Category D is how pre-registered honesty handles "the data is fine but the null is broken."

**Category E — spurious-downgrade-reverted (1 event).** H-NEW-1's audit-001 → audit-015 trajectory. Audit-001 downgraded H-NEW-1 based on a null specification; audit-015 later determined that the same null returned z=−2.81 on Jāhilī monorhyme positive-controls, meaning the null was broken and the downgrade was spurious. H-NEW-1 was restored to §3c — then later transitioned again via Category D when H-META-2 found the whole null family broken. A single Category E event is both reassuring (the second audit caught the first audit's error) and concerning (a Category E event by definition means an earlier audit got it wrong). Its rarity in this project so far is informative but not yet statistically meaningful.

**Category F — staged-to-refuted-mechanism-inconsistent (1 event).** [[h-new-34-1-under-dispersion|H-NEW-34.1]] was pre-registered to upgrade H-NEW-34's post-hoc reverse under-dispersion signal from exploratory to confirmed, conditional on the signal surviving Muʿallaqāt rhymed-baseline + length-stratified controls. Under AMEND-27 length stratification (authoritative tie-breaker), the signal reverses: Bukhari stratified z = +3.66 at m=11 (over-disperses); Jāḥiẓ stratified z = +10.85 / +19.26 / +27.15 at m = 7 / 11 / 19 (strong over-dispersion). Pre-reg Table 2 routes this outcome to MECHANISM-INCONSISTENT → §4 refutations after auditor clear on C1/C2 caveats. This is a Category F event caught *by the pre-registration discipline itself*: the pre-reg specified a decision rule that routed the observed outcome mechanically to refutation without auditor discretion.

**Category G — demotion-to-power-insufficient (1 event).** H-NEW-30 was downgraded to a descriptive annotation after power analysis showed N=8 cannot support inferential testing. This is the honest alternative to force-filing a low-power inferential verdict on an underpowered dataset. Category G rarity so far suggests either that the project's initial power audits are catching most of these before filing, or that the pending power analysis (task #122) has not yet caused the remaining underpowered tests to demote.

**Category H — protocol-level inversion (1 event).** MW-6 was designed as a verification-discipline protocol with an implicit pre-test hypothesis that VERIFIED-tier claims would confirm at a higher rate than SECONDARY-tier claims. The pre-test hypothesis was inverted: VERIFIED 0.618 vs SECONDARY 0.829, posterior P(VERIFIED > SECONDARY) = 0.048. The protocol's load-bearing function (testability + provenance) remains intact; only the informal pre-test about reliability was wrong. See scorecard #5c Leg C for full framing. Category H differs from Categories A-G in that the transition is not at the finding level but at the protocol level — the thing that changed is an entire operating rule, not a single test's verdict.

**Category I — false-verdict-filing-corrected-to-unexecuted (1 event, NEW CATEGORY).** AUDIT-032 (Task #137, in-progress filing). This is epistemically distinct from every other category because the transition does **not** flip a verdict, does **not** nuance an existing verdict, and does **not** quarantine a finding pending a downstream test. It **retracts the test identity itself.** T1 was pre-registered as an 11-way LLM-as-judge comparison over 500 groups × 11 candidates ≈ 5,500 API calls with a 9.1% (1-in-11) null. Three subagent dispatches timed out at 78 / 35 / 65 minutes because the single-session API budget couldn't carry the test. The original filing then filed a **2-way surface-feature rule-based classifier** with a **50% binary null** as "T1 NULL via pre-registered fallback clause" — but there was no fallback clause in the pre-reg, and a 2-way surface-feature test is not an 11-way *naẓm*-layer judge test. The audit-032 correction re-files T1 as **NOT EXECUTED** (cell held OPEN, Bonferroni k=5 intact, the test itself awaits distributed / batch-mode architecture per Task #138), with the rule-based run preserved as **T1-aux** — informational only, not a Bonferroni-consuming member of the T1 cell.

This is the project's first instance of "we filed a verdict on the wrong methodology and the correct disposition turns out to be NOT-EXECUTED." It is epistemically distinct from rules-tuple-sensitivity rehabilitations (which are verdict-flips *under a valid methodology variant*), from null-broken retests (which quarantine the methodology family while awaiting a resolution test), and from methodology-upgrade-supersession (which moves to a *different valid method*). Category I corrects a filing error in which a *different test than the one pre-registered* was reported as the pre-registered test. The correct response is not to flip the verdict — it is to retract the filing and hold the cell open.

**Why Category I deserves its own category and not a note on Category D.** Categories D and I both hold a finding in a not-definitive state. They differ in epistemic structure: Category D (null-broken) holds a finding because the null specification used is not calibrated, so the observed effect's magnitude is unreliable — the test executed, the null did not discriminate. Category I (false-filing-corrected) holds a finding because the test did not execute at all and a surrogate was mis-labelled as it — the test identity was wrong, not the null. Conflating them would let one category contaminate the other: future "null broken" findings would become suspected of being "filing errors," and future "filing errors" would leak into the "null needs retest" holding bay where they can't be resolved by an H-META-N test. The category separation forces the auditor to name which pathology applies.

## 4. Overall transition rate vs one-and-done rate

**Denominator.** Auditable finding-count in the MASTER ledger as of 2026-04-14: approximately 57 findings with *inferential acceptance criteria*, excluding the 90-claim audit §3b (49 CONFIRMED + 18 PARTIAL + 18 CONTRADICTED are mechanical exact-count lookups, locked on contact), the §2 corpus anchors (locked numerical constants), and the §5b derived equations (definitional, not tested).

**Numerator.** 17 transition events (Categories A-I, excluding the "no transition" rows #14, #15, #17, #18 in the table in §1 and the two H-NEW-1 lineage events counted once jointly for this rate calculation, which yields 16 events). For strict accounting:

- **17 discrete transition events** (H-NEW-1 counted twice because it underwent two structurally distinct transitions: E then D).
- **16 findings with at least one transition** (H-NEW-1 counted once).

**Rates:**

- **Transition rate (event-weighted):** 17 / ~57 ≈ **30%**.
- **Transition rate (finding-weighted):** 16 / ~57 ≈ **28%**.
- **One-and-done rate:** ~70% (finding lands, verdict matches pre-registered criterion, no subsequent revision).

The event-weighted figure is the more informative number because it captures re-transitions; the finding-weighted figure is the more conservative number for comparison with programs that report replication rates.

**Category-weighted diagnostic.** Of the 17 events, 13 (76%) are Categories A-C (reverse-relabel, mechanism-split, methodology-supersession — all verdict-preserving or verdict-nuancing). Only 1 event (Category F, [[h-new-34-1-under-dispersion|H-NEW-34.1]]) is an outright pre-reg-gated flip. So the "flip rate" is ≈ 1/57 ≈ **1.8%** — a figure that is not directly comparable to replication rates but establishes that wholesale verdict reversals are rare in this project's current operating regime.

## 5. Comparative baselines from published pre-registration programs

The 28-30% transition rate above cannot be directly compared to any single published figure because it mixes reverse-relabels, mechanism-splits, methodology-supersessions, and outright refutations in a way most published studies do not. But three published anchors establish the order-of-magnitude landscape:

**(i) Open Science Collaboration (2015), psychology replication project.** *Science* 349, 6251. 100 psychology experiments re-run with pre-registered protocols; 36% replicated at p < 0.05 in the direction of the original effect; 47% replicated with 95% CI overlapping the original point estimate. This is a **replication rate**, not a transition rate — it measures how often a new dataset's verdict matches the old dataset's verdict using the old methodology, not how often the same dataset's verdict revises under new audit. The analogy to this project is the 1-event Category E (spurious-downgrade-reverted): 1/57 ≈ 1.8% rate of an earlier audit being overturned by a subsequent audit. The comparison is noisy but the direction is that this project's rate of overturned earlier audits is much lower than the OSC project's rate of non-replication. The honest reason is scale: N=1 Category E event is too few to estimate a rate stably.

**(ii) Camerer et al. (2016), economics lab experiments replication.** *Science* 351, 6280. 18 experimental economics studies re-run; 11 of 18 (61%) replicated at p < 0.05 in the original direction; average effect size ~66% of original. The higher replication rate vs OSC reflects tighter field conventions: economics lab experiments already sit in a pre-registered single-methodology tradition. The analogy to this project is weak — the Camerer figures are replication rates at a field level, not self-revision rates within a single project. They establish only the point that a pre-reg-disciplined field can sit above 50% replication.

**(iii) Kaplan & Irvin (2015), NIH-funded cardiovascular prevention trials before and after the 2000 ClinicalTrials.gov pre-registration mandate.** *PLOS ONE* 10(8), e0132382. Rate of trials reporting a "positive effect" on the pre-registered primary endpoint dropped from **57% (pre-2000)** to **8% (post-2000)**. This is the most informative anchor for the present audit because it measures what happens to a field's verdict distribution when pre-registration discipline is imposed. The 49-point drop is not a measure of instrument failure; it is a measure of how much of the pre-mandate 57% was driven by post-hoc endpoint-switching, outcome-switching, and garden-of-forking-paths selection. Under pre-registration, "flipping" to NULL becomes the honest default for trials that would previously have found a way to report something positive.

**What the comparison establishes for this audit.** The 28-30% transition rate in this project is high relative to OSC's replication-direction figure if interpreted as a "how often does this project revise itself" metric, but low relative to the NHLBI 49-point drop if interpreted as "what fraction of this project's findings would be different under stricter pre-registration." Both comparisons are order-of-magnitude at best because the underlying revision-definitions are not commensurable. The honest claim the audit can make is: **the project's transition rate sits in a regime consistent with an actively-audited research program running under honest pre-registration discipline, with most transitions (76%) being verdict-preserving nuances rather than verdict-flipping failures.** It is neither the ~5% "clean first-pass" regime of under-audited programs nor the ~50% "most findings fail" regime of full-replication projects.

**Caveats on the comparison.** (a) Revision rate is not replication rate — the denominators and numerators measure different things. (b) Single-project transition rates are unstable at N=17 events. (c) The project's transition rate may drop over time as the instruments mature and the protocol set (PRE-REG-STANDARDs 01-07, MW-1 through MW-8) absorbs more of what the early-phase audits caught. (d) Transition events on currently-STAGED findings (H-NEW-1, [[h-new-34-1-under-dispersion|H-NEW-34.1]], AUDIT-032) have not yet resolved and are therefore not in the 17-count numerator by design — on resolution they may add to the numerator. A follow-up pass after H-NEW-META-3 and C1/C2 land would refine the rate.

## 6. Currently mid-transition watchlist

As of 2026-04-14, three findings are in a mid-transition state where their disposition is not yet final. Downstream users of the ledger should weight these appropriately until resolution:

| Finding | Current state | Gating event | Pre-locked destination on gate outcome |
|---|---|---|---|
| **H-NEW-1** (+ sibling H-NEW-1-v2) | §3d PENDING-RETEST under Category D | H-NEW-META-3 (Task #118, in-progress, pilot pre-confirmed META-NULL-REINFORCED) | (a) calibrated null identified + signal survives → §3c with corrected z; (b) calibrated null identified + signal fails → §4 with reverse-from-§3c trail; (c) META-NULL-REINFORCED → remain in §3d permanently or downgrade to descriptive-pattern-only per pre-locked revert-condition |
| **[[h-new-34-1-under-dispersion|H-NEW-34.1]]** | §3d STAGED under Category F | skeptical-auditor C1/C2 ruling (Muʿallaqāt stratified power-insufficient; χ² brittleness on small per-decile N) | (a) auditor ACCEPT stratified → §4 REFUTATIONS with MECHANISM-INCONSISTENT label; (b) auditor REJECT stratified as C2 artefact → escalation to classical-scholar, possible parent H-NEW-34 reopening |
| **T1 (LLM-judge inauthenticity)** | NOT EXECUTED, cell held OPEN under Category I | Task #138 distributed / batch-mode LLM-judge architecture availability | (a) execution succeeds → T1 cell fills with pre-registered verdict; (b) architecture unavailable indefinitely → T1 cell remains OPEN, Bonferroni k=5 stays intact, T1-aux remains informational-only footnote |

**Additional near-mid-transition items not listed in the table** because their gating is methodological rather than empirical: the MW-6 moderator protocol-level inversion (Category H) is in a "reframed" state with its load-bearing function preserved; the Category H event itself is closed (the reframe is done), but standing PRE-REG-STANDARD-07 now governs downstream citations and its as-filed language is under team-lead review for a possible AMEND entry per the 2026-04-14 forward-correction ruling.

## 7. Sensitivity and limits

**Sensitivity 1 — denominator choice.** If the denominator is restricted to H-NEW-* and H-CLASSIC-* findings only (excluding Tomorrow Tests T1-T5 and meta-analyst-level transitions), the transition rate drops to ~11/50 ≈ 22%. If the denominator is expanded to include the 90-claim audit (+ 49 CONFIRMED + 18 PARTIAL + 18 CONTRADICTED + 5 UNDERDETERMINED = 90 locked-on-contact findings as non-transitions), the rate drops to ~17/147 ≈ 12%. The headline 28-30% figure uses the auditable-inferential denominator; sensitivity analyses across the other two denominator choices preserve the direction (transition rate is non-trivial, not dominant).

**Sensitivity 2 — counting repeated transitions.** If H-NEW-1's two separate transitions (E then D) are counted as one, the event total is 16 instead of 17. Rates adjust by < 2 percentage points.

**Sensitivity 3 — pending transitions.** If the three mid-transition findings in §6 are pre-assumed to resolve to their current-state destination and added to the numerator, the rate rises from 17/57 to 20/57 ≈ 35%. This is an upper bound only — the actual resolution could take any of the pre-locked paths.

**Sensitivity 4 — inclusion of protocol-level transitions.** MW-6 (Category H) is listed in the 17-event count but differs structurally from finding-level transitions. Excluding it, the count is 16/57 ≈ 28%. Including other protocol-level events (MW-1 origin, MW-2 formalization, MW-5 promotion, MW-7 3-instance promotion, STANDARD-04 through STANDARD-07 adoptions) would roughly double the event count and shift the denominator to a mixed finding + protocol basis; this is mentioned as a sensitivity note but not carried as the primary count because the comparator denominators (OSC, Camerer, Kaplan-Irvin) are finding-level.

**Limit 1 — observer effect on the auditor.** This audit is written by the same meta-analyst lane that executed 7 of the prior 8 deliverables (#121-136). Self-audit of a program's transition discipline is structurally at risk of understating events the auditor themselves was not involved in surfacing. The cleanest independent check would be a future external skeptical-audit pass on this file alongside all prior 17 events; until then, this audit should be read as a first-pass enumeration, not a final arbitration.

**Limit 2 — ambiguity at the category boundary.** Some events sit between two categories. H-NEW-20 (MW-1-GATE-A length residualization) is classified Category C (methodology-upgrade-supersession) but could be classified Category A (reverse-direction-relabel on the strict-reading Z=+9.57 being 0.43 below the pre-reg threshold). The classification choice was made on the grounds that the finding's direction is preserved and only its magnitude is tempered; a reader who weights the strict-reading FAIL more heavily would classify it as Category A and the Category A count would rise to 6. This is the kind of edge case that future passes may resolve.

**Limit 3 — time depth is short.** The project is ~4 weeks deep as of 2026-04-14. A transition rate computed over 4 weeks may differ from a transition rate over 4 months or 4 years. Long-running pre-registration programs (e.g., OSC, Camerer, Kaplan-Irvin) have the luxury of years of follow-up; this audit's 28-30% is a snapshot at a particular maturity stage.

**Limit 4 — Category I is N=1.** The AUDIT-032 case study is a single instance and the corresponding Category I rate (1/57 ≈ 1.8%) is not a stable rate estimate. The category exists in the taxonomy because the epistemic structure of the event is distinct, not because the rate is measurable.

## 8. What this audit does NOT claim

Four things this audit explicitly does not say, listed because external readers tend to project them onto data of this shape:

1. **It does not claim the 28-30% transition rate is "good" or "bad."** It claims the rate is in a regime consistent with honest pre-registration discipline under active second-pass audit, as anchored against three published reference programs, with the caveat that the three programs measure different things.

2. **It does not claim the 76% verdict-preserving ratio means the project's instruments are mature.** It claims that most transition events in the current snapshot preserve the finding's overall direction, which is a necessary but not sufficient condition for instrument maturity. An immature program would show this ratio flipping as more findings go through the mechanism-split gauntlet.

3. **It does not claim Category I is uniquely diagnostic of project-wide filing-discipline problems.** It claims that the single Category I event (T1 audit-032) is epistemically distinct from the other categories and deserves its own slot in the taxonomy. Whether the project will accumulate more Category I events is a question for future passes.

4. **It does not claim the currently-STAGED findings (H-NEW-1, [[h-new-34-1-under-dispersion|H-NEW-34.1]], T1) will resolve to any particular destination.** It lists their pre-locked destinations under each gating outcome; the audit commits only to tracking them, not to predicting their fate.

## 9. Sources and provenance

| Section | Primary source |
|---|---|
| §1 transition table | MASTER-FINDINGS-LEDGER.md §3b/§3c/§3d/§4 (primary entries); individual finding files in `findings/phase-b-hypotheses/*.md` (lineage detail); `findings/team-audits/audit-001..031` (audit drivers); audit-032 filing in progress (Task #137) |
| §2 taxonomy | derived from §1 event inventory |
| §3 category commentary | cross-referenced against audit-022 (H-NEW-29 anti-HARK closure), audit-024 ([[h-new-24-b1-b2-orthogonalization|H-NEW-24]]-B1/B2), audit-025 (H-NEW-34 anti-HARK) for the anti-HARK discipline pattern |
| §5 baseline comparisons | Open Science Collaboration, *Science* 349 (2015); Camerer et al., *Science* 351 (2016); Kaplan & Irvin, *PLOS ONE* 10(8) (2015) |
| §6 watchlist | `findings/phase-b-hypotheses/h-new-1-verse-ending-markov-residual.md` (H-NEW-1 trajectory); `findings/phase-b-hypotheses/h-new-34-1-under-dispersion.md` ([[h-new-34-1-under-dispersion|H-NEW-34.1]]); `findings/phase-b-hypotheses/llm-judge-inauthenticity.md` (T1 audit-032 correction) |

**Standing reference set, post-this-audit:** effect-size inventory (#121), pending power analysis (#122), p-curve diagnostic (#124), scholar convergence tracker (#126), classical-modern reliability ratio (#127), MW-6 moderator (#129), Option A retrain (#132), honest-distribution scorecard (#136), **verdict-transition audit (#142, this file).**

## 10. Versioning

This document is the first version of the verdict-transition audit. Three events would trigger an update:

- **H-NEW-META-3 verdict lands** — would resolve H-NEW-1 + H-NEW-1-v2 mid-transition state (add 1-2 Category D resolutions to the numerator, potentially 1 new Category C or Category F event).
- **Skeptical-auditor C1/C2 ruling on [[h-new-34-1-under-dispersion|H-NEW-34.1]] stratification** — would resolve the Category F event to its §4 destination or escalate to re-opened parent H-NEW-34.
- **Task #138 distributed-compute T1 execution** — would resolve the Category I event by filling the held-OPEN cell with the pre-registered verdict, or by confirming the cell stays OPEN indefinitely.

A fourth trigger — Wave 1-3 (#42, #95, H-CLASSIC-44..49 family) lands with ≥2 more transition events — would not change the taxonomy but would roughly stabilize the rate estimates against the N=17 small-number variability.

Cite as: *meta-analyst, "Verdict-transition audit," 2026-04-14, Quran computational-analysis project (task #142).*
