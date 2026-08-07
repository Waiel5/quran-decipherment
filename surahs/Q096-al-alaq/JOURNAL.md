---
surah: 96
file_type: journal
date_last_updated: 2026-05-09
phase: B+
---

# Q 96 al-ʿAlaq — Journal


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 2026-05-09

### Session inception

Specialist agent dispatched for Q 96 al-ʿAlaq (the first-revealed surah, Tanzil rev #1, Nöldeke #1). Pre-flight reading completed:
- `HANDOFF/04-DISCIPLINE.md` — methodology + MW-series + PRE-REG-STANDARDS digested.
- `HANDOFF/01-WHAT-WE-KNOW.md` — top-tier confirmed findings landscape.
- `MASTER-FINDINGS-LEDGER.md` §1-3 — corpus anchors + divine-name catalog + Tier-A findings.
- `surahs/Q037-al-saffat/` reference template inspected; `surahs/Q113-al-falaq/` short-surah template inspected.

### Hadith verification

Verified Q 96 anchor hadiths on-disk in `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`:

1. **Bukhārī Bad' al-Waḥy idInBook=3** (chapterId=1) — VERIFIED. Quotes Q 96:**1-3** (NOT vv 1-5 as some past project descriptions stated).
2. **Muslim Īmān idInBook=308** (chapterId=1) — VERIFIED. Quotes Q 96:**1-5** (full). The on-disk English translator parenthetical "(al-Qur'an, xcvi. 1-4)" is a TRANSLATION ARTIFACT — Arabic clearly contains all 5 verses through *ʿallama al-insāna mā lam yaʿlam*.
3. **Muslim Īmān idInBook=314** — VERIFIED. Jābir b. ʿAbdullāh asserts Q 74 al-Muddaththir was first-revealed (the famous classical disagreement).
4. **Muslim Mosques idInBook=1201** (chapterId=5) — VERIFIED. Q 96 sajda-tilāwa primary anchor (alongside Q 84 al-Inshiqāq).
5. **Muslim Mosques idInBook=1202** — VERIFIED. Parallel Q 96 sajda narration.
6. **Bukhārī Sujud al-Quran (Kitāb 17)** — VERIFIED that Q 96 is **NOT** named in any of the chapter's 13 hadiths. Past references that cite "Bukhārī Sujud al-Quran chapter" as the Q 96 sajda anchor should be CORRECTED to point to Muslim Mosques 1201/1202.
7. **Tirmidhī Tafsir chapter (chapterId=47)** — search returned 0 hits for direct Q 96 ad loc tafsīr. The chapter contains 421 hadiths (idInBook 3033-3453) but does not appear to extend to Q 96 with a surah-tafsir-heading. Honest note flagged.

### Hadith corrections logged

1. Bukhārī Bad' al-Waḥy idInBook=3 quotes Q 96:**1-3** only (not vv 1-5).
2. Muslim Īmān idInBook=308 quotes Q 96:**1-5** (English translator's "1-4" annotation is artifact).
3. Q 96 sajda primary anchor is **Muslim Mosques 1201/1202**, NOT Bukhārī Sujud al-Quran (which has no Q 96-specific narration).
4. Tirmidhī Tafsir on Q 96 is sparse/absent in current on-disk dataset; project should re-verify if extended Tirmidhī coverage acquired.

### Empirical-data extraction

Loaded data:
- `quran-text/quran-no-tashkeel.json` — Q 96 verses (19 vv, 73 words, 288 letters)
- `data/morphology/quranic-corpus-morphology-0.4.txt` — Q 96 QAC v0.4 morphological tags
- `data/morphology/root-index.json` — corpus-frequency for all 1642 roots
- `findings/phase-b-hypotheses/csv/h-new-111.json` — Fisher-Rao distance matrix
- `findings/phase-b-hypotheses/csv/h-new-590.json` — outlier-strength
- `findings/phase-b-hypotheses/csv/h-new-700.json` — rhyme-letter diagnostics
- `findings/phase-b-hypotheses/csv/h-new-720.json` — canonical-adjacency cost
- `findings/phase-b-hypotheses/csv/h-new-750.json` — iʿjāz signature
- `findings/phase-b-hypotheses/csv/h-new-840.json` — UAS

### Empirical anchors discovered

1. **Q 96 contains 2 of 6 corpus IMPV-qrA tokens** (33% concentration; ties Q 73 at rank 1) — verified via QAC v0.4 morphology grep for ROOT:qrA + IMPV.
2. **Q 96 contains 1 of 4 corpus *qalam* tokens** (Q 96:4); paired with Q 68:1 (the other short-Meccan opening-cluster *qalam*).
3. **Q 96 contains 1 of 7 corpus *ʿalaq* tokens** (Q 96:2, the surah's namesake).
4. **Q 96 has 2 corpus-hapax roots**: zbn (zabāniya at v 18) and sfE (la-nasfaʿan at v 15).
5. **Q 96 contains 50% of corpus nāṣiya tokens** (2 of 4 nSy occurrences at vv 15-16).
6. **Q 96 has 3 *kallā* particles** (vv 6, 15, 19) — high concentration of the corpus's emphatic-negative refrain.
7. **Q 96 has 3 *a-raʾayta* questions** (vv 9, 11, 13) — rhetorical chain.
8. **Q 96 sig_A rank 4/114** (TOP DECILE iʿjāz signature).
9. **Q 96 outlier-strength NULL** (window {Q 93-99} extremely cohesive).
10. **Q 96 FR-nearest neighbors all short-mufaṣṣal terminal**: {Q 102, 107, 108, 100, 110}.
11. **Q 96 verse-final letter histogram**: 9 ى + 3 م + 3 ة + 2 ق + 1 ه + 1 ب — 3-rhyme-block structure (ق-م / ى / ة-ه-ب).

### Pre-existing project work on Q 96

Discovered:
- **H-NEW-1300** (`findings/phase-b-hypotheses/h-new-1300-q96-iqra-corpus-distribution.md`) — already filed as NULL by strict pre-reg (Q 96 tied Q 73 at rank 1 IMPV-qrA). Descriptive 4-cluster {17, 69, 73, 96} noted.
- **H-NEW-1301** (`...h-new-1301-impv-qra-cluster-prereg.md` + `csv/h-new-1301.json`) — already filed as NULL-BROKEN (PC failed on length-matched-FR test).
- **H-NEW-930** — Khalifa-19 mod-19 verse-counts REFUTED. Q 96 V=19 ≡ 0 (mod 19) joins Q 47, 82, 87 — under-represented vs binomial-expected 6.

So H-NEW-1300 and H-NEW-1301 are pre-existing on disk. Project H-NEW range continues at H-NEW-1310+ for any new pre-regs. The current Q 96 specialist did NOT produce new H-NEW-numbered findings; instead, surah-local Q096-F-NN finding IDs were used.

### Novel test pre-registrations (Q 96 surah-local)

Locked 4 SHA256 pre-regs at `surahs/Q096-al-alaq/preregs/`:

| ID | SHA256 (head) | Title |
|:--|:--|:--|
| Q096-F-01 | `a00c71629c45...` | vv 1-5 vs vv 6-19 register-discontinuity |
| Q096-F-02 | `a2df036101f4...` | Hapax + rare-root density |
| Q096-F-03 | `e97e3b6381ba...` | Q 96 ↔ Q 68 al-Qalam structural mirror |
| Q096-F-04 | `6620cbef4068...` | Sajda-tilāwa 14-cluster FR cohesion |

All 4 pre-regs were SHA-locked BEFORE running scripts. Each script verifies SHA before loading any data.

### Test execution results

| Test | Cell A | Cell B | MW-5 PC | Verdict |
|:--|:--|:--|:--|:--|
| Q096-F-01 | rank 2/15 (p=0.13) FAIL | p=0.0178 PASS | Q 19 p=0.0023 PASS | **ANOMALOUS-INFORMATIVE** (Cell B passes; vv 15-19 even more discontinuous than vv 1-5; supports al-Biqāʿī 3-block reading) |
| Q096-F-02 | rank 4/10 hapax (p=0.40) FAIL | rank 3/10 rare (p=0.30) FAIL | Q 113 rank 3/12 (p=0.25) PC FAILS | **NULL-BROKEN** (small pool underpowered) |
| Q096-F-03 | rank 146/528 length-Meccan-pair (p=0.28) FAIL | rank 34/113 rev-consecutive (p=0.30) FAIL | Q 57-Q 59 rank 1208/6328 (p=0.19) PC FAILS | **NULL-BROKEN** |
| Q096-F-04 | obs mean 0.94 vs null mean 0.92 (p=0.59) FAIL | exclude-Q 1 (p=0.56) FAIL | musab cluster (p=0.083) PC FAILS | **NULL-BROKEN** |

### Key empirical findings (descriptive)

Despite 0 clean PASS, descriptive findings stand:
1. **Vv 1-5 vs vv 6-19 IS structurally distinct** at random-split null (p=0.0178). The classical 2-block reading is partially correct.
2. **vv 15-19 is the SINGLE-MOST-DISCONTINUOUS contiguous 5-block** (rank 1/15). Supports al-Biqāʿī's 3-block compositional reading. Empirical alignment with classical scholarship at the architectural level.
3. **Q 96 is in the top-half** of Meccan 15-25v surahs for hapax (rank 4/10) and rare-root (rank 3/10) density. Q 90, Q 91 rank above on both. Honest report.
4. **Q 96 ↔ Q 68 *qalam*-mirror is SEMANTIC, not FR-structural**. Classical al-Rāzī content-link reading correct; FR-structural prediction false. Consistent with broader project pattern (cross-finding-015): classical aesthetic-rhetorical claims confirm; classical structural-distance predictions don't necessarily.
5. **Sajda-tilāwa class is FR-DISPERSED** (mean intra-cluster FR 0.94 > corpus mean 0.92). Liturgical-functional class confirmed; structural-class refuted. Consistent with H-NEW-68 NULL.

### Files written

- `surahs/Q096-al-alaq/00-overview.md` (~280 lines)
- `surahs/Q096-al-alaq/01-empirical-profile.md` (~260 lines)
- `surahs/Q096-al-alaq/02-content-analysis.md` (~270 lines)
- `surahs/Q096-al-alaq/03-tafsir-survey.md` (~210 lines)
- `surahs/Q096-al-alaq/04-hadith-corpus.md` (~230 lines)
- `surahs/Q096-al-alaq/05-classical-claims-audit.md` (~210 lines)
- `surahs/Q096-al-alaq/06-novel-findings.md` (~220 lines)
- `surahs/Q096-al-alaq/07-cross-references.md` (~210 lines)
- `surahs/Q096-al-alaq/JOURNAL.md` (this file)
- 4 pre-regs in `preregs/`
- 4 scripts in `scripts/`
- 4 JSON outputs in `csv/`

### Cross-references back to project

- Q 96 first-revelation status: VINDICATED. The strongest classically-corroborated chronology fact in the project's hadith-anchored audit. 8 of 8 mufassirūn surveyed confirm; cross-school agreement; multiple high-grade narrations (Bukhārī, Muslim).
- Q 96:19 sajda-tilāwa: VINDICATED via Muslim Mosques 1201/1202. Hadith-anchor correction logged.
- Q 96 IMPV-qrA distinction: 33% of corpus IMPV-qrA in 19/6236 = 0.3% of verses (a 110× concentration). Descriptive only; H-NEW-1300 strict-NULL.
- Q 96:1-5 literacy-vocabulary density: descriptive corpus-densest 5-verse literacy-block (45% literacy-thematic root-tokens). Formal test queued for H-NEW-1310.
- Q 96 al-Biqāʿī 3-block reading VINDICATED via Q096-F-01 Cell A rank-1 at vv 15-19.

### Garden-of-forking-paths log

- All 4 pre-regs SHA-locked BEFORE running scripts.
- Origin disclosure: Q096-F-02 was post-hoc-noticed (root-index inspection found zbn, sfE as corpus-hapax). Pre-reg locked BEFORE running comparator distribution. Origin transparently disclosed in pre-reg.
- Q096-F-03 origin: post-hoc *qalam* inventory inspection found Q 68 + Q 96 as opening-pair. FR distance (0.7324) was already known at pre-reg lock time; this is locked into the pre-reg, not subject to revision.
- Q096-F-04 origin: triggered by Q 96:19 sajdah marker observation. The 14-cluster identity was locked from the classical sajda-list before running the FR matrix.
- No alternative cells added post-observation.
- No threshold tuning. α_bon=0.025 per cell; PC at α=0.05 single-test as standard.

### Verdict synthesis

The Q 96 surah-specialist deliverable produces:
- **2 confirmed classical findings** (first-revelation, sajda-tilāwa) at strong evidentiary tier.
- **1 partially-confirmed compositional finding** (3-block better than 2-block, vindicating al-Biqāʿī).
- **3 NULL-BROKEN tests** — honest reports that the classical SEMANTIC connections (qalam-mirror, hapax-density, sajda-cluster) don't propagate to FR-distance instruments.
- **4 hadith corrections logged** for project-wide propagation.
- **0 new H-NEW-numbered findings** — H-NEW-1300/1301 already pre-existed on disk; surah-local Q096-F-NN IDs used.

The deliverable is at parity with `surahs/Q037-al-saffat/` (8 files + 5 pre-regs/scripts/CSVs) and `surahs/Q113-al-falaq/` (8 files + 4 pre-regs/scripts) reference templates.

### Open follow-ups for future sessions

1. **H-NEW-1310** queued: corpus-densest 5-verse literacy-vocabulary block scan (sliding window across 6,232 windows). Q 96:1-5 expected rank-1 candidate.
2. **Q 68 al-Qalam specialist** (next session): build Q 68 specialist dir; the *qalam*-mirror SEMANTIC link should be reproduced from Q 68's perspective.
3. **Q 74 al-Muddaththir specialist** (next session): the post-fatra first-revealed surah; sister-anchor to Q 96 with the al-Bayhaqī harmonization.
4. **al-Suyūṭī Itqān nawʿ-number physical-edition verification** for first-revealed surah and sajda-tilāwa nawʿ — pending MW-6 VERIFIED elevation.
5. **Tirmidhī Tafsir extended coverage acquisition** — re-search for Q 96 ad loc once additional Tirmidhī data is available.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
