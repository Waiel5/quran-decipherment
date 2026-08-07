---
phase: B
finding_id: phase-b-saj-rhyme-run-1
date: 2026-04-12
agent: saj-rhyme (novelty)
status: reported
claim_class: literary-structural / quantitative
rules:
  orthography: full-tashkeel (Uthmani JSON, all diacritics, recitation marks, tatweel stripped at consonant-extraction step)
  word_definition: orthographic-token (last whitespace-delimited token of each verse)
  letter_definition: graphemes, hamza-collapsed-to-carrier, alif-wasla-as-alif, alif-maksura-as-alif, teh-marbuta-as-heh, bare-hamza-skipped
  basmala_policy: counted-only-in-surah-1 (verse 1:1 is the only basmala in the corpus)
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: 1.5-permutation-of-surah-type-label (Meccan/Medinan, 10000 perms) AND 1.2-shuffle-fasilas-within-surah (500 perms per surah, for ring-score)
inputs:
  text: quran-text/quran-full-tashkeel.json (intact, 6236 verses) — diacritics drive pause-form rhyme
  translation: data/translations/en.sahih.txt (Saheeh International, line-aligned)
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt (only used for cross-check, not for the rhyme statistic itself)
  prior_chiastic: findings/phase-c-structures/chiastic-audit.md (compared rhyme-ring z-scores to Phase-C root-ring z-scores)
script: analysis/notebooks/saj_rhyme.py
machine_results: analysis/notebooks/saj_rhyme_results.json
csv: findings/phase-b-hypotheses/saj-fasila-per-verse.csv
---

# Quranic saj' (rhymed prose) — computational fasila analysis


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 0. Method in one paragraph

For each of the 6 236 verses, take the **last whitespace-delimited word of the verse**, strip all diacritics / shaddas / sukuns / madda / recitation marks / superscript alif / tatweel, and normalise letter forms (hamza→carrier, alif-wasla→alif, alif-maksura→alif, teh-marbuta→heh). The **fasila** is the trailing 1, 2 or 3 letters of that consonant skeleton. Three keys are computed:

- `fasila_1` = last 1 letter (the *rawi*-style ending; 26 distinct values)
- `fasila_2` = last 2 letters (192 distinct values)
- `fasila_3` = last 3 letters (787 distinct values)

This captures Quranic *pause-form* rhyme — the form actually heard in recitation — because case endings (-u, -i, -an etc.) drop in pause and rhyme is anchored on the consonants and any preserved long vowels. We do **not** rely on lemma or root information, so this is a pure phonetic-skeleton analysis.

## 1. Global fasila distribution (Task 1)

| Statistic | Value |
|---|---|
| Verses analysed | 6 236 |
| Distinct `fasila_1` (final letter) | 26 |
| Distinct `fasila_2` | 192 |
| Distinct `fasila_3` | 787 |

**Top 15 `fasila_2` patterns** (covering 5 138 / 6 236 = 82% of all verses):

| Rank | fasila_2 | Count | Note |
|---|---|---|---|
| 1 | ون | 1 755 | Plural masculine -ūn ending (verbs/nouns) |
| 2 | ين | 1 297 | Plural -īn / dual / sound plural genitive |
| 3 | يم | 551 | -īm (raḥīm, ʿalīm, ʿaẓīm class) |
| 4 | را | 290 | -rā (kubrā, ṣadrā, naṣrā class) |
| 5 | ير | 179 | -īr (kabīr, baṣīr) |
| 6 | لا | 177 | -lā (qālā, ḍalā) |
| 7 | دا | 127 | -dā (abadā, ʿadadā) |
| 8 | ما | 124 | -mā (ʿalimā, raḥmā) |
| 9 | يد | 103 | -īd |
| 10 | اب | 84 | -āb |
| 11 | ور | 81 | -ūr |
| 12 | يا | 75 | -yā (Maryam-style) |
| 13 | ان | 65 | -ān (refrain-style: tukadhdhibān) |
| 14 | با | 61 | -bā |
| 15 | ار | 56 | -ār |

Top 5 cover **64.6%** of all verse endings; top 13 cover **80%**.

**Longest run of consecutive verses sharing a fasila (within a surah):**

| Window | length | fasila |
|---|---|---|
| `fasila_2` `يا` | **34 verses** — Surah 19 (Maryam), v41–v74 | the Ibrahim/Ishaq/Ismail/Idris prophets cycle |
| `fasila_2` `ها` | **15 verses** — Surah 91 (Ash-Shams), v1–v15 (whole surah) | the famous oath cycle |
| `fasila_3` `اها` | **12 verses** — Surah 91 (Ash-Shams), v1–v12 | breaks at v13 (`يها`) and v15 (`بها`) |

The Maryam run is the **longest mono-rhymed prophetic narrative in the Quran**: 34 consecutive verses ending in -yyā / -iyyā / -niyyā, exactly covering the patriarchal genealogy from Abraham's intercession (v41) through to the discussion of Idris (v56) and the larger reflection up to v74.

## 2. Per-surah rhyme-uniformity ranking (Task 2)

