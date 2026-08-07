---
surah: 4
surah_name_ar: النساء
surah_name_translit: al-Nisāʾ
file_type: journal
date_last_updated: 2026-05-29
phase: B+
---

# Q 4 al-Nisāʾ — Investigation Journal


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
4. Confirmed `surahs/Q004-al-nisa/` had only empty csv/preregs/scripts subdirs (0/9 substantive files in the
   completeness audit) — created the 8 files + `csv/`.

**Selection rationale:** in the surah-completeness audit, Q 4 was one of 12 fully-empty (0/9) surah dirs.
Among those, Q 4 al-Nisāʾ (al-sabʿ al-ṭiwāl, UAS rank 26, |sig_A| 3.15 — corpus 2nd-largest, the lone
alif-rhyme long surah) and Q 3 Āl ʿImrān are the two longest and most architecturally significant empty
surahs — the largest documentation gaps. Selected as deep-dive B.

**Data extraction (all from disk, no values from memory):**
- `quran-text/quran-no-tashkeel.json` Q 4 (id 4, Medinan, 176 verses) — verified 176 verses; computed
  3,763 words / 16,332 letters (marks stripped); 462 distinct QAC roots (2,462 root-tokens) via
  `data/morphology/root-index.json`.
- `data/revelation-order.csv`: Q 4 = revelation #92 (Tanzil EgStd), Nöldeke #100, Medinan.
- `data/hafs-verse-counts.tsv` line 4 = 176.
- **h-new-111.json** (FR): Q 4 mean FR 1.1375; nearest Q 2 (0.755); top neighbours Q 2, Q 5, Q 3, Q 33, Q 9,
  Q 24; Q 3 rank 3/113, Q 5 rank 2/113.
- **h-new-590.json** (outlier): Q 4 window {1-7}, delta_pct +1.08, classification WEAK_OUTLIER (near-neutral).
- **h-new-700.json** (rhyme/phoneme): top final-letter ا frac 0.9602 (169/176); phoneme vec idx 3 =
  [0.0204, 0.0367, 0.0343, 0.1107]. Q 4 is the LONE alif-rhyme surah among al-ṭiwāl {2,3,4,5,6,7,9}.
- **h-new-750.json** (iʿjāz): rhyme_entropy 0.1989 (z −1.034); sig_A −3.1463 (rank 113/114); sig_B −1.4630
  (rank 100); z_mean_content_distance +2.1124 (most-FR-distant tier).
- **h-new-720.json** (TSP): Q 3→Q 4 −0.04662 rank 4/113 (seamless); Q 4→Q 5 −0.06571 rank 2/113 (2nd-smoothest
  seam in corpus). Q 4 is doubly-seamless; max-neighbour-cost clamps to 0.0.
- **h-new-840.json** (UAS): Q 4 UAS +0.8778 rank 26/114, driven by |sig_A| 3.15 (max-cost 0.0).

**Tafsīr (read from disk):**
- al-Qurṭubī (spa5k `ar-tafseer-al-qurtubi/4/{1,3}.json`): Medinan (refutes Meccan; ʿĀʾisha-Bukhārī testimony;
  rejects "yā-ayyuhā al-nās = Meccan" by Q 2 counterexample); v 3 polygamy = restriction (orphan-girl, Muslim).
- al-Ṭabarī (spa5k `ar-tafsir-al-tabari/4/11.json`): v 11 farāʾiḍ = fixed divine ʿahd; *mithl* raised by the
  *lām*; waṣiyya = ʿahd/iʿlām not governing speech.
- al-Zamakhsharī (`raw/zamakhshari-kashshaf.openiti.raw.txt` L10950-10985): header *madaniyya, 176 āya*
  (matches disk); v 1 conjunction grammar; taqwā motivated by power + ḥifẓ al-ḥuqūq ("matches the surah").
- al-Rāzī (`raw/razi-mafatih-al-ghayb.openiti.raw.txt` al-Nisāʾ block + Q3→Q4 cross-refs L18687, 28218): the
  family-of-ʿImrān → law-of-the-family link; *al-arḥām* as organising principle; the *wa-l-arḥāma* case crux.
