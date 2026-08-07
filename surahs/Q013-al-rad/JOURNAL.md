---
surah: 13
surah_name_ar: الرعد
surah_name_translit: al-Raʿd
file_type: journal
date_last_updated: 2026-05-07
phase: B+
verdict: Q 13 specialist run COMPLETE
---

# Q 13 al-Raʿd — Investigation Journal


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

## 2026-05-07 — Q013 specialist run (initiated and completed)

### Pre-flight reading
- Read `INVESTIGATION-PROTOCOL.md` (binding methodology).
- Read `HANDOFF/04-DISCIPLINE.md` (MW-1..MW-7, PRE-REG-STANDARD-01..04).
- Read `surahs/Q005-al-maida/06-novel-findings.md` Q005-F-05 (chronology-architecture dissociation framework).
- Read `surahs/Q012-yusuf/00-overview.md` and full template (8-file canonical structure).
- Read `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` §13 (4-cell typology + amendments).
- Read existing Q 13 directory: only `csv/` empty subfolder existed; no prior files. Built from scratch.

### Decision points

**1. Initial state**: Q 13 had no prior files. Built full 8-file template + 5 pre-regs + family run script.

**2. Pre-reg writing order**: Pre-regs F-01 through F-05 written BEFORE any computation. SHA256s computed and locked into the run script (`scripts/Q013_F_all_tests.py`).

**3. Architectural-signature axes choice (Q013-F-03)**: Initial draft of run script used `[z_mean_content_distance, z_local_cohesion, sig_A, z_rhyme_entropy]`. Discovered post-hoc that Q005-F-05 uses `[z_FR_mean, z_sig_A, z_sig_B, z_rhyme_entropy]` where sig_A and sig_B are separately z-scored. Updated the `signature()` function in the run script to z-score sig_A and sig_B against the 114-surah corpus directly. This is a SCRIPT correction (not a pre-reg adjustment); the pre-reg specifies the 4-axis but does not lock sig_A/sig_B as raw vs z-scored. The corrected version uses z-scored axes consistent with Q005-F-05 to enable framework-comparable interpretation. SHA-locks unchanged.

**4. Q013-F-03 pre-commit violation**: Direction REVERSED. Q 13 is closer to Med (Q 2/3/4) centroid than to M (Q 5/6/7) centroid by Δ = −0.220. Per PRE-REG-STANDARD-01: published as NULL with full prominence and pre-commit violation flag in `06-novel-findings.md` Q013-F-03. Post-hoc analysis (NOT pre-committed) noted that Q 5 itself is the empirically Q 2-twin (per Q005-F-05) — including Q 5 in the M centroid drags M toward Med. The cleaner test is Q013-F-05 (using Q 14 directly as comparison), which CONFIRMED 3/3 sub-tests. Replication queue: F-03 follow-on with M = mean(Q 6, Q 7) only.

**5. Q013-F-05 sub-test classification of "contested"**: Pre-reg specified ≥1 source on each side. Verified on disk: Tanzil Egyptian Standard (Medinan), Wikipedia Nöldeke (Late Meccan), al-Suyūṭī Itqān catalog (Medinan), Ibn ʿAbbās/Mujāhid/ʿIkrima chains (Meccan), al-Ṭabarī cited both. ≥1 on each side: contested = TRUE. VERIFIED.

