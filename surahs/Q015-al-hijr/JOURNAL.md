---
surah: 15
surah_name_ar: الحجر
surah_name_translit: al-Ḥijr
file_type: journal
date_created: 2026-05-08
phase: B+
---

# Q 15 al-Ḥijr — Investigation Journal

## 2026-05-08 — Specialist run (Q014-Q015-ALR-completer)

### Setup
- Prior state: Q015-al-hijr folder existed with empty `csv/`, `preregs/`, `scripts/` subdirs; no template files (00-overview through 07-cross-references) had been written.
- Pre-flight read: `INVESTIGATION-PROTOCOL.md`, `HANDOFF/04-DISCIPLINE.md`, `surahs/Q012-yusuf/` template, `surahs/Q013-al-rad/` (sibling specialist), `surahs/Q011-hud/`, `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md`.
- Empirical anchors loaded: `findings/phase-b-hypotheses/csv/h-new-{111, 590, 700, 720, 750, 840}.json`. Q15 row keys verified for surah=15 across all artifacts.

### Computational confirmations
- FR matrix loaded from `h-new-111.json` `D_matrix_upper_triangular`. Q 15's FR-nearest = Q 51 al-Dhāriyāt at 0.7788. Q 15's mushaf-adjacent neighbours (Q 14, Q 16) are NOT in Q 15's top-5 FR-nearest.
- Q 15 UAS rank 38/114 (UAS=0.439); sig_A rank 81/114 (−0.765, NEGATIVE); sig_B rank 86/114 (−1.087); rhyme entropy z=−0.42 (near-monorhyme on ن at 82%).
- H-NEW-590 X=15 row: WEAK_OUTLIER classification (delta_pct=+5.51, p_greater_W=0.3473). Q 15 IS modestly content-distinct from its mushaf cohort.
- H-NEW-720 s=14 (Q14→Q15): 0.1988 (top-15 EXPENSIVE); s=15 (Q15→Q16): 0.1698 (top-20 EXPENSIVE).

### Pre-test informational scan (for prereg formulation, NOT result-viewing)
- Computed Iblīs-rebellion lexical comparison across 6 blocks (Q 7, 15, 17, 18, 20, 38). Q 15:28-44 has 5 hapax + 20 near-hapax; Q 7:11-25 has 22 hapax (more); Q 17:61-65 has 18.0% hapax-density (higher). This informed the Q015-F-01 pre-reg with a CONSERVATIVE direction (≥3 hapax) rather than "highest hapax".
- Computed Q 15:9 corpus-uniqueness: confirmed as the unique verse joining all 3 constructions (a) *naḥnu nazzalnā*, (b) *nazzalnā al-dhikr*, (c) *lahu la-ḥāfiẓūn* with revealed-text referent.
- Computed Q 11/15/26/29 prophet-densities: Q 15 = 4.50/1000w (LOWEST); Q 26 = 15.52; Q 29 = 16.28; Q 11 = 21.60. Q 15 is dramatically lowest.

### Pre-registration (locked 2026-05-08)
- Q015-F-01 pre-reg written to `preregs/Q015-F-01-iblis-rebellion-lexical-prereg.md`. SHA: `34f850fd9a0b022d40619db6a3dcae713b9b9ad4694a18e93051b9ba6368562b`.
- Q015-F-02 pre-reg written to `preregs/Q015-F-02-q159-textual-preservation-prereg.md`. SHA: `8d0a1fc2aed12ac29e4a15cc02bfe43b460f6b7999be1306bb0d47ec163e3133`.
- Q015-F-03 pre-reg written to `preregs/Q015-F-03-prophet-density-vs-q11-26-29-prereg.md`. SHA: `dd4a3834537da9f17efe3a4851cf31fd16a66e0a3537eb989ca7461706fb0a89`.
- Bonferroni-k = 3 (locked in YAML frontmatter of all 3 pre-regs); α_bon = 0.0167.

### Run script
- `scripts/Q015_F_all_tests.py` written with embedded SHA verification, seed 20260508.
- Run executed: 2026-05-08. All 3 SHA-OK. JSON outputs written to `csv/Q015-F-{01,02,03}.json` and `csv/Q015-F-family-summary.json`.

### Verdicts
- **Q015-F-01: PASS-DIRECTED** — Q 15:28-44 contains 5 corpus-hapax tokens (≥3 threshold met). Cross-block-dominance not achieved: Q 7:11-25 has 22 hapax, Q 20:115-126 has 18 hapax. Q 15 has the LONGEST and most-developed rebellion-discourse but NOT the highest hapax-count.
- **Q015-F-02: CONFIRMED** — Q 15:9 is corpus-UNIQUE in the combined construction (a + b + c) with revealed-text referent for (c). Q 15:9 is the only verse in the entire 6,236-verse corpus where divine-self-reference + revelation-of-the-Reminder + divine-guardianship-of-the-Reminder are joined.
- **Q015-F-03: CONFIRMED** — Q 15 prophet-density 4.50/1000w is the LOWEST among {Q 11, 15, 26, 29}. Q 11 = 21.60 (highest); Q 26 = 15.52; Q 29 = 16.28. Q 15's prophet-density is 4.8× lower than Q 11's.

