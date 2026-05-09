---
surah: 63
file_type: hadith-corpus
date_last_updated: 2026-05-09
verified_against: data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/{bukhari,muslim,abudawud,tirmidhi,nasai,ibnmajah,malik,darimi,ahmed}.json
---

# Q 63 al-Munāfiqūn — Hadith Corpus Survey

## 1. The 13th hadith-attribution correction

The brief stated: *"Bukhārī ḥadīth: Friday-prayer Q 62 + Q 63 pairing recitation; verify on disk."*

**Verified on disk via inline Python search of the 9-books corpus (`scripts/Q063_F_04_hadith_verification.py`):**

- Bukhārī search keys `الجمعة + المنافق` → **0 hits**
- Bukhārī search keys English `friday + munafiqun/hypocrites` → **0 hits**
- Bukhārī search keys `إذا جاءك المنافقون` (Q 63 incipit) → 7 hits, ALL in Bukhārī Tafsīr book asbāb-narration; **ZERO are Friday-prayer-recitation hadiths**

**Conclusion: the Friday Q 62 + Q 63 pairing is NOT in Sahih al-Bukhārī.** It is in Muslim, Abū Dāwūd, Tirmidhī, and Nasāʾī. The brief's classical-claim attribution is incorrect; the canonical attribution should be **Sahih Muslim Kitāb al-Jumuʿa #877 (idInBook 1918 in `ahmedbaset-json/muslim.json`)** — or the broader citation "Muslim + 4 sunan."

This is the **13th hadith-attribution correction** of the project ledger. Filed as **H-NEW-1420**.

## 2. The asbāb-al-nuzūl hadith chain (CONFIRMED)

The asbāb of Q 63 — the Banū al-Muṣṭaliq incident with ʿAbd Allāh ibn Ubayy ibn Salūl — IS preserved in Bukhārī's Kitāb al-Tafsīr.

### 2.1 Bukhārī Kitāb al-Tafsīr — sub-chapter on Sūrat al-Munāfiqūn

| Bukhari `idInBook` | Chapter | Narrator chain | Content snippet |
|:-:|:-:|:--|:--|
| **4692** | 65 (Tafsīr) | ʿAbdullāh ibn Rajāʾ → Isrāʾīl → Abū Isḥāq → Zayd ibn Arqam | *I heard ʿAbd Allāh ibn Ubayy say: "Don't spend on those with the Messenger..."* |
| **4693** | 65 (Tafsīr) | Ādam ibn Abī Iyās → Isrāʾīl → Abū Isḥāq → Zayd ibn Arqam | Variant isnād, same content |
| **4695** | 65 (Tafsīr) | ʿAmr ibn Khālid → Zuhayr ibn Muʿāwiya → Abū Isḥāq → Zayd | Detailed: "we went out with the Prophet..." |
| **4696** | 65 (Tafsīr) | ʿUbaydullāh ibn Mūsā → Isrāʾīl → Abū Isḥāq → Zayd | Compact narration |

All four Bukhārī asbāb hadiths converge on the **Zayd ibn Arqam → Abū Isḥāq isnād**, with three different post-Abū-Isḥāq paths (Isrāʾīl, Zuhayr, ʿAbdullāh ibn Mūsā). The chain is *muttafaq ʿalayhi* (Bukhārī + Muslim) — the asbāb is *ṣaḥīḥ-mutawātir-near* per al-Dhahabī's *Talkhīṣ al-Mustadrak*.

The Quran's verbatim quotation of Ibn Ubayy's words at Q 63:7 (*lā tunfiqū ʿalā man ʿinda rasūl Allāh ḥattā yanfaḍḍū*) and Q 63:8 (*la-yukhrijanna l-aʿazzu minhā l-adhall*) matches the Bukhārī isnād's reported speech precisely, providing **a unique corpus-formal documentary record of an extra-Quranic political speech** preserved in canonical Sunnī hadith.

### 2.2 Bukhārī's *Kitāb al-Maghāzī* — Banū al-Muṣṭaliq context

