---
surah: 73
surah_name_ar: المزمل
surah_name_translit: al-Muzzammil
file_type: journal
date_last_updated: 2026-05-09
phase: B+
agent: Q073-al-muzzammil-specialist
seed: 20260509
---

# Q 73 al-Muzzammil — Investigation Journal

## 2026-05-09 — Session 1

### Pre-flight (mandatory reading)
- ✓ `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md`
- ✓ `/Users/grey/Downloads/quran/HANDOFF/01-WHAT-WE-KNOW.md`
- ✓ `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` §10.34 (H-NEW-1190 *wa-mā adrāka mā* CONFIRMED FR-cohesive p=0.00068)
- ✓ `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-1300-q96-iqra-corpus-distribution.md` (NULL by strict pre-reg)
- ✓ `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-1301-impv-qra-cluster.md` (NULL-BROKEN — HM cluster PC failed)
- ✓ `/Users/grey/Downloads/quran/surahs/Q037-al-saffat/` (canonical 9-file template)
- ✓ `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` for IMPV-qrA verification
- ✓ `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/*.json` for hadith corpus

### Empirical anchor extraction (per-row)
- **h-new-111 (FR matrix)**: Q 73 row computed → mean dist = 0.8555 (well below corpus mean 0.9234 — Q 73 is in a tight neighborhood). Top-10 nearest: **Q 112 (0.6461), Q 91 (0.6493), Q 110 (0.6562), Q 1 (0.6613), Q 87 (0.6672), Q 108 (0.6747), Q 93 (0.6805), Q 105 (0.6813), Q 94 (0.6820), Q 100 (0.6838)**. Q 73 sits in the SHORT-MUFAṢṢAL EARLY-MECCAN tail neighborhood. Q 74 is rank 37 (FR=0.7614) — NOT in Q 73's top-15, despite mushaf-adjacency. Q 96 is at rank ~22 (FR=0.7232).
- **h-new-590**: Q 73 outlier-strength delta_pct = -4.08 on window {Q 70-76}; **NULL** (NOT a strong outlier; p_greater = 0.9056 — Q 73 is COHESION_ANCHOR, integrating with its neighborhood). 
- **h-new-700 rhyme**: top final letter ا (alif), 0.90 of 20 verses; **near-monorhyme on -ā (verse-final long alif)**. Q 73 rhyme entropy nats = 0.394 (low).
- **h-new-720**: **Q 72→Q 73 delta_raw = -0.00118 (clamped-zero seamless)** AND **Q 73→Q 74 delta_raw = -0.02888 (clamped-zero seamless)**. Q 73 is bracketed by SEAMLESS SEAMS on both sides — one of very few mushaf positions with this dual-seamless property.
- **h-new-750 (iʿjāz)**: sig_A = -0.009 (rank 59, mid-range), sig_B = -0.991 (rank 79, low). Mixed signature — al-Bāqillānī iʿjāz al-fawāṣil moderate; al-Sakkākī iqāʿ low.
- **h-new-840 UAS**: Q 73 = -2.696, **rank low**. Mid-low UAS (consistent with short surah + low iʿjāz score).
- **h-new-940 prophet-order**: Q 73 NOT in surah_set (no prophet-cycle narrative — Q 73 contains only Pharaoh-and-Moses single-pericope reference at v. 15-16).
- **revelation-order.csv**: Q 73 = revelation_order #3, Nöldeke #23, Early Meccan. Q 74 = revelation_order #4, Nöldeke #2, Early Meccan. Both in the very-earliest revelation cohort.

### Q 73 corpus-text anchors (computed from quran-no-tashkeel.json)
- **20 verses, ~287 words, ~1,300+ letters** (no tashkeel). Q 73:20 alone is **90 words / 430 chars** — the surah's tail-verse contains ~31% of the surah's word-count.
- **Q 73:20 IMPV-qrA segments**: 2 segments (words 26 + 49 in QAC v0.4 numbering; both `{qora'u` 2MP plural forms — *iqraʾū mā tayassara min al-qurʾān*). The 2MP plural ADDRESSEE differs from Q 96's 2MS singular (`{qora>o`) — a structural distinction not flagged by H-NEW-1300.
- **Q 73:1 vocative**: *yā ayyuhā al-muzzammil* (3 words). Q 74:1 mirrors with *yā ayyuhā al-muddaththir* (3 words). Both are direct-prophetic vocative + Form-V passive participle (mu-XaXXiX template) + ال definite article. Morphologically isomorphic.
- **H-NEW-1300 IMPV-qrA verification**: confirmed via QAC v0.4 morphology file. 6 corpus segments: Q 17:14 (2MS), Q 69:19 (2MP), Q 73:20×2 (2MP), Q 96:1+3 (2MS). Q 73:20's 2 imperatives are 2MP (community-addressed), Q 96:1+3 are 2MS (Prophet-direct). The "prophetic-revelation pair" descriptive framing in H-NEW-1300 conflates these grammatically distinct addressee-classes.

