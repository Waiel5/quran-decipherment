# Q 71 Nūḥ — Investigation Journal

## 2026-05-30 — Deep-dive (Wave-O)

- **Pass 1 (initial deep-dive, stalled):** wrote 00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey, 04-hadith-corpus, 05-classical-claims-audit, and pre-registered five novel tests (Q071-F-01..F-05 pre-regs + scripts + F-01/F-02 JSONs). The run hit a stream-watchdog stall before writing 06/07/JOURNAL or committing; the analytical core was salvage-committed.
- **Pass 2 (completion):** a relaunched completion agent hit a transient socket error (2 tool-uses, no output). Completion was therefore finalized inline:
  - Re-ran `scripts/Q071_F_01_nuh_cycle_centroid.py` → pre-reg SHA `e19913e9…996f` verified; pericope boundaries OK; all 15 H-NEW-2260 pairwise Jaccards reproduced to 1e-9. **Verdict NULL** (Q 71 rank 5/6 in the Nūḥ-cycle; Arm A NULL, Arm B z=+0.424 p=0.278).
  - Confirmed `csv/Q071-F-02.json` (five-deities): pre-reg SHA `f818bc8d…2947`; **PASS-DIRECTED-STRONG** — 4 strict-singleton idols at Q 71:23, p=4.12×10⁻¹²; Wadd contextual-singleton (also Q 19:96).
  - Wrote 06-novel-findings.md, 07-cross-references.md, this JOURNAL.
- **Empirical profile anchors** (from disk): FR mean 0.8793 (nearest Q112/Q110/Q91); UAS −1.3242 rank 84/114; sig_A 64/114, sig_B 77/114; Q70→71 seam expensive (96/113), Q71→72 smooth.
- **Hadith:** verified on disk per 04-hadith-corpus.
- **Note:** two scripts share the `Q071_F_01_*` stem (`name_root_concentration` and `nuh_cycle_centroid`); the H-NEW-2260-linked cycle-centroid test is the canonical F-01 (the one reported here). F-03/F-04/F-05 remain pre-reg-only (queued).

**Status: 8-file template COMPLETE.** Headline: Q 71 is FR-peripheral to its own Nūḥ-narrative cycle (F-01 NULL) precisely because its lexical mass is the unique idol/daʿwa vocabulary (F-02 PASS) — eponymy without centrality.
