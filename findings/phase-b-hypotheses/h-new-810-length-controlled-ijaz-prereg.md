---
id: H-NEW-810
title: "Pre-reg — Length-controlled iʿjāz partial correlation: does the content-rhyme anti-twinning of H-NEW-730 survive partialling out verse-length?"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-730 (r(content × rhyme) = -0.864 window-by-window) AND H-NEW-770 (verse-length explains ~76% of content-cohesion variance, r ≈ 0.872 letters_per_verse vs d_content; r ≈ 0.873 words_per_verse vs d_content). Critical robustness check: is iʿjāz a length artefact?
discipline: PRE-REG-STANDARD-04
seed: 20260448
---

# [[h-new-810-length-controlled-ijaz|H-NEW-810]] — Length-Controlled iʿjāz Partial Correlation: Pre-Registration

## 1. Hypothesis

The [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] anti-twinning effect — Pearson r(d_content, d_rhyme) = -0.864 across the K=15 100-window mushaf scan — is NOT entirely an artefact of the verse-length compression-tail ([[h-new-770-verse-length-compression-tail|H-NEW-770]]). When verse-length (letters/verse or words/verse) is partialled out, the iʿjāz signature must remain substantially negative (partial r ≤ -0.5) for the [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] reading to hold.

This is a PURE robustness check. Direction of evidence is bidirectional: failure SHRINKS [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]; success STRENGTHENS it.

## 2. Locked metrics (no recomputation)

All three input series are taken VERBATIM from the parent JSON outputs (already on disk, hashed prereg):

- d_content[100] — `findings/phase-b-hypotheses/csv/h-new-730.json` → `d_content`.
- d_rhyme[100]   — `findings/phase-b-hypotheses/csv/h-new-730.json` → `d_rhyme`.
- d_phoneme[100] — `findings/phase-b-hypotheses/csv/h-new-730.json` → `d_phoneme`.
- letters_per_verse[100] — `findings/phase-b-hypotheses/csv/h-new-770.json` → `metric_letters_per_verse.window_obs`.
- words_per_verse[100]   — `findings/phase-b-hypotheses/csv/h-new-770.json` → `metric_words_per_verse.window_obs`.

All five vectors must have length 100 and identical canonical mushaf ordering (s ∈ {1..100} = window-start surah). Length and ordering are checked at run-start; abort if either fails.

## 3. Three locked partial-correlation tests

Using the standard partial-correlation formula:

```
r(X, Y | Z) = (r_xy − r_xz · r_yz) / sqrt((1 − r_xz²) · (1 − r_yz²))
```

with Pearson r as the base correlation, three tests are run:

1. **T1 — r(d_content, d_rhyme | letters_per_verse)** — does iʿjāz survive removing letter-length effect?
2. **T2 — r(d_content, d_rhyme | words_per_verse)**   — same with word-length effect.
3. **T3 — r(d_content, d_phoneme | letters_per_verse)** — same robustness check on the content × phoneme axis.

## 4. Permutation null (locked)

For each test, generate a null distribution of partial correlations under H₀ (no genuine partial association beyond what length explains). Procedure (10000 perms, seed 20260448):

- Shuffle the rhyme (or phoneme) vector ONLY, keeping content and length aligned with the canonical mushaf order.
- Recompute the partial correlation on (content, shuffled-rhyme | length).
- p_perm = fraction of nulls with partial r ≤ observed (one-sided, since the pre-committed direction is negative).

This shuffle holds the content × length and length × length geometries fixed; only the content-rhyme association is broken. (Identical structure to the [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] perm null, with length added as the conditioning vector.)

Fisher z-transform is reported alongside permutation p for completeness, but the perm-p is gating.

## 5. Pre-committed direction

- T1, T2, T3: partial r EXPECTED to be negative.
- Direction = lower-tail (one-sided): observed partial r ≤ null partial r.

## 6. Bonferroni structure

- 3 partial-r tests → α_bon = 0.05 / 3 = 0.01667.

## 7. Pass / partial / fail thresholds (LOCKED)

For each of T1, T2, T3:

- **PASS-INDEPENDENT** (iʿjāz survives length-control): partial r ≤ -0.5 AND perm p ≤ 0.01667.
- **PARTIAL-DEPENDENT** (mixed): partial r ∈ (-0.5, -0.3].
- **PASS-LENGTH-DRIVEN** (iʿjāz dissolves when length is held fixed): partial r > -0.3.

Aggregate verdict on the iʿjāz axis = the reading of T1 and T2 jointly (content × rhyme, two length proxies). T3 (content × phoneme) is reported alongside and treated symmetrically.

## 8. Pre-committed reasoning rules (BEFORE run)

- If T1 AND T2 both PASS-INDEPENDENT → iʿjāz is structurally present BEYOND length; [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] STRENGTHENS; [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] is robust to the [[h-new-770-verse-length-compression-tail|H-NEW-770]] confound.
- If T1 OR T2 lands in PARTIAL-DEPENDENT → iʿjāz is partially length-mediated; [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] SOFTENS but does not fall.
- If T1 AND T2 both PASS-LENGTH-DRIVEN → iʿjāz is largely a verse-length confound; [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] WEAKENS; [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] must be re-narrated as a length-tail phenomenon. THIS RESULT WILL BE REPORTED HONESTLY.
- T3 mirrors the same logic for the content × phoneme axis.

NULL-equally-prominent rule: at every report stage the null reading (length-driven) is presented with the same prominence as the alternative.

## 9. What would FALSIFY the iʿjāz independence

- Any test with partial r > -0.3 and perm p > 0.01667 falsifies independence on that axis.
- T1 and T2 disagreeing wildly (one pass-independent, one length-driven) flags metric-choice fragility — would trigger MW-7 follow-up.

## 10. Files

- Prereg: `findings/phase-b-hypotheses/h-new-810-length-controlled-ijaz-prereg.md` (this file).
- Script: `scripts/h_new_810_length_controlled_ijaz.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-810.json`
- Findings: `findings/phase-b-hypotheses/h-new-810-length-controlled-ijaz.md`
- Journal: `journal/h-new-810-run-1.md`

## 11. Methodology rules

- MW-1 instrument-prior: metrics are inherited verbatim from parents; no new measurement.
- MW-3 alternative-models: two length proxies (letters/words) cross-checked; phoneme axis as a third axis.
- MW-7 not applicable — fully pre-registered.
- PRE-REG-STANDARD-04: hypothesis, null, direction, Bonferroni-3, pass/partial/fail criteria, honesty-rule on length-driven outcome — all LOCKED BEFORE run.

## 12. Disciplines

- ONE-text discipline: single canonical Hafs Quran corpus. No edition framing.
- HONEST-on-failure: if iʿjāz is length-driven, this prereg commits to reporting that finding cleanly, not softening it.
- Bonferroni-tightening permitted post-hoc; loosening forbidden.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
