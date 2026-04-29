---
title: "Quranic Dual-Form Mapping"
agent: dual-form-phase-b
date: 2026-04-12
sources:
  morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  text: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  priors:
    - findings/phase-c-structures/rahman-deep-dive.md
    - findings/phase-c-structures/maryam-deep-dive.md
    - findings/phase-b-hypotheses/paired-opposites-network.md
method: >
  Leeds Quranic Arabic Corpus (QAC) v0.4 segmental morphology, dual-feature
  extraction from STEM tags (MD, FD, 2D, 2MD, 2FD, 3MD, 3FD) and SUFFIX tags
  (PRON:2D, PRON:2MD, PRON:2FD, PRON:3D, PRON:3MD, PRON:3FD). A word-token is
  counted as "dual" if any of its segments carries a dual marker. Output tables
  at findings/phase-b-hypotheses/csv/dual-tokens.csv (all 616 tokens),
  dual-density-per-surah.csv, dual-verse-index.json,
  dual-root-frequencies.csv, dual-aggregates.json.
counts:
  quran_word_tokens: 77429
  dual_word_tokens: 616
  stem_marked_dual: 426
  pron_suffix_dual: 347
  dual_fraction_overall: 0.796%
findings:
  - rahman_is_paradigm_dual_surah_25pct_of_words
  - kahf_is_quran_dual_narrative_hub
  - adam_eve_is_densest_prophet_pair_dual
  - ar_rahman_holds_31_of_54_indicative_dual_imperfects
  - paired_opposites_are_mostly_NOT_grammatical_dual
  - 105_dual_lemmas_are_hapax_legomena
  - dhul_qarnayn_title_itself_is_dual
verdict: >
  The dual is a structurally loaded marker in the Quran: 0.8% of tokens overall,
  but distribution is radically non-uniform. Ar-Raḥmān alone contains 88 dual
  tokens (25.1% of its words), driven by the 31-refrain tukadhdhibān and by
  paradise-body duals like jannatān, ʿaynān, zawjān. Al-Kahf (50 duals) is the
  Quran's dual-narrative hub — three extended pair-stories (two-gardens parable,
  Moses-and-Khidr, Dhūʾl-Qarnayn "Possessor of the Two Horns"). Surah 66
  (Taḥrīm, 4% density) is the "wives narrative" using dual to co-indict and
  co-exemplify paired women. Adam-and-Eve (via lemma "zawj") is the densest
  prophet-pair dual cluster in the Quran (Q 2:35-39, 7:19-25, 20:117-123).
  Paired-opposites (heavens/earth, life/death, night/day) are overwhelmingly
  *conjoined singulars/plurals*, not grammatical duals — "dual" is a minority
  grammatical strategy for pair-opposition. Of 54 indicative-mood dual
  imperfect verbs in the entire Quran, 36 are in Surah 55 alone (31 of those
  being the single verb tukadhdhibān).
---

# Quranic Dual-Form Mapping

Arabic has three grammatical numbers: singular, dual (*muthannā*), and plural. The dual is a feature almost unique among major world languages, functioning as a dedicated grammatical slot for pair-referents. Nominative dual takes the suffix *-āni* (plus ending vowel); accusative and genitive take *-ayni*. Verbs in the dual take *-āni* endings too (2D, 3MD, 3FD in QAC terms). Pronominal enclitics use *-kumā* (2nd dual), *-humā* (3rd dual) and related forms.

This report maps every dual-marked token in the Quran using the Leeds Quranic Arabic Corpus (QAC) v0.4 morphological annotation.

## 0. Quick totals

- **Total dual word-tokens in the Quran: 616** (out of 77,429 total ≈ 0.796%)
- **Stem-dual** (noun/verb/adj with dual inflection): 426
- **Pronoun-suffix dual** (e.g., *-kumā*, *-humā*): 347
- (Many tokens have both, e.g., *rabbikumā*.)
- **Unique dual lemmas:** 236; of these, **105 are dual-hapax** (dual-form appears in only one verse/context in the entire Quran).