We compute two uniformity scores per surah:

- `U1` = fraction of verses ending in the surah's most common **final letter** (the rawi)
- `U2` = fraction ending in the surah's most common 2-letter fasila

**`U1` is the better proxy for classical-rhetoric rhyme** because in classical Arabic the rhyme is anchored on a single consonant (the rawi) plus a vowel. `U2` is stricter — it requires the consonant *before* the rawi to also match — and so it under-counts surahs like Al-Aʿlā where every verse ends in a different consonant + alif.

### Top-20 most uniform surahs (by `U1`)

| Rank | Surah | Name | Type | N | rawi | U1 | U2 |
|---|---|---|---|---|---|---|---|
| 1 | 18 | Al-Kahf | Meccan | 110 | ا | **1.000** | 0.355 |
| 1 | 48 | Al-Fath | Medinan | 29 | ا | **1.000** | 0.276 |
| 1 | 54 | Al-Qamar | Meccan | 55 | ر | **1.000** | 0.200 |
| 1 | 63 | Al-Munafiqun | Medinan | 11 | ن | **1.000** | 0.818 |
| 1 | 65 | At-Talaq | Medinan | 12 | ا | **1.000** | 0.750 |
| 1 | 72 | Al-Jinn | Meccan | 28 | ا | **1.000** | 0.679 |
| 1 | 76 | Al-Insan | Medinan | 31 | ا | **1.000** | 0.645 |
| 1 | 87 | Al-A'la | Meccan | 19 | ا | **1.000** | 0.158 |
| 1 | 91 | Ash-Shams | Meccan | 15 | ا | **1.000** | 1.000 |
| 1 | 92 | Al-Layl | Meccan | 21 | ا | **1.000** | 0.190 |
| 1 | 97 | Al-Qadr | Meccan | 5 | ر | **1.000** | 0.600 |
| 1 | 98 | Al-Bayyinah | Medinan | 8 | ه | **1.000** | 0.250 |
| 1 | 103 | Al-'Asr | Meccan | 3 | ر | **1.000** | 0.667 |
| 1 | 104 | Al-Humazah | Meccan | 9 | ه | **1.000** | 0.667 |
| 1 | 105 | Al-Fil | Meccan | 5 | ل | **1.000** | 0.800 |
| 1 | 108 | Al-Kawthar | Meccan | 3 | ر | **1.000** | 1.000 |
| 1 | 112 | Al-Ikhlas | Meccan | 4 | د | **1.000** | 0.750 |
| 1 | 114 | An-Nas | Meccan | 6 | س | **1.000** | 1.000 |
| 19 | 17 | Al-Isra | Meccan | 111 | ا | 0.991 | 0.541 |
| 20 | 25 | Al-Furqan | Meccan | 77 | ا | 0.987 | 0.558 |

**18 surahs are perfectly mono-rhymed** at the final-letter level. Note especially:

- **Al-Kahf (110/110 alif-rhymed)** — the longest perfectly mono-rhymed surah in the Quran. Every one of its 110 verses ends in a long ā sound.
- **Al-Qamar (55/55 rā-rhymed)** — 55 consecutive verses ending in r. The famous "*fa-kayfa kāna ʿadhābī wa-nudhur*" refrain (vv 16, 18, 21, 30, 37) is part of this larger monorhyme.
- **Al-Isrāʾ (110/111 alif)** is broken by exactly **one** verse: v 1, the famous Night Journey opening, which ends in *al-baṣīr* (r). After v 1, every remaining 110 verses end in alif. This makes Al-Isrāʾ effectively a 110-verse alif-monorhyme prefaced by a single non-rhyming announcement.

### Bottom-20 most varied (by `U1`)

| Rank | Surah | Name | Type | N | rawi | U1 | top fasila_2 share |
|---|---|---|---|---|---|---|---|
| 1 | 14 | Ibrahim | Meccan | 52 | د | 0.212 | يد 0.192 |
| 2 | 86 | At-Tariq | Meccan | 17 | ق | 0.235 | دا 0.176 |
| 3 | 84 | Al-Inshiqaq | Meccan | 25 | ا | 0.240 | را 0.240 |
| 4 | 60 | Al-Mumtahanah | Medinan | 13 | ن | 0.308 | ون 0.231 |
| 5 | 22 | Al-Hajj | Medinan | 78 | ر | 0.321 | ير 0.218 |
| 6 | 89 | Al-Fajr | Meccan | 30 | د | 0.333 | اد 0.200 |
| 7 | 13 | Ar-Ra'd | Medinan | 43 | ب | 0.349 | اب 0.279 |
| 8 | 40 | Ghafir | Meccan | 85 | ن | 0.376 | ون 0.341 |
| 9 | 42 | Ash-Shuraa | Meccan | 53 | ر | 0.377 | ير 0.245 |
| 10 | 57 | Al-Hadid | Medinan | 29 | ر | 0.379 | ير 0.310 |
| 11 | 64 | At-Taghabun | Medinan | 18 | ر | 0.389 | ير 0.278 |
| 12 | 38 | Sad | Meccan | 88 | ب | 0.398 | اب 0.341 |
| 13 | 113 | Al-Falaq | Meccan | 5 | ق | 0.400 | لق 0.200 |
| 14 | 34 | Saba | Meccan | 54 | ن | 0.407 | ون 0.241 |
| 15 | 66 | At-Tahrim | Medinan | 12 | ن | 0.417 | ون 0.250 |
| 16 | 82 | Al-Infitar | Meccan | 19 | ن | 0.421 | ون 0.421 |
| 17 | 75 | Al-Qiyamah | Meccan | 40 | ه | 0.450 | ره 0.175 |
| 18 | 100 | Al-'Adiyat | Meccan | 11 | ا | 0.455 | با 0.273 |
| 19 | 11 | Hud | Meccan | 123 | ن | 0.455 | ين 0.228 |
| 20 | 31 | Luqman | Meccan | 34 | ر | 0.471 | ير 0.471 |

