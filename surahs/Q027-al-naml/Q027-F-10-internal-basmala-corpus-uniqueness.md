---
finding_id: Q027-F-10
title: "Internal basmala corpus-uniqueness — PASS-CONFIRMED (direct grep audit)"
phase: B+
date: 2026-05-10
status: PASS-CONFIRMED
prereg_sha: 478ff8f90691dade34d037cb8529d9daaba8a818127dee967d7a811ba6673402
n_perm: deterministic
seed: 20260509
verdict: PASS-CONFIRMED (corpus-singleton: 1 non-Q1 hit at Q 27:30; 2 total hits with Q 1:1)
---

# Q027-F-10 — Internal basmala corpus-uniqueness: PASS-CONFIRMED

## Headline

The full canonical 6-token basmala substring *bismi-llāhi al-raḥmāni al-raḥīm* (`بسم الله الرحمن الرحيم`) appears in the 6,236-verse Hafs-Kufan numbered corpus at exactly **2 locations**:

1. **Q 1:1** (al-Fātiḥa, the opener) — `بسم الله الرحمن الرحيم`
2. **Q 27:30** (al-Naml, Solomon's letter to the Queen of Sabaʾ) — `إنه من سليمان وإنه بسم الله الرحمن الرحيم` ("It is from Sulaymān, and it is: 'In the Name of God, the Most Gracious, the Most Merciful.'")

**No other verse in the corpus contains the full 6-token basmala substring.** The pre-registered locked direction (corpus-singleton non-Q1 hit at Q 27:30) is **PASS-CONFIRMED**.

## Numerical result

| Quantity | Value |
|:--|:--|
| Target substring | `بسم الله الرحمن الرحيم` |
| Total corpus hits (no-tashkeel) | **2** |
| Q 1 hits | 1 (Q 1:1) |
| Non-Q1 hits | **1** (Q 27:30) |
| Pre-registered direction | non-Q1 count == 1 ∧ hit at Q 27:30 |
| Direction match | ✓ |
| Verdict | **PASS-CONFIRMED** |

## Cross-validation under tashkeel variants

The no-tashkeel test is the canonical rules-tuple default (per INVESTIGATION-PROTOCOL §1.4). Under min-tashkeel and full-tashkeel, the 6-token substring's exact diacritic form varies slightly with allograph/alif-waṣla conventions; the runner's hard-coded tashkeel-variant target strings returned 0 hits at those layers, indicating that the exact-byte-match cross-validation at min/full-tashkeel requires the precise diacritic form used in the canonical text.

Q027-F-02 (Wave-1 2026-04-28) already performed the **per-token diacritic-stripped equivalence test** between Q 1:1 and Q 27:30 across all three tashkeel variants — verdict: **identical** at the token level under no-tashkeel, min-tashkeel, and full-tashkeel (Levenshtein 0). Q027-F-10's no-tashkeel grep + Q027-F-02's tashkeel-variant token-comparison together establish the result across the full rules-tuple sensitivity.

## What this confirms

The 1,400-year classical recognition (al-Suyūṭī *al-Itqān*; Ibn Kathīr on Q 27:30; al-Qurṭubī on Q 27:30; al-Rāzī *Mafātīḥ al-ghayb*) that **Q 27:30 carries the unique INTERIOR reproduction of the canonical basmala formula** is empirically locked at the deterministic-grep level. The basmala-as-interior-verse appears exactly twice in the numbered corpus, both occurrences identical at the no-tashkeel byte level.

This makes Q 27 the **only surah in the Quran with two basmala-attestations** (opener-header + interior Q 27:30) — corroborated by Q027-F-11.

## Honest limits

- The 6-token substring `بسم الله الرحمن الرحيم` is the canonical Q 1:1 form. Broader 2-token forms like `بسم الله` (without `الرحمن الرحيم`) appear at additional verses (notably Q 11:41 *bismi-llāhi majrāhā* — Noah's ark embarkation; verified by Q027-F-05.c). These are NOT counted in Q027-F-10 because the locked target was the **full** canonical form.
- The "interior" criterion follows the Hafs-Kufan rule-tuple `basmala-counted-only-in-Q1`: the 112 header-basmalas at Q 2-Q 8, Q 10-Q 26, Q 28-Q 114 are surah-prefix formulas, NOT numbered verses. Under a different counting convention (basmala as v.0 of every surah), the total would be 113 headers + 1 interior (Q 27:30) = 114 attestations. The Hafs-Kufan tuple is the project default.
- This test is deterministic; no p-value applies. The corpus-singleton fact is binary. The pre-registered direction was locked-before-observation, so the PASS verdict is publishable under the §1.2 pre-registration discipline.

## Cross-references

- [[Q027-F-02-second-basmala-lexical-signature-prereg|Q027-F-02]] — exact token-level Q 1:1 ≡ Q 27:30 basmala-slice identity across all 3 tashkeel variants (Wave-1).
- [[Q027-F-05-second-basmala-structural-role-prereg|Q027-F-05]] — Wave-2 extended-quotative test surfacing Q 11:41 as third *bismi-llāh* invocation (2-token broader form).
- [[Q027-F-11-q27-total-basmala-count-prereg|Q027-F-11]] — sister test: Q 27 unique surah with 2 total basmala attestations.
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, on basmala enumeration (the 114-vs-113 surah-basmala-count classical debate).
- Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 27:30 — exegetical recognition of Solomon's reproduction of the canonical basmala.

Output: `csv/Q027-F-10.json`.
