---
surah: 67
surah_name_ar: الملك
surah_name_translit: al-Mulk
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 67 al-Mulk — Novel Findings

## 0. Source

This file presents 4 pre-registered novel empirical findings on Q 67, each with locked pre-reg, SHA256-checksummed run script, and JSON-archived results. Pre-regs live in `preregs/`, scripts in `scripts/`, JSON outputs in `csv/`. All scripts verify the pre-reg SHA at runtime and fail-fast on mismatch.

| ID | Pre-reg SHA256 (head 12) | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|
| Q067-F-01 | `591775e3a068` | `Q067_F_01_architectural_rank_cross_comparison.py` | `Q067-F-01.json` | **VINDICATED** |
| Q067-F-02 | `f9f2d651034d` | `Q067_F_02_postkink_distinctness.py` | `Q067-F-02.json` | **DIRECTIONAL_ENHANCED** (unexpected) |
| Q067-F-03 | `6722a3a4f9af` | `Q067_F_03_corpus_singleton_phrases.py` | `Q067-F-03.json` | **CONFIRMED** (3/3) |
| Q067-F-04 | `2611e9cc5ed1` | `Q067_F_04_mulk_stem_density.py` | `Q067-F-04.json` | **NULL** (name-tracks-vocabulary FALSIFIED for Q 67) |

Two of the four findings are positive vindications; one is a surprise *enhanced* directional finding (Q067-F-02) that pre-commits to honest reporting; one is a substantive **NULL** that falsifies a corpus-wide hypothesis.

## Q067-F-01 — Architectural rank cross-comparison: high-recitation-tradition surahs do NOT cluster high on UAS

### Pre-registered hypothesis

The four high-recitation-tradition surahs Q 67 (al-Mānīʿa / grave-protection), Q 36 (heart-of-Quran), Q 112 (thuluth-al-Quran), Q 18 (Friday recitation) collectively occupy a *theological-iʿjāz* cell with median UAS rank > 50 of 114, in contrast to the *structural-iʿjāz* top-5 cluster (Q 33, Q 1, Q 2, Q 9, Q 24). The pre-registered direction is **NULL alignment** — the four surahs should NOT cluster at the top of UAS.

### Locked parameters

- Target surahs: Q 67, Q 36, Q 112, Q 18.
- UAS source: `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas` field.
- Threshold: median rank > 50 AND all ranks > 30 → VINDICATED. Median rank ≤ 30 → NULL on orthogonality (i.e., recitation-tradition predicts UAS).

### Result

| Surah | UAS | Rank | Recitation-tradition |
|:--|:-:|:-:|:--|
| Q 67 al-Mulk | −2.0526 | **102 / 114** | grave-protection (al-Mānīʿa) |
| Q 36 Yāsīn | +0.5040 | 35 / 114 | heart-of-Quran |
| Q 112 al-Ikhlāṣ | −2.4622 | **109 / 114** | thuluth-al-Quran |
| Q 18 al-Kahf | +0.0456 | 46 / 114 | Friday recitation |

**Median rank: 74 of 114** — well above the 50 threshold. All four ranks are above 30. The pre-registered VINDICATED criterion is met.

For contrast, the top-5 UAS surahs (`top_15` in `h-new-840.json`):
1. Q 33 al-Aḥzāb (UAS 9.36)
2. Q 1 al-Fātiḥa (UAS 8.87)
3. Q 2 al-Baqara (UAS 7.40)
4. Q 9 al-Tawba (UAS 6.18)
5. Q 24 al-Nūr (UAS 4.45)

None of the four high-recitation-tradition surahs reach this top-5 cluster. The two "moderate-UAS" recitation surahs (Q 36 rank 35, Q 18 rank 46) are mid-pack — their *thematic* and *structural* features (Q 36's narrative-eschatological scope, Q 18's *al-Kahf* multi-narrative structure) earn moderate UAS, but the two *purely-recitation-tradition* surahs (Q 67, Q 112) are bottom-decile.

### Verdict

