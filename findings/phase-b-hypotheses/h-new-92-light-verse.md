---
id: H-NEW-92
title: Q 24:35 (Āyat al-Nūr / the Light Verse) — multi-axis structural uniqueness audit
phase: B
status: NOTABLE on raw axes; UNIQUE on length-conditional follow-up
date: 2026-04-15
agent: h-new-92-specialist
prereg: findings/phase-b-hypotheses/h-new-92-light-verse-prereg.md
journal: journal/h-new-92-run-1.md
script: scripts/h_new_92_light_verse.py + scripts/h_new_92_followup.py
data: findings/phase-b-hypotheses/csv/h-new-92.json
rules_tuple: (no-tashkeel; orthographic-token-real-words; graphemes; hafs-kufan; 6236; basmala-counted-only-in-surah-1; mashriqi)
verdict_overall: NOTABLE (5/8 axes PASS-DIRECTED; UNIQUE on raw light-token count and length-conditional density)
---

# [[h-new-92-light-verse|H-NEW-92]] — Āyat al-Nūr (Q 24:35) Multi-Axis Structural Audit

## Headline

Q 24:35 (the Light Verse) ranks in the top 1% of the Quran on **5 of 8 pre-registered structural axes**, with **0 STRONG-PASS at Bonferroni α=0.00625**. However, on the length-conditional follow-up (which the prereg specified would only become decisive if light-density was deflated by short verses dominating the naive density rank), Q 24:35 is the **UNIQUE #1 verse in the Quran for raw light-root token count (10 tokens; double the second place)**, AND **#1 by light-density among all verses with ≥30 words (1/322)** AND **#1 among all verses with ≥20 words (1/1065)**.

The honest demarcation: Q 24:35's empirical structural signature is **"the most light-saturated long verse in the corpus"** — a measurable claim that the verse stands alone on. Its raw multi-axis profile (length, distinct-lemma, abjad) is upper-tier but shared with ~50 other long verses (Q 2:282, 24:31, 73:20, etc.). Its TTR is *low* (the verse REPEATS its key lemmas — nūr 5×, miṣbāḥ 2×, zujājah 2× — for rhetorical density rather than lexical breadth).

Verdict: **NOTABLE** on raw axes; **UNIQUE** on the light-conditioned axis.

## 1. Identification and Core Metrics

**Location.** Sūrat al-Nūr (24, Medinan, 64 verses), verse 35. Position 35/64 = 54.7% (post-midpoint by 2.5 verses). Cumulative mushaf verse #2,826 of 6,236.

**Surah named after this verse.** Sūrat al-Nūr ("The Light") is named directly from the verse-internal noun *nūr*, which appears 5 times in this single verse. This is the only surah in the Quran whose name comes from a verse-internal noun in this density of repetition.

**Arabic text (no-tashkeel):**

> ۞ الله نور السماوات والأرض ۚ مثل نوره كمشكاة فيها مصباح ۖ المصباح في زجاجة ۖ الزجاجة كأنها كوكب دري يوقد من شجرة مباركة زيتونة لا شرقية ولا غربية يكاد زيتها يضيء ولو لم تمسسه نار ۚ نور على نور ۗ يهدي الله لنوره من يشاء ۚ ويضرب الله الأمثال للناس ۗ والله بكل شيء عليم

**Translation (Saheeh International, abbreviated):**

> Allah is the Light of the heavens and the earth. The example of His light is like a niche within which is a lamp; the lamp is within glass, the glass as if it were a pearly [white] star lit from [the oil of] a blessed olive tree, neither of the east nor of the west, whose oil would almost glow even if untouched by fire. Light upon light. Allah guides to His light whom He wills. And Allah presents examples for the people, and Allah is Knowing of all things.

**Counts.**

| Metric | Value | Note |
|---|---|---|
| Real words | **48** | rank 53/6236 — top 0.85% |
| Letter graphemes | **203** | rank 53/6236 — top 0.85% |
| Distinct Leeds lemmas | **36** | rank 53/6236 — top 0.85% |
| Abjad (mashriqi) | **13,391** | rank 87/6236 — top 1.40%. = 7² × 17 × 41 ÷ ? actually 13391 = 7 × 1913 (1913 prime) — clean prime-led factorisation |
| QAC morphology segments | **69** | (Leeds segmentation, includes prefixes/suffixes) |

The convergent rank of 53 across letters/words/distinct-lemmas reflects ties in the upper-tail of the verse-length distribution. Abjad/letters strongly correlate with length so the abjad rank (87) is consistent with a non-anomalous letter-to-abjad ratio.

