---
surah: 46
surah_name: al-Aḥqāf
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
verdicts_used: VINDICATED, FALSIFIED, DIRECTIONAL, RULES-TUPLE-FRAGILE, NULL, DATA-GAP, NOT-EMPIRICALLY-TESTABLE
---

# Q 46 al-Aḥqāf — classical claims audit


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

Each claim is sourced (scholar + work + passage) and audited against project methodology. Rules-tuple, pre-registered direction, and Bonferroni discipline applied.

## Claim 1: Q 46 is named *al-Aḥqāf* after the geographic locus at Q 46:21 (al-Suyūṭī, *al-Itqān*, nawʿ 17)

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 17 (*asmāʾ al-suwar*) — `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`. Also al-Ṭabarī, al-Qurṭubī, Ibn Kathīr ad Q 46:21.

**Claim**: The surah's name *al-Aḥqāf* is derived from its single mention in the surah at v.21.

**Empirical test (this session)**: 
- Root ح-ق-ف (Hqf) attestations in the corpus: **1** (verified `data/morphology/root-index.json`: `"Hqf": [[46, 21, 7]]`).
- All attestations are in Q 46.
- The eponymous root is a **CORPUS HAPAX** (only attestation in the entire Qurʾān).

**Verdict**: **VINDICATED** at corpus-hapax strength. Q 46's name comes from its only-and-single internal attestation at v.21. This places Q 46 in the **hapax-eponym** sub-class of surah-naming.

## Claim 2: Q 46:15 + Q 31:14 establish the 6-month minimum gestation doctrine (al-Qurṭubī, al-Rāzī, ad loc.)

**Source**: al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, ad Q 46:15 (`data/literature/classical-tafsir/raw/qurtubi-jami-ahkam.openiti.raw.txt`); al-Rāzī, *Mafātīḥ al-ghayb*, ad Q 46:15. Hadith anchor: **Mālik *Muwaṭṭaʾ* #1625** (the ʿAlī-ʿUthmān adjudication, verified `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/malik.json`).

**Claim**: The arithmetic Q 46:15 (*thalāthūna shahran* = 30 months bearing+weaning) − Q 31:14 (*fiṣāluhu fī ʿāmayn* = 24 months weaning) = 6 months minimum gestation.

**Empirical test (textual)**:
- Q 46:15 verbatim (`quran-text/quran-no-tashkeel.json`): *وحمله وفصاله ثلاثون شهرا* — "his bearing-and-weaning is thirty months". ✓ verified.
- Q 31:14 verbatim (`quran-text/quran-no-tashkeel.json`): *وفصاله في عامين* — "and his weaning is in two years (24 months)". ✓ verified.
- Q 2:233 ratifies the two-year max-nursing: *والوالدات يرضعن أولادهن حولين كاملين* — "two complete years". ✓ verified.
- Arithmetic: 30 − 24 = 6. ✓ deterministic.
- Hadith anchor: Mālik #1625 cites Q 46:15 verbatim in the ʿAlī-ʿUthmān adjudication. ✓ verified.

**Verdict**: **VINDICATED** at deterministic-arithmetic + verbatim-hadith-citation strength. The doctrine is empirically grounded in the textual juxtaposition of three verses + canonical hadith citation. The medical-empirical claim that 6 months is biologically possible (modern: 22-24 weeks viability; classical: a minority case) is out-of-empirical-scope for this project.

## Claim 3: Q 46:17 *uffin lakumā* is NOT about ʿAbd al-Raḥmān b. Abī Bakr (ʿĀʾisha, via Bukhārī #4621)

**Source**: al-Bukhārī, *Ṣaḥīḥ*, idInBook 4621 (verified `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json`). Also al-Ṭabarī, al-Qurṭubī, Ibn Kathīr ad Q 46:17.

**Claim**: The Marwān-era political attribution of Q 46:17 to ʿAbd al-Raḥmān b. Abī Bakr is **rejected** by ʿĀʾisha herself.

