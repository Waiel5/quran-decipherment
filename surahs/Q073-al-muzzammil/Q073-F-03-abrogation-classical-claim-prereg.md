---
surah: 73
test_id: Q073-F-03
title: Q 73:20 long-verse abrogation classical claim — hadith on-disk verification
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q073-F-03-abrogation-classical-claim
alpha_bon: 0.05
---

# Q073-F-03 — Pre-registration: Q 73:20 abrogation classical claim — hadith on-disk verification

## 1. Hypothesis (locked before observation)

**H1 (descriptive verification, locked direction):** The classical claim — that **Q 73:20 (the "long verse") abrogated or relaxed the night-prayer prescription of Q 73:1-9** — is supported by a primary-source isnād chain found in at least one of the on-disk *kutub al-tisʿah* (the 9 books: Bukhārī, Muslim, Abū Dāwūd, Tirmidhī, Nasāʾī, Ibn Mājah, Aḥmad, Mālik Muwaṭṭaʾ, Dārimī).

**H1a:** the chain explicitly attributes the abrogation to Q 73:20 (citing the verse-fragment `علم أن لن تحصوه` or `فاقرءوا ما تيسر`).

**H1b:** the chain has a named ṣaḥābī or tābiʿī authority (Ibn ʿAbbās, ʿĀʾisha, ʿIkrima, etc.).

**H0:** No on-disk hadith chain in the 9-books supports the abrogation claim explicitly.

**Direction:** classical claim VERIFIED (LOCKED).

## 2. Operational definition

- **Source corpus**: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/*.json` (Bukhārī, Muslim, Abū Dāwūd, Tirmidhī, Nasāʾī, Ibn Mājah, Aḥmad, Mālik, Dārimī).
- **Search target phrases (with harakat-stripped Arabic)**:
  - `قم الليل إلا قليلا` (the Q 73:2 verse-stem; surveyed for narrations citing it as abrogated)
  - `نسختها الآية` ("the verse abrogated it") — the technical naskh-hadith terminology
  - `علم أن لن تحصوه` (the Q 73:20 fragment which classical naskh-tradition treats as the abrogator)
  - `فاقرءوا ما تيسر` (the Q 73:20 fragment of the IMPV-qrA imperative)
- **Verification operation**: identify any hadith mentioning AT LEAST 2 of the above phrases in the SAME hadith body, OR any single hadith explicitly using `نسخ` (root: n-s-kh, "abrogate") in conjunction with Q 73 verses.
- **Source attribution**: extract isnād (chain of transmission) and matn (text body) for verified hits.

## 3. Test statistic

- N_hits = number of hadith in the 9-books explicitly affirming the abrogation claim.
- The classical claim VERIFIES if N_hits ≥ 1 with EXPLICIT abrogation-language.
- Brief specifically asks for "Mālik Muwaṭṭaʾ + Bukhārī" verification — if the hit is in a DIFFERENT collection (e.g., Abū Dāwūd or Nasāʾī), this is honestly disclosed as a brief-correction.

## 4. Permutation null

Not applicable. This is a **descriptive verification test** of a classical historical-textual claim against a primary-source corpus. The discipline-applicable principle is MW-6 nawʿ-number-verification tagging:
- VERIFIED — primary-source explicit on-disk match
- PENDING — claim cited in secondary literature but not yet on-disk
- SECONDARY-TRIANGULATED — ≥2 modern secondaries cite the same primary-source (but primary unverified)

## 5. Success / Failure

- **VERIFIED**: ≥1 hadith with explicit abrogation isnād found in ≥1 of the 9-books. Brief-correction (if applicable) honestly disclosed.
- **PENDING**: classical claim cited in secondary tafsir on-disk (al-Ṭabarī, al-Rāzī, al-Suyūṭī) but no primary-source isnād hit in the 9-books on-disk.
- **NULL**: no on-disk evidence for abrogation; classical claim is unsupported in the 9-books or in on-disk tafsir.

## 6. Honest limits known a priori

- The 9-books on-disk represent the bulk of canonical sunnī ḥadīth, but EXCLUDE:
  - shīʿī collections (al-Kāfī, etc.)
  - tafsir books (al-Ṭabarī, al-Suyūṭī al-Durr al-Manthūr — though al-Suyūṭī cites Ibn ʿAbbās ʿan ʿIkrima for this naskh)
  - musnad-style collections beyond Aḥmad (al-Ṭabarānī, al-Bayhaqī)
- The brief specifies "Mālik Muwaṭṭaʾ + Bukhārī". My pre-flight indicated NEITHER Bukhārī NOR Mālik contains the explicit Q 73:20 abrogation chain in their hadith inventory. The closest analogue in **Bukhārī** is hadith #4 (the Bad' al-Waḥy chain on Q 74:1-5, NOT Q 73:20). The closest analogue in **Mālik Muwaṭṭaʾ** is the istaysara-from-hady chain (Q 22:37, NOT Q 73:20). The brief's "Mālik + Bukhārī" suggestion is empirically INCORRECT for THIS specific abrogation claim.
- The PRE-FLIGHT actually identified **Abū Dāwūd hadith #1305** as containing the explicit Q 73:20 abrogation chain via Ibn ʿAbbās → ʿIkrima. This is a brief-correction; disclosed in the post-hoc forking-paths log per HANDOFF/04-DISCIPLINE.md.

## 7. Pre-commit attestation

- Pre-flight corpus search located the AD #1305 chain (Ibn ʿAbbās → ʿIkrima); this is logged here BEFORE pre-reg lock. The verification-VERIFIED outcome is therefore observation-locked. The strict-pre-reg test is whether the FULL classical attribution (chain naming, full isnād, matn integrity) holds under scrutiny — answered by reading the full hadith.
- The brief's "Mālik + Bukhārī" inaccuracy is therefore identified BEFORE the test runs; reported transparently.

## 8. Decision rule

1. Search all 9 hadith collections for the 4 target phrases.
2. Identify hadiths matching ≥2 of the 4 phrases AND explicit abrogation language.
3. Extract isnād + matn; verify chain integrity (named transmitters, attribution to a ṣaḥābī or tābiʿī).
4. Cross-reference against on-disk tafsir (al-Ṭabarī, al-Rāzī if available) for triangulation.
5. Apply MW-6 verification tag: VERIFIED / PENDING / SECONDARY-TRIANGULATED / NULL.

## 9. Bonferroni declaration

- bonferroni_k = 1 (single descriptive-verification test).
- bonferroni_family = Q073-F-03-abrogation-classical-claim.
- alpha_bon = 0.05 (single-test cap; no statistical inference performed — descriptive-verification only).

## 10. Connection to existing findings

- **Cross-finding-015** (classical-aesthetic claims survive empirical testing): the Q 73:20 abrogation claim is a DOCTRINAL claim, not aesthetic. Verification depends on primary-source on-disk evidence, not statistical structure.
- **Cross-finding-013** (mushaf as topological ring): Q 73 sits at a known seamless seam (Q 73→Q 74 clamped-zero per H-NEW-720). The ring topology is structural, not abrogation-related.
- **H-NEW-1300 IMPV-qrA**: Q 73:20 is the locus of 2 of the 6 corpus IMPV-qrA segments. The abrogation question is whether the v.20 imperatives REPLACED the v.2-3 prescription. Verifying this gives historical context to the corpus-fact identified in H-NEW-1300.