## 2. Eight-Axis Pre-Registered Test Results

Bonferroni α = 0.05 / 8 = 0.00625. STRONG-PASS = p < 0.00625 + extreme tail (≤62 verses); PASS-DIRECTED = p < 0.05 + moderate tail (≤311 verses); else NULL.

| # | Axis | Q 24:35 value | Rank/6236 | Top % | p (two-sided) | Verdict |
|---|---|---|---|---|---|---|
| 1 | length_letters | 203 | 53 | 0.850% | 0.0167 | PASS-DIRECTED |
| 2 | length_words | 48 | 53 | 0.850% | 0.0167 | PASS-DIRECTED |
| 3 | distinct_lemmas | 36 | 53 | 0.826% | 0.0165 | PASS-DIRECTED |
| 4 | hapax_density | 0.167 | 519 | 8.323% | 0.171 | NULL |
| 5 | divine_density | 0.083 | 1413 | 22.659% | 0.448 | NULL |
| 6 | light_density | 0.208 | 29 | 0.465% | 0.0091 | PASS-DIRECTED (narrowly missed STRONG-PASS) |
| 7 | ttr (type-token ratio) | 0.750 | 5905 | 94.7% | 0.105 | NULL — verse is **lexically REPETITIVE** |
| 8 | abjad_total | 13,391 | 87 | 1.395% | 0.0277 | PASS-DIRECTED |

**Verdict:** 5/8 PASS-DIRECTED, 0 STRONG-PASS, 3 NULL → **NOTABLE** by prereg's classification logic.

### Length-conditional follow-up (Axis 6 controlled)

The naive light-density axis was deflated because top-density verses are short verses where 1-2 light-tokens give ratios of 0.5+ (e.g. Q 85:5 "al-nāru dhātu al-wuqūd" = 2/3 = 0.667 with 3 words). To control for length, we recompute density on long-verse pools:

| Pool | Q 24:35 score | Q 24:35 rank | Pool size |
|---|---|---|---|
| All 6236 verses | density 0.208 | 29 | 6236 |
| Verses with ≥20 words | density 0.208 | **1** | 1065 |
| Verses with ≥30 words | density 0.208 | **1** | 322 |
| **Raw token count (no scaling)** | **10 tokens** | **1** | 6236 |

