---
surah: 22
file_type: journal
date_last_updated: 2026-05-09
phase: B+
---

# Q 22 al-Ḥajj — Investigation Journal

## 2026-05-07 — Wave-1 specialist landing (5 tests)

**Specialist**: Q022-al-hajj-specialist (initial dispatch).

**Pre-registrations locked**:
- Q022-F-01-sajda-cosmic-language-prereg.md (SHA 21ad857d3e8dc676a58e854a3ba0a570147ff0e132cd9a1c272df2a64fb5a14e)
- Q022-F-02-hybrid-bimodality-prereg.md (SHA dc4b798edd9bc908ba3a1e548b2985e4151f418f7862587d63f4c87be59d9654)
- Q022-F-03-true-isolate-persistence-prereg.md (SHA 2b9d468b511b4d8ac46cd900fee7d7b8a5eba81f7271bc10bcd5435c6988c88b)
- Q022-F-04-pilgrimage-density-prereg.md (SHA c7c74ebef135dff2c758949f1e63cf7f76632da483d55883debda04aa5b93331)
- Q022-F-05-q21-q22-q23-triplet-prereg.md (SHA 3504a184dbee8899741cabe482fbde99a905f1455b74be6d2b8a03a4136cd7e1)

**Script**: `surahs/Q022-al-hajj/scripts/Q022_run_all.py`
**Run results JSON**: `surahs/Q022-al-hajj/csv/Q022-F-{01..05}.json`
**Seed**: 20260507; n_perm = 10000 each (where applicable).

**Verdicts**:
- Q022-F-01: VINDICATED (3/3 cells; perm p = 0.012)
- Q022-F-02: NULL (dip + Silverman both fail)
- Q022-F-03: NULL (0/8 metrics in top-quartile-isolation)
- Q022-F-04: VINDICATED (rank 2/114, after singleton Q 108)
- Q022-F-05: DEFAULT_VINDICATED_isolate_behavior (triplet rank 74/112, upper-mid)

## 2026-05-09 — Wave-H follow-up landing (3 sajda-finding tests + full 8-file template)

**Specialist**: Q022-al-hajj-specialist (Wave-H continuation; previous session left only preregs+csv but no 00-07 markdown template).

**Wave-H mandate**: integrate the corpus-wide H-NEW-1330 + H-NEW-1331 sajda-finding family into a focused 3-test follow-up centered on Q 22 as the corpus-singleton double-sajda surah; complete the full 8-file template.

**Pre-registrations locked**:
- Q022-F-06-double-sajda-singleton-prereg.md (SHA b218390fc906bbee30b837e677789da6ece02467a714c9e5464b44bb20a33591)
- Q022-F-07-sajda-cluster-upper-half-prereg.md (SHA 2b8c632036cd616adbe78b3517f7ea32bfaa0b4b3cd828147506ed2239a0c875)
- Q022-F-08-sajda-verses-block-boundaries-prereg.md (SHA 4fcf6b9938fa6a24b655a966319690da93a9b5fc8960c5751b26a91910f51d8d)

**Script**: `scripts/Q022_F_06_07_08_sajda_finding.py`
**Run results JSON**: `surahs/Q022-al-hajj/csv/Q022-F-{06,07,08}.json`
**Seed**: 20260509; n_perm = 10000 (where applicable; F-06 is deterministic, F-07 is rank-based, F-08 is descriptive).

**Verdicts**:
- Q022-F-06: VINDICATED (Q 22 is the corpus-singleton; 15 total sajda markers across 14 surahs)
- Q022-F-07: VINDICATED (Q 22 rank 8/14, upper-half = less-cohesive — pre-committed direction)
- Q022-F-08: DIRECTIONAL_SPLIT (v 77 PASS top-30% boundary; v 18 FAIL — the imperative-sajda is structural, the cosmic-roll-call sajda is mid-block)

## Hadith corpus verification (2026-05-09)

Verified on disk:
- Abū Dāwūd #1402 (ʿAmr b. al-ʿĀṣ; *fī sūrati al-Ḥajji sajdatāni*) — `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/abudawud.json` id 1402
- al-Tirmidhī #578 (ʿUqba b. ʿĀmir; *fuḍḍilat sūratu al-Ḥajji bi-anna fīhā sajdatayni*; Tirmidhī grades *laysa bi-dhāka al-qawī*) — `.../tirmidhi.json` id 578 / idInBook 578
- al-Bukhārī Kitāb Sujūd al-Qurʾān (chapter id 17, idInBook 1036-1048): **VERIFIED SILENT** on Q 22 double-sajda. The Sunnī-majority position rests on Sunan-grade attestation, NOT Bukhārī-Muslim ṣaḥīḥayn evidence.

## File deliverables

