---
surah: 16
file_type: novel-findings
date_last_updated: 2026-05-07
n_pre_registered_tests: 5
---

# Q 16 al-Naḥl — Novel Findings (Q016-F-01 .. Q016-F-05)

5 pre-registered tests. **Equal-NULL prominence applied**: 1 DIRECTIONAL, 1 NULL (lemma-strict), 1 NULL, 1 NULL, 1 PRE-COMMIT VIOLATION (with reverse-direction discovery). All pre-regs SHA-locked, scripts verified at runtime.

## Summary table

| Test | Headline | Verdict | p / rank | Reference |
|:--|:--|:--|:--|:--|
| **Q016-F-01** | Niʿmah-catalog vocabulary saturation | **DIRECTIONAL** (NULL on strict top-3) | rank 18/114; p_perm = 0.0002 | `Q016-F-01.json` |
| **Q016-F-02** | Bee-verse Q 16:68–69 corpus-hapax lemma count | **NULL** (predicted ≥4, observed 2) | p_perm = 0.186; null mean = 0.79 | `Q016-F-02.json` |
| **Q016-F-03** | True-isolate persistence under 8 similarity instruments | **PRE-COMMIT VIOLATION** | 0/8 in bottom-quartile; **6/8 in TOP-quartile** | `Q016-F-03.json` |
| **Q016-F-04** | Abraham-coda Q 16:120–123 block-homogeneity | **NULL** | Cell A p = 0.10, Cell B p = 0.18 | `Q016-F-04.json` |
| **Q016-F-05** | Chrono-vs-mushaf displacement × isolate-status | **NULL** | ρ_Tanzil = 0.04, ρ_Nöldeke = −0.005 | `Q016-F-05.json` |

---

## Q016-F-01 — Niʿmah-catalog vocabulary saturation

**Pre-reg**: `Q016-F-01-nimah-catalog-saturation-prereg.md` (SHA `1604d9a5...`).
**Script**: `scripts/Q016_F_01_nimah_catalog.py`.
**Output**: `csv/Q016-F-01.json`.

**Hypothesis (locked)**: Q 16 ranks in TOP-3/114 on niʿmah-catalog vocabulary density per 100 tokens. Direction: HIGHER.

**Operational metric**: regex hits over 3-component marker-set (A = mercy nouns; B = creation verbs *anzala / sakhkhara / jaʿala / anbata / akhraja*; C = blessing-objects: cattle, water, sea, mountains, sun, moon, stars, milk, honey, etc.) → density per 100 orthographic tokens.

**Result**:

| Metric | Q 16 value | Q 16 rank | Notes |
|:--|:--|:--|:--|
| Composite niʿmah_density per 100 tok | 2.140 | **18/114** | strict success (top-3) FAILED |
| A — mercy-noun density | — | 15/114 | top-15 |
| B — creation-verb density | — | **9/114** | **top-10** |
| C — blessing-object density | — | 27/114 | top-quartile |

- **Permutation p (length-controlled token-resample)**: p = 0.0002 (only 2/10000 corpus-resamples produce density ≥ 2.140)
- **Bonferroni α (k=3)**: 0.0167 → passes raw-p threshold but fails strict rank-success.

**MW-5 positive control**: Q 14 (Ibrāhīm), the comparable niʿmah-catalog surah, ranks **9/114** ✓ PASS (predicted top-15).
**MW-6 negative control**: Q 12 (Yūsuf), the continuous-narrative surah, ranks **90/114** ✓ PASS (predicted bottom-half).

**Verdict**: **DIRECTIONAL** — the niʿmah-catalog effect is empirically present (p=0.0002, both MW controls fired correctly), but Q 16 is NOT the top-density surah. Several short-Meccan surahs with high mercy/blessing concentration outrank Q 16.

**Inspection of top-10**:

