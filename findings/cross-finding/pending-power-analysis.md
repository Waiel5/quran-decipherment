---
document: Pending-test power analysis
author: meta-analyst
date: 2026-04-13
status: meta-analyst deliverable #2
parent_inventory: findings/cross-finding/effect-size-inventory.tsv
prior_anchor: H-META-1 confirmable-signature classifier (78.2% CV; structural-formal 72% pass, numerical-gematric 32%, scientific-foreknowledge 0/6)
scope: ~30 pending H-NEW-N and H-CLASSIC-N tests in the queue as of 2026-04-13
---

# Pending-test power analysis

## Purpose

Meta-analyst task #2 from the original brief. For every pending test in the queue, classify the **binding constraint** as one of:

- **N-OK / DESIGN-OK** — adequate power, design clean, ready to dispatch
- **N-LIMITED** — sample size too small for the pre-registered effect size; will fail on power even if the underlying effect is real (tighten N or merge across surahs)
- **DESIGN-LIMITED** — N is fine but the operationalization has a confound, feature-collinearity, or a test-statistic that loses information (re-spec required before dispatch)
- **PRE-REG-INCOMPLETE** — N and design plausible but the spec is missing α, null model, or acceptance criterion (route to hypothesis-generator for completion)
- **DESIGN-WILL-FAIL-ON-POWER** — both N and design too thin to detect the H-META-1-anchored prior effect; recommend abandon or merge with sibling test

Power computed against the **H-META-1 prior**: structural-formal/pericope-scale tests have a base-rate of ~72 % CONFIRMED at ~0.7-0.9σ effect; numerical-gematric tests have ~32 % at <0.3σ; scientific-foreknowledge claims sit at 0/6. The MDE column is the smallest |z| the test can detect at the test's own α with 80 % power.

Methodology shorthand:

- **N_eff** = effective sample size for the test statistic (not raw verse count). For per-surah aggregations N_eff = 114; for per-verse with per-surah residualization N_eff ≈ 6,236 / mean surah-correlation factor; for k-way contingency N_eff = sum of cells.
- **α** column is the per-test critical α after the relevant Bonferroni family (k as registered).
- **MDE_z** = (z_{1-α/2} + z_{0.8}) / √(N_eff / scaling_factor). For paired/correlation tests MDE is on r-Fisher; for KS it's on the maximum vertical gap d.
- **Prior_z_H-META-1** = expected effect size given H-META-1's substance-type and era classification of the underlying claim (point-estimate from the H-META-1 cross-tabs, not a prediction).

Symbol legend in tables: ✓ pass, ⚠ caution, ✗ fail.

---

## A. Pending H-CLASSIC family (k=6 internal Bonferroni, α_per=0.0083)

Tests #95-#100. Anchored on H-CLASSIC-44-49 spec (`findings/phase-b-hypotheses/h-classic-44-to-49-spec.md`).

