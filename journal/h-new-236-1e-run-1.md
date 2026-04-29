# Journal — H-NEW-236.1e run 1

**Date**: 2026-04-18  
**Command**: `python3 scripts/h_new_236_1e_soft_terminal_penalties.py`

## Purpose

Test whether rhyme / liturgical terminal structure works better as a
**soft preference** than as a hard adjacency law on top of the
H-NEW-236.1a top-50 scaffold.

Locked lambda grid:

- `0.05`
- `0.10`
- `0.20`

## Result

- Positive control `lambda=0` passed
- `lambda=0.05` = `SOFT-NULL`
- `lambda=0.10` = `SOFT-PARSIMONY-CONFLICT`
- `lambda=0.20` = `SOFT-PARSIMONY-CONFLICT`
- No primary passes
- No strict 4/4 passes

Notable nuance:

- `lambda=0.05` is the near-miss
- it closed `59.64%` of the terminal gap
- it kept `L_path` and `L_tail` inside
- but `L_mufassal_short` was still just outside at `z = +2.78`

## Key pattern

- weak lambda keeps `L_path` and `L_tail` inside but fails to close the
  local `mufassal-short` block
- medium / strong lambda close the local block but push `L_path` and
  `L_tail_91_114` outside low

So the soft version reproduces the same tradeoff as the hard covariate
cells rather than solving it.

## Interpretation

This does not look like a broad tuning problem. It looks like the soft
rhyme/liturgical covariates are missing part of the true structure.

That fits the new H-NEW-236.1d clue that the decisive `95 -> 100`
tranche is mostly outside both soft families.

If a genuine soft-only sweet spot exists at all, it is probably in a
very narrow untested band between `0.05` and `0.10` (roughly
`0.07-0.08`). That is a post-hoc interpolation clue, not a landed
result.

## Deliverables

- `scripts/h_new_236_1e_soft_terminal_penalties.py`
- `findings/phase-b-hypotheses/h-new-236-1e-soft-terminal-penalties-prereg.md`
- `findings/phase-b-hypotheses/h-new-236-1e-soft-terminal-penalties.md`
- `findings/phase-b-hypotheses/csv/h-new-236-1e.json`
- `journal/h-new-236-1e-run-1.md`
