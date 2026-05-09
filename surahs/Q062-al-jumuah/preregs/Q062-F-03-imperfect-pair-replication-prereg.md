---
surah: 62
test_id: Q062-F-03
title: H-NEW-58c imperfect-pair Q 62 ↔ Q 64 shared-prefix replication
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 4
bonferroni_family: Q062-specialist
alpha_bon: 0.0125
parent_finding: H-NEW-58c musabbiḥāt tense-split structure
---

# Q062-F-03 — Pre-registration: H-NEW-58c imperfect-pair replication

## 1. Hypothesis (locked before observation)

**H1a (descriptive replication):** Q 62:1 and Q 64:1 share a verbatim character-prefix of approximately 37 characters (the published H-NEW-58c value).

**H1b (structural-binary):** Within the 5-surah inner musabbiḥāt cluster {Q 57, 59, 61, 62, 64}, the 6 cross-tense pairs (perfect × imperfect) share **exactly 0 character-prefix**, while all 4 within-tense pairs (3 perfect-pair + 1 imperfect-pair) share **strictly > 0 character-prefix**.

**H1c (sharpness):** The within-tense / cross-tense partition is *binary*, not gradient — the difference between minimum within-tense prefix and maximum cross-tense prefix is large (≥ 20 characters).

**H0 (joint):** H1a fails by ≥ 5 chars OR H1b fails (any cross-tense pair > 0 OR any within-tense pair = 0) OR H1c fails (within-tense min ≤ cross-tense max + 20).

**Direction:** the perfect-vs-imperfect tense binary structure of the musabbiḥāt cluster is sharp and replicates (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json`. SHA-256 verified at run-time.
- **Surahs**: {Q 57 al-Ḥadīd, Q 59 al-Ḥashr, Q 61 al-Ṣaff} (perfect-tense سبح openers); {Q 62 al-Jumuʿah, Q 64 al-Taghābun} (imperfect-tense يسبح openers).
- **Metric**: shared character-prefix (longest common prefix of v.1 of each surah, character-by-character at the no-tashkeel grapheme level).
- **Tense classification**: pre-locked from verb morphology. سبح = perfect (3 surahs); يسبح = imperfect (2 surahs).

## 3. Test statistic

For each of the C(5, 2) = 10 pairs:
- shared_prefix(a, b) = number of leading characters identical in v.1 of surahs a and b.

Reported per pair plus aggregates:
- mean_within_tense (4 pairs): mean of imperfect-pair + 3 perfect-pairs.
- mean_cross_tense (6 pairs): mean of cross-tense pairs.
- min_within_tense, max_cross_tense: for sharpness check.

## 4. Permutation null (deferred)

The H-NEW-58c parent test ran a 10K-perm null on the FULL cluster's prefix-cohesion (P=0.0001). This pre-reg is a deterministic REPLICATION at the per-pair level; no new null is computed. The single-test α = 0.05 cap applies for the replication-class verdict.

## 5. Success / Failure

- **CONFIRMED**: H1a + H1b + H1c all hold.
- **PARTIAL**: H1b holds (binary structure verified) but H1a numeric value drifts by > 5 chars (rule-tuple drift between H-NEW-58c run and this run).
- **NULL**: H1b fails — the binary structure is not present in this rules-tuple.

## 6. Honest limits known a priori

- **Numeric drift expected at single-byte scale**: the "56" prefix-chars reported for Q 59↔Q 61 in H-NEW-58c may differ by ±1-2 chars in this run owing to ZWNJ / non-printing-mark handling in the no-tashkeel pipeline. If observed, the qualitative binary structure remains unaffected and is the load-bearing claim.
- **5-surah cluster is a fixed classical grouping**; this is not a discovery test, it is a replication.
- Single rule-tuple (no-tashkeel default).
- The "37-char" claim is anchored at H-NEW-58c run-1; replication is to verify it within rule-tuple drift tolerance.

## 7. Falsification

If H1b fails — i.e. ANY cross-tense pair shares > 0 chars, or ANY within-tense pair shares 0 chars — the H-NEW-58c sharp-binary claim is invalidated at the operational definition used. The parent finding's "exact 0 / nonzero" headline becomes a candidate for amendment.

## 8. Cross-references

- Parent: H-NEW-58c musabbiḥāt tense-split (`findings/phase-b-hypotheses/h-new-58c-musabbihat-tense-split.md`).
- H-NEW-103 musabbiḥāt 4-form typology (PASS-DIRECTED at p=0.0049).
- H-NEW-340 musabbiḥāt block+formula stacking (Cell A {Q 57, 59, 61, 62, 64} at 8.1%ile most-cohesive grouping).
- HANDOFF/01-WHAT-WE-KNOW.md "musabbiḥāt cluster (H-NEW-58c)".

## 9. Replication

- Script: `surahs/Q062-al-jumuah/scripts/Q062_F_all_tests.py` function `q062_f_03`.
- Output: `surahs/Q062-al-jumuah/csv/Q062-F-03.json`.