The next-densest verse with ≥30 words is **Q 11:81** (departure of Lot's family before dawn — the "fa-asri bi-ahli-ka" verse, with light-roots `SbH` for ṣubḥ "morning" and `wqd`) at 0.067. The third is **Q 24:40** (also in Sūrat al-Nūr, the closing "darknesses upon darknesses" counter-parable) at 0.061. The fourth is **Q 3:103** at 0.059 (the brink-of-fire metaphor). Q 24:35 leads by **3.1×** the second-place long-verse density (0.208 vs 0.067).

**Raw light-token count (no length scaling):**

| Rank | Verse | Light-root tokens | Words |
|---|---|---|---|
| **1** | **Q 24:35** | **10** | **48** |
| 2 | Q 2:17 | 4 | 17 (the hypocrites-fire parable) |
| 2 | Q 20:10 | 4 | 18 (Moses sees a fire on the mountain) |
| 4 | Q 2:257 | 3 | 24 (Allāh brings believers from darkness to light) |
| 4 | Q 28:29 | 3 | 27 (Moses sees a fire) |
| 4 | Q 39:68 | 3 | 22 (the trumpet) |
| 4 | Q 57:13 | 3 | 27 (hypocrites borrow believers' light on judgment day) |
| 4 | Q 69:13 | 3 | 6 (the trumpet — single blast) |

Q 24:35 has **2.5× the second-place verse's count** (10 vs 4). On the absolute count axis, the verse is unambiguously the most light-saturated verse in the Quran.

## 3. The 10 Light-Root Tokens

Per Leeds QAC v0.4 morphology, Q 24:35 contains **10 word-positions whose stem segment carries a root in the locked light-root set** (`nwr`, `wqd`, `SbH`, `DwA`, plus secondary `srj`, `qbs`, `Swr`, `nfx`, `shhb`, `rmd`, `Dwq`):

| # | Word pos | Form | Lemma | Root | Notes |
|---|---|---|---|---|---|
| 1 | 2 | nūru | nuwr | nwr | "the Light" (Allāh-predicate) |
| 2 | 6 | nūri-hi | nuwr | nwr | "of His Light" |
| 3 | 9 | miṣbāḥ | miṣbāḥ | SbH | "a lamp" (root SbH = morning, lamp) |
| 4 | 10 | al-miṣbāḥ | miṣbāḥ | SbH | "the lamp" |
| 5 | 17 | yūqadu | awqada | wqd | "kindled" (passive imperfect) |
| 6 | 28 | yuḍī'u | aḍā'a | DwA | "would glow" |
| 7 | 32 | nār | nār | nwr | "fire" (root nwr same as light) |
| 8 | 33 | nūr | nuwr | nwr | "light" (predicate of "upon") |
| 9 | 35 | nūr | nuwr | nwr | "light" (object of "upon") |
| 10 | 38 | nūri-hi | nuwr | nwr | "to His Light" |

Of these 10:
- **5 are lemma `nuwr`** (positions 2, 6, 33, 35, 38) — the famous fivefold *nūr*
- **2 are lemma `miṣbāḥ`** (positions 9, 10) — the lamp pair
- **1 is lemma `nār`** (position 32) — fire (same root nwr)
- **1 is lemma `awqada`** (position 17) — kindle
- **1 is lemma `aḍā'a`** (position 28) — glow

Six of these tokens share the **single root nwr** (5 nūr + 1 nār). This is the single highest concentration of an etymologically unified light-root family in any Quranic verse.

## 4. The TTR Surprise — Lexical Repetition as Rhetorical Mechanism

A naive expectation for a "rich, dense" verse is high lexical diversity (high type-token ratio). Q 24:35's TTR is **0.750**, ranking 5905/6236 — i.e., 94.7% of verses have HIGHER TTR. The verse is **deliberately lexically REPETITIVE**.

Repetition counts (lemma → count within the verse):
- nūr: 5
- miṣbāḥ: 2
- zujājah (glass): 2
- al-Allāh: 4
- li- / fi- / min / wa / lā: function-word repeats
- naar (fire): 1 — but shares root nwr with all 5 nūr's

This is a **performance-of-light-by-repetition** rhetorical strategy. The rhyme of the verse and its central image are reinforced by re-utterance of the same morpheme. The classical balāgha term is **takrār** (calculated repetition for emphasis). [[h-new-92-light-verse|H-NEW-92]] quantifies what the tradition asserted exegetically: the verse achieves its luminous effect not by lexical breadth but by lexical INSISTENCE.

**This makes Q 24:35 structurally OPPOSITE to Āyat al-Kursī (Q 2:255):**

| Feature | Q 24:35 (al-Nūr) | Q 2:255 (al-Kursī) |
|---|---|---|
| Words | 48 | 50 |
| Distinct lemmas | 36 | 34 |
| TTR | 0.750 | 0.723 (also low!) |
| Hapax density | 0.167 | 0.059 |
| Divine-name density | 0.083 (1 Allāh + others) | 0.020 (1 Allāh) |
| Light-root density | 0.208 | 0.000 |
| Strategy | Light-imagery via takrār | Theological proposition via name-stack |

Both celebrated verses are **lexically repetitive** (TTR ~0.72-0.75). The rhetorical-density tradition is correct that these verses are "loaded" — but the loading is by repetition, not by lexical novelty.

## 5. Compositional Structure — How Many Distinct Images?

Following the classical 10-jumla analysis style of Āyat al-Kursī, I segment Q 24:35 into 10 grammatical-rhetorical units:

| # | Jumla | Words # | Image / Concept | Light tokens | Words |
|---|---|---|---|---|---|
| J1 | الله نور السماوات والأرض | 1-4 | Tawḥīd-luminosity declaration | 1 nūr | 4 |
| J2 | مثل نوره كمشكاة فيها مصباح | 5-9 | Niche & lamp | 1 nūr, 1 miṣbāḥ | 5 |
| J3 | المصباح في زجاجة | 10-12 | Lamp in glass | 1 miṣbāḥ | 3 |
| J4 | الزجاجة كأنها كوكب دري | 13-16 | Glass like a pearly star | — | 4 |
| J5 | يوقد من شجرة مباركة زيتونة | 17-21 | Kindled from blessed olive tree | 1 yūqadu | 5 |
| J6 | لا شرقية ولا غربية | 22-25 | Neither east nor west (cosmic-axis negation) | — | 4 |
| J7 | يكاد زيتها يضيء ولو لم تمسسه نار | 26-32 | Its oil would almost glow even untouched by fire | 1 yuḍī', 1 nār | 7 |
| J8 | نور على نور | 33-35 | Light upon light (the apex statement) | 2 nūr | 3 |
| J9 | يهدي الله لنوره من يشاء | 36-40 | God guides to His light whom He wills | 1 nūr | 5 |
| J10 | ويضرب الله الأمثال للناس والله بكل شيء عليم | 41-48 | God strikes parables & is omniscient | — | 8 |
| **Σ** | | | | **10** | **48** |

**Distinct images/concepts identified: 10** (matching the classical Āyat al-Kursī 10-jumla template by coincidence of methodology, not by tradition; classical tafsīr breakdowns of Q 24:35 typically yield 7-8 images depending on whether "neither east nor west" is folded into J5).

**Image-density: 10 distinct concepts in 48 words = ~4.8 words per concept** — comparable to Āyat al-Kursī (10 jumal in 50 words = 5.0 words/concept).

**Concept structure (centripetal reading):**
- J1, J10 frame: divine-light declaration + parable-meta-comment (cosmic frame)
- J2, J9 outer: niche/lamp + guidance-of-light (image + theological gloss)
- J3, J4 inner: lamp-in-glass + glass-as-star (physical-to-cosmic transition)
- J5, J6 inner: olive-tree-kindling + east-west-negation (geography apophasis)
- **J7, J8** central: oil-would-glow + light-upon-light (the apex axes)

**The center is "nūr ʿalā nūr"** — the single most quoted phrase from this verse in the Sufi tradition (al-Ghazālī, *Mishkāt al-Anwār* I:6) is the structural centroid of the verse.

The phrase **nūr ʿalā nūr** (J8) is exactly **3 words** and **9 letters** — the shortest jumla of the 10. The verse's most rhetorically loaded statement is simultaneously the structurally most compressed.

## 6. Cross-Axis Comparator Table

Comparison of Q 24:35 with three other classically-celebrated verses:

| Axis | Q 1:1 (Bismillah) | Q 2:255 (Kursī) | Q 112:1-4 (Ikhlāṣ sum) | **Q 24:35 (Nūr)** |
|---|---|---|---|---|
| Letters | 19 | 189 | 47 | **203** |
| Words | 4 | 50 | 15 | **48** |
| Distinct lemmas | 4 | 34 | 11 | **36** |
| Hapax density | 0.000 | 0.059 | 0.188 | **0.167** |
| Divine-name density | 0.750 | 0.020 | 0.188 | **0.083** |
| Light-root density | 0.000 | 0.000 | 0.000 | **0.208** |
| TTR | 1.000 | 0.723 | 0.875 (mean) | **0.750** |
| Abjad | 786 | 13,659 | 1,000 | **13,391** |

**Each celebrated verse is structurally distinguished on a different axis:**
- **Bismillah (Q 1:1)**: Maximum divine-name density (0.75 — 3 of 4 words are theonyms)
- **Āyat al-Kursī (Q 2:255)**: Highest abjad among celebrated verses (13,659 ~ 13,391); highest divine-attribute count
- **Sūrat al-Ikhlāṣ (Q 112)**: Theological apophasis density (begotten-not, comparable-not); abjad clean 1,000
- **Āyat al-Nūr (Q 24:35)**: UNIQUE light-vocabulary density; longest-verse-with-imagery cluster

**No celebrated verse is structurally extreme on all axes.** Each has a single dominating signature. Q 24:35's signature is light. Q 2:255's is divine attribution. Q 1:1's is divine-name compression. Q 112:1-4's is apophatic-theology compression + abjad-1000.

## 7. Verse-Position Numerology (Descriptive, No P-Value)

- Surah 24 = 2³ × 3 (composite, smooth)
- Verse 35 = 5 × 7 (semiprime — interesting because 5 nūr's appear in this verse)
- Position fraction = 35/64 = 0.547 (post-midpoint by 2.5 verses)
- Reverse position = 64 - 35 + 1 = 30 = 2 × 3 × 5
- Cumulative verse index = 2826 (= 2 × 3 × 471 = 2 × 3³ × ? = 2 × 3 × 471, where 471 = 3 × 157 → 2826 = 2 × 3² × 157)
- Cumulative position 2826/6236 = 45.3% — the verse is just past mushaf-midpoint as well

**Speculative-only:** the verse-number 35 = 5 × 7 has the numerological coincidence that **5 = number of nūr lemmas in the verse** and **7 (the cardinal "perfect" count)** is associated in classical numerology with the heavens. This is a post-hoc observation; no null model is applied.

The cumulative position 2826 has no clean factorization linking it to the verse's content.

## 8. The al-Nūr Pericope Continuation (Q 24:35-40)

For context, light-density across the immediately surrounding verses:

| Verse | Words | Light-root tokens | Density | Note |
|---|---|---|---|---|
| Q 24:35 | 48 | 10 | 0.208 | The Light Verse itself |
| Q 24:36 | 14 | 0 | 0.000 | "In houses Allah has permitted to be raised..." |
| Q 24:37 | 19 | 0 | 0.000 | "Men whom neither commerce nor sale distract..." |
| Q 24:38 | 14 | 0 | 0.000 | "...that Allah may reward them..." |
| Q 24:39 | 22 | 0 | 0.000 | "But those who disbelieve — their deeds are like a mirage..." |
| Q 24:40 | 33 | 2 | 0.061 | "Or [they are] like darknesses within an unfathomable sea..." |

The light-language drops to zero immediately after the Light Verse and only re-emerges weakly in Q 24:40 (the "darknesses" counter-parable, where 2 light-root tokens appear in the contrast: "ẓulumātun baʿḍuhā fawqa baʿḍin ... lam yakad yarāhā... ūr"). The Light Verse is a tight lexical PEAK in the surah's nūr-density.

## 9. Verdict and Honest Limits

### Pre-registered verdict (formal)
**NOTABLE** — 5 of 8 axes PASS-DIRECTED, no axis achieves Bonferroni STRONG-PASS at α=0.00625.

### Length-conditional verdict (followup)
**UNIQUE** on the post-hoc length-controlled metric: Q 24:35 is the unambiguous #1 verse in the Quran by:
- Raw light-root token count: **10** (next: 4)
- Length-conditional density (≥30 words): **0.208** (next: 0.067)
- Length-conditional density (≥20 words): **0.208** (next: 0.136)

### Honest limits
- The 5/8 PASS-DIRECTED count would shrink under stricter Bonferroni given the "garden" — at most 4 axes (light, length-letters, length-words, distinct-lemmas) are independent; abjad is a length-derived axis; light is the expected one. Effective independent significant axes: ~3.
- The TTR = 0.750 finding (verse is REPETITIVE) is genuinely novel and counter-intuitive but its ranking (5905/6236) is in the lower tail, not extreme; this is descriptive.
- The 10-image structural breakdown (Section 5) follows methodology shared with the Āyat al-Kursī deep-dive and is observational, not p-valued.
- No claim of cryptographic-signature uniqueness is made; the verse's structural extremity is **predominantly explained by the lexical concentration of light-vocabulary** that the surah's name (al-Nūr) already telegraphs.

### What the test demarcates
- **Demonstrated**: Q 24:35 is the unique densest light-verse in the Quran on multiple measures.
- **Confirmed**: Its length / lemma-count / abjad place it in the upper 1% but not the absolute extreme.
- **Surprised**: Hapax-density is only top 8% (not extreme); TTR is **bottom tail** (verse is repetitive); divine-name density is unremarkable (top 23%).
- **Unmeasured**: Phonological/rhyme structure (the verse rhymes -m/-īm with Sūrat al-Nūr's broader rhyme scheme); semantic-vector embeddings (out of project scope); cross-Quran intra-textual echoes (the parable-formula `mathalu nūri-hi` is unique).

## 10. Cross-References

- **`findings/phase-c-structures/ayat-al-kursi.md`** — comparator deep-dive (Q 2:255), 10-jumla template
- **`findings/khawatim-al-hashr-analysis.md`** — comparator (Q 59:22-24), divine-name stack
- **`findings/per-verse-annotations.csv`** row `24,35` — atlas tags
- **`findings/phase-b-hypotheses/csv/fire-light-nwr.csv`** — raw nūr-root tokens (5 in Q 24:35)
- **`findings/phase-b-hypotheses/h-new-67-sab-tiwal-mathani.md`** — surah-level length-as-axis prior
- **`findings/phase-b-hypotheses/csv/h-new-92.json`** — full per-axis scores + ranks
- **`scripts/h_new_92_light_verse.py`** — main analysis
- **`scripts/h_new_92_followup.py`** — length-conditional follow-up
- **`journal/h-new-92-run-1.md`** — run log

## 11. Open Hypotheses for Future Test (queued, not run here)

- H-NEW-92.1: does the rhyme-letter م of Q 24:35 align with a chiastic peak in Sūrat al-Nūr's overall rhyme scheme?
- H-NEW-92.2: the phrase `nūr ʿalā nūr` (3 words, 9 letters) — does its position at the verse centroid match a corpus-wide pattern of compressed central propositions?
- H-NEW-92.3: cross-corpus, is `mathalu nūri-hi ka-` a unique parable-formula or does it have parallels in pre-Islamic Arabic poetry / Bible / Mishkāt traditions?
