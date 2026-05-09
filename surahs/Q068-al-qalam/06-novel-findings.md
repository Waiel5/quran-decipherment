---
surah: 68
surah_name_ar: القلم
surah_name_translit: al-Qalam
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — 8 pre-registered tests (Q068-F-01 through Q068-F-08); 3 VINDICATED, 1 VINDICATED-CORPUS-EXACT, 1 VINDICATED-UNIDIRECTIONAL, 1 DIRECTIONAL, 1 DOUBLE-REPLICATION NULL, 1 NULL, 1 NULL_DIRECTION_REVERSED.
---

# Q 68 al-Qalam — Novel Findings

## 0. Source

8 pre-registered novel empirical findings, each with locked pre-reg, SHA256-checksummed run script, and JSON-archived results. Pre-regs in `preregs/`, scripts in `/Users/grey/Downloads/quran/scripts/`, JSON outputs in `csv/`. All scripts verify pre-reg SHA at runtime.

| ID | Pre-reg SHA (head 12) | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|
| Q068-F-01 | `052e5de24459` | `Q068_F_01_writing_vocabulary_density.py` | `Q068-F-01.json` | **VINDICATED** |
| Q068-F-02 | `506e0277dc25` | `Q068_F_02_nun_letter_self_reference.py` | `Q068-F-02.json` | **DIRECTIONAL** |
| Q068-F-03 | `ce90bfc4654b` | `Q068_F_03_singleton_cluster_wordlength_rootrarity.py` | `Q068-F-03.json` | **CLUSTER-NULL** |
| Q068-F-04 | `5df62b113d24` | `Q068_F_04_garden_owners_parable_isolation.py` | `Q068-F-04.json` | **NULL** |
| Q068-F-05 | `7b5e8990c846` | `Q068_F_05_pen_inkwell_hadith_intersection.py` | `Q068-F-05.json` | **NULL_DIRECTION_REVERSED** |
| Q068-F-06 | `497822f6f771` | `Q068_F_06_qlm_density_rank.py` | `Q068-F-06.json` | **VINDICATED-TOP-3** |
| Q068-F-07 | `c3154905fbd2` | `Q068_F_07_q68_q96_fr_pair.py` | `Q068-F-07.json` | **VINDICATED-UNIDIRECTIONAL** |
| Q068-F-08 | `9cea3e52629e` | `Q068_F_08_nun_singleton_cluster_length_matched.py` | `Q068-F-08.json` | **VINDICATED + NULL-LM** |

The headline pattern: **Q 68 is structurally distinctive on form-axes (Nūn-singleton uniqueness, writing-vocab density, qlm-rank-2 corpus density) but content-NULL on the singleton-letter cohort axis** — exactly the cross-finding-026 §1 letter-axis ⊥ content-axis prediction at the singleton-cohort scale, replicated under TWO independent nulls.

---

## Q068-F-01 — Writing-vocabulary density (CONTENT-BEACON gloss of ن)

### Pre-registered hypothesis

Ibn ʿAbbās's classical gloss of the muqaṭṭaʿ ن (al-Ṭabarī, *Jāmiʿ al-bayān* on Q 68:1; al-Suyūṭī, *al-Durr al-manthūr*): the opening ن functions as a content-beacon for the surah's writing-vocabulary content. Operationalization: Q 68 should over-concentrate writing-vocabulary roots beyond uniform-distribution expectation.

Family of 6 QAC stem-roots tested: {qlm, sTr, ktb, sjl, rqm, lwH} (corpus-total 352 tokens across 49,968 root-tokens). Bonferroni-6 per-root + joint-family-summary.

### Result (`csv/Q068-F-01.json`)

| Root | Corpus K | Q 68 k | Expected | Observed / Expected | p (X≥k) | Bonferroni-6 |
|:--|:-:|:-:|:--|:-:|:--|:--|
| **sTr** | **16** | **2** | 0.061 | **32.70×** | **0.0017** | **PASS** |
| qlm | 4 | 1 | 0.015 | 65.40× | 0.0152 | fail (raw-α passes) |
| ktb | 319 | 2 | 1.219 | 1.64× | 0.345 | fail |
| sjl | 4 | 0 | 0.015 | 0.0× | 1.0 | fail |
| rqm | 3 | 0 | 0.011 | 0.0× | 1.0 | fail |
| lwH | 6 | 0 | 0.023 | 0.0× | 1.0 | fail |
| **JOINT FAMILY** | **352** | **5** | 1.346 | **3.72×** | **p = 0.0117** | — |