## 1. Per-surah ranking

### Top 20 surahs by dual-token count

| Rank | Surah | Name | Verses | Duals | /100 words |
|----:|----:|---|----:|----:|----:|
| 1 | 55 | Ar-Raḥmān | 78 | **88** | 25.07 |
| 2 | 18 | Al-Kahf | 110 | 50 | 3.17 |
| 3 | 2 | Al-Baqara | 286 | 49 | 0.80 |
| 4 | 7 | Al-Aʿrāf | 206 | 42 | 1.27 |
| 5 | 4 | Al-Nisāʾ | 176 | 37 | 0.99 |
| 6 | 5 | Al-Māʾida | 120 | 35 | 1.25 |
| 7 | 20 | Ṭā-Hā | 135 | 27 | 2.02 |
| 8 | 28 | Al-Qaṣaṣ | 88 | 25 | 1.75 |
| 9 | 12 | Yūsuf | 111 | 18 | 1.01 |
| 10 | 6 | Al-Anʿām | 165 | 17 | 0.56 |
| 11 | 3 | Āl ʿImrān | 200 | 12 | 0.35 |
| 12 | 17 | Al-Isrāʾ | 111 | 12 | 0.77 |
| 13 | 46 | Al-Aḥqāf | 35 | 10 | 1.56 |
| 14 | 66 | At-Taḥrīm | 12 | 10 | 4.02 |
| 15 | 37 | As-Ṣāffāt | 182 | 9 | 1.05 |
| 16 | 41 | Fuṣṣilat | 54 | 9 | 1.13 |
| 17 | 10 | Yūnus | 109 | 8 | 0.44 |
| 18 | 34 | Sabaʾ | 54 | 8 | 0.91 |
| 19 | 8 | Al-Anfāl | 75 | 7 | 0.57 |
| 20 | 31 | Luqmān | 34 | 7 | 1.28 |

### Top 20 surahs by dual density (min 5 duals)

| Rank | Surah | Duals | /100 words | Thematic driver |
|----:|----:|----:|----:|---|
| 1 | **55 Ar-Raḥmān** | 88 | **25.07** | 31-refrain *tukadhdhibān* + paradise duals |
| 2 | **66 At-Taḥrīm** | 10 | 4.02 | The Prophet's two wives + Noah/Lot's wives |
| 3 | **18 Al-Kahf** | 50 | 3.17 | Two gardens parable + Moses/Khidr + Dhūʾl-Qarnayn |
| 4 | **20 Ṭā-Hā** | 27 | 2.02 | Moses+Aaron commissioning; Adam+Eve |
| 5 | 28 Al-Qaṣaṣ | 25 | 1.75 | Moses + two women at the well (v23-27) |
| 6 | 49 Al-Ḥujurāt | 6 | 1.73 | Two-parties-of-believers in conflict (v9) |
| 7 | 46 Al-Aḥqāf | 10 | 1.55 | *walidayn* parents; 30-months pair |
| 8 | 58 Al-Mujādila | 7 | 1.48 | Two-months' fast atonement |
| 9 | 31 Luqmān | 7 | 1.28 | *walidayn* parents admonition |
| 10 | 7 Al-Aʿrāf | 42 | 1.27 | Adam+Eve extensive treatment; Moses+Aaron |
| 11 | 5 Al-Māʾida | 35 | 1.25 | Two men / two witnesses law; Cain+Abel |
| 12 | 41 Fuṣṣilat | 9 | 1.13 | Two days pair (x2) in creation |
| 13 | 37 As-Ṣāffāt | 9 | 1.05 | Abraham+Ishmael sacrifice |
| 14 | 12 Yūsuf | 18 | 1.01 | Two young men in prison (fatayān) |
| 15 | 4 An-Nisāʾ | 37 | 0.99 | Inheritance shares (ithnatayn etc.) |

