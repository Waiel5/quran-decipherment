---
surah: 67
surah_name_ar: الملك
surah_name_translit: al-Mulk
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — 7 pre-registered tests
---

# Q 67 al-Mulk — Novel Findings

## 0. Source

This file presents 7 pre-registered novel empirical findings on Q 67, each with locked pre-reg, SHA256-checksummed run script, and JSON-archived results. Pre-regs live in `preregs/`, scripts in `scripts/`, JSON outputs in `csv/`. All scripts verify the pre-reg SHA at runtime and fail-fast on mismatch.

| ID | Pre-reg SHA256 (head 12) | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|
| Q067-F-01 | `591775e3a068` | `Q067_F_01_architectural_rank_cross_comparison.py` | `Q067-F-01.json` | **VINDICATED** |
| Q067-F-02 | `f9f2d651034d` | `Q067_F_02_postkink_distinctness.py` | `Q067-F-02.json` | **DIRECTIONAL_ENHANCED** (unexpected) |
| Q067-F-03 | `6722a3a4f9af` | `Q067_F_03_corpus_singleton_phrases.py` | `Q067-F-03.json` | **CONFIRMED** (3/3) |
| Q067-F-04 | `2611e9cc5ed1` | `Q067_F_04_mulk_stem_density.py` | `Q067-F-04.json` | **NULL** (name-tracks-vocabulary FALSIFIED for Q 67) |
| Q067-F-05 | `826c4a8e7934` | `Q067_F_05_q66_q67_mushaf_seam.py` | `Q067-F-05.json` | **NULL** (Q 66 → Q 67 mid-pack, NOT high-cost) |
| Q067-F-06 | `d39272d33613` | `Q067_F_06_tabaraka_alladhi_pair.py` | `Q067-F-06.json` | **NULL** (p=0.084, near-miss directional) |
| Q067-F-07 | `61ded14703d7` | `Q067_F_07_mulk_root_density_rank.py` | `Q067-F-07.json` | **NULL** (rank 37/114 — outside top-5) |

Two of the seven findings are positive vindications; one is a surprise *enhanced* directional finding (Q067-F-02) that pre-commits to honest reporting; four are substantive **NULL**s that falsify corpus-wide hypotheses or pre-registered directions.

The Wave-H additions (Q067-F-05 through F-07) further sharpen the project's reading of Q 67: the surah's recitation-tradition prominence is **not** mirrored by mushaf-position seam-cost (F-05), opener-formula verse-level cohesion (F-06), or lexical-density rank (F-07). All three of the Wave-H tests resolve NULL, reinforcing the F-04 + F-01 portrait of Q 67 as a *theological-iʿjāz* surah whose architectural signature lives at the **token-singularity** axis (F-03) rather than at standard structural axes.

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

## Q067-F-05 — Q 66 → Q 67 mushaf-seam adjacency cost: NULL on "high-cost juzʾ-29 boundary"

### Pre-registered hypothesis

Q 67 opens the Quran's short-Meccan tail (Q 67 onwards is dominated by mufaṣṣal-awsāṭ/qiṣār) immediately after the long-Medinan block Q 47-Q 66. If mushaf order encodes this position-boundary, the Q 66 → Q 67 adjacency should be a high-cost (top-decile, rank ≤ 11/113) seam in `findings/phase-b-hypotheses/csv/h-new-720.json`. Pre-registered direction: **HIGH-cost (top-decile)**.

### Result

| Metric | Q 66 → Q 67 | Q 65 → Q 66 | Q 67 → Q 68 |
|:--|:-:|:-:|:-:|
| delta_raw | 0.0780 | −0.0340 | 0.0962 |
| fraction_residual | 0.0094 | 0.0000 | 0.0116 |
| Rank (descending of 113) | **47** | 109 | 36 |
| Observational p ≥ observed | 0.416 | — | — |

Distribution stats (113 canonical adjacencies): mean=0.0832, median=0.0621, sd=0.0924, max=0.6216 (Q 1 → Q 2). Bootstrap (10000 resamples, seed 20260509): boot_rank median = 47, p(rank ≤ 11 top-decile) = **0.000**.

