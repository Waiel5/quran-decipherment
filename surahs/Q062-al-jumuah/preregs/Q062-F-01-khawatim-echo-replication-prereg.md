---
surah: 62
test_id: Q062-F-01
title: Khawātim al-Ḥashr Q 62:1 echo replication — H-NEW-95 verification
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 4
bonferroni_family: Q062-specialist
alpha_bon: 0.0125
parent_finding: H-NEW-95 Khawātim al-Ḥashr extension
---

# Q062-F-01 — Pre-registration: Khawātim-echo replication on Q 62:1

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** Under the broader 14-name Khawātim inventory (all divine names appearing in Q 59:22-24), Q 62:1 contains **exactly 4 echo names** (al-Malik, al-Quddūs, al-ʿAzīz, al-Ḥakīm), independently replicating H-NEW-95's upward revision of H-NEW-63 (which read 3 names under broader-but-not-exhaustive inventory).

**H1b (one-tailed, locked direction):** Under the strict 9-name exclusive Khawātim inventory (the 8 corpus-exclusive names + al-Khāliq under substring rule, per H-NEW-59), Q 62:1 contains **exactly 1 echo name** (al-Quddūs).

**H1c (composite-quotation reading):** Q 62:1 carries the literal substring `الملك القدوس` from Q 59:23 AND the literal substring `العزيز الحكيم` from Q 59:24. This is a *composite quotation* — Q 62:1 lifts the two-word closing pair of BOTH source verses, not a single-source paraphrase.

**H0:** Any of (H1a) Q 62:1 ≠ 4 broader names; (H1b) Q 62:1 ≠ 1 strict name; (H1c) either composite phrase missing.

**Direction:** Q 62:1 = corpus-distinguished Khawātim-echo verse, dual-source composite (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-surah-1; SHA-256 verified at run-time).
- **Inventory**:
  - **Strict 9-name** (per H-NEW-59 / H-NEW-95 specification): {al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir, al-Khāliq, al-Bāriʾ, al-Muṣawwir} — the 8 corpus-exclusive names of Q 59:22-24, extended to 9 with al-Khāliq under substring rule.
  - **Broader 14-name** (per H-NEW-63 / H-NEW-95 robustness arm): the strict 9 PLUS {al-Raḥmān, al-Raḥīm, al-Malik, al-ʿAzīz, al-Ḥakīm} — i.e. ALL divine names appearing in Q 59:22-24.
- **Match rule**: substring search of definite-singular ال + name as a single grapheme string. No proclitic-prefix tolerance beyond substring.

## 3. Test statistic

- N_strict_q62_1 = count of strict-9 names in Q 62:1.
- N_broader_q62_1 = count of broader-14 names in Q 62:1.
- composite_q62_1 = (`الملك القدوس` ∈ Q 62:1) AND (`العزيز الحكيم` ∈ Q 62:1).

## 4. Why no permutation null on this cell

This is a deterministic look-up replication of a published finding (H-NEW-95) with a specific numeric claim. The permutation-null inferential cells live in H-NEW-95's parent test (Cell C bipartite-graph perm + Cell D top-5 concentration perm + Cell E reverse 99-name window perm). This pre-reg's role is REPLICATION VERIFICATION at the literal name-count layer, not re-derivation of a new null. The single-test α = 0.05 cap applies; no Bonferroni cost is incurred for this descriptive cell.

## 5. Success / Failure

- **CONFIRMED**: H1a + H1b + H1c all hold.
- **PARTIAL**: 1 or 2 of the three hold.
- **NULL**: 0 of the three hold; H-NEW-95 numeric claim fails replication.

## 6. Honest limits known a priori

- The strict-vs-broader inventory choice is load-bearing; both arms are reported.
- This is a CONFIRMATORY replication of an already-published finding, NOT a novel test. Rule-tuple sensitivity (mashriqī vs maghribī, hafs vs warsh) is not in scope; the test is locked at the no-tashkeel Hafs default.
- al-Salām is excluded from the strict-inventory match for Q 62:1 because it is absent from Q 62:1 — this is a pre-test prediction, not a post-hoc move.

## 7. Falsification

If Q 62:1's broader-14 count is ≠ 4, then H-NEW-95's upward revision (3 → 4) is **wrong** at the operational definition used; the parent finding's published numeric claim becomes a candidate for amendment. Either the source-text rules-tuple has shifted between the two runs or the count derivation has an error.

## 8. Garden-of-forking-paths log

This pre-reg is a deterministic numeric look-up; there is no choice of estimator, null, or feature-space. The single forking-path was the inventory choice (strict-9 vs broader-14), which is locked at running BOTH and reporting both.

## 9. Replication

- Script: `surahs/Q062-al-jumuah/scripts/Q062_F_all_tests.py` function `q062_f_01`.
- Output: `surahs/Q062-al-jumuah/csv/Q062-F-01.json`.
- Source SHA-256 captured into the JSON at run-time.

## 10. Cross-references

- Parent: H-NEW-95 Khawātim al-Ḥashr extension (`findings/phase-b-hypotheses/h-new-95-khawatim-extension.md`).
- Predecessor: H-NEW-63 Khawātim-echo extended (`findings/phase-b-hypotheses/h-new-63-khawatim-echo-extended.md`).
- MASTER-LEDGER §2 anchor cluster.
- HANDOFF/01-WHAT-WE-KNOW.md "Anchor cluster: Khawātim al-Ḥashr".