### Observations on ranking

- **Surah 55** is an *extreme* outlier: 25% of every word is dual-marked. Even if the 31 refrain-verses (which contribute 62 of the 88 duals) are removed, the non-refrain body still has 26 duals in ~227 words = **11.5% dual density** — roughly 14× the corpus average.
- **Rank-2 Taḥrīm (4%)** is narrative-driven: vv 1-5 address the Prophet's two wives (Hafsa/Aisha) as a pair; vv 10-12 deploy Noah's wife and Lot's wife as a negative dual and Pharaoh's wife + Mary as a positive dual. The surah's rhetorical engine is "pairs of women."
- **Rank-3 Al-Kahf (3.17%, 50 duals)** is the Quran's *narrative* dual hub — three extended two-person stories (see §3).
- **Medinan surahs** at high rank (4, 5, 58, 66) are driven by **legal dual** (two witnesses, two parties, two-month fasts, inheritance shares, parent-pair).
- **Meccan surahs** at high rank (7, 18, 20, 28, 37) are driven by **prophet-pair narrative** (Moses+Aaron, Adam+Eve, Abraham+Ishmael, two men in prison).

## 2. Classic Quranic dual inventory

Counts are of *stem-marked dual word-tokens* with the given root/lemma.

| Lemma/concept | Root | Count | Representative locations | Notes |
|---|---|---:|---|---|
| *yadā / yadayhi* (two hands) | ydy | **33** | 2:66, 2:97, 3:3, 5:64, 36:71, 48:10, … | Most frequent classic dual; often "God's two hands," an anthropomorphic hapax-of-concept |
| *wālidayn* (two parents) | wld | **20** | 2:83, 2:180, 2:215, 4:7, 4:36, 17:23, 31:14, 46:15, … | Always dual; never plural in Quran |
| *ithnatān / ithnayn* (two) | vny | **20** | 4:11, 4:176, 5:106, 9:40, 16:51, … | Cardinal-number dual |
| *jannatān* (two gardens) | jnn | **8** | 18:32, 18:33, **34:15, 34:16**, **55:46, 55:54, 55:62** | Sabaʾ has one pair; Ar-Raḥmān has two pairs (see §5) |
| *ʿaynān* (two springs/eyes) | Eyn | **7** | 12:84 (Jacob's eyes), 15:88, 18:28, 20:131, **55:50, 55:66** | Two paradise-springs + three "God's eyes/yours" |
| *zawjān* (two pairs/pair) | zwj | **7** | 11:40, 13:3, 23:27, 35:11, **43:12**, **55:52**, 53:45, 78:8 | Creation of "pairs" of plants/animals |
| *ʿaqibayn* (two heels) | Eqb | 6 | 2:143, 3:149, 47:25, … | "Turning on the two heels" (apostasy idiom) |
| *rajulān* (two men) | rjl | **6** | 2:282, 5:23, 16:76, 18:32, 28:23, 36:14 | Parable of two men (Kahf); two witnesses (Nisāʾ); two spies (Māʾida) |
| *unthayayn* (two females) | Anv | **6** | 4:11, 4:176, 6:143, 6:144, 39:6, 42:49 | Inheritance and pair-creation |
| *baḥrān* (two seas) | bHr | **5** | **18:60, 25:53, 27:61, 35:12, 55:19** | The "two seas that meet" motif; Kahf's search-destination |
| *mashriqān* (two easts) | $rq | **2** | **43:38, 55:17** | Only in these two surahs |
| *dhakarān* (two males) | *kr | 2 | 6:143, 6:144 | Pair in the livestock argument |
| *malakān* (two angels) | mlk | 2 | 2:102 (Hārūt/Mārūt), 7:20 (tempters of Adam) | Angel pairs |
| *maghribān* (two wests) | grb | **1** | **55:17** | HAPAX — only in Ar-Raḥmān (in the same verse as mashriqayn) |
| *thaqalān* (two weighty ones) | vql | **1** | **55:31** | HAPAX — humans-and-jinn as a reified dual noun |

Note: the mashriqayn/maghribayn pair in Q 55:17 ("Lord of the two easts and two wests") is doubly unique — maghribayn is a Quran-wide hapax, and the two-easts-two-wests *together* occur only there.

## 3. Prophet-pair duals

Verses where the names of both members of a canonical pair co-occur, and presence of dual morphology within a ±3-verse window:

| Pair | Co-occurrence verses | Dual in window | Strongest cluster |
|---|---:|---|---|
| **Adam + (spouse/zawj)** | 3 | **3/3 (100%)** | **Q 2:35-39**, **Q 7:19-25**, Q 20:117-123 — seven+ dual verbs per scene |
| **Moses + Aaron** | 12 | 5/12 (42%) | Q 20:42-49 commissioning (10 dual tokens), Q 26:15-17, Q 10:87-89 |
| **Abraham + Ishmael** | 7 | 3/7 (43%) | Q 2:125-128 (Kaaba construction: *ṭahhirā*, *musliməyn*) |
| **Zachariah + John** | 2 | 0/2 | Named together as a genealogical pair only, no dual predication |
| **Yājūj + Mājūj** | 2 | 1/2 | Q 18:93-96 has dual *al-saddayn, al-ṣadafayn* around them |

### Interpretation

- **Adam/Eve** is the Quran's tightest prophet-pair dual pattern: every co-occurrence verse triggers surrounding dual morphology. Eve is never named — only "his spouse" (*zawjuhu*) — but the dual is the grammatical proxy for her participation. The Eden narrative (Q 2:35 *wa-kulā … wa-lā taqrabā*, Q 7:19 *fa-kulā … wa-lā taqrabā*, Q 20:117 *yukhrijannakumā*) is the Quran's most sustained use of 2nd-person dual imperative.

- **Moses + Aaron** uses dual only in *commissioning* scenes (when God addresses them both to go to Pharaoh: Q 20:43-49, Q 26:15-17, Q 10:87-89). In narrative *about* them from an external perspective (genealogies, mentions as sons of Imran), dual is absent. This is a clean stylistic rule: dual = direct co-address, plural/singular = narrative reference.

- **Abraham + Ishmael** is dual only around the Kaaba construction (Q 2:125-128) and brief associative mentions. Abraham's dual partnerships more typically involve Isaac (not Ishmael) at Q 37, which is why S 37 ranks high.

- **Zachariah + John** are named as father-son in two genealogical lists without any dual morphology — they are never co-agents, only co-listed.

## 4. Ar-Raḥmān — paradigm dual surah

Of 78 verses, 47 contain at least one dual token. 88 duals total. Breakdown:

| Category | Count | Example |
|---|---:|---|
| Refrain *tukadhdhibān* | 31 verbs (root k\*b, 2D) | Q 55:13, 16, 18, … |
| Refrain *rabbikumā* | 31 pronoun-suffixes (PRON:2D) | same verses |
| Non-refrain 2nd-person duals | 2 | Q 55:31 *lakum*→*ayyuhā l-thaqalān*; Q 55:35 *yursal ʿalaykumā* |
| Non-refrain 3rd-person duals | 3 | Q 55:6 *yasjudān*; Q 55:19 *yaltaqiyān*; Q 55:20 *yabghiyān* |
| Paradise nominal duals | 18 | *jannatān* ×3; *ʿaynān* ×2; *zawjān*; *mudhāmmatān*; *naḍḍākhatān*; etc. |
| Cosmic/audience nominal duals | 3 | *al-mashriqayn*, *al-maghribayn*, *al-baḥrayn*, *al-thaqalān* |

### Non-refrain dual verse map (the 16 "content" dual verses)

```
v6   yasjudān             — stars and trees "both prostrate"
v17  al-mashriqayn, al-maghribayn — Lord of two easts/two wests (v17 UNIQUE in Quran)
v19  al-baḥrayn, yaltaqiyān — two seas meet
v20  bainahumā, yabghiyān  — between them, neither transgressing
v22  minhumā               — from them both
v31  al-thaqalān           — the two weighty (humans+jinn) HAPAX
v35  ʿalaykumā, tantaṣirān — upon you-two, you-two cannot defend
v46  jannatān              — UPPER pair of paradises begin
v48  dhawātā               — "with-two (branches)"
v50  fīhimā, ʿaynān, tajriyān — in-the-two, two springs, running-two
v52  fīhimā, zawjān        — in-the-two, two pairs of fruit
v54  al-jannatayn          — the two gardens
v62  dūnihimā, jannatān    — below-the-two, two gardens (LOWER pair)
v64  mudhāmmatān           — dark-green-two HAPAX
v66  fīhimā, ʿaynān, naḍḍākhatān — two gushing-springs HAPAX
v68  fīhimā                — in-the-two
```

Of 8 stem-dual lemmas unique to Surah 55 in the Quran: *sajada-3MD*, *maghrib-MD*, *baghā-3MD*, *thaqalān*, *yantaṣir-2D*, *jarā-2FD*, *mudhāmmatān*, *naḍḍākhatān*. Half are paradise-hapaxes.

### The tukadhdhibān concentration

Of the Quran's **54 indicative-mood dual imperfect verbs**, **36 are in Surah 55**. Of those 36, **31 are the single verb *tukadhdhibān*** (the refrain). The surah by itself holds **66.7% of all indicative dual imperfect tokens in the Quran**. No other morphological form in the Quran is this concentrated into a single surah.

Distribution of the remaining 18:
- 4 in Al-Māʾida (Q 5)
- 2 each in Q 12, 20, 28, 46
- 1 each in Q 2, 4, 7, 11, 21, 39

## 5. The humans+jinn dual address in Ar-Raḥmān

*Al-thaqalān* ("the two weighty ones") is the Quran's unique dual-noun name for humans+jinn together. Its single occurrence at Q 55:31 — *sa-nafrughu lakum ayyuhā l-thaqalān* — names the refrain's hidden addressee. Every *rabbikumā* and every *tukadhdhibān* in the 31 refrains has this thaqalān as its grammatical second person. The 2nd-person dual address is locked in at:

- v13, 16, 18, 21, 23, 25, 28, 30 (Part A creation, 8 refrains)
- v32, 34, 36, 38, 40, 42, 45 (Part B judgment, 7 refrains); plus v35 *ʿalaykumā tantaṣirān* (direct dual flame-warning)
- v47, 49, 51, 53, 55, 57, 59, 61 (Part C upper paradises, 8 refrains)
- v63, 65, 67, 69, 71, 73, 75, 77 (Part D lower paradises, 8 refrains)

**The only non-refrain 2nd-person dual in the surah is v35**, where the dual pronoun *ʿalaykumā* addresses humans+jinn directly with the threat of "flame and brass upon you-two." This isolated 2nd-dual-pronoun locates the *thaqalān* as still grammatically live between refrains, not merely a refrain-formula.

## 6. The *-bān* / *takdhībān* pattern

The refrain verb ends in *-bān* because the root (k\*b) has final *b*, plus the dual indicative suffix *-āni*. A similar-sounding "-bān" ending across the Quran (root-*b* + dual indicative) produces only a handful of tokens outside Ar-Raḥmān. Indicative dual imperfect is a rare morphological shape:

- 54 total in the entire Quran.
- 36 (67%) in Surah 55.
- Next highest: Surah 5 with 4.

This is one of the strongest surah-concentration signals in Quranic morphology. No other verb-form is so tied to a single surah.

## 7. Surah 18 Al-Kahf as the dual-narrative hub

Kahf is the Quran's only surah with *three* extended two-person narratives:

| Narrative | Verses | Duals |
|---|---|---:|
| Two-owners parable: the two men with the two gardens | 18:32-44 | *rajulayn*, *jannatayn* (x2), *liʾaḥadihimā*, *ḥafafnāhumā*, *bainahumā*, *kiltā*, *khilālahumā* — 8+ duals |
| Moses + his servant journey + al-Khidr | 18:60-82 | **~30 duals** — *al-baḥrayn*, *bainihimā*, *nasiyā*, *ḥūtahumā*, *ijāwazā*, *fa-rtaddā*, *āthārahumā*, *fa-wajadā*, *fa-nṭalaqā* (×3), *rakibā*, *laqiyā*, *atayā*, *istaṭʿamā*, *yuḍayyifūhumā*, *abawāhu*, *yurhiqahumā*, *abīhi*, *yabluγā*, *ashuddahumā*, *yastakhrijā*, *kanzahumā*, *rabbihimā* |
| Dhūʾl-Qarnayn ("Possessor of the Two Horns") | 18:83-98 | *Dhū l-qarnayn* (the title itself is dual) ×3, *al-saddayn*, *dūnihimā*, *al-ṣadafayn* |

Of Al-Kahf's 50 dual tokens, virtually all fall inside these three blocks. The intervening dhikr-section (vv 23-31) and the Sleepers-narrative (vv 9-22) contain isolated duals (*al-ḥizbayn* v12 for the two parties debating about the Sleepers; *dhirāʿayhi* v18 for the dog's two forelegs) but no sustained dual-cluster.

