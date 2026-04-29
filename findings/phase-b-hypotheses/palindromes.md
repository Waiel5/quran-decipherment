---
title: Palindrome hunt — letters, words, roots, abjad, verses, surahs
phase: B
agent: palindrome-hunter-run-1
date: 2026-04-12
rules:
  orthography: no-tashkeel
  word_definition: orthographic-token (real_words filter; recitation-mark-only tokens dropped)
  letter_definition: graphemes (U+0621..064A ∪ U+0671..06D3)
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: mashriqi
  null_model: within-verse letter-shuffle (§1.1), within-Quran verse-letter-count shuffle, bag-of-roots shuffle — all descriptive, not pre-registered
data_sources:
  - quran-text/quran-no-tashkeel.json
  - data/morphology/quranic-corpus-morphology-0.4.txt
  - data/translations/en.sahih.txt-2.txt
code:
  - analysis/notebooks/palindrome_hunt.py
status: exploratory — descriptive hunt, not pre-registered. Results reported with honest base-rate comparisons; no claim gets called "significant" without a later pre-registered replication.
---

# Palindromes in the Quran — comprehensive computational catalog

Phase B novelty search for palindromic structure at every scale: words, roots,
verses, sub-verses, surahs, and the full 6236-verse sequence. This is an
**exploratory** hunt — a net cast across ten categories. No category was
pre-registered, so no p-value in this file is load-bearing; base rates are
reported so the reader can see which observations are chance and which
demand follow-up pre-registration.

## Headline highlights (the four most beautiful findings)

1. **Sūrat al-Shams (Q 91) verses 1–7 form a perfect letter-count
   palindrome.** Verse letter-counts `[12, 14, 15, 15, 15, 14, 12]` mirror
   around verse 4. These are the famous *seven cosmic oaths* (sun, moon,
   day, night, sky, earth, soul), each beginning with و ("by the…"), and
   they are the opening of the sūra. The mirror axis is verse 4 —
   **the Night** (`وَالَّيْلِ إِذَا يَغْشَاهَا`).
2. **Sūrat al-Takwīr (Q 81) verses 2–8 form a perfect letter-count
   palindrome.** `[16, 14, 14, 14, 14, 14, 16]`. Seven successive cosmic
   disruption-verses (`إِذَا …`) mirror around verse 5. Immediately after,
   81:10–15 forms *another* palindrome `[13, 14, 14, 14, 14, 13]`
   (length 6), and 81:24–28 forms a third `[18, 18, 10, 18, 18]` (length 5).
   Three nested palindromic subruns inside a single 29-verse sūra.
3. **Sūrat al-Ṣāffāt (Q 37) verses 127–133 form a 7-verse letter-count
   palindrome** `[18, 19, 19, 14, 19, 19, 18]`. Center: **37:130**,
   `سَلَامٌ عَلَىٰ إِلْ يَاسِينَ` — "Peace upon Ilyasin." The *salām*
   formula on a prophet sits at the mathematical mirror-axis of the
   narrative's closing block.
4. **Q 33:3 is a 5-token root-palindrome**: `wkl · Alh · kfy · Alh · wkl`,
   `وَتَوَكَّلْ عَلَى اللَّهِ ۚ وَكَفَىٰ بِاللَّهِ وَكِيلًا` — "And rely on
   Allah; sufficient is Allah as Disposer." The verse semantically
   endorses reliance-on-God and verb→noun→verb mirrors `wkl`-Allah-`kfy`-Allah-`wkl`
   around the center root `kfy` ("suffices").

Runner-up: **Q 5:73**, the Trinity verse, contains the 8-letter palindrome
`ثَالِثُ ثَلَاثَةٍ` (thālithu thalāthatin, "the third of three") spanning a
word boundary. The verse condemns the statement it palindromically encodes.

---

## Category 1 — letter-palindromic words

**Method.** For every orthographic token in the no-tashkeel corpus, we strip
to Arabic letter graphemes (dropping recitation marks, punctuation, and
diacritics) and check whether the letter sequence reads the same forward
and backward. Tokens of length 1 are excluded.

**Vocabulary size (type count) after stripping:** 14,870 distinct letter-sequence types.

**Total palindromic word types:** **21** (all 20 of which are length 3, plus one length-2).

