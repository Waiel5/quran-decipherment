---
surah: 37
test_id: Q037-F-01
title: Corpus-share of the *salāmun ʿalā [PROPHET-NAME]* construction — Q 37 fingerprint test
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
bonferroni_k: 2
bonferroni_family: Q037-F-01-salam-ala-prophet
alpha_bon: 0.025
---

# Q037-F-01 — Pre-registration: *salāmun ʿalā [PROPHET-NAME]* fingerprint test

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** The Quranic phrase-construction *salāmun ʿalā [NAMED-PROPHET]* — i.e. the literal string `سلام على` followed within the same verse by a named prophet token — has **at least 3 corpus instances inside Q 37** (mid-Meccan oath-prophet-cycle surah).

**H1b (one-tailed, locked direction):** Q 37 holds the corpus-MAX share of *salāmun ʿalā [PROPHET]* instances; operationalized as **Q 37 contains ≥75% of all corpus instances** of the construction.

**H0 (joint):** Q 37 has < 3 instances OR Q 37 holds < 75% of corpus instances.

**Direction:** Q 37 = corpus-MAX (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Construction-pattern**: regex `\bسلام على\b` (literal, with word-boundary).
- **Prophet-restriction**: a **valid hit** is one where the verse containing `سلام على` mentions a known prophet from the canonical 25-prophet list within the same verse, OR ends in a prophet-name immediately. The construction *wa-l-salām/wa-salām* variants (e.g., Q 27:59 *wa-salām ʿalā ʿibādihi al-ladhīna ṣṭafā*) are EXCLUDED from the primary count because the addressee is not a named prophet.
- **Equivalent-form note**: Q 19:15, Q 19:33 use *wa-salām ʿalayhi* (with pronominal suffix, not a free *ʿalā [name]*); Q 19:47 uses *salām ʿalayka*; these are EXCLUDED.

## 3. Test statistic

- N_total = total corpus instances of *salāmun ʿalā [PROPHET-NAME]* by the operational definition.
- N_q37 = count restricted to Q 37.
- share_q37 = N_q37 / N_total.

## 4. Permutation null

The "corpus instance share" is best assessed against a structurally-meaningful null:

**Null model A (length-weighted):** Under the null, the N_total construction-tokens are distributed across surahs proportional to surah word-length (longer surahs ⇒ more chance to contain the rare phrase). p-value = probability that a random length-weighted draw of N_total tokens places ≥ N_q37 in Q 37.

**Null model B (uniform-surah):** N_total tokens distributed uniformly over 114 surahs.

Both nulls reported; primary inference uses A. n_perm = 10000, seed = 20260508.

## 5. Success / Failure

- **CONFIRMED**: H1a and H1b both pass; permutation p (length-weighted null A) ≤ α_bon = 0.025.
- **DIRECTIONAL**: H1a passes (Q 37 has ≥3 instances) but H1b fails OR p > α_bon.
- **NULL**: H1a fails (Q 37 has < 3 instances).
- **Pre-commit violation**: Q 37 has 0 instances of the construction.

## 6. Honest limits known a priori

- The construction has only N_total ≈ 4 corpus instances (extremely rare); the test is essentially asking whether a 4-element distribution is concentrated on one surah. Permutation null is non-trivial because length-weighting makes the long-surah baseline non-uniform.
- The phrase-form *wa-salām ʿalā al-mursalīn* (Q 37:181) is a near-twin construction (with prefix و and a non-named-prophet addressee, "the messengers" plural). Sensitivity check: include/exclude this borderline case.
- The pre-reg discloses post-hoc origin: the corpus-anchor extraction during pre-flight observed all 4 instances in Q 37 BEFORE the formal pre-reg lock. Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol":
  - Single-test α=0.05 cap unless extreme p (e.g., < 1e-5) survives any conceivable Bonferroni.
  - Verdict ceiling = **PASS-DIRECTED** (NOT CONFIRMED) until INDEPENDENT REPLICATION.
  - This pre-reg is the formal lock; the direction is positive a priori from the brief (the brief itself pre-commits "≥3 instances are in Q 37").

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (length-weighted null A + uniform null B). α_bon = 0.025.

## 9. Coordination

This is a Q 37-specific construction-fingerprint test. Q 38 specialist did NOT run a salām-related test. No duplication.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q037_F_01_salam_ala_prophet.py`, verified at runtime.