- Ibn Kathīr (spa5k `en-tafisr-ibn-kathir/4/1.json`): Medinan (Ibn ʿAbbās); Ibn Masʿūd's "5 preferred āyāt"
  (Q 4:31, 4:40) via al-Mustadrak.

**Ḥadīth (verified `idInBook` on disk, `ahmedbaset-json/db/by_book/the_9_books`):**
- Last-revealed verse (Q 4:176 kalāla): Bukhārī #4174, #4448 (Book 65 Tafsīr), #6499 (Book 85 al-Farāʾiḍ) —
  al-Barāʾ; texts verified.
- Inheritance (Q 4:11): Tirmidhī #2159 (daughters of Saʿd b. al-Rabīʿ; grading *ḥasan ṣaḥīḥ* from colophon);
  Muslim #4016 (Jābir sickbed, kalāla); Abū Dāwūd #2892 — FLAGGED: names daughters of Thābit b. Qays
  (isnād-variant of the two-daughters case), documented not conflated.
- Polygamy/orphan (Q 4:3): Bukhārī #2398 (Book 47 Waṣāyā), #4368 (Book 65 Tafsīr), #4860/#4888/#4894 (Book 67
  Nikāḥ) — ʿĀʾisha; texts verified.
- Ibn Masʿūd "5 preferred āyāt" — tafsīr-attested (al-Mustadrak via Ibn Kathīr), NOT a single 9-book idInBook;
  flagged.

**Pre-registration (Q004-F-06) — LOCKED BEFORE COMPUTATION:**
- Pre-reg file written first: `Q004-F-06-alif-monorhyme-prereg.md`.
- SHA-256: `47eec58b703727e0acddd9b61bb60dac36b610d3850ebdcb08292e99af55cec6`.
- Embedded in `scripts/Q004_F_06_alif_monorhyme.py` as EXPECTED_SHA; verified at runtime (printed "SHA OK").
- Seed 20260509; 10,000 perms.
- Three arms: A = Q4 unique alif among ṭiwāl (deterministic); B = sig_A bottom-3 + low rhyme entropy
  (deterministic); C = length-stratified frac null (n_verses ≥ 100). Direction-locks set BEFORE running.
- **Pre-committed honest-limit:** the pre-reg NAMED Q 17, Q 18, Q 23 in advance as long surahs that exceed
  Q 4's concentration, pre-committing the Arm-C failure mode (the alif-monorhyme is notable-not-extreme).

**Results (honest):**
- Arm A: al-ṭiwāl letters {2:ن,3:ن,4:ا,5:ن,6:ن,7:ن,9:ن}; alif_members [4] — CONFIRMED. (alt roster {…,8}: Q8 also ن.)
- Arm B: sig_A −3.1463 rank 113/114, z_rhyme_entropy −1.034 — CONFIRMED.
- Arm C: frac 0.9602 (176v) vs null_mean 0.8112, z +1.007, **p_perm 0.17838** — **NULL**; Q17 (0.991), Q18
  (0.991), Q23 (0.966) exceed Q4 (exactly the pre-committed honest-limit).
- Net: SPLIT — 2 deterministic CONFIRMED + 1 length-stratified NULL. Published with equal NULL prominence.

**Decision points / forking-paths:**
- The Arm-C length-stratification (n_verses ≥ 100) was chosen DELIBERATELY to control the trivial
  short-surah-100%-monorhyme confound, and pre-committed. Without it, Q 4 would have spuriously appeared
  extreme against the (mostly short) full corpus. The stratification is the honest control that turned the NULL.
- The pre-reg named the three exceeding surahs (Q17/Q18/Q23) BEFORE running — this is the MW-7 post-hoc cap in
  action: the over-claim was capped at pre-registration.

**Files produced:** 00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey, 04-hadith-corpus,
05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this file), the pre-reg, the script
(`scripts/Q004_F_06_alif_monorhyme.py`), and the JSON (`csv/Q004-F-06.json`).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
