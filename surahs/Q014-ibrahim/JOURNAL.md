---
surah: 14
surah_name_ar: ابراهيم
surah_name_translit: Ibrāhīm
file_type: journal
date_created: 2026-05-08
phase: B+
---

# Q 14 Ibrāhīm — Investigation Journal


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

## 2026-05-08 — Specialist run (Q014-Q015-ALR-completer)

### Setup
- Prior state: Q014-ibrahim folder existed with empty `csv/`, `preregs/`, `scripts/` subdirs; no template files (00-overview through 07-cross-references) had been written.
- Pre-flight read: `INVESTIGATION-PROTOCOL.md`, `HANDOFF/04-DISCIPLINE.md`, `surahs/Q012-yusuf/` template, `surahs/Q013-al-rad/` (sibling specialist), `surahs/Q011-hud/`, `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md`.
- Empirical anchors loaded: `findings/phase-b-hypotheses/csv/h-new-{111, 590, 700, 720, 750, 840}.json`. Q14 row keys verified for surah=14 across all artifacts.

### Computational confirmations
- FR matrix loaded from `h-new-111.json` `D_matrix_upper_triangular`. Q 14's FR-nearest = Q 13 at 0.7838 (verified). Q 13's FR-nearest = Q 14 at 0.7838 (also verified — bilateral mutual-nearest).
- Q 14 UAS rank 20/114 (UAS=1.245); sig_A rank 14/114 (1.546); sig_B rank 15/114 (1.464); rhyme entropy z=+2.07 (corpus top-tier multi-rāwī).
- H-NEW-590 X=14 row: NULL classification (delta_pct=-4.28, p_greater_W=0.4183). Q 14 is a CLUSTER ANCHOR, not an outlier — same pattern as Q 13.
- H-NEW-720 s=13: 0.0497 (CHEAP); s=14: 0.1988 (top-15 EXPENSIVE).

### Pre-test informational scan (for prereg formulation, NOT result-viewing)
- Computed prayer-vocative density for Q 14:35-41 with broad lemma family: 14.95/100w; rank 1/5569 7-verse windows. The 4 highest-density 7-verse windows in the corpus all inside Q 14.
- This pre-test scan informed the formulation of the Q014-F-01 pre-reg with a MORE conservative lemma family (drops a few markers); the formal SHA-locked test re-runs and finds rank 1/5569 robustly with density 14.02/100w.

### Pre-registration (locked 2026-05-08)
- Q014-F-01 pre-reg written to `preregs/Q014-F-01-abrahamic-prayer-density-prereg.md`. SHA: `9bfe6edf1baff43c6e63800f0f2d163ffc726f2bee78f1144643eba7c7059274`.
- Q014-F-02 pre-reg written to `preregs/Q014-F-02-bilateral-twin-q13-prereg.md`. SHA: `122637ab720e00e7d8e3c37dc4cecdb2259fa7df07e578a18092a1461f61609a`.
- Q014-F-03 pre-reg written to `preregs/Q014-F-03-alr-cluster-membership-prereg.md`. SHA: `3c06deac20c5bb6f3db315daf37476682950ffdecc71599d3645f8e211092a91`.
- Bonferroni-k = 3 (locked in YAML frontmatter of all 3 pre-regs); α_bon = 0.0167.

### Run script
- `scripts/Q014_F_all_tests.py` written with embedded SHA verification, seed 20260508, n_perm 10000.
- Run executed: 2026-05-08. All 3 SHA-OK. JSON outputs written to `csv/Q014-F-{01,02,03}.json` and `csv/Q014-F-family-summary.json`.

