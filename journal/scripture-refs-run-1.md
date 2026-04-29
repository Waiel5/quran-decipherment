---
run_id: scripture-refs-run-1
phase: B
date: 2026-04-12
agent: Phase B deep agent — prior-scripture references
inputs:
  - /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/quranic-self-reference.md
  - /Users/grey/Downloads/quran/quran-text/quran-flat-min-tashkeel.txt
output: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/scripture-refs.md
---

# Journal — scripture references run 1

## Method
- Source of truth for token counts: Kais Dukes morphology v0.4 (Buckwalter) grepped by lemma.
- Buckwalter lemma mapping used:
  - Tawrāh → `LEM:t~aworaY`p`  (PN, ROOT not specified in morphology because it is a non-Arabic proper name; corpus does not assign it an Arabic triliteral root).
  - Injīl → `LEM:<injiyl` (PN, no Arabic root assigned).
  - Zabūr → `LEM:zabuwr` (PN, ROOT:zbr).
  - ṣuḥuf → `LEM:SuHuf` (N, FP, ROOT:SHf).
  - muṣaddiq → `LEM:muSad~iq` (active participle form II, ROOT:Sdq).
  - muhaymin → `LEM:muhayomin` (active participle form II, ROOT:hmn).
  - yuḥarrif → `LEM:yuHar~ifu` (V, form II, ROOT:Hrf).
  - furqān → `LEM:furoqaAn` (N, ROOT:frq).
  - ahl al-dhikr → `LEM:>ahol` + `LEM:*ikor` (collocational search of the phrase).

## Counts verified
- Tawrāh: 18 PN tokens — 3:3, 3:48, 3:50, 3:65, 3:93, 3:93, 5:43, 5:44, 5:46, 5:46, 5:66, 5:68, 5:110, 7:157, 9:111, 48:29, 61:6, 62:5. (Matches the hypothesis of 18×.)
- Injīl: 12 PN tokens — 3:3, 3:48, 3:65, 5:46, 5:47, 5:66, 5:68, 5:110, 7:157, 9:111, 48:29, 57:27. (Matches hypothesis of 12×.)
- Zabūr: 3 PN tokens — 4:163, 17:55, 21:105. (Matches hypothesis.)
- ṣuḥuf (plural): 8 tokens — 20:133, 53:36, 74:52, 80:13, 81:10, 87:18, 87:19, 98:2. Of these four specifically name the "scrolls of Abraham and Moses" or "scrolls of Moses": 20:133, 53:36 (+37 Mūsā), 87:18, 87:19.
- muhaymin: 2 tokens only — 5:48 (of the Quran) and 59:23 (of Allāh).
- muṣaddiq / muṣaddiqan: 19 tokens across the morphology; the revelation-to-revelation usage dominates (2:41, 2:89, 2:91, 2:97, 2:101, 3:3, 3:50, 3:81, 4:47, 5:46 ×2, 5:48, 6:92, 35:31, 37:52, 46:12, 46:30, 61:6; plus 3:39 John confirming Jesus).
- yuḥarrifūn (form II of ḥrf): 4 tokens — 2:75, 4:46, 5:13, 5:41.
- furqān: 7 tokens / 6 verses (2:53, 2:185, 3:4, 8:29, 8:41, 21:48, 25:1). The Mūsā-Hārūn usage (Q 2:53 + 21:48) is the critical point for §7.
- ahl al-dhikr: phrase occurs 2× — Q 16:43, Q 21:7. Both in near-identical formulas "fa-sʾalū ahla l-dhikri in kuntum lā taʿlamūn."

## Cross-reference check
- The 18 Tawrāh tokens cluster in three surahs: Āl ʿImrān (5×), al-Māʾidah (7×), remainder scattered (al-Aʿrāf 1, al-Tawbah 1, al-Fatḥ 1, al-Ṣaff 1, al-Jumuʿah 1).
- Injīl's 12 tokens cluster identically: Āl ʿImrān (3×), al-Māʾidah (5×), al-Aʿrāf 1, al-Tawbah 1, al-Fatḥ 1, al-Ḥadīd 1. The distribution of Torah and Gospel is correlated because they are frequently named as a paired dyad ("the Torah and the Gospel") or triad ("the Torah, the Gospel, and the Furqān/Qurʾān").

## Notes
- The Q 21:48 al-furqān reference is a genuine dual-assignment: the word is also the self-name of the Quran (Q 25:1). The Mosaic attestation demonstrates al-furqān is a scriptural category, not a proper name unique to the Quran.
- The tahrīf verbs all use form II (yuḥarrifūn), never form I. Form II intensification is semantically marked: "they bend/twist" rather than "they change."
- Psalm 37:29 as antecedent for Q 21:105's "al-arḍa yarithuhā ʿibādiya l-ṣāliḥūn" is a textual claim (explicit in the Quran: "fī l-zabūri min baʿdi l-dhikri"). Verified that Psalm 37:29 reads "the righteous shall inherit the land" — a near-verbatim match.

## Output
- findings/phase-b-hypotheses/scripture-refs.md (~3000 words) written.
- 400-word summary returned to caller.
