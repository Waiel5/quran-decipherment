# H-NEW-129 Run 1 — Journal

**Date**: 2026-04-18
**Agent**: specialist-a
**Seed**: 20260418
**N_PERM**: 10,000
**Bonferroni**: k=1, α_bon=0.01
**Family**: h-new-129-joint-late-meccan-peak

## Task

Land H-NEW-129: formal joint Late-Meccan peak test across the 5
Pattern-B axes from H-NEW-125 (`qul_density`, `book_reference_density`,
`eschatological_density`, `muq_cardinality`, `loanword_density`).
Read only minimal handoff/open-question/related-finding context, write
the prereg before execution, include MW-5, and report honest limits.

## Minimal context actually used

1. `handoff/03-NEXT-MOVES.md` — NM-31 seed for H-NEW-129.
2. `handoff/04-DISCIPLINE.md` — MW-5 rule.
3. `handoff/05-OPEN-QUESTIONS.md` — H-NEW-125 Pattern-B summary.
4. `findings/phase-b-hypotheses/csv/h-new-125.json` — locked upstream
   per-surah values and phase schema.
5. `scripts/h_new_125_chronology_content.py` — upstream extraction
   conventions.
6. `scripts/cross_finding_012_joint_peak.py` — style and MW-5 handling.
7. `findings/phase-b-hypotheses/h-new-141-pattern-b-within-late-meccan.md`
   — interpretive guardrail that co-peak does not imply within-phase
   latent covariation.

No broader repo sweep. No raw-text re-extraction. No non-owned files
modified.

## Pre-reg workflow

1. Wrote
   `findings/phase-b-hypotheses/h-new-129-joint-late-meccan-peak-prereg.md`
   **before** running any H-NEW-129 permutations.
2. Locked a single inferential cell:
   exact `5/5` unique maxima at `Late Meccan` under the 4-phase
   H-NEW-125 schema.
3. Locked Bonferroni family explicitly:
   `k = 1`, `alpha_bon = 0.01`,
   `bonferroni_family = h-new-129-joint-late-meccan-peak`.
4. Locked MW-5 before execution:
   known 5-axis Pattern-A Medinan bundle
   (`allah_density`, `legal_term_density`,
   `personal_pronoun_density`, `mean_verse_length`,
   `divine_name_density`) must also fire under the same machinery.
5. Chose a conservative unique-max rule:
   ties do not count as hits unless the target phase is the unique max.

## Implementation

Wrote `scripts/h_new_129_joint_late_meccan_peak.py` with these rules:

- load only `findings/phase-b-hypotheses/csv/h-new-125.json`
- use locked phase order
  `Early Meccan / Middle Meccan / Late Meccan / Medinan`
- preserve upstream phase counts `48 / 21 / 21 / 24`
- compute phase means per axis
- compute exact 5-of-5 target-phase hit
- run 10,000 phase-label permutations with seed `20260418`
- write JSON to `findings/phase-b-hypotheses/csv/h-new-129.json`

## Execution result

Observed primary bundle:

- `qul_density` peak = Late Meccan
- `book_reference_density` peak = Late Meccan
- `eschatological_density` peak = Late Meccan
- `muq_cardinality` peak = Late Meccan
- `loanword_density` peak = Late Meccan
- observed `5/5` Late-Meccan peaks

Observed MW-5 bundle:

- `allah_density` peak = Medinan
- `legal_term_density` peak = Medinan
- `personal_pronoun_density` peak = Medinan
- `mean_verse_length` peak = Medinan
- `divine_name_density` peak = Medinan
- observed `5/5` Medinan peaks

Permutation results:

- **Primary**: 225 of 10,000 permutations also hit exact `5/5`
  Late-Meccan peaks
  `=> p = (225 + 1) / 10001 = 0.0226`
- **MW-5**: 598 of 10,000 permutations also hit exact `5/5` Medinan
  peaks
  `=> p = (598 + 1) / 10001 = 0.0599`

Primary does not pass `0.01`. MW-5 also does not pass `0.01`.

## Honest decision

Per MW-5 discipline, this lands **NULL-BROKEN**.

Important distinction:

- the descriptive `5/5` Late-Meccan co-peak is still there
- but the exact-hit permutation instrument is too weak to promote it

I did **not** add any post-hoc rescue statistic, relaxed `4/5` rule,
or muq-dropped sensitivity analysis under H-NEW-129. Those would be
new preregs.

## Diagnosis

The failure mode is the same kind of one seen elsewhere when a binary
peak-location rule is too crude:

1. The statistic keeps only peak identity, not peak margin.
2. Several axes have Late-Meccan means close to Medinan means, so many
   shuffled labelings preserve the same target peak.
3. Because the known Medinan bundle also fails at MW-5, the instrument
   is not discriminative enough for inferential use.

This means H-NEW-129 does **not** negate H-NEW-125 or
`cross-finding-012`; it only shows that this particular 4-phase exact
5-of-5 test is not a valid formal anchor.

## Files written

1. `findings/phase-b-hypotheses/h-new-129-joint-late-meccan-peak-prereg.md`
2. `scripts/h_new_129_joint_late_meccan_peak.py`
3. `findings/phase-b-hypotheses/csv/h-new-129.json`
4. `findings/phase-b-hypotheses/h-new-129-joint-late-meccan-peak.md`
5. `journal/h-new-129-run-1.md`

## What I did NOT do

- I did not modify or revert any non-owned files.
- I did not rerun with a different seed or alternate chronology.
- I did not replace the preregistered MW-5 after seeing it fail.
- I did not rescue the result with a richer statistic under the same ID.
