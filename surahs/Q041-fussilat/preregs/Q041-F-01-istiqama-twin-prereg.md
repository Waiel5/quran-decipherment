---
prereg_id: Q041-F-01
title: Q 41:30 ↔ Q 46:13 *istiqāma* twin-verse exact-match test
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T01:30:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q041-F-01 — *istiqāma* twin-verse uniqueness

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The orthographic-string *إن الذين قالوا ربنا الله ثم استقاموا* (no-tashkeel level, basic Arabic letters) appears EXACTLY in Q 41:30 AND Q 46:13, AND in **NO OTHER VERSE** in the Qurʾān.

## 2. Null

**H0**: The string appears in 0, 1, or >2 verses.

## 3. Operationalization

- Tashkeel level: **no-tashkeel** (default rules-tuple).
- Search method: substring search on the no-tashkeel Quran text (`/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`).
- Search string: `قالوا ربنا الله ثم استقاموا` (verbatim, no-tashkeel).

## 4. Direction lock

Pre-committed: **exactly 2 attestations**, at Q 41:30 and Q 46:13.

## 5. Bonferroni

Single test (k=1).

## 6. Success / failure criteria

- **VINDICATION**: exactly 2 attestations, at Q 41:30 and Q 46:13.
- **NULL** (different count): publish as discrepancy.
- **PRE-COMMIT VIOLATION**: if attestation pattern doesn't match.

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q041-F-01.json` with: search string, total attestations, list of (surah:verse) hits, verdict.

## 9. Rationale

The classical claim (al-Zamakhsharī, al-Rāzī, et al.) that Q 41:30 is the *istiqāma* doctrine prooftext, twinned with Q 46:13, is empirically testable as a string-uniqueness claim. The HM-7 cluster contains both surahs (HM-A Q 41 and HM-B Q 46), making this an internal cluster cross-link.
