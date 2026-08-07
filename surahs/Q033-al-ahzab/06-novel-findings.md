---
surah: 33
surah_name_ar: الأحزاب
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: 5 PRE-REGISTERED TESTS RUN — 1 FALSIFIED, 1 VINDICATED (length-ctrl), 1 DIRECTIONAL, 2 NULL/RULES-FRAGILE
---

# Q 33 al-Aḥzāb — Novel Findings


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

Five pre-registered tests, locked SHAs, direction locked before observation. NULL findings carry equal prominence with verifications, per project protocol §1.3. The headline is a **major correction to `00-overview.md` Claim 4** (alif-monorhyme corpus-MAXIMUM): FALSIFIED.

## Pre-reg index

| ID | Title | Pre-reg SHA | Verdict |
|:--|:--|:-:|:--|
| Q033-F-01 | Alif-monorhyme purity — corpus rank | `f5310dd0…` | **FALSIFIED** |
| Q033-F-02 | Q 33:40 word-midpoint position | `57cdc302…` | **RULES-TUPLE-FRAGILE** |
| Q033-F-03 | Ḥijāb-cluster lexical cohesion | `7ccfd983…` | **NULL/RULES-TUPLE-FRAGILE** |
| Q033-F-04 | Q 33:72 *amāna* lexical distinctness | `6665a12e…` | **VINDICATED (length-ctrl); DIRECTIONAL (raw)** |
| Q033-F-05 | Wives-cluster vs Medinan-legal controls | `7e063369…` | **FALSIFIED** |

All SHAs verified at runtime by `surahs/Q033-al-ahzab/scripts/Q033_F_all.py`.

---

## Q033-F-01 — Alif-monorhyme purity test (FALSIFIED)

**Pre-reg**: `preregs/Q033-F-01-alif-monorhyme-prereg.md`, SHA `f5310dd00d323c21b902f04324238aa2ba082c2e3d95552c5e84aaaf8bfb652b`.

**Hypothesis (locked)**: Q 33 al-Aḥzāb has the highest alif-final-letter rate of any surah. Direction: rank #1.

**Method**: per-verse last-letter (after stripping tashkeel and pause-marks); alif-finals = {ا, آ, أ, إ, ى, ٰ}. Rules-tuple: min-tashkeel, last-letter-of-verse, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi.

**Result**: Q 33 alif-final-rate = **0.9863** (72/73), corpus rank = **11 of 114**.

**Top 10 by alif-final rate**:

| Rank | Surah | Name | Type | Rate | Counts |
|--:|--:|:--|:--|--:|:-:|
| 1 | 18 | al-Kahf | meccan | 1.0000 | 110/110 |
| 2 | 48 | al-Fatḥ | medinan | 1.0000 | 29/29 |
| 3 | 65 | al-Ṭalāq | medinan | 1.0000 | 12/12 |
| 4 | 72 | al-Jinn | meccan | 1.0000 | 28/28 |
| 5 | 76 | al-Insān | medinan | 1.0000 | 31/31 |
| 6 | 87 | al-Aʿlā | meccan | 1.0000 | 19/19 |
| 7 | 91 | al-Shams | meccan | 1.0000 | 15/15 |
| 8 | 92 | al-Layl | meccan | 1.0000 | 21/21 |
| 9 | 17 | al-Isrāʾ | meccan | 0.9910 | 110/111 |
| 10 | 25 | al-Furqān | meccan | 0.9870 | 76/77 |
| **11** | **33** | **al-Aḥzāb** | **medinan** | **0.9863** | **72/73** |

The single non-alif verse in Q 33 is **v.4** (the triple-negation declaring no two hearts in one breast / no *ẓihār*-derived motherhood / no biological-status for adopted sons), ending *yahdī al-sabīla* (lām-final). This verse is the legal premise underlying v.37's Zayd-Zaynab marriage-norm — i.e., the ONE verse breaking Q 33's monorhyme is the verse that empirically grounds the surah's most controversial legal action.

