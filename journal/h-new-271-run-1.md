---
finding_id: h-new-271
run: 1
date: 2026-04-18 to 2026-04-19
specialist: codex
seed: 20260419
---

# H-NEW-271 run 1 journal

## Timeline

1. Read the prereg and confirmed the intended inferential object was an
   arm-wise RF `maxT` permutation over 10 fixed candidates per arm.
2. Audited the older script and found it was using per-winner fallback
   permutation checks rather than the preregistered arm-wise `maxT`.
3. Rewrote `scripts/h_new_271_muq_minimal_phon_family.py` to:
   - keep RF LOOCV as the locked classifier family
   - evaluate all 10 candidates in each arm
   - precompute the 1000 shuffled label vectors
   - run arm-wise `maxT` permutation tests
   - use `n_jobs=1` inside the RF and outer batched parallelism outside
4. Initial sandbox run was too slow and process-pool constrained, so the
   exact rerun was relaunched outside the sandbox to allow the loky
   worker backend to execute the same locked design honestly.
5. The exact run completed and wrote the JSON artifact.
6. Observed the decisive outputs:
   - Arm A winner: `mean_manner` alone
   - Arm A top-1 = `0.6551724137931034`
   - Arm A maxT `p = 0.000999000999000999`
   - Arm B winners:
     `letter_count + mean_makhraj`,
     `letter_count + mean_manner`
   - Arm B maxT `p = 0.000999000999000999`
   - overall verdict = `SINGLE-PHON-FEATURE-SUFFICIENT`
7. Verified that the findings file had been wrapped but the journal file
   was missing, then wrote this journal.

## Notes

- The parsimony result is stronger than expected: the phon-only arm
  passes without `letter_count`.
- `mean_manner` is the only single-axis Arm A ceiling-hitter.
- Both controls stayed alive:
  `full15` reproduced the ceiling and MW-5 `cheat_surah_id` stayed above
  the preregistered threshold.
- The unresolved downstream question is no longer cluster sufficiency.
  It is whether this 1-D axis retains any meaningful singleton-layer
  structure or whether the full 15-D space is only still needed there.
