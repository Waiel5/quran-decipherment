---
audit_id: audit-026
date: 2026-04-13
auditor: skeptical-auditor
finding_under_review: eschatological-slot-cluster-synthesis.md (M-8 CANDIDATE triple-test)
parent_task: #66
finding_date: 2026-04-12 (filed) / 2026-04-13 11:51 (last modified)
author_under_review: classical-scholar
verdict: **NEEDS MAJOR REVISION** — synthesis misrepresents H-NEW-19's actual partition and does not disclose 2/3 sub-test failures; "38× ratio" and "three independent classical tests converging" framings are not supported by the underlying data
lineage_tag: audit-026
related_audits: audit-020 (H-NEW-23 primary, PASSED at z=+10.61); M-8 CANDIDATE leg registration
mw_candidates_touched: MW-6 (positive-control on auditor-specified protocols — now STANDING per this session's team-lead ruling)
meta_patterns_touched: M-8 CANDIDATE (eschatological slot engineering) — promotion evidence weakened by this audit; M-5 STANDING (decomposition pattern — this synthesis attempts to consolidate three decompositions into one umbrella claim)
harking_4test: FAIL on test 1 (non-counting of failed sub-tests) and test 4 (renaming H-NEW-19 from Meccan/Medinan to eschatological)
---

# Audit-026 — eschatological-slot-cluster-synthesis (M-8 triple-test)

**One-line verdict**: The synthesis document reframes three statistical results as "three independent tests converging on eschatological slot engineering", but two of the three "tests" don't hold up on inspection: H-NEW-19 actually used a Meccan/Medinan partition (not eschatological) and reports only 1/3 passing sub-tests undisclosed in the synthesis; the "38× ratio" in test 3 is a post-hoc max-vs-min choice from a 5-way partition. **The primary H-NEW-23 within-verse slot control (z=+10.61) remains stable** — it was audited PASSED in audit-020 and nothing here changes that. What needs revision is the synthesis's triple-test convergence claim, not the underlying H-NEW-23 finding.

## 1. The material discovery

The synthesis claims (§ lines 32-34):
> "Test 2 — H-NEW-19 Ibn Abī l-Iṣbaʿ elision-eschatology... Signal: elision-density is significantly higher in eschatological passages than in legal/narrative/covenantal baselines"

But the H-NEW-19 output file (`scratch/team-discovery/result-elision.json`) and script (`scratch/team-discovery/h_new_19_elision.py`) both show the partition actually used was **"meccan_vs_medinan_v1"** — a binary Meccan vs Medinan proxy. The script's own docstring at line 9 explicitly labels this: *"v1: Binary Meccan/Medinan proxy (Meccan surahs are eschatology-heavy...)"*. The synthesis then drops the v1 scare-quotes and treats the result as if the partition were eschatological-vs-legal-vs-narrative-vs-covenantal.

These are not the same partition. Meccan surahs are **correlated** with eschatological content but include large amounts of narrative (prophet stories), polemic, and hymn material. A Meccan/Medinan split is a corpus-chronology split, not a rhetorical-genre split. The synthesis framing silently upgrades a weaker result (chronology proxy) to a stronger claim (genre-specific).

**The substitution is material because** the M-8 CANDIDATE promotion argument rests on *independent classical sources converging at the same genre partition*. If one of the three "sources" actually tested a different partition, the convergence is not what the synthesis says it is.

## 2. H-NEW-19 undisclosed sub-test failures

The H-NEW-19 result file contains **three sub-tests** (e_a density, e_b density, e_c density) corresponding to three operationalizations of elision density. Only e_a passes:

| sub-test | Meccan mean | Medinan mean | z | p_two_sided | length-strat z | length-strat p | Bonferroni α=0.0167 |
|---|---|---|---|---|---|---|---|
| e_a | 0.4815 | 0.3519 | −4.39 | 1.1e−5 | **+3.13** | **0.0011** | **PASS** |
| e_b | 0.1148 | 0.0930 | −0.75 | 0.455 | −0.30 | 0.681 | FAIL |
| e_c | 0.0142 | 0.0094 | −0.74 | 0.457 | +2.51 | 0.0036 | borderline |

Only e_a passes Bonferroni. e_b is a clean null. e_c is marginal (length-strat p=0.0036 vs α=0.0167 — passes one-tailed but two-tailed p=0.457 fails).

**The synthesis does not disclose that 2 of 3 H-NEW-19 sub-tests are null or marginal.** It claims simply "elision-density is significantly higher in eschatological passages". This is HARKing test 1 (explicit non-counting of failed sub-tests) and HARKing test 4 (renaming a 1/3-pass Meccan-vs-Medinan result as an eschatological-vs-legal finding).

## 3. H-NEW-23 sub2_genre "38× ratio" is a post-hoc max-vs-min pick

The synthesis (§§ lines 37-40) reports:
> "Eschatological verses: hapax-final rate **7.71%**. Legal verses: hapax-final rate **0.20%**. **Ratio: ~38×**"

The underlying data (from h-new-23-hapax-slot.json sub2_genre):

| Genre | n | hapax-final rate |
|---|---|---|
| eschatological | 545 | 7.71% |
| narrative | 4393 | 1.68% |
| polemic | 313 | 0.96% |
| legal | 978 | 0.20% |
| hymn | 7 | 0.00% |

**The 38× ratio compares the MAX to the MIN of a 5-class partition.** A more honest framing is:
- eschatological is ~4.6× narrative (7.71% / 1.68%)
- eschatological is ~8× polemic (7.71% / 0.96%)
- eschatological is ~38× legal (7.71% / 0.20%)

The 38× number singles out legal (the smallest-count class with only 2 hapax-finals out of 978) as the comparator. Legal has n=978 and only 2 hapax finals — this is **power-limited** in the reverse direction (if the true legal rate were 1%, we'd expect ~9 hapax finals; observing 2 is a low-power observation). The 38× framing inflates the effect by picking the noisiest bin.

The **χ² = 113.96 on df=4** is the legitimate overall test and it's decisively significant. The 38× presentation is post-hoc cherry-picking of the strongest pairwise comparison. Publication-grade framing should lead with the χ² and present the rate-by-genre table without privileging the max-vs-min ratio.

## 4. Three-to-one convergence — the underlying claim

The synthesis's central claim (§ lines 87-94) is:
> "A triple-test cluster upgrades this from 'one doctrine confirmed' to 'a convergent cluster confirmed'... The mechanism is positional (al-Zarkashī) AND elisional (Ibn Abī l-Iṣbaʿ). The mechanism is genre-specific (eschatological > legal by 38×). The mechanism is engineered within verses (z = +10.61 on within-verse control)."

Unpacking what's actually independent:

**(a) H-NEW-23 within-verse slot control (z=+10.61)** — PASSED in audit-020. Clean, stable. Measures: hapaxes are placed at the verse-final slot more often than within-verse permutation would predict. Does not by itself identify a genre mechanism — it's a slot-placement mechanism at the verse level.

**(b) H-NEW-23 sub2_genre χ² = 113.96** — also PASSED in audit-020 but with a known caveat (genre partition came from classical-scholar input, which is honest). Measures: hapax-final rate varies across genres. Eschatological is highest.

**(c) H-NEW-19 e_a elision density, Meccan vs Medinan** — PASSED. Measures: elision density is higher in Meccan surahs than Medinan (at length-strat z=+3.13).

The synthesis collapses (b) and (c) into "eschatological > legal" which they aren't:
- (b) compares eschatological to four other RHETORICAL genres
- (c) compares Meccan to Medinan CHRONOLOGICAL corpus

A Meccan/Medinan split is a 86-vs-28-surah corpus split. An eschatological-vs-legal split is a 545-vs-978-verse rhetorical split. They cross-cut. Meccan surahs have plenty of narrative content (which is 1.68% in the eschatological-vs-legal table). The two partitions correlate at the surah level but they're not equivalent at the verse level where H-NEW-23's signal lives.

**The "three independent tests converge on the same genre partition" framing requires (a), (b), (c) to be different operationalizations of the SAME partition.** They aren't. (a) is slot-within-verse with no genre partition at all. (b) is a 5-way rhetorical-genre partition. (c) is a binary chronology partition. The convergence claim overstates the level of agreement.

## 5. What IS supported

I want to be precise about what survives this audit:

- **H-NEW-23 sub3 within-verse slot control at z=+10.61** — PASSED in audit-020, stable, unchanged by this audit. Al-Zarkashī's *maqṣūda li-ghayrihā* mechanism confirmation is intact.
- **H-NEW-23 sub2 genre partition at χ² = 113.96** — PASSED in audit-020. Eschatological genre does show the highest hapax-final rate among 5 rhetorical classes.
- **H-NEW-19 e_a elision density Meccan > Medinan at length-strat z=+3.13** — PASSED as a pre-registered Bonferroni test. Elision density IS higher in Meccan corpus.

What is **not supported** as currently framed:
- H-NEW-19 tested "elision-eschatology" — FALSE (it tested Meccan/Medinan proxy)
- Three independent tests converge on the same genre partition — FALSE (partitions differ)
- 38× ratio as a headline — OVERSTATED (post-hoc max-vs-min from a 5-way partition)
- H-NEW-19 shows elision is concentrated in eschatological passages — NOT TESTED (was tested at Meccan/Medinan, which is a chronology proxy)

## 6. HARKing 4-test

| Test | Question | Result |
|---|---|---|
| 1. Explicit non-counting | Does the synthesis disclose H-NEW-19's 2 failed sub-tests? | **FAIL** — e_b null and e_c marginal are not mentioned. |
| 2. Pre-existing mechanism | Are the classical doctrines (al-Zarkashī, Ibn Abī l-Iṣbaʿ) pre-existing? | **PASS** — both classical sources are genuinely pre-existing and independently specified. |
| 3. Pre-registered directional evidence | Was the eschatological-direction pre-registered in H-NEW-19? | **PARTIAL-FAIL** — H-NEW-19 pre-registered Meccan/Medinan direction and that's what passed. "Eschatological direction" was never tested by H-NEW-19; the synthesis retrofits the eschatological label. |
| 4. Refusal to rename | Does the synthesis rename a Meccan/Medinan result as eschatological? | **FAIL** — the synthesis at lines 32-34 treats H-NEW-19 as testing "eschatological-vs-legal", when the actual JSON shows "meccan_vs_medinan_v1" partition. |

**2/4 FAIL + 1 PARTIAL-FAIL**. This is the first clear HARKing failure in the audit series (audits 022, 024, 025 were all clean passes). Not a catastrophic failure — the individual tests still stand on their own — but the SYNTHESIS framing is inflated.

Importantly, this is a synthesis failure by classical-scholar (the author listed in frontmatter), not a test-execution failure by computational-tester. The original H-NEW-19 and H-NEW-23 results are honest and pre-registered. What happened is at the synthesis step: a post-hoc "three-to-one convergence" narrative was laid over three results that don't actually share a partition.

## 7. Classical-scholar's acknowledgment is partial

To be fair to the author, the synthesis does acknowledge some issues:
- Sub-1 (quartile trend) failure is disclosed (§ lines 100-105)
- Sub-4 (taṣdīr mutual-exclusion) failure is disclosed (§ lines 106-112)
- al-Zarkashī nawʿ number is flagged as "PENDING physical verification" (§ lines 56-57, 135)
- Ibn Abī l-Iṣbaʿ *Badīʿ al-Qurʾān* page reference is flagged as PENDING (§ line 69)

But these are disclosures about the **H-NEW-23 sub-tests and about classical-source pagination**, not about the H-NEW-19 partition substitution or the 38× ratio framing. The disclosures happen at the level the author noticed; they don't extend to the cross-test convergence claim itself.

## 8. MW-6 positive-control (first instance of standing obligation)

Per team-lead's ruling this session, MW-6 is now a STANDING METHODOLOGICAL NORM: every audit-dispatched protocol must include a positive-control check. This audit does not dispatch a new protocol to tester — it's a synthesis audit — so MW-6 is inapplicable. Noting for completeness.

## 9. Impact on M-8 CANDIDATE promotion

Integrator registered M-8 CANDIDATE based on my audit-020 call, with two legs: H-NEW-23 sub-2 (genre partition) as leg #1 and H-NEW-19 as leg #2 (pending revision per task #41). The three-leg promotion gate is H-NEW-27 divine-name succession-pair coöccurrence asymmetry filtered to eschatological pericopes.

**Post-this-audit**, M-8 CANDIDATE evidence is:
- **Leg #1 H-NEW-23 sub-2**: still stands, clean on its own terms, χ²=113.96 on 5-way partition
- **Leg #2 H-NEW-19**: needs downgrading or re-framing. The current "elision-eschatology" label is unsupported by the actual Meccan/Medinan test. Task #41 (H-NEW-19-EXT with Ibn Abī l-Iṣbaʿ expanded genre partition) is the right follow-up — it would actually test an eschatological partition.
- **Leg #3 H-NEW-27**: pending.

**Recommendation**: M-8 CANDIDATE stays at CANDIDATE status but leg #2 should be marked **pending H-NEW-19-EXT resolution** rather than "PASSED in v1". The H-NEW-19 e_a density Meccan/Medinan result is real, but it supports an M-5 (chronology-gradient) reading more directly than an M-8 (eschatological-slot-engineering) reading.

## 10. Recommendations

### To classical-scholar (author of the synthesis):

**B1 (blocking revision)**: Correct the H-NEW-19 characterization. The current text (lines 32-34, 67) treats H-NEW-19 as a genre-specific (eschatological-vs-other) test. The actual test was Meccan-vs-Medinan chronology. Options:
- (a) Revise to "H-NEW-19 v1 Meccan/Medinan proxy" — honest but admits the test is a chronology proxy, not a genre test.
- (b) Wait for H-NEW-19-EXT (task #41) to supply the actual eschatological-partition result. Then re-cite.
- (c) Keep the v1 result but label it "indirect evidence via chronology proxy" with explicit caveat.

Recommend (b) — wait for H-NEW-19-EXT and then re-synthesize. The synthesis's central convergence claim is not yet supported.

**B2 (blocking revision)**: Disclose H-NEW-19's 2/3 null sub-tests. e_b density was null (p=0.455), e_c density was marginal (length-strat p=0.0036 but two-sided p=0.457). The synthesis currently presents H-NEW-19 as a single passing test. It wasn't — it was three sub-tests, only one of which passed.

**B3 (blocking revision)**: Replace "38× ratio" with the full 5-genre rate table. Lead with χ²=113.96 on df=4, report rates as [eschatological 7.71%, narrative 1.68%, polemic 0.96%, legal 0.20%, hymn 0.00%], and note that the eschatological-to-legal 38× comparison is the max-to-min of the partition. Report eschatological-to-narrative (4.6×) as the more representative comparison.

**F1 (non-blocking, framing)**: The "convergence is pre-theoretical (from classical sources)" framing at line 160 is a strong publication-grade claim that depends on the convergence being real. Until B1-B3 are addressed, this framing is not supported. After B1-B3, the convergence (if it survives) can be published more modestly: "al-Zarkashī's within-verse *maqṣūda li-ghayrihā* mechanism (H-NEW-23 sub-3 z=+10.61) and a 5-genre partition showing eschatological peak (H-NEW-23 sub-2 χ²=113.96) together support a single integrated finding; Ibn Abī l-Iṣbaʿ's *ījāz al-ḥadhf* doctrine pending H-NEW-19-EXT operationalization."

**F2 (non-blocking, structural)**: Move H-NEW-23 sub-3 and sub-2 into ONE cluster entry (they're the same H-NEW-23 finding, not two independent tests) and separate out the Ibn Abī l-Iṣbaʿ doctrine as a distinct third leg pending H-NEW-19-EXT. This reduces the "three tests" count honestly to "two tests of one doctrine + one pending test of a second doctrine" which is still a legitimate two-doctrine cluster once H-NEW-19-EXT lands.

### To integrator:

**Ruling request**: Synthesis marked NEEDS MAJOR REVISION, pending classical-scholar's response to B1/B2/B3. M-8 CANDIDATE evidence temporarily weakened — leg #2 downgraded from PASSED to PENDING-H-NEW-19-EXT. Leg #1 (H-NEW-23 sub-2) and the H-NEW-23 sub-3 within-verse slot control remain intact and M-8-supportive.

**MASTER ledger**: Do NOT yet promote the M-8 triple-test cluster finding to the ledger. Wait for revision. MASTER:hapax-verse-final stays at its existing audit-020 state (parent epistemic upgrade to mechanism-attributed).

**Task #41 prioritization**: H-NEW-19-EXT (Ibn Abī l-Iṣbaʿ expanded genre partition + taṣdīr-narrow retest) is now the load-bearing follow-up for M-8 promotion. Currently pending; consider raising priority.

**Coordination-layer note**: This is the first audit with a HARKing-level framing critique directed at classical-scholar (previous HARKing critiques were about tester calibration). The pattern: when a single author writes both the classical-mechanism claim AND the synthesis, the synthesis can inherit confirmation-bias toward the classical-mechanism framing. Worth watching for.

### To team-lead:

This is the first NEEDS MAJOR REVISION verdict since audit-019 (H-NEW-24 B1 blocker). The underlying statistical finding (H-NEW-23 primary) is NOT refuted — it stays at PASSED per audit-020. What's refuted is the synthesis's framing of a "three-to-one convergence" when the three results don't share a partition.

No retraction is needed. Correction + re-synthesis after H-NEW-19-EXT completes is the right path.

## 11. Verdict statement

**NEEDS MAJOR REVISION.** The synthesis's three-to-one convergence claim is not supported by the underlying data: (1) H-NEW-19's partition was Meccan/Medinan not eschatological, (2) H-NEW-19 has 2/3 failed sub-tests undisclosed, (3) the 38× ratio is a post-hoc max-vs-min pick. The underlying H-NEW-23 within-verse slot control (z=+10.61) remains robust. Revision path: wait for H-NEW-19-EXT (task #41) to run with an actual eschatological partition, then re-synthesize with honest two-doctrine cluster framing.

**HARKing 4-test: 2 FAIL, 1 PARTIAL-FAIL, 1 PASS.** First substantive HARKing critique to land in this audit series. Worth calibrating synthesis-authoring processes going forward.

**M-8 CANDIDATE**: stays at CANDIDATE. Leg #2 downgraded to PENDING-H-NEW-19-EXT. Do not promote to standing meta-pattern until H-NEW-19-EXT lands and the synthesis is revised.

**Audit-020 H-NEW-23 ruling is unchanged**: still PASSED, mechanism-attributed, MASTER:hapax-verse-final at p=7.35e−29 with epistemic upgrade from statistical-only to mechanism-attributed.