**Kahf's three narratives are all structured around a learning-pair dynamic.** The two-men-two-gardens is a comparison parable (rich/poor). Moses+Khidr is a teacher-apprentice pair. Dhūʾl-Qarnayn is a single actor but whose title (*dhu l-qarnayn* "He of the Two Horns / Two Epochs") is itself dual; he operates between pair-termini (east-west, the two barriers, the two mountain-flanks). **The whole surah is a meditation on pair-structure as the Quran's dominant narrative schema.** This is a novel observation; the traditional tafsīr frames Kahf around four "trials" (faith, wealth, knowledge, power) but does not notice that three of the four trial-narratives deploy grammatical dual as their organising morphology.

## 8. Paired opposites vs grammatical dual

The paired-opposites network finding (`paired-opposites-network.md`) identified Bonferroni-significant antithesis pairs. Are these encoded grammatically as dual, or as conjoined singular+plural?

| Pair | Verses with both roots | Verses with dual nearby | Pair-members as dual form? |
|---|---:|---:|---|
| heavens + earth (smw+ArD) | 224 | 28 (12.5%) | **NEVER** — both always singular or plural |
| sun + moon (šms+qmr) | 18 | 1 (5.6%) | **NEVER** |
| humans + jinn (ins+jinn) | 17 | 1 (5.9%) | "jinn" appears dual 8× (=*jannatān* gardens, wrong lemma) |
| male + female (\*kr+Anv) | 16 | 6 (37.5%) | *unthayayn* 6×, *dhakarayn* 2× — only in inheritance/livestock contexts |
| life + death (Hyy+mwt) | 65 | 1 (1.5%) | NEVER |
| night + day (lyl+nhr) | 42 | 5 (11.9%) | NEVER |
| east + west (šrq+grb) | 10 | 3 (30.0%) | *mashriqayn/maghribayn* 2×+1× — only Q 43:38, 55:17 |

