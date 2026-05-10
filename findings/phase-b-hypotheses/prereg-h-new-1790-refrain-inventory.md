---
id: H-NEW-1790
title: Refrain-architecture full corpus inventory — strict (≥3) and broad (≥2) verbatim verse-repetition per surah
date_locked: 2026-05-10
seed: 20260510
n_perm: 0  # deterministic ranking — no permutation required for inventory
bonferroni_k: 2
bonferroni_family: H-NEW-1790-refrain-inventory
alpha_bon: 0.025
direction_of_effect: |
  Cell A: Q 55 al-Raḥmān is corpus-rank-1 by refrain-saturation (max_repeat / verse_count under strict ≥3 verbatim-repetition definition), consistent with H-NEW-1320.
  Cell B: at least 5 surahs OTHER THAN Q 55 contain at least one verse repeated verbatim ≥3 times (strict refrain) within their own boundaries.
origin: |
  H-NEW-1320 located the 3-tier refrain architecture {Q 55, Q 77, Q 26}. H-NEW-1230 enumerated 5 refrain-bearing surahs. Neither produced an EXHAUSTIVE inventory of every verbatim-repeating verse in the corpus. This pre-reg formalizes the complete inventory — strict (≥3) AND broad (≥2) — across all 114 surahs.
verdict_ceiling: PASS-DIRECTED (handoff origin = single planned inventory test; INDEPENDENT REPLICATION required for promotion to CONFIRMED)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  verse_string_equality: exact-no-tashkeel-string-after-NFC-and-whitespace-normalization
  near_match_policy: NOT-IN-SCOPE (strict verbatim only; near-match would require Levenshtein and is left for future replication)
  reading_tradition: hafs-kufan
  script: mashriqi
---

# H-NEW-1790 pre-registration

## Hypothesis

The corpus contains a finite, enumerable set of surahs whose internal architecture includes verbatim verse-repetition. Two operational thresholds are tested:

- **STRICT**: a verse appearing verbatim ≥3 times within the same surah.
- **BROAD**: a verse appearing verbatim ≥2 times within the same surah.

### Cell A (inferential — saturation ranking)

Q 55 al-Raḥmān is corpus-rank-1 by refrain-saturation = max_repeat_count(s) / verse_count(s). This restates and extends H-NEW-1320 (which ranked by absolute count). Saturation normalises for surah length, so the test verifies that Q 55's signature survives even when corrected for its short length (78 verses).

### Cell B (descriptive — distribution breadth)

Among the 114 surahs, the count N_strict of surahs containing ≥1 strict-refrain (verse appearing verbatim ≥3 times within that surah) satisfies N_strict ≥ 5 and N_strict ≤ 15. This is a window pre-commitment.

## Test design

### Statistics

For each surah s ∈ {1, ..., 114}:

1. Load `quran-text/quran-no-tashkeel.json`.
2. NFC-normalise; collapse internal whitespace; strip leading/trailing whitespace.
3. Build `Counter(verses_in_surah_s)`.
4. Record:
   - `max_repeat_count(s)` — top frequency in the Counter (=1 if all unique).
   - `strict_refrain_set(s)` — verses with frequency ≥ 3.
   - `broad_refrain_set(s)` — verses with frequency ≥ 2.
   - `saturation(s) = max_repeat_count(s) / verse_count(s)`.

### Cell A test

PASS if Q 55's `saturation(s)` is strict rank-1 across all 114 surahs.
NULL if any other surah ties or exceeds Q 55 on saturation.

### Cell B test

Compute `N_strict` = |{s : strict_refrain_set(s) is non-empty}|.
PASS if 5 ≤ N_strict ≤ 15.
NULL otherwise.

### Bonferroni

k = 2 (Cells A + B). α_bon = 0.025 per cell.

### Acceptance windows

| Cell A | Cell B | Verdict |
|:-:|:-:|:--|
| ✓ | ✓ | PASS-DIRECTED FULL |
| ✓ | ✗ | PASS-DIRECTED CELL-A only |
| ✗ | ✓ | PARTIAL (Cell B only) |
| ✗ | ✗ | NULL |

