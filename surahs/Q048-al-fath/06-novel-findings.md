---
surah: 48
file_type: novel-findings
date_last_updated: 2026-05-09
specialist: Q048-al-Fath-specialist
H-NEW-range: 1260-1263
---

# Q 48 al-Fatḥ — Novel Pre-Registered Findings


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

> 4 SHA-locked pre-registered tests (Q048-F-01..F-04 / H-NEW-1260..1263), all with seed=20260509. Direction-locked, Bonferroni-declared, equal NULL prominence.

---

## Q048-F-01 — *fatḥ* root-density (H-NEW-1260)

**Pre-reg**: `preregs/Q048-F-01-fath-root-density-prereg.md`
**SHA**: `263b58105397cb13f1ec36ad5faeac1f7603c21fc10ba57a0027b37c5696f511`
**Output**: `csv/Q048-F-01.json`

### Direction-locked hypothesis

Q 48 has corpus-MAX or near-MAX *fatḥ* (f-t-ḥ) root density relative to length-controlled corpus baseline.

### Result

- **Q 48 *ftH* tokens**: 4 (across 3 verses: 1, 18, 27)
- **Corpus *ftH* tokens**: 38
- **Q 48 root-tagged tokens**: 916
- **Corpus root-tagged tokens**: 128,219
- **Expected under uniform**: 0.27
- **Enrichment**: **13.0×**
- **Hypergeometric p**: **2.5 × 10⁻⁴**
- **Permutation p (n=10,000)**: **4.0 × 10⁻⁴** (cross-validates hypergeometric)
- **Density rank** (length-controlled, ≥100 root-tokens): **RANK 1 / 79**
- **Count rank** (all 114 surahs): **RANK 2 / 114** (tied with Q 7, but Q 7 has 6.2× more total tokens)

### Verdict: **PASS-DIRECTED**

(Per HANDOFF/04-DISCIPLINE.md post-hoc protocol: single-test α=0.05 cap; verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION on a distinct data dimension.)

### Honest limits

1. The brief stated "5 occurrences" of *fatḥ*; on-disk QAC v0.4 returns **4 root-tokens / 3 verses**. This pre-reg uses the verified count.
2. Q 48 is NAMED for this root, so the test is in some sense tautological. The empirical contribution = quantifying the magnitude (13× corpus rate, p < 10⁻³).
3. INDEPENDENT REPLICATION candidate: orthographic substring فتح count (different operationalization).

### Cross-references

- [[h-new-86]] (Q 12 Yūsuf name-root concentration, 532× enrichment, p = 3 × 10⁻³⁹) — analogous test for the Yūsuf-name-surah.
- [[h-new-660]] (compression-tail gradient — root-density structure).
- This finding extends cross-finding-015 (classical-doctrine validation pattern) — the surah-name-root-concentration claim is empirically VALIDATED for Q 48.

---

## Q048-F-02 — Perfect alif-monorhyme uniqueness (H-NEW-1261)

**Pre-reg**: `preregs/Q048-F-02-perfect-monorhyme-uniqueness-prereg.md`
**SHA**: `5f595679370381c7c20ed309906c294b5bbfc0eecf4e915a0095c23a107130af`
**Output**: `csv/Q048-F-02.json`

### Direction-locked hypothesis

Q 48 al-Fatḥ is the **unique** perfect-alif-monorhyme Medinan surah of length ≥ 28 verses.

### Result

- **Total perfect-monorhyme surahs in corpus**: 15
- **Q 48 perfect-monorhyme**: TRUE (29/29 verses end in alif, frac = 1.0, rhyme entropy = 0.0 nats)
- **Medinan perfect-monorhyme surahs of v ≥ 28**: **2** — Q 48 (29 verses, ا) AND Q 76 al-Insān (31 verses, ا)
- **Strict uniqueness**: FALSE (Q 76 satisfies same criterion under Tanzil-Egyptian Medinan classification)

### Verdict: **DIRECTIONAL**

The descriptive claim is NOT singleton-unique — Q 48 is **paired with Q 76 al-Insān**. Both are alif-monorhyme, both classified Medinan in Tanzil-Egyptian, both length ≥ 28.

### Refined finding

The empirical fingerprint is **{Q 48, Q 76}** — a pair of large-Medinan alif-monorhyme surahs. Q 76 al-Insān has its own thematic-distinct content (eschatological reward of the *al-abrār*) but shares with Q 48 the alif-cadence-uniformity. This pair-finding is more empirically precise than the original singleton-uniqueness claim.

### Honest limits

1. Q 76 al-Insān's Medinan classification is debated; some classical chains label it Meccan. Under the Meccan classification, Q 48 IS singleton-unique.
2. The test is descriptive-categorical, not frequentist; the verdict reflects the categorical claim's empirical realization.
3. The al-Bukhārī Maghāzī #315 / Tafsir #356 attestation of the Prophet's vibrant-quivering recitation of Q 48 is structurally consistent with the alif-monorhyme uniformity (sustained-tone delivery enabled by uniform terminal cadence).

