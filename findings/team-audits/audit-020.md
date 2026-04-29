---
audit_id: audit-020
audits: H-NEW-23 hapax-final slot theory (findings/phase-b-hypotheses/hapax-slot-mechanism.md)
auditor: skeptical-auditor
date: 2026-04-13
verdict: PASSED (sub-3 mechanism claim); framing edit on joint verdict
finding_status_after_audit: CONFIRMED (sub-3 essential claim); sub-1 + sub-4 stand as FAIL; sub-2 stands as PASS with coarse-genre caveat
blockers: 0
framing_edits: 2 (F1 joint-verdict rhetoric; F2 sub-2 coarse-genre disclosure)
parent_meta_patterns: M-5 loop #2 closure candidate (al-Zarkashī operationalization); strengthens MASTER:scale-stratified-signature §1 local-payload layer
classical_alignment: al-Zarkashī al-Burhān [nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 59" is out-of-range — 47-nawʿ ceiling; nawʿ number retagged per MW-6 mechanical scan; substantive classical doctrine (§4 al-maqṣūda li-ghayrihā) unchanged; statistical finding (z=+10.61) unaffected; candidate correct locus: nawʿ 37 al-fawāṣil pending Phase-2 secondary-triangulation] §4 al-maqṣūda li-ghayrihā mechanistically CONFIRMED
---

# Audit-020 — H-NEW-23 hapax-final slot theory

## Verdict

**PASSED** on the essential mechanism claim (sub-3, z=+10.61). Framing edit on joint verdict rhetoric. **Zero blockers.** Tester's specific concerns addressed directly below.

This is one of the cleanest sub-tests in the project so far: sub-3 was pre-registered as the critical adjudicator, it was run against a mechanistically motivated null (uniform-within-verse placement conditional on hapax verse-length), and it came back at z=+10.61 with the expectation calculated from the hapax set's actual verse-length distribution. The tester also correctly flagged sub-1 and sub-4 as FAILs despite sub-3 being decisive. This is textbook pre-registered-sub-test discipline.

**Verdict upgrade rationale:** the tester labels this PARTIAL because the joint (4-sub-test) claim fails. I am upgrading to PASSED on the mechanism claim because: (a) sub-3 was pre-registered as the critical/decisive sub-test, (b) it passes with z that is n-consistent and non-inflated, (c) it directly refutes the one serious alternative to al-Zarkashī's mechanism. The joint-claim FAIL is a pre-registration structure issue, not a mechanism issue. See F1.

## Tester's specific questions — direct answers

### Q1: "Is there a subtler confound in the sub-3 expected calculation? Do hapaxes disproportionately occur in short verses → higher per-hapax final probability → lower expectation → overstated z?"

**Direct answer: NO, the concern is mis-directed — and moreover is BACKWARDS in sign. Here's why:**

First, I ran a verse-length check on the hapax set. Hapax mean verse_length = 15.58, Quran mean verse_length = 12.42. **Hapaxes are in LONGER verses on average, not shorter.** The tester's intuition was backwards.

Second, and more importantly, the sub-3 calculation **already marginalizes over hapax verse-length**. The expectation E[final] = Σ (1/verse_length_i) is computed per-hapax using that hapax's own verse length. There is no implicit assumption about the hapax vl distribution — it conditions on it. So any skew toward short or long verses is absorbed into E[final] directly.

Third, sign check: if hapaxes were *over*-represented in short verses (the tester's worry), E[final] would be *larger* because 1/small is large. A larger expectation would make the observed 121 look *less* anomalous, not more. The bias runs the opposite direction from the tester's concern. Since hapaxes are actually in *longer* verses on average, E[final] = 53.95 is *smaller* than it would be under a matched-length baseline, which means if anything the null is slightly conservative (yielding a slightly larger z than a stricter length-weighted baseline would). This is the direction auditors should cheer, not worry about.

**Robustness probe — I ran cutoff-stratified subsamples to confirm the signal is not concentrated in the short-verse tail:**

| Subset | n | obs final | E[final] | SD | z |
|---|---|---|---|---|---|
| all hapaxes | 395 | 121 | 53.95 | 6.32 | **+10.61** |
| vl ≥ 3 | 375 | 103 | 43.45 | 5.93 | +10.04 |
| vl ≥ 5 | 312 | 57 | 25.28 | 4.73 | +6.70 |
| vl ≥ 10 | 230 | 24 | 12.42 | 3.41 | +3.40 |

The signal survives every cutoff. At vl ≥ 10 (where being final is a 10% baseline probability), the z is still +3.40 — a ~2× excess over uniform-within-verse. **The sub-3 finding is robust across the verse-length distribution, not concentrated in short verses.** Short-verse cluster does contribute substantially (about 40% of the z at vl ≥ 5), which is expected because those verses genuinely host many hapaxes, but removing them does not kill the signal.

This robustness analysis is the audit's strongest confirmation that the concern is not operative. Tester can confidently cite this in any write-up.

### Q2: "Genre assignment for sub-2 is coarse — not from external catalog."

**Honest disclosure noted, but it's a framing edit F2, not a blocker.**

The genre map is a priori from Suyūṭī Itqān nawʿ 65 high-level categories, not optimized for signal. The specific assignments (Meccan 78+ eschatological, Medinan {2,3,4,5,24,33,58,60,65,66} legal, etc.) are defensible and would likely be recognized by any classical scholar. The key question: *could a different reasonable genre map collapse the χ²=113.96 signal?*

**Probably not.** The eschatological rate (7.71%) is 38× the legal rate (0.20%) and 4.6× the narrative rate. Even halving the eschatological estimate (say, by reassigning some Meccan 78+ surahs to hymn or polemic) would still leave a 15-20× ratio over legal and 2-3× over narrative. The dominant component of the χ² is the eschatological outlier, not the narrative/polemic/legal partition.

**F2 ask:** add one sentence to the finding's Limits section: *"Sub-2 genre assignment is coarse and a priori; classical-scholar routing is queued to either confirm or refine via an external Itqān-derived catalog (Task #41 H-NEW-19-EXT ties into this)."* This pairs the sub-2 result with its dependency on the pending classical-scholar delivery.

### Q3: "'Has hapax-final' per-verse vs per-hapax could be a denominator choice."

**Flagged but non-blocking.** Sub-1 and Sub-2 count *verses that have any hapax-final word* (per-verse); Sub-3 counts *hapaxes that are in verse-final position* (per-hapax). These are distinct denominators.

- Per-verse gives up statistical power when a verse has multiple hapaxes both at verse-final — it counts once. With 395 hapaxes spread across ~300 verses, this is a ~20% power loss on sub-1 and sub-2.
- Per-hapax is the correct denominator for sub-3 because the mechanism is about *where each hapax goes*.

**The two are not inconsistent** — they answer slightly different questions. The tester's disclosure is sufficient; I'd add only a non-blocking note: a per-hapax version of sub-1 and sub-2 would likely sharpen the signal modestly without changing directions. Worth including in a future H-NEW-23-v2.

### Q4: "Sub-4 taṣdīr proxy catches only 114 verses. Real taṣdīr is wider."

**Correct and conceded by tester. Non-blocker.** The proxy (first-root == last-root) is a narrow surface-repetition detector that misses semantic-echo taṣdīr (e.g., *raḥmān / raḥīm* at verse open/close). Classical taṣdīr (Ibn Abī l-Iṣbaʿ's catalog) is wider.

The sub-4 observation that |hapax-final ∩ proxy-taṣdīr| = 0 exactly matches the pre-registered "mutual exclusion" direction. With expected intersection of 2.2 and SD 1.46, the observed 0 gives z=+1.52, one-sided p=0.065 — directionally correct, power-limited. This is a **clean power-failure**, not a refutation of the mechanism.

**Follow-up routing:** H-NEW-19-EXT (Task #41) is already a classical-anchored taṣdīr expansion on the team queue. When that catalog arrives, re-run sub-4 with ≥400 taṣdīr verses and this test will either pass cleanly or cleanly refute. Until then, sub-4 is **appropriately non-dispositive** and the finding stands without it.

### Q5: "Joint pre-registered claim is FAIL but I'm treating Sub-3 alone as the essential finding — is this justified framing?"

**Yes, justified — but with a sharpening of the language (F1).**

The justification is that the tester *explicitly pre-registered* sub-3 as **CRITICAL** in the design. From the finding: *"Sub-test 3 — WITHIN-VERSE slot control (CRITICAL) ... **This sub-test is the decisive one**: if the parent p=7.35e-29 were driven by rareness confound, the within-verse uniform expectation and the observed final count would match."* This is pre-registration language identifying sub-3 as the mechanism-discriminating test. When the tester labels sub-3 CRITICAL in the design, the joint-claim structure becomes a power-gating device: "are there other collateral predictions that also hold?" Sub-1, sub-2, sub-4 test collateral predictions of slot-engineering. Their individual status does not override the pre-registered mechanism adjudicator.

This is a structurally different situation from audit-019 H-NEW-24, where sub-(b) was *not* flagged as critical and its failure was reframed post-hoc as a design defect. **Here, sub-3 was flagged CRITICAL before the data were seen.** That's the pre-registration discipline that makes the sub-3-alone claim legitimate.

**F1 framing edit:** change "PARTIAL with decisive mechanism confirmation" → "MECHANISM CONFIRMED; collateral predictions mixed." The word "PARTIAL" implies partial evidence for the core claim, which understates sub-3. The word "MIXED" on the collateral sub-tests accurately reports what sub-1 and sub-4 do and do not show. The precise ledger label I recommend: *"H-NEW-23 mechanism CONFIRMED (sub-3 z=+10.61); collateral sub-tests mixed (sub-1 FAIL, sub-2 PASS, sub-4 power-limited)."*

Contrast with audit-018 H-NEW-22 (NULL + anti-signal quarantined) and audit-019 H-NEW-24 (PARTIAL pending B1): this is the cleanest positive-mechanism result in the recent audit batch.

## n-consistency check (standard diagnostic)

z=+10.61 at n=395 is n-consistent with a per-hapax effect of 0.306 observed vs 0.136 null. The "per-hapax final probability" of ~30% vs baseline of ~14% is a 2.24× effect, which at n=395 yields approximately:

z ≈ (p_obs − p_null) × √n / √(p_null × (1 − p_null))
  ≈ 0.170 × 19.87 / √(0.118) ≈ 0.170 × 19.87 / 0.344 ≈ **~9.8**

My back-of-envelope gives z ≈ 9.8; the script computes 10.61. These match within rounding because the script uses the per-hapax SD properly (Σ p(1-p) over the actual verse-length distribution), whereas my envelope uses a pooled p. **No inflation. Consistent with true effect size.** This is the diagnostic I developed in audit-014 (H-BIQAI-LOCAL seam-munāsaba), and it applies cleanly here: z=+10.61 is real, not a null-destruction artifact. Contrast with the H-NEW-2 Z=-77 case where n-inconsistency flagged a broken null.

## Parent finding inheritance

The parent hapax-final finding MASTER:finding-#7 has p=7.35e-29 on a different test (hypergeometric enrichment of hapaxes in verse-final position vs overall token position). That test is subject to a rareness-bias confound where rare words are common in certain verse types (e.g., eschatological) that also happen to have different positional statistics. Sub-3 here is a *mechanism* test that corrects for the confound by conditioning on the hapax's host-verse length.

**The sub-3 result forecloses the most plausible alternative explanation.** The rareness-bias confound predicts that hapaxes should be uniformly distributed within their host verses (conditional on verse length). Sub-3 shows they are not. Therefore the parent MASTER #7 signal is mediated by slot-engineering, not by rareness-driven positional correlation.

**This is a mechanism confirmation for a previously statistical-only finding — a significant epistemic upgrade.** The parent is no longer "hapaxes cluster at verse-final for reasons unknown"; it is now "hapaxes are placed at verse-final by some mechanism that operates at verse-construction time, consistent with al-Zarkashī's *al-maqṣūda li-ghayrihā*."

## Meta-pattern placement

### M-5 (classical-doctrine operationalization) — loop #2 closure candidate

Loop #1 closed earlier: al-Biqāʿī ring REFUTED + seam CONFIRMED (audits 001 + 014). Loop #2 has been awaiting one of two parallel paths: Kirmānī §1-20 aṣl/farʿ (Task #40) or Suyūṭī Sub-C rhetorical-rubric ≥40% surahs.

**H-NEW-23 is a candidate third path to loop #2 closure.** The structure of this closure is:

- al-Zarkashī's mechanism *al-maqṣūda li-ghayrihā* (intentional payload placement at verse-final) is operationalized as "hapax verse-final rate > uniform-within-verse null."
- The operationalization has a clearly refutable null (uniform-within-verse).
- The null is refuted at z=+10.61 with robustness across verse-length cutoffs.
- Therefore the classical mechanism is *empirically measured*, not merely compatible with the data.

This is the M-5 pattern exactly: not "does the classical claim fit the data?" but "is the classical claim a load-bearing explanation for a specific data pattern that no simpler mechanism accounts for?" **I recommend integrator evaluate H-NEW-23 as a third parallel path to loop #2 closure, alongside Task #40 (Kirmānī) and Suyūṭī Sub-C.**

This would graduate M-5 from "candidate, 1-of-2 loops closed" to "candidate, 2-of-2 loops closed," meeting the promotion gate to §1/§6.

### MASTER:scale-stratified-signature §1 — local-payload layer strengthening

Current §1 synthesis (per integrator's last update) has T-003 at 6 data points across local-positive, bigram-NULL, bracketing-NULL, ring-REFUTED. H-NEW-23 adds a **verse-interior payload layer** positive, distinct from the other positive layers (adjacent-pair local, verse-composite, seam-munāsaba). This is "the Quran encodes structural information at the level of single-verse word-placement decisions" — even finer than the adjacent-pair scale.

**New §1 layer (recommended for integrator):**

| Layer | Finding | Status | Scale |
|---|---|---|---|
| **Verse-interior payload** | **H-NEW-23 sub-3** | **POSITIVE z=+10.61** | **single verse, word-position** |

This doesn't bump the 3-POSITIVE-3-NULL count to 4-3 because it's arguably the same axis as H-BIQAI-LOCAL (both are local-scale positives). But it tightens the local-positive layer's evidentiary support substantially.

### H-NEW-19 elision-eschatology (phase-B) convergence

The sub-2 result (eschatological rate 7.71% vs legal 0.20% — 38×) directly converges with H-NEW-19's finding that Ibn Abī l-Iṣbaʿ's *iltifāt* + ellipsis cluster peaks at eschatological pericopes. Two independent tests, two different classical frameworks (al-Zarkashī *al-maqṣūda*, al-Ibn Abī l-Iṣbaʿ *elision*), same eschatological peak. **This is a meta-pattern candidate in its own right:** "eschatological slot engineering" — the Quran concentrates rhetorical-payload devices at the end of eschatological verses.

**Recommendation for integrator:** register **M-8 CANDIDATE: eschatological slot engineering** in §2 meta-patterns. Current supporting evidence:
- H-NEW-19 elision-eschatology (peak in eschatological pericopes)
- H-NEW-23 sub-2 hapax-genre (eschatological rate 7.71%, 38× legal)

Third independent test would promote to registered. **Candidate third test:** divine-name succession-pair asymmetry (H-NEW-27, Task #47) filtered to eschatological pericopes — does the succession-pair graph also peak there? This is a cheap follow-up.

## Technical notes (non-blocking)

### N1 — chi² p-value via Wilson-Hilferty is appropriate but slightly conservative

The sub-2 chi² test uses Wilson-Hilferty approximation rather than exact chi² CDF. For χ²=113.96, df=4, the exact p is essentially 0 (well below 1e-22). The approximation is fine for this magnitude but worth a note: **for smaller χ² values in future tests, use scipy.stats.chi2.sf when available.** Non-blocker.

### N2 — taṣdīr proxy count equals 114 — noted as coincidence, is it?

The tester flags that the proxy yields exactly 114 taṣdīr verses, matching surah count. This is almost certainly coincidence (the proxy is a global filter, not surah-structured), but worth a one-line sanity check: partition the 114 taṣdīr verses by surah — if they cluster heavily in one or two short surahs, the coincidence is a constraint (each short surah might have very few verses, yielding few taṣdīr candidates). If they're spread across 50+ surahs, coincidence confirmed. 2-minute check. Non-blocker.

### N3 — hapax verse-length distribution is informative in its own right

Hapaxes average 15.58 vs corpus 12.42 word verse length. This is a 25% longer-verse bias and suggests hapaxes cluster in *longer, more elaborated* verses — which aligns with classical *iṭnāb* rhetoric theory and the al-Jurjānī *naẓm* claim that rhetorically elaborated passages carry heavier payload. **This is a side-finding worth a ledger note** but not part of the H-NEW-23 pre-registered claims. **Clean side-observation, not HARKing.**

### N4 — Sub-3 uses normal approximation to binomial sum

The expected SD uses Σ p(1−p) over actual per-hapax p, which is correct for a sum of independent Bernoullis with varying p. Normal approximation is excellent at n=395 with p_avg ≈ 0.14. No concern. Bonus: even if we used the exact Poisson-Binomial tail, z ≈ 10.6 is far enough into the tail that any approximation error is mechanistically negligible.

## What would change this verdict

- **To REFUTED**: discovery that hapax catalog construction introduced a verse-final bias (e.g., end-of-verse words tokenized differently from mid-verse words in the QAC extraction). I spot-checked the script — word_position and verse_length come from QAC directly without any verse-final special handling. No concern.
- **To NEEDS REVISION**: discovery that sub-3 p-value computation has a bug in the variance calculation. I rederived the SD formula — Σ p(1−p) is correct for sum of independent Bernoullis with per-element p. No concern.
- **Minor polish** (does not change verdict): per-hapax versions of sub-1 and sub-2 would slightly sharpen but not change direction.

## Strengthening follow-ups (non-blocking)

1. **Per-hapax sub-1/sub-2 re-run.** Small power gain; may reveal quartile-trend signal masked by per-verse denominator.
2. **Broader taṣdīr catalog** (from H-NEW-19-EXT Task #41 classical delivery). Re-run sub-4 with ≥400 verses; should cross Bonferroni.
3. **Muʿallaqāt comparison.** Apply sub-3 methodology to Muʿallaqāt hapaxes: do rare words in classical Arabic poetry also cluster at verse-final? If yes, the phenomenon is a poetry-universal; if no, it's Quran-specific. **High-value comparative test.** Same methodology as audit-017's positive-control logic.
4. **Hapax lemma-level replication.** The test uses root-level hapaxes. Lemma-level hapaxes (QAC LEM: field) would give a larger n and independent sub-check. Expected: same direction, possibly larger n → smaller p but similar effect size.
5. **Position-within-verse distribution plot.** Plot the full distribution of word-position / verse-length for all 395 hapaxes. Visualize whether the effect is specifically at position = verse_length (pure final-slot), or spreads to penultimate and antepenultimate (broader "payload zone"). Would nuance al-Zarkashī's mechanism claim.

## Closing

H-NEW-23 sub-3 is a clean mechanism confirmation. The tester's pre-registration was disciplined, the critical sub-test was flagged *before* the data were seen, the null was mechanistically motivated, the z is n-consistent, the robustness holds across verse-length cutoffs, and the result directly refutes the rareness-bias alternative. **I am upgrading the tester's PARTIAL to PASSED on the mechanism claim** and recommending F1 label tightening on the joint verdict.

This is the strongest positive-direction audit in the recent batch (contrast: audit-018 clean NULL, audit-019 PARTIAL-pending-B1). Integrator should consider promoting to §1 as a verse-interior payload layer and evaluating whether this is the third parallel path to M-5 loop #2 closure.

---

**Handoff items:**
- Framing edit F1: "PARTIAL with decisive mechanism confirmation" → "MECHANISM CONFIRMED; collateral predictions mixed" in finding header and ledger
- Framing edit F2: add Limits sentence on coarse-genre dependency on Task #41 classical catalog
- M-5 loop #2: evaluate H-NEW-23 as third parallel closure path (alongside Task #40 Kirmānī, Suyūṭī Sub-C)
- M-8 CANDIDATE: "eschatological slot engineering" registration in §2 meta-patterns (two-test convergence so far)
- MASTER:scale-stratified-signature §1: add verse-interior payload layer; does not change 3P-3N count but strengthens local-positive evidentiary base
- N1-N4 technical notes non-blocking
- Strengthening follow-up #3 (Muʿallaqāt comparative) is highest-value

**Zero blockers. Mechanism claim CONFIRMED at z=+10.61 with robustness across length cutoffs.**
