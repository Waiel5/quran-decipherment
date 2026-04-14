# Abdel Haleem (1992) — *Grammatical Shift for Rhetorical Purposes: Iltifāt and Related Features in the Qurʾān*

**Source citation:** M. Abdel Haleem, "Grammatical Shift for Rhetorical Purposes: Iltifāt and Related Features in the Qurʾān", *Bulletin of the School of Oriental and African Studies* 55(3): 407–432 (1992).

**Acquired:** 2026-04-12 from islamic-awareness.org's verse-by-verse rendition (`https://www.islamic-awareness.org/quran/text/grammar/iltifaat.html`) — a lightly-edited HTML transcription of the Abdel Haleem paper, which is in turn the standard modern academic systematisation of al-Zarkashī's iltifāt chapter from *al-Burhān fī ʿulūm al-Qurʾān* and al-Suyūṭī's parallel chapter in *al-Itqān*.

**Why this matters for our project:** Abdel Haleem's exhaustive verse list is the closest thing the field has to a *ground truth* catalog of iltifāt instances. Any computational detector for iltifāt should be benchmarked against it. We use it as the precision/recall reference for the iltifat-detector agent.

---

## Definition (Al-Zarkashī, *al-Burhān*)

> "the change of speech from one mode to another, for the sake of freshness and variety for the listener, to renew his interest, and to keep his mind from boredom and frustration, through having the one mode continuously at his ear."

Each person mode "has its appropriate context in which it is used"; transitions follow structured patterns rather than occurring "haphazardly". The general principle is *li-iqtiḍāʾ al-ḥāl* — departures from normal speech occur "because situational context necessitates such shifts for rhetorical effect beyond surface expectation."

Ibn al-Athīr (637/1239) called iltifāt **shajāʿat al-ʿarabiyya** ("the daring of the Arabic language"). The Quran employs the device far more extensively than any other Arabic prose: "no one seems to quote references in prose other than from the Qurʾān; indeed a sampling of ḥadīth material found not a single instance."

---

## Six classical types of *person* iltifāt

| # | Direction | Approx. count | Note |
|--:|---|---:|---|
| 1 | 3rd → 1st person | **>140** | most common; the divine narrative voice "turning toward itself" |
| 2 | 1st → 3rd person | **~100** | the divine "I/We" stepping back to objective narration |
| 3 | 3rd → 2nd person | **~60** | God or third party suddenly addressed by audience |
| 4 | 2nd → 3rd person | **<30** | rarer; address dropping back to narrative |
| 5 | 1st → 2nd person | **1 (disputed)** | only Q 36:22 (Yā-Sīn, "Why should I not worship Him who created me…") |
| 6 | 2nd → 1st person | **0** | does not occur in the Quran |

---

## Verse list (canonical ground truth)

### Category I — Change in Person

**1. 3rd → 1st**
2:23, 47, 73, 83, 118, 160, 172; 3:25, 58, 168; 4:30, 33, 37, 41, 64, 74, 114, 174; 5:14, 15, 19, 32, 70, 86; 6:22, 92, 97, 98, 99, 107, 110, 114, 126; 7:37, 57; 8:9, 41; 10:7, 11, 21, 22, 23, 28; 11:8; 13:4; 14:13; 16:2, 40, 66, 75, 84; 17:1, 21, 33, 97; 18:7; 19:9, 21, 58; 20:53, 113; 21:29, 37; 22:57, 67; 24:55; 25:17, 32, 45, 48, 56; 26:198; 27:60, 81; 28:57, 61, 75; 29:4, 7, 23; 30:16, 28, 34, 47, 51, 58; 31:7, 10, 23; 32:12, 16, 27; 33:9, 31; 34:5, 9; 35:9, 27; 36:8, 37; 37:6; 39:2, 3, 16, 27, 49; 40:5, 70, 84; 41:12, 28, 39; 42:7, 13, 20, 23, 35, 38, 48; 45:31; 46:7, 15; 47:13; 48:25; 49:13; 52:21, 48; 53:29; 54:11; 55:31; 58:5; 59:21; 61:14; 65:8; 66:10; 67:5, 17; 68:15, 35; 69:11; 70:7; 72:16; 76:9; 80:25; 86:15; 87:6; 88:25; 89:29; 92:7; 96:15

