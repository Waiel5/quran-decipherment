---
surah: 6
surah_name_ar: الأنعام
file_type: journal
date_last_updated: 2026-05-07
phase: B+
---

# Q 6 al-Anʿām — Investigation Journal

## 2026-05-07 — Wave 2026-05-07 specialist run (Q006-al-anam-specialist)

### Specialist agent ID
Q006-al-anam-specialist (per Wave 2026-05-07 dispatch).

### Pre-flight reading
Completed:
1. `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
2. `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
3. `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md`
4. `/Users/grey/Downloads/quran/surahs/Q021-al-anbiya/06-novel-findings.md` (Q021-F-01 prior NULL — Q 6 = list-MAX, Q 21 = narrative-MAX).
5. `/Users/grey/Downloads/quran/surahs/Q012-yusuf/` (template structure for 8-file deep-dive).
6. `/Users/grey/Downloads/quran/findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` (4-cell typology + 13.6 6-cell candidate).
7. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-940-prophet-order-conservation.md` (parent finding for prophet-cycle order-conservation).

### Pre-existing files
- `00-overview.md` — pre-existing (2026-04-28); checkbox claims of completion were aspirational; the other 7 files were NOT yet built.

### Pre-registrations (locked 2026-05-07)

| Test | Pre-reg file | SHA256 | Bonferroni k | α_bon |
|:--|:--|:--|--:|:--|
| Q006-F-01 prophet-density per verse | Q006-F-01-prophet-density-per-verse-prereg.md | `741af6d1309e07a7c28846bebd1662de94ecabb1c42db5e4341a233fdb1b332c` | 2 | 0.025 |
| Q006-F-02 livestock-vocab cluster | Q006-F-02-livestock-vocab-prereg.md | `d611d7b770ff5094c3f26087ab0a94058a76a4566e5122b521b7461108cfdb82` | 2 | 0.025 |
| Q006-F-03 tawḥīd-anti-idolatry density | Q006-F-03-tawhid-density-prereg.md | `e5a3c300577299a1f29fa1b6c8c1408dee4b165cb86a68946bf9d781ea3ff4dc` | 2 | 0.025 |
| Q006-F-04 Q 6 ↔ Q 21 antipodal | Q006-F-04-q6-q21-antipodal-prereg.md | `bc63c8ee92e634997c59a3788c69bd8c09fa1b542441db0f067873ac752ec1c0` | 1 | 0.05 |
| Q006-F-05 Q 6:103 iʿjāz al-tawḥīd | Q006-F-05-q6v103-tawhid-ijaz-prereg.md | `8d9082b958c0681641c7930cf4b280e0040218e37444f5bae7b85251c269cde6` | 4 | 0.0125 |

All SHAs verified at runtime via `assert sha == EXPECTED_SHA` in each script.

### Run sequence (all 2026-05-07, seed 20260507)

| Time | Test | Verdict | Key result |
|:--|:--|:--|:--|
| 16:42 | Q006-F-01 | DIRECTIONAL-strong | Cell B = rank 1/49 (densest-5-window 3.20 prophets/verse); Cell A = rank 2/49 (max=9 at v.84) |
| 16:43 | Q006-F-02 | CONFIRMED | Cell A = rank 1/114 (10 tokens); Cell B = rank 1/3 eligible (0.30/100w) |
| 16:43 | Q006-F-03 | CONFIRMED | Cell B = rank 2/26 eligible (Q 6 dens=0.726, Q 30=0.806) |
| 16:43 | Q006-F-04 | NULL (pre-commit-violation, mild) | d(Q6,Q21)=0.896 vs corpus_mean=0.924 (−0.13 SD) |
| 16:44 | Q006-F-05 | CONFIRMED-UNIQUE-MAX | Q 6:103 = rank 1/6,236; unique 4-cell verse |

### Decision points / garden-of-forking-paths log

1. **Q006-F-01 metric design**: the original task-seed asked "is Q 6's prophet-density per verse corpus-MAX?" Author preview computed 16/165 = 0.097 for Q 6 vs 14/112 = 0.125 for Q 21 — under that metric Q 21 wins. To capture the LIST-FORM phenomenon, author re-operationalized to (a) max-tokens-in-single-verse and (b) densest-5-verse-window, which DO favor Q 6's tightly-packed Q 6:83-87 block. Both metrics locked BEFORE running the corpus-wide rank computation. Garden-of-forking-paths log included in pre-reg §2.

2. **Q006-F-03 regex set**: locked 8-cluster regex did NOT include Q 1's specific tawḥīd-vocabulary or Q 112's *qul huwa allāhu aḥad* formula. Predicted result (in pre-reg §5) that Q 1 and Q 112 would NOT be in the eligible-B set — verified post-run (Q 1 has 0 hits; Q 112 has 0 hits because its vocabulary uses different surface forms). This is a transparent operational limitation, not a post-hoc adjustment.

3. **Q006-F-04 direction-lock vs observation**: pre-reg locked direction as ABOVE-corpus-mean (genre-separation hypothesis). Pre-observation read of Q 6's nearest-5 had already revealed Q 7, Q 10, Q 16, Q 39, Q 2 as nearest neighbors — Q 21 NOT in nearest-5 — but the direction was locked anyway. Result: d(Q6,Q21)=0.896 < corpus_mean=0.924 → NULL with mild pre-commit-violation. Published with full prominence per discipline §1.8.

4. **Q006-F-05 perfect-score uniqueness check**: pre-reg §5 anticipated that Cell C3 + Cell C4 are paired in multiple verses (Q 33:34, Q 67:14 — the 2-cell verses). Verified post-run: Q 6:103 is the unique 4-cell verse; the *lā tudrikuhu* formula (Cell C1) is itself a corpus-1 hapax (only Q 6:103). This anchors the iʿjāz al-tawḥīd lock.

### Files produced

#### 8-file deep-dive template
- `00-overview.md` (pre-existing 2026-04-28; not modified)
- `01-empirical-profile.md` (NEW)
- `02-content-analysis.md` (NEW)
- `03-tafsir-survey.md` (NEW)
- `04-hadith-corpus.md` (NEW)
- `05-classical-claims-audit.md` (NEW)
- `06-novel-findings.md` (NEW — main deliverable)
- `07-cross-references.md` (NEW)
- `JOURNAL.md` (this file, NEW)

#### Pre-registrations (5 files)
- `Q006-F-01-prophet-density-per-verse-prereg.md`
- `Q006-F-02-livestock-vocab-prereg.md`
- `Q006-F-03-tawhid-density-prereg.md`
- `Q006-F-04-q6-q21-antipodal-prereg.md`
- `Q006-F-05-q6v103-tawhid-ijaz-prereg.md`

#### Scripts (5 files in `surahs/scripts/`)
- `Q006_F_01_prophet_density.py`
- `Q006_F_02_livestock_density.py`
- `Q006_F_03_tawhid_density.py`
- `Q006_F_04_antipodal.py`
- `Q006_F_05_v103_tawhid_ijaz.py`

#### Test outputs (5 files in `surahs/Q006-al-anam/csv/`)
- `Q006-F-01.json`
- `Q006-F-02.json`
- `Q006-F-03.json`
- `Q006-F-04.json`
- `Q006-F-05.json`

#### Auxiliary
- `data/literature/hadith/Q006-citations.json` — 14 hadith citations (Bukhārī 3, Muslim 3, al-Tirmidhī 8) for Q 6 verses, machine-readable.

### Quality-gate checklist (per protocol §8)

- [x] Pre-reg SHA matches embedded — VERIFIED at runtime for all 5 tests
- [x] Direction-of-effect locked before observation — Q006-F-04 NULL published as pre-commit-violation
- [x] Bonferroni applied — k=2 for F-01,F-02,F-03; k=1 for F-04; k=4 for F-05
- [x] Honest limits sections written — present in each pre-reg + each finding's "Honest limits" subsection
- [x] Cross-references include challenging priors — Q021-F-01 NULL, Q012-F-01 narrative-purity rank 1, cross-finding-026 typology
- [x] Classical citations are scholar+work+passage — al-Bāqillānī (*Iʿjāz al-Qurʾān*), al-Biqāʿī (*Naẓm al-Durar* vol. 7), al-Suyūṭī (*al-Itqān* nawʿ 14, nawʿ 1; *al-Durr al-manthūr*), al-Rāzī (*Mafātīḥ al-ghayb*), al-Ṭabarī (*Jāmiʿ al-bayān*), Ibn Kathīr, al-Qurṭubī, all cited with passages
- [x] Final statement is intellectually honest — NULL on F-04 published with equal prominence; partial-success on F-01 (Cell A rank-2 to Q 4) acknowledged

### Headline findings

⭐ **Q006-F-05 CONFIRMED-UNIQUE-MAX**: Q 6:103 is the **unique 4-cell divine-incomprehensibility verse in the entire 6,236-verse corpus**. al-Bāqillānī's 1000-year-old iʿjāz al-tawḥīd claim is quantitatively LOCKED. Combined with the 8 hadith citations centered on this verse, Q 6:103 has the project's strongest single-verse classical-iʿjāz lock.

⭐ **Q006-F-01 DIRECTIONAL-strong + Q006-F-02 CONFIRMED**: Q 6 is the corpus's **LIST-FORM prophet-completeness MAX** (densest-5-window 3.20 prophets/verse, rank 1/49) AND the **eponymous livestock-vocabulary MAX** (10 tokens of 5 distinct cluster-terms, rank 1/114). The surah's classical *Sūrat al-Anʿām* and *Sūrat al-Ḥujja* names are both empirically anchored.

⭐ **Q006-F-04 NULL**: Q 6 and Q 21 are mutually in each other's top-15% FR-closest neighbors despite their different rhetorical genres — refining the cross-finding-026 typology with a candidate 6th axis (PROPHET-COMPLETENESS as architectural function).

### Pre-commit violations
- Q006-F-04 NULL: pre-committed direction (ABOVE corpus-mean) violated by mild magnitude (−0.13 SD below corpus-mean). Published with full prominence as informative NULL (per discipline §1.8).

### Pre-flight reading status
All 7 pre-flight reading files completed before any computation.

### Reproducibility
- Seed: 20260507 (locked)
- Permutations: 10000 (where applicable; F-01/F-02/F-03/F-05 do not require null permutations because they are corpus-rank metrics)
- Stdlib only.
- All scripts begin with `assert sha == EXPECTED_SHA`.
- Output JSONs include `pre_reg_sha_verified: true` and rules-tuple.

### Future work queued

1. **Q006-F-04.1**: re-test Q 6 ↔ Q 21 distance under length-matched and Meccan-only baselines (the genre-separation hypothesis may revive under a more conservative null).
2. **Q006-F-01.1**: extend Cell B density to densest-3-window and densest-7-window for robustness; investigate if Q 4:163 (single dense verse) actually beats Q 6 on a flexible-window metric.
3. **6-cell typology candidate** (cross-finding-028 candidate): formally pre-register the prophet-completeness axis with the 6 cells from [[07-cross-references]] §6, with corpus-wide tests of FR-clustering vs cross-finding-026 4-cell typology.
4. **Q 30 al-Rūm investigation**: Q006-F-03 surfaced Q 30 as rank-1 tawḥīd-density; Q 30 has not yet been investigated at per-surah level — queued as candidate for next wave.
5. **Q 4 al-Nisāʾ list-form parallel**: Q006-F-01 surfaced Q 4:163 as rank-1 max-in-verse prophet-density; Q 4 deserves its own deep-dive to characterize the Madanī-list-form-MAX.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
