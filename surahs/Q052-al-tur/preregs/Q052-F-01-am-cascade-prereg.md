---
finding: Q052-F-01
title: "Q 52 al-Ṭūr is corpus-EXACT rank 1 in *am*-rhetorical-question opener architecture"
seed: 20260509
date_locked: 2026-05-09
prereg_locked_before_results: true
bonferroni_k: 3
bonferroni_family: Q052-F-01-am-cascade
alpha_bon: 0.0167
alpha_bon_calculation: "single-test α=0.05 / k=3"
direction_pre_registered: true
---

# Q052-F-01 PRE-REG: Q 52 al-Ṭūr is rank-1 corpus-EXACT in *am*-rhetorical-question opener architecture

## 1. Hypothesis (pre-locked)

**H1 (3-axis test family)**: Q 52 al-Ṭūr is rank 1 of 114 surahs on each of three independent measures of *am*-rhetorical-question opener architecture:

- **H1a (absolute count)**: Q 52 has the highest count of verses opening with the surface-token أم (*am*).
- **H1b (density)**: Q 52 has the highest fraction of verses opening with أم among all 114 surahs (with min 5 *am*-openers as the inclusion threshold).
- **H1c (consecutive run)**: Q 52 has the longest consecutive run of verses opening with أم.

Direction is pre-registered: Q 52 should be **rank 1 (top)** on all three. Sign-flip would be EXPLORATORY-REVERSE.

## 2. Test statistic and operationalization

Computation pipeline (deterministic; no random draw):

1. Load `quran-text/quran-no-tashkeel.json`.
2. For each surah s ∈ {1..114}:
   - For each verse v in s, take the first whitespace-separated token of v.text.
   - n_am(s) = count of verses in s where first-token == "أم"
   - frac_am(s) = n_am(s) / total_verses(s)
   - longest_run_am(s) = max consecutive sequence of verses with first-token == "أم"
3. Compute corpus-rank of Q 52 on each measure.

## 3. Pass criteria

- **H1a**: rank 1 of 114 on n_am — PASS if corpus-rank == 1.
- **H1b**: rank 1 of 114 surahs (with n_am ≥ 5 inclusion threshold) on frac_am — PASS if corpus-rank == 1.
- **H1c**: rank 1 of 114 on longest_run_am — PASS if corpus-rank == 1 (ties allowed; PASS as long as no surah strictly exceeds Q 52).

Each test is a **deterministic count-comparison**, not a permutation null. Single-test α=0.05 with Bonferroni-3 correction (α_bon = 0.0167) does NOT apply directly because the tests are not p-value tests; they are **binary corpus-rank checks**. The Bonferroni-k=3 protection is for the **multi-test inflation** in the family.

If Q 52 fails any of H1a/H1b/H1c, the test is FAIL on that axis. If Q 52 passes all 3, the joint hypothesis PASSES at single-test level.

## 4. Rules tuple

- text source: `quran-text/quran-no-tashkeel.json`
- tokenization: whitespace split
- particle: surface-form `"أم"` (no-tashkeel-stripped; equivalent to QAC `Am` particle)
- consecutive-run definition: any sequence of ≥2 verses with first-token == "أم", measured maximum across the surah.
- exclusion: none (all 114 surahs included; Q 1's 7 verses are checked).

## 5. Bonferroni declaration (per PRE-REG-STANDARD-04)

- bonferroni_k: 3
- bonferroni_family: Q052-F-01-am-cascade
- alpha_bon: 0.0167 (single-test α=0.05 / k=3)
- pre-committed acceptance window: each of H1a/H1b/H1c is PASS iff Q 52 rank == 1 (or tied for 1st).

## 6. Garden-of-forking-paths log

- **Pre-registration origin**: this hypothesis emerged from inline-data-exploration during specialist-deliverable construction 2026-05-09. The discovery (Q 52 has 12 *am*-openers and a 9-verse consecutive run, corpus-EXACT rank 1) was **noticed via eyeballing** during initial Q 52 verse-text review. Per HANDOFF/04-DISCIPLINE post-hoc protocol, this is disclosed transparently:
  - Test family LOCKED before re-running formal corpus-rank computation: 3 tests (count, density, run).
  - Direction pre-registered: Q 52 = rank 1 on all 3.
  - Single-test α=0.05 cap protocol applies (post-hoc-noticed); but the tests are deterministic-count not probabilistic, so α-level is mainly a frame for multi-test inflation.
  - Verdict ceiling: **PASS-DIRECTED** unless replication on independent dimension.
  - Independent replication available: see Q052-F-02 (writing-cluster) and Q052-F-03 (refrain anticipation) — different feature spaces.
- **Why this 3-axis family**: the three measures (count, density, run-length) are pre-registered as the 3 most-natural orthogonal-but-related operationalizations of "how *am*-dense is this surah?". No alternative test cells were considered post-hoc.

## 7. Auxiliary computation

The script also computes (for reference, not for primary verdict):
- Top-15 surahs by absolute count (for context).
- Top-15 by longest consecutive run for any first-word (for the "tied-with-Q-26" framing).
- The Bukhārī #4647 strike-verses (Q 52:35-37) within the 9-verse run for hadith-anchor cross-reference.

## 8. Pre-reg SHA-256 lock

Computed at script-runtime; recorded in `csv/Q052-F-01.json` along with results. Locked at the time the script first executes against `quran-text/quran-no-tashkeel.json`.

## 9. Author

waiel — pre-reg locked 2026-05-09.
