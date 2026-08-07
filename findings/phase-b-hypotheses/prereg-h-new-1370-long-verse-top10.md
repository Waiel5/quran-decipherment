---
id: H-NEW-1370
title: Corpus top-10 longest-verses chronological + rhetorical-type profile
date_locked: 2026-05-09
seed: 20260509
n_perm: 0
bonferroni_k: 1
bonferroni_family: H-NEW-1370-long-verse-top10
alpha_bon: 0.05
direction_of_effect: Of the top-10 longest verses in the canonical corpus (ranked by word-count and separately by character-count, no-tashkeel default), at least 7 belong to Medinan surahs.
origin: Follow-up to Q073-F-05 (Q 73:20 is corpus rank-3 longest verse at 90 words / 430 chars). Q073-F-05 surfaced corpus-top-3 = {Q 2:282, Q 4:12, Q 73:20}. The remaining top-10 was not chronologically profiled. This pre-reg locks the Medinan-domination prediction.
verdict_ceiling: PASS-DIRECTED (single planned pre-registered binomial test; INDEPENDENT REPLICATION required for promotion)
rules_tuple:
  orthography: no-tashkeel
  word_definition: split-on-whitespace (orthographic-token)
  letter_definition: non-space-character (graphemes)
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  ranking_basis: descending by word_count primarily; ties broken by descending char_count; secondary ranking by char_count separately reported
  chronological_source: data/revelation-order.csv field "period" (Meccan/Medinan) — al-Suyūṭī Itqān / Egyptian Standard
---

# H-NEW-1370 pre-registration


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Origin

Q073-F-05 (commit `08313cc15` and earlier) confirmed Q 73:20 is corpus rank-3 longest verse by word-count (90 words, 430 chars) and rank-1 within Early-Meccan subset. The Q073-F-05 output incidentally surfaced the corpus top-25 list. The top-3 corpus list is {Q 2:282, Q 4:12, Q 73:20}. This pre-reg locks the chronological + rhetorical-type profile of the corpus top-10 BEFORE inspecting the remaining ranks.

## Hypothesis

The 114-surah canonical corpus is split ~28 Medinan / ~86 Meccan (per `data/revelation-order.csv` `period` field). The Medinan share of corpus verses is ~37% (Medinan averaging longer verses), Meccan ~63%. If verse-length were uniformly distributed by chronological phase, the expected Medinan count in the top-10 would equal the Medinan share of the corpus by verse-count (not by surah-count).

**Direction-locked prediction**: ≥7 of the top-10 longest verses by word-count are Medinan. The competing null is that the Medinan share in the top-10 matches the corpus-wide Medinan share of verses.

Mechanism prior (NOT a post-hoc gloss): Medinan surahs contain almost all of the corpus's jurisprudential expansion (debt law, inheritance, jihād, marital law, food law, oaths). Jurisprudential expansion encodes legal preconditions and exceptions, which inflate per-verse length. The famous "debt verse" Q 2:282 is exhibit A; the inheritance verses Q 4:11-12 are exhibit B.

## Test design

### Primary test (Cell A — binomial, word-count ranking)

- Compute every verse's word-count using `text.split()` on the no-tashkeel canonical text.
- Sort descending; take the top-10 with ties broken by descending char-count.
- Tag each with the surah's `period` field from `data/revelation-order.csv`.
- One-sided binomial: H₀ = Medinan share in top-10 equals corpus-wide Medinan verse-share (computed at runtime from JSON + revelation-order.csv). Test statistic = observed Medinan count in top-10. Reject H₀ if observed ≥ 7 with p ≤ 0.05.

### Cell B (replication — character-count ranking)

Same procedure ranking by `char_count` (non-space character count) instead of word-count. Pre-locked: report rank-list, Medinan count, and binomial p separately.

### Cell A and Cell B are NOT a Bonferroni family

