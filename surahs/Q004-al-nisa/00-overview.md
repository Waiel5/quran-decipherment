---
surah: 4
surah_name_ar: النساء
surah_name_translit: al-Nisāʾ
surah_name_english: "The Women"
file_type: overview
date_last_updated: 2026-05-29
phase: B+
verdict: 1 pre-registered 3-arm test landed — Arm A CONFIRMED (lone alif-rhyme ṭiwāl) + Arm B CONFIRMED (structural-iʿjāz minimum) + Arm C NULL (not a length-stratified rhyme extreme)
---

# Q 4 al-Nisāʾ — Overview


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

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 4 | canonical |
| Arabic name | النساء | canonical ("the women"; from the family/inheritance/women's-rulings content) |
| Transliteration | al-Nisāʾ | canonical |
| English meaning | "The Women" | classical |
| Verse count | 176 | Hafs-Kūfan (`data/hafs-verse-counts.tsv` line 4); al-Bukhārī #4174 ("last verse revealed = end of al-Nisāʾ, the kalāla") |
| Position in mushaf | 4 | canonical |
| Revelation order | #92 (Tanzil Egyptian Standard); Nöldeke #100 | `data/revelation-order.csv` |
| Type | Medinan (مدنية) | al-Qurṭubī ("the sound view"; ʿĀʾisha: "al-Nisāʾ was revealed while I was with the Prophet" — Bukhārī) |
| Word count (no-tashkeel, marks stripped) | 3,763 | computed (`scripts/Q004_F_06_alif_monorhyme.py` pipeline) |
| Letter count (no-tashkeel) | 16,332 | computed |
| Distinct QAC roots | 462 (2,462 root-tokens) | `data/morphology/root-index.json` |
| Opening | يا أيها الناس اتقوا ربكم — "O mankind, fear your Lord" | *yā-ayyuhā al-nās* universal vocative |
| Predominant rhyme (rāwī) | **ا (alif), 96.0% (169/176 verses)** | `h-new-700.json` rhyme_letter_diagnostics |
| Length class | al-sabʿ al-ṭiwāl ("the seven long ones") | al-Suyūṭī *al-Itqān* |

## 2. Why Q 4 matters for the project

1. **The lone alif-rhyme among the seven long surahs.** Of *al-sabʿ al-ṭiwāl* {Q2,Q3,Q4,Q5,Q6,Q7,Q9}, Q 4 is
   the **ONLY** surah whose dominant verse-ending letter is **alif** (ا) at **96.0%** — the other six are all
   nūn (ن) (Q004-F-06 Arm A, CONFIRMED). The long-Medinan fāṣila is overwhelmingly the *-ūn/-īn* nominal/verbal
   nūn; al-Nisāʾ is the conspicuous exception, holding a near-monorhyme alif across 176 verses.

2. **A structural-iʿjāz (fawāṣil-variety) minimum.** Because the near-monorhyme suppresses verse-ending variety,
   Q 4's al-Bāqillānī *iʿjāz al-fawāṣil* signature sig_A is **−3.1463, rank 113/114** (second-lowest in the
   corpus), with rhyme entropy **0.1989 nats** (z = −1.03, far below average) (Q004-F-06 Arm B, CONFIRMED).
   On the fawāṣil-variety axis al-Nisāʾ is near the corpus floor — its inimitability, if any, is NOT in
   verse-ending variety.

3. **An honest NULL on length-stratified rhyme-extremeness.** Q004-F-06 Arm C is a **NULL**: against a
   length-stratified null (surahs with ≥100 verses), Q 4's 96.0% concentration is NOT in the top 5%
   (p_perm = 0.17838) — three longer-or-comparable surahs exceed it: Q 17 (99.1%), Q 18 (99.1%), Q 23 (96.6%).
   The alif-monorhyme is **notable but not a length-stratified extreme**. This failure mode was
   PRE-COMMITTED in the pre-reg (Q17/Q18/Q23 named in advance), so Arm C is an honest pre-registered NULL,
   not a post-hoc retreat.

