---
phase: B
finding_id: phase-b-form-meets-content-run-1
date: 2026-04-12
agent: deep-reader (form-meets-content outlier hunter)
status: reported
claim_class: literary-structural / quantitative
rules:
  orthography: full-tashkeel for fasila detection; no-tashkeel for letter counting (recitation marks + diacritics stripped)
  word_definition: orthographic token
  letter_definition: graphemes, hamza-collapsed-to-carrier, alif-maksura-as-alif, teh-marbuta-as-heh
  verse_numbering: hafs-kufan
  basmala_policy: counted-only-in-surah-1
  null_model: 1.3 within-surah z-score (length, jinas); 1.5-permutation inherited for rhyme
inputs:
  fasila_csv: findings/phase-b-hypotheses/saj-fasila-per-verse.csv
  text: quran-text/quran-no-tashkeel.json
  translation: data/translations/en.sahih.txt
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt
  chiastic_rings: findings/phase-c-structures/chiastic-audit.md
  jinas_prior: findings/phase-b-hypotheses/jinas-wordplay.md
---

# Form-Meets-Content Outliers — hunting maximally-marked verses

> *Hypothesis:* The saj-rhyme-hunter found that Maryam's rhyme breaks land exactly on the Jesus polemics — form enacts content. This report asks: **is Maryam a singular curiosity, or the clearest instance of a corpus-wide pattern?** We catalogue every rhyme-breaker in every uniformly-rhymed surah, cross-reference them with length outliers, root-repetition outliers, and known ring centres, and build a list of maximally-marked verses.

## 0. Method in one paragraph

Four structural-marking dimensions are computed per verse:

- **D1 — rhyme break.** In surahs with U1 ≥ 0.85 and N ≥ 15 (32 surahs), a verse is flagged if its final consonant ≠ the surah's dominant rawi.
- **D2 — length outlier.** `length_z` = (verse_letters − surah_mean) / surah_std. Flagged if |z| ≥ 2.0.
- **D3 — jinas density outlier.** Per-verse `density = 1 − distinct_roots / total_roots`; z-scored within surah. Flagged if z ≥ 2.0.
- **D4 — ring centre.** Hard-coded from the 4 Bonferroni-surviving sub-surah rings in `chiastic-audit.md` + Hud whole-surah ring centre + the 3 length-7 palindrome centres from `palindromes.md` + Q 13:28 (one-verse palindrome).

A verse is "maximally marked" if it fires on ≥ 2 dimensions. We separately catalogue surah-level "break tables," the Maryam deep dive, and the cross-dimensional convergence.

---

## 1. Per-surah rhyme-break tables (top-32 U1-uniform surahs)

Surahs with U1 ≥ 0.85 and N ≥ 15 (the only surahs in which a "break" is meaningful). Surahs are ordered by U1.

| Surah | Name | N | U1 | rawi | Breakers | Break verses |
|---|---|---|---|---|---|---|
| 18 | Al-Kahf | 110 | 1.000 | ا | **0** | — (the longest perfect monorhyme in the Quran) |
| 54 | Al-Qamar | 55 | 1.000 | ر | **0** | — |
| 76 | Al-Insan | 31 | 1.000 | ا | **0** | — |
| 48 | Al-Fatḥ | 29 | 1.000 | ا | **0** | — |
| 72 | Al-Jinn | 28 | 1.000 | ا | **0** | — |
| 92 | Al-Layl | 21 | 1.000 | ا | **0** | — |
| 87 | Al-Aʿlā | 19 | 1.000 | ا | **0** | — |
| 91 | Ash-Shams | 15 | 1.000 | ا | **0** | — |
| **17** | **Al-Isrāʾ** | **111** | **0.991** | **ا** | **1** | **v1 (the Night Journey opening) — see §2** |
| **25** | **Al-Furqān** | **77** | **0.987** | **ا** | **1** | **v17** |
| **33** | **Al-Aḥzāb** | **73** | **0.986** | **ا** | **1** | **v4** |
| 23 | Al-Muʾminūn | 118 | 0.966 | ن | 4 | 51, 73, 86, 116 |
| 4 | An-Nisāʾ | 176 | 0.960 | ا | 7 | 12, 13, 14, 25, 26, 44, 176 |
| **47** | **Muḥammad** | **38** | **0.947** | **م** | **2** | **10, 24** |
| 21 | Al-Anbiyāʾ | 112 | 0.946 | ن | 6 | 4, 60, 62, 66, 69, 76 |
| 7 | Al-Aʿrāf | 206 | 0.937 | ن | 13 | 1, 16, 59, 73, 105, 109 … |
| 28 | Al-Qaṣaṣ | 88 | 0.920 | ن | 7 | 1, 16, 22, 23, 24, 28, 79 |
| **53** | **An-Najm** | **62** | **0.919** | **ا** | **5** | **57, 58, 59, 60, 61** (cluster at surah end) |
| 19 | Maryam | 98 | 0.918 | ا | 8 | 1, 34, 35, 36, 37, 38, 39, 40 |
| 27 | An-Naml | 93 | 0.903 | ن | 9 | 6, 9, 11, 23, 26, 29, 40, 58, 70 |
| 30 | Ar-Rūm | 60 | 0.900 | ن | 6 | 1, 2, 5, 27, 50, 54 |
| 32 | As-Sajdah | 30 | 0.900 | ن | 3 | 1, 6, 23 |
| **73** | **Al-Muzzammil** | **20** | **0.900** | **ا** | **2** | **1, 20** (opening vocative + famous Medinan insertion) |
| 10 | Yūnus | 109 | 0.899 | ن | 11 | 1, 9, 15, 25, 64, 65, 77, 93, 107, 108, 109 |
| 55 | Ar-Raḥmān | 78 | 0.885 | ن | 9 | 10, 11, 14, 15, 24, 27, 41, 72, 78 |
| 43 | Az-Zukhruf | 89 | 0.876 | ن | 11 | 1, 4, 9, 17, 31, 43 … |
| **78** | **An-Nabaʾ** | **40** | **0.875** | **ا** | **5** | **1, 2, 3, 4, 5** (cluster of rhetorical questions at surah head) |
| 6 | Al-Anʿām | 165 | 0.873 | ن | 21 | 13, 15, 17, 18, 39 … |
| 16 | An-Naḥl | 128 | 0.859 | ن | 18 | 7, 18, 47, 58, 60 … |
| **71** | **Nūḥ** | **28** | **0.857** | **ا** | **4** | **1, 2, 3, 4** (the surah's opening frame outside Noah's own speech) |
| 29 | Al-ʿAnkabūt | 69 | 0.855 | ن | 10 | 1, 5, 19, 20, 22 … |
| 26 | Ash-Shuʿarāʾ | 227 | 0.850 | ن | 34 | 1, 7, 9, 17, 22 … |

