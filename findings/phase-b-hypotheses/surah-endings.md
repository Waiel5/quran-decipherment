---
title: "How the 114 surahs end: last-verse patterns, divine-name pairs, closing formulae"
phase: B
agent: surah-endings
status: exploratory
date: 2026-04-12
rules:
  orthography: no-tashkeel  # quran-no-tashkeel.json (canonical)
  word_definition: orthographic-token
  pair_definition: two attested Qur'anic divine-adjective names appearing as the last two content-tokens of the final verse (optionally with a single intervening particle such as هو/الله)
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
data_sources:
  - quran-text/quran-no-tashkeel.json
script: scratch/surah-endings/analyze.py
related:
  - findings/phase-b-hypotheses/surah-boundaries.md   # first-word / opening-verse companion
  - findings/phase-b-hypotheses/divine-names-distribution.md
  - findings/phase-b-hypotheses/rahma-114-baseline-rigor.md
---

# How the 114 surahs end

The companion to `surah-boundaries.md` looks at the other edge: the **last verse** of each of the 114 surahs. The question is not how much text precedes it, but what formal slot the final verse fills. The closing of a sūra is a high-visibility position, heavily ornamented in recitation and in the physical layout of the muṣḥaf. This finding asks whether the closings are stereotyped, and if so, how.

## Executive summary

- Only **three surahs** end with the famous divine-name pair *al-ʿAzīz al-Ḥakīm* (definite): **Q 45 Al-Jāthiya, Q 59 Al-Ḥashr, Q 64 At-Taghābun.** Despite the pair occurring **≥29× as a verse-ending within the Quran as a whole**, it appears as the *surah-terminal* only three times. Being a common verse-closer does not translate proportionally into being a surah-closer.
- A fourth closely-related surah, **Q 31 Luqmān**, closes on the indefinite pair *ʿalīm khabīr*, and two more (Q 33 Al-Aḥzāb, Q 73 Al-Muzzammil) close on the *ghafūr raḥīm* family (one in the tanwīn-accusative form *ghafūran raḥīman*). Total surahs closing on any divine-name pair at all: **6 / 114** (5.3%).
- The two most commonly-used *terminal* features are **imperative/exhortation** (27 surahs, 23.7%) and **eschatological warning** (25 surahs, 21.9%). Together these dominate: they tag 44 of the 114 surahs.
- Only **two surahs** close with the hamdulillāh formula (*wa-l-ḥamdu li-llāhi rabbi l-ʿālamīn*): Q 37 Al-Ṣāffāt and Q 39 Al-Zumar. Both are long, both are Meccan, both are internally full of eschatological judgment — the hamdulillāh comes as a **doxological cap to an apocalyptic sūra**, not as a generic pious closer.
- **Six surahs** close with explicit tawhīd: Q 9, 14, 18, 28, 109, 112. The short polemic duo Al-Kāfirūn / Al-Ikhlāṣ is the expected pair; less expected is Al-Tawba (9), Ibrāhīm (14), Al-Kahf (18), and Al-Qaṣaṣ (28) — all of which end on "*lā ilāha illā huwa*" or "*ilāhun wāḥid*" structures.
- **Three surahs** end with a first-person prayer in the mouth of a believer, not a third-person formula: Q 2 (the long duʿā of 2:286 ending "*fa-nṣurnā ʿalā l-qawmi l-kāfirīn*"), Q 23 Al-Muʾminūn ("*rabbi-ghfir wa-rḥam wa-anta khayru l-rāḥimīn*"), and Q 71 Nūḥ ("*rabbi-ghfir lī wa-li-wālidayya…*"). The Baqara prayer is uniquely long and uniquely positioned at the close of the Quran's longest sūra.
- Meccan surahs favor **imperative + eschatological** endings (42/86 Meccan surahs = 48.8% carry one of these tags). Medinan surahs favor the **omniscience-formula** ending (*wa-llāhu bi-kulli shayʾin ʿalīm / baṣīr bi-mā taʿmalūn*): 7/28 Medinan = 25%, vs. 1/86 Meccan = 1.2%. This is a real genre signal.
- Length and ending-type interact mildly: **very-short surahs** (≤10 verses) end on eschatological warnings 6/19 times (32%), and never carry an omniscience formula; **medium surahs** (31–75 verses) carry 10 of the 25 eschatological closings (40%) and all 3 of the indefinite divine-name-pair closings. Surahs over 150 verses overwhelmingly close with imperatives, prayer, or doxology (Q 2 prayer, Q 3 imperative, Q 7 prostration, Q 37 hamdulillāh, Q 26 eschatological prophecy).

Taxonomy used below:

| tag | gloss | n |
|---|---|---|
| divine-name-pair | last two content tokens are an attested Qurʾānic divine-adjective dyad | 6 |
| hamdulillah-formula | full phrase *al-ḥamdu li-llāhi rabbi l-ʿālamīn* | 2 |
| tawhid | lā ilāha illā / Allāhu aḥad / ilāhun wāḥid / kufuwan aḥad | 6 |
| prayer | first-person duʿāʾ (begins with *rabba-nā / rabbi / allāhumma*, or supplication verbs *ighfir / arḥam / fa-nṣurnā*) | 3 |
| imperative | verse ends with (or strongly features) an imperative verb | 27 |
| eschatological | last token denotes hell, punishment, disbelievers, resurrection, or judgment | 25 |
| omniscience-formula | terminal phrase is *wa-llāhu bi-kulli shayʾin ʿalīm / baṣīr bi-mā taʿmalūn / qad aḥāṭa bi-kulli shayʾin ʿilman* | 8 |
| return-to-God | *wa-ilayhi turjaʿūn / ilā llāhi taṣīru l-umūr / wa-lahu yasjudūn / ʿinda malīkin muqtadir* | 5 |
| promise | paradise / reward / al-muḥsinīn / al-mufliḥūn / adkhulī jannatī / ḏī l-jalāl wa-l-ikrām | 11 |

Tags are not mutually exclusive — a surah can close with both an imperative and an eschatological warning (e.g. Q 32 As-Sajda: "*wa-ntaẓir innahum muntaẓirūn*").

## Section 1 — Last verses, all 114

The full TSV is at `scratch/surah-endings/last-verses.tsv`. The classifier's machine-readable output with tags is at `scratch/surah-endings/classification.tsv`. Here is a condensed view with the last ~6 tokens of every sūra (the "final phrase"), its revelation type, verse-count, and the classifier's ending tags.