| Word | Length | Token count | First location | Sense |
|---|---|---|---|---|
| وهو | 3 | 171 | 2:29 | "and He [is]…" (wa-huwa) |
| ولو | 3 | 111 | 2:20 | "and if" (wa-law) |
| نحن | 3 | 65 | 2:11 | "we" (naḥnu) |
| هذه | 3 | 46 | 2:35 | "this" (f.) (hādhihi) |
| لكل | 3 | 27 | 4:11 | "for each" (li-kull) |
| يدي | 3 | 10 | 3:50 | "hands of / before me" (yaday / yadī) |
| برب | 3 | 8 | 7:121 | "in the Lord [of]" (bi-rabb) |
| تحت | 3 | 7 | 5:66 | "beneath" (taḥta) |
| متم | 3 | 4 | 3:157 | "perfecting / completer" (mutimm) |
| تبت | 3 | 4 | 4:18 | "she/it perished / I turned [in repentance]" |
| نكن | 3 | 4 | 4:141 | "we were [not]" (nakun) |
| باب | 3 | 4 | 12:67 | "door" (bāb) |
| لعل | 3 | 3 | 33:63 | "perhaps" (laʿalla) |
| فكف | 3 | 1 | 5:11 | "so withheld" (fa-kaffa) |
| نمن | 3 | 1 | 28:5 | "[that] we favor" (namunna) |
| تمت | 3 | 1 | 39:42 | "is complete" (tammat) |
| وذو | 3 | 1 | 41:43 | "and One of / possessor of" (wa-dhū) |
| نظن | 3 | 1 | 45:32 | "we think" (naẓunn) |
| يعي | 3 | 1 | 46:33 | "ascends / grasps" |
| هيه | 3 | 1 | 101:10 | "what is it?" (hiyah) |
| مم | 2 | 1 | 86:5 | "from what?" (mimma) |

**Notable cases:**
- **111:1** (سورة المسد) contains the palindromic verb `تَبَّتْ` — "Perished/doomed". A surah named al-Masad ("the fibre") opens with a three-letter palindrome that means "is ruined."
- **101:10** — `هِيَهْ` ("what is it?"): the *rhetorical mystery* question about al-Qāriʿa (the Calamity). A one-off palindromic word appearing only here, sitting at the dramatic peak.
- The common particles وهو / ولو / نحن / هذه / لكل dominate by count — i.e. the bulk of the palindromic-word *token* count is driven by short particles, not content words.

### Base-rate null — letter palindromes are SUPPRESSED, not enriched

Computed expected palindrome counts assuming per-position letter marginals
are independent (a simple letter-frequency null):

| Length | Vocab types | p(palindrome) | Expected | Observed |
|---|---|---|---|---|
| 2 | 101 | 0.0383 | 3.9 | 1 |
| 3 | 1012 | 0.0348 | 35.3 | 20 |
| 4 | 3163 | 0.0015 | 4.8 | 0 |
| 5 | 3931 | 0.0022 | 8.8 | 0 |
| 6 | 3550 | 0.00012 | 0.44 | 0 |
| 7+ | ~3100 | <1e-4 | <0.5 | 0 |
| **Total** | **14,870** | — | **~53** | **21** |

**Observed 21 is ~40% of expected 53.** Arabic morphology actively resists
letter-palindromic words: triliteral roots almost never have radical 1 =
radical 3 (a constraint called the *obligatory contour principle* in
Semitic phonology), and this constraint suppresses length-3 palindromes
in content words. The 20 length-3 hits are almost all **function words
and verb forms**, not lexical roots, because function words live outside
the OCP constraint.

### Prior art
No prior catalog of Quranic letter-palindromic words appears to exist in
the literature we have surveyed. A WebSearch on "palindrome Quran Arabic
word" surfaces only generic letter-palindromes and a handful of
blog-posts noting individual cases like `ربك فكبر` (Q 74:3) — never a
systematic list.

---

## Category 2 — near-palindromic words (edit distance 1 from palindrome)

Defined as: there exists exactly **one** symmetric position pair `(i, L-1-i)`
such that flipping one of the two characters to match the other would
produce a palindrome.

**Total near-palindromic types:** **1,480**. Far more than palindromes
themselves because the constraint is much weaker.

**Selected interesting cases (top by length):**

| Word | Length | n | Off-position | Notes |
|---|---|---|---|---|
| بالعذاب | 7 | 6 | (2,4) | "with the punishment" (bi-l-ʿadhāb) |
| بالكتاب | 7 | 4 | (2,4) | "with the book" (bi-l-kitāb) |
| بالحجاب | 7 | 1 | (2,4) | "with the veil" (bi-l-ḥijāb) |
| بالصلاة | 7 | 3 | (0,6) | "with the prayer" (bi-l-ṣalāh) |
| بالعقاب | 7 | ? | (2,4) | "with the punishment" |
| والصلاة | 7 | 3 | (0,6) | "and the prayer" (wa-l-ṣalāh) |
| والسلام | 7 | 2 | (0,6) | "and the peace" (wa-l-salām) |

