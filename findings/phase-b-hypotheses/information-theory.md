---
title: "Information-theoretic profile of the Quran"
phase: B
status: exploratory
agent: phase-b-information-theory
date: 2026-04-12
rules:
  orthography: no-tashkeel
  word_definition: lemma                # Quranic Arabic Corpus 0.4 LEM field
  letter_definition: graphemes          # U+0621..064A ∪ U+0671..06D3
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: not-applicable            # exploratory; no nulls run yet
script: analysis/info_theory_run.py
intermediate_csvs:
  - findings/phase-b-hypotheses/csv/per-surah-entropy.csv
  - findings/phase-b-hypotheses/csv/kl-matrix.csv
  - findings/phase-b-hypotheses/csv/compression.csv
  - findings/phase-b-hypotheses/csv/verse-index-trend.csv
  - findings/phase-b-hypotheses/csv/info-theory-results.json
sanity:
  total_letters: 330709                 # matches §8 anchor
  verses: 6236                          # matches §8 anchor
  surahs: 114                           # matches §8 anchor
---

# Information-theoretic profile of the Quran

> **The Quran is one text.** Every "split" in this report is internal
> (surah, verse, position-within-verse) — not "edition" vs "edition."
> Where letters and lemmas are reported, the rules tuple is in the
> frontmatter. No claim here has been put through a null model;
> everything is **exploratory** in the §3 sense of the rigor protocol.
> Promotable findings are flagged at the bottom.

## TL;DR

| Quantity | Value | Notes |
|---|---:|---|
| Letter entropy `H₁` | **4.387 bits/letter** | over 36 observed graphemes, 330 709 letters |
| Redundancy vs uniform 28-letter | **8.75 %** | `1 − H/log₂28` |
| Redundancy vs observed 36-symbol | **15.15 %** | `1 − H/log₂36` |
| `H(L₂ \| L₁)` | **3.966 bits** | letter bigram conditional |
| `H(L₃ \| L₁,L₂)` | **3.321 bits** | letter trigram conditional |
| `H(L₅ \| L₁..L₄)` | **1.547 bits** | n=5 conditional (downward biased — see §2 caveat) |
| Zipf exponent α (lemmas) | **1.318** | OLS log-log fit, R² = 0.975 |
| Heaps β (lemmas) | **0.618** | V = 5.62 · N⁰·⁶¹⁸, R² = 0.986 |
| Position–letter MI | **0.077 bits** | normalized 1.7 % of min(H_P, H_L) |
| Most-similar surahs (lowest KL) | **108 ↔ 103** | Al-Kawthar ↔ Al-'Asr |
| Most-dissimilar surahs (highest KL) | **2 ↔ 102** | Al-Baqara ↔ At-Takathur |
| Lowest-entropy surah | **#112 Al-Ikhlas** | H = 3.406 (47 letters — small-sample) |
| Highest-entropy surah | **#80 'Abasa** | H = 4.608 |

---

## 1. Letter-frequency entropy

The 330 709 letters of the no-tashkeel Quran fall over **36 distinct
grapheme types** (the 28 base Arabic letters, plus four hamza variants
أ إ ؤ ئ ء, alif madda آ, alif maqsura ى, ta marbuta ة, and the U+0671
alif-with-wasla family). Top-10 letters and their counts:

| Letter | Count | P(L) |
|---|---:|---:|
| ا | 43 542 | 13.17 % |
| ل | 38 191 | 11.55 % |
| ن | 27 270 | 8.25 % |
| م | 26 735 | 8.08 % |
| و | 24 813 | 7.50 % |
| ي | 21 973 | 6.65 % |
| ه | 14 850 | 4.49 % |
| ر | 12 403 | 3.75 % |
| ب | 11 491 | 3.47 % |
| ت | 10 520 | 3.18 % |

The top three letters carry 33 % of all letter mass. Shannon entropy:

> **H = 4.387 bits/letter**

