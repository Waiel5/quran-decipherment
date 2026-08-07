---
surah: 3
surah_name_ar: آل عمران
surah_name_translit: Āl ʿImrān
file_type: journal
date_last_updated: 2026-05-29
phase: B+
---

# Q 3 Āl ʿImrān — Investigation Journal


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

## 2026-05-29 — Full 8-file deep-dive (surah-completeness-audit follow-up; selected as a 0/9-stub most-incomplete surah)

**Pre-flight (in order):**
1. Read the quran-investigation skill (SKILL.md).
2. Read `INVESTIGATION-PROTOCOL.md` (full).
3. Reviewed exemplar dirs `surahs/Q073-al-muzzammil/` and `surahs/Q066-al-tahrim/` (8-file gold standard).
4. Confirmed `surahs/Q003-al-imran/` had only empty csv/preregs/scripts subdirs (0/9 substantive files in the
   completeness audit) — created the 8 files + `csv/`.

**Selection rationale:** in the surah-completeness audit, Q 3 was one of 12 fully-empty (0/9) surah dirs.
Among those, Q 3 (al-sabʿ al-ṭiwāl, ALM, UAS rank 37, |outlier| 15.28, FR-nearest to Q 2) and Q 4 al-Nisāʾ
are the two longest and most architecturally significant empty surahs — the largest documentation gaps with
the richest material to integrate. Selected as deep-dive A.

**Data extraction (all from disk, no values from memory):**
- `quran-text/quran-no-tashkeel.json` Q 3 (id 3, Medinan, 200 verses) — verified 200 verses; computed
  3,501 words / 14,985 letters (marks stripped); 439 distinct QAC roots (2,274 root-tokens) via
  `data/morphology/root-index.json`.
- `data/revelation-order.csv`: Q 3 = revelation #89 (Tanzil EgStd), Nöldeke #97, Medinan.
- `data/hafs-verse-counts.tsv` line 3 = 200.
- **h-new-111.json** (FR): Q 3 mean FR 1.0943; nearest Q 2 (0.631); top neighbours Q 2, Q 5, Q 4, Q 8, Q 6;
  Q 2 rank 1/113, Q 4 rank 3/113.
- **h-new-590.json** (outlier): Q 3 window {1-7}, delta_pct −15.28, classification COHESION_ANCHOR.
- **h-new-700.json** (rhyme/phoneme): top final-letter ن frac 0.6091 (197 rhyme-verses); phoneme vec idx 2 =
  [0.0160, 0.0370, 0.0312, 0.1060]. Among ≥100-verse surahs, Q 3 is the SECOND-least-concentrated rhyme.
- **h-new-750.json** (iʿjāz): rhyme_entropy 1.2489 (z +0.87); sig_A −0.8179 (rank 84); sig_B +0.4281 (rank 45);
  z_mean_content_distance +1.6855 (FR-distant — drives sig_A down).
- **h-new-720.json** (TSP): Q 2→Q 3 +0.01646 rank 20/113; Q 3→Q 4 −0.04662 rank 4/113 (seamless). Block
  {2,3,4,5} mean internal seam −0.03196 = **rank 1/111** (smoothest contiguous 4-block); top-3 blocks all in
  al-ṭiwāl.
- **h-new-840.json** (UAS): Q 3 UAS +0.4517 rank 37/114 (cohesion-axis-driven).

**Tafsīr (read from disk):**
- al-Ṭabarī (spa5k `ar-tafsir-al-tabari/3/7.json`): muḥkam = clear/decisive verses, *aṣl al-kitāb*; umm =
  the bulk/refuge; mutashābih = multi-faced wording.
- al-Zamakhsharī (`raw/zamakhshari-kashshaf.openiti.raw.txt` L7765-7858): header *madaniyya, miʾatā āya*;
  mīm-vowel grammar; al-furqān 4 readings; muḥkam/mutashābih.
