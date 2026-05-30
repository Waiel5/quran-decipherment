# Q 20 Ṭā-Hā — Investigation Journal

## 2026-05-30 — Deep-dive (Wave-O)

- **Pass 1 (initial, stalled):** wrote 00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey, and pre-registered + ran a full six-test suite (Q020-F-01..F-06: pre-regs in `preregs/`, scripts in `scripts/`, JSONs in `csv/`). Hit a stream-watchdog stall before writing 04-07/JOURNAL or committing; analytical core salvage-committed.
- **Pass 2 (completion agent):** also stalled (600s watchdog) — Ṭā-Hā is the heaviest stub (135 verses, extended Mūsā narrative, large tafsir reads). The watchdog fired during source reading.
- **Pass 3 (inline finalization):** completed inline to avoid further heavy-agent stalls.
  - Re-ran `scripts/Q020_F_06_musa_hub.py` → SHA OK, boundaries OK; **Arm A CONFIRMED (5/6 signature), Arm B CONFIRMED (z=+5.807, p=0.0001)**.
  - Confirmed the full F-01..F-05 JSON verdicts on disk: F-01 NULL (Moses-marker rank 2 not 1), F-02 NULL (2sg-density z=0.749), F-03 NULL (2-letter muqaṭṭaʿāt 0/4 axes), F-04 NULL (Sāmirī block not isolated, p=0.892), **F-05 CONFIRMED (Q20:14 divine-self-density rank 1, p=0.0015)**.
  - Wrote 04-hadith-corpus (honest: the ʿUmar-conversion narrative is sīra/al-Dāraquṭnī, NOT 9-book; greatest-name formula not Q20-specific; documented data-gap — no numbers from memory), 05-classical-claims-audit (8 claims), 06-novel-findings, 07-cross-references, this JOURNAL.
- **Empirical anchors:** FR mean 1.0403 (content-distant, nearest Q23; Mūsā-cycle in top-10), yāʾ-monorhyme 0.7926, sig_A rank 92/114, H-NEW-590 WEAK_OUTLIER (NULL).

**Status: 8-file template COMPLETE.** Headline: Q 20:9-36 is the lexical HUB of the Mūsā burning-bush cycle (F-06, z=+5.81) and Q 20:14 is the surah's densest tawḥīd-disclosure verse (F-05) — Q 20's signature is narrative-theological centrality, not stylistic/orthographic distinctiveness (4 NULLs). With Q 71 (peripheral to its cycle, §10.119), Q 20 anchors the eponymy↔centrality discriminating principle: cycle-hub iff core-episode-carrier.
