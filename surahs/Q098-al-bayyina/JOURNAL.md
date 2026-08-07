---
surah: 98
surah_name_ar: البينة
surah_name_translit: al-Bayyina
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 98 al-Bayyina — Investigation Journal


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

## 2026-05-30 — Wave-N full 8-file deep-dive (completion of a stalled prior run)

**Situation on entry.** A prior run had written `00-overview.md`, the pre-reg
`Q098-F-01-bariyya-antithesis-prereg.md`, the script `scripts/Q098_F_01_bariyya_antithesis.py`, and the
result JSON `csv/Q098-F-01.json`, then stalled before writing the other 7 template files or committing.
This session completed the 8-file template (01-07 + JOURNAL) and verified the pre-registered test.

**Pre-flight (in order):**
1. Read the quran-investigation SKILL.md.
2. Read `INVESTIGATION-PROTOCOL.md` (full).
3. `ls surahs/Q098-al-bayyina/` and read every existing file (00-overview, pre-reg, script, JSON) — did NOT
   rewrite the complete files.
4. Referenced exemplar `surahs/Q066-al-tahrim/` for the full 8-file standard (read all 8 files).

**Pre-reg + script verification (PRE-REG-STANDARD-04):**
- Pre-reg `Q098-F-01-bariyya-antithesis-prereg.md` SHA-256 = `57eb6828a86fccaecb0a5438ad4acb671a6f8724e16d1669fede67b2d1852b41`.
- Ran `python3 scripts/Q098_F_01_bariyya_antithesis.py` → printed `SHA OK: 57eb6828…1852b41`; reproduced
  `csv/Q098-F-01.json` byte-for-byte. Seed 20260509; 10,000 perms. Runtime-verified.

**Data extraction (all from disk, no values from memory):**
- `quran-text/quran-no-tashkeel.json` Q 98 (id 98, Medinan, 8 verses) — verified 8 verses; 94 words /
  404 letters (marks stripped); 42 distinct QAC roots (60 root-tokens) via `data/morphology/root-index.json`.
