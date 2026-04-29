---
id: H-NEW-770
title: "Pre-reg — Verse-length compression-tail: does verse-length follow the same 1-D law as content-cohesion (H-NEW-660)?"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-660 (R²=0.986 content-cohesion compression-tail) — does verse-length share the architecture, or is content-cohesion a separate axis?
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260446
---

# [[h-new-770-verse-length-compression-tail|H-NEW-770]] — Verse-Length Compression-Tail: Pre-Registration

## 1. Hypothesis

The Quran's mushaf has monotonically decreasing verse-length (letters per verse and/or words per verse) from head to tail, paralleling the content-cohesion compression-tail of [[h-new-660-compression-tail-gradient|H-NEW-660]]. Specifically:

> ℓ̄(window-K=15-start-at-s) ≈ α + β · s, with β < 0,

where ℓ̄ is the within-window mean of per-surah mean verse-length.

This is a positive control: al-Suyūṭī's *al-Itqān* and al-Zarkashī's *al-Burhān* describe the *mufaṣṣal* qualitatively as "shorter verses". [[h-new-770-verse-length-compression-tail|H-NEW-770]] quantifies this and tests whether it mirrors [[h-new-660-compression-tail-gradient|H-NEW-660]]'s R²=0.986 single-parameter law.

## 2. Two locked metrics

For each surah s ∈ {1..114}:
1. **Letters-per-verse** — total letter count (no-tashkeel, including all consonants and long vowels as written) divided by number of verses.
2. **Words-per-verse** — total word count (whitespace-split) divided by number of verses.

For each consecutive K=15 window starting at position s ∈ {1..100}:
- ℓ̄_letters(s) = mean over the 15 surahs in the window of the per-surah letters-per-verse.
- ℓ̄_words(s) = mean over the 15 surahs in the window of the per-surah words-per-verse.

This is the SAME windowing as [[h-new-660-compression-tail-gradient|H-NEW-660]] (K=15, s ∈ {1..100}, 100 windows).

## 3. Models (locked)

For each metric (letters and words), three models are fit to ℓ̄(s) on s:

1. **Linear**: ℓ̄ = α + β·(s − 50.5)
2. **Quadratic**: ℓ̄ = α + β·s + γ·s²
3. **Two-piece linear** with kink grid {25, 35, 50, 65, 75}: ℓ̄ = α + β·max(0, s − kink). Best-kink in grid wins; reported as "two-piece-kink-K".

Primary model per metric = the one with highest adjusted-R².

## 4. Permutation null

Shuffle the 114 surahs to a random order (10000 perms, seed 20260446). Recompute ℓ̄(s) on the shuffled mushaf using each surah's own (locked) per-verse mean. Refit all three models. Empirical p-value of observed R² ≥ R²_null.

(Note: the per-surah per-verse mean is a fixed scalar; shuffling permutes which scalars land in which window. The shuffle preserves the marginal distribution of per-surah verse-lengths but breaks the canonical mushaf order.)

## 5. Pre-committed direction

- β < 0 (verse-length decreases with mushaf-position) for both metrics.
- Permutation p ≤ α_corrected.
- Primary-model R² ≥ 0.50.

## 6. Bonferroni structure

- 3 model-fits per metric × 2 metrics = 6 tests total.
- Bonferroni-6 → α_bon = 0.05/6 = 0.00833.

## 7. Pass/fail thresholds

- **STRICT PASS** (per metric): primary-model β < 0, permutation p ≤ 0.00833, R² ≥ 0.50.
- **DIRECTIONAL** (per metric): β < 0, p ≤ 0.05, R² ≥ 0.30.
- **NULL** (per metric): otherwise.

## 8. Cross-axis test (informational)

After computing window-ℓ̄, also compute Pearson r(window-ℓ̄, window-d̄_content) where d̄_content is the [[h-new-660-compression-tail-gradient|H-NEW-660]] 100-window content-cohesion vector.

- If |r| > 0.6 → content-cohesion may be DERIVATIVE of verse-length variation; [[h-new-660-compression-tail-gradient|H-NEW-660]] is partially confounded.
- If |r| < 0.4 → content-cohesion and verse-length are independent architectural axes.
- 0.4 ≤ |r| ≤ 0.6 → moderate co-variation; both axes contribute.

This Pearson-r test is INFORMATIONAL, not gating. It refines interpretation of [[h-new-660-compression-tail-gradient|H-NEW-660]].

## 9. Predicted ranges

Based on classical mufaṣṣal terminology (al-Suyūṭī, al-Zarkashī) and known terminal-surah brevity (Q 78-114 are mostly < 30 verses with very short verses):

- Words-per-verse: head ≈ 12-18, tail ≈ 4-6. Slope steeply negative.
- Letters-per-verse: head ≈ 60-90, tail ≈ 18-30. Slope steeply negative.
- Two-piece kink: likely near s=50 (Hijra hinge, mufaṣṣal entry) but possibly at s=65 (mufaṣṣal-qiṣār entry) or s=75. Pre-locked grid: {25, 35, 50, 65, 75}.
- R² (linear) expected ≈ 0.50-0.80.
- R² (two-piece) expected ≈ 0.80-0.95.

Pearson r(verse-length, content-cohesion) prediction:
- High prior expectation: r ∈ [0.5, 0.85]. Both quantities decrease together over s. If r > 0.85, content-cohesion is largely a verse-length artifact. If r < 0.4, axes are independent.

## 10. What would FALSIFY

- β ≥ 0 in either metric: gradient wrong → contradicts classical mufaṣṣal claim → would be a major finding.
- R² < 0.30 in either metric: verse-length is NOT 1-D in mushaf-position.
- |r(verse-length, content-d̄)| < 0.2 alongside both passing: verse-length and content-cohesion are entirely orthogonal axes.

## 11. Interpretation rules (committed BEFORE run)

- If [[h-new-770-verse-length-compression-tail|H-NEW-770]] PASSES with R² ≥ [[h-new-660-compression-tail-gradient|H-NEW-660]]'s 0.986 AND |r| > 0.85 → interpret [[h-new-660-compression-tail-gradient|H-NEW-660]] as DERIVATIVE-of-verse-length. Document confound.
- If [[h-new-770-verse-length-compression-tail|H-NEW-770]] PASSES with R² < [[h-new-660-compression-tail-gradient|H-NEW-660]]'s 0.986 AND |r| ∈ [0.5, 0.85] → both axes contribute; [[h-new-660-compression-tail-gradient|H-NEW-660]] stands as content-cohesion-specific signal beyond raw verse-length.
- If [[h-new-770-verse-length-compression-tail|H-NEW-770]] PASSES with |r| < 0.4 → independent axes; [[h-new-660-compression-tail-gradient|H-NEW-660]] is content-specific, verse-length is its own architectural feature.
- If [[h-new-770-verse-length-compression-tail|H-NEW-770]] NULL → [[h-new-660-compression-tail-gradient|H-NEW-660]] cannot be a verse-length artifact.

## 12. Files

- Script: `scripts/h_new_770_verse_length_compression_tail.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-770.json`
- Findings: `findings/phase-b-hypotheses/h-new-770-verse-length-compression-tail.md`
- Journal: `journal/h-new-770-run-1.md`

## 13. Methodology rules

- MW-1: instrument-prior — letters/words per verse, no-tashkeel.
- MW-3: alternative-models — linear, quadratic, two-piece (5-kink grid).
- MW-7 (post-hoc): not applicable — formal pre-registered test.
- PRE-REG-STANDARD-04: hypothesis, null, direction, Bonferroni-6, success criteria locked BEFORE run.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
