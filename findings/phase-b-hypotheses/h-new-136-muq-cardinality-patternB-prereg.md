---
finding_id: h-new-136
title: "Muqaṭṭāʿat cardinality × Pattern-B composite Spearman correlation"
specialist: theorist (pre-reg); executed inline by team-lead 2026-04-17; reproduced by specialist-a 2026-04-17
date_prereg: 2026-04-17
seed: 20260418
bonferroni_k: 1
bonferroni_family: h-new-136-muq-cardinality-patternB
alpha_bon: 0.05
alpha_raw: 0.05
direction_primary: "Spearman ρ(muq_cardinality, PatternB_composite) > 0; one-sided"
length_control: "per-surah density normalization (each axis is per-100-verses)"
rules_tuple: "(29 muqaṭṭāʿat-opened surahs, 4 Pattern-B axes z-normed over 114, Spearman ρ, 10K perm null)"
perms: 10000
verdict_ceiling: "PASS-DIRECTED (single-test k=1; full CONFIRMED requires phase-controlled H-NEW-136.2 follow-up per audit-036)"
parent_model: "scratch/theorist-2026-04-17-unified-equation.md §2 P1★ (originally §7 Prediction 5)"
source_original_prereg: "scratch/theorist-2026-04-17-unified-equation.md §7 (verbatim original theorist pre-reg preserved there)"
status_as_of_2026_04_17: "EXECUTED + REPRODUCED; PASS-DIRECTED; re-labeled per audit-036 as compact-statistic redundant confirmation of P1+P5 joint mechanism, NOT standalone independent predictive win"
---

# [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] — Muqaṭṭāʿat cardinality × Pattern-B composite (standard-location pre-reg extract)

## Provenance note

This is the **standard-location extract** of the [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] pre-reg
for project-discipline symmetry. The **original pre-reg** is embedded
in the theorist's unified-equation proposal at
`scratch/theorist-2026-04-17-unified-equation.md` §7 and is preserved
verbatim there. Both versions are byte-equivalent in their locked
pre-reg commitments (claim, direction, α, k, seed, N, permutation
procedure, pass criterion, MW-5 positive control).

Specialist-a flagged the scratch-location convention gap 2026-04-17
during reproduction; this file closes that gap.

## Claim

Under theorist P1 (scripture-announcement Late-Meccan climax) + P5
(muqaṭṭāʿat mark book-introduction), **among the 29 muqaṭṭāʿat-opened
surahs**, muqaṭṭāʿat cardinality (1..5) should POSITIVELY correlate
with a Pattern-B composite score defined as the z-normed mean of:
- qul_density ([[h-new-125-chronology-content|H-NEW-125]] axis 5)
- book_reference_density (axis 9)
- eschatological_density (axis 8)
- loanword_density (axis 15)

The muq_cardinality axis itself ([[h-new-125-chronology-content|H-NEW-125]] axis 3) is excluded from
the Pattern-B composite to avoid circularity between predictor and
response.

## Hypothesis

**Primary (H1)**. Spearman ρ(muq_cardinality, Pattern-B composite)
over the 29 muqaṭṭāʿat-opened surahs is > 0 at one-sided permutation
p < α = 0.05.

**Pre-registered direction**: POSITIVE (one-sided).
**Pre-registered α**: 0.05 (single test, k=1).

## Pre-registered Bonferroni family

**k = 1**. This is a SINGLE pre-registered test. α_bon = 0.05 (no
correction needed). Prediction 1–4 from theorist proposal §5 are
separate pre-regs if executed (would form their own family).

## MW-5 positive control

Before executing the primary test, re-verify that [[h-new-125-chronology-content|H-NEW-125]] Pattern-B
axes (5, 9, 8, 15) each give ρ > +0.5 with Nöldeke rank across the
full 114 surahs. If any axis fails MW-5, the Pattern-B composite is
compromised and the primary test is invalid.

Expected MW-5 values per [[h-new-125-chronology-content|H-NEW-125]]:
- qul_density: ρ = +0.5421 vs Nöldeke rank
- book_reference_density: ρ = +0.5744
- eschatological_density: ρ = +0.7096
- loanword_density: ρ = +0.8329

## Specification

### Data

- Per-surah axis values: `findings/phase-b-hypotheses/csv/h-new-125.json`
  (pre-computed per-surah values for all 15 axes across all 114 surahs)
- 29 muqaṭṭāʿat-opened surahs (standard list): Q 2, 3, 7, 10, 11, 12,
  13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42,
  43, 44, 45, 46, 50, 68
- muq_cardinality per surah: count of letters in the opener (1..5)

### Composite construction

For each of 114 surahs and each of the 4 Pattern-B axes:
1. z-normalize across all 114 surahs (mean=0, std=1 over the full corpus)
2. Pattern-B composite per surah = mean of the 4 z-scores

Then filter to the 29 muqaṭṭāʿat-opened surahs for the primary test.

### Test statistic

Spearman rank correlation coefficient ρ between muq_cardinality and
Pattern-B composite over n=29 surahs.

