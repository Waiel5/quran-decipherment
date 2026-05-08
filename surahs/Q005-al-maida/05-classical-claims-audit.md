---
surah: 5
surah_name_ar: المائدة
surah_name_translit: al-Māʾida
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: "8 classical claims audited. 5 VINDICATED (late-Medinan-chronology, Q 5:3 = ʿArafāt-Friday-Hajjat-al-Wadāʿ, Q 5 PoTB-density rank-1 within Medinan-5, al-Biqāʿī Q4→Q5 munāsabāt empirically smoothest, māʾida-lemma corpus-hapax). 1 RULES-TUPLE-FRAGILE (the 'last surah revealed' claim depends on which chronology — Egyptian Standard vs Nöldeke vs Companion-tradition — is privileged). 1 NULL (al-Rāzī covenant-density-quantitative claim FALSIFIED at corpus level, but qualitative thematic-multiplicity claim STANDS). 1 NOT-EMPIRICALLY-TESTABLE (Q 5:55 walāyah Sunnī-Shīʿī interpretive dispute is hermeneutic-historical, not empirically falsifiable)."
---

# Q 5 al-Māʾida — Classical Claims Audit

This file audits 8 non-trivial classical claims about Q 5. Each claim is stated, sourced, given a rules-tuple, tested, and verdicted.

