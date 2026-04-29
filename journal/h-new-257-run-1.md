---
journal: h-new-257 run-1
date: 2026-04-17
agent: H-NEW-257 specialist (classical-cross-reference lane)
parent: H-NEW-189 / H-NEW-189.1
task: cross-reference 13 Medinan-inclusio surahs vs al-Biqāʿī *Naẓm al-Durar* at surah-specific level
---

# H-NEW-257 — journal run 1

## Intent

Descriptive scholarship-validation task: determine whether al-Biqāʿī's
*Naẓm al-Durar* (22 vols, Dār al-Kutub al-ʿIlmiyyah 1415/1995) SPECIFICALLY
identifies first-last munāsabāt in the 13 empirically-detected
Medinan-inclusio surahs of H-NEW-189 (plus the 2 Meccan exceptions per task
prompt).

This is NOT an inferential test. No α-level claim is made. MW-7 single-test
α=0.05 cap is NOT invoked because the task is descriptive cross-reference
only.

## Method

1. Read `findings/phase-b-hypotheses/h-new-189-medinan-inclusio.md` +
   `findings/phase-b-hypotheses/h-new-189-medinan-inclusio-prereg-backfill.md`
   for the empirically-detected 13 surahs + shared-root inventory.
2. Grep project for al-Biqāʿī references across:
   `findings/`, `analysis/`, `docs/`, `data/literature/`, `scratch/`,
   `MASTER-FINDINGS-LEDGER.md`.
3. Load project-indexed al-Biqāʿī summaries:
   - `findings/classical-cross-references.md`
   - `data/literature/classical-tafsir/razi-biqai-munasabat-rings.md`
   - `findings/classical-sources/fresh-wave-3-classical-anchors.md`
   - `MASTER-FINDINGS-LEDGER.md` (al-Biqāʿī decomposition §row 226-233)
4. Classify each of 13 surahs into categories (A)/(B)/(C)/(D) per task
   rubric; report Category (A) count + strongest surah-specific candidate.

## Garden-of-forking-paths disclosure (pre-run)

- **Threshold choice**: category (A) requires VERIFIED per-surah
  verse-specific citation anchoring. Pre-committed strict reading; did NOT
  weaken threshold after seeing that no such indexing exists.
- **Surah enumeration**: accepted task prompt's list of 11 Medinan + 2 Meccan
  exceptions as the 13-surah set even though H-NEW-189 top-15 table shows
  only 10 Medinan explicitly and the exact identities of the 11th + any
  additional inclusio surahs are not resolved in the findings file. Did NOT
  re-run the H-NEW-189 script to resolve.
- **al-Biqāʿī edition**: project corpus indexes the ʿAbd al-Razzāq Ghālib
  al-Mahdī Dār al-Kutub al-ʿIlmiyyah 22-volume edition as the canonical
  reference (per h-new-189-prereg-backfill §"Classical anchor — al-Biqāʿī
  precision"); did NOT cross-check against the older 8-volume Hyderabad
  edition cited in some secondary literature (both editions cover same
  content; volume numbering differs).
- **Disposition of "implicit-by-method"**: Q 59 al-Ḥashr could be counted
  in (A) under a WEAK reading (al-Biqāʿī's method would produce a first-last
  claim if asked). Pre-committed STRICT reading places Q 59 in (B) pending
  direct text verification. Honest disclosure: under weak reading count(A)
  could be 1/13, not 0/13; under strict reading count(A) is 0/13.

## Execution

- Read H-NEW-189 primary + backfill files: ~380 lines total.
- Grep al-Biqāʿī references: 91 files project-wide.
- Primary indexed references consulted:
  - `findings/classical-cross-references.md` lines 53-68 (Biqāʿī as
    strongest classical observation; macro-ring disconfirmed at z=-4.87)
  - `data/literature/classical-tafsir/razi-biqai-munasabat-rings.md`
    (Biqāʿī d. 885/1480; 8-vol magnum opus; linear vs chiastic method
    contrast; whole-mushaf ring claim)
  - `findings/classical-sources/fresh-wave-3-classical-anchors.md` line
    76 (22-vol edition referenced; forward-order coherence method)
  - `MASTER-FINDINGS-LEDGER.md` §row 226-233 (differential adjudication —
    local-seam PASS Z=+10.06; macro-ring REFUTED Z=-2.51)
  - Ledger §row 521 (Q 2:149-150 flagship *munāsaba*; Q 59:22-23 second
    pair)
  - Ledger §row 535 (Biqāʿī's intra-surah thesis survives —
    opening-compression-predicts-body p=8.9×10⁻¹¹)

## Findings

- Zero of thirteen surahs produce a VERIFIED per-surah first-last citation
  from al-Biqāʿī's primary text under strict reading.
- One (Q 59 al-Ḥashr) promotes to (B) under implicit-by-method reading via
  ledger §row 521 linkage.
- Two (Q 8, Q 9) are indexed in (C) via the Q 8-Q 9 conceptual-joining
  tradition (adjacent-surah rather than intra-surah).
- Remaining ten are (D) DATA-UNAVAILABLE.
- Verdict under task rubric: **< 5/13 in (A) → general-principle-validated
  but surah-specific-predictions-unvalidated**. Consistent with H-NEW-189's
  existing verdict.
- Strongest surah-specific promote-to-(A) candidate: **Q 59 al-Ḥashr**,
  owing to corpus-maximum shared-count (5 roots) + khawātim Ḥashr
  divine-name saturation + flagship-*munāsaba* neighbourhood per ledger
  row 521.

## Honest limits (inherited from finding file)

1. No direct text access to 22-vol *Naẓm al-Durar* in project corpus.
2. Secondary-literature compresses Biqāʿī's method to doctrine level, not
   per-surah.
3. H-NEW-189 top-15 displays only 10 Medinan inclusio-positive surahs
   explicitly; two additional are below cutoff and not resolved here.
4. Category (A) = 0 is corpus-access upper bound, not substantive negative.
5. MW-7 α cap NOT invoked because no inferential framing.

## Outputs

- Finding file: `findings/phase-b-hypotheses/h-new-257-biqai-medinan-inclusio-crossref.md`
- Journal: this file
- MASTER-LEDGER Wave-5 entry: appended

## Time / cost

- Read operations: 5 (h-new-189 primary, backfill, classical-cross-refs,
  razi-biqai-munasabat, fresh-wave-3-classical-anchors)
- Grep operations: 3 (biqai global, specific-surah global, ledger-local)
- Analysis: single-pass classification, no compute.
- Total specialist elapsed: ~20 min estimated.

## Queue

- H-NEW-257.1 (direct-text Q 59 al-Ḥashr PRIMARY verification)
- H-NEW-257.2 (positive control: verify Q 2:149-150 as flagship *munāsaba*)
- H-NEW-257.3 (secondary-literature round: Saleh, Cuypers, Mir)
