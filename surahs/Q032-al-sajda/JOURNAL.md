---
surah: 32
surah_name_ar: السجدة
surah_name_translit: al-Sajda
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 32 al-Sajda — Investigation Journal


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

## 2026-05-08 — Q032-Q047-retry specialist run (pre-existing F-01/F-02/F-03)

**Three pre-registered tests, SHA-locked, seed 20260508, 10,000 perms each. Bonferroni-k=3.**

- **Q032-F-01** sajda-cosmic-twin. Pre-reg SHA `93541c6eef6193f57ddfce776a465c5445ffb91a8637fd4a868ff4032d806e84` (verified == JSON `pre_reg_sha`). Tested whether Q 32:15 is lexically closer to the cosmic-cluster {Q 13:15, Q 16:49} than to the median of the other 11 sajda-verses. T1 PASS (0.097>0.059); T2 FAIL (0.000); T3 perm FAIL (p=0.34). **DIRECTIONAL 1/3** — Q 32:15 is behavioral-prostration, NOT cosmic-roll-call. Sajda-typology refinement.
- **Q032-F-02** Q 32 ↔ Q 67 twin-axes. Pre-reg SHA `2f94580c3714cc4f7ce375e5160a1a6185935f4ce75a70fd87285b8f8a58e975`. FR-near pair tested on rhyme + sig_A + length-class + divine-density: 1/4 (length-class only). **NULL** at α_bon=0.0125 — the al-Munjiya binding is information-geometric, not surface-stylistic.
- **Q032-F-03** ALM-exception {Q 29, 30, 32} cohesion. Pre-reg SHA `85ef2873698bffbba5dbd5884336e7db0724745176e59d6fec39bae743d202ba`. T_obs 0.927; perm p_low 0.408. **NULL** — confirms muqaṭṭaʿāt-axis-content-orthogonality.

## 2026-05-10 — Wave twin-specialist run (brief-mandated F-04/F-05/F-06) + 8-file scaffold

**Pre-flight (in order):** read quran-investigation SKILL.md; read INVESTIGATION-PROTOCOL.md (full); reviewed exemplar surah dirs; confirmed `surahs/Q032-al-sajda/` held the prior single-file `00-overview-comprehensive.md` + F-01/02/03; built the canonical 8-file template around it.

**Data extraction (all from disk):**
- `quran-text/quran-no-tashkeel.json[31]` Q 32 (id 32, 30 verses) — 378 words; ن-monorhyme ~90%.
- `data/hafs-verse-counts.tsv` line 32 = 30. `data/revelation-order.csv` Q 32 = Tanzil/Suyūṭī #75, Nöldeke ~#70, Meccan (late).
- **h-new-111.json**: FR mean 0.889; nearest Q 67 (0.7534), Q 41 (0.7684), Q 76 (0.8395).
- **h-new-590.json**: Δ%ile −1.36, window {Q 29-35}, NULL (not a content outlier).
- **h-new-700.json / h-new-750.json**: rhyme entropy 0.389 (z=−0.690); sig_A −0.350 (rank 70); sig_B −1.322 (rank 95); local cohesion 1.0546.
- **h-new-720.json**: Q 31→Q 32 +0.1005 mid-pack; Q 32→Q 33 +0.3631 **rank 3/113** (4.4% of L_mushaf), top-3 structural break.
- **h-new-840.json**: UAS 0.7522 rank 27/114 (top-quartile structural-iʿjāz).
- Read ledger §10.21 (H-NEW-1330 14-sajda whole-surah NULL) + H-NEW-1510 (sajda pericope PASS z=+2.685) for the scale-pair context; cross-finding-028 for the liturgical-pair anchor.

**Tafsīr (read from disk, ≥5):** al-Ṭabarī, al-Rāzī (*Mafātīḥ*), al-Qurṭubī, Ibn Kathīr, al-Suyūṭī (*al-Durr* + *al-Itqān* nawʿ 30 sajda-catalog), al-Biqāʿī (*Naẓm al-Durar*, Q 32→Q 33 munāsaba) — see `03-tafsir-survey.md`.

**Ḥadīth (verified idInBook on disk):** Friday-fajr Q 32+Q 76 = al-Bukhārī #870 (replicated #1037); al-Munjiya nightly Q 32+Q 67 = al-Tirmidhī #2975. **Brief's hadith errors corrected on-disk:** Tirmidhī #2891/#2892 are clothing-hadith (NOT Friday-fajr); the Q 32+Q 67 pair is nightly (#2975), not Friday-fajr; the Friday-fajr pair is Q 32+Q 76. Both substrings batteries verified present. See `04-hadith-corpus.md`.

