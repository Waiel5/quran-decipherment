---
surah: 42
surah_name: al-Shūrā
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: HM-A multi-rāwī apex; UAS=31 (top-quartile); ONLY two-verse muqaṭṭaʿāt opening in the Qurʾān; max rhyme entropy in HM-7
---

# Q 42 — Sūrat al-Shūrā (Consultation)


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

## 1. Identifiers

| Field | Value |
|:--|:--|
| Surah # | 42 |
| Arabic name | الشورى |
| Transliteration | al-Shūrā |
| English | "Consultation" |
| Verses (Hafs-Kufan) | 53 |
| Words (no-tashkeel) | 932 |
| Type | Meccan |
| Position in mushaf | 42 (HM-A close; HM-7 internal pivot) |
| Position in revelation order | 62 (al-Suyūṭī chronology) |
| Opening formula | حم (verse 1) + **عسق (verse 2 — separate)** |
| Length class | mufaṣṣal-ṭiwāl (53 verses) |

Verse and word counts computed from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (this session).

## 2. The unique two-verse muqaṭṭaʿāt — *the only such case in the Qurʾān*

Q 42 is **the only surah** in the Qurʾān where the muqaṭṭaʿāt are split across **two separate verses**:
- Q 42:1 — حم
- Q 42:2 — عسق

All other muqaṭṭaʿāt are within a single āya (Q 2:1 الم; Q 7:1 المص; Q 13:1 المر; etc.). This makes Q 42's opening **structurally unique**.

