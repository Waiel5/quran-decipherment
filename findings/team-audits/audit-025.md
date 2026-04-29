---
audit_id: audit-025
date: 2026-04-13
auditor: skeptical-auditor
finding_under_review: H-NEW-34 — abjad-residue-null (findings/phase-b-hypotheses/abjad-residue-null.md)
finding_date: 2026-04-13
parent_task: #68
verdict: **PRIMARY PASSED AS NULL** (null-direction) + **REVERSE SIGNAL PASSED AS HYPOTHESIS-GENERATING** (mechanism pending Muʿallaqāt baseline)
lineage_tag: audit-025
related_audits: audit-021, audit-022, audit-024 (M-5 classical-doctrine operationalization track)
mw_candidates_touched: MW-6 (positive-control on auditor-specified protocols — not triggered here)
meta_patterns_touched: M-5 (classical-doctrine operationalization — 6th parallel path candidate)
harking_4test: CLEAN PASS ALL 4 (exemplary post-hoc labeling)
---

# Audit-025 — H-NEW-34 verse-final abjad modular-residue clustering (ḥisāb al-jummal null)

**One-line verdict**: The pre-registered null against Ibn ʿArabī / Khalifa-19 ḥisāb al-jummal verse-final abjad clustering is **decisively confirmed** at 6/6 tests. The unexpected reverse signal (Quran more uniform than prose baselines, z=−4.28 to −11.36) is honestly labeled post-hoc and has a classical-grounded mechanism hypothesis (fāṣila-driven word-repetition) but **cannot be upgraded to a confirmed finding without a rhymed-Arabic baseline** — the Muʿallaqāt dīwāns are already sitting in `data/baseline-corpora/raw/` and this is a trivial follow-up, not a data-acquisition blocker.

## 1. Reproducibility verification (PASS)

I independently reran the χ² computations on the counts stored in `csv/h-new-34.json`:

| m | Quran counts reported | χ² recomputed | χ² reported | Match |
|---|---|---|---|---|
| 7 | [832,978,781,903,1000,881,844] | 42.1393 | 42.1393 | ✓ |
| 11 | [448,568,609,619,495,519,583,673,611,582,512] | 75.6443 | 75.6443 | ✓ |
| 19 | [324,204,305,...,297] | 312.6586 | 312.6586 | ✓ |

z vs Bukhari m=11 recomputed: −11.3586 vs reported −11.36 ✓.

The script `scripts/h_new_34_abjad_residue.py` is clean:
- Seed 20260414 properly registered
- MODULI = [7,11,19] pre-declared (no post-hoc sweep)
- `random.sample(pool, N)` without replacement (correct)
- Pre-reg NULL decision is one-tailed upper
- Bonferroni k=3 declared up-front
- Hamza-carrier policy matches `methodology.md`
- Baseline corpora `bukhari-noquran.txt` (526k words) and `jahiz-hayawan.txt` (362k words) both exist at the expected paths

## 2. Primary pre-registered claim (PASSED AS NULL — decisively)

**Pre-reg hypothesis**: ḥisāb al-jummal clustering predicts Quran χ² > baseline 95pct for at least one m ∈ {7, 11, 19} against at least one baseline. This would be a signal consistent with Ibn ʿArabī *Futūḥāt* ch. 2 / al-Bisṭāmī *Shams al-Āfāq* / Rashad Khalifa *Miracle 19*.

**Result**: 6 of 6 tests confirm the null. Quran χ² ≪ baseline 95pct in every one of (2 baselines × 3 moduli). p_empirical = 1.000 in all 6 cells. Bonferroni-corrected α = 0.0167: NULL CONFIRMED with enormous margin.

**What is refuted**: The observable "verse-final-word abjad residue distribution clusters at prime moduli" does NOT distinguish the Quran from baseline Arabic prose in the direction predicted by ḥisāb al-jummal. Khalifa's mod-19 claim fails its own test: the Quran's m=19 distribution is 312.66, far below both Bukhari's 740 and Jahiz's 635 mean χ² expectations for same-length random samples. This is a publishable refutation of a specific numerological tradition on a specific operationalization.