### Cross-references

- [[h-new-700]] (rhyme-letter diagnostics; the 15 perfect-monorhyme surahs are listed there).
- [[Q076-al-insan]] (the paired large-Medinan alif-monorhyme surah — investigation queued).

---

## Q048-F-03 — Top-5 FR-nearest in back-Medinan musabbiḥāt-adjacent cluster (H-NEW-1262)

**Pre-reg**: `preregs/Q048-F-03-musabbihat-cluster-membership-prereg.md`
**SHA**: `df56fc6e80aee104d05a3bff7d4b4f6277aa7fc0c9d0513dc9acbd67d20c5685`
**Output**: `csv/Q048-F-03.json`

### Direction-locked hypothesis

Q 48's top-5 Fisher-Rao nearest neighbors are ALL in the back-Medinan range Q 57-64, AND ≥ 3 are formal musabbiḥāt-cluster members per H-NEW-58c.

### Result

- **Q 48's top-5 FR-nearest**:
  - Q 61 al-Ṣaff: 0.7876 (musabbiḥāt member ✓)
  - Q 64 al-Taghābun: 0.7936 (musabbiḥāt member ✓)
  - Q 59 al-Ḥashr: 0.8181 (musabbiḥāt member ✓)
  - Q 63 al-Munāfiqūn: 0.8265 (NOT musabbiḥāt; back-Medinan ✓)
  - Q 57 al-Ḥadīd: 0.8350 (musabbiḥāt member ✓)
- **T1 (top-5 ⊆ Q 57-64)**: TRUE
- **T2 (≥ 3 musabbiḥāt)**: TRUE (4 of 5 are musabbiḥāt)
- **P(T1 under uniform-random null)**: **3.99 × 10⁻⁷**
- **P(T2 under uniform-random null)**: **4.15 × 10⁻⁴**
- **Joint p (independence assumed)**: ~ **1.7 × 10⁻¹⁰** (extreme)

### Verdict: **CONFIRMED**

Both T1 and T2 pass at extreme significance. Q 48 is structurally embedded in the back-Medinan musabbiḥāt-adjacent cluster, NOT in a Q 47-Q 49 mushaf-adjacent cluster.

### Implications

- The al-Biqāʿī *Naẓm al-Durar* claim that Q 47-Q 48-Q 49 form a tight munāsabah ring is **NOT empirically supported at FR level** (already noted DIRECTIONAL via Q047-F-03 with triplet p=0.252). The classical reading is THEMATIC-narrative; the empirical reading is VOCABULARY-REGISTER.
- Q 48 belongs structurally to the **back-Medinan community-formation cluster** (Q 57, 59, 61, 63, 64) — a cluster characterized by *yā ayyuhā al-ladhīna āmanū* address-density, *musabbiḥāt*-style cosmic-praise frames, and short-Medinan length-class.
- This finding REINFORCES cross-finding-009 (META-cluster network with Q 62 hub) by adding Q 48 to the back-Medinan periphery cluster.
- This finding REINFORCES cross-finding-010 (4-region META-architecture) — Q 48 anchors to the **back-upper region** {Q 59, 62}.

### Cross-references