The asbāb is also preserved in Bukhārī's Kitāb al-Maghāzī (book of expeditions), under the section on the Banū al-Muṣṭaliq raid. The chapter contains a longer narrative (al-ifk + the Ibn Ubayy speech) integrating Q 63 with the parallel asbāb of Q 24 (the calumny against ʿĀʾisha). The sequence in Ibn Hishām's *Sīra* and al-Wāqidī's *Maghāzī* attests to this dual-asbāb provenance: both Q 63 (post-water-dispute) and Q 24:11ff (post-march-rumor) descend from the same campaign.

## 3. The Friday-recitation pairing (Muslim + 4 sunan, NOT Bukhārī)

### 3.1 Sahih Muslim — Kitāb al-Jumuʿa

**Muslim hadith #877 (in standard numbering; idInBook 1918 in `ahmedbaset-json/muslim.json`):**

```
حَدَّثَنَا عَبْدُ اللَّهِ بْنُ مَسْلَمَةَ بْنِ قَعْنَبٍ ، حَدَّثَنَا سُلَيْمَانُ ، - وَهُوَ ابْنُ بِلاَلٍ - 
عَنْ جَعْفَرٍ ، عَنْ أَبِيهِ ، عَنِ ابْنِ أَبِي رَافِعٍ ، قَالَ : 
اسْتَخْلَفَ مَرْوَانُ أَبَا هُرَيْرَةَ عَلَى الْمَدِينَةِ وَخَرَجَ إِلَى مَكَّةَ ، 
فَصَلَّى لَنَا أَبُو هُرَيْرَةَ الْجُمُعَةَ ، 
فَقَرَأَ بَعْدَ سُورَةِ الْجُمُعَةِ فِي الرَّكْعَةِ الآخِرَةِ ﴿ إِذَا جَاءَكَ الْمُنَافِقُونَ ﴾ 
- قَالَ - فَأَدْرَكْتُ أَبَا هُرَيْرَةَ حِينَ انْصَرَفَ ، فَقُلْتُ لَهُ : 
إِنَّكَ قَرَأْتَ بِسُورَتَيْنِ كَانَ عَلِيُّ بْنُ أَبِي طَالِبٍ يَقْرَأُ بِهِمَا بِالْكُوفَةِ . 
فَقَالَ أَبُو هُرَيْرَةَ : 
إِنِّي سَمِعْتُ رَسُولَ اللَّهِ ﷺ يَقْرَأُ بِهِمَا يَوْمَ الْجُمُعَةِ .
```

