# Journal — H-NEW-134-FORMAL run 1

**Date**: 2026-04-18  
**Seed**: 20260418  
**N_PERM**: 100000

## Scope

Formal follow-up to the older prophet-named-surah idea, but with a
strictly surface-form family:

- `vocative_share`
- `sequencer_share`

Primary set locked to the 6 explicit prophet-name titles:

- Q 10, Q 11, Q 12, Q 14, Q 47, Q 71

Sensitivity set:

- primary 6 plus Q 19 and Q 31

No prophet-name lexicon was used in the main family.

## Result shape

The strict-6 target set looked positive on both primary axes:

- `vocative_share` passed at `p = 0.01945`
- `sequencer_share` passed at `p = 9.9999e-06`

The expanded 8-surah sensitivity set also looked positive on both axes.

But the planted MW-5 control failed:

- planted `vocative_share` `p = 0.16114`
- planted `sequencer_share` `p = 0.94625`

That forces the overall verdict to **INSTRUMENT-BROKEN**.

## Honest adjudication

This is exactly the kind of run where it would be easy to overclaim if
MW-5 were ignored. The target-set p-values by themselves look good. But
the instrument did not pass its own planted stress test, so the result
cannot be promoted.

Likely issue:

- the slot-matched null is too tight / too distorted, especially in the
  `meccan|100+|muq` slot where only three non-target controls remain
  after removing the target set

## Files

- `scripts/h_new_134_formal_prophet_named_signature.py`
- `findings/phase-b-hypotheses/h-new-134-formal-prophet-named-signature-prereg.md`
- `findings/phase-b-hypotheses/csv/h-new-134-formal.json`
- `findings/phase-b-hypotheses/h-new-134-formal-prophet-named-signature.md`
- `journal/h-new-134-formal-run-1.md`
