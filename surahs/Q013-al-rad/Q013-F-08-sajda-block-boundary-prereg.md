---
surah: 13
test_id: Q013-F-08
title: Q 13:15 sajda-verse as block-boundary — does the sajda-verse mark a thematic-block transition in Q 13?
file_type: pre-registration
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 2
alpha_bon: 0.025
verdict_ceiling: PASS-DIRECTED (single replication required for promotion to CONFIRMED)
classical_anchor: al-Bukhārī, *Ṣaḥīḥ*, *Kitāb sujūd al-Qurʾān* (cluster around hadith #1067-1079 in the project's idInBook convention) — the 14 canonical sajda-verses; Q 13:15 is one of them. al-Suyūṭī, *al-Itqān*, nawʿ 30 (sujūd al-tilāwah). The hypothesis here extends Q022-F-08 (the cosmic-sajda block-boundary typology) to Q 13.
direction_of_effect: LOCKED — within Q 13's 43-verse sequence, the verse-to-verse Fisher-Rao-style content discontinuity at the boundary {verse 15 / verse 16} is ≥ 95th percentile of all within-surah verse-boundaries in Q 13. I.e., the sajda-verse sits at one of the surah's strongest internal thematic seams.
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  text_source: quran-text/quran-no-tashkeel.json[12].verses
  distance_instrument: cosine on TF-vectors of orthographic-tokens (verse-level)
  basmala_policy: counted-only-in-surah-1
  window_size: 3-verse half-windows (verses {12,13,14,15} vs {16,17,18}; truncated at surah boundaries)
---

# Q013-F-08 — Pre-registration: Q 13:15 sajda-verse as block-boundary

## 1. Origin

Q 13:15 (*wa-li-llāhi yasjudu man fī al-samāwāti wa-l-arḍi ṭawʿan wa-karhan wa-ẓilāluhum bi-l-ghuduwwi wa-l-āṣāl*) is one of the 14 canonical sajda-verses (al-Bukhārī *Kitāb sujūd al-Qurʾān*; al-Suyūṭī *al-Itqān* nawʿ 30). Per the Q022-F-08 cosmic-sajda-block-boundary typology, sajda-verses tend to sit at structural seams in their host surahs — the prostration is liturgically a moment of recitational pause, and the textual structure often reflects this with a thematic-block break adjacent to the sajda.

This pre-reg tests the typology on Q 13 specifically: does Q 13:15 sit at a within-surah content-discontinuity seam? The instrument is a within-surah verse-to-verse cosine-distance computation on TF-vectors of orthographic tokens.

## 2. Hypothesis

**H1 (Cell A — sajda-as-block-seam):** The cosine-distance between (the 4-verse half-window ending at v 15) and (the 3-verse half-window beginning at v 16) is ≥ 95th percentile of all 42 verse-boundary distances in Q 13.

**H1 (Cell B — within-surah rank of v15/v16 boundary):** The Q 13:15→16 boundary ranks among the top-5 of the 42 internal boundaries in Q 13 by content-distance.

**H0:** The Q 13:15→16 boundary is content-typical (not in the top decile of within-surah seams).

**Direction (both cells):** sajda-verse sits at a within-surah seam. LOCKED.

## 3. Cluster definition

- 43 verses of Q 13 from `quran-text/quran-no-tashkeel.json[12].verses`.
- 42 internal boundaries: between v_i and v_{i+1}, for i ∈ {1..42}.
- The sajda-boundary of interest: between v 15 (sajda-verse) and v 16.
- Instrument: cosine-distance on TF-vectors built from orthographic tokens (whitespace-delimited, no-tashkeel).
- Half-window definition (Cell A): on the left, the 4-verse window {v_{i-3}, v_{i-2}, v_{i-1}, v_i} = {v 12, v 13, v 14, v 15}; on the right, the 3-verse window {v_{i+1}, v_{i+2}, v_{i+3}} = {v 16, v 17, v 18}. Asymmetric half-windows account for the sajda-verse being included in the LEFT block.

## 4. Test design

### Cell A — sajda-boundary percentile

Compute cosine-distance d_15 between left-half-window and right-half-window at the v15/v16 boundary. Also compute cosine-distance d_i for all 42 internal boundaries with symmetric 3-verse half-windows (or truncated at surah edges). Pre-committed direction: d_15 ≥ 95th percentile of {d_1, ..., d_42}.

PASS if d_15 ≥ 95th-percentile threshold.

### Cell B — within-surah rank

Sort {d_1, ..., d_42} in descending order. Pre-committed direction: rank(d_15) ≤ 5 (top-5 most distant boundaries within Q 13).

PASS if rank(d_15) ≤ 5.

### Cell C — corpus replication (sanity, descriptive)

For each of the OTHER 13 sajda-verses (Q 7:206, Q 16:50, Q 17:109, Q 19:58, Q 22:18, Q 22:77, Q 25:60, Q 27:26, Q 32:15, Q 38:24, Q 41:38, Q 53:62, Q 84:21, Q 96:19 — using the 14-verse list standard, with the Shāfiʿī adding Q 22:77 making 15), compute the within-surah percentile of the sajda-boundary. Report the distribution.

This is descriptive and replicates the Q022-F-08 broader claim. The Q 13 specific test is Cells A + B.

## 5. Bonferroni and significance

**Bonferroni-k = 2** (Cell A 95th-percentile + Cell B top-5 rank). α_bon = 0.025 per cell.

For both cells, the test is deterministic given the locked instrument; "significance" is interpreted as direction-match. The randomization MW-6 instrument-control is implicit in the within-surah rank construction (a random verse-boundary would have rank ≈ 21 ± 12, so a top-5 rank is the 12th-percentile under uniform within-surah null).

## 6. Honest limits

- TF-vector cosine-distance at the single-verse level is noisy; the half-window construction smooths but does not eliminate this. The 4-verse left-window includes the sajda-verse itself, which biases the boundary distance: any high-vocabulary-density verse will appear to discontinue the surrounding tokens. We treat this as a feature, not a confound: the sajda-verse's vocabulary distinctiveness IS the block-boundary signal.
- Q 13's 8-section thematic structure (per `02-content-analysis.md`) places v 15 at the END of the "vv. 12-15 cosmic phenomena" block and v 16 at the START of the "vv. 16-18 monotheist polemic" block. The pre-committed direction is informed by this content-segmentation but the test instrument (cosine on TF-vectors) is content-independent of the segmentation labels.
- The 14-sajda corpus reference (al-Bukhārī sujūd al-Qurʾān) is the *standard* canonical list; the Shāfiʿī school adds Q 22:77 for a 15-sajda list. Cell C uses the 14-list and notes the variant.

## 7. Pre-commit violations

If d_15 < 95th-percentile OR rank(d_15) > 5, the pre-committed direction has failed and the finding is published as NULL — DIRECTION REVERSED with full prominence.