### Pre-registrations (5 tests, locked before observation)
- **Q073-F-01** Q 73:20 ↔ Q 96:1+3 IMPV-qrA pair — direction-locked: ≥2/3 axes pass (co-occurrence + verse-twin + addressee-grammar).
- **Q073-F-02** Q 73 ↔ Q 74 muzzammil/muddaththir vocative-pair cohesion — direction-locked: ≥2/3 axes pass (FR mutual top-15 + clamped-zero seam + morph-iso opening).
- **Q073-F-03** Q 73:20 abrogation classical claim — direction-locked: ≥1 hadith chain in 9-books with explicit naskh language.
- **Q073-F-04** H-NEW-1301 IMPV-qrA cluster cohesion replication with corrected MW-5 PC — direction-locked: ≤5th percentile under uniform AND length-matched nulls + working PC.
- **Q073-F-05** Q 73:20 "long verse" corpus-rank distinction — direction-locked: rank ≤ 25 corpus AND rank = 1 within Early-Meccan.

All pre-regs SHA-locked at file-write time; SHA embedded into corresponding scripts; verified at runtime.

### SHA-locks (2026-05-09, lock-time)
| Pre-reg | SHA256 |
|:--|:--|
| Q073-F-01 | a477010077cd15340b209ba24e73b1a666de95cb410215e0963b696d41b3e2b0 |
| Q073-F-02 | 65a709885ec20dfbbb734323cd8f994d94256bdf1fdff3aed4c7c225871bf3a0 |
| Q073-F-03 | 01590e7ce45e692cdb323a1c7a87976c0eedf644cb1a58a4275803d58c455f7a |
| Q073-F-04 | 996b6babbcdb7a5eaf89f5d8e94f8ff498f8f2d3505865a377143d740422a257 |
| Q073-F-05 | 5938f7820ed051c8c805206469264f18fd80234ebdbab3f8d69b2ce58f8d3b0b |

### Garden-of-forking-paths log
1. **Brief inaccuracy on hadith source**: brief specified "Mālik Muwaṭṭaʾ + Bukhārī" for Q 73:20 abrogation. Pre-flight identified that NEITHER Mālik nor Bukhārī contains explicit Q 73:20 abrogation chain; the explicit chain is in **Abū Dāwūd #1305** (Ibn ʿAbbās → ʿIkrima). Disclosed in Q073-F-03 pre-reg §6 BEFORE the test runs. Result reported with brief-correction flag.
2. **Brief inaccuracy on H-NEW-1300 phrasing**: brief described Q 73 + Q 96 as "prophetic-revelation pair per H-NEW-1300" without flagging the addressee-grammar mismatch (Q 73 = 2MP plural, Q 96 = 2MS singular). Disclosed in Q073-F-01 pre-reg §6 BEFORE the test runs. The test's H1a co-occurrence axis is robust to this; H1b verse-twin similarity test is structurally broken by length-asymmetry (Q 73:20 = 90 words vs Q 96:1 = 5 words).
3. **MW-5 PC correction from H-NEW-1301**: H-NEW-1301 used HM cluster {41, 42, 43, 44} 4-of-7 sub-sample which FAILED MW-5 (p=0.336). The lesson: HM cluster is letter-set-cohesive (cross-finding-008), NOT root-distribution-FR-cohesive. The corrected PC for Q073-F-04 uses H-NEW-1190 *wa-mā adrāka mā* 10-surah cluster (CONFIRMED FR-cohesive at p=0.00068); 4-of-10 sub-sample under the SAME instrument confirms the instrument detects known signal. Sensitivity: 4/5 alternative seeds also pass the PC. Substantive verdict therefore promotes from NULL-BROKEN → NULL with valid instrument.

