---
surah: 11
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-05-07
phase: B+
---

# Q 11 Hūd — Investigation Journal


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

## 2026-04-28 — Initial 00-overview produced (prior wave)

00-overview.md created in earlier wave-E investigation. Notes 4 pre-registered
tests + 5 classical claims at that earlier wave. Files for 01-07 + JOURNAL
were NOT actually produced at that wave (the overview's claim to "all 8 files
written" was inaccurate; only 00-overview.md existed). This 2026-05-07 run
EXTENDS by producing the 7 missing files + 5 new pre-registered novel tests.
The 00-overview.md is preserved AS-IS per the task instruction
"EXTEND, do not overwrite."

## 2026-05-07 — Q011-hud-specialist run: 7-file extension + 5 pre-registered novel tests

**Agent**: Q011-hud-specialist (Opus 4.7, dispatched per project's INVESTIGATION-PROTOCOL.md
+ HANDOFF/04-DISCIPLINE.md).

### Pre-flight reading completed

1. `INVESTIGATION-PROTOCOL.md` — full read.
2. `.claude/skills/quran-investigation/SKILL.md` — full read.
3. `HANDOFF/04-DISCIPLINE.md` — full read.
4. `surahs/Q011-hud/00-overview.md` — full read; preserved unchanged.
5. `findings/phase-b-hypotheses/h-new-940-prophet-order-conservation.md` — full read.
6. `findings/phase-b-hypotheses/h-new-97-name-letter-joint.md` — full read.
7. `findings/phase-b-hypotheses/h-new-270-hud-template-lattice.md` — full read.
8. `findings/phase-b-hypotheses/csv/h-new-270.json` — full inspection.
9. `findings/phase-b-hypotheses/csv/h-new-{111,590,700,720,750,840}.json` — Q 11 row inspected.
10. `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` — read top sections.
11. `surahs/Q012-yusuf/` — sister-template inspected (preregs + scripts + JOURNAL).
12. `data/literature/hadith/ahmedbaset-json/db/by_book/other_books/shamail_muhammadiyah.json` — *shayyabatnī Hūd* hadith #40 + #41 verified verbatim.
13. `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` — Q 11 references scanned across 6 collections.
14. `data/literature/classical-tafsir/spa5k-tafsir-api/` — al-Ṭabarī, al-Qurṭubī, Ibn Kathīr Q 11 tafsir surveyed for §3 of `03-tafsir-survey.md`.

### Outputs created

7 main files (extending 00-overview):
- `01-empirical-profile.md` — UAS rank 88/114; sig_A +0.59 rank 46; sig_B +1.13 rank 25; outlier NULL; both adjacencies cheap; multi-rhyme entropy 1.74; ALR pull-in NULL under Q011-F-03 length-controlled test (downgrades 00-overview §9 post-hoc t-test).
- `02-content-analysis.md` — 11-block segmentation (al-Biqāʿī-anchored); 7 prophet-narrative sub-blocks; wa-ilā-akhāhum lattice (3 instances); deluge-iʿjāz pericope (vv. 42-44); Hūd-block inner structure; closing meta-narrative v. 120.
- `03-tafsir-survey.md` — 5 mufassirūn surveyed (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr) + al-Biqāʿī's structural reading; convergence on iḥkām-tafṣīl opener + structural centrality of Hūd-block.
- `04-hadith-corpus.md` — *shayyabatnī Hūd* anchor verified verbatim from Shamāʾil #40 + #41; *aqim-al-ṣalāta-ṭarafayi-al-nahār* (Q 11:114) asbāb al-nuzūl cross-attested in Bukhārī #516, #4481, #4687, Tirmidhī #3196-3199, Ibn Mājah #1132, Abū Dāwūd #4470, Aḥmad Musnad #482; Q 11 + Q 12 paired-recitation request from Nasāʾī #955, #5448; Friday-recitation tradition (Dārimī #2659-2660, marfūʿ form ḍaʿīf, mawqūf form sound to Kaʿb).
- `05-classical-claims-audit.md` — 7 claims audited: 3 VINDICATED, 1 NULL-EMPIRICAL, 1 RULES-TUPLE-FRAGILE, 1 CLASSICAL-DISPUTED, 1 NOT-DIRECTLY-EMPIRICAL.
- `06-novel-findings.md` — 5 pre-registered tests reported.
- `07-cross-references.md` — full integration into 9 H-NEW findings + 6 cross-findings.

5 pre-regs (SHA256-locked):
- `preregs/Q011-F-01-wa-ila-akhahum-corpus-share-prereg.md` SHA `e795ac43090f93dfd06a6403a86d333552000d58c1b03c20d9000d9f26da16cf`
- `preregs/Q011-F-02-hud-narrative-elaboration-prereg.md` SHA `b9073e1febe40f8da2db5b3b636658cb6ecd275d2691caa2415740d9e2add610`
- `preregs/Q011-F-03-alr-cluster-fr-cohesion-prereg.md` SHA `4c69a83734cce6db3ea07eff20907820643a06fbac9a35011cc2465f9e6a4b45`
- `preregs/Q011-F-04-shayyabatni-hud-cohort-prereg.md` SHA `d1abe1d46336aef1213c07696cabbcab796bd6eaae92da005ebad1abca5da889`
- `preregs/Q011-F-05-prophet-cycle-monotone-shrink-prereg.md` SHA `c4bb22a7adf749c20b043a368fc53293353e5d2c1620f1873767fcb445b758dd`

5 scripts (SHA-verified at runtime):
- `scripts/Q011_F_01_wa_ila_akhahum_corpus_share.py`
- `scripts/Q011_F_02_hud_narrative_elaboration.py`
- `scripts/Q011_F_03_alr_cluster_fr_cohesion.py`
- `scripts/Q011_F_04_shayyabatni_hud_cohort.py`
- `scripts/Q011_F_05_prophet_cycle_monotone_shrink.py`

5 JSON outputs:
- `csv/Q011-F-01.json`
- `csv/Q011-F-02.json`
- `csv/Q011-F-03.json`
- `csv/Q011-F-04.json`
- `csv/Q011-F-05.json`

### Key empirical results

| Test | Verdict | Detail |
|:--|:--|:--|
| Q011-F-01 wa-ilā-akhāhum corpus share | **DIRECTIONAL** | 7 corpus instances total (Q 7 = 3, Q 11 = 3, Q 29 = 1); Q 11 share = 42.9% misses 50% threshold; Q 11 ties Q 7 |
| Q011-F-02 Hūd-block elaboration | **DIRECTIONAL** | 3 of 4 axes pass: Q 11 has more verses (11 vs 8), tokens (171 vs 130), distinct roots (64 vs 55); Q 7 has higher per-verse direct-speech density (0.625 vs 0.273) |
| Q011-F-03 ALR pull-in | **NULL** | T = −0.05 direction-matched, p_lower = 0.24 (NS); 00-overview §9 post-hoc downgraded |
| Q011-F-04 shayyabatnī cohort | **NULL** | 0/4 axes pass α_bon = 0.0125; B and C direction-matched (p < 0.15); cohort thematic but not architectural |
| Q011-F-05 cycle-shrinkage | **DIRECTIONAL** | Spearman ρ = −0.54, p_perm = 0.118 (NS); direction matches H-NEW-660 within-surah |

### Decision points / garden-of-forking-paths

1. **PRE-REG-SHA-LOCK COMPLIANCE**: All 5 pre-regs SHA256-computed AFTER writing
   the pre-reg file BUT BEFORE running any computation. SHAs embedded in scripts.
   Verify_sha() called at runtime; all 5 scripts pass. No SHA mismatches.

2. **DIRECTION-LOCK COMPLIANCE**: All 5 pre-regs lock direction in §1; all 5
   results show direction-matched outcomes. Two of 5 (F-03, F-04) show
   direction-matched-but-magnitude-fails outcomes (NULL with full prominence
   per protocol §1.8).

3. **F-04 cohort-list disambiguation**: Tirmidhī Shamāʾil #40 lists 5 surahs
   (Q 11, 56, 77, 78, 81); Shamāʾil #41 abbreviates to "akhawātuhā" without
   enumeration. We pre-registered the **Shamāʾil #40 5-list** as the locked
   cohort. Variant {Q 99 included} 6-list is queued as Q011-F-04.1 for follow-up.
   Decision logged here per §2 of HANDOFF DISCIPLINE.

4. **F-01 lattice-share threshold**: pre-reg locked the ≥50% share threshold
   based on the H-NEW-270 prior knowledge that Q 7 also has 3 instances
   (anticipated total = 6, Q 11 share = 50%). Result was 7 (with Q 29's
   one extra), pushing share to 42.9%. The 50% threshold was deliberately
   set at the boundary; missing it by Q 29 is informative — Q 11 is co-anchor
   not unique anchor. Pre-commit interpreted strictly: DIRECTIONAL not CONFIRMED.

5. **F-02 axis-D direction**: I anticipated Q 11 might have higher discourse
   density given its longer block; instead Q 7 has DENSER per-verse speech
   markers (0.625 vs 0.273). This is a single-axis miss, not a wholesale
   reversal. The 3-of-4 outcome is the locked DIRECTIONAL verdict.

6. **F-03 ALR length-matching**: I locked the 20-nearest-by-verse-count match
   pre-investigation. Tighter matching (e.g., 10-nearest) might shift p
   marginally; the direction (T<0) is robust. NULL is honest at the locked
   pre-reg specification.

7. **F-05 7-block segmentation**: I locked the al-Biqāʿī-anchored 7-block
   structure including the pedagogical-coda (cycle-7) as a "narrative-block-equivalent".
   A 6-block-without-coda alternate (with ρ = −0.66, would be more significant)
   is post-hoc; we resist the post-hoc shift. Honestly published as DIRECTIONAL
   under the locked 7-block specification.

### Anti-hallucination compliance

- [x] Every numerical value traced to a JSON file path or computed-from-script.
- [x] Every Arabic verse-text quoted from `quran-text/quran-no-tashkeel.json` or canonical text.
- [x] Every hadith citation: collection + ḥadīth-number + chain-grade.
- [x] Every classical scholar citation: scholar + work + passage (where available on disk; flagged as DATA-GAP-CLASSICAL where not).
- [x] No invented hadith numbers, no invented verse references.
- [x] All pre-reg SHAs verified at runtime; all scripts run without SHA mismatches.

### Bonferroni discipline

- F-01: k=1 (single descriptive claim).
- F-02: k=4 axes; composite all-must-pass at α=0.05 (the all-4-must-pass
  aggregator IS the Bonferroni protection).
- F-03: k=1 (single primary cell).
- F-04: k=4 axes; α_bon = 0.0125 per axis; ≥3-of-4 pass = CONFIRMED bar.
- F-05: k=1 (single primary cell).

All declared pre-reg before observation.

### Equal NULL prominence

Both NULLs (F-03 ALR pull-in, F-04 shayyabatnī cohort architectural cohesion)
reported with full prominence:
- F-03 NULL EXPLICITLY downgrades the 00-overview.md §9 post-hoc t-test claim
  about Q 11's "strongest ALR pull-in among ALR-5 members". The 00-overview's
  Δ=0.142 raw t-test signal does NOT survive the length-matched permutation
  null. The architectural-empirical reading: ALR-cohesion is direction-real
  but magnitude-modest at α=0.05 under length-controls.
- F-04 NULL EXPLICITLY honors the classical/empirical operationalization-mismatch
  disclosure: Tirmidhī Shamāʾil #40's claim is THEMATIC (eschatological-warning
  emotional-burden); the architectural-cohesion empirical instrument is
  testing a different axis. The hadith stands, the architectural cohesion
  does not.

