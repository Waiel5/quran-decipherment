---
audit_id: audit-018
audits: team-discovery-017 (H-NEW-22 Quranic acrostic scan)
auditor: skeptical-auditor
date: 2026-04-13
verdict: PASSED AS NULL — anti-signal correctly quarantined, NOT HARKing
finding_status_after_audit: NULL-with-anti-signal (unchanged)
blockers: 0
framing_edits: 1 (minor, on "anti-signal" label)
parent_meta_patterns: MASTER:scale-stratified-signature §1 (7th data point)
classical_alignment: Ibn ʿAshūr (Taḥrīr 1:96-102) dismissal of intra-surah acrostics CONFIRMED; al-Zarkashī (Burhān [nawʿ number PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 59" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; correct location for fawāṣil is candidate nawʿ 37 pending physical verification]) on fawāṣil rhyme-constraint provides mechanism for anti-signal
---

# Audit-018 — H-NEW-22 Quranic acrostic scan (per-surah + cross-surah)


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Verdict

**PASSED AS NULL.** Zero blockers. Pre-registered one-sided positive-direction prediction fails cleanly on all three sub-tests under Bonferroni k=3. Finding status unchanged: NULL-with-anti-signal.

The tester asked me specifically: *"flag if anti-signal disclosure crosses the line from honest-disclosure into HARKing."* Short answer: **NO, it does not.** Extended justification below.

## The HARKing question — direct answer

HARKing = Hypothesizing After Results are Known. The diagnostic is whether a post-hoc result is presented as if it had been predicted, thereby double-counting the data for both discovery and confirmation.

The anti-signal in team-discovery-017 passes four honest-disclosure tests:

1. **Explicit non-counting.** The tester writes: *"Anti-signal is post-hoc and NOT counted toward the pre-registration verdict. It's reported only as a disclosure of actual observed direction."* This is the opposite of HARKing — HARKing would repackage the anti-signal as a two-sided Bonferroni-corrected positive finding. The tester explicitly refuses to do so, even though |z|=3.19 would survive two-sided α_bon=0.0033.

2. **Pre-existing classical mechanism.** The tester grounds the anti-signal in al-Zarkashī *Burhān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 59" out-of-range; candidate nawʿ 37 *al-fawāṣil*]** on fawāṣil being selected for phonetic-acoustic compatibility (sajʿ rhyme-constraint restricts terminal consonants to a small set, mostly ن م ر, suppressing substring diversity). This is a mechanism from prior classical work, not a just-so story invented to fit z=-3.19. Critically, the mechanism was *not used to generate* the H-NEW-22 hypothesis — H-NEW-22 tested Ibn ʿAshūr's *opponents*, not Zarkashī's fawāṣil theory. The anti-signal is what happens when two orthogonal classical claims collide in the data.

3. **Directional symmetry with the Muʿallaqāt baseline.** The N3 test shows classical Arabic monorhyme poetry at rate 0.1149 vs Quran 0.1020. This was *pre-registered*. The directionality of the anti-signal (Quran < baseline) is therefore already present in a pre-registered cell before N1 and N2 are run. It is not a surprise invented after the fact.

4. **Refusal to reframe the verdict.** A HARKing-compromised report would retitle the finding as "H-NEW-22-v2 rhyme-constraint confirmed." The tester does not. The finding's *name* is still the failed acrostic hypothesis. The anti-signal is a footnote. This is the discipline McKay-style pre-registration demands.

**Verdict on HARKing: clean.** This is the correct way to disclose an unpredicted directional result.

## Framing edit F1 (minor)

The phrase "anti-signal" risks connoting more than it means. What the data shows is that Quranic verse-boundary letters are *less* substring-diverse than null baselines — a direct consequence of rhyme selection. Suggested re-label for the ledger entry and any downstream synthesis:

- *"rhyme-constraint suppression of substring diversity at verse boundaries"* (descriptive, mechanistically anchored)
- **not** *"anti-acrostic signal"* (sounds like a second positive finding)

This is not a blocker. The current language is already hedged inside the document; the edit is for ledger-level precision.

## Buckwalter bug — acceptable

The mid-run fix (empty dictionary → Buckwalter→Arabic conversion) is disclosed in forking paths. The pre-registered design (what counts as a hit, what the null is, what the acceptance threshold is) did not change. Only the dictionary-loading implementation changed. This is a standard implementation bug-fix under the "rules tuple unchanged, data pipeline fixed" exception. **No audit concern.**

One mild note: the original run producing "empty dictionary" would have yielded 0 observed hits, which the pre-registered null would also (mechanically) center near 0, giving a non-meaningful null z. Re-running with the correct dictionary does not risk contaminating the test because the dictionary is a fixed external artifact (QAC v0.4), not data-dependent. **Clean.**

## Instrument positive control — present

The Muʿallaqāt first-letter hit rate of 0.1149 serves as an implicit positive control: the instrument DOES detect dictionary substrings when presented with a corpus where terminal-letter diversity is higher. The Quran rate (0.1020) is lower but non-zero, so the instrument is functional across the full pipeline. This satisfies the positive-control principle I introduced in audit-015. **No concern.**

(Contrast with audit-015's H-NEW-1 issue, where the null mechanically destroyed the signal it was meant to test against. Here the null preserves the signal space and the Quran simply has less of it.)

## Classical alignment

1. **Ibn ʿAshūr** (*Taḥrīr* 1:96-102) explicitly dismisses acrostic readings beyond the muqaṭṭaʿāt. H-NEW-22's negative result directly confirms this dismissal at the lexical-substring level. This is the rare case where a NULL finding is substantively informative because the classical position being tested was *already* a rejection — the empirical result vindicates the rejection.

2. **al-Zarkashī** (*Burhān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 59" out-of-range in 47-nawʿ edition; candidate nawʿ 37 *al-fawāṣil*]**, fawāṣil) predicts the anti-signal direction from rhyme-selection, as discussed above.

3. **al-Suyūṭī** (*Itqān* nawʿ 59 on fawāṣil, nawʿ 62 on sajʿ) corroborates Zarkashī.

Three classical sources align with what the data shows. The test adjudicates a *live* classical dispute (the intra-surah acrostic readers vs Ibn ʿAshūr) rather than relitigating settled ground.

## Meta-pattern placement — MASTER:scale-stratified-signature §1 update

Current scale-stratified-signature data points (from audits 016, 017, and now 018):

| Layer | Finding | Status | Scale |
|---|---|---|---|
| Local pairwise | H-BIQAI-LOCAL seam-munāsaba | POSITIVE (z=+10.06) | adjacent verse pairs |
| Verse-composite marker | H-NEW-20 intra-verse pattern | POSITIVE-pending-block-null | verse-internal |
| Bigram transition | H-NEW-13 bigram spectrum | NULL (clean) | letter-bigram |
| Intra-surah bracketing | H-SUYUTI-BRACKETING | NULL (not REFUTED) | within-surah |
| **Verse-boundary acrostic** | **H-NEW-22 acrostic** | **NULL-with-anti-signal** | **verse-boundary letter** |
| Register mixing | H-NEW-13 ḥadīth side-finding | POSITIVE (Bukhari λ_2=0.265) | corpus-register |

This is now the **7th layer data point** (6 loaded above + the Biqāʿī ring REFUTATION at long-range scale, which Integrator has in §1). The stratification pattern tightens: **local positive, boundary-level NULL, corpus-register positive (outside-Quran), long-range NULL.** The Quran exhibits cohesion structure at *short* ranges (adjacent pairs, verse-internal) but not at boundary-letter encoding or long-range bracketing.

This is a substantively novel meta-finding. I recommend integrator elevate MASTER:scale-stratified-signature §1 from candidate to registered.

## Meta-pattern placement — M-5 (classical-doctrine operationalization)

H-NEW-22 confirms a classical REJECTION (Ibn ʿAshūr). M-5 is framed around operationalization of classical doctrines irrespective of polarity, so a confirmed rejection counts. M-5 now has:

- Loop #1 CLOSED: Biqāʿī ring-vs-seam (REFUTED + CONFIRMED)
- 4+ open loops (H-SUYUTI-BRACKETING NULL, H-NEW-13 bigram NULL, H-NEW-1-v3 pending, H-NEW-22 now added)

H-NEW-22 is best registered as a **literal-classical-agreement** instance: the test's NULL outcome agrees with the classical dismissal. This is distinct from "operationalization-shows-doctrine-is-empirical" (Biqāʿī seam).

## Strengthening follow-ups (non-blocking)

None of these affect the verdict. They would sharpen the published claim if resources permit.

1. **Lisān al-ʿArab dictionary comparison.** The 4,927-entry QAC dictionary may undercount historical roots. A Lisān-derived dictionary (est. ~11k roots) would approximately double the hit space and test the "direction not absolute magnitude" claim in the limits section. Expected: direction preserved, magnitudes scale.

2. **Verse-length stratification.** Short verses (common in Meccan surahs) have different boundary-letter statistics than long verses (Medinan). A Meccan/Medinan split might show the anti-signal concentrated in one register, which would further localize the Zarkashī mechanism.

3. **Muqaṭṭaʿāt positive-control sub-test.** Explicitly run the acrostic scan on the 29 muqaṭṭaʿāt surahs' opening letters. If the instrument reports *any* signal there (even just "the letters are letters"), that's a sanity check on how much signal the method can even in principle detect. Expected: still no dictionary hits at length ≥3, but informative to report explicitly.

4. **Non-Quranic baseline with rhyme-constraint.** Test the anti-signal direction on Bible, Tanakh, or Rig Veda verse-boundary letters. If all rhymed/sung corpora show sub-baseline substring rates, the Zarkashī mechanism generalizes and the anti-signal is a poetry-universal. If only the Quran does, it's Quran-specific. **Highest-value follow-up.**

## What would change this verdict

- **To REFUTED:** discovery that the dictionary was mistakenly seeded from Quran text (data leakage). I spot-checked — QAC is upstream of the finding and independent. Not a concern.
- **To NEEDS REVISION:** discovery that the N1/N2 shuffles preserve an artifact that Sub-A's Muʿallaqāt baseline doesn't. The three-null convergence rules this out.
- **To PASSED AS PARTIAL POSITIVE:** if Lisān dictionary pushes the direction above zero. Low prior probability given the magnitude of the current negative effect.

## Closing

This finding is methodologically clean. The tester's HARKing self-check was correctly triggered and correctly resolved. The anti-signal disclosure is disciplined and mechanistically anchored to pre-existing classical work. The null is substantively informative because the classical position being tested was itself a rejection.

Audit-018 cleared. Passing to integrator with MASTER:scale-stratified-signature §1 promotion recommendation and F1 ledger-label edit.

---

**Handoff items:**
- Framing edit F1: re-label "anti-signal" → "rhyme-constraint suppression" in ledger/synthesis
- MASTER:scale-stratified-signature §1: 7th data point added; recommend promotion from candidate to registered
- M-5: new literal-classical-agreement instance (Ibn ʿAshūr rejection confirmed)
- Follow-up #4 (non-Quranic rhymed-corpus baseline) flagged highest-value for future queue
- No blockers; finding status NULL-with-anti-signal unchanged
