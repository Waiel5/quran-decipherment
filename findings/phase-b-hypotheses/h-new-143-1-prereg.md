---
finding_id: h-new-143-1
title: "Root-level rhetorical-bridge test — ROOT morphological-overlap across mushaf boundaries"
specialist: specialist-a
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 3
bonferroni_family: h-new-143-1-root-bridge
alpha_bon: 0.0167
direction_primary: "Top-15 Fisher-Rao-jump boundaries (on at least one of root/char/vlen feature spaces) have HIGHER mean root-overlap bridge strength than other boundaries. Pre-committed positive direction. One-sided upper-tail."
direction_secondary_universal: "The 3 universal Fisher-Rao hinges (Q 14→15, Q 49→50, Q 56→57) have root-overlap bridge strength ABOVE the 50th-percentile of all 113 boundaries (pre-committed)."
direction_secondary_boundary_type: "Within each boundary-type class in B (|B|=54), root-overlap bridge strength is reported. Descriptive, no inferential claim pre-committed."
K_top: 15
rules_tuple: "(QAC-STEM root tokens, last-verse-of-surah-i ∩ first-verse-of-surah-i+1, root-set Jaccard + cosine)"
parent_finding: h-new-143 (surface NULL)
parent_h142: h-new-142 (post-hoc rhetorical-bridge observations)
---

# [[h-new-143-1-root-bridge|H-NEW-143.1]] — Root-level rhetorical-bridge test

## Motivation

[[h-new-143-surface-word-bridge-null|H-NEW-143]] showed that SURFACE-WORD token overlap across boundaries does NOT discriminate top-15 FR-jump boundaries from others (NULL, all 12 tests p > 0.6). The proper instrument for classical munāsabāt is ROOT-level (morphological) overlap, not surface-word.

[[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] post-hoc observed rhetorical bridges at the 3 universal FR hinges:
- Q 14→15: بلاغ→آيات الكتاب (message-about-message)
- Q 49→50: غيب السماوات→والقرآن المجيد (divine knowledge → Quran oath)
- Q 56→57: فسبح→سبح (tasbīḥ imperative → execution)

The Q 56→57 bridge is explicitly ROOT-level (س-ب-ح root shared). Q 14→15 and Q 49→50 are thematic/semantic, possibly detectable via root-overlap.

**Test**: does root-overlap between last-verse-of-surah-i and first-verse-of-surah-i+1 discriminate top-15 FR-jump boundaries from others?

## Hypothesis

**Primary (H1).** Mean root-overlap bridge strength at top-15 FR-jump boundaries is HIGHER than at other 98 boundaries. One-sided Mann-Whitney U. Pass at p < 0.0167 (Bonferroni-3).

**Secondary (H2) — universal hinges.** The 3 universal FR hinges (Q 14→15, Q 49→50, Q 56→57) have root-overlap ABOVE the 50th-percentile of all 113 boundaries.

**Secondary descriptive.** Root-overlap distribution broken down by B-boundary-type. No inferential claim.

## Pre-committed method

### Data

- Root-tokens per verse: QAC v0.4 STEM-segment root attributions (same as [[h-new-111-fisher-rao-mushaf|H-NEW-111]] feature space).
- Boundary-set B: frozen from [[h-new-130-fisher-rao-residuals|H-NEW-130]] (|B|=54).
- Top-15 sets: frozen from [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b/130c.
- Universal hinges: {Q 14→15, Q 49→50, Q 56→57} frozen from [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]].

### Bridge-strength definition

For each of 113 boundaries (i, i+1):
1. Let R_last(i) = set of QAC-STEM roots in the LAST verse of surah i.
2. Let R_first(i+1) = set of QAC-STEM roots in the FIRST verse of surah i+1.
3. Bridge strength metrics:
   - `root_overlap_count` = |R_last(i) ∩ R_first(i+1)|
   - `root_cos` = |R_last(i) ∩ R_first(i+1)| / √(|R_last(i)| · |R_first(i+1)|)
   - `root_jaccard` = |R_last(i) ∩ R_first(i+1)| / |R_last(i) ∪ R_first(i+1)|

Primary metric: **root_cos**. Robustness: overlap_count and jaccard reported.

### Primary test

Mann-Whitney U: top-15 FR-jump boundaries (using union across 3 feature spaces to be inclusive; if any pair is top-15 in ≥1 feature space, include) vs. all other boundaries. One-sided upper-tail.

Alternative specification: run separately for each feature space's top-15 (3 sub-tests, Bonferroni-adjusted within the 3-family).

### Secondary: universal hinges

Rank each of the 3 universal hinges by root_cos among all 113 boundaries. Pass if all 3 are above 50th-percentile. Report specific ranks.

### MW-5

Synthetic sort-by-length ordering: compute root_cos for sort-by-length-adjacent pairs. Report mean and compare to mushaf-adjacent. No formal test; this is instrument-sanity.

## Pre-committed acceptance windows

- **PRIMARY PASS**: Mann-Whitney one-sided p < 0.0167 with top-15 mean > other mean.
- **PRIMARY NULL**: p ≥ 0.0167 OR direction reversal. Publish NULL with equal prominence.
- **SECONDARY UNIVERSAL**: PASS if all 3 hinges have root_cos above P50.
- **SECONDARY UNIVERSAL PARTIAL**: PASS if ≥ 2 of 3 above P50 (qualified).

## Garden of forking paths

- Using QAC-STEM roots because that's [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s feature basis (parent of all top-15 sets). Consistent methodology.
- Using last-1-verse / first-1-verse window because that's what classical munāsabāt scholarship focuses on (the juncture). 2-verse window could be a robustness check.
- Primary metric is cosine (symmetric, length-normalized). Jaccard and overlap-count are robustness.
- Not using surface tokens ([[h-new-143-surface-word-bridge-null|H-NEW-143]] NULL already established).

## Post-hoc-noticed disclosure

This pre-reg is written after [[h-new-143-surface-word-bridge-null|H-NEW-143]] NULL and BEFORE computing root-level bridge values. I have not yet extracted roots from boundary verses.

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_143_1_root_bridge.py`.
3. JSON `findings/phase-b-hypotheses/csv/h-new-143-1.json`.
4. Findings `findings/phase-b-hypotheses/h-new-143-1-root-bridge.md`.
5. Journal `journal/h-new-143-1-run-1.md`.
