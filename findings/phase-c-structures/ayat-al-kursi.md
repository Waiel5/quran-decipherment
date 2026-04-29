---
finding_id: ayat-al-kursi
phase: C
status: deep-dive
date: 2026-04-12
verse: Q 2:255 (Āyat al-Kursī, "The Verse of the Throne")
surah: Al-Baqarah (Medinan, 286 verses)
classical_name: Āyat al-Kursī
hadith_rank: "greatest verse of the Quran" (Muslim 810)
comparator: Khawātim Sūrat al-Ḥashr (Q 59:22-24)
rules:
  orthography: no-tashkeel (Uthmanic rasm, rec-marks filtered)
  word_definition: whitespace-separated real words
  letter_definition: graphemes (hamza carriers counted, tā' marbūta = h-value)
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: mashriqi
  null_model: none for sub-verse ring-pair claims — reported as structural observation, not p-value
---

# Āyat al-Kursī (Q 2:255) — Deep Structural Analysis

Dedicated deep dive on "the greatest verse of the Quran" (Muslim 810), recited by ~1.8 billion Muslims daily and traditionally associated with protection from jinn (Bukhārī 2311; Tirmidhī; Nasāʾī). Paired throughout with `findings/khawatim-al-hashr-analysis.md` as the comparator "Greatest" passage.

## 1. Identification and Core Metrics

**Location.** Al-Baqarah verse 255. Medinan. Sits 32 verses before the end of the Quran's longest surah (286 verses) and inside the passage 2:254-257, between an exhortation to spend in charity (254) and the famous "no compulsion in religion" declaration (256) with its cosmic follow-up (257: Allāh brings believers out of darkness into light).

**Arabic text (no tashkeel):**

> اللّٰه لا إله إلا هو الحي القيوم ۚ لا تأخذه سنة ولا نوم ۚ له ما في السماوات وما في الأرض ۗ من ذا الذي يشفع عنده إلا بإذنه ۚ يعلم ما بين أيديهم وما خلفهم ۖ ولا يحيطون بشيء من علمه إلا بما شاء ۚ وسع كرسيه السماوات والأرض ۖ ولا يئوده حفظهما ۚ وهو العلي العظيم

**Translation (Saheeh International):**

> Allah — there is no deity except Him, the Ever-Living, the Sustainer of [all] existence. Neither drowsiness overtakes Him nor sleep. To Him belongs whatever is in the heavens and whatever is on the earth. Who is it that can intercede with Him except by His permission? He knows what is [presently] before them and what will be after them, and they encompass not a thing of His knowledge except for what He wills. His Kursī extends over the heavens and the earth, and their preservation tires Him not. And He is the Most High, the Most Great.

**Counts.**

| Metric | Value | Note |
|---|---|---|
| Real words | **50** | 2 × 5². Rank 43 in the Quran by word-count (longest verse is 2:282 at 129 words). |
| Letter graphemes | **189** | **189 = 27 × 7 = 3³ × 7**. Clean low-prime factorisation. |
| Abjad (mashriqi) | **13,685** | = 5 × 7 × 17 × 23. Neither 786 (Basmala) nor 1000 (Al-Ikhlāṣ) is a factor. |

Al-Kursī is long but not unusually long; what distinguishes it is **density of theological proposition per word** (see §3) and numerical cleanness of its letter total.

## 2. Divine Attributes — The Layered Enumeration

The verse stacks four positive name-attributes, two meta-attributes of omniscience, two apophatic negations, and two statements of cosmic sovereignty, in one syntactic breath.

**Positive names (asmāʾ al-ṣifāt):**

1. **al-Ḥayy** (الحي, "the Living") — divine-name corpus rank 63, 13 occurrences, 8 as definite-singular; distinguishes divine life from contingent life.
2. **al-Qayyūm** (القيوم, "the Self-Subsisting" / "Sustainer") — rare: only 3 Quranic occurrences (rank 64 in definite singular). All three co-occur with al-Ḥayy.
3. **al-ʿAlī** (العلي, "the Most High") — rank 37, 6 occurrences; here in closing pair.
4. **al-ʿAẓīm** (العظيم, "the Supreme") — pairs with al-ʿAlī.

**Meta-attributes of cosmic knowledge and possession:**

5. **Owner of all in heavens and earth** (lahu mā fī al-samāwāt wa mā fī al-arḍ) — ownership of the totality.
6. **Knower of what is before and behind them** (yaʿlamu mā bayna aydīhim wa mā khalfahum) — temporal omniscience.
7. **They do not encompass His knowledge except by His will** — relational inversion: creature-knowledge only subsists in Creator-permission.
8. **Throne extending beyond heavens and earth** — spatial omnipresence.
9. **Preservation without fatigue** — perpetual sustainment.

**Apophatic negations (the two "lā" clauses):**

- **lā taʾkhudhuhu sinatun wa lā nawm** ("no drowsiness nor sleep takes Him").
- **wa lā yaʾūduhu ḥifẓuhuma** ("nor does their preservation tire Him").

This is **apophatic (negative) theology**: the Quran defines God partly by what does *not* apply to Him (drowsiness, sleep, fatigue). This is the most concentrated patch of negative theology in the Quran's affirmative mode. Compare Q 112:3-4 ("He begets not, nor is He begotten; there is nothing comparable to Him") which is negative-theology-only. Q 2:255 interweaves apophatic and kataphatic statements in a single verse.

**The signature feature.** Āyat al-Kursī operates in the **negative-positive hybrid** mode — apophasis and kataphasis braided. Khawātim al-Ḥashr operates in **positive-theological** mode — 15 divine names piled without apophatic negations. The two "Greatest" passages divide the theological labour.

## 3. Ten Jumal — The Classical Structural Division

Classical tafsīr (al-Ṭabarī 1:571, al-Qurṭubī 3:271, Ibn Kathīr 1:457) enumerates ten "jumal" (sentence-units). Metrics per jumla:

| # | Jumla | Gloss | W | L | Abjad |
|---|---|---|---:|---:|---:|
| J1 | اللّٰه لا إله إلا هو | Tawḥīd identity | 5 | **14** | 176 |
| J2 | الحي القيوم | Name-pair (Life / Self-Subsistence) | 2 | 10 | 236 |
| J3 | لا تأخذه سنة ولا نوم | Apophatic negation 1 | 5 | 16 | 1,985 |
| J4 | له ما في السماوات وما في الأرض | Cosmic ownership | 7 | 24 | 1,874 |
| J5 | من ذا الذي يشفع عنده إلا بإذنه | Rhetorical Q (intercession) | 7 | 24 | 2,911 |
| J6 | يعلم ما بين أيديهم وما خلفهم | Temporal omniscience | 6 | 23 | 1,125 |
| J7 | ولا يحيطون بشيء من علمه إلا بما شاء | Cognitive limit of creatures | 8 | 28 | 1,055 |
| J8 | وسع كرسيه السماوات والأرض | Throne spans cosmos | 4 | 22 | 2,008 |
| J9 | ولا يئوده حفظهما | Apophatic negation 2 (no fatigue) | 3 | 14 | 1,106 |
| J10 | وهو العلي العظيم | Name-pair closer (Height / Grandeur) | 3 | **14** | 1,209 |
| **Σ** | | | **50** | **189** | **13,685** |

**Ring-pair reading.** Mirroring the 10 jumal concentrically (J1↔J10, J2↔J9, J3↔J8, J4↔J7, J5↔J6) yields clean thematic pairing:

```
A   J1   Allāh lā ilāha illā huwa              identity-declaration  [14 letters]
  B   J2   al-Ḥayy al-Qayyūm                   name-pair (Life/Sustenance)
    C   J3   no drowsiness / no sleep          apophasis: no cognitive limit
      D   J4   all in heavens/earth is His     cosmic ownership
        E   J5   who can intercede? (Q)        rhetorical center
        E'  J6   He knows before/behind them   knowledge-center
      D'  J7   they encompass not His knowledge cosmic-knowledge limit
    C'  J8   Throne spans heavens/earth        positive cosmic scope
  B'  J9   nor does preservation tire Him     apophasis: no sustenance-fatigue
A'  J10  wa huwa al-ʿAlī al-ʿAẓīm              name-pair closer  [14 letters]
```

**Structural observations (not p-valued):**

- **A ↔ A′ letter-equality.** J1 = 14 letters; J10 = 14 letters. Exact outer-frame match.
- **C ↔ C′ near-equal abjad.** J3 abjad = 1,985; J8 abjad = 2,008. Difference = 23 (<1.2%). These are the two "cosmic" mirrors: apophatic negation (C) vs positive Throne-expansion (C′). They also contain the verse's two "heavens and earth" references.
- **E ↔ E′ central pair.** J5 (rhetorical Q, 24 letters, abjad 2,911) is the single densest abjad jumla; J6 (knowledge statement, 23 letters, abjad 1,125) answers the question by stating God's omniscience. Ring-center is a question-answer dyad.
- **Word-midpoint falls inside J5.** 50 words / 2 = 25-26; J5 spans words 20-26. The rhetorical question sits on the axis.
- **Letter-midpoint at position 94-95** falls on the J5/J6 boundary.

This is consistent with ring-composition practice: the rhetorical question is placed as the **pivot**, with apophasis and kataphasis spiralling out from it.

## 4. The "Allāh lā ilāha illā huwa" Formula

Exact sequence scan across all 6,236 verses:

| # | Verse | Type | Co-text (first words after formula) |
|---:|---|---|---|
| 1 | **Q 2:255** | Medinan | الحي القيوم (al-Ḥayy al-Qayyūm) |
| 2 | **Q 3:2** | Medinan | الحي القيوم (identical pair) |
| 3 | Q 4:87 | Medinan | ليجمعنكم إلى يوم القيامة (He will gather you on the Day of Resurrection) |
| 4 | Q 9:129 | Medinan | عليه توكلت وهو رب العرش العظيم (I trust in Him, Lord of the Great Throne) |
| 5 | **Q 20:8** | Meccan | له الأسماء الحسنى (to Him belong the Most Beautiful Names) |
| 6 | Q 27:26 | Meccan | رب العرش العظيم (Lord of the Great Throne) |
| 7 | Q 28:70 | Meccan | له الحمد في الأولى والآخرة (to Him belongs praise in the first and the last) |
| 8 | Q 64:13 | Medinan | وعلى الله فليتوكل المؤمنون (let the believers trust in Allah) |

**Eight exact occurrences** of "Allāh lā ilāha illā huwa". Five Medinan, three Meccan. Its cognate formula "الذي لا إله إلا هو" (the One other than whom there is no deity) occurs in only three verses: Q 20:98, Q 59:22, Q 59:23 — and two of those three stack in Khawātim al-Ḥashr.

**Network observations.**

- **Formula + al-Ḥayy al-Qayyūm pair:** only 2:255 and 3:2. These two verses form a dyad.
- **Formula + ʿarsh ʿaẓīm pair:** 9:129 and 27:26 — a second dyad. Notice: *Ayat al-Kursī uses kursī; the other Throne verses pair the tawḥīd-formula with ʿarsh*. The Throne-imagery in Q 2:255 is the outlier (see §8).
- **Formula + asmāʾ al-ḥusnā:** Q 20:8 is the only occurrence that pairs the tawḥīd-formula with the "Most Beautiful Names" meta-statement. Khawātim al-Ḥashr (Q 59:24) is one of four Quranic verses using "lahu al-asmāʾ al-ḥusnā" but uses the variant formula "الذي لا إله إلا هو" not "الله لا إله إلا هو". **Q 20 (Taha) is the bridging surah** — it contains both formula variants (20:8 and 20:98) and the al-Ḥayy al-Qayyūm pair (20:111).

## 5. The Rhetorical Question — Ring-Center

**J5: "Who is there that can intercede with Him except by His permission?"** (*man dhā alladhī yashfaʿu ʿindahu illā bi-idhnihi*)

This is one of ~830 Quranic rhetorical questions. Structurally it sits at the verse's center (words 20-26 of 50; letter midpoint at its boundary with J6). It is the only interrogative jumla in the verse.

**Function in the ring.** The question *staging device* is a Quranic signature at ring-centers — compare `ring-center-semantics.md`: "Rings aren't decorative symmetry; they stage CONTRAST." Al-Kursī's ring-center stages the supreme contrast: **creature-agency (who can intercede?) vs. divine-permission (except by His permission)**. The rhetorical question doesn't demand an answer — it **denies autonomy to any intercessor** by the structure of the question itself. It is apophatic in syntactic mode, not just semantic content.

**Ring-companion J6.** J6 answers the implicit question by asserting God's omniscience of "what is before them and what is behind them." The center-dyad is: *question about creature-autonomy → statement of Creator-omniscience*. The rhetorical question sits on top of the axis; the knowledge-statement sits on the other side. Together they are the axis.

## 6. Āyat al-Kursī vs Khawātim al-Ḥashr — Comparative Table

| Dimension | Ayat al-Kursī (Q 2:255) | Khawātim al-Ḥashr (Q 59:22-24) |
|---|---|---|
| Scope | 1 verse | 3 verses (vv 22-24) |
| Words | 50 | 49 (= 7²) |
| Letters | 189 (= 3³ × 7) | 216 (= 6³) |
| Divine names enumerated | 4 (al-Ḥayy, al-Qayyūm, al-ʿAlī, al-ʿAẓīm) + "Allāh" | 15 |
| Names appearing nowhere else in Quran | 0 | **8** (al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir, al-Bāriʾ, al-Muṣawwir) |
| Apophatic negations | 2 ("lā taʾkhudhuhu... wa lā nawm"; "lā yaʾūduhu") | 0 (one "subḥāna Llāhi ʿammā yushrikūn" — polytheism-rejection, not apophasis in the same sense) |
| Tawḥīd-formula variant | Allāh lā ilāha illā huwa | huwa Allāhu alladhī lā ilāha illā huwa ×2 (twin-opener technique) |
| Interrogative | 1 rhetorical Q at center | 0 |
| Throne reference | Kursī (1×, cosmic extension) | None |
| Internal structure | 10-jumla concentric ring with A↔A′ = 14-letter frame | 3-verse tafṣīl progression: triadic → majesty-octet → creation-triad + meta |
| Ḥadīth anchor | "Greatest verse" (Muslim 810) | "Greatest Name contained" / 70,000 angels (Tirmidhī, Aḥmad) |
| Theological mode | **Negative + positive hybrid** | **Positive name-piling** |
| Self-reference to Qurʾān | None | Q 59:21 prefaces with "this Quran" (hādhā al-Qurʾān) + mountain parable |

**Similarities.**

1. Both use the tawḥīd formula "lā ilāha illā huwa." Ayat al-Kursī opens with it; Khawātim al-Ḥashr uses the *alladhī* variant twice consecutively.
2. Both are Medinan.
3. Both hold the classical rank of "greatest" — ḥadīth-authorised.
4. Both have internal mathematical cleanness in their letter counts (**189 = 3³ × 7** vs **216 = 6³**).
5. Both list divine names culminating in double-name pairs: al-Kursī ends *al-ʿAlī al-ʿAẓīm*; Khawātim ends *al-ʿAzīz al-Ḥakīm* (the Quran's most frequent divine-pair, 29×).
6. Both engineer their center. Al-Kursī centers on a rhetorical question (apophatic-structurally); Khawātim al-Ḥashr centers on the majesty-octet of v23 (50% divine-name density, corpus-rank 1).

**Differences.**

1. **Theological mode.** Al-Kursī braids negative and positive theology in one verse (2 apophatic clauses + 4 positive names + 5 cosmic statements). Khawātim piles positive names without apophatic clauses.
2. **Length asymmetry.** Al-Kursī packs maximal theology into one verse; Khawātim spreads it across three.
3. **Uniqueness loading.** Khawātim is the exclusive Quranic home of 8 divine names. Al-Kursī has no such exclusive holding — every one of its names appears elsewhere. Al-Kursī's distinctiveness lies in the *combination* and the *Throne-reference*, not in name-uniqueness.
4. **Center-type.** Al-Kursī's center is a rhetorical question. Khawātim's center is a name-list.
5. **Self-reference.** Khawātim has v21 (the mountain parable) as a self-referential preface naming the Quran. Al-Kursī has no self-reference.

**Division of theological labour.** The two passages are not redundant. Al-Kursī is the Quran's **cosmic-sovereignty lyric** (with apophatic guardrails). Khawātim al-Ḥashr is the Quran's **divine-names lyric**. Together they form a two-panel diptych: Al-Kursī tells you *what God does* (lives, sustains, possesses, knows, preserves), negatively guarding against anthropomorphism; Khawātim tells you *what God is called* (15 names, climaxing in the self-reference to "the Most Beautiful Names"). Hadith tradition names *both* as greatest for different reasons.

## 7. Al-Ḥayy al-Qayyūm — The Three Occurrences

The name-pair **al-Ḥayy al-Qayyūm** occurs three times:

1. **Q 2:255** (Āyat al-Kursī, J2) — embedded inside the 10-jumla ring.
2. **Q 3:2** — the entire verse is "Allāh lā ilāha illā huwa al-Ḥayy al-Qayyūm." This is a radical compression: Q 3:2 = J1 + J2 of Ayat al-Kursī and nothing else, after the muqaṭṭaʿāt "Alif Lām Mīm" of 3:1.
3. **Q 20:111** — "وعنت الوجوه للحي القيوم" ("and faces shall be humbled before the Ever-Living, the Self-Subsisting"). Here the name-pair carries the preposition *lām* and is the object of humility. Context: Q 20:110 immediately prior says "yaʿlamu mā bayna aydīhim wa mā khalfahum wa lā yuḥīṭūna bihi ʿilmā" — **verbatim J6 + J7 of Ayat al-Kursī** (with minor ending variation). Q 20:110-111 is thus a compressed composite of Ayat al-Kursī jumal J6 + J7 + J2.

The three al-Ḥayy al-Qayyūm verses are a cross-Quranic triptych: **Al-Kursī (full), Q 3:2 (minimalist header), Q 20:110-111 (eschatological-humility variant)**. Classical tradition (al-Qurṭubī, citing al-Ḥasan al-Baṣrī and al-Shaʿbī) places the **Ism Allāh al-Aʿẓam (Greatest Name of God)** in this pair. The tradition has textual warrant: the pair appears in exactly 3 verses, all of which are theologically anchor-points, and one of those three (2:255) is the hadith-named greatest verse.

**Which Greatest-Name claim is older?** The al-Ḥayy al-Qayyūm claim appears in the early tafsīr tradition (al-Ṭabarī quotes al-Shaʿbī and al-Rabīʿ ibn Anas) with isnāds traceable to early-2nd-century Basran and Kufan ḥadīth. The Khawātim al-Ḥashr / Ḥashr-closing claim is anchored in the Tirmidhī/Aḥmad narration of the 70,000-angels ḥadīth with somewhat more variable isnāds. **Both are classical; neither is demonstrably earlier in written tradition** — both stabilise in the 3rd-century hadith compilations. What our corpus analysis can say: **each claim has distinct structural warrant**. The al-Ḥayy al-Qayyūm pair has rarity (3 occurrences) and lexical specificity. Khawātim al-Ḥashr has the 15-name, 8-hapax density concentration. The tradition's willingness to host *both* candidates without reconciling them is itself telling — the "Greatest Name" is a devotional category, not a uniqueness claim.

## 8. Kursī vs ʿArsh — The Throne Distinction

- **Kursī** appears in only **2 verses**:
  - Q 2:255 (divine Throne, cosmic-scale)
  - Q 38:34 ("wa-alqaynā ʿalā kursiyyihi jasadan thumma anāba" — Solomon's throne upon which a body is cast; narrative of Solomon's trial)
- **ʿArsh** (of God) appears **~21 times** (rab al-ʿarsh al-ʿaẓīm in 9:129, 27:26; dhū al-ʿarsh in 85:15; ʿalā al-ʿarsh istawā in 7:54, 10:3, 13:2, 20:5, 25:59, 32:4, 57:4). Total "ʿarsh" in any sense: 28 verse-hits.

**Classical distinction.** The dominant reading (Ibn ʿAbbās, al-Ṭabarī, Ibn Kathīr) takes *kursī* as the **footstool** beneath the ʿarsh, or as metonymy for knowledge/sovereignty (Ibn ʿAbbās: "His Kursī is His knowledge"; al-Ḥasan al-Baṣrī: "His Kursī is His dominion"). A minority identifies kursī with ʿarsh.

**What the corpus shows.** Al-Kursī is a hapax as a divine Throne-term (one occurrence; the second occurrence, Q 38:34, is Solomon's throne — human). ʿArsh is the divine-Throne term the Quran uses consistently. The lexical choice in Q 2:255 is therefore **deliberately marked**: the Quran's single divine invocation of kursī lands in the greatest verse. This is not a synonym-swap; it is a lexically-focal moment.

**The J8 phrase "wasiʿa kursiyyuhu al-samāwāti wa al-arḍa"** ("His Kursī extends over the heavens and the earth") has no cognate formula anywhere in the Quran. It is textually unique. Classical cosmology — whether one reads kursī as literal footstool or metonymic knowledge — makes this phrase the verse's spatial climax: before J8 the focus has been on ownership and knowledge; J8 introduces the *spatial scope* of divine presence.

## 9. Context in Al-Baqarah 254-257 — The Theological Pivot

Local passage:

- **2:254** — Exhortation: spend from what We have provided, before a Day comes with no exchange, no friendship, no intercession. Legal-ethical in mode.
- **2:255** — Āyat al-Kursī. Cosmic-theological in mode.
- **2:256** — "There shall be no compulsion in religion. The right course has become clear from the wrong. Whoever disbelieves in Ṭāghūt and believes in Allah has grasped the most trustworthy handhold with no break in it." Epistemic-ethical in mode.
- **2:257** — "Allah is the ally of those who believe; He brings them from darknesses into the light." Cosmic-salvific in mode.

**Structural pivot reading.** 2:255 is the theological ground on which 2:256 stands. The exhortation to avoid ṭāghūt and grasp the most trustworthy handhold (2:256) is intelligible only if the handhold is (i) most trustworthy because attached to the al-Kursī God (2:255) and (ii) unbreakable because that God is al-Ḥayy al-Qayyūm (no lapse, no sleep, no fatigue). 2:257's "out of darkness into light" imagery picks up the cosmic scale of 2:255. 2:254's "no intercession" is picked up by 2:255's J5 ("who can intercede except by His permission"). **2:254's legal claim and 2:256's epistemic claim are stitched together by 2:255's metaphysical claim.**

This is not a chiastic ring of the kind the `chiastic-audit.md` root-set method detects (that tool works at verse-level and did not flag this passage). It is a **sequential pivot**: legal → metaphysical → epistemic → cosmic. The verse's position in the surah reflects its function as a theological load-bearing wall.

**Intercession motif across 254-256.** The word *shafāʿa* / *yashfaʿu* (intercession) appears in 2:254 ("no intercession" on the Day) and 2:255 ("who can intercede except by His permission"). 2:256 resolves the tension: since there is no autonomous intercession, the handhold one must grasp is the *ʿurwa al-wuthqā* — direct adherence, not mediated intercession. The 3-verse passage is *about* the theology of mediation: first denying autonomous intercession (254), then locating permission in divine sovereignty (255), then prescribing direct faith (256). Ayat al-Kursī is the hinge.

## 10. Al-Baqarah's Macro-Structure — Three Anchors

Al-Baqarah is the longest surah (286 verses). Our corpus analysis has identified three high-salience nodes:

1. **2:131-144 (Abraham-Qibla ring).** Bonferroni-surviving at z = +9.69 — the strongest ring in the Quran. Center at 2:143 (wasaṭ-verse; canonical midpoint). Contains the *twin-opener* 2:149-150 (one of only 2 consecutive twin-opener pairs in the Quran; the other is Q 59:22-23 in Khawātim al-Ḥashr). This is the **Abrahamic-identity anchor**.

2. **2:255-257 (Ayat al-Kursī + "no compulsion" + darkness-to-light).** The **tawḥīd-cosmology anchor**. 2:255 is the hadith-named greatest verse; 2:256 contains the most-cited interfaith principle; 2:257 provides the light-versus-darkness cosmology.

3. **2:282 (longest verse in Quran, 129 words).** The debt-contract verse. The **legal-practical anchor** — Islamic commercial and witnessing law in one verse.

**Observation.** Al-Baqarah hosts three distinct kinds of maximum: maximum ring-structure (131-144), maximum theological-creedal density (255-257), maximum legal-ritual density (282). The surah is a **compendium surah** whose three anchors handle three different registers of Quranic discourse. This is consistent with Al-Baqarah's post-hijra compositional role as the "covenant surah" carrying the Muslim community's foundational legal, creedal, and identity materials.

Note that *all three anchors are inside one surah*. No other surah concentrates ring-structural strength, creedal density, and legal density in its interior. This is one computational explanation for why Al-Baqarah functions as the Quran's longest and most-cited book.

Ayat al-Kursī's placement inside this three-anchor scheme puts it at the **creedal-cosmological axis** of the compendium-surah, with the Abraham ring 111 verses earlier and the long legal verse 27 verses later.

## 11. Abjad and Numerology

**Letter-count 189 = 3³ × 7.** Clean factorisation. For comparison, Khawātim al-Ḥashr (vv 22-24) = 216 = 6³. Both passages land on low-prime cubes/cube-multiples. 7 is the saturated Quranic number (7 heavens, 7 earths, 7 mathānī, 7 gates of Hell/Paradise); 3³ is a perfect cube (compare 6³ in Khawātim).

**Word-count 50 = 2 × 5².** Not a especially striking factorisation, but note that 50 is the same as the Jewish Pentateuch's Jubilee year. No classical Muslim commentator I have found makes this cross-traditional observation.

**Abjad 13,685 = 5 × 7 × 17 × 23.** No obvious significant factor; neither 786 (Basmala) nor 1000 (Al-Ikhlāṣ) divides it. Ratio to Basmala: 13,685 / 786 ≈ 17.41 (not an integer). Ratio to Al-Ikhlāṣ's canonical abjad 1,000: 13.685. These are non-clean, **consistent with an honest corpus** where numerical harmonies are real when they occur and absent when they don't.

**Per-jumla abjad mirror C/C′ (J3 vs J8).** J3 (apophatic "no drowsiness, no sleep") abjad = 1,985. J8 (positive "Throne spans heavens/earth") abjad = 2,008. Difference = 23 (1.15%). These are structural mirrors: the negation of cognitive limit (no drowsiness) mirrors the positive assertion of cosmic scope (Throne extends). The near-equal abjad is observed, not p-tested — reported as structural note.

**Al-Ḥayy al-Qayyūm abjad (J2) = 236.** Al-ʿAlī al-ʿAẓīm abjad (in wa huwa al-ʿAlī al-ʿAẓīm = J10) = 1,209 including *wa-huwa*; the pair *al-ʿAlī al-ʿAẓīm* alone ≈ 1,195. These are the two name-pairs bracketing the verse. Sum J2 + J10 = 1,445.

## 12. Classical Prior Art

**Al-Ṭabarī** (*Jāmiʿ al-Bayān*, d. 310/923, tafsīr on 2:255) — treats the verse jumla-by-jumla, anchors the rhetorical question (J5) on the *istifhām inkārī* (denying rhetorical interrogation), cites Ibn ʿAbbās's reading of kursī as knowledge.

**Al-Rāzī** (*Mafātīḥ al-Ghayb*, d. 606/1210) — extended theological commentary locating the verse's logical structure. Rāzī treats Ayat al-Kursī as the Quran's summary of *uṣūl al-tawḥīd* (principles of divine unity) and structures his commentary around ten questions, aligning loosely with the ten jumal. He identifies the verse as the Quran's systematic-theological apex.

**Al-Qurṭubī** (*al-Jāmiʿ li-Aḥkām al-Qurʾān*, d. 671/1273) — cites multiple hadiths on the verse's merit, including the "greatest verse" hadith of Abū l-Mundhir (Ubayy b. Kaʿb) in Muslim 810. Reports al-Shaʿbī's and al-Rabīʿ ibn Anas's identification of *Ism Allāh al-Aʿẓam* as embedded in al-Ḥayy al-Qayyūm.

**Ibn Kathīr** (*Tafsīr al-Qurʾān al-ʿAẓīm*, d. 774/1373) — the most widely-cited classical tafsīr. Collects the merit-hadiths, the protection-from-jinn tradition (Abū Hurayra's encounter with the devil in Bukhārī 2311 — the devil teaches Abū Hurayra Ayat al-Kursī as protection, validating the practice), and the unique-in-cosmology claim for kursī.

**Al-Ghazālī** (*al-Maqṣad al-Asnā*, on divine names) — treats al-Ḥayy al-Qayyūm together as the two names from which all other divine names derive: al-Ḥayy (substantive being) + al-Qayyūm (self-subsistent sustaining) = the metaphysical ground of all other attributes. This reading is consistent with the classical Greatest-Name-of-God placement in this pair.

**Protection-from-jinn tradition.** Bukhārī 2311 (Abū Hurayra's encounter with a thief who is the Devil; the Devil teaches Ayat al-Kursī as protection, and the Prophet confirms). Tirmidhī 2884 (recitation before sleep brings angelic guard until morning). Muslim 810 (the "greatest verse" ḥadīth). Together these three hadiths anchor the verse's liturgical status: it is recited after each of the 5 daily prayers, before sleep, and as a protective invocation (ruqya).

**On the structural internal ring.** Classical tafsīr recognises the ten jumal and a sense of formal balance but does not (to my knowledge) propose a concentric chiasmus reading in the modern sense. The 14-letter symmetry of J1 ↔ J10, and the 23-abjad distance of J3 ↔ J8, are observations this analysis surfaces; they are consistent with but not derived from classical exegesis.

---

## Three Most Striking Structural Findings — Summary

1. **Two passages, two theological modes, complementary mathematical cleanness.** Āyat al-Kursī: 189 letters = **3³ × 7**, 50 words, *apophatic-kataphatic hybrid*. Khawātim al-Ḥashr: 216 letters = **6³**, 49 words = **7²**, *kataphatic name-piling*. Both passages land on low-prime factorizations; neither is a forced numerical artefact. Together they cover the two theological modes (negative and positive) that the Quran operates in, with matching mathematical cleanness. The tradition's decision to name *both* as "greatest" makes structural sense as a division-of-labour.

2. **Ring-center rhetorical question (Al-Kursī) vs ring-center name-octet (Al-Ḥashr).** Both passages engineer their centers, but with opposite devices. Al-Kursī's J5 rhetorical question "who can intercede except by His permission?" sits at the verse's word-midpoint (words 20-26 of 50) and letter-midpoint boundary. The Khawātim al-Ḥashr center is v23's 8-name sovereignty-octet with 50% divine-name density (rank 1/6236 for density). Al-Kursī uses **apophatic syntax** (question-as-denial) at center; Al-Ḥashr uses **maximal kataphatic density** (8 names). Same structural role, opposite rhetorical devices.

3. **The "Greatest Name" is located by the tradition in overlapping-but-distinct features.** The al-Ḥayy al-Qayyūm placement (Shaʿbī, Rabīʿ ibn Anas — classical) rests on lexical rarity: the pair occurs in exactly 3 verses, all theological anchors (2:255, 3:2, 20:111). The Khawātim al-Ḥashr placement (Tirmidhī, Aḥmad) rests on density: 8 names exclusively here, 15 names total, 49 = 7² words. Both placements survive structural scrutiny; neither falsifies the other. Our corpus analysis adds a third finding the classical tradition does not explicitly note: the **Ayat-al-Kursī 10-jumla outer frame has perfect 14-letter letter-match** (J1 "Allāh lā ilāha illā huwa" = J10 "wa huwa al-ʿAlī al-ʿAẓīm" = 14 letters each), and J3 ↔ J8 have near-identical abjad (1,985 vs 2,008; difference 1.15%). These are not p-tested results but they are observations worth recording: the verse is formally shaped, not just semantically dense.

The two "Greatest" passages — Ayat al-Kursī and Khawātim al-Ḥashr — are not rivals. They are the Quran's two-panel diptych for divine description: one pane shows *what God does* under apophatic-kataphatic braiding (Al-Kursī); the other shows *what God is called* under kataphatic name-piling (Al-Ḥashr). Hadith tradition names both greatest for complementary reasons that hold up under structural scrutiny.

## Files and Cross-References

- Comparator: `findings/khawatim-al-hashr-analysis.md`
- Divine-names frequency tables: `findings/phase-b-hypotheses/divine-names-distribution.md`
- Paired-opposites thematic cognates: `findings/phase-b-hypotheses/paired-opposites-network.md` (J6's "before them / behind them" is a temporal cognate of the Bonferroni-surviving hidden/manifest pair)
- Chiastic audit root-set method (Al-Baqarah 131-144 ring context): `findings/phase-c-structures/chiastic-audit.md`
- Muhkam tawḥīd-formula cluster: `findings/intra-quranic-cross-references.md`
- Run journal: `journal/ayat-al-kursi-run-1.md`