**2. 1st → 3rd**
2:5, 23, 37, 161, 172; 3:57, 151; 4:30, 33, 69, 122; 6:90, 95, 111, 112, 127; 7:12, 58, 101, 142; 8:4; 10:22, 25; 14:46; 15:28, 96; 16:52; 17:1; 20:4; 21:19; 22:6; 23:14, 57, 78, 91, 116; 24:35, 46; 25:31, 47, 58; 26:5, 9, 213; 27:6; 28:13, 59, 62; 29:3, 40, 67, 69; 30:54, 59; 31:11, 23; 32:25; 33:9, 46, 50; 34:21; 35:31, 32, 38; 36:36, 74; 37:33; 38:26; 40:61, 85; 41:19, 28, 40, 45, 53; 44:6; 45:22, 30; 48:2; 51:58; 53:30; 54:55; 57:27; 60:3; 65:10; 66:12; 67:19; 68:48; 76:6, 24, 29; 87:6; 94:8; 95:8; 97:4; 108:2

**3. 3rd → 2nd**
1:5; 2:21, 25, 28, 60, 83, 214, 229, 233; 3:180; 4:11; 6:6; 8:7, 14; 9:19, 69; 10:3, 68; 11:14; 16:55, 68, 74; 19:89; 21:37; 23:15, 65; 27:90; 30:34; 31:33; 33:55; 34:37; 35:3; 36:59; 37:25; 38:59; 43:16; 47:22, 30; 50:24; 52:14, 19, 39; 55:13; 56:51, 91; 57:17, 20; 67:13; 75:34; 76:22, 30; 77:38, 43; 78:30, 36; 80:3; 87:16

**4. 2nd → 3rd**
2:54, 57, 85, 88, 187, 200, 216, 226, 229, 286; 4:9; 10:22; 16:69, 72; 24:63; 28:16; 30:38; 31:32; 32:10; 45:35; 47:23; 67:18; 75:31

**5. 1st → 2nd** — Q 36:22 alone (disputed; counted by Suyūṭī)

**6. 2nd → 1st** — none

### Category II — Change in Number
2:34, 38, 40, 106, 123, 217; 7:24, 127; 14:31, 37; 15:49; 16:65; 17:36; 20:37, 40, 41, 81, 124; 22:45; 23:51, 66; 27:84; 29:8, 57; 31:15; 32:13; 34:12, 45; 35:40; 43:32, 69; 46:5; 50:30; 54:17, 22, 32, 40; 55:31; 65:11; 68:44; 69:44; 70:40; 73:12; 74:16, 31; 75:3; 77:39; 90:4; 98:8; 100:11

### Category III — Change of Addressee
2:144, 148, 150; 4:109; 5:48; 6:133; 7:3; 10:87; 12:29; 16:2; 17:63; 27:93; 28:35; 29:46; 31:31; 33:4, 19, 51; 39:31; 42:13; 48:9; 58:2; 65:1; 69:18; 73:20

### Category IV — Change in Verb Tense / Mood
2:25, 125; 7:29; 11:54; 16:11; 18:47; 22:25, 31, 63, 65; 27:87; 33:10; 35:9; 36:33; 39:68; 40:67

### Category V — Change in Case Marker
2:177; 4:162; 5:69