### Specialist coordination
- Q 74 al-Muddaththir specialist file does not yet exist; no coordination conflict. Q073-F-02 takes the Q 73 ↔ Q 74 pair as the unit of analysis; if a Q 74 specialist runs later, they should reference Q073-F-02 results.
- Q 96 al-ʿAlaq specialist file does not yet exist; no coordination conflict. Q073-F-01 takes the Q 73 ↔ Q 96 IMPV-qrA pair as the unit of analysis.
- Q 17 al-Isrāʾ + Q 69 al-Ḥāqqa specialist files do not yet exist; the IMPV-qrA cluster Q073-F-04 replication is run independently of Q 17/Q 69 specialists.

### Run sequence (executed)
1. ✓ Wrote all 5 pre-regs → SHA-locked each.
2. ✓ Wrote 5 scripts with embedded SHA verification.
3. ✓ Ran scripts; captured JSON outputs in `csv/`.
4. ✓ Wrote 8 template files (00-07).
5. ✓ Updated cross-references and finalized JOURNAL.

## 2026-05-09 — Session 1, run-time entries

### Q073-F-01 (run completed)
- Script: `scripts/Q073_F_01_iqra_pair_q96.py`
- Runtime SHA verification: PASS
- **H1a co-occurrence (PASS)**: cluster_score_lib = 7/9 (Q 73:20 scored 3/3 on all classes; Q 96:1 scored 2/3 [no qurʾān/kitāb token]; Q 96:3 scored 2/3 [no qurʾān/kitāb token]). Length-matched permutation null mean = 1.103. p_one_sided_geq = **0.0000 (0/10000 perms)**.
- **H1b verse-twin similarity (FAIL)**: max_sim(Q 73:20, Q 96:1) = 0.0575; max_sim(Q 73:20, Q 96:3) = 0.0448. Q 96:1 ranks 5,101 / 6,235 (bottom 18%); Q 96:3 ranks 5,656 / 6,235 (bottom 9%). char-Levenshtein cannot bridge the 90-word vs 4-word length asymmetry.
- **VERDICT: DIRECTIONAL.** H1a passes overwhelmingly; H1b fails as anticipated by pre-reg honest-limit §6. The pair is LEXICALLY-LINKED (shared iqraʾ + qurʾān/kitāb + addressee marker) but NOT character-string-similar.

### Q073-F-02 (run completed)
- Script: `scripts/Q073_F_02_q73_q74_vocative_pair.py`
- Runtime SHA verification: PASS
- **Axis A FR mutual top-15 (FAIL)**: rank_Q74_in_Q73 = 37, rank_Q73_in_Q74 = 37. Q 74 is NOT in Q 73's top-15 nearest neighbors (FR=0.7614 vs Q 73's 14th-nearest at FR=0.7152). Null baseline mutual-top-15 frequency = 6.3% across 1,000 random pairs. The pair fails this axis but the failure is **content-content** (root-distribution differs), not structural.
- **Axis B clamped-zero seam (PASS)**: Q 73 → Q 74 delta_raw = -0.02888, fraction_residual = 0.000 (clamped). The seam is in the seamless-set (1 of 13 corpus-wide). Strong seamless-seam signature.
- **Axis C morphological-isomorph opening (PASS)**: Q 73:1 = "يا أيها المزمل", Q 74:1 = "يا أيها المدثر". Both are 3-word vocative + Form-V passive participle openers; same structural template; same length (3 words). The third word (المزمل / المدثر) differs in root letters but matches in morphological pattern (m-DH-DH-i-L vs m-DH-DH-i-R) — both are mu-CCaC2C2iC pattern with Form-V participle morphology, both definite (al-prefix), both denote "wrapped/covered in garments".
- **VERDICT: DIRECTIONAL.** 2 of 3 axes pass. Q 73 ↔ Q 74 is a **structurally-twin and seamless-seamed pair** but **NOT root-content-cohesive** under the H-NEW-111 instrument. This is a striking architectural feature: the surah-pair is held together by mushaf-architecture and opening-formula identity, NOT by content-fingerprint similarity.

