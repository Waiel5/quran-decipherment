---
finding_id: Q050-F-07
date_locked: 2026-05-09
phase: B+
direction: LOCKED
seed: 20260509
---

# Q050-F-07 — Pre-registration: Q 50 ق-letter density vs 30-50-verse Meccan surahs

## Hypothesis

Among the 16 Meccan surahs of 30-50 verses (inclusive), **Q 50 Qāf has the HIGHEST per-letter ق density**. This is a Meccan-length-matched class-rank test, complementary to Q050-F-03 (length-matched-random-window null) but using a more class-specific reference: same revelation-period (Meccan), same length-bracket (30-50 verses).

This is a direct test of the classical iʿjāz claim — explicitly transmitted via al-Rāzī (`razi-muqattaat-surah-qaf.md`) — that **Q 50 is saturated with ق, just as Q 38 is saturated with ṣād** (the parallel classical observation about Q 38).

## Class membership

The 16 Meccan 30-50-verse surahs (computed from `quran-text/quran-no-tashkeel.json` 'type' field):

{Q 31 Luqmān (34), Q 32 al-Sajda (30), Q 35 Fāṭir (45), Q 45 al-Jāthiya (37), Q 46 al-Aḥqāf (35), **Q 50 Qāf (45)**, Q 52 al-Ṭūr (49), Q 67 al-Mulk (30), Q 70 al-Maʿārij (44), Q 75 al-Qiyāma (40), Q 77 al-Mursalāt (50), Q 78 al-Nabaʾ (40), Q 79 al-Nāziʿāt (46), Q 80 ʿAbasa (42), Q 83 al-Muṭaffifīn (36), Q 89 al-Fajr (30)}

n_class = 16.

## Pre-registered direction

**Q 50 RANK = 1** (highest ق density per total-letter-count among the 16 surahs).

Success criteria:
- Q 50 rank = 1 (strict): CONFIRMED-RANK-1
- Q 50 rank = 2 or 3 (top decile of 16): DIRECTIONAL-TOP-3
- Q 50 rank ≥ 4: NULL (and pre-commit-direction violation if rank > 8 — i.e., below median)

## Null and significance

- For class-rank-1 verdict: no permutation needed; rank is a direct enumeration result.
- For statistical significance, additionally compute:
  - Permutation null: randomly relabel the 16 surahs' ق counts onto their letter-totals (10000 perms, seed 20260509); compute P(Q 50 obtains rank 1) under permutation.
  - Bonferroni-1 (this is a single test); α = 0.05.

## Data and rules-tuple

- Text: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (Hafs-Kufan, mushaf-marks-stripped, basmala-not-counted-in-Q-other-than-Q1).
- Letter counting: graphemes (Arabic Unicode), strip Tatweel U+0640, do NOT normalize alif variants for the ق-target (ق is unambiguous), strip whitespace and digits.
- Rules-tuple: (no-tashkeel, grapheme-counting, mushaf-marks-stripped, basmala-not-counted-outside-Q1, Hafs-Kufan, Mashriqi).
- Bonferroni: k = 1 (single test), α = 0.05.
- Seed: 20260509.
- n_perm: 10000.

## SHA lock

Compute SHA256 of THIS file after writing; embed in `scripts/Q050_F_07_qaf_density_vs_meccan_30_50.py`. Verify at runtime; fail-fast on mismatch.

## Output

- JSON: `surahs/Q050-qaf/csv/Q050-F-07.json` with:
  - finding_id, prereg_sha256, seed, rules_tuple, class_definition
  - per_surah_rates: list of (surah_id, name, n_letters, qaf_count, qaf_rate)
  - q50_rank, q50_rate
  - perm_p_rank_1
  - verdict
  - pre_commit_violation flag

## Honest limits

- The 16-surah reference class is itself a length-and-period subset; the broader null (Q050-F-03 length-matched-random-window) showed Q 50 ق density at z = +3.34, p = 10⁻⁴. This test is a different framing — class-rank within a fair-comparable reference.
- The CLASSICAL claim is qualitative ("Q 50 is saturated with ق"). The empirical rank-1 result is the strongest possible single-class quantitative replication.
- This test could in principle FAIL if some other 30-50-verse Meccan surah happens to have higher ق density (e.g., if a surah is itself topically about something with frequent ق-rooted words). Under the locked direction, that outcome = NULL.
