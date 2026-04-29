---
surah: 9
file_type: journal
date: 2026-04-28
phase: B+
---

# Q 9 al-Tawba — Investigation Journal

## 2026-04-28 — Comprehensive single-agent build of all 7 template files

### Specialist agent
Single-agent comprehensive investigation, dispatched per `/Users/grey/Downloads/quran/HANDOFF/NEXT-AGENT-PROMPT` Q 9 task spec.

### Pre-flight reading completed
- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` (full)
- `/Users/grey/Downloads/quran/KNOWLEDGE-GRAPH.md` (root section)
- `surahs/Q009-al-tawba/00-overview.md` (existing scaffold)

### Run sequence

#### 17:18 — Tafsir extraction (Q9 chapters from OpenITI raw files)
- Built `scripts/extract_q9_tafsir.py` to extract Q9 commentary from 10 OpenITI raw tafsirs.
- Header conventions varied — added biqāʿī-style `# (سورة التوبة)` and ṭabarsī-style `# سورة التوبة` patterns.
- 9 Q9-extracted files written to `data/literature/classical-tafsir/raw/{tafsir}-openiti-Q009.txt`:
  - tabari (10994 lines), qurṭubī (5759), rāzī (8284), suyuti-durr (6383), zamakhshari (2148), ibn-kathīr (4052), ṭabarsī (3892), thaʿlabī (3511), biqāʿī (4885), suyūṭī-itqān keyword-context (684 lines).

#### 17:19 — Hadith citations index built
- Built `scripts/build_q9_hadith_citations.py` to scan AhmedBaset 9-books JSON for Q9 keywords.
- Scanned: bukhari, muslim, tirmidhi, abudawud, nasai, ibnmajah, malik, ahmed (8 of 9; darimi not in this dataset).
- 249 Q9 hits across 8 books written to `/Users/grey/Downloads/quran/data/literature/hadith/Q009-citations.md`.
- Hits per book: Bukhari 73, Nasāʾī 44, Muslim 43, Abū Dāwūd 33, Mālik 24, Tirmidhī 16, Ibn Mājah 12, Aḥmad 4 (Aḥmad full-Musnad indexing AWAITING).

#### 17:21 — Pre-registration of 4 novel findings
Pre-reg files written, SHA256 computed and embedded:

| Finding | Pre-reg SHA256 |
|:--|:--|
| Q009-F-01 (mercy density) | `edb931a1294429b216bd18332d59c4c42189cda6bc2d09a192e5ce403b01ec62` |
| Q009-F-02 (hypocrite density) | `980b8caa77bf0778318aa51bb09250c1780adaeb313fef5c9e59bba3d4a83b40` |
| Q009-F-03 (Q9-Q10 boundary) | `a3f04af0f84584cbda89a983e5ad1bb30f4b825ce2e9a435c4d6ec1140ad4842` |
| Q009-F-04 (last-revealed verse) | `f489aa91c6810e7cf19ac634330e949118c41be0634a1ab390b9ab512fbda6bd` |

Bonferroni correction: family k=5; α_corrected = 0.01.

#### 17:22 — Computation runs (all SHA-verified)

##### Q009-F-01 + F-02: density audit
- Script: `/Users/grey/Downloads/quran/scripts/Q009_F_01_02_density.py`
- Source data: `quran-no-tashkeel.json` + `data/morphology/root-index.json` (QAC v0.4)
- Results: `csv/Q009-F-01-02-density-results.json`

Q009-F-01 result:
- Q 9 r-ḥ-m density: 4.86/1k tokens, rank **24/114** (top-quartile)
- Pre-committed direction was rank ≥ 87 (low density). **VIOLATION**: rank ≤ 28.
- Verdict: **FALSIFICATION of classical Position-5 (no-mercy → no-basmala)**.
- Honest publication per protocol §1.3.

Q009-F-02 result:
- Q 9 n-f-q density: 7.85/1k tokens, rank **5/114**.
- Pre-committed threshold rank ≤ 12: **MET**.
- Differential nfq vs. kfr: −12 (Q 9 more distinctively hypocritic than disbeliever-distinctive).
- Verdict: **VINDICATED — al-Faḍiḥa naming empirically grounded**.

##### Q009-F-03: Q9-Q10 boundary
- Script: `/Users/grey/Downloads/quran/scripts/Q009_F_03_q9_q10_boundary.py`
- Source: `findings/phase-b-hypotheses/csv/h-new-720.json`
- Q 9-Q 10 fraction_residual: **3.73%, rank 4/113**.
- Q 6-Q 7 control (muqaṭṭaʿāt-introduction): 0.00%, rank 103/113. Falsifies muqaṭṭaʿāt-as-driver.
- Verdict: **VINDICATED**.

##### Q009-F-04: last-revealed citation density
- Script: `/Users/grey/Downloads/quran/scripts/Q009_F_04_last_revealed.py`
- Scanned 10 OpenITI tafsirs for "آخر ما نزل/آية/سورة" + rival-claim co-occurrence.
- Q 9:128-129: 64; Q 2:281: 61; Q 4:176: 49; Q 5:3: 9.
- Q 9 leads but ratio 64/61=1.05 below pre-committed 1.10× threshold.
- Verdict: **NULL — al-Bayhaqī's harmonization upheld**.

#### 17:35 — All 7 template files written