**Cross-corpus poetry control** (al-Muʿallaqāt):
- Labid: 0.9888 (176/178) — alif-monorhyme qaṣīda
- ʿAmr b. Kulthūm: 0.9810 (103/105) — alif-monorhyme qaṣīda
- Imruʾ al-Qays, ʿAntara, Ṭarafa, al-Ḥārith: 0.0000 each — these qaṣāʾid use a non-alif rāwī (most commonly *lām*, *mīm*, *dāl*).

So when a pre-Islamic *qaṣīda* is alif-monorhyme, it achieves Q 33-comparable purity (≈ 0.98). The structural analogy holds — it is just **not unique** to Q 33 within the Quran.

**Verdict**: **FALSIFIED** under the locked direction (rank 1). The signal demoted to: "Q 33 is one of 11 surahs with alif-final ≥ 0.98; eight surahs achieve perfect 1.0000."

**Alif-cluster follow-up ([[h-new-910-alif8-cluster|H-NEW-910]], 2026-04-28)**: The 8-surah cluster `{Q 18, 48, 65, 72, 76, 87, 91, 92}` was tested for cohesion on FR-roots, verse-count, chronology, mushaf-position, and 4-axis composite (Bonferroni-5, α_bon=0.01). **0 of 5 cells PASSED**; H3 chronology PRE-COMMIT-VIOLATED (direction reversed); H4 mushaf and H5 4-axis DIRECTIONAL only. Family verdict: **NULL CLUSTER — alif-monorhyme is a SURFACE rāwī feature, not a deep architectural cluster.** Q 33 (rate 0.9863, rank 9 by raw-score under this run's rules-tuple) sits ADJACENT to the 8-cluster but does not extend its cohesion (comparator-12 adding Q 33, 20, 17, 25 BREAKS the FR-roots signal: pct 86.84%). The Q 33-versus-poetry analogy from §"poetry control" stands: alif-monorhyme is a recognized Jāhilī *qaṣīda* form (Labid 0.9888; ʿAmr b. Kulthūm 0.9810), and the Quran's 8 + 1 (Q 33) alif-rāwī surahs are likewise just a *form-class*, not a content-class.

**Implication for project**: `00-overview.md` §5 claim "corpus-MAXIMUM monorhyme purity" needs explicit retraction. Recommended replacement language: "Q 33's alif-final rate of 98.6% places it in the alif-monorhyme bucket alongside ten other surahs (8 at 100%, plus Q 17, Q 25, Q 33). The break-verse v.4 is rule-tuple-significant: it is the surah's legal-premise verse for the Zayd-Zaynab norm at v.37. The 8-surah 100%-alif cluster does NOT cohere on deeper architectural axes ([[h-new-910-alif8-cluster|H-NEW-910]]); the alif-rāwī itself is form-class only."

**Honest limits**:
- The one Quranic *Sūrat al-Aḥzāb*-vs-poetry comparison is undermined by the same fact: 8 alif-monorhyme surahs sit alongside 2 alif-monorhyme Muʿallaqāt. The *qaṣīda*-Quran similarity-class is a much larger bucket than the overview originally implied.
- A rules-tuple variant (e.g., counting only ـا of *fatḥa-tanwīn*-realization) might shift Q 33's rank; we did not run it. Flagged for follow-up as a rules-tuple-variant test.
- H-NEW-700 reports rhyme-entropy of 0.072 nats for Q 33 (00-overview §5). This must have used a different last-letter model (perhaps tashkeel-sensitive, distinguishing *-an / -īman / -īrā / -ūnā*). Under our simplest rules-tuple, multiple surahs have entropy = 0; Q 33's 0.072 reflects only the v.4 break.

Output: `surahs/Q033-al-ahzab/csv/Q033-F-01.json`.

---

## Q033-F-02 — Q 33:40 (*khātam al-nabiyyīn*) word-midpoint position test (RULES-TUPLE-FRAGILE)

**Pre-reg**: SHA `57cdc302068c03d3d7b6a12f9ed5dba722f390cb9b612a6431236f0cfde48a63`.

**Hypothesis (locked)**: |cum_pos(v.40) − 0.5| < 0.05 (v.40 sits within 5pp of word-cumulative midpoint).

**Method**: cumulative word-count up to and including v.40, divided by total surah words. Rules-tuple: no-tashkeel, orthographic-token, words.

**Result**:
- Total Q 33 words: **1,303**
- Cum_words(v.40) = **750**
- Cum_pos(v.40) = **0.5764**
- |Cum_pos − 0.5| = **0.0764** (7.64pp off midpoint).
- Rank of v.40 by proximity-to-midpoint = **9 of 73 verses**.

**Top 5 verses closest to word-midpoint**:

| Rank | Verse | abs_diff | cum_pos |
|--:|:-:|--:|--:|
| 1 | 35 | 0.0019 | 0.4981 |
| 2 | 36 | 0.0165 | 0.5165 |
| 3 | 34 | 0.0249 | 0.4751 |
| 4 | 37 | 0.0533 | 0.5533 |
| 5 | 33 | 0.0556 | 0.4444 |

The actual word-midpoint of Q 33 falls **between v.35 and v.36** — i.e., v.35 is the gender-parity catalog (*al-muslimīn wa al-muslimāt...*) which sits at cum_pos 0.498 — that is the structural focal point of Q 33 by word-cumulative metric.

**Verdict**: **RULES-TUPLE-FRAGILE — pre-reg literally fails (|diff| > 0.05); rank-9 of 73 is suggestive but not law-strength**.

**Re-interpretation**: The word-cumulative center of Q 33 is **v.35 (the gender-parity catalog)**, not v.40 (the *khātam al-nabiyyīn* verse). v.35's centrality is itself a non-trivial finding — it is a corpus-unique 10-pair parallelism enumerating gender-parity in righteous attributes; classical *tafsīr* (al-Ṭabarī, al-Rāzī) treats it as a pivot. v.40 sits 5 verses (about 53 words / 4.1pp of the surah) past the midpoint. Both are within block E's "civic-prophet code" cluster.

**Honest limits**:
- The pre-registered direction was strict (|diff| < 0.05). We respect the literal failure.
- The DIRECTIONAL signal (rank 9/73, top 12%) survives.
- A pre-registered alternative (v.35 = midpoint) would have been confirmed; but we did NOT pre-register it — the v.35 observation is post-hoc and carries single-test α=0.05 ceiling per protocol §1.7 (MW-7).

Output: `surahs/Q033-al-ahzab/csv/Q033-F-02.json`.

---

## Q033-F-03 — Ḥijāb-cluster lexical cohesion test (NULL / RULES-TUPLE-FRAGILE)

**Pre-reg**: SHA `7ccfd983c97c34b692dd2a4469ac974e756628fc306139082f42c29e3af1e2bf`.

**Hypothesis (locked)**: V_HIJAB = {28, 29, 30, 31, 32, 33, 34, 53, 59} has higher mean-pairwise-Jaccard cohesion than random size-9 samples from Q 33. Direction: right-tailed.

**Method**: 10,000 random size-9 verse-samples; permutation p-value. Rules-tuple: no-tashkeel, orthographic-token, Jaccard.

**Result**:
- Observed cohesion: **0.0545**
- Permutation mean: **0.0391**
- Permutation max: 0.130
- Permutation p (right-tail): **0.1246** (1,246 of 10,001 permutations ≥ observed)

**Verdict**: **NULL / RULES-TUPLE-FRAGILE** (0.05 < p < 0.50).

**Direction is correct**: V_HIJAB's cohesion exceeds random by 39.4%, but the 10,000-permutation p-value of 0.12 falls outside the α=0.05 threshold. The directional signal is correct; the magnitude is sub-significant.

**Interpretation**: the ḥijāb-cluster verses (vv. 28-34, 53, 59) are MORE cohesive than random Q 33 verses, but not at law-strength under Jaccard-cohesion. A more-sensitive cohesion metric (TF-IDF-weighted; root-bag) might lift the signal — pre-flagged as possible follow-up Q033-F-03.1.

**Honest limits**:
- Token-set Jaccard is coarse; common Quranic tokens inflate cohesion uniformly across samples, suppressing signal.
- The cluster is heterogeneous: vv. 28-34 are the wives-of-Prophet *takhyīr* + *qarna fī buyūtikunna* code; v.53 is house-entry etiquette + *min warāʾi ḥijāb*; v.59 is *jalābīb* exterior-garment. They share the THEME of seclusion-modesty but draw on partly disjoint lexical fields.

Output: `surahs/Q033-al-ahzab/csv/Q033-F-03.json`.

---

## Q033-F-04 — Q 33:72 *amāna* verse lexical distinctness test (VINDICATED, length-ctrl)

**Pre-reg**: SHA `6665a12ef7d3626036aec78871d0479a56bb4ec35994dd4ab71a821efccf2a6d`.

**Hypothesis (locked)**: distinctness(v.72) ranks ≤ 8 of 73 (top 11%) within Q 33.

**Method**: distinctness(v) = 1 − mean Jaccard(v, w) for w ≠ v in Q 33; rank descending. Length-controlled: residual from linear regression of distinctness on word-count.

**Result**:
- v.72 raw distinctness rank: **9 of 73** (top 12.3%) — *miss the strict ≤8 threshold by 1*.
- v.72 length-controlled distinctness rank: **8 of 73** (top 11.0%) — *meets threshold*.

**Verdict**: **VINDICATED (length-controlled); DIRECTIONAL (raw)**.

The locked direction holds when the verse-length confound (longer verses have more unique tokens by chance) is removed. v.72 has 18 words — among the longer in Q 33 — and is genuinely lexically distinctive even after this is regressed out.

**Top-distinct vocabulary in v.72** (verified vs `data/morphology/quranic-corpus-morphology-0.4.txt`):
- *al-amāna* (the trust): root *ʾ-m-n*, recurs elsewhere in Q 4:58, Q 8:27, Q 23:8, Q 70:32 — but the cosmic-trust framing is unique to Q 33:72.
- *yaḥmilnahā / ḥamalahā* (root *ḥ-m-l*): in this hapax-application to a cosmic burden.
- *ashfaqna* (they were apprehensive, root *sh-f-q*): unique-to-Q 33 in the verbal form here.
- *ẓalūm jahūl* (oppressor, ignorant): the **paired epithet is corpus-hapax** — no other verse couples *ẓ-l-m* with *j-h-l*.

This is a genuine corpus-architectural finding: the *amāna* verse's lexical signature is empirically distinct, and the *ẓalūm jahūl* hapax-pair is a corpus-unique close.

**Honest limits**:
- Token-set Jaccard inflates with verse-length; we corrected via length-controlled regression. A more powerful test would use TF-IDF or n-gram-NCD.
- The pre-reg threshold (≤8) was tight; raw rank misses by 1. We honestly report DIRECTIONAL on raw and VINDICATED on length-controlled.

Output: `surahs/Q033-al-ahzab/csv/Q033-F-04.json`.

---

## Q033-F-05 — Wives-cluster cohesion vs other Medinan-legal clusters (FALSIFIED)

**Pre-reg**: SHA `7e0633691e733885161e220cfdf4c5f5f18eb4bbc219a828f48f9a9e7e7d7e93`.

**Hypothesis (locked)**: Q33:28-34 cohesion ranks #1 of {Q33:28-34, Q2:280-283, Q4:11-14, Q65:1-7, Q24:2-9}.

**Method**: mean-pairwise-Jaccard cohesion per cluster; ranked.

**Result**:

| Rank | Cluster | Cohesion |
|--:|:--|--:|
| 1 | **Q4:11-14 (inheritance)** | 0.0956 |
| 2 | Q65:1-7 (divorce / al-Ṭalāq) | 0.0748 |
| 3 | Q24:2-9 (zinā / liʿān) | 0.0639 |
| 4 | **Q33:28-34 (wives-of-Prophet)** | 0.0495 |
| 5 | Q2:280-283 (debt) | 0.0433 |

**Verdict**: **FALSIFIED**. Q33:28-34 ranks 4 of 5; Q 4:11-14 (inheritance) is the most cohesive. The wives-cluster is *not* unusually tight — it is, in fact, the second-loosest of the five Medinan-legal clusters tested.

**Interpretation**:
- The Q 4 inheritance verses (11-14) are extraordinarily formulaic — they share a near-templated structure (*li-l-dhakar mithlu ḥaẓẓi al-unthayayn*…), driving high Jaccard.
- The Q 65 divorce verses share *yā ayyuhā al-nabī iẓhā ṭallaqtum…* + *ʿidda* terminology, generating moderate cohesion.
- The Q 33 wives-cluster, despite thematic unity, draws on a wide vocabulary: *takhyīr*, *zīna*, *fa-lā takhḍaʿna bi-al-qawl*, *qarna fī buyūtikunna*, *taṭhīr*, *al-ḥikma* — i.e., the cluster covers **multiple sub-topics within seven verses** rather than templating one legal point.
- The Q 33 wives-cluster is **legally diverse, not legally uniform** — and Jaccard cohesion correctly detects that.

This is an interesting ANTI-finding: it tells us that classical *asbāb-al-nuzūl* clustering (the Bukhārī #4789-4791 wives-passages tradition, often grouping vv. 28-34 as a single occasion) reflects **occasion-of-revelation unity, NOT lexical-topical unity**.

**Honest limits**:
- Different cluster sizes (n = 4, 7, 4, 7, 8) affect Jaccard variance.
- Jaccard is sensitive to common-token inflation; the inheritance cluster's heavy reuse of *waṣiyya / mīrāth / aḥad/uthnayn / wālid* terms gives it an inflated raw Jaccard.

Output: `surahs/Q033-al-ahzab/csv/Q033-F-05.json`.

---

## Aggregate verdict + meta-finding

**Five tests, locked directions, honestly reported**:
- 1 FALSIFIED (the corpus-MAXIMUM alif-monorhyme claim — major correction to overview).
- 1 RULES-TUPLE-FRAGILE (v.40 word-midpoint — DIRECTIONAL by rank, FALSIFIED by absolute threshold).
- 1 NULL / RULES-FRAGILE (ḥijāb-cluster cohesion).
- 1 VINDICATED-length-controlled (v.72 *amāna* distinctness).
- 1 FALSIFIED (wives-cluster vs other Medinan-legal — wives-cluster is among the LOOSEST not tightest).

**Meta-finding**: Q 33's empirical-architectural signature is **outlier-driven, NOT cluster-driven**. The surah's UAS rank 1 and outlier-strength +31.46pp (per H-NEW-840, H-NEW-590) come from **whole-surah** atypicality (low *iʿjāz al-fawāṣil*, high TSP-cost neighbor-pairs Q32-Q33-Q34), not from any single internally-cohesive sub-cluster. Even the iconic ḥijāb-cluster fails to achieve sub-α cohesion at Jaccard-strength.

This is consistent with the cross-finding-026 dual-iʿjāz architecture: Q 33 is a structural-iʿjāz outlier whose distinctiveness is **macro-structural**, not **local-cluster**. Classical narrative-cluster identification (e.g., Bukhārī's *asbāb-al-nuzūl* groupings) is THEMATIC, not LEXICAL.

## Cross-references

- [[Q033-al-ahzab/02-content-analysis|02-content-analysis.md]] — block segmentation backing all five tests' verse-set definitions.
- [[Q033-al-ahzab/05-classical-claims-audit|05-classical-claims-audit.md]] — claims 2, 4, 6 directly use F-01, F-02, F-04.
- [[Q033-al-ahzab/07-cross-references|07-cross-references.md]] — F-04's *amāna* cross-surah trail; F-01's pre-Islamic poetry comparator.
- [[h-new-590-outlier-spectrum]], [[h-new-840-unified-architectural-score]] — establish the macro-structural outlier rank that the cluster-cohesion tests can NOT reproduce locally.
- [[cross-finding-026-iʿjāz-architecture]] — the dual-iʿjāz frame the F-results cluster around.