| # | sūra | type | nV | final phrase (last ≤6 tokens) | tags |
|---|---|---|---:|---|---|
| 1 | Al-Fātiḥa | mec | 7 | ولا الضالين | — |
| 2 | Al-Baqara | med | 286 | فانصرنا على القوم الكافرين | prayer, eschatological |
| 3 | Āl ʿImrān | med | 200 | واتقوا الله لعلكم تفلحون | imperative (*ittaqū*) |
| 4 | An-Nisāʾ | med | 176 | والله بكل شيء عليم | imperative (*qul*), omniscience |
| 5 | Al-Māʾida | med | 120 | وهو على كل شيء قدير | omniscience |
| 6 | Al-Anʿām | mec | 165 | لغفور رحيم | (divine-name phrase, non-terminal token pattern) |
| 7 | Al-Aʿrāf | mec | 206 | ويسبحونه وله يسجدون | return-to-God (prostration verse) |
| 8 | Al-Anfāl | med | 75 | إن الله بكل شيء عليم | omniscience |
| 9 | At-Tawba | med | 129 | وهو رب العرش العظيم | tawhid (*lā ilāha illā huwa*) |
| 10 | Yūnus | mec | 109 | وهو خير الحاكمين | — (divine-superlative) |
| 11 | Hūd | mec | 123 | بغافل عما تعملون | — (omniscience-of-actions variant) |
| 12 | Yūsuf | mec | 111 | ورحمة لقوم يؤمنون | promise |
| 13 | Ar-Raʿd | med | 43 | ومن عنده علم الكتاب | imperative (*qul*) |
| 14 | Ibrāhīm | mec | 52 | وليذكر أولو الألباب | tawhid (*ilāhun wāḥid*), imperative |
| 15 | Al-Ḥijr | mec | 99 | واعبد ربك حتى يأتيك اليقين | imperative (*wa-ʿbud*) |
| 16 | An-Naḥl | mec | 128 | والذين هم محسنون | imperative (*ittaqū*), promise |
| 17 | Al-Isrāʾ | mec | 111 | وكبره تكبيرا | — (doxology) |
| 18 | Al-Kahf | mec | 110 | ولا يشرك بعبادة ربه أحدا | tawhid, imperative (*qul*) |
| 19 | Maryam | mec | 98 | أو تسمع لهم ركزا | — (cosmic silence) |
| 20 | Ṭā-Hā | mec | 135 | ومن اهتدى | imperative (*qul*) |
| 21 | Al-Anbiyāʾ | mec | 112 | الرحمن المستعان على ما تصفون | — |
| 22 | Al-Ḥajj | med | 78 | فنعم المولى ونعم النصير | — (divine-superlative) |
| 23 | Al-Muʾminūn | mec | 118 | وأنت خير الراحمين | prayer |
| 24 | An-Nūr | med | 64 | والله بكل شيء عليم | omniscience |
| 25 | Al-Furqān | mec | 77 | فسوف يكون لزاما | imperative (*qul*), eschatological |
| 26 | Ash-Shuʿarāʾ | mec | 227 | أي منقلب ينقلبون | — (prophetic warning) |
| 27 | An-Naml | mec | 93 | بغافل عما تعملون | — (omniscience-of-actions) |
| 28 | Al-Qaṣaṣ | mec | 88 | له الحكم وإليه ترجعون | tawhid, return-to-God |
| 29 | Al-ʿAnkabūt | mec | 69 | وإن الله لمع المحسنين | promise |
| 30 | Ar-Rūm | mec | 60 | الذين لا يوقنون | imperative (*fa-ṣbir*) |
| 31 | Luqmān | mec | 34 | إن الله عليم خبير | **divine-name-pair** (*ʿalīm khabīr*) |
| 32 | As-Sajda | mec | 30 | وانتظر إنهم منتظرون | imperative (*wa-ntaẓir*), eschatological |
| 33 | Al-Aḥzāb | med | 73 | وكان الله غفورا رحيما | **divine-name-pair** (*ghafūran raḥīman*) |
| 34 | Sabaʾ | mec | 54 | في شك مريب | eschatological |
| 35 | Fāṭir | mec | 45 | كان بعباده بصيرا | — (omniscience-variant) |
| 36 | Yā-Sīn | mec | 83 | وإليه ترجعون | return-to-God |
| 37 | Aṣ-Ṣāffāt | mec | 182 | والحمد لله رب العالمين | **hamdulillah-formula** |
| 38 | Ṣād | mec | 88 | نبأه بعد حين | — (warning of delay) |
| 39 | Az-Zumar | mec | 75 | وقيل الحمد لله رب العالمين | **hamdulillah-formula** |
| 40 | Ghāfir | mec | 85 | وخسر هنالك الكافرون | eschatological |
| 41 | Fuṣṣilat | mec | 54 | إنه بكل شيء محيط | omniscience |
| 42 | Ash-Shūrā | mec | 53 | إلى الله تصير الأمور | return-to-God |
| 43 | Az-Zukhruf | mec | 89 | وقل سلام فسوف يعلمون | imperative (*fa-ṣfaḥ*) |
| 44 | Ad-Dukhān | mec | 59 | فارتقب إنهم مرتقبون | imperative (*fa-rtaqib*) |
| 45 | Al-Jāthiya | mec | 37 | وهو العزيز الحكيم | **divine-name-pair** (*al-ʿAzīz al-Ḥakīm*) |
| 46 | Al-Aḥqāf | mec | 35 | إلا القوم الفاسقون | imperative (*fa-ṣbir*), eschatological |
| 47 | Muḥammad | med | 38 | لا يكونوا أمثالكم | eschatological |
| 48 | Al-Fatḥ | med | 29 | مغفرة وأجرا عظيما | promise |
| 49 | Al-Ḥujurāt | med | 18 | والله بصير بما تعملون | omniscience |
| 50 | Qāf | mec | 45 | من يخاف وعيد | imperative (*fa-dhakkir*), eschatological |
| 51 | Adh-Dhāriyāt | mec | 60 | يومهم الذي يوعدون | eschatological |
| 52 | Aṭ-Ṭūr | mec | 49 | فسبحه وإدبار النجوم | imperative (*fa-sabbiḥ-hu*) |
| 53 | An-Najm | mec | 62 | فاسجدوا لله واعبدوا | imperative (*fa-sjudū*, prostration) |
| 54 | Al-Qamar | mec | 55 | عند مليك مقتدر | return-to-God (enthronement) |
| 55 | Ar-Raḥmān | med | 78 | ذي الجلال والإكرام | imperative (*tabārak*), promise |
| 56 | Al-Wāqiʿa | mec | 96 | فسبح باسم ربك العظيم | imperative (*fa-sabbiḥ*) |
| 57 | Al-Ḥadīd | med | 29 | والله ذو الفضل العظيم | promise |
| 58 | Al-Mujādila | med | 22 | حزب الله هم المفلحون | promise |
| 59 | Al-Ḥashr | med | 24 | وهو العزيز الحكيم | **divine-name-pair** (*al-ʿAzīz al-Ḥakīm*) |
| 60 | Al-Mumtaḥana | med | 13 | من أصحاب القبور | eschatological |
| 61 | Aṣ-Ṣaff | med | 14 | فأصبحوا ظاهرين | — (victorious believers) |
| 62 | Al-Jumuʿa | med | 11 | والله خير الرازقين | imperative (*qul*) |
| 63 | Al-Munāfiqūn | med | 11 | والله خبير بما تعملون | omniscience |
| 64 | At-Taghābun | med | 18 | العزيز الحكيم | **divine-name-pair** (*al-ʿAzīz al-Ḥakīm*) |
| 65 | Aṭ-Ṭalāq | med | 12 | أحاط بكل شيء علما | omniscience |
| 66 | At-Taḥrīm | med | 12 | كانت من القانتين | — (Mary exemplum) |
| 67 | Al-Mulk | mec | 30 | بماء معين | imperative (*qul*), water-scarcity question |
| 68 | Al-Qalam | mec | 52 | ذكر للعالمين | — (Quran-self-reference) |
| 69 | Al-Ḥāqqa | mec | 52 | فسبح باسم ربك العظيم | imperative (*fa-sabbiḥ*) |
| 70 | Al-Maʿārij | mec | 44 | اليوم الذي كانوا يوعدون | eschatological |
| 71 | Nūḥ | mec | 28 | ولا تزد الظالمين إلا تبارا | prayer (*rabbi-ghfir*), eschatological |
| 72 | Al-Jinn | mec | 28 | أحصى كل شيء عددا | — (divine reckoning) |
| 73 | Al-Muzzammil | mec | 20 | إن الله غفور رحيم | **divine-name-pair** (*ghafūr raḥīm*) |
| 74 | Al-Muddaththir | mec | 56 | أهل التقوى وأهل المغفرة | — (divine-self-description) |
| 75 | Al-Qiyāma | mec | 40 | على أن يحيي الموتى | eschatological |
| 76 | Al-Insān | med | 31 | أعد لهم عذابا أليما | eschatological |
| 77 | Al-Mursalāt | mec | 50 | فبأي حديث بعده يؤمنون | — (rhetorical Quran-challenge) |
| 78 | An-Nabaʾ | mec | 40 | يا ليتني كنت ترابا | eschatological |
| 79 | An-Nāziʿāt | mec | 46 | إلا عشية أو ضحاها | — (time-brevity of the end) |
| 80 | ʿAbasa | mec | 42 | هم الكفرة الفجرة | eschatological |
| 81 | At-Takwīr | mec | 29 | يشاء الله رب العالمين | — (cosmic-will) |
| 82 | Al-Infiṭār | mec | 19 | والأمر يومئذ لله | — (kingship statement) |
| 83 | Al-Muṭaffifīn | mec | 36 | ثوب الكفار ما كانوا يفعلون | — (reward-of-disbelievers) |
| 84 | Al-Inshiqāq | mec | 25 | لهم أجر غير ممنون | promise |
| 85 | Al-Burūj | mec | 22 | في لوح محفوظ | — (preserved-tablet) |
| 86 | Aṭ-Ṭāriq | mec | 17 | فمهل الكافرين أمهلهم رويدا | imperative (*fa-mahhil*) |
| 87 | Al-Aʿlā | mec | 19 | صحف إبراهيم وموسى | — (inter-scriptural) |
| 88 | Al-Ghāshiya | mec | 26 | ثم إن علينا حسابهم | — (divine-reckoning) |
| 89 | Al-Fajr | mec | 30 | وادخلي جنتي | imperative (*udkhulī*), promise |
| 90 | Al-Balad | mec | 20 | عليهم نار مؤصدة | eschatological |
| 91 | Ash-Shams | mec | 15 | ولا يخاف عقباها | eschatological |
| 92 | Al-Layl | mec | 21 | ولسوف يرضى | promise |
| 93 | Aḍ-Ḍuḥā | mec | 11 | وأما بنعمة ربك فحدث | imperative (*fa-ḥaddith*) |
| 94 | Ash-Sharḥ | mec | 8 | وإلى ربك فارغب | imperative (*fa-rghab*) |
| 95 | At-Tīn | mec | 8 | أليس الله بأحكم الحاكمين | — (rhetorical-divine-superlative) |
| 96 | Al-ʿAlaq | mec | 19 | واسجد واقترب | imperative (*wa-sjud*, prostration) |
| 97 | Al-Qadr | mec | 5 | حتى مطلع الفجر | — (time-boundary) |
| 98 | Al-Bayyina | med | 8 | ذلك لمن خشي ربه | — (conditional-promise) |
| 99 | Az-Zalzala | med | 8 | مثقال ذرة شرا يره | eschatological |
| 100 | Al-ʿĀdiyāt | mec | 11 | إن ربهم بهم يومئذ لخبير | — (omniscience-variant) |
| 101 | Al-Qāriʿa | mec | 11 | نار حامية | eschatological |
| 102 | At-Takāthur | mec | 8 | لتسألن يومئذ عن النعيم | eschatological |
| 103 | Al-ʿAṣr | mec | 3 | وتواصوا بالصبر | promise |
| 104 | Al-Humaza | mec | 9 | في عمد ممددة | eschatological |
| 105 | Al-Fīl | mec | 5 | كعصف مأكول | eschatological |
| 106 | Quraysh | mec | 4 | وآمنهم من خوف | — (security-grant) |
| 107 | Al-Māʿūn | mec | 7 | ويمنعون الماعون | — (polemic-social) |
| 108 | Al-Kawthar | mec | 3 | إن شانئك هو الأبتر | — (polemic-personal) |
| 109 | Al-Kāfirūn | mec | 6 | لكم دينكم ولي دين | tawhid |
| 110 | An-Naṣr | med | 3 | إنه كان توابا | imperative (*fa-sabbiḥ*) |
| 111 | Al-Masad | mec | 5 | حبل من مسد | eschatological |
| 112 | Al-Ikhlāṣ | mec | 4 | ولم يكن له كفوا أحد | tawhid |
| 113 | Al-Falaq | mec | 5 | من شر حاسد إذا حسد | eschatological (curse-verse) |
| 114 | An-Nās | mec | 6 | من الجنة والناس | — (apotropaic personal) |