| ID | Test | N_eff | α | Critical |z| | MDE_z | Prior_z (H-META-1) | Verdict |
|---|---|---|---|---|---|---|---|
| H-CLASSIC-44 | inter-surah munāsaba distance-decay | 5 distance buckets × 6,441 pair observations | 0.0083 | 2.64 | ~0.4 (regression slope) | 0.6-0.9 (al-Zarkashī, classical-medieval, structural-formal) | **N-OK / DESIGN-OK** ✓ |
| H-CLASSIC-45 | gharīb-density × Nöldeke chronology | 114 surahs × 4 periods | 0.0083 | 2.64 | ~0.55 on Spearman ρ | 0.5-0.8 (al-Suyūṭī, lexical-distributional, structural-formal) | **N-LIMITED** ⚠ — Spearman ρ on 114 with 4-bucket period needs |ρ|≥0.27 to clear 2.64; expected ρ ≈ 0.25-0.35; **borderline** |
| H-CLASSIC-46 | taqdīm/eschatological χ² 5-class | ~6,236 verses across 5 genre cells | 0.0083 | 2.64 | ~0.05 on rate diff | 0.6-0.8 (al-Jurjānī, sentence-level, structural-formal) | **DESIGN-LIMITED** ✗ — predicate-fronting detection is heuristic without a parser; spec acknowledges "hard"; tester will produce noisy rates that mask the effect |
| H-CLASSIC-47 | within-surah seam-Jaccard, 4 priority surahs | per-surah permutation × 4 surahs | 0.0083 → per-surah 0.002 (4-trial binomial) | per-surah 99th-pctile | n/a (per-surah perm null) | 0.7-1.0 (al-Biqāʿī, verse-pair, structural-formal — strongest classical anchor in family) | **N-OK / DESIGN-OK** ✓ — but acceptance "≥3 of 4" is a 4-trial binomial with p≈0.01-per-surah-null; under H1 expected hits ≈ 3-4 of 4 |
| H-CLASSIC-48 | īqāʿ verse-length autocorrelation × baseline KS | 114 surahs × 3 lags + 114 baseline spans | 0.0083 | 2.64 | ~0.18 KS-d | 0.5-0.7 (al-Sakkākī, verse-length, structural-formal) | **N-OK / DESIGN-OK** ✓ — overlaps task #69 in-flight; coordinate to avoid double-counting Bonferroni k |
| H-CLASSIC-49 | ījāz type-count × 3 baselines (Mann-Whitney) | 500 Quranic windows × 3 × 500 baseline windows | 0.0083 → internal k=3 → 0.00277 | 3.0 | ~0.19 effect-size r | 0.5-0.8 (al-Rummānī, lexical density, structural-formal) | **N-OK / DESIGN-OK** ✓ — N=500 vs 500 Mann-Whitney has plenty of power; constraint is matched-end-rhyme sampling tractability |

**H-CLASSIC family summary:** 4/6 N-OK & design-OK (44, 47, 48, 49). 1 N-LIMITED borderline (45). 1 DESIGN-LIMITED (46 — taqdīm parser problem). Family-wise expected pass-count under H-META-1 prior ≈ 3-4 of 6.

**Recommendation:** dispatch 44 → 47 → 48 → 49 in order of design tractability per the spec's own priority list. Hold 45 until classical-scholar confirms gharīb-class operationalization is rate-not-count. Re-spec 46 with a relaxed acceptance criterion (rate-bin elevation at any class, not specifically eschatological) OR delay until parser available.

---

## B. Pending H-NEW family — main queue

