---
surah: 32
test_id: Q032-F-06
title: Q 32:15 (behavioral sajda) ↔ Q 41:37 (cosmological sajda) cross-reference — within-sajda-14 structural pairing test
file_type: pre-registration
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 2
alpha_bon: 0.025
verdict_ceiling: PASS-DIRECTED (single planned replication required for promotion)
classical_anchor:
  - al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 30 (the 14-canonical sajda-verses list).
  - al-Bukhārī, *Ṣaḥīḥ*, *Kitāb sujūd al-Qurʾān* (cluster around idInBook 1067-1079) — sajda standardization.
  - al-Rāzī, *Mafātīḥ al-ghayb*, on Q 41:37 — the *lā tasjudū li-l-shamsi wa-lā li-l-qamari wa-sjudū li-llāhi* prohibition+command structure; classical pairing-anchor for sun-moon-prostration vocabulary across sajda-verses.
direction_of_effect: LOCKED — cosine-similarity (on TF orthographic-token vectors) between Q 32:15 and Q 41:37 ranks among the TOP-5 of C(14,2)=91 pairwise within-sajda comparisons; specifically, the test pair is in the top-quintile of the 91-pair distribution.
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  text_source: quran-text/quran-no-tashkeel.json
  distance_instrument: cosine on TF-vectors of orthographic-tokens (verse-level)
---

# Q032-F-06 — Pre-registration: Q 32:15 ↔ Q 41:37 sajda cross-reference

## 1. Origin

Q 32-F-01 found Q 32:15 to be a *behavioral* sajda-verse (humans falling in prostration), distinct from the *cosmic-roll-call* cluster {Q 13:15, Q 16:49, Q 22:18}. This raises the question: which OTHER sajda-verses share the *behavioral* prostration vocabulary with Q 32:15?

Q 41:37 (*lā tasjudū li-l-shamsi wa-lā li-l-qamari wa-sjudū li-llāhi alladhī khalaqahunna in kuntum iyyāhu taʿbudūn*) is a *command-prostration* verse: a directive to humans to prostrate to God rather than to celestial objects. It is BOTH a directive-to-humans (behavioral) AND a cosmological-context verse (about the sun and moon). It is a hybrid case.

The brief specifies Q 32:15 + Q 41:37 as a cross-reference pairing. This pre-reg tests whether the pairing is empirically anchored: do the two verses share more lexical tokens than the average sajda-verse pair?

## 2. Hypotheses

**H1 (Cell A — top-5 rank):** Cosine-similarity between Q 32:15 and Q 41:37 (with the sajda symbol ۩ stripped) is among the TOP-5 of the C(14,2) = 91 pairwise comparisons of the canonical 14 sajda-verses.

**H1 (Cell B — top-quintile):** Cosine-similarity Q 32:15 ↔ Q 41:37 is in the top quintile (≥ 80th percentile) of the 91-pair distribution.

**H0:** The pairing is unremarkable (rank > 5 in Cell A, percentile < 80% in Cell B).

**Direction:** LOCKED.

## 3. Sajda-verse list (14 canonical, al-Bukhārī sujūd al-Qurʾān standard)

`[(7,206), (13,15), (16,50), (17,109), (19,58), (22,18), (25,60), (27,26), (32,15), (38,24), (41,38), (53,62), (84,21), (96,19)]`

Note: the Q 41 sajda-verse is at v 38 per the standard Mashriqi enumeration, but classical Maghrebi tradition counts v 37; we use both v 37 and v 38 for robustness and report Cell A under v 38 (the standard) with v 37 as a sensitivity check.

The pre-reg's primary anchor is the standard Mashriqi v 38: *wa-min āyātihi al-laylu wa-l-nahāru wa-l-shamsu wa-l-qamar...* The actual prostration content is split across Q 41:37 (*lā tasjudū*) and v 38 (*yusabbiḥūna lahu*). Both contain the prostration vocabulary; the canonical sajda-verse marker ۩ appears at v 38 in `quran-text/quran-no-tashkeel.json`.

## 4. Test design

### Cell A — top-5 rank within 91 sajda-pair distribution

For each of C(14,2) = 91 sajda-verse pairs, compute cosine-similarity on TF-vectors of orthographic tokens (no-tashkeel, sajda-marker ۩ and pause marks stripped). Rank Q 32:15 ↔ Q 41:38 (and sensitivity Q 32:15 ↔ Q 41:37) within the 91 cosine values, descending.

**Direction-locked:** rank ≤ 5.

PASS if direction met.

### Cell B — top-quintile percentile

Same data. Compute the percentile of the test pair's cosine within the 91-pair distribution. **Direction-locked:** percentile ≥ 0.80.

PASS if direction met.

### Cell C — descriptive within-sajda-14 cosine matrix

Tabulate the full 14×14 cosine matrix as a descriptive artifact. Cell C is NOT a hypothesis test; it serves as a corpus map for follow-on work.

## 5. Bonferroni and significance

**Bonferroni-k = 2** (Cell A + Cell B). α_bon = 0.025 per cell. The Cell A "top-5 rank" threshold ≤ 5/91 ≈ 5.5% is roughly Bonferroni-consistent for a single-pair test against 91-pair null.

## 6. A priori expectation (locked PRIOR to running)

Q 32:15 and Q 41:37/38 both contain the verb root **sjd** ("prostrate") in finite-imperative form, and both reference the human-attitude-toward-divinity ("they do not arrogantly refuse" — Q 32:15 *lā yastakbirūn*; Q 41:37 *wa-sjudū li-llāhi*; Q 41:38 *lahu yusabbiḥūna*). They share the *sjd*+*sbḥ* couplet vocabulary. Pre-committed direction is PASS — top-5 rank likely; PASS-DIRECTED ceiling.

However, the cosmic-cluster pairing {Q 13:15, Q 16:50, Q 22:18, Q 41:38} (verses where universal-creation prostrates) might emerge as the dominant similarity-cluster, potentially DEMOTING Q 32:15 ↔ Q 41:37/38 within the 91-pair ranking. The pre-reg is honest about this risk: if the cosmic-cluster dominates, the test pair may RANK 6-15 rather than top-5.

## 7. Honest limits

- 14 sajda-verses are short (mean ≈ 10 words); cosine on TF-vectors of 10-token verses is noisy. Cell B (percentile) is more robust than Cell A (strict top-5).
- The "sajda-verse" canonical list varies across madhāhib (14 vs 15 vs Shafi'i 14+1). We use the al-Bukhārī standard 14 + Q 41:38 (Mashriqi v 38; Maghrebi v 37).
- Cell C (descriptive 14×14 matrix) may reveal sub-clusters orthogonal to the cosmic-vs-behavioral binary; this is OUT OF SCOPE for the hypothesis test but logged as future-work seed.

## 8. Pre-commit violations

If rank > 5 in Cell A AND percentile < 0.80 in Cell B, the pre-committed direction has failed and the finding is published as NULL — DIRECTION REVERSED with full prominence.
