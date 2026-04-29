---
finding_id: h-new-129
title: "Formal joint Late-Meccan peak across the 5 Pattern-B axes"
specialist: specialist-a
date_prereg: 2026-04-18
seed: 20260418
bonferroni_k: 1
bonferroni_family: h-new-129-joint-late-meccan-peak
alpha_bon: 0.01
alpha_raw: 0.01
direction_primary: "Exact 5-of-5 Pattern-B phase maxima at Late Meccan under the locked 4-phase H-NEW-125 schema; one-sided upper-tail on the joint-hit probability."
rules_tuple: "(114 surahs, upstream H-NEW-125 per-surah axis values, 4 Nöldeke phases with fixed counts 48/21/21/24, exact unique-max joint-hit indicator, 10K phase-label permutations)"
parent_finding: h-new-125
related_finding: cross-finding-012
verdict_ceiling: "PASS-DIRECTED only; the 5-axis bundle was noticed in H-NEW-125 before this prereg, so this is a formal locked follow-up rather than a blind discovery."
---

# [[h-new-129-joint-late-meccan-peak|H-NEW-129]] — Formal joint Late-Meccan peak across the 5 Pattern-B axes

## Motivation

[[h-new-125-chronology-content|H-NEW-125]] showed that 5 axes individually follow a Pattern-B
trajectory at the original 4-phase Nöldeke resolution:

- `qul_density`
- `book_reference_density`
- `eschatological_density`
- `muq_cardinality`
- `loanword_density`

Each of those axes had its highest 4-phase mean in **Late Meccan**.
[[h-new-129-joint-late-meccan-peak|H-NEW-129]] formalizes that observation as a single locked joint test:
is the exact **5-of-5 Late-Meccan peak** unlikely under a phase-label
permutation null?

This is deliberately narrower than `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]`, which asked a
sub-bin concordance question at 8-bin resolution and found the broader
apparatus centered at B7. [[h-new-129-joint-late-meccan-peak|H-NEW-129]] stays at the original [[h-new-125-chronology-content|H-NEW-125]]
resolution and tests only the coarse 4-phase joint peak.

## Hypothesis

**Primary (H1).** Under the locked 4-phase Nöldeke partition used by
[[h-new-125-chronology-content|H-NEW-125]], all 5 Pattern-B axes have their maximum phase mean at
**Late Meccan**. The exact joint event occurs at one-sided permutation
`p < 0.01`.

Pre-registered direction: **Late Meccan only**. A joint peak in any
other phase, or a split peak pattern, is NULL for the primary claim.

## Pre-registered Bonferroni family

There is **one inferential family with one inferential cell**:

- **Cell A (primary)**: exact 5-of-5 Late-Meccan joint peak

Therefore:

- `bonferroni_family = [[h-new-129-joint-late-meccan-peak|h-new-129]]-joint-late-meccan-peak`
- `k = 1`
- `alpha_bon = 0.01`

The `0.01` threshold is intentionally conservative and follows the
handoff seed for NM-31. Descriptive disclosures and MW-5 do **not**
consume Bonferroni slots.

## Data lock

- Upstream source only:
  `findings/phase-b-hypotheses/csv/h-new-125.json`
- No raw-text re-extraction is permitted for this test.
- Axis set is locked to the 5 [[h-new-125-chronology-content|H-NEW-125]] Pattern-B axes listed above.
- Phase labels are locked to the [[h-new-125-chronology-content|H-NEW-125]] schema:
  `Early Meccan`, `Middle Meccan`, `Late Meccan`, `Medinan`
- Phase counts are inherited from upstream:
  `48 / 21 / 21 / 24`

## Statistic

For each axis:

1. Compute the mean axis value within each of the 4 locked phases.
2. Identify the phase with the maximum mean.
3. Treat a tied maximum as **NOT** satisfying the primary claim
   unless `Late Meccan` is the unique maximum. This is conservative.

Define:

- `n_late_meccan_peaks` = number of the 5 axes whose unique maximum is
  `Late Meccan`
- `joint_hit` = `1` iff `n_late_meccan_peaks = 5`, else `0`

The primary inferential target is the probability of `joint_hit = 1`
under the permutation null.

## Permutation null

- `N = 10,000` permutations
- seed `20260418`
- Permute the 114 phase labels across surahs while preserving the
  observed phase counts.
- Recompute all 4 phase means for all 5 axes on each permutation.
- Recompute `joint_hit` on each permutation.

One-sided permutation p-value:

`p = (1 + # {perm_joint_hit = 1}) / (1 + 10000)`

This empirical null is the decision statistic. A naive equal-phase
independence heuristic such as `1 / 4^5` is reported only, if at all,
as intuition and not as the inferential basis.

## MW-5 positive control

Before declaring any primary verdict, the exact same machinery must
fire on a known positive-control bundle from [[h-new-125-chronology-content|H-NEW-125]]:

- `allah_density`
- `legal_term_density`
- `personal_pronoun_density`
- `mean_verse_length`
- `divine_name_density`

Expected control direction: all 5 have unique 4-phase maxima at
**Medinan**.

MW-5 passes only if:

1. observed `n_medinan_peaks = 5`, and
2. the phase-label permutation p-value for the exact 5-of-5 Medinan
   hit is `< 0.01`

If MW-5 fails, the verdict is **NULL-BROKEN** regardless of the
primary result.

## Acceptance windows

- **PASS-DIRECTED**:
  primary observed `joint_hit = 1` and `p_perm < 0.01`, with MW-5 PASS
- **NULL**:
  MW-5 PASS, but primary `joint_hit = 0` or `p_perm >= 0.01`
- **NULL-BROKEN**:
  MW-5 FAIL

Verdict ceiling is **PASS-DIRECTED**, not CONFIRMED, because the
5-axis bundle was already noticed in [[h-new-125-chronology-content|H-NEW-125]] before this exact joint
test was pre-registered.

## Garden-of-forking-paths lock

- No relaxed criterion such as `4/5` or `>= 4/5` is permitted inside
  [[h-new-129-joint-late-meccan-peak|H-NEW-129]]. If desired, that is a new prereg.
- No alternative chronology is permitted inside [[h-new-129-joint-late-meccan-peak|H-NEW-129]].
- No sub-bin refinement is permitted inside [[h-new-129-joint-late-meccan-peak|H-NEW-129]].
- No dropping of `muq_cardinality` is permitted inside [[h-new-129-joint-late-meccan-peak|H-NEW-129]].
  That sensitivity belongs elsewhere.

## Honest limits pre-committed

1. This is a **coarse 4-phase** test. It cannot adjudicate the B6/B7
   staircase already highlighted by `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]`.
2. The axis bundle is **not blind-selected**. [[h-new-125-chronology-content|H-NEW-125]] already
   identified these 5 axes as Pattern-B, so this test is a formal
   lock-down of an existing pattern, not an independent discovery.
3. A joint chronological peak does **not** imply surah-level latent
   covariation within Late Meccan. [[h-new-141-pattern-b-within-late-meccan|H-NEW-141]] already found the 5 axes
   pairwise null within Late Meccan.

## Post-hoc-noticed disclosure

This prereg is written on 2026-04-18 after [[h-new-125-chronology-content|H-NEW-125]] and
`[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]` were already known. I have not yet run the exact
4-phase phase-label-permutation test for [[h-new-129-joint-late-meccan-peak|H-NEW-129]] at the time of
writing this prereg.

## Deliverables

1. `findings/phase-b-hypotheses/h-new-129-joint-late-meccan-peak-prereg.md`
2. `scripts/h_new_129_joint_late_meccan_peak.py`
3. `findings/phase-b-hypotheses/csv/h-new-129.json`
4. `findings/phase-b-hypotheses/h-new-129-joint-late-meccan-peak.md`
5. `journal/h-new-129-run-1.md`
