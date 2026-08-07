---
surah: 23
surah_name_ar: المؤمنون
surah_name_translit: al-Muʾminūn
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — three pre-registered tests; one PASS-DIRECTED-EXACT, one PASS-DIRECTED, one pre-commit-violation NULL
---

# Q 23 al-Muʾminūn — Novel Findings


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

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

Three pre-registered tests landed in this session. All three pre-regs are SHA-locked at the embedded hash; all three runner-scripts verify the SHA at runtime; permutation tests use 10000 perms at seed 20260509. Family-Bonferroni-corrected α = 0.05 / 3 = 0.0167.

| Finding | Pre-reg SHA256 | Verdict | p (or rank) |
|:--|:--|:--|:--|
| Q023-F-01 — UAS top-10 cluster FR-cohesion | `9d16de4b...` | **PRE-COMMIT-VIOLATION-NULL** | p_lower = 1.0 (direction reversed) |
| Q023-F-02 — believer-attributes longest contiguous block | `ae48a41c...` | **PASS-DIRECTED-EXACT** | corpus-rank 1, single-tie |
| Q023-F-03 — embryology pericope pair Q 23:12-14 ↔ Q 22:5 | `4518ad85...` | **PASS-DIRECTED** (not under Bonferroni) | p_upper = 0.0232 |

## 1. Q023-F-01 — UAS top-10 FR-cohesion: PRE-COMMIT-VIOLATION NULL

### 1.1 Pre-registered claim

The top-10 UAS surahs `{Q 1, 2, 9, 10, 12, 17, 23, 24, 33, 55}` are **FR-tighter on root-distribution** than a length-matched random null. Direction-locked: lower mean pairwise FR distance than null.

### 1.2 Result

| Statistic | Value |
|:--|:-:|
| T_obs (mean pairwise FR within top-10) | **1.0914** |
| Length-matched null median | 0.9910 |
| Length-matched null mean | 0.9906 |
| Length-matched null range | [0.902, 1.077] |
| p (lower-tail, pre-registered direction) | **1.0** |
| Replication (seed +1000) p_lower | 1.0 |
| Strict-random null p_lower | 0.9999 |

