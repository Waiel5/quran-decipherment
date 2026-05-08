---
surah: 11
test_id: Q011-F-02
title: Hūd-narrative elaboration Q 11:50-60 vs Q 7:65-72
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_family: Q011-F-02
bonferroni_k: 4
alpha_bon: 0.0125
n_perm: 0
---

# Q011-F-02 — Pre-registration: Hūd-narrative elaboration

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, direction LOCKED on each axis):** The Hūd-narrative in
Q 11:50-60 is more **structurally elaborated** than the Hūd-narrative in
Q 7:65-72 on **all four** of the following axes:

- **A. Verse count**: Q 11 (50–60 = 11 vv) > Q 7 (65–72 = 8 vv).
- **B. Token count** (`split` over whitespace, `quran-no-tashkeel.json`):
  tokens(Q 11:50-60) > tokens(Q 7:65-72).
- **C. Distinct-root count** (QAC v0.4 root annotations,
  `data/morphology/quranic-corpus-morphology-0.4.txt`): Q 11 > Q 7.
- **D. Direct-speech density** (count of `قال`/`قالوا`/`قالت` instances per
  verse in the block): Q 11 > Q 7.

**H0:** Q 11 ≤ Q 7 on ≥ 2 of the 4 axes.

**Direction:** Q 11 > Q 7 on all 4 axes (LOCKED).

## 2. Operational definition

- Q 11 Hūd-narrative block: verses 11:50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60
  (inclusive; 11 verses).
- Q 7 Hūd-narrative block: verses 7:65, 66, 67, 68, 69, 70, 71, 72
  (inclusive; 8 verses).
- **A. Verse count**: 11 vs 8 (deterministic, no statistical test).
- **B. Token count**: split text on whitespace + Arabic punctuation
  `۞ ۚ ۗ ۖ ۘ ۙ` and count non-empty tokens. Sum across the verse block.
- **C. Distinct-root count**: parse QAC v0.4; for each `(surah, verse, word, segment)`
  tuple in the block, collect the `ROOT:xxx` feature; report the size of the
  set of distinct root letters across the block.
- **D. Direct-speech density**: count occurrences of the regex
  `(?:^|\s)(قال|قالوا|قالت|قلنا|قل)(?=\s|$)` per verse, sum, divide by verse
  count. Compare per-verse densities (NOT raw sums; controls for the verse-count
  size confound).

## 3. Test statistic

For each axis, compute the value on Q 11 and Q 7, take the **per-axis
direction match indicator** (1 if Q 11 > Q 7, 0 otherwise). Report:

- 4 indicators
- Whether all 4 = 1 (locked H1).

## 4. Success / Failure

| Outcome | Verdict |
|:--|:--|
| All 4 indicators = 1 AND axis-D direction stable under per-verse normalization | **CONFIRMED** (all 4 axes one-direction) |
| 3 of 4 indicators = 1 | DIRECTIONAL |
| ≤ 2 of 4 indicators = 1 | NULL |
| Q 11 strongly LESS elaborated (0 of 4) | Pre-commit violation; NULL with full prominence |

## 5. Bonferroni context

- Family of k=4 sub-axes; **direction-locked** binary indicators.
- α_bon = 0.0125 / axis ⇒ for the descriptive direction-match, this is
  irrelevant since we are not p-testing each axis. The 4-axis joint claim
  is a single composite verdict at α=0.05 — the all-4-must-pass aggregator
  IS the multiple-comparisons protection (4 chances to falsify, 1 chance to
  vindicate).

## 6. Honest limits known a priori

- The Hūd-narrative-block boundaries are inherited from al-Biqāʿī's
  block-segmentation in Q 11 and from cross-finding analyses for Q 7.
  Different scholars draw the boundary slightly differently
  (e.g., Q 7:65–72 vs 7:65–73; Q 11:50–60 vs 11:50–62). The pre-locked
  bounds are 11:50-60 (al-Biqāʿī) and 7:65-72 (the verse block ending
  with the destruction of the disbelievers, parallel to 11:60).
- A "more elaborated" prediction is a substantive content claim that maps
  onto al-Biqāʿī's *Naẓm al-Durar* observation that Hūd's narrative is
  "central" in Q 11 but "transit" in Q 7. The empirical test honors this
  qualitative difference.
- Per-verse density (axis D) is the size-controlled version. If Q 11's
  raw direct-speech count is higher BUT per-verse density is lower (i.e., Q 7
  is denser per verse but Q 11 has more total verses), the axis-D verdict
  uses the per-verse density (CONSERVATIVE).

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, regex-word-boundary, QAC-v0.4-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. SHA256 lock

Computed at run-time. Embedded in `scripts/Q011_F_02_hud_narrative_elaboration.py`.
