---
id: H-NEW-2270
title: al-Suyūṭī Itqān distributional-claims audit (pre-registration)
date: 2026-05-29
phase: B
author: Waiel Al-Shujaa
status: PRE-REGISTERED
seed: 20260529
---

# H-NEW-2270 — al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* distributional-claims audit

## Purpose

Mine *al-Itqān* nawʿ 1 (makkī/madanī) and nawʿ 19 (ʿadad) for **testable distributional/census
claims**, verify the EXACT wording in the OpenITI source, then verify/falsify each on disk with
exact counts. This extends the H-NEW-2160 *kallā* exemplar (a single al-Suyūṭī/al-Dānī claim
VINDICATED-AFTER-DISAMBIGUATION) to a five-claim block. Equal prominence to falsifications.

## Sources

- Primary text: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, OpenITI raw
  `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`. Exact line refs cited per claim.
- Quran text + makkī/madanī ground-truth: `quran-text/quran-no-tashkeel.json` (per-surah `type` field:
  86 meccan / 28 medinan, matches `data/revelation-order.csv` `period` column: 86/28).
- Morphological disambiguation: QAC v0.4 `data/morphology/quranic-corpus-morphology-0.4.txt`
  (lemma `LEM:` and POS field — the disambiguation gold-standard, per H-NEW-2160 §10.80.1).
- Verse-position arithmetic: `data/hafs-verse-counts.tsv` (Hafs-Kūfan, 6236 verses total).

## Rules-tuple

Default `(no-tashkeel, orthographic-token for text-search; QAC-lemma+POS for homograph disambiguation,
verses, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`. The makkī/madanī label is the canonical
binary `type` field of `quran-no-tashkeel.json`; classification-source divergences (al-Suyūṭī's own
lists vs the project ground-truth, e.g. Q22 al-Ḥajj) are documented per claim, not silently resolved.

## The five pre-registered claims (directions LOCKED before final verdict)

