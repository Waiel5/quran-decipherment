---
surah: 71
surah_name_ar: نوح
surah_name_translit: Nūḥ
file_type: hadith-corpus
date_last_updated: 2026-05-30
phase: B+
verdict: "Five-idol etiology verified in al-Bukhārī Kitāb al-Tafsīr (idInBook 4712, Ibn ʿAbbās chain). Noah-as-first-messenger verified in Bukhārī (6326, 7128) + Muslim (386). NO ṣaḥīḥ surah-specific faḍāʾil-of-Sūrat-Nūḥ ḥadīth located on disk."
---

# Q 71 Nūḥ — Hadith Corpus

**Numbering note (read first).** Hadith numbers below are the `idInBook` values in the
on-disk collection `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`.
These are sequential within each book and may DIFFER from the Fatḥ al-Bārī / Dār al-Salām
numbering used in the existing Q071-F-02 pre-reg. Every number below was verified by
direct lookup on disk; cross-numbering discrepancies are flagged explicitly.

## 1. The five idols of Noah's people — al-Bukhārī, Kitāb al-Tafsīr (the key ḥadīth)

- **Collection:** Ṣaḥīḥ al-Bukhārī, Kitāb al-Tafsīr (chapterId 65, *Kitāb al-Tafsīr*).
- **On-disk number:** **idInBook 4712**
  (`.../the_9_books/bukhari.json`, hadiths[idInBook==4712]).
- **Cross-numbering FLAG:** the Q071-F-02 pre-reg cites this ḥadīth as **"#4920"** —
  that is the Fatḥ al-Bārī / Dār al-Salām sequential number for the same narration.
  The on-disk ahmedbaset collection numbers it **4712**. SAME ḥadīth (the Arabic
  *isnād* and *matn* match verbatim — see below); the discrepancy is purely a
  numbering-scheme difference, flagged per the anti-hallucination rule.
- **Isnād (Arabic, on disk):** *ḥaddathanā Ibrāhīm b. Mūsā, akhbaranā Hishām, ʿan Ibn
  Jurayj, wa-qāla ʿAṭāʾ ʿan Ibn ʿAbbās — raḍiya Allāhu ʿanhumā.*
- **Matn (English, on disk):** "All the idols which were worshiped by the people of
  Noah were worshiped by the Arabs later on. As for the idol Wadd, it was worshiped by
  the tribe of Kalb at Dūmat al-Jandal; Suwāʿ was the idol of Hudhayl; Yaghūth was
  worshiped by Murād and then by Banū Ghuṭayf at al-Juruf near Sabaʾ; Yaʿūq was the idol
  of Hamdān; and Nasr was the idol of Ḥimyar, the branch of Dhū al-Kalāʿ. The names (of
  the idols) formerly belonged to some pious men of the people of Noah, and when they
  died Satan inspired their people to (prepare and place idols …)."
- **Grade:** ṣaḥīḥ (Ṣaḥīḥ al-Bukhārī).
- **Relevance:** the canonical operationalization of the five names at Q 71:23, and the
  basis of the classical statue-of-righteous-men etiology (al-Ṭabarī, al-Baghawī, Ibn
  Kathīr — see `03-tafsir-survey.md`). This is the corroborating source for the
  Q071-F-02 corpus-singleton test.

## 2. Noah as the first messenger — the intercession (shafāʿa) ḥadīth

This is the most-cited ḥadīth touching Nūḥ's prophetic rank (relevant to al-Qurṭubī's
"awwalu rasūlin ursila" claim, `03-tafsir-survey.md` §2).

- **Ṣaḥīḥ al-Bukhārī, idInBook 6326** (chapterId 81): "… 'Go to Noah, the first Apostle
  sent by Allah.' They will go to him and he will say, 'I am not fit for this
  undertaking' …" (verified on disk).
- **Ṣaḥīḥ al-Bukhārī, idInBook 7128** (chapterId 97, Kitāb al-Tawḥīd): "… 'But you'd
  better go to Noah as he was the first Apostle sent by Allah to the people of the
  Earth' …" (verified on disk).
- **Ṣaḥīḥ Muslim, idInBook 386** (chapterId 1, Kitāb al-Īmān): "O Noah, thou art the
  first of the Messengers (sent) on the earth (after Adam), and Allah named thee as a
  'Grateful Servant' (ʿabdan shakūran), intercede for us …" (verified on disk).
- **Grade:** ṣaḥīḥ (Bukhārī + Muslim, *muttafaq ʿalayh*).
- **Note:** the Muslim wording *ʿabdan shakūran* echoes Q 17:3 (*dhurriyyata man ḥamalnā
  maʿa Nūḥin innahu kāna ʿabdan shakūran*), not a Q 71 verse — a Nūḥ-character ḥadīth,
  not a Sūrat-Nūḥ faḍāʾil ḥadīth.

## 3. Faḍāʾil of Sūrat Nūḥ — DATA GAP (honest negative)

A targeted search of the 9 canonical books on disk (al-Bukhārī, Muslim, al-Tirmidhī,
Abū Dāwūd, al-Nasāʾī, Ibn Mājah, Aḥmad) for a surah-specific *faḍīla* of Sūrat Nūḥ
(a "whoever recites Sūrat Nūḥ …" report, or a fixed liturgical placement) returned
**no ṣaḥīḥ surah-level virtue ḥadīth**. Unlike Q 1, Q 36, Q 55, Q 67, Q 112, etc.,
Sūrat Nūḥ has no prominent recitation-virtue tradition in the canonical corpus on
disk. Flagged as NULL-DATA-GAP rather than asserted absent for the whole tradition;
the search was over the on-disk ahmedbaset 9-book collection only.

## 4. Asbāb al-nuzūl

No discrete occasion-of-revelation report attaches to Sūrat Nūḥ as a whole (it is a
Meccan narrative surah, not a response to an event). al-Wāḥidī's *Asbāb*-tradition
material on disk for Q 71 (`en-asbab-al-nuzul-by-al-wahidi/71/13.json`) is homiletic
exegesis of v 13-14 (the *aṭwāran* creation reflection), not a classical *sabab*.

## 5. Summary table

| Topic | Collection | On-disk idInBook | Grade | Status |
|---|---|---|---|---|
| Five idols → Arab tribes | Bukhārī, Kitāb al-Tafsīr | **4712** (= FatḥBārī #4920) | ṣaḥīḥ | VERIFIED on disk |
| Noah first messenger (shafāʿa) | Bukhārī | 6326 | ṣaḥīḥ | VERIFIED on disk |
| Noah first messenger (Tawḥīd) | Bukhārī | 7128 | ṣaḥīḥ | VERIFIED on disk |
| Noah first of messengers / *ʿabd shakūr* | Muslim, Kitāb al-Īmān | 386 | ṣaḥīḥ | VERIFIED on disk |
| Faḍāʾil of Sūrat Nūḥ | — | — | — | NULL-DATA-GAP (none located) |
| Asbāb al-nuzūl (surah-level) | — | — | — | none (Meccan narrative) |

*All numbers above were confirmed by direct JSON lookup. The single most important
cross-check — the Q071-F-02 deity-cluster source — is the Bukhārī Kitāb al-Tafsīr
narration, present on disk as idInBook 4712 (Fatḥ al-Bārī #4920), Ibn ʿAbbās chain.*
