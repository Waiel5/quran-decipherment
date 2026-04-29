---
id: H-NEW-244
title: Q 1 al-Fātiḥa as *umm al-kitāb* — information-theoretic compression test
phase: B
status: prereg
date: 2026-04-17
parent: H-NEW-155 (sui-generis-liturgical confirmed); related H-NEW-192 (Q 1 Δ=−104 position-residual); complement H-NEW-231 (per-surah KL)
seed: 20260419
bonferroni_k: 3
bonferroni_family: h-new-244-umm-al-kitab
alpha_bon: 0.0167
rules_tuple: "(no-tashkeel, hafs-kufan, 7-verse windows on verse-flat corpus, char-4-gram vocabulary, Dirichlet α=0.5 smoothing against full corpus 4-gram vocabulary, simple-stemmer roots for Cell B, seed 20260419)"
direction: "Q 1 expected to RANK HIGH (top-5%) on each of 3 representativeness cells if the classical *umm al-kitāb* claim has compression-theoretic substance"
verdict: PENDING
---

# [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]] — Q 1 *umm al-kitāb* compression pre-registration

## Motivation

Al-Fātiḥa (Q 1) is classically designated *umm al-kitāb* ("mother of
the Book", also *al-Sabʿ al-Mathānī*, "the seven oft-repeated"). The
exegetical tradition — al-Suyūṭī *Itqān* (chapter on faḍāʾil
al-Fātiḥa), al-Ghazālī *Iḥyāʾ ʿulūm al-dīn* vol 1 (Kitāb al-Tilāwa),
al-Rāzī *Mafātīḥ al-ghayb* (extensive Q 1 opening volume), Ibn
Taymiyya *Majmūʿ al-Fatāwā* — claim that Q 1 contains the whole
Quran "in compressed form".

[[h-new-155-q1-sui-generis|H-NEW-155]] CONFIRMED Q 1's vocabulary dispersion (50.4% vs null 39.7%,
p=0.0013): Q 1's 18 STEM roots are MORE widely distributed across
surahs than any random 7-verse window. That is one half of the
compression claim (Q 1's vocabulary is corpus-representative).

The OTHER half has never been tested: does Q 1's FULL DISTRIBUTION
(char-4-gram, not just roots) predict the corpus distribution better
than any other 7-verse window? And when normalized per-verse, is Q 1
the minimum-KL surah?

## Pre-committed hypotheses

All three cells pre-commit direction UP (Q 1 representative; lower
KL = more representative). Bonferroni-3 ⇒ α_bon = 0.0167 per cell.

### Cell A — Q 1 vs ~6230 sliding 7-verse windows (char-4-gram)

For each sliding 7-verse window w over the full 6236-verse corpus,
compute KL(p_w || p_{rest}) on the char-4-gram distribution
(Dirichlet-smoothed α=0.5 on global 4-gram vocabulary).
- H_A: Q 1 (verses 1..7 of surah 1) is in the TOP 5% (lowest KL) of
  the ~6230 windows.
- NULL: Q 1's rank is > 5% (not exceptionally representative).

### Cell B — Q 1 roots' cross-surah presence rate

Extract simple-stemmer roots from Q 1 (the 7-verse set, content words
only). For each of the other 113 surahs, compute
`n_q1_roots_present(s) / n_q1_roots_total`.
- H_B: mean cross-surah Q 1-root presence rate is ABOVE the mean
  presence rate of 10,000 random 7-verse windows' own roots.
- NULL: not above random.

### Cell C — Per-verse-normalized KL

For each surah s (1..114), compute KL(p_s || p_{rest}) on char-4-gram
(Dirichlet α=0.5), then divide by verse-count. Rank Q 1.
- H_C: Q 1 is in the TOP 5% (lowest per-verse-KL) of the 114 surahs.
  ([[h-new-231-kl-divergence-per-surah|H-NEW-231]] showed Q 2 is min raw-KL; Cell C asks whether Q 1 is the
  min PER-VERSE-KL, which penalizes long surahs.)
- NULL: Q 1's per-verse-KL rank > 5%.

## MW-5 cheat control

A random 7-verse window (sampled via the same seed) must NOT rank in
top-5% of Cell A. If it does, the instrument is not discriminative
and Cell A result is invalidated.

## Rules tuple (locked)

- No-tashkeel corpus from `quran-text/quran-no-tashkeel.json`.
- Hafs-Kūfan verse-numbering (6236 total).
- Char-4-gram over the unified no-tashkeel grapheme stream (verse
  text concatenated with space delimiter).
- Dirichlet α = 0.5 smoothing on the global 4-gram vocabulary (union
  over the full corpus — ensures no KL log(0) and matches [[h-new-231-kl-divergence-per-surah|H-NEW-231]]
  α=0.5 smoothing parameter).
- KL = `Σ p(g) · log(p(g) / q(g))` in nats; natural log.
- Cell B root-stemmer: strip QAC-style 3-consonant skeleton
  (approximate) from Arabic orthographic tokens, filter function
  words (الله، في، من، ما، هو، لا، لهم، ﻷ، بك، ﺇن، الذين، ﻻ، ذلك,
  etc. — see script for locked stop-list).
- Seed 20260419.

## Interpretation rules (pre-committed)

- **PASS-PRIMARY (Cell A alone)**: Q 1 in top-5% of windows →
  classical *umm al-kitāb* has quantitative substance under char-4
  gram.
- **PASS-CONFIRMED (A + C)**: compression holds both per-window and
  per-verse-normalized.
- **PASS-FULL (A + B + C)**: strong empirical support; classical
  umm al-kitāb claim vindicated on three independent instruments.
- **MIXED (B alone)**: roots are common but full distribution is not
  representative — Q 1 is a root-seed but not a distributional
  encapsulation.
- **NULL (all 3 fail)**: *umm al-kitāb* is interpretive/liturgical
  only, not a compression-theoretic fact at 4-gram resolution.

## Honest limits pre-declared

1. Char-4-gram is ONE encoding; content-semantic representativeness
   (concept-level encapsulation) is not directly tested.
2. Dirichlet α=0.5 is one smoothing choice; sensitivity to α∈{0.1,
   1.0} not tested inline (could reverse rankings).
3. 7-verse windows cross surah boundaries — a window spanning two
   surahs may have unusually-heterogeneous content, which could
   inflate KL in the null.
4. Cell B simple-stemmer is approximate (not QAC-grade); false
   positives/negatives in root assignment.
5. "Representativeness" here means "low KL to rest-of-corpus",
   which IS compression in the Kraft/MDL sense for a fixed code but
   is not the same as "predicts the rest sequentially".

## Deliverables

- This pre-reg file.
- `scripts/h_new_244_fatiha_compression.py` (to be committed and
  run exactly once under seed 20260419).
- `findings/phase-b-hypotheses/h-new-244-fatiha-umm-al-kitab.md`
  post-run findings.
- `findings/phase-b-hypotheses/csv/h-new-244.json` raw stats.
- MASTER-LEDGER Wave-4 addendum.
- `journal/h-new-244-run-1.md` execution log.
