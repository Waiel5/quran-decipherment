# [[h-new-199-positional-ratios|H-NEW-199]] Pre-registration: Positional ratios of canonical celebrated verses

**Date:** 2026-04-17
**Seed:** 20260419
**Bonferroni k:** 2 (two independent "magic-ratio" hypotheses tested)
**Author:** autonomous agent ([[h-new-199-positional-ratios|H-NEW-199]])

## Question

Classical and folk devotional traditions single out a small set of verses as especially celebrated:
Khawātim al-Ḥashr (Q 59:22–24), Āyat al-Nūr (Q 24:35), Āyat al-Kursī (Q 2:255), Sūrat al-Ikhlāṣ
(Q 112, treated as verse 1 = whole surah proxy), and al-Fātiḥa (Q 1, whole surah).

**Question:** Do their *positions within their surah* — defined as `position / total_verses` —
cluster at any distinguished ratio? In particular we pre-register two candidate ratios:

- H1 (golden): ratios near φ−1 = 0.6180 (distance ≤ 0.05)
- H2 (two-thirds): ratios near 2/3 = 0.6667 (distance ≤ 0.05)

## Data

- Verse-count table: `/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv`
  (114 surahs, Hafs ʿAn ʿĀṣim, standard Cairo 1924 numbering — the project's single canonical corpus).
- No text retrieval needed; analysis is purely positional.

## Target set (frozen before analysis)

For each celebrated verse we pre-register the *minimum* position, *maximum* position, and a
*representative* ratio. For multi-verse passages we test both endpoints and the midpoint.

| code | surah | verse(s) | total | positions tested |
|---|---|---|---|---|
| HASHR1 | 59 | 22 | 24 | 22/24 |
| HASHR2 | 59 | 23 | 24 | 23/24 |
| HASHR3 | 59 | 24 | 24 | 24/24 |
| NUR    | 24 | 35 | 64 | 35/64 |
| KURSI  | 2  | 255 | 286 | 255/286 |
| IKHLAS | 112 | 1..4 (whole surah) | 4 | 1/4, 2/4, 3/4, 4/4 |
| FATIHA | 1 | 1..7 (whole surah) | 7 | 1/7, 4/7, 7/7 |

## Test statistics

For each target ratio r and each hypothesis anchor a ∈ {φ−1, 2/3}:

1. **Anchor-proximity test.** Let d_i = |r_i − a|. Count how many of the N tested
   positions have d_i ≤ 0.05. Under the null (ratios uniform on [0,1]) the probability
   of any single position being within 0.05 of a is 0.10. Use a one-sided binomial test
   with k successes out of N trials against p₀ = 0.10.

2. **Clustering test.** Compute the sample variance of r_i. Under uniform null on [0,1]
   the expected variance is 1/12 ≈ 0.0833. We do NOT formally test this (no pre-registered
   statistic); it is reported descriptively only.

## Decision rule

- Per-test α = 0.05.
- Bonferroni-corrected α = 0.05 / 2 = 0.025 (k=2 for the two anchor hypotheses).
- **Promote** the hypothesis iff the binomial p-value is ≤ 0.025 AND at least 3 of the
  tested positions are within 0.05 of the anchor (to avoid a single coincidence driving
  the result).
- Otherwise **demote**.

## Garden-of-forking-paths declaration

- Target set was chosen from the most-cited devotional set BEFORE seeing any ratios.
- Anchors φ−1 and 2/3 were fixed before computing any ratio.
- Tolerance 0.05 was fixed before analysis (this is ≈ the precision one would get from
  rounding to one decimal place, a natural scale for "about two-thirds of the way through").
- The 7 targets expand to 14 tested positions (3+1+1+4+3 = 12 unique; we pre-register all 12).

Actually, counting: HASHR 3 + NUR 1 + KURSI 1 + IKHLAS 4 + FATIHA 3 = 12 positions.

## Null framing

H0: celebrated-verse positions behave as if sampled uniformly at random from their surah
(every verse position is equally "celebrate-able"). Under H0, r_i = position/total is
approximately uniform on (0, 1], and the probability of being within 0.05 of any fixed
anchor a ∈ (0.05, 0.95) is exactly 0.10.

## Outputs

- `[[h-new-199-positional-ratios|h-new-199]]-positional-ratios-prereg.md` (this file)
- `[[h-new-199-positional-ratios|h-new-199]]-positional-ratios.md` (results)
- `[[h-new-199-positional-ratios|h-new-199]]-work/analyze.py` (script)
- `[[h-new-199-positional-ratios|h-new-199]]-work/results.json` (machine-readable)