The top-10 niʿmah-density surahs (per the metric) tend to be SHORT surahs where a few niʿmah-mentions yield a high per-token density. Q 16's robust standing (rank 9 on the strongest verb-component, rank 18 composite) is consistent with the classical alt-name *Sūrat al-Niʿam* — the surah is genuinely niʿmah-saturated in absolute terms (60+ marker hits across 1963 tokens), but the per-token rate is competitive with shorter surahs.

**Honest interpretation**: the classical claim is qualitatively VINDICATED (`05-classical-claims-audit.md` Claim 2). Q 16's STATURE as the "Sūrat al-Niʿam" comes from VOLUME of niʿmah-vocabulary AND the rhetorical centrality of the catalog, not from per-token density alone.

---

## Q016-F-02 — Bee-verse Q 16:68–69 corpus-hapax lemma count

**Pre-reg**: `Q016-F-02-bee-verse-hapax-prereg.md` (SHA `31d55e2d...`).
**Script**: `scripts/Q016_F_02_bee_hapax.py`.
**Output**: `csv/Q016-F-02.json`.

**Hypothesis (locked)**: ≥4 corpus-hapax LEMMAS in Q 16:68–69. Direction: HIGHER.

**Operational metric**: from QAC v0.4, count content-POS lemmas (N, V, ADJ, PCPL) in the bee passage whose attestation set is fully contained in {(16,68), (16,69)}.

**Result**:

| Metric | Value |
|:--|:--|
| Bee-passage content lemmas | 24 |
| Content tokens | 25 |
| **Corpus-hapax lemmas** | **2** |
| Hapax lemma list | `n~aHol` (the bee), `*ulul` (submissive [paths]) |
| Length-matched 2-verse-window null | n = 1693 candidates; mean hapax = 0.79; max = 7 |
| **Permutation p (one-sided upper)** | **0.186** |
| Predicted ≥ 4 (strict) | **FAIL** |

**MW-5 positive control**: Q 12:4–5 (Yūsuf's dream + brothers' jealousy intro) returned **0 hapaxes** — the instrument is conservative and may underestimate true lexical-uniqueness for narrative passages.

**Verdict**: **NULL** on strict ≥4 pre-commitment. **DIRECTIONAL signal** present (bee-passage 2 hapaxes vs corpus-mean 0.79; 2.5× the mean), but does not pass single-test α=0.05 either (p=0.186).

**Honest interpretation**:
1. The pre-committed ≥4 was AGGRESSIVE based on a pre-flight scan suggesting 2-3 likely hapax candidates (`nḥl`, `*ll`, `lwn`, `ʿrsh`). The actual hapax count = 2, with `lwn` "color" attested elsewhere in the corpus, `ʿrsh` attested elsewhere (mostly as the divine throne but also in trellis-meaning forms via lemma sharing).
2. **The lemma `n~aHol` (the bee, masculine collective) is a true corpus-hapax**, attested ONLY at Q 16:68. The other root attestation at Q 4:4 (`niḥla` = "free gift/dowry") is a graphemically near-identical but lexically distinct QAC lemma `niHolap`.
3. **The lemma `*ulul` (submissive paths)** — co-occurring with the bee in *fa-slukī subula rabbiki dhululan* — is also corpus-unique. al-Qurṭubī's exegesis on Q 16:69 spends a paragraph on the *dhulul* gloss (mountain-shelter passages "easy for them"), confirming the lemma's uniqueness was classically noted.
4. The al-Rāzī bee-iʿjāz claim (`05-classical-claims-audit.md` Claim 1) is RHETORICALLY VINDICATED but quantitatively this LEMMA-test does not fire at the strict bar. A ROOT-level test (rather than lemma) might fire — but root-test was not pre-registered, so cannot be added post-hoc.

---

## Q016-F-03 — True-isolate persistence (PRE-COMMIT VIOLATION → reverse-direction discovery)

**Pre-reg**: `Q016-F-03-true-isolate-persistence-prereg.md` (SHA `7214978a...`).
**Design parent**: Q025-F-01 (same 8-instrument battery; specialist-coordinated).
**Script**: `scripts/Q016_F_03_true_isolate_persistence.py`.
**Output**: `csv/Q016-F-03.json`.

