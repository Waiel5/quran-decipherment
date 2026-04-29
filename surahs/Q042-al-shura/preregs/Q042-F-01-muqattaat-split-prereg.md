---
prereg_id: Q042-F-01
title: Q 42 two-verse muqaṭṭaʿāt-split uniqueness test
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q042-F-01 — two-verse muqaṭṭaʿāt-split uniqueness

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: Across all 29 muqaṭṭaʿāt-opened surahs in the Quran, **Q 42 is the only surah** where the muqaṭṭaʿāt are split into two consecutive verses (verse 1 = ḥā mīm; verse 2 = ʿayn sīn qāf). All other 28 muqaṭṭaʿāt-opened surahs have all muqaṭṭaʿāt within verse 1.

## 2. Null

**H0**: Two or more muqaṭṭaʿāt-opened surahs have multi-verse muqaṭṭaʿāt splits.

## 3. Operationalization

- Tashkeel level: **no-tashkeel**.
- Source: `quran-text/quran-no-tashkeel.json`.
- Muqaṭṭaʿāt-opened surahs (the canonical 29): Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68.
- Test: for each, examine verse 1 (and verse 2 if needed). Identify which verses contain ONLY muqaṭṭaʿāt-letters (i.e., the verse text consists solely of disconnected Arabic letters with no full words).

## 4. Direction lock

Pre-committed: only Q 42 has muqaṭṭaʿāt at v.1 AND v.2.

## 5. Bonferroni

Single test (k=1).

## 6. Success / failure criteria

- **VINDICATION**: Q 42 is the unique surah with v.1 AND v.2 muqaṭṭaʿāt; all other 28 have only v.1.
- **NULL**: discrepancy.

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q042-F-01.json` with: per-surah verse-1 and verse-2 (if applicable) text and "is_muqattaat_only" flag, plus verdict.

## 9. Rationale

al-Suyūṭī (*al-Itqān*, nawʿ 27) and Ibn Kathīr both treat Q 42's two-verse split as unique. This pre-reg formalizes the test.