**Empirical test**: 
- Bukhārī #4621 verbatim isnād (Mūsā b. Ismāʿīl ← Abū ʿAwāna ← Abū Bishr ← Yūsuf b. Māhak): Marwān cites Q 46:17, ʿĀʾisha rejects from behind the curtain. ✓ verified verbatim.
- Classical exegete consensus (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr ad Q 46:17): all follow ʿĀʾisha's rejection.
- al-Suyūṭī, *al-Itqān*, nawʿ 70 (*mubhamāt*): catalogs the verse among the unnamed-referent set.

**Verdict**: **VINDICATED** — the classical scholarly consensus is empirically grounded in Bukhārī #4621 (a *Ṣaḥīḥ* chain). The Marwān-political reading is FALSIFIED at the canonical-hadith level by ʿĀʾisha's direct testimony.

## Claim 4: Q 46:29-32 is the canonical Ibn ʿAbbās jinn-encounter narrative (Muslim #908)

**Source**: Muslim, *Ṣaḥīḥ*, idInBook 908 (verified `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json`). Also al-Qurṭubī ad Q 46:29.

**Claim**: Q 46:29-32 anchors the **Ibn ʿAbbās narration** (Prophet did not see the jinn) as DISTINCT from the **Ibn Masʿūd *layla al-jinn*** narration (Prophet recited TO the jinn, anchored at Q 72).

**Empirical test (this session)**:
- Muslim #908 (Ibn ʿAbbās via Saʿīd b. Jubayr): "**the Prophet did not recite to the jinn nor see them; he set off with a party of his Companions** (intending the market of ʿUkāẓ)…" ✓ verified.
- The verse Q 46:29 *idh ṣarafnā ilayka nafaran min al-jinni yastamiʿūna al-Qurʾān* (verified `quran-text/quran-no-tashkeel.json`) — the framing *ṣarafnā ilayka* ("We diverted to you") supports the Ibn ʿAbbās non-direct-encounter reading.
- al-Qurṭubī ad Q 46:29 catalogs both Ibn ʿAbbās and Ibn Masʿūd traditions; preserves them as **distinct events**.

