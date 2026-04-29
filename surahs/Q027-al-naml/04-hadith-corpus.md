---
surah: 27
surah_name_ar: النمل
file_type: hadith-corpus
date_last_updated: 2026-04-28
phase: B+
verdict: SCAFFOLD — 9-book corpus searched; primary Q 27 hadiths catalogued
---

# Q 27 al-Naml — Ḥadīth Corpus

All ḥadīth citations below were extracted from the 9-book corpus at `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`. Search method: stripped-tashkeel substring search across the Arabic field. Full results saved to `csv/Q027_hadith_search_raw.json`. Numerous false-positives on "Sulaymān" arose because of the transmitter Sulaymān b. Ḥarb (and similar) appearing in isnād chains; these were excluded by topic-relevance filtering.

## 1. ⭐ The basmala-uniqueness ḥadīth (anchored to Q 27:30)

**Tirmidhī/al-Thaʿlabī chain**: from Ibn Burayda ← his father ← the Prophet:

> "Shall I not inform you of a verse that was not revealed to any prophet after Sulaymān b. Dāwūd except me?" I [Burayda] said: "Yes." He said: "With what do you open the recitation of the Qurʾān?" I said: "*bismi llāhi al-raḥmāni al-raḥīm*." He said: "It is, it is."

**Source(s)**:
- al-Thaʿlabī *al-Kashf wa-l-bayān* — preserved in `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/thaclabi-kashf-bayan.openiti.raw.txt` near offset of "إنه من سليمان وإنه" (see `03-tafsir-survey.md` §6).
- Ibn Kathīr *Tafsīr* — same chain via Ibn Abī Ḥātim (cited in `tafsir-quran.openiti.raw.txt`).

**Status**: this ḥadīth is the strongest narrative-level anchor for Q 27:30 as the *historical-introduction text* of the canonical basmala. Its grading varies (some chains weak); the Ibn Burayda-via-his-father chain is preserved in multiple compilers. **NOTE**: I could not match this exact ḥadīth in our 9-book JSON corpus by simple regex (the relevant phrasings did not pass strict filter); it appears in tafsir-borne chains rather than canonical 9-book chains. This is a known property — *fadāʾil*-of-basmala traditions are tafsir-rich, ḥadīth-light.

## 2. The four protected animals — Q 27 ecology in ḥadīth

This is the most-cited Q 27-related ḥadīth in the canonical 9 books: the Prophet forbade killing four animals. **Three of the four (ant, hoopoe, bee) appear in Q 27**.

### Abū Dāwūd #5269

**Arabic** (verbatim from JSON):
> حَدَّثَنَا أَحْمَدُ بْنُ حَنْبَلٍ، حَدَّثَنَا عَبْدُ الرَّزَّاقِ، حَدَّثَنَا مَعْمَرٌ، عَنِ الزُّهْرِيِّ، عَنْ عُبَيْدِ اللَّهِ بْنِ عَبْدِ اللَّهِ بْنِ عُتْبَةَ، عَنِ ابْنِ عَبَّاسٍ، قَالَ إِنَّ النَّبِيَّ صلى الله عليه وسلم نَهَى عَنْ قَتْلِ أَرْبَعٍ مِنَ الدَّوَابِّ النَّمْلَةُ وَالنَّحْلَةُ وَالهُدْهُدُ وَالصُّرَدُ

**English**:
> "The Prophet (ﷺ) prohibited to kill four creatures: ants, bees, hoopoes, and sparrow-hawks (al-ṣurad)."

### Parallel chains
- **Ibn Mājah #2959**: same prohibition; via Abū Hurayra (different chain): "*forbade killing shrikes (al-ṣurad), frogs, ants and hoopoes.*"
- **Ibn Mājah #2960**: same as Abū Dāwūd #5269 — via Ibn ʿAbbās.
- **Sunan al-Dārimī #1292**: same — via Ibn ʿAbbās.

**Significance**: the Prophet's prohibition is **specifically of the Q 27 ecology** (ants from v. 18, hoopoes from v. 20). This is one of the clearest empirical examples of *narrative-to-law* mapping: the surah's narrative content is preserved as Prophetic legal protection.

## 3. The ant-burning ḥadīth (Bukhārī, Muslim)

**Bukhārī #2897 (Kitāb al-Jihād)**:

> حَدَّثَنَا يَحْيَى بْنُ بُكَيْرٍ، حَدَّثَنَا اللَّيْثُ، عَنْ يُونُسَ، عَنِ ابْنِ شِهَابٍ، عَنْ سَعِيدِ بْنِ الْمُسَيَّبِ، وَأَبِي سَلَمَةَ أَنَّ أَبَا هُرَيْرَةَ ـ رضى الله عنه ـ قَالَ سَمِعْتُ رَسُولَ اللَّهِ صلى الله عليه وسلم يَقُولُ "قَرَصَتْ نَمْلَةٌ نَبِيًّا مِنَ الأَنْبِيَاءِ، فَأَمَرَ بِقَرْيَةِ النَّمْلِ فَأُحْرِقَتْ، فَأَوْحَى اللَّهُ إِلَيْهِ أَنْ قَرَصَتْكَ نَمْلَةٌ أَحْرَقْتَ أُمَّةً مِنَ الأُمَمِ تُسَبِّحُ اللَّهِ"

**English**:
> "I heard Allah's Messenger (ﷺ) saying: 'An ant bit a Prophet amongst the Prophets, and he ordered that the place of the ants be burnt. So, Allah inspired to him: It is because one ant bit you that you burnt a nation amongst the nations that glorify Allah?'"

**Muslim #5699 (idInBook)** — same incident, parallel chain through Anas via Hammād b. Salama:
> "An ant had bitten a Prophet (one amongst the earlier Prophets) and he ordered that the colony of the ants should be burnt. And Allah revealed to him: 'Because of an ant's bite you have burnt a community from amongst the communities which sings My glory.'"

**Significance**: the unnamed Prophet (some traditions name him Mūsā, others Sulaymān, others a generic *nabī*) is implicitly contrasted with **Q 27:18-19's Sulaymān**, who sees the ants and **smiles** rather than punishes them. Q 27 is the surah where ants are *protected* by a prophet; the ant-burning ḥadīth is the inverse case — the surah's morality is reinforced by its ḥadīth-counterpart.

## 4. The Beast (al-Dābba) — eschatological ḥadīth

**Tirmidhī #3271** (declared *ḥasan*):
> أَنَّ رَسُولَ اللَّهِ صلى الله عليه وسلم قَالَ "تَخْرُجُ الدَّابَّةُ مَعَهَا خَاتَمُ سُلَيْمَانَ وَعَصَا مُوسَى فَتَجْلُو وَجْهَ الْمُؤْمِنِ بِالْعَصَا وَتَخْتِمُ أَنْفَ الْكَافِرِ بِالْخَاتَمِ"

> "A beast will emerge from the earth. With it shall be the ring of Sulaymān and the staff of Mūsā. It will brighten the face of the believer with the staff, and stamp the nose of the disbeliever with the ring."