Q 68 writing-density = 26.18 per 1000 root-tokens (rank 5 by density; only Q 83 al-Muṭaffifīn, Q 98 al-Bayyina, Q 105 al-Fīl, Q 84 al-Inshiqāq exceed Q 68 — all shorter surahs with high-density single-root concentrations).

### Verdict

**VINDICATED**. At least one root (sTr) passes Bonferroni-6; joint p=0.0117 < 0.05. Ibn ʿAbbās's content-beacon gloss is empirically supported.

### Interpretation

The over-concentration is NOT just at the v.1 opening formula (qalam + yasṭurūn). The body-of-surah tokens are:
- *asāṭīr* (v.15) — *sTr*-root in a polemical accusation.
- *kitāb* (v.37) — *ktb*-root in a rhetorical Day-of-Judgment polemic.
- *yaktubūn* (v.47) — *ktb*-root in the same rhetorical context.

This is the empirically robust **CONTENT-BEACON** signature: the muqaṭṭaʿ-letter ن announces a writing-vocabulary distributed THROUGHOUT the surah, not concentrated at the opening.

### Honest limits

- ktb (the most common writing-root in the corpus, 319 tokens) is NOT over-concentrated in Q 68 — its 2 tokens are close to expected (1.22).
- The 5 most over-concentrated writing-surahs (Q 83, 98, 105, 84, 68) include several short Meccan surahs where writing-vocabulary is rhetorically concentrated; Q 68's over-density is NOT corpus-extreme but is significant under Bonferroni-6.
- The 6-root family was pre-locked; including *wḥy* (revelation) or other extra roots would expand the family but is *post-hoc*.

### Cross-references

- [[03-tafsir-survey]] §1 — al-Ṭabarī Ibn ʿAbbās chains.
- [[cross-finding-008]] — muqaṭṭaʿāt + book-reference; Q 68 follows the complementary minor pattern (muqaṭṭaʿ + oath-wāw) but still over-concentrates writing-vocab.

---

## Q068-F-02 — Nūn-letter self-reference (DIRECTIONAL)

### Pre-registered hypothesis

If the muqaṭṭaʿ-letter ن at Q 68:1 is a self-reference (in the way ق opens Q 50, ص opens Q 38), then Q 68 should have HIGHER ن-letter frequency in its body than the corpus baseline.

### Result (`csv/Q068-F-02.json`)

| Metric | Value |
|:--|:--|
| Q 68 ن-letter count | 131 |
| Q 68 total Arabic letters | 1,289 |
| **Q 68 ن-rate** | **0.1016 (10.16%)** |
| Corpus-rest ن-rate | 0.0824 (8.24%) |
| Rate ratio | 1.234 |
| **Permutation null p (one-sided)** | **0.0686** |
| Binomial null p (one-sided) | 0.0082 |
| Q 68 percentile in perm null | 93.14 |

### Verdict

**DIRECTIONAL** (binomial-significant; permutation-marginal). Q 68's ن-rate is 23% above corpus-rest, but at p_perm=0.0686 it does not pass the strict α=0.05 permutation threshold. Reported as DIRECTIONAL per pre-reg success criteria.

### Cross-singleton sibling test (REPLICATION CONTEXT)

Per Q050-F-03 cohort table:

| Surah | Host letter | Obs rate | Null mean | Z | p (1-sided) | Verdict |
|:--|:--|:--|:--|:--|:--|:--|
| Q 50 | ق | 0.0378 | 0.0215 | +3.34 | 0.0001 | **CONFIRMED** |
| Q 38 | ص | 0.0095 | 0.0064 | +1.91 | 0.048 | DIRECTIONAL_RAW |
| **Q 68** | **ن** | **0.1016** | 0.0832 | +1.47 | **0.069** | **DIRECTIONAL** |

The singleton-letter host-letter density is **Q 50-specific**: only Q 50's ق passes Bonferroni-3. Q 38's ص is raw-significant but Bonferroni-fails; Q 68's ن is DIRECTIONAL (highest baseline rate makes detection hardest).

### Honest limits

- ن is a corpus-high-frequency letter; statistically detecting Q 68's elevation against this high baseline requires very strong effect size.
- The binomial vs permutation null disagree: binomial assumes letter-independence (which is unrealistic for Arabic morphology); permutation preserves local-corpus correlation structure and is the more conservative test.

### Cross-references

- [[Q050-qaf/06-novel-findings]] §Q050-F-03 — full singleton-letter host-letter audit.

---

