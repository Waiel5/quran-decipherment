---
surah: 15
test_id: Q015-F-02
title: Q 15:9 textual-preservation construction corpus-uniqueness
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
bonferroni_k: 3
bonferroni_family: Q015-F-family-2026-05-08
alpha_bon: 0.0167
---

# Q015-F-02 — Pre-registration: Q 15:9 textual-preservation construction corpus-uniqueness

## 1. Hypothesis (locked before observation)

**Background**: Q 15:9 *innā naḥnu nazzalnā al-dhikra wa-innā lahu la-ḥāfiẓūn* — "Indeed, We have sent down the Reminder, and indeed We are its Guardian" — is the canonical Qurʾānic textual-preservation iʿjāz declaration, classically anchored by al-Bāqillānī's *Iʿjāz al-Qurʾān* and al-Khaṭṭābī's *Bayān iʿjāz al-Qurʾān*.

**H1 (direction-locked)**: Q 15:9 is the **corpus-UNIQUE verse** combining ALL THREE of the following constructions:
- (a) divine first-person plural self-reference *naḥnu nazzalnā* (We sent down).
- (b) the verb *nazzala* governing the object *al-dhikr* (the Reminder).
- (c) the divine attribution *lahu la-ḥāfiẓūn* (We are its Guardian) referring to the revealed text.

If all three constructions appear in Q 15:9 alone in the corpus, the verse is corpus-UNIQUE in this combined construction.

**H0 (null)**: Q 15:9 is NOT corpus-unique — at least one other verse joins all three constructions.

**Direction LOCKED**: corpus-unique combined construction at Q 15:9.

## 2. Operational definition

**Constructions** (Arabic, no-tashkeel, substring-search across all 6,236 verses):
- (a) *naḥnu nazzalnā* / *innā naḥnu nazzalnā*: substring `نحن نزلنا` or `إنا نحن نزلنا`.
- (b) *nazzalnā al-dhikr*: substring `نزلنا الذكر` (verb-noun in this exact orthographic order).
- (c) *lahu la-ḥāfiẓūn*: substring `له لحافظون` (with the divine-referent context — referring to the revealed text). NOTE: corpus-search will also find Q 12:12 *innā lahu la-ḥāfiẓūn* (Joseph's brothers' false-guarantee about him); this is a DIFFERENT referent. We count by the EXACT-substring `له لحافظون`, then verify the referent is the revealed text by manual classification at write-time.

**Corpus-unique combined indicator**: Q 15:9 is the unique verse where (a), (b), AND (c) co-occur AND the referent of *lahu* in (c) is the revealed text.

## 3. Test statistic

**Primary (direction-locked)**: combined-corpus-unique indicator (TRUE / FALSE).

**Secondary** (descriptive):
- (a) count of corpus-attestations of *naḥnu nazzalnā*.
- (b) count of corpus-attestations of *nazzalnā al-dhikr*.
- (c) count of corpus-attestations of *lahu la-ḥāfiẓūn*; classification of referent (revealed-text vs other).

## 4. Success / Failure thresholds

- **CONFIRMED**: combined-corpus-unique = TRUE.
- **PASS-DIRECTED**: 2 out of 3 constructions are corpus-unique to Q 15:9 (one shared).
- **NULL**: combined construction appears in ≥ 2 verses.
- **PRE-COMMIT VIOLATION**: combined construction appears in many verses (≥ 5).

## 5. Honest limits known a priori

- Substring-search may miss morphological-variant constructions (e.g., a different prefix on *nahnu nazzalnā* would not match the strict substring). We accept this limitation as a CONSERVATIVE direction (under-reports matches).
- The combined-construction is at the **lexical-syntactic** level. The wider classical theological claim about textual-preservation as iʿjāz is OUT OF SCOPE for empirical-architectural testing. The empirical result is purely about lexical-syntactic uniqueness.
- The (c) referent-classification step requires manual verification (the substring matches Q 9:112, Q 12:12, Q 12:63, Q 15:9 — only Q 15:9 has the divine-referent + revealed-text referent).

## 6. Rules-tuple

`(no-tashkeel, orthographic-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Permutation null

Not applicable for a corpus-uniqueness statistic. The test is direction-locked: corpus-unique = TRUE / FALSE.

## 8. SHA256 lock

To be computed at write-time. Embedded in `scripts/Q015_F_all_tests.py`.