**What is NOT refuted**: The broader claim that *some* letter-number correspondence holds somewhere in the Quran. This test refutes exactly one operationalization (verse-final word, prime moduli, uniform-expectation χ²). A non-prime modulus, a non-terminal position, or a non-uniform expectation could produce different results. The finding correctly limits its claim.

**Verdict on primary**: **PASSED AS NULL**. Clean classical-doctrine operationalization, clean refutation. This is exactly what the M-5 meta-pattern track is designed to produce — a specific classical claim translated into a pre-registered falsifiable test, and decisively decided.

## 3. Reverse signal — quantitative framing correction needed

Tester frames the reverse signal as: "Quran is more uniform than baseline". This is technically correct but potentially misleading without an additional context point.

**Sanity check against theoretical uniform null** (χ² expectation = df = m−1):

| m | Quran χ² | theoretical df | ratio Q/df | z vs theoretical uniform null |
|---|---|---|---|---|
| 7 | 42.14 | 6 | 7.0× | **+10.43** |
| 11 | 75.64 | 10 | 7.6× | **+14.68** |
| 19 | 312.66 | 18 | 17.4× | **+49.11** |

The Quran is STILL **massively non-uniform** — it rejects the uniform null with enormous z-scores. It is simply LESS non-uniform than prose sampling would produce. The correct framing is:

> "The Quran's verse-final abjad residue distributions deviate significantly from uniform (χ² 7-17× the theoretical df, z vs uniform = +10.4 to +49.1), but they deviate LESS than random same-length samples from al-Bukhārī and al-Jāḥiẓ would (z below baseline mean = −4.3 to −11.4). The Quran sits in a narrow window: visibly non-uniform, but less bumpy than matched-length prose."

**F1 recommendation**: Tester, please add this two-axis framing to the §"Unexpected reverse signal" section. "More uniform than prose" ≠ "uniform". Both comparisons are informative and they should be reported side by side. This is not a rejection of your finding — it clarifies the shape of the signal for future citers.

## 4. Reverse signal mechanism — **Muʿallaqāt baseline is the decisive test and the data is already present**

The fāṣila-repetition mechanism hypothesis is plausible and classically-grounded. However, as tester honestly notes, it is asserted not tested. The audit-blocker issue is:

**Claim**: "Quran's rhyme-scheme forces verse-final words onto a small repeating pool, which makes the abjad residue distribution more uniform than un-rhymed prose sampling."

**Prediction**: A RHYMED baseline should show the same under-dispersion. If the Muʿallaqāt produce comparable χ² z-scores (i.e., the mechanism is "rhymed-Arabic-text"), the Quran's reverse signal is mechanistic. If the Muʿallaqāt don't show it (i.e., the Quran under-disperses even vs rhymed baselines), the Quran has additional structure beyond what rhyme-repetition alone explains.

**Data is already present**. The 7 Muʿallaqāt dīwāns are already sitting in `data/baseline-corpora/raw/`:
- diwan-imru-al-qais.txt
- diwan-tarafa.txt
- diwan-zuhayr.txt
- diwan-labid.txt
- diwan-antara.txt
- diwan-amr-ibn-kulthum.txt
- diwan-harith.txt

This is a 30-minute addition to the existing script. Load the pooled dīwāns, extract verse-final words, sample N=6219 (or as many as available) random verse-finals, run the same χ² residue computation. Output: one more row of means/sds/z-scores per modulus.

**B1 recommendation (blocking for reverse-signal promotion)**: Add a third baseline section `muallaqat_nulls_per_m` to `csv/h-new-34.json`. Report the z-scores. If Quran z vs Muʿallaqāt is near zero, mechanism confirmed and the reverse signal becomes M-6 (fāṣila-substrate) candidate. If Quran z vs Muʿallaqāt is still −3 or more, the Quran has surplus under-dispersion beyond rhyme and the reverse signal becomes a novel hypothesis-generating finding in its own right.

Either outcome is publishable. The current state — "we saw a z=−11 reverse signal, plausibly explained by rhyme but not tested" — is incomplete.

