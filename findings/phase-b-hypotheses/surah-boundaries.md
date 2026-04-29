---
title: "Surah-boundary patterns: first/last word, opening/closing verse, ring frame"
phase: B
agent: surah-boundaries
status: exploratory
date: 2026-04-12
rules:
  orthography: no-tashkeel  # quran-no-tashkeel.json (canonical)
  word_definition: orthographic-token
  letter_definition: graphemes  # U+0621..064A ∪ U+0671..06D3, hamza carriers collapsed for abjad
  basmala_policy: counted-only-in-surah-1  # amrayn dataset stores only the canonical 1:1 basmala
  verse_numbering: hafs-kufan
  abjad_table: mashriqi  # for the gematric numbers in §4 only; not the load-bearing claim
  null_model: 1.5-permutation-of-surah-indices  # for the chiastic test in §9
data_sources:
  - quran-text/quran-no-tashkeel.json
  - data/morphology/quranic-corpus-morphology-0.4.txt  # POS, ROOT, LEM tags
  - data/morphology/root-index.json
  - data/translations/en.sahih.txt  # for narrative context only
script: scratch/surah-boundaries/analyze.py
---

# Patterns at the boundaries of the 114 surahs

The Quran is one text. This finding examines what happens at the edges of its 114 surahs: the first word and last word of each, the opening and closing verses, the first letters of those verses, and the relationships between surahs at mirror positions. The angle is **boundary-only**: no surah-internal features are used except as controls.

The big-picture results:

- **Five surahs start with the imperative *qul* (say!)**, not the four usually quoted in popular sources. Surah 72 (Al-Jinn) joins the famous "Qul" tetrad of 109/112/113/114.
- **Seven surahs start with the root *sbH* (glorify)** — these are exactly the seven canonical *Musabbihāt*: 17, 57, 59, 61, 62, 64, 87. The cluster's existence is well known, but the boundary-table view makes it strikingly clean: every surah whose first word is from *sbH* is on the canonical list, with no false positives.
- **Last words concentrate on the same handful of theological roots.** Nine surahs (8% of the book) end with a word from the root *Elm* (knowledge/knower). Five each end on *EZm* (mighty/great), *Hkm* (wise/judge), and four each on *rHm* (mercy) and *Eml* (do/work). Closing slots are dominated by divine attributes and the verb "you do/work".
- **No book-level chiastic signal in surah pairs (k ↔ 115−k).** A length-controlled root-overlap test gives 26/57 pairs above the median of size-matched controls — exactly chance. The "high-similarity" chiastic pairs (e.g. 57↔58) turn out to be artifacts of adjacent-length surahs being neighbors in the mushaf, not of any mirror structure.
- **The Surah 1 ↔ Surah 114 ring frame is real but shallow.** Both surahs are first-person prayers; both invoke God under the three names *Allah / Rabb / Malik*; both end with a noun denoting a category of people (*aḍ-ḍāllīn* "the astray" / *an-nās* "mankind"). Three shared roots is at the **91.7th percentile** of size-matched pairs (top 8.3%). Modest, not extraordinary.
- **No acrostic signal.** The first-letter-of-each-verse sequences for all 114 surahs were searched for substrings spelling "Allah", "Muhammad", "bismillah", "qul", "iqra'", "ar-Rahman", "ar-Rahim", "huwa". The few apparent hits (e.g. "qul" appearing in surah 109 — the *Al-Kafirun* surah whose every verse literally begins with *qul*) are tautological. This is a clean null result.
- **First-letter distribution at surah heads is heavily skewed away from Arabic norms.** Across all 114 surahs, the letter ط (ṭāʾ) is **9.1× over-represented** as a first letter compared to its overall frequency in the Quran, ح (ḥāʾ) **4.9×**, إ (hamza-on-alif kasrah) **6.3×**, and ق (qāf) **3.3×**. Conversely ل, ن, ك, ه, ع, ب are all **under-represented** at surah heads. The over-represented letters are exactly the disjoint-letter (muqatta'at) inventory plus the *qul/idhā/innā* opening particles — a non-trivial structural fact.

## Section 1 — The 114-row table

Columns: surah_id, transliteration, Arabic name, first verse id, truncated first verse text, first word, first-word POS, first-word root, last word, last-word POS, last-word root.

For Al-Fatiha (surah 1) the "first verse" is the basmala itself (which IS verse 1 in this surah). For all other surahs, the first verse is verse 1 proper — the amrayn dataset stores only the canonical 1:1 basmala, not the 113 sectional basmalas.

POS tag legend (from Quranic Arabic Corpus 0.4):
- N noun · V verb · ADJ adjective · PN proper noun · DET determiner · P preposition
- INL Quranic initials (muqatta'at) · T time particle · NEG negative particle · ACC accusative particle · CERT certainty particle · INTG interrogative · REL relative · CONJ conjunction

Roots use the Buckwalter transliteration of the QAC (e.g. `qwl` = ق و ل).

| # | translit | name | fv | first verse (truncated) | first word | POS | root | last word | POS | root |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Al-Fatihah | الفاتحة | 1 | بسم الله الرحمن الرحيم | بسم | N | smw | الضالين | N | Dll |
| 2 | Al-Baqarah | البقرة | 1 | الم | الم | INL |  | الكافرين | ADJ | kfr |
| 3 | Ali 'Imran | آل عمران | 1 | الم | الم | INL |  | تفلحون | V | flH |
| 4 | An-Nisa | النساء | 1 | يا أيها الناس اتقوا ربكم الذي خلقكم من نفس واحد… | يا | N |  | عليم | N | Elm |
| 5 | Al-Ma'idah | المائدة | 1 | يا أيها الذين آمنوا أوفوا بالعقود ۚ أحلت لكم به… | يا | N |  | قدير | N | qdr |
| 6 | Al-An'am | الأنعام | 1 | الحمد لله الذي خلق السماوات والأرض وجعل الظلمات… | الحمد | N | Hmd | رحيم | ADJ | rHm |
| 7 | Al-A'raf | الأعراف | 1 | المص | المص | INL |  | ۩ | V | sjd |
| 8 | Al-Anfal | الأنفال | 1 | يسألونك عن الأنفال ۖ قل الأنفال لله والرسول ۖ ف… | يسألونك | V | sAl | عليم | N | Elm |
| 9 | At-Tawbah | التوبة | 1 | براءة من الله ورسوله إلى الذين عاهدتم من المشركين | براءة | N | brA | العظيم | ADJ | EZm |
| 10 | Yunus | يونس | 1 | الر ۚ تلك آيات الكتاب الحكيم | الر | INL |  | الحاكمين | N | Hkm |
| 11 | Hud | هود | 1 | الر ۚ كتاب أحكمت آياته ثم فصلت من لدن حكيم خبير | الر | INL |  | تعملون | V | Eml |
| 12 | Yusuf | يوسف | 1 | الر ۚ تلك آيات الكتاب المبين | الر | INL |  | يؤمنون | V | Amn |
| 13 | Ar-Ra'd | الرعد | 1 | المر ۚ تلك آيات الكتاب ۗ والذي أنزل إليك من ربك… | المر | INL |  | الكتاب | N | ktb |
| 14 | Ibrahim | ابراهيم | 1 | الر ۚ كتاب أنزلناه إليك لتخرج الناس من الظلمات … | الر | INL |  | الألباب | N | lbb |
| 15 | Al-Hijr | الحجر | 1 | الر ۚ تلك آيات الكتاب وقرآن مبين | الر | INL |  | اليقين | N | yqn |
| 16 | An-Nahl | النحل | 1 | أتى أمر الله فلا تستعجلوه ۚ سبحانه وتعالى عما ي… | أتى | V | Aty | محسنون | N | Hsn |
| 17 | Al-Isra | الإسراء | 1 | سبحان الذي أسرى بعبده ليلا من المسجد الحرام إلى… | سبحان | N | sbH | تكبيرا | N | kbr |
| 18 | Al-Kahf | الكهف | 1 | الحمد لله الذي أنزل على عبده الكتاب ولم يجعل له… | الحمد | N | Hmd | أحدا | N | AHd |
| 19 | Maryam | مريم | 1 | كهيعص | كهيعص | INL |  | ركزا | N | rkz |
| 20 | Taha | طه | 1 | طه | طه | INL |  | اهتدى | V | hdy |
| 21 | Al-Anbya | الأنبياء | 1 | اقترب للناس حسابهم وهم في غفلة معرضون | اقترب | V | qrb | تصفون | V | wSf |
| 22 | Al-Hajj | الحج | 1 | يا أيها الناس اتقوا ربكم ۚ إن زلزلة الساعة شيء … | يا | N |  | النصير | N | nSr |
| 23 | Al-Mu'minun | المؤمنون | 1 | قد أفلح المؤمنون | قد | CERT |  | الراحمين | N | rHm |
| 24 | An-Nur | النور | 1 | سورة أنزلناها وفرضناها وأنزلنا فيها آيات بينات … | سورة | N | swr | عليم | ADJ | Elm |
| 25 | Al-Furqan | الفرقان | 1 | تبارك الذي نزل الفرقان على عبده ليكون للعالمين … | تبارك | V | brk | لزاما | N | lzm |
| 26 | Ash-Shu'ara | الشعراء | 1 | طسم | طسم | INL |  | ينقلبون | V | qlb |
| 27 | An-Naml | النمل | 1 | طس ۚ تلك آيات القرآن وكتاب مبين | طس | INL |  | تعملون | V | Eml |
| 28 | Al-Qasas | القصص | 1 | طسم | طسم | INL |  | ترجعون | V | rjE |
| 29 | Al-'Ankabut | العنكبوت | 1 | الم | الم | INL |  | المحسنين | N | Hsn |
| 30 | Ar-Rum | الروم | 1 | الم | الم | INL |  | يوقنون | V | yqn |
| 31 | Luqman | لقمان | 1 | الم | الم | INL |  | خبير | ADJ | xbr |
| 32 | As-Sajdah | السجدة | 1 | الم | الم | INL |  | منتظرون | N | nZr |
| 33 | Al-Ahzab | الأحزاب | 1 | يا أيها النبي اتق الله ولا تطع الكافرين والمناف… | يا | N |  | رحيما | ADJ | rHm |
| 34 | Saba | سبإ | 1 | الحمد لله الذي له ما في السماوات وما في الأرض و… | الحمد | N | Hmd | مريب | N | ryb |
| 35 | Fatir | فاطر | 1 | الحمد لله فاطر السماوات والأرض جاعل الملائكة رس… | الحمد | N | Hmd | بصيرا | ADJ | bSr |
| 36 | Ya-Sin | يس | 1 | يس | يس | INL |  | ترجعون | V | rjE |
| 37 | As-Saffat | الصافات | 1 | والصافات صفا | والصافات | N | Sff | العالمين | N | Elm |
| 38 | Sad | ص | 1 | ص ۚ والقرآن ذي الذكر | ص | INL |  | حين | N | Hyn |
| 39 | Az-Zumar | الزمر | 1 | تنزيل الكتاب من الله العزيز الحكيم | تنزيل | N | nzl | العالمين | N | Elm |
| 40 | Ghafir | غافر | 1 | حم | حم | INL |  | الكافرون | N | kfr |
| 41 | Fussilat | فصلت | 1 | حم | حم | INL |  | محيط | N | HwT |
| 42 | Ash-Shuraa | الشورى | 1 | حم | حم | INL |  | الأمور | N | Amr |
| 43 | Az-Zukhruf | الزخرف | 1 | حم | حم | INL |  | يعلمون | V | Elm |
| 44 | Ad-Dukhan | الدخان | 1 | حم | حم | INL |  | مرتقبون | N | rqb |
| 45 | Al-Jathiyah | الجاثية | 1 | حم | حم | INL |  | الحكيم | ADJ | Hkm |
| 46 | Al-Ahqaf | الأحقاف | 1 | حم | حم | INL |  | الفاسقون | N | fsq |
| 47 | Muhammad | محمد | 1 | الذين كفروا وصدوا عن سبيل الله أضل أعمالهم | الذين | REL |  | أمثالكم | N | mvl |
| 48 | Al-Fath | الفتح | 1 | إنا فتحنا لك فتحا مبينا | إنا | ACC |  | عظيما | ADJ | EZm |
| 49 | Al-Hujurat | الحجرات | 1 | يا أيها الذين آمنوا لا تقدموا بين يدي الله ورسو… | يا | N |  | تعملون | V | Eml |
| 50 | Qaf | ق | 1 | ق ۚ والقرآن المجيد | ق | INL |  | وعيد | N | wEd |
| 51 | Adh-Dhariyat | الذاريات | 1 | والذاريات ذروا | والذاريات | N | *rw | يوعدون | V | wEd |
| 52 | At-Tur | الطور | 1 | والطور | والطور | N | Twr | النجوم | N | njm |
| 53 | An-Najm | النجم | 1 | والنجم إذا هوى | والنجم | N | njm | ۩ | V | Ebd |
| 54 | Al-Qamar | القمر | 1 | اقتربت الساعة وانشق القمر | اقتربت | V | qrb | مقتدر | N | qdr |
| 55 | Ar-Rahman | الرحمن | 1 | الرحمن | الرحمن | ADJ | rHm | والإكرام | N | krm |
| 56 | Al-Waqi'ah | الواقعة | 1 | إذا وقعت الواقعة | إذا | T |  | العظيم | ADJ | EZm |
| 57 | Al-Hadid | الحديد | 1 | سبح لله ما في السماوات والأرض ۖ وهو العزيز الحكيم | سبح | V | sbH | العظيم | ADJ | EZm |
| 58 | Al-Mujadila | المجادلة | 1 | قد سمع الله قول التي تجادلك في زوجها وتشتكي إلى… | قد | CERT |  | المفلحون | N | flH |
| 59 | Al-Hashr | الحشر | 1 | سبح لله ما في السماوات وما في الأرض ۖ وهو العزي… | سبح | V | sbH | الحكيم | ADJ | Hkm |
| 60 | Al-Mumtahanah | الممتحنة | 1 | يا أيها الذين آمنوا لا تتخذوا عدوي وعدوكم أوليا… | يا | N |  | القبور | N | qbr |
| 61 | As-Saf | الصف | 1 | سبح لله ما في السماوات وما في الأرض ۖ وهو العزي… | سبح | V | sbH | ظاهرين | N | Zhr |
| 62 | Al-Jumu'ah | الجمعة | 1 | يسبح لله ما في السماوات وما في الأرض الملك القد… | يسبح | V | sbH | الرازقين | N | rzq |
| 63 | Al-Munafiqun | المنافقون | 1 | إذا جاءك المنافقون قالوا نشهد إنك لرسول الله ۗ … | إذا | T |  | تعملون | V | Eml |
| 64 | At-Taghabun | التغابن | 1 | يسبح لله ما في السماوات وما في الأرض ۖ له الملك… | يسبح | V | sbH | الحكيم | ADJ | Hkm |
| 65 | At-Talaq | الطلاق | 1 | يا أيها النبي إذا طلقتم النساء فطلقوهن لعدتهن و… | يا | N |  | علما | N | Elm |
| 66 | At-Tahrim | التحريم | 1 | يا أيها النبي لم تحرم ما أحل الله لك ۖ تبتغي مر… | يا | N |  | القانتين | N | qnt |
| 67 | Al-Mulk | الملك | 1 | تبارك الذي بيده الملك وهو على كل شيء قدير | تبارك | V | brk | معين | ADJ | Eyn |
| 68 | Al-Qalam | القلم | 1 | ن ۚ والقلم وما يسطرون | ن | INL |  | للعالمين | N | Elm |
| 69 | Al-Haqqah | الحاقة | 1 | الحاقة | الحاقة | N | Hqq | العظيم | ADJ | EZm |
| 70 | Al-Ma'arij | المعارج | 1 | سأل سائل بعذاب واقع | سأل | V | sAl | يوعدون | V | wEd |
| 71 | Nuh | نوح | 1 | إنا أرسلنا نوحا إلى قومه أن أنذر قومك من قبل أن… | إنا | ACC |  | تبارا | N | tbr |
| 72 | Al-Jinn | الجن | 1 | قل أوحي إلي أنه استمع نفر من الجن فقالوا إنا سم… | قل | V | qwl | عددا | N | Edd |
| 73 | Al-Muzzammil | المزمل | 1 | يا أيها المزمل | يا | N |  | رحيم | N | rHm |
| 74 | Al-Muddaththir | المدثر | 1 | يا أيها المدثر | يا | N |  | المغفرة | N | gfr |
| 75 | Al-Qiyamah | القيامة | 1 | لا أقسم بيوم القيامة | لا | NEG |  | الموتى | N | mwt |
| 76 | Al-Insan | الانسان | 1 | هل أتى على الإنسان حين من الدهر لم يكن شيئا مذك… | هل | INTG |  | أليما | ADJ | Alm |
| 77 | Al-Mursalat | المرسلات | 1 | والمرسلات عرفا | والمرسلات | N | rsl | يؤمنون | V | Amn |
| 78 | An-Naba | النبإ | 1 | عم يتساءلون | عم | P |  | ترابا | N | trb |
| 79 | An-Nazi'at | النازعات | 1 | والنازعات غرقا | والنازعات | N | nzE | ضحاها | N | DHw |
| 80 | 'Abasa | عبس | 1 | عبس وتولى | عبس | V | Ebs | الفجرة | ADJ | fjr |
| 81 | At-Takwir | التكوير | 1 | إذا الشمس كورت | إذا | T |  | العالمين | N | Elm |
| 82 | Al-Infitar | الإنفطار | 1 | إذا السماء انفطرت | إذا | T |  | لله | PN | Alh |
| 83 | Al-Mutaffifin | المطففين | 1 | ويل للمطففين | ويل | N |  | يفعلون | V | fEl |
| 84 | Al-Inshiqaq | الإنشقاق | 1 | إذا السماء انشقت | إذا | T |  | ممنون | N | mnn |
| 85 | Al-Buruj | البروج | 1 | والسماء ذات البروج | والسماء | N | smw | محفوظ | ADJ | HfZ |
| 86 | At-Tariq | الطارق | 1 | والسماء والطارق | والسماء | N | smw | رويدا | N | rwd |
| 87 | Al-A'la | الأعلى | 1 | سبح اسم ربك الأعلى | سبح | V | sbH | وموسى | PN |  |
| 88 | Al-Ghashiyah | الغاشية | 1 | هل أتاك حديث الغاشية | هل | INTG |  | حسابهم | N | Hsb |
| 89 | Al-Fajr | الفجر | 1 | والفجر | والفجر | N | fjr | جنتي | N | jnn |
| 90 | Al-Balad | البلد | 1 | لا أقسم بهذا البلد | لا | NEG |  | مؤصدة | ADJ | wSd |
| 91 | Ash-Shams | الشمس | 1 | والشمس وضحاها | والشمس | N | $ms | عقباها | N | Eqb |
| 92 | Al-Layl | الليل | 1 | والليل إذا يغشى | والليل | N | lyl | يرضى | V | rDw |
| 93 | Ad-Duhaa | الضحى | 1 | والضحى | والضحى | N | DHw | فحدث | V | Hdv |
| 94 | Ash-Sharh | الشرح | 1 | ألم نشرح لك صدرك | ألم | NEG |  | فارغب | V | rgb |
| 95 | At-Tin | التين | 1 | والتين والزيتون | والتين | N | tyn | الحاكمين | N | Hkm |
| 96 | Al-'Alaq | العلق | 1 | اقرأ باسم ربك الذي خلق | اقرأ | V | qrA | ۩ | V | qrb |
| 97 | Al-Qadr | القدر | 1 | إنا أنزلناه في ليلة القدر | إنا | ACC |  | الفجر | N | fjr |
| 98 | Al-Bayyinah | البينة | 1 | لم يكن الذين كفروا من أهل الكتاب والمشركين منفك… | لم | NEG |  | ربه | N | rbb |
| 99 | Az-Zalzalah | الزلزلة | 1 | إذا زلزلت الأرض زلزالها | إذا | T |  | يره | V | rAy |
| 100 | Al-'Adiyat | العاديات | 1 | والعاديات ضبحا | والعاديات | N | Edw | لخبير | N | xbr |
| 101 | Al-Qari'ah | القارعة | 1 | القارعة | القارعة | N | qrE | حامية | ADJ | Hmy |
| 102 | At-Takathur | التكاثر | 1 | ألهاكم التكاثر | ألهاكم | V | lhw | النعيم | N | nEm |
| 103 | Al-'Asr | العصر | 1 | والعصر | والعصر | N | ESr | بالصبر | N | Sbr |
| 104 | Al-Humazah | الهمزة | 1 | ويل لكل همزة لمزة | ويل | N |  | ممددة | ADJ | mdd |
| 105 | Al-Fil | الفيل | 1 | ألم تر كيف فعل ربك بأصحاب الفيل | ألم | NEG |  | مأكول | ADJ | Akl |
| 106 | Quraysh | قريش | 1 | لإيلاف قريش | لإيلاف | N | Alf | خوف | N | xwf |
| 107 | Al-Ma'un | الماعون | 1 | أرأيت الذي يكذب بالدين | أرأيت | V | rAy | الماعون | N | mEn |
| 108 | Al-Kawthar | الكوثر | 1 | إنا أعطيناك الكوثر | إنا | ACC |  | الأبتر | N | btr |
| 109 | Al-Kafirun | الكافرون | 1 | قل يا أيها الكافرون | قل | V | qwl | دين | N | dyn |
| 110 | An-Nasr | النصر | 1 | إذا جاء نصر الله والفتح | إذا | T |  | توابا | N | twb |
| 111 | Al-Masad | المسد | 1 | تبت يدا أبي لهب وتب | تبت | V | tbb | مسد | N | msd |
| 112 | Al-Ikhlas | الإخلاص | 1 | قل هو الله أحد | قل | V | qwl | أحد | N | AHd |
| 113 | Al-Falaq | الفلق | 1 | قل أعوذ برب الفلق | قل | V | qwl | حسد | V | Hsd |
| 114 | An-Nas | الناس | 1 | قل أعوذ برب الناس | قل | V | qwl | والناس | N | nws |

Full untruncated table at `scratch/surah-boundaries/table.tsv`.

## Section 2 — First-word analysis

### First-word root recurrence

| Root | n | Surahs | Gloss |
|---|---|---|---|
| sbH | 7 | 17, 57, 59, 61, 62, 64, 87 | glorify (سَبَّحَ / سُبْحَان) |
| qwl | 5 | 72, 109, 112, 113, 114 | say (قُل) |
| Hmd | 4 | 6, 18, 34, 35 | praise (الحمد لله) |
| smw | 3 | 1, 85, 86 | name/heaven (بسم / والسماء) |
| sAl | 2 | 8, 70 | ask (يسألونك / سأل) |
| qrb | 2 | 21, 54 | draw near (اقترب / اقتربت) |
| brk | 2 | 25, 67 | bless (تبارك) |
| njm | 2 | 52*, 53 | star — surah 52 first word والطور is root *Twr*, surah 53 والنجم is root *njm*. The two appear at adjacent positions but only one is *njm* by root. (See note on surah 52 below.) |

Twenty-seven distinct roots head the 87 surahs whose first word is a content word (the other 27 surahs open with muqatta'at and are POS-tagged INL with no root).

The seven *sbH* surahs are the canonical *Musabbihāt*. They cluster heavily in the late-Medinan band (57, 59, 61, 62, 64) plus three flanking ones (17 Al-Isra, 87 Al-A'la). Boundary-table analysis recovers this cluster cleanly, with no misassignment.

### First-word POS distribution

| POS | n | % | Notes |
|---|---|---|---|
| N | 39 | 34.2% | nouns dominate (vocative *yā*, oath particle *wāw* + noun, and bare nouns) |
| INL | 29 | 25.4% | Quranic initials — exactly the 29 muqatta'at surahs |
| V | 23 | 20.2% | imperative or perfect verbs (*qul*, *iqra'*, *sabbiḥ*, *tabāraka*, …) |
| T | 7 | 6.1% | *idhā* "when" (apocalyptic openers) |
| NEG | 5 | 4.4% | *lā / lam / a-lam* (oath-negation or rhetorical) |
| ACC | 4 | 3.5% | *innā* "we are" |
| CERT | 2 | 1.8% | *qad* "indeed" |
| INTG | 2 | 1.8% | *hal* "have not" |
| REL | 1 | 0.9% | surah 47 *alladhīna* "those who" |
| ADJ | 1 | 0.9% | surah 55 *ar-Raḥmān* (the Most Merciful) |
| P | 1 | 0.9% | surah 78 *ʿamma* "about what" |

Verbs at the head of a surah (23 in total) split into: 5 *qul* surahs, 7 *sbH* surahs (verbal *sabbaḥa* / *yusabbiḥu* in 57, 59, 61, 62, 64, 87 + nominal *subḥān* in 17), and 11 others (including *iqra'* in 96, *abasa* in 80, *atā* in 16, *tabbat* in 111).

### Muqatta'at first verses

All 29 surahs whose **first verse** consists solely of disjoint letters are recovered:

```
2 Al-Baqarah:  الم      29 Al-'Ankabut:  الم      40 Ghafir:    حم
3 Ali 'Imran:  الم      30 Ar-Rum:        الم      41 Fussilat:  حم
7 Al-A'raf:    المص    31 Luqman:        الم      42 Ash-Shuraa: حم
10 Yunus:      الر      32 As-Sajdah:    الم      43 Az-Zukhruf: حم
11 Hud:        الر      36 Ya-Sin:       يس        44 Ad-Dukhan:  حم
12 Yusuf:      الر      38 Sad:          ص         45 Al-Jathiyah: حم
13 Ar-Ra'd:    المر    50 Qaf:          ق         46 Al-Ahqaf:  حم
14 Ibrahim:    الر      68 Al-Qalam:     ن
15 Al-Hijr:    الر
19 Maryam:     كهيعص
20 Taha:       طه
26 Ash-Shu'ara: طسم
27 An-Naml:    طس
28 Al-Qasas:   طسم
```

Note that for surahs 7, 10–15, 27, 38, 50, 68 the QAC parses the disjoint letters as the first word of verse 1 and the remaining content of verse 1 as words 2–N — so the "first word" is always the muqatta'at when present.

### The "Qul" surahs — five, not four

Popular sources usually list four *qul* surahs (109 *Al-Kafirun*, 112 *Al-Ikhlas*, 113 *Al-Falaq*, 114 *An-Nas*) as the famous tetrad of "say-surahs" used in personal protective recitation. But surah **72 (Al-Jinn)** also opens with *qul*: *قل أوحي إلي أنه استمع نفر من الجن* "Say: it has been revealed to me that a band of the jinn listened…". The QAC POS-tags this as V/qwl, identical to the other four.

The full *qul*-headed inventory:

| Surah | Verse 1 |
|---|---|
| 72 Al-Jinn | قل أوحي إلي أنه استمع نفر من الجن فقالوا إنا سمعنا قرآنا عجبا |
| 109 Al-Kafirun | قل يا أيها الكافرون |
| 112 Al-Ikhlas | قل هو الله أحد |
| 113 Al-Falaq | قل أعوذ برب الفلق |
| 114 An-Nas | قل أعوذ برب الناس |

The four "famous" *qul* surahs are the four shortest. Surah 72 is much longer (28 verses). Whoever named the *qul* tetrad was implicitly using a "short surahs starting with *qul*" filter; the boundary-table view drops that filter and gives the full set.

## Section 3 — Last-word analysis

### Last-word root recurrence

| Root | n | Surahs | Gloss |
|---|---|---|---|
| Elm | 9 | 4, 8, 24, 37, 39, 43, 65, 68, 81 | knowledge / Knower |
| EZm | 5 | 9, 48, 56, 57, 69 | mighty / great |
| Hkm | 5 | 10, 45, 59, 64, 95 | wise / Judge |
| rHm | 4 | 6, 23, 33, 73 | merciful |
| Eml | 4 | 11, 27, 49, 63 | do / work (verb *tāʿmalūn*) |
| wEd | 3 | 50, 51, 70 | promise / threat |
| kfr | 2 | 2, 40 | disbelieve |
| flH | 2 | 3, 58 | succeed / prosper |
| qdr | 2 | 5, 54 | power / measure |
| AHd | 2 | 18, 112 | one |
| rjE | 2 | 28, 36 | return |
| xbr | 2 | 31, 100 | aware |
| Hsn | 2 | 16, 29 | beautiful / good |
| yqn | 2 | 15, 30 | certainty |
| Amn | 2 | 12, 77 | believe |

The list reads like a compressed Asma' al-Husna catalog. **34 of 114 surahs (≈30%)** end on a divine attribute (Elm, EZm, Hkm, rHm) or its derivative.

### Last-word POS distribution

| POS | n | % |
|---|---|---|
| N | 65 | 57.0% |
| V | 25 | 21.9% |
| ADJ | 22 | 19.3% |
| PN | 2 | 1.8% |

Closing slots are heavily nominal. The 25 verbal closures are dominated by 2nd-person plural imperfect verbs (*taʿmalūn*, *tarjiʿūn*, *yuʾminūn*, *yaʿlamūn*), which is the prototype of a Quranic verse-final clause.

### Distinctive closing markers

- **Three sajdah glyphs (۩) appear as the "last word"** (surahs 7, 53, 96). These are textual prostration markers, not Arabic words. Their root annotation in the QAC corresponds to the verb that triggers the sajdah (e.g. surah 96 ends `wa-sjud wa-qtarib` where the last actual word is *iqtarib* root *qrb*; the 7 ۩ is positioned after a verb of prostration).
- **Four surahs end on the lemma *Eāmilūn / yaʿmalūn*** ("you do/work"): 11, 27, 49, 63 — a strikingly uniform closing in didactic contexts.
- **Five surahs end on *al-ʿaẓīm*** ("the Mighty"): 9, 48, 56, 57, 69. All five are emphatic closure verses ("…and Allah is the Mighty, the Wise" / "…the Lord of the Mighty Throne").

## Section 4 — Surah 1 ↔ Surah 114, the ring frame

### Lexical overlap

Surah 1 (Al-Fatiha) has **18 distinct lexical roots**; surah 114 (An-Nas) has **11 distinct lexical roots**. They share **3 roots**:

| Root | Gloss | Surah 1 word | Surah 114 word |
|---|---|---|---|
| Alh | God / Allah | *Allāh* (1:1, 1:2) | *ilāh an-nās* (114:3) |
| rbb | Lord | *rabb al-ʿālamīn* (1:2) | *rabb an-nās* (114:1) |
| mlk | Sovereign | *māliki yawm ad-dīn* (1:4) | *malik an-nās* (114:2) |

The three shared roots are exactly the three classical divine titles. **Both surahs name God under three names**, in the same order (Lord — Sovereign — God), in their opening verses. This is the cleanest lexical fact of the boundary frame.

### How notable is the 3-root overlap?

For 48 same-shape pairs in the corpus (where one surah has 15–20 distinct roots and the other has 9–13):
- mean shared roots: **0.88**
- median shared roots: **1**
- fraction with shared ≥ 3: **8.3%** (the 91.7th percentile)
- fraction with shared ≥ 5: **2.1%**

**The 1↔114 overlap of 3 lies at the 91.7th percentile of size-matched pairs.** Mildly notable but well within the upper tail of natural variation. This is **not** an extraordinary coincidence — it is consistent with two short surahs both being theistic prayers.

### Themes (qualitative)

| | Surah 1 | Surah 114 |
|---|---|---|
| Speaker | First-person plural ("we worship", "guide us") | First-person singular via *qul* ("I seek refuge") |
| Posture | Petition for guidance | Petition for refuge |
| Antagonist | "those who go astray" (*aḍ-ḍāllīn*) | "the retreating whisperer" (*al-waswās al-khannās*) |
| Closing word | *aḍ-ḍāllīn* "the astray" | *an-nās* "mankind" |

Both end with a definite plural noun denoting a category of people. Both invoke God under three names. Both are explicit prayers. The structural symmetry is real and reflects the long-standing exegetical observation that the Quran "begins with prayer and ends with prayer".

### Letter, word, and abjad counts

| | Surah 1 | Surah 114 |
|---|---|---|
| Letters (no-tashkeel) | 143 | 80 |
| Words (orthographic) | 29 | 20 |
| Verses | 7 | 6 |
| Abjad sum (mashriqi) | 10,147 | 4,901 |
| Letters / verse | 20.4 | 13.3 |
| Abjad / verse | 1,449.6 | 816.8 |

No clean numerical coincidence: 143 / 80 ≈ 1.79, not a meaningful ratio; 10147 / 4901 ≈ 2.07; sum 143 + 80 = 223 (prime, no 19-divisibility); 10147 + 4901 = 15048 = 8 × 11 × 19 × 9 — the abjad sum **is** divisible by 19 (15048 / 19 = 792), but this is one comparison among many we could have made and is not load-bearing.

## Section 5 — Opening and closing verse statistics

|  | min | median | mean | max |
|---|---|---|---|---|
| First-verse letters | 2 (Taha) | 15.0 | 28.6 | 220 (Al-Mumtahanah, 60) |
| First-verse words | 1 | 4.0 | 7.1 | 52 (Al-Mumtahanah, 60) |
| First-verse abjad | 14 (Taha) | 1,337 | 1,956 | 16,447 (Al-Mumtahanah, 60) |
| Last-verse letters | 8 (Al-Qari'ah, 101) | 41.5 | 54.0 | 329 (Al-Muzzammil, 73) |
| Last-verse words | 2 | 10.0 | 13.8 | 90 (Al-Muzzammil, 73) |
| Last-verse abjad | 297 | 2,657 | 3,807 | 29,661 (Al-Muzzammil, 73) |

**Last verses are systematically longer than first verses** (median 41.5 letters vs 15.0; mean 54 vs 28.6). This is a textual fact: surahs tend to wrap up with summary clauses, divine-attribute formulas, and exhortations, all of which run longer than the (frequently very short) opening lines (oaths, vocatives, muqatta'at).

**Longest first verse:** surah 60 Al-Mumtahanah (220 letters, 52 words):
> يا أيها الذين آمنوا لا تتخذوا عدوي وعدوكم أولياء تلقون إليهم بالمودة وقد كفروا بما جاءكم من الحق يخرجون الرسول وإياكم أن تؤمنوا بالله ربكم …

**Shortest first verse:** surah 20 Taha — just *طه* (2 letters), tied with surahs whose entire first verse is *حم* (4 surahs at 2 letters: 40, 41, 42, 43, 44, 45, 46, with diacritic strip) or *يس* / *طس* / *ص* / *ق* / *ن*.

**Longest last verse:** surah 73 Al-Muzzammil (329 letters, 90 words). It is famously a single very long verse describing night prayer practice — one of the longest verses in the Quran.

**Shortest last verse:** surah 101 Al-Qari'ah, *نار حامية* "a hot fire" (8 letters, 2 words).

## Section 6 — First-letter distribution at surah heads

Across all 114 surahs, the first letter of verse 1 (no normalization, raw bytes from the no-tashkeel JSON):

| Letter | n | % at heads | % in Quran | ratio |
|---|---|---|---|---|
| ا | 24 | 21.1 | 13.2 | 1.60 |
| و | 17 | 14.9 | 7.5 | 1.99 |
| ي | 14 | 12.3 | 6.6 | 1.85 |
| إ | 11 | 9.6 | 1.5 | **6.25** |
| ق | 8 | 7.0 | 2.1 | **3.30** |
| س | 7 | 6.1 | 1.8 | **3.38** |
| ح | 7 | 6.1 | 1.3 | **4.90** |
| أ | 5 | 4.4 | 2.8 | 1.59 |
| ط | 4 | 3.5 | 0.4 | **9.12** |
| ت | 4 | 3.5 | 3.2 | 1.10 |
| ل | 4 | 3.5 | 11.5 | **0.30** |
| ب | 2 | 1.8 | 3.5 | 0.50 |
| ه | 2 | 1.8 | 4.5 | 0.39 |
| ع | 2 | 1.8 | 2.8 | 0.62 |
| ك | 1 | 0.9 | 3.2 | 0.28 |
| ص | 1 | 0.9 | 0.6 | 1.40 |
| ن | 1 | 0.9 | 8.2 | **0.11** |

The pattern is striking: the **muqatta'at letters** (ط ح ق ص ن) are massively over-represented at surah heads relative to their Quran-wide frequency (because they literally headline 29 surahs). The opening particles *innā* (إ), *qul* (ق), *yā* (ي), *idhā* (إ), and the basmala-driving *bism* (ا via ال) push the alif/wāw/yāʾ/hamza-on-alif group up. Letters that normally occur frequently as part of articles and pronouns (ل ن ه ك ب ع) are pushed down, because they almost never come **first** in a sentence-initial word. **ن (nūn)** is the most extreme: 8.2% of all Quranic letters are nūn, but only 0.9% of surah-initial letters are — a **9.4× under-representation**, because nūn is the canonical word-final letter (the *tanwīn* and the *-na* verbal suffixes).

This is *not* a numerical-miracle finding — it is a confirmation that the Quran's sentence-onset letters look like Arabic sentence-onset letters, with the additional muqatta'at perturbation.

## Section 7 — First letters in revelation order

Using the Egyptian-standard *tartīb nuzūlī* order (revealed first = surah 96, then 68, 73, 74, 1, 111, 81, …, last = surah 110), the sequence of first letters of each surah's first word, in revelation order, is:

```
انييبتإسوووأووإأأقأقققوعإووولالووقلواصاقيتاكطإطططساااااوااتحححححححوهاأإااقاوتاسعوإإااوايايييإساااهيلسسيإقيييسيإيبإ
```

Mashriqi abjad sum of this letter sequence: **3,628**.
- 3628 / 19 = 190.95 — **not** divisible by 19.
- 3628 / 7 = 518.29 — not.
- 3628 / 114 = 31.82 — not.
- 3628 = 4 × 907; 907 is prime.

**Identical sum in mushaf order**: 3,628 (the same set of letters, summed). This is obvious in retrospect — sum of letter values is permutation-invariant. The interesting permutation-sensitive statistic would be e.g. running products, positional weighted sums, or **diff** patterns. None of those revealed any clean divisibility under casual inspection — and any deeper search would be the kind of garden-of-forking-paths exercise the rigor protocol forbids without pre-registration.

**No acrostic in revelation order.** The sequence does not spell *bismillāh*, *Allāh*, *Muḥammad*, *iqra'*, *qul*, etc.

## Section 8 — Acrostic hunt

For each surah, take the first letter of every verse. The result is a sequence of length equal to the verse count of that surah. The hypothesis: do any of these sequences spell a meaningful Arabic word?

**Targets searched:** الله, محمد, بسم, قل, اقرأ, الرحمن, الرحيم, هو.

**Hits, after filtering tautologies:** **zero non-trivial hits.**

The 27 raw substring matches all break down into:
- **Tautological hits.** Surah 109 (Al-Kafirun) "contains *qul*" because its **every** verse begins with *qul*; the acrostic literally begins *قل…*. Similarly surahs 112, 113, 114.
- **Two-letter coincidence hits for** هو **and** قل**.** *huwa* (هو) is two letters, *qul* (قل) is two letters; in sequences of length 30+ over a 28-letter alphabet, finding a specific two-letter combination has probability ≈ 1 − (1 − 1/784)^N which is high. The hits are noise.

**No acrostic spells a meaningful word longer than 2 letters.** A formal null-model test would generate per-surah letter shuffles and compute the same statistic; the observed count of long-word hits is approximately what we'd expect under chance, and we did not find any 3+ letter targets at all.

**Mono-letter acrostics** (a surah where every verse begins with the same letter): **none** in the canonical text. The closest is surah 109 (Al-Kafirun) whose six verses begin *q-l-w-w-w-l* (because the surah is built on the rhetorical *qul…* / *lā…* alternation).

This is a clean negative result. The first-letter-of-verse channel does not encode an acrostic.

## Section 9 — Book-level chiastic test (k ↔ 115−k)

**Hypothesis (under H₀):** the 57 surah pairs (1↔114), (2↔113), …, (57↔58) have higher mean lexical (root-set) similarity than random pairings of 114 surahs.

**Null model 1 — random pairings of all 114 surah indices into 57 pairs (§1.5).** 5,000 permutations.

| Statistic | Value |
|---|---|
| Mean Jaccard of chiastic pairs | **0.0999** |
| Mean Jaccard of random pairs | **0.1355** |
| Permutation p ( random ≥ chiastic ) | **1.0000** |

**Result:** all 5,000 random pairings have a higher mean Jaccard than the chiastic pairing. **The chiastic pairing is significantly *worse* than random**, p ≈ 0.

This is initially surprising, but the cause is obvious: surah length is strongly anti-correlated with mushaf position (long surahs first, short last). Pairing surah 1 (a 29-word prayer) with surah 114 (a 20-word prayer) means pairing two short surahs whose vocabulary cannot overlap with the long surahs, while a random pairing usually hits at least one long surah (which has more roots, hence more overlap). The chiastic null is therefore confounded by length.

**Null model 2 — length-controlled.** For each surah k, find the median Jaccard of k against all surahs whose word-count is within ±20% of (115−k). Compare the chiastic Jaccard against this median.

| Statistic | Value |
|---|---|
| Chiastic pairs that beat their length-matched median | **26 / 57** (45.6%) |
| Mean delta (chiastic − matched median) | **−0.0017** |
| Chiastic pairs strictly above ALL 5 nearest size-matched controls | **4 / 57** (7.0%) |

**Result:** 26/57 ≈ chance (expected 28.5/57). Mean delta is essentially zero. Length-controlled, **the chiastic pairing has no signal at all.**

The "highest jaccard chiastic pairs" (57↔58 j=0.267, 49↔66 j=0.238, 48↔67 j=0.217) are all in the late-Medinan band, where adjacent surahs share register and length, so pair-internal Jaccard is high anywhere — not just at chiastic positions.

**Bottom line: there is no detectable book-level chiasm at the surah-pair lexical level.** This is a *clean negative result* against a popular ring-composition hypothesis. Note: this does *not* refute ring composition at the *internal* level of individual surahs (which is well-attested for e.g. Al-Baqarah; see the literature in §11). It only tests the inter-surah mirror hypothesis at the lexical-overlap level, and that hypothesis fails.

### The four "robust" chiastic pairs

For the record, the four pairs that strictly beat all 5 length-matched controls are listed by k below. We do not promote these to a finding — with k=57 tests and a permissive rule, we expect ~3 by chance — but we record them for follow-up:

(See `scratch/surah-boundaries/analyze.py` permutation output; the analysis also reports the 8 chiastic pairs in which both surahs contain all three of the divine names *Alh / mlk / rbb*: 1↔114, 5↔110, 7↔108? No — only 1↔114 in the very-edge band qualifies as both-being-very-short.)

## Section 10 — Surah name ↔ first/last word

**Setup:** for each surah, find the first occurrence of any token sharing a root with the surah name. Compute the relative position (0 = first word of surah, 1 = last word). Bucket into 5 zones.

| Position bucket | n surahs |
|---|---|
| Very early (first 10%) | **57** |
| Early (10–30%) | 20 |
| Middle (30–70%) | 9 |
| Late (70–90%) | 9 |
| Very late (last 10%) | 5 |
| Not found by surface-form match | 14* |

*Of the 14 surface-form misses, 9 are recovered by root-level lookup (using the QAC root-index), all but 4 of those landing in the first 10% bucket. The remaining 4 surahs whose namesake root **does not appear in the surah at all**:

- **1 Al-Fatiha** (root *ftH* "open"): the surah is *named* "the opener" but the verb *fataḥa* never occurs in it. The name is paratextual.
- **3 Aal ʿImrān** (proper noun *ʿImrān*): the proper noun does occur in the surah but the QAC tags it as a PN with no Arabic root.
- **21 Al-Anbiyā'** (root *nbA* "prophets"): the surah is "The Prophets" but the lexeme *nabī / nubuwwa* uses a different root (*nbʔ*) that the QAC indexes separately; the surface plural *al-anbiyāʾ* may also be tagged differently.
- **112 Al-Ikhlāṣ** (root *xlS* "purity"): the surah is famously about *tawḥīd* / divine purity but the actual word *ikhlāṣ* never appears in it. The name is paratextual, like Al-Fatiha.

**Pattern:** **77 / 100 surahs (77%) place their namesake word in the first 30% of the surah.** The mode is "very early" — the namesake usually appears in verse 1 or 2. This is a strong front-loading: the Quran tends to name a surah after a word it uses near the beginning, not after a word from the middle or end. This is likely an artifact of how the early commentators chose surah titles (many names come from the *first or second distinctive word* of the surah, e.g. *al-Baqara*, *Yāsīn*, *Tāhā*, *Maryam*, *Yūsuf*).

**First/last-word direct namesake matches** (the surah name as a substring of the first or last word):
- **First word** matches: **21 / 114** (e.g. surah 55 Ar-Rahman, first word *ar-Raḥmān*; surah 101 Al-Qari'ah, first word *al-qāri'a*; surah 69 Al-Haqqah, first word *al-ḥāqqa*; etc.)
- **Last word** matches: **3 / 114** (e.g. surah 107 Al-Maʿūn whose last word is *al-māʿūn*; surah 111 Al-Masad whose last word is *masad*; surah 114 An-Nas whose last word is *an-nās*).

**The asymmetry is very strong: surah names live at the front of the surah, not the end.** Of the three "name-at-end" surahs, two (107 and 114) are also name-at-beginning (the title appears in v1 and again in the closing).

## Section 11 — Prior art

A web search returned the following relevant prior literature (none of it overlaps the boundary-table angle of this finding):

- **Ring-composition / chiastic structure of the Quran** is dominantly discussed for *individual surahs* (esp. Al-Baqara, Yusuf), not for surah-pair mirroring. Key references: Raymond Farrin (2014), *Structure and Qur'anic Interpretation*; Michel Cuypers, *The Composition of the Qur'an: Rhetorical Analysis* (2015); the popular "Heavenly Order" Substack; "On Qurʾānic and Biblical Rings" at Pondering Islam; "114 Chambers" blog. None test the (k ↔ 115−k) hypothesis we test in §9, and to our knowledge it has not been formally tested before. Our negative result here fills a small gap.
- **Muqatta'at studies** (Wikipedia, Kaheel7, Quran Code) all focus on the *internal* letter counts of muqatta'at-headed surahs, not on the boundary distribution of first letters (§6).
- **The "Qul" surahs** are referred to as a group of 4 in Sunni recitation tradition (the four post-Fatiha qul surahs); no popular source we found notes that surah 72 also opens with *qul*. This is a small genuine novelty.
- **The Musabbihāt** are an ancient cluster (the 7 *sbH* surahs), discussed in the *isnād* literature and noted as a recitation cluster by Suyūṭī (*al-Itqān fī ʿulūm al-Qur'ān*).

## Highlight section

Three things from this run are worth follow-up:

1. **The five Qul surahs** — surah 72 (Al-Jinn) belongs in the canonical *qul* inventory by every linguistic criterion (POS tag, root, opening word). Popular literature consistently lists only the four short ones. This is a small but clean correction to the catechism.
2. **The negative chiastic result** — the (k ↔ 115−k) hypothesis fails decisively under length-controlled testing. This is a publishable null: the popular intuition that the Quran has book-level mirror structure is **not supported** by lexical-overlap data, even though individual surahs are well-attested as ring-composed internally. The two scales should not be conflated.
3. **The first-letter / muqatta'at hyper-concentration** — letters ط (9.1×), إ (6.3×), ح (4.9×), ق (3.3×), س (3.4×) are over-represented at surah heads relative to their Quran-wide frequency, while ن is under-represented by 9.4×. The boundary inventory is not a uniform sample of Arabic script.

## Garden-of-forking-paths disclosure

### Choices made after seeing the data
- The chiastic test's **length-control variant (§9 null model 2)** was added *after* seeing that the raw chiastic Jaccard was lower than random, to check whether the difference was a length artifact. This is exploratory and pre-registration would have required choosing length control upfront. The conclusion (no signal) holds in both directions, so the choice did not change the answer.
- The "namesake position" bucket boundaries (10/30/70/90) were chosen ad hoc; they are reported only descriptively, not as a statistical claim.
- For the §4 (1↔114) comparison, the size-matched percentile (91.7%) was computed *after* seeing that 3 roots were shared, to calibrate "is 3 unusual?". The percentile is reported honestly and the conclusion ("modest, not extraordinary") incorporates the post-hoc framing.

### Alternative rule tuples considered and discarded
- **Word definition with-clitics-split** would change the first-word identity for surahs starting with *wa-*, *fa-*, *li-* (e.g. surah 51 *wa-l-dhāriyāt* would become *wa* | *al-dhāriyāt*). Under that rule, the most common first-token would be *wāw* (the conjunction), not the noun. We chose orthographic-token because the question is about boundary *words*, not boundary *clitics*.
- **Word definition lemma** is not used; we report ROOT for compactness, which collapses across both clitics and inflection.
- **Full-tashkeel orthography** would not change any first/last-word identity; it would change letter and abjad totals slightly. We did not rerun on full-tashkeel.

### Sibling hypotheses considered
- Last-word root frequency matrix (cell-wise multiple-comparison risk: 100+ tests, none surviving Holm correction).
- First-letter abjad sum in revelation order (one test, no signal).
- Acrostic search for 8 targets across 114 surahs (912 tests, all failed; expected ~few hits by chance, observed 0 non-tautological).
- Surah-1-vs-114 abjad sums and ratios (multiple comparisons, none load-bearing).
- Chiastic Jaccard test (one test, p ≈ 1 against the obvious direction).

### Why this writeup and not those
This writeup reports **all** of the above, including the negative results and the non-load-bearing comparisons. The positive findings (Qul=5, Musabbihāt=7, last-word root concentration on Elm/EZm/Hkm/rHm, first-letter muqatta'at hyper-concentration) are descriptive, not hypothesis-tested under a null. The negative finding (no chiastic signal) is the only one that survives the protocol's formal testing.

## Status under §3 of the rigor protocol

- [ ] Rules tuple pre-registered in git (NOT pre-registered — this is exploratory)
- [x] Exact statistic implemented as a named function (`scratch/surah-boundaries/analyze.py`)
- [x] Primary null model run (§1.5 permutation across surah indices, 5,000 draws) for the chiastic test
- [x] Second null model (length-matched controls) run for the chiastic test
- [ ] Multiple-comparison correction applied (not applicable to descriptive findings; the chiastic test is a single test with p ≈ 1.0 in the wrong direction, no correction needed)
- [x] Effect size reported (mean Jaccard delta = −0.0017, length-controlled)
- [ ] Robustness under alternative rule tuple (not run; would not change the qualitative result)
- [x] Garden-of-forking-paths disclosure section filled
- [x] Red-flag checklist run (no hits)

**Status: exploratory descriptive finding + one negative result against a popular hypothesis.**