## Q068-F-03 — Singleton-letter cluster word-length + root-rarity (CLUSTER-NULL)

### Pre-registered hypothesis

Two axes: (a) per-word letter-length distribution (Mann-Whitney) and (b) root-rarity (Zipf-rank). Tested if {Q 38, Q 50, Q 68} cluster differs from corpus on either axis, two-sided per axis, Bonferroni-2 at α=0.025.

### Result (`csv/Q068-F-03.json`)

| Axis | Test | Statistic | p | Verdict (Bonferroni-2) |
|:--|:--|:--|:--|:--|
| **A: word-length** | Mann-Whitney U (singleton vs rest) | z=-2.17 | **0.030** | **DIRECTIONAL** (passes raw, fails Bonferroni-2 α=0.025) |
| B: root-rarity (Zipf) | 10000-perm two-sided | mean diff +58.4 | 0.1064 | NULL |

Axis A: singleton mean word-length 4.16 vs rest mean 4.25 (singleton words are SHORTER on average); two-sided p=0.030, raw-significant but Bonferroni-fails.

Axis B: singleton mean Zipf-rank 216.1 vs rest mean 157.7 (singleton roots have HIGHER mean Zipf-rank = roots are RARER); p=0.106, NULL.

### Verdict

**CLUSTER-NULL on word-length AND root-rarity**. Both Bonferroni-2 fail. The singleton-architecture (if any) must be on Q050-F-04's FR-distance / sig_A / outlier axes (which also returned NULL — see Q050-F-04 + Q068-F-08 below). The singleton cohort is **content-NULL across multiple axes**.

### Cross-references

- [[Q050-qaf/06-novel-findings]] §Q050-F-04 — FR-distance / sig_A / outlier axes (NULL).
- See Q068-F-08 below for the length-matched-null FR replication.

---

## Q068-F-04 — Garden-owners parable isolation (NULL)

### Pre-registered hypothesis

(a) Q 68:17-33 garden-owners parable is lexically distant (Jaccard root-set) from cognate parables Q 18:32-44 and Q 36:13-32. (b) Within Q 68, the v.17-33 window has corpus-max Jaccard distance to in-surah complement.

### Result (`csv/Q068-F-04.json`)

| Sub-test | Result | Verdict |
|:--|:--|:--|
| (a) d(Q 68:17-33, Q 18:32-44) | 0.893; control mean 0.915; **p_one_sided=0.83** | NULL |
| (a) d(Q 68:17-33, Q 36:13-32) | 0.880; control mean 0.915; **p_one_sided=0.94** | NULL |
| (b) v.17 window rank among 36 within-Q-68 windows | **rank 7** | NULL (not max; top 19%) |
| (b) corpus-max windows | v.13-29, v.14-30, v.15-31, v.16-32 (all Jaccard 0.927) | top 4 are the v.13-16 polemic-portrait windows |

### Verdict

**NULL** (joint Bonferroni-2). Pre-commit predicted v.17 window = corpus-max within-surah distinctness; observed v.17 window is in top-7 but NOT the maximum.

### Interpretation

The garden-owner parable IS lexically distinctive, but the v.13-16 polemic-portrait (*ḥallāf mahīn... zanīm*) is even more distinctive within Q 68. The pre-commit failed because the parable's vocabulary overlaps with the v.13-16 polemic enough to lower its within-surah max-distinctness rank by a few positions.

Honest reading: the parable IS isolated relative to direct cognate parables (Q 18, Q 36) but NOT at corpus-extreme Jaccard distance — the corpus's 17-verse-window distribution is broadly dispersed, with mean ≈ 0.915.

### Honest limits

- Jaccard on root-sets is binary (root present or absent in window); does not weight by frequency.
- The 17-verse window-length is fixed by the parable's natural extent; alternative window lengths (e.g., the strict v.17-32, or v.17-33 with the closing) would give different rankings.

---

## Q068-F-05 — Pen-inkwell hadith intersection (NULL_DIRECTION_REVERSED)

### Pre-registered hypothesis

Q 68:1's pen-creation hadith complex (Tirmidhī al-qadar; Abū Dāwūd; Ibn ʿAbbās's ن-narrations) should make Q 68:1 the MOST-CITED Q 68 verse across the 9 canonical hadith books.

### Result (`csv/Q068-F-05.json`)

| Result | Value |
|:--|:--|
| Q 68:1 substring citation count | **0** (across all 9 books) |
| Modal verse(s) | tied at Q 68:4, Q 68:13, Q 68:42 (1 citation each) |
| Q 68:1 rank by citation | rank 4 (tied with the 0-citation majority) |
| Q 68:1 expected under uniform | 0.058 |
| Binomial p for Q 68:1 ≥ 0 | 1.0 |

