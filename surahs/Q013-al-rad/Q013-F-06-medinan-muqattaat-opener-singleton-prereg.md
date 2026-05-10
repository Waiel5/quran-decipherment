---
surah: 13
test_id: Q013-F-06
title: Q 13 is the corpus-unique MEDINAN muqaṭṭaʿāt-opener (al-Suyūṭī classification audit + corpus enumeration)
file_type: pre-registration
date_locked: 2026-05-10
seed: 20260509
n_perm: 0
bonferroni_k: 1
alpha: 0.05
verdict_ceiling: DESCRIPTIVE-CORPUS-EXACT (enumeration test; no permutation null required)
classical_anchor: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 6 (the muqaṭṭaʿāt as Meccan markers); al-Suyūṭī, nawʿ 1 (Meccan/Medinan classification)
direction_of_effect: LOCKED — when the 29 canonical muqaṭṭaʿāt-opener surahs are intersected with the al-Suyūṭī Medinan-classification list, the intersection contains EXACTLY ONE element, namely Q 13. All 28 other muqaṭṭaʿāt-opener surahs are al-Suyūṭī-Meccan.
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  chronology_source: data/revelation-order.csv field `period` (Tanzil Egyptian Standard tradition, congruent with al-Suyūṭī *al-Itqān* nawʿ 1)
  muqattaat_canon: standard 29-surah list {2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68}
---

# Q013-F-06 — Pre-registration: Q 13 is the corpus-unique Medinan muqaṭṭaʿāt-opener

## 1. Origin

al-Suyūṭī, in *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 6, treats the disconnected letters (al-ḥurūf al-muqaṭṭaʿāt) as one of the structural markers of the Meccan period. The classical generalization is that the muqaṭṭaʿāt-openers belong to the Meccan revelation. al-Suyūṭī (nawʿ 1) himself classifies Q 13 al-Raʿd as Medinan, despite its ALMR-opener, making Q 13 the classical exception that the classical scholars themselves register.

This pre-reg is a CORPUS-ENUMERATION test, not a permutation test: it confirms whether Q 13 is the corpus-unique intersection of {muqaṭṭaʿāt-opener} ∩ {Medinan} under the project's default chronology source. The result is then triangulated against al-Suyūṭī's classification and Nöldeke's classification.

## 2. Hypothesis

**H1:** Under the al-Suyūṭī-aligned Tanzil Egyptian Standard chronology in `data/revelation-order.csv`, the intersection of the 29 muqaṭṭaʿāt-opener surahs and the Medinan-period surahs has cardinality exactly 1, with Q 13 al-Raʿd as the unique element.

**H0:** The intersection has cardinality > 1 (i.e., other muqaṭṭaʿāt-openers are also Medinan).

**Direction:** intersection-size = 1, intersection = {13}. LOCKED.

## 3. Cluster definition (locked from corpus surface form)

- **Muqaṭṭaʿāt-opener canon:** the 29 surahs whose first verse is composed entirely of disconnected letters. Per the standard enumeration: {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}.
- **Medinan canon:** all rows of `data/revelation-order.csv` with `period == "Medinan"`.
- **Q 13 case:** the ALMR opener is verified against `quran-text/quran-no-tashkeel.json[12].verses[0].text` and against QAC `morphology/quranic-corpus-morphology-0.4.txt` `(13:1:1)` location-tuple.

## 4. Test design

### Cell A — corpus enumeration

Load `data/revelation-order.csv`. For each of the 29 muqaṭṭaʿāt-opener surahs, retrieve `period`. Count those with period = "Medinan". The pre-committed direction is: count = 1; the one Medinan-classified muqaṭṭaʿāt-opener is Q 13.

### Cell B — chronology cross-check (Nöldeke)

For the same 29 surahs, retrieve `noldeke_phase`. Tabulate the distribution. Pre-committed direction: Q 13 is classified by Nöldeke as Late Meccan (not Medinan), illustrating that the "Medinan exception" status of Q 13 is contested in modern scholarship. This is descriptive, not a hypothesis test.

### Cell C — sanity anchor

Confirm via QAC that Q 13:1 begins with the four-letter token sequence alif-lām-mīm-rā (المر), and that this string occurs as a verse-1 opener for exactly one surah in the corpus (Q 13 only).

## 5. Bonferroni and significance

This is a corpus-enumeration test, not a permutation-null test. There is no random null to permute against: the chronology source is locked (`data/revelation-order.csv`), and the muqaṭṭaʿāt-opener canon is locked (29-surah list). The verdict is binary: either Q 13 is the unique element of the intersection or it is not. No multiple-comparison adjustment is needed for the enumeration itself; the cross-checks (Cell B, Cell C) are descriptive.

**Bonferroni-k = 1 (single planned enumeration test). α = 0.05 nominal (cosmetic, since the test is deterministic).**

## 6. Honest limits

- The "Medinan" classification of Q 13 in `data/revelation-order.csv` follows the Tanzil Egyptian Standard, which aligns with al-Suyūṭī *al-Itqān* nawʿ 1. Nöldeke's *Geschichte des Qorâns* classifies Q 13 as Late Meccan; under that source the intersection would be empty.
- The classical tradition itself preserves both classifications (al-Ṭabarī reports both Meccan and Medinan asbāb chains for Q 13; al-Qurṭubī summarizes the dispute). The "corpus-unique Medinan muqaṭṭaʿāt-opener" status is RULES-TUPLE-CONTINGENT on the choice of chronology source.
- This finding does not imply that the al-Suyūṭī generalization (muqaṭṭaʿāt = Meccan markers) is false; it locates Q 13 as the single edge-case under one of the two main chronology sources on disk.

## 7. Pre-commit violations

If the intersection contains ≥ 2 elements, or contains a surah other than Q 13, the pre-committed direction has failed and the finding is published as NULL — DIRECTION REVERSED with full prominence.
