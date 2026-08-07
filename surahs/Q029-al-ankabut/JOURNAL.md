---
surah: 29
surah_name_translit: al-ʿAnkabūt
file_type: journal
date_last_updated: 2026-05-10
phase: B+
---

# Q 29 al-ʿAnkabūt — Investigation Journal


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

## 2026-05-07: Initial template + Q029-F-01

- 00-overview.md, 01-empirical-profile.md, 02-content-analysis.md, 03-tafsir-survey.md, 04-hadith-corpus.md landed.
- Q029-F-01 pre-reg + script + JSON: 5-lemma hapax-count for Q 29:41 surface verse. Result: 2 corpus-hapax (Eankabuwt + >awohan). Verdict: PASS-DIRECTED.
- 03-tafsir-survey.md surveyed ≥ 5 mufassirūn (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, al-Wāḥidī, Jalālayn, Maʿārif, Ibn ʿAbbās attributed, al-Baghawī).
- 04-hadith-corpus.md catalogued Tirmidhī #2468 (imtihān), #3273 (Saʿd asbāb for Q 29:8), #3274 (Lūṭ's evil meetings).
- Cross-references flagged: cross-finding-008 (ALM exception), H-NEW-590 (WEAK_ANCHOR), H-NEW-840 (UAS rank 44).

## 2026-05-09: Q030-F-08 (whole-surah ALM-6 cluster, hosted at Q 30 specialist)

- Q030-F-08 verdict: PARTIAL (Cell A NULL p=0.418, Cell B length-matched PASS p=0.0225).
- Q 29's within-ALM-6 distances captured: closest neighbors Q 3 (0.842), Q 2 (0.849); Q 30 at rank 7/15 (0.915).
- Implication: Q 29 ↔ Q 30 is NOT a tight FR-pair despite both being cross-finding-008 ALM exceptions.

## 2026-05-10 01:00 CDT: Specialist dispatch (this session)

Brief: Q 29 al-ʿAnkabūt deep-dive completion. Pre-registered tests T1, T2, T3 per session brief.

### Pre-flight reading verified
- INVESTIGATION-PROTOCOL.md — read.
- SKILL.md (quran-investigation) — read.
- SESSION-HANDOFF-2026-05-09-PM.md — read.
- Q 29 existing files — read (00-04 + Q029-F-01).
- Q 30 Q030-F-08 reference — read.
- cross-finding-025 + H-NEW-1380 (scale-of-aggregation corollary) — read.

### Garden-of-forking-paths log

- **Decision 1**: T1 pre-reg framed as PERICOPE-scale (first 3 verses) per brief specification.
  - Operational definition of "pericope" = 3-verse window (v 1, v 2, v 3 of each surah).
  - Aggregation = union of QAC v0.4 ROOT-field assignments per pericope.
  - Test statistic = mean of C(4,2)=6 pairwise root-Jaccards.
  - Null = 10,000 length-matched random 3-verse pericopes from the corpus, excluding the 4 observed pericopes.
  - Direction LOCKED before observation: TIGHTER (J_obs > null mean).
  - A-priori prediction per brief: PASS-DIRECTED at pericope-scale (per cross-finding-025-formal).
- **Decision 2**: T2 / Q029-F-03 pre-reg explicitly excludes permutation null — corpus-singleton is a deterministic dictionary fact, not a probabilistic test. Justified in §4 of the pre-reg.
- **Decision 3**: T3 / Q029-F-04 uses a 3-sub-claim composite verdict; the joint-schema sub-claim (c) is the empirical-novelty.
  - Frailty-roots locked at {`whn`, `DEf`}. Other near-synonyms (e.g., *hayy*) excluded.
  - Shelter-lemma locked at `bayot` (the standard Arabic *bayt*). Other dwelling-lemmas (e.g., *manzil*, *maskan*) excluded.
  - These are stipulated operationalizations; alternative classifications would yield different verdicts. The pre-reg locks ONE schema.

### Pre-reg SHAs

| File | SHA256 |
|:--|:--|
| Q029-F-02 ALM-4 pericope cohesion | `3d4acccc01e01985bcdbef1b4dcd4dd5c7005878862dbd291a7159c4406994d8` |
| Q029-F-03 *ʿankabūt* corpus-singleton | `2718837da9e3c5dce8d955da9752a38f654c9cd100f30b81f5751f46b0a2d6a7` |
| Q029-F-04 spider-parable typological uniqueness | `899a4c2201655c2d28e75c8d9c5cde7fa86e65c6a2d2f7794236311453ffebfe` |

### Run order

1. T2 / Q029-F-03 (deterministic singleton verification). Verdict: PASS-DIRECTED.
2. T3 / Q029-F-04 (deterministic typology verification). Verdict: PASS-DIRECTED (3/3 sub-claims).
3. T1 / Q029-F-02 (permutation test). Verdict: NULL — direction REVERSED (J_obs=0.0434 < null mean=0.0497, z=-0.25, p=0.557).

### Honest pre-commit attestation

T1 was pre-registered as PASS-DIRECTED at pericope-scale per the brief's specification of cross-finding-025-formal. The observed direction REVERSED (J_obs < null mean). Per Protocol §1.8 (Honest pre-commit violations), the verdict is published as NULL with full prominence. No post-hoc adjustment to pre-reg. The NULL is informative as a boundary-case for cross-finding-025: even with strong multi-axis correlation (4 ALM-openers + contiguous mushaf + Late-Meccan chronology + 3/4 book-reference), a 3-verse pericope window does NOT drive root-Jaccard cohesion.

### Files written

- preregs/Q029-F-02-alm-4-pericope-cohesion-prereg.md
- preregs/Q029-F-03-ankabut-corpus-singleton-prereg.md
- preregs/Q029-F-04-animal-parable-typology-prereg.md
- scripts/Q029_F_02_alm_4_pericope_cohesion.py
- scripts/Q029_F_03_ankabut_corpus_singleton.py
- scripts/Q029_F_04_animal_parable_typology.py
- csv/Q029-F-02.json
- csv/Q029-F-03.json
- csv/Q029-F-04.json
- 05-classical-claims-audit.md
- 06-novel-findings.md
- 07-cross-references.md
- JOURNAL.md (this file)

### Quality gates

- [x] Pre-reg SHAs locked and embedded in scripts.
- [x] Direction-of-effect locked before observation.
- [x] Bonferroni applied (k=1 each; α=0.05 each).
- [x] Honest limits sections written in each finding file.
- [x] Cross-references include both supporting (Q029-F-03, Q029-F-04) and challenging (Q029-F-02 NULL) findings.
- [x] Classical scholar citations are scholar + work + passage (where on-disk).
- [x] Equal NULL prominence: Q029-F-02 NULL is published with the same prominence as the PASS-DIRECTED results.

## Open follow-ups

1. **Cross-corpus iʿjāz al-tashbīh test**: scan pre-Islamic poetry baseline (`data/baseline-corpora/raw/`) for the animal-shelter-fragility schema; required for full al-Bāqillānī claim verification.
2. **Q 29:8 ↔ Q 31:14-15 verse-twin quantitative ranking**: queued.
3. **Pericope-window sensitivity**: re-run Q029-F-02 at 5-verse, 7-verse, 10-verse windows to find the cohesion-onset scale (if any).
4. **al-Rāzī page-citation**: physical-edition lookup for *Mafātīḥ al-ghayb* on Q 29:41 (MW-6 PENDING).
5. **Tirmidhī #2468 + #3273 grading verification**: physical-edition lookup for *ḥasan ṣaḥīḥ* tags (MW-6 PENDING).
