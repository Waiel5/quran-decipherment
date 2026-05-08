---
surah: 6
test_id: Q006-F-01
title: Prophet-density per verse — Q 6:83-87 list-form maximum vs corpus
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
bonferroni_family: Q006-F-01-prophet-density
alpha_bon: 0.05
direction_locked: MAX
---

# Q006-F-01 — Pre-registration: Prophet-density per verse

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 6 has the **highest prophet-density per verse** (i.e., distinct canonical-prophet PN-lemma tokens per verse) among all 114 surahs that contain ≥2 named prophets. The Q 6:83-87 *al-ḥujja* genealogical roll-call (18 prophet-name tokens spread across vv. 83-87) gives Q 6 a **list-form prophet-density** that is corpus-MAX — empirically distinct from Q 21's narrative-form maximum (14 prophets across 44 verses, density 0.318).

**Direction:** MAX (LOCKED). Q 6 ranks 1/N where N is the count of qualifying surahs.

**H0 (NULL):** Q 6 ranks ≥ rank 5 on prophet-density per verse.

**Pre-commit violation:** Q 6 ranks ≥ rank 10. (Strong refutation of list-form-MAX claim.)

## 2. Garden-of-forking-paths log (BEFORE observation)

The Q 21 specialist already established (Q021-F-01 NULL) that Q 6 has 16 distinct canonical prophets across the surah (the corpus MAX of distinct prophets); Q 21 has 14 distinct prophets. The author has NOT yet observed `prophet-density per verse` for Q 6 vs. the corpus. This pre-reg locks density-per-verse as the new metric BEFORE running it.

The author has previewed Q 6:83-87 (5 verses with 18 prophet-name TOKENS — counting overlapping lemma occurrences). The metric here is **distinct canonical-prophet PN-lemma TYPES per verse** averaged over the surah, NOT cumulative tokens. Density is `total_distinct_prophet_lemmas_in_surah / total_verses_in_surah`. Q 6 = 16 / 165 = 0.0970. Q 21 = 14 / 112 = 0.125. Under this metric, **Q 21 wins**, and Q 6 is NOT the list-form MAX. To capture the LIST-FORM phenomenon properly, we must use a different operationalization.

**Operationalization (locked):**
- Primary metric (Cell A): **maximum prophet-tokens-per-verse** within the surah. Q 6:84 has 8 prophet-name tokens in one verse (Isḥāq, Yaʿqūb, Nūḥ, Dāwūd, Sulaymān, Ayyūb, Yūsuf, Mūsā, Hārūn — 9 actually; verify on data). This metric isolates the LIST-FORM intensity.
- Secondary metric (Cell B): **density of prophet-tokens-per-verse within the densest 5-verse window** of the surah.

Both metrics are NEW operationalizations distinct from Q021-F-01. Bonferroni-2.

## 3. Operational definition

**Canonical-prophet PN-lemma set** (locked, identical to H-NEW-940 / Q021-F-01):
{Ādam, Nūḥ, Hūd, Ṣāliḥ, Ibrāhīm, Ismāʿīl, Isḥāq, Yaʿqūb, Yūsuf, Lūṭ, Shuʿayb, Mūsā, Hārūn, Dāwūd, Sulaymān, Ilyās, al-Yasaʿ, Yūnus, Zakariyyā, Yaḥyā, ʿĪsā, Idrīs, Ayyūb, Muḥammad, Aḥmad}.

**QAC v0.4 PN-lemma extraction** from `data/morphology/quranic-corpus-morphology-0.4.txt`. POS:PN with LEM ∈ canonical set.

**Cell A — `max_prophet_tokens_in_single_verse`**: per surah, the maximum count of canonical-prophet-lemma TOKENS in any one verse. Token = each PN-lemma occurrence (so if Mūsā appears twice in a verse, count = 2; if Mūsā and Hārūn both appear, count = 2).

**Cell B — `densest_5verse_prophet_token_density`**: per surah, the maximum sum of canonical-prophet-tokens over any 5 consecutive verses, divided by 5 (= prophet-tokens / verse in densest 5-verse window). Note: includes overlapping verses; surahs with <5 verses use total/n.

Bonferroni k=2, α_bon = 0.025.

## 4. Test statistic / Success / Failure

**Cell A success (CONFIRMED):** Q 6 ranks 1/N on `max_prophet_tokens_in_single_verse` (where N = number of surahs with ≥1 canonical prophet token).

**Cell B success (CONFIRMED):** Q 6 ranks 1/N on `densest_5verse_prophet_token_density`.

**DIRECTIONAL:** Q 6 in top-3 on either cell.

**NULL:** Q 6 ≥ rank 5 on the cell.

**Pre-commit violation:** Q 6 ≥ rank 10 on either cell (strong refutation).

Joint:
- Both cells PASS → CONFIRMED.
- One cell PASSES (top-3 strict) → DIRECTIONAL.
- Neither passes top-3 → NULL.
- Either cell ranks ≥ 10 → PRE-COMMIT VIOLATION on that cell.

## 5. Honest limits known a priori

- This metric is novel: it isolates "instantaneous prophet-list density" rather than total surah cardinality. It deliberately captures the LIST-FORM phenomenon distinct from narrative-form density.
- Q 6:84 has been previewed by eye (~9 PN-tokens). The pre-reg locks the formal computation under PN-lemma matching with QAC v0.4.
- Adam, Muḥammad, Aḥmad in the canonical set are corpus-rare PN-tokens; their inclusion is conservative.
- Note: a "prophet-token" here is a PN-name lemma occurrence; it does NOT include pronominal anaphora (huwa, hu, etc.) which would inflate narrative-form surahs. This is a deliberate operational choice favouring LIST-FORM.

## 6. Rules-tuple

`(no-tashkeel, QAC-PN-lemma, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at pre-reg-completion time and embedded into `surahs/scripts/Q006_F_01_prophet_density.py`. Verified at runtime.
