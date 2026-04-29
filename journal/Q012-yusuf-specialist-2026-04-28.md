---
date: 2026-04-28
agent: Q 12 Yūsuf specialist
phase: B+
type: surah-deep-dive
---

# Q 12 Yūsuf — Specialist run journal

## Scope
Build all 7 remaining template files for Q 12 (UAS rank 6/114, the only continuous-narrative surah, ALR cluster member).

## Deliverables completed
- 7 main files (`01`–`07`), `JOURNAL.md` for the surah.
- 4 pre-registration markdowns, SHA256-locked.
- 4 Python scripts in `scripts/Q012_F_NN_*.py`, all SHA-verifying at runtime.
- 5 JSON outputs in `surahs/Q012-yusuf/csv/`.

## Headline empirical results

1. **Q 12 ranks 1/114 on `frac_narrative_verses`** (67.6%). Empirical correlate of *aḥsan al-qaṣaṣ*. Q012-F-01 CONFIRMED.
2. **Q 12 holds 92.6% of corpus-total يوسف tokens** (25/27). Highest single-surah name-eponym concentration in the Quran. Q012-F-03 CONFIRMED.
3. **The phrase أحسن القصص is a Quranic hapax**, occurring exactly at Q 12:3, cross-validated across 3 tashkeel variants. The root q-s-s in Q 12 frames the surah head-tail (Q 12:3, 5, 111). Q012-F-04 CONFIRMED.
4. **Q 12's content-distance signature places it FR-nearest to Q 7, 27, 28, 21, 11** (prophet-narrative cluster), NOT to its formal ALR siblings Q 10/14/15. The empirical "prophet-narrative cluster" is broader than the formal letter-family cluster.
5. **Q 12's most-distant surah in the entire corpus is Q 55 al-Raḥmān** (FR = 1.4185). The narrative-iʿjāz / theological-iʿjāz orthogonality concretized.
6. **Q 12→Q 13 is the most-expensive seam** in Q 12's adjacency profile (TSP 0.216 length-units, top-15 corpus-wide); Q 11→Q 12 is one of the cheapest (0.035, bottom-cluster). The mushaf accepts the right-seam cost to keep Q 12 in the prophet-narrative ALR cluster.

## Honest negative / mixed results

- Q012-F-02 (per-phase cohesion): only 3/10 phases pass Bonferroni α=0.005; 5 needed for CONFIRMED. **DIRECTIONAL** verdict. Power was concentrated in n ≥ 12 phases.
- Classical claim 3 (minimum narrative-breaks): Q 12 ranks 3/10 not 1/10 in the prophet-narrative comparison set; Q 26 al-Shuʿarāʾ (0 breaks) and Q 19 Maryam (1 break) score lower. **RULES-TUPLE-FRAGILE**. The substantive uniqueness of Q 12 is in **single-protagonist continuous form**, not minimum-break-marker count.
- Classical claim 5 (*shaṭr al-ḥusn*): 0 hits in our 9-books JSON. Tradition is real (al-Nawawī's Sharḥ Muslim) but not in our local archive. **DATA-GAP** flagged.

## Pre-registration discipline
- 4 pre-regs SHA256-locked before running.
- 4 scripts SHA-verify at runtime — runtime SHA matches expected (verified by successful run).
- 0 pre-commit violations.

## Files
- `surahs/Q012-yusuf/00-overview.md` (pre-existing)
- `surahs/Q012-yusuf/01-empirical-profile.md` (new)
- `surahs/Q012-yusuf/02-content-analysis.md` (new)
- `surahs/Q012-yusuf/03-tafsir-survey.md` (new)
- `surahs/Q012-yusuf/04-hadith-corpus.md` (new)
- `surahs/Q012-yusuf/05-classical-claims-audit.md` (new)
- `surahs/Q012-yusuf/06-novel-findings.md` (new)
- `surahs/Q012-yusuf/07-cross-references.md` (new)
- `surahs/Q012-yusuf/JOURNAL.md` (new)
- 4 pre-regs in `surahs/Q012-yusuf/Q012-F-NN-*-prereg.md`
- 5 JSONs in `surahs/Q012-yusuf/csv/`
- 4 scripts in `scripts/Q012_F_NN_*.py`

## Verbatim Q 12:3 (cross-validated 3 tashkeel variants)

- **no-tashkeel**: نحن نقص عليك أحسن القصص بما أوحينا إليك هذا القرآن وإن كنت من قبله لمن الغافلين
- **min-tashkeel**: نَحنُ نَقُصُّ عَلَيكَ أَحسَنَ القَصَصِ بِما أَوحَينا إِلَيكَ هٰذَا القُرءانَ وَإِن كُنتَ مِن قَبلِهِ لَمِنَ الغٰفِلينَ
- **full-tashkeel**: نَحۡنُ نَقُصُّ عَلَيۡكَ أَحۡسَنَ ٱلۡقَصَصِ بِمَآ أَوۡحَيۡنَآ إِلَيۡكَ هَٰذَا ٱلۡقُرۡءَانَ وَإِن كُنتَ مِن قَبۡلِهِۦ لَمِنَ ٱلۡغَٰفِلِينَ

The phrase أحسن القصص is orthographically identical (modulo tashkeel decoration) across all 3 variants and occurs exactly once in the Quran, at Q 12:3.
