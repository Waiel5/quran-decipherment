---
id: Q096-F-02
title: Q 96 al-ʿAlaq corpus-hapax-root density and rare-root concentration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q096-F-02-hapax-density
alpha_bon: 0.025
direction_of_effect: Q 96 contains a higher density of corpus-hapax roots (1× across whole Quran) and corpus-rare roots (≤5×) than length-matched short-Meccan-mufaṣṣal surahs. Specifically (Cell A, primary): hapax-root-token-fraction in Q 96 ≥ 95th percentile of length-matched (verses 15-25) surah-distribution. (Cell B, secondary): rare-root-fraction (≤5 corpus attestations) ≥ 95th percentile of same length-matched comparator set.
origin: empirical-discovery — root-index inspection found Q 96 contains 2 corpus-hapax roots: zbn (zabāniya, Q 96:18 — only attestation) and sfE (la-nasfaʿan, Q 96:15 — only attestation). Plus elevated nSy (nāṣiya, only 4× total — 2 of 4 in Q 96) and rare zbn-sfE-nSy concentration in vv 15-18.
verdict_ceiling: PASS-DIRECTED on success; descriptive corroboration of the v 15-18 "concluding-warning" passage's lexical-marking
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: standard-mashriqi
  null_model: length-matched (verses 15-25) short-Meccan-mufaṣṣal surahs
  feature_space: QAC v0.4 ROOT lemmas; corpus-frequency from data/morphology/root-index.json
---

# Q096-F-02 pre-registration

## Hypothesis

Q 96 contains 2 corpus-hapax roots — both in the closing-warning passage vv 15-18:
- **zbn** (zabāniya, "the angels of hell" / "the brutal ones") — Q 96:18, sole Quranic occurrence
- **sfE** (la-nasfaʿan, "we will surely seize/drag") — Q 96:15, sole Quranic occurrence

Plus the rare root **nSy** (nāṣiya, "forelock") with only 4 corpus occurrences total: 2 of which are in Q 96 (vv 15, 16). Total nSy concentration: 50% of corpus occurrences in 19/6236 = 0.3% of corpus verses (a 158× concentration).

The pre-registered direction: Q 96's hapax-root-token fraction and rare-root-token fraction are extreme relative to length-matched short-Meccan-mufaṣṣal comparator surahs.

## Test design

### Comparator set (length-matched)

All Meccan or early-Medinan surahs with verse-count in [15, 25]. Per `quran-no-tashkeel.json` and `data/revelation-order.csv`:
- Q 73 al-Muzzammil (20 v), Q 86 al-Ṭāriq (17 v), Q 87 al-Aʿlā (19 v), Q 88 al-Ghāshiya (26 v — boundary), Q 96 al-ʿAlaq (19 v), Q 53 al-Najm (62 v — out of range), and others 15-25v.

Comparator pool will be locked by script after filtering to verses ∈ [15, 25].

### Cell A — corpus-hapax fraction (PRIMARY)

For each surah in comparator pool, compute fraction of STEM-with-ROOT tokens whose ROOT has corpus-frequency 1 (hapax roots: appears only in this surah, only at this token-position). Q 96's expected fraction is 2 / (Q 96 total STEM-with-ROOT tokens). Direction: Q 96 ≥ 95th percentile of pool. p_perm = rank / |pool|.

PASS-DIRECTED at α_bon = 0.025: p_perm ≤ 0.025.

### Cell B — rare-root fraction (SECONDARY)

Same as Cell A but using corpus-frequency ≤ 5 (rare-root threshold per H-NEW-119 and Q113-F-03 conventions). Direction: Q 96 ≥ 95th percentile.

PASS-DIRECTED at α_bon = 0.025: p_perm ≤ 0.025.

### Bonferroni

k = 2 (Cells A, B). α_bon = 0.025 per cell. Both must pass for full PASS-DIRECTED.

### Anti-flip

Reverse direction (Q 96 has BELOW-median hapax/rare-root density) is a NULL, not reportable PASS.

### Acceptance windows

- Both pass at α_bon = 0.025: full PASS-DIRECTED (the closing-warning vv 15-18 lexical marking is statistically extreme)
- Only A passes: WEAKER-DIRECTED (hapax effect, not rare-root effect)
- Only B passes: WEAKER-DIRECTED (rare-root effect, not hapax effect)
- Both fail: NULL

### Garden-of-forking-paths

- Origin: root-index inspection. zbn and sfE flagged as 1×-corpus during pre-flight reading. The 4-element rare-root concentration in vv 15-18 (zbn 1×, sfE 1×, nSy 4× total of which 2 in Q 96) was visually striking; this pre-reg locks BEFORE running the comparator distribution, with origin disclosed.
- The length-window [15, 25] is locked here; not adjustable post-hoc.
- Comparator pool is "Meccan + early Medinan" as recorded in `revelation-order.csv` (filter: period ∈ {"Meccan", "Mid Meccan", "Early Meccan", "Late Meccan"}); locked here.

### MW-5 positive control

Q 113 al-Falaq (5 verses) is known to have rank-1 rare-root density per Q113-F-03 (50% of distinct roots ≤5×). Reduce length-window to [3,7] for Q 113 control test; positive control passes if Q 113 ≥ 95th percentile of [3,7]-matched pool. If positive control FAILS, NULL-BROKEN.

## Connection to existing findings

- **Q113-F-03** rare-root-density rank 1/19 short surahs (≤10v) — same instrument, different length class. Q 96 is the ≤25-v class candidate.
- **H-NEW-23** hapax-verse-final slot (z = +10.61): the corpus has a strong active-placement signal for hapax at verse-final. Q 96:18 ends with *al-zabāniya* (a corpus-hapax at verse-final position).

## Pre-commit attestation

SHA256-locked. Script will verify before loading root-index.json frequencies.
