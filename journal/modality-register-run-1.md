# Journal — H-NEW-2640, modality × register (run 1)

**Date:** 2026-08-07 · **Author:** Waiel Al-Shujaa · **Brief:** frontier-map F-10
**Outcome:** NULL on all four registered inferences.

## Order of operations

1. **Pre-flight.** The quran-investigation skill, `INVESTIGATION-PROTOCOL.md`,
   frontier-map F-10, `cross-finding-028-formal-…md`, `h-new-2530-register-grammar.md`, and
   `h-new-2540-form-v-valency.md` (§7.2 published contamination, §8.1 self-reported
   run-immutability breach) as the rigor template.
2. **Counts re-verified from disk before anything else.** Two label errors found in the
   frontier map — `POS:EMPH` and `POS:FUT` name feature strings that do not exist, though
   their totals are right (see finding §7). Substring-vs-atom exhibit built: `POS:PRO`
   returns 3,633 by substring, 332 by atom.
3. **Instrument built and calibrated corpus-wide, with no register split in sight.** The
   §3.2 jussive governor rule was designed and its nine-class output frozen
   (1,418 = 351+330+220+189+110+78+67+45+28) *before* the pre-registration was written, and
   those literals were written into the pre-registration as locked values.
4. **H-NEW-2530 six-feature classifier reproduced exactly** (LOO 0.76923, confusion matrix
   cell-for-cell, legal recall 8/20) before adding anything. This is the MW-6.2 gate.
5. **Pre-registration locked**, SHA-256
   `0b300fdb19c351b1692dc06b7163480bdbed642702c02dbf1bf7e9272065de89`, embedded and
   runtime-verified. Four directions locked with written justifications.
6. **Run.** 57 s, 10,000 perms × 2 nulls × 2 seeds × 3 rules-tuples.
7. **Post-hoc diagnostics**, three iterations, each clearly labelled non-registered and
   MW-7-capped.

## Decision points

- **Register labels not re-derived.** `h-new-2530.json` holds no per-surah labels, only the
  pointer `"h-new-2500.json genre_proxy.surah_genre (reused verbatim)"`. Followed that exact
  pointer and gated it at runtime on 2530's own recorded marginals (31/20/40/23) *plus* exact
  reproduction of its published classifier. That is "verbatim from 2530" in the only sense
  the file supports.
- **Conditionals excluded by construction.** H-NEW-2250 owns *idhā*; H-NEW-2630 owns
  *in*/*law*. The four conditional jussive classes were computed only to be stripped out.
  This turned out to matter more than expected — see below.
- **T2 exists because QAC is inconsistent.** Prohibitive *lā* is tagged `POS:PRO` in 330
  jussives and `POS:NEG` in 110 (e.g. Q 2:102:34 `laA takofuro`, plainly prohibitive, tagged
  NEG). Rather than pick, both readings were pre-registered. T2 changes nothing.

## Garden-of-forking-paths log

- **No fork taken on the primary.** The estimator (unweighted mean of per-surah densities),
  the residualisation, the two nulls, the three tuples and all four directions were locked
  before the first register-split computation and were not revisited.
- **Forks taken post-hoc, all disclosed and all reported regardless of outcome.** P1 (raw
  vs residualised features), P2 (length collinearity), P3 (face validity), P4 (pooled
  token-weighted rates), P5 (reliability). P4 is the one that matters: it shows the deontic
  half of the hypothesis alive under a pooled estimator (p_desc = 0.0077, locked direction
  intact) while the epistemic half fails on direction under *both* estimators. **Not
  claimed.** Registered statistic returned p = 0.979; MW-7 caps the post-hoc at α = 0.05
  with no confirmatory standing. Logged as grounds for a *new* pre-registration, with this
  file cited as the origin of the estimator idea.

## Wrong diagnosis reached first

My first reading of the null blamed the length residualisation for eating a real effect —
plausible, since verse length is itself a register signature (H-NEW-770). **P2 refuted it:**
the length covariates absorb only R² = 0.036 (D) and 0.061 (E). The real constraint is the
estimator's sensitivity to small surahs (20/91 under 50 tokens; Q 108 scores 200/1,000 off
two imperatives in ten words). Recorded because the wrong diagnosis came first.

## The confound, corrected by measurement

The brief warned that raw `MOOD:JUS` "measures negation." Measured: *lam*-negation is
**register-flat** (pooled spread 1.61, p_desc = 0.251) — it dilutes, it does not distort.
The component that would actually have made a raw-jussive test misleading is the
**conditional** jussive (521/1,418 = 36.7%), which is the strongest register separator in
the whole mood system (pooled legal 11.04 vs eschatological 1.69, p_desc = 0.0007) and
belongs to H-NEW-2630. A raw-`MOOD:JUS` test would have reported borrowed conditional
signal as a modality finding. The split was necessary for a different reason than stated.

## Self-reported process errors

1. **Pre-registration §9 gives no precedence between "p ≥ α" and "direction reversed",** so
   the verdict code labels I1/I2 `REVERSED-PRECOMMIT-VIOLATION` when F ≈ 0.03 and there is
   no effect to reverse. Over-labelling. The finding states the substantively correct
   reading (NULL) and keeps the flaw on the record rather than editing the locked file.
2. **Seven run directories instead of four.** The post-hoc script imports the primary script
   (deliberately, so every SHA is re-verified rather than re-implemented); I did not
   anticipate that the import also fires the primary's run-directory write. Three spare
   primary runs resulted. **All seven retained** — §8 has no exception for spares, and
   `h-new-2540` §8.1 exists because that judgment was made wrongly before. The accident
   paid for itself: four independent executions produced **byte-identical** `result.json`,
   SHA-256 `1c13fe9a…`.

## Not done, deliberately

`MASTER-FINDINGS-LEDGER.md`, `KNOWLEDGE-GRAPH.md` and
`cross-finding-028-formal-…md` were **not** edited. Seven other tests are running against
those same shared files in this wave and nothing is committed; an uncommitted edit would
collide. Handoff items are in finding §10.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2640-modality-register.md`
- scripts: `findings/phase-b-hypotheses/scripts/h-new-2640.py`, `…/h-new-2640-posthoc.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2640.json`, `…/h-new-2640-posthoc.json`
- finding: `findings/phase-b-hypotheses/h-new-2640-modality-register.md`
- runs: `findings/phase-b-hypotheses/runs/h-new-2640/` (7 directories, all retained)