- `data/revelation-order.csv`: Q 98 = revelation #100 (Tanzil EgStd), Nöldeke #92, **Medinan**.
- `data/hafs-verse-counts.tsv` line 98 = **8** (al-Qurṭubī's *tisʿ āyāt* = 9 is a non-Kūfan counting tradition).
- **h-new-111.json** (FR): Q 98 mean FR **0.8214**; nearest Q 108 (0.4951), Q 110 (0.4994), Q 112 (0.5076);
  5 farthest Q 26/12/6/4/3.
- **h-new-590.json** (outlier): Q 98 IS in `all_surahs_results` (X=98), window {95-101}, delta_pct **+0.01**,
  p 0.9997, classification **WEAK_OUTLIER**. → **CORRECTS the 00-overview "NOT computed / data-gap" claim**
  (documented in 01-empirical-profile §0 correction box). The abs_outlier=0.01 also appears in H-NEW-840.
- **h-new-700.json** (rhyme/phoneme): rhyme idx97 = {top ه, frac **1.0**, n_verses 8} (PERFECT monorhyme);
  phoneme idx97 = [0.0173, 0.0297, 0.0272, 0.1262].
- **h-new-750.json** (iʿjāz): rhyme_entropy **0.0**; sig_A **−0.38628** (rank 73); sig_B **−1.12911** (rank 88);
  local_cohesion 1.7130; mean_content_distance 0.821376.
- **h-new-720.json** (TSP): Q 97→Q 98 delta_raw +0.02750 rank **27/113**; Q 98→Q 99 +0.12653 rank **91/113**.
- **h-new-840.json** (UAS): Q 98 UAS **−1.6965** rank **93/114**; abs_outlier 0.01, max_cost 0.1265, abs_ijaz 0.3863.

**Tafsīr (read in Arabic from disk; 6 mufassirūn):**
- al-Ṭabarī (`spa5k .../ar-tafsir-al-tabari/98.json`): *munfakkīn* = desist (Mujāhid/Qatāda/Ibn Zayd);
  al-bariyya non-hamza majority + Nāfiʿ hamza; v7 Shīʿī gloss (Abū al-Jārūd).
- al-Zamakhsharī (`raw/zamakhshari-kashshaf.openiti.raw.txt` L72523-72560): al-bariyya morphology +
  *khiyār al-bariyya* variant.
- al-Rāzī (`raw/razi-mafatih-al-ghayb.openiti.raw.txt`, Q98 block ≈L262440-262760): v5 īmān-definition,
  v6 suʾālāt (ahl-al-kitāb-before-mushrikīn; kafarū-verb vs mushrikīn-noun), v8 ten masāʾil incl. the
  *karam/raḥma* reward-expansion (grounds the v6/v8 *abadan* asymmetry).
- al-Qurṭubī (`spa5k .../ar-tafseer-al-qurtubi/98.json`): Meccan (Yaḥyā b. Sallām) / Medinan (Ibn ʿAbbās +
  jumhūr); **tisʿ āyāt** (9); the weak Abū al-Dardāʾ faḍīla = *lā yaṣiḥḥ / bāṭil* (Ibn al-ʿArabī); ṣaḥīḥ
  Ubayy report (Bukhārī+Muslim); *qirāʾat al-ʿālim ʿalā al-mutaʿallim*.
- Ibn Kathīr (`spa5k .../en-tafisr-ibn-kathir/98.json`): Medinan; Ubayy report (Aḥmad + "Bukhārī, Muslim,
  Tirmidhī **and Nasāʾī** from Shuʿba"); *munfakkīn* (Mujāhid/Qatāda).
- al-Baghawī (`spa5k .../ar-tafsir-al-baghawi/98.json`): cleanest qiraʾāt — Nāfiʿ + Ibn ʿĀmir hamza both
  occurrences; rest doubled non-hamza (like al-dhurriyya).

**Ḥadīth (verified `idInBook` on disk, `ahmedbaset-json/db/by_book/the_9_books`):**
- Ubayy recitation report — Bukhārī **#4753, #4754** (Book 65 Tafsīr); Muslim **#1757** (Book 6 Travellers'
  Prayer), **#6185** (Book 44 Faḍāʾil al-Ṣaḥāba); Tirmidhī **#3888** (ḥasan ṣaḥīḥ), **#3889** (ḥasan),
  **#3995** (ḥasan ṣaḥīḥ) — all Book 49 al-Manāqib. Gradings read from Arabic colophons.
- al-Nasāʾī: Ibn Kathīr asserts al-Nasāʾī recorded the report, but a full scan of on-disk al-Mujtabā
  (5768 ḥadīth) returned ZERO hits → **flagged as data-gap** (likely al-Sunan al-Kubrā, not on disk). NOT
  an absence claim.
- Abū al-Dardāʾ thawāb faḍīla: recorded + graded *bāṭil* in al-Qurṭubī (Ibn al-ʿArabī).

**Pre-registered test (Q098-F-01) — FINALIZED (4 arms):**
- Arm A: byn raw rank **59/71**; surface البينة beaten by 4 surahs (Q 11 ×4) → **title-density-EXACT
  FALSIFIED** (corrects H-NEW-1820 summary-list entry).
- Arm B: البرية at exactly (98,6),(98,7), n=2 → **CONFIRMED — corpus hapax-pair**.
- Arm C: 1 of **219** adjacent faith-antithetical pairs = Q 98:6-7, pivot خير/شر → **CONFIRMED —
  corpus-UNIQUE antonym muqābala**.
- Arm D: J(v6,v7)=**0.0833** > null_mean 0.0261, z=+1.163, p_lower 0.878; shared root **brA** → direction
  REVERSED → **NULL (pre-commit violation, full prominence)** — replicates H-NEW-2360 jadal-overlap at
  verse-pair scale.

**Decision points:**
1. **H-NEW-590 data-gap correction.** The 00-overview asserted Q 98's outlier was "NOT computed." On disk,
   `all_surahs_results` contains X=98 (WEAK_OUTLIER, delta_pct +0.01). I did NOT edit the complete 00-overview
   (per task instruction "do not rewrite complete files"); instead I logged the correction prominently in
   01-empirical-profile §0 and §2, and in the audit/cross-ref files. The overview's anchor-table value is
   superseded by the on-disk figure.
2. **Tirmidhī chapter.** The 00-overview implied the Tirmidhī recitation reports sit under Tafsīr; on disk
   they are Book 49 (al-Manāqib). Recorded the correct chapter in 04-hadith-corpus.
3. **al-Nasāʾī number.** Not locatable on-disk → flagged, not invented (anti-hallucination rule).
4. **Arm D NULL.** Locked DISJOINT direction reversed → published as NULL with full prominence (not massaged);
   the reversal is the *informative* result (overlap, not disjunction). No garden-of-forking-paths shift —
   the analysis matched the pre-reg exactly; MW-7 peek was disclosed in the pre-reg before locking.

**Files produced this session:** 01-empirical-profile, 02-content-analysis, 03-tafsir-survey,
04-hadith-corpus, 05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this). Already
present (not rewritten): 00-overview, Q098-F-01 pre-reg, scripts/Q098_F_01_bariyya_antithesis.py,
csv/Q098-F-01.json.

**Verdict:** Q098-F-01 = Arm A title-density FALSIFIED (corrects H-NEW-1820 summary) + Arm B CONFIRMED
(bariyya hapax-pair) + Arm C CONFIRMED (corpus-UNIQUE khayr↔sharr muqābala, 1 of 219) + Arm D NULL
(pre-commit violation — jadal-overlap, H-NEW-2360 verse-pair replication). Honest, equal-prominence.

**Queued follow-ups:** Q098-F-02 (the *q-w-m / qayyima* triad — kutub qayyima v3 / dīn al-qayyima v5 / alt-title
al-Qayyima — corpus-distinctive?); Q098-F-03 (formalize the v6 no-*abadan* / v8 *abadan* reward-punishment
asymmetry corpus-wide); Q098-F-04 (locate the al-Qurṭubī 9-āya variant fāṣila split-point).
