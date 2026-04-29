# Journal — H-NEW-139.1 run 1

**Date**: 2026-04-17
**Specialist**: specialist-a
**Task**: #35 — audit-037 adversarial flag on H-NEW-139 uniform null
**Seed**: 20260417 + 2 offset

## Sequence

1. Claimed task #35 per ID-order iteration.
2. Read H-NEW-139 parent findings file. Verified observed 21/29 match count by reproducing data pipeline (verse-final letter extraction, top-3 per surah).
3. Confirmed fāṣila-distribution is massively skewed: ن=50%, ا=15%, م=11%, ر=7%.
4. Wrote pre-reg before running null. Locked weighted-reservoir sampling + global fāṣila-frequency reference.
5. Executed 10K perms with weighted-reservoir draws per surah per perm.

## Result

audit-037 predicted z=+3..+4, still PASS. Actual: z = −2.43, direction REVERSED. Observed 21/29 (72.4%) is BELOW the weighted-null mean of 24.76 (85.4%).

## Interpretation

The uniform 28-letter null overstated the effect by ~8 standard deviations. Muq openings don't match rhymes more than you'd expect from drawing letters at random PROPORTIONAL TO HOW OFTEN EACH LETTER APPEARS AS A FĀṢILA.

## Action taken

Findings file explicitly RETRACTS H-NEW-139's PASS-DIRECTED to NULL-MODEL-ARTIFACT. Listed action items for integrator (ledger update) and synthesizer (cross-finding-015 classical-validation list update).

## Honest flag

This retraction EXEMPLIFIES the value of adversarial auditing. audit-037's flag caught a null-model error that would have propagated into cross-finding-015 ("al-Suyūṭī's rhyme-prefiguration validated"). Without the adversarial catch, the classical-validation ledger would have contained a false positive.

This also VALIDATES the project discipline: the retraction is published with equal prominence to the original; the mechanism (wrong null reference) is explained; H-NEW-139.2 alternative-design is queued.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-139-1-prereg.md`
- Script: `scripts/h_new_139_1_freq_weighted_null.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-139-1.json`
- Findings: `findings/phase-b-hypotheses/h-new-139-1-freq-weighted.md`
- Journal: this file

## DMs

- Will DM team-lead: retraction summary.
- Will DM auditor-037: flag confirmed, even stronger than they predicted.
- Will DM synthesizer: cross-finding-015 update needed.
- Will DM integrator: MASTER-LEDGER update needed.

## Next task

Will claim next ID-order pending: #36 H-NEW-144 cyclic-TSP (if specialist-a relevant) or #37.
