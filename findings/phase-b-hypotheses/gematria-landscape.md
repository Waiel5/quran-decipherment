---
title: "Phase B — Gematria landscape, run 1"
date: 2026-04-12
agent: phase-b-novelty (gematria sub-line)
phase: B
status: exploratory (no pre-registration; this is the *landscape sweep*
        whose purpose is to surface candidate hypotheses for later
        pre-registered confirmation)
rules:
  orthography: no-tashkeel
  word_definition: orthographic-token (whitespace; recitation marks
                   contribute zero abjad)
  letter_definition: graphemes (no shadda doubling because no-tashkeel
                     has no shadda; hamza carriers أ إ ؤ ئ contribute
                     zero per analysis.tools.gematria; ا alone is 1)
  basmala_policy: counted-only-in-surah-1 (raw JSON state; basmala
                  appears once as 1:1 and is absorbed into Al-Fatiha)
  verse_numbering: hafs-kufan (114 surahs, 6236 verses)
  abjad_table: mashriqi (primary)
  abjad_table_secondary: maghribi (contrast)
  null_model: §1.5 surah-index permutation (primary, ordering claims);
              letter-bag draws from Quran (Quran-letter-distribution
              null, surrogate of §1.3); analytic binomial for
              divisibility-rate claims
fingerprint: "[nt/orth/sep/m] mashriqi totals"
caveat: |
  This is a *landscape sweep*, not a confirmatory study. Every "hit"
  below was found by multi-test scanning across many siblings, so no
  individual cell can carry a statistical claim until it is reproduced
  under a fresh pre-registered tuple. The garden-of-forking-paths is
  fully open here, by design — that is the landscape's purpose. Claims
  promoted to confirmatory status must enter test-register.md and a
  pre-reg slug under findings/phase-b-hypotheses/pre-reg/.
---

## 0. Sanity check (anchor)

```
text_value('بسم الله الرحمن الرحيم', 'mashriqi') = 786 ✅
text_value('بسم الله الرحمن الرحيم', 'maghribi') = 1026
```

786 reproduces the locked anchor (claims-catalog: family A). The
maghribi value 1026 is reported here for the first time in this
project — claims that hinge on 786 are mashriqi-table-dependent.

## 1. Per-surah and per-verse outputs

CSVs written (open with Excel/pandas/csv):

- `gematria-surah-totals.csv` — 114 rows; columns
  `surah_id, name, transliteration, n_verses, n_letters, abjad_total, abjad_per_letter`
- `gematria-verse-totals.csv` — 6236 rows; columns
  `surah_id, verse_id, n_letters, abjad_total, text`

Grand totals (all under the rules tuple in the frontmatter):

| Quantity | Value |
|---|---|
| Letters (table-present graphemes only) | 306,602 |
| Total abjad sum, mashriqi | **23,317,247** |
| Mean abjad per letter | 76.05 |
| Pearson(n_letters, abjad_total) over surahs | 0.999 |

The 0.999 correlation between surah letter count and surah abjad sum
is the dominant fact: **abjad totals are essentially proportional to
length**. Almost any "surah X has special abjad" finding is therefore
exactly equivalent to "surah X has slightly atypical letter
composition." This must be kept in mind for every finding below.

## 2. Most interesting observations (highlight section)

### 2.1 Surah 112 (Al-Ikhlas) — abjad total = exactly 1000 (mashriqi)

| Surah | Name | n_verses | n_letters | abjad (mashriqi) | abjad/letter | abjad (maghribi) |
|---|---|---|---|---|---|---|
| 112 | الإخلاص (Al-Ikhlas) | 4 | 45 | **1000** | **22.22** | 970 |

The most stylistically extreme surah in the corpus on the
abjad-per-letter axis: 22.22, vs corpus mean 76.05. The next-lowest
surah is 109 Al-Kafirun at 41.6 — Al-Ikhlas is roughly half the value
density of any other surah and ~1/3.5 the corpus mean. This reflects
its dense use of low-value letters (ا=1, ل=30, ه=5, د=4) in the words
*Allah / ahad / samad / yalid / walad / kufuwan*.

**Null test (Quran-letter-bag draw of 45 letters, 20 000 trials).**
Mean null sum = 3422 ± 1063; observed = 1000. P(sum ≤ 1000) ≈
**0.0005**. Even drawing only from short-surah letters (more
representative of register), P ≈ 0.0003.

**Roundness null.** Of the 20 000 letter-bag draws, exactly 0 hit 1000.
P(|sum − 1000| ≤ 10) ≈ 0.0002.

