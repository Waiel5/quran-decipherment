---
id: H-NEW-213
title: Dominant repetition unit per surah — longest word-level n-gram repeating ≥3 times per surah
phase: B
status: PRE-REGISTERED
date: 2026-04-17
specialist: autonomous-agent (inline execution)
seed: 20260419
bonferroni_k: 2
alpha: 0.05
alpha_bonferroni: 0.025
rules_tuple: "(Hafs-Kūfan; text = quran-text/quran-no-tashkeel.json; verses joined with single space per surah; word tokens = whitespace-split; Quranic pause marks and punctuation ۛ ۖ ۗ ۚ ۞ ۙ stripped; min_count = 3; n-gram range 1..12 words; 'longest' = maximum n such that some n-gram occurs ≥3 times in the surah; ties broken by higher count then lexicographic)"
parent_findings:
  - h-new-180 (Q55 fabi-ayyi-alāʾi-rabbikumā refrain position analysis)
  - h-new-191 (cluster-4 refrain-stylistic — referenced but NOT a saved finding in this project; treated as conceptual anchor)
  - h-new-195 (per-surah letter-bigram entropy; length-residual ranking)
  - h-new-196 (oath-cluster k-means note that H-NEW-191 does not yet exist)
pre_reg: findings/phase-b-hypotheses/h-new-213-dominant-repetition-unit-prereg.md
script: scripts/h_new_213_dominant_repetition_unit.py
output_json: findings/phase-b-hypotheses/csv/h-new-213.json
output_csv: findings/phase-b-hypotheses/csv/h-new-213-per-surah.csv
---

# [[h-new-213-dominant-repetition-unit|H-NEW-213]] — Dominant repetition unit per surah

## Motivation

Classical rhetoric (balāgha) identifies the *lāzima* / refrain as a
stylistic marker: repeated formulaic phrases. Q 55 (al-Raḥmān) is the
canonical example with *fabi-ayyi ālāʾi rabbikumā tukaḏḏibān* repeated 31
times; Q 77 (al-Mursalāt) has *waylun yawma'iḏin lil-mukaḏḏibīn* repeated
10 times. [[h-new-180-q55-refrain-position-result|H-NEW-180]] studied Q55 specifically. [[h-new-195-entropy-per-surah|H-NEW-195]] found short creedal
surahs (al-Nās, al-Ikhlāṣ, al-Kāfirūn) have extreme negative letter-bigram
residuals driven by triple-iterated refrains.

[[h-new-213-dominant-repetition-unit|H-NEW-213]] operationalizes **refrain structure per surah**: the longest
word-level n-gram that repeats ≥3 times within the surah. This converts
a classical qualitative claim into a measurable per-surah axis.

## Method

For each of 114 surahs:
1. Tokenize verses (whitespace-split, pause-marks stripped from the text).
2. For n = 1..12: count all word-n-gram occurrences within the surah.
3. Report MaxN = maximum n such that some n-gram has count ≥3.
4. Report the top n-gram at that length (highest count; ties → lexicographic).

## Primary test (H1)

**Classical refrain-pattern claim**: A non-trivial fraction of surahs
have a dominant repetition unit of length ≥3 words.

- H0: the fraction of surahs with MaxN ≥ 3 is ≤ 0.10 (baseline: chance
  repetition of 3-grams in short texts).
- H1: fraction > 0.10, tested by exact binomial test.
- Direction: one-sided (upper).
- PASS if p_binom < α_bon = 0.025.

## Secondary test (H2)

**Integration with [[h-new-195-entropy-per-surah|H-NEW-195]] entropy ranking**: surahs with MaxN ≥ 3
(refrain-structured) should have more-negative bigram-entropy residual
than surahs with MaxN ≤ 2 (non-refrain).

- H0: median residual (refrain) = median residual (non-refrain).
- Test: two-sided Mann–Whitney U on [[h-new-195-entropy-per-surah|H-NEW-195]] per-surah residuals.
- PASS if p_MWU < α_bon = 0.025 AND direction matches (refrain lower residual).

Bonferroni family k=2.

## Integration question (descriptive, not pre-reg tested)

H-NEW-191 Cluster 4 ("refrain-stylistic") does not exist as a
saved finding (confirmed by grep — [[h-new-196-oath-cluster|h-new-196]] prereg explicitly notes
H-NEW-191 "does not exist in this project yet"). Instead of attempting
reverse inference on a non-existent cluster assignment, we:

(a) Report the list of surahs with MaxN ≥ 3 (our empirical
    "refrain-structured" set).
(b) Cross-check whether this set overlaps with oath-cluster ([[h-new-85-oath-openers|H-NEW-85]] /
    [[h-new-196-oath-cluster|H-NEW-196]]), short creedal surahs (Q 108, 112, 113, 114), and
    Musabbiḥāt (Q 17, 57, 59, 61, 62, 64, 87 / [[h-new-103-musabbihat-4form|H-NEW-103]]).
(c) Report Spearman ρ between MaxN and [[h-new-195-entropy-per-surah|H-NEW-195]] length-residual.

## Robustness / sensitivity

- Rule-variant: with-tashkeel text → does the refrain list change?
- Rule-variant: min_count=2 → is the MaxN distribution stable?
- No null-simulation: counts are exact; no permutation needed for the
  binomial H1 test.

## Outputs

- `scripts/h_new_213_dominant_repetition_unit.py` — analysis script
- `findings/phase-b-hypotheses/csv/h-new-213.json` — summary
- `findings/phase-b-hypotheses/csv/h-new-213-per-surah.csv` — 114 rows:
  surah_id, name, MaxN, top_ngram, count, length_tokens
- `findings/phase-b-hypotheses/h-new-213-dominant-repetition-unit.md` — result

## Pre-commitments

- Seed: 20260419 (no randomness in primary test; declared for audit).
- α_bon = 0.025 (k=2).
- Rules tuple locked above.
- Direction for H1 pre-committed (one-sided upper).
- Direction for H2 pre-committed (refrain lower residual).
- 10% H0 threshold is a conservative deliberate choice — justified by:
  with 1..12 n-gram search, chance ≥3-repeat 3-grams in short texts is
  non-zero; a purely accidental refrain floor of 10% is well above the
  null under a bag-of-words model.
