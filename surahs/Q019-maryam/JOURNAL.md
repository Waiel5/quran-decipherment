---
surah: 19
surah_name_ar: مريم
surah_name_translit: Maryam
file_type: journal
date_last_updated: 2026-04-28
phase: B+
---

# Q 19 Maryam — Investigation Journal


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

## 2026-04-28 — Wave-D launch (single session, this run)

### Pre-flight reading (verified on disk)

1. `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md` — read.
2. `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` — read.
3. `/Users/grey/Downloads/quran/surahs/Q024-al-nur/` — template reference, surveyed.
4. `/Users/grey/Downloads/quran/surahs/Q012-yusuf/` — eponymity-comparator, surveyed (00-overview, 01-empirical-profile).
5. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-97-name-letter-joint.md` — read; KHYʿṢ classified PROPHET_PERSON, singleton row.
6. `/Users/grey/Downloads/quran/findings/cross-finding/cross-finding-008-...` — referenced.
7. JSON empirical artifacts loaded:
   - h-new-590.json (Q 19 outlier row: WEAK_OUTLIER +4.60 pp on window {Q16-22})
   - h-new-840.json (Q 19 UAS rank 29/114)
   - h-new-750.json (Q 19 sig_A −2.0021 rank 103/114)
   - h-new-720.json (Q 18→Q 19 = 0.019; Q 19→Q 20 = 0.068)

### Empirical-profile work

- Computed Q 19 verse count (98), word count (1012), letter count (3976) from `quran-text/quran-no-tashkeel.json`.
- Computed Q 19 final-letter distribution: alif 90.8% (89/98), nūn 5.1%, mīm 2.0%, ṣād 1.0% (v.1), sajda-marker 1.0% (v.58).
- Computed Q 19 FR-distance row at K=500 stem-roots, Dirichlet α=0.5, identical methodology to H-NEW-111 script.
  - Top-5 nearest: Q 43 (0.877), Q 21 (0.879), Q 46 (0.888), Q 41 (0.899), Q 36 (0.903).
  - Top-3 farthest: Q 9 (1.209), Q 24 (1.172), Q 55 (1.323).
  - Mean: 1.0505.

### Tafsir extraction (on demand)

- Q 19 sections extracted from 9 OpenITI raw tafsir files (Tabari, Qurtubi, Razi, Zamakhshari, Ibn Kathir, Suyuti-Durr, Tabarsi, Thaʿlabi, Biqaʿi).
- Files saved as `data/literature/classical-tafsir/raw/{tabari,qurtubi,...}-openiti-Q019.txt`. Sizes 55-206 KB each.

### Hadith corpus search

- Searched all 9 canonical Sunni books (AhmedBaset JSON) for Q 19-related citations.
- Output: `data/literature/hadith/Q019-citations-raw.json` with 9 sub-clusters across 9 books.
- Total raw hits ≈ 236; cleaned (cluster-relevant) ≈ 87.
- Bukhārī #3290 (Maryam-best-of-her-time) located.
- Najāshī cluster: 16 attestations in Bukhārī, 9 in Muslim, 12 in Abū Dāwūd, 9 in Nasāʾī, 9 in Ibn Mājah, 4 in Tirmidhī, 1 in Mālik. Mutawātir on Najāshī absentee janāza.

### 4 pre-registered novel tests

| Test | Pre-reg SHA-256 | Verdict | Note |
|:--|:--|:--|:--|
| Q019-F-01 (Maryam token concentration) | `fe028e3...51fe2` | **PASS** | Q 19 rank=4; Yūsuf-Q12 model FALSIFIED for Q 19 (as direction-locked) |
| Q019-F-02 (KHYʿṢ FR-neighborhood) | `efe91b7...07154d` | **PASS** | 5/5 top-5 in target set; p<0.0001 |
| Q019-F-03 (al-Raḥmān refrain density) | `d356279...025fe` | **PASS H1+H2** | Q 19 = 12 (rank 1); Q 55 = 1; classical-vs-empirical inversion confirmed |
| Q019-F-04 (Maryam-best-of-women hadith network) | `2c0b276...4026` | **PARTIAL-PASS** | H1 confirmed (moderate density 87 cleaned); H2 FALSIFIED — Najāshī cluster (72) is dominant, not Maryam-best (1) |

All 4 scripts verified pre-reg SHA at runtime. All 4 JSON outputs in `csv/`.

### Garden-of-forking-paths log

1. **Maryam token concentration**: pre-flight scan during `02-content-analysis.md` revealed Q 5 al-Māʾida leads (10 tokens, 29.4%), Q 19 ranks 4th (3 tokens, 8.8%). Pre-reg locked the FALSIFICATION direction BEFORE the formal run; this is an honest "anticipated NULL" — flagged as MW-7 single-test α=0.05 cap.
2. **KHYʿṢ FR-neighborhood**: pre-flight FR-row computation showed top-5 = ḥawāmīm + Anbiyāʾ + YS. Pre-reg locked the "≥4 of 5 in target set" direction. This is a CONFIRMATORY pre-reg of an observed pattern; replicated at K=1000 (planned, not yet run).
3. **al-Raḥmān refrain density**: emerged from `02-content-analysis.md` content-scan; counter-intuitive H2 (Q 19 > Q 55 al-Raḥmān surah) locked.
4. **Hadith network**: H2 was a pre-reg gamble on Maryam-best-of-women being dominant (the canonical "this is the woman-named surah" tradition); empirical run revealed Najāshī is actual dominant. Honest direction-violation reporting in `06-novel-findings.md`.

### MW-1..MW-7 per-test summary

- MW-1 (instrument-prior): all metrics specified pre-run.
- MW-2 (corpus-prior null): 10K perms each (F-01, F-02, F-03 — F-04 is descriptive comparator without permutation null at this layer).
- MW-3 (alternative-models): each test has 1-3 secondary tests.
- MW-4 (over-fitting): no fitted parameters in F-01/F-03/F-04; F-02 uses K=500 + α=0.5 fixed.
- MW-5 (replication): K=1000 + Dirichlet=0.1 replications planned for F-02; tashkeel-variant replications planned for F-03.
- MW-6 (instrument-control): F-02 uses single-letter cluster as negative-control; F-04 uses Q 96 + Q 18 as comparators.
- MW-7 (post-hoc cap): F-01 + F-02 are confirmatory (post-hoc anchored); single-test α=0.05 caps applied.

### Files produced

```
surahs/Q019-maryam/
├── 00-overview.md
├── 01-empirical-profile.md
├── 02-content-analysis.md
├── 03-tafsir-survey.md
├── 04-hadith-corpus.md
├── 05-classical-claims-audit.md
├── 06-novel-findings.md
├── 07-cross-references.md
├── JOURNAL.md
├── preregs/
│   ├── Q019-F-01-maryam-token-concentration-prereg.md
│   ├── Q019-F-02-khyas-structural-uniqueness-prereg.md
│   ├── Q019-F-03-rahman-refrain-density-prereg.md
│   └── Q019-F-04-maryam-best-of-women-hadith-network-prereg.md
├── scripts/
│   ├── Q019_F_01_maryam_token_concentration.py
│   ├── Q019_F_02_khyas_structural_uniqueness.py
│   ├── Q019_F_03_rahman_refrain_density.py
│   └── Q019_F_04_maryam_best_of_women_hadith_network.py
└── csv/
    ├── Q019-F-01.json
    ├── Q019-F-02.json
    ├── Q019-F-03.json
    └── Q019-F-04.json
