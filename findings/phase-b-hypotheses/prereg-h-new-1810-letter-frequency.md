---
id: H-NEW-1810
title: Corpus-wide Arabic letter (grapheme) frequency distribution + muqaṭṭāʿat-14 overlap audit
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: H-NEW-1810-letter-frequency (3 pre-registered tests)
alpha_bon: 0.0167
direction_of_effect:
  T1: top-3 letters' summed relative frequency > 25% of all alphabetic-letter graphemes (NON-UNIFORM — direction LOCKED HIGH).
  T2: muqaṭṭāʿat-14 set ⊆ top-14 letters by corpus-wide frequency (al-Suyūṭī Itqān nawʿ 6 al-ḥurūf al-muqaṭṭaʿa observation that the 14 cited letters are the 14 most frequent of Arabic) — EXACT-SET-EQUALITY direction LOCKED.
  T3: muqaṭṭāʿat-14 letters' summed relative frequency is GREATER than 14/28 = 0.50 (half the alphabet, the chance baseline if frequency were uniform across letters); one-tailed.
origin: foundational empirical anchor missing from project as of 2026-05-09 PM. al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 6 (al-ḥurūf al-muqaṭṭaʿa) reports the classical observation, attributed to multiple earlier authorities, that the 14 distinct letters appearing in muqaṭṭāʿat opener-verses are precisely "half of the Arabic alphabet" and represent the high-frequency letters of the language. Modern frequency-table on `data/baseline-corpora/letter-freqs.csv` exists but has never been audited against the al-Suyūṭī overlap claim or rank-locked. This pre-reg locks the corpus-wide frequency table, the top-14 ranking, and the overlap test.
verdict_ceiling: PASS-DIRECTED (3 pre-registered tests; INDEPENDENT REPLICATION required for CONFIRMED promotion).
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token (irrelevant — counting graphemes)
  letter_definition: graphemes (28-letter Arabic alphabet; hamza-bearers ء/أ/إ/ؤ/ئ and ا/آ are normalized — see below)
  basmala_policy: counted-only-in-surah-1 (so basmala graphemes contribute exactly once to corpus totals via Q 1:1)
  verse_numbering: hafs-kufan
  source_file: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  text_normalization:
    - extract every Unicode codepoint in the verses' `text` field
    - filter to the 28 base-letter Arabic alphabet codepoints PLUS hamza-bearers PLUS ة and ى variants
    - hamza-bearer NORMALIZATION (locked BEFORE running): أ/إ/آ → ا; ؤ → و; ئ → ي; standalone ء → ء (its own letter, counted but reported separately); ة → ت for the 28-letter mapping (ḥarf-tāʾ-marbūṭa is orthographically tāʾ); ى → ي (alif-maqṣūra → yāʾ for the 28-letter mapping)
    - this collapses Arabic Unicode codepoints to the canonical 28-letter alphabet: ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي
    - standalone ء (hamza) is tracked separately for transparency but NOT counted as one of the 28 letters (it is a diacritic-marker in classical Arabic alphabetic counting per al-Suyūṭī Itqān nawʿ 6)
  null_model_for_T2: hypergeometric over the 28-letter alphabet — the probability that a uniformly-random 14-subset of the 28 letters exactly matches the muqaṭṭāʿat-14 set is 1 / C(28, 14) = 1 / 40,116,600 ≈ 2.49e-8; for the WEAKER test of overlap ≥ k, hypergeometric P(X ≥ k | population 28, success-states 14, sample 14)
  muqattaat_14_set: ا ل م ص ر ك ه ي ع ط س ح ق ن (per al-Suyūṭī Itqān nawʿ 6; also cited in al-Zarkashī Burhān; the 14 distinct letters across the 29 muqaṭṭāʿat opener-verses of {Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68})
---

# H-NEW-1810 pre-registration — corpus-wide Arabic letter frequency + muqaṭṭāʿat-14 overlap

## Hypothesis (3 pre-registered tests)

**T1 — Non-uniformity**: The relative frequency of the 28 Arabic letters in the no-tashkeel Hafs-Kūfan corpus is NOT uniform. Specifically, the top-3 letters' summed relative frequency exceeds 0.25 (chance expectation under uniform = 3/28 ≈ 0.107). Direction LOCKED HIGH.

**T2 — al-Suyūṭī overlap claim (the strong form)**: The muqaṭṭāʿat-14 set ({ا ل م ص ر ك ه ي ع ط س ح ق ن}) is EXACTLY the top-14 letters by corpus-wide frequency. Test statistic: overlap = |muqaṭṭāʿat-14 ∩ top-14-by-frequency|. Direction LOCKED at overlap = 14 (perfect set-identity).

Reporting also the WEAKER form: how many overlap (k of 14) and the hypergeometric one-tailed p-value P(X ≥ k_observed) under uniformly-random 14-subset selection from 28 letters.

**T3 — Muqaṭṭāʿat-14 summed frequency**: The summed relative frequency of the 14 muqaṭṭāʿat letters exceeds 0.50 (= 14/28, the chance baseline). Direction LOCKED HIGH.

## Pre-committed predictions (the bets)