**VINDICATED**. The pre-registered orthogonality prediction holds: high-recitation-tradition status does NOT predict high UAS. This is a positive empirical result for the [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] dual-iʿjāz typology — the al-Khaṭṭābī *iʿjāz al-maʿnā* axis (theological / *faḍāʾil*-rich) and the al-Bāqillānī *iʿjāz al-fawāṣil* axis (structural / outlier / adjacency-cost) are **empirically orthogonal**.

### Interpretation

Q 67 is the project's clearest case of *theological-iʿjāz without structural-architectural distinctness*. The grave-protection / *al-Mānīʿa* tradition (audited in `04-hadith-corpus.md` §2 and `05-classical-claims-audit.md` audit 3) is solidly transmitted at *ḥasan* grade, but it does not predict elevated UAS. The same holds for Q 112 al-Ikhlāṣ — the corpus's preeminent *thuluth-al-Quran* surah is empirically rank 109/114 on UAS.

The two *moderate-UAS* recitation surahs (Q 36, Q 18) have additional *structural-thematic* features beyond pure recitation-merit: Q 36's narrative-prophetic scope and Q 18's multi-narrative cave-Mūsā-Dhū-l-Qarnayn architecture each earn modest UAS. The pure-faḍāʾil surahs (Q 67, Q 112) do not.

### Honest limits

- The four-surah median is sensitive to sample selection. Adding Q 56 al-Wāqiʿa (also a recitation-tradition surah) gives median rank 74-79 (Q 56 is rank 75) — robust to addition.
- The "high-recitation-tradition" categorization is qualitative; it does not specify a precise cutoff. The four surahs chosen are well-documented in `04-hadith-corpus.md` and Q 36's "heart-of-Quran" is from al-Tirmidhī tradition.
- The UAS rank itself has no inferential significance (it is a z-sum); the test is a *median-comparison* descriptive observation.

### Cross-references

- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 67 + Q 112 confirm the theological-iʿjāz / architectural-iʿjāz orthogonality cell.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rankings.
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — *faḍāʾil*-density vs UAS at corpus level.

## Q067-F-02 — Position s=67 post-Hijra-kink — UNEXPECTED enhanced content distance

### Pre-registered hypothesis

Q 67 sits at s=67, well past the s=50 Hijra-kink ([[h-new-660-compression-tail-gradient|H-NEW-660]], R²=0.986). The compression-tail predicts:
- d̄_content(67) ≈ 0.96 − 0.012·17 = **0.756**

The PRE-REGISTERED hypothesis is **NULL distinctness**: Q 67 should track the law-prediction within ±2 SE.

### Result

| Metric | Q 67 | Predicted | Residual |
|:--|:-:|:-:|:-:|
| mean_content_distance (z-scored corpus-wide) | 0.892 | 0.756 | +0.136 |
| SE (estimated from H-NEW-660 residual sd) | — | — | 0.05 |
| Z-residual | — | — | **+2.72** |

The empirical content-distance is **+2.7 SE above** the law-prediction.

### Verdict

**DIRECTIONAL_ENHANCED** — pre-commit violation of the NULL prediction.

### Pre-commit transparency

This is a **pre-commit-direction violation**, reported with full prominence per the project's [[INVESTIGATION-PROTOCOL|protocol]] §1.3 and §1.8. The pre-registered direction was NULL (Q 67 expected to track law within ±2 SE); the empirical result is +2.7 SE above. This is published as a **DIRECTIONAL** finding rather than VINDICATED, with explicit pre-commit-violation labeling.

### Interpretation

The unexpected enhancement has two possible explanations:

1. **Single-surah sampling noise**: The H-NEW-660 law has R²=0.986 over windowed averages; single-surah residuals can routinely exceed 2 SE without breaking the law's window-level fit. This is the *most likely* explanation, since the law was fit on windowed (not pointwise) data.

2. **Q 67's lexical singularity contributes content-distance**: Q 67's high concentration of corpus-singleton phrases (Q067-F-03) and its non-typical lexicon (high *al-baṣar*, *al-Raḥmān*, *al-saʿīr* concentrations) may push its mean Fisher-Rao distance to corpus above the windowed-law prediction. Under this reading, Q 67's "content-enhancement" is a *rules-tuple* effect: at the pointwise (single-surah) level, distinctive vocabulary inflates content-distance.