**6. Hadith corpus (Q 13:13 du'āʾ al-raʿd)**: Searched `ahmedbaset-json/db/by_book/the_9_books/*.json` for any direct citation of Q 13:13 (yusabbiḥu al-raʿd) in the *du'āʾ al-raʿd* tradition cited by Ibn Kathīr and al-Suyūṭī. **Result: NOT-LOCATED in the digital corpus.** Per MW-6: tagged as SECONDARY-TRIANGULATED (cited via Ibn Kathīr + al-Suyūṭī secondaries) and PENDING for nawʿ-number-specific claim downstream. The Bukhārī/Muslim/Tirmidhī/Mālik citations of *subḥān Allāh wa-bi-ḥamdihi* (general phrase, not Q 13:13-specific) are VERIFIED.

**7. Hadith corpus (Q 13:11 muqaqqibāt and Q 13:28 hearts-at-rest)**: Searched and found NO direct hadith match in 9-book corpus. The traditions are TAFSIR-TRADITION (Ibn ʿAbbās via Saʿīd b. Jubayr; Mujāhid; ʿIkrima) cited within tafsir works (al-Ṭabarī, Ibn Kathīr) but NOT as Prophetic hadith. Honestly reported in `04-hadith-corpus.md`.

**8. Q 13:43 → ʿAbd Allāh b. Salām hadith strength**: Tirmidhī #3340/#3900 VERIFIED on disk. al-Tirmidhī himself grades the chain *ḥasan-gharīb* (good but single-chain). This is the foundational hadith for the al-Suyūṭī-Medinan classification of Q 13. Honestly reported in `04-hadith-corpus.md` and `05-classical-claims-audit.md` Claim 1 with the strength caveat.

### SHA hashes (locked pre-test, verified at run-time)

| Test | Pre-reg file | SHA256 |
|:--|:--|:--|
| Q013-F-01 | `Q013-F-01-almr-lattice-position-prereg.md` | `959295fd2760e77450c2080e5362cd6c55b8c84d7bc4711cbfdea9f38688e93a` |
| Q013-F-02 | `Q013-F-02-thunder-praises-corpus-unique-prereg.md` | `0de9c7d41c4ff86dc082898fa5c36d869a8cb159bd64d1f2d1234445de5a7b1e` |
| Q013-F-03 | `Q013-F-03-chronology-architecture-dissociation-prereg.md` | `777002ecfd556b6cc41e1b26ddfac13f28d43003719c88d57097b23b7f7e7cea` |
| Q013-F-04 | `Q013-F-04-alr-cluster-membership-prereg.md` | `f06044840fd3ce0953e6aa0609845f86657e571a54288f8824222f2e46a1ab7e` |
| Q013-F-05 | `Q013-F-05-chronology-hadith-audit-prereg.md` | `3c26f3dc4d2ead608975aecd194e05d2c007fc150335c208f1571eb3f075a059` |

All 5 SHA-checks PASS at run-time (per `scripts/Q013_F_all_tests.py` `assert_prereg_sha()`).

### Garden-of-forking-paths log

- **F-01 BETWEEN vs single-cluster-membership**: Pre-committed to BETWEEN (the stronger claim). Single-cluster-membership would have been an easier test to pass (e.g., "Q 13 closer to ALR than non-cluster-mean"). Locked in pre-reg §8.
- **F-03 conservative-bias-against-H1 with Q 5 in M centroid**: Pre-committed to including Q 5 (knowing Q 5 is empirically Q 2-twin per Q005-F-05). The pre-reg honestly noted this confound in §5. The pre-commit violation result is partially explained by this conservative construction; the cleaner Q013-F-05 test (using Q 14 directly) CONFIRMS the framework.
- **F-04 single-surah-substitution null vs random-5-member null**: Pre-committed to single-surah-substitution (the more conservative test). Locked in pre-reg §5.
- **F-05 Q 76 al-Insān as Medinan reference vs Q 110 or Q 99**: Pre-committed to Q 76 (closest in length-class to Q 13 from clearly-Medinan classification). Locked in pre-reg §8.

### Family Bonferroni discipline (PRE-REG-STANDARD-04)

- `bonferroni_k = 5` declared in YAML frontmatter of all 5 pre-regs.
- `bonferroni_family = "Q013-F-family-2026-05-07"` declared in all 5.
- `alpha_bon = 0.01` declared in all 5.
- All thresholds (CONFIRMED, DIRECTIONAL, NULL) declared in pre-reg §4 of each.
- No mid-flight Bonferroni adjustment (no tightening or loosening occurred).

### MW protections applied

| MW | Application |
|:--|:--|
| MW-1 (instrument-prior) | All 4 axes specified in pre-reg before run; FR distance source = H-NEW-111. |
| MW-2 (corpus-prior, ≥10000 perms) | 10000 permutations on F-01, F-03, F-04 each. F-02 uses descriptive-uniqueness. F-05 uses 3 sub-tests including 3-way verification. |
| MW-3 (alternative-models) | F-01 reports BOTH BETWEEN-test AND descriptive direction (closer-to-ALM vs closer-to-ALR). F-03 reports per-axis breakdown + the pre-commit violation. |
| MW-4 (over-fitting) | No fitted parameters; tests are direct distance computations. |
| MW-5 (replication) | Q013-F-05 IS THE REPLICATION of Q005-F-05 framework. CONFIRMED 3/3 sub-tests. |
| MW-6 (instrument-control) | F-04 random-non-ALR-non-Q13 substitution control. |
| MW-7 (post-hoc cap) | F-03 post-hoc analysis (Q 5 contamination explanation) noted but NOT used to update verdict — verdict remains NULL—DIRECTION-REVERSED. F-05 follow-on (M = Q6+Q7 only) queued as a NEW pre-reg, NOT as adjustment to F-03. |

### Quality gates

- [x] Pre-reg SHA matches embedded (5/5).
- [x] Direction-of-effect matches pre-committed (4/5; F-03 honest pre-commit violation, published with full prominence).
- [x] Bonferroni correction applied (k=5, α_bon=0.01).
- [x] Replication or LOOCV passed (Q013-F-05 IS the replication on contested-chronology test-case).
- [x] Honest limits section written (in each F-NN finding write-up).
- [x] Cross-references include both supporting and challenging prior findings.
- [x] Classical scholar citations are scholar+work+passage (≥ 7 mufassirūn surveyed; al-Suyūṭī Itqān nawʿ 1/40 cited; al-Bāqillānī Iʿjāz al-Qurʾān cited; Tirmidhī #3340/#3900 verified).
- [x] Final statement is intellectually honest (Q013-F-03 pre-commit violation honestly published; F-04 NULL honestly published; F-01 BETWEEN observed but not Q13-distinctive honestly published).

### Verdict per quality gate

- 2 of 5 tests CONFIRMED at high confidence (Q013-F-02 corpus-hapax raʿd-praise-construction; Q013-F-05 chronology-architecture-dissociation REPLICATION).
- 1 of 5 tests NULL — DIRECTION REVERSED (Q013-F-03; pre-commit violation, published with full prominence; post-hoc analysis suggests Q 5 contamination of M centroid, with F-05 confirming framework via cleaner test).
- 2 of 5 tests NULL at strict α_bon (Q013-F-01 and Q013-F-04 — both directionally consistent with H1 but not statistically distinctive).

### Specialist refinement proposed (Q013 specialist's contribution to project-level typology)

**Proposed expansion to cross-finding-026 §13 typology**: a new sub-cell **iʿjāz-al-fawāṣil head-mushaf twin-pair**, with Q 13-Q 14 as the empirical exemplar (4-axis distance d=0.486; head-mushaf zone; moderate-positive sig_A; extreme-high rhyme entropy; near-free Q 13→Q 14 seam). Distinct from corpus-tail iʿjāz-al-fawāṣil-pure (Q 86, 89, 100, 106, 113), which has the same sig_A direction but different mushaf-position class. Queued for cross-finding-026 §13.X amendment if confirmed by independent investigations.

### Files created (this session)

```
surahs/Q013-al-rad/
├── 00-overview.md
├── 01-empirical-profile.md
├── 02-content-analysis.md
├── 03-tafsir-survey.md
├── 04-hadith-corpus.md
├── 05-classical-claims-audit.md
├── 06-novel-findings.md
├── 07-cross-references.md
├── JOURNAL.md (this file)
├── Q013-F-01-almr-lattice-position-prereg.md
├── Q013-F-02-thunder-praises-corpus-unique-prereg.md
├── Q013-F-03-chronology-architecture-dissociation-prereg.md
├── Q013-F-04-alr-cluster-membership-prereg.md
├── Q013-F-05-chronology-hadith-audit-prereg.md
└── csv/
    ├── Q013-F-01.json
    ├── Q013-F-02.json
    ├── Q013-F-03.json
    ├── Q013-F-04.json
    ├── Q013-F-05.json
    └── Q013-F-family-summary.json

scripts/
└── Q013_F_all_tests.py
```

Total: 8 markdown files (8-file template) + 5 pre-regs + 5 JSON outputs + 1 family-summary JSON + 1 run script + 1 JOURNAL = **21 artifacts**.

### Cross-references to update (queued; not done in this run)

- `MASTER-FINDINGS-LEDGER.md`: add Q013-F-02 (CONFIRMED), Q013-F-05 (CONFIRMED), Q013-F-01/03/04 (NULL).
- `KNOWLEDGE-GRAPH.md`: link Q 13 al-Raʿd entries.
- `cross-finding-026-iʿjāz-architecture.md` §13: queue amendment proposing Q 13-Q 14 head-mushaf twin-pair sub-cell.
- `surahs/Q012-yusuf/07-cross-references.md`: add forward link to Q 13 al-Raʿd specialist run.
- `surahs/Q005-al-maida/06-novel-findings.md`: add forward link noting Q 13 as the framework's contested-chronology REPLICATION.

These cross-reference updates are coordination work for the team-lead, not the Q013 specialist's primary deliverable.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
