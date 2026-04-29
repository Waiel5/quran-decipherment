# palindrome-hunter run 1 — Phase B novelty agent

**Date:** 2026-04-12
**Agent:** palindrome-hunter (Phase B novelty, Opus 4.6 1M)
**Charter:** hunt palindromes at every scale — words, roots, verses, sub-verses, surahs, whole Quran.
**Primary corpus:** `quran-text/quran-no-tashkeel.json` (anchor-locked, see methodology §8).
**Morphology:** `data/morphology/quranic-corpus-morphology-0.4.txt` (Leeds QAC v0.4, Buckwalter).
**Output:** `findings/phase-b-hypotheses/palindromes.md`
**Code:** `analysis/notebooks/palindrome_hunt.py`

## Decisions

1. Rules tuple locked as `(no-tashkeel, orthographic-token+real_words filter, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi, descriptive nulls)`. Committed before running the analysis.
2. "Letters only" normalization: strip every non-letter (tashkeel, recitation marks, punctuation) from each token before checking palindromicity, so the test is on the consonantal skeleton.
3. Category 1 palindrome test applied to *types*, not tokens — 14,870 distinct stripped word types, yielding 21 palindromic types. Token-count statistics reported alongside.
4. Category 4 uses the *first* ROOT tag from the Leeds QAC morphology line for each token position. Tokens without a root are dropped.
5. Category 6 set the reporting threshold at ≥ 7 letters after peeking at the shorter distribution (which was overwhelming — length-3 palindromes are everywhere). Flagged as a fork in the findings' Garden-of-Forking-Paths section.
6. Category 9 used both "longest contiguous palindromic subrun" (per-trial max) and "number of nontrivial subruns of length ≥ 5" (per-trial count). The second is more sensitive and is the one that produced the headline signal.
7. Category 10 antonym dictionary is small (~40 pairs), hand-rolled. Results are treated as exploratory only.

## Anchors sanity-checked

- Loader returned 114 surahs, 6236 verses ✓
- Letter count sequence has length 6236 ✓
- Morphology corpus contains ROOT tags; 1642 distinct roots (matches the existing root-cartography document) ✓

## Results in one paragraph

Nine of ten categories produce either chance-level or depleted counts.
One category (Category 9 — whole-Quran verse-letter-count palindromic
subruns) shows clear enrichment: 12 nontrivial palindromic subruns of
length ≥ 5 observed vs 0–3 under 100 within-Quran shuffles. Three of
those subruns are length 7, including the full opening of Sūrat al-Shams
(seven cosmic oaths, letter counts 12–14–15–15–15–14–12 mirroring around
the night-verse 91:4) and a 7-verse span of Sūrat al-Takwīr. These are
the hunt's strongest positive signals. The most elegant single case by
inspection is Q 33:3 whose five-root sequence `wkl-Alh-kfy-Alh-wkl`
is a perfect root-palindrome that semantically encodes the theological
content of the verse ("rely on Allah; Allah suffices").

## Base-rate computations performed

1. C1 per-position letter marginal null → expected 53 palindromic word types, observed 21 → DEPLETED by 2.5×.
2. C4 within-verse root-bag shuffle Monte Carlo (200 trials per verse, only for lengths ≤ 8) → expected 71, observed 73 → chance.
3. C6 within-verse letter shuffle (30 trials) → expected median 84 verses with palindromic substring ≥ 7, observed 19 → DEPLETED by ~4.4×.
4. C9 within-Quran letter-count shuffle (300 trials for longest subrun, 100 trials for count ≥ 5) → observed 12 nontrivial subruns vs shuffle max 3, observed max subrun length 7 vs shuffle max 7 in only 2/300 trials → ENRICHED (empirical p ≲ 0.01).

## Known gaps / what I did not do

- Did not run comparable-corpus null (§1.4) — no early hadith corpus
  mounted in this agent's workspace. This is the right test for C9 to
  settle whether "short Meccan oath sūras have palindromic letter-count
  structure" or "any short repetitive Arabic oath text has palindromic
  letter-count structure."
- Did not run Markov n-gram surrogate (§1.3).
- Did not pre-register. This entire run is exploratory.
- Did not search all length-2-or-greater palindromes across every lemma
  form (kept to consonantal skeleton only).