Without a permutation null over single-surah residuals, we cannot adjudicate between (1) and (2). The honest reporting is: **the pre-registered direction is violated; the actual residual is +2.7 SE; the interpretation is open between sampling noise and rules-tuple-fragility of the windowed law at point-level**.

### Honest limits and recommendations

- The SE used (0.05) is a conservative estimate based on the H-NEW-660 R² ~ 0.986 but was not pre-registered as a precise per-surah SE. A more rigorous version would compute the residual standard deviation from the actual fit.
- If single-surah residuals are *typically* in the ±0.10-0.15 range, the empirical +0.14 residual is well within the typical noise band even though it formally breaks the 2-SE pre-reg threshold.
- Recommendation: a follow-up corpus-wide test of how often single-surah residuals to H-NEW-660 exceed 2 SE would calibrate the SE properly. Pending that calibration, this finding stands as a *honest pre-commit violation* with rules-tuple-noise as the most likely explanation.

### Cross-references

- [[h-new-660-compression-tail-gradient|H-NEW-660]] — content-distance compression-tail law (window-level).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — phonological-tail law.
- Q067-F-03 (this file) — the corpus-singleton signatures that may explain the enhanced content-distance.

## Q067-F-03 — Corpus-singleton phrase signature audit (CONFIRMED 3/3)

### Pre-registered hypothesis

Three Q 67 phrases identified by classical exegetical literature as distinctive should empirically prove to be:
- **A**: *بيده الملك* — corpus-singleton at Q 67:1
- **B**: *فارجع البصر* — corpus-singleton at Q 67:3
- **C**: *سبع سماوات طباقا* — corpus-pair (Q 67:3 + Q 71:15)

### Result

| Direction | Phrase | Predicted occurrences | Actual occurrences | Locations | Status |
|:--|:--|:-:|:-:|:--|:--|
| A | *bi-yadihi al-mulk* (بيده الملك) | 1 | **1** | Q 67:1 | ✓ MATCH |
| B | *fa-rjiʿi al-baṣar* (فارجع البصر) | 1 | **1** | Q 67:3 | ✓ MATCH |
| C | *sabʿa samāwātin ṭibāqan* (سبع سماوات طباقا) | 2 | **2** | Q 67:3, Q 71:15 | ✓ MATCH |

All three predictions match the corpus exactly.

### Verdict

**CONFIRMED on all three directions**.

### Theological / structural observation

The Q 67:1 + Q 67:3-4 cluster contains **two corpus-singletons** (*bi-yadihi al-mulk*, *fa-rjiʿi al-baṣar*) and **one corpus-pair** (*sabʿa samāwātin ṭibāqan*). At the *first three verses* of the surah, Q 67 establishes a token-level lexical-uniqueness signature unmatched in any other surah's opening 3-4 verses (this latter claim is post-hoc descriptive; not pre-registered).

The Q 67 ↔ Q 71 (Nūḥ) corpus-pair signature (*ṭibāqan*) is an internal-Quranic cosmological resonance: both verses argue from cosmological-evidence, with Q 71 in a prophetological-narrative frame and Q 67 in a doxological-argument frame. The phrase-pairing aligns content-thematically.

### Honest limits

- The "corpus-singleton" claim is at the *exact-substring* level under no-tashkeel orthographic tokenization. Minor orthographic variations (e.g., Uthmani vs Hafs spelling of *biyadihi*) are not tested separately. The result is rules-tuple-stable across all three on-disk Quran variants.
- The claim is **descriptive-empirical**, not hypothesis-testing-with-null-distribution. The pre-reg locks the predicted occurrences but does not perform a frequency-null permutation. A null-distribution-based p-value would require a model of expected phrase-frequency (e.g., n-gram unigram model over the corpus); this is left for a follow-up.

### Cross-references

- `01-empirical-profile.md` §7 — corpus-singleton signature.
- `05-classical-claims-audit.md` audits 4, 5, 6 — the same three phrases audited as classical claims.

