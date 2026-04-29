# H-NEW-58 — Surah-Pair Twinning — Run 1 Journal

**Date**: 2026-04-15
**Specialist**: h-new-58-specialist
**Seed**: 20260416

## Sequence

1. **Reviewed environment**: confirmed loader.py, divine-names CSV
   format, QAC morphology v0.4 file, prior h_new_56 script style.
2. **Wrote pre-reg** (`h-new-58-surah-pair-twinning-prereg.md`) BEFORE
   running any data-touching code on the 4 classical pairs:
   - Locked 4 pairs: Q2+Q3, Q8+Q9, Q113+Q114, Q73+Q74.
   - Locked 5 axes: root-jaccard, verse-len, rhyme-entropy, divine-
     density, hapax-density.
   - Locked Bonferroni-20 (4 × 5), α_bon = 0.0025.
   - Locked PASS criterion: ≥ 2 / 4 pairs sig on ≥ 2 / 5 axes at α_bon.
   - Locked MW-5: P_muawwidhatan must show ≥ 2 axes p < 0.001 else
     INSTRUMENT_FAIL.
   - Locked null: 10 K random adjacent (i, i+1) surah pairs, exclude the
     test pair from its own null.
3. **Wrote script** (`scripts/h_new_58_surah_pair_twinning.py`):
   - Loads no-tashkeel JSON, QAC stem-roots per surah, divine-names CSV.
   - Computes per-surah scalars then pair-similarity in [0, 1] for all
     5 axes via the pre-committed formulas.
   - Builds adjacent-pair null per pair.
   - Computes upper-tail p, Bonferroni decision, PASS criterion, MW-5.
4. **First run**: MW-5 failed (0 / 5 axes for muʿawwidhatān at p < 0.001).
   Inspected per-axis observed values manually:
   - Verse length: muʿawwidhatān sim 0.86 — many short late-mushaf
     surahs are similar to each other; not unusual.
   - Rhyme entropy: Q113 H = 1.92, Q114 H = 0.0 (Q114 is monorhyme on
     `اس`). Scalar similarity 1 - 1.92 / 1.92 = 0.000.
   - Divine density: both 0.0 (rabb is not a counted divine name in the
     existing CSV) — sim = 1.0 by `1 − 0/eps`, but ~10% of nulls also
     have both surahs at 0 divine names, so p = 0.10.
   - Hapax density: Q113 has hapax roots, Q114 does not — sim = 0.000.
   - Root-jaccard: 4/18 ≈ 0.22 — also unremarkable (very small surahs,
     mostly stop-word / pronoun / dem-name overlap).
5. **Per pre-reg rule** ("if MW-5 fails, the procedure itself is broken
   ... do not declare H-NEW-58 itself as either PASS or NULL"), I did
   NOT change any pre-committed metric. Instead I added a *secondary*
   diagnostic null using any-(i,j) pairs (clearly logged as POST-HOC and
   excluded from PASS/NULL declaration) to characterize the gap between
   the pre-committed metric and the underlying tradition.
6. **Second run** (with secondary diagnostic added): same primary
   results (instrument fail, 0 / 20 sig cells); secondary diagnostic
   shows only P_zahrawan × A1_root_jaccard at p = 0.0006 against any-
   pair null. All other 19 cells unremarkable even against the looser
   any-pair null.

## Garden-of-forking-paths log

Every choice in the pre-reg was locked before any pair-similarity number
was computed. Specifically:
- Adjacent-only null was chosen because all 4 test pairs are adjacent
  (defensible as a matched-control choice), NOT after seeing that this
  null is tight.
- The 5 axes were chosen for tooling availability (root jaccard via
  QAC, verse length via no-tashkeel JSON, rhyme via 2-char suffix,
  divine density via existing CSV, hapax via QAC + corpus count) BEFORE
  any pair similarity was computed.
- Bonferroni k = 20 (full grid) was chosen rather than k = 4 (per-pair
  axis-pooled). This is a TIGHTENING vs k = 4 (so per the
  bonferroni_tightening_vs_loosening rule it self-verifies; no
  ratification needed).
- The MW-5 control was pre-committed, not added after observing the
  failure.

The post-hoc secondary diagnostic (any-pair null) was added between
runs 1 and 2 to *describe* the gap, not to change the verdict. Its
results are explicitly fenced off from the PASS/NULL declaration in
both the JSON and the findings markdown.

## Outputs

- Pre-reg: `findings/phase-b-hypotheses/h-new-58-surah-pair-twinning-prereg.md`
- Script: `scripts/h_new_58_surah_pair_twinning.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-58.json`
- Findings: `findings/phase-b-hypotheses/h-new-58-surah-pair-twinning.md`

## Verdict

**INSTRUMENT_FAIL_NO_DECLARATION** under pre-reg rule.

Substantive reading: classical surah-pair tradition is a functional /
liturgical / thematic pairing claim, not a statistical-shape twinning
claim. Of 5 statistical-shape axes:
- only 1 of 20 cells reaches Bonferroni (and only under the secondary
  *any-pair* null, post-hoc): P_zahrawan × root-jaccard, p ≈ 6 × 10⁻⁴
- 0 of 20 cells reach uncorrected α = 0.05 under the pre-registered
  adjacent-pair null

This is a strong NULL on the pre-registered hypothesis with clean
diagnosis of why (and a clear suggested follow-up: test pairs on
**functional** axes — shared opener prefix, shared liturgical use,
shared narrative protagonist).

## Suggested follow-up: H-NEW-58b

Test 4 classical pairs against null on functional axes:
- F1: longest shared opening string-prefix length (LCS on prefix)
- F2: longest shared closing string-suffix length
- F3: shared incipit lemma (does v1 lemma overlap?)
- F4: liturgical-collection co-membership (ruqya, morning-evening
  adhkār, etc.) — text-independent feature from hadith
- F5: shared narrative protagonist (Mūsā / Ibrāhīm / Maryam / etc.)

P_muawwidhatan should crush F1 (`qul aʿūdhu bi-rabbi al-` is 17 chars
of identical prefix, vs random adjacent-pair median ≈ 0).
