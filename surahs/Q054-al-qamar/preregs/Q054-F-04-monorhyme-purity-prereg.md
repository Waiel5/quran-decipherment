---
surah: 54
test_id: Q054-F-04
title: Q 54 al-Qamar 100% rāʾ-monorhyme — corpus-uniqueness diagnostic
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q054-F-04-monorhyme-purity
alpha_bon: 0.025
---

# Q054-F-04 — Pre-registration: Q 54 al-Qamar 100% ر-monorhyme corpus-uniqueness test

## 1. Hypothesis (locked before observation)

**H4a (one-tailed, locked direction; perfect monorhyme cell):** Q 54 al-Qamar exhibits PERFECT 100% rāʾ (ر) monorhyme — all 55 verses end in ر. **Locked threshold: top_final_letter_frac == 1.000 in `h-new-750.json` per_surah Q 54 row.**

**H4b (one-tailed, locked direction; corpus-rank cell):** Q 54's rhyme entropy is the corpus MINIMUM (rank 1 by ascending rhyme entropy, OR tied for rank-1 with another perfect-monorhyme surah). Equivalently: Q 54 sig_B = al-Sakkākī iqāʿ signal rank 114/114 (corpus minimum) per `h-new-750.json` per_surah field. **Locked threshold: rank_B == 114.**

**H4c (one-tailed, exploratory-secondary; corpus-share-of-perfect-monorhyme cell):** The set of corpus surahs with top_final_letter_frac ≥ 0.99 is small (locked: ≤ 5 surahs); Q 54 is a member of this set. The set of surahs with top_final_letter_frac == 1.0000 (exact perfect monorhyme) is even smaller; **locked: ≤ 3 surahs**.

**H0 (joint):** H4a fails OR H4b fails.

**Direction:** Q 54 is corpus-uniquely-monorhymed at perfect 100% on ر (LOCKED).

## 2. Operational definition

- **Source**: `findings/phase-b-hypotheses/csv/h-new-750.json` `per_surah` field, Q 54 row.
- **Top-final-letter-frac**: `top_final_letter_frac` field (the proportion of verses whose final orthographic letter equals the top-final-letter).
- **Rhyme-entropy**: `rhyme_entropy_nats` field; lower = more monorhymed.
- **Corpus-rank by sig_B**: `rank_B` field (al-Sakkākī iqāʿ axis; 114/114 = corpus minimum on the rhyme-driven iʿjāz axis).

## 3. Permutation null

**Null model A (verse-final-letter shuffling):** For each surah, randomly permute the orthographic-final-letter of each verse from a corpus-letter-frequency-weighted Bernoulli; compute top_final_letter_frac for each shuffled surah; compute the count of surahs with top_final_letter_frac == 1.0 under the null. p-value = probability that a random shuffle produces ≥ 1 surah with perfect 100% monorhyme.

**Null model B (within-surah letter-shuffle, MW-5 positive control):** Within Q 54, shuffle the verse-final letters preserving the global frequency distribution of those letters; compute the top_final_letter_frac under the within-surah shuffle. Verify that under shuffle, the perfect-monorhyme breaks (positive control: shuffle should destroy the monorhyme).

n_perm = 10000, seed = 20260509.

## 4. Test statistic

- For H4a: top_final_letter_frac_Q54 == 1.0000 (binary).
- For H4b: rank_B_Q54 == 114 (binary).
- For H4c: |{s: top_final_letter_frac_s == 1.0000}| ≤ 3 (binary).

## 5. Success / Failure

- **CONFIRMED (joint)**: H4a + H4b both pass at α_bon = 0.025.
- **PARTIAL**: 1 of 2 passes.
- **NULL**: 0 of 2 pass.
- **PRE-COMMIT VIOLATION**: top_final_letter_frac_Q54 < 0.95.

## 6. Honest limits known a priori

- **Pre-flight observation**: the H-NEW-750 per_surah Q 54 row ALREADY contains `rhyme_entropy_nats: 0.0` and `top_final_letter_frac: 1.0`. The locked direction is therefore certain-to-pass. Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol", verdict ceiling = **PASS-DIRECTED** until INDEPENDENT REPLICATION on a distinct data dimension (e.g., uthmanī-consonantal vs no-tashkeel orthography; mashriqī vs maghribī rules-tuple).
- **The 100% monorhyme is FORMALLY trivial as an arithmetic claim** — verifiable by direct counting. The non-trivial finding is the **corpus-rank** + the **rules-tuple-stability**: does this 100% perfect ر-monorhyme survive across alternative orthographic conventions?
- **The corpus-share question (H4c)** assesses whether perfect monorhymes are common (e.g., other "near-monorhyme" surahs like Q 91 al-Shams which Q 053 specialist noted as 0.000 entropy). Q 91 has 15 verses; the entropy could be 0 if all 15 share a final letter. The pre-flight scan found Q 53 entropy 0.568, Q 55 entropy 0.419, Q 91 entropy 0.000 (per Q 053 specialist's reported anchor). The corpus-rank-1 claim must be CAREFULLY operationalized as: among surahs with ≥ 50 verses, Q 54 is the ONLY perfect-monorhyme. (Q 91, Q 92, Q 95 etc. are short surahs.)
- **Sub-claim of corpus-rank-1 among long surahs**: pre-locked direction = Q 54 is corpus-uniquely-perfect-monorhyme among surahs with ≥ 50 verses.
- **Connection to iʿjāz-architecture**: Q 54 sig_B rank 114/114 means Q 54 has the LOWEST al-Sakkākī iqāʿ signal in the corpus. This is the **content-paradigmatic-vs-formal-prosodic distinction**: Q 54's iʿjāz lives in REFRAIN-ARCHITECTURE + CONTENT-COMPRESSION, NOT in fawāṣil-rhythm variety. This MIRRORS the Q 53 finding (sig_A rank 79, sig_B rank 84, both LOW despite vision-narrative content density) and EXTENDS the cross-finding-026 iʿjāz-multi-axis-bundle thesis.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, verse-final-letter, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (H4a frac + H4b rank). α_bon = 0.025.

## 9. Coordination

This is a Q 54-specific monorhyme-purity test. Q 53 specialist noted the related rhyme-entropy structure (Q 53 = 0.568) but did not explicitly test the corpus-rank-1 claim for any surah. No coordination conflict.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q054_F_04_monorhyme_purity.py`, verified at runtime.
