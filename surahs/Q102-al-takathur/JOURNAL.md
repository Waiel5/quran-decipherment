---
surah: 102
surah_name_ar: التكاثر
surah_name_translit: al-Takāthur
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 102 al-Takāthur — Investigation Journal

## 2026-05-30 — Wave-N full 8-file deep-dive (completion of a stalled prior run)

**Context.** A prior run wrote `00-overview.md`, the pre-reg
(`Q102-F-01-kalla-reduplication-prereg.md`), the script
(`scripts/Q102_F_01_kalla_reduplication.py`), and `csv/Q102-F-01.json`, then stalled before writing
files 01-07 + JOURNAL and before committing. This session completed the template.

**Pre-flight (in order):**
1. Read the quran-investigation skill (SKILL.md).
2. Read `INVESTIGATION-PROTOCOL.md` (binding methodology).
3. `ls surahs/Q102-al-takathur/` — read every existing file (00-overview, pre-reg, script, csv) without
   rewriting the complete ones.
4. Reviewed exemplar `surahs/Q066-al-tahrim/` (all 8 files) for structure, depth and tone.

**Finalize the pre-registered test (Q102-F-01) — re-ran the script from disk:**
- `python3 scripts/Q102_F_01_kalla_reduplication.py` → printed **"SHA OK:
  87433a4dd51b12605a09e63140437f480ac2e551b05014137837b0d31046acf4"** (pre-reg file hash == embedded
  EXPECTED_SHA == `prereg_sha` in the JSON; independently re-computed the pre-reg SHA = identical).
- Result reproduced the on-disk JSON exactly:
  - **Arm A:** Q 102 *kallā* verses [3,4,5], run 3; others_max_run 2; census 33; first-half rebuke
    surahs []. A-H1/A-H2/A-H3 all True → **CONFIRMED.**
  - **Arm B:** single-particle adjacent near-twin pairs = [(75,34,35,ثم),(78,4,5,ثم),(102,3,4,ثم)];
    B-H1 count 3 (q102_3_4 present), B-H1 FAIL (pre-commit violation, count≠1); bare-threat locs
    [[102,3],[102,4]], B-H2 PASS → **DIRECTIONAL.**
  - **B-H3 (context):** obs 3, null_mean 0.183, p_perm ≈ 0.0002.

**Data extraction (all from disk, no values from memory):**
- `quran-text/quran-no-tashkeel.json` Q 102 (id 102, Meccan, 8 verses) — verified 8 verses; computed
  **28 words / 123 letters** (marks stripped); **11 distinct QAC roots** (Elm, Eyn, jHm, kvr, lhw, nEm,
  qbr, rAy, sAl, yqn, zwr) via `data/morphology/quranic-corpus-morphology-0.4.txt`.
- `data/revelation-order.csv`: Q 102 = revelation #16, period Meccan, noldeke_phase "Early Meccan".
- `data/hafs-verse-counts.tsv` line 102 = 8.
- **h-new-111.json** (FR, index 102): mean FR **0.8011**; nearest **Q 108 (0.2937)**; top-8 = Q108/107/106/
  111/103/100/105/112; Q 101 rank 13 (0.3863); farthest Q3/4/9/6/2. Corpus mean 0.9235.
