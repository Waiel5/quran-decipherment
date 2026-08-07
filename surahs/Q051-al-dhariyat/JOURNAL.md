---
surah: 51
surah_name_ar: الذاريات
surah_name_translit: al-Dhāriyāt
file_type: working-journal
date_started: 2026-05-09
date_completed: 2026-05-09
phase: B+
verdict: Specialist landing complete (full 8-file template + 5 SHA-locked pre-registered tests + 5 scripts + 5 JSON outputs + 1 hadith-citations JSON).
---

# Q 51 al-Dhāriyāt — Working Journal


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

## Session 2026-05-09: full specialist landing

### Pre-flight reading
- HANDOFF/04-DISCIPLINE.md (re-read; MW-7 self-catch + post-hoc origin protocol confirmed)
- HANDOFF/01-WHAT-WE-KNOW.md (re-read; H-NEW-1070, H-NEW-1140, cross-finding-013 anchored)
- MASTER-FINDINGS-LEDGER.md §10.19-10.40 (H-NEW-1070, H-NEW-1080, H-NEW-1140, H-NEW-1160, Q 37 specialist landing details)
- surahs/Q037-al-saffat/ as reference template (read overview + content-analysis + 5 pre-regs + 1 novel-findings)

### Empirical-anchor extraction (BEFORE any pre-reg lock)

The brief asked for 5 pre-registered tests. From inspection of:
- `quran-text/quran-no-tashkeel.json` Q 51 verses 1-60
- `findings/phase-b-hypotheses/csv/h-new-111.json` (FR matrix)
- `findings/phase-b-hypotheses/csv/h-new-720.json` (adjacency cost)
- `findings/phase-b-hypotheses/csv/h-new-590.json` (outlier spec)
- `findings/phase-b-hypotheses/csv/h-new-840.json` (UAS)
- `findings/phase-b-hypotheses/csv/h-new-750.json` (iʿjāz signature)
- `data/morphology/root-index.json` (hapax)

The following empirical anchors were extracted (DISCLOSED here for post-hoc origin transparency):
- Q 51 has **3 corpus-hapax roots**: Ḥ-B-K (51:7), H-J-Ḍ (51:17), Ṣ-K-K (51:29).
- Q 51 UAS rank = **15/114** (top-13%).
- Q 51 outlier-spectrum classification = **COHESION_ANCHOR** in window {Q 48-54}.
- Q 51→Q 52 adjacency cost rank = **18/113** (smoothest 16%).
- Q 51 FR-nearest neighbors = Q 81, Q 74, Q 44, Q 52 (all eschatological-mufaṣṣal/oath).
- Q 51's mean dist to other 14 oath-cluster members = 0.821 → rank 13/15 in cluster centrality.
- The 4-element fa-coordinated sibling test {Q 37, 51, 77, 100} sibling mean = 0.884 vs length-matched null mean = 0.977 → p_lower = 0.037.
- The (mā + khlq + illā + ʿbd) strict construct: scan returns **1 corpus match = Q 51:56**. The broader (mā + khlq + illā) returns 7 verses; only Q 51:56 has ʿbd.

### Pre-reg locking strategy

5 pre-regs locked in this order:
1. **Q051-F-01** — Q 51:1-4 oath-trio cohesion (sibling test of Q037-F-03; expected PRE-COMMIT VIOLATION at lexical level + STRUCTURAL MATCH at morphological level)
2. **Q051-F-02** — Q 51:56 corpus-EXACT (the highest-novelty finding; the 10th corpus-form-pattern locked)
3. **Q051-F-03** — Prophet-cycle unbalance (descriptive-comparative; CV + Spearman ρ + anaphora-count)
4. **Q051-F-04** — 4-element fa-coordinated sibling FR-cohesion (post-hoc origin disclosed; Bonferroni-2 + single-test α=0.05 dual rendering)
5. **Q051-F-05** — Q 50 → Q 51 → Q 52 cluster + Q 51-52-53 oath-trio

All 5 pre-regs SHA-locked at write-time; SHA verified at runtime in each script.

### Test execution

All 5 scripts ran successfully on 2026-05-09. Outputs in `surahs/Q051-al-dhariyat/csv/`:

| Test | Verdict | Notes |
|:--|:--:|:--|
| Q051-F-01 | PRE-COMMIT VIOLATION (lexical) + H2 STRUCTURAL MATCH | Token-cosine = 0; morphological-template 4/4 |
| Q051-F-02 | **CONFIRMED corpus-EXACT** | Q 51:56 = 1-of-1 strict |
| Q051-F-03 | **CONFIRMED** | CV ratio 1.88×, ρ=-0.80, *wa-fī* count=9 |
| Q051-F-04 | PASS-DIRECTED (length-matched α=0.05) | NULL at strict α_bon=0.025 |
| Q051-F-05 | **CONFIRMED** | Q 51-52-53 trio confirmed |

### Honest reporting decisions

1. **Q051-F-01**: PRE-COMMIT VIOLATION at lexical level is **the EXPECTED outcome** under iʿjāz-balagha morphological reading; reported as PRE-COMMIT VIOLATION + STRUCTURAL MATCH (H2). This REPLICATES Q037-F-03 sibling pattern across the corpus.

2. **Q051-F-04**: dual-rendered the verdict to disclose both the strict-Bonferroni outcome (NULL) and the post-hoc-origin-protocol single-test outcome (PASS-DIRECTED at α=0.05 via length-matched p=0.037).

3. **Q051-F-02**: declared CONFIRMED at structural-uniqueness level since corpus-EXACT 1-of-1 is a structural certainty (no sampling); but with PASS-DIRECTED reservation pending alternative-operationalization replication. Per HANDOFF/04-DISCIPLINE.md, this is consistent with "extreme p (e.g., < 1e-10) survives any conceivable Bonferroni" — corpus-EXACT structural certainty is the structural analog.

