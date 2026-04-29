---
test_id: Q002-F-02
title: Khawātim al-Baqara (Q 2:284-286) — 3-verse divine-name-density rank vs all 3-verse windows
target_claim: al-Bukhārī tradition (multiple chains; ḥadīth ~#5009-5010) — the last three verses of al-Baqara "suffice" (man qaraʾahumā fī laylatin kafatāhu) for nightly protection.
date_locked: 2026-04-28
phase: B+
status: PRE-REGISTERED
seed: 20260428
---

# Pre-registration — Q002-F-02: Khawātim al-Baqara divine-name-density

## 1. Hypothesis (LOCKED)

**H1**: The 3-verse window (Q 2:284-286) has total divine-name occurrence count and distinct-name count in the TOP 5% of all sliding 3-verse windows (size 6,234) within the corpus.

**H0**: The window's rank is no better than the 5th percentile (rank > 312 of 6,234).

**Direction (LOCKED)**: TOP tail (HIGH density).

## 2. Comparator: H-NEW-95 result

H-NEW-95 found Q 59:22-24 was rank 1/6234 in the 99-name density family. We thus expect Q 2:284-286 to rank LOWER than Q 59:22-24, but still in the top 5% if the hadith claim has empirical correlate.

## 3. Operationalisation

- **Sliding 3-verse windows**: every (s, v) such that v+2 ≤ verse-count(s). Total = 6,236 − 2·114 = 6,008 windows. We add cross-surah windows tracking the canonical mushaf order: total 6,234.
- **Density** = (sum of name-occurrence counts in the 3 verses) / (sum of word-lengths).
- **Matching rule** identical to Q002-F-01.

## 4. Test statistic

- Rank of (Q 2, 284-286) window in descending sort of density.
- Raw count of name-occurrences and distinct names in the window.

## 5. Success / failure

- **VINDICATED**: rank ≤ 62 (top 1%) on density AND top-5 on distinct count.
- **DIRECTIONAL**: top 5% (rank ≤ 312).
- **NULL**: rank > 312.
- **PRE-COMMIT VIOLATION**: rank > 5922 (bottom 5%).

## 6. MW-1..7

- **MW-2**: The 6,234-window empirical distribution IS the null.
- **MW-5 replication**: also test on min-tashkeel variant.
- **MW-6 control**: report the window-length-only rank (control for whether the result is driven by total verse-length).

## 7. Output paths

- Script: `/Users/grey/Downloads/quran/scripts/Q002_F_02_khawatim_baqara_density.py`
- JSON: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/csv/Q002-F-02.json`
- Findings: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/Q002-F-02-khawatim-baqara.md`

*Locked 2026-04-28.*
