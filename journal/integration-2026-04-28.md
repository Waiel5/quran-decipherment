---
title: Integration journal — Wave A + Wave B per-surah investigations + cross-finding-026 4-cell typology amendment
date: 2026-04-28
specialist: integration-specialist (autonomous)
phase: B+
inputs: 7 surah-folder deep-investigations (Q 1, Q 2, Q 9, Q 12, Q 24, Q 33, Q 55) + cross-finding-026 + MASTER-FINDINGS-LEDGER + KNOWLEDGE-GRAPH
outputs: cross-finding-026 §13 amendment, MASTER-FINDINGS-LEDGER §9, KNOWLEDGE-GRAPH per-surah navigation section
verdict: integration-COMPLETE
---

# Integration journal 2026-04-28

## Pre-flight reading completed

1. `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md` — methodology entry-point.
2. `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` — full binding methodology.
3. All Wave A and Wave B per-surah investigations under `/Users/grey/Downloads/quran/surahs/`:
   - Q 1 al-Fātiḥa: 8 template files + Q001-F-01..F-04 (5 pre-registered tests; 1 VINDICATED, 1 NULL, 1 NULL with refinement, 1 PRE-COMMIT-VIOLATION + corrected-direction VINDICATED).
   - Q 2 al-Baqara: 8 template files + Q002-F-01..F-05 (5 pre-registered tests; 1 VINDICATED, 1 RULES-TUPLE-FRAGILE, 1 DIRECTIONAL, 2 NULL).
   - Q 9 al-Tawba: 8 template files + Q009-F-01..F-04 (4 pre-registered tests; 1 FALSIFIED-classical-claim, 2 VINDICATED, 1 NULL).
   - Q 12 Yūsuf: 8 template files + Q012-F-01..F-04 (4 pre-registered tests; 3 CONFIRMED, 1 DIRECTIONAL).
   - Q 24 al-Nūr: 8 template files + Q024-F-01..F-04 (4 pre-registered tests, all CONFIRMED).
   - Q 33 al-Aḥzāb: 8 template files + Q033-F-01..F-05 (5 pre-registered tests; 1 VINDICATED-length-ctrl, 1 RULES-TUPLE-FRAGILE, 1 NULL, 2 FALSIFIED).
   - Q 55 al-Raḥmān: 8 template files + Q055-F-01..F-05 (5 pre-registered tests; 3 CONFIRMED, 1 DIRECTIONAL, 1 RULES-TUPLE-FRAGILE→MODERATE).
4. `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` (read in full prior to amendment).
5. `MASTER-FINDINGS-LEDGER.md` — read tail to confirm integration anchor.
6. `KNOWLEDGE-GRAPH.md` — full read to confirm navigation conventions.

## Part 1 — cross-finding-026 §13 amendment (4-cell typology)

Appended §13 "Amendment 2026-04-28: 4-cell typology" to `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` (in place; no rewrite of §1-§12). The amendment:

- Cites the Q 24 specialist's motivating finding: top-5 UAS (rank 5) + top-3 outlier-strength (+23.51 pp, rank 3) + both-side top-15 adjacency-cost (Q 23-Q 24 rank 11 + Q 24-Q 25 rank 5 = 6.04% combined) + sig_A = -0.79 rank 82/114. Source: `surahs/Q024-al-nur/01-empirical-profile.md` §11 + `05-classical-claims-audit.md` §2.
- Documents the 4-cell typology with Q 24 + Q 33 as the *Structural-twin-pair* cell (only 2 surahs in the corpus with both adjacencies in top-15 by H-NEW-720 cost). Sources: Q 24 + Q 33 empirical-profiles.
- Integrates the Q 9 specialist's chronology-driven adjacency-cost finding (Q9-Q10 = 4th-most-expensive at 3.73%, muqaṭṭaʿāt-onset control falsified). Source: `surahs/Q009-al-tawba/06-novel-findings.md` Q009-F-03.
- Integrates the Q 12 specialist's q-s-s head-tail bookend finding. Source: `surahs/Q012-yusuf/06-novel-findings.md` Q012-F-04.
- Integrates the Q 33 specialist's 5-test cluster-cohesion verdict (1 length-ctrl-pass, 4 NULL/FALSIFIED) confirming Q 33's macro-structural (not local-cluster) outlier signature. Source: `surahs/Q033-al-ahzab/06-novel-findings.md`.
- Notes the cross-finding-027 candidate (5th cell, *iʿjāz al-takrīr*, in flight) anchored by Q 55's 31-fold refrain + 23× dual-pronoun density + corpus-min sig_A. Source: `surahs/Q055-al-rahman/06-novel-findings.md` §"Synthesis".

The amendment leaves §1-§12 (the 3-axis quantitative law, TSP-residual decomposition, classical lock table, 4 architectural laws) **unchanged**. The 3-cell vs 4-cell shift is at the per-surah resolution, not at the corpus-law level.

## Part 2 — MASTER-FINDINGS-LEDGER §9 (Wave 2026-04-28 Per-Surah)

Appended a new §9 with subsections per surah (9.1-9.7), a falsifications subsection (9.8 with 8 entries), a vindications subsection (9.9 with 9 entries), and a NEW corpus-wide structural facts subsection (9.10 with 8 entries). Every claim is grounded in a specific specialist file path and pre-reg SHA where applicable. The 5-bullet per-surah summaries cover: (a) pre-registered novel test results with verdicts; (b) classical-claims-audit verdicts; (c) NEW corpus-wide structural facts; (d) cross-corpus implications where the specialist flagged them.