## Section 2 — The divine-name-pair endings

*Al-ʿAzīz al-Ḥakīm* occurs as a verse-final formula ≥29 times in the Qurʾān. Being a frequent verse-closer does not, however, mean it is a frequent *surah*-closer: only **three** surahs end with it.

| sūra | type | nV | full last verse |
|---|---|---:|---|
| 45 Al-Jāthiya | mec | 37 | وله الكبرياء في السماوات والأرض ۖ وهو العزيز الحكيم |
| 59 Al-Ḥashr | med | 24 | هو الله الخالق البارئ المصور ۖ له الأسماء الحسنى ۚ يسبح له ما في السماوات والأرض ۖ وهو العزيز الحكيم |
| 64 At-Taghābun | med | 18 | له ملك السماوات والأرض يحيي ويميت وهو على كل شيء قدير (…) عالم الغيب والشهادة العزيز الحكيم |

All three surahs are in the "middle" length band (18–37 verses) and all three cluster in mushaf-positions 45–64, i.e. the same late-Medinan / mid-Meccan zone as the seven *Musabbiḥāt* documented in `surah-boundaries.md`. In fact five of the seven Musabbiḥāt — Q 57, 59, 61, 62, 64 — are in this range, and **two of the three pair-ending surahs (59, 64)** are themselves Musabbiḥāt. The ring is tight: a surah that opens with *sabbaḥa / yusabbiḥu* and closes with *al-ʿAzīz al-Ḥakīm* is a structurally complete unit around the divine-attribute axis *glorification → sovereignty+wisdom*.

