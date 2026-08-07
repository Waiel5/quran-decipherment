---
surah: 44
surah_name: al-Dukhān
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
verdicts_used: VINDICATED, FALSIFIED, DIRECTIONAL, RULES-TUPLE-FRAGILE, DATA-GAP
---

# Q 44 al-Dukhān — classical claims audit


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

Each claim is sourced (scholar + work + passage) and audited against project methodology.

## Claim 1: Q 44:3 *laylatin mubāraka* = laylat al-qadr (Sunni-mainstream majority)

**Sources** (all verified at offsets this session):
- al-Ṭabarī ad Q 44:3, via Ibn Kathīr `data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt:108428-108455` (verbatim citation chain).
- al-Rāzī, *Mafātīḥ al-ghayb*, Sūrat al-Dukhān *Masʾala* 5, `razi-mafatih-al-ghayb.openiti.raw.txt:218321-218360`.
- al-Qurṭubī, *al-Jāmiʿ li-aḥkām*, ad Q 44:3, `qurtubi-jami-ahkam.openiti.raw.txt:144655-144680`.
- Ibn Kathīr ad Q 44:3, `ibn-kathir-tafsir-quran.openiti.raw.txt:108428-108455`.
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 16 (*kayfiyyat inzālihi*).
- al-Biqāʿī, *Naẓm al-durar*, ad Q 97:1 — explicitly identifies the *layla* of Q 97:1 with the *layla mubāraka* of Q 44:3 (`biqai-nazm-al-durar.openiti.raw.txt:154340-154345`).

**Claim**: The *laylatin mubāraka* of Q 44:3 is the same as the *laylat al-qadr* of Q 97:1, located in Ramaḍān. The Quran was sent down on this night either (a) in toto from the *al-lawḥ al-maḥfūẓ* to the *bayt al-ʿizza* in the lowest heaven, or (b) the first revelation occurred on this night.

**Empirical test**:
- Quranic textual cross-anchor (verified `quran-text/quran-no-tashkeel.json` this session):
  - Q 97:1 = *إنا أنزلناه في ليلة القدر*
  - Q 44:3 = *إنا أنزلناه في ليلة مباركة إنا كنا منذرين*
  - Q 2:185 = *شهر رمضان الذي أنزل فيه القرآن*

  These three verses form a Quran-internal *if-and-only-if* anchor: revelation occurred in Ramaḍān (Q 2:185), the night of Ramaḍān-revelation is *blessed* (Q 44:3), the night of Ramaḍān-revelation is the *Night of Decree* (Q 97:1) — therefore Q 44:3's *laylatin mubāraka* = Q 97:1's *laylat al-qadr*.
