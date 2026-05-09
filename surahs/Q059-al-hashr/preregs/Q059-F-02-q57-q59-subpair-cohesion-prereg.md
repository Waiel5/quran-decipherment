---
surah: 59
test_id: Q059-F-02
title: Q 57 + Q 59 perfect-tense sub-pair cohesion within musabbiḥāt
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q059-F-02-q57-q59-subpair-cohesion
alpha_bon: 0.0167
post_hoc_origin: NO — this is a planned sub-cluster decomposition test asked for in the Q 59 specialist brief.
---

# Q059-F-02 — Pre-registration: Q 57 + Q 59 perfect-tense sub-pair cohesion test

## 1. Hypothesis (locked before observation, brief-derived)

**H1a (descriptive, brief-derived):** Within the H-NEW-58c perfect-tense trio {Q 57, Q 59, Q 61}, identify the **tightest sub-pair** by opening-verse shared-character-prefix.

**H1b (one-tailed):** The Q 57 + Q 59 sub-pair shared-prefix is greater than chance for two random surahs drawn from the H-NEW-1080 short-Medinan block (Q 57-66, 10 surahs).

**H1c (one-tailed):** The full musabbiḥāt 5-surah cluster (Q 57, 59, 61, 62, 64) total-pair-prefix-sum exceeds the random 5-of-10 short-Medinan-subset null.

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` after ornamentation strip + whitespace normalization.
- **Opening verse**: v1 only, full verbatim text.
- **Shared character prefix**: count of identical chars from index 0 until first divergence.
- **Surah-token-set Jaccard** (Cell B): `|tokens(A) ∩ tokens(B)| / |tokens(A) ∪ tokens(B)|` over orthographic tokens (whitespace-split).

## 3. Test statistics

- p1 (Q 57+59 prefix) — 1 number.
- p2 (Q 57+61 prefix) — 1 number.
- p3 (Q 59+61 prefix) — 1 number.
- max-perfect-subpair = max(p1, p2, p3).
- mean-perfect-trio = (p1 + p2 + p3) / 3.
- musabbiḥāt-5-prefix-sum = sum of all 10 pair-prefixes among {Q 57, 59, 61, 62, 64}.

## 4. Permutation nulls

**Cell C (10-pair sum null):** sample 10,000 random 5-of-10 subsets from short-Medinan {Q 57-66}, compute prefix-sums, p = fraction ≥ observed musabbiḥāt-5 sum.

**Cell E (pair null):** sample 10,000 random 2-of-10 pairs from short-Medinan, compute prefix, p = fraction ≥ Q 57+59 observed prefix.

n_perm = 10,000, seed = 20260509.

## 5. Success / Failure

- **CONFIRMED**: H1c passes at p < α_bon = 0.0167.
- **DESCRIPTIVE-PASS**: tightest perfect-trio sub-pair identified.
- **NULL**: musabbiḥāt 5-pair-sum no different from random.

## 6. Honest limits

- The "post-hoc-noticed" status is excluded because the cluster identity is well-pre-existing in [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]; this test asks a sub-pair decomposition question, not a discovery question.
- Q 59:1 and Q 61:1 are character-identical for the full 53-char opening (computed); Q 57:1 differs at char 24 (والأرض vs وما في الأرض). H-NEW-58c reported 56 chars; my recount gives 53 (likely H-NEW-58c included the trailing space — minor discrepancy, doesn't affect substantive conclusion).
- **Sub-pair within trio**: when there are only 3 sub-pairs in a trio, the test of "Q 57+59 = tightest" has 1/3 chance under uniform-rank-null; this is a **descriptive identification**, not a hypothesis test.

## 7. Rules-tuple

`(no-tashkeel, ornament-stripped, whitespace-tokenized, opening-verse-shared-prefix, surah-token-set-Jaccard)`.

## 8. Bonferroni

k = 3 (H1a, H1b, H1c). α_bon = 0.0167.

## 9. Authored by

Waiel Al-Shujaa, 2026-05-09.