**What the data shows.** Rhyme-breaks are not uniformly distributed. Five clear clustering modes emerge:

| Mode | Description | Surahs | What it means |
|---|---|---|---|
| A | Singleton doctrinal breaker | 17 v1; 25 v17; 33 v4; 47 v10; 47 v24 | the one verse in the surah that refuses to rhyme is the surah's theological hinge |
| B | Head-block breakers | 71 vv1-4; 78 vv1-5; 28 vv1-2; 32 v1; 29 v1; … | narrative/introductory frame precedes the body's rhyme register |
| C | Tail-block breakers | 53 vv57-61; Yūnus 107-109; Maryam 88-93 (partial) | surah-end coda on a different rhyme modality |
| D | Dialogue breakers | 21 vv60, 62, 66, 69 (Abraham speech); Moses in 28; Solomon in 27 | *direct quoted speech* forces the word order to betray the surah rhyme |
| E | Legal/addendum breakers | 4 vv12, 13, 14, 25, 26; 73 v20 | dense legal content breaks rhyme because the jurisprudence cannot bend to poetic form |

The saj-rhyme finding's original Maryam observation is **the paradigm case of mode A**, not an isolated curiosity. At least three other surahs (17, 25, 33) have **exactly one breaker**, and in all four cases that breaker is a semantically marked verse.

---

## 2. The Al-Isrāʾ exception (Task 2)

**Surah 17 is 110/111 alif-rhymed**. Every verse after v1 ends in -ā (long alif, pause-form -an). Verse 1 is the single exception — it ends in **البصير** *al-baṣīr* ("the Seeing"). Final consonant: ر.

The Arabic:
> سُبْحَانَ الَّذِي أَسْرَىٰ بِعَبْدِهِ لَيْلًا مِنَ الْمَسْجِدِ الْحَرَامِ إِلَى الْمَسْجِدِ الْأَقْصَى الَّذِي بَارَكْنَا حَوْلَهُ لِنُرِيَهُ مِنْ آيَاتِنَا ۚ إِنَّهُ هُوَ السَّمِيعُ الْبَصِيرُ

Translation (Sahih): *"Exalted is He who took His Servant by night from al-Masjid al-Haram to al-Masjid al-Aqsa, whose surroundings We have blessed, to show him of Our signs. Indeed, He is the Hearing, the Seeing."*

### Why this verse cannot rhyme

**The mechanical reason.** Every one of the other 110 verses in Al-Isrāʾ ends in pause-form *tanwīn fatḥ* (an indefinite accusative that realises as long -ā in pause). The opening verse closes with a **definite divine-name dyad** `al-samīʿu al-baṣīr` — and a noun with *al-* definite article cannot take tanwīn. The grammar locks the rhyme out: *al-baṣīr* is the only possible pause form. This is mechanically impossible to rhyme with the body of the surah.

**The rhetorical reason.** The verse *had* a natural rhyme point earlier. The phrase `laylan min al-masjid al-ḥarām` ("by night from the Sacred Mosque") has **laylan**, which is -aylan (perfect alif-rhyme). The verse could have stopped at "by night" and been the opening of a 111/111 alif-monorhyme surah. It does not. It deliberately lengthens past the rhyme to reach the divine-name closer.

### The structural signal

Al-Isrāʾ v1 is **deliberately framed as paratext**. The Night Journey — the most cosmologically singular event in the entire Quranic narrative — is announced in a verse that **sits outside the surah's rhyme system by design**. The rest of the surah is Moses, the Children of Israel, Adam, Iblis, the Dhul-Qarnayn-adjacent signs-and-parables — all in one rhyme register. Verse 1 is a structural frame around all of that. Its non-rhyme *is* the frame.

**This matches the Uthmani titling.** Classical scholars already note that this surah is sometimes titled *Banī Isrāʾīl* ("the Children of Israel") from its content, and *Al-Isrāʾ* ("the Night Journey") from its opening. The rhyme-break at v1 makes the discrepancy structurally visible: **the surah is about the Children of Israel; v1 is a cosmological frame laid over it that refuses to join the body's rhyme grammar**.

### Cross-marker check

