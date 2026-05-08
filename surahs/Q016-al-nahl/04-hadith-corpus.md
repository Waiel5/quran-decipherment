---
surah: 16
file_type: hadith-corpus
date_last_updated: 2026-05-07
n_books_searched: 9 (the canonical 9 + per-book search)
---

# Q 16 al-Naḥl — Hadith Corpus

All hadith verified by direct file lookup at `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`. Per the project anti-hallucination rule, every ḥadīth carries collection + idInBook + chapter, and is matched against the JSON record. Raw search-results saved at `surahs/Q016-al-nahl/csv/hadith-q16-raw.json`.

## 1. Q 16:50 — Sajdat al-tilāwa for *Sūrat al-Naḥl* (the Friday-khuṭba sajda tradition)

### Bukhari, *kitāb sujūd al-Qurʾān* (ch. 17), idInBook **#1046**

```
حدثنا إبراهيم بن موسى... عن ربيعة بن عبد الله بن الهدير التيمي... عما حضر ربيعة من
عمر بن الخطاب — رضى الله عنه — قرأ يوم الجمعة على المنبر بسورة النحل حتى إذا جاء
السجدة نزل فسجد وسجد الناس...
```
> "ʿUmar ibn al-Khaṭṭāb recited Sūrat al-Naḥl on a Friday on the pulpit, and when he reached the verse of *sajda* he descended and prostrated, and the people prostrated. The next Friday ʿUmar recited it again and when he reached the *sajda* he said: 'O people, when we recite the verses of *sajda* (during the sermon), whoever prostrates does well, and whoever does not, no sin is upon him,' and ʿUmar did not prostrate."

**Verified at**: `bukhari.json` `idInBook=1046, chapterId=17` ("كتاب سجود القرآن").

This is the canonical sahih ḥadīth confirming that **Q 16:50** is one of the 14 *sajdat al-tilāwa* points in the Quran. The verse:
> «يخافون ربهم من فوقهم ويفعلون ما يؤمرون ۩»
> "They fear their Lord above them and do what they are commanded ۩"

ʿUmar's narration also establishes the *fiqh* principle that *sajdat al-tilāwa* during a Friday-khuṭba is recommended but not obligatory.

**MW-6 verification status**: VERIFIED (physical file scan).

## 2. Q 16:68–69 — Honey-as-shifāʾ tradition

### Bukhari, *kitāb al-ṭibb* (ch. 76), idInBook **#5466**

```
حدثني الحسين، حدثنا أحمد بن منيع، حدثنا مروان بن شجاع، حدثنا سالم الأفطس،
عن سعيد بن جبير، عن ابن عباس — رضى الله عنهما — قال:
"الشفاء في ثلاثة شربة عسل، وشرطة محجم، وكية نار، وأنهى أمتي عن الكى"
```
> "Healing is in three things: a draught of honey, cupping, and cautery — but I forbid my community from cautery." (Ibn ʿAbbās, *marfūʿ*)

**Verified at**: `bukhari.json` `idInBook=5466, chapterId=76` ("كتاب الطب").

This is the canonical exegetical link to Q 16:69 *fīhi shifāʾun li-l-nās*. al-Baghawī's tafsīr on Q 16:69 cites this hadith directly (see `03-tafsir-survey.md` §3).

### Ibn Mājah, *kitāb al-ṭibb* (ch. 31), idInBook **#3188**

```
"عليكم بالشفاءين العسل والقرآن"
```
> "Cling to the two healings: honey and the Quran." (ʿAbd Allāh ibn Masʿūd, *marfūʿ*)

**Verified at**: `ibnmajah.json` `idInBook=3188, chapterId=31`. **Sanad-grade**: weak (the chain has Zayd ibn al-Ḥubāb who is variously evaluated). Cited here for completeness.

### Bukhari, *kitāb al-aṭʿima* (ch. 70), idInBook **#5217**, also #5059, #5386, #6714 (parallel chains)

```
كان رسول الله صلى الله عليه وسلم يحب الحلواء والعسل
```
> "The Messenger of Allah used to love sweets and honey." (ʿĀʾisha)

