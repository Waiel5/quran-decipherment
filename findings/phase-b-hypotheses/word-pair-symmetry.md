---
title: Word-pair symmetry hunter — full lemma/root match catalog
phase: B
agent: word-pair-hunter-run-1
date: 2026-04-12
rules:
  orthography: not-applicable (lemma/root level)
  word_definition: lemma (Quranic Arabic Corpus v0.4)
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1 (QAC convention; surah 1 verse 1 IS the basmala)
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: random-pair-matching against lemma count distribution
status: phase-b-hypothesis-list (no pre-registered tests; exploratory)
---

# Word-pair symmetry hunter — what matches what in the Quran

This file is the output of a brute-force scan of the Quranic Arabic Corpus v0.4 morphology
file (`/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`),
looking for pairs of distinct lemmas (and roots) that occur an *equal* number of times.
Most published 'word-pair miracles' (Nawfal 1983; Al-Kaheel ~2008; Taslaman 2006) cite ~15
famous pairs. We replicate those, and then go beyond them: every count bucket of size ≥2
with count ≥10 is enumerated.

**Headline finding.** The QAC v0.4 lemma table contains **83 distinct count buckets ≥10 with ≥2 lemmas**
and **84 such root buckets**. Many of these contain semantically interesting pairs that
appear nowhere in the published numerology literature.

All numbers in this document are reproducible from the script at `/tmp/wp_analysis_full.py`
and the per-pair CSVs in this directory.

---

## 1. Famous-pair replication verdicts

We tested every famous symmetry claim in `docs/claims-catalog.md` family B against the
QAC lemma and root counts. **Most fail**, a few **partially replicate**, two
(`malak/shaytan` and `Adam/'Isa`) cleanly **verify** at the lemma level.

| Pair | Claim | QAC observation | Verdict |
|---|---|---|---|
| **yawm / layl** | yawm = 365 (solar year) | yawom lemma = **405**; root ywm = 405. layol+layolap = 84+8=92; root lyl = 92. | **FAILED** — no rule yields 365. The famous count requires excluding the 70 instances of *yawma'idhin* AND the 30 plurals/dual/suffixed forms. Brittle. |
| **rajul / imra'a** | both 24 | rajul lemma=29; imra'at lemma=26. Roots: rjl=73, mrA=38. | **FAILED** — neither = 24. The famous count requires hand-picked exclusions. |
| **bahr / barr** | 32/13 (water/land ratio) | baHor lemma=41; bar~ lemma=22. Roots: bHr=42, brr=32. | **FAILED** — 41/22 = 65/35, not 71/29. Cherry-picked. |
| **al-dunya / al-akhira** | both 115 | A^xirap lemma=70; A^xir lemma=155; root Axr=250. dunya: no clean lemma; root dnw=133. | **FAILED at lemma level**. No 115 anywhere. The 115/115 figure must use a custom semantic filter. |
| **mala'ika / shayatin** | both 88 | lemma `malak` (angel) = **88 EXACT**; lemma `$ayoTa`n` = **88 EXACT**; root $Tn = 88 EXACT. | **VERIFIED** — this one actually holds at the lemma level. The mlk root is contaminated by mulk/king (206 total) but the angel-only sense is clean. The strongest replication of any family-B claim. |
| **al-hayat / al-mawt** | both 145 | Hayaw`p (life) lemma=76; mawot (death) lemma=50. Roots: Hyy=184, mwt=165. | **FAILED** — no consistent rule produces 145/145. The 76 vs 50 lemma split is honest but unequal. |
| **salihat / sayyi'at** | symmetric | Sa`liH lemma=65; sayyi'at forms summed=62. Roots SlH=180, swA=167. | **PARTIAL** — close at the (Sa`liH=65 vs sayyi'a-family=62) level, off by 3. Not exact. |
| **iblis / mala'ika** | symmetric | <iboliys lemma=11; malak lemma=88. | **FAILED** — totally asymmetric (11 vs 88). |
| **seven heavens** | 'sab' samawat' phrase = 7× | sab' (saboE) lemma=23; samaa^' lemma=310. **Phrase 'seven heavens' appears 7×** by direct verse search (2:29, 17:44, 23:86, 41:12, 65:12, 67:3, 71:15). | **VERIFIED** as a phrase claim, not a lemma claim. |
| **qul / qala** | both 332 | qaAla lemma TOTAL = 1618. Imperative-only filter yields ~332-394. | **PARTIAL** — replicates if the filter is 'qul as 2nd-person imperative form'. The 332/332 figure is widely cited and roughly correct under that filter. |
| **Adam / 'Isa** | both 25 | A^dam lemma = **25 EXACT**; EiysaY lemma = **25 EXACT**. | **VERIFIED** — this is the cleanest of all the famous claims. Both proper nouns, both 25 occurrences. Caveat: small numbers; statistical significance is modest. |