- T1 prediction: corpus is HIGHLY non-uniform; top-3 = {ا, ل, م} per `data/baseline-corpora/letter-freqs.csv` quran-no-tashkeel row; expected sum ≈ 0.13166 (ا) + 0.11548 (ل) + 0.08246 (ن) ≈ 0.33 — WAIT — this would be top-3 by raw codepoint; under our locked normalization (أ/إ/آ → ا; ة → ت; ى → ي) the top-3 will likely re-rank to {ا, ل, م} or {ا, ل, ن} depending on alif-variant absorption.
- T2 prediction: STRONG-FORM PASS — overlap = 14 (exact set identity), the classical al-Suyūṭī claim verifies; muqaṭṭāʿat-14 = top-14 letters by corpus-wide frequency.
- T3 prediction: muqaṭṭāʿat-14 summed frequency > 0.85 (since the 14 absent letters are all low-frequency).

If T2-strong FAILS, the WEAKER hypergeometric form (overlap k of 14, p one-tailed) is the reported finding.

## Computation

```
1. Load /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json.
2. For each verse: iterate Unicode codepoints; apply locked normalization rules.
3. Aggregate counts across all 114 surahs (basmala in Q 1:1 already present in the file, counted as locked).
4. Compute relative frequencies on the 28-letter base alphabet.
5. Rank letters descending; capture top-14, top-3.
6. Compute overlap with muqaṭṭāʿat-14 set; compute hypergeometric p.
7. Compute muqaṭṭāʿat-14 summed relative frequency.
8. Report T1, T2, T3 verdicts vs locked thresholds.
```

## Decision rule

- T1 PASS if (top-3 sum) > 0.25 AND direction matches lock (HIGH).
- T2 STRONG-FORM PASS if overlap = 14 exactly.
- T2 WEAK-FORM PASS-DIRECTED if hypergeometric one-tailed p < α_bon (0.0167); WEAK-FORM NULL otherwise.
- T3 PASS if (muqaṭṭāʿat-14 summed freq) > 0.50 AND direction matches lock (HIGH).
- Any direction reversal = pre-commit violation per Protocol §1.8.

## What would falsify the al-Suyūṭī claim

- T2-strong FAIL: overlap < 14. A single letter of the 14 muqaṭṭāʿat set being outside the top-14-by-frequency is sufficient to falsify the EXACT-SET form of the al-Suyūṭī claim. Examples of single letters that could displace the set: if any of {و, ف, ت, ب, د} (frequent letters NOT in muqaṭṭāʿat-14) outranks one of {ص, ط, ح, ق, ع} (rarer letters that ARE in muqaṭṭāʿat-14), the strong claim fails.
- Even ONE such displacement makes the al-Suyūṭī "the 14 are the high-frequency letters" claim FALSE in its strict reading.

## Cross-corpus controls (reported but not pre-committed)

For descriptive comparison only, we will also load `data/baseline-corpora/letter-freqs.csv` (pre-computed by prior session) and report the analogous top-14 + overlap for: bukhari-noquran, sira-ibn-hisham, jahiz-hayawan, mutanabbi-diwan, and the muʿallaqāt average. This is descriptive — NOT a pre-registered hypothesis test — and reported for context.

## Honest limits

1. The normalization rule (أ → ا, ة → ت, ى → ي, ؤ → و, ئ → ي) is one possible canonical-28 mapping; alternative mappings (e.g., keeping ة separate; keeping ى separate; keeping hamza-bearers separate) would yield slightly different rankings. The locked mapping follows classical Arabic alphabetic-letter convention as cited in al-Suyūṭī Itqān nawʿ 6.
2. al-Suyūṭī's claim is qualitative ("the high-frequency letters"); reading it as the strict top-14 set-equality is the strongest empirical instantiation. A looser reading (e.g., "predominantly high-frequency") could survive even if 1-2 letters are displaced.
3. Letter frequency is rules-tuple-sensitive: tashkeel-handling, hamza-bearer treatment, ة/ى policies all matter. The locked normalization is documented; deviations require their own pre-reg.
4. The classical claim does not specify the corpus on which the frequency assertion holds — al-Suyūṭī likely had a generalist intuition about Arabic-language frequency, not specifically Qurʾānic frequency. We test it on the Qurʾān corpus (the natural target) AND descriptively on cross-corpus baselines (bukhari, poetry).

## Cross-references

- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 6 — al-ḥurūf al-muqaṭṭaʿa
- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, kitāb 23 — muqaṭṭaʿāt
- `data/baseline-corpora/letter-freqs.csv` — pre-computed letter-frequency baseline (raw, unnormalized)
- H-NEW-1730 — al-Khalifa muqaṭṭāʿat letter-count audit (MIXED)
- H-NEW-1600, H-NEW-1530, H-NEW-1720, H-NEW-1740 — Code-19 falsification series
- H-NEW-113 letter-position; H-NEW-151 single-letter-muq char-4gram; H-NEW-600 letter families; H-NEW-88 letter-set predictor

## Seed and reproducibility

- Seed: `20260509` (used for any randomization; this test is largely deterministic, but the seed is locked for any future replication that introduces stochastic elements).
- All numerical outputs to be saved to `findings/phase-b-hypotheses/csv/h-new-1810.json`.
- Run script: `findings/phase-b-hypotheses/scripts/h-new-1810.py`.
- Pre-reg SHA: locked at first commit; embedded in run script; verified at runtime.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
