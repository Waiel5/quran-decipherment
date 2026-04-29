---
finding_id: Q036-F-03
title: "Q 36:82 *kun-fa-yakūn* climax-position uniqueness corpus-wide"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 20260428
n_perm: 0  (deterministic check)
bonferroni_k: 1
alpha_raw: 0.05
direction: positive (Q 36:82 expected to be positioned >95% through Q 36; uniquely so among the 8 corpus *kun-fa-yakūn* verses)
---

# Q036-F-03 — Q 36:82 *kun-fa-yakūn* is the corpus's only climax-positioned *kun-fa-yakūn* verse

## Hypothesis

The classical exegetical observation (al-Rāzī Q 36:82, al-Zamakhsharī Q 36:82, Ibn Kathīr Q 36:82) that Q 36 is "constructed around" the *kun-fa-yakūn* climax operationalises as: of the 8 corpus *kun fa-yakūn* verses, **Q 36:82 is the only one positioned at >95% through its surah**, with the next-closest instance (Q 40:68) at <90%.

## Locked operationalisation

Search `quran-text/quran-no-tashkeel.json` for the orthographic-exact phrase `كن فيكون`. Record (surah, verse, total-verses, position = verse_id / total_verses) for each match.

The corpus-wide instance set is finite and known to be 8 verses (verified pre-pre-reg from the same datafile):
- Q 2:117, Q 3:47, Q 3:59, Q 6:73, Q 16:40, Q 19:35, Q 36:82, Q 40:68.

The locked test:
- Q 36:82 position-in-surah > 95%: TRUE / FALSE.
- The 7 other instances' max position-in-surah < 90%: TRUE / FALSE.
- The gap between Q 36:82 and the next-closest is ≥ 10 percentage points: TRUE / FALSE.

## Rules-tuple

`(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`. Cross-validate against `quran-text/quran-min-tashkeel.json` for orthographic stability.

## Direction (LOCKED)

The direction is **POSITIVE**: Q 36:82 expected at >95%; others below 90%; gap ≥ 10pp.

## Success criteria

- All 3 conditions TRUE: **CONFIRMED**.
- 2 of 3: **DIRECTIONAL**.
- ≤ 1 of 3: **NULL**.

## Discriminating cross-check

The 8 corpus instances and their positions can be tabulated; the test is deterministic. The "discriminating" element is the comparison to the next-closest instance.

## Bonferroni context

This is a single test; α_raw = 0.05 is the threshold. There is no permutation null (the test is deterministic on the corpus's 8 *kun fa-yakūn* verses); the threshold is the descriptive-uniqueness criterion.

## Output files

- Pre-reg: `preregs/Q036-F-03-kun-fa-yakun-climax-position-prereg.md`
- Script: `scripts/Q036_F_03_kun_fa_yakun_climax.py`
- JSON: `csv/Q036-F-03.json`
- Findings: `06-novel-findings.md` Q036-F-03.