**This same Muʿallaqāt-baseline gap is also blocking**:
- Task #63 (H-NEW-22-BASELINE rhymed-corpus generalization for verse-boundary acrostic)
- Task #72 (T-004 Muʿallaqāt positive-control for hapax-verse-final slot engineering)

Three findings now need Muʿallaqāt-as-baseline. I am reinforcing this as a cross-finding priority in my integrator dispatch.

## 5. n-consistency diagnostic

The strongest reverse z is Bukhari m=11 at −11.36. Is this a large effect or sample-size inflation? Unlike Mann-Whitney, the z here comes from (observed_chi2 − null_mean) / null_sd over 1000 permutations with fixed N=6219. The null sd scales roughly as sqrt(2·df·N/(N/m)) ≈ sqrt(2(m−1)) for the theoretical chi-square under uniform, but baseline samples have wider variance due to baseline word-abjad heterogeneity (Bukhari m=11 null sd = 53.8 vs theoretical sd ≈ 4.47 under uniform).

Effect-size interpretation: Cohen's d equivalent here is (75.64 − 686.81) / 53.81 = −11.36, which is d = 11.36 — an enormous effect. But "enormous" is measured against the *range* of the null distribution, not against an a priori scale. A better interpretation: the observed Quran χ² (75.64) is less than 11 of the 1000 baseline permutations combined (p_empirical = 0 — nothing in the baseline goes that low). This is a directionally decisive rejection, not a marginal z-inflation from large N.

**Verdict**: The reverse signal is genuinely large, not sample-size artifact. Its interpretation is a mechanism question, not an effect-size question.

## 6. Dropped verses — accuracy correction

Tester writes: "17 of 6,236 verses excluded due to ambiguous final-word extraction. Excluded verses are mostly muqaṭṭaʿāt and edge cases where the last token is a single disconnected letter or special mark."

**I enumerated the 17 dropped verses**:

| Surah:verse | Dropped token | Type |
|---|---|---|
| 7:206 | ۩ | sajda mark (U+06E9) |
| 13:15 | ۩ | sajda mark |
| 16:50 | ۩ | sajda mark |
| 17:109 | ۩ | sajda mark |
| 18:1 | ۜ | saktah mark (U+06DC) |
| 19:58 | ۩ | sajda mark |
| 22:18, 22:77 | ۩ | sajda mark |
| 25:60 | ۩ | sajda mark |
| 27:26 | ۩ | sajda mark |
| 32:15 | ۩ | sajda mark |
| 38:24 | ۩ | sajda mark |
| 41:38 | ۩ | sajda mark |
| 53:62 | ۩ | sajda mark |
| 69:28 | ۜ | saktah mark |
| 84:21 | ۩ | sajda mark |
| 96:19 | ۩ | sajda mark |

**None of these are muqaṭṭaʿāt**. They are 15 sajda (prostration) markers and 2 saktah (pause) markers that the text source appends as terminal tokens in the verse string. The sajda-marker set is a known canonical set (15 verses in standard Ḥafṣ recitation).

**F2 recommendation**: Please correct the §"Garden of forking paths" and §"Summary statistics" passages to say "17 verses dropped where the last whitespace-delimited token is a sajda marker (U+06E9, 15 verses) or saktah marker (U+06DC, 2 verses); these are recitation glyphs, not words". This is a minor accuracy correction, not a methodological issue — the dropped set is defensible and small, but the characterization is wrong.

A downstream consideration: the sajda-verse set is itself a known classical object (the "verses of prostration"). It would be interesting to check whether excluding them materially shifts the chi² — almost certainly not at N=15/6219, but a one-line robustness check would close the gap.

## 7. Garden of forking paths review

Tester discloses:
- Moduli {7, 11, 19} pre-registered; no sweep (✓)
- Mashriqi abjad table locked in methodology.md (✓)
- Hamza policy locked in methodology.md (✓)
- Bonferroni k=3 declared (✓)
- 1000 perms per baseline (adequate for one-tailed upper test)
- 17 verses excluded, characterization partially wrong (see §6)

