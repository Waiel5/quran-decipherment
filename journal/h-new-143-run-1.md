# Journal — H-NEW-143 + H-NEW-143.1 run 1

**Date**: 2026-04-17
**Specialist**: specialist-a
**Task**: #30 (H-NEW-143) + queued H-NEW-143.1
**Seed**: none (deterministic; no simulation)

## H-NEW-143 — Surface-word bridge NULL

Task description noted "NULL — 99/113 transitions have zero shared tokens" with FR_TOP15 mean bridge=0.13 vs 0.27, MW p=0.48. I reproduced the qualitative NULL but got 92/113 zero-overlap and different mean values (using cosine). Metric choice differs but NULL robust: 12/12 tests (3 feature × 4 metrics) p > 0.6, all effect signs NEGATIVE (top-15 has LOWER surface bridge).

Conclusion: surface-word is wrong instrument for classical munāsabāt. Queued H-NEW-143.1 for root-level replication.

## H-NEW-143.1 — Root-level bridge test

Pre-reg filed BEFORE extracting root-level bridges. Executed per spec.

### Results

- Primary union-top-15 vs other: mean 0.040 vs 0.033, z=+0.15, p_upper=0.44. **NULL**.
- Per-feature:
  - Root top-15: 0.064 vs 0.031, z=+0.96, p_upper=0.17. Direction correct, underpowered.
  - Char-4-gram top-15: 0.061 vs 0.031, z=+0.94, p_upper=0.17. Same pattern.
  - Verse-length top-15: 0.041 vs 0.034, z=−0.37, p_upper=0.65. Negative direction.
- Universal hinges:
  - Q 14→15: cos=0 (rank 7/113), no shared roots.
  - Q 49→50: cos=0 (rank 36/113), no shared roots.
  - **Q 56→57: cos=0.408 (RANK 1 of 113), shared roots {sbH, smw}**. Classical tasbīḥ-echo CONFIRMED at root level.
- Pre-committed ≥2/3 universal above P50 → FAIL (only 1/3).

### Single strong finding

**Q 56→57 is the Quran's rank-1 root-bridge across all 113 boundaries.** This is the mushaf's strongest root-bridge, exactly at the Ḥadīd→al-Wāqiʿah boundary where classical al-Biqāʿī reads the "sabbiḥ → sabbaḥa" imperative-execution echo.

### H-NEW-142 claim update

H-NEW-142 identified 3 rhetorical bridges. Root-level test confirms 1 of 3 (Q 56→57). The other 2 (Q 14→15 and Q 49→50) have semantic/conceptual bridges but zero shared roots. "4th classical validation" claim is NARROWED from "3-of-3 universal hinges" to "exemplar-level validation at Q 56→57".

## Artifacts written

- H-NEW-143:
  - `scripts/h_new_143_surface_word_bridge.py`
  - `findings/phase-b-hypotheses/csv/h-new-143.json`
  - `findings/phase-b-hypotheses/h-new-143-surface-word-bridge-null.md`
- H-NEW-143.1:
  - `findings/phase-b-hypotheses/h-new-143-1-prereg.md`
  - `scripts/h_new_143_1_root_bridge.py`
  - `findings/phase-b-hypotheses/csv/h-new-143-1.json`
  - `findings/phase-b-hypotheses/h-new-143-1-root-bridge.md`
- Journal: this file

## Team communication

- Will DM team-lead: both NULL/MIXED; H-NEW-142 claim narrowed; Q 56→57 rank-1 is striking.
- Will DM synthesizer: cross-finding-015 classical-scholarship validation wording should be refined.
