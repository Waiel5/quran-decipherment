---
surah: 96
surah_name_ar: العلق
surah_name_translit: al-ʿAlaq
file_type: hadith-corpus
date_last_updated: 2026-05-09
phase: B+
verdict: 6 anchor hadiths verified on-disk; ID corrections logged
---

# Q 96 al-ʿAlaq — Hadith Corpus Anchors

## 1. Verified-on-disk hadith inventory for Q 96

All hadiths below verified against `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`. The MW-6 verification tier is "VERIFIED" for these on-disk hadith identifiers (ID-string + chapterId + idInBook + Arabic text).

### Anchor #1 — Bukhārī Bad' al-Waḥy idInBook=3 (THE FIRST-REVELATION HADITH)

| Field | Value |
|:--|:--|
| Source | Ṣaḥīḥ al-Bukhārī |
| File | `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json` |
| chapterId | 1 (Bad' al-Waḥy / Revelation) |
| **idInBook** | **3** |
| global id | 3 |
| Narrator | ʿĀʾisha umm al-muʾminīn (via ʿUrwa b. al-Zubayr → Ibn Shihāb al-Zuhrī → ʿUqayl → al-Layth → Yaḥyā b. Bukayr) |
| Q 96 verses cited | **vv 1-3** ONLY |
| MW-6 tier | VERIFIED (on-disk Arabic text + English translation reviewed 2026-05-09) |

**Arabic text (verbatim from on-disk JSON, key passage):**

```
حَتَّى جَاءَهُ الْحَقُّ وَهُوَ فِي غَارِ حِرَاءٍ، فَجَاءَهُ الْمَلَكُ فَقَالَ اقْرَأْ‏.‏ قَالَ "مَا أَنَا بِقَارِئٍ"...
ثُمَّ أَرْسَلَنِي فَقَالَ {اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ * خَلَقَ الإِنْسَانَ مِنْ عَلَقٍ * اقْرَأْ وَرَبُّكَ الأَكْرَمُ}
```

**English** (on-disk verbatim): "Read in the name of your Lord, who has created (all that exists), created man from a clot. Read! And your Lord is the Most Generous." (96.1, 96.2, 96.3)

**Critical observation**: Bukhārī's hadith quotes ONLY vv 1-3. The full vv 1-5 form is NOT in Bukhārī's narration; it appears in Muslim's parallel narration (idInBook 308; see below).

### Anchor #2 — Muslim Īmān idInBook=308 (PARALLEL FIRST-REVELATION, vv 1-5)

| Field | Value |
|:--|:--|
| Source | Ṣaḥīḥ Muslim |
| File | `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json` |
| chapterId | 1 (Īmān / Faith) |
| **idInBook** | **308** |
| global id | 7585 |
| Narrator | ʿĀʾisha (via ʿUrwa → Ibn Shihāb → Yūnus → Ibn Wahb → Abū al-Ṭāhir Aḥmad b. ʿAmr) |
| Q 96 verses cited | **vv 1-5** (full) |
| MW-6 tier | VERIFIED |

**Arabic text (verbatim, key passage)**:

```
ثُمَّ أَرْسَلَنِي فَقَالَ { اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ * خَلَقَ الإِنْسَانَ مِنْ عَلَقٍ * اقْرَأْ وَرَبُّكَ الأَكْرَمُ * الَّذِي عَلَّمَ بِالْقَلَمِ * عَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ}
```

**English** (on-disk, with translator's misnumbering — see correction below):
"Recite in the name of your Lord Who created, created man from a clot of blood. Recite. And your most bountiful Lord is He Who taught the use of pen, taught man what he knew not (al-Qur'an, xcvi. 1-4)."

**HADITH CORRECTION (logged 2026-05-09)**: The on-disk English translator parenthetical "(al-Qur'an, xcvi. 1-4)" is a TRANSLATION ARTIFACT — the Arabic clearly contains vv 1-5 (through *ʿallama al-insāna mā lam yaʿlam*). The translator may have collapsed vv 4-5 (both starting with *ʿallama*) into a single "verse 4" in their notation. Project should cite Muslim 308 as quoting **vv 1-5**, not "vv 1-4."

### Anchor #3 — Muslim Īmān idInBook=314 (THE JĀBIR DISAGREEMENT)

| Field | Value |
|:--|:--|
| Source | Ṣaḥīḥ Muslim |
| File | same |
| chapterId | 1 (Īmān) |
| **idInBook** | **314** |
| global id | 7591 |
| Narrator | Yaḥyā → Abū Salama → Jābir b. ʿAbdullāh |
| Q reference | Asserts Q 74 al-Muddaththir was first revealed; mentions Q 96 *iqraʾ* as alternate |
| MW-6 tier | VERIFIED |

**English**: "Yahya reported: I asked Abu Salama what was revealed first from the Qur'an. He said: 'O, the shrouded one.' I said: 'Or "Recite."' Jabir said: 'I am narrating to you what was narrated to us by the Messenger of Allah (ﷺ).' He said: 'I stayed in Hira' for one month and when my stay was completed, I came down... and Allah, the Exalted and Glorious, sent down this: you who are shrouded! arise and deliver warning, your Lord magnify, your clothes cleanse.'"

**Significance**: This hadith is the BASIS for the classical Jābir-vs-ʿĀʾisha disagreement on first-revealed surah. The classical resolution (al-Bayhaqī, al-Suyūṭī, al-Qurṭubī): Q 96:1-5 is first revealed AT THE CAVE OF ḤIRĀʾ; Q 74 is first revealed POST-FATRA (after the pause). Both correct in different senses.

### Anchor #4 — Muslim Mosques idInBook=1201 (Q 96 SAJDA-TILĀWA)

| Field | Value |
|:--|:--|
| Source | Ṣaḥīḥ Muslim |
| File | same |
| chapterId | 5 (al-Masājid wa-mawāḍiʿ al-ṣalāh) |
| **idInBook** | **1201** |
| global id | 8478 |
| Narrator | Abū Hurayra (via ʿAṭāʾ b. Mīnā → Ayyūb b. Mūsā → Sufyān b. ʿUyayna) |
| Q 96 reference | "We performed prostration along with the Prophet at *idhā al-samāʾu inshaqqat* (Q 84:1) and *iqraʾ bi-smi rabbika* (Q 96:1)" |
| MW-6 tier | VERIFIED |

**Arabic** (verbatim): "سَجَدْنَا مَعَ النَّبِيِّ صلى الله عليه وسلم فِي { إِذَا السَّمَاءُ انْشَقَّتْ} وَ { اقْرَأْ بِاسْمِ رَبِّكَ}"

**English**: "We performed prostration along with the Messenger of Allah (ﷺ) (as he recited these verses:) 'When the heaven burst asunder' and 'Read in the name of Thy Lord' (al-Qur'an, xcvi. 1)."

**Significance**: PRIMARY anchor for Q 96 sajda-tilāwa membership in the canonical 14-surah Sunni list. Al-Bukhārī's *Sujud al-Quran* chapter (Kitāb 17) does NOT have a Q 96-specific narration; Muslim is the explicit Q 96 anchor.

### Anchor #5 — Muslim Mosques idInBook=1202 (Q 96 SAJDA-TILĀWA, parallel)

| Field | Value |
|:--|:--|
| chapterId | 5 (Mosques) |
| **idInBook** | **1202** |
| global id | 8479 |
| Narrator | Abū Hurayra (via ʿAbd al-Raḥmān al-Aʿraj → Ṣafwān b. Sulaym → Yazīd b. Abī Ḥabīb → al-Layth → Muḥammad b. Rumḥ) |
| Q 96 reference | "The Messenger of Allah prostrated at *idhā al-samāʾu inshaqqat* and *iqraʾ bi-smi rabbika*" |
| MW-6 tier | VERIFIED |

**Arabic**: "سَجَدَ رَسُولُ اللَّهِ صلى الله عليه وسلم فِي { إِذَا السَّمَاءُ انْشَقَّتْ} وَ { اقْرَأْ بِاسْمِ رَبِّكَ}"

**Significance**: Parallel narration anchoring Q 96 sajda. The two narrations (1201, 1202) form a multi-narrator (multi-chain) corroboration.

### Anchor #6 — Bukhārī Sujud al-Quran chapter overview (Kitāb 17)

| Field | Value |
|:--|:--|
| Source | Ṣaḥīḥ al-Bukhārī |
| chapterId | 17 (Sujūd al-Qurʾān / Prostration During Recital) |
| Total hadiths in chapter | 13 (idInBook 1036-1048) |
| Q 96-specific narration | **NOT PRESENT** |
| Surahs explicitly named with sajda | Q 53 al-Najm (idInBook 1036, 1039, 1040, 1042); Q 38 Ṣād (1038); Q 32 al-Sajda (1037 implied via "ALM tanzīl"); Q 76 hal atā (1037 implied via "hal atā ʿalā al-insān"); Q 84 al-Inshiqāq (1043, 1047) |

**Significance**: Bukhārī's Sujud al-Quran chapter NAMES specific sajda-surahs but Q 96 is not among them in this chapter. The Q 96 sajda is anchored via Muslim Mosques 1201, 1202 (Anchor #4-5 above), not Bukhārī. Past project descriptions that placed Q 96 sajda anchor in Bukhārī Sujud al-Quran should be CORRECTED to point to Muslim 1201/1202.

## 2. The first-revelation hadith — full text + analysis

The Bukhārī Bad' al-Waḥy idInBook=3 narration is canonical. Below is the structural breakdown:

### Stage 1 — Pre-revelation dreams + retreat to Ḥirāʾ
*"The first thing the Prophet experienced of revelation was the true vision in sleep. He would not see a vision but it came true like the dawn. Solitude was made dear to him, and he used to seclude himself at the cave of Ḥirāʾ, engaging in worship for many nights..."*

### Stage 2 — The angelic encounter (3 commands + 3 squeezes)
*"...until the truth (al-ḥaqq) came to him while he was at Ḥirāʾ. The angel came and said: **'iqraʾ' (Recite!)**. The Prophet said: 'mā anā bi-qāriʾ' (I cannot recite). [The angel] seized me and pressed me until I was at the limit of endurance, then released me and said: **'iqraʾ' (Recite!)**. I said: 'mā anā bi-qāriʾ.' He seized me a second time, pressed me until I was at the limit, then released me and said: **'iqraʾ' (Recite!)**. I said: 'mā anā bi-qāriʾ.' He seized me a third time, then released me and said: **{اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ * خَلَقَ الإِنْسَانَ مِنْ عَلَقٍ * اقْرَأْ وَرَبُّكَ الأَكْرَمُ}** (Q 96:1-3)."*

The 3-iqraʾ-from-the-angel + 3-mā-anā-bi-qāriʾ-from-the-Prophet + 3-physical-seizings is a tripartite ritual of revelation-induction. The eventual Q 96:1-3 is the OUTPUT after the third seizing.

### Stage 3 — Return to Khadīja, encounter with Waraqa
*"The Prophet returned trembling to Khadīja saying: 'zammilūnī zammilūnī' (cover me, cover me). Khadīja covered him until the terror passed. He told her: 'I fear for myself.' Khadīja said: 'No! Allah will never disgrace you. You uphold kinship, bear the burden of others, give to those who have nothing, host the guest, and assist in calamities of truth.' She took him to Waraqa b. Nawfal (her cousin, an old Christian who knew Hebrew scripture). Waraqa said: 'This is the nāmūs (the protector of secrets) whom Allah sent to Mūsā. I wish I were young so that I could be alive when your people drive you out.'"*

### Stage 4 — The fatra (pause)
*"Then Waraqa died and the revelation paused (fatara al-waḥy)."*

### Significance for Q 96 chronology

This hadith establishes:
- Q 96:1-3 (vv 1-3 specifically per Bukhārī; vv 1-5 per Muslim 308) = first NUZŪL EVENT.
- The fatra follows.
- Q 74 al-Muddaththir is the FIRST POST-FATRA revelation (per Muslim 314 / Jābir narration); Q 96 vv 6-19 are revealed at some other later point in the early Meccan period.
- The classical synthesis (al-Suyūṭī, al-Bayhaqī): Q 96:1-3 (or 1-5) is FIRST-REVEALED-AT-CAVE; Q 74:1-5 is FIRST-REVEALED-POST-FATRA; Q 1 al-Fātiḥa is FIRST-REVEALED-AS-COMPLETE-SURAH.

## 3. Chronological-tradition cross-reference

Per `data/revelation-order.csv`:

| Tanzil rev-order | Surah | Nöldeke order | Phase |
|:-:|:-:|:-:|:--|
| 1 | **Q 96** al-ʿAlaq | 1 | Early Meccan |
| 2 | Q 68 al-Qalam | 18 | Early Meccan |
| 3 | Q 73 al-Muzzammil | 23 | Early Meccan |
| 4 | Q 74 al-Muddaththir | 2 | Early Meccan |
| 5 | Q 1 al-Fātiḥa | 48 | Early Meccan |

The **Tanzil ordering and Nöldeke ordering both agree Q 96 = #1**. Q 74 al-Muddaththir is at #4 in Tanzil (post-fatra Anchor #3 above) but Nöldeke at #2 (some Western scholarship treats Q 74 as first; this is a classical-vs-academic chronology disagreement). The project's standard is Tanzil ordering, so Q 96 = first revealed.

## 4. Asbāb al-nuzūl literature (vv 9-19)

Multiple chains in the asbāb compendia (al-Wāḥidī, al-Qurṭubī ad loc., al-Suyūṭī *Durr al-manthūr*) anchor vv 9-19 to the **Abū Jahl** ʿAmr b. Hishām confrontation:

### The Abū Jahl scenes (compiled from al-Wāḥidī)

1. **Abū Jahl threatens the Prophet's prayer**: he swore to step on the Prophet's neck if found prostrating at the Kaʿba.
2. **The Prophet recites Q 96:9-13** (*a-raʾayta alladhī yanhā ʿabdan idhā ṣallā* — "Have you seen the one who forbids a servant when he prays?") in response.
3. **Abū Jahl approaches** intending to assault, but recoils — multiple chains describe a vision of fire or terror that drives him back.
4. **The Prophet recites vv 15-18** (*la-nasfaʿan bi-l-nāṣiyati nāṣiyatin kādhibatin khāṭiʾatin fa-l-yadʿu nādiyahū sa-nadʿu al-zabāniya*) — direct threat by name to Abū Jahl's tribal council and the eschatological zabāniya counterpart.

The **closing v 19** *kallā lā tuṭiʿhu wa-sjud wa-qtarib* is then directed to the PROPHET — "Don't obey him; prostrate and draw near." The sajda-event becomes the structural counter-action to Abū Jahl's forbidding of prayer.

This Abū Jahl context is corroborated across 12+ chains in al-Suyūṭī's *al-Durr al-manthūr* (ad loc.). It is the densest asbāb-traditioned passage in the early Meccan corpus.

## 5. Tirmidhī coverage

Verified via `tirmidhi.json`:

- Tafsir chapter (chapterId=47, "Chapters on Tafsir of the Qur'an"): contains 421 hadiths (idInBook 3033-3453). The Tirmidhī Tafsir chapter does **NOT** appear to extend to Q 96 with a surah-tafsir-heading hadith — search returned 0 hits for direct Q 96 ad loc tafsīr in this dataset.
- Faḍāʾil al-Qurʾān chapter (chapterId=45): no Q 96-specific virtues hadith found in the on-disk JSON.

**Honest report**: Tirmidhī Tafsir on Q 96 in our on-disk dataset is sparse-to-absent. This may reflect the dataset's Tafsir chapter coverage cutoff or genuine Tirmidhī sparseness on Q 96; the latter would be unusual given Q 96's first-revelation status. If the project extends Tirmidhī coverage, Q 96 should be re-checked.

## 6. Cross-corpus search summary

Q 96-related hadith summary across the 9-books on-disk:

| Source | Q 96-specific hadiths found | Key id |
|:--|:--:|:--|
| Bukhārī | 1 (Bad' al-Waḥy 3) | idInBook 3 |
| Muslim | 3 (Īmān 308 first-rev; Mosques 1201, 1202 sajda) | idInBook 308, 1201, 1202 |
| Tirmidhī | 0 found in Tafsir chapter | — |
| Abū Dāwūd | (not searched comprehensively) | — |
| Nasāʾī | (not searched comprehensively) | — |
| Ibn Mājah | (not searched comprehensively) | — |

## 7. Hadith corrections logged 2026-05-09

The following hadith citations should be UPDATED in project documentation:

1. **Bukhārī first-revelation hadith quotes vv 1-3, NOT vv 1-5** — past project descriptions that say "Bukhārī ḥadīth #3 cites vv 1-5" should be tightened to "vv 1-3."
2. **Muslim 308 quotes vv 1-5** (the full canonical first-revelation text). The on-disk English translator's "(al-Qur'an, xcvi. 1-4)" parenthetical is a translation artifact; the Arabic has all 5 verses.
3. **Q 96 sajda anchor is Muslim Mosques 1201/1202, NOT Bukhārī Sujud al-Quran** — Bukhārī's chapter 17 (Sujūd al-Qurʾān) does NOT contain a Q 96-specific sajda narration. Muslim is the explicit Q 96-sajda anchor.
4. **Tirmidhī Tafsir on Q 96 is sparse/absent in current dataset** — past project descriptions referencing "Tirmidhī Tafsīr ch. 96" should be flagged as needing on-disk verification (the current dataset's Tirmidhī Tafsir chapter does not appear to contain Q 96 ad loc).

## 8. Hadith authenticity

| Anchor | Grading | Note |
|:--|:--:|:--|
| Bukhārī 3 (Bad' al-Waḥy) | Ṣaḥīḥ (in Bukhārī) | Highest authenticity tier |
| Muslim 308 (Īmān) | Ṣaḥīḥ (in Muslim) | Highest authenticity tier |
| Muslim 314 (Īmān) | Ṣaḥīḥ (in Muslim) | Highest tier; classical disagreement-traditioned |
| Muslim 1201 (Mosques) | Ṣaḥīḥ (in Muslim) | Q 96 sajda primary anchor |
| Muslim 1202 (Mosques) | Ṣaḥīḥ (in Muslim) | parallel narration |

All anchor hadiths for Q 96 are at the highest classical-authenticity tier (Bukhārī or Muslim narration). The classical first-revelation tradition is among the most heavily corroborated facts in Sunni hadith literature.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