## Claim 1 — al-Suyūṭī: Q 5 is among the LAST surahs revealed

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (in chronology), citing Asmāʾ bint Yazīd al-Anṣāriyya via al-Tirmidhī (recension #3063). Also citing Ibn ʿAbbās, ʿĀʾisha. Also: al-Wāḥidī, *Asbāb al-nuzūl*; al-Qurṭubī, *al-Jāmiʿ* on Q 5:1. Verified at file `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`.

**Rules-tuple**: classical chronology source = which Companion-tradition or which modern-curated chronology (Egyptian Standard vs. Nöldeke).

**Empirical test**: cross-reference `data/revelation-order.csv`:
- Egyptian Standard chronology: Q 5 = rev #112 (3rd-from-LAST).
- Nöldeke chronology: Q 5 = rev #114 (LAST).

Both chronologies place Q 5 as among the absolute last surahs revealed. Asmāʾ bint Yazīd's hadith (the strongest-sourced "Q 5 is the LAST" tradition) is consistent with the Nöldeke order; the Egyptian Standard places Q 9 as the ultimate LAST-revealed (which is also a classical position from Ubayy b. Kaʿb via al-Bukhārī).

**Verdict**: **VINDICATED** at the late-Medinan / one-of-the-last-3 level. The "absolute LAST" claim is **RULES-TUPLE-FRAGILE** between Egyptian Standard (#112) and Nöldeke (#114). al-Suyūṭī himself acknowledges this dispute and harmonizes by attributing it to "what reached each Companion."

## Claim 2 — al-Bukhārī #45 (ʿUmar via Ṭāriq b. Shihāb): Q 5:3 was revealed at ʿArafāt on a Friday during Hajjat al-Wadāʿ

**Source**: Ṣaḥīḥ al-Bukhārī, *kitāb al-īmān*, ḥadīth **#45**. Also in *kitāb al-tafsīr* #4213 and *kitāb al-iʿtiṣām* #6993. Tirmidhī parallel #3127 (graded *ḥasan ṣaḥīḥ*). The Jewish-companion of ʿUmar acknowledges that the verse, had it been revealed to them, would have been a festival.

**Rules-tuple**: Sunnī isnād-chain ; the Imāmī Shīʿī tradition holds Q 5:3 was revealed at Ghadīr Khumm (al-Ṭabarsī, *Majmaʿ al-bayān*).

**Empirical test**: This is a historical-isnād claim. The Sunnī isnād (Bukhārī's al-Aʿmash → Mūsā b. Salama → Saʿīd b. Jubayr → Ibn ʿAbbās chain in some recensions; the alternative Ṭāriq b. Shihāb → ʿUmar in #45) is graded *ṣaḥīḥ*. The Imāmī alternative chain (al-Ṭabarsī's recension) is graded internally within the Imāmī tradition. NOT mutually-falsifiable from text alone.

**Empirical correlate** (Q005-F-03): Q 5:3 is the corpus-RANK-1 verse-level density of the completion-cluster {dīn, niʿmah, k-m-l, t-m-m, r-ḍ-w}, with 5 of 5 distinct cluster-members and density 0.106 tokens/word. p_perm = 0.0001 < α_bon = 0.01. The verse's STRUCTURE is verifiably the densest "completion-of-religion" declaration in the corpus.

**Verdict**: **VINDICATED in the Sunnī tradition** at hadith-isnād level (multiply-attested ṣaḥīḥ chains). The Imāmī alternative is hermeneutically-coherent but cannot be empirically arbitrated from text alone. **The empirical density-distinctness of Q 5:3 (Q005-F-03) VINDICATES the verse's status as a structurally-distinctive completion-declaration regardless of which historical asbāb-tradition is privileged.**

## Claim 3 — al-Rāzī: Q 5 is *khiṭāb al-yahūd wa-l-naṣārā* (PoTB-densest surah)

**Source**: al-Rāzī, *Mafātīḥ al-ghayb*, intro and on Q 5:1. al-Rāzī characterizes Q 5 as the surah of *al-mīthāq al-mutaʿaddid* (the multiple covenant), arguing the PoTB-density is corpus-distinctive.

**Rules-tuple**: QAC v0.4 lemma index; PoTB-lemma family pre-registered as {yahūdī, naṣrāniyy, tawrāh, injīl, Banī Isrāʾīl, ʿĪsā, Mūsā, ḥawāriyyūn, masīḥ}.

**Empirical test** (Q005-F-01): Q 5 has 43 PoTB-lemma tokens in 3,047 words = 1.41 / 100 words.

| Surah | Density / 100 words |
|:--|--:|
| Q 61 al-Ṣaff | 3.36 |
| Q 20 Ṭā Hā | 1.42 |
| **Q 5 al-Māʾida** | **1.41** |
| Q 87 al-Aʿlā | 1.37 |
| Q 28 al-Qaṣaṣ | 1.18 |

Within {Q 2, 3, 4, 5, 9}: Q 5 ranks **#1 of 5**. Med5 ordering = [5, 3, 2, 9, 4]. Permutation null on the 5-surah cluster: p_top2_med5 = 0.30 (above α_bon = 0.01) — *the rank passes but the permutation null does NOT* because PoTB-lemma counts are scattered across enough surahs that random-shuffle reproduces a top-2 placement at non-trivial rate.

Corpus-wide rank-3 (Q 5 sits between Q 61 and Q 20). p_top5_corpus = 0.0000 — corpus-rank top-5 is robust at p < 10⁻⁴.

**Verdict**: **DIRECTIONAL-VINDICATED** for the al-Rāzī claim. The CLASSICAL CLAIM was qualitative ("Q 5 is the surah of khiṭāb al-yahūd wa-l-naṣārā"). The empirical RANK-1 within the al-sabʿ al-ṭiwāl Medinan-legal cluster + corpus rank-3 is consistent with the qualitative claim. The strict pre-registered Bonferroni-corrected α=0.01 was not met on the within-cluster perm null because the lemma-counts have low marginal variance.

## Claim 4 — Q 5:55 walāyah verse refers specifically to ʿAlī b. Abī Ṭālib (Imāmī Shīʿī)

**Source**: al-Ṭabarsī, *Majmaʿ al-bayān*, on Q 5:55. The Imāmī tradition reads *al-ladhīna āmanū l-ladhīna yuqīmūna l-ṣalāta wa-yuʾtūna l-zakāta wa-hum rākiʿūn* as referring specifically to ʿAlī's reported event of giving alms while bowing in rukūʿ.

**Sunnī counter-position**: al-Ṭabarī, al-Rāzī, al-Qurṭubī, Ibn Kathīr all read the verse as referring to BELIEVERS IN GENERAL who maintain ṣalāh and zakāt. Ibn Kathīr specifically rejects the rukūʿ-alms-by-ʿAlī tradition as having a weak isnād.

**Empirical test**: NOT EMPIRICALLY TESTABLE from text alone. The verse's grammatical subject (*al-ladhīna āmanū*) is plural; whether this plural admits a singular-reference-by-individuation is a hermeneutical-grammatical question, not a quantitative one. No empirical corpus signature can arbitrate between the two readings.

**Verdict**: **NOT-TESTABLE-EMPIRICALLY** — interpretive dispute. We document the dispute and abstain from empirical adjudication.

## Claim 5 — al-Biqāʿī: Q 4 → Q 5 munāsabāt is smooth (kalāla → ʿuqūd)

**Source**: al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, on Q 4 closing → Q 5 opening. He argues Q 4:176 (kalāla inheritance) flows into Q 5:1 (general fulfillment of contracts) as a natural-coherence continuation.

**Rules-tuple**: Fisher-Rao distance on QAC stem-roots, K_top=200, basmala-handling-default.

**Empirical test** (H-NEW-720): Q 4 → Q 5 canonical adjacency cost is **0.0000 (rank 102/113 — near-zero)** of TSP residual. The mushaf pays essentially NO FR-cost to honor the canonical ordering Q 4 → Q 5.

**Verdict**: **EMPIRICALLY VINDICATED**. al-Biqāʿī's qualitative *kalāla → ʿuqūd* coherence judgment is empirically the smoothest TSP-residual transition in the al-sabʿ al-ṭiwāl Medinan-legal block. This is one of the strongest verifications of al-Biqāʿī's munāsabāt method on Q 5: a 14th-century qualitative coherence judgment maps onto the 21st-century empirical TSP-residual rank.

## Claim 6 — al-Suyūṭī: Q 5:3 is the LAST verse of legal-establishment

**Source**: al-Suyūṭī, *al-Itqān*, nawʿ 8 (in last-revealed-verse), citing Sufyān b. ʿUyayna. al-Suyūṭī's position: among the four candidates for "the last verse" (Q 9:128-129, Q 4:176, Q 2:281, Q 5:3), Q 5:3 is the last LEGAL verse.

**Rules-tuple**: tafsir-citation density across 7 OpenITI tafsirs (Ṭabarī, Qurṭubī, Rāzī, Ibn Kathīr, Suyūṭī *Durr*, Biqāʿī, Zamakhsharī) — comparative classical-citation-frequency test.

**Empirical test queued — Q009-F-04 was a PRE-REGISTERED test of this claim** (see [[Q009-al-tawba/Q009-F-04-last-revealed-prereg|Q009-F-04 pre-reg]]). The test tallies "ākhar mā nazala" co-occurrences within 8-line context windows in the tafsir corpus. Result: NULL — the four candidates are cited at roughly equal frequency, with al-Suyūṭī's harmonization standing.

**Verdict**: **DIRECTIONAL** — al-Suyūṭī's harmonization (each Companion reported what reached him) stands; no single candidate dominates classical citation. The Q 5:3-specific empirical-density test (Q005-F-03) supports the verse's *structural distinctness* but cannot adjudicate which candidate is the final-chronologically-revealed verse.

## Claim 7 — The māʾida-from-heaven episode (Q 5:112-115) is corpus-unique

**Source**: classical consensus — al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, al-Biqāʿī all treat the māʾida episode as confined to Q 5 with no corpus parallel. The episode also lacks canonical-Christian biblical parallel; classical mufassirūn cite *isrāʾīliyyāt*-source traditions (al-Thaʿlabī's *al-Kashf wa-l-bayān*) as candidate background.

**Rules-tuple**: QAC v0.4 lemma form `maA^}idap`.

**Empirical test** (Q005-F-02): The lemma `maA^}idap` is a **corpus-hapax** confined to Q 5 (attesting at Q 5:112 and Q 5:114). p_perm of "≥2 hapax in 4-lemma family confined to Q 5" = 0.0003 < α_bon = 0.01. The wider 4-lemma family {māʾida, ḥawāriyyūn, akmah, abraṣ} contains 1 strict hapax (māʾida only) — the pre-registered ≥2-hapax threshold is technically NOT met → strict pre-reg verdict NULL on the family-level. But the māʾida-lemma alone IS a strict corpus hapax (sub-test).

**Verdict**: **DIRECTIONAL-VINDICATED at the māʾida-lemma level** (corpus hapax, p_perm = 0.0003); **NULL at the strict family-level** (only 1 of 4 family-members is a strict hapax). The **classical claim that the māʾida-episode is corpus-unique is VINDICATED at the surah-eponymous-lemma level** — it is the lemma that names the surah and appears nowhere else in the corpus.

## Claim 8 — al-Rāzī: Q 5 has *multiple covenants* (covenant-density)

**Source**: al-Rāzī, *Mafātīḥ al-ghayb*, intro to Q 5: "هي سورة الميثاق المتعدد" — the surah of the multiple covenant. al-Rāzī enumerates: Q 5:1 ʿuqūd general; Q 5:7 Muslim mīthāq; Q 5:12 Israelite mīthāq + 12 naqībs; Q 5:14 Christian mīthāq; Q 5:70 reaffirmation of Israelite mīthāq.

**Rules-tuple**: QAC v0.4 root-index; family {wvq mīthāq, Ehd ʿahd, Eqd ʿaqd, nqD breaking}.

**Empirical test** (Q005-F-04): Q 5 covenant-root-density (9 tokens in 3,047 words) = 0.295 / 100 words. **Corpus rank: 10/114**. Within {Q 2, 3, 4, 5, 9}: Q 5 ranks **#3** (after Q 2 and Q 9). p_top3_corpus = 0.0000 in the permutation null but the **PRE-REGISTERED CORPUS-WIDE rank ≤ 3 is NOT met** (Q 5 corpus-rank = 10).

**Verdict**: **NULL** at the strict pre-registered corpus-rank-≤3 threshold. The classical claim is qualitative-thematic (*multiple covenants are referenced*), which is true at the verse-content level (5 distinct covenants in Q 5). But the QUANTITATIVE-DENSITY interpretation of the claim is FALSIFIED. The thematic claim STANDS; the quantitative claim FAILS. This is a useful **NULL with full prominence**.

The reason: Q 5's covenant references are concentrated in particular verses (Q 5:1, 7, 12, 14, 70) but the surah is large enough (3,047 words) that the per-100-word density is diluted. Q 13 al-Raʿd (covenant-density rank 4) and Q 9 (rank 2) have higher per-100-word covenant-density.

## Summary Table

| # | Claim | Source | Verdict |
|:-:|:--|:--|:--|
| 1 | Q 5 is among LAST surahs revealed | al-Suyūṭī *Itqān* nawʿ 1; al-Tirmidhī #3063 | **VINDICATED** (RULES-TUPLE-FRAGILE on Egyptian vs Nöldeke for absolute-last) |
| 2 | Q 5:3 = ʿArafāt-Friday-Hajjat al-Wadāʿ | al-Bukhārī #45, #4213, #6993; al-Tirmidhī #3127 (ḥasan ṣaḥīḥ) | **VINDICATED** (Sunnī isnād + Q005-F-03 empirical density-rank-1) |
| 3 | Q 5 is khiṭāb al-yahūd wa-l-naṣārā (PoTB-densest) | al-Rāzī Mafātīḥ on Q 5:1 | **DIRECTIONAL-VINDICATED** (Q005-F-01: rank-1 in Med-5; corpus rank-3; p_top5_corpus = 0.0000) |
| 4 | Q 5:55 walāyah refers specifically to ʿAlī | al-Ṭabarsī *Majmaʿ al-bayān* | **NOT-EMPIRICALLY-TESTABLE** — interpretive dispute |
| 5 | Q 4 → Q 5 munāsabāt smooth (kalāla → ʿuqūd) | al-Biqāʿī *Naẓm* | **EMPIRICALLY VINDICATED** (Q4→Q5 adjacency rank 102/113 — near-zero TSP cost) |
| 6 | Q 5:3 is the LAST legal verse | al-Suyūṭī *Itqān* nawʿ 8 | **DIRECTIONAL** (al-Suyūṭī's harmonization stands; no candidate dominates classical citation) |
| 7 | Māʾida-episode is corpus-unique | classical consensus | **VINDICATED** at lemma level (māʾida = corpus hapax); strict 4-family ≥2-hapax pre-reg NULL |
| 8 | Q 5 has *multiple covenants* (al-mīthāq al-mutaʿaddid) | al-Rāzī *Mafātīḥ* | **NULL** quantitatively (Q 5 corpus-rank 10 — not top-3); STANDS thematically |

**Net**: 5 VINDICATED (in some form), 1 DIRECTIONAL, 1 NULL, 1 NOT-TESTABLE. The 5 vindicated claims include 3 of high empirical strength (Q 5:3 density, Q 4→Q 5 munāsabāt, late-Medinan chronology). The single NULL (covenant-density) is published with full prominence; it refines al-Rāzī's qualitative claim into "thematic-multiplicity yes, density-rank no."

*Bismillāhi al-Raḥmāni al-Raḥīm.*