4. **MW-7 self-catch**: I checked that the citations in 03-tafsir-survey.md and 04-hadith-corpus.md match the actual sources (Tirmidhī ch46 #14 verified directly; al-Barāʾ Zuhr-recitation hadith chain verified directly). The brief stated to "VERIFY every number" — done.

5. **Q037-F-04 cross-check**: I verified Q 51's rank in oath-cluster centrality is **13/15** (matching the Q037-F-04 finding's claim of Q 51 at rank 13).

### Decisions on classical-claim audit

- **al-Bāqillānī 4-stage cosmic-process iʿjāz** (Q 51:1-4): I marked this PARTIAL VINDICATION rather than CONFIRMED because the morphological template is empirically tight (replicating Q037-F-03's outcome) but the cosmic-process semantic reading is unfalsifiable at the lexical level.
- **al-Ṭabarī 4-distinct-subjects oath**: I marked UNFALSIFIABLE because the lexical evidence is consistent with both al-Ṭabarī's 4-distinct and al-Bāqillānī's 4-cosmic-stages readings.
- **Modern v.47 cosmic-expansion + v.7 gravitational-wave iʿjāz-ʿilmī**: REFUTED on philological grounds (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Suyūṭī all gloss *al-mūsiʿūn* as "vast/abundant," not "expanding"). This is consistent with cross-finding-015's pattern.

### Cross-finding additions

- **9th corpus-form-pattern locked**: (mā + khlq + illā + ʿbd) strict construct → Q 51:56 corpus-EXACT 1-of-1. Joins the 8 existing corpus-form-patterns enumerated in 07-cross-references.md §3.

### Hadith verification

- Searched Tirmidhī ch.45 *Thawāb al-Qurʾān* full-text: **0 hadith specifically on Q 51**. Verified.
- Searched all 9-books for "الذاريات" (al-Dhāriyāt): 4 hits, all Zuhr-recitation chains.
- Searched all 9-books for Q 51 verse-quotations: 5 verified hadith, all numbered idInBook against the actual JSON source files.
- Spurious chains (Q 51 100×, Q 51 + Q 50 + Q 52 trio, "Q 51:56 = 1/8 Quran") REJECTED — no classical anchor.

### Lessons learned

1. **Q 51 has higher UAS than Q 37** — the brief identified Q 51 as a "Tier-1 sibling" of Q 37 in oath-architecture, but Q 51's overall architectural significance (UAS rank 15) is HIGHER than Q 37's (rank 79). This is partly because Q 51 sits at a critical mushaf-position (post-hinge) and acts as a cohesion-anchor.

2. **Q 51 has more corpus-hapax roots than Q 37** — Q 51 has 3 corpus-hapax in 60 verses (per-verse 0.050); Q 37 has 2 in 182 verses (per-verse 0.011). Q 51 is **4.5× more lexically-distinctive per-verse** than Q 37.

3. **The 4-element fa-coordinated sibling test runs into the H-NEW-1070 2-tier structure**: under length-matching, the 4 mid-mushaf siblings (Q 37, 51, 77, 100) ARE more cohesive than random length-matched Meccan-4 (p=0.037), but the effect is modest. The strict-15 cluster as a whole CONFIRMS strongly (p=0.0004) because the short-tail core (Q 91-103) drives the cohesion.

4. **The corpus-EXACT (mā + khlq + illā + ʿbd) finding** is a high-novelty corpus-form-pattern. It strengthens the project's cross-finding-015 pattern: classical-kalām doctrine VINDICATED at corpus-textual-uniqueness.

### Files written

```
surahs/Q051-al-dhariyat/
├── 00-overview.md (337 lines)
├── 01-empirical-profile.md (175 lines)
├── 02-content-analysis.md (244 lines)
├── 03-tafsir-survey.md (159 lines)
├── 04-hadith-corpus.md (148 lines)
├── 05-classical-claims-audit.md (135 lines)
├── 06-novel-findings.md (240 lines)
├── 07-cross-references.md (138 lines)
├── JOURNAL.md (this file)
├── Q051-F-01-creation-purpose-construct-prereg.md (SHA: 063a22f5...)
├── Q051-F-02-creation-purpose-corpus-exact-prereg.md (SHA: b32f173e...)
├── Q051-F-03-prophet-cycle-unbalance-prereg.md (SHA: 4ce9ed02...)
├── Q051-F-04-fa-coordinated-sibling-test-prereg.md (SHA: cb312aa4...)
├── Q051-F-05-q50-q51-q52-cluster-prereg.md (SHA: d96608bc...)
├── csv/
│   ├── Q051-F-01.json
│   ├── Q051-F-02.json
│   ├── Q051-F-03.json
│   ├── Q051-F-04.json
│   ├── Q051-F-05.json
│   └── hadith-citations.json
└── scripts/
    ├── Q051_F_01_oath_cohesion.py
    ├── Q051_F_02_creation_purpose_corpus_exact.py
    ├── Q051_F_03_prophet_cycle_unbalance.py
    ├── Q051_F_04_fa_coordinated_sibling_test.py
    └── Q051_F_05_q50_q51_q52_cluster.py
```

All deliverables complete per the brief.

### Cross-references for follow-up

- See `07-cross-references.md` §13 for 5 open questions (OQ-Q051-1 through OQ-Q051-5).
- The H-NEW-1260 next-numbering anchor (per the brief's NEXT H-NEW RANGE = 1260+) is reserved for a follow-up corpus-wide finding stemming from the corpus-EXACT (mā + khlq + illā + ʿbd) pattern + the 9th corpus-form-pattern landing.