**Unflagged forking paths I checked**:
- Word-boundary definition: "last whitespace-delimited token" is the only reasonable choice at the rasm level and is consistent across the project. Not a path.
- Abjad-sum vs abjad-product: only sum was tested. Product would be a different test entirely; not a forking path for this finding.
- Per-surah stratification: not applied. Could show whether the reverse signal is uniform across surahs or concentrated in heavily-rhymed Meccan sections. Not required for the primary test. Should be added to the followup.

**No HARKing red flags**. Moduli were pre-registered, direction was pre-registered, post-hoc reverse observation is explicitly labeled.

## 8. HARKing 4-test framework

| Test | Question | Result |
|---|---|---|
| 1. Explicit non-counting | Does tester claim the NULL direction as a primary finding, with post-hoc reverse as exploratory? | **PASS** — §"Null vs reverse — how to report" explicitly: "The primary pre-registered test was NULL-CONFIRMED unambiguously... The reverse signal is a genuinely unexpected observation... Was NOT pre-registered as a two-tailed hypothesis... Reported honestly as an exploratory observation requiring pre-registered replication." |
| 2. Pre-existing mechanism | Is the mechanism hypothesis classically grounded, not invented after seeing the data? | **PASS** — The fāṣila (rhyme) constraint is a standard classical observation (al-Rummānī, al-Bāqillānī, al-Suyūṭī all discuss it). Tester invokes it as an explanation, not as a hypothesis retrofit. |
| 3. Pre-registered directional evidence | Is the pre-reg decision rule clean? | **PASS** — "Quran χ² ≤ baseline 95pct for all three m → NULL confirmed". One-tailed upper. Bonferroni k=3. Clean. |
| 4. Refusal to rename | Does tester reframe the failed-positive as a success? | **PASS** — Tester explicitly names the primary finding "NULL-CONFIRMED" and creates a separate exploratory §. Does not relabel the reverse signal as the "real finding". |

**4/4 CLEAN PASS**. This is another model example for the team's HARKing training, alongside H-NEW-29 (audit-022) and H-NEW-24-B1/B2 (audit-024).

## 9. Meta-pattern implications

**M-5 (classical-doctrine operationalization) — 6th parallel path candidate**:
- Path 1: H-NEW-19 Ibn Abī l-Iṣbaʿ elision-eschatology
- Path 2: H-NEW-20 al-Rāzī linear munāsaba
- Path 3: H-NEW-23 al-Zarkashī *maqṣūda li-ghayrihā*
- Path 4: H-NEW-18 al-Kirmānī mutashābih directionality
- Path 5: H-NEW-29 al-Jāḥiẓ *takrār maqbūl*
- Path 6 (NEW, this audit): H-NEW-34 Ibn ʿArabī / Khalifa ḥisāb al-jummal (PASSED AS NULL)

Note this is a null-direction addition — M-5 is defined as "operationalization track", not "confirmation track". A clean null is still a data point in the operationalization exercise. I will mention this in integrator dispatch and let them rule on whether nulls count toward M-5 promotion evidence.

**M-6 (pericope-substrate) — potential path via rhyme mechanism**: If the Muʿallaqāt baseline follow-up shows that the reverse signal is rhyme-driven, H-NEW-34 becomes a M-6 candidate path (fāṣila-as-substrate). If it shows the Quran still under-disperses vs rhymed baselines, it becomes a standalone novel finding. Pending follow-up.

**MW-6 not triggered**: H-NEW-34's null protocol was appropriately pre-registered by tester. No auditor-specified broken protocol to catch. This is an organic pre-reg discipline success.

## 10. Recommendations to tester

**F1 (non-blocking, framing)**: Add two-axis framing to §"Unexpected reverse signal": Quran is non-uniform (z=+10.4 to +49.1 vs theoretical df) but less bumpy than prose (z=−4.3 to −11.4 below baseline means). Report both.

**F2 (non-blocking, accuracy)**: Correct the dropped-verses characterization. Replace "mostly muqaṭṭaʿāt" with "15 sajda markers (U+06E9) and 2 saktah markers (U+06DC) — terminal recitation glyphs, not words". Enumerate the list (my §6 table) in a comment or appendix for reproducibility.

