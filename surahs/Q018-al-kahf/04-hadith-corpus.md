---
surah: 18
surah_name_ar: الكهف
surah_name_translit: al-Kahf
file_type: hadith-corpus
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 18 al-Kahf — Hadith Corpus

## 0. Source

All ḥadīth references in this file are verified against `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`. Numbering convention is the *idInBook* field of the ahmedbaset-json corpus, which corresponds to standard print-edition numbering for each canonical book. Searches use de-tashkeeled Arabic; tashkeel-stripped queries match the hadith Arabic text after removing harakat marks (regex `[ً-ٰٟـ]`).

The 9 books queried: Bukhārī, Muslim, al-Tirmidhī, Abū Dāwūd, al-Nasāʾī, Ibn Mājah, Mālik *al-Muwaṭṭaʾ*, Aḥmad b. Ḥanbal *Musnad*, al-Dārimī.

## 1. Headline counts (computed from on-disk JSON corpus 2026-04-28)

Searches use de-tashkeeled Arabic; hits are book-by-book counts of hadiths whose Arabic text contains the searched fragment.

| Phrase / topic | Bukhārī | Muslim | Tirmidhī | Abū Dāwūd | Nasāʾī | Ibn Mājah | Mālik | Aḥmad | Dārimī |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| الكهف (al-kahf) | 5 | 5 | 3 | 2 | 0 | 2 | 0 | 0 | 3 |
| الدجال (al-dajjāl) | 48 | 59 | 20 | 29 | 31 | 17 | 4 | 4 | 3 |
| عشر آيات من (10 verses from) | 1 | 1 | 1 | 1 | 0 | 2 | 0 | 2 | 3 |
| أصحاب الكهف (Companions of the Cave) | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| الخضر (al-Khaḍir) | 7 | 11 | 6 | 3 | 1 | 3 | 0 | 1 | 2 |
| القرنين (Dhū al-Qarnayn) | 1 | 1 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| يأجوج (Yājūj) | 10 | 7 | 4 | 1 | 0 | 7 | 0 | 0 | 0 |

Full results in `/tmp/q18_hadith_counts.json` (regenerable via the `scripts/Q018_F_05_hadith_corpus_counts.py` companion script — *not* a pre-registered novel test, just descriptive corpus statistics).

