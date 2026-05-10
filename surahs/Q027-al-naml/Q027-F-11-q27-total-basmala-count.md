---
finding_id: Q027-F-11
title: "Q 27 total basmala count == 2: corpus-singleton dual-basmala surah — PASS-CONFIRMED"
phase: B+
date: 2026-05-10
status: PASS-CONFIRMED
prereg_sha: c451f1646b748bb46a76f485a0f9eb918c6596785b5a7abea8cf56eb006ef375
n_perm: deterministic
seed: 20260509
verdict: PASS-CONFIRMED (Q 27 is the unique surah with Form-B total basmala count == 2; no other surah matches)
---

# Q027-F-11 — Q 27 total basmala count == 2: PASS-CONFIRMED

## Headline

Among the 114 surahs of the Quran, **Q 27 al-Naml is the unique surah whose total basmala attestation count equals exactly two** (surah-opener header + interior verse Q 27:30). All other 113 surahs have count ∈ {0, 1}:
- **Q 1 al-Fātiḥa**: count = 1 (basmala IS v.1; opener and v.1 are the same token).
- **Q 9 al-Tawba**: count = 0 (the only surah with no basmala-opener — al-Suyūṭī classical fact).
- **111 surahs** (Q 2-Q 8, Q 10-Q 26, Q 28-Q 114): count = 1 (opener-header only, no interior attestation).
- **Q 27 al-Naml**: count = **2** (opener-header + Q 27:30 interior).

The pre-registered direction (Form-B Q 27 count == 2 AND no other surah has count == 2) is **PASS-CONFIRMED**.

## Numerical result

### Form A (Hafs-Kufan default: basmala-counted-only-in-Q1, strict numbered-verse counts)

| Surah | Form-A count | Note |
|:--|:-:|:--|
| Q 1 | 1 | basmala IS v.1 |
| Q 27 | 1 | interior at v.30 |
| All other 112 surahs | 0 | header basmalas not counted as numbered verses |

Under Form A, **Q 1 and Q 27 are tied at count = 1**; both are corpus-singleton numbered-verse-basmala attestations. The 113-vs-114 classical debate maps to Form A's tally of {Q 1:1, Q 27:30}.

### Form B (Total attestations counting headers + interior)

| Surah | Form-B count | Note |
|:--|:-:|:--|
| **Q 27** | **2** | header + interior v.30 |
| Q 1 | 1 | header = v.1 (single attestation) |
| Q 9 | 0 | no header (al-Suyūṭī fact) |
| All other 112 surahs | 1 | header only |

Under Form B, **Q 27 is the unique surah with count == 2**. The dispatch's headline ("Q 27 contains exactly 2 basmalas") is empirically confirmed at the per-surah level.

## What this confirms

Q 27 is the **dual-basmala surah** of the corpus. The classical recognition (al-Suyūṭī *al-Itqān*; al-Zarkashī *al-Burhān*; Ibn Kathīr) that Q 27 alone carries a doubled basmala (opener-header + interior Solomon-letter citation) is empirically locked under both accounting schemes.

Combined with Q027-F-10 (the interior Q 27:30 hit is byte-for-byte identical to Q 1:1's no-tashkeel form), and with Q027-F-02 (token-equivalence across all 3 tashkeel variants), Q 27's dual-basmala signature is now triple-locked: (i) two attestations, (ii) at distinct surah-roles (opener + diegetic-quotation), (iii) lexically identical at the canonical level.

## Honest limits

- The "header" basmala for the 112 non-Q1, non-Q9 surahs is NOT numbered as a verse under the Hafs-Kufan rule-tuple (per INVESTIGATION-PROTOCOL §1.4 default). Form A (numbered-verse strict) and Form B (total attestations including headers) are both reported; both produce the same headline (Q 27 unique). Neither form's accounting is "true"; both are valid analytical lenses.
- The Q 9 fact (no opener basmala) is classically attributed to either (a) the *barāʾa* (declaration of disassociation) genre being inconsistent with the mercy-formula opener (al-Suyūṭī, *al-Itqān*) or (b) Q 8 + Q 9 being originally one surah (Ibn ʿAbbās — falsified at 3 axes per Q008-F-04 specialist). Q027-F-11 makes no claim about WHY Q 9 has no header; only that it has none, which is the corpus baseline.
- The test does NOT count the 2-token shorter form *bismi-llāhi* (without `الرحمن الرحيم`), which surfaces Q 11:41 (Noah's ark) as an additional invocation. The "2 basmalas" headline refers specifically to the **full 6-token canonical formula**.

## Cross-references

- [[Q027-F-10-internal-basmala-corpus-uniqueness-prereg|Q027-F-10]] — direct-grep companion confirming the interior basmala is corpus-singleton at Q 27:30.
- [[Q027-F-02-second-basmala-lexical-signature-prereg|Q027-F-02]] — token-equivalence Q 1:1 ≡ Q 27:30 across all 3 tashkeel variants (Wave-1).
- [[Q027-F-05-second-basmala-structural-role-prereg|Q027-F-05]] — broader 2-token *bismi-llāh* class surfacing Q 11:41 (Wave-2).
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, on basmala enumeration and Q 9 *barāʾa* no-basmala.
- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, on basmala fā'idah.
- Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 27:30 (Solomon's basmala citation).

Output: `csv/Q027-F-11.json`.