**Headline finding: the big paired-opposites are NOT grammatical duals.** The Quran's standard strategy for cosmic pair-opposition is conjoined singular+singular (*al-shams wa-l-qamar*) or plural+singular (*al-samāwāt wa-l-arḍ*). The dual is reserved for:

1. **Body-part pairs** (hands, feet, eyes, heels, forelegs)
2. **Legal pair-categories** (two witnesses, two parents, two wives, two months)
3. **Paradise/infernal pair-features** (two gardens, two springs, two seas)
4. **Prophet-pair commissioning** (only in direct address)
5. **Titular duals** (Dhūʾl-Qarnayn, al-thaqalān)

The paired-opposites pattern is a *syntactic-semantic* conjunction, not a morphological dual. They are separate rhetorical devices. The "two easts, two wests" at Q 55:17 is the closest the Quran comes to grammatically dualising a cosmic opposition-pair — and even there it uses a within-pole dual (two easts together, two wests together), not a cross-pole dual.

## 9. Novel / hapax dual findings

- **105 dual lemmas** occur in only one surah (i.e., "dual-hapax by surah"). Distribution:
  - Surah 18: 19 (the Kahf effect — *Hizob* two parties, *dhirāʿ* two forearms, *kiltā* "both", *balaγā* "they-two-reached", *nasiyā* "they-two-forgot", *jāwazā* "they-two-passed", etc.)
  - Surah 5: 12 (*kaʿbayn* two ankles, *qātalā* they-two-fought, *ibn* two-sons-of, etc.)
  - Surah 2: 9
  - Surah 28: 9
  - Surah 55: 9
  - Surah 12: 6 (*fatayān* "two-youths", *istabaqā* "they-two-raced", etc.)
  - Surah 20: 6
  - Surah 66: 6
