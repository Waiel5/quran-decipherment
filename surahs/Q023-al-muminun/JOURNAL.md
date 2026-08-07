---
surah: 23
surah_name_ar: المؤمنون
surah_name_translit: al-Muʾminūn
file_type: journal
date_last_updated: 2026-05-09
phase: B+
---

# Q 23 al-Muʾminūn — Investigation Journal


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

## 2026-04-28 (initial landing)

Initial investigation completed by prior specialist. Files landed:
- 00-overview.md
- 01-empirical-profile.md
- 02-content-analysis.md
- 03-tafsir-survey.md
- 04-hadith-corpus.md

Key findings from 2026-04-28:
- UAS rank 9 / 114 (top decile).
- Outlier-strength −10.91 pp (COHESION_ANCHOR classification).
- Rhyme entropy 0.148 nats (rank 109/114 — corpus's 6th-purest monorhyme).
- Q 22→Q 23 cost rank 6/113; Q 23→Q 24 cost rank 11/113.
- Five-movement reading proposed.
- Embryology + believer-typology + prophet-cycle structure mapped.

## 2026-05-09 (Wave-H specialist completion)

Wave-H specialist landing — completion of the 8-file template + 3 pre-registered tests.

### Files added 2026-05-09

- `05-classical-claims-audit.md` — 5 classical claims audited (al-Zamakhsharī flḥ inclusio, al-Suyūṭī monorhyme classification, al-Biqāʿī Q 22→Q 23 munāsabah, al-Ṭabarī Jannat ʿAdn tradition, Tirmidhī ʿUmar 10-verses ḥadīth)
- `06-novel-findings.md` — 3 pre-registered tests with verdicts
- `07-cross-references.md` — full cross-reference map
- `preregs/Q023-F-01-uas-top10-fr-cluster-prereg.md` (SHA `9d16de4b...`)
- `preregs/Q023-F-02-believer-attributes-longest-block-prereg.md` (SHA `ae48a41c...`)
- `preregs/Q023-F-03-embryology-pair-q22-q23-prereg.md` (SHA `4518ad85...`)
- `scripts/Q023_F_01_uas_top10_fr_cluster.py`
- `scripts/Q023_F_02_believer_attributes_longest_block.py`
- `scripts/Q023_F_03_embryology_pair_jaccard.py`
- `csv/Q023-F-01.json`
- `csv/Q023-F-02.json`
- `csv/Q023-F-03.json`

### Pre-registered tests run

| Test | Verdict | Permutation p | Notes |
|:--|:--|:-:|:--|
| Q023-F-01 (UAS top-10 FR-cohesion) | **PRE-COMMIT-VIOLATION-NULL** | p_lower = 1.0 (direction reversed) | T_obs = 1.091, null median = 0.991; cluster is FR-DISPERSED. Adds NULL to cross-finding-025. |
| Q023-F-02 (believer-attributes longest run) | **PASS-DIRECTED-EXACT** | rank-1 single-tie | Q 23:2-5 = corpus-EXACT longest strict-marker run (4 vv); Q 70:32-34 runner-up (3 vv); disbeliever-control max = 2 vv. |
| Q023-F-03 (embryology pair Q 23:12-14 ↔ Q 22:5) | **PASS-DIRECTED** | p_upper = 0.0232 (not Bonferroni-pass) | J_obs = 0.089 vs null p95 = 0.074; 7 shared distinctive tokens including the 3 embryological stage-terms. |

### Pre-reg SHA verification

All 3 scripts embedded the pre-reg SHA256 hash and verified at runtime; all 3 verifications passed.

### Pre-commit-violation report (Q023-F-01)

The pre-registered direction was FR-cohesion (lower mean pairwise FR within top-10 UAS); observed direction is FR-dispersion (T_obs above null median by 0.10 FR-units). Per Protocol §1.8, this is published as **NULL with full prominence** and flagged as direction-reversed. The finding adds an important data point to [[cross-finding-025|cross-finding-025]]: high-UAS aggregates are multi-axis clusters, not root-distribution clusters. The marker-thickness rule applies to multi-axis aggregates with thin per-axis correlation.

### Hadith-number reconciliation

The prompt's mention of "ʿĀʾisha hadith on Prophet's prayer-from-Q 23 (Muslim 770/771 — VERIFY)" was checked against `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json`. Muslim idInBook 770 and 771 in this dataset are Abū Hurayra hadiths on ṣalāh-takbīr form, not Q 23-specific. The Q 23-specific hadiths verified on disk:

- **Muslim idInBook 2230** — *Ṭayyib* hadith citing Q 23:51 + Q 2:172. The unique Muslim-Q 23 hadith in the dataset.
- **Tirmidhī idInBook 3257** — ʿUmar 10-verses hadith citing Q 23:1-10.
- **Tirmidhī idInBook 3259** — **ʿĀʾisha's gloss on Q 23:60** (*yuʾtūna mā ātaw wa-qulūbuhum wajila*). The classical ʿĀʾisha-and-Q 23 hadith, in Tirmidhī (and Ibn Mājah 3936), not Muslim. This is what the prompt likely intended.
- **Nasāʾī idInBook 1009** — Conquest-day Q 23 recitation by the Prophet at the Kaʿba (ʿAbd Allāh b. al-Sāʾib narration).

The 04-hadith-corpus.md file (2026-04-28) uses the correct numbers; the prompt's Muslim 770/771 reference does not match this dataset's indexing and has been flagged here. No correction needed in 04.

### Decision points

- Used existing 01-empirical-profile rank Q 23 = 9 (not "rank 8" as the prompt's headline suggested). 9 is the H-NEW-840 actual rank.
- The pre-reg for F-01 locked the cohesion direction; the result reversed it. Honest report per Protocol §1.8.
- F-02 used strict-marker definition (الذين هم / والذين هم); reported looser-marker top-5 transparently to flag rules-tuple sensitivity.
- F-03 sits between single-test α=0.05 and family-Bonferroni α=0.0167. Verdict: PASS-DIRECTED, not CONFIRMED.

### Quality-gate status

- [x] Pre-reg SHA matches embedded ✓ (verified at runtime for all 3 scripts)
- [x] Direction-of-effect matches pre-committed: 2/3 yes (F-02 rank-test, F-03 PASS); 1/3 reversed (F-01 published as NULL)
- [x] Bonferroni applied: family α = 0.05/3 = 0.0167
- [x] Replication (F-01: seed +1000 confirmed direction)
- [x] Honest limits sections in 05, 06, 07 ✓
- [x] Cross-references include both supporting and challenging priors ✓
- [x] Classical citations are scholar + work + passage ✓
- [x] Final statements are intellectually honest ✓ (F-01 explicitly flagged as direction-reversed; F-03 explicitly flagged as not Bonferroni-pass)

### Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md (5 audits + 1 NOT-TESTABLE + 4 VINDICATED)
- [x] 06-novel-findings.md (3 pre-registered tests, all verdicts published)
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] 3 pre-regs in `preregs/`
- [x] 3 scripts in `scripts/`
- [x] 3 JSON outputs in `csv/`

Q 23 al-Muʾminūn specialist landing is **complete**.
