# H-NEW-770 run-1 journal — verse-length compression-tail

**Date**: 2026-04-28
**Seed**: 20260446
**Pre-reg SHA**: cd270d5b87ffad07712ba5eed75cc6746774b0e8b17deb0d7cbf64fda17a6989

## Pre-commit (before run)

- Direction: β < 0 (verse-length decreases toward terminus). Predicted by classical mufaṣṣal terminology.
- Kink expected near s=50 (Hijra hinge / mufaṣṣal entry).
- Predicted ranges: words/verse 12-18 → 4-6; letters/verse 60-90 → 18-30.
- Predicted Pearson r(verse-length, content-d̄) ∈ [0.5, 0.85]. Threshold 0.85 set as "verse-length artifact" boundary.

## Garden-of-forking-paths log

Choices locked in prereg before any computation:
- Letter-counting convention: all non-whitespace chars in no-tashkeel JSON (`text` field). Chose this because the no-tashkeel file already strips diacritics; counting non-whitespace gives a clean rasm-letter count.
- Word-counting convention: whitespace-split tokens. Standard.
- Per-surah aggregation: arithmetic mean of per-verse counts. Could have used median; mean is the standard convention.
- Window K=15: inherited from H-NEW-660 for direct comparability. No K-sweep — that is queued as a separate test.
- Kink grid {25, 35, 50, 65, 75}: 5 candidates spanning the mushaf. Pre-locked.
- Permutation = surah-shuffle (114 permutations preserve marginal distribution of per-surah verse-lengths). 10000 perms.
- Bonferroni-6: 3 models × 2 metrics. Conservative because the two metrics are nearly co-linear (r≈0.9999), but pre-locked.

## Run

```
$ python3 scripts/h_new_770_verse_length_compression_tail.py
```

(takes ~30-60s for 10000 perms × 2 metrics × 3 models with pure Python arithmetic)

## Headline results

| Metric | Primary | R² | β_lin | Perm p |
|:--|:--|:-:|:-:|:-:|
| letters/verse | two-piece-kink-50 | 0.8071 | -0.5603 | 0.00070 |
| words/verse | two-piece-kink-50 | 0.8105 | -0.1418 | 0.00070 |

**Both STRICT PASS** at α_bon = 0.00833 (Bonferroni-6).

Per-surah examples:
- Q1: 20.4 letters/verse, 4.1 words/verse (al-Fātiḥa is short despite Meccan opener — outlier)
- Q2: 93.5 letters/verse, 23.2 words/verse
- Q108: 14.3 letters/verse, 3.3 words/verse
- Q114: 13.3 letters/verse, 3.3 words/verse

Window range:
- letters/verse: 75 → 16.5 (4.5× compression)
- words/verse: 18.6 → 3.9 (4.7× compression)
- (vs H-NEW-660 content-d̄: 0.99 → 0.32 = 3.1× compression)

## Cross-axis Pearson (vs H-NEW-660 content-d̄)

- r(letters/verse, content-d̄) = +0.8719
- r(words/verse, content-d̄) = +0.8730

**Both barely cross the pre-committed |r| > 0.85 threshold for "verse-length artifact" concern.** This forced careful decomposition.

## Decomposition

```
content_d ~ words_per_verse (univariate):     R² = 0.7621
residual ~ s (linear):                        R² = 0.0611, β=-0.00085
residual ~ s (two-piece-kink-50):             R² = 0.1802, β=-0.00258

content_d ~ kink50_post (H-NEW-660 alone):    R² = 0.9860
content_d ~ words + kink50_post:              R² = 0.9884  (Δ=+0.0024)
```

**Critical reading**: the H-NEW-660 single-parameter law (kink-50 post-position) ALREADY captures essentially the entire joint compression-tail signal. Adding verse-length adds only 0.24 R² points. Verse-length and content-cohesion are co-effects of post-kink mushaf-position.

## Verdict

The compression-tail is a multi-feature architectural property. Content-cohesion (H-NEW-660 R²=0.986) and verse-length (H-NEW-770 R²≈0.81) both follow the two-piece-kink-at-s=50 law. They are co-aligned (r≈0.87) but not redundant: ~18% of post-kink content variance is residual-to-verse-length and still position-structured.

H-NEW-660 is **NOT derivative of verse-length** — but it is **partially co-variant** with it (76% univariate overlap). The cleaner reading: post-kink mushaf-position is the COMMON CAUSE of both axes.

## Disciplinary notes

- ONE text. Permutation null was equal-prominence per H-NEW-660 convention; null R² mean ~0.06 for two-piece, observed 0.81 → far from null.
- The result PARTIALLY refines H-NEW-660 — the framing of H-NEW-660 as a "content-cohesion law" should be broadened to "compression-tail law that governs multiple correlated features." Documented in §4 of findings.
- Bonferroni-6 is conservative because metrics are nearly co-linear; tightening to Bonferroni-3 (one per metric primary-model) would still pass at p=0.0007 < 0.0167. Bonferroni TIGHTENING (per project memory feedback_bonferroni_tightening_vs_loosening.md) self-verifies; we keep the original committed Bonferroni-6.

## Files written

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-770-verse-length-compression-tail-prereg.md`
- `/Users/grey/Downloads/quran/scripts/h_new_770_verse_length_compression_tail.py`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-770.json`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-770-verse-length-compression-tail.md`
- this journal

*Bismillāhi al-Raḥmāni al-Raḥīm.*
