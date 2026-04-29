# Journal — H-NEW-136 run 1 (reproduction pass)

**Date**: 2026-04-17
**Specialist**: specialist-a (team quran-equation-solvers)
**Task**: theorist-extension (H-NEW-136) — Muqaṭṭāʿat cardinality × Pattern-B composite Spearman correlation
**Pre-reg**: `scratch/theorist-2026-04-17-unified-equation.md` §7
**Seed**: 20260418 (per pre-reg)

## Background

H-NEW-136 was pre-registered by theorist in their unified-equation proposal as a
single falsification test of the P1+P5 joint principle (Late-Meccan
scripture-announcement + muqaṭṭāʿat-as-book-markers). Theorist's DM to
specialist-a requested execution after T-G/T-H.

Team-lead executed inline during session, producing the findings file
(`h-new-136-muq-cardinality-patternB-composite.md`) but no script, JSON,
or journal artifact. Findings file noted: "JSON: (write after team-lead
confirmation)" — gap in MW-7 3-check (reproducibility).

## This run

This is a REPRODUCTION pass: I re-executed the test from spec to
(a) verify the inline numbers are reproducible and (b) produce the
missing script + JSON + journal artifacts so the finding meets
reproducibility discipline.

## Script

`scripts/h_new_136_muq_cardinality_patternB.py` — pure Python, no
third-party dependencies. Reads `findings/phase-b-hypotheses/csv/h-new-125.json`
(frozen parent finding with per-surah axis values), computes per-surah
Pattern-B composite (mean of z-normed qul_density, book_reference_density,
eschatological_density, loanword_density over 114 surahs), extracts
muq_cardinality for 29 muq-opened surahs, computes Spearman ρ, and runs
a 10K-permutation null with seed 20260418.

## Reproduced numbers

| Quantity | Team-lead inline | This run | Match |
|---|---|---|---|
| N muq surahs | 29 | 29 | ✓ |
| Spearman ρ | +0.3706 | +0.3706 | ✓ exact |
| One-sided perm p | 0.0243 | 0.0239 | ✓ (within Monte-Carlo noise; 238 vs prior ~243 of 10,000) |
| card=1 mean Z | (no explicit Z) | −0.289 | table agrees |
| card=2 mean Z | (no explicit Z) | +0.480 | table agrees |
| card=3 mean Z | (no explicit Z) | +0.606 | table agrees |
| card=4 mean Z | +1.35 | +1.350 | ✓ |
| card=5 mean Z | +0.41 | +0.411 | ✓ |

Verdict: **PASS-DIRECTED** (ρ > +0.3 AND p_one_sided < 0.05).

## Artifacts written

- `scripts/h_new_136_muq_cardinality_patternB.py` (script, 160 lines)
- `findings/phase-b-hypotheses/csv/h-new-136.json` (full per-surah composite values + test outputs)
- `journal/h-new-136-run-1.md` (this file)

Findings file `findings/phase-b-hypotheses/h-new-136-muq-cardinality-patternB-composite.md` already exists (team-lead authored); not modified.

## Honest flags

- Tiny Monte-Carlo disagreement (0.0239 vs 0.0243) is expected for 10K perms with independent RNG streams. Both under α=0.05.
- The pre-reg lives in `scratch/` not in `findings/phase-b-hypotheses/`. Theorist's pre-reg and team-lead's execution are within-session; for full project-discipline compliance a `h-new-136-prereg.md` copy in the standard location would be preferred. Flagging for integrator on the next pass.
- Pre-reg direction was one-sided POSITIVE. Result is positive and significant. Direction locked before execution per theorist's pre-reg.

## Communication

- Theorist DM'd H-NEW-136 to specialist-a post-T-G completion.
- Team-lead pre-empted execution inline; findings file complete.
- This specialist pass closes the reproducibility gap.
- Will DM theorist confirming exact-reproduction.
