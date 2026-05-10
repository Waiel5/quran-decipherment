---
prereg_id: Q046-F-05
title: aḥqāf (sand-dunes) surface-form hapax verification
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q046-F-05 — *aḥqāf* corpus-singleton

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The surface-form word **الأحقاف** (*al-aḥqāf*, "the sand-dunes") is a corpus-singleton at **Q 46:21**. Variant orthographic forms (without the definite article: أحقاف) may also be absent elsewhere.

## 2. Null / negation

**H0**: الأحقاف appears more than once, OR not at Q 46:21.

## 3. Operationalization

- Source: `quran-text/quran-no-tashkeel.json`.
- Primary search: `الأحقاف` (with article).
- Secondary search: `أحقاف` (without article, anywhere).
- Cross-reference at root level: `Hqf` in `data/morphology/root-index.json`.

## 4. Direction lock

Pre-committed: **الأحقاف unique at Q 46:21**.

## 5. Bonferroni

k=3 (Q 46 family). α_corrected = 0.0167. Test is exact.

## 6. Success / failure criteria

- **VINDICATED**: 1 attestation at Q 46:21.
- **NULL_OR_DISCREPANCY**: any disagreement.

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q046-F-05.json`: surface_form_loci, root_Hqf_attestations, verdict.

## 9. Rationale

Like *jāthiya* (Q 45), the *aḥqāf* form is widely cited as a Quranic hapax (al-Suyūṭī *al-Itqān*). The verification confirms the lexical signature of the surah-name.

## 10. Honest limits

- Surface-form is rules-tuple-dependent; the consonantal skeleton (no-tashkeel) is the default.
- Classical *muʿjam* lexica may distinguish "aḥqāf" as a plural of *ḥiqf* (sand-curve) from related forms; this test does not parse the morphology.