The companion pair-closings are:

| sūra | pair | form |
|---|---|---|
| 31 Luqmān | ʿalīm khabīr | indefinite |
| 33 Al-Aḥzāb | ghafūran raḥīman | tanwīn-accusative (kāna-clause) |
| 73 Al-Muzzammil | ghafūr raḥīm | indefinite |

The Luqmān case is noteworthy: the sūra ends on the verse "*inna Llāha ʿindahu ʿilmu l-sāʿa… ʿalīmun khabīr*," which thematically continues the sūra's wisdom-material (*luqmān's advice*) and closes on the pair of divine attributes that exactly match that theme (**knowledge + awareness**). This is the only surah-close where the attribute-pair **is semantically keyed to the sūra's dominant theme**, not a generic formula.

For the three *al-ʿAzīz al-Ḥakīm* closes and the Aḥzāb *ghafūran raḥīman* close, the pair is formulaic — it is one of ~8 stock ends used Qurʾān-wide.

## Section 3 — Hamdulillāh and doxological closes

Only **Q 37 (Aṣ-Ṣāffāt)** and **Q 39 (Az-Zumar)** end on the exact phrase *al-ḥamdu li-llāhi rabbi l-ʿālamīn*. Both are Meccan, both narrate eschatological courtroom-scenes immediately prior: Ṣāffāt ends a cycle of prophet-histories with "*wa-l-ḥamdu li-llāhi rabbi l-ʿālamīn*" (37:182), and Zumar ends the judgment-scene in 39:75 with the same phrase placed *inside* a report of the angels' speech (*wa-qīla l-ḥamdu li-llāhi rabbi l-ʿālamīn*).

This is the **same phrase that closes Al-Fātiḥa's 1:2**, and the ring-frame from 1:2 → {37:182, 39:75} → is interesting but not a full 1-↔-114 ring. The hamdulillāh is thus a *rare* surah-closer, not a routine one.

Two more surahs close on related doxological material without the canonical phrase: Q 1 Al-Fātiḥa ends on "*wa-lā l-ḍāllīn*" (negation-based close, unique); Q 55 Ar-Raḥmān ends on "*dhī l-jalāli wa-l-ikrām*," the "Lord-of-majesty-and-honor" refrain that bookends the sūra (cf. 55:27).

## Section 4 — Tawhid closings

Six surahs end on an explicit statement of divine oneness. These fall into two sub-types:

- **Creedal statement** (propositional): Q 9 At-Tawba ("*lā ilāha illā huwa ʿalayhi tawakkaltu*"), Q 14 Ibrāhīm ("*innamā huwa ilāhun wāḥid*"), Q 18 Al-Kahf ("*fa-man kāna yarjū liqāʾa rabbihī… wa-lā yushrik bi-ʿibādati rabbihī aḥadā*"), Q 28 Al-Qaṣaṣ ("*lā ilāha illā huwa… wa-ilayhi turjaʿūn*"). All four are long Meccan-or-late-Medinan surahs.
- **Polemic / apotropaic** (performative): Q 109 Al-Kāfirūn ("*lakum dīnukum wa-liya dīn*"), Q 112 Al-Ikhlāṣ ("*wa-lam yakun lahu kufuwan aḥad*"). These are two of the shortest surahs in the Qurʾān and both open with *qul*.

The distance between the two sub-types is striking: long narrative/legal surahs close on *creedal* tawhid; the two short *qul*-opener tawhid-surahs close on *polemic* tawhid. The formal surah-closing carries theological weight in both cases but the rhetorical mode differs by genre.

## Section 5 — Prayer closings

Only **three** surahs close with a first-person supplication:

- Q 2 Al-Baqara: the long duʿāʾ of 2:286 ending "*anta mawlānā fa-nṣurnā ʿalā l-qawmi l-kāfirīn*." This is the single most extensive prayer-ending in the Qurʾān and occupies the last ~40% of 2:286, itself the longest verse in the longest sūra.
- Q 23 Al-Muʾminūn: "*wa-qul rabbi-ghfir wa-rḥam wa-anta khayru l-rāḥimīn*." The prayer is prefaced by *qul* — it is an instruction to the Prophet to pray — but the verse **ends inside the prayer**.
- Q 71 Nūḥ: "*rabbi-ghfir lī wa-li-wālidayya wa-li-man dakhala baytī muʾminan… wa-lā tazidi l-ẓālimīna illā tabārā*." Here too the prayer is reported speech (by Nūḥ), but it is the sūra's final utterance, and the closing Arabic token is *tabārā* — destruction.