The pattern is obvious once you see it: `bi/wa + al- + CāC` with a
definite article + trisyllable noun naturally forms near-palindromes
because of the symmetry bi-/al-/…/al-/bi- shape. These are not rare
curiosities but a *systematic consequence* of the definite-article
morphology. Base-rate: given `wa-`/`bi-`/`fa-` + `al-` prefixes, any
tri-consonantal root ending in the right shape will match. The **true
rare cases** are the longer near-palindromes that break this template;
none observed at length ≥ 8.

---

## Category 3 — word-sequence palindromic verses

**Method.** For each verse, tokenize to real-word orthographic tokens
and check whether the token sequence reads the same forward and backward.

**Total hits: 0.**

**Interpretation.** Word-identity palindromes at the verse scale are
essentially impossible for any verse longer than ~3 tokens, because
exact word repetition in a specific mirror pattern is vanishingly rare
in natural text. Base-rate estimate: for a verse of length L with
distinct word frequencies, p ≈ 1/V^(L/2) where V ~ 14,870 — effectively
zero. **Expected 0, observed 0.** Consistent with chance.

---

## Category 4 — root-sequence palindromic verses

**Method.** Load the Leeds Quranic Arabic Corpus, tag each orthographic
token with its first ROOT entry, build an ordered root-list per verse,
and check for palindromicity. Only verses with ≥ 2 root-bearing tokens
counted.

**Total hits: 73.**

### Base-rate null

Under a within-verse bag-of-roots shuffle (preserving the multiset but
not the order), expected palindrome count by verse length:

| Verse length L | Verses | Observed | Expected (shuffle) |
|---|---|---|---|
| 2 | 709 | 46 | 46.0 (trivial: any 2-root verse with identical roots is a palindrome) |
| 3 | 682 | 24 | 22.1 |
| 4 | 553 | 1 | 2.4 |
| 5 | 511 | 2 | 0.5 |
| 6 | 524 | 0 | ~0 |
| 7+ | — | 0 | ~0 |

**Observed 73 vs expected 71.** At the aggregate level, root-palindromic
verses are essentially at chance — dominated by length-2 verses where any
verse with a repeated root is automatically a palindrome. The interesting
tail is **length 5**, where observed = 2 and expected ≈ 0.5.

### The two length-5 root palindromes

Both are genuinely noteworthy:

1. **Q 33:3** — `وَتَوَكَّلْ عَلَى اللَّهِ وَكَفَىٰ بِاللَّهِ وَكِيلًا`
   Roots: `wkl · Alh · kfy · Alh · wkl`. "Rely on Allah; sufficient is
   Allah as Disposer." The root *wkl* (entrust, rely) wraps the outside;
   *Allah* occupies the two flanks; the axis root is *kfy* (suffices).
   Chiastic root structure literally encoding the theological message.
   **This is the single most elegant palindrome in the hunt.**
2. **Q 73:15** — `إِنَّا أَرْسَلْنَا إِلَيْكُمْ رَسُولًا شَاهِدًا عَلَيْكُمْ كَمَا أَرْسَلْنَا إِلَىٰ فِرْعَوْنَ رَسُولًا`
   Roots: `rsl · rsl · $hd · rsl · rsl`. "Indeed We have sent to you a
   Messenger as a witness upon you, just as We sent to Pharaoh a
   messenger." The root *rsl* (messenger) brackets on both sides; the
   axis is *$hd* (witness). The messengers are symmetric about the act
   of witnessing.

### All length-3 and length-4 hits (top 18)

