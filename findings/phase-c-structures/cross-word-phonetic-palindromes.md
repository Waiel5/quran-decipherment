---
finding_id: h-new-16-palindromes
phase: B
status: REVERSE SIGNAL (palindromes UNDER-represented; one-tailed H fails, two-tailed significant for depletion)
date: 2026-04-13
rules_tuple: (no-tashkeel, tajwid-normalized, rasm-consonant, hamza→alif, 28-letter)
null_model: within-verse word-shuffle (200 perms) + verse-length-matched bigram Markov (100 perms)
bonferroni_k: 3
seed: 20260413
author: computational-tester
---

# H-NEW-16 — cross-word phonetic palindromes ≥7 consonants

## Hypothesis

After minimal tajwīd normalization (hamzat al-waṣl deletion at word-start after
a consonant), the Quran should contain **more** palindromic consonant-substrings
of length ≥7 than two nulls predict, with clustering near verse boundaries.
Hypothesis was that hidden phonetic palindromes are a compositional signature.

## Methodology

Normalization: hamza variants → alif, ى → ي, ة → ه. Tajwīd rule: at each
word-start, if the word begins with alif AND the previous word's final consonant
is not alif/wāw/yāʾ, drop the alif (hamzat al-waṣl elision). Produces a
consonant-only string per verse, 310,805 total characters.

Palindrome finder: brute-force center-expansion, reporting all ℓ ≥ 7 matches.

**Null 1 — within-verse word-shuffle**: shuffle words within each verse, 200
perms. Tests whether observed palindrome count exceeds what random word-
reordering produces.

**Null 2 — bigram Markov**: build bigram transition matrix from full Quranic
tajwid-concat, sample length-matched strings per verse, 100 perms.

Bonferroni k = 3, α_bon = 0.00333.

## Results (one-tailed, H: palindromes OVER-represented)

| Test | Observed | Null μ | Null σ | z | p (one-sided, upper) | Pass? |
|---|---|---|---|---|---|---|
| Per-verse palindrome count | **67** | 148.3 | 12.75 | **−6.38** | 0.9999999999 | **FAIL** |
| Bigram Markov sample | **67** | 128.8 | 13.07 | **−4.73** | 0.9999989 | **FAIL** |

Both tests FAIL the original one-tailed hypothesis direction.

## Reverse-direction observation (two-tailed depletion)

The Quran's palindrome count is **dramatically LOWER** than both nulls. Under a
two-tailed interpretation:

- Null 1: z = −6.38 → two-tailed p ≈ **1.8 × 10⁻¹⁰** for depletion
- Null 2: z = −4.73 → two-tailed p ≈ **2.3 × 10⁻⁶** for depletion

**The Quran has FEWER cross-word phonetic palindromes than random reshuffles
of its own words or than bigram-statistics-matched synthetic Arabic.** The
depletion ratio is 67 / 148.3 = 0.45 (null 1) and 67 / 128.8 = 0.52 (null 2).
The Quran contains roughly half as many ℓ ≥ 7 consonant palindromes as naive
shuffles produce.

This is a genuinely unexpected finding that needs honest framing. It's a
two-tailed significant effect in the DEPLETED direction. Two-tailed was NOT
pre-registered, so it's exploratory.

## Sub-analysis: verse-boundary clustering

Of 77 palindromes found in the full-tajwid concat (slightly different count
than the per-verse scan because full-concat allows palindromes crossing verses):
- **37 near verse boundary** (midpoint within 10 chars of verse edge)
- **40 in verse center** (midpoint > 10 chars from edge)

No dramatic edge-clustering. A length-equalized null (palindromes uniformly
distributed in verses) would predict ~20/77 near-edge if edge = first/last
10 chars per verse and mean verse length ≈ 50. Observed 37/77 is nominally
enriched — but the enrichment test wasn't formally pre-registered and the
overall palindrome count is already depleted.

## Top 15 longest palindromes (full concat, tajwid-normalized)

| Length | String | Position |
|---|---|---|
| 10 | هثالثثلاثه | 61467 |
| 9 | نمنالانمن | 60167 |
| 9 | الوالاولا | 148165 |
| 9 | لنمانامنل | 198658 |
| 9 | كانمومناك | 214398 |
| 9 | الوالاولا | 279050 |
| 9 | وربكفكبرو | 298022 |
| 8 | قتاللاتق | 19868 |
| 8 | ثالثثلاث | 61468 |
| 7 | اامنماا | 11911 |
| 7 | لهلالهل | 20974 |
| 7 | لهلالهل | 24765 |
| 7 | لقيفيقل | 34746 |
| 7 | تالالات | 36267 |
| 7 | هملعلمه | 46285 |