All 8 template files completed 2026-05-09:
- 00-overview.md — basic facts + double-sajda corpus-singleton + first-jihād + universal-vocative open/close + cross-tafsir + 8-test summary
- 01-empirical-profile.md — UAS, outlier, iʿjāz signature, adjacency cost, FR nearest neighbors, sajda-cluster rank, all H-NEW metrics
- 02-content-analysis.md — block decomposition (I-VII), verse-by-verse, double-sajda typology table
- 03-tafsir-survey.md — 7 mufassirūn (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Biqāʿī, al-Suyūṭī) + summary table
- 04-hadith-corpus.md — Abū Dāwūd #1402 + Tirmidhī #578 + first-permission cluster + Bukhārī silence audit + Maliki dissent
- 05-classical-claims-audit.md — 7 audited classical claims with verdicts (vindicated / null / partial)
- 06-novel-findings.md — full 8-test inventory + cross-finding integration
- 07-cross-references.md — neighbors, clusters (sajda + isolate + vocative + first-jihād), H-NEW integration, classical-scholar cross-references, cross-finding-008/013/015/025/026 connections

## Garden-of-forking-paths log

- 2026-05-09 Wave-H: pre-existing F-01..F-05 preregs+csv+script were left in place from 2026-05-07; no modifications. The 3 new preregs (F-06, F-07, F-08) were added as Wave-H follow-ups with their own seed (20260509) and SHA-locks.
- F-06 chose ۩ glyph count over al-Suyūṭī's textual enumeration because the printed mushaf's glyph IS the canonical inscriptional encoding of "the Quran contains a sajda here." This is text-inscription-level evidence (deterministic) not interpretive evidence.
- F-07 chose strict upper-half threshold (rank > 7) over inclusive (rank ≥ 7) to lock direction sharply. Q22's actual rank = 8, satisfying the strict pre-reg.
- F-08 included a pilot-information disclosure in the pre-reg's Garden-of-forking-paths log because the pilot (during scaffolding) showed the predicted "both pass" was unlikely. The pre-committed direction (BOTH pass) was retained despite pilot showing v18 would likely fail — this honors the pre-reg discipline at the cost of an expected partial-failure. The verdict DIRECTIONAL_SPLIT exactly tracks the pilot prediction.

## Cross-references to project state

- Wave-H session is the 2026-05-09 PM mass-parallel landing; see `HANDOFF/SESSION-HANDOFF-2026-05-09-PM.md`.
- Q022 specialist contributes the second-most empirically-significant landing in Wave-H (after Q 53 al-Najm specialist).
- Q022-F-06 + Q022-F-07 + Q022-F-08 jointly support the marker-thickness rule (cross-finding-025): a single-verse marker (sajda-trigger) does not produce FR-cohesion at the surah-aggregate level, and the specific surah carrying the singleton-double does NOT lift itself out of the less-cohesive half.

## Honest verdict status

| Test | Wave | Pre-committed direction | Empirical direction | Verdict |
|:--|:-:|:--|:--|:--|
| Q022-F-01 | 1 | cosmic-cluster > Q22:77 + median-others | confirmed (0.322 vs 0.000) | VINDICATED |
| Q022-F-02 | 1 | bimodal | unimodal | NULL (pre-commit violation: NONE — direction-locked correctly) |
| Q022-F-03 | 1 | ≥6/8 metrics in top-quartile | 0/8 in top-quartile | NULL (pre-commit violation: NONE) |
| Q022-F-04 | 1 | rate(Q22) > rate(Q2) + rate(Q5) | rate(Q22) 0.31 > Q2 0.23 > Q5 0.14 | VINDICATED |
| Q022-F-05 | 1 | NOT bottom-quartile | upper-mid (rank 74/112) | DEFAULT_VINDICATED |
| Q022-F-06 | H | Q22 unique-double, verses 18+77 | confirmed | VINDICATED |
| Q022-F-07 | H | Q22 rank > 7 of 14 | rank 8 | VINDICATED |
| Q022-F-08 | H | both v18 + v77 in top-30% | v77 YES, v18 NO | DIRECTIONAL_SPLIT |

No pre-commit violations across the 8-test family.

## Next agent recommendations

- Promote Q022-F-08's Type-A vs Type-B sajda typology to a formal pre-registered cross-surah test (compare all 15 sajda-verses' within-surah block-boundary signal).
- Replicate Q022-F-03 on Q 16, Q 21, Q 23, Q 25 to test the H-NEW-126 TRUE-ISOLATE core's FR-roots-instrument-specificity systematically.
- Maliki-rules-tuple replication of Q022-F-06 (single-sajda; under that rule, Q 22 would NOT be the corpus-singleton).
- Integration of Q022 findings into MASTER-FINDINGS-LEDGER §10.45+ (Wave-H Q022 entry).
