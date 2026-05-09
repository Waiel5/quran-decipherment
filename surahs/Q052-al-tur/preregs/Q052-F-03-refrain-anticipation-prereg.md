---
finding: Q052-F-03
title: "Q 52:11 fa-waylun yawmaʾidhin li-l-mukadhdhibīn is the EARLIEST and ONLY-non-{Q 77, Q 83} corpus-occurrence of the Q 77-refrain"
seed: 20260509
date_locked: 2026-05-09
prereg_locked_before_results: true
bonferroni_k: 3
bonferroni_family: Q052-F-03-refrain-anticipation
alpha_bon: 0.0167
direction_pre_registered: true
---

# Q052-F-03 PRE-REG: Q 52:11 is the corpus-EARLIEST mid-mushaf advance-instance of the Q 77 *waylun yawmaʾidhin li-l-mukadhdhibīn* refrain

## 1. Hypothesis (pre-locked)

**H1 (corpus-EXACT distribution)**: The substring "ويل يومئذ للمكذبين" (no-tashkeel) appears in **exactly 12 verses** in the corpus, distributed across **exactly 3 surahs** {Q 52, Q 77, Q 83} with the following breakdown:
- Q 52 al-Ṭūr: 1 occurrence (v.11)
- Q 77 al-Mursalāt: 10 occurrences
- Q 83 al-Muṭaffifīn: 1 occurrence

**H2 (mushaf-position-earliest)**: Q 52:11 (mushaf position s=52) is the EARLIEST mushaf-occurrence of the refrain among all 12 occurrences.

**H3 (mid-mushaf-isolation)**: Q 52:11 is the ONLY occurrence of the refrain OUTSIDE the immediate Q 77 + Q 83 "short-Meccan-tail eschatology cluster" (per H-NEW-1200). Q 77 and Q 83 are mushaf-adjacent within the larger Q 77-83 region; Q 52 is structurally isolated 25 mushaf-positions earlier.

## 2. Test statistic and operationalization

For the substring "ويل يومئذ للمكذبين" (no-tashkeel):

1. Load `quran-text/quran-no-tashkeel.json`.
2. For each verse v across all 6,236, check whether v.text contains the exact substring "ويل يومئذ للمكذبين".
3. Aggregate by surah; record (surah_id, verse_id, full_text) for each match.
4. Compute mushaf-order earliest position.

## 3. Pass criteria

- **H1 PASS**: total_count == 12 AND surahs == {52, 77, 83} AND counts in each are {52:1, 77:10, 83:1}.
- **H2 PASS**: min(mushaf_position) == s=52, and Q 52:11 is the earliest verse.
- **H3 PASS**: Q 77 and Q 83 are mushaf-position-near (s=77 and s=83, distance 6); Q 52 is mushaf-isolated (gap = 25 mushaf-positions to nearest other refrain-bearing surah).

Bonferroni-3 protection: each cell (H1, H2, H3) at α_bon = 0.0167 single-test equivalent. The tests are deterministic-count, not p-value tests, so the Bonferroni protects against multi-test inflation.

## 4. Rules tuple

- text source: `quran-text/quran-no-tashkeel.json`
- substring: exact match for "ويل يومئذ للمكذبين" (the lowercase tail of *fa-waylun* matches via the *waylun* substring; we search the substring without the leading wa-/fa- to capture all variants).
- with-leading-fa- variant: Q 52:11 has *fa-waylun*; Q 77/Q 83 have plain *waylun*. The substring search uses the un-prefixed form, so all variants are captured.
- inclusion: all 6,236 verses; no exclusion.

## 5. Bonferroni declaration

- bonferroni_k: 3 (H1 + H2 + H3)
- bonferroni_family: Q052-F-03-refrain-anticipation
- alpha_bon: 0.0167
- pre-committed acceptance window: 3 binary checks, all must pass for CONFIRMED.

## 6. Direction pre-registered

H1: refrain is corpus-distributed exactly as specified.
H2: Q 52:11 is mushaf-earliest.
H3: Q 52:11 is mushaf-isolated by ≥10 mushaf-positions from the next-nearest refrain-bearing surah.

## 7. Garden-of-forking-paths

- Pre-registration origin: this hypothesis emerged from inline-substring-search 2026-05-09 during construction of the Q 52 specialist deliverable; al-Rāzī (*Mafātīḥ al-ghayb* vol. 28 pp. 247-250) provides the classical-anchor reading. Independent confirmation was obtained from the on-disk Quran JSON corpus before the formal write-up of `06-novel-findings.md`.
- 3 cells pre-locked.
- No post-hoc alternatives considered.

## 8. Empirical anchor

This test directly extends:
- H-NEW-1230 (refrain-architecture): Q 77 has the corpus's clearest 10× refrain.
- al-Rāzī, *Mafātīḥ al-ghayb* (classical-anchor reading of Q 52:11 as advance-instance).
- al-Suyūṭī, *al-Itqān* nawʿ 63 al-takrār (classical typology of refrain).
- cross-finding-013 (mushaf-as-ring-topology): a 25-mushaf-position anticipation is a Layer-3-or-stronger cross-surah signal.

## 9. Pre-reg SHA-256 lock

Locked at script-runtime; recorded in `csv/Q052-F-03.json`.

## 10. Author

waiel — pre-reg locked 2026-05-09.
