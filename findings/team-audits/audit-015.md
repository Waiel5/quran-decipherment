---
audit_id: audit-015
target_finding: team-discovery-014 (H-NEW-1-v2 rhyme-residual robustness battery)
auditor: skeptical-auditor
date: 2026-04-12
verdict: METHODOLOGICAL ERROR IN AUDIT-001 PROTOCOL; RETEST REQUIRED BEFORE DOWNGRADE
parent_finding: team-discovery-001 H-NEW-1, audit-001
cc: integrator
---

# Audit-015 — H-NEW-1-v2 rhyme-residual battery: the null is broken, not the finding

## Verdict: METHODOLOGICAL ERROR IN AUDIT-001 — retest required before downgrade

Computational-tester correctly executed the audit-001 protocol and correctly flagged that the null appears to be over-correcting. On inspection of the script, **the null is not over-correcting — it is outright broken** at the "retrain Markov on shuffled corpus" step. The H-NEW-1 finding should NOT be downgraded on the basis of team-discovery-014; a corrected retest is required.

This is my error: audit-001 requested a "terminal-shuffle with Markov retrain" protocol without specifying the training-corpus invariance required to make it a valid null. I correct that specification here.

## The methodological error, explained

Original H-NEW-1 claim: **the Markov model (trained on verse-interior text) assigns higher surprise to rhyme-break terminals than to rhyme-conforming terminals** — evidence that the rhyme structure is not predictable from local character transitions.

The right null: holding the trained model fixed, shuffle the *assignment* of which terminal is "break" vs "conforming" (i.e., shuffle the rhyme-set membership or the terminal character at each verse-end position). Measure whether the observed gap exceeds what you'd see under random assignment of break-vs-conforming labels.

The script's null (lines 123–155): shuffles the terminals across verses, **then retrains the Markov model on the shuffled corpus** (line 138: `permuted_verses.append({'text': v['text'][:-1] + t})`, then inside `surprise_gap` at line 100–104, the Markov model is rebuilt on the permuted verses).

This is a different and incoherent test. Under shuffling:
- Observed terminals are decoupled from verse context → Markov model trained on this has no terminal-prediction signal.
- Both "break" and "conforming" verse-ends are now unpredictable under the retrained model.
- Expected null gap: large positive value (the retrained model assigns high surprise to *everything* at verse-end), not zero.
- Observed gap (trained on real data, fixed): smaller, because the real model has genuine terminal-prediction capacity.
- Therefore **observed gap < null mean gap → z negative**, mechanically.

The script's baseline finding — Jāhilī poetry at z=-2.81 under the same null — confirms the pathology. Jāhilī poetry has extremely strong rhyme (qaṣīda monorhyme); a null model that returns z=-2.81 for it is wrong on a corpus with a known positive rhyme signal. This is a positive-control failure.

## Why the two positive cells are not a rescue

`all_order3_classical_rawi` (z=+5.53) and `medinan_order3_classical_rawi` (z=+8.78) are cells where the broad classical-rawī set (10 letters, covering ~77% of all verse-ends) is the "conforming" set. Under this set partition, the "break" class is only ~16% of verse-ends, dominated by alif and a few rarer terminals. Small-N in the break class + broad conforming class shifts the gap-under-null distribution in a way that happens to let a real effect survive the broken null. But these cells are not interpretable as "the signal survives at classical-rawī + order-3" — they are interpretable as "the broken null happens to mis-correct in the other direction under this partition."

Do not downgrade, do not upgrade — the two positive cells should be treated as equally uninterpretable as the 25 negative cells.

## What the correct audit-001 test should be

**Null v2 (the one I should have specified):** hold the Markov model fixed (trained once on the real corpus). At each verse-end, randomly permute whether the terminal character is labeled "break" or "conforming," preserving the observed marginal rate (e.g., if 16% of real terminals are break, 16% of permuted labels are break). Recompute the gap between mean surprise of "break-labeled" and "conforming-labeled" terminals. Repeat 10,000 times.

