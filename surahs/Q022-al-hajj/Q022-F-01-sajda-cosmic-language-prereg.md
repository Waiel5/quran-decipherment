---
test_id: Q022-F-01
title: "Sajda-verse cosmic-language clustering — Q 22:18 with cosmic-roll-call sajdas (Q 13:15, Q 16:49)"
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q022-F-01-sajda-similarity
alpha_bon: 0.01667
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q022-al-hajj-specialist
---

# Q022-F-01 Pre-registration — Sajda-verse cosmic-language clustering

## Hypothesis

Of the 14 canonical sajda-verses (al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 30), Q 22 contains TWO (vv. 18 and 77 per Hanafi/Shāfiʿī tradition; Maliki: only 18 per al-Tirmidhī #578 *Uqbah b. ʿĀmir* and Abū Dāwūd #1402 *ʿAmr b. al-ʿĀṣ*). Q 22:18's vocabulary follows a *cosmic-roll-call* pattern (sun, moon, stars, mountains, trees, animals, men) that is shared with two other sajda-verses: Q 13:15 ("All who are in the heavens and earth prostrate to Allāh willingly or unwillingly, and their shadows in mornings and evenings") and Q 16:49 ("Whatever is in the heavens and on earth prostrates to Allāh of the creatures..."). Q 22:77 is an *imperative-action* sajda ("Bow, prostrate, worship") with a different lexical signature.

## Pre-committed prediction

**Direction-locked**: cosine similarity (over normalized word-token vectors) between Q 22:18 and the cosmic-roll-call sajda-verses {Q 13:15, Q 16:49} is HIGHER than:
- (a) similarity between Q 22:18 and Q 22:77 (the other Q22 sajda)
- (b) similarity between Q 22:18 and the median of the other 11 (non-cosmic) sajda-verses

## Tests (Bonferroni-3 family)

1. **T1**: Mean cosine(Q22:18, {Q13:15, Q16:49}) > Mean cosine(Q22:18, {other 11 sajdas})
2. **T2**: Mean cosine(Q22:18, {Q13:15, Q16:49}) > cosine(Q22:18, Q22:77)
3. **T3**: Permutation null — randomly assign 2 sajda-verses as "cosmic" and recompute T1; observed rank vs 10,000 perms.

α_bon = 0.05/3 = 0.01667.

## Tokenization

- Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Strip Arabic-script punctuation marks (sajda symbol ۩, pause marks ۚ ۖ ۗ ۘ ۚ ۛ ۜ ۠ ۡ ۤ ۦ ۧ ۨ ۭ).
- Tokens: whitespace-separated word-forms (orthographic-token level).
- TF vectors with L2-normalization for cosine.

## Sajda-verse list (14 canonical, per al-Itqān nawʿ 30 / al-Bukhārī #1071-1079):

`[(7,206), (13,15), (16,49), (17,109), (19,58), (22,18), (22,77), (25,60), (27,25), (32,15), (38,24), (41,37), (53,62), (84,21), (96,19)]`

Note: 15 verses in al-Suyūṭī's count (he includes (84,21) and the Hanafi/Shāfiʿī (22,77)). Maliki count = 11 (excludes 22:77, 38:24, 41:37, 84:21, 22:18 reading varies).

## Direction-of-effect lock

Predicted direction: **cosmic > Q22:77 AND cosmic > median-other**.
If reversed (cosmic < Q22:77 OR cosmic ≤ median-other), report as NULL with explicit pre-commit-violation flag.

## Success criteria

- VINDICATED: T1 AND T2 AND T3 all pass at α_bon=0.01667.
- DIRECTIONAL: 1-2 of 3 pass at α_bon.
- NULL: 0 of 3 pass.

## Failure modes

- Tokens too sparse (<5 unique tokens): mark NULL-DATA-GAP.
- Cosmic-pair similarity < Q22:77 similarity: pre-commit violation.

## Garden-of-forking-paths log

- BEFORE running: chose cosine over Jaccard because Jaccard is too coarse for short verses with shared function-words (الله, في).
- BEFORE running: chose word-token over root-token because the COSMIC-ROLL-CALL is a SURFACE lexical pattern (الشمس، القمر، النجوم، الجبال، الشجر، الدواب) — surface forms are the test target, not root abstractions.
- BEFORE running: cosmic-anchor-set = {13:15, 16:49} chosen by classical pattern (al-Rāzī *Mafātīḥ* on Q 22:18 cross-references both); not by computed similarity.
