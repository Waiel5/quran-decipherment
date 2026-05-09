---
test_id: Q072-F-03
title: Q 72:1-19 (jinn-confession) and Q 46:29-32 (Aḥqāf jinn-pericope) lexical-similarity vs length-matched corpus null
hypothesis_class: paired-pericope-cohesion
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
rules_tuple: "(no-tashkeel, orthographic tokens (whitespace-split, no normalization), Jaccard on type-sets, length-matched permutation null over all eligible same-length windows, basmala-counted-only-in-Q1, Hafs-Kufan)"
bonferroni_k_local: 1
alpha_local: 0.05
---

# Q072-F-03 — Q 72:1-19 ↔ Q 46:29-32 jinn-pericope lexical-similarity vs null

## Hypothesis

The two surviving Quranic pericopes that explicitly narrate the jinn-listening-to-recitation event — **Q 72:1-19 (the jinn-confession block, opening with *qul ūḥiya ilayya annahu istamaʿa nafarun mina al-jinn*) and Q 46:29-32 (the al-Aḥqāf jinn-pericope, opening with *wa-idh ṣarafnā ilayka nafaran mina al-jinn yastamiʿūna al-qurʾān*)** — share more lexical content (orthographic-token Jaccard) than a length-matched random pair drawn from the corpus.

## Theoretical rationale

Classical tafsir (al-Biqāʿī *Naẓm al-Durar* §Q72, ad loc.; al-Rāzī *Mafātīḥ* ad Q 46:29 and Q 72:1; Abū Ḥayyān cited in Biqāʿī) explicitly debates whether these are the **same event narrated twice** or **two distinct events**. Both pericopes share the diagnostic phrasing *nafarun mina al-jinn* (a Quranic-hapax pairing — *nafar* appears only in jinn-contexts in Q 46:29 and Q 72:1), and both report a jinn-listening + jinn-confession sequence.

If the two pericopes share an unusually high token overlap relative to length-matched corpus windows, this empirically validates the classical "same-event" reading (or at minimum confirms strong lexical-shared-formula composition). If overlap is statistically typical, the pericopes are distinct-events with distinct vocabulary.

## Pre-committed prediction

**Direction: PASS** — Jaccard(Q 72:1-19 tokens, Q 46:29-32 tokens) > 95%ile of length-matched corpus-null at α = 0.05.

## Null distribution

The Q 72:1-19 block is held FIXED. The Q 46:29-32 block is replaced by 10,000 random verse-windows drawn from the corpus matching its (verse-count, total-word-count) profile within ±25% on word count. For each draw, compute Jaccard(Q 72:1-19, draw); the null distribution is over these Jaccards. The window must NOT overlap Q 72 itself.

## Window-pair geometry

- Q 72:1-19: 19 verses, ~193 tokens.
- Q 46:29-32: 4 verses, ~73 tokens.

Note the asymmetric verse-counts — Q 46:29-32 is the SHORT block; Q 72:1-19 is the LONG block (which absorbs and re-narrates the same event with embedded reported speech). Null draws match the SHORT block's word-count (≈73 words ±25%, i.e. ≈55-91 words) drawn from ANY contiguous verse-window in the corpus excluding the two reference blocks themselves.

## Success criteria

- **PASS (PRIMARY)**: observed Jaccard > 95%ile of 10,000-perm null (one-sided p ≤ 0.05).
- **DIRECTIONAL**: observed Jaccard > null mean but p > 0.05.
- **NULL**: observed Jaccard ≤ null mean.

## Companion observable

Beyond Jaccard, record the size of the shared-token intersection and which specific tokens appear in BOTH pericopes — focus on the jinn-event diagnostic vocabulary (*al-jinn*, *nafar*, *istamaʿa*/*samiʿnā*, *qurʾān*, *yahdī*/*hudā*, *qawmihim*, *āmannā*).

## Honest limit

Jaccard-on-orthographic-tokens is a coarse instrument. Length-matched null controls for the LENGTH bias but NOT for the GENRE bias (both pericopes are reported-speech-from-the-jinn, which may share formula vocabulary because both quote jinn in similar register). The test is therefore a NECESSARY-NOT-SUFFICIENT check for shared-event reading. A PASS supports but does not prove the classical same-event interpretation; a NULL would weigh against it.
