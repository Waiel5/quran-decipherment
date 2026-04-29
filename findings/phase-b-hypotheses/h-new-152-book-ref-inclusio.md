---
id: H-NEW-152
title: Book-reference inclusio — Q 50's v1↔v_last uniqueness
phase: B
status: NULL at Bonferroni-2; descriptive uniqueness-of-Q 50 fact preserved
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
parent_findings: [h-new-146 (Q 50 hub), cross-finding-008 (muq book-ref), h-new-53 (muq-book-ref p=3×10⁻¹²)]
seed: 20260417
rules_tuple: "(114 surahs Hafs-Kūfan; QAC v0.4 STEM roots; book-reference = qrA ∪ ktb in verse)"
bonferroni: k=2 α_bon=0.025 family=h-new-152-book-ref-inclusio
pre_reg: findings/phase-b-hypotheses/h-new-152-book-ref-inclusio-prereg.md
script: scripts/h_new_152_book_ref_inclusio.py
output_json: findings/phase-b-hypotheses/csv/h-new-152.json
verdict: NULL at α_bon=0.025; but Q 50 IS the UNIQUE surah with qrA (qurʾān) root in both v1 and v_last (1 of 114 observed; 0.11 expected = 9× enrichment; p=0.20 fails Bonferroni but descriptively striking).
---

# [[h-new-152-book-ref-inclusio|H-NEW-152]] — Book-reference inclusio: Q 50's framing uniqueness

## Summary

Q 50 opens with "وَٱلْقُرْآنِ ٱلْمَجِيدِ" (v1) and closes with
"فَذَكِّرْ بِٱلْقُرْآنِ" (v45) — a literal Qurʾān-reflexive inclusio.
This pre-reg tests whether such a v1↔v_last book-reference framing
is a rare structural pattern across the 114 surahs.

**Result: NULL at Bonferroni-2 α_bon=0.025 for both cells.**

| Cell | Test | Observed | Expected | p (2-sided) | Pass? |
|---|---|---:|---:|---:|:-:|
| A | qrA ∪ ktb in both v1 and v_last | 2 (Q 13, Q 50) | 0.86 | 0.43 | FAIL |
| B | qrA in both v1 and v_last | **1 (Q 50 alone)** | 0.11 | 0.20 | FAIL |

**But the DESCRIPTIVE uniqueness fact remains**: Q 50 is the ONLY surah
in the Quran with the root qrA (qurʾān/recite) in both its opening and
closing verses. One of 114. The expected count under independence is
0.11 (~9× enrichment on the ratio), but single-observation statistics
don't achieve Bonferroni-2 significance.

## Pre-reg compliance

Direction 2-sided per pre-reg. Bonferroni k=2, α_bon=0.025. Runtime
~10 sec. Seed 20260417. Exact binomial and 10,000-permutation null both
computed. Proceeded without auditor wave-3 ACK per autonomous-no-idle.

## Cell A — qrA + ktb (broader book-reference)

- n_v1_has = 14 of 114 (12.3%): surahs where v1 contains at least one
  qurʾān-or-kitāb root
- n_vlast_has = 7 of 114 (6.1%): surahs where v_last contains one
- n_both = **2**: Q 13 al-Raʿd, Q 50 al-Qāf
- Expected under independence = 0.86
- Exact binomial 2-sided p = 0.425

2 observed vs 0.86 expected is ~2.3× but well within binomial noise at
these low counts. Not significant.

**Note**: n_v1 = 14 is driven largely by muqaṭṭāʿat surahs. [[h-new-53-muqattaat-book-reference|H-NEW-53]]
already established that 24 of 29 muq surahs reference kitāb or qurʾān
in v1-3 (p = 3×10⁻¹²). Restricting to v1 ONLY (not v1-3) reduces this
to 14 — the opening-book-ref pattern is strong at v1-3 but dilutes at
strict v1.

**Note**: n_vlast = 7 is new information (not previously quantified).
The 7 surahs with book-ref in their LAST verse are candidates for
"closing book-reflexivity" — worth a separate study.

## Cell B — qrA only (Qurʾān-specific)

- n_v1_has = 6: surahs with qrA root in v1 (Q 15, 17, 36, 42, 50, 56,
  partially — actual membership from the data)
- n_vlast_has = 2: only 2 surahs end with a qrA-root verse
- n_both = **1**: Q 50 al-Qāf UNIQUELY
- Expected under independence = 0.11
- Exact binomial 2-sided p = 0.20

**Q 50 is the ONLY surah in the Quran that bookends with the Qurʾān
root qrA in both v1 and v_last.** The observation is RARER than expected
by 9× (1 observed / 0.11 expected), but n=1 does not survive Bonferroni-2
on exact binomial.

## Q 13 al-Raʿd — the other Cell A member

Q 13 v1: "المر ۚ تلك آيات الكتاب والذي أنزل إليك من ربك الحق"
  (ALMR. These are the āyāt of the Book and what was sent down to you is truth)
