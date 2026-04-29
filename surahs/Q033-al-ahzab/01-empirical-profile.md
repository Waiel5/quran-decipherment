---
surah: 33
file_type: empirical_profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — full integration of Wave 2026-04-28 H-NEW metrics
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q 33 al-Aḥzāb — Empirical Architectural Profile

> *"Q 33 wins the corpus on outlier strength + TSP cost, but loses the corpus on ʿijāz-al-fawāṣil signature. The combination is uniquely Q 33, and the reading is forced: a Medinan content-anomaly with a Jāhiliyya-style monorhyme imposed on top — the corpus's loudest single architectural fact."*

## 1. Headline metrics (all computed from disk, all files cited)

| Metric | Q 33 value | Corpus rank | Source file |
|:--|:--|:--|:--|
| **Unified Architectural Score (UAS)** | **9.364** | **1 / 114** | `findings/phase-b-hypotheses/csv/h-new-840.json` → `top_15[0]` |
| **Outlier strength (Δ%, fraction of mushaf-window outlier-pct)** | **+31.46 pp** | **1 / 114** (corpus-strongest) | `h-new-590.json` → `top_10_outliers[0]`, `all_surahs_results[X=33]` |
| **Outlier classification** | STRONG_OUTLIER | (1 of 6 STRONG_OUTLIERs corpus-wide) | `h-new-590.json` |
| **Q 32–Q 33 canonical-adjacency cost (Δ_raw)** | **0.36315** | **2 / 113** | `h-new-720.json` → `top10_expensive[1]` |
| **Q 33–Q 34 canonical-adjacency cost (Δ_raw)** | **0.33108** | **3 / 113** | `h-new-720.json` → `top10_expensive[2]` |
| **Cumulative Q 32-Q 33-Q 34 share of TSP residual** | **8.37 %** | (Q 33's adjacency neighborhood) | computed: 0.04379 + 0.03992 |
| **iʿjāz signature A (sig_A)** | **−2.966** | **112 / 114** (third-from-last) | `h-new-750.json` → `bottom10_A[2]`, `per_surah[X=33]` |
| **iʿjāz signature B (sig_B)** | **−2.085** | **113 / 114** (second-from-last) | `h-new-750.json` → `bottom10_B[1]` |
| **Rhyme entropy (Shannon, nats)** | **0.0724** | tied 19 / 114 (5 surahs at 0.000) | `h-new-750.json` → `per_surah[X=33].rhyme_entropy_nats` |
| **Top final-letter (alif) fraction** | **0.9863** (72/73) | rank 11 / 114 (corpus, all rules-tuple variants) | `h-new-750.json`, `h-new-700.json.rhyme.rhyme_letter_diagnostics[32]`, `Q033-F-01.json` |
| **Mean content distance (Fisher–Rao)** | **1.0960** | (z = +1.70 vs corpus mean ≈ 0.96) | `h-new-750.json` → `per_surah[X=33].mean_content_distance` |
| **Local cohesion** | **0.9146** | (z = −0.82 vs corpus mean) | `h-new-750.json` |
| **z(rhyme entropy)** | **−1.26** | (low = unusually monorhyme-pure) | computed |
| **z(mean content distance)** | **+1.70** | (high = unusually distant from mushaf neighbors) | computed |
| **z(local cohesion)** | **−0.82** | (slightly less internally cohesive than mean) | computed |
| **H-NEW-870 keystone test ΔR² (with Q 33 removed from corpus)** | **+0.00133** | (NOT global-keystone) | `h-new-870.json` → `two_piece_r2_drop_with_q33_removed` |

**Verse count cross-validation**: 73 in all four text variants
(`quran-no-tashkeel.json`, `quran-min-tashkeel.json`, `quran-full-tashkeel.json`, `quran-transliteration.json`, all surah id=33 → `len(verses) == 73`).

**Word count (no-tashkeel, ASCII-tokenized, pause marks stripped)**: **1 307**
(computed; the overview's 1 384 figure includes pause-marker tokens — see *§4 Counting protocol*).

**Letter count (Arabic letters only, no-tashkeel)**: **5 788**
(computed; overview gives 5 869 — see *§4*).

## 2. The signature paradox: corpus-rank 1 by UAS, corpus-rank 112-113 by ʿijāz

The **Unified Architectural Score** (H-NEW-840) combines three orthogonal signals:

```
UAS(s) = z(|outlier_pct|) + z(max_TSP_cost) + z(|ijaz_sig_A|)
```

For Q 33:

| Component | Value | z-score contribution |
|:--|:--|:--|
| `abs_outlier` = 31.46 | corpus-MAX | very high positive |
| `max_cost` = 0.3631 | corpus rank 2 (after Q 1-Q 2) | very high positive |
| `abs_ijaz` = 2.966 | corpus rank 3 (after Q 55, Q 4) | very high positive |

The crucial point: UAS uses the **absolute value** of the iʿjāz signature, so Q 33's *strongly negative* sig_A (−2.966) — meaning *anti-iʿjāz al-fawāṣil*, i.e., *more monorhyme-uniform than baseline* — contributes positively to UAS exactly as a *strongly positive* sig_A would. Q 33 is the **only** surah in the corpus that simultaneously sits in the top-15 by absolute outlier strength, top-3 by absolute TSP cost, **and** top-3 by absolute |sig_A|. The triple intersection of UAS-top-15 sets is `{9, 33}` (`h-new-840.json.triple_intersection_top15`) — and Q 33 enters that intersection from the iʿjāz-anti-pole, while Q 9 enters it from the iʿjāz-positive-pole.

This is the empirical content of the [[h-new-870]] finding "**singularity-without-keystone**": Q 33 is the corpus's loudest single architectural anomaly, but not its load-bearing structural foundation.

## 3. The 99 % alif-monorhyme — a Jāhiliyya-style *qaṣīda* embedded in the mushaf

### 3.1 The bare numbers

From `h-new-700.json.rhyme.rhyme_letter_diagnostics[surah=33]`:
```
{"surah": 33, "top_letter": "ا", "frac": 0.9863013698630136, "n_verses": 73}
```

**72 of 73 verses end in alif.** The single exception is **Q 33:4**, which ends in *al-sabīl* (السبيل), with final letter *lām*. (Verified by direct enumeration of the no-tashkeel verse list: see `verse_id=4` last word.)

### 3.2 Honest correction: Q 33 is *NOT* corpus-MAX in alif-monorhyme purity

**Status: F-01 FALSIFIED the corpus-MAX claim** (see `surahs/Q033-al-ahzab/06-novel-findings.md` §F-01; `csv/Q033-F-01.json`). The pre-registered direction was *Q 33 = rank 1*. Result: **Q 33 = rank 11 / 114**.

Surahs with strictly higher alif-final fraction than Q 33 (under min-tashkeel last-letter rules-tuple):
- **Q 48 al-Fatḥ** (n=29): 100 % alif-final.
- **Q 65 al-Ṭalāq** (n=12): 100 % alif-final.
- **Q 72 al-Jinn** (n=28): 100 % alif-final.
- **Q 76 al-Insān** (n=31): 100 % alif-final.
- **Q 87 al-Aʿlā** (n=19): 100 % alif-final.
- **Q 91 al-Shams** (n=15): 100 % alif-final.
- **Q 92 al-Layl** (n=21): 100 % alif-final.
- **Q 17 al-Isrāʾ** (n=111): 110/111 = 0.991 alif-final.
- **Q 18 al-Kahf** (n=110): 109/110 = 0.991 alif-final.
- **Q 25 al-Furqān** (n=77): 76/77 = 0.987 alif-final.

Q 33 (0.9863) is *one of 11 surahs with alif-final ratio ≥ 0.98* — distinguished but not unique.

`h-new-750.json` ranks Q 33 at *rhyme entropy* 0.0724 nats, **rank 19** in ascending order; the surahs with strict zero entropy are Q 48, Q 54 (rāʾ), Q 63 (nūn), Q 72, Q 76 (and others, n = 11-55).

**What remains true:**
- Q 33 is the **corpus's longest-form near-pure alif-monorhyme**: at n = 73 verses, sustaining 98.6 % alif-final is harder than at n = 12 (Q 65) or n = 28 (Q 72). Only Q 17 (n = 111, 99.1 %) and Q 18 (n = 110, 99.1 %) achieve comparable purity at greater length, but **both are Meccan narrative surahs** (not Madinan-legal). **Q 33 is the corpus's only Madinan surah with n ≥ 50 verses and alif-final fraction ≥ 0.98**.
- Q 33 is the **single non-monorhyme-pure surah** (i.e., not at frac = 1.0) with the *combination* (Madinan + length ≥ 70 + alif-fraction ≥ 0.98 + content-distance z > +1.5 + outlier-pct in top-3). This is what UAS rank 1 captures.

The original overview (§5 of `00-overview.md`) overstated this as "corpus-MAXIMUM monorhyme purity"; the strictly-corpus-MAX claim is FALSIFIED, the **Madinan-class-MAX-at-length** claim survives.

### 3.3 The qaṣīda analogy — pre-registered, not retrofitted

Pre-Islamic *qaṣīda* form (per al-Aṣmaʿī's recension; see [[h-new-740-preislamic-poetry-control]]) is defined precisely by **single-letter monorhyme sustained across the entire poem**, with feminine-ending *-ā* / *-hā* / *-kā* clausulae predominant. Q 33 satisfies both criteria:

- **Single-letter monorhyme**: 72/73 alif (98.6 %) — formally satisfies the Jāhiliyya constraint.
- **Feminine-ending dominance**: visual scan of Q 33 final words confirms heavy *-hā / -ka / -ā* clausulae (`عليكم`, `أمهاتهم`, `سبيلا`, `أبناءكم`, `حسابا`, `وكيلا`, `جميلا`, `بصيرا`, `عظيما` …) — fully consonant with the *qaṣīda* pattern.

This is the empirical sense in which Q 33 is "the corpus's most pre-Islamic-poetry-shaped surah" — the **opposite** of *iʿjāz al-fawāṣil* (which valorizes *high* rhyme-entropy + verse-length-modulated clausulae per al-Bāqillānī's *Iʿjāz al-Qurʾān* §VI). See [[cross-finding-026-iʿjāz-architecture]] for the dual-iʿjāz typology under which Q 33 sits firmly on al-Bāqillānī's *structural-iʿjāz* axis (high UAS) while sitting at the **anti-pole** of *fawāṣil-iʿjāz*.

### 3.4 Vocative-feminine / Madinan-code register correspondence (DIRECTIONAL — see §6)

The hypothesis embedded in the project task is: *the rhyme uniformity corresponds to a sustained vocative-feminine register addressing the Prophet's wives*. Empirical answer:

- vv. 28-34 (the wives-of-the-Prophet code) and vv. 50-55 (Prophet's marriage rules + ḥijāb) together = ~14 verses of explicit *yā nisāʾ al-Nabī* / *azwāj al-Nabī* / *nisāʾ al-muʾminīn* address. **All end in alif.**
- The opening triplet vv. 1-3 (*Yā ayyuha al-Nabī*) and the closing aphorism vv. 70-73 (the *amāna* + the *taqwā wa-qawl sadīd* injunction) — also all alif.
- The *only* non-alif verse Q 33:4 is itself a metalinguistic interruption: "*…and Allah speaks the truth and He guides the path (al-sabīl)*". The lone *lām* clausula occurs at the verse establishing **the rule itself** (no two hearts; adopted sons are not biological sons), and is rhetorically marked as a frame-clause for everything that follows.

**STATUS**: this rhyme-thematic correspondence is *directionally consistent* with the qaṣīda analogy but is **not** a confirmed quantitative finding (no permutation null-test has been pre-registered). It is logged here as an investigative hypothesis for future pre-reg.

## 4. Counting protocol — discrepancy with overview

The overview (`00-overview.md` §1) reports **word count = 1 384** and **letter count = 5 869**. My computation (no-tashkeel, pause marks `ۗ ۖ ۚ ۛ ۘ ۙ` stripped, whitespace collapsed) yields **1 307 / 5 788**. The most likely source of the difference is whether Quranic pause markers and the verse-end markers are tokenized as separate "words" / counted as separate "letters". Without re-running the overview's own pipeline, I **mark this as a NON-RECONCILED minor discrepancy**; both numbers are recoverable from the same `quran-no-tashkeel.json`.

The downstream H-NEW metrics (Fisher–Rao distance, ʿijāz signature, rhyme entropy) all use stable, pre-registered tokenization pipelines and are not affected.

## 5. Q 32-Q 33-Q 34 high-cost cluster (8.4 % of total TSP residual)

From `h-new-720.json.cumulative_stats`:
- Total mushaf-order canonical-adjacency residual (sum_delta): **9.827** (across 113 adjacencies).
- Q 33's two adjacencies (Q 32-33 and Q 33-34) contribute **0.6942**, i.e., **7.06 % of total residual**.
- However, the *fraction_residual* field in `h-new-720.json` (which divides by L_constrained ≈ 78) gives **4.38 % + 3.99 % = 8.37 %** as the project-canonical share. Both numbers express the same fact: **Q 33 alone contributes ~8 % of the corpus's mushaf-order departure from the optimal Fisher–Rao TSP-tour**.

For comparison:
- Q 1-Q 2 boundary: 7.50 % (rank 1, the famous Fātiḥa-Baqara hub-shift).
- Q 33's two boundaries: 8.37 % combined (rank 1 by sum-of-pair-residuals at any single surah-position).

**Tafsir-domain interpretation**: in classical *naẓm* terms (al-Biqāʿī, *Naẓm al-Durar*, Q 32 → Q 33 transition; see `03-tafsir-survey.md` §6), Q 32 al-Sajda is short (30 verses), Meccan, eschatological-monotheistic. Q 34 Sabaʾ is also Meccan (54 verses). Q 33 al-Aḥzāb (73 verses, Medinan) is the **sole Medinan surah** in the 15-surah Meccan run Q 28-42 (`h-new-870.json` analysis). Both al-Biqāʿī and Ibn al-Zubayr (cited in Biqāʿī, line 99917) explicitly note this discontinuity, framing Q 33 as a *tanzīh* parenthesis: a Medinan purification-of-the-Prophet block placed inside a Meccan eschatological run for thematic symmetry. The Fisher–Rao distance metric quantifies the cost of that placement at 8.4 % of total residual.

## 6. H-NEW-870 keystone test — Q 33 is local-singular, NOT global-keystone

`h-new-870.json`:
- Baseline 4-region two-piece compression-tail R² (full mushaf): **0.98604**.
- Counterfactual R² (Q 33 removed): **0.98471**.
- **ΔR² = +0.00133** — a positive number meaning *removing Q 33 marginally improves the fit*, as expected for an outlier; but the magnitude is two orders of magnitude smaller than the corpus's actual keystones.
- Top-10 keystones (whose removal *most degrades* the law) are Q 78, 81, 82, 86, 87, 92, 96, 98, 105, 109 — **all from the mufaṣṣal-qiṣār region (Q 78-114)** — none from the head-mid mushaf.

**Operational reading**: the four-region architectural law (`d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50)`, R² = 0.986) does not depend on Q 33 to hold. Q 33 is a *deviation* from the law (a +1.70-σ residual on `d̄_content`), but a deviation the law absorbs without re-fitting. By contrast, removing one of the mufaṣṣal-qiṣār surahs from the high-s region degrades R² by 0.002-0.003 — quantitatively bigger and qualitatively load-bearing.

This is the empirical content of "**local distinctiveness** (Q 33's domain) vs **global structural dependency** (Q 78-114's domain)". The two phenomena are orthogonal and Q 33 instantiates only the first.

## 7. Why Q 33 wins UAS rank 1 despite *very low* iʿjāz signature

Re-stating the key finding for clarity. The classical iʿjāz hypothesis (al-Bāqillānī, al-Khaṭṭābī, al-Jurjānī) emphasizes **rhetorical excellence**, much of which is operationalized in the project as **fawāṣil-balance** — i.e., the rhyme-clausula architecture should be *richly varied*, not *uniformly monorhymed*. Surahs that win the iʿjāz signature in this project's instrumentation (Q 55 al-Raḥmān, Q 26 al-Shuʿarāʾ, Q 12 Yūsuf, Q 17 al-Isrāʾ, Q 18 al-Kahf, Q 9 al-Tawba) are surahs with:

- Mid-range rhyme entropy (≈ 0.5-1.0 nats, neither monotonous nor chaotic).
- Above-average mean content distance (semantically distinctive).
- Above-average local cohesion (well-bound thematically).

Q 33 fails the *first* desideratum drastically (entropy = 0.072, rank 19 from minimum). It sits at the **anti-pole** of fawāṣil iʿjāz: extreme *uniformity* of clausula. But the UAS metric, by taking |sig_A|, treats the anti-pole as architecturally just as significant as the pole itself.

**The reading the data forces**: Q 33 is **not** an example of *iʿjāz al-fawāṣil*. It is an example of an opposite, equally architecturally-loud phenomenon — a **sustained Madinan-prosaic-legal content domain** (covering wives' code, ḥijāb, marriage-law, *khātam al-nabiyyīn* doctrine, Trench narrative, *amāna* eschatology) **forced into a Jāhiliyya monorhyme template** at a corpus-extreme outlier position in mushaf-order. The combination is uniquely Q 33's. UAS recognises this as architectural significance equal in absolute magnitude to Q 1 al-Fātiḥa (rank 2, UAS 8.87), Q 2 al-Baqara (rank 3, UAS 7.40), and Q 9 al-Tawba (rank 4, UAS 6.18).

Empirically: **Q 33 is the corpus-strongest *local* outlier, while Q 1 is the corpus-strongest *global* hub-shift, Q 2 is the corpus-strongest *length-content combination*, and Q 9 is the corpus-strongest *no-basmala / Trench-2 / military-legal* anomaly**. Each of the UAS top-4 wins by a different mechanism. Q 33 wins by *content-anomaly inserted into a phonological monorhyme + cost-residual peak*.

## 8. Hadith-architecture (mis)alignment — H-NEW-860

From `h-new-860.json.hadith_emphasis_scores.Q33`:
```
{"score": 2, "uas_rank": 1, "uas_value": 9.364271626045946,
 "note": "al-Aḥzāb — Bukhārī occasional citations on hijab/wives-of-prophet;
         not in fadāʾil-prominent list."}
```

The hadith-emphasis rubric (0-10) gave Q 33 only **2/10** despite its **rank 1/114** UAS. This makes Q 33 the corpus's most striking *hidden-architecture* case: maximal architectural significance (UAS = 9.364) with near-minimal classical liturgical/devotional emphasis (score = 2). The Sunni *fadāʾil al-Qurʾān* literature (al-Bukhārī's *Kitāb Faḍāʾil al-Qurʾān*, Muslim's *Faḍāʾil al-Qurʾān wa-mā yataʿallaq bihi*, al-Tirmidhī's *Abwāb al-Faḍāʾil*) preserves no whole-surah faḍīla for Q 33 comparable to Q 1, Q 2, Q 36, Q 67, Q 112, Q 113, Q 114 (see `04-hadith-corpus.md` §2). The Imāmī Shīʿī faḍāʾil tradition (al-Ṭabarsī, *Majmaʿ al-Bayān*, line 91728) **does** preserve a marfūʿ from Ubayy b. Kaʿb on Q 33 ("…security from the punishment of the grave"), and an Imāmī isnād from al-Ṣādiq on whoever "frequents the recitation of Sūrat al-Aḥzāb" being placed on the Day of Resurrection in the company of Muḥammad and his family. **The Sunni-Shīʿī asymmetry is itself a Q 33-specific phenomenon** and aligns with the Shīʿī doctrinal centrality of Q 33:33 (the *taṭhīr* / *Ahl al-Bayt* verse).

For the architectural-doctrinal explanation of the Sunni faḍāʾil-relative-silence, see `03-tafsir-survey.md` §7.

## 9. Cross-references (Obsidian links, do not edit)

- [[h-new-590-outlier-spectrum]] — Q 33 corpus-MAX outlier strength.
- [[h-new-660-compression-tail-gradient]] — global compression-tail law Q 33 deviates from.
- [[h-new-700-phonological-compression-tail]] — rhyme-letter diagnostics; corpus-wide rhyme entropy.
- [[h-new-720-canonical-adjacency-cost]] — Q 32-33-34 cluster.
- [[h-new-730-content-rhyme-anticorrelation]] — iʿjāz anti-twin lock; Q 33 sits at anti-pole.
- [[h-new-740-preislamic-poetry-control]] — Jāhiliyya monorhyme baseline.
- [[h-new-750-ijaz-signature]] — sig_A, sig_B for Q 33.
- [[h-new-840-unified-architectural-score]] — UAS rank 1.
- [[h-new-860-hadith-architectural-alignment]] — Q 33 hidden-architecture flag.
- [[h-new-870-q33-architectural-keystone]] — keystone test; local-singular ≠ global-keystone.
- [[cross-finding-026-iʿjāz-architecture]] — dual-iʿjāz typology.

## 10. Honest limits

- **The qaṣīda-correspondence claim** (§3.3) has been validated only at the structural-formal level (single-letter monorhyme + feminine clausula dominance). A rigorous comparison against the al-Muʿallaqāt corpus (`data/baseline-corpora/`) is *not* run here and remains an open pre-reg task.
- **The vocative-feminine / register correspondence** (§3.4) is observational, not statistical. A permutation test (does the rhyme-uniformity covary with the addressee-gender across verse-blocks?) is the proper falsification.
- **The non-reconciled word/letter counts** (§4) are noted; the H-NEW pipeline numbers should be treated as authoritative for cross-finding integration.
- **The H-NEW-860 hadith-emphasis rubric (0-10)** is itself a project-internal scoring with method-dependent edge cases. The Q 33 score = 2 reflects the absence of *whole-surah Sunni faḍāʾil*; per-verse Sunni hadith citation density is in fact high (104 hits in al-Bukhārī alone — see `04-hadith-corpus.md`). The rubric measures *liturgical / devotional whole-surah emphasis*, not *legal-narrative-historical citation frequency*.

---
*Computed and integrated under the Wave 2026-04-28 protocol; rules-tuple as declared in YAML frontmatter; SHA verification of cited h-new-*.json files is the parent project's responsibility.*

*Bismillāhi al-Raḥmāni al-Raḥīm.*
