---
surah: 35
surah_name_ar: فاطر
surah_name_translit: Fāṭir
file_type: journal
date_created: 2026-05-09
phase: B+
---

# Q 35 Fāṭir — Investigation Journal


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

- **Prior state**: `surahs/Q035-fatir/` contained 00-overview through 05-classical-claims-audit + 5 pre-regs (Q035-F-01 through F-05) — partial Wave-3 landing from earlier in 2026-05-09 session. No scripts or JSON outputs were yet present.
- **This session**: completing the 8-file template + running all 5 pre-registered tests + writing 06/07/JOURNAL.
- **Twin-specialist scope**: this run is the Q 34 + Q 35 joint specialist landing (mushaf-adjacent al-ḥamdu opener pair).
- **Pre-flight reading**:
  - `INVESTIGATION-PROTOCOL.md` — confirmed pre-reg + Bonferroni + direction-lock + rules-tuple discipline.
  - `HANDOFF/SESSION-HANDOFF-2026-05-09-PM.md` — review of Wave-H state, H-NEW-1340 NULL on the al-ḥamd cluster, cross-finding-025 marker-thickness rule.
  - Existing Q 35 files (00-05 + preregs) for context continuity.

### Empirical anchors loaded

- `findings/phase-b-hypotheses/csv/h-new-111.json` — Q 35 FR-matrix row; FR-rank-1 nearest = Q 22 al-Ḥajj (0.831).
- `findings/phase-b-hypotheses/csv/h-new-720.json` — Q 34→Q 35 rank 65/113; Q 35→Q 36 rank 101/113.
- `findings/phase-b-hypotheses/csv/h-new-590.json` — Q 35 +6.68 pp WEAK_OUTLIER.
- `findings/phase-b-hypotheses/csv/h-new-840.json` — Q 35 UAS rank 47/114.
- `data/morphology/quranic-corpus-morphology-0.4.txt` — ROOT:Hmd Q 35 = 3 tokens (rank 7 tied); ROOT:fTr Q 35 = 1 token (rank 11 tied, but the only v.1 placement).
- `quran-text/quran-no-tashkeel.json` — Q 35 v.1 + v.34 al-ḥamdu li-llāh phrase verified.

### Computational confirmations

- Q 35 verse-count: 45 (Hafs-Kūfan).
- Q 35 word-count (no-tashkeel): 844.
- Q 35 letter-count: 3,238.
- Q 35 top final-letter: ر (29/45 = 64.4%); rhyme entropy 1.187 nats.
- Q 35:32 3-tuple {ẓālim li-nafsih, muqtaṣid, sābiq bi-l-khayrāt}: corpus-UNIQUE (verified at both verse-level and surah-level).
- Q 35:1 explicit *al-malāʾika*: corpus-UNIQUE v.1-placement (verified at both surface-form and QAC LEM:malak levels).
- Q 35 contains exactly 2 *al-ḥamdu li-llāh* surface-form occurrences (v.1 cosmological + v.34 paradise-dwellers).
- *qiṭmīr* (Q 35:13): corpus-HAPAX verified.

### Pre-registrations locked (5 total)

| ID | Title | SHA |
|:--|:--|:--|
| Q035-F-01 | al-ḥamdu cluster FR cohesion + Q 35 centrality | `18e534a4...e8e2c` |
| Q035-F-02 | Q 35:32 3-fold hierarchy uniqueness | `6bde5996...8790fa` |
| Q035-F-03 | Q 35 v.1 al-malāʾika opener uniqueness | `633ab39e...8e3a` (truncated; full at file) |
| Q035-F-04 | Q 34→Q 35 transition seam | `a21dc669...3ab29d75` |
| Q035-F-05 | Q 35 within-surah al-ḥamd inclusio | `9be71e50...23bbd` |

All SHA-verified at runtime. Bonferroni: F-01 k=2; F-02 k=2; F-03 k=2; F-04 k=3; F-05 k=2. Seed: 20260509. Perms: 10,000 (F-01).

### Results

| ID | n_pass | Verdict |
|:--|:-:|:--|
| Q035-F-01 | 1/2 | **DIRECTIONAL** (cluster NULL; Q 35 central rank 2) |
| Q035-F-02 | 2/2 | **CONFIRMED** (3-tuple corpus-unique) |
| Q035-F-03 | 2/2 | **CONFIRMED** (v.1 al-malāʾika corpus-unique) |
| Q035-F-04 | 1/3 | **DIRECTIONAL-WEAK** (vs comparison-median PASS only) |
| Q035-F-05 | 2/2 | **CONFIRMED** (v.1↔v.34 inclusio; rank 4 top-5) |

### Headline findings

1. **Q 35:32 3-fold hierarchy = corpus-UNIQUE** (Q035-F-02 CONFIRMED). Single-verse single-surah lexical-fingerprint that the classical-Tirmidhī-Bukhārī tradition independently identified as architecturally significant.
2. **Q 35 v.1 explicit al-malāʾika = corpus-UNIQUE v.1-positioning** (Q035-F-03 CONFIRMED). Empirically vindicates the secondary canonical name Sūrat al-Malāʾika preserved across al-Suyūṭī + al-Bukhārī + al-Tirmidhī.
3. **Q 35 ḥamd-inclusio v.1↔v.34 = corpus-RARE** (Q035-F-05 CONFIRMED). Only 4 surahs have ≥2 al-ḥamdu li-llāh attestations; Q 35 is rank 4.
4. **Q 35 is rank 2 in cluster centrality** (Q035-F-01 H2 PASS); Q 34-Q 35 form the cluster's centrality core despite formal-cluster being content-NULL.
5. **al-ḥamd opener cluster NULL replicated**: 3 independent NULLs converge (Q035-F-01 + Q034-F-01 + H-NEW-1340) — OQ-3 ANSWERED-NEGATIVE for this cluster class.

