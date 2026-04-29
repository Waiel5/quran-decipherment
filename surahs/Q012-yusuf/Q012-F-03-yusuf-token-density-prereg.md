---
surah: 12
test_id: Q012-F-03
title: Concentration of the name يوسف across the 114 surahs
file_type: pre-registration
date_locked: 2026-04-28
seed: 12030
---

# Q012-F-03 — Pre-registration: Yūsuf-name concentration

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** The orthographic token يوسف is **at least 80% concentrated in surah Q 12** out of all its Quranic occurrences. Q 12 is the lexical-name-eponym-locus for the prophet's name.

**H0:** Concentration is < 50% (i.e. Q 12 contains less than half of all يوسف tokens).

**Direction:** Concentration in Q 12 > 80% (LOCKED).

## 2. Operational definition

**Token**: orthographic exact-match `يوسف` (no-tashkeel, whitespace-tokenized, no derivational variants).

**Per-surah counts**: number of token-occurrences.
**Concentration metric**: `tokens_in_Q12 / total_tokens_in_Quran`.

## 3. Comparison frame

For perspective, the same metric for several other Quranic personal-names:
- موسى (Mūsā), عيسى (ʿĪsā), إبراهيم (Ibrāhīm), يعقوب (Yaʿqūb), نوح (Nūḥ).

Each name's primary surah-locus and concentration is reported.

## 4. Success / Failure

- **CONFIRMED**: ≥ 80% concentration of يوسف in Q 12.
- **DIRECTIONAL**: 60–80%.
- **NULL**: < 50%.

## 5. Rules-tuple

`(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 6. Honest limits

- Excluding derivational variants (e.g. يوسفك, ليوسف with prefix) understates total occurrences. Acceptable because the test asks about the **bare-name token** specifically as a literary-eponym signal.
- A name's concentration can be confounded by surah-length: a long surah trivially has more occurrences. The metric is **fraction of total**, not per-word density, to avoid this confound.

## 7. SHA256 lock

Embedded at run-time in `scripts/Q012_F_03_yusuf_density.py`.