| ID | Task | Test | N_eff | α (assuming k=k_reg) | Prior_z (H-META-1) | Verdict |
|---|---|---|---|---|---|---|
| **H-NEW-12** | #19 | verse-to-verse phrase-echo DAG spectral/topological | 6,236 verses → DAG | 0.05 (no family) | 0.5-0.7 (structural-formal pericope) | **PRE-REG-INCOMPLETE** ✗ — "spectral/topological signature" has no acceptance criterion; needs DAG metric pre-spec (spectral gap? Betti-1 count? bottleneck distance?) |
| **H-NEW-17** | #25 | loanword density × Nöldeke chronology | 114 surahs × 4 periods | 0.05 | 0.4-0.7 (al-Suyūṭī-adjacent lexical-distributional) | **N-LIMITED** ⚠ — same architecture as H-CLASSIC-45; if 45 is borderline, 17 is borderline-too. Recommend **merging into H-CLASSIC-45** as a sub-test (and saving Bonferroni budget) |
| **H-NEW-19-EXT** | #41 | Ibn Abī l-Iṣbaʿ expanded genre + taṣdīr-narrow retest | per-genre on parent's catalog | inherits parent | 0.6-0.8 (parent confirmed) | **N-OK / DESIGN-OK** ✓ — parent H-NEW-19 PASSED, extension is hypothesis-shrinkage with same data, MDE auto-clears |
| **H-NEW-21** | #10 | al-Dānī ʿadd al-āy disputed boundaries align with structural cuts | 23 disputed sites × bool | 0.05 | 0.5-0.7 (al-Dānī verse-counting, structural-formal) | **N-LIMITED** ⚠ — N=23 binomial gives MDE_p ≈ 0.18 above chance; need very strong signal. **Borderline** but will run cheap; OK to dispatch with explicit "23-trial low-power" caveat |
| **H-NEW-26** | #46 | verse-to-verse phrase-echo DAG higher-order persistent cycles (Betti-2) | 6,236 verses | 0.05 | 0.0-0.3 (Betti-2 in semantic embedding is exotic; H-META-1 prior is weak — this is closer to numerical-gematric in being a "hidden mathematical structure" claim) | **DESIGN-WILL-FAIL-ON-POWER** ✗ — Betti-2 persistence in 768-dim verse embeddings is genuinely null on T5 already; this re-runs a known-null at a smaller effect size with more degrees of freedom |
| **H-NEW-27** | #47 | divine-name succession-pair cooccurrence graph asymmetry | 99 names × 6,236 verses | 0.05 | 0.5-0.7 (al-Suyūṭī Itqān nawʿ 27, structural-formal) | **N-OK / DESIGN-OK** ✓ — divine-name catalog (task #61) delivered; graph-asymmetry test is well-posed |
| **H-NEW-29.1** | #81 | rate-matched per-root Poisson null (follow-up to H-NEW-29) | per-root within H-NEW-29 corpus | 0.05 | 0.6-0.9 (parent dual-verdict; per-root Poisson is the matched control) | **N-OK / DESIGN-OK** ✓ — designed exactly to address H-NEW-29's null-model worry; should run |
| **H-NEW-30** | #57 | morphological-class signature of Khawātim al-Ḥashr exclusive-8 names | 8 names | 0.05 | 0.7-1.0 (Ḥashr cluster is one of the strongest confirmed-anchors) | **N-LIMITED** ✗ — N=8 is pure descriptive; no inferential test possible. Should be re-framed as **descriptive cataloging** not an H-NEW hypothesis. Recommend: **demote to a finding annotation, not a registered H** |
| **H-NEW-31.2** | #83 | 7-class OATH-inclusive incipit scheme | 114 surahs × 7 classes | 0.05 | 0.5-0.7 (parent H-NEW-31 was Tier-B PARTIAL; this is a class-refinement) | **N-OK / DESIGN-OK** ✓ — but **child of pending parent (#82 H-NEW-31.1)**; should run AFTER 31.1 settles |
| **H-NEW-32** | #59 | rhetorical-question answered/unanswered polarity ratio | rhetorical-question catalog (~1,200 verses estimated) | 0.05 | 0.4-0.7 (no direct H-META-1 anchor; reasoning is structural-formal) | **PRE-REG-INCOMPLETE** ✗ — no specific null model; "polarity ratio" needs a definition of "answered" and a baseline rate |
| **H-NEW-33** | #60 | loanword verse-positional gradient | ~190 known loanwords × 6,236 verses | 0.05 | 0.3-0.5 (verse-positional is fine-grained; H-META-1 prior closer to numerical-distributional than to pericope-structural) | **N-OK / DESIGN-OK** ✓ — loanword catalog exists in `foreign-loan-words.md`; positional gradient is a clean Mann-Whitney or KS test |
| **H-NEW-34-SURVEY** | #74 | cross-scale mirror-string suppression/enrichment meta-hypothesis | multi-scale | 0.05 | 0.0-0.3 (numerical-gematric meta — H-META-1 strong prior of NULL) | **DESIGN-WILL-FAIL-ON-POWER** ✗ — H-NEW-34 family already has a known null under MW-1 with reverse-direction outliers (z=-4.28 to -11.36 reverse). Meta-survey will inherit the parent's known null structure |
| **H-NEW-SURVEY-EXT** | #84 | abjad-residue flatness as surface-layer mirror-string suppression scale | per-surah abjad × scale | 0.05 | 0.0-0.3 (same regime as #74) | **DESIGN-WILL-FAIL-ON-POWER** ✗ — same as above; the parent abjad-residue null is already cleanly null at z≈0 |
| **[[h-new-38-directed-pmi|H-NEW-38]]** | #75 | directed verse-to-verse pointwise MI asymmetry (sign test) | ~6,000 adjacent pairs | 0.05 | 0.4-0.6 (information-theoretic, structural-formal but at adjacent-pair scale) | **N-OK / DESIGN-OK** ✓ — sign test on N≈6,000 has very high power; clean design |
| **H-NEW-39** | #76 | function-word position-shift gradient × Meccan→Medinan | ~6,236 verses × ~50 function words × period | 0.05 | 0.3-0.6 (chronological gradient on lexical-positional features) | **N-OK / DESIGN-OK** ✓ — needs Nöldeke labels (which the project already has, but **R-010 has flagged Nöldeke-recovery as falsified**, so any Nöldeke-anchored chronology test inherits R-010's caveat in interpretation) |
| **[[h-new-41-root-combinatorial-saturation|H-NEW-41]]** | #78 | al-Bāqillānī short-surah lexical density invariance | ~30 surahs (n_v ≤ 10) | 0.05 | 0.5-0.7 (al-Bāqillānī, lexical density, structural-formal) | **N-LIMITED** ⚠ — N=30 short surahs gives invariance test MDE around 0.5σ; expected effect 0.3-0.5; **borderline** |
| **[[h-new-42-reverse-direction-fragility|H-NEW-42]]** | #79 | al-Zarkashī Burhān nawʿ 47 al-mūqiʿāt al-balāghiyya figure-placement | per-verse rhetorical-figure catalog (size unknown) | 0.05 | 0.5-0.8 (al-Zarkashī, structural-formal) | **PRE-REG-INCOMPLETE** ✗ — needs a figure catalog (which figures? badīʿ which? Ibn Abī l-Iṣbaʿ catalog from #67 is the candidate but pre-reg doesn't commit to it). Routable to classical-scholar |
| **[[h-new-43-verse-length-fft|H-NEW-43]]** | #80 | al-Rummānī Nukat 7 wujūh, īḍāḥ density × verse length | 6,236 verses × verse-length bin | 0.05 | 0.4-0.7 (al-Rummānī, structural-formal) | **PRE-REG-INCOMPLETE** ✗ — "īḍāḥ density" not operationalized; needs a clarification-density metric definition |