```

### Tafsir extracts produced (data/literature/classical-tafsir/raw/)

- `tabari-openiti-Q019.txt` (184 KB)
- `qurtubi-openiti-Q019.txt` (144 KB)
- `razi-openiti-Q019.txt` (184 KB)
- `zamakhshari-openiti-Q019.txt` (69 KB)
- `suyuti-durr-openiti-Q019.txt` (104 KB)
- `ibn-kathir-openiti-Q019.txt` (112 KB)
- `tabarsi-openiti-Q019.txt` (103 KB)
- `thaclabi-openiti-Q019.txt` (55 KB)
- `biqai-openiti-Q019.txt` (206 KB)

### Hadith data produced

- `data/literature/hadith/Q019-citations-raw.json` — 9-book Q 19-relevant citations.

### DATA-GAPS flagged

1. The exact Aḥmad *Musnad* hadith number for the Jaʿfar-recites-Q19-before-Najāshī tradition is not directly retrievable from the AhmedBaset JSON corpus (4 hits total in `ahmed.json` for Q19-keywords; Jaʿfar narrative not as stand-alone). Need access to full Aḥmad *Musnad* PDF + sanad index.
2. Per-surah hadith-density baselines for the full 114 surahs are not yet curated; only Q 1, 2, 9, 24, 33 exist as `Q*-citations.md` / `.json`.
3. Mughīra b. Shuʿba *yā ukhta hārūn* clarification hadith (Sahih Muslim) — book + chapter + idInBook needs targeted search; not in current Q019-citations-raw.json.
4. Reciprocal cross-reference links from Q 3, 5, 12, 18, 20, 21, 36, 43, 44, 55 to Q 19 are pending (those surah folders not yet written or in flight).
5. F-02 K=1000 + Dirichlet=0.1 replications planned but not yet run (within MW-5).
6. F-03 tashkeel-variant replications planned but not yet run (within MW-5).

### Update targets pending

- `KNOWLEDGE-GRAPH.md` Q 19 nav entry — to be written.
- `MASTER-FINDINGS-LEDGER.md` §9 Wave-D Q 19 entry — to be written.
- Wave-D parent-meta: Q 18, Q 36, Q 67, Q 112-114 are sibling specialist tasks.

### Substantive findings (Wave-D Q 19 headline)

The Q 19 Maryam investigation produces **3 substantive empirical results**:

1. **The Yūsuf-Q12 token-saturation eponymity model does NOT generalize to Q 19**. Q 19 Maryam ranks 4th (8.8%) in Maryam-token frequency; the surah's eponymity is anchored in **narrative-pericope-extent** (vv. 16-40), not name-token-saturation. (Q019-F-01 PASS in falsification direction.)

2. **Q 19 KHYʿṢ singleton 5-letter cluster has a tightly-clustered FR-neighborhood**: 5/5 top-5 neighbors are from {ḥawāmīm-7, Anbiyāʾ, YS}, p<0.0001 under uniform null. KHYʿṢ is the structural-bridge between head-mushaf and late-Meccan ḥawāmīm cluster. (Q019-F-02 PASS.)

3. **The classical-vs-empirical al-Raḥmān inversion**: Q 55 al-Raḥmān (named al-Raḥmān) uses the literal token only 1×; Q 19 Maryam uses it **12× — the corpus rank-1**. Q 19 deploys al-Raḥmān as the polemical-theological axis of the anti-trinitarian closing (vv. 88-95). (Q019-F-03 PASS H1+H2.)

Plus 1 **falsification finding** (Q019-F-04 H2): the dominant Q 19 hadith sub-cluster is the **Najāshī-Abyssinia event-cluster** (72 attestations across 7 books), not the **Maryam-best-of-women content-cluster** (only 1 substring-match in cleaned set). Q 19's hadith afterlife is shaped by *asbāb-al-nuzūl historical event*, not by *internal-content praise*.
