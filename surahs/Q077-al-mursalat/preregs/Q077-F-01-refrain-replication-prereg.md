---
surah: 77
test_id: Q077-F-01
title: Q 77 refrain architecture replication — corpus rank-2 + 10× exact verbatim count
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q077-F-01-refrain-replication
alpha_bon: 0.0167
---

# Q077-F-01 — Pre-registration: Q 77 refrain architecture replication

## 1. Hypothesis (locked before observation)

H-NEW-1320 (PASS-DIRECTED FULL, 2026-05-09) ranked Q 77 al-Mursalāt as **rank-2 in corpus refrain saturation** with the *waylun yawmaʾidhin li-l-mukadhdhibīn* refrain repeating 10× across 50 verses. This pre-registration replicates the H-NEW-1320 result on Q 77 specifically AND adds three further axes of refrain-architectural verification:

**H1 (Cell A — exact-count replication):** Q 77's *waylun yawmaʾidhin li-l-mukadhdhibīn* (= "ويل يومئذ للمكذبين") refrain count is **exactly 10** under the no-tashkeel rule. Cell A passes if count == 10 AND consistent across no-tashkeel / min-tashkeel / full-tashkeel variants.

**H2 (Cell B — corpus rank confirmation):** Q 77 ranks **2/114** by max identical-verse-repeat-count (replicating H-NEW-1320). Cell B passes if rank_q77 == 2.

**H3 (Cell C — within-corpus refrain monopoly):** the EXACT string *ويل يومئذ للمكذبين* (no-tashkeel) appears in Q 77 ten times AND in Q 83:10 once (per H-NEW-1230 disclosed; ledger says "+ 2 outliers Q 52, Q 83"; the Q 52 outlier is *fa-wayl yawmaʾidhin* not the verbatim string, so corpus exact = 11 occurrences, of which 10 are in Q 77). Cell C passes if 10 of the 11 corpus-exact occurrences are in Q 77 (≥ 90.9% concentration).

**H0:** Q 77 has no privileged refrain density (count != 10, or rank > 2, or concentration < 90%).

## 2. Operational definitions

- Source: `quran-text/quran-no-tashkeel.json` (canonical no-tashkeel text); `quran-text/quran-min-tashkeel.json`, `quran-text/quran-full-tashkeel.json` for cross-variant.
- **Refrain string (no-tashkeel)**: ويل يومئذ للمكذبين — exact NFC-normalized, whitespace-collapsed match.
- **Refrain string (min/full-tashkeel)**: under variant-aware normalization (strip diacritics, normalize alif/yāʾ/tāʾ-marbūṭa) the string should reduce to the no-tashkeel form ويل يومئذ للمكذبين.
- **Cell A statistic**: integer count of verses in Q 77 whose normalized text equals the refrain string.
- **Cell B statistic**: rank of Q 77 in {1, ..., 114} sorted by max identical-verse-repeat-count (ties broken by surah number).
- **Cell C statistic**: corpus_count(refrain_in_Q77) / corpus_count(refrain_anywhere).

## 3. Test statistic

- Cell A: count_q77 (target = 10).
- Cell B: rank_q77 (target = 2).
- Cell C: concentration = q77_count / total_count (target ≥ 0.909).

## 4. Success / Failure

- **PASS-DIRECTED FULL**: H1 + H2 + H3 all pass.
- **PASS-DIRECTED PARTIAL**: 2 of 3 pass.
- **NULL-DIRECTED**: 0-1 of 3 pass.
- **Pre-commit violation**: count != 10 (Cell A directly disconfirms H-NEW-1320 disclosed value); flag for cross-finding amendment.

## 5. Honest limits known a priori

- This is a REPLICATION pre-registration of an already-PASS-DIRECTED finding (H-NEW-1320). The verdict ceiling is therefore **REPLICATION-CONFIRMATION** — independent operationalization at the surah-specialist level, not a fresh discovery.
- Empirical-anchor extraction (DISCLOSED): exploratory inspection of Q 77 verses pre-pre-reg revealed the refrain at vv {15, 19, 24, 28, 34, 37, 40, 45, 47, 49} = 10 verses; corpus-wide check found 1 additional exact match at Q 83:10 and 1 near-match at Q 52:11 (with leading فـ); the test-logic does not depend on this empirical-anchor knowledge — count is locked at integer == 10 and rank at integer == 2.
- The H-NEW-1230 ledger says Q 77 has "10× + 2 outliers Q 52, Q 83." Empirically Q 52:11 is *fa-wayl yawmaʾidhin li-l-mukadhdhibīn* (with prefix fāʾ), so under STRICT verbatim-no-tashkeel match the corpus-exact count is 11 (10 in Q 77 + 1 in Q 83), not 12. This does NOT break the test; it tightens H3 to ≥ 90.9% concentration which is the stricter form of the brief's claim.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token-exact, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` for Cells A and C; `(no-tashkeel, identical-verse-counter, Hafs-Kufan)` for Cell B.

## 7. Bonferroni

k = 3 (Cell A count, Cell B rank, Cell C concentration). α_bon = 0.05/3 = 0.0167. The tests are deterministic-integer-counts under fixed corpus, so no permutation null is computed; pass/fail is by exact-equality / threshold-comparison.

## 8. Garden of forking paths

- All exploratory observations (refrain positions {15, 19, 24, 28, 34, 37, 40, 45, 47, 49}; intervals; cross-corpus exact matches) were noted PRE-LOCK and disclosed above. No alternative test family was attempted and discarded.
- The Q 52:11 prefix-fāʾ near-echo and Q 83:10 exact echo are disclosed for transparency; the test does NOT downgrade based on prefix-fāʾ inclusion/exclusion since H3 is locked at the exact-no-tashkeel-string definition.
- An attractive alternative test would be "refrain INTERVALS form a tightening sequence" (intervals: 4,5,4,6,3,3,5,2,2 with second-half mean 3.0 < first-half mean 4.4). This is queued for a SEPARATE pre-reg (Q077-F-04 below) and explicitly NOT folded into this family.

## 9. SHA256 lock

The corresponding script `scripts/Q077_F_01_refrain_replication.py` will embed and verify this pre-reg's SHA256 at runtime. SHA computed AFTER this file is written.
