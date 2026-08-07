---
surah: 113
surah_name_ar: الفلق
surah_name_translit: al-Falaq
surah_name_english: The Daybreak / The Dawn-Cleavage
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: SCAFFOLD-COMPLETE — Wave-D launch; 9-file template + journal; 4 pre-registered novel tests; 5 classical claims audited
---

# Q 113 al-Falaq — Overview


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
| Surah ID | 113 | canonical |
| Arabic name | الفلق | canonical |
| Transliteration | al-Falaq | canonical |
| English meaning | "The Daybreak / The Cleaving / The Dawn-rift" | classical |
| Verse count | 5 | `quran-no-tashkeel.json` Q113 (Hafs-Kufan) |
| Position in mushaf | 113 (penultimate) | canonical |
| Type | Meccan (majority) / Medinan (minority — linked to sorcery asbāb-al-nuzūl) | classical disagreement |
| Position in revelation order (al-Suyūṭī) | 20 (Egyptian standard); other chronologies vary | al-Suyūṭī, *al-Itqān* nawʿ 1; `data/revelation-order.csv` |
| Word count (no-tashkeel orthographic) | 23 | computed |
| Letter count (no-tashkeel, no spaces) | 73 | computed |
| Root-tokens (QAC v0.4) | 11 | `data/morphology/quranic-corpus-morphology-0.4.txt` Q113 |
| Distinct roots | 10 | qwl, Ew, rbb, flq, xlq, gsq, wqb, nfv, Eqd, Hsd |
| Bismala status | Standard | canonical |
| Predominant rāwī | د (40%, tied with ق 40%; ب 20%) | computed (verified §5) |
| Rhyme entropy (Shannon, nats) | **1.0549** | `h-new-750.json` per_surah surah=113 |

## 2. Classical names

- **al-Falaq** (الفلق) — "The Daybreak / The Cleavage" (canonical name; from v.1 *rabbi l-falaq*)
- **al-Muʿawwidha al-ūlā** (المعوذة الأولى) — "The First Refuge-Surah" (one of the muʿawwidhatān)
- **Sūrat al-Maʿūdhāt** (with Q 114) — paired classical name

The pair-name *muʿawwidhatān* (المعوذتان) refers to Q 113 + Q 114 together — the two surahs that begin *qul aʿūdhu*. al-Bukhārī, *Ṣaḥīḥ*, ḥadīth #4439 explicitly identifies the pair as the muʿawwidhatān recited by the Prophet during his final illness.

## 3. Opening formula

Q 113 opens with **qul aʿūdhu bi-rabbi l-falaq** ("Say, I take refuge in the Lord of the daybreak"). It is the first of the *muʿawwidhatān* (refuge-pair) and the first of the *aʿūdhu*-formulae in the corpus tail.

The *qul aʿūdhu bi-rabbi*-construction is corpus-rare; it appears only at:
- Q 113:1 *qul aʿūdhu bi-rabbi l-falaq*
- Q 114:1 *qul aʿūdhu bi-rabbi l-nās*

These are the only two attestations of the imperative-refuge construction in the entire 114-surah corpus. The construction is itself a structural marker of the muʿawwidhatān.

## 4. Length classification

Q 113 is in the **mufaṣṣal-qiṣār / muʿawwidhatān** zone. 5 verses, 73 letters — bottom-15 of corpus by letter-count.

## 5. Rhyme structure

Verified verse-final letters (computed from `quran-no-tashkeel.json`):

| Verse | Ends with | Final letter | Final cluster |
|:-:|:-:|:-:|:-:|
| 1 | الفلق | ق | -al-falaq |
| 2 | خلق | ق | -khalaq |
| 3 | وقب | ب | -waqab |
| 4 | العقد | د | -al-ʿuqad |
| 5 | حسد | د | -ḥasad |

**Distribution**: ق × 2 (40%), د × 2 (40%), ب × 1 (20%). Rhyme entropy = 1.0549 nats — **moderate-high diversity**.

This is one of the corpus's **mixed-rhyme short surahs**. The shift from ق (vv. 1-2) to ب (v.3) to د (vv. 4-5) follows the content-arc: cosmic-creation imagery (ق-ق) → twilight darkness (ب) → magic-and-envy (د-د).

The H-NEW-750 reports "top final letter: د (40%)" via tiebreak — but ق also has 40%. The surah is **bi-modal-rhyme** (ق + د tied) with a single ب.

