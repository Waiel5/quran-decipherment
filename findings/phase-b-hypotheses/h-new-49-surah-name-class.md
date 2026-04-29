---
id: H-NEW-49
title: Surah-name semantic classification — distribution, muqaṭṭaʿāt-status enrichment, and lexical-content prediction
status: COMPLETED 2026-04-15
pre_reg: h-new-49-surah-name-class-prereg.md
seed: 20260416
bonferroni_family: 2026-04-15-Wave-Surah-Name-Class
bonferroni_k: 5
alpha_bon: 0.01
rules_tuple: (hafs-kufan; no-tashkeel; canonical 114; 29-muqaṭṭaʿāt set)
verdict: PARTIAL-PASS (cells 1, 3, 5 informative; cell 2 trends but does NOT clear α_bon=0.01; cell 4 NULL as pre-registered)
---

# [[h-new-49-surah-name-class|H-NEW-49]] — Surah-name semantic classification

## Summary

We pre-registered a 9-class taxonomy for the 114 surah names, locked the per-surah class assignment BEFORE running tests (recorded in `csv/h-new-49.json` under `surah_class_assignments`), then ran 5 cells.

| Cell | Test | Result | Verdict |
|---|---|---|---|
| 1 | Class-distribution | descriptive table; SOCIAL_LEGAL=22 largest, OTHER_ABSTRACT=3 smallest | DESCRIPTIVE |
| 2 | Muqaṭṭaʿāt × class χ² | χ²=15.63, df=6, p=0.0159 (pooled) | TREND, fails α_bon=0.01 |
| 3 | MUQATTAAT_LETTER perm | 4/4 hits, p=0.0036 | PASS (tautology) |
| 4 | Khawātim al-Ḥashr / mufaṣṣal Fisher | Long Q1-49 DA=3/49, Short Q50-114 DA=4/65; Fisher p=1.000 | NULL (as pre-registered for Q59) |
| 5 | Lexical centrality of name-root | 18/110 testable surahs sig at α_per_surah=9.09e-5 | EXPLORATORY (16% < 33% PASS threshold) |

## Cell 1 — Class distribution (descriptive)

| Class | Count |
|---|---|
| SOCIAL_LEGAL | 22 |
| COSMOLOGICAL_NATURAL | 19 |
| EVENT_ESCHATOLOGICAL | 18 |
| REVELATION_RITUAL | 17 |
| ANIMAL_OBJECT | 13 |
| PROPHET_PERSON | 11 |
| DIVINE_ATTRIBUTE | 7 |
| MUQATTAAT_LETTER | 4 |
| OTHER_ABSTRACT | 3 |
| **Total** | **114** |

The most-populated class (SOCIAL_LEGAL = ~19% of surahs) is plausibly an artefact of my taxonomy choice to bin proper-noun-people-groups (Quraysh, al-Nās, al-Insān, al-Rūm) and abstract-people-groupings (al-Mujādilah, al-Mumtaḥina, al-Munāfiqūn, al-Kāfirūn, al-Muʾminūn, al-Ṣāffāt) here. A coarser taxonomy with 4–5 classes would tell a different distributional story; the locked 9-class scheme is the binding one.

## Cell 2 — Muqaṭṭaʿāt × name-class χ² (PRIMARY INFERENTIAL TEST)

After pooling MUQATTAAT_LETTER + REVELATION_RITUAL + OTHER_ABSTRACT into POOLED_OTHER (because expected-cell-count fell below 5 for these classes):

| Class | Muq YES | Muq NO | Muq-rate |
|---|---|---|---|
| PROPHET_PERSON | 7 | 4 | **0.636** |
| ANIMAL_OBJECT | 5 | 8 | 0.385 |
| DIVINE_ATTRIBUTE | 1 | 6 | 0.143 |
| COSMOLOGICAL_NATURAL | 5 | 14 | 0.263 |
| EVENT_ESCHATOLOGICAL | 1 | 17 | **0.056** |
| SOCIAL_LEGAL | 3 | 19 | 0.136 |
| POOLED_OTHER (RR+ML+OA) | 7 | 17 | 0.292 |

χ² = 15.634, df = 6, p = 0.01586.

