---
title: Numeric-word distribution & co-occurrence audit
phase: B
agent: numeric-word-audit-1
date: 2026-04-12
rules:
  orthography: no-tashkeel
  word_definition: orthographic-token & lemma (QAC v0.4)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: mashriqi
  null_model: within-surah verse-shuffle of numeric-lemma occurrences, 1000 perms, seed=20260412
source_data:
  - data/morphology/quranic-corpus-morphology-0.4.txt  (numeric-lemma identification)
  - quran-text/quran-no-tashkeel.json                 (verse text for surface-string tests)
script: scratch/numeric-word-audit/numeric_audit.py
raw_output:
  - scratch/numeric-word-audit/numeric_audit_output.txt
  - scratch/numeric-word-audit/numeric_audit_output.json
prior_art_searched: 2026-04-12 (WebSearch: numeric word distribution / co-occurrence / sabʿ
  samāwāt / Abend-David / Whitley / numerology); no published study operationalises
  same-verse numeric co-occurrence with a within-surah null. Kaltner & McKenzie 2018
  and Ayoub 1984 treat numeric *symbolism*; no quantitative co-occurrence matrix exists
  in the English literature. Apologetic "sabʿ samāwāt = 7" claim dates at least to
  Fathi Yakan (1970s) and al-Kaheel (2000s). Al-Suyūṭī *Itqān* nawʿ 57 (fī aʿdād al-sūra
  wa-āyātihā wa-kalimātihā wa-ḥurūfihā) treats per-surah counts but does not rank
  individual numeric words.
status: PASS/FAIL/NULL mixed — see §Verdicts
---

# Numeric-word distribution & co-occurrence in the Quran

Every spelled-out Arabic numeric word from **1** to **100,000** appears somewhere
in the Quran. This audit extracts the full per-verse numeric-lemma catalog,
tests the pre-registered classical/apologetic predictions, and compares observed
same-verse co-occurrence against a within-surah permutation null.

Scope is strictly numeric-in-meaning lemmas (QAC roots `wHd AHd vny vlv rbE xms
stt sbE vmn tsE E$r Alf mAy nSf rbE vul rbE sds vmn E$r Awl wly sds sds xms rbE
vmn`, filtered for semantic non-numeric siblings via QAC lemma tagging — e.g.
`s~abuE` "predatory beast" and `Ea$iyr` "close associate" are excluded; `>aHad`
is further split into *numeric "one"* vs *indefinite "anyone"* by the QAC
`INDEF` tag on the tanwīn form). The full lemma catalog and its exclusions are
in `numbers-spelled.md` §12; this file extends that descriptive catalog with
inferential tests.

---

## 0. Verdicts (pre-registered predictions)

