---
finding_id: h-new-151
run: 1
date: 2026-04-17
specialist: specialist-B
seed: 20260417
---

# H-NEW-151 run 1 journal

## Timeline

1. Pre-reg drafted for char-4-gram replication of H-NEW-146 Cell C single-letter-muq sub-cluster.
2. Direction locked negative (replication).
3. Executed. Result:
   - Within (Q 38, 50, 68) mean = 0.934
   - Between mean = 0.981
   - Delta = −0.046, z = −1.06, p = 0.15
   - Direction consistent with root finding but magnitude ~1/3
   - VERDICT: NULL

## Observations

- **Direction preserved across feature spaces** (root: delta=-0.142; char-4-gram: delta=-0.046). The single-letter-muq sub-cluster is a real weak signal.
- **Magnitude 3× smaller** under char-4-gram. The parent H-NEW-146 Cell C p=0.031 was already near-miss; this char-4-gram replication is just null.
- **Q 38-Q 50 is closest singleton pair** (0.889), then Q 50-Q 68 (0.945), then Q 38-Q 68 (0.968). ص-ق pair is the tightest; ص-ن the weakest.
- **Phonological note**: ص, ق, ن are all coronal/uvular consonants. Phonological similarity may be a better axis for sub-clustering than content similarity.

## Deliverables

- `findings/phase-b-hypotheses/h-new-151-single-letter-muq-char4gram-prereg.md`
- `scripts/h_new_151_single_letter_muq_char4gram.py`
- `findings/phase-b-hypotheses/csv/h-new-151.json`
- `findings/phase-b-hypotheses/h-new-151-single-letter-muq-char4gram.md`
- This journal

## Deviations from pre-reg

None.

## Next

DM team-lead with the 3-task run summary; claim next task if available.
