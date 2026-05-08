---
finding_id: Q016-F-01
title: Niʿmah-catalog saturation in Q 16 al-Naḥl
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q016-al-nahl-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q016-F-01-nimah-density
bonferroni_k: 3
alpha_bon: 0.0167
direction: one-sided UPPER on niʿmah-vocabulary density per 100 tokens (Q 16 > corpus baseline; rank ≤ 3/114)
success_criterion: Q 16 ranks in top-3 of `nimah_density_per_100tok` AND permutation-null p ≤ α_bon = 0.0167
failure_criterion: Q 16 ranks > 10/114
rules_tuple: "(no-tashkeel, orthographic-token, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
script: surahs/Q016-al-nahl/scripts/Q016_F_01_nimah_catalog.py
output_json: surahs/Q016-al-nahl/csv/Q016-F-01.json
parent_oq: Q 16 named as "Sūrat al-Niʿam" (al-Qurṭubī, intro to Q 16; al-Suyūṭī *Itqān*, nawʿ 17 reporting Qatāda)
---

# Q016-F-01 — Niʿmah-catalog saturation (pre-reg)

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 16 al-Naḥl has a niʿmah-catalog vocabulary density that is **in the top-3** among the 114 surahs (per 100 orthographic tokens). The classical alt-name *Sūrat al-Niʿam* corresponds to a quantitatively-detectable saturation of created-blessing vocabulary in Q 16.

**H0:** Q 16 ranks no better than 11/114 on the metric.

**Direction:** Q 16 > corpus median on niʿmah_density_per_100tok (LOCKED).

## 2. Operational definition

**Niʿmah-catalog marker set** (no-tashkeel Arabic, regex word-boundary; selected to track God's natural-blessing roll-call vocabulary specifically — NOT generic divine-mercy terms):

A. **Blessing/mercy nouns**: نعمة، نعم، نعمت، نعمه، رحمة، رحمه (the abstract niʿmah/raḥma)

B. **Subjugation/causation verbs (3M.PERF + 3M.IMPF)**: سخر، سخرنا، يسخر، أنزل، أنزلنا، أنزل، نزلنا، أنبت، أنبتنا، ينبت، جعل، جعلنا، يجعل، أخرج، أخرجنا، يخرج

These are the **classic Quranic creation-act verbs** that drive the niʿmah-catalog rhetoric (e.g., *anzala min al-samāʾi māʾan*, *sakhkhara lakum al-baḥra*, *jaʿala lakum al-jibāla*, *anbata lakum bihi al-zarʿa*).

C. **Created-blessing object nouns** (the ROLL-CALL targets): الأنعام، أنعام، الماء، البحر، البحار، الأنهار، الجبال، الشجر، الأشجار، الثمرات، السماء، الشمس، القمر، النجوم، الليل، النهار، اللبن، العسل، الزرع، الفلك (the litany items)

**Per-surah metric**:
- `nimah_density_per_100tok` = (Σ matches across A∪B∪C) / (total orthographic tokens) × 100

The 3-component split (A=mercy-noun, B=creation-verb, C=blessing-object) is locked to also enable 3-cell secondary analysis (Bonferroni k=3 family).

## 3. Test statistics

**Primary**: Q 16's rank on `nimah_density_per_100tok` (1 = highest).
**Secondaries** (Bonferroni k=3 family):
- F-01a: rank on the A-component density (mercy-noun)
- F-01b: rank on the B-component density (creation-verb)
- F-01c: rank on the C-component density (blessing-object)

**Permutation null**: per primary, randomly relabel the 114 surahs' identities 10000 times (i.e., sample 10000 random permutations of {1..114}); record the rank of "the surah relabeled to position 16" — actually, a simpler null: under the Q016 row, the empirical p is the fraction of 114 surahs whose density ≥ Q16's; for permutation-null, randomly resample 1963 tokens (Q 16's token count) **without replacement** from the corpus pool 10000 times, count matches, and compute the fraction with density ≥ Q 16's empirical density. This controls for surah-length.

## 4. Success / Failure

- **Strict success (CONFIRMED, top-3)**: Q 16 ranks in top-3/114 on `nimah_density_per_100tok` AND permutation-null p ≤ α_bon = 0.0167.
- **Directional**: Q 16 in top-10/114 (perm p ≤ 0.05 raw).
- **NULL**: Q 16 > rank 10.
- **Pre-commit violation**: Q 16 ranks bottom-quartile (≥ 86) — pre-commit violation per PRE-REG-STANDARD-01.

## 5. Honest limits

- Marker set is curated, not exhaustive. The list is the project-canonical niʿmah-catalog set per the al-Qurṭubī intro to Q 16 + al-Rāzī's enumeration in *Mafātīḥ al-ghayb* on Q 16:5–18.
- Token-density (not lemma-density) is used because no-tashkeel orthographic tokens are the rules-tuple default.
- Some markers (e.g., "نعمة") appear in non-niʿmah-catalog contexts (e.g., Q 14:34 "if you count the niʿmah of Allah"). The metric is a *proxy*, not an exhaustive niʿmah-catalog detector. Q 14:34 also passes through the metric — that is acceptable because Q 14 is one of the *also*-niʿmah-catalog surahs in classical exegesis.

## 6. Garden-of-forking-paths log

- **Why per-100-tokens not per-verse?** Per-verse would be biased toward long-verse surahs; per-token is length-normalized.
- **Why top-3 strict?** Q 16's classical alt-name *Sūrat al-Niʿam* is a STRONG positive prior. If the metric is well-defined, top-3 is the natural success threshold; weakening to top-10 would be loosening post-observation. Top-3 is locked.
- **Why no rate-of-Allah-name baseline?** The hypothesis is specifically about niʿmah-CATALOG vocabulary, not about religiosity in general. Q 16's Allah-density is at the corpus 75th-percentile (h-new-126), not a relevant control.
- **Inclusion of أَنزَلَ verb forms**: critical because the classic catalog phrase is *anzala min al-samāʾi māʾan*. Excluding would defeat the test.

## 7. MW protections

- MW-1 (instrument-prior): regex marker-list locked above.
- MW-2 (corpus-prior): 10000-permutation null on token-resample.
- MW-3 (alternative-models): F-01a/b/c sub-tests provide model-variant control.
- MW-5 (positive-control): Q 14 Ibrāhīm (also a niʿmah-catalog surah per al-Qurṭubī) should rank in the top-15 to validate the instrument.
- MW-6 (instrument-control): Q 12 Yūsuf (a narrative surah, not a niʿmah-catalog) should rank in the bottom-half. If Q 12 ranks top-15, the instrument is mismatched.
- MW-7 (post-hoc cap): the top-3 threshold is PRE-REGISTERED.

## 8. Files

- Pre-reg: `surahs/Q016-al-nahl/Q016-F-01-nimah-catalog-saturation-prereg.md`
- Script: `surahs/Q016-al-nahl/scripts/Q016_F_01_nimah_catalog.py`
- Output: `surahs/Q016-al-nahl/csv/Q016-F-01.json`

*PRE-REG LOCKED 2026-05-07 — SHA256 to be computed and embedded in run script.*
