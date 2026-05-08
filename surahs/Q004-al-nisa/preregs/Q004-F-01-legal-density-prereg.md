---
finding_id: Q004-F-01
title: Q 4 al-Nisāʾ legal-density rank in the corpus
status: PRE-REGISTERED
date: 2026-05-07
specialist: Q004-al-nisa-specialist
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q004-novel-tests-2026-05-07
alpha_bon: 0.01
direction: HIGHER (Q 4 in top-3 corpus-wide on legal-imperative + inheritance-fraction density per 100 words)
acceptance_window: rank ≤ 3 of 114 on the composite "legal-density-per-100-words" score
---

# Q004-F-01 — Legal-density rank: pre-registration

## Hypothesis

Q 4 al-Nisāʾ is, per al-Suyūṭī (*al-Itqān*, nawʿ on āyāt al-aḥkām) and al-Zarkashī (*al-Burhān*), the corpus's most legally dense surah — the locus of maximal *iʿjāz al-tashrīʿī* (juridical-iʿjāz). The classical claim is qualitative; this test makes it quantitative.

## Operationalisation

- Text: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (Hafs-Kufan; Quran is one text).
- Rules-tuple: `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.
- For each of all 114 surahs, compute two RAW counts and the composite score:

  (a) Legal-imperative tokens — substring-match in the no-tashkeel text against this fixed lexicon (locked here):
      `["لا تأكلوا", "لا تقتلوا", "لا تنكحوا", "لا تقربوا", "كتب عليكم", "كتب عليكم", "حرمت عليكم", "أحلت لكم", "ولا تنكحوا", "فاكتبوه", "فليكتب", "فللذكر", "للذكر", "ليس عليكم", "أوصاكم"]`
      (deduplicated at execution; substrings allow proclitics).

  (b) Inheritance-fraction lexemes — substring-match for:
      `["النصف", "نصف", "الثلث", "ثلث", "الربع", "ربع", "الثمن", "ثمن", "السدس", "سدس", "الثلثان", "الثلثين", "ثلثا"]`

  Composite: `score(s) = (count_a(s) + count_b(s)) / words(s) * 100`.

- Comparison surahs (legal-Medinan): Q 2, Q 4, Q 5, Q 9, Q 24, Q 33, Q 58, Q 60, Q 65.
- Primary verdict: Q 4 rank in top-3 of all 114 by the composite score.

## Null model

- MW-2 corpus-prior null: scramble surah-labels on the (count, words) pairs and re-compute the composite-score rank distribution. 10000 permutations under seed=20260507.
- Report: percentile-rank of Q 4's actual composite score against the null distribution of Q 4's score under random label re-assignment of (count_a + count_b) tokens to surahs at the per-token level.

## Direction & alternative

- DIRECTION-LOCKED: top-3 rank (HIGHER score → higher rank-position).
- If Q 4 rank is 4-6: DIRECTIONAL-NEAR; if rank > 6: NULL/REVERSED with full prominence.

## Bonferroni

- Family: Q004-novel-tests-2026-05-07, k=5.
- α_bon = 0.05 / 5 = 0.01.
- Single-test α applied to the rank-test above.

## Failure / NULL conditions

- Q 4 rank > 3 → DIRECTIONAL/NULL.
- Q 4 rank in top-3 BUT permutation-p > α_bon → DIRECTIONAL only.
- Lexicon-substring matches yield zero for >80% of the corpus → re-examine lexicon (lexicon-fragility); flag as RULES-TUPLE-FRAGILE.

## Pre-commit-violation handling

A reverse direction (Q 4 rank > 25) is treated as falsifying the qualitative classical claim; published with full prominence as a CLASSICAL-CLAIM-FALSIFIED null.

## Honest limits acknowledged in advance

- Substring matching catches most morphological forms but may miss rare tashkeel-sensitive ones; this is rules-tuple-fragile by design.
- "Imperative density" is a proxy for legal density; it does not capture descriptive legal verses (e.g., "al-zānī wa-al-zāniyatu" Q 24:2).
- The lexicon was built from al-Suyūṭī's 4-tier legal-verse classification and al-Zarkashī chapter on aḥkām; any lexicon enlargement post-execution is a pre-commit violation.