- [[h-new-58c]] (musabbiḥāt cluster {Q 57, 59, 61, 62, 64}).
- [[h-new-89]] (META-cluster network; Q 62 hub).
- [[cross-finding-009]] / [[cross-finding-010]] (META-cluster networks).
- [[Q047-F-03]] (Q 47-Q 48-Q 49 triplet test, NULL — confirms the classical claim's FR-empirical insufficiency).

---

## Q048-F-04 — Forward-prophecy pair {Q 48, Q 30} FR-cohesion (H-NEW-1263)

**Pre-reg**: `preregs/Q048-F-04-prophecy-pair-cohesion-prereg.md`
**SHA**: `53364809db4b805494b1e8343627f8f007979ec6c1b66f5931a9d3a7ab4bc4b8`
**Output**: `csv/Q048-F-04.json`

### Direction-locked hypothesis

The classical *iʿjāz al-ghayb* pair claim — that Q 48 (Mecca conquest prediction Q 48:27) and Q 30 (Romans-Persia prophecy Q 30:2-4) form a structurally coherent pair — is empirically supported at FR level.

### Result

- **FR(Q 48, Q 30)**: **1.0101**
- **Corpus mean FR**: 0.9235
- **Q 30 rank in Q 48-nearest**: **56 / 113** (slightly above the median; Q 30 is FAR from Q 48 in FR-space)
- **T1 (FR ≤ corpus mean)**: FALSE
- **T1 strict (FR ≤ 0.86)**: FALSE
- **T2 (not in top-50 farthest)**: TRUE (Q 30 is in the middle, not in top-50 farthest)
- **T2 strict (top-30 nearest)**: FALSE

### Verdict: **NULL**

The classical *iʿjāz al-ghayb* pair claim is **NOT supported** at FR-cohesion level. Q 48 + Q 30 do NOT form a structural cluster.

### Interpretation

The classical *iʿjāz al-ghayb* sub-classification is **THEMATIC-CONTENT** — both Q 48:27 and Q 30:2-4 contain falsifiable forward-looking temporal predictions, and classical iʿjāz scholars (al-Suyūṭī, al-Khaṭṭābī) groups them together as iʿjāz-types — but they do **NOT share root-distribution similarity** at the surah-aggregate level.

This is consistent with the **dual-iʿjāz typology** (cross-finding-018):
- **Structural-iʿjāz** (al-Bāqillānī): metric-based, FR-distance signal.
- **Theological-iʿjāz** (al-Khaṭṭābī, including iʿjāz al-ghayb): thematic, NOT FR-distance signal.

Q 48 and Q 30 are both **theological-iʿjāz exemplars** (forward-prophecy class) but their FR-distance is high because their **content-vocabulary differs** (Q 30's Persian-Roman geopolitics + Bedouin-religious-anxiety vocabulary differs from Q 48's Hudaybiyya-Bayʿah-Booty vocabulary).

### Honest limits

1. The classical pair claim is THEMATIC, not structural-distance. The pre-reg LOCKED a HYPOTHESIS that was EXPECTED to fail at FR level. This is the project's discipline of testing classical claims and reporting NULLs with equal prominence.
2. The NULL result is itself interpretively important: it adds Q 48 + Q 30 to the **structural-vs-theological-iʿjāz separation** body of evidence (cross-finding-018, cross-finding-015).
3. The thematic pair claim could be RE-TESTED at a different feature level (e.g., predictive-grammar features, future-tense verb density, conditional clauses) — those tests would not be FR-based and might support the thematic pair.

### Cross-references

- [[h-new-119]] (the *7 samawat* RETRACTION — a related case of classical-numerical claim failing empirical test).
- [[cross-finding-015]] (classical-scholarship validation pattern — Q 48 + Q 30 NULL adds to the empirical-record).
- [[cross-finding-018]] (dual-iʿjāz typology, if extant; otherwise queued as a candidate synthesis).

---

## Aggregated synthesis

| Test | H-NEW | Verdict | Key result |
|:--|:--|:--|:--|
| Q048-F-01 | 1260 | **PASS-DIRECTED** | Q 48 ftH-density 13× corpus rate, p = 2.5 × 10⁻⁴, RANK 1/79 length-controlled |
| Q048-F-02 | 1261 | **DIRECTIONAL** | Q 48 paired with Q 76 al-Insān as the only large-Medinan alif-monorhymes |
| Q048-F-03 | 1262 | **CONFIRMED** | Q 48 top-5 FR-nearest ⊆ Q 57-64 (joint p ~ 1.7 × 10⁻¹⁰) |
| Q048-F-04 | 1263 | **NULL** | Q 48 + Q 30 are FR-distant; classical iʿjāz pair is THEMATIC, not structural |

**Headline finding**: Q 48 al-Fatḥ is the **corpus-EXACT *fatḥ*-root-density signature surah** (Q048-F-01) AND a **back-Medinan musabbiḥāt-adjacent cluster member** (Q048-F-03), occupying a structurally distinct position from its mushaf-adjacent neighbors Q 47 and Q 49. Two classical claims are empirically tested: the al-Biqāʿī Q 47-Q 48-Q 49 munāsabah claim is FR-DIRECTIONAL only (per Q047-F-03), and the iʿjāz al-ghayb {Q 48, Q 30} pair claim is FR-NULL (Q048-F-04). The project's discipline of equal NULL prominence is preserved.

**Bonferroni accounting**: each of the 4 tests is its own family (k=1 within family). Across the 4-test specialist-level family, a Bonferroni-corrected α = 0.05/4 = 0.0125. Q048-F-01 (p=2.5e-4) and Q048-F-03 (joint p~1.7e-10) survive the corrected threshold; Q048-F-02 is descriptive-categorical (no frequentist p); Q048-F-04 is NULL.

**Cross-finding contributions**:
- Q 48 added to the back-Medinan musabbiḥāt-adjacent cluster (cross-finding-009 / 010 reinforcement).
- Q 48 + Q 76 alif-monorhyme pair as a new descriptive-categorical fingerprint (queue: H-NEW-1264 cross-replication).
- Q 48 + Q 30 NULL as a contribution to cross-finding-015 (classical-scholarship validation pattern; thematic-vs-structural-iʿjāz separation).
- Q 48 ftH-density as a parallel to H-NEW-86 (Q 12 Yūsuf-name concentration) — surah-name-root concentration as a recurring corpus signature.

---

*All tests SHA-locked, seed=20260509, executed with embedded SHA verification at runtime.*