Cell A is the primary hypothesis. Cell B is a replication on the same data with a different (closely related) metric. Reporting both — primary is Cell A, Cell B is auxiliary replication; Cell B does NOT inflate α for Cell A.

### Additional descriptive analysis (NOT hypothesis-locked)

For each top-10 verse (both rankings), identify and report:
1. Surah ID + verse ID + word-count + char-count
2. Surah's `period` (Meccan/Medinan)
3. Surah's `noldeke_phase` (Early/Middle/Late Meccan or Medinan)
4. Rhetorical TYPE — one of {debt-and-contract, inheritance-and-bequest, ritual-instruction, marital-and-family-law, food-and-purity-law, jihād-and-warfare, polemical-narrative, prophetic-address-vocative, mixed-jurisprudential, other}. Assignment is human-coded based on the verse's primary thematic content. This is descriptive cataloging, NOT a statistical test.

### Acceptance windows

| Cell A (word-count Medinan ≥ 7) | Verdict |
|:-:|:--|
| Yes, p ≤ 0.05 | PASS-DIRECTED |
| Yes, p > 0.05 | DIRECTIONAL |
| No, but ≥ 5 Medinan | PARTIAL (under-powered toward direction) |
| No, < 5 Medinan | NULL |
| Medinan = 0 | PRE-COMMIT VIOLATION (direction reversed) |

### Garden-of-forking-paths

- Origin disclosed: extension of Q073-F-05 corpus top-25 list. The Q073-F-05 JSON contains the full top-25 ranking already on disk; I have **not viewed** the chronological tags for ranks 4-10 before locking this pre-reg.
- Direction locked at ≥7 Medinan.
- Ranking metric: word-count primary, char-count auxiliary, both pre-committed.
- Rules-tuple is the project default no-tashkeel/whitespace tokenization.
- Rhetorical-type taxonomy is human-coded; the 9 type labels above are pre-committed; assignments will be reported per-verse and verifiable from the cited verse text + classical tafsir summary.

### Anti-flip

A reversed direction (Medinan < corpus baseline, i.e., Meccan-dominated top-10) is NOT a reportable PASS. Publish as NULL with reverse-direction note. The Medinan-dominated prediction is mechanistically motivated (jurisprudential expansion) and must hold in its locked direction.

## Connection to existing findings

- **Q073-F-05** confirmed Q 73:20 is corpus rank-3 by word-count. This pre-reg profiles the remaining 9 entries.
- **H-NEW-770 verse-length compression-tail (kink-50 law)** establishes verse-length as a structural axis with R²=0.81. The top-10 outliers test the upper-tail residual of that law.
- **Cross-finding-016 Late-Meccan apparatus** and **cross-finding-018 Medinan jurisprudence**: Medinan-domination at the top-10 verse-length tail would support the architectural separation between Meccan kerygmatic-rhetoric (short verses, dense rhyme) and Medinan jurisprudential-expansion (long verses, sparse rhyme).
- **Q 2:282 debt verse**: classically the longest verse in the Quran (al-Suyūṭī Itqān nawʿ 19; al-Zarkashī Burhān). Confirmation that Q 2:282 is rank-1 in the canonical corpus by word-count is a sanity check on the instrument.

## Pre-commit attestation

Locked by SHA256. Run script verifies SHA before computing.

## Computation plan

1. Load `quran-text/quran-no-tashkeel.json`.
2. Load `data/revelation-order.csv` for `period` and `noldeke_phase`.
3. Enumerate (surah, verse) pairs; compute word-count and char-count per verse.
4. Sort by word-count descending; take top-10.
5. Tag with period and noldeke_phase.
6. Compute corpus Medinan-verse-share (count of Medinan-period verses / total).
7. One-sided binomial: P(X ≥ k | n=10, p=medinan_share) where k = observed Medinan count.
8. Repeat ranking by char-count.
9. Emit JSON.
10. Verdict per acceptance window.