4. **The last-revealed verse (the kalāla).** Bukhārī #4174 / #4448 (al-Barāʾ): the last complete surah revealed
   was Barāʾa (Q 9), and the last *verse* revealed was the end of al-Nisāʾ — *yastaftūnaka qul Allāhu yuftīkum
   fī al-kalāla* (Q 4:176). Q 4 thus carries the chronologically final verse of the Qurʾān.

5. **The inheritance-law locus (farāʾiḍ).** Q 4:11-12, 176 are the Qurʾān's primary inheritance verses — the
   foundation of the entire *ʿilm al-farāʾiḍ*. Their occasion (the daughters of Saʿd b. al-Rabīʿ) is verified
   in Tirmidhī #2159 (**ḥasan ṣaḥīḥ**) and Abū Dāwūd #2892.

6. **FR-nearest to the al-ṭiwāl head.** Q 4's nearest Fisher-Rao neighbours are Q 2 (0.755), Q 5 (0.778),
   Q 3 (0.793) — it sits inside the long-Medinan-legal cluster. The Q 3→Q 4 and Q 4→Q 5 seams are both
   seamless (ranks 4/113 and 2/113), making Q 4 a doubly-seamless interior member of the al-ṭiwāl head.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 1.1375 (well above corpus mean 0.9235) | `h-new-111.json` (Q4 row) |
| Nearest FR neighbour | Q 2 al-Baqara (0.755) | `h-new-111.json` |
| Top FR neighbours | Q 2 (0.755), Q 5 (0.778), Q 3 (0.793), Q 33 (0.837), Q 9 (0.842) | `h-new-111.json` |
| Q 3 → Q 4 seam | delta_raw = −0.04662, rank 4/113 (**seamless**) | `h-new-720.json` |
| Q 4 → Q 5 seam | delta_raw = −0.06571, rank 2/113 (**seamless**) | `h-new-720.json` |
| H-NEW-590 | delta_pct = +1.08, **WEAK_OUTLIER** | `h-new-590.json` |
| H-NEW-700 rhyme | **ا (alif), 96.0%** (169/176) | `h-new-700.json` |
| H-NEW-750 sig_A | **−3.1463 (rank 113/114)** | `h-new-750.json` |
| H-NEW-750 sig_B | −1.4630 (rank 100/114) | `h-new-750.json` |
| H-NEW-750 rhyme entropy | 0.1989 nats (z −1.034) | `h-new-750.json` |
| H-NEW-840 UAS | +0.8778 (rank 26/114) | `h-new-840.json` |

## 4. Surface structure (major blocks)

| Block | Verses | Function |
|---|---|---|
| Universal vocative + the single-soul creation; orphans' property | 1-2 | *yā-ayyuhā al-nās*; family foundation |
| Polygamy/justice + orphan-marriage ruling; dowries | 3-6 | family law |
| **Inheritance shares (farāʾiḍ)** | 7-14 | the primary *mawārīth* verses (Q 4:11-12) |
| Indecency rulings; marriage prohibitions (the forbidden degrees) | 15-28 | family/marriage law |
| Property justice; the men/women maintenance verse (4:34) | 29-42 | social-legal |
| Ritual purity; the People-of-the-Book + hypocrite polemic | 43-91 | legal + polemic |
| Homicide expiation; the *qaṣr* (shortened prayer) in war; the hypocrites | 92-104 | legal + battlefield |
| Defence of the wronged; the Banū Ubayriq affair; munāfiqūn | 105-126 | legal-narrative |
| Reconciliation between spouses; justice; the People of the Book | 127-159 | family + polemic |
| ʿĪsā polemic (he was not crucified, v 157); the People of the Book | 157-162 | creedal-polemic |
| The prophets' chain; the closing kalāla inheritance verse (v 176) | 163-176 | creed + the last-revealed farāʾiḍ verse |