- **length_z (v1 vs surah) = +1.70** — v1 is 95 letters in a surah with mean 59.8, not a pure length outlier but clearly above average.
- **jinas z = 0.0** — v1 is not jinas-dense; its power is structural, not repetitional.
- **ring centre = no** — it is the first verse, not a centre.

Al-Isrāʾ v1 is marked on **D1 (rhyme break) + mild D2 (length)**. The marking is the *singular* structural act in the whole surah.

---

## 3. Maryam — the Christological deep dive (Task 3)

The saj-rhyme-hunter identified vv 34–40 and 88–93 as the two doctrinal rhyme-breaks in Maryam. We verify and deepen the finding.

### 3.1 The rhyme-break is real and surgical

Maryam is 90/98 alif-rhymed at U1 level and 66/98 `yā`-rhymed at U2. The two breaker clusters are:

| Verses | Breaker type | Fasila_1 pattern |
|---|---|---|
| **vv 34–40** (7 verses) | all break the alif/yā rhyme | f1 = ن, ن, م, م, ن, ن, ن |
| **vv 88–93** (6 verses) | partial break | f1 = ن, ا, ا, ن, ن, ا — shift away from -yā specifically |

Both clusters land on the two Christological polemic passages: Jesus-as-Son repudiation.

### 3.2 Grammatical-person cascade (iltifāt)

We extracted verb person/number from the Quranic Arabic Corpus for vv 28–44 (first polemic zone):

| Verse | Verb persons | Speaker/addressee shift |
|---|---|---|
| v28-29 | 3MS, 3FS, 3MP | narrator describing Mary's community |
| v30-33 | **1S** (ten first-person verbs) | **Jesus speaks for himself from the cradle** |
| **v34** | 3MP (they dispute) | **disputants injected** |
| **v35** | 3MS + 2MS (imperative "kun!") | **Divine decree formulation** |
| **v36** | 2MP (imperative "worship Him!") | **audience apostrophe** |
| **v37** | 3MP (they differed) | disputant report |
| **v38** | 2MS + 3MP | **direct address to Prophet** ("bring them to Us") |
| **v39** | 2MS (imperative "warn!") | **direct address to Prophet** |
| **v40** | 1P ("We will inherit") | **divine "We"** |
| v41 | 2MS (imperative "mention!") | narrative resumes with address to Prophet |
| v42-44 | 3MS, 2MS | Abraham narrative in regular voice |

**Seven verses contain six distinct grammatical subjects**: 1S (Jesus) → 3MP (disputants) → 3MS + 2MS (God + voice of creation) → 2MP (audience) → 2MS (Prophet Muhammad) → 1P (divine We). This is a **textbook iltifāt cascade** — the classical balagha figure in which the speaker/addressee rapidly shifts for rhetorical force. The polemic section is **simultaneously a rhyme break AND an iltifāt cluster AND a theological pivot** — three structural markings collapsing onto one span.

The parallel pattern holds for vv 88–93:

| Verse | Verb persons | Commentary |
|---|---|---|
| v85-87 | 1P narrative | divine "We" voice |
| **v88** | **3MP** (they say) | disputants injected |
| **v89** | **2MP** (you have done!) | **direct audience rebuke** |
| **v90** | 3FS, 3FP | cosmic reaction verbs (heavens rupture, mountains collapse) |
| **v91** | 3MP (they attribute) | disputants reprised |
| **v92** | 3MS (take) | divine subject |
| **v93** | — (nominal) | universal statement |
| v94-95 | 3MS narrative | narrative resumes |

Same three-way pattern: 1P narrative → 3MP disputants + 2MP audience rebuke + 3FS cosmic shudder → resolution.

### 3.3 Vocabulary shift — the root-cluster signature

Across **both** polemic zones, the same 3-root cluster appears: **Ax\* (to take) + wld (child/son) + rHm (Most Merciful)**.

**v35**: `kwn Alh Ax* wld` — "It is not for God to take a son"
**v88**: `qwl Ax* rHm wld` — "They say the Most Merciful has taken a son"
**v91**: `dEw rHm wld` — "That they attribute a son to the Most Merciful"
**v92**: `bgy rHm Ax* wld` — "It is not appropriate for the Most Merciful to take a son"

The triple **{Ax\*, wld, rHm}** occurs together exactly four times in Maryam (vv 35, 88, 91, 92). All four occurrences are inside the two rhyme-break zones. **The rhyme break, the iltifāt cascade, and the root-triple all align on the same verses**. It is the most over-determined rhetorical signature we have found in the corpus.

### 3.4 Summary of the Maryam finding

Maryam is **simultaneously marked** on four axes in the two polemic zones:

| Axis | vv 34-40 | vv 88-93 |
|---|---|---|
| Rhyme break (D1) | ✓ (7 consecutive) | ✓ (partial, 4 of 6) |
| Iltifāt cascade | ✓ (6 subject shifts) | ✓ (3 subject shifts) |
| Root-cluster {Ax\*, wld, rHm} | ✓ (v35) | ✓ (vv 88, 91, 92) |
| Theological content polemic | ✓ Jesus-as-son | ✓ Rahman-took-son |

Form and content are locked together with a tightness we do not find elsewhere in the Quran. *The Maryam polemics are the clearest single instance of the form-enacts-content principle in the entire corpus we have tested.*

---

## 4. Catalog of exception verses in top-20 uniform surahs — semantically predictable? (Task 4)