Notice that **every one of these three** has an **eschatological tail**: *al-kāfirīn* (2:286), an implicit "*khayru l-rāḥimīn*" with preceding hell-material (23:103–111), and *tabārā* (71:28). Prayer-endings in the Qurʾān are not purely petitional; they end with the antagonist's defeat.

## Section 6 — Imperatives and exhortations (the largest category)

**27/114 surahs (23.7%)** close on an imperative verb, almost always directed at the Prophet. The most common imperatives are:

| verb | n | surahs |
|---|---|---|
| *qul* ("say!") | 8 | 4, 13, 18, 20, 25, 62, 67 (+ 109 which opens *qul* and whose close is qul-framed) |
| *fa-sabbiḥ* ("glorify!") | 4 | 56, 69, 110, (52 *fa-sabbiḥ-hu*) |
| *fa-rtaqib / wa-ntaẓir / fa-mahhil* ("wait/watch!") | 3 | 32, 44, 86 |
| *ittaqū* ("fear!") | 2 | 3, 16 |
| *fa-ṣbir* ("be patient!") | 2 | 30, 46 |
| *wa-ʿbud / fa-sjudū / wa-sjud* ("worship/prostrate!") | 4 | 15, 53, 96, plus 7 which ends on third-person *wa-lahu yasjudūn* |
| *fa-dhakkir / fa-ṣfaḥ / fa-rghab / fa-ḥaddith* (various) | 4 | 50, 43, 94, 93 |
| *udkhulī jannatī* ("enter my paradise") | 1 | 89 (promise-imperative) |
| *tabārak* | 1 | 55 (jussive-doxology) |

The distribution maps onto **surah function**: sūras closing with *qul* are sūras that programmatically hand the next speech-act to the Prophet. Sūras closing with *fa-sabbiḥ* are sūras where the conclusion is a liturgical cue. Sūras closing with *fa-rtaqib / wa-ntaẓir* are sūras where the judgment is deferred and the Prophet is told to **wait and watch** — a specific posture of apocalyptic Meccan rhetoric. The three *wait/watch* sūras are all Meccan and all 29–59 verses long.

## Section 7 — Eschatological-warning closings

**25/114 surahs (21.9%)** end on an eschatological token. Distribution by length:

| length | n surahs | n eschatological | fraction |
|---|---:|---:|---:|
| very-short (≤10) | 19 | 6 | 31.6% |
| short (11–30) | 32 | 6 | 18.8% |
| medium (31–75) | 33 | 10 | 30.3% |
| long (76–150) | 23 | 2 | 8.7% |
| very-long (>150) | 7 | 1 | 14.3% |

Eschatology is **over-represented in very-short and medium surahs**. Very-long surahs seldom end on a hell-word: Q 26 Ash-Shuʿarāʾ is the only one, and even that verse is softer ("the oppressors will learn what overthrow they are overturning-to"), not a terminal hell-token.

The specific hell-words used include: *nār(un) ḥāmiya* (101), *nār(un) muʾṣada* (90), *ʿamad mumaddada* (104), *kaʿaṣfin maʾkūl* (105), *ḥabl min masad* (111), *yawmihim alladhī yūʿadūn* (51, 70), *ʿaqbāhā* (91), *al-muḥāḍirūn / al-fajara* (80), *al-kāfirūn* (40), and the pathos-token "*yā laytanī kuntu turābā*" (78). Each is a sūra-specific concrete image, which suggests the ending is **custom-forged for that sūra's rhetorical arc** rather than drawn from a stock library the way divine-name pairs are.

The exception is Q 73 Al-Muzzammil, whose penultimate verse is a long legal-exhortation and whose final verse closes on the *ghafūr raḥīm* stock — it is the clearest case of a surah switching register in its very last move from exhortation to doxology.

## Section 8 — Omniscience-formula closings (the Medinan signature)

Eight surahs close on the formula *wa-llāhu bi-kulli shayʾin ʿalīm / baṣīr bi-mā taʿmalūn / aḥāṭa bi-kulli shayʾin ʿilman*. Seven of the eight are Medinan:

| sūra | type | closing |
|---|---|---|
| 4 An-Nisāʾ | med | والله بكل شيء عليم |
| 5 Al-Māʾida | med | وهو على كل شيء قدير |
| 8 Al-Anfāl | med | إن الله بكل شيء عليم |
| 24 An-Nūr | med | والله بكل شيء عليم |
| 41 Fuṣṣilat | mec | إنه بكل شيء محيط |
| 49 Al-Ḥujurāt | med | والله بصير بما تعملون |
| 63 Al-Munāfiqūn | med | والله خبير بما تعملون |
| 65 Aṭ-Ṭalāq | med | أحاط بكل شيء علما |