- Did not compute the semantic-chiasmus category under any model better
  than a ~40-entry antonym dictionary.
- Did not try maghribi abjad for C5 (C5 was 0 under mashriqi, expected
  0 under maghribi).

## Claims I promote to pre-registration

1. **C9 "verse-letter-count palindromic subruns are enriched in the
   Quran vs a within-Quran shuffle null"**, specifically:
   - Primary statistic: count of distinct nontrivial palindromic subruns
     of length ≥ 5 (expand-around-center, excluding constant runs) in
     the 6236-long sequence of per-verse letter counts.
   - Null: within-Quran shuffle, 10⁴ trials.
   - Secondary null: within-surah shuffle (controls for surah-length
     heterogeneity), 10⁴ trials.
   - Tertiary null: length-matched random blocks from a stripped early-
     hadith corpus, once mounted.
   - Hypothesis: observed count is in the upper 99.5% tail of the null
     distribution.
2. **Q 91:1–7 letter-count palindrome** is the specific sub-hit; it
   deserves a standalone pre-registration asking whether the seven oath
   verses of al-Shams form a palindromic block at a rate exceeded by
   fewer than 1% of shuffled surah-91 letter-counts.
3. **Sūrat al-Takwīr contains multiple nested palindromic subruns**
   (three in Q 81) — the question is whether any other 29-verse Quranic
   block contains three.

## Claims I explicitly do NOT promote

- C1 (21 word palindromes) is interesting as a *depletion* signal but
  makes no positive claim and needs no pre-reg.
- C4 root-palindromic verses are at chance in aggregate. The individual
  length-5 cases (33:3 and 73:15) are beautiful but not statistically
  anomalous — they go into the Phase C chiastic/ring-composition
  catalog, not the Phase B significance pipeline.
- C6 letter-substring palindromes are depleted in aggregate; the
  beautiful cases (thālith thalāth, kullun fī falakin, rabbaka fa-kabbir)
  are aesthetic observations, not stat claims.

## File receipts

- `analysis/notebooks/palindrome_hunt.py` — main analysis script
- `/tmp/palindrome-hunt/results.json` — structured intermediate dump (14 MB; ephemeral)
- `findings/phase-b-hypotheses/palindromes.md` — final deliverable
- this journal — `journal/palindrome-hunter-run-1.md`

## Runtime

- Category 1+2: ~2 s
- Category 3: ~1 s
- Category 4 (morphology load + scan): ~6 s
- Category 5: ~2 s
- Category 6: ~20 s
- Category 7: ~4 s
- Category 8: ~2 s
- Category 9 (within-Quran longest-pal-substring O(n²) on 6236): ~90 s
- Category 10 (english antonym scan): ~5 s
- Nulls (extra passes): ~6 min total
- End-to-end: ~8 min

## Single most surprising finding

**Sūrat al-Shams 1–7 form a perfect letter-count palindrome
[12, 14, 15, 15, 15, 14, 12] spanning the opening seven cosmic oaths.**
The Arabic rhetorical trope of oath-series (qasam) is famous in these
short Meccan surahs; what the hunt newly shows is that al-Shams
encodes that trope *metrically* as a 7-element integer palindrome whose
axis is the night-verse (91:4). The probability of seeing a length-7
palindromic subrun anywhere in a shuffled 6236-long Quran is ~0.7% under
our shuffle null, and observing three such subruns (plus nine shorter
ones) is at p < 0.01.

## Runner-up

**Q 33:3 — `وَتَوَكَّلْ عَلَى اللَّهِ وَكَفَىٰ بِاللَّهِ وَكِيلًا` — has the five-root
palindromic structure `wkl·Alh·kfy·Alh·wkl`.** The verb "entrust" and
the divine name mirror across the axis root "suffices." This is
classical *tarṣīʿ* (interior rhyme / return-the-end-onto-the-beginning)
at the root level, not the word level, which is unusual because *tarṣīʿ*
normally applies to word endings. The root-level realization means the
chiasm survives inflectional variation of the individual words — a more
abstract symmetry than classical Arabic rhetorical nomenclature usually
captures.
