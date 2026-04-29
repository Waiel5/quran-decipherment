---
id: H-NEW-66
title: Verse-pair structural-twin network — corpus-wide
phase: B
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (BEFORE any pair-similarity computation runs)
parent: H-NEW-8 (twin-opener Lock — 2 surah-pairs ≥30 char prefix); H-NEW-58b (surah-pair shared prefix; auto-recovered musabbiḥāt)
seed: 20260416
rules_tuple: (no-tashkeel; whitespace-tokens; basmala-only-in-Q1; recitation-marks stripped from text before n-gram extraction)
---

# [[h-new-66-verse-twins-network|H-NEW-66]] — Verse-Pair Structural Twin Network (Pre-registration)

## Question

For each of the 6,236 verses, what is its most-similar OTHER verse in
the corpus? When we knit those top-1 directed pointers together, does
the resulting **twin-network** show non-random structure (heavy-tailed
in-degree, mutual edges = 2-cycles, intra-surah enrichment, etc.)?

## Locked similarity metric (chosen and frozen BEFORE execution)

**Primary metric: shared 5-character n-gram count (raw count, not Jaccard).**

For each verse v with normalized character string s(v):

1. Strip tashkeel (already absent in `quran-no-tashkeel.json` body) and
   strip the recitation-mark glyphs `ۖ ۗ ۘ ۚ ۛ ۜ ۝ ۞` and any character
   in the Unicode "Arabic Pause Marks" + standalone honorifics. Then
   collapse whitespace to single spaces, strip leading/trailing.
2. Slide a length-5 character window across s(v) including the spaces.
   Build the multiset N5(v) of length-5 strings.
3. For pair (v, v'), similarity sim(v, v') = |N5(v) ∩ N5(v')| where
   the intersection is taken as a multiset intersection (min of counts).

Locked rationale: 5-character n-grams are the smallest window that
captures meaningful Arabic morpheme spans (typical root + prefix or
root + suffix). Raw count, not Jaccard, deliberately rewards longer
verses that genuinely share substring material — the H-NEW-8 finding
is *length*-of-shared-prefix, not normalized similarity. Jaccard would
artificially demote the very Q 2:149-150 / Q 59:22-23 case the parent
hypothesis identified.

## Locked filters (chosen BEFORE execution)

- **Min-word threshold (locked): 5 words per verse.** Verses with fewer
  than 5 whitespace-tokens (after strip) are EXCLUDED from being either
  source or target in the twin lookup. Rationale: avoids trivial
  single-word twins (e.g. الحمد لله رب العالمين-style fragments matching
  by a single word), and matches the H-NEW-8 ≥30-char-prefix spirit.
- **Adjacency exclusion (locked): same surah, |Δid| ≤ 2.** A verse
  cannot have its top-1 twin be in the same surah within 2 verses of
  itself (catches v±1, v±2, and v itself). Cross-surah pairs are NEVER
  excluded by adjacency; the prohibition is intra-surah-only.
- **Self exclusion: trivially, v ≠ v'.**

## Procedure (locked)

1. Load `quran-no-tashkeel.json` via the standard loader.
2. Normalize all 6,236 verses; build N5 multisets.
3. Mark each verse as ELIGIBLE (≥5 words after strip) or INELIGIBLE.
   Ineligible verses are still included as POTENTIAL targets for
   eligible sources? **Locked: NO.** Both source and target must be
   eligible. Report total eligible count.
4. For each eligible v, scan all other eligible v', compute sim(v, v')
   (skipping the adjacency-excluded ones), record top-1 target =
   argmax sim and its score.
5. Build the directed graph G with one out-edge per eligible source.
6. Compute graph stats:
   - in-degree distribution (k → count of nodes with that many incoming)
   - mutual-edge count (v→v' AND v'→v): these are the 2-cycles
   - weakly-connected component sizes (sorted)
   - intra-surah out-edge fraction (out-edges where source.surah == target.surah)
   - top-50 highest-similarity edges across the whole corpus
7. Null model (locked): per-verse character shuffle using
   `tools.shuffler.shuffle_characters` with seed = 20260416 + 1000*v_index
   (i.e. reproducible per-verse seeds). Recompute the entire pipeline
   on the shuffled text; report the same statistics.

## MW-5 method-witness (positive control)

The Q 2:149 ↔ Q 2:150 pair (the H-NEW-8 ≥30-char twin opener) MUST
appear in the top-50 highest-similarity pairs. If it does not, the
instrument is broken and the run is logged as INSTRUMENT-FAIL.

## What counts as PASS / NULL / NOTABLE

This is an **exploratory/structural** hypothesis: there is no single
test statistic to declare PASS/NULL on. The pre-registered claims are:

- **NOTABLE-1**: top-1 in-degree is heavy-tailed (max in-degree
  ≥ 3× median observed-vs-null ratio).
- **NOTABLE-2**: intra-surah out-edge fraction is ≥ 2× the null
  expectation.
- **NOTABLE-3**: mutual-edge count exceeds null mean + 3σ.

Each NOTABLE that fires is reported individually; none is required.
The deliverable is the published structure, not a binary verdict.

## Garden-of-forking-paths disclosure

Choices fixed BEFORE seeing any results:
- 5-char n-gram (vs Jaccard-trigram or shared-word) — chosen for
  H-NEW-8-consistency (length-rewarding, substring-based).
- Min 5 words — matches inferred lower bound of "non-trivial verse".
- |Δid| ≤ 2 adjacency exclusion (vs ±1 or ±5) — ±2 is a balance:
  catches the obvious Q 2:149-150-style adjacency but does not over-
  exclude longer-range within-surah parallelism.
- Per-verse character shuffle null (vs whole-corpus shuffle) — preserves
  per-verse character histograms; tests pure ORDER signal.
- Top-1 only (vs top-k) — minimum claim; top-k could be added in a
  later [[h-new-66-verse-twins-network|H-NEW-66]].k extension and is not part of this pre-reg.

## Data + outputs

- Input: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Loader: `/Users/grey/Downloads/quran/analysis/tools/loader.py`
- Shuffler: `/Users/grey/Downloads/quran/analysis/tools/shuffler.py`
- Script: `/Users/grey/Downloads/quran/scripts/h_new_66_verse_twins.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-66.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-66-verse-twins-network.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-66-run-1.md`

## Status

PRE-REGISTERED 2026-04-15. Spec locked before any verse-pair scan
runs. Seed 20260416 frozen.
