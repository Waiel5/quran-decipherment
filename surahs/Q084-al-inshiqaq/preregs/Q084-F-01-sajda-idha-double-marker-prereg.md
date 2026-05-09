---
finding_id: Q084-F-01
title: Q 84 sajda + idhā-cosmic-opener double-marker corpus-uniqueness verification
phase: B+
date_locked: 2026-05-09
seed: 20260509
n_perm: 0  # exact-count test
bonferroni_k: 1
alpha_bon: 0.05
script: surahs/Q084-al-inshiqaq/scripts/Q084_F_01_sajda_idha_double_marker.py
parent_findings: H-NEW-1200, H-NEW-1330
---

# Q084-F-01 — Sajda + idhā-cosmic-event-opener double-marker pre-registration

## Hypothesis

H1: Q 84 al-Inshiqāq is the corpus's UNIQUE surah that is BOTH:
- (a) An idhā-cosmic-event-opener (member of the 5-surah Sub-cluster A: {Q 56, 81, 82, 84, 99} per H-NEW-1200), AND
- (b) A sajdat al-tilāwa (recitation-prostration) surah (member of the 14-surah classical Sunnī sajda list per H-NEW-1330: Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96)

H1a: The intersection of (a) ∩ (b) is exactly {Q 84} — a singleton.

## Direction (LOCKED before observation)

- |idhā-cosmic-opener ∩ sajda-list| = 1 (Q 84 only)
- Among the 5 idhā-cosmic-openers, only Q 84 carries a sajda verse (Q 84:21).
- Among the 14 sajda surahs, only Q 84 opens with idhā-cosmic-event.

Counter-direction (intersection ≥ 2 OR Q 84 not in intersection) = NULL.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

The sajda list = classical Sunnī 14 (per H-NEW-1330; al-Suyūṭī *al-Itqān* nawʿ 73; al-Bukhārī, Muslim, Tirmidhī cross-validated). Idhā-cosmic-opener list = H-NEW-1200 Sub-cluster A.

## Operationalization

1. Lock the 5-surah idhā-cosmic-opener set: {56, 81, 82, 84, 99}.
2. Lock the 14-surah sajda set: {7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96}.
3. Compute intersection: I = idhā ∩ sajda.
4. Verify Q 84:21 contains the sajda glyph (۩) in the canonical Hafs-Kufan text.
5. Verify Q 84:1 opens with *idhā al-samāʾu inshaqqat*.

## Success criteria

- |I| = 1 and 84 ∈ I → CONFIRMED
- |I| > 1 → NULL (the double-marker is not unique)
- 84 ∉ I → instrument failure (NULL-BROKEN)

## Failure conditions

- Any other idhā-cosmic-opener carries a sajda glyph.
- Q 84 lacks the sajda glyph in the canonical text.

## Pre-commit honesty

Direct corpus lookup; no permutation needed (the lists are LOCKED classical-tradition sets).

## Connection to existing findings

H-NEW-1330 confirmed the 14-surah sajda set is NOT FR-cohesive (sajda is a LOCAL marker, not a surah-aggregate signature). H-NEW-1200 confirmed the 5-surah idhā-opener set IS FR-cohesive. This pre-reg asks: given the orthogonal nature of the two cluster definitions, is Q 84 the UNIQUE bridge surah?

If CONFIRMED, this means Q 84 carries TWO independent classical-form-pattern markers — one from the eschatological-content axis (idhā) and one from the liturgical-prostration axis (sajda). Q 84 is then the corpus's sole BIPLEX-MARKER surah connecting these two architectural systems.
