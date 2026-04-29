# Journal — H-NEW-132 run 1

**Date**: 2026-04-18
**Specialist**: codex
**Task**: Q7 Al-A'raf vs Q11 Hud prophet-cycle parallelism
**Seed**: 20260418

## Sequence

1. Stopped work on the occupied `h-new-130` lane and redirected to fresh task
   `h-new-132` exactly as requested.
2. Located the prior broad prophet-cycle attempt (`h-new-197`) and the existing
   prophet-pericope resources to avoid inventing a new corpus or freehand
   segmentation.
3. Inspected only the raw Arabic text of Q7:59-93 and Q11:25-95 to freeze the
   shared prophet windows. No cross-window similarity matrix was computed before
   the pre-reg.
4. Wrote the pre-reg around a bounded exact-assignment test:
   - five shared prophet blocks only: Noah, Hud, Salih, Lot, Shuayb
   - PN-stripped QAC root distributions as the primary representation
   - exact `5! = 120` assignment null
   - row-wise nearest-neighbor recovery as secondary
   - PN-only lemma assignment as positive control
5. Implemented `scripts/h_new_132_prophet_cycle_parallelism.py`.
6. Executed the script once deterministically and wrote
   `findings/phase-b-hypotheses/csv/h-new-132.json`.
7. Read the resulting matrix and drafted the finding as `PARTIAL-PASS`.

## Results

### Primary

- Canonical Q7 <-> Q11 assignment is the **unique minimum** among all 120
  bijections.
- `p_primary = 1/120 = 0.00833`
- Observed canonical sum-distance = **3.5928**
- Diagonal mean distance = **0.7186**
- Off-diagonal mean distance = **0.7760**
- Mean gap = **0.0575**

### Secondary

- Row-wise nearest-neighbor recovery = **2/5**
- `p_secondary = 0.2000`
- Only **Salih** and **Lot** map to themselves by local nearest neighbor.
- **Noah, Hud, Shuayb** all collapse toward Q11 **Salih**.

### Positive control

- PN-only exact assignment also gives canonical as unique minimum.
- `p_positive = 1/120 = 0.00833`
- Margin to runner-up = **0.4815**
- Pipeline sanity check passes cleanly.

## Key read

This is not a null. It is also not a strong clean match. The correct statement
is:

**Q7 and Q11 share a recoverable five-block prophet-cycle at the global
assignment level, but not at the stricter row-wise unique-fingerprint level
once prophet names are removed.**

The critical detail is the runner-up: it differs only by swapping **Noah** and
**Hud**, and is worse by just **0.0223**. So the global signal is present but
tight, not overwhelming.

## Honest notes

1. The secondary failure is structurally informative, not random noise.
   Q11 Salih behaves like a centroid-like formulaic block.
2. This follow-up is narrower than H-NEW-197 and therefore more successful, but
   it does NOT rescue the broader claim that prophet retellings share one common
   sequential template.
3. Moses was excluded in advance and stayed excluded. I did not reopen that
   choice after seeing results.

## Files written

- `scripts/h_new_132_prophet_cycle_parallelism.py`
- `findings/phase-b-hypotheses/h-new-132-prophet-cycle-parallelism-prereg.md`
- `findings/phase-b-hypotheses/h-new-132-prophet-cycle-parallelism.md`
- `findings/phase-b-hypotheses/csv/h-new-132.json`
- `journal/h-new-132-run-1.md`