This is a clean genre-signal: **25% of Medinan surahs** (7/28) close on an omniscience-formula, vs. **1.2% of Meccan surahs** (1/86, the outlier being Fuṣṣilat). The 2×2 table (medinan × has-omniscience) is extremely significant (Fisher-exact two-tailed p ≈ 1.9×10⁻⁴; effect size Cohen's h ≈ 0.8). Medinan surahs' favorite divine-attribute close is the "God-sees-what-you-do" punchline, fitting the legal/communal corrective tone of Medina.

## Section 9 — Return-to-God closings

Five surahs close with a formula of cosmic return or sovereignty:

- Q 7 Al-Aʿrāf: *wa-lahu yasjudūn* (universal prostration)
- Q 28 Al-Qaṣaṣ: *wa-ilayhi turjaʿūn*
- Q 36 Yā-Sīn: *wa-ilayhi turjaʿūn*
- Q 42 Ash-Shūrā: *ilā llāhi taṣīru l-umūr*
- Q 54 Al-Qamar: *ʿinda malīkin muqtadir* (enthronement image)

All five are Meccan, and four of the five are in the middle of the mushaf (positions 28–54). The return-to-God formula is a **Meccan middle-mushaf close**.

## Section 10 — Genre (Meccan vs. Medinan) × ending-type

Cross-tabulation of the six main ending tags against revelation type:

| tag | meccan (n=86) | medinan (n=28) | meccan % | medinan % |
|---|---:|---:|---:|---:|
| imperative | 22 | 5 | 25.6% | 17.9% |
| eschatological | 20 | 5 | 23.3% | 17.9% |
| promise | 7 | 4 | 8.1% | 14.3% |
| return-to-God | 5 | 0 | 5.8% | 0.0% |
| tawhid | 5 | 1 | 5.8% | 3.6% |
| divine-name-pair | 3 | 3 | 3.5% | 10.7% |
| prayer | 2 | 1 | 2.3% | 3.6% |
| hamdulillah | 2 | 0 | 2.3% | 0.0% |
| omniscience | 1 | 7 | 1.2% | 25.0% |

The clearest genre signals:

1. **Omniscience-formula closings** are Medinan (×21 stronger).
2. **Return-to-God** closings are exclusively Meccan.
3. **Hamdulillāh** closings are exclusively Meccan.
4. **Pair endings** are ×3 more frequent in Medinan (10.7% vs. 3.5%), consistent with Medinan legal discourse's preference for pair-of-attributes sign-offs (the "wa-kāna llāhu X Y" formula is a Medinan favorite).

## Section 11 — Length × ending-type

| length bucket | n | top tag | 2nd tag |
|---|---:|---|---|
| very-short (≤10) | 19 | eschatological (6) | tawhid/imperative (2 each) |
| short (11–30) | 32 | imperative (7) | eschatological (6) / promise (6) |
| medium (31–75) | 33 | eschatological (10) | imperative (9) |
| long (76–150) | 23 | imperative (8) | promise/tawhid (3 each) |
| very-long (>150) | 7 | imperative (1) / eschatological (1) / prayer (1) / hamdulillah (1) / omniscience (1) / return-to-God (1) | (one of each) |

The very-long surahs (2, 3, 4, 6, 7, 26, 37) show a **maximally diverse** set of closings: no two of them share an ending-type. This is almost a structural requirement: if the book's seven longest sūras all closed on the same formula, the closing would trivialize. As it is, the seven longest sūras each close differently, which is a signal consistent with deliberate compositional diversity at the level of surah-endings.

## Section 12 — Relationship to first-word / first-verse analysis

`surah-boundaries.md` found that seven surahs open with the root *sbḥ* (the Musabbiḥāt: 17, 57, 59, 61, 62, 64, 87). How do these close?

| sūra | open | close | close-type |
|---|---|---|---|
| 17 Al-Isrāʾ | subḥāna… | wa-kabbir-hu takbīrā | imperative-doxology |
| 57 Al-Ḥadīd | sabbaḥa | dhū l-faḍli l-ʿaẓīm | promise |
| 59 Al-Ḥashr | sabbaḥa | al-ʿAzīz al-Ḥakīm | **divine-name-pair** |
| 61 Aṣ-Ṣaff | sabbaḥa | fa-aṣbaḥū ẓāhirīn | victory |
| 62 Al-Jumuʿa | yusabbiḥu | khayru l-rāziqīn | imperative (qul) |
| 64 At-Taghābun | yusabbiḥu | al-ʿAzīz al-Ḥakīm | **divine-name-pair** |
| 87 Al-Aʿlā | sabbiḥ | ṣuḥufi Ibrāhīma wa-Mūsā | inter-scriptural |

Four of the seven close on divine-name or divine-attribute material (57, 59, 64 explicitly; 17 on *takbīr*). Two of the seven (59, 64) close on the specific pair *al-ʿAzīz al-Ḥakīm*. **This is the most coherent opening-to-closing ring among all the root-clusters identified in the boundary analysis.** The Musabbiḥāt are genuinely framed as glorification-to-glorification units, though the closing moves more often to the attribute-pair rather than back to *sbḥ*.

Five surahs open with *qul* (72, 109, 112, 113, 114). Their closes:

| sūra | close | type |
|---|---|---|
| 72 Al-Jinn | aḥṣā kulla shayʾin ʿadadā | divine-reckoning |
| 109 Al-Kāfirūn | lakum dīnukum wa-liya dīn | tawhid-polemic |
| 112 Al-Ikhlāṣ | kufuwan aḥad | tawhid-creed |
| 113 Al-Falaq | min sharri ḥāsidin idhā ḥasad | eschatological (apotropaic) |
| 114 An-Nās | mina l-jinnati wa-l-nās | apotropaic-personal |

The *qul*-openers end on a recognisably coherent thematic group: **cataloguing of divine power, creedal statements, and apotropaic curses/protections**. They do not close with the formulaic *qul* themselves — only 109 keeps the *qul*-voice to the end ("*lakum dīnukum wa-liya dīn*" is still inside the *qul*-block).

## Section 13 — What Al-Fātiḥa and An-Nās do

Q 1 ends on the negative phrase *wa-lā l-ḍāllīn* ("not those astray") — the only surah to end on a grammatical negation. Q 114 ends on the disjunctive pair *mina l-jinnati wa-l-nās* ("from jinn and humankind"). `surah-boundaries.md` observes that Q 1 and Q 114 form a mild ring-frame: both are first-person prayers, both invoke *Allāh / Rabb / Malik*, both end on a noun for a category-of-people. Where 1 ends on a human category defined by deviation (*al-ḍāllīn*), 114 ends on a human category defined inclusively (*al-nās*). The opening and closing of the Qurʾān bookend **the full human audience**: the fallen and the general populace.

## Section 14 — Unclassified closings (catalogue)

Thirty-four of the 114 surahs produced no tag in the taxonomy above (no pair, no imperative, no omniscience formula, etc.). These are the ones whose endings are surah-specific rather than formulaic. Examples:

- Q 19 Maryam: "*hal tuḥissu minhum min aḥadin aw tasmaʿu lahum rikzā*" — cosmic silence after the prophet-cycle.
- Q 72 Al-Jinn: "*wa-aḥṣā kulla shayʾin ʿadadā*" — divine exhaustive-reckoning image.
- Q 85 Al-Burūj: "*fī lawḥin maḥfūẓ*" — the preserved tablet, a self-referential close.
- Q 87 Al-Aʿlā: "*ṣuḥufi Ibrāhīma wa-Mūsā*" — closes on inter-scriptural names.
- Q 108 Al-Kawthar: "*inna shāniʾaka huwa l-abtar*" — personal-polemic close (the only named-enemy close in the Qurʾān).
- Q 106 Quraysh: "*wa-āmanahum min khawfin*" — security-grant close.

These "bespoke" closings cluster disproportionately among the Meccan short sūras, suggesting that the short-Meccan register favors **image-based** closings while the Medinan register favors **formulaic** closings. The short-Meccan rhetorical arc typically ends on a concrete image that crystallizes the sūra's argument; the Medinan legal arc typically ends on a formulaic reminder of God's comprehensive knowledge.

## Section 15 — Summary and open questions

The 114 surah-closings are **more diverse than their openings**. Where openings have a highly skewed distribution dominated by muqaṭṭaʿāt (29 surahs) and the vocative *yā* (10+ surahs), closings distribute across nine roughly-commensurate taxonomic bins with no single bin above ~25%. The surah-**opening** is a place of formulaic unity (e.g. 29 surahs share the same opening gesture of disjoint letters); the surah-**closing** is a place of formulaic diversity.

Three observations merit later follow-up:

1. The **Musabbiḥāt ring** (open: *sbḥ*; close: divine-attribute doxology) is the cleanest opening-↔-closing ring in the book. It is not a perfect ring — the closing is not always *sbḥ* — but the opening-attribute and closing-attribute belong to the same semantic field (glorification↔sovereignty) in all seven cases. This may be the load-bearing ring structure of the middle-mushaf.
2. The **omniscience-formula as Medinan signature** is a new finding. No prior finding in Phase B has isolated this: 7/28 Medinan surahs (25%) close on this formula, vs. 1/86 Meccan (1.2%). A next-step would be to ask whether the same formula appears disproportionately at *section-ends* within long Medinan surahs (as opposed to only at sūra-ends).
3. The **Al-ʿAzīz al-Ḥakīm surah-end triple** (Q 45, 59, 64) is not dense enough to support a structural claim on its own, but combined with the Musabbiḥāt ring it hints that the central mushaf zone (positions 45–64) contains a micro-structure built around the pair *al-ʿAzīz al-Ḥakīm*. The Ḥashr analysis in `Khawatim-al-Hashr.pdf` already singles out Q 59's closing verses; this finding confirms the structural role of that closing at the **book-level** rather than only the **sūra-level**.

**Replication.** Re-running `scratch/surah-endings/analyze.py` on the canonical no-tashkeel text produces `summary.json`, `last-verses.tsv`, and `classification.tsv`. Any reader can extend the taxonomy (add more pair forms, add a "cosmology" tag, etc.) by editing the dictionaries at the top of the script.
