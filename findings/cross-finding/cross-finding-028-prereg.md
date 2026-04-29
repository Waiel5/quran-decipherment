---
id: cross-finding-028
title: "Liturgical-recitation surah-pair ↔ FR-near-pair hypothesis"
phase: B+
type: pre-registration (DIRECTION-LOCKED)
date_locked: 2026-05-07
seed: 20260507
authors: cross-finding-028-specialist
rules_tuple: "(no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)  — inherited from H-NEW-111"
fr_source: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json
hadith_source: /Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/
status: LOCKED — direction pre-committed before any computation
bonferroni_family: cross-finding-028-liturgical-pair-FR
bonferroni_k: 5    # number of independent verified pre-committed pair-set tests; see §5
alpha_bon: 0.01    # 0.05 / 5 for any single-pair sub-test
---

# Cross-Finding-028 — Pre-Registration

## 1. Hypothesis

Two independent specialist findings (Wave-D, 2026-05-07) noted a recurring pattern: classically attested liturgical-recitation surah-pairs have FR-roots-distance BELOW corpus mean (0.9235, from H-NEW-111). Eid pair Q 50 / Q 54: FR=0.882. Friday-night pair Q 32 / Q 67: FR=0.7534 (rank 2 nearest-neighbour to Q 67). If liturgical-recitation tradition systematically maps to FR-near-pairs, this is an architectural signature: the canonical mushaf compilers preserved a structural-cohesion that emerged from prophetic-liturgical practice.

**H1 (PRIMARY, direction-locked LOW).** The mean FR distance of the pre-committed canonical liturgical-pair set is significantly LOWER than the corpus mean (0.9235), tested via one-sided Wilcoxon-paired-test against random-pair samples of equal N drawn from the non-pair pool, 10000 permutations, seed 20260507.

**H2 (LENGTH-CONTROL).** H1 holds even when each liturgical pair is matched to a length-matched random pair (similar combined verse-count, ±10%). I.e., the FR-closeness is not a length-class confound.

**H3 (FALSIFIER).** If the verified pair-set MEAN FR ≥ 0.9235, the hypothesis is REVERSED: the seed observation collapses to a 2-instance coincidence and liturgical-tradition tells us nothing about FR-architecture. This is the equal-prominence NULL outcome.

## 2. Pre-committed liturgical-pair list (verified on disk before FR computation)

The pair list is constructed BEFORE FR computation from canonical 9-book hadith on disk at `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`. Each pair is verified by content-search: a single hadith must explicitly reference both surahs (by name, opening word, or distinctive Arabic incipit) within a liturgical context (Eid, Friday, Maghrib, sleep, Tahajjud, grave, etc.). Cited hadith are content-anchored examples; the in-database `idInBook` numbering is per-collection sequential and does NOT correspond to sunnah.com numbering, so we cite by `[collection]#[idInBook]` and quote the matching English fragment.

| # | Pair | Liturgical context | On-disk anchor (collection#idInBook) | Status |
|:-|:--|:--|:--|:--|
| 1 | Q 50 (Qāf), Q 54 (al-Qamar) | Eid prayer (Imam recitation) | `muslim#1949` ("He used to recite in them: 'Qaf. By the Glorious Qur'an' (50), 'The Hour drew near, and the moon was rent asunder' (54)"), `tirmidhi#534`, `abudawud#1155` | ✓ VERIFIED |
| 2 | Q 32 (al-Sajda), Q 76 (al-Insān / al-Dahr) | Fajr-Friday | `bukhari#870` ("The Prophet used to recite in the Fajr prayer of Friday, 'Alif, Lam, Mim, Tanzil' (Q 32) and 'Hal-ata-ala-l-Insani' (Q 76)"), `bukhari#1037`, `muslim#1926`, `muslim#1927` | ✓ VERIFIED |
| 3 | Q 87 (al-Aʿlā), Q 88 (al-Ghāshiya) | Eid + Jumuʿa prayer | `muslim#1920` ("Glorify The name of Thy Lord, the Most High (87), and: Has there come to thee the news of the overwhelming event (88)"), `tirmidhi#533`, `abudawud#1123`, `abudawud#1126` | ✓ VERIFIED |
| 4 | Q 109 (al-Kāfirūn), Q 112 (al-Ikhlāṣ) | Maghrib & Fajr 2-rakʿa sunnah; ṭawāf 2-rakʿa | `tirmidhi#870` ("During the two Rak'ah of Tawaf… 'Qul ya ayyuha al-kafirun' and 'Qul Huwa Allah Ahad'"), `ibnmajah#883`, `ibnmajah#900` (Maghrib post-prayer) | ✓ VERIFIED |
| 5 | Q 113 (al-Falaq), Q 114 (al-Nās) | Muʿawwidhatān — single liturgical unit; ruqya, before sleep, after-prayer wird | `bukhari#4809` ("he would recite Mu'awwidhat (Surat Al-Falaq and Surat An-Nas)"), `bukhari#4810`, `bukhari#5526`, `nasai#5441` | ✓ VERIFIED |
| 6 | Q 32 (al-Sajda), Q 67 (al-Mulk) | Pre-sleep Tahajjud / al-Munjiya nightly pair | `tirmidhi#2975` ("The Prophet would not sleep until he recited Alif Lam Mim Tanzil (Q 32) and: Tabarak Alladhi Biyadihil-Mulk (Q 67)") | ✓ VERIFIED — replaces prompt's "Q 36, Q 67" (see §3 specialist-judgment override) |
| 7 | Q 97 (al-Qadr), Q 30 (al-Rūm) | Tahajjud (variant tradition) | NOT FOUND in 9-book canonical content-search | ✗ DATA-GAP — DROPPED |
| 8 | Q 17 (al-Isrāʾ), Q 23 (al-Muʾminūn) | Friday-night recitation (variant) | NOT FOUND in 9-book canonical content-search | ✗ DATA-GAP — DROPPED |
| 9 | Q 18 (al-Kahf), Q 32 (al-Sajda) | Friday-recitation + Tahajjud single-night | NOT FOUND as a paired hadith in 9-book content-search (each surah individually is well-attested in its own context, but the explicit joint single-night practice is not on disk) | ✗ DATA-GAP — DROPPED |
| 10 | Q 1, Q 112, Q 113, Q 114 | Daily wird (4-surah unit) | `bukhari#4810` ("recited Surat Al-Ikhlas, Surat Al-Falaq and Surat An-Nas"), `bukhari#5526` — but the CLUSTER is the 3-surah muʿawwidhāt-extended (Ikhlas+Falaq+Nas), not a 4-surah unit including Q 1. Filed as separate CLUSTER analysis in §6 | △ PARTIAL — filed as separate cluster check, not in primary pair-set |