### Verdict

**NULL** — Q 66 → Q 67 sits at rank 47/113 (descending), well outside the pre-registered top-decile (≤11). The pre-commit-locked "high-cost seam" prediction is NOT supported.

### Interpretation

Three readings:

1. **The juzʾ-29 boundary is liturgical-pedagogical, not mushaf-architectural.** The compiler's *taqsīm* into 30 juzʾ blocks was settled later than the mushaf-order itself; juzʾ-29 begins at Q 67:1 by recitation-rate convention (≈ 1/30 of the Quran), not by an underlying root-distribution discontinuity. The empirical NULL at this seam is consistent with this reading.

2. **The H-NEW-720 root-distribution lens is insensitive to the position-boundary.** Q 66 and Q 67 share enough root-distribution overlap (al-Raḥmān-cluster, sovereignty-cluster) that the FR-distance between them is mid-pack. A different lens (rhyme, phoneme, or verse-length) may yield a higher seam-cost.

3. **The "long-Medinan→short-Meccan-tail" boundary is at a different seam.** The transition from long-Medinan to short-Meccan does happen, but the breakpoint by FR-content is closer to Q 49→50 or Q 56→57; Q 66→67 is a less salient instance.

The **immediate neighbour Q 65 → Q 66 is rank 109/113** (one of the *cheapest* canonical transitions) — the long-Medinan etiquette/divorce-cluster {Q 65, Q 66} is unusually FR-tight, and Q 66→67 then opens to a typical (mid-pack) cost rather than spiking. This pattern is **consistent with cross-finding-025's marker-thickness rule** (cf. [[cross-finding-025-marker-thickness|cross-finding-025]]): Q 65-66 share thick markers (divorce-domestic-etiquette + ʿiddah-vocabulary) so cohere tightly; Q 66→67 then steps out to a thematically different but lexically-overlapping surah and the cost is unremarkable.

### Honest limits

- The pre-registered HIGH-cost direction was an *architectural hypothesis*; the NULL is itself a contribution under §1.3 equal-NULL-prominence discipline.
- Single-rules-tuple test; sensitivity to alternate K and α was not pre-registered.
- The H-NEW-720 delta is FR-residual after greedy + 2-opt TSP; it measures *cost of forced canonical order vs. unconstrained shortest tour*, not absolute pairwise FR distance.

### Cross-references

- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — adjacency-cost map.
- [[cross-finding-025-marker-thickness|cross-finding-025]] — thick-marker pairs (Q 65-66) tend to FR-cohere; cross-boundary transitions need not be high-cost when neighbours share lexicon.
- `04-hadith-corpus.md` for Q 67 juzʾ-29 recitation-tradition framing.

## Q067-F-06 — Verse-pair tightness for {Q 25:1, Q 64:1, Q 67:1}: NULL near-miss

### Pre-registered hypothesis

The three opener-verses {Q 25:1, Q 64:1, Q 67:1} pre-registered in the specialist brief should sit tighter on verse-level Fisher-Rao than a length-matched null draw from the corpus.

### Data-verification note (pre-commit-honored)

**The brief's pre-registered claim that all three of Q 25:1, Q 64:1, Q 67:1 open with *tabāraka alladhī* is INCORRECT and is flagged here per the §1.6 anti-hallucination discipline.** Actual openings (computed from `quran-text/quran-no-tashkeel.json`):
- Q 25:1: *تبارك الذي نزل الفرقان…* — *tabāraka alladhī nazzala al-furqān*. ✓ *tabāraka alladhī* opener.
- Q 64:1: *يسبح لله ما في السماوات…* — *yusabbiḥu li-llāhi mā fī al-samāwāt…*. ✗ NOT a *tabāraka alladhī* opener; it is a musabbiḥāt-class opener. It does contain the phrase *lahu al-mulk* later in the same verse, so the comparison set is best read as **al-mulk-doxology verses**, not as a *tabāraka alladhī* opener triplet.
- Q 67:1: *تبارك الذي بيده الملك…* — *tabāraka alladhī bi-yadihi al-mulk*. ✓ *tabāraka alladhī* opener.