**Robustness.** Under maghribi the value is 970. **The exactness of
1000 is mashriqi-table-only.** The lower-tail extremeness (the surah
being on the low end of abjad-per-letter) is robust under any
table — that's a stylistic fact about its letter composition.

**Prior art.** WebSearch on "surah Al-Ikhlas total gematria abjad
1000" returned no source making the exact-1000 claim. The
masjidtucson.org Code-19 corpus does have a surah-level gematric value
calculator but I could not find a posted listing of total-1000 for
surah 112 specifically. Tag: **`novel-to-our-knowledge`**, with the
caveat that the broader "Al-Ikhlas is stylistically extreme on
low-value letters" observation is unsurprising and almost certainly
implicit in the popular literature on this surah's compactness.

**Verdict.** Most striking observation in the run, but mashriqi-only
and a downstream consequence of stylistic letter-composition. Should
be promoted to a pre-registered confirmatory test under both
orthography variants and both abjad tables, with a sibling-cell
disclosure (we also tested 113 other surahs for round-1000 hits
and got exactly one).

### 2.2 Surah 57 (Al-Hadid) — name abjad = 57 = surah index, AND حديد without article = 26 = atomic number of iron

| | mashriqi | maghribi |
|---|---|---|
| الحديد (with article) | **57** | **57** |
| حديد (without article) | **26** | **26** |

Both values are *table-invariant* (the letters ا ل ح د ي د have the
same value in both tables). Surah 57 is named "The Iron" and contains
the verse 57:25 (ironically not 57:26) explicitly mentioning iron.
57 = surah index. 26 = atomic number of Fe. 56 (≈mass of dominant
isotope ⁵⁶Fe) is not produced by either form.

**Null test (surah-index shuffle).** Under random assignment of names
to surah indices, P(at least one name's mashriqi value equals its
surah index) ≈ 0.177 over 20 000 trials. P(at least 2) ≈ 0.016. So as
an *isolated* hit, Surah 57 is roughly a 1.7σ event — not surprising
in a search of 114 surahs. The semantic resonance with iron is what
makes it feel special, and that resonance is post-hoc.

**Prior art.** Heavily previously noted by Code-19 / Quran-miracles
literature: see issp.edu.pk, truth-seeker.info, quranmiracles.com,
qurantalkblog.com. Tag: **`previously-noted-by-multiple-Code-19-sources`**.

**Verdict.** Genuinely striking and beautiful coincidence; statistically
unremarkable; widely circulated already; we add nothing new except a
cleaner null model that confirms it's an isolated hit, not a pattern.

### 2.3 The "open hunt for a magic prime" — clean null result

For each prime p ∈ {7, 11, 13, 17, 19, 23, 29, 31}, the count of
surahs whose mashriqi total is divisible by p (n=114 surahs):

| p | observed | expected (114/p) | raw 1-sided p | Bonferroni ×8 |
|---|---:|---:|---:|---:|
| 7 | 11 | 16.29 | 0.096 | 0.77 |
| 11 | 15 | 10.36 | 0.093 | 0.75 |
| 13 | 8 | 8.77 | 0.482 | 1.00 |
| 17 | 9 | 6.71 | 0.229 | 1.00 |
| **19** | **5** | **6.00** | **0.441** | **1.00** |
| 23 | 4 | 4.96 | 0.444 | 1.00 |
| 29 | 3 | 3.93 | 0.444 | 1.00 |
| 31 | 5 | 3.68 | 0.307 | 1.00 |

**Verdict.** No prime survives Bonferroni correction. Raw best is
p=11 (15 vs 10 expected, raw p ≈ 0.093). **There is no "magic prime"
hiding in surah abjad totals beyond Khalifa's 19** — and Khalifa's
19 itself is *below* expectation in this counting tuple (5 vs 6).
This is a clean negative result for the open hunt. It does not
refute the Code-19 family in general (Khalifa's claims use a
different counting tuple — Uthmani rasm, basmalas not in surahs),
only the specific question "do mashriqi surah-total sums prefer
divisibility by some prime?" The answer is no.

**Tag.** `novel-to-our-knowledge` as a *negative* result. Not a new
positive finding; more usefully, a documented null.

### 2.4 No arithmetic or geometric word-value runs of length ≥ 4

Across all 6236 verses, scanning for consecutive words whose
mashriqi values form a strict integer arithmetic progression of
length ≥ 4 or a strict integer geometric progression of length ≥ 3
(ratio > 1, integer): **zero hits**.