Verified the 7 Wave A/B surahs are all referenced with full file paths:
- §9.1 Q 1 al-Fātiḥa — Wave A (5 pre-reg tests + 7 classical claims).
- §9.2 Q 2 al-Baqara — Wave A (5 pre-reg tests + 10 classical claims).
- §9.3 Q 9 al-Tawba — Wave B (4 pre-reg tests + 8 classical claims).
- §9.4 Q 12 Yūsuf — Wave B (4 pre-reg tests + 7 classical claims).
- §9.5 Q 24 al-Nūr — Wave B (4 pre-reg tests + 8 classical claims).
- §9.6 Q 33 al-Aḥzāb — Wave B (5 pre-reg tests + 6 classical claims).
- §9.7 Q 55 al-Raḥmān — Wave B (5 pre-reg tests + 6 classical claims).

The headline-level "last-updated" footer was updated to flag the §9 addition.

## Part 3 — KNOWLEDGE-GRAPH per-surah navigation

Inserted a new "PER-SURAH INVESTIGATIONS (Wave A + Wave B, 2026-04-28)" section before the METHODOLOGY GUARDS section. Includes:

- Wikilinks to all 7 surah folders' 8-file template + per-surah-novel-tests indexed by Q{NNN}-F-NN.
- The 4-cell typology summary with assignment of Q 1 → All-axis, Q 24/Q 33 → Structural-twin-pair, Q 55 → 5th-cell candidate (cross-finding-027 in flight).
- Falsifications + vindications + new structural facts summary referencing MASTER-FINDINGS-LEDGER §9.8-9.10.
- Updated CLASSICAL SCHOLARS anchor map with 8 scholar-section additions (al-Bukhārī per-surah, al-Tirmidhī per-surah, al-Suyūṭī *al-Itqān* per-surah, al-Qurṭubī, al-Ṭabarsī, al-Thaʿlabī, al-Biqāʿī, al-Bayhaqī) + per-surah extensions to al-Bāqillānī and al-Khaṭṭābī.
- Explicit "Queued: cross-finding-027" sub-section noting the 5th-cell candidate awaiting cross-surah evaluation.

## Anti-hallucination discipline

Every numerical claim in the integration outputs is traceable to a specific on-disk file. No invented ḥadīth numbers (al-Bukhārī #4474, #4674, #4008, #5009, #756, #4797-4798, #3243-3251, #4482-4483 all verified in the audit files). No invented verse references (Q 24:35, Q 33:21, Q 33:40, Q 33:72, Q 9:128-129, Q 12:3, Q 12:5, Q 12:111, Q 2:255, Q 2:282 all verified in source profiles). No invented numerical values (UAS ranks, Δ%ile values, Jaccard scores, FR distances, p-values all traceable to per-surah JSON or audit files).

## Honest limits of the integration

1. The 4-cell typology in cross-finding-026 §13 is based on per-surah resolution from 7 deeply-investigated surahs; the cell-assignment for Q 86, 89, 100, 106, 113 (iʿjāz-al-fawāṣil-pure) and Q 112, 114 (iʿjāz-al-maʿnā) are corpus-level inferences from H-NEW-750/840, NOT from per-surah deep investigations. A future Wave should validate cell-assignment for these via per-surah deep-dives.
2. The cross-finding-027 candidate is **explicitly queued, not asserted as confirmed** — the integration text consistently flags it as "in flight" / "5th-cell candidate" / "pending corpus-level pre-registered LOOCV."
3. The Q 33 amendment retracted the "alif-monorhyme corpus-MAX" framing in `00-overview.md` §5; the master ledger §9.6 and §9.8 now cite the corrected version (rank 11/114, 8 surahs at 100%). The retraction-of-overview action itself is logged in `surahs/Q033-al-ahzab/06-novel-findings.md` and was not separately re-opened during this integration.
4. The Q 55 *ʿarūs al-Qurʾān* hadith attribution is corrected throughout: Mishkāt #2083 / Bayhaqī's *Shuʿab al-Īmān*, NOT al-Tirmidhī #3291 (the project's prior attribution was incorrect; the related Tirmidhī #3375 is a different Jābir hadith). The correction is documented in master ledger §9.7 and KNOWLEDGE-GRAPH al-Tirmidhī entry.
5. Cell boundaries between *Structural-twin-pair* and *All-axis* / *iʿjāz-al-fawāṣil-pure* are 2-element bright lines (Q 24 + Q 33 only); future per-surah investigations may discover additional Structural-twin-pair members or refine Q 9's intermediate position.

## Integration-COMPLETE checklist

- [x] cross-finding-026 §13 amendment in place (in-place append, §1-§12 untouched).
- [x] MASTER-FINDINGS-LEDGER §9 appended (with subsections 9.1-9.10).
- [x] KNOWLEDGE-GRAPH per-surah navigation section inserted (with wikilinks to all 7 folders).
- [x] All 7 Wave A/B surahs (Q 1, 2, 9, 12, 24, 33, 55) referenced in all three deliverables.
- [x] All falsifications cite a specific specialist-file path.
- [x] All vindications cite a specific specialist-file path.
- [x] Cross-finding-027 noted as queued, not asserted.
- [x] Anti-hallucination check: every numerical claim traceable to disk.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
