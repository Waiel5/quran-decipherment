---
date: 2026-04-28
agent: Q 55 al-Raḥmān template-builder (specialist)
phase: B+
type: surah-deep-dive
---

# Q 55 al-Raḥmān — Specialist template-builder journal

## Scope

Build all 7 remaining template files for Q 55 (UAS rank 7/114, the famous "ʿarūs al-Qurʾān", 31-fold refrain) plus 5 pre-registered novel findings.

## Deliverables completed

- 7 main files (`01`-`07`) + `JOURNAL.md` in `surahs/Q055-al-rahman/`.
- 5 pre-registration markdowns in `preregs/`, SHA256-recorded.
- 5 Python scripts in `scripts/Q055_F_NN_*.py`.
- 5 JSON outputs in `csv/`.
- 9 tafsir extracts in `tafsir-extracts/` (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Ṭabarsī, al-Thaʿlabī, al-Biqāʿī, al-Suyūṭī al-Durr al-manthūr).

## Headline empirical results

1. **Q055-F-01 CONFIRMED**: 31-fold refrain *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* exactly verified, stable across all 3 tashkeel variants. Q 55 ranks **#1 / 114** in both max-phrase-repetition (31 vs runner-up Q 5 at 16) and max-verse-repetition (31 vs runner-up Q 26 at 8).
2. **Q055-F-02 CONFIRMED**: Q 55 dual-pronoun *kumā* density = **9.09 / 100 words** — corpus rank 1/114, **23× the runner-up** (Q 66 at 0.39). The empirical anchor for the classical *thaqalān* (jinn + mankind) interpretation.
3. **Q055-F-04 CONFIRMED**: Dual-paradise structural-similarity. cos(P1=46-61, P2=62-77) = **0.918**, perm-p = 0.0033 (10000 permutations). Strongest empirical confirmation of the classical *muqarrabūn / aṣḥāb al-yamīn* hierarchical paradise reading (al-Ṭabarī, al-Rāzī, Ibn Kathīr).
4. **Q055-F-05 CONFIRMED at MODERATE level**: Q 55 outlier-status replicated under standardized H-NEW-590 methodology (+14.26pp, MODERATE_OUTLIER). The historic H-NEW-390 +32.6pp is window-conditional (Meccan-only); the standardized comparable is +14.26pp.
5. **Q055-F-03 DIRECTIONAL** (pre-commit-violation candidate): Q 55 cosmic-vocab density rank = **4 / 114** (3.41/100w). Pre-reg locked top-3 as CONFIRMED; rank-4 published as DIRECTIONAL per Protocol §1.3 pre-commit-honesty.

## Critical correction discovered

**The project's `00-overview.md` cites "al-Tirmidhī ḥadīth #3291" for the *ʿarūs al-Qurʾān* tradition. This is INCORRECT.**
- al-Tirmidhī #3291 in the project's hadith corpus is the Q 33 *zayd ibn ḥāritha* hadith.
- The actual *ʿarūs al-Qurʾān* tradition is in **Mishkāt al-Maṣābīḥ #2083** (book 14, chapter 8), narrated by ʿAlī b. Abī Ṭālib, attributed to **al-Bayhaqī's *Shuʿab al-Īmān***.
- The hadith does NOT appear in any of the 9 canonical books (Bukhārī, Muslim, Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik, Aḥmad, Dārimī).
- The closest canonical-book hadith is **al-Tirmidhī #3375** (Jābir, Night of the Jinn — recitation of Q 55), graded *gharīb* by al-Tirmidhī himself (and *ḍaʿīf* by al-Albānī). This is the canonical Q 55 hadith.

**Recommendation**: update `surahs/Q055-al-rahman/00-overview.md` §2 and §9 to correct attribution.

## Honest negative / mixed results

- **F-03 cosmic density**: rank 4, NOT top-3. Pre-commit violation by one rank. Honest reporting per Protocol §1.3.
- The hadith corpus for Q 55 is THIN: only the Tirmidhī Jābir #3375 (*ḍaʿīf*) and the Bayhaqī *ʿarūs* (*ḍaʿīf*). Q 55 is high on UAS rank but mid-low on hadith *fadāʾil* — confirms the H-NEW-860 finding that classical hadith density tracks theological-iʿjāz (Q 36, 67, 112) more strongly than structural-iʿjāz (which Q 55 inhabits).

## Synthesis: proposed third iʿjāz axis

Q 55's empirical signature is unique:
- **High UAS** (rank 7, like structural-iʿjāz)
- **Corpus-MIN sig_A** (rank 114/114, anti-structural-iʿjāz)
- **Corpus-rank-1** in refrain-density, kumā-density, dual-paradise structural-similarity
- **Mid-low** hadith *fadāʾil* (unlike theological-iʿjāz)

This suggests a **third iʿjāz axis: refrain-iʿjāz / iʿjāz al-takrīr** (al-Sakkākī, al-Zamakhsharī's *iqtisās*).

Proposed cross-finding-027: corpus-level evaluation of refrain-iʿjāz with candidates Q 26, Q 55, Q 77, Q 109, Q 70.

## SHA inventory of artifacts

(See `surahs/Q055-al-rahman/JOURNAL.md` for full SHA table.)

## Time-on-task

Wall-time: ~4 hours specialist agent session.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