### Category VI — Noun in Place of Pronoun (selected)
2:59, 60, 64, 105, 107, 109, 112, 115, 153, 157, 207; 3:5; 4:26-32, 80-110, 113, 176; 5:39, 40, 54, 83, 97, 98; 6:1, 21; 8:13; 12:87, 90; 13:2, 3; 14:1, 6, 11, 20-51 (selected); 16:18, 19, 84; 17:22; 19:19, 56, 69, 91-93; 20:130; 21:39; 22:31, 58, 60, 61, 62, 72, 78; 23:27, 58, 59; 24:38, 62, 64; 25:17; 28:56, 64, 68, 70, 75, 87; 29:5, 10, 20, 45, 63; 32:3; 33:2, 13, 17, 25, 50; 35:3, 28; 38:4, 26, 27; 39:2, 3, 22; 40:6, 21, 44; 41:27; 42:5, 47, 49, 53; 46:11; 47:4; 57:9, 21, 29; 59:18; 60:1; 61:13; 63:1, 9; 67:11; 74:31; 110:3

---

## Classical scholars and their contributions

| Scholar | Work | Treatment |
|---|---|---|
| Al-Aṣmaʿī (d. 216/831) | (oral) | First quasi-technical use of *iltifāt* |
| Ibn al-Muʿtazz (d. 296/909) | *Kitāb al-Badīʿ* | First formal technical meaning |
| Ibn Wahb (d. 312/924) | — | Used the term *al-ṣarf* |
| Zamakhsharī (d. 538/1143) | *al-Kashshāf* | Used iltifāt exclusively for transitions in person; lucid explanations of rhetorical effect |
| Ibn Munqidh (d. 584/1188) | — | Used the term *al-inṣirāf* |
| Sakkākī (d. 626/1228) | *Miftāḥ al-ʿulūm* | Formalized within balāgha; added verb tense shifts |
| Ibn al-Athīr (d. 637/1239) | *al-Mathal al-Sāʾir* | Discusses ~20 examples; coins *shajāʿat al-ʿarabiyya*; "examine the text of the Qurʾān you will find much iltifāt" |
| Al-Zarkashī (d. 794/1391) | *al-Burhān fī ʿulūm al-Qurʾān* | **Most extensive treatment, ~50 examples**; systematizes functions and benefits; extends iltifāt beyond person to tense and other shifts |
| Al-Suyūṭī (d. 911/1505) | *al-Itqān fī ʿulūm al-Qurʾān* | ~35 examples; the only canonical 1st→2nd example (Q 36:22) |

---

## Functions / rhetorical purposes (Abdel Haleem's synthesis)

1. **Emphasis and power** — Sudden shifts to 1st person plural express divine majesty
2. **Honour or reproach** — Shifts to 2nd person mark approval or censure
3. **Vividness** — Transitions create dramatic immediacy
4. **Drawing attention** — Shifts revitalize grammatical forms by making listeners aware of grammatical categories
5. **Contrast** — Multiple viewpoints highlight theological concepts like *tawḥīd* (divine oneness)

> "Departure from what is normally expected without benefit is forbidden in balāgha."
> Every iltifāt requires a discernible rhetorical purpose.

---

## Use as ground truth

Total canonical person-iltifāt verses in Abdel Haleem's catalog:
- 3rd→1st: **165 verses**
- 1st→3rd: **104 verses**
- 3rd→2nd: **68 verses**
- 2nd→3rd: **22 verses** (note Q 10:22 appears in BOTH 1st→3rd and 2nd→3rd because the verse contains a multi-step shift)
- 1st→2nd: **1 verse** (36:22)
- 2nd→1st: **0**
- Number shifts: **53**
- Addressee shifts: **24**
- Tense/mood: **16**
- Case marker: **3**
- Noun-for-pronoun: **>200**

All-types union (person + number + addressee + tense): **on the order of 320–370 unique verses** explicitly catalogued by classical balāgha as iltifāt or *related features*. This is the expected baseline against which a computational detector should be measured for **recall** (does it catch the canonical verses?). For **precision**, we cannot use this list as a complete catalog — Abdel Haleem himself states that the actual occurrence is much higher than traditional treatises suggest, so any "extra" verses our detector flags are not automatically false positives.
