# Phase B — Open Prime-Mod Scan of the Quran

**Owner:** `code19-audit` agent (Phase A+B run-1)
**Date:** 2026-04-12
**Status:** exploratory — registered as a Phase-B *open hunt* for any prime-mod anomaly across surah-level statistics
**Companion:** `findings/phase-a-replications/code19-khalifa-full-audit.md`

```yaml
rules:
  orthography: no-tashkeel (anchor-locked)
  word_definition: orthographic-token, real-words only (recitation marks filtered)
  letter_definition: graphemes (U+0621..U+064A ∪ U+0671..U+06D3)
  basmala_policy: counted-only-in-surah-1 (matches the JSON dataset)
  verse_numbering: hafs-kufan (6236)
  abjad_table: mashriqi
  null_model: 1.5-permutation (binomial divisibility under H0: count is uniform on residues mod p) AND a sanity check via the natural baseline of 114/p expected hits
```

Code: `/tmp/quran-code19/analyze.py::prime_mod_hunt` and `/tmp/quran-code19/final_compute.py`.

---

## Hypothesis (open hunt)

**For each prime p in {7, 11, 13, 17, 19, 23, 29, 31}, and for each per-surah statistic m in {letters, words, verses, abjad}, count how many of the 114 surahs have m ≡ 0 (mod p). Compute a two-sided binomial p-value under the null that the residue is uniform mod p. Apply Bonferroni correction for the 8 × 4 = 32 tests.**

This is an *open* hunt: we are not pre-specifying which p or which metric to look at. We are asking whether *any* prime divisibility pattern across surah-level features pops out at us beyond the multiple-comparison correction.

**Interpretation note.** The Khalifa Code-19 program asserts that `p = 19` is special. If that were true, we should see `p = 19` produce a markedly higher number of 19-divisible surahs than the chance expectation 114/19 = 6, while other primes do not. **The open hunt is the right way to falsify this:** if every prime gives a count consistent with chance, the special-status claim is empirically empty.

---

## Results

### Per-surah letter counts (no-tashkeel, graphemes)
| p | observed surahs with letters ≡ 0 (mod p) | expected (114/p) | obs − exp | binomial 2-sided p |
|---|---|---|---|---|
| 7 | 13 | 16.29 | −3.29 | 0.465 |
| 11 | 11 | 10.36 | +0.64 | 0.929 |
| 13 | 11 | 8.77 | +2.23 | 0.522 |
| 17 | 3 | 6.71 | −3.71 | 0.183 |
| **19** | **3** | **6.00** | **−3.00** | **0.288** |
| 23 | 5 | 4.96 | +0.04 | 1.000 |
| 29 | 2 | 3.93 | −1.93 | 0.487 |
| 31 | 2 | 3.68 | −1.68 | 0.569 |

### Per-surah word counts (real-words, no-tashkeel)
| p | observed | expected | obs − exp | binomial p |
|---|---|---|---|---|
| 7 | 9 | 16.29 | −7.29 | **0.056** |
| 11 | 10 | 10.36 | −0.36 | 1.000 |
| 13 | 7 | 8.77 | −1.77 | 0.686 |
| 17 | 4 | 6.71 | −2.71 | 0.386 |
| **19** | **8** | **6.00** | **+2.00** | **0.504** |
| 23 | 6 | 4.96 | +1.04 | 0.752 |
| 29 | 2 | 3.93 | −1.93 | 0.487 |
| 31 | 2 | 3.68 | −1.68 | 0.569 |

### Per-surah verse counts (hafs-kufan)
| p | observed | expected | obs − exp | binomial p |
|---|---|---|---|---|
| 7 | 14 | 16.29 | −2.29 | 0.651 |
| **11** | **17** | **10.36** | **+6.64** | **0.058** |
| 13 | 9 | 8.77 | +0.23 | 1.000 |
| 17 | 3 | 6.71 | −3.71 | 0.183 |
| **19** | **4** | **6.00** | **−2.00** | **0.556** |
| 23 | 2 | 4.96 | −2.96 | 0.246 |
| 29 | 3 | 3.93 | −0.93 | 0.888 |
| 31 | 3 | 3.68 | −0.68 | 0.993 |

