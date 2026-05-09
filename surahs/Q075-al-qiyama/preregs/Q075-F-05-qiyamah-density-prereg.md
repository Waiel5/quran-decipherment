---
surah: 75
test_id: Q075-F-05
title: *qiyāmah* surface-form density — Q 75 corpus-rank
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q075-F-05-qiyamah-density
alpha_bon: 0.025
direction: Locked — Q 75 holds CORPUS-MAX density of *al-qiyāmah* surface-form per 1000 words (an explicit name-token-density iʿjāz check)
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q075-F-05 — Pre-registration: *qiyāmah* surface-form density

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** Q 75 holds the **corpus-MAX density** of the surface-form القيامة (*al-qiyāmah*) per 1000 words. Pre-committed: rank 1 of 114 by density.

**H1b (one-tailed, locked direction):** Q 75's density is at least 2× the next-highest surah's density.

**H0:** Q 75 is not rank 1, OR Q 75/next < 2.

**Direction:** Q 75 = corpus-MAX (LOCKED).

## 2. Operational definition

### Source text
`quran-text/quran-no-tashkeel.json` (rules-tuple default).

### Surface-form
- Token: القيامة (no-tashkeel form, with the `al-` definite article).
- Pre-commit acknowledgement: this is the surface-form, not the q-y-m root. The root q-y-m has many additional surface-forms (قام, يقوم, إقامة, مستقيم, etc.) but the QIYĀMA-ESCHATOLOGY-DAY usage is dominantly the surface-form القيامة.

### Test statistic
For each of 114 surahs:
- count_s = number of occurrences of القيامة in surah s.
- words_s = total word-count (no-tashkeel, ornament-stripped).
- density_s = 1000 * count_s / words_s.

Rank surahs by density_s descending. Ties broken by raw count.

### Pre-committed prediction
- rank(Q 75) = 1.
- density_Q75 > 2 × density_rank2.

## 3. Permutation null

Cell A (rank): no perm null needed; rank is a discrete corpus property.

Cell B (2× factor): bootstrap CI on density_Q75 / density_rank2 ratio? Not needed for surface-count test — count is deterministic. The 2× pre-committed threshold is a substantive prediction about Q 75's distinctness, not a probabilistic test.

## 4. Test cells

- **Cell A**: rank check.
- **Cell B**: 2× factor check.

## 5. Success / Failure

- **CONFIRMED / VINDICATED**: Both cells pass.
- **PASS-DIRECTED**: Cell A passes (rank 1) but Cell B fails (factor < 2).
- **NULL**: Cell A fails.

## 6. Honest limits

- This is a deliberately-narrow surface-form test. The full root q-y-m would tell a different story — many surahs have many forms.
- The prediction of rank 1 is strongly motivated by the surah's NAMING after this very token. The test is a sanity-check: does the surah named *al-Qiyāma* actually lead the corpus on its name-token density? The answer is empirically interesting only if it's NO (refuting the naming-vindication assumption); a YES answer is expected.
- Pre-commit acknowledgement: the brief-author has noted that "Q 75 al-Qiyāma control density = 66.67/1000" appears in the MASTER-FINDINGS-LEDGER §10.7 table for an UNRELATED test (eschatology-formula 8-pattern density across yawm/sāʿa/ṣūr/qiyāma/baʿth/nār/janna/m-w-t roots). That figure is a multi-pattern composite and is NOT comparable to this Q075-F-05 single-surface-form test. The Q075-F-05 prediction (rank 1, factor 2×) is for the surface-form القيامة alone.

## 7. Rules-tuple

Default.

## 8. Bonferroni

k = 2. α_bon = 0.025.

## 9. Coordination

No prior surface-form-density test for *al-qiyāmah* alone has been pre-registered. The Q036-F-04 8-pattern eschatology composite (NULL for Q 36) is a different test.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q075_F_05_qiyamah_density.py`, verified at runtime.
