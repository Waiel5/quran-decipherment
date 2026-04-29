---
prereg_id: Q046-F-03
title: Q 46 *al-Aḥqāf* corpus-hapax eponymity strength
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T03:20:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q046-F-03 — *al-Aḥqāf* corpus-hapax eponymity

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The root ح-ق-ف (Hqf) underlying the surah-name *al-Aḥqāf* has **exactly one** corpus-wide attestation, and that attestation is in Q 46. Q 46 is therefore a **hapax-eponym** surah.

## 2. Null

**H0 (corpus-hapax)**: Hqf has > 1 attestations in the corpus (i.e., not corpus-hapax).

## 3. Operationalization

- Source: `/Users/grey/Downloads/quran/data/morphology/root-index.json`, key `"Hqf"`.
- Count of attestations.
- Verification at orthographic level: regex search for `أحقاف`/`الأحقاف` in `quran-text/quran-no-tashkeel.json`.

## 4. Direction lock

Pre-committed: **count = 1**, **location = Q 46:21**.

## 5. Bonferroni

Single test (k=1). Deterministic verification.

## 6. Success / failure criteria

- **VINDICATED**: count == 1 AND location == [46, 21, *].
- **REFUTED**: count ≠ 1 OR location ≠ Q 46.

## 7. Seed

N/A (deterministic).

## 8. Output

JSON to `csv/Q046-F-03.json` with: corpus_count, location, surface_form, comparison-class (hapax-eponym surahs).

## 9. Notes

Classical anchor: al-Suyūṭī *al-Itqān* nawʿ 17 (asmāʾ al-suwar) — surah named for v.21 attestation; al-Ṭabarī ad Q 46:21.

Comparison-class: corpus-hapax-eponym surahs include
- Q 46 al-Aḥqāf (Hqf, 1 attestation)
- Q 105 al-Fīl (fyl "elephant", 1 root attestation in Q 105:1)
- Q 99 al-Zalzala (zlzl, 2 attestations both in Q 99)

Corpus-hapax (1/1) is a **stricter** condition than surah-hapax (only-in-the-surah but with multiple internal attestations).
