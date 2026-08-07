---
surah: 34
surah_name_ar: سبإ
surah_name_translit: Sabaʾ
file_type: journal
date_created: 2026-05-09
phase: B+
---

# Q 34 Sabaʾ — Investigation Journal


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

## 2026-05-09 — Twin-specialist run (Q 34 + Q 35)

### Setup

- **Prior state**: `surahs/Q034-saba/` contained 00-overview through 04-hadith-corpus + 1 pre-reg + 1 script + 1 JSON (Q034-F-01) — partial Wave-3 landing from earlier in 2026-05-09 session.
- **This session**: completing the 8-file template + running 4 additional pre-registered tests (Q034-F-02 through F-05) + writing 05/06/07/JOURNAL.
- **Twin-specialist scope**: this run is the Q 34 + Q 35 joint specialist landing (mushaf-adjacent al-ḥamdu opener pair).
- **Pre-flight reading**:
  - `INVESTIGATION-PROTOCOL.md` — confirmed pre-reg + Bonferroni + direction-lock + rules-tuple discipline.
  - `HANDOFF/SESSION-HANDOFF-2026-05-09-PM.md` — review of Wave-H state, H-NEW-1340 NULL on the al-ḥamd cluster, cross-finding-025 marker-thickness rule.
  - Existing Q 34 files (00-04 + Q034-F-01) for context continuity.

### Empirical anchors loaded

- `findings/phase-b-hypotheses/csv/h-new-111.json` — Q 34 FR-matrix row + top-10 neighbors (rank 1 Q 41, rank 10 Q 27).
- `findings/phase-b-hypotheses/csv/h-new-720.json` — Q 33→Q 34 rank 111/113 + Q 34→Q 35 rank 65/113 verified.
- `findings/phase-b-hypotheses/csv/h-new-590.json` — Q 34 NULL outlier (delta_pct −4.70).
- `findings/phase-b-hypotheses/csv/h-new-840.json` — Q 34 UAS rank 18/114.
- `data/morphology/quranic-corpus-morphology-0.4.txt` — ROOT:Hmd counts (Q 34 = 3 tokens, rank 6 tied).

### Computational confirmations

- Q 34 word-count (no-tashkeel): 887 — verified.
- Q 34 verse-count: 54 — verified Hafs-Kūfan.
- Sabaʾ proper-noun (LEM:saba<) corpus-distribution: 2 attestations exactly (Q 27:22, Q 34:15) — verified.
- al-ḥamdu li-llāh opener cluster {Q 1, 6, 18, 34, 35}: phrase-search verified in `quran-text/quran-no-tashkeel.json` — all 5 surahs match.
- Q 34's *qul* count = 15 across 14 verses (5.22× corpus mean) — computed.
- Q 34's dual-ḥamd v.1 (corpus-unique double *al-ḥamd*) — verified by phrase-search.

### Pre-registrations locked (5 total)

| ID | Title | SHA |
|:--|:--|:--|
| Q034-F-01 | al-ḥamd cluster FR cohesion | `26500022...8063a` |
| Q034-F-02 | Q 27↔Q 34 Saba-pair | `a8fd1b2d...07600` |
| Q034-F-03 | ḥmd root rank corpus 114 | `70d7b5ec...3c00` |
| Q034-F-04 | Q 34→Q 35 seam LOW-cost | `6f2d39c9...5333` |
| Q034-F-05 | opener sequential-pair distances | `83414986...928e3` |

All SHA-verified at runtime. Bonferroni: F-01/F-02/F-03/F-04 = k=3, F-05 = k=2. Seed: 20260509. Perms: 10,000.

### Results (CONFIRMED at SHA + direction-lock + Bonferroni)

| ID | n_pass | Verdict |
|:--|:-:|:--|
| Q034-F-01 | 0/3 | **NULL** (cluster content-NULL on FR) |
| Q034-F-02 | 1/3 | **DIRECTIONAL-WEAK** (mutual top-10 only) |
| Q034-F-03 | 2/3 | **DIRECTIONAL** (top-10 token-count + density; tied median) |
| Q034-F-04 | 1/3 | **DIRECTIONAL-WEAK** (FR-intra-median only; seam mid-pack) |
| Q034-F-05 | 1/2 | **DIRECTIONAL** (all-pair percentile pass; not minimum seq pair) |

### Headline findings