The 10-letter palindrome **هثالثثلاثه** at pos 61467 and its overlapping
8-letter كـثالثثلاث **literally** encode "third [of] three" (*thālith al-thalātha*)
— the phrase occurs in Q 5:73 condemning Trinitarian formulations. The
rasm arrangement happens to be a palindrome: ث-ا-ل-ث-ث-ل-ا-ث.

**But this finding should be treated as curiosity-level**: when you search
for ℓ ≥ 7 palindromes in 310k characters of tajwid-consonant text with an
8-character alphabet of high-frequency letters, finding one that lines up
with "*thālith al-thalātha*" is expected by chance. The interesting result
is that the overall density is DEPLETED, not that one or two hits exist.

Also noteworthy: **وربكفكبرو** at pos 298022 (length 9) reads "and your Lord,
then-... greatness" — a palindromic encoding around "*rabbuka fa-kabbir*"
(Q 74:3 *wa-rabbaka fa-kabbir*). Another chance hit on a famous verse.

## Garden of forking paths (disclosed)

- Tajwīd normalization: hamzat al-waṣl deletion rule is the simplest
  compositional operationalization but NOT full tajwīd (idghām, iqlāb, iẓhār
  not modeled). A fuller tajwīd would erase more word-boundaries and likely
  yield MORE palindromes in observed AND null.
- ℓ ≥ 7 cutoff chosen a priori (coincidentally matches a common English-
  palindrome-finder cutoff); sensitivity at ℓ ≥ 5, 6, 8 not tested.
- Null 1 uses within-verse word-shuffle (~50 words per verse average) — may
  UNDERESTIMATE within-word palindrome preservation. Null 2 uses char-level
  bigram Markov — no word structure preserved.
- Two-tailed interpretation of depletion is POST-HOC. Pre-registered was
  upper-tail only.
- No correction for within-verse / cross-verse palindrome overlap in the
  per-verse count vs full-concat count (slight discrepancy: 67 vs 77).
- Bonferroni k = 3 inherited from pre-registration; the third test was
  verse-boundary clustering which was informally reported without formal z.

## Classical framing

No classical tradition predicts palindromic consonant structure in the Quran
at this scale — the hypothesis was pure-novelty. Had the test shown ENRICHMENT,
it would have been a genuinely new finding with no prior scholarly anchor. The
depletion finding is actually interesting in a different way: it suggests the
Quran's consonantal arrangement ACTIVELY AVOIDS palindromic repetition, or
(equivalently) its word-boundary structure produces fewer accidental palindromes
than random word-order would. Whether this reflects a compositional choice, a
Semitic root-morphology constraint (templatic morphology produces fewer
palindromes?), or something else is unclear without a classical Arabic prose
comparison.

A followup using Bukhari/Jahiz tajwid-normalized concatenation as a natural-
Arabic baseline would say whether the depletion is Quran-specific or is a
general feature of Arabic prose under these normalization rules.

## Limits

1. **Tajwīd is incomplete**. Only hamzat al-waṣl deletion is modeled. Full
   tajwīd (idghām shafawī, iqlāb, ghunna) would yield a different consonant
   sequence.
2. **Post-hoc two-tailed** reframing of a pre-registered one-tailed test is
   exploratory, not confirmatory. The depletion result should be cited as
   "observed effect, needs independent replication with pre-registered
   two-tailed null."
3. **Bigram null might under-represent palindromes** if Quranic prose has
   positive long-range autocorrelation that shuffling/Markov destroys.
4. **Word-shuffle null might over-represent palindromes** if word-internal
   letter-sequences include palindromic fragments that get preserved under
   shuffle.
5. **No Arabic prose comparison**. Without a Bukhari/Jahiz baseline, I cannot
   say whether Quranic depletion is ≠ general Arabic prose.
6. **Alphabet collapse to 28 letters after normalization** reduces alphabet
   size and INCREASES expected palindrome density under null. Quranic
   observed should be compared to Quran-normalized, which the two nulls do
   correctly.

## Verdict

**ORIGINAL ONE-TAILED HYPOTHESIS: FAIL.** The Quran does NOT contain more
cross-word phonetic palindromes of length ≥7 than word-shuffle or bigram-
Markov nulls predict.

**POST-HOC TWO-TAILED OBSERVATION: DEPLETION SIGNIFICANT.** The Quran
contains roughly half as many such palindromes as both nulls (observed 67
vs null 148 and 129; z = −6.38 and z = −4.73). Two-tailed p ≈ 10⁻¹⁰ / 10⁻⁶.
**The Quranic consonantal rhythm either actively avoids or structurally does
not produce palindromic substrings at this scale.** Treat as exploratory
pending replication with pre-registered two-tailed design and natural-Arabic
baseline comparison.

## Files

- Script: `scripts/h_new_16_palindromes.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-16-palindromes.json`
- Seed: 20260413