**Verdict**: **VINDICATED** at explicit-canonical-hadith strength. Q 46:29-32 is anchored to the Ibn ʿAbbās narration (Muslim #908); Q 72 is anchored to the Ibn Masʿūd *layla al-jinn* narration (separate canonical hadiths). The classical taxonomy of two distinct jinn-encounters is preserved.

## Claim 5: Q 46:35 *ūlū al-ʿazm* identifies five prophets (Nūḥ, Ibrāhīm, Mūsā, ʿĪsā, Muḥammad) (al-Suyūṭī, *al-Itqān*, nawʿ 67)

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 67 (*fī al-anbiyāʾ wa-l-rusul*); al-Ṭabarī, al-Rāzī, Ibn Kathīr ad Q 46:35.

**Claim**: The phrase *ūlū al-ʿazm* in Q 46:35 identifies five top-tier prophets, cross-referenced with Q 33:7 + Q 42:13.

**Empirical test (this session)**:
- The phrase *ūlū al-ʿazm* (as a fixed multi-word expression) in `quran-text/quran-no-tashkeel.json`: **CORPUS HAPAX** (1 attestation, Q 46:35). ✓ verified by regex search.
- Q 33:7 verbatim: *وإذ أخذنا من النبيين ميثاقهم ومنك ومن نوح وإبراهيم وموسى وعيسى ابن مريم* — names exactly five (Muḥammad implicit by *minka*; Nūḥ, Ibrāhīm, Mūsā, ʿĪsā explicit). ✓ verified.
- Q 42:13 verbatim: *شرع لكم من الدين ما وصى به نوحا والذي أوحينا إليك وما وصينا به إبراهيم وموسى وعيسى* — same five (Muḥammad by *awḥaynā ilayka*; Nūḥ, Ibrāhīm, Mūsā, ʿĪsā explicit). ✓ verified.

**Verdict**: **VINDICATED** at corpus-hapax + cross-verse-triangulation strength. The phrase is a single attestation; the five-prophet identification is anchored by parallel covenant-verses (Q 33:7 + Q 42:13). The doctrine is the **single-verse exegetical anchor** for the entire *ūlū al-ʿazm* taxonomy.

**Honest limit**: Some classical traditions (al-Suyūṭī catalogs minorities) name 6 or expand. The five-prophet identification is the dominant Sunnī view but not unanimously locked.

## Claim 6: Q 46:10 witness from Banū Isrāʾīl is ʿAbdallāh b. Salām (multiple hadith chains)

**Source**: al-Ṭabarī ad Q 46:10; Ibn Kathīr ad loc.; Bukhārī #3191/3480/3649 + 12 more chains (verified densely in `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json`); Muslim, Tirmidhī, Ibn Mājah, Abū Dāwūd, Mālik, Dārimī parallel chains (61 total ʿAbdallāh-b.-Salām hits across 8 books).

**Claim**: The "witness from Banū Isrāʾīl" of Q 46:10 is ʿAbdallāh b. Salām.

**Empirical test**:
- 61 ʿAbdallāh-b.-Salām hadith citations across 8 of 9 canonical books (this session). The ʿAbdallāh-b.-Salām cluster is one of the most-cited Companion-clusters.
- BUT: classical exegetical disagreement persists. al-Shaʿbī, Masrūq (al-Ṭabarī ad Q 46:10): "the verse is Meccan; ʿAbdallāh b. Salām's conversion was Medinan; therefore the witness must be a different referent or generic."
- al-Zamakhsharī genericises: "any one of Banū Isrāʾīl who recognises the Qurʾān's prior-scripture-confirmation."
- al-Suyūṭī *al-Itqān* nawʿ 70 (*mubhamāt*): catalogs Q 46:10 among the un-named-referent verses.

**Verdict**: **DIRECTIONAL with classical-internal-dissent**. The ʿAbdallāh-b.-Salām attribution is the dominant exegetical view (Saʿd b. Abī Waqqāṣ chain at Bukhārī, multiply attested) but the chronology objection (al-Shaʿbī/Masrūq) is preserved by classical scholars. The *mubham* status survives at the rules-tuple level — the verse text itself does NOT name the witness.

## Claim 7: Q 46 → Q 47 is a HIGH canonical-adjacency-cost transition (per h-new-720)

**Source**: User-prompt assertion; project's [[h-new-720-canonical-adjacency-cost|H-NEW-720]] data file.

**Claim**: The Q 46 → Q 47 boundary represents a high-cost transition due to triple discontinuity (ḥawāmīm exit + Meccan→Medinan + name-class shift).

**Empirical test (this session)**:
- Q 46 → Q 47 δ-cost = **0.0873** (verified `h-new-720.json`).
- Rank: **42 / 113** (sorted by descending cost).
- Fraction of TSP residual: **1.05%**.
- Top-10 expensive: Q 1-Q 2 (7.5%), Q 32-Q 33 (4.4%), Q 33-Q 34 (4.0%), Q 9-Q 10 (3.7%), Q 24-Q 25 (3.5%), Q 22-Q 23 (3.1%), Q 42-Q 43 (2.8%), Q 56-Q 57 (2.7%), Q 12-Q 13 (2.6%), Q 7-Q 8 (2.6%).
- Q 46 → Q 47 at 1.05% is **3.5× cheaper than the median top-10**.

**Verdict**: **REFINED — not high, but moderate-upper-third (rank 42/113)**. The user-prompt characterisation is empirically softened. The boundary cost is **above-median** (the median rank is 57, so 42 is upper-third) but **NOT extreme**.

**Refinement**: The triple-discontinuity (HM exit + Meccan→Medinan + name-class shift) does NOT translate to a top-tier TSP cost. The Q 46 ↔ Q 47 FR-distance of 0.9905 IS high (pull from h-new-111), placing the surah pair in the FR-dissimilar half — but the canonical-adjacency cost (which measures the residual after 2-opt optimization) is moderate. The mushaf-canonical neighbor of Q 46 is FR-distant but not TSP-cost-extreme. **Pre-registered** as Q046-F-01 in [[06-novel-findings]].

## Claim 8: Q 46 is Meccan (al-Suyūṭī, *al-Itqān*, nawʿ 19)

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 19 (*al-makkī wa-l-madanī*).

**Claim**: Sūrat al-Aḥqāf is Meccan throughout, possibly excepting v.10 per a minority tradition.

**Empirical test**: 
- Per `data/revelation-order.csv` (Nöldeke + al-Suyūṭī chronology cross-referenced), Q 46 is Meccan, revelation-order rank 66 (late Meccan).
- The minority view exempting v.10 (the witness verse) is preserved by al-Shaʿbī/Masrūq tradition (al-Ṭabarī ad loc.); rejected by majority.
- Internal style (multi-block register; HM-B near-monorhyme; eschatological-narrative density) is consistent with late-Meccan style.

**Verdict**: **VINDICATED at the methodological-consensus level**.

## Claim 9: HM-7 cluster *al-Ḥawāmīm dībāj al-Qurʾān* (Ibn Masʿūd) — Q 46 contribution

**Source**: Ibn Masʿūd via Abū ʿUbayd, *Faḍāʾil al-Qurʾān*; cited in Ibn Kathīr, opening of Sūrat Ghāfir (`data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt`).

**Claim**: The seven ḥawāmīm surahs are the "brocade" of the Qurʾān — Q 46 is the closing member.

**Empirical test (cluster-level, inherited from [[Q040-ghafir/05-classical-claims-audit|Q 40 audit Claim 1]])**:
- HM-7 mean UAS = (Q40=−0.868 + Q41=+0.436 + Q42=+0.568 + Q43=+0.537 + Q44=−1.882 + Q45=+0.350 + Q46=−1.591) / 7 = **−0.350**.
- Corpus mean UAS = 0.0 by construction.
- HM-7 is **slightly below corpus mean** on UAS.
- Q 46's contribution: UAS rank 91/114 — pulls the cluster mean DOWN.

**Verdict**: **DIRECTIONAL at cluster level** — Q 46 is one of the two HM-7 members (with Q 44) in the bottom quartile by UAS. The *dībāj* designation is rhetorically supported by HM-7's internal cohesion (20%ile in [[h-new-570-muqattaat-content-cluster]]) but Q 46 specifically does NOT meet a UAS-extreme threshold. Q 46's role is the **HM-B closer** + **bookend** — not a standalone *dībāj* member.

## Claim 10: Q 46:15 *asbāb al-nuzūl* about Abū Bakr's mother (user-prompt suggestion)

**Source**: User-prompt suggestion. Verified-on-disk classical sources to be checked.

**Claim**: The asbāb al-nuzūl for Q 46:15 involves Abū Bakr's mother.

**Empirical test (this session)**:
- Search of 9-book hadith corpus: "Umm Rūmān" (= Abū Bakr's WIFE; ʿĀʾisha's MOTHER) appears in Q 46:17-context (Bukhārī #3249, etc.) NOT Q 46:15.
- Abū Bakr's MOTHER is **Umm al-Khayr Salmā bt. Ṣakhr** (per *sīra* tradition); search for this name returned no Q 46:15-anchored canonical hadith hits in this session.
- Classical asbāb-al-nuzūl per al-Wāḥidī: per-Q46:15 file NOT verified on disk this session — **DATA-GAP**.
- Ibn Kathīr ad Q 46:15 (consolidated raw file): mentions the *qaḍāʾ ʿAlī* (Mālik #1625) as the canonical anchor, not specifically Abū Bakr's mother.

**Verdict**: **DATA-GAP / partially-MISATTRIBUTED**. The user-prompt's "asbāb al-nuzūl about Abū Bakr's mother" appears to **conflate Q 46:15 with Q 46:17** — the latter is anchored to **Umm Rūmān** (ʿĀʾisha's mother, Abū Bakr's WIFE) via the Marwān-ʿĀʾisha exchange (Bukhārī #4621). The Q 46:15 anchor is the **ʿAlī-ʿUthmān 6-month-pregnancy adjudication** (Mālik #1625). Both are vindicated; the conflation is corrected.

## 11. Summary table

| Claim | Verdict | Strength |
|:--|:--|:--|
| 1. *al-Aḥqāf* eponymity (Q 46:21 hapax) | VINDICATED | Corpus-hapax (1/1) |
| 2. Q 46:15 + Q 31:14 → 6-month gestation | VINDICATED | Deterministic + Mālik #1625 verbatim |
| 3. Q 46:17 NOT ʿAbd al-Raḥmān (ʿĀʾisha) | VINDICATED | Bukhārī #4621 ṣaḥīḥ |
| 4. Q 46:29-32 = Ibn ʿAbbās jinn-narrative | VINDICATED | Muslim #908 verbatim |
| 5. Q 46:35 *ūlū al-ʿazm* = 5 prophets | VINDICATED | Corpus-hapax + Q 33:7 + Q 42:13 |
| 6. Q 46:10 witness = ʿAbdallāh b. Salām | DIRECTIONAL with classical dissent | 61 hits but mubham-status preserved |
| 7. Q 46→Q 47 HIGH adjacency-cost | REFINED (moderate-upper-third) | Rank 42/113 |
| 8. Q 46 Meccan classification | VINDICATED | Universal classical consensus |
| 9. *al-Ḥawāmīm dībāj* (Q 46 contribution) | DIRECTIONAL at cluster level | Q 46 pulls UAS DOWN |
| 10. Q 46:15 asbāb on Abū Bakr's mother | DATA-GAP / CONFLATION-CORRECTED | Likely Q 46:17 + Umm Rūmān |

## 12. Honest limits

1. The *al-Aḥqāf* corpus-hapax (Claim 1) is at extreme strength (1/1 attestation); the doctrine of name-derivation is empirically locked.
2. The 6-month gestation claim (Claim 2) is a **textual-arithmetic-jurisprudential** vindication; the medical-empirical correctness is out of scope.
3. The Q 46→Q 47 boundary (Claim 7) is the user-prompt's most empirically soft claim — refinement to "moderate-upper-third" is necessary.
4. The "Abū Bakr's mother" framing (Claim 10) appears to be a memory-conflation in the user-prompt — the actual canonical anchor links Q 46:17 (not Q 46:15) to Umm Rūmān.
5. Per-Q46 al-Wāḥidī asbāb extract not verified on disk this session — DATA-GAP for full verse-by-verse asbāb.
6. The Ibn Masʿūd *layla al-jinn* tradition's full disambiguation from the Q 46-anchored Ibn ʿAbbās tradition is partially deferred — both belong to canonical hadith and require careful per-record attribution.

## 13. Cross-references

- [[Q046-al-ahqaf/02-content-analysis|Q 46 content]] — verse-block details
- [[Q046-al-ahqaf/03-tafsir-survey|Q 46 tafsīr]] — classical positions
- [[Q046-al-ahqaf/04-hadith-corpus|Q 46 ḥadīth corpus]] — hadith verification
- [[Q040-ghafir/05-classical-claims-audit|Q 40 claims audit]] — HM-7 cluster claims
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — adjacency cost rank
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 91
- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]]

*Bismillāhi al-Raḥmāni al-Raḥīm.*