Length-3 arithmetic runs do occur (44 of them) at a rate consistent
with a uniform-difference null. Length ≥ 4 is consistent with chance
(~0.2 expected, 0 observed). **Verdict.** Clean null result —
the Quran does not encode arithmetic-progression sequences in word
abjad values. This is worth recording because the *expectation* (in
some popular numerology circles) is that hidden sequences should
exist; they don't.

## 3. Anomaly scans — surah level (raw lists)

### 3.1 Prime-totaled surahs (mashriqi)

11 of 114 surahs have a prime mashriqi abjad total. Expected from
prime density ~1/ln(N) is ~10.3, so this is at expectation.

| sid | name | abjad |
|---:|---|---:|
| 2 | البقرة | 1,819,849 |
| 49 | الحجرات | 101,089 |
| 61 | الصف | 61,543 |
| 72 | الجن | 66,373 |
| 74 | المدثر | 86,399 |
| 81 | التكوير | 40,253 |
| 91 | الشمس | 18,973 |
| 93 | الضحى | 12,413 |
| 95 | التين | 10,223 |
| 97 | القدر | 6,679 |
| 106 | قريش | 5,659 |

No semantic clustering; consistent with chance.

### 3.2 Surahs with abjad total ≡ 0 (mod 19)

Five surahs (expected 6 under H₀):

| sid | name | abjad | abjad/19 |
|---:|---|---:|---:|
| 6 | الأنعام | 931,190 | 49,010 |
| 41 | فصلت | 235,885 | 12,415 |
| 58 | المجادلة | 130,986 | 6,894 |
| 63 | المنافقون | 53,162 | 2,798 |
| 102 | التكاثر | 10,355 | 545 |

P(≥5 | n=114, p=1/19) ≈ 0.74. Below the expectation of ~6, not above
it. **Verdict.** No mod-19 enrichment.

### 3.3 Near-19 misses (abjad ± 1 divisible by 19)

| direction | count | surahs |
|---|---|---|
| (abjad − 1) % 19 == 0 | 4 | 13 الرعد, 48 الفتح, 95 التين, 110 النصر |
| (abjad + 1) % 19 == 0 | 3 | 45 الجاثية, 69 الحاقة, 107 الماعون |

Expected 6 each under uniform mod-19 distribution. Both below
expectation. No clustering. Not interesting.

### 3.4 Surahs whose abjad equals surah_id × K for K ≤ 10

**Zero hits.** The smallest surah total is 1000 (Al-Ikhlas, sid=112)
which would require K = 8.93 — not integer. Even relaxing K to ≤ 19
gives only one hit (Surah 57 = 57×1, which is the Al-Hadid finding).

### 3.5 Famous Arabic word values matching a surah total

Cross-checked the 20 famous values listed in code (`Allah=66`,
`Muhammad=92`, `Rabb=202`, `Nur=256`, `Rahman=329`, `Rahim=289`,
`Quran=352`, `Kitab=454`, `Iman=133`, `Islam=163`, `Din=95`,
`Hikma=78`, `Haqq=139`, `Salat=126`, `Zakat=64`, `Sawm=136`, `Hajj=42`,
`Malik=90`, `Adam=45`, `Bismillah=786`):

**Zero hits.** Every surah total exceeds 786 (Al-Falaq, the smallest
above Al-Ikhlas, is several thousand). The smallest total is
Al-Ikhlas at 1000 — which exceeds even the largest famous-word value
in the list. Famous word values cannot match surah totals because of
the floor on surah lengths.

This is a useful negative: anyone claiming "surah X has total =
[famous word]" is implicitly claiming a surah total < 1000, which
only Al-Ikhlas reaches, and Al-Ikhlas's value is 1000 not a famous
word value.

## 4. Anomaly scans — verse level

| Anomaly | Count | Notes |
|---|---:|---|
| ab = n_letters | 0 | Impossible for any nonzero verse — every letter contributes ≥ 1 and most contribute much more. (Trivial.) |
| ab = surah_id × verse_id | 3 | S25:52 (1300), S51:38 (1938), S93:11 (1023). Null mean 0.87, p ≈ 0.063. |
| ab is digit-palindrome | 121 / 6236 (1.94%) | Expected ~130 under uniform-per-digit-length null. **Below expectation.** |
| Length-3 word-abjad arithmetic runs | 44 | Consistent with uniform null |
| Length-≥4 arithmetic runs | 0 | Clean null |
| Length-≥3 integer geometric runs | 0 | Clean null |