- al-Rāzī (`raw/razi-mafatih-al-ghayb.openiti.raw.txt` muqaṭṭaʿāt + munāsaba threads): muqaṭṭaʿāt survey;
  the *wāw* of al-rāsikhūn crux.
- al-Qurṭubī (spa5k `ar-tafseer-al-qurtubi/3/{1,7}.json`): muqaṭṭaʿāt = God's secret (al-Shaʿbī, al-Thawrī,
  Abū Bakr, ʿAlī); v 7 ʿĀʾisha "fa-ḥdharūhum" (Muslim) + Abū Umāma / Khārijites.
- Ibn Kathīr (spa5k `en-tafisr-ibn-kathir/3/1.json`): first 83 āyāt = Najrān delegation (year 9);
  al-Ḥayy al-Qayyūm = Greatest Name (cross-ref Āyat al-Kursī).

**Ḥadīth (verified `idInBook` on disk, `ahmedbaset-json/db/by_book/the_9_books`):**
- al-Zahrāwān: Muslim #1766 (Book 6, Abū Umāma — *ghamāmatān* text verified), #1768 (al-Nawwās b. Samʿān).
- al-ism al-aʿẓam (Q 3:2): Tirmidhī #3562 (Book 5; grading *ḥasan ṣaḥīḥ* from Arabic colophon), Abū Dāwūd
  #1497 (Book 4) — both with the al-Ḥayy al-Qayyūm text.
- muḥkam/mutashābih (Q 3:7): Bukhārī #4342 (Book 65 Tafsīr; ʿĀʾisha *محكمات … فاحذروهم*), #4547 region,
  Muslim #6610 (Book 47).
- Najrān/Mubāhala (Q 3:61): Bukhārī #4187, #4188 (Book 64 Maghāzī; al-ʿĀqib/al-Sayyid), #3582 (Book 62),
  #6980 (Book 95).
- Solo Āl-ʿImrān faḍāʾil → flagged as data-gap (virtue is paired with al-Baqara as al-Zahrāwān).

**Pre-registration (Q003-F-01) — LOCKED BEFORE COMPUTATION:**
- Pre-reg file written first: `Q003-F-01-tiwal-block-cohesion-prereg.md`.
- SHA-256: `40f796b7f07db6196fd397180b449e780382ba154684033fb8ecb2329f80c4d7`.
- Embedded in `scripts/Q003_F_01_tiwal_block.py` as EXPECTED_SHA; verified at runtime (printed "SHA OK").
- Seed 20260509; 10,000 perms.
- Three arms: A = {2,3,4,5} smoothest contiguous 4-block (deterministic rank); B = Q3 cohesion-anchor (590);
  C = max-statistic permutation null (control for 111-block multiplicity). Direction-locks set BEFORE running.
  Arm C's max-statistic null (min over 111 blocks) pre-committed as the multiplicity control.

**Results (honest):**
- Arm A: block {2-5} mean seam −0.03196, **rank 1/111** — CONFIRMED.
- Arm B: Q3 delta_pct −15.28, COHESION_ANCHOR — CONFIRMED.
- Arm C: obs −0.03196 vs null-min-mean −0.01683, z −1.174, **p_perm 0.12319** — **NULL** (block smoothness
  reproducible by 12.3% of random seam-arrangements once block-multiplicity controlled).
- Net: SPLIT — 2 deterministic CONFIRMED + 1 permutation NULL. Published with equal NULL prominence.

**Decision points / forking-paths:**
- The Arm-C max-statistic null (minimum over all 111 blocks) was chosen DELIBERATELY and pre-committed as the
  honest multiplicity control — a naive "compare obs to mean random block" would have spuriously "confirmed."
  The max-statistic is what correctly turned the NULL. This is the load-bearing methodological choice.
- Arm A and Arm B are deterministic and need no α; only Arm C consumes the family α (0.05/1).

**Files produced:** 00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey, 04-hadith-corpus,
05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this file), the pre-reg, the script
(`scripts/Q003_F_01_tiwal_block.py`), and the JSON (`csv/Q003-F-01.json`).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
