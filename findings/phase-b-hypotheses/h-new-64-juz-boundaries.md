---
id: H-NEW-64
title: Do canonical juzʾ (30-part) boundaries correspond to natural structural breaks?
phase: B
status: COMPLETE
date: 2026-04-15
agent: h-new-64-specialist
seed: 20260416
verdict: NULL
positive_control: VALID (3 of 4 axes exceed observed)
parent: project_quran_decipherment
prereg: h-new-64-juz-boundaries-prereg.md
---

# [[h-new-64-juz-boundaries|H-NEW-64]] — Juzʾ Boundaries vs Structural Breaks (NULL)

## Bottom line

The canonical 30-juzʾ partition does **NOT** correspond to natural
structural breaks in the Quranic text under any of the four
pre-registered axes (topic shift, rhyme-class shift, narrative-pivot,
length discontinuity), nor under the joint test. The juzʾ system
appears to be **purely length-driven**, consistent with its origin as
an editorial recitation aid, not as a structural exegesis of the text.

The positive control is VALID (surah-boundary positions, sampled to
match cardinality, exceed observed juzʾ-boundary statistics on 3 of 4
axes — A, B, D — with p < 0.001 on each, confirming the pipeline
detects real structural breaks when they exist).

## Pre-registered PASS criteria

α_Bonf = 0.05 / 5 = **0.01** (4 axes + 1 joint).

| Axis | Statistic         | SUM_obs | Null mean | Null p99 | z      | p      | PASS? |
|------|-------------------|---------|-----------|----------|--------|--------|-------|
| A    | Topic-shift       | 26.081  | 26.305    | 26.792   | −1.08  | 0.860  | NO    |
| B    | Rhyme-class shift | 13.100  | 13.194    | 16.567   | −0.07  | 0.531  | NO    |
| C    | Narrative pivot   | 12.050  |  8.474    | 12.211   | +2.35  | 0.014  | NO    |
| D    | Length disc.      |  5.539  |  5.106    |  6.920   | +0.62  | 0.264  | NO    |
| —    | Joint Σz          |  1.818  |  —        |  5.473   |  —     | 0.196  | NO    |

**0 of 4 axes pass; joint does not pass. GLOBAL VERDICT: NULL.**

Axis C (narrative pivot via proper-noun count asymmetry) approaches
significance (p = 0.014) and would pass an uncorrected α = 0.05 single
test, but does not survive Bonferroni correction (α_Bonf = 0.01) and
the joint test is far from passing.

## Positive control (MW-5)

29 surah-boundary positions sampled (seed-deterministic) from the 113
internal surah seams. Pre-reg required ≥ 3/4 axes to exceed observed
juzʾ statistics for pipeline validity.

| Axis | PC SUM | juzʾ SUM | Exceeds? | p vs null  |
|------|--------|----------|----------|------------|
| A    | 27.16  | 26.08    | YES      | < 0.001    |
| B    | 24.70  | 13.10    | YES      | < 0.001    |
| C    |  6.74  | 12.05    | NO       | 0.872      |
| D    |  9.73  |  5.54    | YES      | < 0.001    |

3 of 4 axes exceed → **positive control VALID**. Pipeline detects real
structural breaks at surah seams on the topic, rhyme, and length axes.
(Axis C does not — interpretable: proper-noun density does not jump
at surah seams in random samples; surah seams aren't named-entity
seams.)

## Per-boundary "naturalness" ranking

Mean S_joint among the 7 surah-aligned juzʾ starts: **+3.44**
Mean S_joint among the 22 intra-surah juzʾ starts:  **−0.67**

Surah-aligned juzʾ boundaries are systematically more "natural" than
intra-surah ones — but this is structural and tautological: the 7
surah-aligned cuts ride on real surah seams (which are real breaks),
while the 22 intra-surah cuts ride on no structural feature. The juzʾ
system inherits naturalness from surah boundaries when they happen to
align, but adds none of its own at the 22 intra-surah cuts.

### 5 most-natural juzʾ boundaries (highest S_joint)

| juzʾ | starts at | S_joint | Surah-aligned? | Notes |
|------|-----------|---------|----------------|-------|
| 18   | Q23:1     | +8.12   | YES | Sūrat al-Muʾminūn opening |
| 29   | Q67:1     | +4.76   | YES | Sūrat al-Mulk opening |
| 17   | Q21:1     | +4.23   | YES | Sūrat al-Anbiyāʾ opening |
| 14   | Q15:1     | +3.59   | YES | Sūrat al-Ḥijr opening |
| 30   | Q78:1     | +2.63   | YES | Sūrat al-Naba opening (juzʾ ʿamma) |

All 5 most-natural juzʾ boundaries are surah-aligned — i.e., they are
structurally natural ONLY because they happen to coincide with a
surah seam. The juzʾ system gets credit for not breaking the seam,
but it adds nothing.

### 5 least-natural juzʾ boundaries (lowest S_joint)

| juzʾ | starts at | S_joint | Surah-aligned? |
|------|-----------|---------|----------------|
| 16   | Q18:75    | −2.35   | NO  |
| 5    | Q4:24     | −2.39   | NO  |
| 24   | Q39:32    | −2.44   | NO  |
| 8    | Q6:111    | −3.06   | NO  |
| 9    | Q7:88     | −3.56   | NO  |

All 5 least-natural juzʾ boundaries are intra-surah and have NEGATIVE
S_joint (i.e., the windows around them are MORE similar than random
internal cuts). This is consistent with juzʾ being placed at
length-uniform offsets, with mild bias TOWARD topical / lexical
continuity (a long topical passage gets cut at an arbitrary verse
mid-passage, where both windows share the same vocabulary).

## Interpretation

The juzʾ system is, on this evidence, a **pure recitation
length-balancer** — a 30-fold partition for monthly Ramaḍān recitation,
placed without regard to internal text structure. The 7 surah-aligned
juzʾ starts are easy "rest stops" the partitioners chose where
length-budgeting happened to allow it, but no axis shows juzʾ
boundaries as a SET preferring natural seams.

This is a NULL result with full pipeline validity. It coheres with the
classical scholarly view (e.g., al-Suyūṭī, *al-Itqān* 19) that the
juzʾ partition is a *taqsīm li-l-qirāʾa* — a recitation division —
without being a *taqsīm li-l-maʿānī* (semantic division).

## Comparison to surah boundaries

Surah boundaries are real structural breaks (positive control
confirms: A, B, D each p < 0.001). Juzʾ boundaries are not. The two
partitions are categorically different:

- **Surah** = composed structural unit; boundaries align with
  topic / rhyme / length shifts.
- **Juzʾ** = imposed editorial unit; boundaries align with neither.

## Files

- Script: `scripts/h_new_64_juz_boundaries.py`
- JSON dump: `findings/phase-b-hypotheses/csv/h-new-64.json`
- Pre-reg: `findings/phase-b-hypotheses/h-new-64-juz-boundaries-prereg.md`
- Journal: `journal/h-new-64-run-1.md`

## Caveats

- Window w = 10 verses is a single ex-ante choice. Sensitivity at w = 5
  / 20 was not run in this pass (would be a follow-up if the result had
  been borderline; for a clear NULL with the joint test at p ≈ 0.20,
  the choice of w is not load-bearing).
- Proper-noun list is closed and substring-matched; any subset
  variation would shift axis C only.
- The Quran is ONE text — this analysis treats canonical 1..114 mushaf
  order with no editions framing. The juzʾ partition is the editorial
  recitation overlay; the result is about that overlay, not the text.