- `01-empirical-profile.md` — full integration of UAS, outlier-strength, iʿjāz signature, adjacency costs, density profile.
- `02-content-analysis.md` — verse-by-verse covering 129 verses across 8 thematic blocks.
- `03-tafsir-survey.md` — survey of 8 mufassirūn (Ṭabarī, Zamakhsharī, Rāzī, Qurṭubī, Ibn Kathīr, Biqāʿī, Suyūṭī, Suyūṭī-Itqān, Ṭabarsī, Thaʿlabī).
- `04-hadith-corpus.md` — 12 sections covering al-Tirmidhī #3170 (no-basmala), al-Bukhārī #4674 (al-Faḍiḥa), #4222 (Tabuk-deputy), #4224 (Kaʿb b. Mālik), #4986 (Q9:128 collection), Q9-tafsir hadiths.
- `05-classical-claims-audit.md` — 8 audits: 3 VINDICATED (al-Faḍiḥa, Q 9-Q 10 boundary, al-sabʿ al-ṭiwāl outlier), 2 FALSIFIED (Q 8-Q 9 unity, no-mercy → no-basmala), 1 NULL (last-revealed dominance), 1 NOT-TESTABLE (lost-opening), 1 NOT-TESTABLE (Tawrāt/Injīl reference).
- `06-novel-findings.md` — 4 pre-registered novel findings (F-01 to F-04).
- `07-cross-references.md` — neighbours, cluster membership, dual-iʿjāz typology, H-NEW backlinks.

### Headline findings

1. **Q 9 mercy-vocabulary density rank 24/114** (above corpus mean) — **classical "no-mercy → no-basmala" position FALSIFIED**.
2. **Q 9 hypocrisy density rank 5/114** — al-Faḍiḥa naming VINDICATED (pre-registered).
3. **Q 9 → Q 10 canonical-adjacency cost is rank 4/113** most expensive in mushaf; muqaṭṭaʿāt-driver hypothesis FALSIFIED by Q 6-Q 7 control. Q 9-Q 10 is plausibly chronology-driven.
4. **Q 9:128-129 last-revealed citation count = 64** vs. Q 2:281 = 61 — directionally correct but below 1.10× threshold; al-Bayhaqī's harmonization upheld.

### Garden-of-forking-paths log

- Pre-reg F-04: I considered using only the 7 OpenITI tafsirs (excluding Suyūṭī-Itqān, Ṭabarsī, Thaʿlabī). I extended to 10 because all 10 are valid classical-tafsir sources. This *strengthens* the test (more data) and was decided BEFORE running.
- F-03: I added Q 6-Q 7 as a *control* test (muqaṭṭaʿāt cluster onset is also Q 7-المص). This was added AT pre-reg time, not post-hoc. The control's verdict (cheap, rank 103/113) was unforeseen but confirms the chronology-driver thesis.
- F-01: The 1.10× margin for F-04's threshold was set to require **clear dominance**. With a softer 1.05× threshold the result would be VINDICATED. We deliberately chose the stricter threshold to avoid false-positives.
- Q 8-Q 9 unity test (Audit 1): re-used H-NEW-890 T1 result rather than recomputing (same data, same rules-tuple).
- The "chronology-driver" interpretation of Q 9-Q 10 cost (Audit 7) is post-hoc but documented as a hypothesis for future testing.

### Honest limits documented
- Sunan al-Dārimī missing from the AhmedBaset 9-books JSON; full Aḥmad Musnad citations also undercounted.
- F-01's mercy-density test uses QAC roots; it doesn't decompose to the *target* of mercy (which might be narrower for Q 9 than corpus).
- F-04 used a fixed 8-line context window; results are mildly window-size dependent.

### Files produced

```
/Users/grey/Downloads/quran/surahs/Q009-al-tawba/
├── 00-overview.md
├── 01-empirical-profile.md
├── 02-content-analysis.md
├── 03-tafsir-survey.md
├── 04-hadith-corpus.md
├── 05-classical-claims-audit.md
├── 06-novel-findings.md
├── 07-cross-references.md
├── JOURNAL.md
├── Q009-F-01-mercy-density-prereg.md
├── Q009-F-02-hypocrite-density-prereg.md
├── Q009-F-03-q9-q10-boundary-prereg.md
├── Q009-F-04-last-revealed-prereg.md
├── csv/
│   ├── Q009-F-01-02-density-results.json
│   ├── Q009-F-03-q9-q10-boundary.json
│   └── Q009-F-04-last-revealed.json
└── scripts/
    ├── extract_q9_tafsir.py
    └── build_q9_hadith_citations.py

/Users/grey/Downloads/quran/scripts/
├── Q009_F_01_02_density.py
├── Q009_F_03_q9_q10_boundary.py
└── Q009_F_04_last_revealed.py

/Users/grey/Downloads/quran/data/literature/hadith/
└── Q009-citations.md (auto-built, 249 ḥadīth)

/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/
├── ibn-kathir-openiti-Q009.txt
├── tabari-openiti-Q009.txt
├── qurtubi-openiti-Q009.txt
├── razi-openiti-Q009.txt
├── biqai-openiti-Q009.txt
├── suyuti-durr-openiti-Q009.txt
├── suyuti-itqan-openiti-Q009.txt (keyword-context excerpt)
├── tabarsi-openiti-Q009.txt
├── thaclabi-openiti-Q009.txt
└── zamakhshari-openiti-Q009.txt
```

### Quality-gate verification

- [x] Pre-reg SHA matches embedded in run scripts (4× verified at runtime).
- [x] Direction-of-effect locked before running (4× pre-reg files).
- [x] Bonferroni correction applied (k=5, α_bon=0.01).
- [x] Replication: F-01 cross-checked against regex-search; F-02 differential cross-check vs. kfr.
- [x] Honest limits sections written in every file.
- [x] Cross-references include FALSIFICATIONS as well as VINDICATIONS.
- [x] Classical citations are scholar+work+passage everywhere.
- [x] Final statements are intellectually honest (FALSIFIED reported with full prominence, NULL reported as NULL not "marginal vindication").

*Bismillāhi al-Raḥmāni al-Raḥīm.*
