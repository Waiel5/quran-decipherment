# Numerical Coincidences — Run 1 Journal

**Agent:** numerical-coincidences-1
**Date:** 2026-04-12
**Output:** `findings/phase-b-hypotheses/numerical-coincidences.md`
**Script:** `scratch/numerical-coincidences/analyze.py`

## Goal

Build a unified reference for famous numbers in the Quranic apologetic
literature. For each N, answer: "what does the Quran *look like* at N?"
across eight axes (surah verse counts, verse word counts, verse letter
counts, abjad-N word forms, thematic neighborhood, famous-word abjad
matches, spelled-out numerals, lemma counts).

## Approach

1. Read methodology + statistical-rigor + claims-catalog. The protocol
   is clear: this dossier is **exploratory** (no pre-registration), so
   nothing here is a "finding," only a starting point for Phase B
   pre-registered tests.

2. Single Python script (`scratch/numerical-coincidences/analyze.py`)
   that loads `quran-no-tashkeel.json` (intact per `text-shape` audit)
   and the QAC v0.4 morphology, then computes every cell programmatically.

3. Locked anchors first (matching `methodology.md §8`): 114 surahs,
   6236 verses, 77797 real-word tokens, 330709 letters, Bismillah = 19
   letters / 4 words / abjad 786. All match.

4. Per-number sections written for: 1, 3, 4, 5, 7, 9, 10, 12, 14, 19,
   28, 30, 40, 50, 70, 72, 77, 99, 100, 114, 313, 365, 786, 1000, 12000,
   50000.

5. Buckwalter lemma keys verified against `probe_lemmas.py` first (the
   first run had wrong keys for Maryam, Adam — caught Adam=`A^dam` and
   Maryam=`maroyam` correctly on second pass).

## Hits worth flagging (NOT YET TESTED — exploratory only)

The dossier's "Top 12 striking coincidences" section captures my
short-list. The three I'd lead a write-up with:

1. **`raHomap` (mercy) lemma count = 114**.
   The Quran's central self-description matches its surah count exactly.
   Out of 4832 unique QAC lemmas, exactly 1 has this count.
   Whether 114 is "interesting" in 1/4832 terms depends on the prior
   that "the count of *some* central concept matches *some* structural
   constant." That's a forking-paths question. Pre-register a test.

2. **Adam = Isa = 25 (lemma counts, REPLICATES)**.
   Famous parity claim from the popular literature. The QAC counts are
   exactly 25 each for `A^dam` and `EiysaY`. This is both reproducible
   and theologically loaded — Quran 3:59 explicitly compares them. It is
   the cleanest pair in the dossier.

3. **`shams` (sun) = 33, `qamar` (moon) = 27, root counts also 33 / 27**.
   Both are well-documented apologetic claims and they REPLICATE for
   the QAC lemma counts. 27 is the lunar sidereal period (27.32 days).

Other replicating claims that would be too easy to dismiss as base-rate
but should still be in the test register:
- **shaytan = malak = 88** (parity, REPLICATES)
- **jahannam = 77** (and `>amara` = 77 also) — replicates the famous
  Khalifa-attributed claim
- **Surah 25 (Al-Furqan) is the only surah with exactly 77 verses**, and
  jahannam appears 77 times — twin coincidence
- **Surah 19 = Maryam, only chapter named for a woman**. Maryam lemma = 34
  occurrences. This is the famous "more times than the New Testament"
  factoid; numerically it replicates.
- **Bismillah letters = 19, words = 4, abjad = 786** — Khalifa anchor
  REPLICATES.
- **wahid (واحد) abjad = 19** under mashriqi convention. Yields a
  beautiful 'word for one' = 'Khalifa's 19' result.
- **huda (هدى) abjad = 19, surface count 38 = 2 × 19**. Similar.
- **171 verses (= 19 × 9) have exactly 19 letters** under no-tashkeel.
- **28 verses have exactly 1 orthographic word** — and these are dominated
  by the muqatta'at openings. 28 = number of letters in Arabic alphabet.
- **qaAlu (3MP perfect "they said") = 332 = rasul lemma count**. This is
  *not* the famous Al-Kaheel "qul = qala" claim; it's a different pairing
  that works under QAC. The Al-Kaheel claim itself does *not* replicate
  cleanly (qul IMPV all = 349, qaAla PERF all = 1004, ratio almost 3:1).

## Claims that DO NOT replicate under our rules tuple

- **Allah = 2698 (Khalifa's 19×142 anchor)**. Our QAC count is 2699.
  Khalifa rejected 9:128-129 to get to 2698 — well-documented in Bilal
  Philips 1987.
- **yawm = 365 (solar year)**. Our QAC `yawom` lemma count = 405. Refuted.
- **hayat = mawt = 145**. Our `Hayaw\`p` = 76, `mawot` = 50. Refuted.
- **qul = qala** (any Al-Kaheel-style version): differ by hundreds.
  The "equality" exists only for cherry-picked subsets.
- **Maryam abjad does anything special**: it sums to 290, no famous
  match.

## Methodological self-criticism

This dossier is, by construction, a Bible-Codes-style exercise: I
enumerated dozens of cells (8 cells × 26 numbers ≈ 208 statistics), and
every "hit" I report is one cell out of those 208+. Under any honest
multiple-comparison correction, the threshold for a single cell being
"surprising" is tight. Nothing here is published as a finding. The
purpose of the dossier is to give Phase B a *menu* of pre-registration
candidates.

The next step is for someone to pick one of the top-12 striking items,
write a pre-registration markdown under
`findings/phase-b-hypotheses/pre-reg/`, run the right null model from
`§1.6` of the rigor protocol, and publish the result regardless of
direction.

## Files written

- `findings/phase-b-hypotheses/numerical-coincidences.md` — the dossier,
  ~92 KB, ~2200 lines.
- `scratch/numerical-coincidences/analyze.py` — reproducible script.
- `scratch/numerical-coincidences/probe_lemmas.py` — lemma key probe.
- `scratch/numerical-coincidences/probe_extra.py` — extra lemma counts.

## Cross-references for the test register

If/when these become Phase B targets:
- `raHomap` count = 114 — needs comparable-corpus null (1.4)
- `A^dam` = `EiysaY` = 25 — needs lemma-shuffle null and comparable-corpus
- `$amos` = 33, `qamar` = 27 — needs lemma-shuffle null
- `jahan~am` = 77 — needs lemma-shuffle null
- `wahid` abjad = 19 (a number-theoretic claim, not a count) — needs
  null over alternative gematria conventions

## Notes on data quality

- `quran-no-tashkeel.json` is the only intact flat text per the
  `text-shape` audit. All counts here use it.
- QAC v0.4 lemma counts are *not* the same as a surface-form filter;
  for any literature claim that gives a specific number, we need to
  check whether the claimant's count matches lemma, surface, or
  surface+prefixes. For the famous parity claims (Adam/Jesus,
  shams/qamar) the lemma count works under QAC.
- Whole-token Arabic searches in no-tashkeel will *miss* prefixed
  forms like `بالله`, `لله`, `الله` separately. This is why our
  whole-token Allah count is 2153 while the QAC lemma count is 2699.

## Time spent

Approx. 90 minutes total: 30 reading methodology + claims, 30 writing
the script (with 2-3 lemma-key bug-fix iterations), 20 inspecting
output and refining the synthesis section, 10 writing this journal.