- **h-new-590.json** (outlier): Q 102 NOT in α-tested candidates {1,9,18,55,62,112}, BUT `all_surahs_results`
  carries a descriptive record: window {99-105}, d_W 0.3577, d_W−X 0.3536, **delta_pct 0.0, p 1.0,
  classification NULL** (deep in-block cohesion). [Corrects 00-overview's "DATA-GAP" framing.]
- **h-new-700.json** (rhyme/phoneme): top final-letter ن frac **0.5** (4/8); phoneme vec idx 101 =
  [0.0, 0.0732, 0.0325, 0.0407].
- **h-new-750.json** (iʿjāz): rhyme_entropy 1.0397 (z +0.49); mean_content_distance 0.8011 (z −1.21);
  local_cohesion 2.769 (z +1.70); **sig_A +1.6963 (rank 12), sig_B +2.1914 (rank 4/114, top-4).**
- **h-new-720.json** (TSP): Q 101→Q 102 delta_raw +0.02873 rank 30/113; Q 102→Q 103 +0.04795 rank 44/113.
- **h-new-840.json** (UAS): UAS **−0.7412 (rank 67/114)**; abs_outlier 0.0 (non-candidate), max_cost
  0.04795, abs_ijaz 1.6963 (=sig_A). Understated due to abs_outlier=0.
- **h-new-1820.json** (title-density): Q 102 root *kvr*, title_density_rank **2**, is_rank_1 false,
  rank_1_surah **108**. Q 108 rank-1. Title-density independence VINDICATED.
- **h-new-2230-qac-lemma-numerical-rerun.md** (claim 7): rebuke-*kallā* lemma = **33 EXACTLY** (raw
  substring 38 conflates 5 *kullan*); replicated by Q102-F-01 Arm A.

**Tafsīr (6 authorities, cited scholar+work+passage from disk):**
- al-Ṭabarī (spa5k `ar-tafsir-al-tabari/102/{1,2,4}.json`): v1 boast in wealth/numbers (Qatāda "naḥnu
  akthar min Banī Fulān"); v2 *ʿadhāb al-qabr* proof via ʿAlī (al-Minhāl←Zirr←ʿAlī isnād — same family as
  Tirmidhī #3439); v4 *takrīr li-l-taghlīẓ* + al-Ḍaḥḥāk's kuffār/muʾminūn reading.
- al-Qurṭubī (`ar-tafseer-al-qurtubi/102/{1,8}.json`): "makkiyya fī qawl jamīʿ al-mufassirīn, rawā
  al-Bukhārī annahā madaniyya, thamānī āyāt"; two readings of *alhā* (boast/forget); Imruʾ al-Qays shāhid;
  v8 *al-naʿīm* via Muslim←Abū Hurayra hunger-hadith.
- Ibn Kathīr (`en-tafisr-ibn-kathir/102/1.json`): "Book of Ar-Riqaq … Ubayy bin Kaʿb: we used to think
  this was a part of the Qurʾan until al-Takāthur was revealed" (= Bukhārī #6201).
- al-Jalālayn (`en-al-jalalayn/102/{2,4,7}.json`): v2 two readings (death/grave-counting); v4 doubling =
  soul-extraction + grave; v7 *ʿayna* verbal noun, ra'ā=ʿāyana, "repeated for emphasis".
- al-Baghawī (`ar-tafsir-al-baghawi/102/2.json`): asbāb — Qatāda (Jews) / Muqātil-al-Kalbī (Banū ʿAbd
  Manāf vs Banū Sahm grave-counting boast).
- al-Suyūṭī *Itqān* nawʿ 40 ← al-Dānī: *kallā* census = 33, mufaṣṣal-concentrated (via H-NEW-2230).

**Ḥadīth (verified `idInBook` on disk, tashkeel-stripped matn + chapter cross-checked):**
- "māl mālī" servant: Muslim **#7236** (Zuhd); Tirmidhī **#2411** (Zuhd, *ḥasan ṣaḥīḥ*), **#3438** (Tafsīr,
  *ḥasan ṣaḥīḥ*); Nasāʾī **#3621**.
- Valley-of-gold + Ubayy abrogation: Bukhārī **#6197/#6200/#6201** (Kitāb al-Riqāq, adjacent); Muslim
  **#2299** (Zakāt); Tirmidhī **#2406** (Zuhd).
- ʿAlī grave-torment: Tirmidhī **#3439** (Tafsīr, *gharīb*); al-Ṭabarī v2 (same al-Minhāl←Zirr←ʿAlī isnād).
- Recitation: Aḥmad **#639** (Musnad ʿAlī) — witr of 9 mufaṣṣal surahs incl. al-Takāthur.
- No dedicated faḍāʾil ḥadīth in 9-book set → flagged data-gap (not absence claim).

**Corrections logged (relative to 00-overview):**
1. H-NEW-590: Q 102 is NOT a pure "DATA-GAP" — a descriptive `all_surahs_results` NULL record exists
   (delta_pct 0.0, p 1.0, window {99-105}). The UAS abs_outlier=0 stands; the descriptive NULL is now
   reported in `01` §2. (00-overview §3 said "NOT a tested candidate → DATA-GAP, treated as 0".)
2. Grave-torment narration: 00-overview §7 attributed it to al-Ṭabarī alone; it is also Tirmidhī **#3439**
   (*gharīb*), same isnād family. Logged in `04` §7.

**Decision point — Arm B verdict.** B-H1's locked direction (count = 1, Q 102-exclusive) was violated:
the *thumma*-doubled adjacent threat-refrain is a 3-member family {Q 75, Q 78, Q 102}. Published as a
pre-commit violation with full prominence; B-H2 (bare-threat Q 102 singleton) PASSES; net Arm B =
DIRECTIONAL per the pre-reg verdict map (exactly one of two gating cells). NOT massaged. No
garden-of-forking-paths shift: the analysis matched the pre-reg exactly; the locked direction was simply
wrong, and the correction is the finding (Q 102 belongs to a *thumma*-family AND uniquely strips the
threat bare).

**Files produced this session:** 01-empirical-profile, 02-content-analysis, 03-tafsir-survey,
04-hadith-corpus, 05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this).
Pre-existing (not rewritten): 00-overview, pre-reg, script, csv/Q102-F-01.json.

**Verdict:** Q102-F-01 = **Arm A CONFIRMED** (corpus-unique 3-consecutive rebuke-*kallā* run, vv 3-4-5;
census 33, homograph-clean) + **Arm B DIRECTIONAL** (bare-threat Q 102 singleton ✓ B-H2; *thumma*-refrain
is a 3-member family ✗ B-H1, pre-commit violation). Honest, equal-prominence reporting.

**Queued follow-ups:** Q102-F-02 (formalize the *thumma*-doubled threat-refrain family {Q 75, 78, 102}
as a corpus cross-finding; is *thumma* the unique doubler?); Q102-F-03 (the *ʿilm→ʿayn→ḥaqq* al-yaqīn
3-grade cross-surah distribution); Q102-F-04 (Q 102↔Q 108 *kvr* FR-twin + title-density-#1 coincidence).