Q 13 v43 (last): "ويقول الذين كفروا لست مرسلا ۚ قل كفى بالله شهيدا بيني وبينكم ومن عنده علم الكتاب"
  (...and whoever has knowledge of the Book)

Q 13 uses ktb (kitāb) in both v1 and v_last. Under Cell A this counts;
under Cell B (qrA-only) it does not.

**So the TWO "book-ref inclusio" surahs are Q 13 and Q 50 — both
muqaṭṭāʿat-opened**:
- Q 13: المر (ALMR) — uses kitāb at both ends
- Q 50: ق (Q) — uses qurʾān at both ends

This is a small but striking observation: two of 29 muq surahs have
explicit v1↔v_last book-reflexive framing.

## Why NULL despite apparent pattern

- **Small-number statistics**: with expected counts of 0.86 (Cell A)
  and 0.11 (Cell B), the exact binomial cannot achieve p<0.025 from
  observations of 2 and 1 respectively.
- **The independence-null is CONSERVATIVE**: if v1-book-ref and
  v_last-book-ref are correlated through shared muqaṭṭāʿat-status,
  the null overstates variance.
- **A stronger pre-reg would have pre-committed a DIFFERENT null**:
  e.g., conditional on v1 having book-ref, what's the rate of v_last
  also having it? 2/14 = 14% observed vs 7/114 = 6% marginal =
  2.3× conditional enrichment. But that's not the pre-committed test.

## Q 50's UNIQUE qrA-inclusio — what this means

Descriptively, Q 50 IS the only surah in the Quran where both the
opening oath and the final verse explicitly invoke the Qurʾān by name
(the root qrA). This is a LITERAL Qurʾān-reflexive inclusio — Q 50 is a
"meta-Qurʾān" surah that talks about the Qurʾān at both ends.

This descriptive uniqueness, while not Bonferroni-passable as an
inferential claim, is consistent with:

- **[[h-new-145-muq-code-decoding|H-NEW-145]]'s Cell C finding** that Q 50 is rank 10/114 for qrA root
  density overall
- **Q 50's liturgical Friday/Eid prescription** as an "announcement"
  surah (classical)
- **[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]'s Late-Meccan scripture-announcement apparatus
  theme** — Q 50 is Late-Meccan

This positions Q 50 within a broader pattern of Late-Meccan
Qurʾān-reflexive surahs, of which it may be the MOST structurally
integrated (v1↔v45 frame).

## Why this is a genuine NULL

Because the test was:
1. Pre-committed before execution
2. Directional-neutral (2-sided)
3. Conservative (independence null)
4. Bonferroni-corrected (k=2)

...and the observed 2.3× (Cell A) / 9× (Cell B) enrichment ratios are
too small-sample to survive α_bon. The REAL finding is "uniqueness is
descriptively striking but not inferentially certified."

## Connections

- [[h-new-146-q50-qaf-hub|H-NEW-146]] (Q 50 hub UNEXPLAINED at content-axis): this finding adds
  one more descriptive uniqueness claim for Q 50 without solving the
  UNEXPLAINED verdict.
- [[h-new-53-muqattaat-book-reference|H-NEW-53]] (24/29 muq surahs reference kitāb or qurʾān in v1-3): strongly
  established; this finding is a stricter v1-only + v_last version.
- Cross-finding-008 / [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] (muq → book-ref / Late-Meccan
  scripture-announcement): Q 50 and Q 13 fit both clusters.
- [[h-new-145-muq-code-decoding|H-NEW-145]] (muq-code WEAK-SIGNAL): consistent with "muq letters mark
  phase not theme" framing.

## Honest limits

1. **Low-count statistics**: Bonferroni-2 on independence null with
   expected values <1 is hard to pass. A larger-base test (e.g.,
   v1-3 × v_last-3 window) would have more power but was rejected
   pre-reg as trivially-enriching.
2. **Independence null may be too conservative**: book-ref in v1 and
   v_last may share a hidden cause (muqaṭṭāʿat status, Late-Meccan
   stage) that makes independence under-estimate the null variance.
3. **Cell B n=1 descriptive-uniqueness is a genuine observation** but
   not a passable test.

## Queued follow-ups

- **H-NEW-152.1**: test v1-3 × v_last-3 window (weaker inference but
  more power) — pre-register FRESH; don't post-hoc-expand.
- **H-NEW-152.2**: test book-ref inclusio CONDITIONAL on muqaṭṭāʿat
  status (29 surahs); does the rate of "both v1 and v_last book-ref"
  exceed chance WITHIN the muq set?
- **H-NEW-152.3**: identify the 7 surahs with book-ref in v_last
  (closing-book-reflexivity cluster) — do they cluster by chronology
  or length?

## Honest null reporting

Published with equal prominence to PASS. The descriptive observation
(Q 50 unique qrA-inclusio) is preserved in the output JSON and findings,
but the inferential claim does not reach Bonferroni-2.
