---
prereg_id: Q045-F-05
title: jāthiya (kneeling) surface-form hapax verification
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q045-F-05 — *jāthiya* surface-form corpus-singleton

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The surface-form word **جاثية** (*jāthiya*, "kneeling," in the precise orthographic shape that appears at Q 45:28) is a **corpus-singleton** (hapax legomenon): it appears exactly *once* in the entire Quran, at Q 45:28.

The root *j-th-w* (`jvw` in Buckwalter) may have more attestations; the test is at the orthographic-token level (no-tashkeel).

## 2. Null / negation

**H0**: The surface-form جاثية appears more than once, OR not at Q 45:28.

## 3. Operationalization

- Source: `quran-text/quran-no-tashkeel.json`.
- Search target: literal string `جاثية` (with leading whitespace or at line-start, with trailing whitespace or end-of-verse).
- Enumerate all (surah, verse) loci.
- Cross-check at root level using `data/morphology/root-index.json` for `jvw`.

## 4. Direction lock

Pre-committed: **exactly 1 attestation at Q 45:28**.

## 5. Bonferroni

Member of Q 45 novel-findings family (k=3 in this batch). α_corrected = 0.0167. Test is exact.

## 6. Success / failure criteria

- **VINDICATED**: 1 attestation at Q 45:28.
- **NULL_OR_DISCREPANCY**: any disagreement.

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q045-F-05.json`: attestation_loci, n_attestations, root_jvw_attestations (all), verdict.

## 9. Rationale

Surah names often draw from a distinctive lexical token. The Q 45 *jāthiya* is widely cited as a hapax in the Quranic dictionary tradition (al-Suyūṭī *al-Itqān* §40 catalogs the unique-word phenomenon). This pre-reg formalizes the verification on disk.

## 10. Honest limits

- The orthographic-token test is rules-tuple-dependent; under min-tashkeel or full-tashkeel the surface form may include short vowels and behave differently. The default (no-tashkeel) is reported.
- The classical *muʿjam* tradition uses root-form rather than surface-form hapax; we report both.
