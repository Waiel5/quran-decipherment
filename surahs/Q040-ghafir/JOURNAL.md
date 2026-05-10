---
surah: 40
surah_name: Ghāfir
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-05-09
phase: B+
---

# Q 40 Ghāfir — investigation journal

## 2026-04-28 (Session 1) — full-template completion

### Garden-of-forking-paths log (BEFORE running any computation)

Before computing Q040-F-01 (jadal-density), the following decisions were locked:
- **Tashkeel level**: no-tashkeel (project default).
- **Root operationalization**: QAC v0.4 stem-root annotations (NOT lemma-root, NOT word-form match).
- **Target root**: ج-د-ل (Buckwalter "jdl") — NOT generalized dispute-vocabulary clusters.
- **Density unit**: per 1000 tokens (NOT per 1000 words / per 1000 verses / per surah).
- **Baseline**: corpus-mean excluding Q 40 itself.
- **Direction**: pre-committed Q 40 > corpus mean.
- **Verdict thresholds**: |z|>1.0 = directional; |z|<1.0 = NULL; pre-commit-violation if z<-1.0.

These choices were locked in `preregs/Q040-F-01-jadal-density-prereg.md` and SHA256-locked at `8905026b7fa0b8d415c037585d4f3d5b1b80306f1ef0220b54a5bb2992dbb752` BEFORE the script ran.

### Run timeline

1. Pre-flight reading: SKILL.md + INVESTIGATION-PROTOCOL.md + existing 00/01/02 files for Q 40.
2. Empirical-data integration: pulled Q 40 metrics from h-new-111, h-new-590, h-new-700, h-new-720, h-new-750, h-new-840.
3. Computed Q 40 FR-nearest/farthest neighbors from the full FR distance matrix in h-new-111.
4. Wrote 03-tafsir-survey.md, 04-hadith-corpus.md, 05-classical-claims-audit.md.
5. Pre-registered Q040-F-01 (jadal-density) at SHA256 `8905026b...`.
6. Wrote `Q040_F_01_jadal_density.py` with embedded SHA verification.
7. Ran Q040-F-01 → result: z = +8.75 (corpus extreme, DIRECTIONAL VINDICATION).
8. Wrote 06-novel-findings.md, 07-cross-references.md, JOURNAL.md.

### NULLs surfaced (equal prominence)

- **Claim 4 (Believer-of-Pharaoh names)**: NULL-CLASSICAL — classical isnāds for candidate names are weak; the text's *mubham* status holds.
- **Claim 1 (*dībāj al-Qurʾān*)**: DIRECTIONAL only — HM-7 mean UAS is *below* corpus mean (-0.35); not a top-tier cluster on UAS.
- **Findings 2-3**: post-hoc descriptive; capped at MW-7 single-test α.

### Pre-commit honoring

- Q040-F-01 direction-pre-committed (Q 40 > mean) MATCHED observed direction. No pre-commit violation.

### Honest limits

- Per-Q040 raw extractions of Ibn Kathīr / al-Qurṭubī / al-Rāzī were located by surah-name markers within the consolidated OpenITI files, not as discrete per-Q040 extraction files. The latter would strengthen citation-precision.
- *Faḍāʾil al-Qurʾān* literature traditions (Abū ʿUbayd) are NOT in the 9-book pull and would expand Q 40's ḥadīth-corpus footprint.
- **al-Bukhārī's *Tafsīr* book chapter on Sūrat al-Muʾmin** was identified by chapter-title but not extracted as record-level IDs in this session — flagged for follow-up.

### Verdict

Q 40 Ghāfir investigation **COMPLETE** (per the 8-template-set + JOURNAL standard). One pre-registered novel finding (Q040-F-01) at corpus-extreme strength. Cluster-role: **HM-A opener**. Defining empirical fact: **#1 jadal-densest surah in the Qurʾān (z=+8.75)**.

### Cross-references

- [[hawamim-7-cluster-synthesis|HM-7 cluster synthesis]] — Q 40's role in the cluster
- [[Q040-ghafir/06-novel-findings|Q 40 novel findings]]

---

## 2026-05-09 (Session 2) — Wave-H follow-up: 3 new pre-registered tests + H-NEW-1395

### Garden-of-forking-paths log (BEFORE running)

For each of Q040-F-02, Q040-F-03, Q040-F-04, and H-NEW-1395:
- Pre-reg markdown locked first; SHA256 computed; SHA embedded in run script with fail-fast verification.
- Direction one-tailed and pre-committed BEFORE viewing data.
- N_perm = 10,000; seed = 20260509 (matches session-wide Wave-H convention).
- Bonferroni α_corr = 0.025 for k=2 cells on H-NEW-1395.

### Run timeline

1. Q040-F-02 (HM corpus-EXACT): wrote prereg → SHA `2932348c...` → script → ran → VINDICATED. HM-set = {40..46} exactly.
2. Q040-F-03 (*ghfr*-density rank): wrote prereg → SHA `3854e007...` → script → ran → NULL (rank 25, not top-5). Direction NOT held; clean NULL — Q 40's name is attribute-pointing, not density-pointing.
3. Q040-F-04 (Believer-of-Pharaoh phrase-singleton): wrote prereg → SHA `cab6798d...` → script → ran → VINDICATED (1 hit, Q 40:28).
4. H-NEW-1395 (ḥawāmīm-7 FR-cohesion): wrote prereg at findings/phase-b-hypotheses/prereg-h-new-1395-hawamim-cluster.md → SHA `06bc435a...` → script at findings/phase-b-hypotheses/scripts/h-new-1395.py → ran → NULL. obs d̄=0.8672; cell A p=0.2086; cell B p=0.0514; PC valid (p_pc=0.0414).

### Pre-commit honoring

All four tests pre-committed direction one-tailed lower (for FR-cohesion / hits / rank). Two VINDICATED (F-02, F-04), one DIRECTIONAL-VINDICATION-failed (F-03 NULL with correct direction-frame), one NULL with valid PC (H-NEW-1395). No pre-commit violations.

### Equal NULL prominence

- Q040-F-03 NULL **promoted** to a substantive finding in 06-novel-findings — Q 40's *Ghāfir* name is attribute-pointing not density-pointing, falsifying the naïve naming-density prior.
- H-NEW-1395 NULL **promoted** to a substantive finding — adds HM-7 to the growing evidence (with H-NEW-1301, H-NEW-1340) that muqaṭṭaʿāt-axis ≠ FR-root-axis. Reinforces cross-finding-025 marker-thickness rule.

### Cross-references

- [[h-new-1395-hawamim-cluster|H-NEW-1395]] — ḥawāmīm cluster cohesion NULL
- [[cross-finding-025-marker-thickness-vs-fr-cohesion-threshold|cross-finding-025]] — marker-thickness rule supported
- [[Q040-ghafir/06-novel-findings|Q 40 novel findings §5-7]]