### Verdicts
- **Q014-F-01: CONFIRMED** — Q 14:35-41 corpus-MAX prayer-density rank 1/5569 (density 14.02/100w; 15 prayer tokens / 107 words). Top 4 windows in corpus all inside Q 14. Q 14 whole-surah density rank 4/114.
- **Q014-F-02: CONFIRMED** — Q 13 ↔ Q 14 bilateral mutual-nearest (BOTH directions: Q 14's FR-nearest = Q 13, Q 13's FR-nearest = Q 14, both at d=0.7838). 4-axis architectural twin: d_arch(Q14, Q13) = 0.486 vs d_arch(Q14, Q76) = 4.77 — twin-strength ratio **9.82×** (slightly stronger than Q013-F-05's 8.83×).
- **Q014-F-03: NULL** at α_bon = 0.0167. p_perm_strict = 0.40 (random 4-surah subsets are FR-closer than ALR-strict siblings 40% of the time); p_perm_ext = 0.072 (DIRECTIONAL but not significant). Replicates H-NEW-610 letter-family-content-NULL (6th replication: full-29, ḥawāmīm-7, ALM-6, ALR-5, Q013-F-04, Q014-F-03).

### Hadith number verification
- Bukhārī #61: VERIFIED as date-palm hadith (good-word parable Q 14:24-25).
- Bukhārī #1321, #4493: VERIFIED as al-Barāʾ b. ʿĀzib hadith on Q 14:27 / qawl thābit / grave-questioning.
- Muslim #7040, #7041: VERIFIED as parallels of the same al-Barāʾ chain.
- Tirmidhī #3204: VERIFIED as parallel of the same Q 14:27 grave-questioning hadith.
- Bukhārī #5911: VERIFIED — directly cites Q 14:25 verse-text *tuʾtī ukulahā kulla ḥīn*.
- **CRITICAL CORRECTION**: Bukhārī #3364 is NOT the Hagar-Mecca-settling narrative as widely-cited in secondary tafsir literature. Direct verification shows #3364 is about the Ghifar/Aslam tribes. The CORRECT Hagar-Mecca-settling narrative is **Bukhārī #3225** (long version, ~4500 chars; via Ibn ʿAbbās → Saʿīd b. Jubayr → multiple chains; with parallels #3224, #3226). The brief form *yarḥamu Allāhu umm Ismāʿīl* is at #2274. This correction is documented in `04-hadith-corpus.md` §3 with explicit attention drawn for downstream propagation.

### Files written
- `00-overview.md`, `01-empirical-profile.md`, `02-content-analysis.md`, `03-tafsir-survey.md`, `04-hadith-corpus.md`, `05-classical-claims-audit.md`, `06-novel-findings.md`, `07-cross-references.md`, `JOURNAL.md` (this file).
- `preregs/Q014-F-01-abrahamic-prayer-density-prereg.md`
- `preregs/Q014-F-02-bilateral-twin-q13-prereg.md`
- `preregs/Q014-F-03-alr-cluster-membership-prereg.md`
- `scripts/Q014_F_all_tests.py` (top-level scripts directory)
- `csv/Q014-F-01.json`, `csv/Q014-F-02.json`, `csv/Q014-F-03.json`, `csv/Q014-F-family-summary.json`

### Discipline notes (Bonferroni asymmetry, direction-locking)
- Bonferroni-k = 3 was determined BEFORE running any test. The k=3 family is fixed: Q014-F-01, F-02, F-03. No mid-flight tightening or loosening.
- Direction was locked in pre-reg YAML frontmatter for each test:
  - F-01: Q 14:35-41 has corpus-MAX density (rank 1).
  - F-02: Q 14's FR-nearest is Q 13 AND Q 14 closer to Q 13 than to Q 76 (4-axis).
  - F-03: Q 14 closer to ALR-siblings than to random 4-surah subsets.
- F-01 and F-02 directions matched empirically. F-03 directional component matched (mean Q14→ALR < random) on the ext but at NULL significance; on the strict variant, Q 14 is modestly farther from ALR-strict (delta = +0.017).
- No pre-commit violations. F-03 NULL is not a violation but rather a correctly direction-locked test where the corpus-architectural prior (H-NEW-610 NULL) predicted the result.

### Cross-finding context updates queued
- cross-finding-026 §13 architectural-cell typology: Q 14 + Q 13 confirmed as a bilateral twin-pair sub-cell ("didactic-cosmological-prayer-iʿjāz-positive head-mushaf"). Update queued.
- H-NEW-610 letter-family-content-NULL framework: Q014-F-03 is the 6th replication; replication count update queued.
- Q014-F-01 corpus-MAX prayer-density is a new entry in the cross-finding-026 §4 "classical-attention → empirical-MAX" correspondence inventory. Update queued.

### Next-agent / follow-on items
- F-04 (queued): test Q 14's signature against alternative cluster definitions (e.g., "head-mushaf medium-length cosmological-creator surahs" set, including Q 22, 35, 40, 71). Pre-reg pending.
- F-05 (queued): replicate the Q 14:35-41 prayer-density-MAX finding across rules-tuple variants (full-tashkeel-anchored, transliteration-anchored, etc.) for rules-tuple sensitivity.
- Cross-replication: Q014-F-02's bilateral-twin signal could be tested across alternative distance metrics (e.g., NCD on raw text, JS-divergence on root distributions) to verify the metric-invariance of the twin signal.

### Honest reporting note
- Q 14:35-41 corpus-MAX result is ROBUST. The exact density value (14.02 vs 14.95 in informational scan) differs by lemma-family scope; both numbers point to the same rank-1 result. The pre-reg locked the conservative lemma family; the formal-test density of 14.02 is the locked figure.
- Q014-F-03 NULL is consistent with prior framework expectation; the test is published with full prominence as NULL per equal-NULL-prominence discipline.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