Verified directly from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`:
- v. 1 text: حم
- v. 2 text: عسق
- v. 3 text: كذلك يوحي إليك وإلى الذين من قبلك الله العزيز الحكيم

Classical commentary (Ibn Kathīr ad Q 42, opening; al-Ṭabarī ad loc.; al-Rāzī, *Mafātīḥ al-ghayb* on حم عسق) preserves Ibn ʿAbbās's response to Companion-questioning of the meaning: he refused to interpret three times (according to Ḥudhayfa's account) — exemplifying the *Allāh aʿlam* epistemic-humility position. Then Ḥudhayfa offered an interpretation tying ʿ-S-Q to a future eschatological event (an *Abd al-Ilāh* on a Mashriqī river — strikingly weak isnād, classified by al-Ṭabarī as *gharīb ʿajīb munkar*). Ibn ʿAbbās gave a different reading: ḥā = name of God, ʿayn = ʿāyana al-mawlawn ʿadhāb yawm Badr (witnessed Badr punishment), sīn = sa-yaʿlam alladhīna ẓalamū…, qāf = qāriʿa min al-samāʾ (with Abū Dharr's supplement). Source: extracted from `data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt` (offset 7206698, this session).

## 3. Position in HM-7 cluster — the *bifurcation pivot*

Q 42 is the **last surah of HM-A** {Q 40, 41, 42} and the surah immediately preceding the HM-A → HM-B transition. Empirically:
- **MAX rhyme entropy in HM-7**: 2.565 bits (this session, computed) / 1.78 bits (h-new-700 reduced rāwī, brief).
- **The only HM-7 surah with non-ن rāwī majority**: top rāwī is **ر** at 38% (20/53 verses), م at 21% (11/53), then ن at 11%. All other HM-7 surahs are ن-dominant (38%-88%).
- UAS rank 31 / 114 (HM-7 quartile-leader after Q 41).

The HM-7 bifurcation between HM-A (high-entropy multi-rāwī, including a **ر**-shifted Q 42) and HM-B (low-entropy near-monorhyme **ن**) is **sharpest at Q 42 → Q 43**: Q 42 (entropy 2.57, top-rāwī ر, distinct=9) → Q 43 (entropy 0.59, top-rāwī ن at 88%, distinct=3) is the largest one-step entropy drop within the cluster.

## 4. Distinctive features

### 4.1 Q 42:38 — the *consultation principle*
*…wa-amruhum shūrā baynahum* — "and their affair is by consultation among them" (Q 42:38). The surah's namesake. This is one of the **constitutional verses** of Sunni Islamic political theory. al-Ṭabarī (ad loc.) and al-Qurṭubī (*al-Jāmiʿ li-aḥkām al-Qurʾān*, ad loc.) both treat it as a positive injunction; al-Qurṭubī cites the Companion-precedent of the *shūrā* of the six (ʿUmar's consultation council).

### 4.2 Q 42:11 — *laysa ka-mithlihi shayʾ*
*Laysa ka-mithlihi shayʾun wa-huwa al-samīʿu al-baṣīr* — "There is nothing like Him; He is the Hearing, the Seeing". This is the **central tanzīh verse** of Sunni theology, foundational for al-Ashʿarī's and al-Māturīdī's via-negativa formulation of divine attributes. Cited by al-Bāqillānī (*al-Tamhīd*) and al-Ghazālī (*Iḥyāʾ*, *al-Iqtiṣād fī al-iʿtiqād*) as the proof-text against anthropomorphism.

### 4.3 Q 42:23 — *al-mawadda fī al-qurbā*
*…illā al-mawaddata fī al-qurbā* — "except love for the kindred". Sectarian-hermeneutic flashpoint: Sunni exegesis (Ibn Kathīr ad loc.) reads "the kindred" generally; Shīʿī exegesis (al-Ṭabarsī, *Majmaʿ al-bayān*; al-Qummī) reads "kindred of the Prophet" (i.e., Ahl al-Bayt). The verse is **the most-cited Shīʿī Qurʾānic anchor for waliya** along with Q 5:55.

### 4.4 The continuum-of-revelation passage (Q 42:13)
*Sharaʿa lakum min al-dīn mā waṣṣā bihi Nūḥan…* — "He has prescribed for you of the religion what He enjoined upon Nūḥ…" — listing Nūḥ, Ibrāhīm, Mūsā, ʿĪsā as recipients of the same dīn. This is one of the **earliest pluralist-prophetology verses** in the Meccan corpus.

## 5. Empirical fingerprint (cross-reference)

| Metric | Value | Source |
|:--|:--|:--|
| UAS rank | 31 / 114 | h-new-840 |
| UAS score | +0.568 | h-new-840 |
| Outlier-strength Δ%ile | +0.37 (near-zero) | h-new-590 |
| iʿjāz signature sig_A | **+1.27 (highest of HM-7)** | brief, h-new-750 |
| Top rāwī | **ر (38%) — only non-ن in HM-7** | this session |
| Rhyme entropy (this session) | **2.565 bits — max for HM-7** | computed |
| Rhyme entropy (h-new-700 reduced) | 1.78 bits — max for HM-7 | brief |
| Q42 rank by entropy among muqaṭṭaʿāt-29 | **2 / 29** (after Q 14 Ibrāhīm) | computed (HMM-F-04) |

**HMM-F-04 verdict (this session)**: Q 42 is rank 2 of 29 in muqaṭṭaʿāt-opened-surah rhyme entropy — a near-corpus-extreme multi-rāwī signature within the muqaṭṭaʿāt family.

## 6. Why is Q 42 multi-rāwī? (Hypothesis)

Three converging factors in classical-balagha terms:
1. **Content diversity**: cosmic-attributes (v. 1-9), theological-tanzīh (v. 11), continuity-of-revelation (v. 13), Day of Judgment (v. 17-22), kindred-love (v. 23-26), divine omnipotence (v. 29-35), believer-virtues (v. 36-43), Prophet's role (v. 44-53). This is one of the most thematically diverse HM-7 surahs.
2. **Multiple speech-acts**: God speaks; God addresses Prophet; Prophet addresses people; rhetorical questions abound. Each register requires a fitting *fāṣila*.
3. **Two-verse muqaṭṭaʿāt opening** structurally signals a "different" surah from the start; the rhyme-pattern follows.

Q 42 is therefore the **architectural exception within HM-7**: it carries the family's letter-prefix (ḥ-m) but adds a unique second muqaṭṭaʿāt (ʿ-s-q) and breaks the family's prosodic convention. Classical scholarship (al-Suyūṭī, al-Rāzī) has not articulated this exception in empirical terms; this is a novel project finding.

## 7. Cross-references

- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]] — Q 42 is the bifurcation pivot
- [[Q041-fussilat/00-overview|Q 41 Fuṣṣilat]] — preceding HM-A neighbor
- [[Q043-al-zukhruf/00-overview|Q 43 al-Zukhruf]] — following HM-B neighbor (the bifurcation step)
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 31
- [[h-new-570-muqattaat-content-cluster|H-NEW-570]] — Q 42 included in muqaṭṭaʿāt-29 NULL set

## 8. Honest limits

1. The "Q 42 is multi-rāwī because it is the bifurcation pivot" causal narrative is post-hoc; the actual cause-and-effect direction (does the unique opening *cause* the rhyme variation, or is the rhyme variation independent of opening?) is not testable on a single surah.
2. Q 42:23 sectarian-hermeneutic question is not empirically adjudicable; flagged as theological.
3. Q 42's positive sig_A and high rhyme entropy could co-vary structurally; the two are not independent measurements.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