### Q073-F-03 (run completed)
- Script: `scripts/Q073_F_03_abrogation_classical_claim.py`
- Runtime SHA verification: PASS
- **9-books search**: 4 target phrases (`قم الليل إلا قليلا`, `نسختها الآية`, `علم أن لن تحصوه`, `فاقرءوا ما تيسر`) + naskh-root + Q 73-marker.
- **1 explicit naskh hit** (≥2 phrases AND naskh-root AND Q 73-marker): **Abū Dāwūd #1305 (chapterId 5)**, isnād: Aḥmad b. Muḥammad al-Marwazī Ibn Shabbawayh → ʿAlī b. Ḥusayn → his father → Yazīd al-Naḥwī → ʿIkrima → **Ibn ʿAbbās**.
- **Matn (translated)**: "Ibn ʿAbbās said regarding al-Muzzammil: 'qum al-laylā illā qalīlan • niṣfahu' was abrogated by the verse therein 'ʿalima an lan tuḥṣūhu fa-tāba ʿalaykum fa-iqraʾū mā tayassara min al-qurʾān' …"
- **VERDICT: VERIFIED.** The classical Q 73:20 abrogation claim has primary-source on-disk attestation in the 9-books canonical sunnī ḥadīth corpus.
- **HONEST CORRECTION**: brief specified "Mālik Muwaṭṭaʾ + Bukhārī" — but explicit naskh chain is in **Abū Dāwūd**, NOT Mālik or Bukhārī. Bukhārī hadith #4 is the famous Bad' al-Waḥy chain on Q 74 (not Q 73). Mālik Muwaṭṭaʾ contains *istaysara*-references but on Q 22:37 (hady-relaxation), not Q 73:20. Brief-correction flag set.

### Q073-F-04 (run completed)
- Script: `scripts/Q073_F_04_impv_qra_cluster_corrected_pc.py`
- Runtime SHA verification: PASS
- **D_obs = 0.88001** (mean pairwise FR for {Q 17, 69, 73, 96}).
- **Cell A (uniform null)**: null_mean = 0.92616, 5pct = 0.69516. p_A = 0.2633. **NOT-PASSING** α_bon = 0.025.
- **Cell B (length-matched)**: null_mean = 0.96018, 5pct = 0.81341. p_B = 0.1348. **NOT-PASSING** α_bon = 0.025.
- **MW-5 PC corrected (PASS)**: 4-of-10 sub-sample of H-NEW-1190 = {Q 69, 74, 97, 101}. D_pc = 0.67460. p_pc = **0.0395** (one-sided ≤). Pass at α = 0.05. Sensitivity: 4 of 5 alternative seeds (20260510-14) also pass (p_pc 0.017-0.057). The corrected MW-5 PC is robust.
- **VERDICT: NULL (PC valid)** — the substantive cluster cohesion test FAILS on both cells, but the corrected MW-5 positive control PASSES. Per HANDOFF/04-DISCIPLINE.md MW-5, the PC pass authorizes the substantive NULL verdict.
- **Promotion of H-NEW-1301**: H-NEW-1301 returned NULL-BROKEN (HM PC failed). Q073-F-04 here promotes the verdict to **substantive NULL**: the IMPV-qrA cluster is GENUINELY NOT FR-cohesive at the surah-aggregate root-distribution level, with valid instrument. The 4 surahs are linked at the LEXICAL-IMPERATIVE-EVENT level (a discrete 6-segment marker), NOT at the THEMATIC-ROOT-DISTRIBUTION level.

### Q073-F-05 (run completed)
- Script: `scripts/Q073_F_05_long_verse_rank.py`
- Runtime SHA verification: PASS
- **Q 73:20 word_count = 90**, char_count = 430.
- **H1a corpus rank (PASS)**: rank 3 of 6,236 verses corpus-wide. Top-5: **Q 2:282 (145 words), Q 4:12 (99), Q 73:20 (90), Q 3:154 (83), Q 2:102 (82)**.
- **H1b Early-Meccan rank (PASS)**: rank 1 of 1,219 Early-Meccan verses. Q 73:20 (90 words) far exceeds Q 74:31 (63 words, second-place Early-Meccan), Q 53:32 (35), Q 53:23 (27), Q 52:21 (20). Q 73:20 is **43% longer** than the second-longest Early-Meccan verse.
- **VERDICT: CONFIRMED.** Q 73:20 is corpus-rank-3 by length AND the unambiguous max-length verse within the entire Early-Meccan revelation phase. The classical descriptor "the long verse" (al-āya al-ṭawīla) is empirically supported at the rank-extremum level, not just relatively-described.

