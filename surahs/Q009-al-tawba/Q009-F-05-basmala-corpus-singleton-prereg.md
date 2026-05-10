---
finding_id: Q009-F-05
prereg_date: 2026-05-09
prereg_type: corpus-exact-verification
status: PRE-REGISTERED
---

# Q009-F-05 — Basmala corpus-singleton verification (pre-registration)

## 1. Hypothesis (DIRECTION-LOCKED)

**H1**: Q 9 al-Tawba is the **corpus-only** surah whose canonical printed opener does NOT contain the basmala formula *bismi llāhi al-raḥmāni al-raḥīm*. Under the printed-convention rules-tuple (`quran-simple-txt.txt` with basmala as canonical opener for 113 of 114 surahs), the total basmala count in the entire corpus is exactly **114** = 113 surah-openers (all surahs except Q 9) + 1 internal occurrence at Q 27:30 (Solomon's letter to Bilqīs).

This is the empirical-textual verification of the universal classical claim attested in:
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 6 *fī asbāb sukūt al-basmala fī Barāʾah* and nawʿ 7.
- al-Bayhaqī via al-Suyūṭī: 5 reasons for the basmala-omission.
- al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, introduction to Q 9 (5 classical positions).
- al-Tirmidhī, *Sunan*, ḥadīth #3086 (ʿUthmān ibn ʿAffān's response).

## 2. Pre-committed direction

LOCKED:
- T1a: Number of surahs whose canonical printed opener IS basmala = **113**.
- T1b: Number of surahs whose canonical printed opener is NOT basmala = **1** (Q 9).
- T1c: Number of internal basmala occurrences (not as opener) = **1** (Q 27:30).
- T1d: Total basmala occurrences in the printed corpus = **114**.

## 3. Rules-tuple

- corpus-1 (data-stored / Hafs-Kufan numbered convention): `quran-text/quran-no-tashkeel.json`, `quran-text/quran-min-tashkeel.json`, `quran-text/quran-full-tashkeel.json` — in these files, basmala is stored as v.1 ONLY for Q 1 (per Hafs verse-numbering); the 112 other surahs have basmala-as-opener BUT it is NOT numbered as a verse. Expected: 1 v.1-basmala (Q 1) + 1 internal (Q 27:30) = 2 stored occurrences. Q 9 is the ONLY surah whose v.1 begins with anything other than the basmala.
- corpus-2 (printed convention): `data/alt-text/quran-simple-txt.txt` — basmala printed before every surah except Q 9. Expected: 114 total basmala occurrences (113 openers + 1 internal).
- token-level: orthographic match of the canonical 4-word basmala formula (with NFKD diacritic-strip for tolerance to tashkeel variants).
- Test both Mashriqi (default JSON) and printed (alt-text simple) conventions.

## 4. Pre-committed thresholds

| Outcome | Verdict |
|:--|:--|
| Stored-JSON: exactly 1 surah has basmala as v.1 (Q 1), 113 surahs do NOT, 1 internal (Q 27:30). And printed: 113 opener-basmalas + 1 internal = 114 total. | **VINDICATED at corpus-exact** |
| Any deviation | **FALSIFIED** |

## 5. Bonferroni correction

Family k = 8 pre-registered Q 9 audits (F-01 through F-07 + extant). α_corrected = 0.05/8 = 0.00625. This test is deterministic count-verification; no permutation null needed.

## 6. Method

```python
# corpus-1 (JSON)
for s in 1..114:
    v1_starts_with_basmala = bool(basmala_pattern.match(verses[0]['text']))
internal = count of basmala in any non-v1 verse across all surahs
# corpus-2 (printed)
n_basmala = count of basmala matches in NFKD-stripped quran-simple-txt.txt
```

## 7. Replication

- Independently verify Q 27:30 contains the internal basmala (Solomon's letter): pre-registered locus.
- Independently verify Q 9 v.1 is not the basmala: opens with *barāʾatun mina llāhi wa-rasūlih*.

## 8. Pre-commit

This is a corpus-exact verification with deterministic outcome. SHA256 embedded in the run script.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