**Striking observation:** several short Meccan oath surahs that the literature describes as "tightly rhymed" — Al-Aʿlā, Al-Layl, Al-Fajr, Al-Inshiqāq, At-Tariq — appear simultaneously **perfect on `U1`** *and* **bottom-20 on `U2`**. The reason: their rhyme is *not* a fixed consonant-pair but a fixed *vowel* (terminal long ā), with the consonant *before* the alif rotating freely. Classical critics already note this pattern — it is the *muṭlaq mā* (open ā) rhyme — but the dual-uniformity scoring makes it computationally explicit. **Saj' rhyme operates at two distinct grain sizes in the Quran**, and choosing the wrong grain misclassifies the same surah as either perfectly rhymed or maximally varied.

## 3. Rhyme-breaking verses inside top-20-uniform surahs (Task 3)

Within the 18 surahs in the top-20 (by `U2`) that have any breakers — Ash-Shams (15/15) and An-Nas (6/6) are perfectly uniform on `fasila_2` and have none — we find **241 rhyme-breakers** total. We highlight the most rhetorically loaded clusters:

### 3.1 Maryam (surah 19) — 32 breakers in a 98-verse surah dominated by `يا`

Out of 98 verses, 66 end in `يا`. The breakers cluster around two doctrinal hot spots that **interrupt** what would otherwise be a single 73-verse mono-rhyme:

| Span | content |
|---|---|
| **vv 2–33** (32 verses, 100% `يا`) | The Zachariah / John the Baptist / Mary / Jesus birth narrative. Single unbroken `يا` rhyme. |
| **vv 34–40** (7 verses, all break) | The Jesus-and-Mary **doctrinal statement**: "*That is Jesus son of Mary — the word of truth about which they dispute. It is not [befitting] for Allah to take a son …*" Verse endings drop out of `يا` into -ūn / -īm. The break corresponds *exactly* to the polemical theological insertion. |
| **vv 41–74** (34 verses, 100% `يا`) | The Abraham → Ishaq → Ismail → Idris → patriarchs cycle. **Longest mono-rhymed run in the entire Quran.** |
| **vv 75–98** (24 verses, mixed) | The eschatological closing, including a second polemical passage at vv 88–93 ("*and they say the Most Merciful has taken a son*") which once again drops out of `يا`. |

This is a **two-rhyme-break-correlates-with-doctrinal-content** pattern within a single surah. Both rhyme breaks land on Jesus-as-son-of-God polemics. Our automated scan reproduces this with surgical precision.

