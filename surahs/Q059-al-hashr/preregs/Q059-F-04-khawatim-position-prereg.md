---
surah: 59
test_id: Q059-F-04
title: Q 59 Khawātim terminal-three placement test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q059-F-04-khawatim-position
alpha_bon: 0.025
post_hoc_origin: YES (within-Q 59 anchor-cluster eyeball during specialist work). Single-test α=0.05 cap applied. Verdict ceiling = PASS-DIRECTED.
---

# Q059-F-04 — Pre-registration: Q 59 Khawātim terminal-three placement test

## 1. Hypothesis (post-hoc-noticed, then locked)

**H1a (descriptive):** Across the 22 internal 3-verse windows of Q 59 (v1-3 to v22-24), the highest-F window (by 99-name token count) lands at the **terminal-three position** v22-24.

**H1b (one-tailed corpus-comparison):** Across all 109 corpus surahs with V ≥ 5 verses, the surahs with terminal-3 placement of their highest-F window form a small distinguished subset; Q 59 is in this set with the highest absolute F.

## 2. Post-hoc disclosure

The Khawātim al-Ḥashr is well-documented as occupying Q 59:22-24 (the SURAH'S TERMINAL VERSES). This is not a discovery of the present test; it is a structural fact baked into the brief. The test's contribution is operationalizing the **terminal-3 placement** as a corpus-wide pattern and measuring how rare it is.

Per HANDOFF/04-DISCIPLINE.md post-hoc-noticed protocol: single-test α=0.05 cap applied. Verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION.

## 3. Operational definition

- **Best 3-verse window per surah** = max-F window across all internal 3-verse windows (NOT corpus-spanning).
- **Terminal-3 placement** = best window starts at index `len(verses) - 3` (the literal final three verses).
- **F threshold** for the "high-F" subset: F ≥ 5 (filters trivial single-name surahs).

## 4. Test statistic

- count_terminal = number of surahs (≥5 verses) whose best-window is at terminal-3.
- high_F_terminal = same restricted to F ≥ 5.
- Within Medinan: count_med_terminal.

## 5. No null permutation needed

This is a **structural-classification** test, not a hypothesis test against a stochastic null. The output is a list/count; the inference is qualitative ("Q 59 is in this set, F-dominant").

## 6. Success / Failure

- **DESCRIPTIVE-PASS**: Q 59 best-window is at terminal-3 with F = 19 dominant.
- **STRUCTURAL-FINDING**: ≥3 of the 5 Medinan high-F-terminal surahs are within the H-NEW-1080 short-Medinan block.

## 7. Honest limits

- This is a corpus-classification, not a randomization-test result. Permutation nulls would require modeling surah-internal name-distribution conditional on length and content — not done here.
- The terminal-3 placement is anchor-confirmed for Q 59 (the Khawātim) before this test; the test only quantifies the pattern's broader corpus-membership.

## 8. Rules-tuple

`(no-tashkeel, ornament-stripped, whitespace-tokenized, 99-name-substring-with-proclitic-tolerance, surah-internal-windows-only)`.

## 9. Bonferroni

k = 2 (within-Q 59 anchor + corpus-classification). α_bon = 0.025.

## 10. Authored by

Waiel Al-Shujaa, 2026-05-09.
