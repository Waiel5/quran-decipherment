---
surah: 47
file_type: journal
date_started: 2026-05-08
date_last_updated: 2026-05-10
phase: B+
---

# Q 47 Muḥammad — Specialist Journal

## 2026-05-08 — Q032-Q047 retry-specialist run

- Created `00-overview-comprehensive.md` (single-file deep-dive, 11 sections).
- Pre-registered + ran 3 tests:
  - Q047-F-01 Muhammad-naming density (VINDICATED, rank #1 of 4).
  - Q047-F-02 War-vocabulary density (VINDICATED, rank 2/114).
  - Q047-F-03 Q 47-48-49 triplet cohesion (NULL, mid-pack).
- JSONs written to `csv/`.
- Auto-commit by specialist (pre-Wave-J).

## 2026-05-10 — Wave-J specialist run (this session)

### 00:30-00:45 — Pre-flight reading

- Read `INVESTIGATION-PROTOCOL.md` full.
- Read `SESSION-HANDOFF-2026-05-09-PM.md` for Wave-H context.
- Read existing `00-overview-comprehensive.md`, Q047-F-01 prereg, Q047-F-01.json, Q047-F-02.json, Q047-F-03.json.
- Inspected `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json` schema.

### 00:45 — HONEST CORRECTION on brief's Bukhārī #4567 / Q 47:31 claim

- Brief instructed verification of Bukhārī #4567 on Q 47:31 *wa-la-nablu wannakum*.
- Verified on disk: Bukhārī idInBook #4567 is on Q 28:85 (*la-rāddaka ilā maʿādin* — "to Mecca"), NOT Q 47:31.
- Searched all 9 hadith books for Arabic phrase ولنبلونكم / لنبلونكم — 0 matches.
- Logged this as a HONEST CORRECTION in `04-hadith-corpus.md` §0; replaced with the verified Bukhārī #4623-4625 Q 47:22 tafsīr-bāb.

### 00:50 — Pre-registration of 3 new tests per brief

- Wrote `Q047-F-04-muhammad-corpus-inventory-prereg.md` — corpus-EXACT prediction for Muhammad/Aḥmad attestation set.
  - SHA256 locked: `81bf3a4589017eaf4f9cc47780be170b2267a5b07362833092bf04934ca2200a`
- Wrote `Q047-F-05-qtl-root-density-prereg.md` — top-3 prediction for QAC qtl-root density per-1000-w.
  - SHA256 locked: `252b11f712566aeb4a345abd759d14c9d4b8b2a4561ae234b369e3f528070005`
- Wrote `Q047-F-06-q47-q48-adjacent-pair-prereg.md` — in_all_three (bottom-15 cohesive) + FR pair-rank quartile (Bonferroni-2).
  - SHA256 locked: `3b74c07902f7e50f4630a5ca6c48e836e00921f38222f83296082b90fc53dc72`

### 00:55 — Script execution

- Wrote `scripts/Q047_F_04_muhammad_corpus_inventory.py`, `scripts/Q047_F_05_qtl_root_density.py`, `scripts/Q047_F_06_q47_q48_adjacent_pair.py`.
- All three scripts embed SHA-locks and fail-fast on mismatch.
- All three SHA-verifications passed at runtime.
- Results:
  - Q047-F-04 → **VINDICATED**: 4 Muḥammad attestations + 1 Aḥmad attestation, exact-set match.
  - Q047-F-05 → **NULL**: Q 47 rank 19/114 per-1000-w (top-3 pre-reg fails).
  - Q047-F-06 → **NULL**: Q 47-Q 48 mid-pack on all three D-matrices (rank 71/89/75); FR pair-rank 35.4% (not in bottom-25%).
- JSONs written to `csv/Q047-F-04.json`, `csv/Q047-F-05.json`, `csv/Q047-F-06.json`.

### 01:00-01:30 — Eight-file template build

- Wrote `00-overview.md` (the canonical 8-file slot; the prior `00-overview-comprehensive.md` retained as parallel reference).
- Wrote `01-empirical-profile.md` — all H-NEW metrics integrated; computed Q 47's nearest 10 FR-neighbors.
- Wrote `02-content-analysis.md` — 7 thematic blocks, verse-by-verse, vocabulary distinctness.
- Wrote `03-tafsir-survey.md` — al-Ṭabarī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Zamakhsharī + al-Biqāʿī supplementary.
- Wrote `04-hadith-corpus.md` — verified Bukhārī #4623-4625, Muslim #6358, Tirmidhī #2671 + HONEST CORRECTION on brief's #4567 claim.
- Wrote `05-classical-claims-audit.md` — 6 claims audited (Suyūṭī chronology, Biqāʿī ring, Qurṭubī sūrat-al-Qitāl, Bukhārī editorial pair, Suyūṭī asmāʾ nawʿ 17, cross-finding-028 no-fadāʾil).
- Wrote `06-novel-findings.md` — summary table + per-test deep-dive for Q047-F-04, F-05, F-06.
- Wrote `07-cross-references.md` — H-NEW links, cross-findings, sister-surah dossiers.

### 01:30 — Garden-of-forking-paths log

Decisions made BEFORE result observation:
1. Q047-F-04: chose "standalone token" not "substring"; chose no-tashkeel default tuple; verified Aḥmad spelling (أحمد with hamza) before searching.
2. Q047-F-05: chose per-1000-w rate as brief-specified; acknowledged small-N inflation risk BEFORE running; committed to NOT switch metric post-hoc.
3. Q047-F-06: chose to interpret "in_all_three=True" as COHESION direction (bottom-15) not BOUNDARY direction (top-15 jumps); this is a brief-interpretation choice documented BEFORE running. Acknowledged Bonferroni-2 from two sub-tests (Test A and Test B).

### 01:35 — Verdict summary

- 3 prior tests (F-01, F-02, F-03): 2 VINDICATED, 1 NULL.
- 3 new tests (F-04, F-05, F-06): 1 VINDICATED, 2 NULL.
- TOTAL: 3 VINDICATED, 3 NULL.
- All NULLs published with equal prominence per Protocol §1.3.

### 01:40 — Auto-commit per brief instruction

- Commit message: "Q 47 Muḥammad specialist landing — Muḥammad-naming corpus inventory + qitāl pair"
- Files: `surahs/Q047-muhammad/` + `scripts/Q047_F_04_*.py`, `scripts/Q047_F_05_*.py`, `scripts/Q047_F_06_*.py`.
- Git author/committer: waiel (per project-wide protocol).

## Loose-ends / candidate future tests

- Q047-F-07 (post-hoc): Q 47 rhyme-monotony rank among 38-verse-length surahs (likely top-1).
- Q047-F-08: Identification + interpretation of the 2 ا-rāwī exception verses (Q 47's only non-م-rāwī verses).
- Q047-F-09: "Thwarting-of-deeds" refrain test (vv. 1, 8, 9, 28, 32 — corpus-scale rank).
- Q047-F-10: Q 47-Q 48 TSP-edge cheap-pair vs other corpus cheap-edges — controlled MW-3 alternative on edge-cost metric.
- Hadith deep-dive: full Muslim/Tirmidhī/Abū Dāwūd Q 47 citations not exhaustively cataloged in this run.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