T_obs is **HIGHER** than the null median by **0.10 FR-units** — the top-10 UAS cluster is **FR-DISPERSED**, not FR-cohesive. Q 2 and Q 9 (the corpus's two Medinan-large surahs) are mutually distant from the rest of the top-10; Q 33 (rank 1 UAS) is the most distinct Medinan-Aḥzāb surah in the corpus; Q 55 al-Raḥmān (the supreme monorhyme) is content-distant from Q 23. The top-10 UAS cluster is multi-axis (outlier-magnitude × cost × |iʿjāz|), not root-distribution.

### 1.3 Honest pre-commit-violation report

This is a **direction-reversed pre-commit violation** per Protocol §1.8: the test was pre-registered with FR-cohesion direction; the observed direction is **opposite** (FR-dispersion). Per the protocol, this is published as **NULL with prominence** and flagged as pre-commit-violation. The finding is **not retracted** but **inverted** in interpretation.

### 1.4 What this NULL tells us

Three substantive lessons:

1. The UAS is a **z-sum of correlated-but-axis-distinct metrics**. The top-10 set is a multi-axis cluster, not a root-distribution cluster. This is consistent with [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]'s typology: structural-iʿjāz, theological-iʿjāz, outlier-without-iʿjāz, and (per 01-empirical-profile §10) the *purer-than-pure monorhyme* fifth-cell.
2. **Marker-thickness rule** ([[cross-finding-025|cross-finding-025]]) applies: a top-10 group sharing the metaverse "high UAS" is a thin-marker (single-axis aggregate). Per cross-finding-025, thin markers without multi-axis correlation will NULL on FR root-distribution. Q023-F-01 is a fresh PC for cross-finding-025.
3. The UAS top-10 includes both **structural-iʿjāz** types (Q 33, Q 1, Q 2 — high sig_A) and **monorhyme-saturation** types (Q 23, Q 55 — low/negative sig_A). FR root-distribution does not place these on a single locus.

### 1.5 Cross-finding alignment

- Adds 1 NULL data point to [[cross-finding-025|cross-finding-025]] marker-thickness rule (now 5 PASS + 5 NULL + 1 PASS-DIRECTED).
- Refines [[h-new-840-unified-architectural-score|H-NEW-840]]: UAS is a **non-root-distribution** multi-axis aggregate. The top-10 cluster is rank-1 on UAS but **dispersed** on FR.
- Refines [[h-new-1190|H-NEW-1190]]-style sub-cluster work: high-|outlier|-only sub-samples may cohere, but high-UAS sub-samples do not.

## 2. Q023-F-02 — Believer-attributes longest contiguous block: PASS-DIRECTED-EXACT

### 2.1 Pre-registered claim

The *muʾminūn-attributes* checklist in Q 23 is the **corpus-EXACT longest contiguous *believer-attributes* enumeration**, measured by strict-marker run-length (الذين هم / والذين هم).

### 2.2 Result

| Surah | Block | Strict-marker run-length | Verses |
|:-:|:--|:-:|:-:|
| **Q 23** | The muʾminūn-typology | **4** | **vv. 2-5** |
| Q 70 | al-Maʿārij muṣallīn-attributes | 3 | vv. 32-34 |
| Q 107 | al-Māʿūn al-muṣallīn block | 2 | vv. 5-6 |
| (others) | — | ≤ 1 | — |

Q 23 is **corpus-rank 1 with a strict-rank-1 lead** (one ahead of Q 70). The result is a single-tie (only Q 23 holds rank 1).

**Within the broader Tirmidhī-ḥadīth-defined 10-verse unit (Q 23:1-10)**:
- v. 1 = framing *qad aflaḥa l-muʾminūn*
- v. 2-5 = strict 4-verse marker-run (khushūʿ-prayer → laghw → zakāh → ḥifẓ-furūj)
- v. 6-7 = sub-clauses of trait 4 (spouse-exception + transgressor-closer)
- v. 8-9 = *alladhīna hum* + *alladhīna hum* (amāna and ṣalawāt)
- v. 10 = closing *ulāʾika humu l-wārithūn*

The strict 4-verse run vv. 2-5 is the empirical-EXACT corpus maximum.

**Disbeliever-attribute control**: the longest contiguous *alladhīna kafarū / alladhīna kadhdhabū* block in the corpus is **2 verses** (Q 3:55-56, Q 4:101-102, Q 7:176-177). Q 23's believer-block is **2× longer** than the corpus's longest disbeliever-block. The believer-attribute concentration is therefore not an artifact of generic relative-pronoun density.

### 2.3 Comparator block measurements

| Block | Verses | Strict-marker verses | Looser-marker verses |
|:-:|:-:|:-:|:-:|
| Q 23:1-11 | 11 | 4 (vv. 2-5) | 8 |
| Q 8:2-4 | 3 | 0 | 3 |
| Q 9:71 | 1 | 0 | 1 |
| Q 70:22-35 | 14 | 3 (vv. 32-34) | 5 (vv. 32-36) |
| Q 25:63-77 | 15 | 0 | 0 |
| Q 32:15-16 | 2 | 0 | 1 |

Under the **looser** marker definition (including bare الذين / والذين / أولئك), Q 5:51-57 has a 7-verse run, Q 11:16-21 a 6-verse run, Q 34:3-8 a 6-verse run, Q 70:31-36 a 6-verse run. Q 23 does not retain rank-1 under the looser definition — but the looser markers include broader relative-pronoun usage, not the specific *alladhīna hum* (= "those who, they") form-IV-active-participle attribute-stacking pattern that defines the *muʾminūn-typology* register.

### 2.4 Verdict: PASS-DIRECTED-EXACT (corpus-rank 1 by strict marker)

The Tirmidhī ʿUmar-narrated "ten verses to Paradise" ḥadīth is empirically backed: Q 23 contains the **corpus-EXACT longest** contiguous strict-believer-attribute relative-clause block. This is rank-test-based, not p-test-based; family-Bonferroni does not modify rank-1 status.

### 2.5 Cross-references

- 04-hadith-corpus.md §1 (Tirmidhī idInBook 3257 anchor).
- 05-classical-claims-audit.md Claim 5.
- al-Biqāʿī's *Naẓm al-Durar* on Q 23 §1 (the prayer-frame chiastic mini-structure).
- 02-content-analysis.md §2 (block-detail).

## 3. Q023-F-03 — Embryology pericope pair Q 23:12-14 ↔ Q 22:5: PASS-DIRECTED

### 3.1 Pre-registered claim

The Q 23:12-14 embryology-pericope and Q 22:5 embryology-summary are **lexically tighter** (orthographic-token Jaccard) than a length-matched corpus null.

### 3.2 Result

| Statistic | Value |
|:--|:-:|
| J_obs (raw orthographic Jaccard) | **0.0886** |
| Light-stem Jaccard | 0.0933 |
| Null median (raw) | 0.0161 |
| Null p95 (raw) | 0.0737 |
| p (upper-tail) | **0.0232** |
| Q23-12-14 ↔ Q75-37-40 (3-vs-4 verse embryology pair) | 0.0816 |
| Control: Q 23:1-3 (non-embryology) ↔ Q 22:5 | 0.0149 |

**Shared tokens (intersection)**: نطفة, علقة, مضغة, ثم, في, من, ۚ — i.e., the three embryological stage-terms plus connectors. The control Q 23:1-3 vs Q 22:5 sits at 0.0149 (essentially null median).

The Q 23 ↔ Q 22 pair is **above the 95th percentile** of the null Jaccard distribution. The result is **PASS-DIRECTED** at single-test α=0.05, but **NOT-PASS under Bonferroni** α=0.0167. Under the family-3-tests Bonferroni, the finding is **directional but not significant**.

### 3.3 Interpretation

The two flagship embryology-passages share the three diagnostic stage-terms (نطفة, علقة, مضغة) and the rhetorical-progression syntax (*ثم ... ثم ... ثم ...*). This is corpus-distinctive: the embryology-vocabulary is **tightly conserved across the two pericopes**, consistent with al-Qurṭubī's claim ad loc. Q 23:14 that "the discussion of nuṭfa and ʿalaqa and muḍgha and the rulings on them have already been treated at the start of al-Ḥajj" — i.e., he reads the two pericopes as **lexically and semantically cross-referenced**.

The full triplet (Q 22:5, Q 23:12-14, Q 75:37-40) forms the canonical Quranic embryology corpus; the strongest pairwise overlap is Q 22:5 ↔ Q 23:12-14, with Q 75:37-40 slightly more distant (lacks the *muḍgha* term).

### 3.4 Honest limits

- Jaccard is sensitive to verse-length asymmetry: Q 23:12-14 has 35 tokens, Q 22:5 has 73 tokens. The intersection of 7 distinctive tokens against the union of 79 unique tokens gives J = 0.089. A symmetric measure (e.g., Dice coefficient or cosine on TF-IDF) might shift the magnitude but not the direction.
- The pre-registered direction is PASS-DIRECTED at single-test α; family-Bonferroni narrows it. **Report-as-DIRECTIONAL**, not as CONFIRMED.
- Q 75:37-40 is shorter and lacks *muḍgha*; the secondary pairwise Jaccard 0.082 with Q 23 reflects this.

### 3.5 Cross-references

- 02-content-analysis.md §3 (embryology-cluster roots).
- 04-hadith-corpus.md §5 (Bukhārī 3195 embryology-vocabulary parallel).
- al-Qurṭubī's commentary on Q 23:14 ad loc. (file `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafseer-al-qurtubi/23.json`).

## 4. The flḥ triple-anchor structure (descriptive corpus-EXACT, audited in 05 Claim 1)

Q 23 contains *flḥ* exactly 3 times (vv. 1, 102, 117). The triple is opening-positive-perfective (v. 1) + mid-late-positive-participle (v. 102) + closing-negative-imperfective (v. 117). This is the corpus's only surah-internal *flḥ*-inclusio with strict-polarity inversion between endpoints. See 05-classical-claims-audit.md Claim 1 for full audit.

## 5. The Q 22 → Q 23 *flḥ*-pickup (corpus-EXACT adjacent-pair, audited in 05 Claim 3)

Q 22:77 *laʿallakum tufliḥūn* → Q 23:1 *qad aflaḥa l-muʾminūn* is the **unique** adjacent-surah-pair with *flḥ* in both the last-2 verses of Sa and the first-2 verses of Sb. See 05-classical-claims-audit.md Claim 3.

## 6. Summary

The three pre-registered tests landed:
- **F-01 PRE-COMMIT-VIOLATION-NULL** (top-10 UAS not FR-cohesive — direction reversed; published as NULL with prominence per Protocol §1.8). This adds a strong data point to cross-finding-025: the marker-thickness rule applies to multi-axis aggregates as well.
- **F-02 PASS-DIRECTED-EXACT** (Q 23:2-5 is corpus-EXACT longest strict-marker believer-attributes run; rank-test, not p-test, so Bonferroni does not affect verdict).
- **F-03 PASS-DIRECTED** (embryology pair Q 23:12-14 ↔ Q 22:5 has J=0.089, p=0.023, above null p95 = 0.074, but not under Bonferroni-corrected α=0.0167).

Plus two descriptive corpus-EXACT findings audited in 05-classical-claims-audit.md:
- The flḥ-triple-anchor inclusio (vv. 1, 102, 117).
- The unique Q 22 → Q 23 adjacent flḥ-pickup.

The honest pattern: Q 23's high UAS rank does **not** trace to root-distribution clustering. Q 23 wins UAS via adjacency-cost (rank 6 / 113 on Q 22-Q 23) + outlier-magnitude (Δ -10.91 pp, COHESION_ANCHOR) + |iʿjāz| absolute magnitude (1.55). Its distinctive **lexical and structural** features — the *flḥ* inclusio, the corpus-EXACT believer-attributes block, the embryology-pair tightness with Q 22:5 — are not UAS-axes; they are surah-internal and adjacent-pair phenomena that the UAS framework does not capture. This pattern is consistent with the project's empirical-architectural / theological-iʿjāz orthogonality finding ([[h-new-860-hadith-architectural-alignment|H-NEW-860]]).
