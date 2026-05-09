---
surah: 60
test_id: Q060-F-02
title: Q 60:12 women's bayʿa formula — corpus-EXACT structure test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q060-F-02-womens-bayca
alpha_bon: 0.025
---

# Q060-F-02 — Pre-registration: Women's bayʿa formula corpus-EXACT structure

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** The feminine-plural verbal form *yubāyiʿna+ka* ("they (fem.pl.) pledge to you") with surface-string `يبايعنك` occurs in **EXACTLY 1 verse** corpus-wide, and that verse is Q 60:12.

**H1b (one-tailed, locked direction):** The chained feminine-plural negative-imperative construction `(و)لا ي/ت...ن` with **≥4 instances within a single verse** occurs in **EXACTLY 1 verse** corpus-wide, and that verse is Q 60:12.

**H0 (joint):** Either form has ≥2 corpus instances OR neither form has Q 60:12 as the locus.

**Direction:** Q 60:12 = corpus-EXACT for both axes (LOCKED).

## 2. Operational definition

### 2a. Test (a): yubāyiʿna+ka surface-string match

- **Source text**: `quran-text/quran-no-tashkeel.json`.
- **Pattern**: literal regex `يبايعنك` (no diacritics, no word-boundary needed since the form is morphologically distinctive).
- **Counting rule**: count distinct verses where the surface-string occurs at least once.
- **Sensitivity**: report the masculine-plural twin `يبايعونك` count separately as a comparator.

### 2b. Test (b): ≥4-element chain of feminine-plural negative-imperative in single verse

- **Pattern element**: regex `(?:لا|ولا)\s+(?:يشركن|يسرقن|يزنين|يقتلن|يأتين|يعصينك|يعصين|يحفظن|يبدين|يضربن|يرين|يطمث|يحلل|يكتمن|يفترين|يخلطن)` — a closed list of feminine-plural verb-forms ending in -na with prefixed (wa-)lā.
- **Counting rule**: count chained-element matches per verse; verses with ≥4 are the test set.
- **Sensitivity**: report verses with 2-3 chains as comparators.

## 3. Test statistic

For each test, the count of corpus-EXACT verses matching the pattern.

## 4. Permutation null

The "corpus-EXACT to one verse" null is degenerate (the construction either occurs in N verses or not). The empirical claim is a discrete count, NOT a permutation-statistic. Documented limit per HONEST-LIMITS-LEDGER §rare-construction:

- For genuinely-corpus-EXACT constructions (n=1 or 2 corpus-wide), the only meaningful null is the **a priori probability of co-location**. Under length-weighted random distribution of N=1 occurrence across the corpus, Q 60 (377 words / 77,797 total = 0.485%) is the expected location with probability 0.00485. So observing the construction at Q 60:12 by chance has p = 0.485% under length-weighted null.

## 5. Decision rule

- **CORPUS-EXACT (verdict)**: Observed count = 1 AND the verse is Q 60:12. This is a state-of-the-corpus claim, not a probability test. The empirical claim stands as a structural fingerprint.
- **CONFIRMED with permutation-null discount**: under length-weighted null, p_lengthweighted ≤ α_bon = 0.025.
- **NULL**: observed count > 1 (formula appears elsewhere) — direction reversed.

## 6. Pre-commit violation handling

If observed count is 0 (formula doesn't appear) OR ≥2 (not corpus-exact), publish as direction-reversed NULL.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, regex-fixed-pattern, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (two independent tests: yubāyiʿna form + chained-prohibitions). α_bon = 0.025 each.

## 9. Honest limits known a priori

- Both axes are RARE-CONSTRUCTION fingerprint tests, not statistical-power tests. The empirical interest is in the *uniqueness* itself, not in beating a noise floor.
- Pre-flight observation: brief disclosed Q 60:12 has the women's bayʿa formula. The pre-reg disclosure: this is post-hoc-noticed at the SURAH-targeting level (the brief named the test). Per discipline §post-hoc protocol, verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION on a distinct data dimension. We treat the empirical-corpus-uniqueness as fact-of-the-corpus (not a probabilistic claim) and the length-weighted null p as an independent secondary check.

## 10. Coordination

This test does not duplicate any other Q 60 specialist test.

## 11. SHA256 lock

Computed at completion-time, embedded into result JSON.
