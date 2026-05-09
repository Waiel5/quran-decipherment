---
id: Q096-F-01
title: Q 96 al-ʿAlaq vv 1-5 vs vv 6-19 register-discontinuity test
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q096-F-01-2-block-discontinuity
alpha_bon: 0.05
direction_of_effect: The classical "vv 1-5 first revealed, vv 6-19 added later" tradition (Bukhārī Bad' al-Waḥy idInBook=3 quotes vv 1-3; Muslim Īmān idInBook=308 quotes vv 1-5; al-Ṭabarī, al-Suyūṭī Itqān nawʿ on first-revealed surah) predicts a content-register discontinuity at the v 5/v 6 boundary. The two blocks should differ in root-set composition more than random 5/14 splits within Q 96 generate. Specifically: the Jensen-Shannon (JS) divergence between vv 1-5 root-distribution and vv 6-19 root-distribution should exceed the 95th percentile of all C(19,5) = 11628 possible 5/14 contiguous-block splits, OR exceed the 95th percentile of 10000 random non-contiguous 5/14 splits — both cells reported.
origin: classical-tradition-pre-registered (Bukhārī + Muslim + al-Suyūṭī Itqān ch. on first-revealed); not post-hoc-inspection-driven
verdict_ceiling: PASS-DIRECTED on success; corroboration of classical chronology at root-distribution layer
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token (whitespace-split)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1 (irrelevant for Q 96)
  verse_numbering: hafs-kufan
  abjad_table: standard-mashriqi (irrelevant)
  null_model: two-cell — Cell A all C(19,5)=11628 contiguous 5-block splits; Cell B 10000 random non-contiguous 5/14 partitions
  feature_space: QAC v0.4 ROOT lemmas per token (excluding particles/pronouns/conjunctions; STEM tokens with ROOT field)
---

# Q096-F-01 pre-registration

## Hypothesis

The classical tradition recorded in Bukhārī Bad' al-Waḥy (idInBook=3) and Muslim Īmān (idInBook=308) places the FIRST revelation event as Q 96:1-3 (Bukhārī) or Q 96:1-5 (Muslim); al-Suyūṭī's *al-Itqān fī ʿulūm al-Qurʾān* nawʿ on first-revealed surah confirms vv 1-5 as the first-revealed core, with vv 6-19 revealed later (post-Khadīja initial-shock period; the "Abū Jahl context" of vv 9-19 implies a later social setting where the Prophet was already publicly praying and being persecuted).

If this two-block compositional history left a register-trace, then the root-distribution of vv 1-5 (5 verses, 20 words) should be measurably different from vv 6-19 (14 verses, 53 words) at JS-divergence above null.

## Test design

### Cell A — contiguous-block null (PRIMARY)

Iterate all C(19,5) = 11628 ways to choose 5 contiguous verses from Q 96. For each, compute JS divergence between the chosen 5-verse block and the remaining 14-verse block. Observed split = vv {1,2,3,4,5}; expected rank = 1/11628 if the v 5/6 boundary is THE register discontinuity. Pre-registered acceptance: rank ≤ 581 (top 5%) → PASS-DIRECTED.

### Cell B — random non-contiguous null (SECONDARY)

Generate 10000 random 5/14 partitions of {1,…,19}. For each, compute JS divergence. p_perm = fraction of random partitions with JS ≥ observed (vv 1-5 vs vv 6-19). PASS-DIRECTED if p_perm ≤ 0.05.

### Bonferroni

k = 2 cells. α_bon = 0.025 per cell. Both must pass for full PASS-DIRECTED on the directional claim.

### Acceptance windows

- Both A and B pass at α_bon = 0.025: PASS-DIRECTED (classical 2-block claim corroborated at root-distribution layer)
- Only A passes (contiguous-block but not random-split): WEAKER-DIRECTED (the v 5/6 boundary is the BEST contiguous boundary but not exceptional vs unrestricted partitions — interpretable as "the contiguous-boundary regime is informative but the absolute discontinuity is moderate")
- Only B passes: ANOMALOUS — flag for review (would suggest the v 5/6 boundary is NOT the BEST contiguous boundary, contra hypothesis)
- Both fail: NULL

### Anti-flip

Reverse direction (vv 1-5 ≈ vv 6-19 root-distribution) is a NULL outcome, not a reportable PASS. The hypothesis is unidirectional.

### Garden-of-forking-paths

- Hypothesis sourced from classical tradition BEFORE running the test (verified in Bukhārī JSON `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json` chapterId=1 idInBook=3; Muslim `muslim.json` chapterId=1 idInBook=308). No empirical inspection of root-distribution Z-scores prior to lock.
- JS divergence chosen as the symmetric, bounded, length-comparable measure (KL is asymmetric; Hellinger is similar but JS is the symmetrized log-likelihood-ratio-ish). Pre-committed.
- Particle/pronoun/conjunction filter: only STEM tokens with a ROOT field per QAC v0.4. Pre-committed.
- Smoothing: Dirichlet additive smoothing α=0.5 (Jeffreys prior) on root-count vectors, locked here.

### MW-5 positive control

Use Q 19 Maryam vv 1-40 (Zechariah-John block) vs vv 41-98 (Mary-Jesus block + later sections) as a known compositional-block change in classical sequence (al-Suyūṭī recognizes the block-shift). Compute JS divergence with the same instrument; p_perm should rank Q 19 high (≤ 5%) if instrument is calibrated. If positive control FAILS, NULL-BROKEN.

## Connection to existing findings

- **Bukhārī Bad' al-Waḥy idInBook=3** quotes vv 1-3 explicitly; **Muslim Īmān idInBook=308** quotes vv 1-5 explicitly.
- **al-Suyūṭī Itqān nawʿ on first-revealed surah** (verify nawʿ-number on physical copy before quoting verbatim; pending MW-6 VERIFIED).
- **rhyme-discontinuity at v 5/6**: vv 1-5 rhyme-letter sequence is ق-ق-م-م-م (3 distinct); vv 6-14 are 9 verses ending in ى (monorhyme block); v 15 onward shifts to ة/ه/ب — the empirical rhyme-typology already shows a 2- or 3-block structure aligning with classical claims.

## Pre-commit attestation

This pre-reg is locked by SHA256 hash. Run script verifies SHA before computing JS divergences.