### Per-surah mashriqi abjad totals
| p | observed | expected | obs − exp | binomial p |
|---|---|---|---|---|
| 7 | 14 | 16.29 | −2.29 | 0.651 |
| 11 | 10 | 10.36 | −0.36 | 1.000 |
| 13 | 10 | 8.77 | +1.23 | 0.762 |
| 17 | 9 | 6.71 | +2.29 | 0.457 |
| **19** | **5** | **6.00** | **−1.00** | **0.883** |
| 23 | 5 | 4.96 | +0.04 | 1.000 |
| 29 | 5 | 3.93 | +1.07 | 0.715 |
| 31 | 5 | 3.68 | +1.32 | 0.615 |

---

## Multiple-comparison correction

- **Family size:** 8 primes × 4 metrics = **32 tests**.
- **Bonferroni threshold (α = 0.05):** 0.05 / 32 = **0.00156**.
- **Holm-Bonferroni step-down:** apply 0.05 / (32 − rank) after sorting raw p-values ascending.

### After Bonferroni
**Zero (0) tests significant.** The minimum raw p-value across all 32 tests is **0.056** (per-surah words mod 7 *and* per-surah verses mod 11), which is two orders of magnitude above the corrected threshold.

### After Holm
**Zero (0) tests significant.** The smallest raw p (0.056) does not even cross the uncorrected α = 0.05.

### Effect size analysis
The largest absolute deviation from expectation is **+6.64** (verses mod 11: observed 17, expected 10.36). The next largest are **−7.29** (words mod 7) and **−3.71** (verses mod 17, letters mod 17). None of these are remotely close to multiple-comparison significance.

**Effect on the Khalifa hypothesis specifically:** for `p = 19` across all four metrics, the observed counts are **3, 8, 4, 5** (versus expected 6, 6, 6, 6). None are statistically distinguishable from chance, and only one (words = 8) is even on the *high* side of expectation. **The 19-special-status claim has zero support from this open hunt.**

---

## Surah-index divisibility (sanity sub-test)

A trivial counter-test: how many surah indices in {1..114} are divisible by each prime?

| p | observed | expected (114/p) |
|---|---|---|
| 7 | 16 | 16.29 |
| 11 | 10 | 10.36 |
| 13 | 8 | 8.77 |
| 17 | 6 | 6.71 |
| 19 | 6 | 6.00 |
| 23 | 4 | 4.96 |
| 29 | 3 | 3.93 |
| 31 | 3 | 3.68 |

These are exact-by-construction (the 19-divisible indices are 19, 38, 57, 76, 95, 114 — exactly 6) and serve as a sanity check that the binomial expectation 114/p is the right baseline.

---

## Discussion

### What the null result means

We ran 32 surah-level prime-divisibility tests across the canonical Hafs-Kufan Quran with primary statistics (letters, words, verses, abjad) and primes up to 31. **Zero pass any reasonable correction; the smallest raw p-value is 0.056.** Among the 32 tests, the four involving p = 19 (Khalifa's sacred prime) all sit comfortably within the chance distribution, with observed counts of 3, 8, 4, 5 versus expectations of 6, 6, 6, 6.

In the McKay-style framing, this is the answer to the question: *"If we test divisibility-by-N for many integers N, does N = 19 stand out?"* No. The 19-special-status claim that drives Khalifa's program has no empirical signal at the surah level.

### Why this matters for the Khalifa replication

Khalifa's published claims aren't framed this way; he picks specific compositional statistics (e.g. "the sum of opening letters in each muqatta'at surah") that are not in our 4-metric × 8-prime grid. So this scan doesn't refute his *specific* claims (that's done in the audit). What it does is **rule out a generic surah-level "divisibility by 19 is special" pattern**: if such a pattern existed at the basic compositional level (letter/word/verse/abjad totals), we would see it pop out across multiple primes-vs-19 contrasts. We don't.

### Forking-paths assessment