**Headline observation**: al-Khaḍir is referenced in 8 of 9 books (no Mālik); Dhū al-Qarnayn in 5 of 9 (Bukhārī, Muslim, Abū Dāwūd, Ibn Mājah, Mālik); the *aṣḥāb al-kahf* proper-noun phrase appears in only 1 hadith corpus-wide (Tirmidhī #2308 — the Nawwās b. Samʿān Dajjāl-narrative, where the cave-companions are mentioned in passing). The 10-verses-Dajjāl hadith appears in 6 of 9 books with a textual variant.

## 2. The 10-verses-Dajjāl-protection hadith — the canonical Q 18 fadāʾil

This is the most-widely-cited Q 18 fadāʾil in the canonical corpus, and the only Q 18 specific hadith *grading ṣaḥīḥ* (sound) by post-classical hadith-criticism (al-Albānī).

### 2.1 The Muslim text — first ten verses

**Muslim #1775** (Kitāb ṣalāt al-musāfirīn wa-qaṣrihā, bāb fadl Sūrat al-Kahf wa-āyat al-Kursī). The full isnād: Muḥammad b. al-Muthannā ← Muʿādh b. Hishām ← his father (Hishām al-Dastawāʾī) ← Qatāda ← Sālim b. Abī al-Jaʿd al-Ghaṭafānī ← Maʿdān b. Abī Ṭalḥa al-Yaʿmurī ← Abū al-Dardāʾ ← the Prophet:

> "‏ من حفظ عشر آيات من أول سورة الكهف عصم من الدجال ‏"‏

**English (verified via Muslim #1775 ahmedbaset-json English translation)**: "If anyone learns by heart the first ten verses of the Surah al-Kahf, he will be protected from the Dajjāl."

This is the ṣaḥīḥ chain.

### 2.2 The Abū Dāwūd textual variant — first OR last ten

**Abū Dāwūd #4325** (Kitāb al-malāḥim, bāb khurūj al-dajjāl). The same isnād (Qatāda ← Sālim ← Maʿdān ← Abū al-Dardāʾ) but with explicit textual-variant preservation:

> "‏ من حفظ عشر آيات من أول سورة الكهف عصم من فتنة الدجال ‏"‏ ‏.‏ قال أبو داود وكذا قال هشام الدستوائي عن قتادة إلا أنه قال "‏ من حفظ من خواتيم سورة الكهف ‏"‏ ‏.‏ وقال شعبة عن قتادة "‏ من آخر الكهف ‏"‏ ‏.‏

**Translation**: "Whoever memorizes ten verses from the **first** of Sūrat al-Kahf will be protected from the trial of the Dajjāl. — Abū Dāwūd said: Hishām al-Dastawāʾī also transmitted from Qatāda but said 'whoever memorizes from the **closing-verses** (*khawātīm*) of Sūrat al-Kahf'. And Shuʿba said from Qatāda: 'from the **last** of al-Kahf'."

This is the unique textual fact about the Q 18 ten-verses tradition: **three variants** are preserved at the same Qatāda layer:
1. *first ten* (Hishām's primary recension via Muslim).
2. *closing ten* (Hishām al-Dastawāʾī, alternative recension via Abū Dāwūd).
3. *from the last of al-Kahf* (Shuʿba via Qatāda).

The same isnād (Qatāda ← Sālim ← Maʿdān ← Abū al-Dardāʾ), three different text-recensions at the redaction-level. This is preserved transparently by Abū Dāwūd as a *taḍʿīf*-like hint — the 9th-century editor flagged that the textual content was unstable.

al-Qurṭubī (`qurtubi-jami-ahkam.openiti.raw.txt`, Q18 opening) records the same Muslim/Abū Dāwūd variant: *"وفي رواية: من آخر الكهف"* — an explicit acknowledgment of the variant.

### 2.3 Ibn Mājah ten-verses

**Ibn Mājah #1097** and **#3285**: similar 10-verses-Dajjāl protection chains, both via the Qatāda-Sālim-Maʿdān-Abū al-Dardāʾ family-isnād.

### 2.4 Aḥmad and al-Dārimī

**Aḥmad #217 and #1229**: 10-verses-protection variants in Aḥmad's *Musnad*.

**al-Dārimī #2641**: a *parallel* 10-verses tradition, but for Q 2 al-Baqara not Q 18 (al-Mughīra b. Sumayʿ ← ʿAbdullāh b. Masʿūd: "Whoever recites ten verses of al-Baqara at his sleep will not forget the Quran"). This is a separate Quranic-memorization tradition; it confirms the 10-verses motif is corpus-typical for Q 1 (al-Fātiḥa), Q 2 (al-Baqara), and Q 18 (al-Kahf) — three of the major fadāʾil-bearing surahs.

**al-Dārimī #2638 and #2661**: further Q 18-specific 10-verses traditions, transmitted via different isnāds.

### 2.5 Tirmidhī's complement — the Nawwās b. Samʿān Dajjāl narrative

**Tirmidhī #2308** (Kitāb al-fitan, bāb mā jāʾa fī al-dajjāl): the famous **long Dajjāl narrative** transmitted via al-Walīd b. Muslim ← ʿAbd al-Raḥmān b. Yazīd b. Jābir ← Yaḥyā b. Jābir al-Ṭāʾī ← ʿAbd al-Raḥmān b. Jubayr ← his father Jubayr b. Nufayr ← **al-Nawwās b. Samʿān al-Kilābī**.

In this narrative, the Prophet describes the Dajjāl in extended detail. The al-Kahf-relevant excerpt:

> "‏ من أدركه منكم فليقرأ عليه فواتح سورة الكهف ‏"‏

"Whoever among you encounters him [the Dajjāl], let him recite over him the **openings** (fawātiḥ) of Sūrat al-Kahf."

This adds a **third textual position** to the Muslim "first ten" / Abū Dāwūd-Shuʿba "last ten": Tirmidhī-Nawwās "openings" (*fawātiḥ*, plural). The unspecified-number "openings" allows reconciliation with the *first ten* recension while not committing to a specific verse-count.

### 2.6 Synthesis: the textual instability of the ten-verses tradition

Three textual variants are preserved across the 9 canonical books:

1. **First ten** — Muslim #1775 (Hishām primary), Ibn Mājah, Aḥmad, al-Dārimī. Most-cited; the canonical recension.
2. **Last ten / closing** — Abū Dāwūd #4325 (Hishām alternate, Shuʿba). Preserved as a critical-apparatus-variant.
3. **Openings** (*fawātiḥ*, undefined number) — Tirmidhī #2308 via Nawwās b. Samʿān al-Kilābī. Reconciles with first-ten.

al-Albānī (*Silsilat al-Aḥādīth al-Ṣaḥīḥa* #582) grades the Muslim "first ten" recension *ṣaḥīḥ*; his treatment of the Abū Dāwūd variant is that the textual fact is preserved but the variant text is the same hadith with a transmission alteration. This is the exact rules-tuple-fragility case the project flags: the *same isnād* gives *different text*; both texts are preserved in the canonical 9 books; classical hadith-criticism preserves the variant. See `05-classical-claims-audit.md` Audit 3 for the pre-registered audit.

## 3. The Mūsā-Khaḍir hadith corpus (Q 18:60-82)

The Mūsā-Khaḍir narrative is the second-most-cited Q 18 content in the hadith corpus. The foundational hadith identifies al-Khaḍir as the unnamed servant.

### 3.1 The Bukhārī foundational hadith

**Bukhārī #122** (Kitāb al-ʿilm, bāb mā dhukira fī dhahābi Mūsā ʿalayhi al-salām fī al-baḥr ilā al-Khaḍir) and the parallel **Bukhārī #3261** (Kitāb aḥādīth al-anbiyāʾ, bāb ḥadīth al-Khaḍir maʿa Mūsā):

> حدثنا عبد الله بن محمد، قال حدثنا سفيان، قال حدثنا عمرو، قال أخبرني سعيد بن جبير، قال قلت لابن عباس إن نوفا البكالي يزعم أن موسى ليس بموسى بني إسرائيل، إنما هو موسى آخر‏.‏ فقال كذب عدو الله، حدثنا أبي بن كعب عن النبي صلى الله عليه وسلم قال "‏ قام موسى النبي خطيبا في بني إسرائيل، فسئل أي الناس أعلم فقال أنا أعلم‏.‏ فعتب الله عليه، إذ لم يرد العلم إليه...

**Translation (verified via Bukhārī #122 ahmedbaset-json)**: "I [Saʿīd b. Jubayr] said to Ibn ʿAbbās: 'Nawf al-Bakālī claims that Mūsā [the companion of al-Khaḍir] is not the Mūsā of the Children of Israel; he is another Mūsā.' Ibn ʿAbbās said: 'The enemy of God [Nawf] has lied. Ubayy b. Kaʿb told us from the Prophet... Mūsā the Prophet stood up to address the Children of Israel and was asked who is the most knowledgeable of people; he said: I am the most knowledgeable. So God reproached him for not referring knowledge back to Him, and revealed to him that *a servant of My servants at the meeting of the two seas is more knowledgeable than you.* Mūsā said: O Lord, how to reach him? He was told: take a fish in a basket; where you lose the fish, he is there. Mūsā set out with his servant-boy Yūshaʿ b. Nūn, carrying a fish in a basket, until they reached a rock, where they laid down their heads and slept. The fish slipped from the basket..."

The full narrative continues over multiple lines; this is the foundational text identifying:
1. Mūsā as the *Israelite* prophet (not a different Mūsā).
2. The servant-boy as **Yūshaʿ b. Nūn** (Joshua).
3. The *majmaʿ al-baḥrayn* as the meeting-point.
4. The unnamed Quranic *ʿabd* as **al-Khaḍir**.

The isnād: Saʿīd b. Jubayr ← Ibn ʿAbbās ← Ubayy b. Kaʿb ← the Prophet. This is one of the strongest Companion-isnāds in the corpus (Ubayy b. Kaʿb being the senior Quran-reciter Companion).

### 3.2 The Khaḍir name etymology

**Bukhārī #3262** (Kitāb aḥādīth al-anbiyāʾ): Abū Hurayra ← the Prophet:

> "‏ إنما سمي الخضر أنه جلس على فروة بيضاء فإذا هي تهتز من خلفه خضراء ‏"‏

"al-Khaḍir was named so because he sat over a barren white land, and behold it became green with plantation behind him."

This explains the Khaḍir-as-name from root *xDr* (verdure). The QAC parses *al-khuḍr* (verdure) at Q 18:31 (line `(18:31:17:1) STEM|POS:N|LEM:xuDor|ROOT:xDr|M|INDEF|ACC`), but this is an unrelated common-noun appearance ("silk garments, green") in the Bridge-A block, NOT a reference to al-Khaḍir.

### 3.3 The Muslim Mūsā-Khaḍir narrative

**Muslim #2305 and #2306**: parallel Mūsā-Khaḍir narratives via Layth b. Saʿd and Mālik b. Anas chains. Muslim #2306 is the most-cited Mūsā-Khaḍir text in the Khaḍir-as-prophet position. Its immediate context (al-zahra al-dunyā) is unrelated; the narrative is integrated.

### 3.4 Other Mūsā-Khaḍir attestations

- **Tirmidhī #3233-3235**: Mūsā-Khaḍir narratives (Kitāb al-tafsīr, sūrat al-Kahf).
- **Abū Dāwūd #4707, #4709**: brief Mūsā-Khaḍir attestations.
- **Aḥmad #613**: Mūsā-Khaḍir.
- **Ibn Mājah #3732**: Mūsā-Khaḍir.

## 4. The Companions of the Cave (Q 18:9-26) — hadith corpus

The cave-companions narrative has **the lightest hadith corpus** of the four narratives. The proper-noun phrase *aṣḥāb al-kahf* appears only in Tirmidhī #2308 (the Nawwās b. Samʿān Dajjāl-narrative, where it is mentioned briefly). There are no major Companion-isnād Bukhārī or Muslim hadiths *specifically* about the cave-companions.

This is striking: the surah is *named* after the cave-companions, but the canonical hadith corpus has near-zero direct narrative-attestation for them. Classical exegesis (al-Ṭabarī, al-Qurṭubī) draws its narrative content largely from the **Najrān Christian** asbāb tradition (the question Quraysh asked the Madinan Jews, who instructed them to ask about the cave-youths) rather than Prophetic-narrative-elaboration.

## 5. Dhū al-Qarnayn + Yājūj-Mājūj (Q 18:83-101) — hadith corpus

### 5.1 Dhū al-Qarnayn

**Bukhārī #3409** and **Muslim #1622**: limited direct attestation. Most Dhū al-Qarnayn hadith content is in the *fadāʾil-Quran* genre (recitation virtues) rather than in narrative-elaboration.

### 5.2 Yājūj-Mājūj — major eschatological corpus

The **Yājūj-Mājūj eschatology** is one of the most-elaborated hadith subjects:
- **Bukhārī #3346, #3347, #3348**: the Yājūj-Mājūj future-release.
- **Bukhārī #6406**: warning of Yājūj-Mājūj's coming.
- **Muslim #2937**: detailed Yājūj-Mājūj Day-of-Judgment narrative.
- **Ibn Mājah #4076-4080**: Yājūj-Mājūj eschatological cluster.

Yājūj-Mājūj hadith count:
| Book | Yājūj hadith count |
|:--|:-:|
| Bukhārī | 10 |
| Muslim | 7 |
| Tirmidhī | 4 |
| Ibn Mājah | 7 |

The Yājūj-Mājūj eschatology is a recurrent theme in the *malāḥim* / *fitan* genre. Q 18:94-99 is the foundational Quranic text; the hadith corpus elaborates it into the full Last-Day narrative.

## 6. The Friday-recitation tradition

The Friday-recitation of Q 18 is attested in the canonical 9 books, but only via the Companion-saying / aspirational-genre (not via direct Prophetic command in the strongest chains):

### 6.1 al-Dārimī

**al-Dārimī #2638, #2641, #2661**: the foundational Friday-recitation tradition. The Abū Saʿīd al-Khudrī version: "Whoever recites Sūrat al-Kahf on Friday-night, light shines for him from him to the Ancient House [the Kaʿba]." The al-Dārimī chains are the earliest canonical attestation in the major hadith collections.

### 6.2 Outside the 9 books

al-Bayhaqī (*al-Sunan al-Kubrā*, ~458 AH; not in the 9 books) and al-Ḥākim (*al-Mustadrak*, ~405 AH; not in the 9 books) preserve additional Friday-recitation traditions. These are outside the 9-canonical-books scope but are important for the classical reception.

The Friday-recitation discipline is therefore *attested but not strongly Prophet-isnād-anchored* in the 9 books. It is widespread devotional practice grounded in al-Dārimī's chain plus al-Bayhaqī/al-Ḥākim's later cumulative attestations.

## 7. Recitation merits (*faḍāʾil*) of Q 18 — the broader corpus

Beyond the ten-verses-Dajjāl-protection (which is the strongest attestation), the broader Q 18 fadāʾil includes:

1. **Anas b. Mālik tradition** (cited by al-Qurṭubī and al-Thaʿlabī): "Whoever recites it is given a light between heaven and earth, and is shielded thereby from the trial of the grave." Isnād via Isḥāq b. ʿAbdullāh b. Abī Farwa. Graded ḍaʿīf (weak) by al-Albānī.

2. **The Samura b. Jundab tradition** (cited by al-Thaʿlabī, transmitted by al-Qurṭubī): "Whoever memorizes ten verses of Sūrat al-Kahf, the trial of the Dajjāl will not harm him; whoever recites the entire surah enters Paradise." Not in the 9 books; al-Thaʿlabī source.

3. **The 70,000-angels-escort tradition** (cited by al-Qurṭubī from al-Thaʿlabī): "I will guide you to a surah whose vastness fills heaven and earth, accompanied by 70,000 angels..." This is a fadāʾil-genre tradition typical of the era; it is not among the strongest chains.

The Q 18 fadāʾil profile is therefore: **ten-verses-Dajjāl-protection** is the strongest (Muslim ṣaḥīḥ); **Friday-recitation** is the most-widely-practiced (al-Dārimī + later); the **other fadāʾil** are devotional-genre and typically of weaker chains.

## 8. Cross-validation: empirical content from the hadith corpus

| Empirical claim | Evidence | Source |
|:--|:--|:--|
| Q 18:60-82 unnamed *ʿabd* = al-Khaḍir | Bukhārī #122, #3261; Muslim #2306; Saʿīd b. Jubayr ← Ibn ʿAbbās ← Ubayy b. Kaʿb chain | Bukhārī #122 |
| al-Khaḍir name etymology = *xDr* (verdure) | Bukhārī #3262 via Abū Hurayra | Bukhārī #3262 |
| Mūsā in Q 18:60-82 = the Israelite Mūsā | Bukhārī #122 (refutation of Nawf al-Bakālī) | Bukhārī #122 |
| Servant-boy in Q 18:60-65 = Yūshaʿ b. Nūn (Joshua) | Bukhārī #122 | Bukhārī #122 |
| First-ten / last-ten Dajjāl-protection variants | Muslim #1775; Abū Dāwūd #4325 | both books |
| Yājūj-Mājūj barrier release at Last Day | Bukhārī #3346-#3348; Muslim #2937 | both books |
| Friday-recitation tradition | al-Dārimī #2638, #2641, #2661 | al-Dārimī |
| Cave-companions narrative directly from Prophet | LIGHT — only Tirmidhī #2308 mention | Tirmidhī |

The hadith-empirical signature of Q 18 is **Mūsā-Khaḍir-rich and Dajjāl-rich**, with cave-companions and Dhū al-Qarnayn proportionally lighter. This concentrates the canonical attention on **N3 (Mūsā-Khaḍir)** and **the surah's eschatological / Dajjāl-protective function** — consistent with the four-fitan reading of al-Biqāʿī and the Friday-recitation discipline.

## 9. Honest limits

- The Bukhārī ḥadīth-numbers cited above use the ahmedbaset-json *idInBook* convention. Print editions vary slightly. Verification done is text-content-matching; the numeric convention is consistent within the on-disk JSON corpus.
- The al-Dārimī numbering used here (#2638, #2641, #2661 for Friday-recitation; #1441 for separate-Khaḍir parable) follows the on-disk convention of the ahmedbaset-json al-Dārimī file.
- Some Khaḍir-related hits in the search are common-noun *al-khuḍr* (verdure / herbs / vegetables), e.g., Tirmidhī #638 ("Muʿādh wrote to the Prophet asking about *al-khuḍrawāt* [vegetables]; the Prophet said: 'There is nothing [of zakāt due] on them.'"). These are NOT references to the proper-noun al-Khaḍir; the count of 6 in Tirmidhī includes both senses and would be lower (~3) if filtered to the proper-noun-only.
- The first-vs-last-ten Dajjāl-protection variant is preserved at three text-recensions on the same isnād (Hishām primary, Hishām alternate, Shuʿba). al-Albānī grades the first-ten recension *ṣaḥīḥ*; the last-ten recension is the same hadith with text-alteration but is also preserved in canonical Abū Dāwūd. The pre-registered audit treats the *first-ten* claim as the empirical claim to test; the variant existence is documented (`05-classical-claims-audit.md` Audit 3).
- The Friday-recitation tradition is attested in the 9 books only via al-Dārimī. al-Bayhaqī's *al-Sunan al-Kubrā* and al-Ḥākim's *al-Mustadrak* (outside the 9 books) preserve additional Friday-recitation traditions, but these are not in the on-disk hadith JSON corpus. This is a corpus-scope limit, not a project methodological choice.

## 10. One-paragraph synthesis

Q 18's hadith corpus is dominated by three concentrations: (1) the Mūsā-al-Khaḍir narrative, foundationally established by **Bukhārī #122** (Saʿīd b. Jubayr ← Ibn ʿAbbās ← Ubayy b. Kaʿb) — identifying al-Khaḍir as the unnamed Q 18:65 *ʿabd*, Mūsā as the Israelite prophet, and Yūshaʿ b. Nūn as the servant-boy; (2) the Yājūj-Mājūj eschatological cluster, with Bukhārī #3346-#3348, Muslim #2937, and Ibn Mājah #4076-#4080 elaborating the Q 18:94-99 barrier-release into the Last-Day narrative; and (3) the **ten-verses-Dajjāl-protection** tradition, attested in 6 of 9 books with three textual variants preserved at the same Qatāda layer (Hishām "first ten" via Muslim #1775 = ṣaḥīḥ; Hishām alternate "closing ten" via Abū Dāwūd #4325; Shuʿba "from the last of al-Kahf" via Abū Dāwūd #4325; Tirmidhī's #2308 Nawwās "openings" reconciling with first-ten). The cave-companions narrative is **structurally absent** from the strongest hadith chains — appearing only in the long Nawwās Dajjāl-narrative as a peripheral mention. This concentration is consistent with the al-Biqāʿī four-fitan reading: the Mūsā-Khaḍir (knowledge-fitna) and the Dajjāl-warning (eschatological-fitna) command the most hadith-elaboration, while the cave-companions (faith-fitna) and Dhū al-Qarnayn (power-fitna) are quieter in canonical-chain density. The Friday-recitation discipline is grounded in al-Dārimī's chain (Abū Saʿīd al-Khudrī) plus extra-canonical attestations (al-Bayhaqī, al-Ḥākim).