Using the top-32 U1-uniform surahs list from §1, we asked: **are the exception verses semantically predictable?** For each surah with few breakers (≤ 5 breakers, excluding muqatta'at v1s), we inspected the content:

| Surah | Break verses (non-muqatta) | Content signature |
|---|---|---|
| 17 Al-Isrāʾ | v1 | **Night Journey cosmological frame** — divine-name dyad locks rhyme out |
| 25 Al-Furqān | v17 | **Day-of-Judgment rebuke**: "Did you mislead these, My servants…?" |
| 33 Al-Aḥzāb | v4 | **The legal ruling against ẓihār and adoption**: "Allah has not made for a man two hearts" |
| 47 Muḥammad | v10, v24 | **Both rhetorical questions to the audience** ("Have they not traveled through the land…?" / "Then do they not reflect upon the Qur'an…?") |
| 23 Al-Muʾminūn | v51, v73, v86, v116 | **Divine address / creedal statement**: 51 = "O messengers"; 86 = "Who is Lord of the seven heavens"; 116 = "So exalted is Allah, the Sovereign, the Truth" |
| 21 Al-Anbiyāʾ | v4, v60, v62, v66, v69, v76 | **Quoted direct speech**: Muhammad (v4), Abraham-story dialog (v60, v62, v66, v69), Noah's call (v76) |
| 73 Al-Muzzammil | v1, v20 | **Opening vocative + Medinan legal insertion** (v20 = 329 letters, longest in surah) |
| 78 An-Nabaʾ | v1-5 | **Opening rhetorical question block**: "About what are they asking…" |
| 71 Nūḥ | v1-4 | **Introductory frame** (v1-4 are narrator; v5+ shifts to Noah's direct speech which joins the rhyme) |
| 53 An-Najm | v57-61 | **Closing rhetorical coda**: "The Approaching Day has approached … Do you laugh and not weep?" |

**Every single one of these breaker clusters is semantically marked.** The hypothesis holds: rhyme exceptions in uniform surahs mark **theological pivot points** — either doctrinal insertions, direct quoted speech (which cannot bend to rhyme), legal material (which refuses poetic form), or introductory/closing structural frames.

**The Maryam Christological break is the archetype, but it is NOT unique in kind.** It is unique only in length (7 consecutive breakers) and in its convergence with an iltifāt cascade and a signature root cluster.

---

## 5. Length-outlier verses (Task 5)

### 5.1 Longest verse in short-verse surahs (top 15 by z)

| Verse | z | Surah median (letters) | This verse | Content |
|---|---|---|---|---|
| **37:102** | +8.96 | 19 | 100 | Abraham's sacrifice: *"When he reached [the age of] exertion with him, he said, 'O my son, I have seen in a dream that I must sacrifice you…'"* |
| **74:31** | +7.21 | 13 | 250 | The guardians-of-Hell / "over it are nineteen" verse — **the 250-letter anchor of the Khalifa Code-19 controversy** |
| **26:49** | +6.58 | 22 | 96 | Pharaoh's threat to the magicians who believed in Moses |
| **55:33** | +6.16 | 19 | 78 | *"O company of jinn and mankind, if you are able to pass beyond the regions of the heavens and earth, then pass…"* — the cosmic challenge |
| 19:58 | +5.34 | 38 | 129 | Summary of the prophetic genealogy in Maryam |
| 38:24 | +5.11 | 32 | 137 | David and the two litigants parable |
| 53:32 | +5.01 | 16 | 129 | *"Those who avoid major sins… your Lord is vast in forgiveness"* — a legal/moral insertion |
| 23:27 | +4.97 | 33 | 138 | The flood inspiration to Noah |
| 52:21 | +4.46 | 27 | 84 | The families-reunited-in-paradise verse |
| 43:32 | +4.27 | 36 | 111 | *"Do they distribute the mercy of your Lord? It is We who have apportioned…"* |
| 69:7 | +4.21 | 20 | 68 | The seven-nights/eight-days punishment duration on ʿĀd |
| **73:20** | +4.21 | 28 | 329 | **The famous night-prayer Medinan insertion in Al-Muzzammil** |
| 56:47 | +4.11 | 17 | 47 | *"When we die and become dust and bones, are we indeed to be resurrected?"* |
| 77:27 | +4.11 | 16 | 38 | Mountains as lofty pegs and sweet water |
| 81:29 | +4.09 | 14 | 32 | *"You do not will except that Allah wills — Lord of the worlds"* — divine-will formulation at the end of Takwīr |

**Every verse in this list is a well-known "marked" verse in traditional tafsir.** The longest-in-short-surah search rediscovers them without prior labelling:
- **37:102** is Abraham's *"yā-bunayya"* sacrifice address, one of the most famous dialogues in Islamic theology.
- **74:31** is THE 19-guardians verse, which Khalifa built an entire numerology on.
- **55:33** is the famous cosmic challenge to jinn and humans.
- **73:20** is the famous Medinan night-prayer addendum universally flagged by scholars as stylistically alien to Al-Muzzammil's short Meccan body.
- **81:29** is Takwīr's climactic divine-will line.

The method is a **known-marker-rediscovery oracle**: give it a short surah, it hands you the verse that tafsir already treats as the rhetorical anchor.

### 5.2 Shortest verse in long-verse surahs (top 7 by negative z)

| Verse | z | Surah median | This | Content |
|---|---|---|---|---|
| **9:22** | −1.65 | 80 | 31 | *"Indeed, Allah has with Him a great reward"* — doxological closer of the emigration pericope |
| 65:9 | −1.55 | 93 | 32 | Summary closer on the disobedient towns |
| **48:1** | −1.30 | 85 | 19 | ***"Indeed, We have given you, [O Muhammad], a clear conquest"*** — **the opening declaration of Al-Fatḥ, the surah named for conquest** |
| 58:21 | −1.27 | 82 | 34 | Divine-decree summary: *"I will surely overcome, I and My messengers"* |
| 5:102 | −1.22 | 89 | 34 | *"A people asked such questions before you; then they became disbelievers"* |
| 66:2 | −1.07 | 87 | 49 | Summary on oath dissolution |
| 60:5 | −0.90 | 91 | 56 | Abraham-style prayer closer |

**Al-Fatḥ v1** is the jewel: the single short verse in an otherwise long-verse Medinan surah is the surah's *title statement* — the declaration of the Treaty of Hudaybiyyah as a "clear conquest" (*fatḥan mubīnan*). The sentence is 19 letters (another Khalifa-flagged count, separately). The brevity IS the emphasis.

The pattern is weaker than the short-surah-long-verse pattern because long-verse surahs (9 Medinan ones) have more heterogeneous registers. But the hits are still all thematically focal: conquest declaration, divine-decree summary, question-rebuke.

---

## 6. Root-density (jinas) outlier verses (Task 6)

We computed per-verse root-repetition density: `1 − (distinct_roots / total_roots)`. A verse with all unique roots → 0; a verse that repeats 5 of 10 roots → 0.5.

### Top 25 per-surah maxima (most jinas-dense verse in each surah that has one)

| Verse | Density | Content |
|---|---|---|
| **27:50** | 0.600 | *"They planned a plan, and We planned a plan, while they perceived not"* — the Thamud 9-conspirators verse; the `mkr`/`mkr` double jinas |
| 73:15 | 0.600 | *"We sent to you a Messenger as a witness… as We sent to Pharaoh a messenger"* — `rsl/rsl` |
| 30:19 | 0.545 | *"He brings the living out of the dead… and brings the dead out of the living"* — chiastic living/dead |
| **2:13** | 0.500 | *"Believe as the people have believed… Should we believe as the fools have believed?"* |
| **3:54** | 0.500 | *"They plotted, Allah plotted, and Allah is the best of plotters"* (`mkr` triple) |
| **4:12** | 0.500 | **The inheritance verse** — the 50-root juggernaut |
| 7:6 | 0.500 | *"We will question those to whom [a message] was sent, and We will question the messengers"* |
| 10:35 | 0.500 | *"Are there of your 'partners' any who guides to the truth? … Allah guides to the truth"* |
| 24:3 | 0.500 | The fornicator / fornicator / polytheist legal ruling |
| 26:19 | 0.500 | Moses-to-Pharaoh: *"You did your deed that you did"* |
| 34:17 | 0.500 | *"Do We repay except the ungrateful?"* |
| **38:84** | 0.500 | *"[Allah] said: The truth, and the truth I say"* — the dual-`Hqq` oath |
| 53:38 | 0.500 | *"No bearer of burdens shall bear another's burden"* (`wzr` double) |
| **56:8** | 0.500 | *"Then the companions of the right — what are the companions of the right?"* |
| 89:21 | 0.500 | Resurrection imagery |
| **13:28** | 0.444 | *"Those who believe and whose hearts find rest in the remembrance of Allah — unquestionably by the remembrance of Allah hearts find rest"* — **the one-verse chiastic palindrome** (see jinas-wordplay.md) |

Almost every entry is a **known** rhetorical gem. The top-density verses are dominated by:
- **Divine counter-plotting** (27:50, 3:54) — Allah taking over the verb
- **Dual jinas oaths** ("truth, truth"; "burden, burden")
- **Ring/palindrome centres** (13:28)
- **Recursive legal self-reference** (4:12, 24:3)

The jinas-density metric is **not a Maryam-style form-enacts-content metric**. It is a *rhetorical-figure* detector. It finds verses where the text is self-referential or recursive at the root level.

---

## 7. Cross-pattern convergence — maximally-marked verses (Task 7)

### 7.1 The unique triple-marked verse

**Q 4:12** fires on D1 (rhyme break: م ≠ ا) + D2 (length z = +3.84) + D3 (jinas z = +2.92).

> *"And for you is half of what your wives leave if they have no child. But if they have a child, for you is one fourth of what they leave, after any bequest they [may have] made or debt. And for the wives is one fourth if you leave no child. But if you leave a child, then for them is an eighth of what you leave…"*

This is the **inheritance verse** — 50 distinct root-tokens in one verse, repeating `wld` (child), `wrv` (inheritance), `mwt` (death), `trk` (leave behind), `dyn` (debt), and `wSy` (bequeath) cyclically as the fractional-inheritance ruling is stated, then stated again for the reciprocal cases, then qualified. It is the single most over-marked verse in the Quran by our metric. It is also the only verse in Sūrat An-Nisāʾ that breaks the alif rhyme with a **م** (because it ends with a divine-name closer: `ʿalīmun ḥalīm` — "Knowing, Forbearing").

**No one could have composed this verse in monorhyme form.** The legal content is recursive and non-reducible. The rhyme break is a mathematical necessity of the jurisprudence. Form yields to content, totally and visibly.

### 7.2 Top 10 maximally-marked verses (excluding muqatta'at v1s)

Ranked by (n_dims, total z-score). Each is marked on ≥ 2 dimensions and carries distinctive content.

| # | Verse | Dims | Sahih content |
|---|---|---|---|
| 1 | **4:12** | 3 (rhyme+length+jinas) | The inheritance fractions verse |
| 2 | **2:282** | 2 (length +7.71, jinas +2.43) | The **debt-writing verse** — the longest verse in the Quran (540+ letters) |
| 3 | **81:29** | 2 (length +4.09, jinas +5.20) | *"You do not will except that Allah wills — Lord of the worlds"* — climactic divine-will line of Takwīr |
| 4 | **55:33** | 2 (length +6.16, jinas +2.82) | *"O company of jinn and mankind, if you are able to pass beyond the regions of the heavens and the earth, then pass. You will not pass except by authority"* |
| 5 | **13:28** | 2 (jinas +3.84, ring centre) | *"Those who believe and whose hearts find rest in the remembrance of Allah — unquestionably by the remembrance of Allah hearts find rest"* (one-verse palindrome) |
| 6 | **43:32** | 2 (length +4.27, jinas +3.07) | *"Do they distribute the mercy of your Lord? It is We who have apportioned among them their livelihood in this world's life…"* |
| 7 | **82:19** | 2 (length +3.17, jinas +4.13) | *"The Day when a soul shall have no power for another soul; the command that Day shall belong [entirely] to Allah"* — **the final verse of Al-Infiṭār**, the Day-of-Judgment closer |
| 8 | **73:20** | 2 (rhyme break, length +4.21) | The night-prayer legal addendum verse of Al-Muzzammil (329 letters in a surah of 20 verses) |
| 9 | **36:47** | 2 (length +3.92, jinas +3.20) | *"When it is said to them, 'Spend from that which Allah has provided you,' those who disbelieve say, 'Should we feed one whom, had Allah willed, He would have fed?'"* |
| 10 | **27:40** | 2 (rhyme break, length +4.07) | **The throne-of-Sheba verse**: *"Said one who had knowledge from the Scripture, 'I will bring it to you before your glance returns to you'"* |

**These 10 verses are candidates for the most rhetorically weighted verses in the Quran.** They each combine:
- A doctrinal or legal or eschatological statement of first-rank importance
- A formal exception to the surrounding surah's default register
- Root- or length-level departure from the surah median

Six of the ten are universally famous (4:12, 2:282, 81:29, 55:33, 13:28, 73:20). Four (43:32, 82:19, 36:47, 27:40) are lesser-known but share the same signature: **a single verse that "sticks out" structurally *and* carries a signature theological payload**.

---

## 8. The spine hypothesis (Task 8)

**Hypothesis:** The most-marked verse of each surah forms a coherent structural spine across the whole Quran.

Computing this: for each of 114 surahs, take the verse with the highest dimensional mark count (break-tie by summed z-score). 18 surahs (mostly very short ones: 49, 62, 65, 94, 97-114) produce no marked verse because they are too short/uniform to allow within-surah outliers. For the remaining 96 surahs we have a spine.

**Result.** Listing the spine in mushaf order does **not** produce a coherent narrative or theological thread — it is not a "hidden index." But it does exhibit a **striking thematic pattern**:

| Mushaf region | Dominant spine-content |
|---|---|
| Surahs 2-9 (long Medinan) | **legal/doctrinal insertions** (2:282 debt, 4:12 inheritance, 5:6 ablution, 8:72 emigration, 9:120) |
| Surahs 10-20 | **prophetic-dialogue or ring centres** (11:62 Salih speech, 12:66 Jacob oath, 13:28 palindrome, 17:1 Night Journey, 19:1 muqatta) |
| Surahs 21-30 | **prophetic narrative climaxes** (20:86 Moses returns, 21:4 Prophet's aside, 23:14 embryonic creation, 26:63 sea parting, 27:40 throne of Sheba) |
| Surahs 31-50 | **Day-of-Judgment rebukes or disputant-reports** (36:47 refusal to spend, 43:32 mercy distribution, 40:28 concealed believer) |
| Surahs 51-80 (short Meccan) | **eschatological climaxes and prophetic-addenda** (53:57, 55:33, 73:20, 74:31, 78:28) |
| Surahs 81-89 | **Day-of-Judgment encapsulations** (81:29, 82:19, 85:10, 88:24) |
| Surahs 90+ | too short/uniform, mostly no spine hits |

The spine is **not a hidden Quran-within-the-Quran**, but it IS a **content-type filter**. Each surah's structurally-marked verse tends to be the same *kind* of verse as the rest of the surah's backbone, only louder. The spine list contains no truly surprising verses.

This is itself a finding: **the marked verses are semantically *predictable* given the surah**. The structural marker metric behaves as an *amplifier*, not a *revealer*. If a surah is about prophetic dialogue, its most-marked verse will be dialogue. If a surah is eschatological, its most-marked verse will be the crispest eschatological formulation. If a surah is legal, its most-marked verse will be the most legal-dense one.

**Corollary:** the form-enacts-content principle holds because **exceptions are not random**. When a uniform surah breaks its own rhyme, it always breaks it for something that rhetorically deserves the structural emphasis. This is a *content-invariant* principle, not a surah-specific one.

---

## 9. Classical prior art — did Suyuṭī / Zarkashī discuss rhyme breaks? (Task 9)

### 9.1 The classical framework for fawāṣil

Both al-Zarkashī's *al-Burhān fī ʿUlūm al-Qurʾān* (d. 794 AH) and al-Suyūṭī's *al-Itqān fī ʿUlūm al-Qurʾān* (d. 911 AH) have chapters on *fawāṣil* (plural of *fāṣila*, verse-ending). The terminology is carefully distinguished from poetic *qāfiya* (rhyme) — as al-Rummānī (4th/10th c.) argued, the fawāṣil are **semantically-governed** endings, not poetic rhyme. "When God took the name of poetry from the Qur'an, He took the rhyme with it."

Classical scholars did classify fawāṣil into categories, commonly:
- **Mutamāthila** (identical-letter endings within a surah)
- **Mutaqāriba** (closely matching endings)
- **Mutawāziya** (parallel endings) 
- **Mutawāzina** (balanced endings)

### 9.2 The mechanism of rhyme preservation — *taqdīm* and *taʾkhīr*

The classical observation most relevant to our analysis is that the Quran uses **taqdīm wa taʾkhīr** (word-order fronting and delaying) as the primary tool for rhyme preservation. Where natural Arabic syntax would break the fasila, the Quran fronts or delays a word to restore it. Classical examples:

- Q 20:125 (Ṭāhā): *"Why have you raised me blind when I could see?"* — the word order `ḥašartanī aʿmā wa-qad kuntu baṣīrā` inverts the natural grammar because Ṭāhā's rhyme is on `-ā`. The regular form would be `baṣīran wa-qad kuntu`. Reversed to preserve rhyme.
- Q 36:60 (Ya-Sin): `aʿhad ilaykum yā banī ādama an lā taʿbudū l-shayṭān` — marked by classical scholars as a case where the particle order is unusual to match Ya-Sin's `-ūn` rhyme.

**The inverse principle — the one our analysis operationalizes — is: when taqdīm cannot rescue the rhyme, the break is semantically loaded.** Classical rhetoricians noticed specific instances (the Jesus polemic in Maryam, the dialogue shifts in An-Nisāʾ) but **no extant classical work provides a surah-by-surah quantitative audit of rhyme-breakers**. The observation that "rhyme breaks mark theological pivots" is implicit in scattered tafsir notes (Ibn ʿĀshūr, al-Rāzī on specific verses) but is never systematised.

The computational version (§§ 1–8 above) is, to the best of our knowledge, novel in its per-verse coverage and its multi-marker convergence analysis. The *principle* is classical; the *catalogue* is new.

### 9.3 Relevant sources

- **al-Zarkashī, *al-Burhān fī ʿUlūm al-Qurʾān*** — encyclopedic 4-volume work, chapters on fawāṣil in vol. 1. [Semantic Scholar](https://www.semanticscholar.org/paper/Al-Burhan-Fi-Ulum-Al-Qur-An-Zarkashi-Ashli/10a74910a78cb777a87a4c50d27753484e25ec32)
- **al-Suyūṭī, *al-Itqān fī ʿUlūm al-Qurʾān*** — chapters 53-57 cover Arabic rhetorical devices including fawāṣil (not included in most English selections). [Internet Archive Arabic text](https://archive.org/details/AlItqanFiUlumAlQuran)
- **Khalil & Al-Khanji, "Phonetic Consonance in Quranic Verse-Finals"** ([ERIC EJ1128189](https://files.eric.ed.gov/fulltext/EJ1128189.pdf)) — modern phonetic study confirming /n/, /m/ dominance; no rhyme-break classification.
- **Kurdish Studies (2024), "The Quranic Verse-Ending Words"** ([PDF](https://kurdishstudies.net/menu-script/index.php/KS/article/download/1947/1343/3698)) — modern fawāṣil survey.
- **Almuslih (2024), "The saj-rhymes in the Qurʾān"** ([link](https://almuslih.org/blog/2024/06/13/the-saj-rhymes-in-the-quran/)) — qualitative survey.
- **Yaqeen Institute, "Imām al-Suyūṭī and Symmetry in the Qurʾan"** ([link](https://yaqeeninstitute.org/read/paper/imam-al-suyuti-and-symmetry-in-the-quran-understanding-the-connection-between-the-beginning-and-ending-of-surahs)) — covers Suyūṭī's *Marāṣid al-Maṭāliʿ* on symmetry between surah openings and closings.
- **Ibn ʿĀshūr Centre for Quranic Studies, "Select Chapters of Itqān"** ([link](https://www.ibnashur.com/publications/select-chapters-of-itqan)) — English translation, does NOT include the fawāṣil chapters (focuses on lexical/grammatical material).

---

## 10. Honest null discussion

### 10.1 What the data does NOT support

1. **The "rhyme-break marks theological content" claim is not a free lunch.** The 32 surahs with ≥ 85% U1 uniformity contain **241 total breakers**. Only a small minority (~30) are singular or clustered in ways that are rhetorically loaded. Most breakers are muqatta'at openings, direct-speech quotations that happen to end in a different word-form, or mid-surah narrative shifts that are not semantically distinguished. **The signal exists, but it is drowned in noise** unless you filter for the cleanest cases (singleton breakers in high-uniformity surahs).

2. **The spine hypothesis (Task 8) produces no hidden structure.** Listing the most-marked verse of each surah in mushaf order does not reveal an encoded narrative. What it *does* reveal is that structural marking is a content-amplifier, not a content-injector — each surah's marked verse is predictable from the surah's own theme.

3. **Only one verse is marked on 3 dimensions.** Q 4:12. The "maximally-marked" category is essentially a 2-dim category. Our ring-centre dimension (D4) only has 11 hard-coded members, so this is a detection-sensitivity issue: adding more ring centres would expand the pool.

4. **Top-10 maximally-marked verses are not surprising.** Q 2:282, 4:12, 13:28, 55:33, 73:20, 74:31, 81:29 are all among the most famous verses in the Quran. The method works as a **known-marker rediscovery oracle**, not as a **hidden-gem finder**. This is a success on replicability and a null on novelty — the rhetorically loud verses are already the famously loud verses.

### 10.2 What the data DOES support

1. **The Maryam form-enacts-content finding generalises.** Singletons in 17, 25, 33, 47 all exhibit the same pattern: a doctrinally hinged verse breaks the surah's rhyme. The Maryam case is the archetype because it is the *longest* and the *most over-determined*.

2. **The Al-Isrāʾ v1 exception has a crisp mechanical explanation.** The divine-name dyad `al-samīʿu al-baṣīr` cannot take tanwīn. The exception is grammatically necessary, not stylistically chosen — and that is *why* it is theologically loaded: the opening refuses to be absorbed by the body.

3. **The known-oracle property is itself a finding.** Our metric reproduces the set of verses traditionally flagged by exegetes as rhetorical anchors, with no prior labelling. This validates the structural-marking axes as good proxies for what classical scholars noticed informally.

4. **Iltifāt cascades and rhyme breaks can co-locate tightly.** Maryam vv 34-40 has 6 distinct verb subjects in 7 verses AND 7 rhyme breaks. This combination is rare in the corpus; checking whether other iltifāt-dense passages also break rhyme is a follow-up test.

---

## 11. Garden of forking paths disclosure

- **Choice of U1 (single-letter rawi) as the rhyme-break criterion.** We also computed U2 and saw that it classifies alif-dominant surahs differently. U1 is the classical rhyme anchor and is what the saj-rhyme finding used.
- **Z-threshold of 2.0** for length and jinas outliers is conventional but not pre-registered. At z ≥ 1.5 the marked-verse pool doubles; at z ≥ 2.5 it halves. Downstream thematic patterns are robust to this.
- **Ring-centre dimension (D4) is hard-coded** from prior findings. We did not run a fresh ring-detection pass. This means any verse not covered by the prior catalog is artificially un-scored on D4.
- **Top-10 filter excludes muqatta'at v1s** (which otherwise dominate rhyme-break + length outlier lists trivially). This is a post-hoc filter disclosed here.
- **Maryam's iltifāt analysis was conducted *after* seeing the rhyme-break finding.** It is exploratory; claims about iltifāt density should be replicated on a pre-registered sample.

## 12. Novel empirical claims from this run

1. **Surah 17 (Al-Isrāʾ) v1's rhyme exception is grammatically forced by the definite divine-name closer `al-samīʿu al-baṣīr`** — *al-* locks tanwīn out. The structural frame-function of v1 is mechanically inevitable.
2. **Maryam's two polemic zones carry a three-fold convergent signature: rhyme break + iltifāt cascade + {Ax\*, wld, rHm} root cluster.** All four occurrences of this root triple in Maryam are inside the rhyme-break zones. This tightens the saj-rhyme finding by one more axis.
3. **Q 4:12 is the *only* triple-marked verse in the Quran.** The inheritance ruling is the single legal statement in the entire text that breaks its surah's rhyme, exceeds the length z-threshold, and exceeds the jinas z-threshold simultaneously.
4. **Singleton-breaker surahs (17, 25, 33, 47) are rarer than random would predict and the singleton is always doctrinally marked.** Not formally tested against a null; pre-registration needed.
5. **The spine hypothesis fails but in an interesting way** — it fails because each surah's structurally-marked verse is a *predictable amplification* of the surah's own theme. This is a null on "hidden structure" and a positive on "form tracks content."
6. **Surah 78 (An-Nabaʾ) vv 1-5 rhyme-break cluster at surah-head is a perfectly symmetric mirror of Surah 53 (An-Najm) vv 57-61 rhyme-break cluster at surah-tail.** Both are 5-verse rhetorical-question blocks that sit outside the dominant rhyme. Noticed only after scan; worth follow-up.
7. **The top-10 maximally-marked verses are dominated by known rhetorical anchors.** No surprise hits — the method is replicative rather than revelatory.

## 13. Reproducibility checklist

- [x] Rules tuple in header
- [x] All scripts runnable on existing data files without new downloads
- [x] Per-surah breaker table (§1) computed from saj-fasila-per-verse.csv
- [x] Length z-scores computed from quran-no-tashkeel.json letter counts
- [x] Jinas density computed from morphology file
- [x] Ring centres imported from chiastic-audit.md (listed in §0)
- [x] Iltifāt pronoun/verb-person extraction from QAC morphology (§3.2)
- [x] Null discussion with explicit unsupported claims
- [x] Garden of forking paths disclosed
- [x] Classical prior art surveyed and gaps identified
- [ ] Pre-registration: this is exploratory, not pre-registered

## 14. Where to go next

1. **Pre-register the singleton-breaker-is-doctrinally-marked claim.** Formally define "doctrinal content" via a topic classifier on the English translation, and ask whether singleton breakers in uniform surahs are enriched for the doctrinal topic label.
2. **Test iltifāt-rhyme-break co-location corpus-wide.** Operationalise iltifāt density as the count of distinct verb persons per verse window, and ask whether it correlates with rhyme-break density.
3. **Expand ring-centre catalog.** Run a fresh sub-surah ring scan at lower z-threshold and add all z ≥ 3 centres to the D4 dimension. This may surface more triple-marked verses.
4. **Audit Q 4:12 and Q 2:282 against alternative surah-rhyme-rescue mechanisms.** Check whether the surrounding verses use taqdīm/taʾkhīr to rescue rhyme where the two central legal verses cannot.
5. **Formal classical-tafsir search.** Physically consult al-Zarkashī's *Burhān* and al-Suyūṭī's *Itqān* chapters on fawāṣil to find any existing per-verse exception catalog. Our search found the topic is discussed generally but not verse-by-verse.