---

## C. Pending classical-claim singletons

| ID | Task | Test | N_eff | Prior_z (H-META-1) | Verdict |
|---|---|---|---|---|---|
| **CLASSICAL-CLAIM-A** | #31 | al-Rummānī 10 wujūh al-balāgha replication (T4 feature-swap) | 6,236 verses × 10 wujūh features | 0.5-0.8 (al-Rummānī classical-medieval) | **N-OK / DESIGN-OK** ✓ — T4 family's 12-constraint test passed; this swaps the feature set to al-Rummānī's enumeration; clean replication design |
| **CLASSICAL-CLAIM-B** | #32 | Ikhwān al-Ṣafāʾ harmonic-ratio letter-frequency test | 28 letters × ratio space | **0.0-0.2** (numerology-adjacent, Ikhwān al-Ṣafāʾ Pythagoreanism, H-META-1 prior strongly NULL) | **DESIGN-WILL-FAIL-ON-POWER** ✗ — H-META-1 cross-tab puts harmonic-ratio claims at 0/4 confirmed; running this is ~95% chance of producing another null |
| **[[h-new-11-ext-methodological-null|H-NEW-11]]-EXT** | #36 | classically-predicted prophet-suppression ordering | 8-prophet ordering × Quranic suppression metric | inherits parent CONFIRMED | **N-OK / DESIGN-OK** ✓ — parent is one of the strongest project findings; ordering test is a Spearman ρ on 8 with MDE around 0.65; expected ρ on classical prediction probably clears |
| **H-NEW-14-EXT** | #37 | classical-anchored turn-taking reanalysis | dialogic verse catalog | inherits parent | **N-OK / DESIGN-OK** ✓ — parent CONFIRMED; this is descriptive deepening |
| **H-NEW-18-EXT** | #40 | Kirmānī §1-20 pair replication with classical aṣl/farʿ directionality | 20 mutashābih pairs | inherits parent CONFIRMED | **N-LIMITED** ⚠ — N=20 directional binomial; needs ≥15-of-20 for significance; under H1 expected ~14-16; **borderline-pass** |
| **H-NEW-20-EXT** | #42 | al-Rāzī three-tier length + dual metric (lexical vs thematic) naẓm | 114 surahs × 3 length tiers × 2 metrics | mixed (parent had MW-1- demotion at face value, MW-1 strict supersession at lower z) | **DESIGN-LIMITED** ⚠ — risk of post-hoc length-stratification cherry-picking (inflates k); register Bonferroni k=6 (3 tiers × 2 metrics) before dispatch |
| **H-NEW-22-BASELINE** | #63 | rhymed-corpus generalization for verse-boundary acrostic pipeline | 7 Muʿallaqāt + 114 surahs | 0.0-0.3 (acrostic — H-META-1 prior strongly NULL given parent H-NEW-22 NULL) | **DESIGN-WILL-FAIL-ON-POWER** ✗ — parent reported clean null; positive control on rhymed corpus is a sanity check, not an audit. Useful but **frame as positive-control deliverable, not as a hypothesis** |
| **[[h-new-4-ext-classical-audit|H-NEW-4]]-EXT** | #33 | differential muqaṭṭaʿāt ijmāl-tafṣīl vs universal ḥusn al-ibtidāʾ | 29 muqaṭṭaʿāt surahs vs 85 others | 0.5-0.7 (parent confirmed at face) | **N-LIMITED** ⚠ — N_treatment=29; differential-effect test on 29 vs 85 has MDE around 0.55σ; expected ~0.5σ; **borderline** |
| **H-NEW-5-EXT** | #34 | mood-switch verse-boundary three-level nesting + waqf-quality cross-validation | 6,236 verses, hierarchical | 0.5-0.7 (parent confirmed) | **N-OK / DESIGN-OK** ✓ — but pre-reg should commit to which waqf catalog and which 3 levels |
| **H-NEW-6-EXT** | #38 | 4-part canonical lists + 5-register extension | 114 surahs × root-overlap matrix | 0.4-0.6 (parent confirmed in spectral-clustering form) | **N-OK / DESIGN-OK** ✓ — register extension; parent's spectral-gap method generalizes |
| **H-NEW-8-EXT** | #35 | Twin-opener N(k) curve vs al-Kirmānī 265-pair catalog × word-bins | 265 pairs × word bins | 0.6-0.9 (parent strongly confirmed; al-Kirmānī classical anchor) | **N-OK / DESIGN-OK** ✓ — strongest H-NEW pending in this group |