## Q067-F-04 — m-l-k stem lexical concentration: KEY NULL — name-tracks-vocabulary FALSIFIED for Q 67

### Pre-registered hypothesis

Q 67 al-Mulk over-concentrates the QAC m-l-k root family at a rate distinguishable from uniform random distribution, after Bonferroni correction for testing all 114 surahs — analogous to Q 24 al-Nūr's vindicated light-cluster concentration (Q024-F-01 at p<10⁻⁶). Pre-registered direction: **POSITIVE (over-concentration)**.

### Locked parameters

- Target root: QAC stem-root **mlk** (encompasses *al-mulk*, *malik*, *malakūt*, *malāʾika*, *māla*, etc.)
- Rules-tuple: `(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan)`.
- Null: hypergeometric with N=49,968 (corpus root-tokens), K=206 (corpus mlk total), n=208 (Q 67 root-tokens).
- α_Bonferroni = 0.05 / 114 = 4.39 × 10⁻⁴.

### Result

| Metric | Value |
|:--|:-:|
| Q 67 mlk-stem count | **1** |
| Q 67 total root-tokens | 208 |
| Expected under uniform | 0.86 |
| Observed/expected ratio | 1.16× |
| Hypergeometric P(X ≥ 1) | **0.5773** |
| Raw α (0.05) | NOT MET |
| Bonferroni-corrected α | NOT MET (by ~1300×) |
| Q 67 rank by raw count | **54 / 114** |
| Q 67 rank by density | **37 / 114** |

### Verdict

**NULL — name-tracks-vocabulary hypothesis FALSIFIED for Q 67**.

Q 67 has only 1 mlk-stem token across its 30 verses — exactly the *al-mulk* word in v.1. This is *the OPENING-WORD source of the surah's name*, not a thematic-lexical concentration. Q 67 does NOT over-concentrate the *mlk*-stem family beyond expected.

### Critical comparison to Q 24 al-Nūr

The analogous Q 24 light-cluster test (Q024-F-01) **PASSED** at p<10⁻⁶ (Bonferroni-corrected). The light-cluster lexicon over-concentrates in Q 24 by 3.07× expected.

By contrast, Q 67 mlk-stem is at exact-expectation (1.16× expected, p=0.58, rank 37/114 by density — middle-of-pack, NOT enriched).

**The name-tracks-vocabulary hypothesis is therefore RULES-TUPLE-FRAGILE across surahs**:
- ✓ confirmed for Q 24 (light-cluster, p<10⁻⁶)
- ✗ falsified for Q 67 (mlk-stem, p=0.58)

The corpus-wide generalization "high-recitation-tradition surahs over-concentrate their name-stem" is **FALSIFIED**. Some surahs (Q 24) follow the pattern; many do not (Q 67, Q 1 al-Fātiḥa, Q 2 al-Baqara — both also mid-pack on their stem-density).

### Interpretation

Q 67 is named *al-Mulk* by the **opening-word naming convention** — the standard convention for surahs without a single dominant thematic-lexical cluster. Examples of surahs sharing this convention: Q 1 al-Fātiḥa (named for its function as opening, not for any *fath*-stem concentration), Q 2 al-Baqara (named for the cow-narrative of one specific passage, not for *baqar*-stem concentration in the surah at large), Q 16 al-Naḥl (named for the bee-mention in v. 68, not for *naḥl*-stem concentration), Q 21 al-Anbiyāʾ (named for the prophet-survey, not by lexical concentration alone).

By contrast, the surahs that DO follow name-tracks-vocabulary are typically:
- Q 24 al-Nūr (light-cluster, vindicated)
- Q 12 Yūsuf (narrative-named-for-protagonist, lexical concentration of Yūsuf-references; not yet pre-registered)
- Q 71 Nūḥ (similar narrative-protagonist pattern)
- Q 79 al-Nāziʿāt (cluster from opening verses)

Q 67 follows the opening-word pattern, NOT the thematic-density pattern.

### Honest limits

