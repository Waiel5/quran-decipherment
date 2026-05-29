---
surah: 66
surah_name_ar: التحريم
surah_name_translit: al-Taḥrīm
file_type: journal
date_last_updated: 2026-05-29
phase: B+
---

# Q 66 al-Taḥrīm — Investigation Journal

## 2026-05-29 — Wave-N full 8-file deep-dive (single-specialist landing)

**Pre-flight (in order):**
1. Read the quran-investigation skill (SKILL.md).
2. Read `INVESTIGATION-PROTOCOL.md` (full).
3. Reviewed template dirs `surahs/Q073-al-muzzammil/` and `surahs/Q058-al-mujadala/` (structure, depth, tone).
4. Confirmed `surahs/Q066-al-tahrim/` did not exist; created it + `csv/`.

**Data extraction (all from disk, no values from memory):**
- `quran-text/quran-no-tashkeel.json` Q 66 (id 66, Medinan, 12 verses) — verified 12 verses; computed
  254 words / 1,105 letters (marks stripped); 96 distinct QAC roots (171 root-tokens) via
  `data/morphology/root-index.json`.
- `data/revelation-order.csv`: Q 66 = revelation #107 (Tanzil EgStd), Nöldeke #109, Medinan. Q 9 = #113.
- `data/hafs-verse-counts.tsv` line 66 = 12.
- **h-new-111.json** (FR): Q 66 mean FR 0.9093; nearest Q 110 (0.726); prophet-vocative co-members all
  mid-to-far (Q 60 r27, Q 49 r32, Q 65 r49, Q 33 r72).
- **h-new-590.json** (outlier): Q 66 window {63-69}, delta_pct −1.90, p 0.808, classification NULL (cohesion member).
- **h-new-700.json** (rhyme/phoneme): top final-letter ن frac 0.4167; phoneme vec idx 65 = [0.0217,0.0443,0.0235,0.1095].
- **h-new-750.json** (iʿjāz): rhyme_entropy 1.2367; sig_A +0.9856 (rank 34); sig_B +0.3466 (rank 48); local_cohesion 1.152.
- **h-new-720.json** (TSP): Q 65→Q 66 delta_raw −0.03397 rank 5/113 (seamless); Q 66→Q 67 +0.07804 rank 67.
  Confirmed 13 seamless seams; Q 64→Q 65→Q 66 double-seamless.
- **h-new-840.json** (UAS): Q 66 UAS −1.0521 rank 77/114.
- **h-new-1520-prophet-vocative-pericope.md**: read; Q 66 contributes windows 1-3 & 9-11; Q 9:73-75 × Q 66:9-11
  flagged as #2 directive pair (J=0.245), "textual near-twins."

**Tafsīr (read in Arabic from disk):**
- al-Ṭabarī (spa5k `ar-tafsir-al-tabari/66/1.json`): Māriya-primary; Zayd b. Aslam, al-Shaʿbī←Masrūq; *anta ʿalayya ḥarām* = laghw.
- al-Zamakhsharī (`raw/zamakhshari-kashshaf.openiti.raw.txt` L66958-67008): Māriya + honey; *zalla*; taḥilla two senses; madhhab survey.
- al-Rāzī (`raw/razi-mafatih-al-ghayb.openiti.raw.txt` L243800-243859): Q65→Q66 munāsaba; 3 masāʾil (tanbīh not ʿitāb); cites al-Kashshāf verbatim (confirmed by on-disk comparison).
- al-Qurṭubī (spa5k `ar-tafseer-al-qurtubi/66/{1,11,12}.json`): Medinan-consensus, 12 āyāt, "Sūrat al-Nabī"; honey-version (Muslim); v11 Yaḥyā b. Sallām ring-reading; v12 jayb-reading.
- Ibn Kathīr (spa5k `en-tafisr-ibn-kathir/66/{1,10}.json`): Bukhārī honey-narration; v9 jihād; vv10-12 independence-of-fate.

**Ḥadīth (verified `idInBook` on disk, `ahmedbaset-json/db/by_book/the_9_books`):**
- Honey/Maghāfir: Bukhārī #4704 (Book 65 Tafsīr), #5058, #5059, #6447, #6714; Muslim #3555, #3556 (Book 18);
  Abū Dāwūd #3715, #3716 (Book 27); Nasāʾī #3427, #3804, #3968.
- Ibn ʿAbbās–ʿUmar (tafsīr of v 4): Bukhārī #4705, #4706, #4707, #4708 (Book 65), #2372 (Book 46), #4983 (Book 67);
  Tirmidhī #3402 — grading **ḥasan ṣaḥīḥ gharīb** read from Arabic colophon.
- Māriya version: al-Wāḥidī *Asbāb* Q 66:1 (Ibn ʿAbbās←ʿUmar); al-Ṭabarī Q 66:1.
- No surah-named faḍāʾil ḥadīth found in 9-book set → flagged as data-gap (not absence claim).

**Pre-registration (Q066-F-01) — LOCKED BEFORE COMPUTATION:**
- Pre-reg file written first: `Q066-F-01-tahrim-seal-prereg.md`.
- SHA-256: `749a186efd3959ab1e0eddfa435f916f8104454bf347a43d9466c1a1705c4d44`.
- Embedded in `scripts/Q066_F_01_tahrim_seal.py` as EXPECTED_SHA; verified at runtime (printed "SHA OK").
- Seed 20260509; 10,000 perms.
- Two arms: A = verbatim verse-twin rarity (deterministic); B = antithetical dual-exemplar seal (B-H1 corpus-
  exclusivity deterministic; B-H2 direction-locked believer-pair-tighter; B-H3 permutation cohesion vs null).
- Direction-lock for B-H2/B-H3 set BEFORE running. Anticipated risk (frame-root bias pulling v10-v11) documented in pre-reg.

**Computation result (`csv/Q066-F-01.json`):**
- Arm A: Q 66:9 partner = [(9,73)] (A-H1 ✓); 11 verbatim-twin groups ≥10 tok (A-H2 ✓). **CONFIRMED.**
- Arm B: B-H1 ✓ (adjacent kafarū→āmanū frame corpus-exclusive to Q66:10-11). B-H2 ✗: J(11,12)=0.0833 <
  J(10,11)=0.2000 — direction REVERSED. B-H3 ✗: z=+0.715, p_perm=0.2543. **NULL (pre-commit violation), 1/3.**

**Decision point:** Arm B direction reversed on a locked prediction → published as NULL with full prominence
(PRE-REG-STANDARD-04, MEMORY feedback_bonferroni / equal-NULL-prominence). NOT massaged. The reversal mechanism
(parable-frame roots shared by v10-v11 but not v12; Maryam's verse is the lexical outlier) is documented as a
first-class scale-of-aggregation finding (frame-cohesion ≫ theme-cohesion). No garden-of-forking-paths shift:
the analysis matched the pre-reg exactly.

**Files produced:** 00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey, 04-hadith-corpus,
05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this), + pre-reg + script + csv/Q066-F-01.json.

**Verdict:** Q066-F-01 = Arm A CONFIRMED (verbatim twin Q66:9≡Q9:73) + Arm B NULL (pre-commit violation;
B-H1 frame-exclusivity passes). Honest, equal-prominence NULL.

**Queued follow-ups:** Q066-F-02 (verbatim-twin chronology), Q066-F-03 (v5 8-virtue corpus-singleton formal promotion),
Q066-F-04 (parable-pair-scale re-test of the seal). Corpus-wide verbatim-long-verse-twin network → candidate H-NEW.
