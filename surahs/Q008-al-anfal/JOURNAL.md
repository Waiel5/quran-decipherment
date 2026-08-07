---
surah: 8
surah_name_ar: الأنفال
surah_name_translit: al-Anfāl
file_type: journal
date_last_updated: 2026-05-09
phase: B+
agent: Q008-al-anfal-specialist
seed: 20260509
---

# Q 8 al-Anfāl — Investigation Journal


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

## 2026-05-09 — Session 1 (Wave-F specialist landing)

### Pre-flight (mandatory reading)
- [x] `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md`
- [x] `/Users/grey/Downloads/quran/HANDOFF/01-WHAT-WE-KNOW.md`
- [x] `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` §10.36-10.43 (Wave-E findings, including H-NEW-1240 13-seamless-seams + H-NEW-1250 Q 55 dual-audience)
- [x] `/Users/grey/Downloads/quran/surahs/Q008-al-anfal/00-overview.md` (existing baseline; carried forward)
- [x] `/Users/grey/Downloads/quran/surahs/Q037-al-saffat/` (template reference for 8-file structure + pre-reg + script discipline)

### Empirical anchor extraction (per-row)
- **h-new-111 (FR matrix)**: Q 8 row computed → mean dist = 1.0745 (well above corpus mean 0.923). Top-10 nearest: Q 3 (0.807), Q 22 (0.851), Q 2 (0.874), Q 48 (0.900), Q 5 (0.902), Q 4 (0.907), Q 60 (0.908), Q 59 (0.909), Q 9 (0.911), Q 29 (0.911). **Notable**: Q 9 is rank 9 of nearest, NOT rank 1.
- **h-new-590 (outlier spectrum)**: Q 8 outlier-strength Δ = +9.81 pp on window {Q 5-11}; **WEAK_OUTLIER**. p_greater = 0.6209 (NOT a strong outlier).
- **h-new-700 rhyme**: top final letter ن (nūn), 0.520 of 75 verses; rhyme entropy = 1.286 nats (HIGH — Medinan-ṭiwāl poly-rhyme pattern).
- **h-new-720**: Q 7 → Q 8 fraction_residual = 0.0256, **rank 10/113** (top decile expensive — chronology-break seam). Q 8 → Q 9 fraction_residual = 0.0074, **rank 58/113** (mid). Q 9 → Q 10 fraction_residual = 0.0373, **rank 4/113** (very expensive). Q 8 + Q 9 form a Medinan-island flanked by expensive boundaries.
- **h-new-750**: Q 8 sig_A = -0.557 (rank 75/114, mid-low); sig_B = +0.234 (rank 53/114, near-median). z_rhyme_entropy = +0.93; z_mean_content_distance = +1.49; z_local_cohesion = -0.70.
- **h-new-840 UAS**: Q 8 = +1.0364, **rank 22/114** (TOP QUINTILE). Driven by max_cost (Q 7→Q 8 expensive) + abs_outlier (+9.81 pp).
- **h-new-890 T1 (pre-existing)**: d_FR(Q 8, Q 9) = 0.911; rank_le 81/113; verdict NULL — Q 8 + Q 9 unity FALSIFIED at FR-distance level.
- **h-new-1240 (13 seamless seams)**: Q 8 → Q 9 NOT in clamped-zero set. Confirms unity-falsification at TSP-cost level.

### Q 8 corpus-text anchors (computed)
- 75 verses, 1,320 words, 5,465 letters (no-tashkeel, sans spaces); avg verse length 17.6 words / 72.9 letters.
- Final-letter rhyme: ن (52.0%), م (25.3%), ر (13.3%), ب (5.3%), then minor.
- *anfāl* / nfl-root: 4 corpus attestations (Q 8:1 ×2, Q 17:79 nāfila, Q 21:72 nāfila); Q 8 holds 50% of all nfl-root, 100% of spoils-of-war sense.
- Q 8:17 yaqīn-formula *wa-mā ramayta idh ramayta wa-lākinna allāha ramā* — corpus-singleton verified by regex (1/6,236 verses).
- Q 8 inclusio: phrase **هم المؤمنون حقا** (al-muʾminūn ḥaqqā) appears at v.4 AND v.74 — corpus-rare 2-occurrence inclusio; both occurrences in Q 8 only.
- Q 8 vs Q 9 root-Jaccard = 0.350 (rank 13/113 in adjacent pairs; rank 196/6,441 in all pairs / top 3.0%) — high Medinan-pair signature, NOT corpus-MAX.