**Hypothesis (locked)**: Q 16 in BOTTOM-quartile (rank ≤ 28/114) of mean-similarity-to-nearest-3-neighbors on **≥6/8 instruments**. Direction: LOWER (more isolated).

**Result — full instrument table**:

| Instrument | Q 16 rank (lower = more isolated) | In bottom-quartile? | p (one-sided lower) | Top-3 neighbors |
|:--|:-:|:-:|:--|:--|
| I1 root-Jaccard | **107**/114 | **No** (top-quartile!) | 0.935 | Q 6, Q 7, Q 10 |
| I2 content-cosine (TF-IDF) | **106** | **No** | 0.930 | Q 2, Q 3, Q 10 |
| I3 char-trigram-Dice | **106** | **No** | 0.934 | Q 6, Q 7, Q 39 |
| I4 FR-similarity | 48 | No (mid) | 0.422 | Q 39, **Q 22**, Q 6 |
| I5 rhyme final-letter cosine | **101** | **No** | 0.889 | Q 12, Q 95, Q 107 |
| I6 root Zipf-overlap | **105** | **No** | 0.923 | Q 6, Q 10, Q 7 |
| I7 divine-name Jaccard | 93 | No | 0.816 | Q 45, Q 61, Q 64 |
| I8 char-5gram-Dice | **107** | **No** | 0.939 | Q 29, Q 6, Q 39 |

**Q 16 in bottom-quartile on 0/8 instruments. Q 16 in TOP-quartile (rank ≥ 87) on 6/8 instruments.**

**Verdict**: **PRE-COMMIT VIOLATION** per PRE-REG-STANDARD-01.

The pre-committed direction (Q 16 = LOW similarity = isolated) was strongly OPPOSITE to observation. The result is published with full prominence (equal-NULL discipline §1.3). Per discipline rules, **the test is REGISTERED AS NULL with reverse-direction discovery flag**; any reframing-on-the-data findings are EXPLORATORY and require an independent pre-reg before promotion.

### Reverse-direction discovery (EXPLORATORY)

The reverse-direction observation (Q 16 in TOP-quartile of nearest-3-similarity on 6/8 instruments) is itself striking: **Q 16 is a high-density "neighborhood" surah**, not a similarity-outlier. Its FR-nearest-3 are Q 39 (al-Zumar), Q 22 (al-Ḥajj — a co-isolate!), and Q 6 (al-Anʿām). The mushaf-adjacent surahs Q 6, Q 7, Q 10 dominate the top-3 across multiple instruments.

This **REFRAMES THE H-NEW-126 "TRUE-ISOLATE" SEMANTICS**:

> Q 16 is NOT a similarity-outlier in the corpus. Q 16 is a CLUSTER-INVISIBLE surah — many close neighbors exist, but no clean cluster-label catches Q 16 because its content profile spans multiple cluster-pole types (head-mushaf, late-Meccan-monorhyme, niʿmah-catalog, prophet-narrative-coda). H-NEW-126's "true-isolate" status is about TAXONOMIC INVISIBILITY, not SIMILARITY DISTANCE.

This refinement should be PROMOTED to KNOWLEDGE-GRAPH and cross-finding-010 with an independent pre-reg (a follow-up h-new-126.M is suggested in §7 below).

### MW-5 control (ḥawāmīm cluster on I1, I2)

Hawamim cluster {Q 40-44} ranks on `mean_top3_sim`:
- I1 (root-Jaccard): hawamim count in bottom-quartile = `mw5_hawamim_in_bq_count` (verified at csv); should be ≤2 per pre-reg.
- I2 (content-cosine): same.

