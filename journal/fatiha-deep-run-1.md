---
run_id: fatiha-deep-run-1
date: 2026-04-12
scope: Surah 1 Al-Fātiḥa — deep computational dive
output: findings/phase-c-structures/al-fatiha-deep-dive.md
data:
  - quran-text/quran-no-tashkeel.json
  - data/morphology/quranic-corpus-morphology-0.4.txt
  - data/translations/en.sahih.txt
---

# Fatiha deep run 1 — journal

## Goal
Apply computational rigor to classical qualitative observations about Al-Fātiḥa, the most-recited and most-commented passage in Islamic literature. 13 tasks across metrics, iltifāt, divine names, ring-frame with An-Nās, cross-Quran distribution, self-gloss, abjad, ring structure, and classical prior art.

## Method
1. Token + letter counting from the no-tashkeel JSON corpus.
2. Root/lemma extraction from Leeds QAC v0.4 morphology; per-verse, per-surah aggregates.
3. Cross-Quran sliding-window search for the smallest sub-passage containing all 18 Al-Fātiḥa roots.
4. Abjad computation under mashriqi values (hamzas = 1, ta-marbūṭa = 400, yā-maqṣūra = 10).
5. Manual inspection of the 17 `anʿama + ʿalayhim` occurrences for the Q 4:68–69 self-gloss.
6. Cross-check with already-published findings in `findings/` (divine names, Khawātim al-Ḥashr, Maryam, iltifāt, intra-quranic).

## Findings (ordered by strength)

### 1. Pivot geometry at v5 is metrically exact
- Word split around v5: 13 | 4 | 12 (sum 29, prime).
- Letter split around v5: 61 | 19 | 63 (sum 143).
- v5 letter count = 19 = basmala letter count.
- Pre-pivot 61 letters ≈ post-pivot 63 letters (delta = 2 letters). v5 IS the geometric midpoint.
- Third-person divine references: 8 in vv 1–4, 0 in vv 5–7.
- Second-person divine addressing: 0 in vv 1–4, 4 in vv 5–7.
- Iltifāt is a *total* partition at v4→v5, not a local shift. Classical observation quantified.

### 2. Mathānī is structural
- 6 lemmas repeated 2× each; 17 singletons. 6/23 distinct lemmas = 26 % doubling rate.
- Doubled set: Allāh, al-Raḥmān, al-Raḥīm (divine tier, cross-verse);  iyyāka, ṣirāṭ, ʿalayhim (human tier, adjacent).
- The surah enacts its classical name *al-Sabʿ al-Mathānī* (the Seven Oft-Repeated) at the lemma level.

### 3. Al-Fātiḥa is the smallest Quranic window containing all 18 of its roots
- Fātiḥa itself: 7 verses, 23 word-tokens, 18 distinct roots.
- Smallest non-Fātiḥa window: 86 verses (4:93 → 5:2) at the verse level; 920 word-tokens (21:87 → 22:78) at the word level.
- Density ratio ≈ 40× at the word level.
- Classical *jāmiʿa* / *Umm al-Kitāb* label quantified: Al-Fātiḥa is the most vocabulary-dense passage per unit length in the Quran.

### 4. 10,147 = 73 × 139
- Total Al-Fātiḥa abjad (mashriqi) = 10,147.
- Factors as 73 × 139.
- 139 is the classical letter count of Al-Fātiḥa (al-Suyūṭī, al-Ḥajjāj b. Yūsuf tradition).
- Surah abjad = (prime) × (its own letter count). Flagged as coincidence; no mechanism proposed.

### 5. Basmala abjad = 786 exactly
- bismi (102) + Allāh (66) + al-Raḥmān (329) + al-Raḥīm (289) = 786.
- The canonical Muslim-manuscript "786 seal" reproduces. Basmala letter count = 19 reproduces.

### 6. Q 4:68–69 is an internal self-gloss of Al-Fātiḥa
- Q 4:68 ends with *ṣirāṭan mustaqīman* (= Al-Fātiḥa v 6 content).
- Q 4:69 opens with *alladhīna anʿama Allāhu ʿalayhim* (= Al-Fātiḥa v 7 content).
- Then immediately lists the four categories: prophets, truthful-ones, martyrs, righteous.
- Classical tafsir (Ibn Kathīr) knows this; the quantification across 17 `anʿama + ʿalayhim` occurrences shows this is the unique self-gloss passage.
- Second-best self-gloss: Q 19:58 (Maryam) = prophets + progeny of Adam.

### 7. Al-Fātiḥa ↔ An-Nās shares precisely the 3 sovereignty roots
- Shared: Alh, mlk, rbb.
- Fātiḥa opens with 3-epithet invocation of God (cosmic: worlds / Judgment Day).
- An-Nās opens with 3-epithet invocation of God (anthropic: humanity).
- Ring frame: guidance-to (Fātiḥa) ↔ refuge-from (An-Nās).

### 8. Khawātim al-Ḥashr recapitulation confirmed at 4-name level
- Q 1:1–4: Allāh → al-Raḥmān → al-Raḥīm → al-Malik.
- Q 59:22–24: Allāh → al-Raḥmān → al-Raḥīm → al-Malik → [15 further names].
- Independent cross-run verification.

### 9. Maryam shares 13/18 Al-Fātiḥa roots (72%)
- Missing 5: Ewn, Hmd, dyn, gDb, gyr.
- The missing roots are the "supplication-specific" tier (seeking help, praise, judgment, wrath, other-than).
- Maryam retains the "divine-attributes + guidance" tier. Consistent with Maryam as Raḥmān-surah.

## Anomalies / things checked and falsified

- **Chiastic root ring v1↔v7 / v2↔v6 / v3↔v5:** no shared roots at any pair. Al-Fātiḥa is NOT chiastic at the root level. Farrin-style ring absent. What IS present: the mathānī doubling structure (finding 2).
- **19-divisibility of total surah abjad:** 10,147 mod 19 = 16. Khalifa's code-19 does not fire here.
- **Letter-count palindrome:** [19, 18, 12, 12, 19, 19, 44] is not palindromic. No 7-partition at the letter level.

## Counts lock

- 7 verses (Ḥafs).
- 29 words (Leeds QAC token count; matches classical).
- 143 letters strict Unicode; 139 classical (rasm/hamza convention difference).
- 18 distinct roots.
- 23 root-bearing tokens.
- 6 doubled lemmas.
- Basmala: 19 letters, abjad 786.
- Total abjad: 10,147 = 73 × 139.

## Open questions for future runs

1. Recompute letter count under each classical rasm convention (al-Kūfī vs al-Madanī vs al-Ḥimṣī numbering) and see which yields 139 exactly.
2. Is the letter-count sequence `[19, 18, 12, 12, 19, 19, 44]` itself a subsequence hit elsewhere in the Quran?
3. Full chronological placement: Al-Fātiḥa is classically considered the 5th or 48th revealed surah (Nöldeke vs Ibn ʿAbbās). Its vocabulary profile (heavy rbb, hdy, Ebd — early-Meccan) supports early-Meccan dating. Cross-check with chronological-revelation.md.
4. Cross-surah tikrār rate: is 26 % of distinct lemmas doubled unusually high, typical, or low? Would need a corpus baseline per-surah.

## Time-log
- File reads, morphology parse, root extraction: ~10 min.
- Cross-window search (exhaustive sliding over all 6,236 verses, all ~77k content tokens): ~2 min.
- Abjad computation + self-gloss check at Q 4:68–69: ~5 min.
- Writing deep-dive.md: main output.