**B1 (BLOCKING for reverse-signal promotion)**: Add Muʿallaqāt dīwān pool as third baseline. All 7 dīwāns are already in `data/baseline-corpora/raw/`. Run the same 1000-perm chi² null with sample size matched to available pool (or to Quran N=6219, whichever is smaller). Report z-scores per modulus. If Quran z vs Muʿallaqāt is in [−1, +1], rhyme mechanism is confirmed and the reverse signal becomes descriptive of rhymed-Arabic structure generally. If Quran z remains < −3, the Quran has structure beyond rhyme and the reverse signal is a novel M-6 candidate.

**F3 (non-blocking, enhancement)**: Per-surah stratification of the reverse signal. Does the under-dispersion concentrate in the short Meccan heavily-rhymed section (surahs 78-114) or is it spread across the whole text? A quick `z_by_surah_length_quartile` breakdown would answer this.

**F4 (non-blocking, followup)**: H-NEW-34a (verse-initial abjad residue as rhyme-free control) and H-NEW-34b (per-rhyme-class abjad dispersion) are good follow-up hypotheses. Pre-register them before running. I'll support their task creation if and when you have bandwidth.

## 11. Recommendations to integrator

1. **H-NEW-34 status**: Accept PASSED AS NULL for the primary pre-registered claim. Refutation of Ibn ʿArabī / Khalifa-19 verse-final abjad clustering at m ∈ {7, 11, 19} is clean and publishable.

2. **Reverse signal status**: HYPOTHESIS-GENERATING pending Muʿallaqāt baseline. Do not promote to confirmed or exploratory-confirmed until B1 is run.

3. **M-5 (classical-doctrine operationalization) promotion evidence**: now 6 parallel paths total, of which 4 are positive and 2 are null (H-NEW-34 is the clean null; H-NEW-29 was a mixed-direction null/confirmed). Consider whether M-5 promotion criteria should count nulls as evidence-of-operationalization (they do, I argue — a specific classical claim translated into a decidable test and decisively decided is the whole point).

4. **Cross-finding Muʿallaqāt-baseline priority**: Three currently-pending findings need Muʿallaqāt-as-baseline — task #63 (H-NEW-22-BASELINE), task #72 (T-004 Muʿallaqāt positive-control), and now H-NEW-34 B1 (this audit). I recommend you bundle these into a single sub-task for tester: "Build standard Muʿallaqāt pooled-dīwān baseline module, parameterized to serve all three current needs." Saves redundant pipeline work.

5. **HARKing training corpus**: H-NEW-34 joins H-NEW-29 and H-NEW-24-B1/B2 as model examples of clean post-hoc labeling. Consider spinning a brief `findings/meta/harking-model-cases.md` memo — I'm happy to draft it if you want.

6. **No MW-6 counterfactual**: This finding was properly pre-registered by tester without auditor intervention. The MW-6 infrastructure is not relevant here. Noting for completeness.

## 12. Verdict statement

**Primary**: H-NEW-34 PASSED AS NULL. Ibn ʿArabī / Khalifa-19 ḥisāb al-jummal verse-final abjad clustering is refuted on the pre-registered observable. 6/6 tests confirm, Bonferroni-corrected.

**Reverse signal**: HYPOTHESIS-GENERATING. Robust statistical observation (z=−4.28 to −11.36 below two prose baselines), honest post-hoc labeling, plausible classical-grounded mechanism (fāṣila repetition), mechanism test trivially available (Muʿallaqāt baseline in existing data). Promotion to confirmed reverse finding is blocked only on the 30-minute Muʿallaqāt run.

**Auditor conduct rating**: CLEAN PASS on HARKing 4-test. Exemplary pre-registration discipline. Honest exploratory labeling. Concrete follow-up proposals (H-NEW-34a/b) with specified operationalizations.

**Parent upgrade path**: None required — primary claim status is stable at PASSED AS NULL. Reverse-signal upgrade path to CONFIRMED runs through B1 (Muʿallaqāt baseline). Reverse-signal upgrade path to NOVEL-MECHANISM-SIGNAL runs through B1 + H-NEW-34a/b follow-ups.

**This is the third consecutive audit (022, 024, 025) where the tester's pre-registration and HARKing discipline has been exemplary.** Audit rate is going up, quality is holding. Noted for the team-level journal.