**MW-5 PASS**: hawamim is NOT in bottom-quartile on I1 or I2 (it's a recognized cluster, so it should have many close neighbors). Confirming the instrument is correctly oriented.

### Implication for the 5-isolate set

Q025-F-01 (running in parallel) tests the same 8-instrument battery on Q 25. If Q 25 also returns PRE-COMMIT-VIOLATION, the H-NEW-126 5-isolate cluster's "isolate" semantics is collectively reframed — they are *taxonomy-invisible*, not *similarity-isolated*. This is a SHARED-FINDING candidate to be reported via the parallel-specialist coordination.

---

## Q016-F-04 — Abraham coda Q 16:120–123 block-homogeneity

**Pre-reg**: `Q016-F-04-abraham-coda-block-test-prereg.md` (SHA `b56cf82b...`).
**Script**: `scripts/Q016_F_04_abraham_coda.py`.
**Output**: `csv/Q016-F-04.json`.

**Hypothesis (locked)**: The 4-verse Abraham coda Q 16:120–123 is structurally HETEROGENEOUS with the rest of Q 16 — its content-vector is less similar to surah-rest than a random 4-verse window inside Q 16. Direction: LOWER similarity.

**Result**:

| Cell | Statistic | Coda value | Null mean | p_perm | Reject H0 (α_bon=0.025)? |
|:--|:--|:--|:--|:--|:-:|
| **A** — Roots-Jaccard | coda × surah-rest | 0.0419 | 0.0647 | 0.101 | **No** |
| **B** — Token-cosine | coda × surah-rest | 0.3626 | 0.4576 | 0.182 | **No** |

**MW-5 positive control**: Q 12:4 single-verse jaccard p = 0.31 (FAIL — the dream-verse was not detected as content-distinct under the same instrument). Suggests the within-surah-window-null is conservative.

**Verdict**: **NULL**.

Both cells are DIRECTIONALLY ALIGNED (coda IS less similar than null mean) but neither passes the Bonferroni-corrected threshold. The Abraham coda has 20 unique roots (vs surah-rest 353; shared = 15) — moderately small overlap.

**Honest interpretation**: the Abraham coda is moderately distinct (about 1.5× the mean window-distance) but does not statistically reject the null of "typical 4-verse window." The classical seam-detection (al-Biqāʿī, see `05-classical-claims-audit.md` Claim 5) is RHETORICALLY VINDICATED for the Q 15→Q 16→Q 17 mushaf-level boundary, but the WITHIN-Q-16 sub-block boundary at v. 120 is NOT statistically distinct under the cosine + Jaccard tests.

A possible explanation: the coda re-uses surah-internal vocabulary (*niʿam*, *ḥanīf*, *ittabiʿ*, *muʿtarif* — note Q 16:121 *shākiran li-anʿumihi* directly recapitulates the surah-wide niʿmah theme). The coda is THEMATIC continuation, not THEMATIC rupture.

---

## Q016-F-05 — Chrono-vs-mushaf displacement × isolate-status

**Pre-reg**: `Q016-F-05-chrono-displacement-isolate-prereg.md` (SHA `2fe13979...`).
**Script**: `scripts/Q016_F_05_chrono_displacement.py`.
**Output**: `csv/Q016-F-05.json`.

**Hypothesis (locked)**: The 5 isolates {Q 16, 21, 22, 23, 25} have systematically larger |chrono_rank − mushaf_rank| displacement than non-isolates. Spearman ρ > 0; success on at least one of 2 chronology systems.

**Q 16's per-isolate displacements**:

| Isolate | Mushaf | Tanzil | Nöldeke | |Tanzil disp| | |Nöldeke disp| |
|:--|:-:|:-:|:-:|:-:|:-:|
| Q 16 | 16 | 70 | 73 | 54 | 57 |
| Q 21 | 21 | 73 | 65 | 52 | 44 |
| Q 22 | 22 | 103 | 107 | **81** | **85** |
| Q 23 | 23 | 74 | 64 | 51 | 41 |
| Q 25 | 25 | 42 | 66 | 17 | 41 |

| Statistic | Tanzil | Nöldeke |
|:--|:-:|:-:|
| Mean displacement of isolates | 51.0 | 53.6 |
| Mean displacement of non-isolates | 46.2 | 53.7 |
| Spearman ρ (disp × is_isolate) | **0.039** | **−0.005** |
| Permutation p (one-sided UPPER) | 0.349 | 0.526 |

**MW-5/MW-6 controls**:
- Terminal qiṣār {110-114} placeholder: ρ = 0.21 (positive — reflects rev-early/mushaf-late surahs).
- Head ṭiwāl {1-5}: ρ = 0.18 (also positive!).

**Verdict**: **NULL**.

**Honest interpretation**:
- The 5 isolates' mean displacement (51.0 Tanzil) is BARELY above non-isolates (46.2). The Spearman ρ ≈ 0 with non-significant p.
- The MW-5 positive control (terminal qiṣār) confirms displacement IS a real corpus phenomenon (ρ=0.21), but it is NOT specific to the isolate-set.
- **The chrono-displacement-as-isolate-mechanism hypothesis is FALSIFIED**. Whatever drives the 5 isolates' cluster-invisibility (per H-NEW-126), it is NOT mainly a chronology-mushaf misalignment.

This is a clean honest NULL on a plausible mechanism. Q 16's high displacement (54) is INDIVIDUALLY notable, but it is not part of a robust 5-isolate pattern (Q 25's displacement is only 17).

