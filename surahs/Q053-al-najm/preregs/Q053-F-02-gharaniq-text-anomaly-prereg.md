---
surah: 53
test_id: Q053-F-02
title: "Q 53:19-23 reverse-direction empirical text-anomaly null (gharānīq adversarial)"
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q053-F-family-2026-05-09
alpha_bon: 0.0167
---

# Q053-F-02 — Pre-registration: Empirical text-anomaly null on Q 53:19-23

## 1. Hypothesis (locked before observation)

**H1 (REVERSE-DIRECTION test, two-tailed)**: If the *gharānīq* / "satanic verses" classical narrative were historically true (i.e., if verses *tilka l-gharānīqu l-ʿulā wa-inna shafāʿatahunna la-turtajā* had been temporarily inserted between Q 53:20 and Q 53:21 and subsequently corrected/removed), the resulting current text of Q 53:19-23 should exhibit detectable lexical-distribution anomalies vs. the corpus baseline of 5-verse windows.

**Direction (reverse)**: We predict the text WILL show NO lexical anomaly — i.e., that the corpus-baseline test will produce a NULL result. This is a falsification test: if the text DID show anomaly, the gharānīq-historicity claim would gain empirical support; if it does NOT, the claim loses one more verification axis.

**H0 (the gharānīq-historicity hypothesis)**: Q 53:19-23 SHOULD have anomalous lexical-distribution metrics (token count significantly different from corpus mean; type-token ratio in extreme tail; hapax-rate elevated) reflecting the textual-disturbance from interpolation-removal.

**H1 (the null hypothesis as adversarial-direction)**: Q 53:19-23 does NOT show anomalous lexical-distribution; it is statistically-typical for a short-Meccan polemical block.

**REVERSE-DIRECTION LOCKING**: This is a sanity-check test where finding NO ANOMALY (NULL) is the expected outcome that adversarially-confirms the textual-history (i.e., no-interpolation). The null direction is THE empirical claim. Per project's adversarial-discipline framework (HANDOFF/04-DISCIPLINE.md), this is a legitimate use of the reverse-direction test.

## 2. Operational definition

**Block**: Q 53:19-23 (5 verses).

**Metrics computed**:
- `n_tokens(block)` = total token count (split by whitespace)
- `n_unique(block)` = unique-token count
- `ttr(block)` = type-token ratio = n_unique / n_tokens
- `block_token_count_rank` = rank of the block's token count among all 5,783 5-verse windows in the corpus (low-to-high)
- `block_ttr_rank` = rank of the block's TTR among all 5,783 5-verse windows

**Corpus baseline**: All 5-verse contiguous windows across all 114 surahs (excluding surahs with <5 verses); n = 5,783 total windows.

## 3. Test statistic

**Primary (REVERSE-direction-locked)**: Q 53:19-23's metrics fall WITHIN the corpus 5%-95% percentile range (i.e., NO extreme-tail signature).

**Secondary**: Q 53:19-23 token-count rank (low-to-high) and TTR-rank.

## 4. Success / Failure thresholds

- **NULL CONFIRMED (which is the expected result)**: Q 53:19-23 metrics lie within corpus 5%-95%-ile (i.e., 290 ≤ token-count-rank ≤ 5493 / 5783; analogous for TTR).
- **DIRECTIONAL ANOMALY** (would weaken the gharānīq-falsification): Q 53:19-23 metrics in extreme tail (rank ≤ 290 OR rank ≥ 5493).
- **EXTREME ANOMALY** (would significantly weaken the gharānīq-falsification): Q 53:19-23 in top-1% / bottom-1% (rank ≤ 58 OR rank ≥ 5725).

## 5. Honest limits known a priori

- A NULL result here does NOT positively confirm "no interpolation occurred" — it confirms only that *if* interpolation occurred, no detectable lexical-distribution signature was left in the surviving text after the alleged correction.
- The test is sensitive only to lexical-distribution anomalies; syntactic / structural / metrical anomalies require different operationalizations (out of scope for this test; PENDING future cross-replication).
- 5-verse window granularity may miss verse-level interpolation. A more sensitive test would be at the verse-level (5 single-verse comparisons), but that requires a different baseline.
- The test does NOT assess the *historicity* of the narrative directly — it assesses whether the text shows residual-evidence-of-editing. These are logically distinct.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token-whitespace-split, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Permutation null

Not applicable; the test is rank-against-baseline. The threshold for NULL CONFIRMED is rank in the 5%-95% range.

## 8. Garden-of-forking-paths log

- The reverse-direction structure is SPECIALLY-DECLARED here: NULL is the predicted-and-desired outcome. Per HANDOFF/04-DISCIPLINE.md, reverse-direction tests must be explicitly disclosed; this disclosure is locked here.
- The 5-verse window granularity was chosen as a compromise between within-block resolution (1-verse would be too coarse for distribution detection) and corpus-baseline-comparability (5-verse aligns with the project's standard window-size for comparable analyses). This choice was made BEFORE result-viewing.
- The token-count + TTR + rank-statistics were specified before result-viewing.
- This test is NOT a strong falsification of historicity claims; it is one verification axis among several. The composite-verification is at `05-classical-claims-audit.md` §2 (combining 9-book null + empirical-text null + classical-Sunni-mainstream rejection).

## 9. SHA256 lock

To be computed at write-time. Embedded in `scripts/Q053_F_all_tests.py`.
