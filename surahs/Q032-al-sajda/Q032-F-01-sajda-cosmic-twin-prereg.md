---
test_id: Q032-F-01
title: "Sajda-verse cosmic-language clustering — Q 32:15 vs Q 13:15 + Q 16:49 (replication of Q022-F-01)"
date_locked: 2026-05-08
seed: 20260508
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q032-F-01-sajda-cosmic-twin
alpha_bon: 0.01667
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q032-Q047-retry-specialist
parent_findings:
  - Q022-F-01 (sajda-cosmic-language clustering for Q 22:18 vs Q 13:15 + Q 16:49 — VINDICATED)
classical_anchors:
  - al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 30 (sajda-verses canonical list)
  - al-Bukhārī, *Ṣaḥīḥ*, kitāb sujūd al-Qurʾān (idInBook 1067-1079 cluster)
---

# Q032-F-01 Pre-registration — Sajda-verse cosmic-twin extension to Q 32:15

## Hypothesis

Q 32:15 is a *cosmic-roll-call sajda-verse*: "Only those believe in Our verses who, when they are reminded by them, fall down in prostration and exalt with praise of their Lord, and they are not arrogant." Although Q 32:15 is more *behavioral* (humans falling in prostration) than *cosmic-roll-call* per se, the broader sajda-cluster — Q 13:15, Q 16:49, Q 22:18 — share a thematic and lexical inventory of universal-prostration vocabulary (سجد، خر، تسبيح، جميع المخلوقات).

Replicating the Q022-F-01 protocol: we test whether Q 32:15 is lexically closer to the prior-attested cosmic-cluster {Q 13:15, Q 16:49} than to the median of the other 11 sajda-verses.

## Pre-committed prediction (DIRECTION LOCKED)

**Direction-locked**: cosine similarity (over normalized word-token vectors, no-tashkeel, orthographic) between Q 32:15 and {Q 13:15, Q 16:49} is HIGHER than:
- (a) median similarity of Q 32:15 with the other 11 sajda-verses (excluding Q 13:15, Q 16:49, Q 22:18)
- (b) cosine(Q 32:15, Q 22:18) is ALSO above the median-other (a check on the broader sajda-cosmic family)

## Tests (Bonferroni-3 family)

1. **T1**: Mean cosine(Q 32:15, {Q 13:15, Q 16:49}) > Median cosine(Q 32:15, {other 11 sajdas})
2. **T2**: Cosine(Q 32:15, Q 22:18) > Median cosine(Q 32:15, {other 11 sajdas})
3. **T3**: Permutation null — randomly choose 2 sajda-verses as "cosmic," recompute T1; observed p_perm < α_bon=0.01667.

α_bon = 0.05/3 = 0.01667.

## Tokenization

- Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Strip Arabic-script punctuation and sajda symbols (۩ ۚ ۖ ۗ ۘ ۛ ۜ ۠ ۡ ۤ ۦ ۧ ۨ ۭ).
- Tokens: whitespace-separated word-forms (orthographic-token level).
- TF vectors with L2-normalization for cosine.

## Sajda-verse list (15 canonical, per al-Itqān nawʿ 30 / al-Bukhārī sujūd al-Qurʾān)

`[(7,206), (13,15), (16,49), (17,109), (19,58), (22,18), (22,77), (25,60), (27,25), (32,15), (38,24), (41,37), (53,62), (84,21), (96,19)]`

Q 32:15 is the test target; cosmic-anchor-set = {Q 13:15, Q 16:49}; broader cosmic family = {Q 13:15, Q 16:49, Q 22:18}.

## Direction-of-effect lock

Predicted direction: **mean(Q32:15 ↔ cosmic-anchor-set) > median-other-11**. If reversed, report as NULL with explicit pre-commit-violation flag.

## Success criteria

- VINDICATED: T1 AND T2 AND T3 all pass at α_bon=0.01667.
- DIRECTIONAL: 1-2 of 3 pass at α_bon.
- NULL: 0 of 3 pass.

## Failure modes

- Tokens too sparse (<5 unique tokens): mark NULL-DATA-GAP.
- Cosmic-pair similarity < median-other-11: pre-commit violation.

## Garden-of-forking-paths log

- BEFORE running: chose cosine over Jaccard; following Q022-F-01 protocol exactly for replication validity.
- BEFORE running: cosmic-anchor-set = {Q 13:15, Q 16:49} chosen by classical *cosmic-roll-call* signature (sun, moon, stars, mountains, trees, animals, humans prostrating); not by computed similarity. This matches the Q022-F-01 anchor exactly.
- BEFORE running: Q 32:15's *cosmic-roll-call* status is partial — it describes humans-only prostration, not the full creation-roll-call. So I expect WEAKER cosine than Q 22:18→cosmic, but still above median-other.
- KNOWN PRIOR: Q022-F-01 was VINDICATED for Q 22:18 (the strongest cosmic-roll-call sajda).