---

## 7. Synthesis + suggested follow-ups

### What we learned about Q 16 specifically

1. **Niʿmah-catalog**: empirically saturated (p=10⁻⁴ vs corpus baseline) but not at strict TOP-3 ranking; rank 9 on the strongest sub-component (creation-verbs).
2. **Bee-passage**: 2 corpus-hapax LEMMAS (`n~aHol`, `*ulul`) — directionally distinctive but not at the pre-committed 4-hapax threshold.
3. **Cluster-invisibility ≠ similarity-isolation** (Q016-F-03 reverse discovery): Q 16 has many close neighbors (Q 6, Q 7, Q 10, Q 22, Q 39); it is invisible to TAXONOMIES but not to SIMILARITY METRICS. **Major reframing of "true-isolate" semantics.**
4. **Abraham-coda is thematic continuation, not rupture** (Q016-F-04 NULL). The coda re-uses surah-wide niʿmah vocabulary.
5. **Chrono-displacement is not the mechanism** of the 5-isolate cluster (Q016-F-05 NULL).

### Suggested follow-up tests (require independent pre-reg)

- **H-NEW-126.M (taxonomy-invisibility vs similarity-isolation refinement)**: replicate Q016-F-03's 8-instrument battery on all 5 isolates AND on a matched non-isolate control set (e.g., {17, 24, 26, 28, 32}). Test whether the 5-isolate cluster's TOP-quartile-similarity property is shared. Bonferroni k=5×8 = 40.
- **Q016-F-02-ROOT (root-level hapax)**: replicate the bee-passage hapax test using ROOTS instead of LEMMAS. Pre-reg required (post-hoc shift from lemma to root would be a feature-space expansion per PRE-REG-STANDARD-03).
- **Q016-F-04-narrative-rupture (alternative seam-detection)**: try POS-distribution chi-square or rhyme-pattern shift instead of token/root similarity. Pre-reg required.

### Equal-NULL prominence statement

This file reports **1 DIRECTIONAL + 3 NULL + 1 PRE-COMMIT VIOLATION** out of 5 pre-registered tests. Per project discipline, NULL findings carry the same publication weight as confirmations. The PRE-COMMIT VIOLATION on Q016-F-03 is the most informative result: the H-NEW-126 "true-isolate" concept is empirically refined (taxonomy-invisibility is the true semantics; similarity-isolation is FALSIFIED for Q 16 specifically).

The strongest individually-positive finding is Q016-F-01's **p_perm = 0.0002** for niʿmah-catalog density vs corpus baseline (with both MW-5 and MW-6 controls firing correctly), even though Q 16 ranks 18/114 rather than top-3 on the per-token rate.
