# Journal — H-NEW-236.1d run 1

**Date**: 2026-04-18  
**Command**: `python3 scripts/h_new_236_1d_minimal_k_bracket.py`

## Purpose

Tighten the hard-hinge parsimony bracket after H-NEW-236.1b showed:

- `K=50` is not sufficient for strict 4/4 closure
- `K=100` is sufficient

Locked grid before execution:

- `K = {73, 80, 85, 90, 95, 100}`

The first internal `mufassal-short` edge enters at rank `73`, so the
search was centered on that threshold.

## Result

- Positive control passed: fresh-seed `K=50` reproduced the inherited
  non-closing state.
- Strict pass set: `{100}`
- Strict fail set: `{73, 80, 85, 90, 95}`
- New tested bracket: **`(95, 100]`**

Most important pattern:

- `K=85` and `K=90` repair the local `mufassal-short` block and keep
  `L_path` inside, but still fail on `L_tail_91_114`
- `K=95` still fails
- the five added edges from `95 -> 100` are all late-tail edges:
  `92-93`, `99-100`, `100-101`, `101-102`, `109-110`

## Interpretation

This run strengthens the case that the terminal residual is not just
"more hinges." The last closing information appears to be a **specific
late-tail scaffold**.

That makes the next experiment clear:

- start from the over-correcting H-NEW-236.1c base
- add only the late-tail repair tranche
- test whether the tail and global path can be repaired with fewer
  constraints than the full top-100 scaffold

## Deliverables

- `scripts/h_new_236_1d_minimal_k_bracket.py`
- `findings/phase-b-hypotheses/h-new-236-1d-minimal-k-bracket-prereg.md`
- `findings/phase-b-hypotheses/h-new-236-1d-minimal-k-bracket.md`
- `findings/phase-b-hypotheses/csv/h-new-236-1d.json`
- `journal/h-new-236-1d-run-1.md`