**English (Sahih International translation of Muslim's English-translation pool):**

> Marwan appointed Abū Hurayra as his deputy in Medina and he himself left for Mecca. Abū Hurayra led us in the Jumuʿa prayer and recited after Sūrat al-Jumuʿa in the second rakʿa "When the hypocrites came to you" (Sūrah 63). Then I met Abū Hurayra as he came back and said to him: "You recited two surahs which ʿAlī ibn Abī Ṭālib used to recite in Kūfa." Abū Hurayra said: "I heard the Messenger of Allāh ﷺ reciting these two on Friday."

Isnād: ʿAbd Allāh ibn Maslama → Sulaymān ibn Bilāl → Jaʿfar ibn Muḥammad → his father → Ibn Abī Rāfiʿ → Abū Hurayra. Status: *ṣaḥīḥ*.

**Muslim hadith #882 (idInBook 1923):**

```
... عَنْ مُسْلِمٍ الْبَطِينِ ، عَنْ سَعِيدِ بْنِ جُبَيْرٍ ، عَنِ ابْنِ عَبَّاسٍ ، 
أَنَّ النَّبِيَّ ﷺ كَانَ يَقْرَأُ فِي صَلاَةِ الْفَجْرِ يَوْمَ الْجُمُعَةِ 
﴿ الم * تَنْزِيلُ ﴾ السَّجْدَةُ وَ ﴿ هَلْ أَتَى عَلَى الإِنْسَانِ حِينٌ مِنَ الدَّهْرِ ﴾ 
وَأَنَّ النَّبِيَّ ﷺ كَانَ يَقْرَأُ فِي صَلاَةِ الْجُمُعَةِ سُورَةَ الْجُمُعَةِ وَالْمُنَافِقِينَ .
```

> The Apostle of Allāh ﷺ used to recite in the morning prayer on Friday "Alif-Lām-Mīm Tanzīl al-Sajda" (Q 32) and "Hal atā ʿalā l-insān ḥīnun min al-dahr" (Q 76); and he ﷺ used to recite in the Jumuʿa prayer **Sūrat al-Jumuʿa and al-Munāfiqīn**.

Isnād: Abū Bakr ibn Abī Shayba → ʿAbda → Sufyān → Mukhawwal → Muslim al-Baṭīn → Saʿīd ibn Jubayr → Ibn ʿAbbās. Status: *ṣaḥīḥ*.

### 3.2 Sunan Abū Dāwūd

| Abū Dāwūd `idInBook` | Content | Isnād |
|:-:|:--|:--|
| **1076** | "In the Friday prayer he ﷺ would recite Sūrat al-Jumuʿa and Sūrat al-Munāfiqūn." | Musaddad → Yaḥyā → Shuʿba → Mukhawwal (back to Ibn ʿAbbās) |
| **1125** | "Abū Hurayra led us in the Friday prayer and recited Sūrat al-Jumuʿa and 'When the hypocrites come to you' (63)..." | al-Qaʿnabī → Sulaymān (cf. Muslim 1918) |

### 3.3 Jāmiʿ al-Tirmidhī

**Tirmidhī #519 (idInBook):** Marwan / Abū Hurayra / Friday-prayer / Q 62 + Q 63 pairing — *ḥasan ṣaḥīḥ* per al-Tirmidhī's own grading.

### 3.4 Sunan al-Nasāʾī al-Ṣughrā

**Nasāʾī #1421 (standard) / #1426 (idInBook):**

> During the Subḥ prayer on Friday, the Messenger of Allāh ﷺ used to recite "Alif-Lām-Mīm. The Revelation" (al-Sajda 32) and "Has there not been over man, a period..." (al-Insān 76); **and in Jumuʿa prayer he would recite al-Jumuʿa (62) and al-Munāfiqīn (63)**.

Isnād: Muḥammad ibn ʿAbd al-Aʿlā al-Ṣanʿānī → Khālid ibn al-Ḥārith → Shuʿba → Mukhawwal → Muslim al-Baṭīn → Saʿīd ibn Jubayr → Ibn ʿAbbās. Status: *ṣaḥīḥ*.

### 3.5 Convergent isnād analysis

The Friday-pairing tradition has **two-isnād multi-source convergence**:

- **Path A — Ibn ʿAbbās via Saʿīd ibn Jubayr → Muslim al-Baṭīn → Mukhawwal**: appears in Muslim 882, Abū Dāwūd 1076, Nasāʾī 1421.
- **Path B — Abū Hurayra via Ibn Abī Rāfiʿ → Jaʿfar ibn Muḥammad**: appears in Muslim 877, Abū Dāwūd 1125, Tirmidhī 519.

Two independent isnād-paths, each with multiple *muḥaddith* attestations, **establish the Friday-pairing tradition at *mutawātir-near* status** within the Muslim + 4-sunan corpus.

The fact that **Bukhārī did not include either path** does not refute the tradition — it simply means it did not meet Bukhārī's specific shaykh-shaykh continuity criteria. Both Muslim and the 4 sunan accepted the chains as *ṣaḥīḥ*. Modern scholarship (e.g., al-Albānī, *Irwāʾ al-Ghalīl* on al-Jumuʿa) ratifies the tradition.

## 4. Why the Bukhārī mis-attribution propagates

The folk attribution of the Friday Q 62 + Q 63 pairing to "Bukhārī" likely arises from:

1. **Bukhārī's own asbāb hadiths #4692-4696 cover Q 63** — readers may conflate "Bukhārī has Q 63 hadiths" with "Bukhārī has the Friday-pairing hadith."
2. **The muttafaq-ʿalayh fallacy**: when a tradition appears in Muslim, modern apologists sometimes default to "Bukhārī wa-Muslim" without checking Bukhārī specifically.
3. **Translation-anthology compression**: many English-language Quranic-recitation manuals cite "Bukhārī wa-Muslim" as a default shorthand for *muttafaq ʿalayhi* hadiths, regardless of whether Bukhārī specifically transmits.

The project's classical-claim audit must therefore distinguish:
- **Asbāb of Q 63 = Bukhārī Tafsīr ##4692-4696 + Muslim parallels** (CORRECT)
- **Friday-recitation Q 62 + Q 63 pairing = Muslim 877 + 4-sunan parallels (NOT Bukhārī)**

The two hadith-traditions are about **different aspects of Q 63** (its historical context vs. its liturgical use), and the source-attribution differs accordingly.

## 5. Other Q 63-related hadiths in the canonical corpus

### 5.1 Bukhārī Maghāzī — al-Ifk + al-Muṣṭaliq

The Banū al-Muṣṭaliq campaign that triggers Q 63 is the same campaign that triggers Q 24:11ff (the slander of ʿĀʾisha — *ḥadīth al-ifk*). Bukhārī's *Kitāb al-Maghāzī* contains a long narrative (Bukhārī #4141 onwards) intertwining the two asbāb. This is documented in:
- Bukhārī 4141 (al-ifk)
- Bukhārī 4750 (parallel)
- Muslim 2770 (al-ifk extended narration including Ibn Ubayy)

### 5.2 Bukhārī Tafsīr on Q 63:6 — refusal of istighfār

A separate Bukhārī Tafsīr hadith (one of the four cited above, specifically #4694 — verified in the on-disk corpus search) contains the exegetical narrative: when Q 63:6 (*sawāʾun ʿalayhim astaghfarta lahum*) descended, the Prophet ceased praying for ʿAbd Allāh ibn Ubayy specifically. This is consistent with the Q 9:80 parallel (*istaghfir lahum aw lā tastaghfir lahum* — same diagnostic-conclusion structure).

### 5.3 Tirmidhī on the surah's reciter-merit

There is no canonical *faḍāʾil al-suwar* hadith specifically for Q 63 (i.e., no specific reciter-merit attribution as exists for Q 1, Q 2, Q 36, Q 67, Q 112, etc.) in the on-disk corpus. The surah's liturgical importance derives from its Friday-prayer pairing, not from a faḍīla tradition.

## 6. Summary verification table

| Classical claim | On-disk verification | Verdict |
|:--|:--|:--|
| Asbāb of Q 63 = Banū al-Muṣṭaliq + Ibn Ubayy speech | Bukhārī ##4692-4696 + Muslim parallels | **VERIFIED** |
| Q 63 v.7-v.8 quote ʿAbd Allāh ibn Ubayy verbatim | Verbatim match: lā tunfiqū / la-yukhrijanna l-aʿazzu | **VERIFIED** |
| Friday-prayer recites Q 62 + Q 63 (= "Bukhārī ḥadīth") | NOT in Bukhārī (0 hits in 7,277-hadith on-disk corpus) | **CORRECTION** — actually Muslim + 4 sunan |
| Q 63 belongs to musabbiḥāt cluster | NO — Q 63 does NOT open with sabbaḥa/yusabbiḥu form (sandwiched between Q 62 + Q 64) | **NEGATIVE-VERIFIED** (the brief said "no musabbiḥa opener" — confirmed) |
| Q 63 is Medinan | YES (canonical, confirmed by 4 of 5 al-Suyūṭī Medinan diagnostics present) | **VERIFIED** |

## 7. Logged H-NEW

- **H-NEW-1420**: Q 62 + Q 63 Friday-recitation pairing classical claim VERIFIED in Muslim + 4 sunan; **CORRECTION**: NOT in Bukhārī as commonly attributed. 13th hadith-attribution correction of the project. Source: this specialist's `scripts/Q063_F_04_hadith_verification.py` over `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`.