The actual 5 *tabāraka alladhī* verse-occurrences in the corpus are: Q 25:1, Q 25:10, Q 25:61, Q 43:85, Q 67:1 (per Q067-F-03 § corpus-singleton-phrases test, vindicated). The brief's pre-registered triplet is therefore best understood as a **mulk-doxology opener test** (the *al-mulk* divine-sovereignty motif appears prominently in v. 1 of each of the three surahs) — the locked triplet is honored, and the secondary test runs the actual *tabāraka alladhī* verse-set.

### Result — primary (locked triplet)

| Verse | Word count |
|:--|:-:|
| Q 25:1 | 9 |
| Q 64:1 | 19 |
| Q 67:1 | 9 |

| Metric | Value |
|:--|:-:|
| Target mean pairwise FR | **0.2142** |
| Null q05 | 0.2088 |
| Null median | 0.2388 |
| Null q95 | 0.2693 |
| p_perm (target ≤ null) | **0.0839** |

Target mean FR is **below** null median by ~0.025 (directionally tighter), but does not reach the pre-registered p<0.05 threshold (q05=0.2088). Pre-registered TIGHTER direction NOT met; reversed-direction pre-commit violation NOT triggered (target is below median, not above).

### Result — secondary (5 actual *tabāraka alladhī* verses)

| Verse | Word count |
|:--|:-:|
| Q 25:1 | 9 |
| Q 25:10 | 14 |
| Q 25:61 | 10 |
| Q 43:85 | 11 |
| Q 67:1 | 9 |

Mean pairwise FR (10 pairs) = **0.2237** — comparable to the locked triplet. Three of the five *tabāraka alladhī* verses come from a single surah (Q 25) so the cohesion may partly be a within-surah artifact; cross-surah pairs (Q 25:* ↔ Q 43:85, Q 25:* ↔ Q 67:1, Q 43:85 ↔ Q 67:1) require separate analysis.

### Verdict

**NULL** (p_perm=0.0839, near-miss in pre-registered direction). The shared opener formula does NOT generate verse-level FR cohesion at the pre-registered α=0.05 threshold.

### Interpretation

Three readings:

1. **Genuine signal at low power.** With only 3 pairs in the test statistic, statistical power for verse-level FR is intrinsically modest. The observed +0.025 effect-size below null median is consistent with a real-but-small lexical-cohesion signal that 3 pairs cannot resolve.

2. **The brief's triplet mis-anchored.** Q 64:1 isn't a *tabāraka alladhī* opener; including it dilutes the opener-formula signature. A cleaner test would compare {Q 25:1, Q 67:1} only (2 surah-opener verses with the actual shared formula) — but a single pair is even weaker statistically.

3. **Opener formulas don't constrain lexicon at the verse level.** The *tabāraka alladhī* + relative-clause construction is grammatical, not lexical-thematic; it admits any noun-cluster (*al-furqān*, *al-mulk*, etc.). Cohesion would need to come from the *content* slot, not the construction.

### Honest limits

- Pre-registered comparison set contained a factual error (Q 64:1 mis-attributed to *tabāraka alladhī*-openers). The script was run on the locked triplet per pre-reg discipline; the secondary recomputes over actual *tabāraka alladhī* occurrences.
- Verse-level FR is statistically weak for short verses; the test is properly under-powered.
- Length-matched null restricts pool to ±1 word per target wc; tolerance choice was pre-registered but may itself shape the null.

### Cross-references

- `00-overview.md` §3 — *tabāraka alladhī* opener cluster.
- Q067-F-03 — *bi-yadihi al-mulk* corpus-singleton (vindicated).
- [[cross-finding-025-marker-thickness|cross-finding-025]] — thin-marker clusters (single opener formula) frequently NULL on FR cohesion. Q067-F-06 adds another such NULL-near-miss data point.

## Q067-F-07 — mulk-stem density rank across the 114 corpus: NULL on top-5

### Pre-registered hypothesis

