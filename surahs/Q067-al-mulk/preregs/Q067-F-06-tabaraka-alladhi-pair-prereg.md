---
finding_id: Q067-F-06
title: tabāraka alladhī verse-pair Q 67:1 ↔ Q 25:1 ↔ Q 64:1 — are these openers tighter on Fisher-Rao than length-matched null?
date_locked: 2026-05-09
phase: B+
seed: 20260509
n_perm: 10000
rules_tuple: (no-tashkeel, QAC-stem-roots, K=500, Dirichlet α=0.5, FR-distance verse-level over root-presence indicator, Hafs-Kufan)
---

# Q067-F-06 — Pre-registration

## Hypothesis

Three surahs open with the doxological *tabāraka alladhī* (perfect of *brk* + relative pronoun): Q 25 al-Furqān (v. 1), Q 64 al-Taghābun (v. 1), Q 67 al-Mulk (v. 1). If the *tabāraka alladhī* opener marks a shared theological-rhetorical signature, then the three opening verses should sit closer to each other in lexical/root space than a length-matched null draw from the corpus.

NB: Q 25 contains additional internal *tabāraka alladhī* occurrences at v. 10 and v. 61, but we restrict the verse-pair test to v. 1-openers only (the pre-registered comparison set is exactly {Q 25:1, Q 64:1, Q 67:1}).

## Pre-registered direction (LOCKED)

**TIGHTER**: mean pairwise Fisher-Rao distance among the 3 *tabāraka alladhī* opener-verses is **smaller** than the empirical 5th-percentile of length-matched null triplets.

## Locked parameters

- **Comparison set**: verses {Q 25:1, Q 64:1, Q 67:1}.
- **Verse vector**: per-verse QAC root-presence indicator over the corpus's top-K=500 roots (binary 0/1 presence, no token-count weighting; rationale: verses are too short for stable count distributions).
- **Distance**: Fisher-Rao on Dirichlet-smoothed (α=0.5) normalized count vectors.
- **Null**: 10000 random triplets of corpus verses with length matched to {Q 25:1, Q 64:1, Q 67:1} word-count tuple ±1 word per verse.
- **Length-matching tolerance**: ±1 word per verse from the target triplet (5, 11, 9 words after no-tashkeel normalization — to be computed at runtime; tolerance applies to the actual measured word-counts).
- **Test statistic**: mean pairwise FR distance across the 3 verses (3 pairs).

## Success criterion

**TIGHTER**:
- Observed mean FR_pair < null 5th percentile (p_perm < 0.05).

**NULL**:
- Observed mean FR_pair ≥ null 5th percentile.

## MW protections

- **MW-1 (instrument-prior)**: FR on Dirichlet-smoothed verse-root-presence vectors.
- **MW-2 (corpus-prior)**: 10000 length-matched null triplets.
- **MW-3 (alternative-models)**: Re-test with all 4 occurrences of *tabāraka alladhī* (Q 25:1, 25:10, 25:61, 67:1) — descriptive secondary.
- **MW-6 (instrument-control)**: report observed mean FR_pair and full null distribution quantiles.
- **MW-7 (post-hoc cap)**: pre-reg locks the 3-verse opener set BEFORE running; no expansion post-hoc except as descriptive secondary.

## Failure conditions

- p_perm ≥ 0.05: NULL — *tabāraka alladhī* opener signature does NOT generate verse-level lexical cohesion beyond chance.
- Reversed direction (observed > null median): NULL with pre-commit-violation flag.

## Honest limits

- Verses are short (5-11 words); the root-presence vector is sparse. Statistical power for verse-level FR is intrinsically modest.
- The 3-verse comparison set has only 3 pairs; the test statistic is unstable. Length-matched null controls for this.
- Cross-tashkeel sensitivity not tested at the verse level (rules-tuple-conditional).

## Output

`/Users/grey/Downloads/quran/surahs/Q067-al-mulk/csv/Q067-F-06.json`