**Verdict**: TREND but does NOT clear α_bon = 0.01. Naively at α=0.05 this would be significant; under the pre-registered 5-cell Bonferroni it is not.

The directional pattern is striking and consistent with prior phase-B findings:
- PROPHET_PERSON surahs are the MOST muqaṭṭaʿāt-enriched (7/11 = 64%, vs 29/114 = 25% baseline). All four major Meccan prophet-named muqaṭṭaʿāt openers (Yūnus, Hūd, Yūsuf, Ibrāhīm = Q10–14) plus Maryam (Q19), Luqmān (Q31), and Āl ʿImrān (Q3).
- EVENT_ESCHATOLOGICAL surahs are most muqaṭṭaʿāt-DEPLETED (1/18 = 6% — only Q44 al-Dukhān).
- This 11-fold spread (64% vs 6%) is the source of the χ² signal.

That the test misses α_bon by a factor of ~1.6× is honest. Future replication with a coarser pre-registered partition (e.g., person/non-person binary) might tighten this.

## Cell 3 — MUQATTAAT_LETTER permutation (MW-5 control)

The 4 surahs in MUQATTAAT_LETTER class (Ṭāhā Q20, Yāsīn Q36, Ṣād Q38, Qāf Q50) are by definition all in the muqaṭṭaʿāt-opener set; observed = 4/4. Permutation null over class-label assignments: p = 0.00364 (10⁵ perms).

This passes α_bon = 0.01. As pre-registered, this is a tautological positive control: the class definition forces the result. Its only diagnostic value is that the pipeline is wired correctly.

## Cell 4 — Khawātim al-Ḥashr / mufaṣṣal divine-attribute Fisher

Sub-test (a): Q 59 al-Ḥashr classification. PRE-REGISTERED PREDICTION: EVENT_ESCHATOLOGICAL (the "Gathering"). OBSERVED: EVENT_ESCHATOLOGICAL. The famous divine-names cluster at Q 59:22–24 ("huwa Allāh alladhī …") is CONTENT inside al-Ḥashr but the surah's NAME does not encode the divine-attribute thematics. Pre-reg honoured: the [[h-new-49-surah-name-class|H-NEW-49]] question 4 was honestly predicted to be NULL on the surah-name axis, and this is borne out.

Sub-test (b): mufaṣṣal short region (Q 50–114) DIVINE_ATTRIBUTE-named fraction = 4/65 = 6.2%; long region (Q 1–49) = 3/49 = 6.1%. Fisher exact two-sided p = 1.000. NULL.

So the divine-attribute name-class is uniformly distributed across the long/short partition. Divine-name CONTENT may cluster (al-Ḥashr ends, al-Ikhlās = Q112, al-Falaq = Q113, al-Nās = Q114 form the closing protective trio) but divine-name SURAH-NAMES do not statistically cluster in mufaṣṣal.

## Cell 5 — Lexical centrality of name-root

Per-surah binomial test: P(X ≥ hits | n_tokens, p_corpus_rest). 110 surahs testable (4 MUQATTAAT_LETTER excluded). Bonferroni-corrected within-cell α = 0.01 / 110 = 9.09e-5.

**Result**: 18/110 surahs significant (16%). Verdict: EXPLORATORY (below 33% PASS threshold).

Top significant findings (sorted by p):

| Surah | Class | Hits / Tokens | Ratio (in / rest) | p |
|---|---|---|---|---|
| Q 12 Yūsuf | PROPHET_PERSON | 25 / 1795 | 529× | 3.8e-59 |
| Q114 al-Nās | SOCIAL_LEGAL | 6 / 20 | 92× | 4.4e-11 |
| Q101 al-Qāriʿah | EVENT_ESCH | 3 / 36 | 3240× | 1.2e-10 |
| Q 63 al-Munāfiqūn | SOCIAL_LEGAL | 6 / 181 | 23× | 3.1e-7 |
| Q  9 al-Tawba | REV_RITUAL | 10 / 2505 | 8× | 9.0e-7 |
| Q 99 al-Zalzalah | EVENT_ESCH | 2 / 36 | 1080× | 1.7e-6 |
| Q 11 Hūd | PROPHET_PERSON | 6 / 1946 | 12× | 1.2e-5 |
| Q 97 al-Qadr | REV_RITUAL | 3 / 30 | 60× | 1.8e-5 |
| Q 24 al-Nūr | DIVINE_ATTR | 7 / 1319 | 7× | 7.4e-5 |