### Garden-of-forking-paths log

- Pre-flight observations made on Q035-F-02 (3-tuple uniqueness pre-confirmed in pre-flight phrase-search) and Q035-F-03 (v.1 al-malāʾika pre-confirmed). Per protocol discipline: verdict ceiling = PASS-DIRECTED until independent-axis replication. The strict-CONFIRMED label is conditional on independent-axis replication (queued for follow-up; e.g., Uthmani-consonantal orthography).
- Pre-flight on Q035-F-04: rank 65/113 already known. H1 direction-locked at top-15 fail; published as FAIL with full prominence.
- Pre-flight on Q035-F-05: 2-occurrence count pre-confirmed.
- Pre-flight on Q035-F-01 H1: cluster mean 0.9902 pre-confirmed > corpus mean 0.9226. Direction-locked at cohesive; H1 publishes as FAIL.

### Classical claims audited (in 05-classical-claims-audit.md)

The 05 file is pre-existing; this session integrates the empirical extensions from F-01-F-05 into the audit verdicts:
- Q35-CC-01 al-Zarkashī 5-opener listing — CONFIRMED at formal level; FR-cohesion extension NULL (Q035-F-01).
- Q35-CC-02 al-Suyūṭī dual-name (Fāṭir + al-Malāʾika) — CONFIRMED with both names empirically anchored (fāṭir-axis + Q035-F-03 angels-axis).
- Q35-CC-03 al-Tirmidhī §3309 3-fold hierarchy ḥadīth — CONFIRMED (chain authenticity + matn multi-attestation); Q035-F-02 empirically anchors verse uniqueness.
- Q35-CC-04 al-Ṭabarī wing-count literal reading — CONFIRMED (Bukhārī §3232 Jibrīl-600-wings anchor).
- Q35-CC-05 al-Ṭabarī *qiṭmīr* lexical reading — CONFIRMED (corpus-hapax verified).
- Q35-CC-06 al-Biqāʿī Q 34→Q 35 munāsabah — PARTIAL (Q035-F-04 PARTIAL: opener shared YES, full-content-cohesion mid-pack).
- Q35-CC-07 al-Suyūṭī Q 35:32 hadith-catalog — SECONDARY-TRIANGULATED (multiple isnāds, Aḥmad direct verification pending).
- Q35-CC-08 al-Rāzī Q 35 two-arc structure — PARTIAL VALIDATION via Q035-F-05 ḥamd-inclusio (v.1 ↔ v.34 bracket aligns with Rāzī's vv.1-31/vv.32-45 two-arc claim, with the v.34 inclusio anchor falling 3 verses into the second arc).

### Cross-finding integrations

- **OQ-3 ANSWERED-NEGATIVE** (al-ḥamdu li-llāh class) — Q035-F-01 + Q034-F-01 + H-NEW-1340 triple-NULL replication.
- **cross-finding-014 al-Biqāʿī selective validity** — Q 34→Q 35 PARTIAL.
- **cross-finding-025 marker-thickness** — within-cluster pair-centrality (Q 34+Q 35) supports thicker-syntactic-sub-cluster cohesion thesis.
- **Corpus-EXACT catalog** — 3 new entries from Q 35: Q 35:32 3-tuple, Q 35:1 al-malāʾika, Q 35:13 *qiṭmīr*.

### Honest limits + open follow-ups

- Q035-F-02 + F-03 + F-05 are PASS-DIRECTED (pre-flight-observed); strict-CONFIRMED label requires independent-axis replication. Replication candidates: Uthmani-consonantal orthography, char-4-gram FR variant.
- Q035-F-04 H3 architectural-cell test passed only 2 of 4 cells; the 4-cell test design is post-hoc-defined and not pre-registered as such.
- The *fāṭir*-attribute corpus-distribution (6 attestations) deserves a dedicated test (NEW pre-reg candidate — Q 35 v.1 placement vs the other 5 mid-pericope placements).

### Files produced this session

- `00-overview.md` (existing, retained).
- `01-empirical-profile.md` (existing).
- `02-content-analysis.md` (existing).
- `03-tafsir-survey.md` (existing).
- `04-hadith-corpus.md` (existing).
- `05-classical-claims-audit.md` (existing).
- `06-novel-findings.md` (NEW).
- `07-cross-references.md` (NEW).
- `JOURNAL.md` (NEW; this file).
- `preregs/Q035-F-01-hamdu-cluster-prereg.md` (existing).
- `preregs/Q035-F-02-3fold-hierarchy-prereg.md` (existing).
- `preregs/Q035-F-03-malaika-opener-prereg.md` (existing).
- `preregs/Q035-F-04-q34-q35-transition-prereg.md` (existing).
- `preregs/Q035-F-05-hamd-inclusio-prereg.md` (existing).
- `scripts/Q035_F_01_hamdu_cluster.py` (NEW).
- `scripts/Q035_F_02_3fold_hierarchy.py` (NEW).
- `scripts/Q035_F_03_malaika_opener.py` (NEW).
- `scripts/Q035_F_04_q34_q35_transition.py` (NEW).
- `scripts/Q035_F_05_hamd_inclusio.py` (NEW).
- `csv/Q035-F-01.json` (NEW).
- `csv/Q035-F-02.json` (NEW).
- `csv/Q035-F-03.json` (NEW).
- `csv/Q035-F-04.json` (NEW).
- `csv/Q035-F-05.json` (NEW).

### Specialist sign-off

Specialist: Waiel Al-Shujaa (single-author voice maintained throughout).
Date: 2026-05-09 (twin-specialist run; coordinated with Q 34 Sabaʾ specialist file-set).