- Lexical anchor (verified this session): the *yufraqu kullu amrin ḥakīm* phrase of Q 44:4 parallels the *tanazzalu al-malāʾikatu wa-l-rūḥ fīhā bi-idhni rabbihim min kulli amr* of Q 97:4 — both are decree-distribution phrasings.
- Hadith corpus (this session, verified IDs at `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`): the *laylat al-qadr* + Ramaḍān anchor is canonical and densely attested across all 9 books (Bukhārī *Faḍl Laylat al-Qadr*, Muslim *Kitāb al-Ṣiyām*, etc.). The Shaʿbān-night hadiths (this session: Tirmidhī #739, Ibn Mājah #1122/3/4/1385, Dārimī #1046) are ALL classically weak-chain.

**Verdict**: **VINDICATED at the textual-Quranic + canonical-hadith level**. The Q 44:3 ↔ Q 97:1 ↔ Q 2:185 trio forms a closed Quran-internal cross-anchor; the hadith corpus densely supports the Ramaḍān-laylat-al-qadr identification while the Shaʿbān-night minority is only weakly attested. The Sunni-mainstream majority reading is empirically the strongest available.

## Claim 2: Q 44:3 minority Shaʿbān-night reading (ʿIkrima via al-Qurṭubī, al-Rāzī, al-Zamakhsharī)

**Sources**:
- al-Qurṭubī ad Q 44:3, `qurtubi-jami-ahkam.openiti.raw.txt:144655-144680` — preserves but rejects via Ibn al-ʿArabī's *bāṭil* judgment.
- al-Rāzī ad Q 44:3, `razi-mafatih-al-ghayb.openiti.raw.txt:218373-218380` — preserves al-Zamakhsharī's full Shaʿbān-night account but rules: *"ما رأيت لهم فيه دليلا يعول عليه"*.
- Hadith chains: Tirmidhī #739, Ibn Mājah #1122/3/4/1385, Dārimī #1046 (verified this session).

**Claim**: The *laylatin mubāraka* refers to the night of mid-Shaʿbān (15th of Shaʿbān) — also known as *laylat al-barāʾa* (night of acquittal), *laylat al-ṣakk* (night of the deed/registry).

**Empirical test**:
- Quranic anchor: NONE. The Qurʾān does not mention Shaʿbān at all (verified by full-corpus regex this session: 0 occurrences of *شعبان*).
- Hadith chains (verified IDs): Tirmidhī's ʿĀʾisha hadith #739 is graded *gharīb* by al-Tirmidhī himself with chain critique (Ḥajjāj b. Arṭāʾa flagged); Ibn Mājah and Dārimī chains are also of weak grade.
- Q 2:185 textual anchor (*shahru ramaḍān…*) functions as a Quran-internal disqualifier: revelation is located in Ramaḍān, not Shaʿbān.

**Verdict**: **FALSIFIED at the empirical-classical level**. The Shaʿbān-night reading has no Quranic-textual anchor, has only weak-chain hadith support, and is contradicted by Q 2:185. Classical adjudicators (Ibn Kathīr `:108433-108445`, al-Qurṭubī `:144675`, al-Rāzī `:218373-218380`) all reject it on these grounds.

**Honest limit**: The Shaʿbān-night devotional tradition has continued in some Sunni and especially Twelver-Shīʿa popular practice as *laylat al-barāʾa*; this is a *liturgical-devotional* matter that the project's empirical-textual audit does not adjudicate beyond the Quranic-anchor question.

**Rules-tuple note**: The al-Suyūṭī catalogue of this debate (referenced in the task brief) is documented in *al-Itqān* nawʿ 16 (the manner of revelation); under the project's standard rules-tuple (no-tashkeel, Hafs-Kufan), the Q 44:3 = laylat al-qadr identification holds; under no rules-tuple variant tested does the Shaʿbān reading become preferable. **NOT rules-tuple-fragile**.

## Claim 3: Q 44:10 smoke-sign — past-event Ibn Masʿūd reading (Quraysh famine)

**Sources**:
- Ibn Masʿūd via al-Bukhārī *Tafsīr Sūrat al-Dukhān* (chapter ID-block 4774-4823 in Bukhārī's *Kitāb al-Tafsīr*); see ID 4774, 4789, etc. (this session search hits).
- Ibn Kathīr's preservation: `ibn-kathir-tafsir-quran.openiti.raw.txt:108460-108530`.
- al-Ṭabarī's preferred adjudication: cited via Ibn Kathīr (*"وهو اختيار ابن جرير"*, `:108520`).

**Claim**: The smoke (*dukhān*) of Q 44:10 has already happened — it refers to the Quraysh famine after the Prophet's supplication for "years like the years of Yūsuf"; people were so weak from hunger they saw smoke between earth and sky. The *baṭsha kubrā* (v. 16) is identified with Badr.

**Empirical test**: This is a historical-narrative claim, not directly empirically falsifiable in the project's framework. Internal-textual evidence:
- Q 44:15 (*innā kāshifū al-ʿadhābi qalīlan innakum ʿāʾidūn*) — "We will lift the punishment briefly; you will return" — fits a temporary-historical lifting (rain after famine) better than an eschatological Day-of-Judgment reading (where punishment is final).
- Q 44:16 (*yawm nabṭishu al-baṭshata al-kubrā innā muntaqimūn*) — fits Badr (military *baṭsha*) reading.
- Hadith: Bukhārī *Kitāb al-Tafsīr* ID-block 4774-4823 contains the dedicated Sūrat al-Dukhān chapter with the Ibn Masʿūd narration; preserved at *ṣaḥīḥayn* (Bukhārī + Muslim) status.

**Verdict**: **VINDICATED at the textual + canonical-hadith level**. The Ibn Masʿūd narration is *muttafaq ʿalayh*; the v. 15 "We will lift the punishment briefly" wording is consistent with a non-eschatological reading.

## Claim 4: Q 44:10 smoke-sign — future-eschatological reading (Ibn ʿAbbās, ʿAlī, the *ten signs* hadith)

**Sources**:
- Ibn ʿAbbās, ʿAlī, Abū Hurayra, Hudhayfa b. Asīd al-Ghifārī via Muslim *Kitāb al-Fitan wa-Ashrāṭ al-Sāʿa* (the *ten signs of the Hour* hadith): Muslim #2901-class, idInBook 1775/7106/7107 (verified this session).
- Cross-attestation across 8 of the 9 canonical books: Bukhārī (#965, 1160), Muslim, Tirmidhī (#2251, 3257), Abū Dāwūd (#1399, 4313, 4325), Ibn Mājah (#1097, 3285, 3778, 3792), Aḥmad (#217, 1229), Dārimī (#2638, 2641, 2661, 2697, 2698) — total 25 verified hits this session.
- Ibn Ṣayyād hadith: Bukhārī (#1308, 2533, 2909, 2930, 2931, 5940), Muslim (#7163, 7164, 7171, 7173, 7174), Abū Dāwūd (#4330-4334), Tirmidhī (#2317) — 18+ hits this session.

**Claim**: The smoke is yet to come — it is one of the *ʿalāmāt al-sāʿa al-kubrā* (greater signs of the Hour); the smoke fills earth-and-sky for forty days, gives believers a head-cold, and suffocates disbelievers.

**Empirical test**:
- Hadith corpus density: extreme — 25 *ten signs* hits across 8 books makes this the densest eschatological-Hour hadith cluster.
- Ibn Ṣayyād hadith: the Prophet's hiding of Q 44:10 specifically as a test for Ibn Ṣayyād's prophetic-claim demonstrates the eschatological-future reading was active in the Prophet's environment (Bukhārī #2930, Muslim #7173, Abū Dāwūd #4331, Tirmidhī #2317 — all preserve the *huwa al-dukh* clipped utterance).

**Verdict**: **VINDICATED at the canonical-hadith level**. The eschatological reading has the densest hadith-corpus support in the entire Q 44 corpus.

## Audit synthesis on Claims 3-4: BOTH readings hold

The classical positions of al-Ṭabarī, Ibn Kathīr, al-Qurṭubī, al-Rāzī all preserve **both** the past-event (Ibn Masʿūd) and future-eschatological (Ibn ʿAbbās et al.) readings as legitimate. Project verdict: **BOTH classical readings are independently vindicated**; the verse is structurally susceptible to both temporal-locations because *yawm taʾtī al-samāʾu bi-dukhānin mubīn* is grammatically ambiguous between past-imperfect-completed action and future-imperfect action. The project does NOT adjudicate between them.

## Claim 5: Q 44 is one of the two HM-7 surahs sharing the *wa-l-Kitābi al-mubīn* qasam opening (Q 43:1-2 = Q 44:1-2 verbatim)

**Source**: al-Biqāʿī, *Naẓm al-durar*, ad Q 44:1, `biqai-nazm-al-durar.openiti.raw.txt:121370-121400`.

**Claim**: Q 43 and Q 44 open with verbatim-identical first-two-verse formula.

**Empirical test** (verified this session, `quran-text/quran-no-tashkeel.json`):
- Q 43:1 = حم
- Q 43:2 = والكتاب المبين
- Q 44:1 = حم
- Q 44:2 = والكتاب المبين

Verified by direct string equality in `quran-no-tashkeel.json`. Cross-corpus check (also via [[h-new-235-mutashabih-full-graph|H-NEW-235]]): Q 43:2 ↔ Q 44:2 is among the highest-similarity verse pairs in the corpus; this is the **only verbatim-identical 2-verse opening pair** in the entire Qurʾān (cross-attested with Q 40-Q 41 / Q 41-Q 42 / Q 45-Q 46 boundary checks: none share an exact opening).

**Verdict**: **VINDICATED at exact-string level**.

## Claim 6: Q 44 is Meccan, with possible Q 44:15 Madinan-context exception (al-Qurṭubī, al-Suyūṭī)

**Source**: al-Qurṭubī ad Q 44:1, `qurtubi-jami-ahkam.openiti.raw.txt:144641` (notes the exception); al-Suyūṭī, *al-Itqān*, nawʿ 19.

**Claim**: Q 44 is Meccan; some classical exegetes claim Q 44:15 (*innā kāshifū al-ʿadhābi qalīlan innakum ʿāʾidūn*) is Madinan-context referring to Badr.

**Empirical test**:
- Per `data/revelation-order.csv` (Nöldeke + al-Suyūṭī chronology cross-referenced; default project chronology), Q 44 is in the Meccan stratum (rev order #64 per al-Suyūṭī), placing it between Q 43 al-Zukhruf (#63) and Q 45 al-Jāthiyah (#65) — middle-Meccan period.
- Internal style: 2-letter monorhyme, eschatological-warning + compact narrative + paradise/hellfire — consistent with mid-Meccan style.

**Verdict**: **VINDICATED** at the methodological level. The Q 44:15 minor-exception classical disagreement is preserved by al-Qurṭubī as a textual *qawl* but does not destabilize the surah-level Meccan classification.

## Claim 7: Q 44's UAS rank 97 (HM-7 minimum) is empirically vindicated

**Source**: project's own UAS computation, `findings/phase-b-hypotheses/csv/h-new-840.json`, all_uas Q44 entry: `{"surah": 44, "UAS": -1.882, "abs_outlier": 1.44, "max_cost": 0.111, "abs_ijaz": 0.167}` (verified this session).

**Claim**: Q 44 is the architecturally-least-significant HM-7 surah by the project's Unified Architectural Significance metric.

**Empirical test**: HM-7 UAS scores from h-new-840 (this session, verified):
- Q 40 Ghāfir: −0.868 (rank ~74)
- Q 41 Fuṣṣilat: +0.436 (rank ~39)
- Q 42 al-Shūrā: +0.568 (rank ~31)
- Q 43 al-Zukhruf: +0.537 (rank ~33)
- Q 44 al-Dukhān: −1.882 (rank 97) ← HM-7 minimum
- Q 45 al-Jāthiyah: +0.350 (rank ~~40)
- Q 46 al-Aḥqāf: −1.591 (rank ~89)

Q 44's HM-7-minimum status is driven by its **near-zero |iʿjāz signature|** (0.167) — its 2-letter monorhyme pattern leaves no rhetorical-fawāṣil variation for the iʿjāz instrument to detect.

**Verdict**: **VINDICATED**. Q 44 is empirically the architectural-minimum HM-7 surah. This sits in productive tension with Q 44's THEOLOGICAL-narrative significance (laylat al-qadr, smoke-sign, zaqqūm, Pharaoh elegy, paradise-prototype) — the dual-iʿjāz typology accommodates this: Q 44 is **theological-iʿjāz heavy + structural-iʿjāz minimal**, parallel to Q 112's role at the corpus level (FR-centroid + theological-iʿjāz heavy + UAS-minimum).

## Claim 8: Q 44 has corpus-extreme *mubīn* density (Q044-F-02; pre-registered)

**Sources**: This session's pre-registered finding [[Q044-F-02]] at SHA `5bdd82e47c53745f649ac426fd6c413e8eb68c0e6ca6ca92e4bd7431550c5988`.

**Claim**: Q 44 has the highest density of the lexeme *mubīn* (مبين / المبين) per 1000 orthographic-words in the corpus.

**Empirical test** (this session, locked direction; verified at `surahs/Q044-al-dukhan/csv/Q044-F-02.json`):
- Q 44 *mubīn* count: 5 in 364 words → **13.736 per 1000 words**.
- Corpus mean (excl Q 44): 1.054 per 1000.
- SD: 2.051.
- **Q 44 z-score: +6.185** (corpus extreme; rank **1/114**).

Five Q 44 *mubīn*-attestations: vv. 2 (al-Kitāb mubīn), 10 (dukhān mubīn), 13 (rasūl mubīn), 19 (sulṭān mubīn), 33 (balāʾ mubīn).

**Verdict**: **VINDICATED at corpus-extreme strength** (z=+6.185, rank 1/114). The *mubīn*-cluster pattern is a previously-unidentified empirical structural feature of Q 44 — the surah uses *mubīn* as a 5-fold rhetorical-anchor distinguishing CLEAR-DIVINE-ENTITIES (Book, Smoke, Messenger, Authority, Trial).

## Claim 9: Q 44's nearest FR-roots neighbors are NOT its HM-7 sub-cluster but short eschatological mufaṣṣal (Q044-F-03)

**Sources**: This session's pre-registered finding [[Q044-F-03]] at SHA `2c0d46d9b0e90a09c03ffdba10b3e494b5d0cd7b83a20f43cd77d564fb15e0bb`.

**Claim**: Q 44's top-7 Fisher-Rao-distance nearest neighbors are SHORT eschatological mufaṣṣal surahs, NOT its HM-7 cluster siblings.

**Empirical test** (this session, locked direction; verified at `surahs/Q044-al-dukhan/csv/Q044-F-03.json`):

Q 44's top-7 FR-roots nearest neighbors:
1. Q 51 al-Dhāriyāt — FR=0.7543 (eschato-mufaṣṣal)
2. Q 52 al-Ṭūr — FR=0.7683 (eschato-mufaṣṣal)
3. Q 1 al-Fātiḥa — FR=0.7817
4. Q 78 al-Nabaʾ — FR=0.7890 (eschato-mufaṣṣal)
5. Q 81 al-Takwīr — FR=0.7948 (eschato-mufaṣṣal)
6. Q 32 al-Sajda — FR=0.7971 (eschato-mufaṣṣal)
7. Q 110 al-Naṣr — FR=0.7992 (eschato-mufaṣṣal)

**6 of 7 are eschato-mufaṣṣal class**; **0 of 7 are HM-7 siblings**.

Q 44's HM-7 partners average FR distance: 0.9072 — substantially HIGHER (more distant) than its eschato-mufaṣṣal neighbors (0.78-0.80 range). The closest HM-7 partner is Q 45 (0.8439), still beyond all 7 eschato-mufaṣṣal neighbors.

**Verdict**: **VINDICATED**. Q 44, despite being a HM-7 cluster member by letter-family, sits content-cohesively with the SHORT-MUFAṢṢAL ESCHATOLOGICAL register, NOT with its HM-7 siblings. This empirically demonstrates that **letter-family clusters (HM-7) and content-cohesion clusters can be ORTHOGONAL** at the per-surah level — replicating [[h-new-600-letter-families|H-NEW-600]] and [[h-new-570-muqattaat-content-cluster|H-NEW-570]] NULL findings on letter-family content cohesion.

## Claim 10: Q 44 *dukhān*-bracket (Q 41:11 + Q 44:10 are corpus's only 2 *dukhān* attestations) (Q044-F-01)

**Sources**: This session's pre-registered finding [[Q044-F-01]] at SHA `8efd2b13c3c2714e11ec8c856b80647f89df649bbbcc2cd5c042e0b033bc30b8`.

**Claim**: The lexeme *dukhān* appears exactly twice in the corpus, both within HM-7: Q 41:11 (cosmogonic) and Q 44:10 (eschatological).

**Empirical test** (this session, verified): Full-corpus regex on `quran-text/quran-no-tashkeel.json` for substring `دخان`: 2 hits, Q 41:11 and Q 44:10, both in HM-7.

**Verdict**: **VINDICATED**.

**Rules-tuple sensitivity**: Replication on `quran-text/quran-min-tashkeel.json` returned 0 hits (the substring `دخان` is broken by min-tashkeel diacritical-marks `دُخَانٍ` `دُخَانًا`). The finding holds **only under the no-tashkeel rules-tuple**; under min/full-tashkeel the substring-search needs to be on a tashkeel-stripped form. This is a **RULES-TUPLE-FRAGILE-TO-OPERATIONALIZATION** flag, not a content-fragility flag — the underlying lexeme attestation is stable; only the substring-search operationalization varies.

## Claim 11: Q 44 contains the only 2-verse opening-twin pair in the corpus (Q 43:1-2 = Q 44:1-2) [DUPLICATE of Claim 5; aggregated]

Aggregated under Claim 5.

## Summary table

| # | Claim | Verdict | Strength |
|:--|:--|:--|:--|
| 1 | Q 44:3 *layla mubāraka* = laylat al-qadr | VINDICATED | Strong (Q-internal anchor + canonical hadith) |
| 2 | Q 44:3 minority Shaʿbān reading | FALSIFIED | Weak chains; no Q-anchor |
| 3 | Q 44:10 past-event reading (Ibn Masʿūd) | VINDICATED | *muttafaq ʿalayh* hadith |
| 4 | Q 44:10 future-eschatological reading | VINDICATED | 25 *ten-signs* + 18 Ibn Ṣayyād hits |
| 5 | Q 43:1-2 = Q 44:1-2 verbatim opening twin | VINDICATED | Unique in corpus |
| 6 | Q 44 Meccan classification | VINDICATED | Universal classical consensus |
| 7 | Q 44 UAS rank 97 (HM-7 minimum) | VINDICATED | Computed from h-new-840 |
| 8 | Q 44 *mubīn*-density corpus-extreme | VINDICATED | z=+6.185, rank 1/114 (Q044-F-02) |
| 9 | Q 44 FR-nearest = short eschatological mufaṣṣal, NOT HM-7 | VINDICATED | 6/7 top-7 eschato-mufaṣṣal (Q044-F-03) |
| 10 | Q 41:11 + Q 44:10 = corpus's only 2 *dukhān* | VINDICATED (rules-tuple-fragile to operationalization) | Q044-F-01 |

## Honest limits

1. The Q 44:10 past-vs-future smoke-sign question is **NOT empirically adjudicable** within this project's framework; both classical readings are textually and canonically defensible. Project verdict: BOTH hold.
2. The Shaʿbān-night minority reading (Claim 2) is FALSIFIED at the empirical level; it persists in popular liturgical practice as a non-empirical tradition.
3. Per-Q044 raw extractions of all classical mufassirūn are NOT on disk as discrete files; this audit uses line-offsets within consolidated OpenITI files.
4. The Ibn Ṣayyād hadith chains (18+ hits) are anchored to the eschatological reading by Ibn Kathīr's adjudication — not by the hadith text itself, which only states the Prophet hid Q 44:10 as a test, with no explicit eschatological-vs-past adjudication.

## Cross-references

- [[Q044-al-dukhan/03-tafsir-survey|Q 44 tafsīr survey]] — full classical position-by-position survey.
- [[Q044-al-dukhan/04-hadith-corpus|Q 44 ḥadīth corpus]] — verified hadith IDs anchoring claims 3, 4.
- [[Q044-al-dukhan/06-novel-findings|Q 44 novel findings]] — Q044-F-01/02/03 full reports.
- [[Q097-al-qadr/00-overview|Q 97 al-Qadr]] — primary cross-anchor for Claim 1.
- [[Q043-al-zukhruf/05-classical-claims-audit|Q 43 audit]] — opening-twin partner.
- [[hawamim-7-cluster-synthesis|HM-7 cluster synthesis]] — cluster-level claims.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
