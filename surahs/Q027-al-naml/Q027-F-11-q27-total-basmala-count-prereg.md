---
finding_id: Q027-F-11
title: "Q 27 total basmala count: opener + Q 27:30 == 2 (corpus-singleton dual-basmala surah)"
phase: B+
date: 2026-05-10
status: PRE-REGISTERED
seed: 20260509
n_perm: deterministic
rules_tuple: "(no-tashkeel, orthographic-substring, basmala-as-surah-opener AND basmala-as-interior-verse counted separately, Hafs-Kufan, Mashriqi)"
---

# Q027-F-11 — Q 27 total basmala count == 2 (corpus-singleton dual-basmala surah)

## Hypothesis (locked)

**H1 (locked direction)**: Among the 114 surahs of the Quran, **Q 27 is the unique surah whose total basmala-attestation count (counting opener-prefix + interior verse occurrences of `بسم الله الرحمن الرحيم`) equals exactly TWO.** All other 113 surahs have either 1 (the 112 surahs Q 2-Q 8, Q 10-Q 26, Q 28-Q 114 except Q 9 — their opening basmala-header) or 0 (Q 9 al-Tawba, the only surah with no basmala-opener).

**Falsification conditions** (any one ⇒ H1 FALSIFIED):
1. Q 27 total basmala count ≠ 2.
2. Any other surah has basmala-count == 2.
3. Q 9 al-Tawba has any interior basmala attestation > 0.
4. Q 1 al-Fātiḥa has basmala-count outside {1, 2} — under the Hafs-Kufan rule-tuple (basmala-counted-only-in-Q1) Q 1:1 IS the basmala so its count is 1; under (basmala-counted-everywhere) Q 1's count is also 1 because the v.0 opener IS the v.1.

Locked direction: **per-surah count uniqueness — only Q 27 has count == 2**.

## Method

Deterministic substring count per surah (no permutation null — the test is a per-surah-uniqueness claim).

1. Load `quran-text/quran-no-tashkeel.json` (interior verses).
2. For each of 114 surahs, compute `interior_count[s]` = number of verses in surah s containing the full 6-token substring `بسم الله الرحمن الرحيم`.
3. For each surah s, compute `opener_count[s]` = 1 if s has a basmala-header opener (= all surahs except Q 9), else 0. For Q 1, the basmala IS v.1, so we count it as the opener (`opener_count[1] = 1, interior_count[1] = 1` — but they refer to the SAME token; per the Hafs-Kufan rule-tuple, Q 1 has total = 1).
4. For Q 27 specifically: opener_count = 1 (Q 27 has an opener basmala) + interior_count = 1 (Q 27:30) → total = 2.
5. For all other 113 surahs: total ∈ {0, 1}.

To avoid the Q 1 double-count ambiguity, we report the test in TWO unambiguous forms:

**Form A (Hafs-Kufan default tuple, basmala-counted-only-in-Q1)**:
- Q 1 total = 1 (the basmala IS v.1)
- Q 9 total = 0 (no opener)
- Q 27 total = 2 (opener-header + v.30 interior occurrence)
- All 111 other surahs total = 1 (opener-header only; no interior basmala)
- **Locked: Q 27 is the unique surah with total == 2.**

**Form B (basmala-counted-everywhere)**:
- Q 1 total = 2 (v.1 counted as itself; plus a putative "v.0" opener — but Q 1's basmala IS v.1, so the "v.0" is the same token; under this counting Q 1 has only 1)
- Most accepted form: Q 1 total = 1, opener_basmala counted as v.0 for the 112 other surahs.
- Q 27 total = 2 (opener-v.0 + v.30 interior).
- **Locked: Q 27 is the unique surah with total == 2.**

Both forms produce the same headline: **Q 27 has count == 2; no other surah does**.

## Pre-registered success criteria

- **PASS-CONFIRMED**: Q 27 has exactly 2 basmala-attestations (opener + v.30); no other surah has count == 2.
- **PASS-DIRECTED**: Q 27 has 2; ≤ 1 other surah also has 2 (would indicate a missed interior attestation elsewhere; would also auto-fail Q027-F-10 H1).
- **FALSIFIED**: any other deviation.

## Classical anchors

- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, classical recognition of Q 27 as carrying TWO basmalas (opener-header + interior Q 27:30), making the corpus total basmala count = 114 (if Q 9 is excluded) or 113 (if interior-only counted) — the "114 vs 113" debate.
- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, on basmala enumeration.
- Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 27:30 — explicit recognition that this surah carries a second basmala unique to it.
- al-Rāzī, *Mafātīḥ al-ghayb*, on Q 27:30 — discusses the doubled basmala as a structural marker of Solomon's letter.

## Honest limits (pre-committed)

- The Hafs-Kufan rule-tuple `basmala-counted-only-in-Q1` is the project default (per INVESTIGATION-PROTOCOL §1.4). Under this tuple, Form A is canonical. Form B accommodates the alternative tuple. Both forms confirm Q 27 uniqueness.
- The test does NOT count the broader "embedded *bismi-llāh*" 2-token form (which surfaces Q 11:41 *bismi-llāhi majrāhā* per Q027-F-05.c) — that is a different, broader marker.
- The test does NOT make any claim about whether the basmala-header is a "verse" (this is a 1,400-year classical disagreement); it simply counts the substring under both accounting schemes and reports both. Q 27 is unique under either.

## Pre-commit declaration

The SHA256 of this file is embedded in the runner script for fail-fast verification per §1.2.
