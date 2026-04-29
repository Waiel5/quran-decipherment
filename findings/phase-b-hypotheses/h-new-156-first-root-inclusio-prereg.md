---
finding_id: h-new-156
title: "First-content-root inclusio — does the first root of v1 reappear in v_last, and is this pattern more common at muqaṭṭāʿat surahs?"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 1
bonferroni_family: h-new-156-first-root-inclusio
alpha_bon: 0.05
alpha_raw: 0.05
parent_findings: [h-new-152 (Q 50 qrA-inclusio UNIQUE), h-new-53 (muq-book-ref), cross-finding-006 (muq multi-axis)]
rules_tuple: "(114 surahs; QAC v0.4 STEM roots; first-content-root = first STEM root in v1 after any muq letters; v_last = last verse of surah)"
pre_reg_standard: PRE-REG-STANDARD-04
---

# [[h-new-156-first-root-inclusio|H-NEW-156]] — First-content-root inclusio

## Motivation

[[h-new-152-book-ref-inclusio|H-NEW-152]] found that Q 50 is the unique surah with the qurʾān root
(qrA) in both v1 and v_last. That's the strictest form of "inclusio"
(rhetorical frame). A LOOSER, more general form: does the FIRST
content-word's root reappear anywhere in the last verse?

Classical balāgha (al-Rāzī, al-Zarkashī) identifies inclusio
(rhetorical closure) as a deliberate authorial strategy. This test asks:
is this loose-inclusio pattern STRUCTURALLY more common in
muqaṭṭāʿat-opened surahs than in non-muq?

## Hypothesis

For each of 114 surahs:
- `first_root[s]` = first STEM root in v1 (skipping muq-letter tokens which
  aren't STEM-tagged), falling back to v2 if v1 has no STEM root
- `last_verse_roots[s]` = set of STEM roots in v_last
- `inclusio[s]` = 1 if `first_root[s] ∈ last_verse_roots[s]`, else 0

**H_0**: inclusio rate is equal between muq and non-muq surahs.

**H_1**: inclusio rate is HIGHER in muq surahs than non-muq.

## Method

1. Parse QAC. For each surah, find first STEM root in v1 (or v2 if v1
   has none — esp. for muq-only v1 which has no STEM roots).
2. Collect last-verse STEM root set.
3. Compute inclusio binary per surah.
4. Compute: rate_muq = inclusio_count_in_muq / 29
            rate_nonmuq = inclusio_count_in_nonmuq / 85
5. Observed diff = rate_muq − rate_nonmuq
6. Fisher's exact test (1-sided upper-tail).
7. Permutation null (10,000 shuffles of muq-status labels).

**PASS**: Fisher 1-sided p < 0.05 AND permutation 1-sided p < 0.05.

## MW-5 positive control

Apply the same pipeline to a known-random label: shuffle muq-status
across the 114 surahs 10,000 times; measure empirical p. Should come
out flat near 0.5 under shuffled null (confirmed by the permutation
null itself).

## Direction-lock

DIRECTION LOCKED POSITIVE (muq-rate > non-muq-rate) BEFORE viewing any
data. This hypothesis is theoretically motivated by [[h-new-53-muqattaat-book-reference|H-NEW-53]] (muq surahs
self-reference book), [[h-new-152-book-ref-inclusio|H-NEW-152]] (Q 50 qrA-inclusio), and classical
balāgha framing.

## Garden of forking paths

- **First-root over first-5-roots window**: locked single-root. Window
  alternatives rejected (inflates base rate, would trivially pass).
- **v_last any root, not first-v_last-root**: locked "any root in v_last".
  Stricter "first root in v1 matches first root in v_last" would be
  too sparse.
- **STEM root only, not full morphological**: QAC v0.4 STEM tokens.
  Matches [[h-new-53-muqattaat-book-reference|H-NEW-53]] methodology.
- **Skip muq-letter tokens**: QAC tags them as separate non-STEM entries,
  so skipping naturally filters them out.
- **Fisher exact + permutation**: two inferential tests; consistent p
  requirement both.
- **Direction 1-sided**: pre-committed based on theoretical motivation.

## Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_156_first_root_inclusio.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-156.json`
- Findings: `findings/phase-b-hypotheses/h-new-156-first-root-inclusio.md`
- Journal: `journal/h-new-156-run-1.md`

Runtime <30 sec.