## 5. Pre-registered novel finding (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q004-F-06 Arm A | **CONFIRMED** | Q 4 is the unique alif-rhyme surah (96.0%) in al-sabʿ al-ṭiwāl; the other six are all nūn |
| Q004-F-06 Arm B | **CONFIRMED** | Q 4's structural-iʿjāz sig_A is rank 113/114 (second-lowest), rhyme entropy 0.199 nats (z −1.03) — a fawāṣil-variety minimum |
| Q004-F-06 Arm C | **NULL** | Q 4's 96.0% rhyme concentration is NOT a length-stratified extreme (p=0.178); Q 17, Q 18, Q 23 exceed it (pre-committed honest-limit fired) |

## 6. Cross-references

- **Q 3 Āl ʿImrān** — Q 3→Q 4 seamless seam (rank 4/113); the family/creed surah leads into the family-law
  surah (al-Rāzī / al-Biqāʿī munāsaba); FR rank 3 neighbour.
- **Q 5 al-Māʾida** — Q 4→Q 5 seamless seam (rank 2/113); FR-nearest after Q 2; the legal-Medinan continuation.
- **Q 9 al-Tawba** — Bukhārī #4174: last *complete* surah = Q 9; last *verse* = Q 4:176 (kalāla). The two
  bracket the chronological end of revelation.
- **H-NEW-720** — Q 3→Q 4 and Q 4→Q 5 both seamless; Q 4 is a doubly-seamless interior al-ṭiwāl member.
- **H-NEW-700 / -750** — the alif-monorhyme and the sig_A floor.

## 7. Classical-tradition status (see `03-tafsir-survey.md`, `05-classical-claims-audit.md`)

- al-Qurṭubī (*al-Jāmiʿ li-aḥkām*): Medinan ("the sound view"), citing ʿĀʾisha (Bukhārī) that al-Nisāʾ was
  revealed in her time with the Prophet (i.e. in Medina); rejects the "every *yā-ayyuhā al-nās* is Meccan"
  rule by the Q 2 counterexample; v 3 polygamy under 14 masāʾil (the orphan-girl occasion, Muslim/ʿĀʾisha).
- al-Ṭabarī (*Jāmiʿ al-bayān*): the farāʾiḍ of v 11 (*yūṣīkum Allāhu fī awlādikum li-l-dhakari mithlu ḥaẓẓi
  al-unthayayn*) as a divine bequest-command binding on all heirs.
- al-Zamakhsharī (*al-Kashshāf*): the surah's legal density; the grammatical treatment of the inheritance
  fractions.
- al-Rāzī / al-Biqāʿī: the Q 3→Q 4 munāsaba (the family of ʿImrān → the law of the family).
- al-Bāqillānī (iʿjāz al-fawāṣil): Q 4 sig_A rank 113/114 — al-Nisāʾ is a fawāṣil-variety MINIMUM (the
  near-monorhyme alif), confirming that its iʿjāz is not on the verse-ending-variety axis.

## 8. Open questions / queued tests

- Q004-F-02 (queued): is Q 4 the corpus's densest single surah for legal-ruling root-tokens (*w-r-th*
  inheritance, *n-k-ḥ* marriage, *w-ṣ-y* bequest, *ṭ-l-q* divorce)?
- Q004-F-03 (queued): the *yā-ayyuhā alladhīna āmanū* believer-vocative count in Q 4 vs the corpus density
  (Q 4 carries many) — is al-Nisāʾ in the believer-vocative top tier?
- Q004-F-04 (queued): the last-revealed-verse claim — does Q 4:176 (kalāla) sit at a measurable
  revelation-order / content boundary relative to Q 9?

---

*Investigation: Wave (2026-05-29) Q 4 al-Nisāʾ full 8-file deep-dive. See JOURNAL.md for the method log;
06-novel-findings.md for Q004-F-06 detail; 04-hadith-corpus.md for verified farāʾiḍ + last-verse + polygamy chains.*
