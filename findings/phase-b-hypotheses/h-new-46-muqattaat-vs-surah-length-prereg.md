---
id: H-NEW-46
title: Muqaṭṭaʿāt presence vs surah length — does muqaṭṭaʿāt openings concentrate in long surahs above what would be predicted by random selection conditioned on length?
status: PRE-REGISTERED 2026-04-16
spec_locked_at: 2026-04-16 (BEFORE running null model; eyeball: top-3 longest surahs (Q 2, Q 7, Q 26) all open with muqaṭṭaʿāt — disclosed)
bonferroni_family: 2026-04-16-Wave-Muqattaat-Extended
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: (hafs-kufan; verse-count metric)
primary_data: 114 surah lengths (verse counts) + 29 muqaṭṭaʿāt-opened indicator
---

# [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] — Muqaṭṭaʿāt vs Surah Length

## Question

Are muqaṭṭaʿāt-opened surahs significantly LONGER than non-muqaṭṭaʿāt-opened surahs, beyond what uniform random 29-from-114 selection would predict?

## Garden-of-forking-paths disclosure

Eyeball: Q 2 (286 verses, longest), Q 7 (206 v.), Q 26 (227 v.) all open with muqaṭṭaʿāt. The top-2 by length (Q 2 and Q 7 if you exclude the medium ones) are muqaṭṭaʿāt-openers. This was noticed before the test was specified.

Honest protection: lock the 4-cell test family BEFORE running the null. Not all four cells are eyeball-derived; only cell 1 (mean-length) is post-hoc-flagged.

## The 4 pre-registered test cells

For each, the data is the 29 muqaṭṭaʿāt-opened surah indices and their verse counts; null = 10⁵ uniform random samples of 29 surahs from {1..114}.

### Cell 1 — Mean verse-count enrichment (eyeball-noticed)

Test statistic: mean verse-count of muqaṭṭaʿāt surahs vs mean of random-29-from-114.
Direction: one-sided upper (muqaṭṭaʿāt longer).

### Cell 2 — Median verse-count enrichment

Test statistic: median verse-count.
Direction: two-sided.

### Cell 3 — Top-K representation

Test statistic: how many of the 29 muqaṭṭaʿāt are in the top-29 by verse-count?
Direction: one-sided upper.

### Cell 4 — Tail-K (shortest) suppression

Test statistic: how many of the 29 muqaṭṭaʿāt are in the bottom-29 by verse-count?
Direction: one-sided lower.

## Null model

10⁵ uniform random samples; seed = 20260416. For each, compute all 4 cell statistics. Empirical p.

## MW-5 positive control

Pipeline already validated by [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] (same null engine). Spot-check: if we deliberately pick the 29 longest surahs as our "fake muqaṭṭaʿāt set", cell 1 should give p < 1e-4.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| 0 cells significant at α=0.0125 | NULL |
| 1 cell significant | EXPLORATORY (1-cell pass on a length-correlated family) |
| 2-3 cells significant | PARTIAL-PASS |
| All 4 cells significant | STRONG-PASS — muqaṭṭaʿāt concentrate in long surahs across all length-related axes |

## Mechanism interpretation

If pass: the muqaṭṭaʿāt assignment correlates with surah length. Possible mechanisms:
- Long surahs are typically Medinan or middle-Meccan — chronological correlate
- Long surahs may have more "structural authority" calling for a distinctive opener
- The 14 muqaṭṭaʿāt letter-set encodes surah-content information that correlates with length

If null: muqaṭṭaʿāt assignment is length-independent.

## Integrity

- Cell 1 post-hoc flagged.
- Bonferroni k=4 declared before null design.
- Publish all 4 cells regardless of direction.
