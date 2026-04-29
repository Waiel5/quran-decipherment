---
finding_id: h-new-278
run: 1
date: 2026-04-18
specialist: codex
seed: 20260418
---

# H-NEW-278 run 1 journal

## Timeline

1. Received scoped task to own only five files for `H-NEW-278` on `OQ-19`.
2. Read parent context from `HANDOFF/05-OPEN-QUESTIONS.md` (`OQ-19`) and `HANDOFF/03-NEXT-MOVES.md` (`NM-36`), plus parent code around `scripts/h_new_131_q108_supernode.py` and `scripts/h_new_131_1_alpha_sweep.py`.
3. Confirmed that `NM-36` and `H-NEW-131.1` are **not** the same correction family:
   - `NM-36`: literal `count / N_i` before ordinary Dirichlet smoothing
   - `H-NEW-131.1`: per-surah `alpha_i` scaling
4. Chose the narrowest honest implementation: baseline replication plus one literal `NM-36` rerun plus a deterministic label-permutation control.
5. Drafted pre-reg with two scored cells:
   - Cell A = top-3 replication check
   - Cell B = Q 108 vs Q 7 degree check
6. Wrote `scripts/h_new_278_length_normalized_mst.py`.
7. Ran a quick dry check before finalizing the write-up; observed an immediate harsh collapse (`Q108=1`, `Q7=15`). Kept the design unchanged because this matched the literal `NM-36` transform and the prereg already locked that path.
8. Executed the final script run.
9. Final results:
   - Baseline replication matched exactly: top-3 = `(Q108:24, Q7:10, Q112:8)`.
   - Literal length-normalized rerun: top-3 = `(Q7:15, Q2:9, Q17:9)`.
   - Q 108 degree = `1`; Q 7 degree = `15`; Q 112 degree = `1`.
   - Cell A FAIL: only overlap with baseline top-3 is `Q7`; Q108 is not top-3.
   - Cell B FAIL: `1` is not greater than `15`.
   - MW-5 label permutation PASS: degree multiset unchanged; Q108's label-specific degree changed `1 -> 3`.
10. Wrote findings note and this journal.

## Observations / notes

- The result is **much harsher** than H-NEW-131.1. That is the main scientific point of the run. If someone casually says "length-normalization still leaves Q 108 as a hub," they are only talking about the per-surah-`alpha_i` family, not the literal `NM-36` family.

- Q 108's collapse to a leaf is not numerically mysterious. Under the literal transform, Q 108 brings only `4/7` of a unit of empirical mass into the top-500 feature space before meeting a flat prior mass of `250`. The prior dominates everyone, and the short-surah mass advantage is gone.

- Q 7 taking over as the top hub at degree 15 fits the parent H-NEW-131 intuition: once the shortest-surah smoothing effect is removed aggressively, a broad-content long Meccan surah becomes the natural center.

- Q 112 also collapses from degree `8 -> 1`. So the literal transform is not merely "anti-Q108"; it broadly demotes very short terminal surahs.

## Deviations from pre-reg

- None. The dry check happened after the design was already locked and did not cause any threshold or rule changes.

## Files touched

- Created: `findings/phase-b-hypotheses/h-new-278-length-normalized-mst-prereg.md`
- Created: `scripts/h_new_278_length_normalized_mst.py`
- Created: `findings/phase-b-hypotheses/csv/h-new-278.json`
- Created: `findings/phase-b-hypotheses/h-new-278-length-normalized-mst.md`
- Created: `journal/h-new-278-run-1.md`

## Next

- Report the landed verdict for OQ-19 with the exact Q108 and Q7 degree results.
- Explicitly distinguish this from H-NEW-131.1 so the project record does not collapse two different normalization families into one claim.
