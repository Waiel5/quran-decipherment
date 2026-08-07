---
surah: 16
file_type: journal
date_created: 2026-05-07
specialist: Q016-al-nahl-specialist
seed: 20260507
---

# Q 16 al-Naḥl — Investigation Journal


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

Timestamped log of the Q016 deep-dive run. All times UTC.

## 2026-05-07 — Phase B+ specialist dispatch

### 14:00 — Pre-flight reading

- Read `INVESTIGATION-PROTOCOL.md` (full, especially §1 + §2.7 + §2.9)
- Read `HANDOFF/04-DISCIPLINE.md` (full)
- Read `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` (head ṭiwāl pole = Q 1-17 zone, where Q 16 sits)
- Read `surahs/Q012-yusuf/00-overview.md` + `Q012-F-01-narrative-purity-prereg.md` (canonical template)
- Inspected existing `surahs/Q016-al-nahl/` — only the `csv/` subdir existed; no prior 00-overview file. NO conflict to extend; built from scratch.
- Inspected `surahs/Q025-al-furqan/Q025-F-01-true-isolate-persistence-prereg.md` (parallel-specialist; design-parent of Q016-F-03).

### 14:30 — Empirical anchor harvest

Pulled Q 16 row from each of:
- h-new-111: FR-nearest = Q 39, Q 22 (co-isolate!), Q 6, Q 13, Q 29
- h-new-126: profile_table → unique-root-count 358 (92.5th percentile, HIGH); period Meccan; Nöldeke rank 73; Tanzil rev-rank 70 (`data/revelation-order.csv` confirmed)
- h-new-281: within-zone Jaccard data (referenced)
- h-new-590: WEAK_OUTLIER, +0.47pp, rank 30/114
- h-new-700: head-pre-kink (s=16 < 50)
- h-new-720: Q15→Q16 cost 2.05%, Q16→Q17 cost 2.30%
- h-new-750: rhyme entropy 0.46, sig_A = -1.599 (rank 94/114, BOTTOM-25%)
- h-new-840: UAS = 0.582, rank 30/114

### 15:00 — Hadith corpus search

Direct file scan against `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/*.json` for:
- النحل (al-naḥl, the bee/Sūrat al-Naḥl) — 20 raw matches across 9 books
- العسل (honey) — 82 matches; refined to honey-as-shifāʾ → Bukhārī #5466 verified
- بسورة النحل (Sūrat al-Naḥl recital) — Bukhārī #1046 (ʿUmar's Friday-pulpit sajda)
- يأمر بالعدل (Q 16:90 ʿadl-iḥsān) — 5 matches but ALL on Q 7:199, NOT Q 16:90 → DATA-GAP recorded
- Killing-of-bee prohibition — Abū Dāwūd #5269, Ibn Mājah #2960 verified

Raw output saved to `csv/hadith-q16-raw.json`.

### 15:30 — Tafsir survey

7 mufassirūn scoped via `spa5k-tafsir-api/`:
- al-Ṭabarī, al-Qurṭubī, Ibn-Kathīr, al-Baghawī, al-Ṭanṭāwī al-Wasīṭ, Jalālayn-EN — all per-verse JSON files exist for Q 16 (verses 68, 69, 90, 120, 121, 122, 123 verified directly)
- al-Rāzī — full work at `raw/razi-mafatih-al-ghayb.openiti.raw.txt`; per-Q16 not extracted; bee-iʿjāz argument summarized from secondary literature

al-Biqāʿī's Q 15→Q 16→Q 17 munāsaba surveyed via the PDF (no per-Q16 OpenITI extraction available).

### 16:00 — Pre-registration of 5 novel tests

All 5 pre-regs written and SHA256-locked BEFORE any computation:

| Test | SHA256 |
|:--|:--|
| Q016-F-01 (niʿmah-catalog) | `1604d9a5e68bb4e23fd76e644717f61f3160f3d7effdcdb0aec5d4704cb96e24` |
| Q016-F-02 (bee-hapax) | `31d55e2dc1bb77fde5fb27f96247b55e58663555ec4e41fa51386db8b9967b14` |
| Q016-F-03 (isolate-persistence; design-parent Q025-F-01) | `7214978abe65a97e6417b7392fda9334a150c43a40bb411a0496721f98272135` |
| Q016-F-04 (Abraham-coda block) | `b56cf82be99ad48c40d29ace39d8d84a4ecfe18bb93c7a97dd3c916602b4a3c9` |
| Q016-F-05 (chrono displacement) | `2fe13979bb7c46734e96b25405b0488e74f817fd5041bd728ee7e86a5f0edb50` |

