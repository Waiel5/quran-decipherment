# [[h-new-199-positional-ratios|H-NEW-199]] Results: Positional ratios of canonical celebrated verses

**Date:** 2026-04-17
**Seed:** 20260419
**Bonferroni k:** 2
**Pre-reg:** `[[h-new-199-positional-ratios|h-new-199]]-positional-ratios-prereg.md`
**Verdict (both pre-reg hypotheses):** **DEMOTED**
**Secondary descriptive finding:** **TERMINAL-CLUSTERING** (post-hoc, not promoted; flagged for future pre-registration)

## Data

12 pre-registered positions (ratio = verse / total_surah_verses):

| target | surah | verse | total | ratio |
|---|---|---|---|---|
| HASHR | 59 | 22 | 24 | 0.9167 |
| HASHR | 59 | 23 | 24 | 0.9583 |
| HASHR | 59 | 24 | 24 | 1.0000 |
| NUR | 24 | 35 | 64 | 0.5469 |
| KURSI | 2 | 255 | 286 | 0.8916 |
| IKHLAS | 112 | 1 | 4 | 0.2500 |
| IKHLAS | 112 | 2 | 4 | 0.5000 |
| IKHLAS | 112 | 3 | 4 | 0.7500 |
| IKHLAS | 112 | 4 | 4 | 1.0000 |
| FATIHA | 1 | 1 | 7 | 0.1429 |
| FATIHA | 1 | 4 | 7 | 0.5714 |
| FATIHA | 1 | 7 | 7 | 1.0000 |

Mean ratio = 0.7106. Sample variance = 0.0922 (uniform null = 0.0833). Slight over-dispersion
relative to Uniform(0,1), consistent with bimodal clustering at endpoints rather than
concentration at a middle value.

## Pre-registered tests

| anchor | value | hits within 0.05 | expected | binomial p (one-sided) | α_corr | decision |
|---|---|---|---|---|---|---|
| golden ratio (φ−1) | 0.6180 | 1 / 12 | 1.20 | 0.7176 | 0.025 | **DEMOTED** |
| two-thirds | 0.6667 | 0 / 12 | 1.20 | 1.0 | 0.025 | **DEMOTED** |

Only one position (Q 1:4, al-Fātiḥa's central verse `iyyāka naʿbudu wa-iyyāka nastaʿīn`,
ratio 0.5714) falls within the φ−1 band, and zero fall within the 2/3 band. Neither cluster
is detectable above chance; both pre-registered hypotheses fail their promotion criteria.

## Descriptive observations (NOT promoted — post-hoc)

Histogram of ratios by 0.10 bin:

```
[0.0-0.1]  0
[0.1-0.2]  1   Q1:1 (al-Fātiḥa opener — but this is Basmala)
[0.2-0.3]  1   Q112:1
[0.3-0.4]  0
[0.4-0.5]  0
[0.5-0.6]  3   Q24:35, Q112:2, Q1:4
[0.6-0.7]  0
[0.7-0.8]  1   Q112:3
[0.8-0.9]  1   Q2:255
[0.9-1.0]  5   Q59:22, Q59:23, Q59:24, Q112:4, Q1:7
```

**5 of 12 positions (41.7%) sit in the top decile of their surah.** Under Uniform(0,1) the
expected count is 1.2, and the one-sided binomial P(X≥5 | n=12, p=0.10) ≈ 0.0043 — would
clear Bonferroni **if** this had been pre-registered. It was not. Logging this as a candidate
for [[h-new-200-name-class-predictor|H-NEW-200]]+ with an independent extension-set.

Note: 3 of the 5 terminal hits are the three consecutive final verses of Q 59 (HASHR is by
definition clustered at the end of its surah — those three atoms are not independent tests,
so the effective count is closer to 3 independent hits out of the 10-position set excluding
the two extra HASHR verses, giving P(X≥3 | n=10, p=0.10) ≈ 0.0702, not significant). The
apparent significance is therefore partly an artefact of counting the Ḥashr closing triad
as three positions.

**Cleaner descriptive statement:** celebrated devotional verses tend to fall at or very
near the *end* of their surah — ending-position is a natural sanctity locus in the Quranic
architecture (khātima). This is a known rhetorical intuition (classical ʿilm al-munāsaba
treats openings and closings as specially weighted) rather than a φ- or ⅔-based structure.

## Conclusions

1. **Pre-registered:** neither golden-ratio clustering nor two-thirds clustering holds for
   the canonical celebrated-verse set. Both hypotheses demote under Bonferroni α = 0.025.
2. **Descriptive:** the tested set trends toward the surah terminus, not toward any "magic"
   interior ratio. This is consistent with classical understanding of khātima-emphasis and
   with the fact that three of the five celebrated passages (Ḥashr, Ikhlāṣ verse 4, Fātiḥa
   verse 7) literally end their surah — an ascertained textual feature, not a discovered
   pattern.
3. **Extension candidate:** pre-register a broader devotional set (e.g., Muʿawwidhatān,
   Yā-Sīn opening/closing, Ṣād verse 38:26, first/last of each ḥizb) with independent data
   and re-test "top-decile clustering" as a primary hypothesis.

## Outputs

- `[[h-new-199-positional-ratios|h-new-199]]-positional-ratios-prereg.md` (pre-reg, this run)
- `[[h-new-199-positional-ratios|h-new-199]]-positional-ratios.md` (this file)
- `[[h-new-199-positional-ratios|h-new-199]]-work/analyze.py` (deterministic, seed-locked)
- `[[h-new-199-positional-ratios|h-new-199]]-work/results.json` (machine-readable)
