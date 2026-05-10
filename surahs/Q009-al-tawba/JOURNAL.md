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

---

## 2026-05-09 — Wave-H specialist extension (3 new pre-registered tests)

### Brief from dispatcher
Add Q 9 specialist deliverables T1 (basmala corpus-exact verification), T2 (Q 8 → Q 9 seam smoothness for al-Biqāʿī thematic-couplet), T3 (Q 9 long-Medinan verse-length signature). Pre-register, SHA-lock, deterministic-count where applicable, honest reporting. Bonferroni family expands from k=5 to k=7 → α_bon = 0.05/7 ≈ 0.00714.

### Run log

```
2026-05-09T22:30:00-05:00  pre-reg-write   Q009-F-05-basmala-corpus-singleton-prereg.md
2026-05-09T22:30:01-05:00  pre-reg-write   Q009-F-06-q8-q9-seam-smoothness-prereg.md
2026-05-09T22:30:02-05:00  pre-reg-write   Q009-F-07-long-medinan-verse-rank-prereg.md
2026-05-09T22:30:30-05:00  sha-lock        F-05: e3beb6605cd44a6883e01be279a701f9fc1fa08dac6f9e78d4984488220050a7
2026-05-09T22:30:30-05:00  sha-lock        F-06: 6fd9d94553ada755192702f89e4939f635403853225edf35b10904a78e53f88c
2026-05-09T22:30:30-05:00  sha-lock        F-07: c97f9d9d352acf0f83f873a125651ae9e55c59cd1cce3121bd9056e37512168f
2026-05-09T22:35:00-05:00  run             scripts/Q009_F_05_basmala_corpus_singleton.py
                                            → VINDICATED-CORPUS-EXACT (114 = 113 + 1)
2026-05-09T22:35:05-05:00  run             scripts/Q009_F_06_q8_q9_seam_smoothness.py
                                            → NULL (rank-smooth 56/113, mid-band)
2026-05-09T22:35:10-05:00  run             scripts/Q009_F_07_long_medinan_verse_rank.py
                                            → NULL-DIRECTIONAL (rank 12/114, top-decile but JUST outside top-10)
2026-05-09T22:40:00-05:00  ledger-update   05-classical-claims-audit.md: add Audits 9-10
2026-05-09T22:40:30-05:00  ledger-update   06-novel-findings.md: add F-05/06/07 sections, Bonferroni k=7
2026-05-09T22:40:45-05:00  ledger-update   00-overview.md: verdict line refreshed
```

### Headline summary

| Test | Pre-committed direction | Result | Verdict |
|:--|:--|:--|:--|
| T1 (F-05) basmala corpus-singleton | 113 openers + 1 internal Q 27:30 = 114 | **EXACT** | **VINDICATED-CORPUS-EXACT** |
| T2 (F-06) Q 8 → Q 9 seam smoothness ≤ top-30% | rank 56/113 mid-band | NULL | al-Biqāʿī thematic-couplet NOT supported at FR-seam-smoothness |
| T3 (F-07) Q 9 verse-length top-10 | rank 12/114 (top-decile, just outside top-10) | NULL-DIRECTIONAL | direction supported, magnitude just-missed |

### Garden-of-forking-paths log

- F-05 has two equally-valid rules-tuples (stored-JSON vs printed-convention). Both were pre-committed and both verified. Reporting BOTH transparently.
- F-06 chose `delta_raw` (raw FR-TSP penalty) over `fraction_residual` because `delta_raw` is the direct cost penalty and ranks identically (verified). The pre-reg specified `delta_raw`.
- F-07 was tested across all three tashkeel variants for stability check. Result: rank oscillates 11/12/13 — rules-tuple-fragile at the borderline. Honest NULL-DIRECTIONAL, NOT massaged to VINDICATED via tashkeel-choice cherry-picking.

### Why the NULLs matter

This pair of NULLs (F-06, F-07) is informative:
- F-06 NULL shows that al-Biqāʿī's *tanāsub* reading of Q 8 ↔ Q 9 does NOT translate to FR-roots seam-smoothness, *even though* the stronger Ibn ʿAbbās "one surah" claim was already FALSIFIED in [[Q008-F-01]]. The two surahs are mid-band-distant — neither unified, nor smoothly-coupled, nor structurally-isolated from each other. Their connection is interpretive (content/theme/asbāb), not root-distributional.
- F-07 NULL-DIRECTIONAL shows that Q 9's UAS rank 4/114 is NOT driven by extreme verse-length alone (rank 12/114 by length). The UAS-4 status comes from outlier-strength + content-cohesion-isolation, not from sheer prose density.

### Updated quality gates

- [x] Pre-reg SHA matches embedded (7× now).
- [x] Direction-of-effect locked before running (7× pre-reg files).
- [x] Bonferroni correction applied (k=7, α_bon ≈ 0.00714).
- [x] Replication: F-07 cross-checked across 3 tashkeel variants (stability log included).
- [x] Honest NULL prominence: F-06 NULL and F-07 NULL-DIRECTIONAL reported as NULLs without massaging.
- [x] Cross-references updated in 00-overview.md and 05-classical-claims-audit.md.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
