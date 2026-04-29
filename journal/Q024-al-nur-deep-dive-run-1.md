---
date: 2026-04-28
agent: Q024-al-nur deep-dive specialist
status: COMPLETE
---

# Q024 al-Nūr deep-dive — run 1 (2026-04-28)

## Task

Build all 7 remaining template files for Q 24 al-Nūr (UAS rank 5 / 114, Medinan-legal centerpiece, contains āyat al-nūr Q 24:35).

## Files produced

All under `/Users/grey/Downloads/quran/surahs/Q024-al-nur/`:
- 01-empirical-profile.md
- 02-content-analysis.md
- 03-tafsir-survey.md
- 04-hadith-corpus.md
- 05-classical-claims-audit.md
- 06-novel-findings.md
- 07-cross-references.md
- JOURNAL.md
- preregs/Q024-F-{01,02,03,04}-*-prereg.md (4 files)
- scripts/Q024_F_{01,02,03,04}_*.py (4 files)
- csv/Q024-F-{01,02,03,04}.json (4 files)

## Key findings

### Empirical (from H-NEW data)

- UAS rank 5 / 114 (UAS = 4.4501).
- Outlier-strength rank 3 / 114 (Δ = +23.51 pp).
- Q 24-Q 25 canonical-adjacency cost rank 5 / 113.
- Q 23-Q 24 cost rank 11 / 113.
- Q 24 has BOTH adjacencies in top-15 expensive — only Q 33 shares this property.
- sig_A rank 82 / 114 (anti-structural-iʿjāz despite top-5 UAS).
- Mean FR distance to corpus 1.0704 (rank 105 / 114, far from corpus).
- Nearest FR neighbours: Q 49, Q 64, Q 2, Q 4, Q 5 (Medinan-legal cluster).
- Farthest: Q 55 al-Raḥmān (FR = 1.4264).

### 4 Pre-registered novel tests (all CONFIRMED)

- **Q024-F-01 light-vocabulary density**: VINDICATED at p < 10⁻⁶ Bonferroni-corrected; 27 light-tokens vs 8.80 expected; rank 2 / 114 by raw count, rank 7 / 114 by density. Discriminating control on Q 33 al-Aḥzāb (4 vs 9 expected, p=0.98) confirms test discriminates correctly.
- **Q024-F-02 Light-verse vs Throne-verse**: CONFIRMED on both directions. Q 24:35 has 21 light-tokens; Q 2:255 has 0. Q 24:35 at word-ratio 0.489 (centerpiece); Q 2:255 at word-ratio 0.845 (last-quarter). Q 24:35 has 4 Allāh-tokens / Q 2:255 has 2; Q 2:255 has 6 divine-attribute roots / Q 24:35 has 1.
- **Q024-F-03 al-ifk cohesion + Q 24:35 midpoint**: CONFIRMED on both. al-ifk Q 24:11-20 at 81.5th percentile cohesion; Q 24:35 contains both word-median and letter-median of Q 24.
- **Q024-F-04 hijab passages comparison**: CONFIRMED on all three directions. Root-Jaccard Q 24:30-31 ↔ Q 33:53-59 = 0.153; *xmr* (khimār) only in Q 24; *Ḥjb* (ḥijāb) only in Q 33.

### 8 Classical claims audited

| Audit | Verdict |
|:--|:--|
| 1. al-Qurṭubī's *maqṣūd* = chastity-and-covering | VINDICATED |
| 2. al-Bāqillānī *iʿjāz al-fawāṣil* | FALSIFIED locally / VINDICATED globally |
| 3. al-Ṭabarsī Q 24-named-for-light-density | VINDICATED p < 10⁻⁶ |
| 4. "Two parallel hijab passages" | FALSIFIED (re. symmetry); VINDICATED (re. lexical-distinction) |
| 5. al-ifk Q 24:11-20 coherent unit | VINDICATED |
| 6. Q 24:35 structural midpoint | VINDICATED |
| 7. Q 24:55 unique community-istikhlāf | VINDICATED |
| 8. al-Thaʿlabī's classical letter/word counts | VINDICATED 1.3% / 0.2% precision |

### Surprising findings

1. The Light-verse predicate "Anta nūru al-samāwāti wa-l-arḍ" appears in the canonical Prophetic **Tahajjud-dhikr in all 9 hadith books** (Bukhārī #1088, Muslim #1700, etc.) — Q 24:35's opening words are liturgically embedded in daily prayer practice. Post-hoc descriptive observation.
2. Q 24:35 is **rank 1 / 6,236 by light-cluster root count** with 21 tokens — and the next-highest verse has only 6 tokens, a 3.5× gap.
3. The home-entry+hijab block (vv. 27-31) is at **95.3rd percentile cohesion** vs the al-ifk passage at 81.5th — the most-cohesive Q 24 passage is NOT the famous one.
4. **Q 24 and Q 33 are the only two surahs with BOTH adjacencies in top-15 expensive** — they are structural twins by mushaf-position but lexically opposite (Q 24 light-rich, Q 33 light-depleted; Q 24 anti-sig_A, Q 33 highest-sig_A).
5. Q 24:35 (Light-verse) is at word-ratio 0.489 of Q 24 (centerpiece), but **Q 2:255 (Throne-verse) is at word-ratio 0.845 of Q 2** (late-third-quarter). The two great verses occupy structurally different positions — only Q 24:35 is a literal centerpiece.

## Verdict

INVESTIGATION COMPLETE. All 8 template files written. 4 pre-registered novel tests CONFIRMED. 8 classical claims audited (6 VINDICATED, 2 FALSIFIED-with-refinement). All findings cross-referenced into KNOWLEDGE-GRAPH and ready for handoff.
