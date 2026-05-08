---
finding_id: Q025-F-03
title: Q 25 and Q 67 as a *tabāraka alladhī* opener-pair — joint structural similarity test
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q025-al-furqan-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q025-F-03-tabaraka-pair
bonferroni_k: 4
alpha_bon: 0.0125
direction: one-sided HIGHER similarity (Q25,Q67) than null random surah-pairs across 4 instruments
success_criterion: ≥3/4 instruments place the (Q25, Q67) pair in the top-decile of pairwise similarity vs random pairs, all at p ≤ α_bon
rules_tuple: "(no-tashkeel, orthographic-token, graphemes, Hafs-Kufan, Mashriqi)"
script: surahs/Q025-al-furqan/scripts/Q025_F_03_tabaraka_pair.py
output_json: surahs/Q025-al-furqan/csv/Q025-F-03.json
---

# Q025-F-03 — *Tabāraka alladhī* opener-pair (pre-reg)

## Hypothesis

The Quran has exactly 2 surahs that open with the formula *tabāraka alladhī*: Q 25 al-Furqān (*tabāraka alladhī nazzala al-furqāna ʿalā ʿabdihi*) and Q 67 al-Mulk (*tabāraka alladhī biyadihi al-mulk*).

**Pre-committed claim**: this surface-formal pair is also a structural pair on at least 3 of 4 corpus-wide similarity instruments (i.e., the pair scores in the top-decile vs random non-tabāraka pairs).

## The 4 instruments

For each, define a similarity score on surah-pairs (a, b):
1. **I1 — Fisher-Rao similarity**: `1 / (1 + d_FR(a,b))` from h-new-111.
2. **I2 — top-rhyme-letter identity**: 1 if Q a and Q b share their dominant final-letter (per h-new-700 rhyme_letter_diagnostics), 0 otherwise.
3. **I3 — opening-word identity** (graphemic, no-tashkeel orthographic token, post-bismala): 1 if Q a and Q b share verse-1's first orthographic word, 0 otherwise. (Q25 v.1 first word = `تبارك`, Q67 v.1 first word = `تبارك` ⇒ 1 by construction; this is a positive control on the pair-definition, NOT a free test.)
4. **I4 — sig_A iʿjāz similarity**: `1 - |sig_A(a) - sig_A(b)| / range(sig_A)` from h-new-750.

For each instrument, compute the (Q25, Q67) pair score and its rank/percentile in the distribution of all C(114,2)=6441 surah pairs.

## Bonferroni accounting

k = 4 instruments. α_bon = 0.05 / 4 = 0.0125.

I3 (opening-word identity) is a definitional positive-control — both surahs ARE selected because they share *tabāraka*. Reporting it does not cost a Bonferroni cell because it's verifiable by inspection. The genuine inferential cells are I1, I2, I4 (k_inferential = 3, with α_bon_inferential = 0.0167; we use the conservative tightening to k=4 throughout).

## Acceptance / failure

- ≥3/4 instruments (including I3) and ≥2/3 inferential instruments at p ≤ α_bon ⇒ **PASS-DIRECTED**: Q 25 / Q 67 form a structural pair beyond their shared opener.
- 2/4 (i.e., I3 + 1 inferential) ⇒ **DIRECTIONAL**.
- ≤1/4 ⇒ **NULL**: the *tabāraka* opener is a SURFACE-ONLY pairing.

## Direction is locked

Direction: HIGHER similarity than random pairs on each of I1, I2, I4. (I3 is constructive.) Reversed direction (e.g., Q25/Q67 score in bottom-decile of FR similarity) is a pre-commit violation.

## MW protections

- MW-1 (instrument-prior): 4 instruments specified before computation.
- MW-2 (corpus-prior): null distribution = empirical distribution of all 6441 pair-similarity scores.
- MW-5 (positive-control): I3 is a sanity-check by construction.
- MW-6 (instrument-control): MW-6 = the same 4-instrument family applied to a CONTROL pair {Q 1, Q 6} (al-Fātiḥa + al-Anʿām, both opening with *al-ḥamd lillāhi* — a different formal-opener-pair) should ALSO score in top-decile on at least 1 instrument, demonstrating the framework detects known pair-cohesion. If MW-6 control fails on >2 instruments, the test is NULL-BROKEN.

## Garden-of-forking-paths log

- 4 not 5 instruments because we want one of each TYPE: continuous-content (FR), discrete-rhyme, discrete-opener, continuous-iʿjāz. Each captures a different architectural axis.
- (Q1, Q6) is the natural MW-6 control because they share *al-ḥamd lillāhi* opener (the only other opener-class doublet of comparable length classes; Q1 is short but its opener is canonical).

## Files

- Pre-reg: `surahs/Q025-al-furqan/Q025-F-03-tabaraka-pair-prereg.md`
- Script: `surahs/Q025-al-furqan/scripts/Q025_F_03_tabaraka_pair.py`
- Output: `surahs/Q025-al-furqan/csv/Q025-F-03.json`

*PRE-REG LOCKED 2026-05-07.*