## 6. Empirical architectural profile (headline)

| Metric | Value | Rank / 114 | Source |
|:--|:--:|:--:|:--|
| **UAS (Unified Architectural Score)** | **−0.2938** | **57 / 114** (mid-corpus) | `h-new-840.json` |
| Outlier-strength Δ%ile | 0.00 pp (NULL) | rank 45 / 114 | `h-new-590.json` |
| **iʿjāz signature sig_A** | **+1.8900** | **rank 7 / 114** (top decile, *iʿjāz al-fawāṣil*) | `h-new-750.json` |
| **iʿjāz signature sig_B** | **+3.2433** | **rank 2 / 114** | `h-new-750.json` |
| Mean FR distance to corpus | 0.7843 | rank 7 / 114 (FR-centroid top decile) | `h-new-111.json` |
| Q 112 → Q 113 adjacency cost | 0.0683 length-units (0.82%) | rank 52 / 113 | `h-new-720.json` |
| Q 113 → Q 114 adjacency cost | 0.0623 length-units (0.75%) | rank 56 / 113 | `h-new-720.json` |

**Architectural-cell classification**: Q 113 is in the ***iʿjāz-al-fawāṣil-pure*** cell of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2 — high sig_A (rank 7), moderate UAS (rank 57), moderate outlier — the classical *iʿjāz al-fawāṣil* exemplar in al-Bāqillānī's terminology. Cell members per cross-finding-026 §13.2: **Q 86, 89, 100, 106, 113**.

## 7. Verbatim text (canonical, no-tashkeel)

| Verse | Arabic | Transliteration | English (illustrative) |
|:-:|:--|:--|:--|
| 1 | قل أعوذ برب الفلق | *qul aʿūdhu bi-rabbi l-falaq* | "Say, I take refuge in the Lord of the daybreak" |
| 2 | من شر ما خلق | *min sharri mā khalaq* | "from the evil of what He has created" |
| 3 | ومن شر غاسق إذا وقب | *wa-min sharri ghāsiqin idhā waqab* | "and from the evil of darkness when it descends" |
| 4 | ومن شر النفاثات في العقد | *wa-min sharri l-naffāthāti fī l-ʿuqad* | "and from the evil of the women who blow on knots" |
| 5 | ومن شر حاسد إذا حasad | *wa-min sharri ḥāsidin idhā ḥasad* | "and from the evil of an envier when he envies" |

The 5 verses encode 1 refuge-formula (v.1) + 4 evil-typology entries (vv.2-5). See `02-content-analysis.md`.

## 8. The sorcery asbāb-al-nuzūl — preview

Multiple chains (al-Bukhārī ḥadīth #5763 *kitāb al-ṭibb b. al-siḥr*; #3268 *kitāb badʾ al-khalq b. ṣifat iblīs*; Muslim *kitāb al-salām*; Aḥmad *Musnad* multi-chain; al-Wāḥidī *Asbāb al-nuzūl*) report that the Prophet was bewitched by **Labīd ibn al-Aʿṣam** (a Jewish-clan sorcerer of Banū Zurayq), who tied 11 knots (*ʿuqad*) into a hair, with Q 113 + Q 114 revealed as the 11-verse refuge-cure (5 + 6 verses = 11 = the count of knots). When the Prophet recited each verse, one knot untied.

This is one of the most chain-attested asbāb traditions in the canonical corpus. See `04-hadith-corpus.md` and `05-classical-claims-audit.md` Claim 1 for chain analysis.

## 9. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 113 NULL outlier (rank 45).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 112-Q 113 mid; Q 113-Q 114 mid.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — Q 113 sig_A rank 7, sig_B rank 2.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 113 UAS rank 57.
- [[h-new-111-fisher-rao-distance|H-NEW-111]] — Q 113 FR-centroid rank 7 / 114.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2 — Q 113 = *iʿjāz-al-fawāṣil-pure* cell member.
- [[Q112-al-ikhlas/00-overview|Q 112 al-Ikhlāṣ]], [[Q114-al-nas/00-overview|Q 114 al-Nās]] — cluster siblings.
- [[muawwidhat-cluster-synthesis|muʿawwidhāt cluster synthesis]].

## 10. Investigation status

- [x] 00-overview.md (this file)
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md

*Bismillāhi al-Raḥmāni al-Raḥīm.*