### Hadith-corpus extraction (verified by direct Arabic-text grep against AhmedBaset JSON)
- **Bukhārī idInBook=4439** (Saʿīd b. Jubayr → Ibn ʿAbbās "Sūrat al-Anfāl nazalat fī Badr") — VERIFIED.
- **Bukhārī idInBook=4674** (3-surah identification chain: Anfāl-Tawba-Ḥashr → Badr-Fāḍiḥa-Banū-Naḍīr) — VERIFIED.
- **Muslim idInBook=7363** (parallel chain via ʿAbdallāh b. Muṭīʿ; matn *tilka Sūrat Badr*) — VERIFIED.
- **Muslim idInBook=4456** (ʿUmar / Abū Bakr Badr-prisoner-ransom debate; Q 8:67 reproach) — VERIFIED. Direct contains *mā kāna li-nabīyin an yakūna lahu asrā*.
- **Tirmidhī idInBook=3163** (Saʿd b. Abī Waqqāṣ sword-asbāb for Q 8:1) — VERIFIED. Direct contains *yasʾalūnaka ʿan al-anfāl*.
- **Tirmidhī idInBook=3168** (Ibn Masʿūd / Suhayl b. al-Bayḍāʾ chain on Q 8:67 reproach) — VERIFIED.
- **Bukhārī idInBook=3793** (al-Barāʾ → 313-Badr-warriors via Ṭālūt-typology) — VERIFIED.
- **Bukhārī Maghāzī chapter (id=64)**: 488 hadiths total (idInBook 3785-4272); 73 *Badr*-mentions (15% density) — densest single-battle cluster in canonical-9 books.
- **Q 8:17 phrase in hadith corpus**: 0 direct matn-quotes across all 9 collections — the verse is invoked-as-citation in tafsir but NOT echoed-as-prayer-formula.

### Pre-registrations (3 tests, locked before observation)
1. **Q008-F-01** Q 8 + Q 9 unity test on 3 axes (FR distance / canonical adjacency cost / root-Jaccard) — direction-locked: STRONG Ibn ʿAbbās one-surah claim → very-similar.
2. **Q008-F-02** Q 8:17 yaqīn-formula corpus-singleton — direction-locked: V₁=V₂ wa-mā V idh V wa-lākin = 1 corpus match.
3. **Q008-F-03** qitāl-cluster {Q 8, 9, 47, 48, 61} FR-cohesion — direction-locked: cluster-cohesive at group + Q 8 specific.

All pre-regs SHA-locked at file-write time; SHAs embedded into corresponding scripts; verified at runtime.

### SHA-locks (2026-05-09, lock-time)
| Pre-reg | SHA256 |
|:--|:--|
| Q008-F-01 | a2423796bdf29f272ea069b621c482383b84435548cac43d3931fd247f717681 |
| Q008-F-02 | 07b8e87374de1e7a5733169b78a1fc0aaa773abfac7cdbf922de336df11c1f20 |
| Q008-F-03 | fd442dbfd1dc245b7d931e2501fbd91e8fb89c27466439cc25e0f32fff92488f |

### Garden-of-forking-paths log
- **Q008-F-01 post-hoc disclosure**: H-NEW-890 T1 already established Q 8 + Q 9 FR-distance NULL prior to this specialist run. The Q008-F-01 pre-reg formalizes a 3-axis re-statement; this is double-attestation rather than independent novel test. Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol", verdict ceiling = **PASS-DIRECTED for falsification**. The 3-axis joint Bonferroni-3 corrected falsification is robust.
- **Q008-F-02 post-hoc disclosure**: the corpus-singleton finding for Q 8:17 was observed during pre-flight survey BEFORE pre-reg lock. Per protocol, single-test α=0.05 cap and PASS-DIRECTED ceiling apply. Independent-replication: the same regex on alternative orthographic conventions should yield the same singleton-status.
- **Q008-F-03**: this is genuinely-novel (no prior Quran-Decipherment test of the qitāl-cluster cohesion). Direction-locked positive. NULL on H1 is therefore an honest empirical NULL.

### Specialist coordination
- **Q 9 al-Tawba** (`surahs/Q009-al-tawba/`): sister surah; the parallel Q009-F tests are checked NOT to duplicate the Q 8/Q 9 unity test (which is HERE).
- **Q 7 al-Aʿrāf** specialist file does not yet exist; the Q 7 → Q 8 chronology-break seam analysis is queued for joint future work.
- **Q 47, 48, 61** specialist files do not yet exist; Q008-F-03 cluster cohesion test is the project's first pre-registered cohesion test for the qitāl-cluster.

### Run sequence (planned and executed)
1. ✓ Write all 3 pre-regs → SHA-lock each.
2. ✓ Write 3 scripts with embedded SHA verification.
3. ✓ Run scripts; capture JSON outputs in `csv/`.
4. ✓ Write 8 template files (00-07).
5. ✓ Update cross-references and finalize JOURNAL.

## 2026-05-09 — Session 1, run-time entries

### Q008-F-01 (run completed)
- Script: `scripts/Q008_F_01_q8_q9_unity.py`
- Runtime SHA verification: PASS
- **Axis A**: d_FR(Q 8, Q 9) = 0.9110; rank_le = 81/113; p = 0.7168. **H1 FAIL** (rank > 11).
- **Axis B**: q8_q9 fraction_residual = 0.0074; q8_in_clamped_zero = False; rank by cost = 58/113. **H2 FAIL** (NOT in clamped-zero seamless set of 13 pairs).
- **Axis C**: J(Q 8, Q 9) = 0.3504; rank_in_all_pairs = 196/6,441 (top 3.0% but not corpus-MAX). **H3 FAIL** (rank ≠ 1).
- **Verdict: NULL-FALSIFIES-STRONG-IBN-ABBAS**.
- Output: `csv/Q008-F-01.json`.

