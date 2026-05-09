---
surah: 111
surah_name_ar: المسد
surah_name_translit: al-Masad
surah_name_english: The Palm-Fibre / The Twisted Strands
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD-COMPLETE — Wave-H late-landing specialist; 9-file template; 4 pre-registered novel tests; 5 classical claims audited
---

# Q 111 al-Masad — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 111 | canonical |
| Arabic name | المسد | canonical |
| Transliteration | al-Masad | canonical |
| English meaning | "The Palm-Fibre / The Twisted Strands" (rope-fibre word from v.5) | classical |
| Verse count | 5 | `quran-no-tashkeel.json` Q111 (Hafs-Kufan) |
| Position in mushaf | 111 | canonical |
| Type | Meccan (early; mufaṣṣal-qiṣār) | al-Suyūṭī, *al-Itqān* nawʿ 1 |
| Position in revelation order (al-Suyūṭī Egyptian standard) | 6 — among the very earliest revelations | al-Suyūṭī, *al-Itqān*; `data/revelation-order.csv` |
| Word count (no-tashkeel orthographic) | 23 | computed from disk |
| Letter count (no-tashkeel, no spaces) | 81 | computed from disk |
| Root-tokens (QAC v0.4) | 15 | `data/morphology/quranic-corpus-morphology-0.4.txt` Q111 |
| Distinct roots | 15 | tbb, ydy, Abw, lhb, gny, Ean, mwl, ksb, Sly, nwr, mrA, Hml, HTb, jyd, Hbl, msd |
| Bismala status | Standard | canonical |
| Predominant rāwī | ب (80% — vv.1-4); ـد terminal (20% — v.5) | computed (verified §5) |
| Rhyme entropy (Shannon, nats) | **0.5004** | `h-new-750.json` per_surah surah=111 |

## 2. Classical names