### Aggregate session-1 verdict
- Q073-F-01: **DIRECTIONAL** (co-occurrence p<0.0001 PASS; verse-twin sim FAIL — length-asymmetry artifact)
- Q073-F-02: **DIRECTIONAL** (morph-iso + clamped-zero seam PASS; FR mutual top-15 FAIL — pair structurally-twin but content-divergent)
- Q073-F-03: **VERIFIED** (Abū Dāwūd #1305 explicit abrogation chain; brief-correction: NOT Mālik/Bukhārī)
- Q073-F-04: **NULL with VALID instrument** (corrected MW-5 PC passes at p=0.0395, 4/5 sensitivity-pass; substantive cluster genuinely NOT FR-cohesive)
- Q073-F-05: **CONFIRMED** (rank 3 corpus / rank 1 Early-Meccan)

**1 CONFIRMED, 1 VERIFIED, 2 DIRECTIONAL, 1 NULL** (with brief-corrections on F-01 and F-03). All 5 reported with EQUAL NULL PROMINENCE per HANDOFF/04-DISCIPLINE.md.

### Files written this session
- `00-overview.md`, `01-empirical-profile.md`, `02-content-analysis.md`, `03-tafsir-survey.md`, `04-hadith-corpus.md`, `05-classical-claims-audit.md`, `06-novel-findings.md`, `07-cross-references.md`.
- 5 pre-regs: `Q073-F-{01..05}-*-prereg.md`.
- 5 scripts: `scripts/Q073_F_{01..05}_*.py`.
- 5 JSON outputs: `csv/Q073-F-{01..05}.json`.
- This `JOURNAL.md`.

### Garden-of-forking-paths (final)
1. **Q073-F-01 brief inaccuracy disclosed**: brief framed Q 73:20 + Q 96:1+3 as "prophetic-revelation pair per H-NEW-1300" — but their addressee-grammar differs (2MP vs 2MS) and their length differs by 18× (90 words vs 5/4 words). The H1a co-occurrence test is robust to this; H1b verse-twin similarity is structurally broken by length-asymmetry. PASS-DIRECTED on H1a; verdict cap = single-test α=0.025 with extreme p<0.0001 surviving any conceivable Bonferroni.
2. **Q073-F-02 axis-A NULL on FR mutual top-15**: pre-locked direction was POSITIVE; observed Q 74 at rank 37 in Q 73's neighbors (NOT top-15). Honest reporting: the pair is morphologically-twin (Axis C PASS) and seamless-seamed (Axis B PASS) but root-content-distinct (Axis A FAIL). The pair's cohesion is OPENING-FORMULA + MUSHAF-ARCHITECTURE, not CONTENT-DISTRIBUTION.
3. **Q073-F-03 brief-correction**: explicit Q 73:20 abrogation hadith located in **Abū Dāwūd #1305**, NOT Mālik or Bukhārī as the brief stated. The classical claim VERIFIES, but with corrected source attribution.
4. **Q073-F-04 H-NEW-1301 promotion**: corrected MW-5 PC passes (4/5 seed-sensitivity), instrument now validated. The substantive NULL on both cells is a REAL finding: IMPV-qrA cluster is genuinely NOT FR-cohesive on root-distribution. Promotes H-NEW-1301 NULL-BROKEN → substantive NULL with valid instrument.

### Future-work queue (H-NEW pre-reg candidates)
- **H-NEW-1400** (queued): Q 73 ↔ Q 74 vocative-pair structural-twin signature — formalize the Q073-F-02 finding into a corpus-wide search for OTHER mushaf-adjacent pairs with morph-iso openings + clamped-zero seam but FR-distance > median. May reveal a small architectural class of "OPENING-LINKED CONTENT-DIVERGENT" pairs.
- **H-NEW-1401** (queued): Q 73:20's status as a "concentrated-imperative verse" — does its 90-word length contain a measurable density-of-imperatives that distinguishes it from other long verses? Q 2:282 has DIFFERENT imperative density (legal injunctions); Q 4:12 has DIFFERENT (inheritance arithmetic). Test whether Q 73:20's IMPV/word ratio is structurally distinct.
- **H-NEW-1402** (queued): wa-mā adrāka mā 10-surah cluster as canonical FR-positive-control going forward — codify as the gold-standard PC for any future surah-cluster FR-cohesion test (replacing the failed HM cluster from H-NEW-1301).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
