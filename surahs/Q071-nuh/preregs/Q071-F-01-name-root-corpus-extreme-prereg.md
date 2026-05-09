---
finding_id: Q071-F-01
title: Q 71 Nūḥ name-root concentration — replication of H-NEW-86 framework on Q 71
parent_finding: H-NEW-86 (surah-name-as-key-root)
date_pre_registered: 2026-05-09
seed: 20260509
agent: Q 71 Nūḥ specialist (Waiel Al-Shujaa)
test_type: closed-form hypergeometric (no permutation)
bonferroni_family: Q071-novel-tests-2026-05-09
bonferroni_k: 5
alpha_bon: 0.01
direction_locked: TWO-SIDED but pre-committed expected enrichment direction (ratio_in > ratio_rest)
acceptance_window: p_two ≤ alpha_bon = 0.01 AND ratio ≥ 5 AND hits_in ≥ 3
mw5_positive_control: Q 12 Yūsuf (re-derive enrichment via same pipeline; expected p ≪ 1e-30)
mw7_internal_check: cross-reference H-NEW-86 csv for the same Q 71 entry to verify
---

# Q071-F-01 — Q 71 Nūḥ name-root concentration corpus-EXACT-extreme test

## 1. Hypothesis

Under the H-NEW-86 framework (surah-name-as-key-root, Leeds Quranic Arabic Corpus
v0.4 morphology, ROOT/LEM matching), the lexeme `nuwH` (the name Nūḥ as a proper-name
LEM) concentrates inside Q 71 at a rate significantly above the rest-of-corpus baseline
under hypergeometric two-sided p-value, with Bonferroni-114 correction for the
H-NEW-86 family-of-114 tests.

## 2. Pre-committed direction

The prediction is enrichment-direction: `ratio_in/ratio_rest > 1`. This is the
direction asserted by the parent H-NEW-86 finding for Q 71 (one of the 26 surahs
clearing the Bonferroni-114 cutoff in the parent test).

## 3. Method

- **Corpus**: Leeds Quranic Arabic Corpus v0.4 morphology, ROOT field (or LEM for
  proper-noun surah names like Nūḥ).
- **Target**: LEM = `nuwH` (Buckwalter transliteration of the proper-name Nūḥ).
- **Population**: 77,429 morphological tokens across 6,236 verses (per H-NEW-86 csv).
  Of these: 226 inside Q 71 (n_in), 77,203 outside Q 71 (n_rest).
- **Test statistic**: `hits_in` = count of `nuwH`-LEM occurrences inside Q 71;
  `hits_rest` = same outside Q 71.
- **p_two**: closed-form hypergeometric two-sided.
- **Effect size**: enrichment ratio = `(hits_in / n_in) / (hits_rest / n_rest)`.

## 4. Acceptance window

- p_two ≤ α_bon = 0.01 (i.e., 0.05 / 5 tests in this surah's family) **AND**
- enrichment ratio ≥ 5 **AND**
- hits_in ≥ 3

If all three conditions met → **PASS-DIRECTED**. If 2/3 met → **DIRECTIONAL**.
If only 1/3 met → **NULL**.

If the result is direction-reverse (ratio < 1), the verdict is **NULL** regardless
of p-value (this is a directional pre-reg).

## 5. Garden-of-forking-paths

- The H-NEW-86 parent test already published Q 71 as one of 26 Bonferroni-114
  passers (p_two = 2.78e-04, ratio = 25.62×, hits_in = 3). This Q071-F-01 is a
  REPLICATION-IN-CONTEXT test, NOT a new exploratory test. Its function is to
  re-anchor the surah-specific entry inside the surah's specialist deliverable.
- The H-NEW-86 ROOT-vs-LEM choice was locked at the parent-test pre-reg level;
  Q 71 uses LEM `nuwH` because Nūḥ is a proper noun. This is honored here.
- Bonferroni-114 (parent) is more conservative than Bonferroni-5 (this surah's
  family); per the bonferroni-asymmetry rule, the parent's Bonferroni-114
  control is the binding one (TIGHTENING is self-verifying).

## 6. Independent-replication notes

This test is a replication-in-context. An INDEPENDENT replication on a distinct
data dimension would test, e.g., Q 71 nūn-letter-frequency (graphemic axis,
distinct from morphological axis) — that is filed as a separate H-NEW-N test.

## 7. Honest disclosure

Q 71 hits_in = 3 looks small in absolute terms — much smaller than Q 11 Hūd
(hits_in = 5) or Q 12 Yūsuf (hits_in = 25). The enrichment ratio (25.62×) is
driven by the SHORT n_in (226 tokens) — Q 71 is a dense short surah where
3 occurrences in 226 tokens stands out far above corpus baseline. This is
NOT a paradox; H-NEW-86's framework specifically rewards rate-density.

## 8. Cross-references

- [[h-new-86-surah-name-as-key-root|H-NEW-86]] — parent test, Bonferroni-114
  Q 71 entry already passes.
- [[h-new-49-1-prophet-enrichment|H-NEW-49.1]] — Q 71 in the 8-conservative
  prophet-named list (non-muq cell with Q 47).
- 06-novel-findings.md Q071-F-01 — result.