**Significance**: the Beast (al-Dābba) of **Q 27:82** carries the ring of Sulaymān (the surah's central character, vv. 15-44). This ḥadīth **reads Q 27:82 as a recovery / re-emergence** of the Sulaymanic seal. The eschatological closing of Q 27 thus *circles back* to its narrative center — a structural-semantic chiasmus the ḥadīth makes explicit.

## 5. The Beast among "six things to hasten before"

**Muslim #7214** (idInBook), via Abū Hurayra:
> "Hasten in performing these good deeds (before these) six things (happen): (the appearance) of the Dajjāl, the smoke (al-dukhān), the Beast of the earth (*dābbat al-arḍ*), the rising of the sun from the west, the general turmoil (specific to one), and the *amr al-ʿāmma*."

**Parallels**:
- **Muslim #303** (in *Kitāb al-Īmān*): "When three things appear faith will not benefit one who has not previously believed: the rising of the sun from its place of setting, the Dajjāl, and the Beast of the earth."
- **Muslim #7107** (idInBook 7107): the apartment-of-the-Prophet ḥadīth — eschatological signs.
- **Ibn Mājah #3793**: same six-signs list, via Anas b. Mālik.
- **Tirmidhī #3271** as above.

**Significance**: al-Dābba of Q 27:82 is **canonically an eschatological sign** in 9-book ḥadīth. It is cross-referenced with the Dajjāl, the smoke, the Sun-from-west, and other classical end-time markers. **Q 27 is thus a "creed" surah at its closing block** in a way that aligns with theological-iʿjāz (al-Khaṭṭābī's *iʿjāz al-maʿnā*) even though the surah's UAS-rank-23 places it on the structural-iʿjāz axis.

## 6. Q 27 sajda — prostration in recitation

**Ibn Mājah #790**:
> "I performed eleven prostrations with the Prophet (ﷺ) of which there were none in the *mufaṣṣal*. Al-Aʿrāf, al-Raʿd, al-Naḥl, Banī Isrāʾīl [Q 17], Maryam, al-Ḥajj, the prostration in al-Furqān, **Sūrat al-Naml**, the prostration of *al-sajda*, the prostration of *Ṣād*…" (text continues)

This places Q 27 in the canonical list of **sajda surahs** (surahs with a prostration verse during recitation). The prostration verse is **Q 27:25-26** — *al-sajdate-marker* in the verse-end at our text-rendered v.26 (the *innallāha lā ilāha illā huwa rabbu al-ʿarshi al-ʿaẓīm* — Lord of the Mighty Throne).

**Cross-validate**: Q 27 verse 26 in `quran-no-tashkeel.json`:
```
26 ألا يسجدوا لله الذي يخرج الخبء في السماوات والأرض ويعلم ما تخفون وما تعلنون
```
And the sajda-marker (۩) appears at the end of v.26, confirmed in our text.

## 7. *Fadāʾil* (virtues) traditions specific to Q 27 — DATA-GAP

I searched the 9-book corpus for *fadāʾil al-Naml* / *recite Sūrat al-Naml* but found no explicit canonical *fadāʾil*-tradition for the surah. The recitation-virtues traditions for Q 27 appear in:
- al-Suyūṭī *al-Durr al-manthūr* (some Ibn ʿAbbās narrations on the meaning of v.18 / v.30, as previously cited).
- al-Suyūṭī *Khaṣāʾiṣ al-kubrā* and *al-Itqān* (Q 27 as locus for *ījāz al-qaṣr*).

**Note**: this is consistent with `[[h-new-860-hadith-architectural-alignment]]` — Q 27 is a high-UAS surah but mid-low on the *fadāʾil*-frequency axis (the empirical orthogonality of structure-iʿjāz vs meaning-iʿjāz). The strongest theological "iʿjāz" here is the basmala-anchoring tradition (§1), but it is *tafsir-borne*, not *9-book-canonical*.

## 8. Summary table — by collection

| Collection | Q 27-relevant hits | Type |
|:--|:-:|:--|
| Bukhārī | 1 | The ant-burning ḥadīth (#2897) |
| Muslim | 6 | Ant-burning (#5699) + 5 al-Dābba ḥadīths |
| Tirmidhī | 3 | 1 al-Dābba (#3271) + 2 ant-related |
| Abū Dāwūd | 6 | 4 protected-animals + 1 Naml-sajda + 1 hoopoe |
| al-Nasāʾī | 1 | ant-related |
| Ibn Mājah | 9 | 5 protected-animals + 2 hoopoes + 1 al-Dābba + 1 sajda |
| Mālik *Muwaṭṭaʾ* | 0 | (no Q 27-specific aside from generic Sulaymān-isnād-noise) |
| Aḥmad *Musnad* | 0 | (similar — generic isnād noise) |
| al-Dārimī | 2 | protected-animals + hoopoe |

**Total**: ~28 distinct Q 27-relevant ḥadīths across 9-book corpus, all clustering on three motifs:
1. Q 27 ecology (ants, hoopoes, bees) — protected-animals legal tradition.
2. Q 27:82 al-Dābba — eschatological-signs traditions.
3. Q 27 as sajda-surah.

The "second basmala" itself is **not** the locus of canonical 9-book ḥadīth; its *fadāʾil*-traditions are tafsir-borne (Ibn Burayda chain).

## 9. Honest limits

- I did NOT manually verify every isnād grading. The Tirmidhī al-Dābba ḥadīth is graded *ḥasan* in standard editions; the Bukhārī ant ḥadīth is in the canonical *ṣaḥīḥ*. Other gradings should be checked against al-Albānī or al-Dāraquṭnī compilations for finer reading.
- The Ibn Burayda *hiya hiya* basmala-uniqueness ḥadīth was found in tafsir corpora (al-Thaʿlabī, Ibn Kathīr); my regex did not match it cleanly in the 9-book JSON. This may be a chain-citation issue (the JSON often abbreviates isnāds); a deeper search would resolve.
- Q 27 fadāʾil-DATA-GAP is genuine: I did not find any explicit *fadāʾil al-Naml* recitation-virtues ḥadīth in the canonical 9 books. al-Tirmidhī's *Sunan* has *fadāʾil al-Qurʾān* sections that name many surahs by virtue but not Q 27 specifically (further verification needed; flag for a focused future search).
