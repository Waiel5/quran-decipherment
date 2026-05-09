---
prereg_id: Q076-F-04
surah: 76
title: Shīʿī Ahl-al-Bayt revelation-cause classical-claim audit
date_locked: 2026-05-09
phase: B+
hypothesis_class: classical-claim-audit
post_hoc: false
direction_locked: Sunni canonical-hadith corpus shows the Ahl-al-Bayt revelation-cause IS NOT VERIFIED at Bukhārī/Muslim/Tirmidhī level
bonferroni_k: 4
bonferroni_family: Q076-F
alpha_bon: 0.0125
seed: 20260509
verse_numbering: hafs-kufan
orthography: no-tashkeel
audit_class: deductive-historical (not permutation-null)
---

# Q076-F-04 — The Shīʿī Ahl-al-Bayt revelation-cause for Q 76: classical-claim audit

## The classical claim (the target hypothesis)

According to the Imāmī Shīʿī tafsir tradition (al-Ṭabarsī *Majmaʿ al-Bayān* on Q 76; al-Ṭūsī *al-Tibyān*; the *Tafsīr al-ʿAyyāshī*), Q 76:5–22 (the paradise-tableau passage) was revealed about the household of the Prophet — ʿAlī b. Abī Ṭālib, Fāṭima al-Zahrāʾ, al-Ḥasan, and al-Ḥusayn — when they fed an orphan, a poor man, and a captive from their iftar food during three consecutive days while themselves fasting and breaking fast on water alone. The story:

> "Al-Ḥasan and al-Ḥusayn fell ill; the Prophet and the Companions visited them. They suggested ʿAlī make a vow to fast three days in gratitude when they recovered. ʿAlī, Fāṭima, and their servant Fiḍḍa each made the vow. Each evening of the three nights, just as iftar was being prepared, a beggar (mere day 1) / orphan (day 2) / captive (day 3) came to the door asking for food. The household gave their entire iftar away each day, breaking fast on water alone. On the third night, Q 76:5–22 was revealed, with v. 7 (yūfūna bi-l-nadhr) and v. 8 (wa-yuṭʿimūna l-ṭaʿām ʿalā ḥubbihi miskīnan wa-yatīman wa-asīran) directly tied to their conduct."

This is Imāmī tafsir's strongest revelation-cause assertion for Q 76 and is widely cited as one of the Qurʾānic textual proofs of Ahl al-Bayt sanctification (alongside Q 33:33 *āyat al-taṭhīr*, Q 5:55 *āyat al-wilāya*).

The claim is also recorded by some Sunni authorities — notably **al-Suyūṭī's *al-Durr al-Manthūr* on Q 76**, citing Ibn Mardawayh, ʿAbd b. Ḥumayd, al-Ḥākim al-Naysābūrī, and others. Al-Wāḥidī also cites it (via *Asbāb al-Nuzūl*). It is **NOT** in al-Bukhārī or Muslim.

## The audit hypothesis (direction-locked)

H₁: The Ahl-al-Bayt revelation-cause for Q 76 is NOT verifiable at the canonical Sunni-hadith corpus level (Bukhārī + Muslim + Tirmidhī). The narrative is a SECONDARY Imāmī-traditional claim, with isolated Sunni transmission paths in al-Suyūṭī's *al-Durr al-Manthūr* (which itself cites al-Wāḥidī's *Asbāb*, al-Ḥākim's *al-Mustadrak*, etc., none of which are at Bukhārī/Muslim ṣaḥīḥ-rank).

H₀: The Ahl-al-Bayt revelation-cause appears in canonical Sunni ṣaḥīḥ corpora at strong sanad-rank.

## Tests

### Cell A — Bukhārī corpus search

Search Bukhārī for keywords: ['هل أتى', 'الإنسان حين من الدهر', 'المسكين واليتيم والأسير', 'يوفون بالنذر', 'فاطمة', 'علي بن أبي طالب' co-occurring with Q 76 markers].

Expected: ZERO match for the revelation-cause story; ONLY match Bukhārī #870 + #1037 (Friday Fajr Q 32 + Q 76 recitation).

### Cell B — Muslim corpus search

Same search criteria. Expected: ONLY match Muslim #9200 (Friday Fajr Q 32 + Q 76 parallel).

### Cell C — Tirmidhī corpus search

Same. Expected: ONLY Tirmidhī #26300 (Friday Fajr parallel).

### Cell D — al-Suyūṭī *al-Durr al-Manthūr* secondary trace

Trace the Ahl-al-Bayt narrative via on-disk al-Durr al-Manthūr extracts (if available) or via independent verification of the chain. The narrative is reportedly transmitted via:
1. Ibn ʿAbbās → ʿAṭāʾ → various paths (per al-Wāḥidī)
2. ʿAbd b. Ḥumayd 
3. Some Imāmī-only paths via al-Aṣbagh b. Nubāta

Sanad-quality assessment: per Ibn Taymiyya (*Minhāj al-Sunna*) the narrative lacks Sunni-ṣaḥīḥ rigor; modern Sunni hadith critics (al-Albānī) classify all variants as ḍaʿīf or maḍrūb due to chain-discontinuity and weak narrators (al-Aṣbagh b. Nubāta is matrūk per Sunni ʿilm al-rijāl).

## Verdict-template (deductive-historical, not statistical)

- **AUDIT-VERIFIED-NEGATIVE** if Cells A, B, C all return ZERO for the revelation-cause narrative AND Cell D confirms ḍaʿīf-rank Sunni transmission
- **AUDIT-VERIFIED-POSITIVE** if Cells A or B contain any sanad-strong revelation-cause hadith
- **AUDIT-INCONCLUSIVE** if intermediate

## Honest framing

This is NOT a sectarian-polemical audit. The Imāmī tradition has its own internal sanad standards by which the revelation-cause is mutawātir; the question here is solely whether the Sunni canonical-ṣaḥīḥ corpus independently corroborates it. A negative finding **does NOT refute the Imāmī claim under Imāmī sanad standards**; it only registers that the claim is not Sunni-canonically corroborated, which is the standard the Quran Decipherment Project applies to all classical claims (per MW-6 hadith-verification protocol).

## Garden-of-forking-paths log

The hypothesis was framed before any text-search was run: the brief explicitly identified the Shīʿī Ahl-al-Bayt narrative as an "adversarial audit candidate." The audit returns whatever the Sunni hadith corpus contains; no flexibility in defining what counts as a positive match.