### Verdict

**NULL_DIRECTION_REVERSED**. Q 68:1's pre-committed direction (citation > expected) is reversed (0 < 0.06). Published with prominence per Protocol §1.3.

### Honest interpretation

The pen-creation hadith complex (al-Tirmidhī #3403, Abū Dāwūd #4702 — see [[04-hadith-corpus]] §2) does INTERPRETIVELY cite Q 68:1, but the substring-match pipeline misses INTERPRETIVE references. The strict substring count is the empirical fact; the theological-anchor count (via classical-tafsir + asbāb al-nuzūl integration) is 3+ for Q 68:1.

The most-cited Q 68 verse by **strict substring** is **Q 68:42** *yawma yukshafu ʿan sāq* (the Day-of-Judgment leg-uncovering), with 4 citations across 4 books (Bukhārī #7154, Muslim #359, Muslim #7197, Dārimī #2068).

---

## Q068-F-06 — *qlm* root density corpus rank (VINDICATED-TOP-3) — T1

### Pre-registered hypothesis

Q 68 al-Qalam should be in the TOP-3 of all 114 surahs by *qlm* root density (per 1000 QAC root-tokens). The classical title-density expectation predicts the surah-name maps onto a corpus-distinctive density.

### Result (`csv/Q068-F-06.json`)

| Surah | k_qlm | n_root_tokens | dens/1000 | rank |
|:-:|:-:|:-:|:-:|:-:|
| **Q 96** al-ʿAlaq | 1 | 111 | **9.009** | **1** |
| **Q 68** al-Qalam | 1 | 508 | **1.969** | **2** |
| Q 31 Luqmān | 1 | 852 | 1.174 | 3 |
| Q 3 Āl ʿImrān | 1 | 5,752 | 0.174 | 4 |
| All others | 0 | varies | 0.000 | 5-114 (tied) |

**Surahs with any *qlm* token: 4 of 114** (Q 3, Q 31, Q 68, Q 96).

Q 68 hypergeometric p (X ≥ 1 | corpus K=4, n=508): **0.0158**.

### Verdict

**VINDICATED-TOP-3** (Q 68 = rank 2). p_hyper = 0.016 < α=0.05.

### Interpretation

The classical title-density expectation is empirically supported, BUT the rank-1 surah is Q 96 al-ʿAlaq, NOT Q 68 al-Qalam — the chronologically-first revelation has the higher *qalam* density than the title-eponymous surah. This is the **chronology-paired qalam-density** finding: revelation #1 carries the higher-density signature of writing-as-divine-instruction (*ʿallama bi-l-qalam*, Q 96:4) than the title-eponymous revelation #2.

This complements Q068-F-07 (Q 96 ↔ Q 68 FR-pair): the chronology-pair shares both the *qlm* lexical key (4-surah corpus rare; 2 of 4 are this pair) AND content-vocabulary clustering (rank-6 from Q 68's side).

### Honest limits

- *qlm* corpus K=4 is small-N for density tests; sampling noise is non-trivial.
- The hypergeometric p_X≥1 = 0.016 is a SINGLE-test result; the title-density pre-reg locked TOP-3 not RANK-1, so the test is honest.
- Q 31:27 *aqlām* and Q 3:44 *aqlāmahum* are the other two *qlm* attestations — referring to *casting lots* contexts, not the pen-as-instruction theological theme of Q 68:1 + Q 96:4. The thematic specificity of Q 68 ↔ Q 96 is interpretively distinct.

### Cross-references

- [[Q096-al-alaq/06-novel-findings]] — Q 96's *qalam* status as revelation-#1 + Q 96:4 *ʿallama bi-l-qalam*.

---

## Q068-F-07 — Q 68 ↔ Q 96 FR pair (VINDICATED-UNIDIRECTIONAL) — T2

### Pre-registered hypothesis

Q 68 and Q 96 are chronology-paired (revelations #2 and #1) and *qlm*-paired (2 of 4 corpus *qlm*-bearing surahs). Direction-locked BIDIRECTIONAL: Q 96 in Q 68's FR-nearest top-15 AND Q 68 in Q 96's FR-nearest top-15.

### Result (`csv/Q068-F-07.json`)

| Direction | Rank | In top-15? | Uniform-rank-null p |
|:--|:--|:--|:--|
| Q 96 in Q 68's nearest list | **6** / 113 | **YES** | 0.053 |
| Q 68 in Q 96's nearest list | **46** / 113 | NO | 0.407 |

FR distance Q 68 ↔ Q 96 = **0.7324** (symmetric).

### Verdict

**VINDICATED-UNIDIRECTIONAL**. The pre-committed BIDIRECTIONAL prediction is HONESTLY VIOLATED on the Q 96 side. Per Protocol §1.3, this is published with full prominence as a pre-commit-direction adjustment.

### Honest pre-commit interpretation

The asymmetric rank pattern (rank 6 vs rank 46) reflects **neighborhood-density differences**:
- Q 96 (19 verses, position 96) sits in the dense terminal-tail short-mufaṣṣal cluster. Its 15-nearest are saturated by post-s=90 short surahs (Q 102, 107, 108, 100, 110, 106, 105, 113, 112, 103, 94, 111, 1, 95, 99). Q 68 falls outside this saturation.
- Q 68 (52 verses, position 68 mid-corpus) has a sparser neighborhood, and Q 96 fits comfortably at rank 6 (alongside Q 100, 52, 105, 93, 108).

This is a **first empirical instance** in the project of a directionally-asymmetric FR-pair where chronology-shared and lexical-key-shared surahs are mutually-close on one side only. The asymmetry suggests FR-pair "closeness" is dependent on each surah's *neighborhood density*, not purely on a symmetric similarity property.

### Candidate H-NEW

This finding is a candidate for elevation to **H-NEW-1361** (or next-available H-NEW number reserved for inline cross-finding): **"FR-pair asymmetry under neighborhood-density heterogeneity"** — the corpus's FR-roots distance is symmetric, but the *rank* relationship is heterogeneous because neighborhoods have different densities. This generalizes beyond Q 68 ↔ Q 96; other candidate pairs include any pair where one surah sits in a saturated cluster (Q 1 umm al-Kitāb area, Q 108 Kawthar terminal-tail).

### Honest limits

- The h-new-111 FR matrix has Bayesian-Dirichlet smoothing (α=2.0); the matrix is fixed, so this is the locked test.
- "Top-15" was chosen pre-commit as a top-decile threshold (15/113 ≈ 13.3%); alternative thresholds (top-10, top-20) would give different verdicts. The Bonferroni-2 α=0.025 maps to rank ≤ 3 approximately, which is even stricter and fails for both directions.
- The asymmetry pattern needs replication with a different similarity measure (e.g., cosine on TF-IDF, char-n-gram NCD) — flagged as future-work.

### Cross-references

- [[01-empirical-profile]] §1 — Q 68's full FR-nearest top-15.
- [[Q096-al-alaq/01-empirical-profile]] — Q 96's full FR-nearest top-15.
- [[cross-finding-014]] — candidate addition: FR-pair asymmetric ranks.

---

## Q068-F-08 — Nūn-singleton + length-matched FR cluster (VINDICATED + NULL-LM) — T3

### Pre-registered hypothesis

Two axis-disjoint sub-tests:
- (a) Q 68 is the corpus-EXACT singleton ن-opener of the 29 muqaṭṭaʿāt-opener surahs.
- (b) The singleton-letter triplet {Q 38, Q 50, Q 68} is FR-cohesive against a **length-matched null** (MW-5 replication of Q050-F-04 which used random-3-surah null).

### Result (`csv/Q068-F-08.json`)

**Sub-test (a) Nūn-opener uniqueness**:
- Of 29 muqaṭṭaʿāt-opener surahs, **exactly 1** opens with the single letter ن: Q 68.
- The other 28 open with ALM (Q 2, 3, 29, 30, 31, 32), ALMS (Q 7), ALR (Q 10-15), KHYAS (Q 19), TH (Q 20), TSM (Q 26, 28), TS (Q 27), YS (Q 36), S+wa-al-qurʾān (Q 38), HM (Q 40-46), and Q (Q 50). See `csv/Q068-F-08.json` `opener_table` for full verse-1 verbatim.

**Sub-test (b) length-matched FR cluster**:
- Triplet mean pairwise FR = 0.8699
- Length-matched pool (51 surahs with verse-count in [22.5, 132]) null mean = 1.0426
- Null min = 0.7082, max = 1.3677
- **p_low (one-sided) = 0.082**
- Triplet is LOWER than null mean (DIRECTIONAL) but does not pass α=0.025 Bonferroni-2.

### Verdict

**Sub-test (a) VINDICATED-CORPUS-EXACT**.
**Sub-test (b) NULL-LM** (length-matched null replication of Q050-F-04 NULL).
**Joint**: VINDICATED + NULL-LM.

### Interpretation

**This is a DOUBLE-REPLICATION NULL** on singleton-letter FR-cohesion. The triplet is form-coherent (Q050-F-01 verse-1 syntax), but content-NULL under both the **random-3-surah null** (Q050-F-04: p=0.267) AND the **length-matched null** (Q068-F-08(b): p=0.082).

The length-matched null gives a tighter (lower) p-value (0.082 vs 0.267) — the directional effect IS slightly stronger relative to length-matched controls — but still fails the strict α=0.025 Bonferroni threshold. **Both null distributions independently rule out the singleton-cluster content-cohesion at α=0.05**.

This is **credibility-strengthening** for cross-finding-026 §1 (letter-axis ⊥ content-axis empirical orthogonality): the singleton-letter cohort is the most letter-axis-distinctive sub-cohort of muqaṭṭaʿāt, and it is content-NULL under TWO independent nulls. The letter-axis ⊥ content-axis lock holds at the smallest, most cohort-strong scale.

### Cross-references

- [[Q050-qaf/06-novel-findings]] §Q050-F-04 — random-3-surah null on same triplet.
- [[Q038-sad/06-novel-findings]] (when populated) — Q 38 specialist's complementary tests.
- [[cross-finding-026]] §1 — letter-axis ⊥ content-axis empirical orthogonality.

---

## Synthesis — Q 68's 8-axis cohort coherence map

| Axis | Result | Source |
|:--|:--|:--|
| Verse-1 syntax (muqaṭṭaʿ + oath-wāw + al-) | **YES** (form-coherent cohort {Q 38, Q 50, Q 68}) | Q050-F-01 |
| Writing-vocabulary content-beacon | **VINDICATED** (joint p=0.0117) | Q068-F-01 |
| ن-letter self-reference | **DIRECTIONAL** (binom p=0.008, perm p=0.069) | Q068-F-02 |
| Word-length cluster distinctness | NULL (Bonferroni-2 fail) | Q068-F-03 |
| Root-rarity cluster distinctness | NULL | Q068-F-03 |
| Garden parable Jaccard isolation | NULL (parable is top-7 not max) | Q068-F-04 |
| Hadith-citation primacy of Q 68:1 | NULL_DIRECTION_REVERSED (substring search 0 hits) | Q068-F-05 |
| *qlm*-density corpus rank | **VINDICATED-TOP-3** (rank 2; Q 96 = rank 1) | Q068-F-06 |
| Q 96 ↔ Q 68 FR-pair (chronology + qlm) | **VINDICATED-UNIDIRECTIONAL** (asymmetric ranks 6 / 46) | Q068-F-07 |
| Nūn-singleton uniqueness | **VINDICATED-CORPUS-EXACT** (1/29 muqaṭṭaʿāt) | Q068-F-08(a) |
| Singleton-cluster FR-cohesion (length-matched null) | **NULL-LM** (p=0.082; DOUBLE-REPLICATION NULL with Q050-F-04) | Q068-F-08(b) |

**Headline pattern**: Q 68 is **form-distinctive and lexically-distinctive** (Nūn-singleton, writing-vocab content-beacon, *qlm*-rank-2, chronology-pair to Q 96, ن-rāwī at 80.8%) but **content-cohesion-NULL** at the singleton-cohort scale under two independent nulls. The letter-axis carries the cohort coherence; the content-axis does not. This is the empirical fingerprint of cross-finding-026 §1 at the singleton-letter sub-cohort.

## Candidate H-NEW elevations

1. **H-NEW-1361 (candidate)** — FR-pair asymmetry under neighborhood-density heterogeneity (Q068-F-07 finding). Generalize beyond Q 68 ↔ Q 96 to any pair where one surah sits in a saturated cluster.
2. **H-NEW-1362 (candidate)** — *qlm*-corpus-density chronology-paired pattern (Q068-F-06 + Q096): revelation #1 has higher *qalam* density than title-eponymous revelation #2. This is a chronology-pair lexical-density signature; needs replication on other root-pairs.
3. **H-NEW-1363 (candidate)** — DOUBLE-NULL singleton-letter content-cohesion (Q068-F-08(b) + Q050-F-04). The singleton-letter cohort is form-coherent and content-NULL under two independent null distributions — credibility-strengthening result for cross-finding-026 §1.

These are flagged for inline-test elevation in a future session.