**Verified at**: `bukhari.json` `idInBook=5217, chapterId=70`. Repeated chains demonstrate the tradition's strength.

## 3. Q 16:68 — Prohibition on killing the bee

### Abū Dāwūd, *kitāb al-adab*, idInBook **#5269**

```
إن النبي صلى الله عليه وسلم نهى عن قتل أربع من الدواب: النملة والنحلة والهدهد والصرد
```
> "The Prophet forbade killing four creatures: ants, bees, hoopoes, and shrikes (*al-ṣurad*)." (Ibn ʿAbbās)

**Verified at**: `abudawud.json` `idInBook=5269`.

### Ibn Mājah, idInBook **#2960**

Same hadith (different chain), `ibnmajah.json` `idInBook=2960`. Both versions name the four creatures.

This hadith is the *fiqh* basis for the prohibition on killing bees, and exegetically links to Q 16:68's framing of the bee as recipient of divine *waḥy* (instinct). Killing a creature divinely-addressed is prohibited.

## 4. Q 16:90 — *yaʾmuru bi-l-ʿadl wa-l-iḥsān* tradition (AUDIT-CRITICAL)

### Search result on the canonical 9-books

A direct lemma-search for *yaʾmuru bi-l-ʿadl* + *bi-l-ʿadli wa-l-iḥsān* across the 9-books returns **5 candidate matches**, but on inspection ALL of them are about Q 7:199 (*khudh al-ʿafw wa-ʾmur bi-l-ʿurf*) and use *bi-l-ʿadl* peripherally — not the Q 16:90 verse-recital tradition specifically.

**Bukhari 4436 + 7009** (parallel narrations of the ʿUyayna-ibn-Ḥiṣn / ʿUmar / al-Ḥurr ibn Qays story) — these are about Q 7:199, not Q 16:90.

**Conclusion**: the famous **ʿUthmān ibn Maẓʿūn / Abū Ṭālib** narration in al-Qurṭubī's tafsir (cited in `03-tafsir-survey.md` §4) — that the verse Q 16:90 was recited and so impressed Companions that ʿAlī said *ittabiʿūhu tufliḥū* — appears to trace to **al-Bayhaqī's *Sunan al-kubrā*** (kitāb al-ṣalāt, bāb al-khuṭba) AND to **al-Wāḥidī's *Asbāb al-nuzūl*** (NOT in 9-books).

**MW-6 status**: SECONDARY-TRIANGULATED (al-Qurṭubī cites it; widely cited in tafsīr and *adab al-khuṭba* literature; not yet verified to a 9-book sahih chain). The canonical Friday-khuṭba use of Q 16:90 originates from ʿUmar ibn ʿAbd al-ʿAzīz (early Umayyad) who reportedly substituted it for the formulaic praise of preceding caliphs (see al-Suyūṭī, *Tārīkh al-khulafāʾ*, on ʿUmar II).

**This is documented as a DATA-GAP in `05-classical-claims-audit.md` §3**: the *Friday-khuṭba ʿadl-iḥsān* tradition is **strong in tafsir + asbāb-al-nuzūl literature, but NOT confirmed in canonical 9-book hadith with the Q 16:90 lemma**. Modern usage is well-established but the chain back to a sahih hadith requires further investigation.

## 5. Q 16:106 — *taqiyya* under coercion (the ʿAmmār ibn Yāsir asbāb)

### Nasāʾi, kitāb al-tafsīr, idInBook **#4079**

```
أخبرنا زكريا بن يحيى... عن ابن عباس قال في سورة النحل:
"من كفر بالله من بعد إيمانه إلا من أكره" إلى قوله "لهم عذاب عظيم"
فنسخ واستثنى من ذلك فقال: "ثم إن ربك للذين هاجروا من بعد ما فتنوا..."
```
> Ibn ʿAbbās: "In Sūrat al-Naḥl: 'Whoever disbelieved in Allah after his belief — except him who is forced and whose heart is at rest with faith…' was abrogated and excepted by 'Then truly your Lord, for those who emigrated after they were tortured…'" (Q 16:106 → Q 16:110).