- **al-Masad** (المسد) — "The Palm-Fibre" (canonical name; from v.5 *ḥablun min masad*).
- **al-Lahab** (اللهب) — "The Flame" (alternative classical name; from v.1, v.3 *abī lahabin*, *nāran dhāta lahab*). Both names are widely attested across the *Maṣāḥif* tradition (al-Suyūṭī, *al-Itqān* nawʿ 17 *fī asmāʾ al-suwar*; Ibn Kathīr's *muqaddima*).
- **Tabbat** (تبت) — "Perish" (a third classical name; from the surah's opening word, parallel to other *opening-word* names like *al-Insān* / *Hal atā* and *al-Ḥamd* for Q 1).

## 3. Opening formula

Q 111 opens with the perfect-tense imprecation **tabbat yadā abī lahabin wa-tabb** ("Perish the two hands of Abū Lahab — and may he himself perish"). Three structural facts about this opening:

1. **It is the only Quranic surah that opens with a curse-imprecation against a SPECIFIC NAMED CONTEMPORARY OPPONENT.** No other surah names a non-prophet contemporary individual as the recipient of divine condemnation. (See §8 corpus-uniqueness verdict.)
2. **The verb *tabba* (ROOT:tbb) is corpus-rare**: 4 attestations total (Q 11:101 *tatbīb*, Q 40:37 *tabāb*, Q 111:1 *tabbat* + *tabba*). Q 111 contains 2 of the 4 corpus attestations of this root.
3. **The opening uses the perfect tense as a prophetic-decree** — declaring the failure already accomplished — a rhetorical pattern al-Zamakhsharī treats as a divine *ʿuṭā*-decree (the perfect of certainty).

## 4. Length classification

Q 111 is in the **mufaṣṣal-qiṣār** zone. 5 verses, 81 letters — bottom-15 of corpus by letter-count. Within the muʿawwidhāt-tail neighborhood (Q 108-114), Q 111 sits at letter-count rank 5 of 7 (longer than Q 108, 110, 112; shorter than Q 109, 113, 114). Its 23 words match Q 113 exactly.

## 5. Rhyme structure

Verified verse-final letters (computed from `quran-no-tashkeel.json`):

| Verse | Final word | Final letter | Final cluster |
|:-:|:-:|:-:|:-:|
| 1 | وتب | ب | -tabb |
| 2 | كسب | ب | -kasab |
| 3 | لهب | ب | -lahab |
| 4 | الحطب | ب | -al-ḥaṭab |
| 5 | مسد | د | -masad |

**Distribution**: ب × 4 (80%), د × 1 (20%). Rhyme entropy = 0.5004 nats — **moderate concentration on a single rhyme** with a single final-verse shift. The ب → د shift at v.5 is structurally the same shape al-Bāqillānī catalogues as a *fāṣila*-cadence-shift signature (a final-verse rhyme-pivot that closes the surah on a distinct phonetic register; cf. Q 105 al-Fīl, Q 100 al-ʿĀdiyāt).

The 4-verse ب-block + 1-verse د-pivot creates a **terminal cadence-flip** that mirrors the surah's content arc: vv.1-4 catalogue the Abū Lahab + wife failure; v.5 closes with the visual-tableau (the rope around her neck). The rhyme shift coincides with the content shift from biographical curse to terminal image.

## 6. Empirical architectural profile (headline)

| Metric | Value | Rank / 114 | Source |
|:--|:--:|:--:|:--|
| **UAS (Unified Architectural Score)** | **−2.1882** | **105 / 114** (bottom decile) | `h-new-840.json` |
| Outlier-strength Δ%ile | 0.00 pp (NULL) | rank 0 (no contribution) | `h-new-590.json` |
| iʿjāz signature sig_A | +0.7764 | rank 41 / 114 (mid) | `h-new-750.json` |
| **iʿjāz signature sig_B** | **+1.7728** | **rank 11 / 114** (top decile) | `h-new-750.json` |
| Mean FR distance to corpus | 0.7954 | **rank 15 / 114** (top decile FR-centroid) | computed from `h-new-111.json` |
| Q 110 → Q 111 adjacency cost | 0.0170 length-units (0.21%) | rank 93 / 113 (cheap) | `h-new-720.json` |
| Q 111 → Q 112 adjacency cost | 0.0221 length-units (0.27%) | rank 89 / 113 (cheap) | `h-new-720.json` |

**Architectural-cell classification**: Q 111 is a **structurally-cheap mufaṣṣal-qiṣār member with a distinctive content-uniqueness signature**. UAS bottom-decile reflects: (a) zero outlier-contribution, (b) very low max-cost (cheap pair-ranks), (c) moderate iʿjāz-balāgha. The surah's distinctive architectural value is **content-specific (named-opponent-condemnation)** rather than UAS-ranked structural-iʿjāz — a key diagnostic for the *content-iʿjāz-pure* sub-cell.

## 7. Verbatim text (canonical, no-tashkeel)

| Verse | Arabic | Transliteration | English (illustrative) |
|:-:|:--|:--|:--|
| 1 | تبت يدا أبي لهب وتب | *tabbat yadā abī lahabin wa-tabb* | "Perish the two hands of Abū Lahab — and may he himself perish" |
| 2 | ما أغنى عنه ماله وما كسب | *mā aghnā ʿanhu māluhu wa-mā kasab* | "His wealth has not availed him, nor what he has earned" |
| 3 | سيصلى نارا ذات لهب | *sa-yaṣlā nāran dhāta lahab* | "He will burn in a Fire of flame" |
| 4 | وامرأته حمالة الحطب | *wa-mraʾatuhu ḥammālata l-ḥaṭab* | "And his wife — the carrier of firewood" |
| 5 | في جيدها حبل من مسد | *fī jīdihā ḥablun min masad* | "Around her neck a rope of palm-fibre" |

The 5 verses encode 1 imprecation (v.1) + 1 wealth-failure declaration (v.2) + 1 future-tense damnation (v.3) + 2 wife-tableau verses (vv.4-5). See `02-content-analysis.md`.

## 8. Corpus-uniqueness — preview

Q 111 is empirically the corpus's **ONLY** surah that opens with — and is structurally devoted to — the **condemnation of a SPECIFIC NAMED CONTEMPORARY OPPONENT**. The corpus contains 107 distinct PN-tagged proper-name lemmas in the QAC morphology (`data/morphology/quranic-corpus-morphology-0.4.txt`); contemporary (Muhammadan-era) individuals named via PN-tag are exactly 3:

- *muḥammad* (Muhammad himself; 4 attestations in praise/identification context)
- *aḥmad* (the prophesied future name; Q 61:6, single attestation)
- *zayd* (Zayd ibn Ḥāritha, the Prophet's freedman + adopted son; Q 33:37, single attestation, in a positive-marriage context)

**None of these 3 are condemnations.** Q 111's *abī lahabin* is named via the kunya-construction *abī* (father, ROOT:Abw) + *lahab* (flame, ROOT:lhb) — i.e., via his cognomen rather than via a single-lemma PN-tag — but the referent is unambiguously the historical individual ʿAbd al-ʿUzzā ibn ʿAbd al-Muṭṭalib (Abū Lahab), the Prophet's paternal uncle and most-prominent early-Meccan opponent. See `05-classical-claims-audit.md` Claim 1 for the full corpus-uniqueness argument.

The asbāb-al-nuzūl tradition (al-Bukhārī ḥadīth #4564, #4595, #4767, #1348, #4767; Muslim *kitāb al-īmān* #7691; al-Tirmidhī *Tafsīr* #29227) consistently anchors the surah to the **Mt. Ṣafā public-warning incident** — when the Prophet ascended Mt. Ṣafā after the revelation of Q 26:214 (*wa-andhir ʿashīrataka l-aqrabīn*) and called the Quraysh tribes to listen, Abū Lahab interrupted with *tabban laka, sāʾira l-yawmi! a-li-hādhā jamaʿtanā?* ("May you perish all the day! Is it for this that you gathered us?") — and Q 111 was revealed in direct response. See `04-hadith-corpus.md` for full chain analysis.

## 9. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 111 NULL outlier (0.00 pp Δ%, classification NULL).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 110→Q 111 rank 93 cheap; Q 111→Q 112 rank 89 cheap; both are structurally near-free placements.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — Q 111 sig_A rank 41, **sig_B rank 11 / 114** (top decile).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 111 UAS rank 105 (bottom decile).
- [[h-new-111-fisher-rao-distance|H-NEW-111]] — Q 111 FR-centroid rank 15 / 114; nearest = Q 108 al-Kawthar (0.2324).
- [[h-new-1240-13-seamless-seams|H-NEW-1240]] — Q 110→Q 111 and Q 111→Q 112 are NOT among the 13 seamless seams (both have positive delta; structurally cheap but not zero-cost).
- [[Q108-al-kawthar/00-overview|Q 108 al-Kawthar]] — Q 111's #1 FR-nearest neighbor (0.2324).
- [[Q112-al-ikhlas/00-overview|Q 112 al-Ikhlāṣ]] — successor; al-Biqāʿī treats Q 111→Q 112 as transition from creature-failure to creator-success (Q 112 cluster sibling).
- [[Q026-al-shuara/00-overview|Q 26 al-Shuʿarāʾ]] — Q 26:214 *wa-andhir ʿashīrataka l-aqrabīn* is the trigger-verse for the Mt. Ṣafā incident that occasions Q 111.

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