### Hadith number verification
- **Bukhārī #4273, #4441, #4474, #4497, #4498, #4799**: VERIFIED for Q 15:87 (al-mathānī = al-Fātiḥa). Bukhārī #4498 most-explicit verse-anchor (umm al-Qurʾān = al-sabʿ al-mathānī).
- **Bukhārī #3240, #4226, #4496**: VERIFIED for Q 15:80-84 (Hijr-tribe / Madāʾin Ṣāliḥ tradition; Prophet's prohibition of entry without weeping).
- **Abū Dāwūd #1460 + Nasāʾī #917**: VERIFIED for the alternative *al-sabʿ al-ṭiwāl* tradition (the seven LONG surahs as al-mathānī).
- Q 15:9 textual-preservation: NOT-FOUND as a direct verse-quoting Prophetic hadith in 9-book corpus. Anchored at tafsir + iʿjāz-literature level only.
- Q 15:28-44 Iblīs-rebellion: NOT-FOUND as direct Q 15:28-44 verse-citation in Prophetic hadith. Adam-creation traditions (Bukhārī #3326, #6227) are related but not direct verse-citations.

### Files written
- `00-overview.md`, `01-empirical-profile.md`, `02-content-analysis.md`, `03-tafsir-survey.md`, `04-hadith-corpus.md`, `05-classical-claims-audit.md`, `06-novel-findings.md`, `07-cross-references.md`, `JOURNAL.md` (this file).
- `preregs/Q015-F-01-iblis-rebellion-lexical-prereg.md`
- `preregs/Q015-F-02-q159-textual-preservation-prereg.md`
- `preregs/Q015-F-03-prophet-density-vs-q11-26-29-prereg.md`
- `scripts/Q015_F_all_tests.py` (top-level scripts directory)
- `csv/Q015-F-01.json`, `csv/Q015-F-02.json`, `csv/Q015-F-03.json`, `csv/Q015-F-family-summary.json`

### Discipline notes (Bonferroni asymmetry, direction-locking)
- Bonferroni-k = 3 was determined BEFORE running any test. The k=3 family is fixed: Q015-F-01, F-02, F-03. No mid-flight tightening or loosening.
- Direction was locked in pre-reg YAML frontmatter for each test:
  - F-01: ≥3 hapax tokens.
  - F-02: corpus-unique combined construction at Q 15:9.
  - F-03: Q 15 prophet-density LOWEST of {Q 11, 15, 26, 29}.
- All 3 directions matched empirically. Q015-F-01 has primary-direction PASS but secondary cross-block-dominance NOT achieved (publishing as PASS-DIRECTED rather than CONFIRMED is the intellectually-honest verdict).
- No pre-commit violations.

### Cross-finding context updates queued
- cross-finding-026 §4 "classical-attention → empirical-MAX" inventory: add Q 15:9 corpus-unique textual-preservation construction (Q015-F-02).
- cross-finding-026 §13 architectural-cell typology: Q 15 confirmed as a member of the iterative-narrative-near-monorhyme sig_A-negative cell {Q 12, Q 15, Q 36}.
- H-NEW-610 letter-family-content-NULL framework: Q 15's ALR-distance also non-distinctive (consistent with prior NULL).

### Iblīs-typology axis documentation
- **Q 14:22** (post-judgment-eschatological-self-disavowal) + **Q 15:28-44** (pre-creation-rebellion-with-God) jointly span the corpus's CLEAREST typological axis on Iblīs-discourse. Mushaf-adjacency Q 14 + Q 15 contains the **complete temporal-axis of Iblīs-discourse** — pre-creation and post-judgment as the two ends.
- This is documented in both `surahs/Q014-ibrahim/07-cross-references.md` §4 and `surahs/Q015-al-hijr/07-cross-references.md` §4.

### Next-agent / follow-on items
- F-04 (queued): test the *aṣḥāb al-Ḥijr* (Q 15:80) corpus-uniqueness against other tribe-collectives (*aṣḥāb al-Ayka*, *aṣḥāb al-Rass*, *aṣḥāb al-Akhdūd*, *aṣḥāb al-fīl*, etc.).
- F-05 (queued): Q 15 → Q 16 munāsabah audit at the canonical-adjacency-cost-of-0.17 level (rank-17 expensive seam) vs al-Biqāʿī's qualitative claim of cohesion.
- Cross-replication: Q015-F-02's corpus-uniqueness could be tested across alternative orthographic conventions (Uthmani-consonantal, full-tashkeel) to verify the rules-tuple invariance.

### Honest reporting note
- Q015-F-01's PASS-DIRECTED verdict is published with full prominence rather than promoted to CONFIRMED. The cross-block-dominance comparison (Q 15:28-44 vs Q 7:11-25, Q 20:115-126) shows that Q 15 is NOT the most-hapax-dense Iblīs-rebellion block. The classical claim is more accurately about Q 15's narrative-development (longest fully-articulated rebellion-with-respite-and-vow-and-exclusion sequence), not hapax-vocabulary-uniqueness.
- Q015-F-02 (Q 15:9 corpus-unique) is the strongest empirical anchor of the 3 tests — a deterministic corpus-uniqueness verification with 0 confounds.
- Q015-F-03 (Q 15 lowest prophet-density of the 4-surah set) is empirically clean and direction-matched. Q 15 is structurally a *sparse-naming, dense-narrative* surah.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