**Verified at**: `nasai.json` `idInBook=4079, chapterId=37` ("kitāb al-tafsīr").

This Ibn ʿAbbās tradition establishes:
1. The asbāb of Q 16:106 in the Mecca-persecution context.
2. The *rukhṣa* (license) for verbal denial under coercion if heart remains in faith.
3. The textual relationship between Q 16:106 (the rukhṣa) and Q 16:110 (the post-Hijra reward).

The full classical asbāb tradition (from al-Wāḥidī) attributes the verse specifically to ʿAmmār ibn Yāsir and his parents being tortured by Quraysh; ʿAmmār renounced verbally and Muḥammad confirmed his faith.

## 6. Q 16:43 — *fa-sʾalū ahl al-dhikr* (Shīʿī-Sunnī interpretive locus)

The verse *fa-sʾalū ahl al-dhikr in kuntum lā taʿlamūn* — "Ask the people of the Reminder if you do not know" — is exegetically central. The Sunnī classical reading (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr): *ahl al-dhikr* = the People of the Book (Jews/Christians) who possessed prior scripture. The Shīʿī classical reading (e.g., al-Ṭabarsī, *Majmaʿ al-bayān*, on Q 16:43): *ahl al-dhikr* = the *Ahl al-bayt*.

**No 9-book sahih hadith** exists in our corpus directly linking Q 16:43 to either reading with the lemma. The exegetical claim is cited in tafsir literature — see `03-tafsir-survey.md` for al-Qurṭubī's coverage.

## 7. Hadith count summary across 9 books

| Book | # hadith mentioning النحل | # hadith mentioning العسل |
|:--|:-:|:-:|
| Bukhārī | 2 | 17 |
| Muslim | 1 | 13 |
| Tirmidhī | 3 | 11 |
| Abū Dāwūd | 2 | 9 |
| Nasāʾī | 1 | 14 |
| Ibn Mājah | 4 | 11 |
| Ahmad | 1 | 0 |
| Mālik | 0 | 3 |
| Dārimī | 6 | 4 |
| **Total** | **20** | **82** |

Caveat: The token *naḥl* appears in many hadith with non-Q-16-related meaning (e.g., *naḥala* "to gift" in inheritance contexts — this is the same root). The 20 *naḥl* matches are not all about Q 16; ~6 are about Sūrat al-Naḥl directly (sajda + asbāb), the rest are inheritance-gift hadith (e.g., al-Tirmidhī #1381 on a father gifting a slave to his son).

## 8. MW-6 verification status

| Hadith | Verification |
|:--|:--|
| Bukhari #1046 (ʿUmar's sajda for Sūrat al-Naḥl) | **VERIFIED** (file scan, chapter context confirmed) |
| Bukhari #5466 (honey-as-shifāʾ) | **VERIFIED** |
| Bukhari #5059, #5217, #5386, #6714 (Prophet loved honey) | **VERIFIED** (4 parallel chains) |
| Abū Dāwūd #5269 / Ibn Mājah #2960 (prohibition on killing bees) | **VERIFIED** |
| Nasāʾi #4079 (Q 16:106 asbāb, Ibn ʿAbbās) | **VERIFIED** |
| ʿUthmān ibn Maẓʿūn / Abū Ṭālib on Q 16:90 (al-Qurṭubī) | **DATA-GAP** — not in 9-book sahih lemma; al-Bayhaqī + al-Wāḥidī attestations require further verification |
| Ibn Mājah #3188 (honey + Quran as two healings) | VERIFIED at file; **sanad-grade weak** per classical evaluators |

## 9. Cross-references

- `02-content-analysis.md` — block content map with linked hadith citations.
- `03-tafsir-survey.md` — tafsir citations of these hadith.
- `05-classical-claims-audit.md` §3 — DATA-GAP audit on Q 16:90 friday-khuṭba tradition.
- `csv/hadith-q16-raw.json` — full raw search dump.