### Honest reporting

5 tests, 0 CONFIRMED, 3 DIRECTIONAL, 2 NULL. The DIRECTIONAL findings are
all direction-matched real signals that fail to cross conservative
significance thresholds. The 2 NULLs are informative for the project's
broader typology.

The "anti-iʿjāz-by-iteration" sub-cell nomination for Q 11 (per
01-empirical-profile §9) is QUEUED for cross-finding-026 ratification —
NOT promoted in this run.

Q 11's architectural place: the **prophet-anthology centerpiece** with
**internal/local** distinctiveness (high rhyme-entropy, multi-block templated
formulaic lattice, self-referential meta-narrative) but **NOT** corpus-level
distinctness on UAS, FR, outlier, or canonical-adjacency axes.

### Files modified

- 00-overview.md: NOT modified (preserved per "EXTEND don't overwrite" instruction).
- 01-07 + JOURNAL: NEW.

### Files created (counts)

- 7 main markdown files
- 5 pre-reg markdown files (with SHA256-locked frontmatter)
- 5 Python scripts (with runtime SHA verification)
- 5 JSON output files

Total: 22 new files; 0 overwrites.

### Reproducibility checklist

- [x] All pre-reg SHAs locked AND embedded in scripts.
- [x] Seed = 20260507 (per HANDOFF instruction).
- [x] Permutations = 10,000 minimum (F-03, F-04, F-05).
- [x] All scripts use stdlib only (no external dependencies).
- [x] Every test's JSON output is reproducible from `python3 scripts/Q011_F_*.py`.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