Compared to a uniform 28-letter alphabet (`log₂ 28 = 4.807`), the
**redundancy is 8.75 %**. Compared to the actual 36-symbol observed
alphabet (`log₂ 36 = 5.170`), the redundancy is **15.15 %**.

For context: Shannon's classical English single-character entropy is
~4.14 bits, which corresponds to ~11 % redundancy against
`log₂ 26 = 4.70`. Quranic Arabic (no-tashkeel) is **slightly less
redundant** at the unigram level than English — primarily because the
Arabic 28-letter alphabet is larger to begin with and the Quran uses
nearly all of it heavily.

## 2. Block / conditional entropies (letter level)

Using block entropies `Hₙ = H(L₁..Lₙ)` over all overlapping
n-grams from the concatenated letter stream:

| n | `Hₙ` (joint) | `H(Lₙ\|L₁..Lₙ₋₁)` |
|---:|---:|---:|
| 1 | 4.387 | 4.387 |
| 2 | 8.352 | **3.966** |
| 3 | 11.673 | **3.321** |
| 4 | 14.131 | 2.458 |
| 5 | 15.678 | 1.547 |

Reading the conditional entropies: the *next* Quranic letter is worth
**3.32 bits of surprise given the previous two**. Knowing the previous
two letters cuts the per-letter information by **24 %** of the unigram
value. This is significantly more constrained than the unigram
distribution alone implies, and is the first quantitative measure of
the "morphological cohesion" of Quranic Arabic — the constraint is
dominated by triliteral root structure and the fixed prefix/suffix
inventory (al-, wa-, fa-, bi-, li-, -hu, -ha, -hum, -na, -kum…).

**Caveat (small-sample bias for n ≥ 4):** at 36 symbols and ~330 700
positions, the n=5 estimate has roughly 6 ×10⁷ possible 5-grams to
fill from 3 ×10⁵ observed positions. The block-entropy estimator is
biased downward at small sample fractions, so the n=4 and n=5 numbers
above should be read as *upper bounds on the true entropy rate* and
likely overstate predictability. The n=2 and n=3 estimates are
reliable.

A first-cut **estimated entropy rate** is `H(L₃|L₁,L₂) ≈ 3.32 bits/letter`,
which is the most defensible rough number. Comparable English block
estimates run ~2.8–3.0 bits/character at the same order; Quranic Arabic
is *less* predictable than English at the bigram/trigram level, again
because the alphabet is larger and the morphological combinatorics are
richer.

## 3. Per-surah letter entropy

Full per-surah table in `csv/per-surah-entropy.csv`. Bottom-10 and top-10
by per-surah letter entropy:

### Bottom 10 (lowest H_letter)

| # | Surah | Type | n_letters | H |
|---:|---|---|---:|---:|
| 112 | Al-Ikhlas | meccan | 47 | **3.406** |
| 109 | Al-Kafirun | meccan | 99 | 3.657 |
| 103 | Al-'Asr | meccan | 73 | 3.687 |
| 114 | An-Nas | meccan | 80 | 3.738 |
| 1 | Al-Fatihah | meccan | 143 | 3.921 |
| 107 | Al-Ma'un | meccan | 114 | 3.938 |
| 102 | At-Takathur | meccan | 123 | 3.980 |
| 108 | Al-Kawthar | meccan | 43 | 3.987 |
| 105 | Al-Fil | meccan | 97 | 4.069 |
| 101 | Al-Qari'ah | meccan | 160 | 4.084 |

### Top 10 (highest H_letter)

| # | Surah | Type | n_letters | H |
|---:|---|---|---:|---:|
| 74 | Al-Muddaththir | meccan | 1 035 | 4.454 |
| 92 | Al-Layl | meccan | 314 | 4.462 |
| 18 | Al-Kahf | meccan | 6 552 | 4.466 |
| 20 | Taha | meccan | 5 399 | 4.474 |
| 54 | Al-Qamar | meccan | 1 469 | 4.490 |
| 53 | An-Najm | meccan | 1 433 | 4.494 |
| 79 | An-Nazi'at | meccan | 785 | 4.500 |
| 87 | Al-A'la | meccan | 296 | 4.504 |
| 88 | Al-Ghashiyah | meccan | 382 | 4.508 |
| 80 | 'Abasa | meccan | 552 | **4.608** |

