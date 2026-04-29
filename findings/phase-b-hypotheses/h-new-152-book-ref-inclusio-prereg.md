---
finding_id: h-new-152
title: "Book-reference inclusio — is Q 50's v1↔v45 Qurʾān-reflexive framing structurally unique?"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 2
bonferroni_family: h-new-152-book-ref-inclusio
alpha_bon: 0.025
alpha_raw: 0.05
rules_tuple: "(114 surahs Hafs-Kūfan; QAC v0.4 STEM roots; book-reference = any occurrence of root qrA (Qurʾān) OR ktb (kitāb) in target verse)"
pre_reg_standard: PRE-REG-STANDARD-04
---

# [[h-new-152-book-ref-inclusio|H-NEW-152]] — Book-reference inclusio: Q 50's unique v1↔v_last framing

## Motivation

Q 50 al-Qāf opens (v1: "ق وَٱلْقُرْآنِ ٱلْمَجِيدِ") and closes
(v45: "فَذَكِّرْ بِٱلْقُرْآنِ مَن يَخَافُ وَعِيدِ") with explicit
Qurʾān-references. This is a rhetorical inclusio — the surah is LITERALLY
book-framed: "by the Qurʾān" at opening, "remind by the Qurʾān" at closing.

Is this inclusio a UNIQUE structural pattern, or does it appear in other
surahs? If rare, it adds a new axis to cross-finding-006 (muqaṭṭāʿat
multi-axis synthesis) and/or [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] (Late-Meccan scripture-
announcement apparatus).

A preliminary dry-run (not pre-registered-inferential; scoping only)
found only 2 of 114 surahs have book-reference roots in both v1 and
v_last. This is very sparse. Pre-reg locks the inferential test below.

## Hypothesis

### Cell A — rarity of v1↔v_last book-ref inclusio (PRIMARY)

**H_0**: The observed frequency of surahs with both v1 AND v_last
containing book-ref roots (qrA ∪ ktb) is consistent with independent
random placement.

**H_1**: The frequency is LOWER than independent random placement
(i.e., the pattern is RARER than chance), OR HIGHER (pattern is
special-class).

Under independence null:
- P(v1 has book-ref) = (count of v1-has) / 114
- P(v_last has book-ref) = (count of v_last-has) / 114
- Expected both = P(v1) × P(v_last) × 114

Observed: count of surahs with both v1-and-v_last book-ref.

**Test**: exact binomial p comparing observed to expected.
PASS: |observed − expected| / √(expected × (1 − p_joint)) > z threshold;
α_bon = 0.025 (2-sided).

### Cell B — uniqueness of Q 50 (PRIMARY 2/2)

**H_0**: Q 50 is NOT distinctive among the "v1-and-v_last book-ref"
set (if that set has > 1 member, Q 50 is an ordinary member).

**H_1**: Q 50 has a specific feature — the root ROOT-Q-R-A (qurʾān)
appearing in BOTH v1 AND v_last — that is rarer than just any book-ref
root in both.

For Cell B, restrict book-ref to specifically the qrA root (not ktb).
Count surahs with qrA root in both v1 and v_last.

**Test**: under null, P(v1 has qrA) × P(v_last has qrA) × 114.

PASS: observed count ≤ 2 (Q 50 + at most one other) and binomial p < 0.025.

## Method

### Data

- Text: QAC v0.4 STEM root tokens per verse (same as [[h-new-111-fisher-rao-mushaf|H-NEW-111]], [[h-new-146-q50-qaf-hub|H-NEW-146]]).
- Surah verse counts: `quran-text/quran-no-tashkeel.json`.
- Target roots: qrA (qurʾān/recite/read) and ktb (kitāb/write/book).

### Procedure (pre-committed)

1. For each of 114 surahs, compute:
   - `has_bookref_v1[s]` = any STEM root in v1 ∈ {qrA, ktb}
   - `has_bookref_vlast[s]` = any STEM root in v_last ∈ {qrA, ktb}
   - `inclusio_both[s]` = both are True
2. Count N_both = #{s : inclusio_both[s]}
3. Compute expected N_both under independence:
   p1 = #{v1-has} / 114
   plast = #{v_last-has} / 114
   expected = p1 × plast × 114
4. Compute exact binomial p for observed-vs-expected under independence.
5. Repeat for qrA-only for Cell B.

### Permutation null (robustness check)

Separately: 10,000 permutations — shuffle the 114 v1-book-ref labels,
shuffle the 114 v_last-book-ref labels independently. Count N_both
under each shuffle. Empirical p: fraction of perms with N_both ≥ observed
(upper-tail) or ≤ observed (lower-tail), 2-sided.

## Bonferroni

- Family = [[h-new-152-book-ref-inclusio|h-new-152]]-book-ref-inclusio
- k = 2 (Cell A qrA+ktb; Cell B qrA-only)
- α_bon = 0.025
- 2-sided for both

## Garden of forking paths

- **Book-reference roots = {qrA, ktb}**: locked pre-result. qrA is the
  direct Qurʾān-reflexive root; ktb covers kitāb (Book). Alternatives
  rejected pre-result: adding ʾyH (āya — too broad; ~400 corpus occurrences),
  adding tlw (tilāwa — only 20 occurrences, sparse); adding substring
  matches (loosens specificity).
- **v_last vs v_penultimate**: chose v_last strictly. Alternative rejected:
  "last 3 verses" (too loose; would trivially enrich).
- **Count ≥ 1 STEM root match**: binary. Alternatives rejected:
  frequency weight (arbitrary weighting), token-count (unclear
  thresholds).
- **2-sided test**: no theoretical reason to predict whether inclusio
  is rarer-than-null (chance placement) or richer-than-null (intentional
  structural feature). Either could be the finding.

## Pre-committed acceptance matrix

| Cell A (qrA+ktb) | Cell B (qrA only) | Verdict |
|---|---|---|
| PASS (rarer than null) | PASS (Q 50 unique or near-unique) | STRUCTURAL — book-ref inclusio is a genuine rare structural pattern |
| PASS | FAIL | PARTIAL — broader book-ref rare, qrA-specific common |
| FAIL | PASS | NARROW — qrA-inclusio rare but broader ktb weakens pattern |
| FAIL | FAIL | NULL — no rare-inclusio pattern; Q 50 not structurally distinctive on this axis |

## Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_152_book_ref_inclusio.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-152.json`
- Findings: `findings/phase-b-hypotheses/h-new-152-book-ref-inclusio.md`
- Journal: `journal/h-new-152-run-1.md`

Null and pass published with equal prominence. Runtime target <30 sec.