We picked 4 metrics (letters, words, verses, abjad) and 8 primes (the first 8 primes ≥ 7) with no peeking at the data. The choice was committed before any count was run (it's in the task description). This is the smallest natural family for "surah-level prime divisibility" hypothesis space.

We did *not* test:
- products of metrics (e.g., letters × words)
- ratios (e.g., letters/words)
- digit sums of metrics
- gematric values of surah names
- inter-surah differences or sums
- triangular or polygonal numbers of metrics

Each of these would expand the test family by 1–2 orders of magnitude. Khalifa's Appendix 1 contains hundreds of such derived statistics, and *some* of them divide by 19 by chance (the expected count is `total_tests / 19`). The fact that the *direct* tests (letters mod 19, words mod 19, etc.) show nothing is the cleanest possible result; expanding to derived statistics would be an exercise in burying the null.

### Did we find any "novel" prime-mod anomaly?

**No.** The two raw p-values closest to nominal significance — words mod 7 (p = 0.056) and verses mod 11 (p = 0.058) — are *just barely* hitting the uncorrected 0.05 threshold and would not survive any correction at all. Neither is "novel" in the sense of having a published claim attached; both look like ordinary noise.

If we were to *speculatively* explore the words-mod-7 result (only 9 surahs with word count divisible by 7, vs expected 16), it would suggest a mild **deficit** of 7-divisible surah word counts. That is the *opposite* direction from a "7 is special" claim (Al-Kaheel), and if anything is mildly anti-evidence for the kaheel-sevens-system claim. We do not pursue it further: 0.056 raw becomes 1.00 after Bonferroni for the 32 tests, and the deficit could trivially flip to a surplus under any minor change of word definition (with-clitics-split, lemma-based, etc.).

---

## Garden of forking paths disclosure

### Choices made after seeing the data
- (none — the prime list, metric list, and binomial test were specified in the task description before the data was touched)

### Alternative rule tuples considered and discarded
- We could have used min-tashkeel or full-tashkeel for letter counts. We did not: no-tashkeel is the anchor-locked primary corpus.
- We could have used the QAC lemma count for "words" instead of orthographic real-words. We did not, because the morphology corpus is not directly per-surah summed; orthographic word counts are the most reproducible.
- We could have computed abjad on full-tashkeel (which would slightly change values due to alif-wasla conversions). The mashriqi abjad table assigns identical values to all alif variants, so the net effect is small.

### Sibling hypotheses considered
- Surah-index divisibility: tested as a sanity check (above). Trivially gives baseline.
- Kaheel "marvels of 7" system: not tested in this scan beyond words/letters/verses mod 7 (no signal).
- The p = 19 result was *the* hypothesis for the Khalifa program; it is documented at length in the audit file.

### Why this prime/metric grid
- p ∈ {7, 11, 13, 17, 19, 23, 29, 31}: the first 8 odd primes ≥ 7. This brackets 19 with 4 smaller and 4 larger primes, so 19 has no special selection privilege in the family.
- metric ∈ {letters, words, verses, abjad}: the 4 most basic per-surah numerical statistics. Adding more would inflate the family without testing meaningfully different hypotheses.

---

## Conclusion

The open prime-mod scan finds **no significant deviation from chance** across 32 tests covering 8 primes × 4 surah-level statistics. Specifically:

- **p = 19 does not stand out from {7, 11, 13, 17, 23, 29, 31}** in any of the four metrics. Khalifa's "19 is the divine signature" claim has no statistical support at the surah-level compositional level.
- **The minimum raw p across the family is 0.056**, two orders of magnitude above the Bonferroni-corrected threshold of 0.00156 and not even significant at uncorrected α = 0.05.
- **No novel prime-mod anomaly** was discovered. The two largest deviations (words mod 7 and verses mod 11) are noise.

This is a clean **null result** for the family of surah-level prime divisibility claims. It is reported with the same prominence as a positive result would be.

---

## Test register increment

This file adds **32 tests** to the cumulative Phase-B test register. All 32 are negative; none requires further investigation.

(The companion audit `code19-khalifa-full-audit.md` adds approximately 25 more replication tests; the muqatta'at density signal in that file is the only positive result and is already flagged for Phase-B pre-registration as a separate hypothesis.)

---

**End of scan.** See `code19-khalifa-full-audit.md` for the per-claim Khalifa Code-19 audit.