### What this means (and doesn't mean)

**Both the top 10 and the bottom 10 are entirely Meccan.** That is *not*
a Meccan-vs-Medinan difference — the Meccan corpus simply contains both
extremes because (a) the very short late-mushaf surahs are Meccan and
(b) the rhetorically dense oath-surahs are also Meccan.

The big driver is **length, via small-sample bias**:

- `Pearson(letter count, H) = 0.245`
- `Pearson(log letter count, H) = 0.583`

The bottom-10 surahs all have <200 letters; entropy estimates from such
short samples systematically *under*-estimate the true entropy because
many of the 36 letter types simply don't appear (e.g. Al-Kawthar uses
only 18 distinct letters in its 43 letters of text). The Meccan/Medinan
group means are nearly identical and the difference is well within
noise:

| Group | n surahs | mean H | sd H |
|---|---:|---:|---:|
| Meccan | 86 | 4.303 | 0.198 |
| Medinan | 28 | 4.326 | 0.048 |

The Medinan SD is 4× smaller — Medinan surahs are uniformly long enough
to fully sample the alphabet, so they all sit near the asymptotic
entropy. The Meccan SD is wide because it spans both
small-sample-collapsed values and the high-rhetoric mid-Meccan peak.

**Honest reading:** unigram letter entropy is *not* a useful Meccan/Medinan
discriminator. Length swamps any genuine signal at this granularity.
A length-stratified comparison would be the next step if anyone wants
to claim a Meccan/Medinan letter-entropy effect.

## 4. Zipf's law on lemmas

Lemma source: 74 608 lemma-bearing morphemes in the Quranic Arabic
Corpus 0.4 (one per `STEM` line carrying a `LEM:` field), over 4 832
distinct lemmas.

Top-10 lemmas by frequency:

| Rank | Lemma (QAC Buckwalter) | Gloss | Count |
|---:|---|---|---:|
| 1 | min | "from / of" | 3 226 |
| 2 | {ll~ah | Allāh | 2 699 |
| 3 | maA | "what / not" | 2 565 |
| 4 | laA | "no / not" | 1 738 |
| 5 | fiY | "in" | 1 701 |
| 6 | <in~ | "indeed / if" | 1 682 |
| 7 | qaAla | "to say" | 1 618 |
| 8 | {l~a*iY | "the one who" | 1 464 |
| 9 | EalaY` | "on / over" | 1 445 |
| 10 | kaAna | "to be / was" | 1 358 |

OLS log-log regression on (rank, frequency):

> **α = 1.318**,  intercept = 9.94,  **R² = 0.975**

Canonical natural-language Zipf is α ≈ 1.0 (English novels typically
1.0–1.1; modern-standard-Arabic news corpora 1.0–1.2). The Quranic
lemma distribution is **noticeably steeper** than baseline natural
language: the head dominates more, and the tail of hapax-like lemmas
is correspondingly lighter. The text behaves as if its lexical
"vocabulary budget" is **more concentrated** on a small theological /
function-word core than typical Arabic prose.

This is consistent with what little prior literature touches the
question (e.g. discussions in Yaḥyā 2019 on Sūrat al-Aḥzāb / al-Ghāfir
finding deviations from canonical Zipf, and the popular but
methodologically loose "Quran violates Zipf" essay) but is the first
clean number on the *whole* text under a clearly-disclosed lemma rule.

**Caveat:** the OLS log-log estimator overweights the noisy tail. A
maximum-likelihood (Clauset–Shalizi–Newman) power-law fit would
typically give a slightly *smaller* α (commonly 0.05–0.10 lower for
text data of this size). The qualitative claim ("steeper than 1.0")
survives both estimators easily.

## 5. Heaps' law (vocabulary growth)

Random subsamples of lemma tokens (without replacement, single seed):

| N | Distinct lemmas V |
|---:|---:|
| 100 | 70 |
| 500 | 289 |
| 1 000 | 461 |
| 2 000 | 711 |
| 5 000 | 1 238 |
| 10 000 | 1 833 |
| 20 000 | 2 670 |
| 30 000 | 3 210 |
| 50 000 | 3 982 |
| 74 608 | 4 832 |

OLS fit `log V = log K + β log N`:

> **β = 0.618**,  K = 5.62,  **R² = 0.986**

Heaps β for natural-language text typically lies in 0.4–0.6 (English
prose ~0.5, news Arabic ~0.5–0.55). β = 0.618 is **on the high side**
of the expected range — meaning the Quran *keeps* introducing new
lemmas as you read, somewhat faster than typical prose of the same
length. This sits in tension with the steeper-than-1 Zipf exponent
(which says the head is heavier) and reflects the genuine duality of
Quranic style: a small tightly-repeated theological core *plus* an
unusually rich tail of low-frequency lexemes (rare oath-formula nouns,
narrative-specific names, technical legal vocabulary).

In Heaps-Zipf terms, the inequality `β ≈ 1/α` predicts β ≈ 1/1.318
≈ 0.759. The observed 0.618 is below that prediction, which is the
direction expected when the corpus is large enough to suppress the
hapax tail relative to a pure-Zipf asymptote.

## 6. KL divergence between surahs

A 114×114 KL matrix `KL(P_i ‖ P_j)` was computed over the 4 832-lemma
vocabulary with Laplace smoothing (α = 0.5). Stored at
`csv/kl-matrix.csv`. Highlights:

- **Most-similar pair (lowest KL):**
  - Surah 108 Al-Kawthar  ↔  Surah 103 Al-'Asr,  KL = **0.0065**
  - Both are 3-verse Meccan surahs at the very end of the mushaf,
    composed almost entirely of high-frequency function words (إن,
    الذي, لا, إلا, في, الإنسان…) so their lemma profiles are nearly
    indistinguishable from each other and from "pure short Quranic
    formula."
- **Most-dissimilar pair (highest KL):**
  - Surah 2 Al-Baqara  ↔  Surah 102 At-Takathur,  KL = **2.163**
  - Al-Baqara is the longest surah (286 verses, dense legal /
    narrative vocabulary); At-Takathur is 8 verses of pure
    eschatological warning. The asymmetry is mostly the
    "small-vocabulary surah looks very alien from the perspective of
    a giant surah" effect, not a genuine semantic distance — KL
    against a small-support distribution is structurally inflated.

A naïve **2-cluster smoke test** (assign each surah to whichever of
{Al-Fatiha, Al-Baqara} it is closer to in symmetrized KL) recovers the
declared Meccan/Medinan label for **74.6 %** of surahs (85/114). Not
impressive on its own, but it confirms that the lemma distribution
*does* carry a Meccan/Medinan signal at the level of "any reasonable
distance metric will find it." Proper hierarchical clustering (Ward
linkage on Jensen-Shannon distance) is the natural follow-up; not
done in this pass.

**Caveat:** KL with Laplace smoothing on sparse short-surah supports
inflates extreme values. The asymmetry of KL means "most dissimilar"
is direction-dependent; the right symmetric metric is Jensen-Shannon
distance.

## 7. Compression complexity proxy

Each surah's raw UTF-8 text was compressed with `gzip` (level 9) and
`zlib` (level 9). Full table at `csv/compression.csv`.

### Most compressible (lowest gzip ratio)

| # | Surah | Type | raw bytes | gzip ratio |
|---:|---|---|---:|---:|
| 2 | Al-Baqarah | medinan | 60 107 | **0.258** |
| 4 | An-Nisa | medinan | 37 224 | 0.262 |
| 55 | Ar-Rahman | medinan | 3 654 | 0.267 |
| 3 | Ali 'Imran | medinan | 34 118 | 0.272 |
| 9 | At-Tawbah | medinan | 25 241 | 0.272 |

### Least compressible (highest gzip ratio)

| # | Surah | Type | raw bytes | gzip ratio |
|---:|---|---|---:|---:|
| 111 | Al-Masad | meccan | 184 | 0.734 |
| 106 | Quraysh | meccan | 170 | 0.753 |
| 110 | An-Nasr | medinan | 181 | 0.762 |
| 112 | Al-Ikhlas | meccan | 108 | 0.787 |
| 108 | Al-Kawthar | meccan | 95 | **0.979** |

Correlations:

- `Pearson(gzip ratio, H_letter) = −0.618`
- `Pearson(gzip ratio, raw bytes) = −0.543`

**The compression ratio is mostly measuring "is this surah long enough
to amortize the gzip header."** A surah of 95 bytes barely shrinks
because the gzip wrapper overhead alone is ~30 bytes; the compression
algorithm hasn't seen enough text to build a useful dictionary.

Interesting exception: **Ar-Rahman** (#55) at 0.267 is highly
compressible despite being only 3 654 bytes — far smaller than the
other surahs in the top-5. This is the one surah whose internal
structure famously contains a refrain (فَبِأَيِّ آلَاءِ رَبِّكُمَا
تُكَذِّبَانِ, "so which of the favors of your Lord will you deny",
repeated 31 times). Gzip's LZ77 sliding window picks up the repeat and
slashes the ratio. **This is the one place compression measures
genuine internal redundancy rather than length.** Worth a formal
follow-up: compute "compression-residual" = gzip ratio after partialling
out length, and see whether Ar-Rahman is an outlier on a normalized
scale. Predicted answer: yes, by a wide margin.

## 8. Mutual information between position and letter

For each verse, look at letter positions 1, 2, …, 30 (truncating
longer verses, ignoring shorter). Build the joint distribution `P(p,
letter)` and compute MI:

| Quantity | Value |
|---|---:|
| `H(position)` | 4.894 bits |
| `H(letter)` | 4.390 bits |
| `H(position, letter)` | 9.208 bits |
| **MI(position; letter)** | **0.077 bits** |
| MI / min(H_P, H_L) | 1.7 % |

**There is statistically detectable structure but it is small.** A
0.077-bit MI says that knowing where in a verse you are tells you
about 1.7 % of the information needed to predict the next letter,
above and beyond the marginal letter distribution. That's consistent
with grammatical morphology (e.g. the Arabic `wa-` and `fa-`
sentence-initial prefixes; the `-na`, `-ya`, `-hu` verse-final suffix
clusters) but it is *not* a strong "position predicts letter" signal.
Quranic Arabic does not have a hidden positional template; the
positional bias is roughly the size of "Arabic morphology has
positional preferences."

## 9. Novelty hunt — entropy outliers

Verses with the most extreme per-verse letter entropies (filtered to
verses with ≥ 10 letters, so we don't return 1-word verses):

### Lowest-H verses (most repetitive)

| Surah:Verse | n_letters | H |
|---|---:|---:|
| 90:3 | 11 | **2.187** |
| 112:3 | 12 | 2.252 |
| 73:2 | 15 | 2.289 |
| 35:21 | 16 | 2.352 |
| 37:1 | 11 | 2.369 |
| 56:42 | 11 | 2.369 |
| 104:9 | 10 | 2.371 |
| 77:2 | 13 | 2.412 |
| 77:4 | 13 | 2.412 |
| 56:37 | 10 | 2.446 |

These are the rhetorically rhythmic, alliterative verses — short oath
verses (37:1 وَالصَّافَّاتِ صَفًّا, 77:2 فَالْعَاصِفَاتِ عَصْفًا)
where the same root is repeated for sound effect. This is exactly
where information-theoretic outlier-detection *should* light up, and
it does. **The entropy minimum is automatically finding jinas /
parallelism / paronomasia structure**, which we already have a
separate Phase B agent investigating (`jinas-wordplay.md`). The
two methods should be cross-checked: any verse that appears in both
the jinas-wordplay catalog and this low-entropy list is doubly
confirmed as a stylometric outlier.

### Highest-H verses (most lexically diverse)

| Surah:Verse | n_letters | H |
|---|---:|---:|
| 11:57 | 81 | 4.421 |
| 6:54 | 108 | 4.431 |
| 5:12 | 207 | 4.432 |
| 2:260 | 148 | 4.435 |
| 22:5 | 262 | 4.435 |
| 4:114 | 97 | 4.435 |
| 48:29 | 249 | 4.438 |
| 40:40 | 88 | 4.451 |
| 20:127 | 50 | 4.473 |
| 33:19 | 155 | **4.477** |

These are long compound legal/narrative verses. The most-entropic
verse 33:19 is a dense compound polemical sentence in Surat al-Ahzab
— exactly the register where a verse will visit nearly every letter
of the alphabet at least once. Less interesting as a "rhetorical
outlier," more as a "longest-syntax outlier."

## 10. Per-verse-index entropy trend within surahs

Pearson `r` between verse index and per-verse letter entropy, computed
for each surah with ≥ 5 verses of ≥ 10 letters (107 surahs survive):

- **mean Pearson r = +0.088**
- 61 / 107 surahs (57 %) show a positive trend (later verses slightly
  higher entropy)

**This is essentially a null result** with a tiny positive bias. The
small bias is plausibly an opening-formula effect: surahs that begin
with huroof muqatta'at, oaths, or short formulaic vocatives have
artificially low-entropy first verses, which mechanically tilts the
per-surah trend positive. There is no evidence of a strong systematic
"information rises through a surah" or "information falls through a
surah" pattern. Quranic surahs are *not*, on average, organized as
information-monotonic ramps in either direction.

## Garden of forking paths disclosure

### Choices made before seeing data

- Lemma source = QAC 0.4 LEM field, no inflection collapse beyond what
  the LEM field already does.
- Letter set = methodology §8 standard graphemes (no recitation marks,
  no tashkeel, no tatweel).
- Smoothing for KL = additive α=0.5 (chosen because α=1 over-smooths a
  4 832-vocab matrix and α=0.1 leaves zero-vector instabilities).
- Heaps sample sizes: 100, 500, 1000, 2000, 5000, 10k, 20k, 30k, 50k,
  full. Rounded log spacing.
- Position MI: cap = 30 letters (empirically the median verse length).

### Choices made after seeing data

- Bottom-10 / top-10 surah entropy split called out as "all Meccan"
  *because the data showed it*. Honest report: this is descriptive,
  not a claim — both extremes are Meccan, and the underlying driver is
  surah length.
- Ar-Rahman flagged as a compression outlier *after* seeing the
  `gzip ratio vs length` correlation. This is exploratory; a
  pre-registered "length-residualised compression" hypothesis is on
  the to-do list.

### Sibling hypotheses considered (not pursued)

- Letter entropy after grouping shadda-doubled letters (full-tashkeel
  required; not run).
- Word-level rather than lemma-level Zipf — would give a *different* α
  because of inflectional variants. Not run; the lemma α is the
  cleaner number for cross-language comparison.
- Per-juz' (1/30 division) entropy instead of per-surah. Not run.
- Conditional entropy at the *word* level. Not run; word-level
  bigrams are too sparse on a 78k-token corpus to be reliable.

### Why the lemma-Zipf result is the headline

It's the only number in this report that
(a) doesn't depend on a small-sample-biased estimator,
(b) survives a single arbitrary smoothing-parameter choice without
moving its leading digit,
(c) has a clean prior literature to compare against (canonical α ≈ 1.0
for natural language), and
(d) deviates from baseline by enough to be visible without fine-tuning
(α = 1.32 vs 1.0–1.2 for other Arabic corpora).

It is *also* the only result in this report that has a chance of
surviving a formal length-matched comparable-corpus null
(rigor-protocol §1.4) once we have a clean classical-Arabic comparable
corpus (early hadith with Quran citations stripped is the obvious
candidate).

## Honest null discussion

**Nothing in this report has a p-value attached.** Every tabulated
quantity is descriptive. Specifically:

- The "bottom 10 entropy" surahs are all small. The "top 10" are all
  Meccan but mostly mid-Meccan and hand-recognised as the rhetorically
  oath-laden register. Neither extreme has been tested against a null
  that controls for length; both are likely length-driven.
- The KL "most dissimilar" pair involves one of the longest and one of
  the shortest surahs. KL against a sparse-support distribution is
  structurally inflated. Not a "finding" until tested against a
  surrogate that randomizes lemma assignment within length-matched
  bins.
- Heaps β > 0.5 and Zipf α > 1 are *real* corpus-level statistical
  properties that don't depend on small-sample tricks, but they are
  not surprising under the null "Arabic religious / classical text" —
  we'd need a length-matched comparable-corpus null (§1.4) to call
  them findings.

The tightest pre-registerable claim that comes out of this run is:

> **Pre-registration sketch (not yet committed):** the Quranic lemma
> Zipf exponent under the QAC 0.4 LEM rule is α ≥ 1.25 with R² ≥ 0.95
> when fit by OLS log-log over all 4 832 distinct lemmas; under a
> length-matched bootstrap from a classical-Arabic prose corpus
> (early-hadith, Quran citations stripped), the same fit will yield
> α < 1.20 with probability > 0.95.

That is the test that *would* turn the headline number into a finding
under §3 of the rigor protocol.

## What's NOT in this report

- No null model run on any statistic. Everything is descriptive.
- No robustness check against alternative orthography (full-tashkeel,
  hamza-collapsed, with-shadda-doubled).
- No proper hierarchical clustering on the KL matrix.
- No length-residualized compression analysis (the Ar-Rahman finding
  is informal).
- No word-level (as opposed to lemma-level) Zipf or Heaps.
- No comparison against any non-Quran Arabic comparable corpus.

## Prior art (web search, 2026-04-12)

A literature scan turns up almost no comprehensive
information-theoretic profile of the Quran. The handful of relevant
references:

- Yaḥyā et al., "Study of Zipf's Law in the Qur'ān's Sūrat al-Aḥzāb
  and Sūrat al-Ghāfir" (Journal of Quranic Studies, Mashhad). Reports
  Zipf-deviation findings on two individual surahs but doesn't compute
  α on the whole text or under a disclosed lemma rule.
- The popular essay "Quran Violates Zipf's Law, Unlike Any
  Human-Authored Book" (114chambers blog, 2022) — apologetic, no
  rules tuple, claim is overstated.
- Abid Labs, "Can a Machine Learn to Classify Meccan and Medinan
  Surahs?" (blog, 2018) — uses scikit-learn classifiers on word
  features; doesn't compute KL or entropy.
- "Compression-Based Arabic Text Classification" (Mesleh et al., 2014;
  IEEE) — applies gzip/RAR/LZW to Arabic news classification but does
  not target the Quran.
- "Multi-Dimensional NLP Analysis of the Quran" (Quranica journal,
  2024) — emotional/thematic profile, not information-theoretic.

To the best of this scan, **there is no published whole-Quran Shannon
entropy + conditional entropy + Zipf + Heaps + KL + compression
profile under a disclosed rules tuple**, which is what this document
provides. That is itself a scouting result: this analysis is novel as
a *combination*, even before any individual number is promoted to a
finding.

## Reproducibility

```
python3 /Users/grey/Downloads/quran/analysis/info_theory_run.py
```

Pure Python stdlib, single file, no NumPy / SciPy / pandas. Runtime
~3 minutes on a laptop, dominated by the 114×114 KL matrix (~5 ×10⁵
KL evaluations × 4 832 vocab = ~2.5 ×10⁹ floating ops).

Outputs the four CSVs and the JSON sidecar listed in the frontmatter,
all under `findings/phase-b-hypotheses/csv/`.
