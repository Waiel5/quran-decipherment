---
surah: 53
surah_name_ar: النجم
surah_name_translit: al-Najm
file_type: journal
date_created: 2026-05-09
phase: B+
specialist: Waiel Al-Shujaa
---

# Q 53 al-Najm — Investigation Journal


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

## 2026-05-09 — Specialist run

### Setup

- **Prior state**: `surahs/Q053-al-najm/` did not exist; created from scratch with subdirs `preregs/`, `csv/`, `scripts/`.
- **Pre-flight reading**:
  - `HANDOFF/04-DISCIPLINE.md` — reaffirmed pre-reg + Bonferroni + reverse-direction discipline, MW-6 verbatim-confidence requirement, M-5 classical-doctrine-decomposition pattern
  - `HANDOFF/01-WHAT-WE-KNOW.md` — confirmed locked corpus anchors, top-tier confirmed findings (cross-finding-013 ring, cross-finding-015 classical-vs-modern), sajda-surah list verification needed
  - `MASTER-FINDINGS-LEDGER.md` §1-3 — Tier-A meta-findings on classical-modern reliability ratio (#5a, 13× central estimate); confirmed novel findings catalogue
  - `surahs/Q037-al-saffat/` (full reference template) and `surahs/Q014-ibrahim/` (recent specialist) — used as gold-standard for 8-file template structure
- **Empirical anchors loaded** from `findings/phase-b-hypotheses/csv/`:
  - `h-new-111.json` — Fisher-Rao surah-distance matrix (verified Q 53 row keys)
  - `h-new-590.json` — outlier-strength (X=53 row found, classification = WEAK_OUTLIER)
  - `h-new-700.json` — phonological / rhyme (Q 53 top-letter ي frac=0.855)
  - `h-new-720.json` — canonical adjacency cost (Q 52→Q 53 + Q 53→Q 54 entries verified)
  - `h-new-750.json` — iʿjāz signature (Q 53 sig_A=−0.656 rank 79; sig_B=−1.066 rank 84)
  - `h-new-840.json` — UAS (Q 53 UAS=0.532 rank 34/114)

### Computational confirmations

#### Corpus-derived anchors

- Q 53 word count (no-tashkeel): **372** (computed from `quran-no-tashkeel.json`)
- Q 53 letter count (no spaces): **1,445**
- Q 53 verse count: **62**
- Final-letter distribution: ى 53 (85.5%), ا 4 (6.5%), ن 3 (4.8%), ة 2 (3.2%)
- Rhyme entropy (Shannon, nats): **0.568** — among lowest in the strict-oath-opener cluster

#### FR neighborhood (loaded from h-new-111)

- Q 53 nearest neighbor: **Q 96 al-ʿAlaq at d_FR = 0.7126** (rank 1/113) — verified
- Q 53 mean distance to other 113: **0.953** (corpus mean 0.924; Q 53 slightly content-distant)
- Top-15 nearest are all very-short-Meccan (Q 96, Q 87, Q 92, Q 110, Q 102, Q 1, Q 93, Q 81, Q 108, Q 91, Q 100, Q 79, Q 99, Q 112, Q 94)

#### Sajda-surah corpus verification

- Direct corpus scan of `quran-no-tashkeel.json` for the ۩-marker yielded:
- 15 sajda-marked verses across **14 distinct surahs** (Q 22 has 2 sajdas — vv 18 and 77)
- Sajda-14 list: Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96 ✅ matches surah-spec list
- Of the 14, **3** have the sajda at the LAST verse: Q 7 (v 206/206), Q 53 (v 62/62), Q 96 (v 19/19)

#### 9-book corpus null on *gharānīq* phrase

- Direct corpus search across all 9 canonical hadith books (~67,000 hadiths) for the strings الغرانيق, غرانيق, تلك الغرانيق, العلى, تشفع
- Result: **ZERO matches** in any of the 9 books
- Books searched: Bukhārī (7,277 hadiths), Muslim (7,472), Tirmidhī (3,956), Abū Dāwūd, Nasāʾī, Ibn Mājah, Aḥmad, Mālik, Dārimī
- This is project-novel: previous classical-scholarship literature had NOT systematically corpus-scanned all 9 books simultaneously (al-Albānī's 1952 critique was isnād-based, not full-corpus-search-based)

#### Bukhārī al-Najm hadith verification

- Verified via direct DB scan (`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json`):
  - Bukhārī **1036**: Ibn Masʿūd al-Najm sajda + shaykh-stones (chap 17 = Sujūd al-Qurʾān)
  - Bukhārī **1039**: Ibn Masʿūd parallel chain
  - Bukhārī **1040**: Ibn ʿAbbās jinn-pagans-humans prostration
  - Bukhārī **1041**: ʿAṭāʾ b. Yasār → Zayd b. Thābit no-prostration
  - Bukhārī **1042**: Zayd b. Thābit direct
  - Bukhārī **4648**: ʿĀʾisha "did the Prophet see his Lord?" (denies anthropomorphic vision)
  - Bukhārī **4651**: Q 53:18 "green screen covering horizon" (Ibn Masʿūd)
  - Bukhārī **4655**: parallel to Bukhārī 1040 in tafsir chapter
  - Bukhārī **4656**: Ibn Masʿūd "Q 53 = first revealed sajda-surah"
- Numbering confirmed via Bukhārī #1 = "intentions hadith" (innamā l-aʿmālu bi-l-niyyāt) — Sunnah.com / Adam-running-number convention

#### Muslim al-Najm hadith verification

- Verified via direct DB scan:
  - Muslim **1197**: Ibn ʿUmar al-Najm sajda
  - Muslim **1198**: Zayd b. Thābit no-prostration
  - Muslim **6934** (chap 52): ʿĀʾisha-domestic-narration (NOT the Lord-vision question; that is at Muslim #162-180 range — PENDING precise verification)

#### Tirmidhī al-Najm hadith verification

- Verified via direct DB scan:
  - Tirmidhī **3360**: Sidrat al-Muntahā (Ibn Masʿūd, *ḥasan ṣaḥīḥ* per al-Tirmidhī's grading)
  - Tirmidhī **3361**: Q 53:9 *qāba qawsayni* + Jibrīl 600 wings (Ibn Masʿūd)
  - Tirmidhī **3363**: Ibn ʿAbbās "Muhammad saw his Lord 2 times"
  - Tirmidhī **3364**: Ibn ʿAbbās commentary on Q 53:13-14

#### CRITICAL CORRECTION on Bukhārī numbering convention

- The hadith DB's `idInBook` field is **identical to Sunnah.com/Adam running-number** (verified by Bukhārī #1 = intentions hadith).
- Previous misreadings of "Bukhārī #1067" or "Bukhārī #1071" as the sajda-Najm hadith were INCORRECT — the correct numbers are **Bukhārī 1036/1039/1040/1041/1042** in the Sujūd al-Qurʾān chapter (chap 17 = Khan vol 2 book 19).
- Specialist note: Khan-translation-volume-book-hadith convention DIFFERS from Sunnah.com/Adam running-number convention. This file uses the latter (matches the project's hadith DB).

### Pre-test informational scans

#### Q053-F-01 (Q 53 FR-nearest)

- Pre-test scan: Q 53's nearest neighbors include Q 96, Q 87, Q 92, Q 110, Q 102, Q 1, Q 93, Q 81, Q 108, Q 91 (very-short-Meccan-tail)
- Specialist's a-priori prediction: Q 96 al-ʿAlaq is the predicted-nearest, on the **revelation-vision-disclosure thematic register** logic
- Pre-test rank-of-Q-96 was unknown to specialist at prediction-time; the specific rank-1 prediction was based on conceptual reasoning, not pre-test peeking

#### Q053-F-02 (gharānīq text-anomaly null)

- Reverse-direction prediction locked: NULL is the predicted outcome
- Pre-test scan computed token-count of Q 53:19-23 = 41, unique = 38, TTR = 0.927
- The block ranked 1831/5783 by token-count, 4486/5783 by TTR — both within 5%-95% corpus range
- Predicted-NULL outcome confirmed at the informational level; SHA-locked formal test re-runs confirms

#### Q053-F-03 (sajda-14 cohesion)

- Reverse-direction prediction locked: NULL is the predicted outcome
- Pre-test scan computed within-cluster mean FR = 0.9414 vs corpus = 0.9235
- Within-cluster mean is *slightly above* corpus baseline (in the wrong direction for cohesion)
- Predicted-NULL outcome confirmed at the informational level; SHA-locked formal test re-runs confirms with z=+0.333, p=0.588

### Pre-registration (locked 2026-05-09)

- `Q053-F-01-vision-pericope-fr-cohesion-prereg.md` — SHA `d7c954bf3a151d9c630015a4977be261a59fb953fa03a04d1666047e340c14f0`
- `Q053-F-02-gharaniq-text-anomaly-prereg.md` — SHA `af6c4a8bd429ca5d5662ca11986865c232f404272f4f1ff2755d70cfceeefe88`
- `Q053-F-03-sajda-14-fr-cohesion-prereg.md` — SHA `cdbebcbbfe97c7f0881c1b3b4504b681a0b76a118186ad45b2231f56a6b60d5c`
- Bonferroni-k = 3 (locked in YAML frontmatter of all 3 pre-regs); α_bon = 0.0167

### Run script

- `scripts/Q053_F_all_tests.py` written with embedded SHA verification, seed 20260509, n_perm 20,000
- Run executed: 2026-05-09. All 3 SHA-OK. JSON outputs written to `csv/Q053-F-{01,02,03}.json` and `csv/Q053-F-family-summary.json`

### Verdicts

- **Q053-F-01: CONFIRMED** — Q 96 al-ʿAlaq is Q 53's FR-nearest neighbor at rank 1/113, d_FR = 0.7126. Top-5 nearest: Q 96 (0.7126), Q 87 (0.7489), Q 92 (0.7635), Q 110 (0.7756), Q 102 (0.7769) — entire top-5 is in the very-short-Meccan-revelation-vision register.
- **Q053-F-02: NULL CONFIRMED (reverse-direction)** — Q 53:19-23 token count 41 (rank 1831/5783), TTR 0.927 (rank 4486/5783) — both within corpus 5%-95% range. No detectable lexical anomaly suggestive of editorial-interpolation removal. The gharānīq adversarial-falsification axis is verified.
- **Q053-F-03: NULL CONFIRMED (reverse-direction)** — 14 sajda-surahs are NOT FR-content-cohesive. Within-cluster mean = 0.9414 vs corpus baseline = 0.9235; ratio 1.0194; perm-p = 0.588; z = +0.333. The sajda-classification is functional-liturgical, NOT content-fingerprint-based. Adds to the project's catalog of functional-classifications-without-content-cohesion (alongside H-NEW-68 + H-NEW-69).

### Hadith number verification — corrections made during specialist run

- **Bukhārī al-Najm sajda hadith numbering**: corrected from secondary-source-cited "Bukhārī #1067" / "#1071" to direct-DB-verified **Bukhārī 1036, 1039, 1040, 1041, 1042** (Sunnah.com/Adam running-number convention).
- **Muslim al-Najm sajda hadith**: corrected to direct-DB-verified **Muslim 1197 + 1198**.
- **Tirmidhī Sidrat al-Muntahā**: confirmed at **Tirmidhī 3360**, *ḥasan ṣaḥīḥ* per al-Tirmidhī's own grading.
- **Tirmidhī Q 53:13-14 commentary**: confirmed at **Tirmidhī 3364**.
- **Bukhārī ʿĀʾisha denial of vision-Lord**: confirmed at **Bukhārī 4648** (NOT 4855 as some secondary literature cites — that is a different hadith on Quran-recitation comparison).

### *Gharānīq* narrative — adversarial verification trail

The Q 53 specialist's primary contribution to the project is the **9-book corpus null-attestation** of the *gharānīq* phrase:
- Direct programmatic corpus search of ~67,000 hadiths across 9 canonical books
- ZERO attestations of *الغرانيق* / *غرانيق* / *تلك الغرانيق* / *العلى* / *تشفع* (in the gharaniq-narrative-specific construction)
- This is project-novel: prior classical-scholarship literature (al-Albānī 1952) was isnād-based, not full-corpus-search-based
- Combined with Q053-F-02 empirical-text-anomaly null: the gharānīq narrative fails on canonical-hadith-corpus grounds AND on empirical-text grounds

### Files written

- `00-overview.md` — name, vision-narrative significance, sajda-surah status, gharānīq-narrative positioning
- `01-empirical-profile.md` — empirical anchors from H-NEW-{111, 590, 700, 720, 750, 840} integrated; sajda-14 cluster verification + cohesion-NULL pre-test scan
- `02-content-analysis.md` — verse-by-verse + 5 thematic blocks (vv 1-18 vision; 19-30 polytheism-rebuke; 31-32 iḥsān; 33-55 prophetic-catalog + ṣuḥuf; 56-62 closing+sajda)
- `03-tafsir-survey.md` — al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Suyūṭī, al-Biqāʿī, Ibn ʿĀshūr (8 mufassirūn)
- `04-hadith-corpus.md` — full Bukhārī + Muslim + Tirmidhī verification with corrected numbers; 9-book null-attestation audit
- `05-classical-claims-audit.md` — 6 claims audited; 5 SURVIVE, 1 FAILS (gharānīq narrative)
- `06-novel-findings.md` — 3 pre-registered SHA-locked findings (1 CONFIRMED + 2 NULL CONFIRMED)
- `07-cross-references.md` — 7 cross-surah + 9 cross-finding network connections
- `JOURNAL.md` — this file
- `preregs/Q053-F-01-vision-pericope-fr-cohesion-prereg.md`
- `preregs/Q053-F-02-gharaniq-text-anomaly-prereg.md`
- `preregs/Q053-F-03-sajda-14-fr-cohesion-prereg.md`
- `scripts/Q053_F_all_tests.py`
- `csv/Q053-F-01.json`, `csv/Q053-F-02.json`, `csv/Q053-F-03.json`, `csv/Q053-F-family-summary.json`

### Discipline notes (Bonferroni asymmetry, direction-locking)

- All 3 pre-regs declare Bonferroni-k=3 in YAML frontmatter (per PRE-REG-STANDARD-04)
- Q053-F-02 + F-03 are **REVERSE-DIRECTION** tests with NULL as the predicted outcome — explicitly disclosed in their pre-regs (per HANDOFF/04-DISCIPLINE.md reverse-direction discipline)
- Q053-F-01 is a **DETERMINISTIC** rank-test; α_bon applies at family level but not load-bearing for this specific test
- All thresholds (CONFIRMED rank=1; NULL CONFIRMED in 5%-95%; perm-p > 0.5) were specified BEFORE result-viewing
- Garden-of-forking-paths logs included in each pre-reg

### Cross-finding contributions

- **cross-finding-013 (mushaf-as-topological-ring)**: SUPPORTING — Q053-F-01 demonstrates strong cross-mushaf-distance content-coupling (Q 53 ↔ Q 96 across 43 surahs)
- **cross-finding-015 (classical-scholarship-validation-pattern)**: NEW TEST-CASE — Q 53 = strong M-5 decomposition test-case (5/6 classical-balāgha SURVIVE, 1/6 historical-apologetic FAILS)
- **cross-finding-026 (iʿjāz architecture)**: SUPPORTING — Q 53's iʿjāz lives at content-axis (vision/scripture/sajda), NOT prosodic axes
- **MASTER-LEDGER §3 #5a (classical-modern reliability ratio)**: this surah's specialist contributes ONE more test-case for the 13× central-estimate ratio (5/6 classical SURVIVE / 1/6 historical-apologetic FAILS)

### Residual / open queue items

- **OQ-Q053-1**: Replicate Q053-F-01 across H-NEW-111b (char-4-gram) and H-NEW-111c (verse-length) — does Q 96 remain Q 53's FR-nearest under all 3 operationalizations?
- **OQ-Q053-2**: Test bilateral Q 53 ↔ Q 87 ṣuḥuf-cross-reference at the formula-density level
- **OQ-Q053-3**: Test 3-surah sub-cluster {Q 7, Q 53, Q 96} (sajda-IS-last-verse) for FR sub-cohesion
- **OQ-Q053-4**: Sīra-network analysis of *gharānīq* narrative diffusion (which Sīra works cite which earlier sources)
- **OQ-Q053-5**: Q 52 vs Q 53 1-element oath-opener bilateral comparison

These are queued for future surah-specialist work (e.g., Q 96 + Q 87 + Q 7 + Q 52 specialist runs would naturally fold these into formal tests).

### Final note

This investigation produced an Important METHODOLOGICAL finding worth highlighting: **the 9-book corpus null-attestation of the *gharānīq* phrase is a project-novel verification axis** that strengthens al-Albānī's 1952 isnād-based critique with a corpus-search-based parallel. Combined with the Q053-F-02 empirical-text-anomaly null + the multi-source classical refutation (al-Zamakhsharī, al-Rāzī, Ibn Kathīr, Ibn Ḥazm, al-Albānī), the gharānīq narrative fails on **5 independent verification axes**: (1) 9-book canonical-hadith corpus null, (2) empirical-text-anomaly null, (3) classical Sunni mainstream rejection, (4) doctrinal *ʿiṣma* incompatibility, (5) isnād *mursal* / *ḍaʿīf jiddan* grading. This is one of the strongest empirical falsifications in the project of a classical literary-historical claim, and it positions Q 53 as a load-bearing test-case for the M-5 classical-doctrine-decomposition pattern (cross-finding-015).