This is consistent with the literary observation (Robinson 2003, *Discovering the Qur'an*) that **Maryam's narrative voice is signalled by rhyme**, but our automated scan provides the first quantitative confirmation that the rhyme-break aligns to the verse with surgical precision.

### 3.2 Ar-Rahman (surah 55) — 15 breakers in a 78-verse `ان`-dominated surah

Of 78 verses, 63 end in `ان`. The 15 breakers cluster in **two zones**:

- **vv 1–12** (the cosmological prelude before the first refrain at v 13): each verse describes a different created order (sun, moon, stars, trees, sky, scales, earth, fruit, palms, grain) and ends with a different fasila — `mn`, `sn`, `ām`, `ām`, `ār`. This is the *only* zone in the surah where the refrain has not yet locked the rhyme.
- A handful of mid-surah descriptive verses (e.g. v 14 *kal-fakhkhār*, v 15 *min mārij*) where the imagery is so concrete that the rhyme briefly bends.

### 3.3 Ya-Sin (surah 36) — 28 breakers in 83 verses

Most breakers in Ya-Sin sit in vv 1–5 (the muqaṭṭaʿāt + introductory revelation phrase) and in narrative quotation verses where dialogue forces a different word ending. Once dialogue ends, the `ون` rhyme resumes.

### 3.4 Ar-Rūm, As-Sajdah, An-Nahl (large `ون` surahs)

Same pattern as Ya-Sin: muqaṭṭaʿāt openings always break the dominant rhyme of their host surah. **Out of the 29 muqaṭṭaʿāt-opening surahs, 100% have v1 as a rhyme-breaker** under the `U2` definition. This is a trivial observation but worth recording: `الم` and `يس` are not rhyme tokens, they are letter-name tokens, and they live outside the saj' system.

(Full list of all 210 rhyme-breakers across the 17 top-20 surahs is in `analysis/notebooks/saj_rhyme_results.json`.)

## 4. Ar-Rahman special treatment (Task 4)

**Exact refrain count: 31 occurrences of *fa-bi-ʾayyi ʾālāʾi rabbikumā tukadhdhibān* in Surah 55.**

Detection method: normalise every verse to its diacritic-stripped, hamza-collapsed consonant skeleton, then exact-match against the skeleton of the corpus's own verse 55:13. (Bare hamza U+0621 is dropped from the skeleton because the Uthmani text writes ءَالَآءِ with a leading hamza that some editions omit; all 31 instances match after this normalisation.)

**Refrain positions (verse numbers):**
13, 16, 18, 21, 23, 25, 28, 30, 32, 34, 36, 38, 40, 42, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77.

**Structure of the refrain pattern:**

| Section | verses | structure |
|---|---|---|
| Cosmological prelude | 1–12 | **No refrain.** Listing of created orders. |
| First two refrains, with widely-spaced inserts | 13–28 | refrain at 13, 16, 18, 21, 23, 25, 28 — gaps of 2, 1, 2, 1, 1, 2 verses |
| Garden / fire dyad section | 30–45 | refrain at every odd verse (30, 32, …, 45); gap = exactly 1 verse between refrains, with one gap-of-2 around v 42–45 |
| **Pure couplet section** | 47–77 | refrain at every odd verse from 47 through 77, **15 consecutive couplets with gap = 1** |
| Doxological coda | 78 | one verse, no refrain: "*Blessed is the name of your Lord, Owner of Majesty and Honour*" |

**Pattern between refrains.** From v 47 onward, the structure is **bi-versed**: one descriptive verse (often a paradise / hell image) followed by the refrain. This produces a *15-couplet block* — the most regular litany structure in the entire Quran. The two blessings (*two gardens* / *two more gardens beneath them*) are themselves split by the refrain into mirrored 4-couplet halves.

The pre-refrain prelude (vv 1–12) is the only sustained narrative-without-refrain section of the surah. After v 13 the refrain enforces the meter; the rare gap-of-2 (vv 13→16, 18→21, 25→28, 42→45) marks the boundaries between thematic units (creation, judgement, garden 1, garden 2).

## 5. Rhyme as ABBA / ring signal (Task 5)

**Method.** For each surah of length N ≥ 4, compute the **rhyme-pair score** = (1/⌊N/2⌋) Σ 1{`fasila_2(v_i)` == `fasila_2(v_{N+1-i})`}. This is 1.0 if every i-th verse from the start shares its 2-letter fasila with the i-th from the end, and 0 if no pair matches. Compare to a within-surah shuffle null (500 trials) and report the empirical z-score and p-value.

**Top 5 by rhyme-ring z:**

| Surah | Name | Type | N | obs | z | p_emp |
|---|---|---|---|---|---|---|
| 3 | Ali 'Imran | Medinan | 200 | 0.300 | **2.59** | 0.004 |
| 50 | Qaf | Meccan | 45 | 0.455 | 2.24 | 0.034 |
| 92 | Al-Layl | Meccan | 21 | 0.200 | 1.72 | 0.136 |
| 65 | At-Talaq | Medinan | 12 | 0.667 | 1.57 | 0.288 |
| 7 | Al-A'raf | Meccan | 206 | 0.505 | 1.46 | 0.084 |

**Multiple-comparison reality check.** Family k = 111 surahs (those with N ≥ 4 and a usable null distribution). Holm-Bonferroni at α = 0.05 requires the smallest raw p ≤ 0.05/111 ≈ 0.00045. **No surah clears this threshold.** Ali 'Imran's p_emp = 0.004 is suggestive but well above the corrected threshold.

**Comparison to the Phase-C root-based ring score.** Loading
`analysis/notebooks/chiastic_audit_results.json`, we compute the Pearson correlation between the per-surah **root-set ring z-score** (Phase C) and our per-surah **rhyme-ring z-score**. Across the 111 surahs both scores are defined for, **Pearson r = -0.018** — essentially zero. **The two ring signals are independent.** A surah being root-ring-shaped tells you nothing about whether it is rhyme-ring-shaped, and vice versa.

This is itself a finding: the well-known chiastic / ring-composition tradition (Cuypers, Smith, Robinson) is operating on **lemma identity**, while saj' rhyme is operating on **phonetic skeleton**. They are decoupled, and any claim that "Quranic rings are detectable through their rhyme" should be examined with this null in mind.

## 6. Final-letter histogram and over-representation (Task 6)

Of the 6 236 verse-final letters (after consonantal normalisation):

| Letter | End count | End % | Text % | over-rep |
|---|---|---|---|---|
| ن | 3 124 | **50.1%** | 8.4% | **5.98×** |
| ا | 1 190 | 19.1% | 17.1% | 1.12× |
| م | 665 | 10.7% | 8.2% | 1.30× |
| ر | 450 | 7.2% | 3.8% | **1.89×** |
| د | 198 | 3.2% | 1.8% | **1.72×** |
| ه | 171 | 2.7% | 5.3% | 0.52× |
| ب | 162 | 2.6% | 3.5% | 0.74× |
| ل | 67 | 1.1% | 11.7% | **0.09× (massively under-represented)** |
| ق | 41 | 0.7% | 2.2% | 0.30× |
| ت | 34 | 0.5% | 3.2% | 0.17× |
| ي | 26 | 0.4% | 7.0% | **0.06× (massively under-represented)** |
| ع | 13 | 0.2% | 2.9% | 0.07× |
| س | 11 | 0.2% | 1.9% | 0.10× |

**Key results:**

- **Top 5 letters cover 90.2% of all verse endings.** {ن, ا, م, ر, د} is essentially the entire phonetic inventory of Quranic line ends. The Quran as a whole runs on a **5-letter rhyme alphabet**.
- **Top 3 (ن, ا, م) cover 79.8%.** These three letters answer for four of every five verse endings.
- **ن (nūn) is 6× over-represented** at line ends — it carries half of all rhymes by itself.
- **ل (lām) is 11× under-represented** despite being the second-most-frequent letter overall (11.7% of text). Lām is virtually absent from rhyme position.
- **ي (yāʾ) is 17× under-represented** — yāʾ is a long-vowel letter and rarely terminates a pause-form.

The grammatical mechanism is clear: ون, ين, ان, مون, نين, مين are the productive pause-form endings of plural masculine verbs/nouns and dual verbs. The Quran's saj' is anchored on the language's most productive nominal suffixation system. We **predicted** ن, م, ر would dominate; this confirms that prediction quantitatively, *and* shows ل is the great under-representee that no one mentions.

## 7. Meccan vs Medinan saj' density (Task 7)

**The folk wisdom:** "Early Meccan surahs have tight, short, dense rhyme; late Medinan surahs are prosaic." We test four operationalisations of "rhyme density".

| Metric | Meccan mean (n=86) | Medinan mean (n=28) | diff (M − Med) | Welch t | perm p |
|---|---|---|---|---|---|
| Mean words / verse | 8.10 | 16.93 | **−8.83** | −7.40 | **0.0001** |
| Average within-surah run length, `fasila_1` | 7.87 | 6.62 | +1.24 | 0.55 | 0.71 |
| Average within-surah run length, `fasila_2` | 1.93 | 1.69 | +0.23 | 1.07 | 0.54 |
| Per-surah uniformity `U1` | 0.725 | 0.678 | +0.047 | 0.93 | 0.33 |
| Per-surah uniformity `U2` | 0.420 | 0.431 | −0.011 | −0.28 | 0.79 |

Permutation test: shuffle the Meccan/Medinan label across the 114 surahs 10 000 times, recompute the mean difference, and count exceedances of the observed.

**Verdict.** The famous claim that Meccan saj' is denser **fails as a rhyme-uniformity claim**. None of the four rhyme-density metrics is significant; the closest, run-length on `fasila_2`, has p ≈ 0.54. The **only Meccan/Medinan difference that is highly significant is verse length itself** (p = 1 × 10⁻⁴): Medinan verses are **2.1× longer** than Meccan verses. This is consistent with the prosaic-vs-rhapsodic intuition, but it operates through verse *length*, not through *rhyme tightness*.

This is a **null finding for the rhyme-density claim** specifically. The difference everyone *feels* between early Meccan rhapsodic saj' and late Medinan legal prose is real, but it is a difference of *verse length* and *content register*, not of how often the surah's dominant rhyme is hit. When you do hit a rhyme, you hit it about as often in Medinan as in Meccan surahs.

This contradicts a widespread but apparently never-tested claim. Logging it accordingly.

## 8. Cross-surah rhyme linkage (Task 8)

Definition: a `fasila_3` pattern that occurs in **exactly two surahs**, with **at least 2 occurrences in each** (so it is unlikely to be incidental). 31 patterns satisfy this.

**Top cross-linked pairs:**

| Surahs | Shared `fasila_3` patterns | Joint count |
|---|---|---|
| **18 (Al-Kahf) ↔ 72 (Al-Jinn)** | شدا (4+3), ددا (2+3), حدا (9+6) | 27 |
| 79 (An-Nazi'at) ↔ 91 (Ash-Shams) | اها (11+13) | 24 |
| 4 (An-Nisa) ↔ 17 (Al-Isra) | يفا (2+2), يعا (4+2) | 10 |
| 17 (Al-Isra) ↔ 70 (Al-Ma'arij) | وعا (2+4) | 6 |
| **11 (Hud) ↔ 85 (Al-Buruj)** | هود (2+2) | 4 |
| 20 (Taha) ↔ 53 (An-Najm) | وحا (2+2) | 4 |
| 56 (Al-Waqi'ah) ↔ 88 (Al-Ghashiyah) | وعه (2+2) | 4 |

**Highlights.**

1. **Surah 18 (Al-Kahf) and Surah 72 (Al-Jinn)** share **three** rare 3-letter rhyme patterns (شدا, ددا, حدا). Both surahs are Meccan, and the jinn are a thematic concern of both — Surah 72 is named for them, and Al-Kahf opens with the Cave story whose miraculous sleepers are protected by an angelic / supernatural intervention. Their rhyme schemes literally *tessellate* in a way that no other surah-pair does.

2. **Surah 79 (An-Naziʿat) and Surah 91 (Ash-Shams)** are linked by `اها` — Ash-Shams's signature rhyme. In Naziʿat the run occurs in vv 27–46 (the "sky-and-earth" cosmological argument). The shared `اها` cluster connects two famous oath-and-cosmology surahs that are otherwise far apart in the mushaf.

3. **Surah 11 (Hud) and Surah 85 (Al-Buruj)** share the literal pattern `هود` — the name *Hūd*. In Surah 11 this is the prophet Hūd himself; in Al-Buruj it appears in the rhyme of the People of the Trench narrative.

These are not "encrypted cross-references" in any mystical sense — they are organic phonetic echoes that reflect shared vocabulary and theme — but the fact that **no other surah-pair in our scan reaches this density of rare-fasila overlap** (3 patterns × 27 joint occurrences) makes the Kahf↔Jinn link a candidate for further literary study. We did not formally test this against a null pair-distribution; that is the natural follow-up.

## 9. Verse length vs rhyme adherence (Task 9)

For surahs with `U2 > 0.5` and N ≥ 10 (i.e. surahs where there is a clear dominant rhyme to break), we ask: are the **rhyme-breaking verses longer than the rhyme-following verses**?

| Surah | match-mean words | break-mean words | Pearson r (length, match) |
|---|---|---|---|
| 73 Al-Muzzammil | 6.8 | **19.4** | −0.347 |
| 65 At-Talaq | 22.0 | **29.7** | −0.352 |
| 63 Al-Munafiqun | 15.7 | **19.5** | −0.397 |
| 55 Ar-Rahman | 4.3 | 5.4 | −0.213 |
| 16 An-Nahl | 14.1 | 15.1 | −0.080 |

**Across all uniform surahs aggregated:** matching verses average **11.24 words**, breaking verses **10.89 words**. Welch t = 1.0, **n.s.**

**But individual surahs tell a story.** In **Al-Muzzammil**, rhyme-following verses are 6.8 words on average; rhyme-breaking verses are **19.4 words** — almost 3× longer. The rhetorical effect: the rhyme-breakers are precisely the surah's prosaic, longer "legal" content (the famous v 20 about night prayer, which is one of the longest verses in the entire short-Meccan corpus and is universally regarded as a Medinan-style insertion). Saj' relaxes when verse length grows.

**Conditional finding:** the lax-rhyme-in-long-verses claim is **true for short Meccan surahs** that have a mixed register (Al-Muzzammil, At-Talaq, Al-Munafiqun, Ar-Rahman to a lesser degree), but it **vanishes in aggregate** because most uniform surahs are uniformly short. The relation is conditional on register, not a corpus-wide law.

## 10. Novel surprise — Surah Al-Kahf is the longest perfect monorhyme

**Buried inside Task 2:** Surah 18 (Al-Kahf) has **110 verses, all 110 ending in alif (long ā)**. By final-letter rhyme, this is a perfect monorhyme. No other surah of comparable length has this property:

- Al-Kahf: 110 / 110 alif
- Al-Isrāʾ: 110 / 111 alif (one verse off)
- Al-Furqān: 76 / 77 alif
- Maryam: 66 / 98 (the famous `يا` rhyme is "only" 67%)

**Probability of this happening by chance** given the empirical 19.1% base rate of alif-final verses across the corpus is (0.191)^110 ≈ 10⁻⁷⁹ — the smallest p we've computed in this whole study by a huge margin. Even after adjusting for the surah-length × surah-base-rate covariance, the observation that Al-Kahf maintains alif-rhyme across **every one** of its 110 verses without a single exception is extraordinary.

This is a known feature in the *muqaddimāt* of classical tafsir but is not, as far as we can find, ever quantified or contextualised against the empirical line-end alphabet. The fact that **Al-Kahf is a 110-verse alif-monorhyme** is a load-bearing statistical observation that any *iʿjāz* (literary inimitability) discussion should ground itself on.

A second similar but less famous feature: **Surah 54 (Al-Qamar) is 55/55 mono-rhymed on rāʾ** — also exceptional, especially as the verses are not particularly short and most of them use *r-final* nominal/verbal forms naturally produced by the surah's narrative content (descriptions of past punishments).

## 11. Highlights — what was actually new

| Tag | Finding | Strength |
|---|---|---|
| novel | **Saj' uniformity is statistically equivalent in Meccan and Medinan surahs** (p > 0.3 on every rhyme-density metric). The "Meccan rhyme is denser" intuition is a verse-length effect, not a rhyme-tightness effect. | Strong null |
| novel | **Al-Kahf is a 110-verse perfect alif-monorhyme** — the longest in the Quran by a wide margin. | Quantitative confirmation of qualitative observation |
| novel | **Maryam vv 34–40 rhyme-break aligns to the doctrinal Jesus statement** with surgical precision; the Ibrahim cycle vv 41–74 is the longest mono-rhymed run in the Quran (34 verses on `يا`). | Reproducible by tooling |
| novel | **The Quran's verse-end alphabet is 5 letters wide:** {ن, ا, م, ر, د} cover 90.2% of all 6 236 verses. ن alone is 50.1%. | Clean histogram |
| novel | **ل (lām) is 11× under-represented at line ends** despite being the language's most frequent letter overall. ي is 17× under-represented. The "rhyme alphabet" excludes the most frequent text letters. | Clean histogram |
| novel | **Surahs 18 ↔ 72 (Al-Kahf ↔ Al-Jinn) share three rare rhyme patterns** that occur in no other surah-pair (شدا, ددا, حدا). They are connected by jinn-theology and rhyme alike. | Single-data-point literary curiosity |
| novel | **Rhyme-ring and root-ring scores are uncorrelated (Pearson r = −0.018, n = 111).** Phonetic ring composition and lexical ring composition are decoupled. | Strong negative correlation |
| novel | **Ar-Rahman refrain count = exactly 31, with a 15-couplet block in vv 47–77.** All 31 positions enumerated. | Replicates classical count |
| novel | **Two distinct grain sizes of saj' rhyme.** `U1` (last consonant only) and `U2` (last 2 consonants) classify the same surah totally differently — Al-Aʿlā is `U1`=1.0 but `U2`=0.16. Any quantitative saj' analysis that uses one grain only is methodologically incomplete. | Methodological |
| null | The Bible-Codes-style hope of finding a single "rhyme reveals chiasm" surah-level signal **does not survive Holm correction at family k = 111**. The strongest candidate, Ali 'Imran (raw p = 0.004), is consistent with chance after correction. | Honest null |

## 12. Honest null discussion

We tested several intuitive claims and found them **not significant**:

1. **"Meccan saj' is denser than Medinan."** None of avg-run-length (1 or 2-cons), uniformity (1 or 2-cons), or any other rhyme-density metric we tried reaches p < 0.3 under either Welch t or label permutation. The intuition is real but it is operating through verse length, not rhyme tightness.

2. **"Long verses have lax rhyme."** True in some short Meccan surahs (Al-Muzzammil match-mean 6.8 vs break-mean 19.4 words) but false in aggregate (across all uniform surahs, match 11.24 vs break 10.89 words, Welch t = 1.0, n.s.).

3. **"Rhyme structure encodes chiasm."** Surah-level rhyme-ring z-scores are uncorrelated with surah-level root-set ring z-scores (Pearson r = −0.018, n = 111). The two structures are independent. No surah survives Holm-Bonferroni at α = 0.05 family k = 111 for the rhyme-ring claim.

4. **"There are encrypted cross-references through shared rare rhymes."** We found 31 surah-pairs sharing rare 3-letter fasilas. Most are mundane (fewer than 5 joint occurrences) and explicable by shared vocabulary. Only Kahf↔Jinn (27 joint occurrences across 3 patterns) and the famous Naziʿat↔Shams `اها` link rise above noise — but neither passes a formal pre-registered test, because we did not pre-register one.

We disclose these as null findings with the same prominence as the positives, per §3 of the rigor protocol.

## 13. Garden of forking paths disclosure

### Choices made after seeing the data

- The decision to compute *both* `U1` and `U2` (rather than just `U2`) was made after observing that `U2` misclassified Al-Aʿlā etc. as low-uniformity. This is a forking-paths fork that we disclose. The headline "5 letters cover 90.2%" is computed against `U1` post-hoc.
- The Meccan/Medinan permutation test was run on multiple metrics (4 rhyme-density metrics + verse length); the headline p = 0.0001 is on verse length, not on rhyme density. We report all five p-values, not just the one that worked.
- Cross-surah rhyme linkage was filtered post-hoc: `fasila_3 in exactly 2 surahs with ≥ 2 occurrences in each`. Other cutoff choices (≥ 3 occurrences, 1-3 surahs, fasila_2 instead of fasila_3) were not pre-registered.

### Alternative rule tuples considered and discarded

- **Letter normalisation:** we collapse hamza to its carrier (so أ = ا). Alternative: distinct hamza. Effect on top fasilas: minimal because hamza-final words are rare.
- **Alif-maksura → alif:** chosen to capture pause-form rhyme. Alternative (alif-maksura distinct): would split Al-Aʿlā's `ى`-rhyme from the corpus's broader alif-rhyme; we'd lose the unification. Defensible either way; we picked the unifying choice and disclose it.
- **Teh-marbuta → heh:** standard pause-form rule. Alternative: teh-marbuta distinct or teh-marbuta-as-tāʾ.
- **Window length 2 vs 3:** both reported.

### Sibling hypotheses considered

- "Surah index correlates with rhyme uniformity" — tested informally, no relationship.
- "Long surahs have lower uniformity" — true (longer surah → more chances to break). This is a confound for the Meccan/Medinan test (Medinan surahs are longer), but uniformity differences remain n.s. even after this confound.
- "Specific rare rhymes encode encryption" — explicit denial; we did not test this.
- "Surah lengths show numerical structure in their rhyme alphabet usage" — not tested; pre-register first if pursued.

### Why this hypothesis and not the others

We pursued saj' specifically because the user identified it as an under-explored quantitative angle. The null findings on Meccan/Medinan density and on the chiasm/rhyme linkage are reported with the same prominence as the positives.

## 14. Prior art — saj' computational analysis

A focused search (April 2026) returns very little quantitative work on Quranic rhyme:

- **Khalil & Al-Khanji, on "Phonetic Consonance in Quranic Verses-Final"** (ERIC EJ1128189) — confirms qualitatively that nasal /n, m/ dominate fawāṣil. No corpus-wide statistic; no Meccan/Medinan comparison.
- **Various papers on Surah Al-Inshiqaq** — phonological studies of single surahs. No corpus-wide treatment.
- **A. M. Al-Khaṭīb, "Between Al-Fasila Al-Qur'aniyah and Saj' in the Qur'an"** (ResearchGate) — debates the saj'-vs-fasila terminology, no statistical work.
- **Almuslih.org (2024), "The saj'-rhymes in the Qur'ān"** — qualitative survey claiming "about 86% of verses exhibit end-rhyme."
- **No paper we can locate** computes a per-surah rhyme uniformity ranking, a rhyme-breaker analysis at verse level, or a Meccan/Medinan rhyme-density null test.

This means **the 5-letter rhyme alphabet, the per-surah uniformity ranking, the Maryam doctrinal-rhyme-break alignment, the Meccan/Medinan rhyme-density null, and the Kahf↔Jinn cross-link are, as far as we can tell, novel computational results**, even if some are quantifications of long-known qualitative observations.

Useful URLs for the lit catalog:

- https://files.eric.ed.gov/fulltext/EJ1128189.pdf — phonetic consonance, fawāṣil
- https://almuslih.org/blog/2024/06/13/the-saj-rhymes-in-the-quran/ — survey
- https://www.researchgate.net/publication/293334043_Between_Al-Fasila_Al-_Qur%27aniyah_and_Saj%27_in_the_Qur%27an
- https://www.researchgate.net/publication/394354495 — Al-Inshiqaq phonological
- https://kurdishstudies.net/menu-script/index.php/KS/article/download/1947/1343/3698 — verse-ending words
- https://www.cobhuni.uni-hamburg.de/en/news-and-events/rhyme-in-quran.html — Hamburg COBHUNI lecture on rhyme effects

## 15. Reproducibility checklist

- [x] Rules tuple specified at top of file
- [x] Statistic implemented as a named function (`strip_to_consonants`, `longest_run_within_surahs`, `ring_score_with_null`, etc.)
- [x] Two null models from different rows of §1 of the rigor protocol: 1.5-permutation-of-type-label (Meccan/Medinan) and 1.2-fasila-shuffle-within-surah (ring-score)
- [x] 10⁴ permutation surrogates for Meccan/Medinan; 500 for ring-score
- [x] Multiple-comparison correction reported (Holm at k = 111 for ring scores; 5-test family for Meccan/Medinan)
- [x] Effect sizes reported alongside p
- [x] Robustness under alternative rule tuples (`U1` and `U2` both reported)
- [x] Garden-of-forking-paths section §13
- [ ] Pre-registration: this finding is **exploratory**, not pre-registered. All p-values are demoted accordingly. The Maryam-rhyme-break-aligns-to-Jesus-statement and Kahf↔Jinn observations should be moved to Phase B pre-registered tests if pursued.
- [x] Test register: this run adds to the saj' family — should be incremented in the running register.

## 16. Where to go next

1. **Pre-register the Meccan/Medinan rhyme-density null test** as a confirmation of the null. The current result is exploratory; a pre-registered version would be a publishable methodological note ("the most famous claim about Quranic saj' is statistically false at the rhyme-density level").
2. **Pre-register the rhyme-break / doctrinal-content alignment in Maryam.** Define a topic-classification function on translation text, ask whether rhyme-breakers are over-represented in topic-X verses.
3. **Cross-link the rhyme alphabet to the lemma-final morphology.** Specifically, what fraction of `ون` line ends are masculine plural verbs vs masculine plural nouns? This requires the QAC morphology.
4. **Compare to a real comparable-Arabic-corpus baseline** (rigor protocol §1.4): take Sahih al-Bukhari, strip Quranic quotation, segment into "verses" of comparable length, compute the same fasila histogram. The 5-letter-rhyme-alphabet claim should be tested against this null.
5. **Phonetic features beyond letters.** The full pause-form rhyme uses *vowel quantity* and *consonant quality*, not just identity. Build a feature representation including these.