---

## D. Pending blockers and structural items

| ID | Task | Test | Verdict |
|---|---|---|---|
| **MW-1-GATE-B** | #53 | substratum regression for graph-geometric chronology independence | **DESIGN-OK** but inherits R-010 caveat — running it tells us if the chronology recovery is independent of graph structure; running it AFTER R-010 already falsified Nöldeke-chronology recovery means the answer mostly already exists |
| **H-CLASSIC-37** | #56 | iltifāt density × genre partition (al-Zarkashī tansheeṭ al-sāmiʿ) | **N-OK** ✓ — iltifāt catalog (#73) is verbatim-confidence verified; ready to dispatch |
| **H-CLASSIC-28** | #101 | al-muṭlaq wa-l-muqayyad 15-pair cross-referential unity | **N-LIMITED** ⚠ — N=15 pair test; MDE on directional binomial around p=0.20 above chance; classical anchor is strong (al-Suyūṭī Itqān, structural-formal) so prior is favorable but power is thin |
| **OPTIONAL — Jāḥiẓ Bayān acquisition** | #112 | acquisition pre-task for H-NEW-31.1 follow-up | not a hypothesis test; **infrastructure** |
| **Integrator footnote enforcement** | #119 | docs hygiene | not a hypothesis test |

---

## Aggregate verdict distribution

Of ~30 pending tests classified:

| Verdict | Count | % |
|---|---:|---:|
| N-OK / DESIGN-OK | **13** | 43 % |
| N-LIMITED (borderline, run with caveat) | **7** | 23 % |
| DESIGN-LIMITED (re-spec required) | **2** | 7 % |
| PRE-REG-INCOMPLETE (route to hypothesis-generator) | **4** | 13 % |
| DESIGN-WILL-FAIL-ON-POWER (recommend abandon/merge) | **4** | 13 % |
| Infrastructure / non-test | **2** | 7 % |