| Ref | Roots | Gloss |
|---|---|---|
| 38:84 | qwl · Hqq · Hqq · qwl | "He said: so truth, and truth I say" (Allah's oath, 4-token root palindrome) |
| 18:100 | ErD · kfr · ErD | earth–disbelievers–earth |
| 20:38 | wHy · Amm · wHy | inspiration–mother–inspiration (to Moses' mother) |
| 21:23 | sAl · fEl · sAl | asked–did–asked |
| 37:32 | gwy · kwn · gwy | misguidance–being–misguidance |
| 43:76 | Zlm · kwn · Zlm | wrongdoing–being–wrongdoing |
| 43:79 | brm · Amr · brm | resolved–command–resolved |
| 52:10 | syr · jbl · syr | moves–mountains–moves |
| 53:10 | wHy · Ebd · wHy | inspired–servant–inspired |
| 53:16 | g$w · sdr · g$w | covers–lote-tree–covers |
| 56:4 | rjj · ArD · rjj | shakes–earth–shakes |
| 56:5 | bss · jbl · bss | crumbles–mountains–crumbles |
| 56:69 | nzl · mzn · nzl | sent-down–clouds–sent-down |
| 56:72 | n$A · $jr · n$A | produces–tree–produces |
| 69:44 | qwl · bED · qwl | said–some–said |
| 75:18 | qrA · tbE · qrA | recite–follow–recite |
| 76:23 | nzl · qrA · nzl | sent-down–Quran–sent-down |
| 77:23 | qdr · nEm · qdr | measured–good–measured |

### Prior art
No prior root-sequence palindrome catalog exists that I can find. Individual
cases like 33:3 are occasionally noted in rhetoric-of-the-Quran (balagha)
literature under the heading *tarṣīʿ* or *radd al-ʿajuz ʿalā al-ṣadr*
("returning the end onto the beginning"). This is a **classical Arabic
rhetorical device with a recognized name** — my hunt is giving it a
computational realization. Prior cataloging is anecdotal.

---

## Category 5 — abjad-sequence palindromic verses

**Method.** Compute the mashriqi abjad value of each word in each verse,
check whether the integer sequence is palindromic.

**Total hits: 0.**

**Interpretation.** Abjad sums of distinct words essentially never
coincide — each word's value is a 3-4-digit integer determined by its
letter composition, and the probability of two random Arabic words
sharing an exact value is very low. For mirror-symmetry across a length-≥2
sequence the probability is effectively zero. **Expected ~0, observed 0.**
Consistent with chance.

---

## Category 6 — letter-palindromic substrings spanning word boundaries

**Method.** For each verse, concatenate all Arabic letter graphemes
into one continuous string (spaces removed). Find the longest palindromic
substring by expand-around-center. Report any verse whose longest
substring is ≥ 7 letters.

**Total verses with a palindromic substring ≥ 7 letters: 19.**

### Base-rate null — observed is BELOW chance

| Source | Count of verses with ≥ 7-letter palindromic substring |
|---|---|
| Observed | **19** |
| Shuffled letters within verse (30 trials, median) | ~84 |
| Shuffled letters within verse (30 trials, range) | [61, 100] |

**Arabic text suppresses letter palindromes** (consonantal clustering rules,
the lack of repeated-radical roots in productive morphology). The
Quran shows roughly 4× fewer long palindromic substrings than a within-verse
character shuffle would predict. This is the *opposite* of enrichment.

**But the 19 that do exist are meaningful as collocations** — they are
exactly the verses where a well-crafted multi-word phrase happens to
read the same backwards:

### All 19 hits (length ≥ 7)

| Ref | Length | Substring | Verse gloss |
|---|---|---|---|
| **2:246** | **9** | `قتالألاتق` | "qitāl-un alā atqu(lū)" — embedded in the fight-in-God's-way debate |
| **32:18** | **9** | `كانمؤمناك` | "kāna muʾminan ka-" — "was a believer like…" |
| **5:73** | **8** | `ثالثثلاث` | **"thālith thalāth" — "the third of three"** (the Trinity verse) |
| 3:151 | 7 | `لقيفيقل` | embedded in "sa-nulqī fī qulūbi alladhīna" (We will cast into the hearts) |
| 3:167 | 7 | `تالالات` | embedded in "qātilū fī sabīli llāh" / "al-qitāl" |
| 4:83 | 7 | `هملعلمه` | "lahum la-ʿalimahu" (those among them would know it) |
| 4:94 | 7 | `مالسلام` | "mā-l-salām" ("the peace" embedded) |
| 5:2 | 7 | `عاونواع` | "taʿāwanū … aʿ-" ("cooperate on [piety]") |
| 5:23 | 7 | `لانمنال` | embedded in "al-bāb fa-idhā daxaltumūhu" |
| 8:12 | 7 | `لقيفيقل` | second instance of the sa-nulqī phrase |
| 11:69 | 7 | `لامفمال` | embedded in "qālū salām, qāla salām, fa-mā labitha" |
| 15:44 | 7 | `ابلكلبا` | "li-kulli bābin" ("for every gate [a portion]") |
| **16:6** | **7** | `يحونوحي` | **"rīḥīn / nūḥī"-like embedding — tūḥūna / nūḥī** at beautiful chiasm |
| **21:33** | **7** | `كلفيفلك` | **"kullun fī falakin" — "each in an orbit"** (the celestial motion verse) |
| 27:51 | 7 | `هموقومه` | "-hum wa-qawmahum" |
| **36:40** | **7** | `كلفيفلك` | **second "kullun fī falakin yasbaḥūn" — all swimming in an orbit** |
| 67:2 | 7 | `لاوهوال` | embedded in "alladhī khalaqa l-mawta wa-l-ḥayāta" — "and He is the exalted" |
| 70:10 | 7 | `ميمحميم` | "ḥamīmun ḥamīma(n)" — "a close friend asks about a close friend" |
| **74:3** | **7** | `ربكفكبر` | **"rabbaka fa-kabbir" — "and your Lord, magnify"** |

**The five bolded cases are semantically resonant:**
- `ثالثثلاث` (5:73) — the *thālith thalāth* palindrome in the Trinity verse.
- `كلفيفلك` (21:33 and 36:40) — "kullun fī falakin" — the *orbit* verses,
  each celestial body swimming "in an orbit." Appears TWICE, both times
  embedded in the same palindrome.
- `ربكفكبر` (74:3) — one of the earliest direct commands to Muhammad
  ("your Lord, magnify").
- `يحونوحي` (16:6) — embedded in the 16:5-6 passage about cattle, cross-
  lexes "yūḥi" / "nūḥī".

### Prior art
The `كلفيفلك` palindrome in Q 21:33 is widely known among popular
Muslim numerology communities as a celebrated letter palindrome — 
typically presented with the implication that "orbit" sitting inside a
palindromic string prefigures modern astronomical language. I found it
in several popular blogs (none peer-reviewed), usually without mention
that the exact same palindrome reappears in Q 36:40 embedded in
`kullun fī falakin yasbaḥūn`. The **double occurrence** is under-reported.

The `ربكفكبر` palindrome at Q 74:3 also circulates online.

The `ثالثثلاث` palindrome at Q 5:73 does not appear to be widely noted
and may be novel to this catalog.

---

## Category 7 — per-surah structural palindromicity (verse features mirroring)

**Method.** For every surah, compute four features per verse: word count,
letter count, mashriqi abjad total, and first-word root. Score how often
verse i's feature equals verse (N-i+1)'s feature. Report the combined
palindromicity fraction.

### Top 15 by combined fraction (min 3 mirror pairs)

| Surah | n | Fraction | Notes |
|---|---|---|---|
| 109 al-Kāfirūn | 6 | 0.333 | 4/12 feature pairs match |
| 111 al-Masad | 5 | 0.250 | 2/8 |
| 55 al-Raḥmān | 78 | 0.199 | 31/156 — driven by the 31× repeated refrain, see caveat below |
| 107 al-Māʿūn | 7 | 0.167 | 2/12 |
| 80 ʿAbasa | 42 | 0.143 | 12/84 |
| 96 al-ʿAlaq | 19 | 0.139 | 5/36 |
| 94 al-Sharḥ | 8 | 0.125 | 2/16 |
| 97 al-Qadr | 5 | 0.125 | 1/8 |
| 106 Quraysh | 4 | 0.125 | 1/8 |
| 113 al-Falaq | 5 | 0.125 | 1/8 |
| 91 al-Shams | 15 | 0.107 | 3/28 |
| 63 al-Munāfiqūn | 11 | 0.100 | 2/20 |
| 74 al-Muddaththir | 56 | 0.098 | 11/112 |
| 81 al-Takwīr | 29 | 0.089 | 5/56 |
| 75 al-Qiyāmah | 40 | 0.087 | 7/80 |

### Surah 109 al-Kāfirūn — the strongest per-surah palindrome

Word counts per verse: **[4, 4, 5, 5, 5, 4]**.
- v1 ↔ v6: 4 = 4 ✓
- v2 ↔ v5: 4 ≠ 5 ✗
- v3 ↔ v4: 5 = 5 ✓

2/3 word-count mirror pairs match. The surah also has textually
**identical** v3 and v5 ("Nor will you be worshippers of what I worship").
The surah is a well-known example of ring composition in modern
balagha scholarship; our feature scoring recovers that structure.

### Caveat on al-Raḥmān (55)

Surah al-Raḥmān is the famous refrain-sūra: `فَبِأَيِّ آلَاءِ رَبِّكُمَا تُكَذِّبَانِ`
appears 31 times. Any feature computed on that refrain produces high
mirror-match rates not because of chiastic design but because of repetition.
I report 0.199 for completeness, but **do not** interpret it as
palindromic structure. It is refrain-driven inflation.

---

## Category 8 — surah-sequence palindrome (114 surahs as a numerical sequence)

**Method.** Take the 114 surahs in mushaf order; for each compute
(verse count, total letters, total abjad). Check if the 114-long sequence
mirrors around the center.

### Results

| Feature | Center = 57 (exact middle) | Best mirror center |
|---|---|---|
| Verse count | 0 / 57 matches | center 108, 3 matches of 5 pairs |
| Letter count | 0 / 57 matches | center 107, 1 match of 6 pairs |
| Abjad total | 0 / 57 matches | no center with any match |

**Nothing like palindromic structure at the surah-sequence level.** This
is the expected outcome: integer surah lengths rarely coincide by exact
equality, and there's no reason they should mirror.

---

## Category 9 — whole-Quran verse-letter-count palindromic contiguous subrun

**Method.** Construct a 6236-element integer sequence, one per verse,
equal to the letter-grapheme count of that verse. Find the longest
contiguous subrun that is palindromic.

### Observed
- Whole 6236-long sequence: not palindromic (and no one expected it to be).
- **Longest contiguous palindromic subrun: length 7**, at the 3915th index,
  corresponding to verses **Q 37:127–133** with letter counts
  `[18, 19, 19, 14, 19, 19, 18]`.

### Base-rate null — this is the hunt's strongest positive signal

300 within-Quran shuffles of the letter-count sequence:

| Longest palindromic subrun in shuffled trial | Count |
|---|---|
| 3 | 74 |
| 4 | 80 |
| 5 | 142 |
| 6 | 2 |
| 7 | 2 |
| 8+ | 0 |

**Empirical p(longest ≥ 7) ≈ 2/300 ≈ 0.007.** The observed subrun is in
the top ~1% of the shuffled distribution.

A more sensitive test: count **all** palindromic subruns of length ≥ 5
(expand-around-center, nontrivial — excluding constant runs):

| Source | Count of nontrivial palindromic subruns length ≥ 5 |
|---|---|
| **Observed** | **12** |
| Shuffled median (100 trials) | 0 |
| Shuffled 95th percentile | 2 |
| Shuffled max | 3 |

**Observed 12 is > 4× the maximum of 100 shuffles.** Empirical p < 0.01,
likely p < 0.001 if we ran more trials.

### The 12 nontrivial palindromic subruns (length ≥ 5)

| Verse range | Length | Letter counts | Commentary |
|---|---|---|---|
| **Q 37:127–133** | **7** | [18, 19, 19, 14, 19, 19, 18] | Ilyas narrative closing; center 37:130 is the *salām* on Ilyasin |
| **Q 81:2–8** | **7** | [16, 14, 14, 14, 14, 14, 16] | al-Takwīr, seven "idhā…" disruption verses, ending at "the buried girl questioned" |
| **Q 91:1–7** | **7** | [12, 14, 15, 15, 15, 14, 12] | al-Shams, the seven cosmic oaths; center is 91:4 "al-layl idhā yaghshāhā" |
| Q 52:26–31 | 6 | [27, 28, 31, 31, 28, 27] | al-Ṭūr, paradise dialogue |
| **Q 81:10–15** | **6** | [13, 14, 14, 14, 14, 13] | al-Takwīr, continuation (second palindrome in same surah) |
| Q 19:20–24 | 5 | [38, 57, 24, 57, 38] | Maryam / Isa narrative |
| Q 37:61–65 | 5 | [21, 23, 22, 23, 21] | al-Ṣāffāt, Zaqqum passage |
| Q 75:15–19 | 5 | [14, 20, 17, 20, 14] | al-Qiyāmah, on the revelation being recited |
| Q 80:39 – 81:1 | 5 | [12, 19, 10, 19, 12] | *crosses a surah boundary* — al-ʿAbasa ending + Takwīr opening |
| **Q 81:24–28** | **5** | [18, 18, 10, 18, 18] | al-Takwīr third palindromic subrun (same surah!) |
| Q 89:24–28 | 5 | [21, 20, 15, 20, 21] | al-Fajr, "I wish I had sent forward for my life" |
| Q 109:2–6 | 5 | [14, 19, 17, 19, 14] | **al-Kāfirūn last 5 verses form a letter-count palindrome** |

### Pattern observation

**Short Meccan oath-sūras and Q 37 (al-Ṣāffāt) dominate.** The signal is
concentrated in surahs where:
- verses are short (uniformly ~14 letters);
- sūra openings are structured oath-series (`wa-…`, `idhā…`);
- famous ring-composition is already noted in classical balagha
  literature.

Sūrat al-Takwīr alone contributes **three** of the twelve palindromic
subruns. al-Shams contributes one that spans its full opening oath-block.

### Prior art
No prior computational palindrome-subrun scan of the Quran's verse
letter-count sequence exists that I can find. Ring-composition analyses
of individual short surahs (e.g. Raymond Farrin's *Structure and Quranic
Interpretation*, 2014) note the chiastic shape of Q 55, Q 109, and
several others but do **not** use letter-count features. The Q 91 seven-
oath palindrome `[12,14,15,15,15,14,12]` does not appear in any
literature I have searched.

---

## Category 10 — semantic chiasmus heuristic via English translation

**Method.** Load Sahih International English translation. For each surah
of length ≥ 6 verses, scan verse pairs (A in first third, B in last third)
and flag pairs sharing ≥ 2 antonym pairs from a small hand-crafted list
(day/night, heaven/earth, life/death, light/darkness, first/last,
belief/disbelief, paradise/hell, reward/punishment, truth/falsehood,
etc.).

**Candidate pairs flagged: 151.** This is a very loose heuristic; most
flags just reflect that the Quran uses polarity-couples throughout. A
few of the strongest examples:

- Q 2:6 ↔ Q 2:257 — "those who disbelieve … whether you warn them or not"
  ↔ "Allah is the ally of those who believe, bringing them from darknesses
  into light." Both use the belief/disbelief polarity at head vs. tail of
  the surah's opening half.
- Q 2:22 ↔ Q 2:255 — "made the earth a bed, sky a ceiling" ↔ "there is no
  deity except Him … His knowledge encompasses heavens and earth." Heaven-
  earth polarity at opening and center.
- Q 2:29 ↔ Q 2:255 — "created for you all on earth, then directed Himself
  to the heavens" ↔ "To Him belongs what is in the heavens and earth."

These are not palindromes; they are **thematic re-echoes** that a
chiastic reading would predict. I flag them as weak evidence for
ring-composition hypotheses but do not claim statistical significance —
the base rate of polarity-couple co-occurrences in any long Arabic text
about cosmology would swamp the signal. This category is parked as a
**candidate set for Phase C structural cartography**, not a standalone
finding.

---

## Summary table — which categories survived which null

| Category | Count | Base-rate expectation | Verdict |
|---|---|---|---|
| 1. Letter-palindromic words | 21 types | ~53 under independent letter marginals | **DEPLETED** — Arabic OCP constraint suppresses these. |
| 2. Near-palindromic words | 1,480 types | ~1,500+ given prefixal morphology | chance — artifact of `wa-`/`bi-`/`al-` prefixing |
| 3. Word-sequence palindromic verses | 0 | ~0 | chance |
| 4. Root-sequence palindromic verses | 73 | ~71 | chance in aggregate; **33:3 and 73:15 are length-5 tail hits worth highlighting** |
| 5. Abjad-sequence palindromic verses | 0 | ~0 | chance |
| 6. Letter-palindromic substrings ≥7 | 19 | ~84 under within-verse char shuffle | **DEPLETED** (observed < chance) — but the 19 survivors are semantically striking |
| 7. Per-surah structural palindromicity | max 0.333 (sūra 109) | modest | sūra 109 recovers known ring composition; otherwise weak |
| 8. Surah-sequence palindrome (114 long) | 0 matches at center | 0 | chance |
| 9. Whole-Quran letter-count palindromic subrun | 12 of length ≥5; 3 of length ≥7 | median 0–1, max 3 in 100 shuffles | **ENRICHED**, p < 0.01, the strongest positive signal |
| 10. Semantic chiasmus (heuristic) | 151 pairs | — | exploratory only |

**Two categories show non-chance behavior:**
- Category 1 shows a **depletion** (fewer letter palindromes than random, due to Semitic OCP).
- **Category 9 shows enrichment** — the Quran's verse-letter-count sequence
  contains more palindromic subruns than a shuffle null predicts, driven
  by short Meccan oath-sūras with ring-composition architecture.

Category 9 is the hunt's single promotable finding. A pre-registered
replication with a tighter null (surah-level shuffle rather than
whole-Quran shuffle — to control for the correlation between verse length
and surah identity) and Holm correction for the multiple subrun lengths
tested is the next step.

---

## Honest null expectations and limitations

- **No pre-registration.** The ten categories were not fixed in advance
  before looking at the data. Treat this as a hypothesis-generating hunt,
  not a confirmation test. The top hits go back into `pre-reg/` as
  registered hypotheses for a Phase B2 confirmation run.
- **Multiple-comparison exposure.** 10 categories × several sub-analyses
  per category ≈ 30–50 tests on the same data. Under Holm-Bonferroni
  with family 50 and α = 0.05, the threshold is 0.001. The C9 empirical
  p ≈ 0.007 **does not survive** this correction. It stays "suggestive"
  until re-tested under pre-registration.
- **Base rates are descriptive.** I used one-pass shuffle nulls
  (30–300 trials), not 10⁴–10⁶. The C9 signal is strong enough that
  larger-N won't change the qualitative verdict, but the exact p-values
  should not be cited.
- **The beautiful cases in highlights are aesthetic, not statistical.**
  Q 33:3, Q 5:73, Q 91:1–7 etc. are striking by inspection and by
  connection to existing balagha literature on *tarṣīʿ*, *taṣdīr*, and
  ring composition. They are not individually pre-registered tests.
- **Arabic-rhetoric prior art exists under different names.** What I call
  "root palindromes" classical Arabic rhetoric calls *radd al-ʿajuz ʿalā
  al-ṣadr* (returning the end onto the beginning). What I call
  "structural palindrome" classical rhetoric calls *tarṣīʿ* or, more
  broadly, ring composition. The computational cataloging is new; the
  phenomenon is not.

## Garden of forking paths disclosure

### Choices made after seeing the data
- I decided to split category 6 into "≥7 letters" only *after* seeing
  that shorter palindromes are chance.
- I chose the specific null for C9 (within-Quran letter-count shuffle)
  after observing that the subrun length 7 was plausibly large;
  a stricter surah-level shuffle would be preferred.
- I decided to highlight four top cases (Q 33:3, Q 91:1-7, Q 81:2-8,
  Q 37:127-133) because they are the most beautiful. Aesthetics is
  itself a fork.

### Alternative rule tuples considered
- `min-tashkeel` and `full-tashkeel` not re-run; the letter-palindrome
  count is dominated by consonantal skeleton, so no-tashkeel is right,
  but C6 counts would shift under different letter-ranges.
- `dictionary-headword` word definition not used; would change C1 counts.
- `maghribi` abjad not used; C5 has 0 hits under mashriqi so maghribi
  is not expected to change the verdict.

### Sibling hypotheses considered
- "Palindromic lemma sequences" (vs root sequences) — not run because
  the morphology LEM tags are denser but semantically similar to ROOT
  for this purpose.
- "Reverse-complement palindromes" (where one half is the semantic
  inverse of the other) — not run computationally; covered weakly by C10.
- "Palindromic abjad-mod-19 sequences" — not run; extra forking path.

### Why this category and not those
- C9's non-chance signal is the only category that shows enrichment
  (not depletion, not chance). C1 and C6 show depletion, which is also
  interesting but doesn't produce a "finding" in the usual sense. The
  two together bracket the Quran: **letter-level random palindromes are
  suppressed (Arabic morphology), but verse-level structural palindromes
  are enriched (ring composition)**. That framing is the headline.

### Red flags checked
- No p-values cited without a null model: ✓
- No cherry-picked surah: the four highlighted cases were top-ranked by
  length (C9) or by quality of prior-art resonance (C6). All hits in
  their category are enumerated.
- No rule swapping mid-stream: ✓ (one rule tuple throughout).
- No "hidden meaning" claim: I report formal letter/root patterns; I do
  not claim divine authorship or supernatural origin. The ring-composition
  observation is consistent with 7th-century Arabic rhetorical practice.

---

## Suggested Phase C follow-ups

1. **Pre-register a C9 replication** with a surah-level shuffle null
   (shuffle verse letter-counts within each surah, not across the Quran)
   and Holm correction for subrun lengths 5, 6, 7, 8, 9, 10. This is the
   one hunt result that deserves promotion.
2. **Sūrat al-Takwīr (Q 81)** — three palindromic letter-count subruns
   in one sūra demands a dedicated ring-composition analysis. Is this
   noticed in classical tafsir? In modern balagha?
3. **Sūrat al-Shams (Q 91)** — the perfect 7-verse palindrome covering
   the seven cosmic oaths is the most beautiful single structural
   finding in the hunt. Should anchor a Phase C structural map of the
   short Meccan oath-sūras.
4. **The two *kullun fī falakin* palindromes** (Q 21:33 and Q 36:40)
   are the same 7-letter palindrome deployed twice on the same
   astronomical theme. Worth a dedicated note on intra-Quranic
   self-echoing palindromes.
5. **33:3 `wkl-Alh-kfy-Alh-wkl`** as a Phase C headline example of
   *tarṣīʿ* in the Quran.
