---
id: H-NEW-1320
title: Refrain-saturation corpus-rank — Q 55 rank-1 + sibling identification
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: H-NEW-1320-refrain-saturation
alpha_bon: 0.025
direction_of_effect: |
  Cell A: Q 55 al-Raḥmān has the strict-maximum max_identical_verse_repeat_count of any of the 114 surahs (rank #1).
  Cell B: Q 26 al-Shuʿarāʾ and Q 77 al-Mursalāt each rank in top-5 by max_identical_verse_repeat_count.
origin: handoff §7b — "Cross-finding-027 iʿjāz al-takrīr extension: now that Q 55 has corpus-EXACT dual-audience signature, find the 2nd and 3rd most-refrain-architectured surahs (Q 26, Q 77 candidates)"
verdict_ceiling: PASS-DIRECTED (handoff origin = single planned test family; INDEPENDENT REPLICATION required for promotion)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  verse_string_equality: exact-no-tashkeel-string-after-whitespace-normalization
  null_model: corpus-wide-verse-string-permutation-preserving-surah-verse-counts
---

# H-NEW-1320 pre-registration

## Origin

Handoff §7b: "now that Q 55 has corpus-EXACT dual-audience signature (H-NEW-1250), find the 2nd and 3rd most-refrain-architectured surahs (Q 26, Q 77 candidates)."

This pre-reg formalizes the search: define refrain saturation rigorously, rank all 114 surahs, test whether Q 55 is strict rank-1 and whether Q 26/Q 77 are in the top-5.

## Hypothesis

### Cell A (inferential)

The maximum identical-verse-repeat-count per surah is a corpus-EXTREME signature for Q 55 al-Raḥmān, exceeding all 113 other surahs strictly.

### Cell B (descriptive ranking + ranked-position test)

Q 26 al-Shuʿarāʾ AND Q 77 al-Mursalāt each rank in the top-5 of the max-repeat-count corpus ranking.

## Test design

### Statistic: max_repeat_count(s)

For each surah s ∈ {1,…,114}:
1. Strip tashkeel; normalize whitespace; lowercase Arabic (already canonical).
2. Compute Counter of verse strings.
3. max_repeat_count(s) = the highest frequency of any verse-string within surah s.

The corpus rank of Q 55 by max_repeat_count is the test statistic for Cell A.

### Cell A: rank test

PASS if Q 55 strict rank-1 (no ties); NULL otherwise (under PRE-REG-STANDARD-01 strict pre-commitment).

### Cell A permutation null (additional)

Pool all 6,236 verse-strings (from no-tashkeel, with whitespace normalization). Randomly redistribute to surahs preserving each surah's verse-count. Compute max_repeat_count per random surah; record max-over-all-surahs. p_perm = fraction of 10000 perms where max-over-all-surahs ≥ Q 55's observed value.

### Cell B: top-5 inclusion

PASS if both Q 26 and Q 77 rank ≤ 5; PARTIAL if one ranks ≤ 5; NULL if neither.

### Bonferroni

k = 2 (Cell A + Cell B). α_bon = 0.025 per cell.

### Acceptance windows

| Cell A | Cell B | Verdict |
|:-:|:-:|:--|
| ✓ (rank-1 strict + p_perm ≤ 0.025) | ✓ (Q 26, Q 77 both top-5) | PASS-DIRECTED FULL |
| ✓ | partial (1 of 2 top-5) | PASS-DIRECTED CELL-A-only |
| ✗ | ✓ | PARTIAL |
| ✗ | ✗ | NULL |

### Garden-of-forking-paths

Origin disclosed: handoff §7b. No verse-frequency data viewed. Direction locked: Q 55 strict rank-1 + Q 26/Q 77 top-5. The cluster identity (Q 26, Q 77 specifically) is locked from the handoff text. The exact statistic (max identical-verse-repeat-count) is an a-priori operationalization of "refrain saturation"; alternative operationalizations (longest repeated n-gram, intra-surah Levenshtein clustering, refrain-pattern Markov detection) are NOT within this pre-reg's scope.

### Rules-tuple sensitivity

Test runs on no-tashkeel only (default). A future H-NEW-1321 could replicate under min-tashkeel orthography, where some near-identical verses might collapse or de-collapse depending on diacritic differences.

### Anti-flip

Reverse direction (Q 55 NOT rank-1) is a NULL — published with prominence.

### MW-5 positive control

Under verse-permutation null, the structurally-known identical-verse pair Q 1:1 = Q 27:30 ("bismillāh al-raḥmān al-raḥīm") should NOT trigger a high max_repeat_count for either surah (since each has only 1 occurrence of the bismillāh). This is a sanity check that the statistic doesn't double-count cross-surah repetitions.

The instrument-control specifically: under random verse-permutation, the average max_repeat_count per surah should be ~1.0 (most verses unique under random shuffle). If the null distribution shows mean max-over-all-surahs ≫ 2, the null is broken.

## Connection to existing findings

- H-NEW-1250 / cross-finding-027: Q 55 al-Raḥmān corpus-EXACT dual-audience architectural signature; the *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* refrain is the central iʿjāz al-takrīr feature.
- H-NEW-83: noted Q 77 al-Mursalāt has refrain-density 0.20 (next after Q 55's 0.40). This pre-reg formalizes that descriptive observation as a corpus rank.
- H-NEW-1190 *wa-mā adrāka mā*: a different REFRAIN family (cross-surah, not within-surah). Distinct phenomenon.
- Cross-finding-014 + cross-finding-027: iʿjāz al-takrīr (eloquence-of-repetition) as a meta-principle. This rank result extends the search.

## Pre-commit attestation

Locked by SHA256. Run script verifies before loading verse-string data.