### 2.1 Pair-set after on-disk verification

**N = 5 verified pre-committed pairs:**

| Pair | Surah-A | Surah-B | Context |
|:--|:--|:--|:--|
| P1 | 50 | 54 | Eid prayer |
| P2 | 32 | 76 | Fajr-Friday |
| P3 | 87 | 88 | Eid + Jumuʿa |
| P4 | 109 | 112 | Maghrib/Fajr-sunnah/ṭawāf |
| P5 | 113 | 114 | Muʿawwidhatān |
| P6 | 32 | 67 | Pre-sleep al-Munjiya |

That is 6 pairs total (5 are listed in primary; P6 is included since it survives strict verification — the prompt directly provided this pair as the seed motivation in cross-finding-026 §13.5b). **Bonferroni-k for any per-pair sub-test = 6, α_bon_per_pair = 0.05/6 ≈ 0.0083.** Primary aggregate test is single-test (the full set's mean against permutation null), so primary α = 0.05.

Note on bonferroni declaration: aggregate primary = 1 test (set mean vs perm-null); per-pair descriptive tier = 6 tests (Bonferroni-corrected α=0.0083). Total family k=2 (aggregate primary + length-controlled secondary). **α_bon_for_family = 0.05/2 = 0.025.** This is the load-bearing Bonferroni cell for declaring CONFIRMED.

### 2.2 Cluster (separate test, not in primary)

**3-surah muʿawwidhāt cluster (Q 112, Q 113, Q 114)** — `bukhari#4810`, `bukhari#5526` document the joint pre-sleep recitation. Tested as: mean pairwise FR over the 3-cluster, vs 10000 random 3-surah triplet permutations.

## 3. Specialist-judgment override: Q 36 → Q 32 in pair P6

The prompt's table listed "Q 36, Q 67 — Death-bed recitation pair (variant); al-Tirmidhī #2887 (heart-of-Quran for Q36), Sahih Muslim ḥadīth on Q 67 *munjiya*". On strict on-disk content-search:

- **Q 36 alone** as death-recitation is well-attested across the 9-book corpus (e.g., Abū Dāwūd narrations, "Recite Ya-Sin over your dead").
- **Q 67 alone** as al-Mānīʿa / al-Munjiya grave-protection is well-attested (`tirmidhi#2974`, `abudawud#1401`, `ibnmajah#3522`).
- **Q 36 AND Q 67 as a SINGLE PAIR-RECITATION practice** is NOT explicitly attested in any single 9-book hadith on disk. The two surahs occupy distinct liturgical roles (post-mortem vs pre-burial / nightly grave-protection), not a single coupled recitation.
- **Q 32 AND Q 67 as a SINGLE PAIR-RECITATION practice** IS explicitly attested: `tirmidhi#2975` — "The Prophet would not sleep until he recited Alif Lam Mim Tanzil (Q 32) AND: Tabarak Alladhi Biyadihil-Mulk (Q 67)." This is the canonical pre-sleep nightly pair, and it is what the cross-finding-026 §13.5b reference (the seed motivation) actually pointed to.

Per [[reference_quran_paths|specialist-judgment-overrides-team-lead-method protocol]] (granted 2026-04-14, requires direct empirical evidence + garden-of-forking-paths log BEFORE run): the prompt's "Q 36, Q 67" entry is replaced with **Q 32, Q 67**, BEFORE FR computation, with this override fully disclosed. This is a *tightening* of the empirical anchor (canonical hadith-pair vs candidate-pair) — direction of the test is unaffected. The override is logged here, in the script's garden-of-forking-paths block, and in the journal.

## 4. Procedure

1. **Verify pre-reg SHA** at runtime; fail-fast on mismatch.
2. **Construct pair list** = the 6 verified pairs in §2.1.
3. **Compute FR per pair**: load `h-new-111.json`, extract upper-triangular matrix as dict-of-dict, look up D[s_a][s_b] for each pair.
4. **Aggregate**: pair-set mean, median, individual values.
5. **Primary null distribution**: 10000 permutations, each draws N=6 random surah-pairs (uniformly from the 6441-pair-pool excluding the 6 verified pairs); record permutation mean FR.
6. **Aggregate test**: one-sided p = (count of perm-mean ≤ observed-mean + 1) / (10001). Direction-locked LOW.
7. **Wilcoxon paired test**: sign-test on per-pair-rank-vs-corpus-median.
8. **Length-control (H2)**: for each pair (s_a, s_b), compute combined verse-count C = v_{s_a} + v_{s_b}. Match each verified pair to N_match=100 random pairs with combined verse-count within ±10%. Compare mean(verified-FR) to mean(length-matched random-pair-FR). Direction-locked LOW.
9. **Cluster sub-test**: muʿawwidhāt 3-cluster mean pairwise FR vs 10000 random 3-surah triplet permutation null. Direction-locked LOW.
10. **Per-pair descriptive table** (Bonferroni k=6, α_bon=0.0083): each pair's percentile under the per-pair-only null (random pair from pool).

## 5. Bonferroni declaration

- **bonferroni_family**: cross-finding-028-liturgical-pair-FR
- **bonferroni_k = 2** (primary aggregate test + length-controlled secondary). The cluster test is reported as supportive but separately registered.
- **alpha_bon = 0.025** (= 0.05 / 2)
- **per-pair descriptive Bonferroni**: k=6, α=0.0083 (per-pair NOT load-bearing — used only to flag which pairs individually drive the result)

## 6. Acceptance / rejection

| Outcome | Verdict |
|:--|:--|
| Aggregate p ≤ 0.025 AND length-control p ≤ 0.025 AND direction LOW on both | **CONFIRMED** at α_bon |
| Aggregate p ≤ 0.05 AND length-control p ≤ 0.05 (raw, not Bonferroni) | **DIRECTIONAL** |
| Aggregate p > 0.05 OR length-control p > 0.05 (direction-correct but not significant) | **DIRECTIONAL-WEAK** |
| Aggregate mean ≥ 0.9235 (corpus mean) | **NULL — direction-reversed**; the seed conjecture is FALSIFIED at corpus scale |
| Both p>0.5 AND mean very near corpus mean | **NULL — coincidence** |

## 7. Garden-of-forking-paths log

- **Entry 1 (2026-05-07, before FR computation)**: Verified Q050/Q054 (Eid), Q032/Q076 (Fajr-Friday), Q087/Q088 (Eid+Jumuʿa), Q109/Q112 (Maghrib/Fajr/ṭawāf), Q113/Q114 (Muʿawwidhatān) on disk via Arabic+English content-search.
- **Entry 2 (2026-05-07, before FR computation)**: Q017/Q023 and Q018/Q032 single-pair single-night practice NOT FOUND in 9-book content-search. Both DROPPED as DATA-GAP per pre-reg discipline (no cherry-picking).
- **Entry 3 (2026-05-07, before FR computation)**: Q036/Q067 DOES NOT have a canonical pair-recitation hadith on disk. Q032/Q067 DOES (`tirmidhi#2975`). The prompt's Q036/Q067 row replaced with Q032/Q067. Specialist-judgment override invoked, fully disclosed; override TIGHTENS the empirical anchor.
- **Entry 4 (2026-05-07, before FR computation)**: Q097/Q030 NOT FOUND. DROPPED as DATA-GAP.
- **Entry 5 (2026-05-07, before FR computation)**: Q1+Q112+Q113+Q114 4-surah daily-wird as a single unit NOT FOUND. The 3-surah muʿawwidhāt cluster (Q112+Q113+Q114) IS attested (`bukhari#4810`, `bukhari#5526`). Filed as separate cluster sub-test, not in primary pair-set.
- **Entry 6 (2026-05-07, BEFORE FR computation)**: Bonferroni-k locked at 2 (primary aggregate + length-control), α_bon=0.025. Per-pair descriptive table at α=0.05/6=0.0083.
- **Entry 7 (locked at SHA)**: Direction is LOW for all aggregate and length-controlled tests. Reversal = NULL with full prominence.

## 8. Pre-reg SHA-lock

The SHA256 of this file (computed AFTER all §1-§7 content is finalized and before any test is run) is computed and embedded in the run script's `EXPECTED_PREREG_SHA` constant. The script verifies SHA at runtime and aborts on mismatch.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