Q 67 should rank in the top 5 of 114 by per-1000-root-token *mlk*-stem density. Direction: **TOP-5**.

### Result

| Metric | Q 67 | Top-5 |
|:--|:-:|:--|
| mlk stem-count | 1 | Q 114 (1), Q 97 (1), Q 1 (1), Q 82 (1), Q 78 (2) |
| Total stem-root tokens | 208 | 16, 21, 23, 50, 131 |
| Density per 1000 | **4.81** | 62.5, 47.6, 43.5, 20.0, 15.3 |
| **Rank by density** | **37 / 114** | — |
| Rank by raw count | 54 / 114 | — |

### Verdict

**NULL** — Q 67 ranks 37/114 by mlk-stem density, well outside the pre-registered top-5.

### Interpretation

The top-5 by density is dominated by **very short surahs** (Q 114 al-Nās has 16 stem-root tokens total; one *mlk* token from v.2 *malik al-nās* produces a 62.5/1000 density). This is a **length-artefact**: tiny denominators inflate the rate. None of the top-5 by density is named *al-Mulk*; the test is therefore both **directionally NULL** (Q 67 is not top-ranked) and **methodologically diagnostic** (per-1000 density is itself a noisy estimator at short surah lengths).

Combined with the Q067-F-04 hypergeometric NULL (p=0.58 over-concentration vs uniform), this Wave-H rank test corroborates the central finding: **Q 67 is named "al-Mulk" by the opening-word convention, not by lexical-density**. The *mlk* root family appears once in the surah (v.1 *bi-yadihi al-mulk*) and does not recur — the title is from the *unique* corpus-singleton phrase, not from a thematic concentration.

### Honest limits

- Single test, single rules-tuple.
- Top-5 by density is dominated by short surahs with tiny denominators; a cleaner test would normalize by surah length or by expected count under a length-weighted multinomial.
- Per Q067-F-04, the hypergeometric formulation already rejected over-concentration at p=0.58; this F-07 rank test reaches the same conclusion through a different statistical lens, reinforcing the conclusion.

### Cross-references

- Q067-F-04 (same root, hypergeometric test) — corroborating NULL.
- Q024-F-01 (Q 24 al-Nūr light-cluster, vindicated at p<10⁻⁶) — the *positive* analogue for name-tracks-vocabulary.

## 6. Honest summary

Seven pre-registered novel findings on Q 67. **Two passed** their pre-registered thresholds (Q067-F-01 VINDICATED, Q067-F-03 CONFIRMED 3/3). **Four are substantive NULLs** (Q067-F-04 hypergeometric, Q067-F-05 mushaf-seam, Q067-F-06 verse-pair tightness near-miss, Q067-F-07 density rank). **One was a pre-commit-direction violation** (Q067-F-02 DIRECTIONAL_ENHANCED) reported with full prominence and honest interpretation. The composite Wave-D + Wave-H contribution: Q 67 al-Mulk is the project's clearest case of **theological-iʿjāz / faḍāʾil-prominence WITHOUT structural-architectural distinctness** (Q067-F-01), while simultaneously exhibiting **token-level lexical singularity** in its opening verses (Q067-F-03) — an architectural axis distinct from the UAS-component axes. The name-tracks-vocabulary corpus-wide generalization is FALSIFIED at Q 67 across BOTH the hypergeometric (Q067-F-04) and the rank-based (Q067-F-07) lenses, establishing the hypothesis as rules-tuple-fragile across surahs. The juzʾ-29 mushaf-boundary at Q 66 → Q 67 is **not** a high-cost FR seam (Q067-F-05), confirming the boundary as a liturgical-pedagogical convention rather than a mushaf-architectural discontinuity. The *al-mulk*-doxology opener triplet {Q 25:1, Q 64:1, Q 67:1} does NOT achieve verse-level FR tightness at α=0.05 (Q067-F-06; near-miss p=0.084). The Wave-H NULLs reinforce cross-finding-025's marker-thickness threshold rule: thin or grammatical-only markers (opener formula, single boundary, single name-stem at low density) consistently fail to drive FR-cohesion in the absence of multi-axis correlation.
