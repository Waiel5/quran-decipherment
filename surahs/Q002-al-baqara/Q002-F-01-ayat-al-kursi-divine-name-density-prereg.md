---
test_id: Q002-F-01
title: Ayat al-Kursī (Q 2:255) divine-name-density rank — empirical audit of "the greatest verse" claim
target_claim: al-Bukhārī ḥadīth #4008 (and Muslim) — Q 2:255 is "the greatest verse" of the Quran (aʿẓam āya).
date_locked: 2026-04-28
phase: B+
status: PRE-REGISTERED
seed: 20260428
---

# Pre-registration — Q002-F-01: Āyat al-Kursī divine-name-density

## 1. Hypothesis (LOCKED)

**H1**: Q 2:255 has divine-name density (count of distinct + total occurrences of the 99 names from `/Users/grey/Downloads/quran/data/asma-al-husna.txt`, normalised by verse word-length) at the EXTREME tail (rank ≤ 10 out of 6,236 by total density, rank ≤ 5 by distinct-name count) of the Quran corpus.

**H0 (null)**: Q 2:255 ranks no better than the 1st-percentile (i.e. rank > 62) for both metrics under the empirical distribution of all 6,236 verses.

**Direction-of-effect (LOCKED)**: Q 2:255 is in the TOP tail (HIGHER divine-name density than 99% of corpus verses).

## 2. Operationalisation

- **Text variant**: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (verses with sajda-marks stripped).
- **99-names list**: `/Users/grey/Downloads/quran/data/asma-al-husna.txt` (line-stripped, comments removed).
- **Matching rule (LOCKED)**: a name is "present" in a verse iff its no-tashkeel surface form appears as a *whole word* (whitespace- or punctuation-bounded). Multi-token names (e.g. "مالك الملك", "ذو الجلال والإكرام") are matched as adjacent tokens.
- **Two metrics**:
  - `total_density` = (count of name-occurrences in verse) / (word-count of verse).
  - `distinct_density` = (count of distinct names appearing) / (word-count of verse).
- **Tie-breaking**: by raw count of name-occurrences (descending), then by lower verse word-length.

## 3. Test statistic

- Rank of Q 2:255 in the sorted-descending list of `total_density` and `distinct_density` across all 6,236 verses.
- Also: raw counts (total occurrences, distinct names) for Q 2:255.

## 4. Success / failure criteria

- **VINDICATED**: Q 2:255 ranks in top-10 by `total_density` AND top-5 by `distinct_density`.
- **DIRECTIONAL**: top-1% (rank ≤ 62) on both metrics but failing the stronger thresholds.
- **NULL**: rank > 62 on either metric.
- **PRE-COMMIT VIOLATION**: Q 2:255 in BOTTOM tail (rank > 6174) — would falsify the hadith claim's empirical correlate.

## 5. Why this test is fair

al-Bukhārī's claim is theological (greatest verse). If it has any *empirical* correlate, the most natural is divine-name density: Q 2:255 names Allah explicitly (Allah, al-Ḥayy, al-Qayyūm, al-ʿAlī, al-ʿAẓīm) within 50 words. Density-rank is a falsifiable proxy.

## 6. Bonferroni

This is one of 5 novel Q 2 tests (Q002-F-01 through Q002-F-05). Family-α = 0.05/5 = 0.01. We use rank-based thresholds (top-10 of 6236 ≈ 0.16% < 0.01 family-α) and report uncorrected ranks for transparency.

## 7. Replication

- **MW-5 sub-replication**: re-run on `quran-min-tashkeel.json` (orthographic robustness). Result must agree on top-10 status.

## 8. MW-1..7

- **MW-1 (instrument-prior)**: density definition + name list LOCKED in this file before run.
- **MW-2 (corpus-prior)**: Use the entire 6,236-verse empirical distribution as null reference (no need for permutation null since this is a rank claim).
- **MW-3 (alternative-models)**: We compute BOTH total-density AND distinct-density as orthogonal model variants.
- **MW-4 (over-fitting)**: No fitted parameters.
- **MW-5 (replication)**: tashkeel sub-replication.
- **MW-6 (instrument-control)**: NULL-control: also report Q 2:255 word-length rank (i.e. is the result driven by Q 2:255 being short, not name-dense?).
- **MW-7 (post-hoc cap)**: This test is pre-registered before run; no post-hoc cap needed.

## 9. Output paths

- Script: `/Users/grey/Downloads/quran/scripts/Q002_F_01_ayat_al_kursi_divine_name_density.py`
- JSON: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/csv/Q002-F-01.json`
- Findings: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/Q002-F-01-ayat-al-kursi-divine-name-density.md`

*Locked 2026-04-28. SHA256 to be computed and embedded in script.*