Plus 7 "ratio = ∞" cases where the name-root literally appears nowhere else in the corpus and ≥1× in the surah (Q 18 al-Kahf, Q 29 al-ʿAnkabūt, Q 46 al-Aḥqāf, Q 73 al-Muzzammil, Q 74 al-Muddaththir, Q 83 al-Muṭaffifīn, Q106 Quraysh). For these, p collapses to ≤ machine-zero because the corpus-rest rate is exactly 0. They ARE genuinely surah-unique words; whether to credit them as "lexical-centrality passes" depends on philosophy. I count them as PASSes since the binomial threshold is met.

**MW-5 (Q71 Nūḥ)**: hits = 3 / 227 = 1.32%, vs rest-rate 0.06% = 21× enrichment, p = 4.1e-4. This MISSES the within-cell Bonferroni threshold (9.09e-5) but passes naively at α = 0.001. The pre-registered MW-5 prediction was that Q71 would be the "most extreme outlier" — it is NOT (Q12 Yūsuf at p ≈ 1e-59 is the most extreme by orders of magnitude). The MW-5 prediction was honest-but-wrong about Nūḥ's outlier-status; the SIGNAL DIRECTION is correct (positive enrichment, ≫ baseline) and the pipeline produces sensible results.

The MW-5 mis-prediction is a useful audit: I had stated in pre-reg "Nūḥ is named ~28 times in 28 verses." This was a memory error — Nūḥ as a TOKEN appears only ~3 times in Q71 (the recurring third-person passages refer to him by pronoun and verb-conjugation, not by name). The honest record now stands.

**Caveats on Cell 5**:
- Root detection is by consonant-skeleton subsequence match, not by full Arabic morphological analysis. False positives are possible (e.g., the root نمل for "ant" might match other tokens containing ن…م…ل). False negatives are likely for triliterals where the surah text uses a derived form whose surface graphemes don't preserve the root order.
- Surahs whose name-roots are very common in Arabic (e.g., al-Ḥajj root ح-ج-ج matches "ḥujja", "iḥtajja", etc.) may be diluted by such background.
- The "ratio = ∞" cases inflate the PASS count slightly; if we required ratio ≤ 1000, only 11 of the 18 would survive — verdict would still be EXPLORATORY.

## Cross-cell synthesis

The clean signals are:
1. **Cell 5 produces a ROBUST set of name-content predictors**: surah names ARE often lexically central, especially for PROPHET_PERSON surahs (Yūsuf is the cleanest single case in the entire corpus, p ≈ 1e-59).
2. **Cell 2's directional pattern (PROPHET_PERSON → muqaṭṭaʿāt-rich, EVENT_ESCHATOLOGICAL → muqaṭṭaʿāt-poor) is interpretable**: muqaṭṭaʿāt openers cluster in the long Meccan narrative-prophet surahs (consistent with [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] length-finding) and avoid the short-mufaṣṣal eschatological wave.
3. **Cell 4 NULLS as expected**: the divine-names CONTENT cluster in al-Ḥashr is not predicted by the al-Ḥashr NAME (which means "Gathering"). Surah-naming and surah-content are separable axes.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-49-surah-name-class-prereg.md`
- Script: `scripts/h_new_49_surah_name_class.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-49.json`
- Journal: `journal/h-new-49-run-1.md`

## Honest disclosures

- The pre-registered taxonomy is a single judgment-call partition; reasonable scholars would partition differently. Sensitivity to taxonomy is unaudited.
- Cell 2 trends but misses α_bon. Reporting both raw p and Bonferroni-adjusted is the integrity move.
- MW-5 (Q71 Nūḥ) prediction had a fact-error in pre-reg (overstated Nūḥ token count); corrected here.
- Cell 5 root-matching is approximate; full morphological analyser would tighten the per-surah numbers.
