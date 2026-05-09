---
id: H-NEW-1300
title: Q 96 al-ʿAlaq *qrʾ*-imperative corpus-distribution
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-1300-iqra-distribution
alpha_bon: 0.05
direction_of_effect: Q 96 has the maximum *qrʾ*-imperative count of any of the 114 surahs (rank #1 by absolute count of IMPV verb-segments with ROOT:qrA)
origin: post-hoc-noticed (handoff §7b high-EV inline test list, 2026-05-09)
verdict_ceiling: PASS-DIRECTED (post-hoc origin, single-test α=0.05 cap until INDEPENDENT REPLICATION)
rules_tuple:
  orthography: no-tashkeel
  word_definition: morphological-segment (QAC v0.4)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: standard-mashriqi
  null_model: random-relocation-of-IMPV-qrA-segments-uniformly-over-114-surahs-weighted-by-surah-verse-count
---

# H-NEW-1300 pre-registration

## Hypothesis

Q 96 al-ʿAlaq, the first-revealed surah per Bukhārī Bad' al-Waḥy, contains the imperative `iqraʾ` ("read! / recite!") at vv 1 and 3 — the very first command revealed. This pre-reg locks the empirical question: **is Q 96 the corpus-EXACT-rank-1 surah by IMPV verb-segments with root *qrʾ* (QAC code: ROOT:qrA, POS:V, IMPV)?**

## Test design

### Cell A (primary): Absolute count

For each of the 114 surahs, count word-segments tagged `POS:V|IMPV|ROOT:qrA` in `data/morphology/quranic-corpus-morphology-0.4.txt`.

**Direction-locked**: Q 96 ≥ all 113 other surahs.

**Decision**: PASS if Q 96 strictly maximum (rank 1 of 114, no ties); PASS-WEAK if Q 96 in top-3 with tie at rank 1 ≤ 1 surah; NULL otherwise.

### Cell B (secondary descriptive): per-verse density

Compute count / verse_count per surah; report ranking. Single descriptive cell, no inferential test.

### Permutation null (Cell A)

Pool all IMPV+qrA segments. Re-assign each to a random surah, weighted by that surah's total IMPV-segment count (preserves marginal). Compute p = fraction of 10000 permutations where the random rank-1 surah's count ≥ Q 96's observed count, AND Q 96's permuted count ≥ Q 96's observed count. Report p_perm.

### Bonferroni

Single test (Cell A inferential). Cell B descriptive only. k=1. α_bon = 0.05.

### Acceptance window

Q 96 strictly maximum AND p_perm ≤ 0.05 → PASS-DIRECTED.
Q 96 strictly maximum AND p_perm > 0.05 → DESCRIPTIVE-ONLY.
Q 96 not rank 1 → NULL.

### Garden-of-forking-paths

This is **post-hoc-noticed**: the question was raised by handoff §7b high-EV inline test list. No prior viewing of the rank distribution. Direction is locked solely by classical first-revelation tradition (Q 96 contains the *first* imperative). No alternative cells will be added post-observation.

### Rules-tuple sensitivity

Test will be re-run under (a) lemma `qara>a` instead of root `qrA` (to exclude derived nouns like *qurʾān* from the imperative count). Both are reported. The IMPV filter alone already excludes nouns; the lemma filter is a sanity check.

## Anti-flip

If Q 96 is NOT rank 1, this is published as NULL with prominence per PRE-REG-STANDARD-01. The reverse direction ("Q 96 is corpus-typical or below-median for *qrʾ* IMPV") is NOT a reportable finding from this pre-reg.

## Connections to existing findings

- Cross-finding-008 / cross-finding-016: muqaṭṭāʿat as book-introduction markers; *qrʾ* / *kitāb* / *qalam* extended writing-cluster. Q 96 references *qalam* explicitly at v 4 — connects to H-NEW-56 extended-writing-cluster.
- Cross-finding-012 Late-Meccan scripture-announcement apparatus: Q 96 is **Early** Meccan, so this is the ANTI-PATTERN — does the corpus's first imperative carry the seed of a feature that peaks ~80 surahs later in chronology?
- H-NEW-74 *qul* imperative count = 332. *iqraʾ* is structurally analogous (IMPV speech-act direct address to Prophet). Per-corpus IMPV inventory contextualizes both.

## Pre-commit attestation

This pre-reg is locked at SHA computed from this file's bytes (computed by run script before execution). The script will refuse to run unless the on-disk SHA matches the value embedded in the script.