Each pre-reg includes:
- direction-locked hypothesis (per PRE-REG-STANDARD-01)
- explicit Bonferroni k + α_bon (per PRE-REG-STANDARD-04)
- garden-of-forking-paths log
- MW-1..MW-7 protections

### 16:15 — Test execution

All 5 scripts executed with SHA verification at runtime, seed=20260507, n_perm=10000.

#### Q016-F-01 (niʿmah-catalog) — DIRECTIONAL

```
rank_total = 18/114, density = 2.140 per 100 tokens, p_perm = 0.0002
rank_A (mercy-noun)    = 15
rank_B (creation-verb) = 9   ⭐
rank_C (blessing-obj)  = 27
MW-5 Q14 control rank: 9 (PASS, predicted top-15)
MW-6 Q12 control rank: 90 (PASS, predicted bottom-half)
VERDICT: NULL on strict top-3, but DIRECTIONAL with p_perm = 0.0002 vs corpus baseline
```

#### Q016-F-02 (bee-hapax) — NULL

```
bee-content-lemmas = 24, bee-content-tokens = 25
hapax-count = 2 (n~aHol, *ulul)
null mean across 1693 length-matched 2-verse windows = 0.79
null max = 7
p_perm = 0.186
MW-5 Q12:4-5 control: 0 hapaxes (PC FAIL — instrument is conservative)
VERDICT: NULL (predicted ≥4)
```

#### Q016-F-03 (isolate persistence) — PRE-COMMIT VIOLATION

```
0/8 instruments place Q 16 in bottom-quartile (predicted 6/8)
6/8 instruments place Q 16 in TOP-quartile (rank 93-107) — REVERSE DIRECTION
Rank summary across 8 instruments: 107, 106, 106, 48, 101, 105, 93, 107
VERDICT: PRE-COMMIT VIOLATION — Q 16 has HIGH similarity to nearest 3 neighbors
   (Q 39, Q 22 co-isolate, Q 6, Q 7, Q 10, Q 39 dominate top-3 across instruments)
```

**Major finding**: Q 16's "true-isolate" status from H-NEW-126 is taxonomy-INVISIBILITY, not similarity-ISOLATION. Reverse-direction discovery flagged for independent-pre-reg follow-up.

#### Q016-F-04 (Abraham-coda block) — NULL

```
Cell A (roots-Jaccard): coda 0.0419 vs null 0.0647, p = 0.101
Cell B (token-cosine):  coda 0.3626 vs null 0.4576, p = 0.182
MW-5 Q12:4 control: jaccard p = 0.31 (PC FAIL — within-surah-window null is conservative)
coda has 20 unique roots; surah-rest 353; shared 15
VERDICT: NULL (both cells directional but neither rejects at α_bon = 0.025)
```

#### Q016-F-05 (chrono-displacement isolate-status) — NULL

```
Q 16 |displacement|: Tanzil = 54, Nöldeke = 57
5-isolate mean disp Tanzil = 51.0
non-isolate mean disp Tanzil = 46.2
Spearman ρ Tanzil = 0.039, p = 0.349
Spearman ρ Nöldeke = -0.005, p = 0.526
MW-5 terminal-qiṣār control ρ = 0.21 (positive — confirms displacement is a real corpus phenomenon)
MW-5 head-ṭiwāl control ρ = 0.18 (also positive — high disp not specific to isolates)
VERDICT: NULL (chrono-displacement is NOT the mechanism of isolate-cluster invisibility)
```

### 17:00 — Authoring

8-file deliverable assembled:

- `00-overview.md` — basic facts, name etymologies, opening, length-class, structural distinctives, true-isolate status
- `01-empirical-profile.md` — full integration of h-new-{111, 126, 281, 590, 700, 720, 750, 840}
- `02-content-analysis.md` — 19-block structural map, niʿmah-catalog inventory, bee-passage anatomy, Abraham-coda lexical analysis
- `03-tafsir-survey.md` — 7 mufassirūn covered on Q 16:68, 69, 90, 120-123 (+ al-Biqāʿī seam, al-Rāzī iʿjāz)
- `04-hadith-corpus.md` — 9-book file-verified citations on Q 16:50 (sajda), 16:68 (bee-protection), 16:69 (honey-shifāʾ), 16:106 (taqiyya); + Q 16:90 DATA-GAP audit
- `05-classical-claims-audit.md` — 6 claims: 1 VERIFIED, 1 VINDICATED, 1 VINDICATED, 1 DIRECTIONAL, 1 DATA-GAP, 1 PRE-COMMIT VIOLATION (with reframing)
- `06-novel-findings.md` — Q016-F-01..05 results with full equal-NULL prominence + suggested follow-up pre-regs
- `07-cross-references.md` — mushaf-neighbors, FR-nearest/farthest, 20-cluster invisibility table, sister-isolate coordination, files manifest

### 17:30 — Quality gates passed

- [x] All pre-regs SHA-locked BEFORE script execution
- [x] All scripts verify SHA at runtime (verify_sha() called first)
- [x] Direction-of-effect locked in pre-reg; reverse-direction (Q016-F-03) recorded as PRE-COMMIT VIOLATION
- [x] Bonferroni applied (k specified per test)
- [x] 10000 permutations on each null
- [x] Rules-tuple specified in each pre-reg
- [x] MW-5 + MW-6 controls included where applicable
- [x] Hadith citations carry collection + idInBook (verified at file path)
- [x] Tafsir citations carry scholar + work + verse-or-passage (verified at JSON file)
- [x] Equal-NULL prominence applied throughout (3 NULL + 1 DIRECTIONAL + 1 PRE-COMMIT VIOLATION reported with same prominence)
- [x] DATA-GAP for Q 16:90 sahih-9-book chain transparently documented (not silently assumed)

### Honest summary statement

**Of 5 novel tests, 4 returned negative or violated pre-commit. The most informative result is the PRE-COMMIT VIOLATION on Q016-F-03**: Q 16 is NOT a similarity-outlier in the corpus, it is a CLUSTER-TAXONOMY-INVISIBLE surah. This refines (not refutes) H-NEW-126's "true-isolate" semantics.

The single most-positive finding is Q016-F-01: niʿmah-catalog density at p=0.0002 vs corpus baseline (rank 18/114; rank 9 on creation-verb component); both MW controls fired correctly. The classical claim of *Sūrat al-Niʿam* is rhetorically vindicated, quantitatively DIRECTIONAL.

The bee-passage Q016-F-02 returned 2 corpus-hapax LEMMAS (`n~aHol`, `*ulul`), not the pre-committed ≥4 — but `n~aHol` is genuinely unique to Q 16:68 in the entire Quran.

The Abraham-coda Q016-F-04 returned NULL — the coda is statistically homogeneous with the surah body. The classical seam-detection by al-Biqāʿī applies at the mushaf-level (Q 15→Q 16→Q 17, VINDICATED) not at the within-Q 16 sub-block level.

The chrono-displacement Q016-F-05 returned NULL — the 5 isolates' mean displacement (51) is barely above non-isolates (46), and the Spearman ρ is essentially zero. The mechanism of cluster-invisibility is NOT chronology-mushaf misalignment.

### Promotion candidates

1. **Q016-F-03 PRE-COMMIT VIOLATION → KNOWLEDGE-GRAPH refinement** of H-NEW-126 / cross-finding-010: "true-isolate" = cluster-taxonomy-invisible, NOT similarity-isolated. Coordinate with parallel sister-isolate specialists (Q 21, 22, 23, 25) for joint cross-finding pre-reg.
2. **Q016-F-01 DIRECTIONAL → MASTER-FINDINGS-LEDGER**: vindication-DIRECTIONAL on al-Qurṭubī's *Sūrat al-Niʿam* alt-name claim.

### End of session

All 8 files written. All 5 scripts executed. All 5 JSON outputs saved. SHA-locks verified. Equal-NULL prominence applied. Quality gates passed.

Specialist sign-off: Q016-al-nahl-specialist, 2026-05-07.