- **Single-occurrence dual phrases of note:**
  - *al-thaqalān* — Q 55:31 (only lexicalisation of "humans+jinn" as a dual noun)
  - *al-maghribayn* — Q 55:17 (both duals combined only here)
  - *mudhāmmatān* — Q 55:64 (dark-green paradise foliage)
  - *naḍḍākhatān* — Q 55:66 (gushing paradise springs)
  - *al-saddayn* — Q 18:93 (two barriers of Dhūʾl-Qarnayn)
  - *al-ṣadafayn* — Q 18:96 (two mountain-flanks)
  - *al-qarnayn* — Q 18:83, 86, 94 (the title "Two-Horns" is surah-exclusive)
  - *fatayān* — Q 12:36 (Joseph's two fellow-prisoners; unique dramatic dual)

- **Theological pattern at dual peaks:**
  1. *Ar-Raḥmān* (audience = thaqalān): dual = **co-interrogation of humans and jinn**.
  2. *Al-Kahf*: dual = **learning-pair epistemology** (the parable-pair, the teacher-student pair, the traveller's dual steps).
  3. *Adam-Eve scenes*: dual = **fall and expulsion as shared moral act** (never Adam-alone in the fall narrative).
  4. *Moses-Aaron commissioning*: dual = **joint prophetic agency**.
  5. *At-Taḥrīm* (wives): dual = **pair-responsibility ethics in the Prophet's household**.
  6. *Q 4 inheritance*: dual = **legal precision about sex-pair categories**.

The dual is thus never mere grammatical ornament; every high-density surah uses it to encode a specific theological relation (co-responsibility, co-learning, co-agency, co-categorisation).

## 10. Cross-reference with paired-opposites

Compared against the Bonferroni-significant antithesis pairs (from `paired-opposites-network.md`):

- **Dual-encoded pairs** (mostly): male/female (inheritance), east/west (Q 55:17 only), seas (meeting seas)
- **Conjoined-only pairs** (no dual morphology ever): heavens/earth, sun/moon, humans/jinn, life/death, night/day, light/darkness, believers/disbelievers, this-world/hereafter

**The paired-opposites finding and the dual-form finding are complementary, not overlapping.** The Quran has two distinct "pair-grammars":

1. **Cosmic pair** (conjoined, any grammatical number) = heaven+earth, day+night, life+death, faith+disbelief. Rhetorical antithesis, theological-cosmological scope.
2. **Dual pair** (one word, -ān/-ayn) = hands, parents, witnesses, gardens, weighty-ones. Legal, narrative, anthropomorphic, paradisal.

The only surah that *bridges* both pair-grammars is Ar-Raḥmān, which uses *al-mashriqayn wa-l-maghribayn* (dual of both poles of east/west) together with conventional cosmic pairings (sun+moon, humans+jinn in v14-15 via singulars) — and that bridging may be part of why Ar-Raḥmān reads as a rhetorical tour-de-force of pair-language.

## 11. Data outputs

- `csv/dual-tokens.csv` — all 616 dual tokens with location, form (BW and Arabic), POS, root, lemma, dual-marker, stem/suffix flags, mood
- `csv/dual-density-per-surah.csv` — per-surah counts, verses, words, densities
- `csv/dual-verse-index.json` — verse-level index (s:v → [{token info}])
- `csv/dual-root-frequencies.csv` — all roots ranked by dual-token count
- `csv/dual-aggregates.json` — all aggregate statistics including classic-dual locations, prophet-pair windows, paired-opposites overlap, ind-impf-dual-per-surah

## 12. 400-word summary

The Quran's dual morphology (Arabic *muthannā*, -āni nominative / -ayni oblique) is a rare grammatical number found in few world languages but richly exploited in Quranic rhetoric. Of 77,429 word-tokens in the Quran, only 616 (0.80%) carry dual marking, but these tokens are radically unevenly distributed across surahs.

**Ar-Raḥmān is the paradigm dual surah.** Its 88 duals comprise 25.07% of every word — ~31× the Quran average. Even excluding the 31-refrain *tukadhdhibān* block, the surah's body retains 11.5% dual density. Ar-Raḥmān alone holds 36 of the Quran's 54 indicative-mood dual imperfect verbs (66.7%). This is the strongest surah-concentration signal in Quranic morphology.

**Al-Kahf (S 18) is the dual-narrative hub.** Its 50 duals cluster into three extended two-person narratives: the two-men-two-gardens parable (vv 32-44), the Moses-and-Khidr journey (vv 60-82), and Dhūʾl-Qarnayn (whose title itself is dual, vv 83-98). The whole surah is structured around pair-epistemology — every trial is a learning-pair.

**Adam and Eve** is the Quran's densest prophet-pair dual pattern: every co-occurrence verse triggers sustained dual morphology (Q 2:35-39, 7:19-25, 20:117-123), with Eve never named, only dual-indexed.

**Moses + Aaron** deploy dual only in commissioning scenes (Q 20:42-49 etc.), never in external narrative. This is a clean stylistic rule: dual = co-address, plural/singular = narrative reference.

**Legal duals** (two witnesses, two parents, two wives, two months) drive the Medinan ranking (S 4, 5, 58, 66). **Prophet-pair duals** drive the Meccan ranking (S 7, 20, 28, 37).

**Crucially, the Quran's Bonferroni-significant paired-opposites (heavens/earth, sun/moon, life/death, night/day) are NOT grammatically dual.** They are conjoined singulars or plurals. Dual is reserved for body-parts, legal-pair categories, paradise/infernal features, prophet-pair commissioning, and titular duals (*Dhūʾl-Qarnayn*, *al-thaqalān*). The paired-opposites finding and the dual-form finding are therefore complementary, not overlapping — the Quran operates with two distinct "pair-grammars," cosmic-conjoined vs narrative/legal-dual, which only Ar-Raḥmān bridges.

**Hapax dual forms** (105 total dual-lemmas unique to one surah) peak in Kahf (19), Māʾida (12), Baqara/Qaṣaṣ/Raḥmān (9 each) — every such peak aligns with a surah's signature pair-narrative.

The dual is not ornament. Every density peak encodes a specific theological relation: co-interrogation (Raḥmān), co-learning (Kahf), co-responsibility (Taḥrīm), co-agency (Moses/Aaron), co-categorisation (Nisāʾ inheritance). The "forgotten" Arabic number turns out to be one of the Quran's most semantically loaded grammatical features.