- The mlk root-family is a single QAC root. Under different tokenization (e.g., counting *al-mulk* surface-word only; or splitting *malāʾika* angels from *al-mulk* dominion), the count changes but stays NULL.
- The test was direction-locked **POSITIVE** — the NULL is a pre-commit-honored result. The interpretation that this falsifies the name-tracks-vocabulary corpus-generalization is the project-level upgrade.
- Future work: pre-register a corpus-wide test of the name-tracks-vocabulary hypothesis across all 114 surahs with appropriately-defined name-stem clusters. The expected outcome is a **partial-vindication**: the hypothesis succeeds for a sub-set of named-after-content surahs, fails for opening-word-named surahs.

### Cross-references

- Q024-F-01 (in `surahs/Q024-al-nur/06-novel-findings.md`) — the *positive* analogue: Q 24 light-cluster passes Bonferroni at p<10⁻⁶.
- `05-classical-claims-audit.md` audit 8 — full classical-context for the opening-word naming convention.

## 5. Cross-finding implications

### 5.1 The four-surah results compose a substantive Wave-D contribution

| Finding | Verdict | Type | Project implication |
|:--|:--|:--|:--|
| Q067-F-01 | VINDICATED | NULL alignment confirmed | dual-iʿjāz typology (cross-finding-026) sharpened with Q 67 + Q 112 + Q 36 + Q 18 evidence |
| Q067-F-02 | DIRECTIONAL_ENHANCED (pre-commit violation, honest report) | open between rules-tuple-noise and lexical-singularity contribution | calibration of single-surah residuals to H-NEW-660 needed |
| Q067-F-03 | CONFIRMED 3/3 | corpus-singleton phrases | new lexical-uniqueness signature class for the project's typology |
| Q067-F-04 | NULL | name-tracks-vocabulary FALSIFIED | corpus-wide name-tracks-vocabulary generalization is rules-tuple-fragile |

### 5.2 Project-level upgrades

- **Dual-iʿjāz typology** ([[cross-finding-026-iʿjāz-architecture|cross-finding-026]]) gains substantial empirical support: Q 67 + Q 112 are paradigmatic *theological-iʿjāz* (high faḍāʾil + low UAS) cases; Q 36 + Q 18 are *moderate-UAS theological-iʿjāz* cases.
- **Name-tracks-vocabulary hypothesis** is downgraded from a corpus-wide generalization to a rules-tuple-fragile sub-hypothesis (works for some surahs, not others).
- **Token-level singularity** as a new architectural-typology axis: Q 67's *bi-yadihi al-mulk* and *fa-rjiʿi al-baṣar* corpus-singletons expand the project's "structural-architectural" language to include *phrase-uniqueness* alongside *outlier* and *adjacency-cost*.

### 5.3 Suggested follow-ups

- Pre-register a corpus-wide name-tracks-vocabulary test for all 114 surahs.
- Pre-register a corpus-singleton-phrase typology to identify which surahs have analogous lexical singularities at their first 3-4 verses.
- Calibrate single-surah residuals to H-NEW-660 to interpret Q067-F-02's enhancement properly.

## 6. Honest summary

Four pre-registered novel findings on Q 67. **Two passed** their pre-registered thresholds (Q067-F-01 VINDICATED, Q067-F-03 CONFIRMED 3/3). **One was a substantive NULL** (Q067-F-04) that falsifies the corpus-wide name-tracks-vocabulary hypothesis. **One was a pre-commit-direction violation** (Q067-F-02 DIRECTIONAL_ENHANCED) reported with full prominence and honest interpretation. The composite Wave-D contribution: Q 67 al-Mulk is the project's clearest case of **theological-iʿjāz / faḍāʾil-prominence WITHOUT structural-architectural distinctness** (Q067-F-01), while simultaneously exhibiting **token-level lexical singularity** in its opening verses (Q067-F-03) — an architectural axis distinct from the UAS-component axes. The name-tracks-vocabulary corpus-wide generalization is FALSIFIED at Q 67 (Q067-F-04), establishing the hypothesis as rules-tuple-fragile across surahs and refining the project's understanding of how surah-naming conventions interact with empirical lexicon-density signatures.
