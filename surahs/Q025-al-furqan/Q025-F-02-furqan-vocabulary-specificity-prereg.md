---
finding_id: Q025-F-02
title: Architectural distinctness of Q 25:1's nominal-titular use of *al-furqān*
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q025-al-furqan-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q025-F-02-furqan-distinctness
bonferroni_k: 3
alpha_bon: 0.01666
direction: Q 25:1 is the UNIQUE Quranic instance where *al-furqān* is the autonymic title of the very revelation being announced (vs. retrospective scripture-reference)
success_criterion: descriptive: 1/7 attestations match the title-autonym pattern; binary verdict on a 3-cell taxonomy
rules_tuple: "(no-tashkeel, orthographic-token, root-frq via QAC v0.4, Hafs-Kufan, Mashriqi)"
script: surahs/Q025-al-furqan/scripts/Q025_F_02_furqan_distinctness.py
output_json: surahs/Q025-al-furqan/csv/Q025-F-02.json
---

# Q025-F-02 — Furqān-vocabulary specificity (pre-reg)

## Hypothesis

The Arabic root √f-r-q has 72 QAC-attested forms in the Quran, of which the noun *furqān* (form `furoqaAn` in QAC) appears exactly 7 times: Q 2:53, Q 2:185, Q 3:4, Q 8:29, Q 8:41, Q 21:48, Q 25:1.

**Pre-committed claim**: Q 25:1 is structurally distinct among the 7 *furqān* attestations. Specifically, it is the UNIQUE attestation in which *al-furqān* functions as the **autonymic title of the very revelation being announced in the surah's opening verse** — that is, the surah declares "Blessed is He who sent down THE-FURQĀN upon His servant" where *al-furqān* refers proleptically to the surah/revelation itself.

The other 6 attestations all couch *al-furqān* in one of three retrospective frames:
- **Mosaic-scripture frame**: *al-furqān* given to Mūsā / Mūsā + Hārūn (Q 2:53; Q 21:48)
- **Quran-as-furqān-among-other-functions frame**: paired with *al-Qurʾān* / *al-hudā* / *al-bayyināt* (Q 2:185, Q 3:4) — *al-furqān* is one of several names/functions of an already-given scripture
- **Moral-discrimination / day-of-victory frame**: instrumental "criterion" or *yawm al-furqān* of Badr (Q 8:29, Q 8:41)

Only Q 25:1 uses *al-furqān* as the **proper-noun-style title-attribution** of the speaking revelation.

## Three test cells

**Cell A — Position-in-surah uniqueness**: Q 25:1 is the only *furqān* attestation appearing in verse 1 of any surah. Direction-locked: 1/7 = unique.

**Cell B — Subject-of-*nazzala* uniqueness**: Q 25:1 is the only *furqān* attestation appearing as the direct object of the verb *nazzala* (form II "to send down repeatedly") with the speaking revelation as direct object. The other Q-2:185 and Q-3:4 use *anzala* (form IV); Q-21:48 uses *ātaynā* (form IV "we gave"); Q-2:53 uses *ātaynā*; Q-8:29 uses *yajʿalu* (general); Q-8:41 uses *anzalnā*. Direction-locked: 1/7 = unique.

**Cell C — Direct-mention of *ʿabdihi* (His servant) co-occurrence**: Q 25:1 uniquely co-occurs *al-furqān* + *ʿabdihi* (the Prophet) + *al-ʿālamīn* (the worlds) in a single verse of titular announcement. Other attestations lack the *ʿabdihi*-anchored indirect-reference-to-Muḥammad construction. Direction-locked: 1/7 = unique.

## Bonferroni accounting

k = 3 cells. α_bon = 0.05 / 3 = 0.01666. All three are descriptive-binary cells, not permutation-null cells; the test is whether all 3 verify or any fail.

## Acceptance / failure

- 3/3 cells verify ⇒ **DESCRIPTIVE-CONFIRMED**: Q 25:1's autonymic title-use of *al-furqān* is structurally unique among the 7 corpus attestations.
- 2/3 ⇒ **DIRECTIONAL**.
- ≤1/3 ⇒ **NULL** (Q 25:1 is not architecturally distinct).

## Direction is locked

Direction: Q 25:1 is unique. Falsification: any other attestation matches all three Cell criteria simultaneously.

## Garden-of-forking-paths log

- The 7-attestation family is exhaustively defined by QAC v0.4 lemma `furoqaAn`. No cherry-picking.
- Cells A, B, C are pre-registered before consulting any tafsir. The verbs *nazzala / anzala / ātaynā / yajʿalu* are read directly from the verse texts.
- This is descriptive uniqueness (not inferential significance); no permutation null is computed because the population (n=7) is exhaustively enumerable.

## Files

- Pre-reg: `surahs/Q025-al-furqan/Q025-F-02-furqan-vocabulary-specificity-prereg.md`
- Script: `surahs/Q025-al-furqan/scripts/Q025_F_02_furqan_distinctness.py`
- Output: `surahs/Q025-al-furqan/csv/Q025-F-02.json`

*PRE-REG LOCKED 2026-05-07.*