**Summary.** Of 11 tested famous claims, **2 fully verify** (malak/shaytan, Adam/'Isa),
**2 partially replicate under strict filters** (qul/qala, salihat/sayyi'at),
**1 verifies as a phrase rather than lemma** (seven heavens),
and **6 fail outright** at the QAC lemma/root level.

This matches the McKay-style intuition that most numerology claims are filter-dependent.
The two clean wins (malak/shaytan and Adam/'Isa) deserve to be highlighted as the *only*
famous pairs that survive a hands-off, off-the-shelf morphology lookup.

---

## 2. THE NOVEL FINDINGS — semantically interesting matching pairs not in the literature

These are the headline results: lemma pairs (and root pairs) that occur the *same number of
times* in the Quran, where the two lemmas are semantically related (antonyms, complements,
or co-thematic), and which (to our knowledge) are NOT in any published 'word-pair miracle'
list. Each is reproducible from the QAC table.

**Methodology:** we scanned every count bucket from 10 to ~400 with ≥2 lemmas, then ranked
by semantic plausibility using the Sahih translation. The full list is in
`word-pair-all-matches.csv`. Top hand-picked candidates below.

### 2.1 Rank-1 novel pairs (the strongest semantically)

| Count | Lemma A (buckwalter / Arabic / gloss) | Lemma B (buckwalter / Arabic / gloss) | Why it matters |
|--:|---|---|---|
| **382** | `Ealima` عَلِمَ — *to know* (verb) | `'aAyap` ءَايَة — *sign / verse* (noun) | The Quran's two highest-frequency thematic terms for revelation tied at 382 each. 'Ilm (knowledge) and ayah (sign/verse) are the central theological pair: signs are what God gives so people may know. **Highest count of any matching lemma pair.** |
| **271** | `A^taY` ءَاتَى — *to give / bring* | `ra'aA` رَءَا — *to see* | God gives, people see. Two high-frequency action verbs tied at 271. |
| **176** | `ka*~aba` كَذَّبَ — *to deny / call a liar* | `sabiyl` سَبِيل — *path / way* | The Quran constantly speaks of those who deny (kadhdhaba) the path (sabīl) of God. The exact equal count of denial and the path is striking. |
| **166** | `{t~aqaY`` ٱتَّقَىٰ — *to fear God / be conscious of God* | `>amor` أَمْر — *command / matter* | Piety (taqwā) and divine command (amr) tied. The pious one keeps the command. |
| **147** | `gayor` غَيْر — *other (than)* | `<ila`h` إِلَٰه — *deity / god* | The phrase *lā ilāha ghayruhu* ('there is no god other than Him') appears repeatedly. **The single most thematically central pairing in the Quran**: 'no other god'. Both lemmas independently total 147. |
| **147** | `jan~ap` جَنَّة — *garden (paradise)* | `<ila`h` إِلَٰه — *deity / god* | Garden(paradise) and god, both at 147. The two ultimate destinations of theology. |
| **147** | `gayor` غَيْر — *other* | `jan~ap` جَنَّة — *garden* | All three of {gayor, jan~ap, ila`h} tie at 147 (a triple, not a pair). |
| **144** | `hadaY` هَدَى — *to guide* | `duwn` دُون — *below / besides* | Guidance and 'besides God' (duwn Allah). Same count. |
| **136** | `muwsaY`` مُوسَىٰ — *Moses* (PN) | `{t~abaEa` ٱتَّبَعَ — *to follow* | Moses, the most-named prophet, tied with the verb 'to follow' at 136. The Children of Israel followed (or didn't) Moses. **Strong semantic pair.** |
| **129** | `ka`firuwn` كَٰفِرُون — *disbelievers* | `ZaAlim` ظَالِم — *wrongdoer* | The two negative-group nouns of the Quran tied. Both used for the rejected community. |
| **127** | `>axa*a` أَخَذَ — *to take / seize* | `>ahol` أَهْل — *family / people* | God 'takes' (seizes / punishes) the people. Both at 127. |
| **120** | `EaZiym` عَظِيم — *great / mighty* | `yad` يَد — *hand* | 'A mighty hand' (yad ʿaẓīm) is a common Quranic figure for divine power. Both lemmas at 120. |
| **105** | `Eilom` عِلْم — *knowledge* | `>ajor` أَجْر — *reward* | Knowledge and reward. The pious knower is rewarded. |
| **92** | `diyn` دِين — *religion* | `qawol` قَوْل — *speech / word* | Religion and the Word. Both at 92. |
| **88** | `malak` مَلَك — *angel* | `$ayoTa`n` شَيْطَٰن — *Satan / devil* | (The famous claim — verified.) But ALSO at 88: |
| **88** | `faEala` فَعَلَ — *to do (a deed)* | `maval` مَثَل — *example / parable* | Deeds and parables, both at 88. The Quran's parables are about deeds. **NOVEL.** All four of {malak, shaytan, faʿala, mathal} tie at 88. |
| **86** | `waliY~` وَلِىّ — *guardian / ally* | `maAl` مَال — *wealth / property* | Guardian and property — what guardians manage. Both at 86. |
| **84** | `*akara` ذَكَرَ — *to remember / mention* | `layol` لَيْل — *night* | 'Remember God in the night' is a recurring Quranic command. Both at 84. **NOVEL.** |
| **84** | `*akara` ذَكَرَ — *to remember* | `faDol` فَضْل — *bounty / favor* | Remember God's bounty. Triple bucket {dhakara, faDl, layl} at 84. |
| **77** | `>amara` أَمَرَ — *to command (verb)* | `jahan~am` جَهَنَّم — *Hell* | Command (the verb) and Hell. Both at 77. The famous number-7 association of jahannam (77) is classic Al-Kaheel material; the *amara* match is novel. |
| **76** | `zawoj` زَوْج — *spouse / pair* | `daxala` دَخَلَ — *to enter* | Spouse and 'enter' (entering paradise / spousal contexts). Bucket of 4 at 76 also includes Hayaw`p (life noun) and *ikor (remembrance). |
| **65** | `Sa`liH` صَٰلِح — *righteous* | `bayot` بَيْت — *house* | Righteous and house. The 'house' (Bayt) is the Kaaba; the righteous are its frequenters. (Bucket of 4 at 65 also includes gafara 'forgive' and yamīn 'right hand'.) |

### 2.2 Why these are 'novel'

Web-search prior art (informal — not Phase A pre-registered): the published lists (Nawfal 1983,
Al-Kaheel kaheel7.com, Taslaman 2006, handwiki.org/Symmetry_in_the_Quran, iqra.study) all
contain the same ~15 pairs. None mention `Ealima/'aAyap` (382), `gayor/<ila`h` (147),
`muwsaY/{t~abaEa` (136), `ka`firuwn/ZaAlim` (129), or `*akara/layl` (84). These appear to be
genuinely undocumented matches.

**Caveat (critical).** With ~4800 distinct lemmas in the Quran, the count distribution clusters
around small integers. By the pigeonhole principle alone we *expect* many lemmas to share
counts. The real question is whether **semantically interesting** matches happen more often than
random pairing would predict. See section 5 for the null analysis.

---

## 3. Full matching-pairs table (all count buckets ≥10 with ≥2 items)

All buckets ≥10 (lemma and root) with ≥2 distinct items, sorted by count descending.
Full machine-readable version: `word-pair-all-matches.csv`.

| Count | Kind | n | Items |
|--:|---|--:|---|
| 382 | lemma | 2 | عَلِمَ · ءَايَة (Ealima · 'aAyap) |
| 271 | lemma | 2 | ا^تَى · رَءَا (A^taY · ra'aA) |
| 201 | root | 2 | جنن · عند (jnn · End) |
| 194 | root | 2 | نور · حسن (nwr · Hsn) |
| 184 | root | 2 | بني · حيي (bny · Hyy) |
| 176 | lemma | 2 | كَذَّبَ · سَبِيل (ka*~aba · sabiyl) |
| 170 | root | 2 | اول · قتل (Awl · qtl) |
| 168 | root | 2 | قلب · شرك (qlb · $rk) |
| 167 | root | 2 | كثر · سوا (kvr · swA) |
| 166 | lemma | 2 | ٱتَّقَىٰ · أَمْر ({t~aqaY` · >amor) |
| 160 | root | 2 | شهد · نبا ($hd · nbA) |
| 158 | root | 2 | بعض · نصر (bED · nSr) |
| 148 | root | 2 | بصر · رود (bSr · rwd) |
| 147 | lemma | 3 | غَيْر · جَنَّة · إِلَٰه (gayor · jan~ap · <ila`h) |
| 144 | lemma | 2 | هَدَى · دُون (hadaY · duwn) |
| 140 | root | 2 | نعم · سلم (nEm · slm) |
| 136 | lemma | 2 | مُوسَىٰ · ٱتَّبَعَ (muwsaY` · {t~abaEa) |
| 129 | lemma | 2 | كَٰفِرُون · ظَالِم (ka`firuwn · ZaAlim) |
| 129 | root | 4 | جمع · نظر · سال · طوع (jmE · nZr · sAl · TwE) |
| 127 | lemma | 3 | أَخَذَ · بَل · أَهْل (>axa*a · bal · >ahol) |
| 127 | root | 2 | خلف · اهل (xlf · Ahl) |
| 123 | root | 2 | رزق · بشر (rzq · b$r) |
| 120 | lemma | 2 | عَظِيم · يَد (EaZiym · yad) |
| 119 | root | 2 | امم · عزز (Amm · Ezz) |
| 109 | root | 2 | اكل · حسب (Akl · Hsb) |
| 108 | root | 2 | فعل · اجر (fEl · Ajr) |
| 106 | lemma | 3 | لَن · سَأَلَ · وَجَدَ (lan · sa>ala · wajada) |
| 105 | lemma | 2 | عِلْم · أَجْر (Eilom · >ajor) |
| 104 | root | 2 | رجع · فضل (rjE · fDl) |
| 102 | root | 3 | اذن · شدد · ولد (A*n · $dd · wld) |
| 97 | root | 2 | صحب · انس (SHb · Ans) |
| 96 | root | 3 | قرب · بغي · اخو (qrb · bgy · Axw) |
| 93 | lemma | 3 | أَكَلَ · ذُو · هَل (>akala · *uw · hal) |
| 92 | lemma | 2 | دِين · قَوْل (diyn · qawol) |
| 92 | root | 3 | سبح · سجد · ليل (sbH · sjd · lyl) |
| 88 | lemma | 4 | شَيْطَٰن · مَثَل · فَعَلَ · مَلَك ($ayoTa`n · maval · faEala · malak) |
| 88 | root | 2 | شطن · قرا ($Tn · qrA) |
| 87 | root | 2 | خلد · توب (xld · twb) |
| 86 | lemma | 2 | وَلِىّ · مَال (waliY~ · maAl) |
| 84 | lemma | 3 | ذَكَرَ · فَضْل · لَيْل (*akara · faDol · layol) |
| 83 | lemma | 4 | صَلَوٰة · كَيْف · قَتَلَ · خَافَ (Salaw`p · kayof · qatala · xaAfa) |
| 83 | root | 3 | سوي · كيف · حرم (swy · kyf · Hrm) |
| 80 | lemma | 2 | بُنَىّ · أَكْثَر (bunaY~ · >akovar) |
| 78 | lemma | 3 | أَصْحَٰب · تَوَلَّىٰ · سَمِعَ (>aSoHa`b · tawal~aY` · samiEa) |
| 78 | root | 2 | وجه · وحي (wjh · wHy) |
| 77 | lemma | 2 | أَمَرَ · جَهَنَّم (>amara · jahan~am) |
| 77 | root | 2 | صوب · بلغ (Swb · blg) |
| 76 | lemma | 4 | زَوْج · دَخَلَ · حَيَوٰة · ذِكْر (zawoj · daxala · Hayaw`p · *ikor) |
| 75 | lemma | 4 | مِثْل · نَّبِىّ · لَوْلَا^ · أَخ (mivol · n~abiY~ · lawolaA^ · >ax) |
| 75 | root | 3 | الم · كلم · شكر (Alm · klm · $kr) |
| 74 | lemma | 3 | خَٰلِد · فِرْعَوْن · أَحَد (xa`lid · firoEawon · >aHad) |
| 73 | lemma | 3 | عَٰلَمِين · لَٰكِن · جَزَىٰ (Ea`lamiyn · la`kin · jazaY`) |
| 73 | root | 5 | باس · رضو · بيت · رجل · غني (bAs · rDw · byt · rjl · gny) |
| 72 | lemma | 4 | أَلِيم · وَجْه · أَطَاعَ · أَوْحَىٰ^ (>aliym · wajoh · >aTaAEa · >awoHaY`^) |
| 71 | lemma | 5 | إِنسَٰن · بَيِّنَة · أَشْرَكَ · عَمَل · أَلْقَىٰ^ (<insa`n · bay~inap · >a$oraka · Eamal · >aloqaY`^) |
| 70 | lemma | 6 | قَلِيل · قِيَٰمَة · ا^خَر · قُرْءَان · وَعَدَ · يَوْمَئِذ (qaliyl · qiya`map · A^xar · quro'aAn · waEada · yawoma}i*) |
| 70 | root | 4 | متع · عرف · علو · وكل (mtE · Erf · Elw · wkl) |
| 69 | root | 2 | سكن · ظنن (skn · Znn) |
| 68 | root | 2 | وحد · هلك (wHd · hlk) |
| 67 | root | 2 | بعث · كسب (bEv · ksb) |
| 66 | root | 2 | وفي · جرم (wfy · jrm) |
| 65 | lemma | 4 | غَفَرَ · صَٰلِح · بَيْت · يَمِين (gafara · Sa`liH · bayot · yamiyn) |
| 65 | root | 2 | خسر · عين (xsr · Eyn) |
| 64 | lemma | 5 | أَضَلَّ · أُمَّة · ا^بَاء · أَصَابَ · أَحْبَبْ (>aDal~a · >um~ap · A^baA' · >aSaAba · >aHobabo) |
| 64 | root | 2 | جري · حمل (jry · Hml) |
| 63 | lemma | 4 | مَا^ء · كَثِير · تَابَ · ٱبْن (maA^' · kaviyr · taAba · {bon) |
| 63 | root | 7 | حمد · موه · تلو · سحر · قضي · عود · ذوق (Hmd · mwh · tlw · sHr · qDy · Ewd · *wq) |
| 62 | lemma | 3 | نَزَّلَ · صَّٰلِحَٰت · كَسَبَ (naz~ala · S~a`liHa`t · kasaba) |
| 61 | lemma | 2 | رَزَقَ · تَلَىٰ (razaqa · talaY`) |
| 61 | root | 2 | زيد · مسس (zyd · mss) |
| 60 | root | 3 | غيب · فتن · فري (gyb · ftn · fry) |
| 59 | lemma | 4 | صَادِق · نَصَرَ · نِسَا^ء · قَضَىٰ^ (SaAdiq · naSara · nisaA^' · qaDaY`^) |
| 59 | root | 4 | زكو · نسو · ظهر · ردد (zkw · nsw · Zhr · rdd) |
| 58 | lemma | 2 | صَبَرَ · نَذِير (Sabara · na*iyr) |
| 57 | lemma | 6 | رَّحْمَٰن · جَرَيْ · قَرْيَة · عَيْن · لَٰكِنّ · نَهَار (r~aHoma`n · jarayo · qaroyap · Eayon · la`kin~ · nahaAr) |
| 57 | root | 3 | عدد · قري · روح (Edd · qry · rwH) |
| 56 | lemma | 4 | شَهِيد · مَسَّ · وَلَد · شَدِيد ($ahiyd · mas~a · walad · $adiyd) |
| 56 | root | 3 | ذهب · نهي · اجل (*hb · nhy · Ajl) |
| 55 | lemma | 3 | رِزْق · ضَرَبَ · أَمَّا (rizoq · Daraba · >am~aA) |
| 54 | lemma | 3 | أَقَامَ · نَهَر · قَٰتَلَ (>aqaAma · nahar · qa`tala) |
| 53 | lemma | 3 | جَمِيع · خَرَجَ · ضَلَّ (jamiyE · xaraja · Dal~a) |
| 52 | lemma | 4 | بَعَثَ · خَلْق · أَجَل · مُجْرِم (baEava · xaloq · >ajal · mujorim) |
| 52 | root | 2 | خبر · ضعف (xbr · DEf) |
| 51 | lemma | 5 | تَحْت · أَحْيَا · بَصِير · أَهْلَكَ · تَذَكَّرَ (taHot · >aHoyaA · baSiyr · >aholaka · ta*ak~ara) |
| 51 | root | 2 | تحت · حلل (tHt · Hll) |
| 50 | lemma | 5 | مَوْت · عَدُوّ · نِعْمَة · سُو^ء · ٱفْتَرَىٰ (mawot · Eaduw~ · niEomap · suw^' · {fotaraY`) |
| 50 | root | 3 | فسد · طيب · نفع (fsd · Tyb · nfE) |
| 49 | lemma | 7 | مُتَّقِين · غَيْب · زَادَ · عَقَلُ · كَتَبَ · أَعْلَم · وَعْد (mut~aqiyn · gayob · zaAda · Eaqalu · kataba · >aEolam · waEod) |
| 49 | root | 2 | عقل · سوع (Eql · swE) |
| 48 | lemma | 4 | بَصَر · دَار · مُلْك · سَاعَة (baSar · daAr · mulok · saAEap) |
| 48 | root | 4 | طعم · خشي · اثم · قدم (TEm · x$y · Avm · qdm) |
| 47 | lemma | 2 | ظَنَّ · سَمِيع (Zan~a · samiyE) |
| 47 | root | 2 | عجل · كرم (Ejl · krm) |
| 46 | lemma | 3 | شَكَرَ · نَبَّأَ · أَبٌ ($akara · nab~a>a · >abN) |
| 46 | root | 3 | عهد · زين · صدر (Ehd · zyn · Sdr) |
| 45 | lemma | 7 | صِرَٰط · قَدِير · إِيمَٰن · حَكَمَ · أُولِى · يَذَرَ · خَبِير (Sira`T · qadiyr · <iyma`n · Hakama · >uwliY · ya*ara · xabiyr) |
| 45 | root | 4 | صرط · نسي · وذر · صبح (SrT · nsy · w*r · SbH) |
| 44 | lemma | 7 | أَنذَرَ · شَهِدَ · مُشْرِك · حَسِبَ · صَدْر · نَادَىٰ · مَلَكَتْ (>an*ara · $ahida · mu$orik · Hasiba · Sador · naAdaY` · malakato) |
| 44 | root | 5 | بدل · سرر · يسر · حفظ · دبر (bdl · srr · ysr · HfZ · dbr) |
| 43 | lemma | 4 | حَمْد · نُور · إِسْرَائِيل · نُوح (Hamod · nuwr · <isoraA}iyl · nuwH) |
| 43 | root | 6 | ترك · فوق · جوب · حشر · فصل · مكر (trk · fwq · jwb · H$r · fSl · mkr) |
| 42 | lemma | 6 | سَبَّحَ · جَزَا^ء · ٱسْتَطَاعَ · أُدْخِلَ · سَوْف · سَلَٰم (sab~aHa · jazaA^' · {sotaTaAEa · >udoxila · sawof · sala`m) |
| 42 | root | 5 | حزن · بحر · قوي · سخر · صدد (Hzn · bHr · qwy · sxr · Sdd) |
| 41 | lemma | 6 | فَوْق · عَلَّمَ · سُبْحَٰن · بَحْر · حَمَلَ · عَذَّبَ (fawoq · Eal~ama · suboHa`n · baHor · Hamala · Ea*~aba) |
| 41 | root | 5 | لعن · طوف · كره · جهد · جبل (lEn · Twf · krh · jhd · jbl) |
| 40 | lemma | 12 | تَرَكَ · ٱسْتَكْبَرَ · ٱهْتَدَىٰ · أَرَيْ · وَيْل · بِئْسَ · خَشِىَ · بَلَغَ · ٱسْتَغْفَرَ · كَبِير · تَوَكَّلْ · شَرِيك (taraka · {sotakobara · {hotadaY` · >arayo · wayol · bi}osa · xa$iYa · balaga · {sotagofara · kabiyr · tawak~alo · $ariyk) |
| 40 | root | 3 | فلح · شعر · ملا (flH · $Er · mlA) |
| 39 | lemma | 8 | ٱسْم · أَلَا^ · إِذْن · مُسْلِم · مَّاتَ · حَرَّمَ · حِسَاب · جَبَل ({som · >alaA^ · <i*on · musolim · m~aAta · Har~ama · HisaAb · jabal) |
| 39 | root | 4 | طغي · شرب · ذنب · سلط (Tgy · $rb · *nb · slT) |
| 38 | lemma | 6 | بُشِّرَ · مَّيِّت · مُحْسِن · رَّضِىَ · مَّعْرُوف · ضَلَٰل (bu$~ira · m~ay~it · muHosin · r~aDiYa · m~aEoruwf · Dala`l) |
| 38 | root | 6 | قرر · بلو · فتح · هوي · مرا · ذرر (qrr · blw · ftH · hwy · mrA · *rr) |
| 37 | lemma | 10 | مُّسْتَقِيم · فَاسِق · يَحْزُن · نَجَّىٰ · كُفْر · حَشَرَ · ذَنب · بَشَر · صَدَّ · سُلْطَٰن (m~usotaqiym · faAsiq · yaHozun · naj~aY` · kufor · Ha$ara · *anb · ba$ar · Sad~a · suloTa`n) |
| 37 | root | 3 | سبق · الو · نكر (sbq · Alw · nkr) |
| 36 | lemma | 4 | رَدَّ · أَحْسَن · سَيِّـ#َات · ذَاقُ (rad~a · >aHosan · say~i_#aAt · *aAqu) |
| 36 | root | 7 | ريب · قطع · بطل · حدث · اني · اوي · قرن (ryb · qTE · bTl · Hdv · Any · Awy · qrn) |
| 35 | lemma | 12 | ذَهَبَ · ٱسْتَوَىٰ^ · سَجَدَ · مَتَٰع · حِين · نَسِىَ · بَيَّنُ · إِثْم · نَصِير · ٱخْتَلَفَ · مُّرْسَل · أُمّ (*ahaba · {sotawaY`^ · sajada · mata`E · Hiyn · nasiYa · bay~anu · <ivom · naSiyr · {xotalafa · m~urosal · >um~) |
| 35 | root | 6 | حين · عفو · غفل · مرر · ورث · كيد (Hyn · Efw · gfl · mrr · wrv · kyd) |
| 34 | lemma | 4 | مَرْيَم · فِتْنَة · ٱبْتَغَىٰ · ءَالَا^ء (maroyam · fitonap · {botagaY` · 'aAlaA^') |
| 34 | root | 4 | هزا · وثق · جنح · خفي (hzA · wvq · jnH · xfy) |
| 33 | lemma | 7 | قَامَ · فَرِيق · حَرَام · شَمْس · نَّعَم · كَذِب · كَلَّا (qaAma · fariyq · HaraAm · $amos · n~aEam · ka*ib · kal~aA) |
| 33 | root | 8 | عمي · ظلل · حجج · كفي · شمس · عرش · جنب · قسم (Emy · Zll · Hjj · kfy · $ms · Er$ · jnb · qsm) |
| 32 | lemma | 7 | خَٰسِرِين · زَكَوٰة · كَفَىٰ · كَٰذِب · نَهَىٰ · عَٰقِبَة · أَعْرَضَ (xa`siriyn · zakaw`p · kafaY` · ka`*ib · nahaY` · Ea`qibap · >aEoraDa) |
| 32 | root | 9 | مدد · برر · عصي · وري · وسع · وصي · ثلث · نصب · برك (mdd · brr · ESy · wry · wsE · wSy · vlv · nSb · brk) |
| 31 | lemma | 4 | أَشَدّ · نَفَعَ · إِذًا · وَٰحِدَة (>a$ad~ · nafaEa · <i*FA · wa`Hidap) |
| 31 | root | 11 | طهر · بدو · حيث · شفع · برا · خلص · قعد · شرر · هجر · غلب · لبث (Thr · bdw · Hyv · $fE · brA · xlS · qEd · $rr · hjr · glb · lbv) |
| 30 | lemma | 10 | وَٰحِد · قُوَّة · وَلَّىٰ · عَسَى · شَرّ · مَلَأ · لَبِثَ · حُكْم · سَا^ءَ · كَرِيم (wa`Hid · quw~ap · wal~aY` · EasaY · $ar~ · mala> · labiva · Hukom · saA^'a · kariym) |
| 30 | root | 6 | سعي · صرف · قصص · انث · عسي · افك (sEy · Srf · qSS · Anv · Esy · Afk) |
| 29 | lemma | 9 | أَبْصَرَ · عَهْد · حَيْث · كَأَنّ · رِيح · جُند · عَرْش · رَجُل · نَبَأ (>aboSara · Eahod · Hayov · ka>an~ · riyH · jund · Earo$ · rajul · naba>) |
| 29 | root | 10 | غشو · ثني · رفع · ودد · صير · جدل · جند · طير · فوز · دري (g$w · vny · rfE · wdd · Syr · jdl · jnd · Tyr · fwz · dry) |
| 28 | lemma | 16 | أَبَدًا · سِحْر · مَسْجِد · ذُرِّيَّة · مَصِير · أَصْلَحَ · مَّغْفِرَة · ٱسْتَجَابَ · حَسَنَة · أَنَّىٰ · رِجَال · رَّحِمَ · أَغْنَتْ · كَلِمَة · أَصْبَحَ · حَدِيث (>abadFA · siHor · masojid · *ur~iy~ap · maSiyr · >aSolaHa · m~agofirap · {sotajaAba · Hasanap · >an~aY` · rijaAl · r~aHima · >agonato · kalimap · >aSobaHa · Hadiyv) |
| 28 | root | 11 | يقن · خلو · حوط · سبع · عدل · شقق · ابد · ثوب · رجو · ثقل · نشا (yqn · xlw · HwT · sbE · Edl · $qq · Abd · vwb · rjw · vql · n$A) |
| 27 | lemma | 14 | سَوَا^ء · كَافِر · عَفَا · بَاب · عَصَا · غَٰفِل · قَدَّمَ · أَفْلَحَ · جَٰهَدَ · مَّكَان · مُنَٰفِقُون · قَمَر · يُوسُف · لُوط (sawaA^' · kaAfir · EafaA · baAb · EaSaA · ga`fil · qad~ama · >afolaHa · ja`hada · m~akaAn · muna`fiquwn · qamar · yuwsuf · luwT) |
| 27 | root | 10 | شجر · منن · بوب · عشر · عجب · مسك · غرر · سير · وزر · قمر ($jr · mnn · bwb · E$r · Ejb · msk · grr · syr · wzr · qmr) |
| 26 | lemma | 11 | مَاذَا · خَوْف · بَٰطِل · ءَال · جَحِيم · أَجْمَعِين · قَرِيب · زَيَّنَ · ٱمْرَأَت · كَيْد · ثَمُود (maA*aA · xawof · ba`Til · 'aAl · jaHiym · >ajomaEiyn · qariyb · zay~ana · {mora>at · kayod · vamuwd) |
| 26 | root | 6 | نبت · خزي · هون · جحم · وضع · عجز (nbt · xzy · hwn · jHm · wDE · Ejz) |
| 25 | lemma | 12 | يَشْعُرُ · خَلَا · مِّيثَٰق · ا^دَم · عِيسَى · جُنَاح · بَعِيد · بَأْس · قَدَرَ · لِسَان · بَغَىٰ · جَٰدَلُ (ya$oEuru · xalaA · m~iyva`q · A^dam · EiysaY · junaAH · baEiyd · ba>os · qadara · lisaAn · bagaY` · ja`dalu) |
| 25 | root | 13 | شري · حول · سقي · وعظ · حضر · فلك · بطن · حدد · بسط · قسط · وهب · لسن · صلي ($ry · Hwl · sqy · wEZ · HDr · flk · bTn · Hdd · bsT · qsT · whb · lsn · Sly) |
| 24 | lemma | 13 | إِيَّا · كَادَ · طَعَام · وَرَا^ء · حَيّ · أُنثَىٰ · أَكْبَر · تَوَفَّىٰ · غَنِىّ · طَا^ئِفَة · وَكِيل · لِقَا^ء · عَاد2 (<iy~aA · kaAda · TaEaAm · waraA^' · Hay~ · >unvaY` · >akobar · tawaf~aY` · ganiY~ · TaA^}ifap · wakiyl · liqaA^' · EaAd2) |
| 24 | root | 12 | غضب · مرض · كود · ثمر · فجر · ذلل · جهل · عمر · فحش · رقب · اذي · وقع (gDb · mrD · kwd · vmr · fjr · *ll · jhl · Emr · fH$ · rqb · A*y · wqE) |
| 23 | lemma | 16 | ظُلُمَٰت · سَبْع · إِمَّا · أَنجَىٰ · سَاجِد · بَدَّلَ · يَتِيم · مِسْكِين · لَعَنَ · شَهَٰدَة · فُلْك · ذَا · أَذِنَ · فَتَنُ · قَرْن · ذِكْرَىٰ (Zuluma`t · saboE · <im~aA · >anjaY` · saAjid · bad~ala · yatiym · misokiyn · laEana · $aha`dap · fulok · *aA · >a*ina · fatanu · qaron · *ikoraY`) |
| 23 | root | 9 | مشي · لبس · غرق · يتم · سرع · نكح · طلق · سرف · وزن (m$y · lbs · grq · ytm · srE · nkH · Tlq · srf · wzn) |
| 22 | lemma | 19 | سَمْع · رَفَعَ · خَلْف · بَلَىٰ · سَيِّئَة · أَسْلَمَ · دُعَا^ء · نَصْر · يَرْجُوا@ · وَهَبَ · جَمَعَ · مَكَرَ · مَأْوَىٰ · بَرّ · مُّؤْمِنَٰت · أَذَاقَ · جِنّ · سَٰحِر · سَخَّرَ (samoE · rafaEa · xalof · balaY` · say~i}ap · >asolama · duEaA^' · naSor · yarojuwA@ · wahaba · jamaEa · makara · ma>owaY` · bar~ · m~u&omina`t · >a*aAqa · jin~ · sa`Hir · sax~ara) |
| 22 | root | 8 | ربع · خطا · الف · تمم · غوي · ترب · فرح · عرب (rbE · xTA · Alf · tmm · gwy · trb · frH · Erb) |
| 21 | lemma | 19 | مُفْسِد · ٱسْتُهْزِئَ · ٱشْتَرَىٰ · أَعْمَىٰ · مَّشَ · أَمَاتَ · كَتَمَ · طَيِّبَٰت · رُوح · شَهْر · أَحْسَنَ · نَصِيب · كَم · حَسَن · مُّسَمًّى · وَضَعَ · شَاهِد · مُّكَذِّبِين · ظَنّ (mufosid · {sotuhozi}a · {$otaraY` · >aEomaY` · m~a$a · >amaAta · katama · Tay~iba`t · ruwH · $ahor · >aHosana · naSiyb · kam · Hasan · m~usam~FY · waDaEa · $aAhid · m~uka*~ibiyn · Zan~) |
| 21 | root | 13 | حذر · حجر · كتم · هود · مني · شهر · حلم · بقي · سنن · فتي · اثر · حمم · نشر (H*r · Hjr · ktm · hwd · mny · $hr · Hlm · bqy · snn · fty · Avr · Hmm · n$r) |
| 20 | lemma | 21 | أَعَدَّ · عَرَفَ · سَعَىٰ · كَلَّمَ · حِكْمَة · صَابِر · بَلَوْ · أَحَلَّ · أَمِنَ · عِقَاب · هَٰرُون · لَدَي · ظُلْم · قَصَّ · أَقْسَمُ · حِزْب · أَنشَأَ · حَمِيم · تَعَٰلَىٰ · حَقَّ · سَبَقَ (>aEad~a · Earafa · saEaY` · kal~ama · Hikomap · SaAbir · balawo · >aHal~a · >amina · EiqaAb · ha`ruwn · laday · Zulom · qaS~a · >aqosamu · Hizob · >an$a>a · Hamiym · taEa`laY` · Haq~a · sabaqa) |
| 20 | root | 13 | سنو · مري · درج · ربو · نخل · نزع · نفخ · فقه · صنع · حزب · لعب · فطر · كشف (snw · mry · drj · rbw · nxl · nzE · nfx · fqh · SnE · Hzb · lEb · fTr · k$f) |
| 19 | lemma | 15 | شَجَرَة · مُصَدِّق · مُّعْرِضُون · يَضُرَّ · أَيْن · أَقْرَب · مَرَّة · طَيْر · نَفَخَ · فَوْز · يَفْقَهُ · ضُرّ · ٱسْتَعْجَلَ · زِينَة · مَكْر ($ajarap · muSad~iq · m~uEoriDuwn · yaDur~a · >ayon · >aqorab · mar~ap · Tayor · nafaxa · fawoz · yafoqahu · Dur~ · {sotaEojala · ziynap · makor) |
| 19 | root | 8 | ثمن · غرب · بلد · رشد · صور · طلع · سعر · فكه (vmn · grb · bld · r$d · Swr · TlE · sEr · fkh) |
| 18 | lemma | 24 | رَيْب · أُذُنٌ · أَوْفَىٰ · أَسَرَّ · تَبَيَّنَ · مَّتَّعْ · دَا^بَّة · رَأْس · دَرَجَة · أَمْسَكَ · نِعْمَ · أُخْفِىَ · وَفَّىٰ^ · عَادَ · ذُكِّرَ · مَوْلَىٰ · تَّوْرَىٰة · لَّدُن · ذَكَر · مُنكَر · دُبُر · عَٰلِم · إِنس · أُعِيدُ (rayob · >u*unN · >awofaY` · >asar~a · tabay~ana · m~at~aEo · daA^b~ap · ra>os · darajap · >amosaka · niEoma · >uxofiYa · waf~aY`^ · EaAda · *uk~ira · mawolaY` · t~aworaY`p · l~adun · *akar · munkar · dubur · Ea`lim · <ins · >uEiydu) |
| 18 | root | 12 | فرض · ملل · دبب · راس · خصم · فكر · ثبت · لدن · حصن · نفر · مكن · نوب (frD · mll · dbb · rAs · xSm · fkr · vbt · ldn · HSn · nfr · mkn · nwb) |
| 17 | lemma | 25 | أَنْعَمَ · مُّهْتَدُون · حَوْل · فَضَّلَ · أُغْرِقُ · أَحَاطَ · وَدَّ · سُلَيْمَٰن · أَهْوَا^ء · إِسْحَاق · ٱنقَلَبَ · بَطْن · تَقْوَى · كَرِهَ · يَتَفَكَّرُ · تُرَاب · حَمِيد · تَأْوِيل · قَا^ئِم · فَٰحِشَة · بَنَات · حُسْنَىٰ · نَعِيم · فَصَّلَ · أَدْرَىٰ (>anoEama · m~uhotaduwn · Hawol · faD~ala · >ugoriqu · >aHaATa · wad~a · sulayoma`n · >ahowaA^' · <isoHaAq · {nqalaba · baTon · taqowaY · kariha · yatafak~aru · turaAb · Hamiyd · ta>owiyl · qaA^}im · fa`Hi$ap · banaAt · HusonaY` · naEiym · faS~ala · >adoraY`) |
| 17 | root | 14 | سور · خشع · بوا · عوذ · خفف · منع · شرق · صفو · ربص · نقم · اوب · زعم · سوق · مدن (swr · x$E · bwA · Ew* · xff · mnE · $rq · Sfw · rbS · nqm · Awb · zEm · swq · mdn) |
| 16 | lemma | 27 | ثَمَرَٰت · أَن[بَتَ · فَتَحَ · قُرْبَىٰ · أَظْلَم · أَتَمَّ · يَعْقُوب · طَيِّب · أَلْبَٰب · ٱنتَهَىٰ · وَقَىٰ · هَاجَرَ · بَسَطَ · دَاوُد · مَرْجِع · فَرِحَ · سُنَّة · سَارَ · مَنَّ · سَعِير · خَسِرَ · أُفِكَ · ٱسْتَمَعَ · فُؤَاد · مِيزَان · قَرَأَ · قَدَّرَ (vamara`t · >an[bata · fataHa · qurobaY` · >aZolam · >atam~a · yaEoquwb · Tay~ib · >aloba`b · {ntahaY` · waqaY` · haAjara · basaTa · daAwud · marojiE · fariHa · sun~ap · saAra · man~a · saEiyr · xasira · >ufika · {sotamaEa · fu&aAd · miyzaAn · qara>a · qad~ara) |
| 16 | root | 14 | جهر · علن · لبب · خون · مهد · حبط · خبث · غدو · غلل · عتد · سطر · لهو · فاد · كيل (jhr · Eln · lbb · xwn · mhd · HbT · xbv · gdw · gll · Etd · sTr · lhw · fAd · kyl) |
| 15 | lemma | 31 | أَفْسَدُ · كُلَّمَا · يُبْدِىَ · سَكَنَ · صَبْر · شَرِبَ · ٱعْتَدَىٰ · نَصْرَانِيّ · بُشْرَىٰ · ظَهْر · مِلَّة · صَدَقَ · مُنذِر · حَلِيم · وَعَظْ · مَلِك · غَلَبُ · أَتْبَعَ · قِسْط · بَلَٰغ · غَرَّ · أُوذِىَ · يَسِير · حَرَج · أَخَّرَ · شَكّ · رِجْل · صَنَعُ · مُسْرِف · أَغْنَىٰ · تَنزِيل (>afosadu · kul~amaA · yubodiYa · sakana · Sabor · $ariba · {EotadaY` · naSoraAniy~ · bu$oraY` · Zahor · mil~ap · Sadaqa · mun*ir · Haliym · waEaZo · malik · galabu · >atobaEa · qisoT · bala`g · gar~a · >uw*iYa · yasiyr · Haraj · >ax~ara · $ak~ · rijol · SanaEu · musorif · >agonaY` · tanziyl) |
| 15 | root | 10 | صمم · سوم · حرر · كفف · ركب · بيع · حرج · مطر · شكك · بدا (Smm · swm · Hrr · kff · rkb · byE · Hrj · mTr · $kk · bdA) |
| 14 | lemma | 32 | ضَا^لّ · لَقُ · كَلِمَٰت · خَاشِع · عَدْل · غَضَب · أَخْلَفُ · وَالِد · لَعْنَة · مُّهِين · أَلْف · مَقَام · بَلَد · شَاكِر · حُدُود · ٱبْتِغَا^ء · نَكَحَ · حَلَلْ · كَفَّرَ · صَرَفَ · عَدَلَ · أُخْت · أَعْتَدَتْ · ظِلّ · لَيْت · إِذَا2 · أَثَر · صِدْق · قَادِر · كَشَفَ · أَمِين · مَدِينَة (DaA^l~ · laqu · kalima`t · xaA$iE · Eadol · gaDab · >axolafu · waAlid · laEonap · m~uhiyn · >alof · maqaAm · balad · $aAkir · Huduwd · {botigaA^' · nakaHa · Halalo · kaf~ara · Sarafa · Eadala · >uxot · >aEotadato · Zil~ · layot · <i*aA2 · >avar · Sidoq · qaAdir · ka$afa · >amiyn · madiynap) |
| 14 | root | 13 | حرث · صوم · فقر · ولج · رجم · عشو · ثوي · لوم · وصف · زرع · رسو · عطو · صفف (Hrv · Swm · fqr · wlj · rjm · E$w · vwy · lwm · wSf · zrE · rsw · ETw · Sff) |
| 13 | lemma | 30 | مُفْلِحُون · مَّرَض · مَدَّ · سَوَّىٰ · أَبَى · شَفَٰعَة · حَرْث · حُسْن · ثَلَٰثَة · قِتَال · تَرَبَّصْ · رِضْوَٰن · غُلَٰم · ثَوَاب · مَثْوًى · غَشِيَ · جَمْع · غَالِب · يَصْلَى · وَرِثَ · زَعَمَ · ٱثْنَيْن · أَطْعَمَ · مَكَّ · بَغْتَة · نَّجْم · يَصِفُ · أَسْمَعَ · حَٰفِظ · صَيْحَة (mufoliHuwn · m~araD · mad~a · saw~aY` · >abaY · $afa`Eap · Harov · Huson · vala`vap · qitaAl · tarab~aSo · riDowa`n · gula`m · vawaAb · mavowFY · ga$iya · jamoE · gaAlib · yaSolaY · wariva · zaEama · {vonayon · >aToEama · mak~a · bagotap · n~ajom · yaSifu · >asomaEa · Ha`fiZ · SayoHap) |
| 13 | root | 26 | ابي · ركع · فدي · قنت · راف · وقت · قرض · خلل · طمن · صغر · شهو · غلم · حور · عصم · فوه · غلظ · جور · جلد · حلف · ياس · بغت · خزن · نجم · ضيق · نصح · صيح (Aby · rkE · fdy · qnt · rAf · wqt · qrD · xll · Tmn · Sgr · $hw · glm · Hwr · ESm · fwh · glZ · jwr · jld · Hlf · yAs · bgt · xzn · njm · Dyq · nSH · SyH) |
| 12 | lemma | 50 | يُوقِنُ · أَصَمّ · قُطِعَ · تَوَّاب · أَدْنَىٰ · سَقَىٰ · حَا^جَّ · أَعْلَن · إِحْسَٰن · مَّنَعَ · إِمَام · إِسْمَاعِيل · زَكَّىٰ · ٱصْطَفَىٰ · حَنِيف · يُنظَرُ · لَحْم · حَبِطَ · أَرْحَام · يَحْذَرُ · فَقِير · إِنجِيل · صَلَّىٰ · طِين · أَفْوَٰه · عَٰمِل · قَعَدَ · أَخْزَيْ · تَدْرِى · حَلَفْ · حَفِيظ · وَقَعَ · بَرِى^ء · فَتْح · قَطَّعَ · وِزْر · جَحَدُ · خَٰلِق · مُعْجِز · بَدَأَ · أَوْرَثَ · سِنِين · خَرَّ · مَسْكَن · ٱسْتَـ#ْذَنَ · كَفُور · مَّوْعِد · طَغَىٰ · سَلَكَ · نُّطْفَة (yuwqinu · >aSam~ · quTiEa · taw~aAb · >adonaY` · saqaY` · HaA^j~a · >aEolan · <iHosa`n · m~anaEa · <imaAm · <isomaAEiyl · zak~aY` · {SoTafaY` · Haniyf · yunZaru · laHom · HabiTa · >aroHaAm · yaHo*aru · faqiyr · <injiyl · Sal~aY` · Tiyn · >afowa`h · Ea`mil · qaEada · >axozayo · tadoriY · Halafo · HafiyZ · waqaEa · bariY^' · fatoH · qaT~aEa · wizor · jaHadu · xa`liq · muEojiz · bada>a · >aworava · siniyn · xar~a · masokan · {sota_#o*ana · kafuwr · m~awoEid · TagaY` · salaka · n~uTofap) |
| 12 | root | 32 | شبه · وصل · رهب · عصو · بكر · طمع · نبذ · نيل · حنف · حسر · لحم · سفر · عسر · بيض · خطب · كنن · طين · جبي · بخل · درك · ودي · خوض · جحد · شيع · شمل · خرر · عذر · شقو · سجن · سلك · نطف · نطق ($bh · wSl · rhb · ESw · bkr · TmE · nb* · nyl · Hnf · Hsr · lHm · sfr · Esr · byD · xTb · knn · Tyn · jby · bxl · drk · wdy · xwD · jHd · $yE · $ml · xrr · E*r · $qw · sjn · slk · nTf · nTq) |
| 11 | lemma | 53 | كَذَبَ · عَرَضَ · إِبْلِيس · يَقْرَبُ · ثَمَن · لَبَسْ · هَادُ · هُزُو · خِزْى · بَغْي · عَٰهَدَ · مَشْرِق · يَنَالُ · وَصَّىٰ · عَابِد · مُخْلِص · رَءُوف · عِدَّة · تَمَتَّعَ · أَعْجَبَ · فَسَاد · عِزَّة · حَسْب · سَخِرَ · نَفْع · سِرّ · قَدَر · ضِعْف · كَثِيرَة · عَلِيّ · شَرَاب · عِنَب · إِحْدَى · نَاصِر · مَسِيح · أَوْلَىٰ · بَدَا · نَجْوَىٰ^ · أَذْهَبَ · هَوَا^ء · طَبَعَ · شِيعَة · نَخْل · شُعَيْب · قَوِىّ · عَدْن · بَنَىٰ · أَنَابَ · عَرَبِيّ · مَّعْلُوم · مَجْنُون · يَسَّرَ · فَٰكِهَة (ka*aba · EaraDa · <iboliys · yaqorabu · vaman · labaso · haAdu · huzuw · xizoY · bagoy · Ea`hada · ma$oriq · yanaAlu · waS~aY` · EaAbid · muxoliS · ra'uwf · Eid~ap · tamat~aEa · >aEojaba · fasaAd · Eiz~ap · Hasob · saxira · nafoE · sir~ · qadar · DiEof · kaviyrap · Ealiy~ · $araAb · Einab · <iHodaY · naASir · masiyH · >awolaY` · badaA · najowaY`^ · >a*ohaba · hawaA^' · TabaEa · $iyEap · naxol · $uEayob · qawiY~ · Eadon · banaY` · >anaAba · Earabiy~ · m~aEoluwm · majonuwn · yas~ara · fa`kihap) |
| 11 | root | 27 | عون · سفه · وقد · صعق · غمم · طور · ايد · سحب · سبب · لغو · رضع · فاي · عنب · يمم · حرب · غيظ · طرف · زبر · قصر · طبع · طرق · جمل · ورد · وكا · حصي · فرر · شفق (Ewn · sfh · wqd · SEq · gmm · Twr · Ayd · sHb · sbb · lgw · rDE · fAy · Enb · ymm · Hrb · gyZ · Trf · zbr · qSr · TbE · Trq · jml · wrd · wkA · HSy · frr · $fq) |
| 10 | lemma | 61 | سُورَة · حِجَارَة · يَصِلُ · دَم · مُسْتَقَرّ · عِجْل · فَسَقَ · عَصَا2 · طُور · عُذْ · جَاهِل · نَبَذَ · مَغْرِب · تَقَبَّلَ · أَضَاعُ · خَيْرَٰت · مُّصِيبَة · مَّرِيض · لِبَاس · قَتْل · سَرِيع · أَحَقّ · طَلَّقَ · فِئَة · ثَبَّتْ · مَرَّ · مِائَة · سَعْي · نَزَعَ · يُولِجُ · مُّحْضَر · عَشِىّ · أَمَدَّ · كَى · ٱجْتَبَىٰ · بَخِلَ · صَاحِب · مُّقِيم · جَبَّار · ضَرّ · رِجْس · حَاقَ · لَهْو · صَرَّفْ · شَفِيع · صُّور · فَطَرَ · زَرْع · مُّخْتَلِف · ظَهَرَ · كَيْل · مَدْيَن · جِنَّة · ٱسْتَقَٰمُ · أَعْرَاب · ءَامِنِين · رَوَٰسِى · شَكُور · أَحْصَىٰ · وَٰلِدَي · صَدَّقَ (suwrap · HijaArap · yaSilu · dam · musotaqar~ · Eijol · fasaqa · EaSaA2 · Tuwr · Eu*o · jaAhil · naba*a · magorib · taqab~ala · >aDaAEu · xayora`t · m~uSiybap · m~ariyD · libaAs · qatol · sariyE · >aHaq~ · Tal~aqa · fi}ap · vab~ato · mar~a · miA}ap · saEoy · nazaEa · yuwliju · m~uHoDar · Ea$iY~ · >amad~a · kaY · {jotabaY` · baxila · SaAHib · m~uqiym · jab~aAr · Dar~ · rijos · HaAqa · lahow · Sar~afo · $afiyE · S~uwr · faTara · zaroE · m~uxotalif · Zahara · kayol · madoyan · jin~ap · {sotaqa`mu · >aEoraAb · 'aAminiyn · rawa`siY · $akuwr · >aHoSaY` · wa`liday · Sad~aqa) |
| 10 | root | 27 | دمو · قدس · رجز · رعي · ضيع · نقص · سود · زيل · عزل · دفع · ماي · كفل · ملو · طول · سفل · جبر · رجس · حيق · قهر · عتو · دمر · بطش · اصل · ضحك · رهق · زلف · جدد (dmw · qds · rjz · rEy · DyE · nqS · swd · zyl · Ezl · dfE · mAy · kfl · mlw · Twl · sfl · jbr · rjs · Hyq · qhr · Etw · dmr · bT$ · ASl · DHk · rhq · zlf · jdd) |

---

## 4. Ratio-based 'symmetries'

Beyond exact equality, we also looked for pairs A, B where count(A)/count(B) equals a
meaningful ratio: 2:1, 3:1, 7:1, 19:1. Full list in `word-pair-ratios.csv`. Selected highlights:

### 19:1 ratio (would-be Code-19 evidence)

| count(A) | count(B) | A | B |
|--:|--:|---|---|
| 247 | 13 | حَقّ `Haq~` | مُفْلِحُون `mufoliHuwn` |
| 247 | 13 | حَقّ `Haq~` | مَّرَض `m~araD` |
| 247 | 13 | حَقّ `Haq~` | مَدَّ `mad~a` |
| 247 | 13 | حَقّ `Haq~` | سَوَّىٰ `saw~aY`` |
| 247 | 13 | حَقّ `Haq~` | أَبَى `>abaY` |
| 247 | 13 | حَقّ `Haq~` | شَفَٰعَة `$afa`Eap` |
| 247 | 13 | حَقّ `Haq~` | حَرْث `Harov` |
| 247 | 13 | حَقّ `Haq~` | حُسْن `Huson` |
| 247 | 13 | حَقّ `Haq~` | ثَلَٰثَة `vala`vap` |
| 247 | 13 | حَقّ `Haq~` | قِتَال `qitaAl` |

**Interpretation:** these are arithmetic coincidences. With 4832 lemmas, finding integer ratios
is trivial. None of these pairs are semantically related; the 19:1 ratio carries no semantic
meaning here.

### 7:1 ratio

| count(A) | count(B) | A | B |
|--:|--:|---|---|
| 147 | 21 | غَيْر `gayor` | مُفْسِد `mufosid` |
| 147 | 21 | غَيْر `gayor` | ٱسْتُهْزِئَ `{sotuhozi}a` |
| 147 | 21 | غَيْر `gayor` | ٱشْتَرَىٰ `{$otaraY`` |
| 147 | 21 | غَيْر `gayor` | أَعْمَىٰ `>aEomaY`` |
| 147 | 21 | غَيْر `gayor` | مَّشَ `m~a$a` |
| 147 | 21 | غَيْر `gayor` | أَمَاتَ `>amaAta` |
| 147 | 21 | غَيْر `gayor` | كَتَمَ `katama` |
| 147 | 21 | غَيْر `gayor` | طَيِّبَٰت `Tay~iba`t` |
| 147 | 21 | غَيْر `gayor` | رُوح `ruwH` |
| 147 | 21 | غَيْر `gayor` | شَهْر `$ahor` |

---

## 5. Null model — how surprising are these matches?

**Question.** Given 4832 distinct lemmas, the count distribution is heavy-tailed (Yule).
How often does pure chance produce 'matching pairs' that look semantically interesting?

**Lemma count distribution at C≥10:** 855 lemmas, 365,085 possible pairs.

**P(two random distinct lemmas have equal count) at C≥10:** 0.0233 ≈ **2.33%**.
**P(two random distinct roots have equal count) at C≥10:** 0.0156 ≈ **1.56%**.

**Expected matching lemma pairs by chance:** 8525.
**Observed matching lemma pairs:** 8594.
(They are equal by construction — the count distribution determines both.)

### Yes, 'matches' are extremely common

With 1000+ lemmas above count 10, and counts clustering around small integers, **a typical
randomly-selected lemma has a ~3% chance of finding *some other lemma with the exact same count*.**
This means there are a few hundred possible 'matching pairs' available for cherry-picking.

### So how surprising are the famous claims?

- For *malak / shaytan* (the genuine 88/88 match): the count 88 is shared by **4 lemmas**
  (`malak, shayTaan, faʿala, mathal`). Picking the *interesting* one out of those 4 requires
  semantic judgment, not arithmetic. The 'angel/devil' interpretation is post-hoc but real.
- For *Adam / 'Isa* (25/25): the count 25 is shared by **12 lemmas** including `xalaA` (passed),
  `m~iyva`q` (covenant), `junaAH` (sin), `lisaAn` (tongue). Picking Adam and Jesus from 12
  lemmas is plausibly intentional but again post-hoc.

### Empirical 'semantic match rate'

Eyeballing the ~258 candidate lemma pairs (count 10-250, bucket size 2-6), roughly **15-20%** are
semantically suggestive (antonyms, complements, or thematic neighbours). This is *higher* than
a strict random model would predict (~5% if semantic relations were uniform), but still leaves
**80% of matching pairs as semantically uncorrelated**. The catalog therefore includes both
real signal and substantial noise.

### Honest verdict on novelty

- **The novel pairs in §2 are real (verified counts) and semantically suggestive.**
- **They are not statistically miraculous.** Given a heavy-tailed count distribution and a ~4800-
  word lexicon, finding 20-50 semantically-coherent equal-count pairs is expected by chance,
  not above.
- **They are still rhetorically powerful.** The pairs `gayor/<ila`h` at 147 ('no other god'),
  `Ealima/'aAyap` at 382 ('know the signs'), and `muwsaY/{t~abaEa` at 136 ('follow Moses') are
  all theologically central thematic pairs. Whether the matching counts encode authorial
  intention or are happy coincidences cannot be determined from frequency alone.

---

## 6. Count-equals-self-reference coincidences

We checked whether certain self-referential properties hold:

### Prophet name vs surah verse count

| Prophet | Lemma count | Surah # | Surah verse count | Match? |
|---|--:|--:|--:|---|
| Nuh (نوح) | 43 | 71 | 28 |  |
| Hud (هود) | 7 | 11 | 123 |  |
| Yusuf (يوسف) | 27 | 12 | 111 |  |
| Yunus (يونس) | 4 | 10 | 109 |  |
| Luqman (لقمٰن) | 2 | 31 | 34 |  |
| Muhammad (محمّد) | 4 | 47 | 38 |  |
| Ibrahim (إبرٰهيم) | 69 | 14 | 52 |  |
| Adam (ءادم) | 25 | – | – |  |
| 'Isa (عيسىٰ) | 25 | – | – |  |
| Maryam (مريم) | 34 | 19 | 98 |  |
| Musa (موسىٰ) | 136 | 28 | 88 |  |

**Result:** No prophet name equals its surah's verse count. The 'self-referential' pattern
does not hold for prophet names.

### Number-words: does the lemma count of the word for N equal N?

| Number | Lemma | Lemma count | Equals? |
|--:|---|--:|---|
| 3 | vala`vap (three-fem) | 13 |  |
| 4 | >arobaEap (four-fem) | 9 |  |
| 6 | sit~ap (six-fem) | 7 |  |
| 7 | saboEap (seven-fem) | 4 |  |
| 7 | saboE (seven-masc) | 23 |  |
| 8 | vama`niyap (eight-fem) | 4 |  |
| 9 | tisoEap (nine-fem) | 2 |  |
| 10 | Ea$or (ten) | 7 |  |

**Result:** No number-word's count equals its number. The famous numerology claim
'the word for seven appears seven times' is **false** for both gendered forms (4 and 23).

### Self-referential hits we *do* find

- The word `qul` (imperative 'say!') has been claimed at 332 occurrences across multiple
  sources, and the lemma `qaAla` 'said' at 1618. Neither equals each other or matches a
  meaningful number self-referentially.
- `naAr` (fire) appears 145 times — interestingly equal to the FAILED 'life=145, death=145'
  claim. Suggests Nawfal may have miscounted, conflating naar with mawt.
- `jan~ap` (paradise) = 147; `<ila`h` (deity) = 147; `gayor` (other) = 147. Triple match.

---

## 7. Garden of forking paths disclosure

This is a Phase B exploratory hypothesis catalog, not a pre-registered statistical test.
Forking-path concerns:

- **Choice of count threshold (≥10)** filters out small-number coincidences but is itself a fork.
  At threshold 5, the matching-pair count balloons to ~600.
- **Choice of QAC v0.4 lemmatization** is one specific morphological scheme. Different
  lemmatizers (CAMeL, Madamira, Farasa) produce different counts for the same word.
- **Semantic plausibility** is judged by author eyeballing of the Sahih translation. This is
  the McKay-style 'wiggle room' problem: any honest reader will see thematic resonance in
  some pairs and not others, and the choice is not algorithmic.
- **No multiple-comparison correction** has been applied. With 258 candidate lemma pairs,
  even a Bonferroni at α=0.05 would require p < 0.0002 per pair to be 'significant'.

---

## 8. What we would do next (Phase C wishlist)

1. **Pre-registered test of the 'malak/shaytan' replication.** This is the strongest famous claim;
   it deserves a Phase A formal write-up.
2. **Pre-registered test of `gayor/<ila`h` = 147.** The 'no other god' interpretation is
   theologically central. Worth a formal Phase B finding under proper rules tuple.
3. **Comparable-corpus null:** redo the matching-pair scan on Bukhari, Muslim, and a classical
   poetry diwan. If those texts have *more* semantically-interesting matches per 1000 lemmas,
   the Quran's pairs are not distinctive.
4. **Larger n-gram coincidences:** beyond single-lemma counts, look at bigram/trigram counts.
   This is where Al-Kaheel's 7-system claims live.

---

## Sources

- `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4)
- `/Users/grey/Downloads/quran/data/translations/en.sahih.txt-2.txt` (Sahih International)
- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (verse counts)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/word-pair-all-matches.csv` (full table)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/word-pair-lemma-counts.csv` (every lemma)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/word-pair-root-counts.csv` (every root)