### Permutation null

10,000 permutations of the Pattern-B composite labels over the 29
surahs (muq_cardinality values kept in original order). For each
permutation, compute Spearman ρ. One-sided p = (#{perm_ρ ≥ observed}
+ 1) / (10,001).

### Seed

20260418.

### Pass criteria (pre-registered)

- **PASS-DIRECTED**: ρ > +0.3 AND permutation p_one_sided < 0.05
- **STRONG-PASS**: ρ > +0.5 AND permutation p_one_sided < 0.01

### Expected outcome (theorist prediction)

ρ in range +0.4 to +0.6 at p < 0.01.

### Fail interpretation

If ρ < 0 (reversal) or ρ not significantly different from 0, P1+P5
joint prediction at the surah-level axis is FALSIFIED. The 2
principles would need to be re-examined — possibly P5 applies
independently of P1's chronological-climax structure, meaning the
muqaṭṭāʿat marker is chronology-independent even though its overall
occurrence is chronology-stratified.

## Executed result (2026-04-17; PASS-DIRECTED with audit-036 caveat)

| Quantity | Team-lead inline | Specialist-a reproduction |
|---|---:|---:|
| N | 29 | 29 |
| Spearman ρ | **+0.3706** | **+0.3706** (exact match) |
| One-sided permutation p | 0.0243 | 0.0239 (independent RNG stream) |
| Direction | POSITIVE ✓ | POSITIVE ✓ |
| Verdict | PASS-DIRECTED | PASS-DIRECTED (confirmed) |

**Cardinality breakdown (both runs match)**:

| card | N | Mean Pattern-B | Surahs |
|:-:|:-:|:-:|---|
| 1 | 3 | −0.289 | Q 38 ص, Q 50 ق, Q 68 ن |
| 2 | 9 | +0.480 | حم cluster + يس, طه, طس |
| 3 | 13 | +0.606 | الم cluster + الر cluster + طسم |
| 4 | 2 | **+1.350** | Q 7 المص, Q 13 المر |
| 5 | 2 | +0.411 | Q 19 كهيعص, Q 42 حمعسق |

## audit-036 latent-dependence caveat (2026-04-17)

auditor flag: the 29 muqaṭṭāʿat-opened surahs are Late-Meccan-
concentrated by construction (25/29 Meccan, Late-Meccan mode). The
+0.37 ρ cannot discriminate:
- **Phase-level** covariation (muq-opened → Late-Meccan → Pattern-B
  elevated) from
- **Surah-level** covariation (within-phase, muq-cardinality encodes
  Pattern-B density beyond chronology)

**Status re-labeling per audit-036**: [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] is a
**compact-statistic redundant confirmation of P1+P5 joint mechanism**,
already independently evidenced by cross-finding-008 + [[h-new-125-chronology-content|H-NEW-125]].
It is NOT a standalone independent predictive win.

**Recommended follow-up (H-NEW-136.2)**: restrict the test to
Late-Meccan-only muqaṭṭāʿat-opened surahs (n ≈ 9-14) to isolate
surah-level from phase-level covariation. A positive ρ within
Late-Meccan-only would be genuine independent evidence of the
surah-level mechanism.

## MW-7 3-check reproducibility status (2026-04-17)

- **Check 1 (pre-reg authored)**: theorist, 2026-04-17 in
  `scratch/theorist-2026-04-17-unified-equation.md` §7
- **Check 2 (primary execution)**: team-lead inline, 2026-04-17;
  findings file authored with primary results
- **Check 3 (independent reproduction)**: specialist-a, 2026-04-17;
  EXACT ρ match, p within Monte-Carlo noise; artifacts written
  (`scripts/h_new_136_muq_cardinality_patternB.py`,
  `findings/phase-b-hypotheses/csv/h-new-136.json`,
  `journal/h-new-136-run-1.md`)

MW-7 3-check COMPLETE.

## Relationship to other findings

- Parent: theorist unified-equation §7 Prediction 5
- Triggered P1+P5 merge → P1★ (see theorist §2 updates)
- Parent data: [[h-new-125-chronology-content|H-NEW-125]] (per-surah Pattern-B axis values)
- Supports (compact-statistic): cross-finding-008 (muq → book-intro)
- Subject to: audit-036 latent-dependence caveat
- Follow-up proposed: H-NEW-136.2 (Late-Meccan-only restriction)
- Related: H-NEW-136.1 (card=5 sub-class NULL; separately executed
  and found null; not confounded by phase)

## Files

- Pre-reg (this file, standard-location extract):
  `findings/phase-b-hypotheses/h-new-136-muq-cardinality-patternB-prereg.md`
- Pre-reg (original theorist location, verbatim):
  `scratch/theorist-2026-04-17-unified-equation.md` §7
- Findings file (team-lead-authored):
  `findings/phase-b-hypotheses/h-new-136-muq-cardinality-patternB-composite.md`
- Reproduction script (specialist-a):
  `scripts/h_new_136_muq_cardinality_patternB.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-136.json`
- Journal: `journal/h-new-136-run-1.md`