This null tests "could the observed gap be produced by random assignment of break-vs-conforming labels?" — which is the right question for H-NEW-1's claim.

**Alternative null v3 (stronger):** hold the model fixed, shuffle the actual terminal *characters* across verses (preserving marginal character distribution). Recompute gap. This tests "does the specific pairing of (context, terminal) in the real data produce a bigger gap than random pairings?"

Either v2 or v3 is a valid audit-001 protocol. What the script implemented (retrain on shuffled) is neither.

## Blockers for downgrade

**B1.** Re-run the battery with null v2 OR v3 (model fixed, not retrained). Until that is done, H-NEW-1 retains its original CONFIRMED status.

**B2.** Confirm on the baseline Jāhilī poetry that the corrected null returns a *positive* z (since qaṣīda monorhyme is a known-positive rhyme signal). If Jāhilī z > 0 under v2/v3, the null is valid and the Quran result is interpretable. If Jāhilī z ≤ 0, something else is wrong.

**B3.** The 6 audit-001 items (rhyme-set sensitivity, Markov order sweep, Meccan/Medinan split, matched poetry baseline, alif-vs-nun split, bimodality) remain the right battery. Re-run them all under v2/v3.

## Non-blocking notes

- Hartigan dip simplification (lines 158–182) substitutes a skewness/kurtosis bimodality coefficient for the real dip statistic. That's a weaker test but not broken. Re-run with a proper dip statistic (e.g., `scipy.stats.diptest` if available) if possible; otherwise flag as limitation.
- `n_perm=200` is tight. v2/v3 should use ≥ 10,000 perms (the script at line 196 already documents this as a compute-budget choice).
- Bonferroni k=24 across 27 cells + baseline is correctly conservative.
- `SET_CURRENT = set('ناردم')` in the script differs from the original H-NEW-1 rhyme set — verify this matches the original finding's set before any comparative claim.

## What I got wrong in audit-001 and what I'd write now

Audit-001 critique #6 (the Markov-retrain issue) was phrased imprecisely. What I intended was "the Markov model shouldn't be privileged with training on exactly the structure being tested" — which is concern about the model being *too good*, not a prescription to retrain on shuffled data. The correct remedy is either (a) train Markov on a separate corpus (e.g., Bukhari prose) to remove the self-training advantage, or (b) use a character-language-model baseline that is both independent and strong. Retraining on shuffled data is the wrong remedy.

Revised audit-001 protocol (for this retest and future Markov-based surprise tests):
- Fix the trained Markov model.
- Permute labels OR permute the terminal-character positions (v2 / v3).
- Do NOT retrain on the permuted corpus.
- Cross-check with Markov trained on a matched-Arabic prose corpus to rule out self-training advantage.

## Meta-pattern notes

This is a **methodological correction, not a finding update**. H-NEW-1 status remains unchanged — still CONFIRMED at z=+6.1 under the original null — until the corrected v2/v3 battery is run.

This also highlights a broader principle I should have flagged earlier: **when a null is designed, it must first pass a positive-control test** (returns positive z on a corpus where the signal is known to exist). Jāhilī poetry is the right positive control for rhyme tests. Audit-001 should have required the positive control up front. I will apply this to future audits.

**M-5 unaffected.** H-NEW-1 is a phonotactic finding, not a classical-doctrine operationalization.

## Action for computational-tester

1. Do NOT mark H-NEW-1 as downgraded.
2. Re-run the 6-item battery with null v2 (fix Markov, permute labels) and null v3 (fix Markov, permute terminal characters).
3. Require Jāhilī-poetry positive-control pass (z > 0) before interpreting Quranic results.
4. 10,000 perms per cell.
5. Report both v2 and v3 results to me and integrator.

## Action for integrator

Hold H-NEW-1 status at original CONFIRMED pending v2/v3 retest. Do not apply team-discovery-014 to the ledger as a downgrade. Log this audit as a correction of audit-001 protocol specification.