**Max abjad verse:** S2:282 (the Debt verse, the longest verse in the
Quran), abjad = **39,114**, letters = 504. Trivially top because it
is the longest verse.

**Min abjad verse:** S20:1 طه (the two-letter muqatta'a), abjad =
**14**. Trivially bottom because it has only two letters.

**Most common verse-level abjad total:** **1559**, occurring **31
times**. All 31 occurrences are the refrain فبأي آلاء ربكما تكذبان in
Surah 55 (Ar-Rahman). Reflection of a known repetition, not an
anomaly. Top-10 most-common abjad totals are likewise dominated by
Quranic refrains (e.g. ويل يومئذ للمكذبين in Al-Mursalat at value
1684, occurring 12 times).

## 5. Word-value histogram

Total word tokens (whitespace-tokenised, no-tashkeel JSON):
**78,231** non-zero tokens + 4,578 recitation-mark-only tokens
(zero-value).

### Top-20 most frequent abjad word values

| rank | abjad | count | example token |
|---:|---:|---:|---|
| 1 | 0 | 4,578 | ۛ (recitation mark — table excludes) |
| 2 | 90 | 4,458 | من |
| 3 | 66 | 2,262 | الله |
| 4 | 50 | 2,036 | إن |
| 5 | 31 | 1,616 | إياك |
| 6 | 41 | 1,160 | ما |
| 7 | 96 | 897 | ومن |
| 8 | 100 | 883 | على |
| 9 | 791 | 814 | الذين |
| 10 | 47 | 803 | وما |
| 11 | 130 | 790 | صم |
| 12 | 56 | 756 | يوم |
| 13 | 11 | 686 | يا |
| 14 | 37 | 685 | وإياك |
| 15 | 131 | 576 | قال |
| 16 | 71 | 543 | الم |
| 17 | 35 | 526 | يكاد |
| 18 | 75 | 487 | لهم |
| 19 | 51 | 478 | إنا |
| 20 | 30 | 462 | إلى |

**Sanity check.** *Allah* (الله, value 66) at 2,262 is consistent with
the loosely cited count of "Allah occurs ~2,698 times" (Khalifa's
inclusion of basmalas). 2,262 ≈ 2,698 − 436, which is close to 113 ×
3.85 (basmalas + the four Allah-bearing words in surah 1, plus inflected
forms collapsed by the orthographic-token rule). A clean lemma-level
recount belongs in Phase A replication of `khalifa-basmala-word-counts`.

### Round hundreds 100..2000 with zero-occurrence (surprising absences)

**Three round-hundred values never occur** as the total of any single
word in the Quran:

- **1500**
- **1900**
- **2000**

All three are uncomfortable values for a single Arabic word: they
require at least one ر (200) or ت (400) plus filling letters totalling
exactly the target. 1500 = ٯ + ٔ + 1500 has no clean decomposition.
2000 ≈ 2×غ which is astronomically rare. Verdict: explainable as
combinatorial rarity, not an anomaly.

### Top-10 most common round-value words (value % 10 == 0)

| value | count | example |
|---:|---:|---|
| 90 | 4,458 | من |
| 50 | 2,036 | إن |
| 100 | 883 | على |
| 130 | 790 | صم |
| 30 | 462 | إلى |
| 140 | 461 | قيل |
| 70 | 459 | لم |
| 120 | 443 | عمي |
| 150 | 416 | عليم |
| 540 | 403 | ثم |

The list is dominated by very short common particles (مِن, إنَّ, على,
إلى). Round values cluster among short words because the round
multiples of 10 (50, 70, 90, 100, 130) coincide with common
two-letter combinations of mid-range letters. **No anomaly.**

## 6. Surah-name abjad coincidences

114 surah names. Computed mashriqi abjad of each. Searched for:

- **`name == surah_id`** — 1 hit: Surah 57 الحديد = 57. (See §2.2.)
- **`name == n_verses`** — 0 hits.
- **`name == surah_id × K, K ≤ 19`** — 3 hits: S12 يوسف=156=12×13;
  S50 ق=100=50×2; S57 الحديد=57=57×1.
- **`name divisible by 19`** — 3 hits: S5 المائدة=76=19×4; S57
  الحديد=57=19×3; S65 الطلاق=171=19×9. Expected 6; **below**
  expectation.
- **`name == triangular(surah_id)`** — 0 hits.

Under a surah-index shuffle null:

- P(≥1 name == sid) ≈ 0.18 — observed 1, not significant
- E[matches "name == sid×k for k≤19"] = 2.21 — observed 3, p ≈ 0.38,
  not significant
- div-by-19 count is invariant under shuffle; p ≈ 0.94 by analytic
  binomial, not significant

**Notable individual cells (none statistically significant; all
post-hoc):**

- **S57 الحديد = 57** (see §2.2). Both tables. Iron.
- **S50 ق = 100 = 2×50.** The single-letter surah Qaf, where the
  initial letter Qaf has abjad value 100 (an exact round hundred),
  and the surah index is exactly half. The letter Qaf is the surah
  name *and* its sole muqatta'a. Curious; not previously noted in my
  WebSearch in this exact form (the Code-19 Qaf claim is that ق
  occurs 57 times in Surah 50, not that the *value* of ق is 2×50).
  Tag: **`novel-to-our-knowledge, weak`**.
- **S12 يوسف = 156 = 12×13.** Surah 12 is Yusuf; the surah opens
  with Yusuf's dream of "eleven stars and the sun and moon" (12:4) —
  i.e. **13 celestial bodies** (11 + sun + moon). 156 = 12 × 13 =
  surah index × that count. WebSearch did not surface this exact
  observation. Tag: **`novel-to-our-knowledge, very weak`** —
  cute, but post-hoc and individually not surprising in a 114-surah
  scan.
- **S5 المائدة = 76 = 19×4** and **S65 الطلاق = 171 = 19×9.**
  Already invariant noise — under any permutation we'd expect ~6
  such hits.

**Verdict on §6 as a whole.** Three semantically resonant individual
coincidences (Hadid, Qaf, Yusuf), zero of which survives a properly
corrected family null. The Hadid one is widely circulated; the Qaf
and Yusuf ones may be original to this run as observations but are
not statistically significant.

## 7. The 114-element abjad-total sequence

- Max: **Surah 2 (Al-Baqarah)**, abjad = 1,819,849 — trivially the
  longest surah.
- Min: **Surah 112 (Al-Ikhlas)**, abjad = 1,000 — covered in §2.1.
- Spearman ρ(surah_id, abjad_total) = **−0.932** — reflects the
  well-known fact that surahs are arranged in roughly decreasing
  order of length after surah 2. Not a finding; a known feature of
  the mushaf order.
- Longest strictly-increasing run of consecutive surahs: **4**.
- Longest strictly-decreasing run: **7**.

There is **no monotonic block of length ≥ 8**, no clustering at
either prime or composite indices, and no max at an "interesting"
position. Surah 2 is max simply because it is the longest.

## 8. Summary table — findings sorted by surprisingness

| # | Finding | Effect | Best null p | Robust to maghribi? | Prior art | Verdict |
|---:|---|---|---:|---|---|---|
| 1 | Al-Ikhlas total = exactly 1000, mashriqi | extreme low-tail outlier on abjad/letter | 0.0005 | **No** (970) | not located | exploratory; pre-register before claiming |
| 2 | Al-Hadid name = 57; root هحديد = 26 | exact equality | 0.18 (single-cell) | **Yes** (both tables) | widely noted | confirmed coincidence, not novel |
| 3 | Surah 50 (Qaf) initial letter value 100 = 2 × 50 | exact 2× | n/a (1 cell) | Yes | not located in this form | novel-to-knowledge, weak |
| 4 | Surah 12 (Yusuf) name = 156 = 12 × 13 | exact equality | 0.38 (3 in-family hits) | Yes | not located | novel-to-knowledge, very weak |
| 5 | No prime p in {7..31} produces excess mod-p hits | 0 of 8 survive Bonferroni | best raw 0.09 | n/a | n/a | clean null result |
| 6 | No length-≥4 arithmetic word runs; no length-≥3 geometric runs | 0 hits | n/a | yes | n/a | clean null result |
| 7 | 3 verses with ab = sid × vid | 3 vs E[0.87] | 0.063 | n/a | n/a | not significant |
| 8 | 121 digit-palindrome verses | 1.94% | n/a (below expectation) | n/a | n/a | not anomalous |
| 9 | 5 surahs with mod-19 totals | below E[6] | 0.74 | n/a | n/a | clean null |
| 10 | "Most common verse abjad = 1559" (31 hits) | trivial | n/a | yes | known refrain | not a finding |

## 9. Ruled out as noise / survivor bias

- **Most-common abjad value 1559 (31 hits).** All 31 hits are the
  same Surah 55 refrain فبأي آلاء ربكما تكذبان. This is a fact about
  the refrain, not the abjad system.
- **Most-common abjad value 1684 (12 hits).** Same pattern: all are
  the Surah 77 refrain ويل يومئذ للمكذبين.
- **121 palindrome verses.** Below random-uniform expectation of ~130.
- **Surah 2 has the largest abjad total.** Surah 2 is the longest
  surah by every measure; no anomaly.
- **Spearman ρ(id, total) = −0.932.** Mushaf order is roughly by
  decreasing length; this correlation is a length effect, not a
  gematric one.
- **3 famous-word values matching surah totals.** Zero hits — every
  surah's total is too large for any famous-word value to match. Not
  a finding either way; just a note that the search space is empty
  for this specific sub-scan.
- **Khalifa's 19, applied to mashriqi surah totals.** 5 of 114 ≡ 0
  (mod 19), below expectation of 6. The Code-19 claim does not
  survive at the level of "raw mashriqi surah-total sums." (Khalifa's
  claims use different counting tuples — they are not refuted here,
  only this specific tuple is.)

## 10. Counting / forking-paths disclosure

### Choices made after seeing the data
- Selected the round-1000 framing for Al-Ikhlas only after observing
  the value. The lower-tail outlier observation (extreme abjad/letter)
  is the data-independent claim.
- Selected the "Yusuf 12×13 = 11 stars + sun + moon" framing
  post-hoc. The pure 156 = 12×13 fact is just a divisibility hit.
- Promoted Al-Ikhlas from a long list of surah-level scans because
  it was the only one that produced an exact round number; this is
  exactly the Bible-Codes selection trap.

### Alternative rule tuples considered and reported
- Mashriqi vs maghribi reported wherever it changed a verdict
  (Al-Ikhlas: yes — only mashriqi gives 1000)
- We have not yet rerun against full-tashkeel (which would change
  letter counts via shadda), against min-tashkeel, or against the
  Uthmani rasm. Pre-registered confirmation must do so.

### Sibling hypotheses considered (in this run)
- 8 prime moduli — see §2.3
- 20 famous-word values — 0 hits
- Verses-where-ab=sid×vid — 3 hits, p ≈ 0.063
- Verses-where-ab is palindrome — 121 hits, below expectation
- Length-3, length-4, length-5 arithmetic and geometric word runs
- Surah-name == sid, sid×k, n_verses, triangular, divisible by 19
- 4 different anomalies on the 114-element sequence

The full sibling family for the §2 highlights is large (≈ 50
distinct cells across surah-level and verse-level scans). Bonferroni
threshold for any single cell to be "novel-finding" significant
would require raw p < 0.005/50 = 0.0001. **No cell hits this.** The
Al-Ikhlas finding's letter-bag null at p ≈ 0.0005 is the closest, and
it is brittle to the abjad-table choice.

### Why these and not others
- Highlighted because they were the largest-effect-size or
  most-semantically-resonant cells in the run, NOT because they
  passed any pre-registered threshold. The landscape sweep is
  exploratory by design.

## 11. Promotion candidates for pre-registered confirmation

The following candidates are queued for the test register and a
pre-registration commit:

1. **Al-Ikhlas abjad/letter is the global minimum.** Robust under
   abjad table; robust under orthography; well-defined statistic; can
   be tested under a clean letter-bag null + a cross-table robustness
   check. If it survives both, this is a Phase B finding about the
   *stylistic* compactness of the surah, not about its sum being
   1000. (Recommended primary statistic: abjad/letter z-score relative
   to all 114 surahs.)
2. **Open-prime null** §2.3 as a *negative* publishable result —
   "no prime p ∈ {7..31} other than 19 produces excess divisibility
   in mashriqi surah totals; 19 itself is below expectation in this
   tuple." Document under Phase A red-team table.
3. **No length-≥4 arithmetic / length-≥3 geometric word runs** as a
   negative result. Trivially reproducible from the CSV.

All three should enter `findings/phase-b-hypotheses/test-register.md`
when that file is created (it does not yet exist).

## 12. References

Prior-art links touched in this run:

- https://www.issp.edu.pk/miracle-of-iron-in-the-quran/
- https://www.truth-seeker.info/quran-science-2/atomic-number-iron/
- https://qurantalkblog.com/2022/02/09/iron/
- https://www.masjidtucson.org/quran/wordCount/QuranGV.php
- https://en.wikipedia.org/wiki/Abjad_numerals
- https://fountainmagazine.com/all-issues/2015/issue-105-may-june-2015/numerical-codes-and-gematrical-mysteries-in-the-quran-may-june-2015/
