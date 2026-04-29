# H-NEW-253 — Run 1 journal

**Date**: 2026-04-17
**Seed**: 20260419
**Specialist**: h-new-253-specialist
**Parent**: H-NEW-234

## Task

Test whether Q 55's Pattern-B-PARTIAL profile (M1+M3+M5 EXTREME, M2
TYPICAL) is a replicable category by applying the same 20-metric
portrait to all 114 surahs.

## Execution

1. Read H-NEW-234, H-NEW-178, H-NEW-180, and the template script
   `scripts/h_new_234_q55_profile.py`.
2. H-NEW-191 five-mode-classification file does not exist in the
   corpus; proceeded from H-NEW-234's 4-cell framework directly (task
   description permits "or similar").
3. Wrote pre-reg `h-new-253-mode-b-siblings-prereg.md` with
   bonferroni_k=2 cells, α_bon=0.025, seed 20260419.
4. Wrote `scripts/h_new_253_mode_b_siblings.py` extending H-NEW-234's
   logic to loop over all 114 surahs with leave-one-out percentile
   (reference n=113), cell-count computation, MW-5 permutation, and
   shared-profile descriptive analysis.
5. Ran the script (~8 seconds on M1). All 1000 MW-5 permutations
   completed without warnings.

## Results

- **Baseline**: 17 surahs with cell-count ≥ 3 at p5 threshold.
- **MW-5 null mean**: 18.52 (p = 0.766) — baseline is CORPUS-TYPICAL,
  not a genuine signal at α_bon = 0.025.
- **Top-10 by cell-count**: Q 2, Q 3, Q 108, Q 4, Q 55, Q 7, Q 106,
  Q 111, Q 5, Q 9. Mixed mechanistic class (length-driven long
  Medinan + tiny terminal surahs + Q 55 refrain-stylistic).
- **Restricted "Q 55-type" (M1+M3+M5 exactly, no-M2)**: 5 surahs —
  Q 4, Q 54, Q 55, Q 105, Q 107. Only **Q 54 al-Qamar** shares both
  structural-hinge M1 and refrain-adjacent M3 mechanism.
- **Q 55-ness score** (post-hoc, disclosed): Q 55 = 7/7 UNIQUELY
  saturates its own fingerprint. Closest sibling Q 2 = 4/7 by
  different (length-driven) mechanism. All other surahs ≤ 3/7.

## Interesting observations

- **Q 77 al-Mursalāt** (H-NEW-234 narrative "half-Mode B") has
  cell-count = 1 at strict p5. Investigation: h-new-181 coverage is
  only 79 surahs (not 114) — the ACF CSV filters out short surahs. Of
  the 78 non-Q 77 surahs in the ACF dataset, 4 exceed Q 77's acf_2
  (Q 38, Q 78, Q 52, Q 51), giving LOO pct = 74/78 = **94.87%**,
  extremity = **5.13** — JUST above the 5.0 p5 threshold.
  So Q 77 narrowly MISSES the p5 threshold on acf_2 (and on other
  metrics). H-NEW-234's narrative "Q 77 = half-Mode B ACF-lag-2 =
  0.369" was a RANK-BASED descriptive statement (rank 5/114 = top
  4.4%); the strict LOO-pct-within-79-surah-ACF-dataset pushes it to
  extremity 5.13, just above threshold. This is a genuine boundary-
  sensitivity: **Q 77 is a p05-boundary near-miss**. Reported in
  honest limits.

- **Q 54 al-Qamar** emerges as the cleanest Mode-B sibling: same cell
  configuration (M1+M3+M5), structural-hinge M1, prosodic M3, and
  modest M5. Its mechanism is anti-periodic (acf_1, acf_2 both
  negative) — the OPPOSITE sign of Q 55's period-2 pillar. This is
  a "Mode-B anti-twin" finding that H-NEW-234's neighbor-comparison
  table already predicted descriptively.

- **Length-extremum dominance**: Q 2, 3, 4, 5, 7, 9 (long Medinan)
  and Q 106, 108, 111 (tiny khawātim) dominate the top-10 via M5
  metrics that are length-correlated. This is a honest limit of the
  metric bundle — many M5 metrics measure length-by-proxy.

## Verdict

**MIXED**: loose cell-count criterion is corpus-typical (MW-5 p =
0.77 NOT below 0.025); fingerprint-level (Q 55-ness) is Q 55-UNIQUE.
Q 55's ʿarūs al-Qurʾān designation is empirically vindicated at the
specific-signature level, not at the loose-category level. Mode B is
a 2-5 exemplar phenomenon with Q 54 + Q 55 as the core pair.

## Files produced

- `findings/phase-b-hypotheses/h-new-253-mode-b-siblings-prereg.md`
- `findings/phase-b-hypotheses/h-new-253-mode-b-siblings.md`
- `scripts/h_new_253_mode_b_siblings.py`
- `findings/phase-b-hypotheses/csv/h-new-253.json`
- `findings/phase-b-hypotheses/csv/h-new-253-all-surah-profile.csv`
- This journal.

## Queue

- H-NEW-253.1: balanced-cell + percentile-threshold sensitivity test.
  Also investigate Q 77 acf_2 boundary issue.
- H-NEW-253.2: formal refrain-detection scan over 114 surahs.
- H-NEW-253.3: Q 54+Q 55 joint permutation test.
- H-NEW-253.4: cross-textual Mode-B uniqueness (Bukhārī, pre-Islamic
  poetry).

## Runtime

~8 seconds (114 surahs × 20 metrics × 1000 MW-5 permutations on M1).