### Garden-of-forking-paths

The inventory is deterministic — no permutation required. The pre-commitments are:
- Saturation as the rank statistic for Cell A (NOT absolute count, which is H-NEW-1320's locked axis).
- Window [5, 15] for N_strict — derived from H-NEW-1230 (5 strict refrain surahs) and H-NEW-1320 (only top-3 reach count ≥ 8) as anchors; window ≥ 5 because H-NEW-1230 explicitly enumerated 5; ≤ 15 because no known prior finding suggests more than ~10-12 surahs cross threshold ≥3. Locked before computation.
- "Refrain" defined strictly as exact-verbatim verse-string match after NFC + whitespace normalisation; no near-match, no Levenshtein, no fuzzy matching.
- Cross-surah refrain-pairs (where the SAME verse repeats in TWO DIFFERENT surahs) are POST-HOC observational supplement, NOT pre-registered cells. Reported descriptively with MW-7 single-test cap (no Bonferroni reduction for the inventory result).

### Rules-tuple sensitivity

Tested on no-tashkeel only. Different tashkeel levels (min, full) could shift the strict-refrain count by collapsing or splitting vocally-distinct repetitions. Out-of-scope for this pre-reg.

### Anti-flip

Reversed direction (Q 55 NOT rank-1 by saturation; N_strict outside [5, 15]) is published with prominence as NULL or pre-commit violation per Protocol §1.8.

### MW-5 instrument-control

The bismillāh formula appears at the head of 113 surahs (Q 9 excluded) but is counted-only-in-surah-1 per rules-tuple. The Quran's full-text-data file under `quran-text/quran-no-tashkeel.json` lists verse strings per surah; the basmala is verse 1 of Q 1, and the opening of subsequent surahs is data-file-dependent. Verify under runtime that no surah other than Q 1 has the bismillāh string as a verse entry; if data file pre-strips it, that's the operational reality and the rules-tuple is met. Q 1:1 vs Q 27:30 cross-surah identity is INTRA-surah for neither — both verses are unique within their own surah, so this does NOT inflate the strict-refrain count.

## Outputs

- Top-10 surahs ranked by saturation (descending), with refrain-text + count + verse-count.
- Per-surah strict-refrain enumeration (every verse appearing ≥3 times).
- Per-surah broad-refrain enumeration count (every verse appearing ≥2 times) — count + count of unique broad-refrain verses.
- Cross-surah refrain-pair table (every verse-string that appears in MORE THAN ONE surah, with surah list + total count) — post-hoc supplement.
- Comparison to H-NEW-1320 3-tier finding {Q 55, Q 77, Q 26}.

## Connection to existing findings

- **H-NEW-1320**: 3-tier refrain architecture {Q 55 / Q 77 / Q 26} ranked by absolute count. This pre-reg uses SATURATION (count / verse_count), which is a complementary axis.
- **H-NEW-1230**: 5 refrain-bearing surahs {Q 55, Q 77, Q 26, Q 54, Q 37} — H-NEW-1230 used combined-refrain-count across multiple refrains per surah; this pre-reg uses MAX single-refrain-count.
- **Cross-finding-027 (H-NEW-1250)**: Q 55 dual-audience architectural signature — this inventory verifies that Q 55's saturation rank survives length-normalization.
- **H-NEW-1190** *wa-mā adrāka mā* (cross-surah refrain family) — distinct from intra-surah refrain; the cross-surah supplementary table will surface any overlap.
- **al-Suyūṭī** *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on *al-takrīr fī al-Qurʾān*: classical takrīr taxonomy includes both intra-surah (lafẓī) and cross-surah refrain (maʿnawī). This finding focuses on intra-surah lafẓī.
- **al-Zarkashī** *al-Burhān fī ʿulūm al-Qurʾān*, *al-nawʿ al-tāsiʿ wa-l-arbaʿūn* (the 49th type — *takrār*): the classical typology of repetition. This empirical inventory tests the corpus-distribution of intra-surah lafẓī takrār.

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. Direction locked: Q 55 saturation rank-1; N_strict in [5, 15]. Any reversal published as NULL with prominence per Protocol §1.8.
