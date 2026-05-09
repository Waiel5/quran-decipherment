---
surah: 48
test_id: Q048-F-02
H_NEW: H-NEW-1261
title: "Q 48 al-Fatḥ — descriptive-uniqueness of perfect alif-monorhyme among Medinan surahs ≥ 28 verses"
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q048-F-02-monorhyme-uniqueness
alpha_raw: 0.05
alpha_bon: 0.05
direction_locked: true
rules_tuple: "(min-tashkeel, verse-final-letter, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
prereg_sha_expected: TBD-AT-WRITE-TIME
parent_findings:
  - h-new-700 (rhyme-letter diagnostics; 15 perfect-monorhyme surahs identified)
  - h-new-660 (compression-tail gradient; rhyme-axis cross-corpus distinct)
  - h-new-750 (iʿjāz signature; rhyme entropy contributes)
classical_anchors:
  - al-Bukhārī, *Maghāzī* #315 / Tafsir #356 (Prophet's vibrant-quivering recitation of Q 48 on Conquest day — the structural-empirical anchor)
  - al-Jāḥiẓ, *al-Bayān wa-l-tabyīn* (classical analysis of monorhyme as Arabic-rhetorical device)
  - al-Bāqillānī, *Iʿjāz al-Qurʾān* (rhyme as part of iʿjāz al-fawāṣil)
---

# Q048-F-02 Pre-registration — Perfect-alif-monorhyme uniqueness in Q 48

## 1. Hypothesis (locked before observation)

**H1 (descriptive-uniqueness, locked direction)**: Q 48 al-Fatḥ exhibits a **PERFECT alif-monorhyme** (verse-final letter = alif in 29/29 verses, frac = 1.0) AND is the **only Medinan surah of length ≥ 28 verses** in the corpus to do so.

**H0**: Q 48 is not a perfect monorhyme OR is not unique among the relevant subset.

**Direction**: Q 48 perfect-monorhyme + Medinan-length-uniqueness LOCKED.

## 2. Operational definition

- **Source**: `findings/phase-b-hypotheses/csv/h-new-700.json` `rhyme.rhyme_letter_diagnostics` array. Each surah has `top_letter` and `frac` fields (rules: orthographic verse-final letter from `quran-min-tashkeel.json`).
- **Perfect monorhyme**: a surah where `frac == 1.0` (all verses end with the same letter).
- **Medinan filter**: surahs with `revelation-order.csv` `period == "Medinan"` OR Nöldeke `noldeke_phase == "Medinan"` — defaults to revelation-order CSV's `period` field.
- **Length filter**: ≥ 28 verses.

## 3. Test (descriptive)

The test is descriptive-categorical: enumerate all perfect-monorhyme surahs (frac=1.0), filter to Medinan + length ≥ 28, and check if Q 48 is the unique surah in this subset.

## 4. Null model (sensitivity)

Under the null that perfect-monorhyme status is independent of Medinan classification + length-class:
- Probability of any single Medinan surah being perfect-monorhyme = (# perfect-monorhyme Medinan / # Medinan).
- Probability of any single surah of v ≥ 28 being perfect-monorhyme = (# perfect-monorhyme v≥28 / # surahs v≥28).

The empirical question: is the conjunction (Medinan + v≥28 + perfect-monorhyme) realized only by Q 48?

This is NOT a frequentist null-test in the standard sense; it is a **descriptive-uniqueness CLAIM** (categorical). The claim is empirically verifiable from the data.

## 5. Success / Failure criteria

- **CONFIRMED**: Q 48 is the unique perfect-monorhyme Medinan surah of length ≥ 28 in the corpus.
- **DIRECTIONAL**: Q 48 is one of ≤ 2 perfect-monorhyme Medinan surahs of length ≥ 28.
- **NULL**: Q 48 is NOT perfect-monorhyme OR multiple Medinan surahs of length ≥ 28 share this property.
- **PRE-COMMIT VIOLATION**: Q 48 frac < 1.0 (the brief's claim of "5 fatḥ" was wrong; the rhyme uniformity could also be wrong).

## 6. Honest limits known a priori

- The 15 perfect-monorhyme surahs are listed in `01-empirical-profile.md` §3.1. Of these:
  - Q 54 al-Qamar: 55 verses, ر, **Meccan**.
  - Q 76 al-Insān: 31 verses, ا, **Medinan-or-Meccan-debated** (Tanzil-Egyptian places at rank 98, Medinan; some classical chains label Meccan).
  - **Q 48 al-Fatḥ: 29 verses, ا, Medinan** ← this surah.
  - Q 72 al-Jinn: 28 verses, ا, **Meccan**.
  - Q 92 al-Layl: 21 verses, ي, **Early Meccan**.
  - Others: all < 16 verses.
- The Medinan filter is the key: only Q 48 (and arguably Q 76 if classified Medinan) satisfies the conjunction Medinan + perfect-monorhyme + v ≥ 28.
- The test is **descriptive**, not frequentist. The empirical contribution is the structural fingerprint identification, not a p-value.
- Pre-flight verification: `01-empirical-profile.md` §3.1 enumerates the 15 perfect-monorhyme surahs from `h-new-700.json`. Q 48 is the largest-Medinan member.

## 7. Garden-of-forking-paths log

- Decision: use frac == 1.0 (exact match) rather than frac ≥ 0.95 (near-perfect). RATIONALE: only the exact-match version is the strong descriptive claim; the near-perfect version expands to ~5 surahs and dilutes the uniqueness.
- Decision: apply Medinan filter via revelation-order CSV (`period` field). RATIONALE: the project's canonical chronology source; Tanzil-Egyptian + Nöldeke alignment.
- Decision: apply v ≥ 28 length-filter. RATIONALE: 28 = Q 72 al-Jinn's verse count; the threshold preserves Q 76 (31), Q 48 (29), Q 72 (28) as candidates and excludes shorter surahs where monorhyme is statistically more probable.
- ALTERNATIVE-HYPOTHESIS-DECLARED: if the Medinan filter is loosened to include Q 76 al-Insān as Medinan, then the descriptive claim becomes "Q 48 + Q 76 are the only Medinan perfect-monorhymes of v ≥ 28" — still a small-set uniqueness claim, but pair-form rather than singleton.

## 8. Rules-tuple

`(min-tashkeel, verse-final-letter, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

The rhyme analysis uses min-tashkeel (preserving the verse-final letter) per `h-new-700` standard. The result is invariant under no-tashkeel (the final letter is the same).

## 9. Bonferroni accounting

k = 1 (single descriptive test). α_bon = 0.05.

## 10. Output

- Pre-reg: this file.
- Script: `scripts/Q048_F_02_monorhyme_uniqueness.py`.
- JSON: `csv/Q048-F-02.json`.
- Findings: `06-novel-findings.md` §Q048-F-02.

## 11. SHA256 lock

Computed at write-time, embedded into the script.