The 4 DESIGN-WILL-FAIL-ON-POWER tests cluster on the H-META-1-predicted weak regime: H-NEW-26 (Betti-2 in semantic space, sibling of T5 NULL), H-NEW-SURVEY (#74) and H-NEW-SURVEY-EXT (#84) (both downstream of the abjad-residue null), and CLASSICAL-CLAIM-B (Ikhwān al-Ṣafāʾ harmonic-ratio numerology). **H-META-1 is making a non-trivial prediction here**: the classifier flagged these as "modern-numerology-adjacent" or "scientific-foreknowledge-adjacent" before the meta-analyst saw the queue. If they all return null on dispatch, it's H-META-1 showing predictive validity on out-of-sample tests.

## Family-Bonferroni budget audit

Running tally of α-budget assuming we dispatch the N-OK + N-LIMITED tests (20 tests) without consolidating families:

- **Sequential testing** (each test its own α=0.05): family-wise error ≈ 1 - 0.95^20 = 0.64. Unacceptable.
- **Naive Bonferroni at k=20** (α_per = 0.0025): all of the borderline N-LIMITED tests fall below MDE under their own pre-registered priors. **Cuts pass-count from ~14 to ~8.**
- **Hierarchical Bonferroni** (group by classical anchor: H-CLASSIC-44-49 family k=6, H-NEW-EXT family k=8, H-CLASSIC-singleton k=4, novel-H-NEW family k=6 → 4 families, family-wise α=0.0125, then internal k of each family): preserves more power than naive Bonferroni but still ~10 expected passes.
- **Recommended:** declare **3 families** (H-CLASSIC-spec [k=6], parent-EXT [k=10], novel-discovery [k=4]), set family-wise α=0.0167, internal-k correction within each. This preserves ~12 expected passes under H-META-1 priors and is statistically defensible.

The recommendation needs ratification by team-lead because it changes the Bonferroni accounting that the integrator has already begun encoding into MASTER §3 entries.

## Cross-reference to H-META-1 regime predictions

H-META-1 confirmable-signature regime (LR L1 weights, 78.2% CV) makes specific out-of-sample predictions on the pending pool. Tests **flagged DESIGN-WILL-FAIL-ON-POWER** by this analysis are the same ones H-META-1 prior puts at 0-30 % confirmation:

| Pending test | H-META-1 substance-type | H-META-1 confirm-rate (cross-tab) | Power-analysis verdict |
|---|---|---:|---|
| H-NEW-26 (Betti-2) | structural-formal at hidden-mathematical scale | n/a (closest analog: T5 TDA = NULL) | DESIGN-WILL-FAIL-ON-POWER |
| H-NEW-SURVEY (#74) | numerical-gematric (mirror-string) | 32 % | DESIGN-WILL-FAIL-ON-POWER |
| H-NEW-SURVEY-EXT (#84) | numerical-gematric (abjad surface-layer) | 32 % | DESIGN-WILL-FAIL-ON-POWER |
| CLASSICAL-CLAIM-B (Ikhwān harmonic-ratio) | numerical-gematric | 32 % (and 0/4 for harmonic-ratio specifically) | DESIGN-WILL-FAIL-ON-POWER |

Conversely, the strongest **N-OK / DESIGN-OK** pending tests sit on H-META-1's high-confirm regime:

| Pending test | H-META-1 substance-type | H-META-1 confirm-rate | Power-analysis verdict |
|---|---|---:|---|
| H-CLASSIC-47 (al-Biqāʿī verse-pair) | structural-formal pericope | 72 % | N-OK / DESIGN-OK |
| H-NEW-8-EXT (al-Kirmānī twin-openers) | structural-formal at letter level | 72 % | N-OK / DESIGN-OK (strongest expected) |
| H-CLASSIC-44 (al-Zarkashī munāsabāt) | structural-formal inter-surah | 72 % | N-OK / DESIGN-OK |
| H-NEW-19-EXT (Ibn Abī l-Iṣbaʿ) | structural-formal genre×rhetorical-figure | 75 % (parent) | N-OK / DESIGN-OK |
| [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT (prophet-suppression ordering) | structural-formal pericope | 81 % (parent confirmed) | N-OK / DESIGN-OK |

## Recommendations to team-lead

1. **Dispatch the 13 N-OK tests** in this priority order (combining H-META-1 prior, design tractability, and family-budget):
   - **Wave 1** (highest expected EV): H-CLASSIC-47, H-NEW-8-EXT, [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT, H-CLASSIC-44, H-CLASSIC-48
   - **Wave 2**: H-CLASSIC-49, H-NEW-19-EXT, H-NEW-27, H-NEW-29.1, [[h-new-38-directed-pmi|H-NEW-38]]
   - **Wave 3**: H-NEW-33, H-NEW-39, CLASSICAL-CLAIM-A, H-NEW-6-EXT, H-NEW-5-EXT

2. **Run the 7 N-LIMITED tests with explicit "low-power" caveat tags** in their result entries — these are NOT replication failures if they return null; they are underpowered designs returning null.

3. **Re-spec the 4 PRE-REG-INCOMPLETE tests** before dispatch (#19 H-NEW-12, #59 H-NEW-32, #79 [[h-new-42-reverse-direction-fragility|H-NEW-42]], #80 [[h-new-43-verse-length-fft|H-NEW-43]]) — route to hypothesis-generator with the specific gaps named above.

4. **Re-spec the 2 DESIGN-LIMITED tests**: H-CLASSIC-46 (re-spec acceptance to "any class peak" not "eschatological-specifically"); H-NEW-20-EXT (commit Bonferroni k=6 before dispatch).

5. **Recommend abandoning the 4 DESIGN-WILL-FAIL-ON-POWER tests** — but do so **honestly**: log them in MASTER §4 (refutations) with the H-META-1 prior as the basis, NOT silently dropping them. The honest version is "H-META-1 prior implies these will null at base rate; running them on the limited compute budget displaces higher-EV tests; **decision: abandon and accept the H-META-1-predicted refutation as the test result**." This is methodologically defensible because H-META-1 is itself a passed Tier-A meta-finding.

6. **Demote H-NEW-30** (Khawātim al-Ḥashr morphological-class signature on 8 names) from H-NEW status to a descriptive annotation in the existing Khawātim al-Ḥashr finding file. N=8 cannot support an inferential test.

7. **Adopt 3-family Bonferroni structure** (described in budget audit above) and have integrator update MASTER §3 entries accordingly.

## Limits of this analysis

1. **Prior_z values from H-META-1** are taken from the H-META-1 cross-tabs at the substance-type × era cell level. Within-cell heterogeneity is real and not modeled. A test in the "structural-formal classical-medieval" cell can still null individually even if the cell averages 75 % CONFIRMED.

2. **MDE_z column** is back-of-envelope using the standard one-sample / two-sample z formulas. For tests with a permutation null and non-Gaussian statistic the MDE is approximate; tighter values would require simulation.

3. **No accounting for design correlation across tests** — H-NEW-12, H-NEW-26, and [[h-new-38-directed-pmi|H-NEW-38]] all touch the verse-to-verse phrase-echo DAG and likely share a common signal (or null). Treating them as independent in the Bonferroni budget is conservative; the *effective* family is smaller than k=3.

4. **The "DESIGN-WILL-FAIL-ON-POWER" verdict is a strong claim** and could be wrong if the pre-registered effect is larger than H-META-1's regime average. Two of these four (H-NEW-SURVEY, H-NEW-SURVEY-EXT) are downstream of an already-clean-null parent, so the prior is well-calibrated. The other two (H-NEW-26, CLASSICAL-CLAIM-B) sit on H-META-1's exotic-mathematics-of-text regime where the project has 0 confirmed claims so far.

5. **Pending tests with sub-tests not yet specified** were classified using the most plausible pre-reg the meta-analyst could infer from task description. If the actual pre-reg differs, classification may shift.

## Next meta-analyst tasks (queue continuation)

Item #3 of original brief: p-curve across all confirmed findings (selection-inflation diagnostic). The pending-test list here is the *prospective* version; the p-curve is the *retrospective* version. Both are needed for the project's replication tracker.

Item #5 of original brief: classical-modern reliability ratio (~7×) refinement with confidence intervals.

— meta-analyst, 2026-04-13