1. **al-ḥamdu opener cluster content-NULL on FR** (Q034-F-01) — replicates H-NEW-1340, OQ-3 answer NEGATIVE.
2. **Q 27 ↔ Q 34 Saba-pair = mutual top-10 FR** (Q034-F-02 H2) — non-trivial structural pair-relation; ~9% baseline.
3. **Q 18 ↔ Q 34 is the TIGHTEST sequential opener-pair** (Q034-F-05 post-hoc) — *alladhī*-relative-clause syntactic sub-cluster emerges; candidate for cross-finding-025 thicker-marker test.
4. **Q 34 → Q 35 seam mid-pack** (Q034-F-04 rank 65/113) — al-Biqāʿī opener-twin smoothness claim PARTIAL: opener-form shared but FR-content seam not extreme.
5. **Q 33 → Q 34 seam VERY rough** (rank 111/113) — al-Biqāʿī thematic-discontinuity claim VINDICATED at extremity.

### Garden-of-forking-paths log

- Pre-flight observations made BEFORE pre-reg lock on Q034-F-01 (cluster mean 0.9902 > corpus mean 0.9226 was known). Verdict ceiling DESCRIPTIVE-EMPIRICAL per protocol discipline.
- Pre-flight observation on Q034-F-04 H1 (rank 65/113 > 20) and Q034-F-05 H1 (Q 18↔Q 34 tightest = 0.8984 < Q 34↔Q 35 = 0.9268). Direction-locked at opposite (predicted) result per discipline; both H1 PUBLISHED AS FAIL with full prominence.
- Q034-F-02 H1 pre-flight observation (D[Q27,Q34] = 0.8661, percentile 31.30% > 25% threshold). Direction locked; H1 publishes as FAIL.

### Classical claims audited (in 05-classical-claims-audit.md)

- Q34-CC-01 al-Zarkashī 5-opener listing — CONFIRMED.
- Q34-CC-02 al-Ṭabarī Sabaʾ-kingdom identification — CONFIRMED.
- Q34-CC-03 al-Bukhārī/Muslim Q 34:28 universal-prophecy hadith — CONFIRMED (7-book convergence).
- Q34-CC-04 al-Biqāʿī Q 33→Q 34 munāsabah — PARTIAL (VINDICATED at rough-seam extremity).
- Q34-CC-05 al-Biqāʿī Q 34→Q 35 opener-twin munāsabah — PARTIAL (VINDICATED at opener-form level only).
- Q34-CC-06 al-Suyūṭī Late-Meccan chronology — CONFIRMED.

### Cross-finding integrations

- **cross-finding-014 al-Biqāʿī selective validity** — adds 2 data points (Q 33-34 + Q 34-35).
- **cross-finding-025 marker-thickness** — adds 2 data points: formal-opener-tag thin (NULL); syntactic-relative-clause-sub-cluster approaches threshold (post-hoc).
- **OQ-3** answer-NEGATIVE locked for al-ḥamdu li-llāh class.

### Honest limits + open follow-ups

- Q034-F-03 H3 fails because Q 34 ties at the cluster-median density; this is a knife-edge.
- The *alladhī*-relative-clause sub-cluster {Q 6, Q 18, Q 34} merits a properly-pre-registered FR-cohesion test (NEW pre-reg candidate).
- The 5-tests are all DIRECTIONAL or NULL; no CONFIRMED. Q 34's strongest empirical signature remains the corpus-unique dual-ḥamd v.1 and the mutual-top-10 Saba-pair (Q 27↔Q 34).

### Files produced this session

- `00-overview.md` (existing, retained).
- `01-empirical-profile.md` (existing).
- `02-content-analysis.md` (existing).
- `03-tafsir-survey.md` (existing).
- `04-hadith-corpus.md` (existing).
- `05-classical-claims-audit.md` (NEW).
- `06-novel-findings.md` (NEW).
- `07-cross-references.md` (NEW).
- `JOURNAL.md` (NEW; this file).
- `preregs/Q034-F-02-q27-q34-saba-pair-prereg.md` (existing).
- `preregs/Q034-F-03-hmd-root-rank-prereg.md` (NEW).
- `preregs/Q034-F-04-q34-q35-seam-prereg.md` (NEW).
- `preregs/Q034-F-05-opener-pair-distances-prereg.md` (NEW).
- `scripts/Q034_F_02_q27_q34_saba_pair.py` (NEW).
- `scripts/Q034_F_03_hmd_root_rank.py` (NEW).
- `scripts/Q034_F_04_q34_q35_seam.py` (NEW).
- `scripts/Q034_F_05_opener_pair_distances.py` (NEW).
- `csv/Q034-F-02.json` (NEW).
- `csv/Q034-F-03.json` (NEW).
- `csv/Q034-F-04.json` (NEW).
- `csv/Q034-F-05.json` (NEW).

### Specialist sign-off

Specialist: Waiel Al-Shujaa (single-author voice maintained throughout).
Date: 2026-05-09 (twin-specialist run; coordinated with Q 35 Fāṭir specialist file-set).