### Q008-F-02 (run completed)
- Script: `scripts/Q008_F_02_yaqin_formula.py`
- Runtime SHA verification: PASS
- N_strict (V₁=V₂ with wa-lākin): **1**. Sole match: **Q 8:17** (V = رميت "ramayta").
- N_loose: 3 (all in Q 8:17 — the regex picks up overlapping spans within the same verse).
- uniqueness_q817_strict: True (1.0); uniqueness_q817_loose: 1.0.
- **Verdict: CONFIRMED-CORPUS-SINGLETON**.
- Output: `csv/Q008-F-02.json`.

### Q008-F-03 (run completed)
- Script: `scripts/Q008_F_03_qital_cluster.py`
- Runtime SHA verification: PASS
- D_intra (cluster mean) = 0.9039; null mean (random-5-subset) = 0.9226 ± 0.1015; **p = 0.3399 — NULL on cluster-cohesion**.
- D_q8_cluster = 0.9170; D_q8_corpus = 1.0745; **diff = -0.1575** (Q 8 individually closer to cluster than to corpus).
- Cluster centrality ranking: Q 48 (1) → Q 61 (2) → Q 8 (3) → Q 47 (4) → Q 9 (5).
- **Verdict: DIRECTIONAL** (H1 NULL; H2 PASS).
- Output: `csv/Q008-F-03.json`.

### Aggregate run summary
- 1 CONFIRMED (Q008-F-02 yaqīn-formula corpus-singleton).
- 1 DIRECTIONAL (Q008-F-03 qitāl-cluster: Q 8 individually-near, group NULL).
- 1 NULL-FALSIFIES (Q008-F-01 Ibn ʿAbbās one-surah claim falsified).

All 3 reported with EQUAL NULL PROMINENCE per HANDOFF/04-DISCIPLINE.md.

### Cross-finding consequences
- **cross-finding-015** (classical-scholarship validation pattern): Q008-F-02 adds 1 to SURVIVED tally (al-Bāqillānī iʿjāz-keystone vindicated); Q008-F-01 adds 1 to REFUTED tally (strong Ibn ʿAbbās one-surah claim). Pattern persists.
- **cross-finding-013** (mushaf as topological ring): Q 8 + Q 9 are NOT seamless-conjoined (rank 58/113 cost) but flanked by major chronology-break seams (Q 7→Q 8 rank 10; Q 9→Q 10 rank 4). The basmala-omission is a structural-continuity marker, NOT a unity-claim. Consistent with CF-013 ring-topology framing.
- **H-NEW-1260** queued (cluster-substructure follow-up): Q008-F-03 reveals 4-surah qitāl-content-core {Q 8, 47, 48, 61} + Q 9 al-Tawba periphery — analogous 2-tier substructure to H-NEW-1070.1 oath-cluster.

## File checklist
- [x] 00-overview.md (carried forward from existing)
- [x] 01-empirical-profile.md (NEW)
- [x] 02-content-analysis.md (NEW; 4-block thematic + 9-segment verse-by-verse)
- [x] 03-tafsir-survey.md (NEW; 5 mufassirūn + al-Biqāʿī)
- [x] 04-hadith-corpus.md (NEW; 7 verified chains; full Arabic-text-grep verification)
- [x] 05-classical-claims-audit.md (NEW; 7 claims, 1 FALSIFIED, 4+1 VINDICATED)
- [x] 06-novel-findings.md (NEW; 3 pre-registered tests, all SHA-locked + run + reported)
- [x] 07-cross-references.md (NEW; CF-013 ring-topology hinge analysis)
- [x] preregs/Q008-F-01-q8-q9-unity-prereg.md
- [x] preregs/Q008-F-02-yaqin-formula-prereg.md
- [x] preregs/Q008-F-03-qital-cluster-prereg.md
- [x] scripts/Q008_F_01_q8_q9_unity.py
- [x] scripts/Q008_F_02_yaqin_formula.py
- [x] scripts/Q008_F_03_qital_cluster.py
- [x] csv/Q008-F-01.json
- [x] csv/Q008-F-02.json
- [x] csv/Q008-F-03.json
- [x] JOURNAL.md (this file)

## Next-session queue
- **H-NEW-1260** corpus-wide pre-registration of qitāl-content-core 2-tier-substructure (suggested by Q008-F-03 finding).
- **Q 9 al-Tawba** specialist run — should reference Q008-F-01 to avoid duplication of Q 8/Q 9 unity test.
- **Q 47 / Q 48 / Q 61** specialist runs — joint analysis of qitāl-cluster from each member's perspective.
- **Q 8:17 yaqīn-formula independent replication**: re-run on alternative orthographic conventions if available.