### Claim 1 — al-Jaʿbarī muqaṭṭaʿāt criterion
**Wording** (Itqān nawʿ 1, al-Jaʿbarī's qiyāsī ṭarīq, line 1171-1174):
"كل سورة … أولها حرف تهجٍّ سوى الزهراوين والرعد … فهي مكية" — *every sūra whose opening is a
ḥarf al-tahajjī (muqaṭṭaʿāt), except the two Zahrāwān (al-Baqara Q2, Āl ʿImrān Q3) and al-Raʿd (Q13),
is Meccan.*
**Test**: of the 29 muqaṭṭaʿāt surahs, the Medinan ones must be EXACTLY {Q2, Q3, Q13}.
**Locked direction**: Medinan-muqaṭṭaʿāt set == {2,3,13}; all other 26 Meccan.
**Verdicts available**: CONFIRMED (exact match) / RULES-FRAGILE (off by classification source) / FALSIFIED.

### Claim 2 — Makkī b. Abī Ṭālib munāfiqūn criterion
**Wording** (Itqān nawʿ 1, line 1175): "كل سورة فيها ذكر المنافقين فمدنية زاد غيره سوى العنكبوت" —
*every sūra mentioning the munāfiqūn is Medinan; others add: except al-ʿAnkabūt (Q29).*
**Test**: surahs containing the hypocrite lexeme (QAC lemmas munāfiqūn / munāfiqāt / nifāq /
nāfaqa-verb / munfiqīn, root nfq, hypocrite-sense only — EXCLUDING the spending-sense anfaqa/infāq).
All such surahs Medinan EXCEPT exactly Q29.
**Locked direction**: Meccan members of the hypocrite-surah set == {29} (singleton); rest Medinan.
**Verdicts**: CONFIRMED / RULES-FRAGILE / FALSIFIED.

### Claim 3 — Ibn Masʿūd / Ibn ʿAṭiyya address criterion (bidirectional)
**Wording** (Itqān nawʿ 1, lines 1146-1152): Ibn Masʿūd (via al-Ḥākim/al-Bayhaqī/al-Bazzār):
"ما كان {يا أيها الذين آمنوا} أنزل بالمدينة وما كان {يا أيها الناس} فبمكة" — *what bears
"yā ayyuhā alladhīna āmanū" was revealed at Medina; what bears "yā ayyuhā al-nās" at Mecca.*
Ibn ʿAṭiyya / Ibn al-Faras (line 1151-1152) QUALIFY: the *āmanū* direction is "ṣaḥīḥ" but
"al-nās" "may come in the Medinan" (قد يأتي في المدني).
**Test (3a, strong direction)**: every sūra containing the phrase "يا أيها الذين آمنوا" is Medinan.
**Locked direction 3a**: Meccan members of the āmanū-address set == ∅ (empty).
**Test (3b, weak direction)**: every sūra containing "يا أيها الناس" is Meccan.
**Locked direction 3b**: Medinan members of the al-nās-address set == ∅ (empty).
**Verdicts**: 3a and 3b reported separately. If 3a holds and 3b fails, that REPRODUCES Ibn ʿAṭiyya's
own asymmetry verdict (the claim is *self-qualified* in the source) → 3a CONFIRMED, 3b
QUALIFIED-IN-SOURCE / FALSIFIED-AS-STATED.

### Claim 4 — al-Hudhalī (al-Kāmil) sajda criterion
**Wording** (Itqān nawʿ 1, line 1176): "وفي كامل الهذلي كل سورة فيها سجدة فهي مكية" —
*in al-Hudhalī's al-Kāmil: every sūra containing a sajda (prostration verse) is Meccan.*
**Test**: the 13 surahs carrying one of the 14 sajda-verses (Shāfiʿī count, Itqān nawʿ 19 line
6783-6786: al-Aʿrāf 7, al-Raʿd 13, al-Naḥl 16, al-Isrāʾ 17, Maryam 19, al-Ḥajj 22 [×2], al-Furqān 25,
al-Naml 27, al-Sajda 32, Fuṣṣilat 41, al-Najm 53, al-Inshiqāq 84, al-ʿAlaq 96) must ALL be Meccan.
**Locked direction**: Medinan members of the sajda-surah set == ∅ (empty).
**Verdicts**: CONFIRMED / RULES-FRAGILE / FALSIFIED. Any Medinan sajda-surah is a counterexample.

### Claim 5 — al-Dānī / al-Dīrīnī kallā upper-half criterion (H-NEW-2160 refinement)
**Wording** (Itqān nawʿ 1, al-Dīrīnī's verse, lines 1178-1180):
"وما نزلت كلا بيثرب فاعلمَنْ / ولم تأتِ في القرآن في نصفه الأعلى" — *kallā was never revealed at
Yathrib (Medina); and it never came in the upper half of the Quran.* (al-Dānī's count = 33, all in
the lower/mufaṣṣal half; cf. H-NEW-2160.)
**Test**: (5a) QAC-disambiguated rebuke-kallā (POS=AVR, `LEM:kal~aA`) count == 33; (5b) all 33
attestations fall AFTER the classical letter-count midpoint niṣf al-Qurʾān, which al-Suyūṭī (nawʿ 19,
line 4362-4363) places at the *nūn* of *nukran* in al-Kahf (Q18:74); (5c) none of the 33 occurs in a
surah classified Medinan.
**Locked direction**: count==33; earliest rebuke-kallā verse-position > position(Q18:74); Medinan
rebuke-kallā surahs == ∅.
**Verdicts**: VINDICATED-AFTER-DISAMBIGUATION (count + position both hold) / RULES-FRAGILE (holds under
letter-midpoint but not surah-index midpoint) / FALSIFIED.

## Multiple-comparison note

Five claims (Claim 3 split 3a/3b → 6 cells). These are independent qualitative classical assertions,
each tested as an exact-count census (not a p-value family); no global null is required (per task spec).
Where a count is a hit/miss against an exact predicted value, it is reported as exact agreement. Each
claim's homograph/sense ambiguity is tested under ≥2 lenses (raw substring vs QAC-lemma+POS) where
applicable (Claims 2 and 5).

## Failure / honesty conditions

- If the project `type` ground-truth disagrees with al-Suyūṭī's OWN makkī/madanī list for a surah
  pivotal to a verdict, the claim is RULES-FRAGILE, not CONFIRMED, and the divergence is published.
- Direction is locked above; a reversed result is published as FALSIFIED with full prominence.
- Every count is recomputed from disk by the script; no value is asserted from this pre-reg's prose.

## Files

- script: `findings/phase-b-hypotheses/scripts/h-new-2270.py` (embeds this file's SHA-256, verifies at runtime)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2270.json`
- finding: `findings/phase-b-hypotheses/h-new-2270-itqan-distributional-audit.md`