**Pre-registration (LOCKED BEFORE COMPUTATION), seed 20260509, 10,000 perms, Bonferroni-k=3 (α_bon≈0.017):**
- **Q032-F-04** ALM-4 mid-Meccan FR-cohesion. Pre-reg SHA `363410f7172124d9e93c7d106a81e32ba4759747d55893efb345522527648d48` (embedded as prereg_sha_expected; runtime prereg_sha_actual matched).
- **Q032-F-05** Friday-fajr + al-Munjiya per-pair strict-1σ. Pre-reg SHA `eea6e10e756410f07dbd4667463fca9fe87d820aa8fbbb86d3614f173bd4afcb` (expected==actual verified in JSON).
- **Q032-F-06** Q 32:15 ↔ Q 41:38 sajda cross-reference. Pre-reg SHA `6e3918d8cd80e5d44d7d9565785ca92e1dd17298a82aaaa93d5e16ed7c684d89` (expected==actual verified in JSON).

**Computation results (`csv/Q032-F-04.json`, `-F-05.json`, `-F-06.json`):**
- **Q032-F-04 NULL** (both cells): T_obs 0.9159 vs corpus 0.9235; uniform p=0.3659; length-matched p=0.1262. 5th muqaṭṭaʿāt-marker-thickness replication; direction was PASS-expected → honest NULL.
- **Q032-F-05 NULL** (strict-1σ failed; strong directional): Q 32↔Q 76 z=−0.40; Q 32↔Q 67 z=−0.81; joint p_perm=0.0237 (misses α_bon=0.017). PARTIAL — refines cross-finding-028 at per-pair scale, does not falsify the aggregate.
- **Q032-F-06 PARTIAL** (top-quintile met, top-5 missed): cosine(Q 32:15, Q 41:38)=0.1491, rank 10/91, percentile 0.901. Surprise: Q 32:15's strongest sajda-pair is Q 7:206 (rank 5), an *istakbara*-anchored behavioral sub-cluster.

**Decision points:**
- Q032-F-04 direction was PASS-expected; result NULL → published with full prominence (no massaging). MW-5 positive control ḤM-7 T_obs 1.0246 confirms the test can detect dispersion.
- Q032-F-05 locked an aggressive strict-1σ threshold; both pairs are directionally consistent but neither clears it. Published as NULL/PARTIAL with equal prominence; the aggregate cross-finding-028 PASS (p=0.0009) is untouched.
- No garden-of-forking-paths shift: analyses matched their pre-regs exactly. The brief's two hadith-numbering errors were corrected by on-disk verification before locking F-05.

## 2026-05-30 — 8-file completion (this landing)

Completed the two remaining template files: **07-cross-references.md** (neighbors, ALM-cluster, sajda H-NEW-1330/1510 scale-pair, dual-liturgy pair, cross-finding roles) and **JOURNAL.md** (this file). The 06-novel-findings family (F-01..F-06) was already finalized and SHA-verified; all six pre-reg SHAs re-checked on disk this session against their JSON `pre_reg_sha` / `prereg_sha_expected` fields — all six match. No new test was pre-registered (the existing family already satisfies ≥3 pre-registered tests per Protocol §11).

**Files produced/confirmed:** 00-overview, 00-overview-comprehensive (preserved), 01-empirical-profile, 02-content-analysis, 03-tafsir-survey, 04-hadith-corpus, 05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this) + 6 pre-regs + 6 csv JSON outputs.

**Verdict summary:** Q032-F-01 DIRECTIONAL (sajda behavioral, not cosmic); F-02 NULL (twin is info-geometric only); F-03 NULL (ALM-exception); F-04 NULL (ALM-4, 5th marker-thickness replication); F-05 NULL/PARTIAL (per-pair strict-1σ; aggregate cf-028 intact); F-06 PARTIAL (Q 32:15 ↔ Q 41:38 top-quintile; strongest pair is Q 7:206). Honest, equal-prominence NULLs throughout. Q 32's distinguishing architecture = dual-liturgy anchor + rank-3 structural-break terminus + mid-Meccan ALM terminus (conjunction is corpus-unique).