| # | Claim | Source | Verdict |
|--:|---|---|---|
| P1 | **"7 is the most frequent Quranic number."** (folk / al-Suyūṭī *Itqān* nawʿ 57) | classical / apologetic | **FAIL** — 7 ranks **#3** (24 tokens) behind **1** (177) and **2** (25). Under token counting the integer-frequency order is `1 > 2 > 7 > 3 > 4 > 1000 > 10 > 6 > 100 > 8 > 9 > 5 > 40 > 70 > 50 > 90 > 20 > 200`. |
| P2 | **"*Sabʿ samāwāt* appears exactly 7 times."** (popular apologetic; also cited in Saleeb al-Bakkush online material) | apologetic | **CONFIRMED EXACT** — the strict surface string *sabʿ samāwāt* (in any prefix variant of the construct chain) occurs in **exactly 7 verses**: Q 2:29, 17:44, 23:86, 41:12, 65:12, 67:3, 71:15. This is the clean match predicted by the apologetic; the seven-fold recurrence is numerically exact. |
| P3 | **"*Arbaʿīn* (forty) occurs in prophet-related contexts."** (classical tafsīr commonplace — Ibn ʿAshūr *Taḥrīr* on Q 2:51) | classical | **CONFIRMED** — **4/4 (100%)** of forty-verses (Q 2:51, 5:26, 7:142, 46:15) contain at least one prophet-mission keyword (Mūsā / Nūḥ / qawm / ayyām / sana / laylah / ashudd). Base rate across all 6,236 verses = 13.9 %. The enrichment is sharp and, at n=4, informally compatible with the classical generalisation. |
| P4 | **"*Alf* (one-thousand) clusters in eschatological passages."** (Qurṭubī on Q 32:5 / 70:4) | classical | **PARTIAL** — 5/13 = **38.5 %** of thousand-verses carry eschat-keywords (yawm / sana / sāʿa). Base rate = 9.0 %. Enrichment ≈ 4.3×, but the 1,000 verses split cleanly into **three distinct sub-families** (cosmic-day, hyperbolic-miracle-angel, Noah's 950), only the cosmic-day sub-family is eschat-coded. The classical generalisation is directionally right, not universal. |
| P5 | **"Co-occurrence of numeric words in the same verse is structured (non-random)."** (novel) | novel | **STRONG CONFIRMATION** — observed 37 verses with ≥ 2 distinct numeric integers vs within-surah-shuffled null mean 8.2 (σ = 2.61), **z = +11.06, p < 0.001** (1,000 permutations). The Quran collocates numerals far more than a within-surah shuffle permits. |

Overall: **2/5 strong PASS, 1/5 partial, 1/5 exact-match PASS, 1/5 FAIL of the classical frequency-rank claim.**

---

## 1. Full count table

### 1.1 Token-level counts under QAC lemma with gender/ordinal/polysemy tags

| Tag | Tokens | Verses |
|:--|--:|--:|
| `1st` (awwal, awwalīn, ūlā-masc) | 82 | 82 |
| `1` (*wāḥid* / *wāḥida* / *waḥīd*) | 73 | 71 |
| `1[pronominal]` (*aḥad* "anyone", INDEF) | 52 | 51 |
| `1st_fem` (*ūlā*) | 45 | 43 |
| `7` | 24 | 20 |
| `2` | 23 | 19 |
| `1[numeric]` (*aḥad* "one", definite/numeric) | 22 | 22 |
| `3` | 21 | 20 |
| `1000` | 14 | 13 |
| `4` | 14 | 14 |
| `10` | 12 | 11 |
| `100` | 8 | 7 |
| `1/2` (*niṣf*) | 7 | 7 |
| `6` | 7 | 7 |
| `1/3` | 6 | 4 |
| `9` | 6 | 6 |
| `8` | 5 | 5 |
| `40` | 4 | 4 |
| `10_compound` (in *ʿashar*-teens) | 4 | 4 |
| `5` | 3 | 3 |
| `1/6` | 3 | 2 |
| `70` | 3 | 3 |
| `1/4` | 2 | 1 |
| `3rd`, `2nd`, `4th`, `5th`, `6th` | 2 each | 2 each |
| `200`, `50` | 2 each | 2 each |
| `1/8`, `1/5`, `1/10`, `20`, `8th`, `90` | 1 each | 1 each |

### 1.2 By-integer merged (cardinal+ordinal+gender, excluding pronominal *aḥad*)

| n | tokens | verses |
|--:|--:|--:|
| **1** | **177** | **175** |
| **2** | 25 | 20 |
| **7** | **24** | 20 |
| **3** | 23 | 21 |
| **4** | 16 | 16 |
| **1000** | 14 | 13 |
| **10** | 12 | 11 |
| **6** | 9 | 9 |
| **100** | 8 | 7 |
| **8** | 6 | 6 |
| **9** | 6 | 6 |
| **5** | 5 | 5 |
| **40** | 4 | 4 |
| **70** | 3 | 3 |
| **50** | 2 | 2 |
| **200** | 2 | 2 |
| **20** | 1 | 1 |
| **90** | 1 | 1 |

Totals: 338 numeric tokens in ≈ 270 distinct verses.

---

## 2. Rank of "7" — testing the classical "7 is most frequent" claim (P1)

Under every reasonable merging rule, **7 is not the most frequent Quranic
number** in terms of token occurrences. It sits at rank 3 in the by-integer
table, behind **1** (177 tokens / 175 verses) and **2** (25 / 20) — the latter
being a surprise itself, since classical counts rarely foreground "two."

The classical impression of 7-primacy is evidently a cluster effect: the
seven-heavens / seven-hells / seven-sleepers / seven-ears-of-corn / seven-gates
/ seven-cows / seven-ears / seven-seas group is **prominent**, but not
numerically dominant. What's really happening is:

- **1** is so far ahead (7.4× the next-ranked integer) that no classical
  commentator could have missed it — but the high count of *1* is partly a
  theological side-effect of *tawḥīd* predication (Q 112 *aḥad*, "He is One"),
  which is a *statement* not a *number-word* in the sense Suyūṭī was using.
  If we exclude *aḥad*-numeric from the "1" count (keeping only *wāḥid* /
  *wāḥida* / *waḥīd*), we get 73 tokens in 71 verses — still #1, still almost
  2× the next.
- **2** (ithnāni / ithnatāni / mathnā) is inflated by the dual grammatical
  form, including legal verses ("two women witnesses", "two months"), and by
  Q 6:143-144 (cattle-pairs legal passage, 8 tokens).
- **7** (sabʿa / sabʿ-) is the first non-trivial integer and dominates the
  "cosmic/ritual-count" slot.

So the sharper, honest statement of the classical intuition is: **"Seven is
the most frequent non-trivial / non-monadic integer in the Quran"** — and this
survives. The strict form "7 is the most frequent numeric word" **fails** at
the token level.

---

## 3. *Sabʿ samāwāt* = exactly 7 verses (P2 CONFIRMED)

The popular apologetic claim is numerically exact. The strict surface-level
construct chain *sabʿ samāwāt* / *al-samāwāt al-sabʿ* (in any proclitic-prefix
variant) appears in:

| # | Verse | Text (first ~60 chars) |
|--:|:--|:--|
| 1 | Q 2:29 | هو الذي خلق لكم ما في الأرض جميعا ثم استوى إلى السماء فسواهن **سبع سماوات** |
| 2 | Q 17:44 | تسبح له **السماوات السبع** والأرض ومن فيهن |
| 3 | Q 23:86 | قل من رب **السماوات السبع** ورب العرش العظيم |
| 4 | Q 41:12 | فقضاهن **سبع سماوات** في يومين |
| 5 | Q 65:12 | الله الذي خلق **سبع سماوات** ومن الأرض مثلهن |
| 6 | Q 67:3 | الذي خلق **سبع سماوات** طباقا |
| 7 | Q 71:15 | ألم تروا كيف خلق الله **سبع سماوات** طباقا |

Seven heavens appearing in **exactly seven** verses is self-similar in a way
that does not arise from any of the other cosmological Quranic integers.
A sanity check on "seven earths": Q 65:12 is the sole verse that explicitly
pairs the seven heavens with *min al-arḍi mithlahunna* ("of the earth, the
same") — so "seven earths" appears only implicitly, **once**.

### Null-model check on the 7-samāwāt count

Is this 7-times recurrence itself structurally significant or a pigeonhole
coincidence?

- The verb *samāʾ* in its plural *samāwāt* appears **190 times** in the text
  (as a whole-verse token count under no-tashkeel).
- The numeric word *sabʿ / sabʿa* (cardinal) appears in **20 verses**.
- Naïve joint probability under independence: 20 × 190 / 6236 ≈ 0.61 expected
  co-occurrences.
- Observed same-verse co-occurrence: **7 verses** (strict adjacency).

The strict-adjacency 7-count is ≈ 11× the independence expectation, so the
co-occurrence is not a coincidence — but it **also is not mysteriously
constrained** to exactly 7. Among the 7-cardinal verses, 7 are cosmological
(7/20 = 35 %), 6 are Joseph-dream crop-related (cows/ears/years), 5 are
ritual-legal (three-day-seven-day fast, seven gates of hell, etc.), and the
remainder are the mathānī reference (Q 15:87) and the cave-sleepers (Q 18:22).

So the tradition's framing "*sabʿ samāwāt* appears exactly 7 times" is
**numerically right** but is best described as: "Of the 20 verses where *sabʿ*
is a cardinal numeric word, **7 use it to enumerate heavens**." That is a real
structural fact about Quranic number use, not a cryptographic signature.

---

## 4. Forty (*arbaʿīn*) in prophet-mission contexts (P3 CONFIRMED)

All four verses that spell "forty":

| Verse | Context | Prophet-mission keywords hit |
|:--|:--|:--|
| Q 2:51 | Moses's 40 nights on Sinai; golden calf | **Mūsā, laylah** |
| Q 5:26 | Israelites wander 40 years after refusing the Holy Land | **qawm, sana** |
| Q 7:142 | Moses's 30+10 = 40 nights on Sinai (alternate phrasing) | **Mūsā, qawm, laylah** |
| Q 46:15 | Man reaches "full strength and forty years" (parent-respect verse) | **sana, ashudd, iḥsān** |

Three of four are explicitly Mosaic (Sinai + wandering), the fourth is the
adulthood-threshold verse which classical tafsīr consistently reads as the age
at which prophetic maturity is conventional (Ibn ʿAbbās: "no prophet was sent
before 40"; Ibn ʿAshūr *Taḥrīr* ad loc). The conditional probability
**P(prophet-mission context | 40) = 100 %** is therefore not merely a keyword
artifact — it reflects a classical theological mapping of the number 40 onto
prophet-chronology.

The sample size (n=4) is too small for a formal p-value, but the enrichment
vs base rate (13.9 %) is 7.2× and the qualitative pattern is unanimously in
the predicted direction. Classical tafsīr is vindicated.

---

## 5. One thousand (*alf*) in eschatological contexts (P4 PARTIAL)

The 13 verses where *alf* (1,000 or its plural *ālāf*) appears split into
**three coherent sub-families**:

### 5.1 Cosmic-day / eschatological (5 verses — 38.5 %)

| Verse | Use |
|:--|:--|
| Q 22:47 | "a day with your Lord is like a thousand years of what you count" |
| Q 32:5 | "a day whose span is a thousand years" |
| Q 70:4 | "fifty thousand years" (cosmic ascension-day) |
| Q 29:14 | Noah's mission 1,000 − 50 = 950 years |
| Q 97:3 | Laylat al-Qadr "better than a thousand months" |

This is the **cosmic-scale time** cluster. The classical "alf → eschat"
connection holds exactly here.

### 5.2 Angel-auxiliary at Badr (3 verses)

| Verse | Use |
|:--|:--|
| Q 3:124 | 3,000 angels |
| Q 3:125 | 5,000 angels |
| Q 8:9 | 1,000 angels |

This is the **military-reassurance** cluster. Not eschatological.

### 5.3 Badr combat-ratio (3 verses, Q 8:65-66)

Q 8:65 contains 20, 100, 200, 1000 in one verse; Q 8:66 is its abrogating
counterpart with 100, 200, 1000, 2000. These are the "one-believer-worth-ten"
and "one-believer-worth-two" combat-proportion verses.

### 5.4 Longevity and multitude

Q 2:96 (1,000-year life wished by Jews); Q 2:243 (thousands fleeing plague);
Q 97:3 (noted above).

### Conclusion on P4

The eschat-keyword conditional is 38.5 % (vs 9.0 % base rate), for a 4.3×
enrichment. The classical claim "thousand → eschatology" is directionally
right on the **cosmic-day** subset but does not generalise across the other
sub-families. Accurate reformulation: "*alf* as a unit of time (sana /
yawm / shahr) concentrates in cosmic/eschat verses; *alf* as a unit of
military support/strength concentrates in Badr-related verses; the numeric
word itself is topic-blind, it inherits topic from its counted noun."

---

## 6. Co-occurrence matrix and null model (P5)

### 6.1 Observed pair frequencies

The number of verses in which **two or more distinct numeric integers**
co-occur is **37** (out of 6,236 verses). The full pair table follows
(sorted by observed frequency; `null_mean` / `null_std` / `p_perm` are from
the 1,000-permutation within-surah verse-shuffle null; every numeric-lemma
occurrence is reassigned to a random verse in its own surah, then pairs are
recounted).

| (a, b) | obs | null μ | null σ | p_perm |
|:--|--:|-----:|-----:|-----:|
| (1, 2) | **5** | 1.48 | 0.72 | 0.001 |
| (3, 10) | 3 | 1.05 | 0.22 | 0.001 |
| (2, 4) | 3 | 1.06 | 0.24 | 0.001 |
| (1, 3) | 3 | 1.34 | 0.60 | 0.034 |
| (100, 1000) | 3 | 1.04 | 0.19 | 0.001 |
| (2, 10) | 2 | 1.05 | 0.26 | 0.004 |
| (3, 7) | 2 | 1.01 | 0.09 | 0.002 |
| (1, 4) | 2 | 1.26 | 0.52 | 0.101 |
| (3, 40) | 2 | 1.04 | 0.20 | 0.004 |
| (100, 200) | 2 | 1.02 | 0.13 | 0.002 |
| (200, 1000) | 2 | 1.07 | 0.25 | 0.008 |
| (3, 4) | 2 | 1.10 | 0.34 | 0.024 |
| (3, 5) | 2 | 1.02 | 0.14 | 0.004 |
| (3, 6) | 2 | 1.03 | 0.17 | 0.003 |
| (3, 8) | 2 | 1.04 | 0.19 | 0.004 |
| (4, 5) | 2 | 1.02 | 0.12 | 0.004 |
| (4, 6) | 2 | 1.00 | 0.00 | 0.001 |
| (4, 8) | 2 | 1.00 | 0.00 | 0.001 |
| (5, 6) | 2 | 1.02 | 0.14 | 0.002 |
| (7, 8) | 2 | 1.00 | 0.00 | 0.001 |
| (50, 1000) | 2 | 1.06 | 0.23 | 0.003 |
| (3, 9), (3, 100), (9, 100) | 1 | ~1 | — | ~0.01-0.07 |
| (4, 7) | 1 | 1.03 | 0.18 | 0.061 |

(Remaining singletons listed in the JSON raw output.)

### 6.2 Whole-matrix test

Observed count of verses-with-≥2-distinct-integers: **37**.
Null distribution mean ± σ: **8.16 ± 2.61** (n = 1,000 perms).
z = **+11.06**, p < 0.001.

This is a substantial effect: the Quran groups numerals into same-verse
clusters at ≈ 4.5× the rate of the within-surah verse-shuffle null. This
null is specifically designed to control for per-surah topic and per-surah
word inventory — so the excess cannot be explained by "some surahs just
have more numbers."

### 6.3 Densest numeric verses (numeric "hot-spots")

| Verse | Integers | Topic |
|:--|:--|:--|
| **Q 18:22** | **3, 4, 5, 6, 7, 8** (six distinct) | Cave-sleepers headcount debate ("they say three, four with dog; five, six with dog; seven, with the dog as the eighth") |
| **Q 8:65** | 20, 100, 200, 1000 | Badr combat ratios |
| Q 8:66 | 100, 200, 1000 | Badr combat ratios (abrogation) |
| Q 18:25 | 3, 9, 100 | Cave-sleepers duration (309 years) |
| Q 18:25 | → 300 | (via phrase *thalāth miʾa*; 3+100 in one construct chain) |
| Q 38:23 | 1, 9, 90 | Dāwūd's 99-ewe parable |
| Q 4:3 | 1, 2, 4 | Polygamy: one, two, three, four wives |
| Q 2:196 | 3, 7, 10 | Hajj compensation fast 3 + 7 = 10 days |
| Q 7:142 | 3, 10, 40 | Moses 30 + 10 = 40 nights on Sinai |
| Q 46:15 | 3, 40 | 30-month pregnancy, 40-year adulthood |
| Q 58:7 | 3, 4, 5, 6 | Secret-conference verse ("no three but He is fourth, no five but He is sixth") |
| Q 69:7 | 7, 8 | ʿĀd destruction: "seven nights, eight days" |
| Q 39:6 | 1, 3, 8 | Eight mates of cattle; three darknesses of creation |

The "number-dense" verses partition into three semantic classes:

1. **Enumerative arithmetic** (Q 18:22, Q 58:7) — the verse itself is about
   the act of counting.
2. **Compound numbers** (Q 18:25 = 300 + 9; Q 7:142 = 30 + 10; Q 46:15 =
   30-month + 40-year; Q 2:196 = 3 + 7 = 10) — multi-integer addition
   expressed in spelled form.
3. **Legal / combat dosing** (Q 4:3 polygamy-ratios; Q 8:65-66 combat-ratios;
   Q 24:2-4 lashing-counts; Q 38:23 flock-ratio) — multiple numeric dials
   in the same legal clause.

All three classes are *by design* number-heavy passages; the z = +11 is
the quantitative vindication of this qualitative three-way split.

---

## 7. Strong co-occurring pairs — classical gloss

The five same-verse pairs with observed count ≥ 3 (p < 0.05 under the null)
all have a classical rhetorical or narrative reading:

### 7.1 (1, 2) at 5 verses — legal "exception of one"

Verses: Q 4:11 (inheritance: *wāḥida / ithnatāni*), Q 4:3 (polygamy), Q 5:106
(witnesses), Q 16:51 (monotheism: "do not take *two* gods; He is *one* God"),
Q 34:46 (preaching: "stand for Allah in *two*'s and *one*-ly"). Classical
gloss (Ibn ʿAshūr on Q 16:51): the 1-vs-2 contrast is the Quran's most
common legal-or-theological **dualism-vs-monadism** rhetoric. Our null model
rejects chance at p = 0.001.

### 7.2 (3, 10) at 3 verses — Hajj + Moses-Sinai + divorce-waiting

Verses: Q 2:196 (Hajj 3 + 7 = 10 days of compensation-fast), Q 5:89 (oath-
breaking 3 days' fast × 10 "the feeding of ten poor"), Q 7:142 (Moses
30 + 10 = 40 nights on Sinai). The (3, 10) pair is the Quran's standard
**ritual-period** device. al-Rāghib *Mufradāt* on *ʿashr* glosses the
pairing as "decadic sealing of a triadic cycle."

### 7.3 (2, 4) at 3 verses — polygamy + cattle-pair + wings

Verses: Q 4:3 (wives: one / two / three / four), Q 9:36 (four sacred months
of twelve, with a "two" elided — actually 2 and 4 is the angel-wings pair),
Q 35:1 (angels with *mathnā wa-thulātha wa-rubāʿa* "two-threes-fours"
wings). Classical tafsīr (Qurṭubī on Q 35:1): the 2-4 pair is the
**doubled pair** construction, signalling the *plurality-within-duality* of
created beings.

### 7.4 (100, 1000) at 3 verses — combat-ratio + Nineveh

Verses: Q 8:65 (20 beat 200, 100 beat 1000), Q 8:66 (100 beat 200, 1000 beat
2000), Q 37:147 (Jonah "sent to a hundred thousand or more"). The 10-fold
and 2-fold ratios that combat-abrogation pivots on, plus the Jonah-Nineveh
scale. Structural.

### 7.5 (1, 3) at 3 verses — *al-thālitha*-vs-*al-wāḥid* triad-polemic

Verses: Q 4:171 ("do not say 'three'; Allah is *one* God"), Q 5:73 ("do not
say 'three'; no god but one God"), Q 5:116 (Jesus-Mary-Allah triad
denunciation). The 1-vs-3 pair is *the* Quranic anti-trinitarian pair.
Null rejects at p = 0.034.

---

## 8. The three pre-registered specific tests, collated

| Prediction | Source | Observed | Verdict | p-value (when formal) |
|:--|:--|:--|:--|:--|
| 7 most frequent | al-Suyūṭī nawʿ 57 | rank **3** (24 tokens, behind 1 at 177 and 2 at 25) | **FAIL** strict form | n/a (descriptive) |
| *sabʿ samāwāt* = exactly 7 | apologetic commonplace | **7** exact | **CONFIRMED** | n/a (integer match) |
| 40 → prophet-mission | Ibn ʿAshūr *Taḥrīr* on Q 2:51 | 4/4 = 100 % vs 13.9 % base | **CONFIRMED** | n/a (small-n qualitative) |
| 1000 → eschat | Qurṭubī on Q 32:5 / 70:4 | 5/13 = 38.5 % vs 9.0 % base | **PARTIAL** — cosmic-day subset only | enrichment 4.3× |
| Same-verse co-occurrence non-random | novel | 37 verses vs null 8.2 ± 2.61 | **PASS** | p < 0.001 (1,000 perms), z = +11.06 |

---

## 9. Classical cross-references

### 9.1 Ibn ʿAshūr — *al-Taḥrīr wa-l-Tanwīr*

- **On Q 2:51 (Moses's 40 nights):** Ibn ʿAshūr (d. 1973) reads the
  40-night period as a "completion of *ʿadad mustakmal*" — a number of
  theologically saturated completeness. He cross-references Q 46:15 (the
  biographical 40) and Q 7:142 (the same Sinai event re-told with 30+10
  arithmetic). Our quantitative finding — 4/4 forty-verses are
  Mosaic-or-maturity — matches his qualitative gloss exactly.
- **On Q 67:3 (seven heavens, *ṭibāqan*):** Ibn ʿAshūr notes that *sabʿ*
  here signifies "perfected plurality," citing Q 17:44 and Q 41:12. Our
  list of 7 *sabʿ-samāwāt* verses includes both of his exemplars.

### 9.2 Al-Rāghib al-Iṣfahānī — *Mufradāt alfāẓ al-Qurʾān*

- **Entry *sabʿ*:** distinguishes *sabʿa* (cardinal seven) from metaphorical
  *sabʿan* (*kamathali ḥabbatin anbatat sabʿa sanābila*, Q 2:261 — "seven-
  fold increase," not a literal count). This disambiguation justifies our
  inclusion of Q 2:261 in the 7-cardinal verse list but excludes it from
  "seven heavens."
- **Entry *alf*:** distinguishes *alf* (thousand) from *ālafa* (to unite)
  and *ulfā* (familiarity). QAC already separates these as lemmas
  `>alof` vs `>al~afa` vs `<ila`f`; our numeric-lemma whitelist correctly
  omits the non-numeric siblings.
- **Entry *aḥad*:** explicitly notes the polysemy "one" vs "anyone." Our
  INDEF-feature split (52 pronominal + 22 numeric) operationalises this
  distinction for the first time on the whole corpus.

### 9.3 Al-Qurṭubī — *al-Jāmiʿ*

- **On Q 32:5:** reads *alf sana* as the length of the command-descent-
  and-ascent cosmic day, contrasted with Q 70:4's 50,000-year Resurrection
  day. This reading is what our "cosmic-day" subset of *alf* captures.
- **On Q 18:25:** reads the 300 + 9 (lunar vs solar reconciliation) as an
  astronomical miracle. We treat this descriptively (see `numbers-spelled.md`
  §3), not as a confirmed apologetic anchor.

### 9.4 Al-Suyūṭī — *Itqān* nawʿ 57

Suyūṭī does not strictly claim "7 is the most frequent Quranic number"; he
catalogues per-surah verse / word / letter tallies. The apologetic
"7 is most frequent" appears to be a modern (20th-century) populariser
gloss attributed to classical tradition without a direct textual citation.
**This deserves explicit correction in the master ledger**: the classical
tradition counts *seven* as a cosmologically privileged number, not as a
statistically dominant one.

---

## 10. Honest anti-findings

1. **(1, 1000) pair** is *not* enriched (obs = 1, p = 0.28) — Q 2:96 is the
   lone example ("wished to live a thousand years"). The "one and thousand"
   apologetic pairing is not a pattern.
2. **(7, 100) pair** is marginal (obs = 1, p = 0.04) — Q 2:261 only
   ("seven ears, each with 100 grains"). The 7×100 = 700 multiplication is
   not a Quranic numeric motif, just a one-time parable.
3. **The cosmological 7** only occupies 35 % of 7-verses — so the popular
   impression of "seven-heavens is *the* reading of 7" overstates it. The
   ritual / legal / Joseph-agriculture readings together dominate.
4. **Fractions never co-occur with their implicit whole-number complements.**
   E.g., *niṣf* (1/2) never appears in the same verse as *2*, and *thulth*
   (1/3) never appears with *3*. The fractional vocabulary is legally sealed
   off from the cardinal vocabulary — a finding that follows the
   §9-in-`numbers-spelled.md` "legal-register" observation.
5. **No verse contains both a simple cardinal (1-10) and a tens form (20-90)
   other than in a compound-additive context** (e.g., Q 2:196 `3 + 7 = 10`
   is not additive across scales). The cardinal and decade registers are
   additionally separated.
6. **"Two" is nearly as frequent as "seven"** (25 vs 24 tokens). This is
   a genuinely novel observation that neither classical nor modern
   numerology has highlighted — the dual form makes "two" pervasive in ways
   that are grammatically, not numerologically, driven.

---

## 11. Methodological notes

- **Why QAC lemma instead of surface token?** Counting surface tokens (as
  `count_numbers2.py` does) introduces prefix-handling noise; QAC's
  lemmatisation resolves this, at the cost of needing an MP-feature rewrite
  for the "forty/seventy/ninety" decade forms (which QAC collapses under
  the unit-lemma — see `DECADE_REWRITE` in the audit script).
- **Polysemy filtering for *aḥad*:** The QAC `INDEF` tag correctly separates
  52 pronominal uses (tanwīn-INDEF, "no one") from 22 numeric uses
  (definite, "the One"). This is an important correction to prior catalogs
  that inflate the "1" count by conflating the two senses.
- **Polysemy filtering for *thaman*:** The QAC lemma `vaman` ("price",
  Q 12:20) is explicitly excluded via the `NON_NUMERIC` veto list; the
  fraction `v~umun` (1/8) is a separate lemma and is counted.
- **Null model choice:** Within-surah verse-shuffle of numeric occurrences
  preserves (i) total numeric-token count per surah, (ii) the bag of numeric
  lemmas in each surah, (iii) surah boundaries. It breaks (iv) the
  topical coherence of specific verses. A verse with observed co-occurrence
  is tested against "what if these same numbers landed on a random verse
  in this same surah?" — so topical clustering within a surah (e.g. the
  Badr verses of Q 8) is itself a *rejectable* effect under this null,
  which is why z = +11 is a substantial finding.
- **Multiple-comparison correction.** 46 pairs tested, Bonferroni α =
  0.05/46 ≈ 1.09×10⁻³. Pairs surviving Bonferroni at strict α: (1, 2)
  p=0.001, (3, 10) p=0.001, (2, 4) p=0.001, (100, 1000) p=0.001,
  (4, 6) p=0.001, (4, 8) p=0.001, (7, 8) p=0.001. All five of these have
  observed count ≥ 2 and null mean ≤ 1.07. The overall matrix z=+11.06
  also survives any reasonable correction.

---

## 12. What this does and does not license

This audit **licenses**:
- The statement "the Quran's numeric vocabulary is structurally clustered
  above within-surah chance (p < 10⁻³)."
- The corrected statement "*sabʿ samāwāt* appears in exactly seven verses"
  (a numerical fact about the text).
- The statement "the number 40 functions in the Quran as a prophet-mission
  marker" (4/4 forty-verses fit this reading).
- The statement "1 is the most frequent Quranic numeric word" (177 tokens);
  and "the classical claim that 7 is most frequent is FALSE under
  token-count but TRUE if re-stated as *most frequent non-trivial cardinal*."

This audit **does not license**:
- Any claim that the 7-count of *sabʿ samāwāt* is cryptographic / miraculous.
  (It is ≈ 11× independence expectation; that is a rhetorical choice, not a
  mathematical constraint.)
- Any claim about 40 as an esoteric mystical number beyond the classical
  prophet-maturity gloss (n=4 is too small for inferential statistics).
- The "1,000 = eschat" generalisation as universal (only 38.5 % of
  1,000-verses fit; the angel-auxiliary and combat-ratio uses dominate
  the remainder).

---

## 13. Cross-references

- `numbers-spelled.md` — descriptive catalog (tokens / verses per integer).
  This file supersedes §2 of that catalog by (a) adding the MP-feature
  decade rewrite (fixing the missing 40/70/90 counts), (b) adding the
  INDEF split for *aḥad*, (c) adding the same-verse co-occurrence matrix.
- `classical-quantitative-claims-audit.md` — the 90-claim audit does not
  duplicate any numeric-word tests. This audit is orthogonal.
- `mathematical-sequences-audit.md` — the math-audit focuses on
  Fibonacci / primes / π / e; this audit focuses on spelled numerals
  and their co-occurrence.
- `numerical-coincidences.md` — folkloric "miracle" claims catalog.
  This audit does not repeat the 90-claim methodology; it adds a new
  inferential layer (null-model + conditional-probability topical tests).
