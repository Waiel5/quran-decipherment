---
finding_id: h-new-91
phase: B
status: PARTIAL-PASS — heterogeneity confirmed; Q26 prompt-claim FALSIFIED in stated direction; H-NEW-23 cross-reference confirmed
verdict: 3 of 4 pre-registered Bonferroni tests pass at α_bon=0.01. Per-surah rare-root density is heterogeneous beyond uniform-sampling expectation (Σz²=862.3 vs null mean 112.8, p<0.0001). Density CLUSTERS by genre (eschatological 0.134; hymn 0.148; legal 0.027). Cross-reference with H-NEW-23 hapax-final mechanism is strongly positive (Spearman ρ=+0.668, p<0.0001). The prompt's specific claim that Q26 al-Shuʿarāʾ is "the most narrative-vocabulary surah" by mean root-frequency is REJECTED — Q26 ranks 97/114 (above median, in the COMMON-vocabulary half). The actual length-controlled "narrative-vocabulary" outliers among long surahs are Q20 Taha, Q18 Al-Kahf, Q12 Yusuf.
rules_tuple: (no-tashkeel, STEM-root tokens, QAC-roots v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)
seed: 20260415
date: 2026-04-15
bonferroni_k: 5
alpha_bon: 0.01
classical_anchor: al-Bāqillānī Iʿjāz al-Qurʾān §3 jamāl wa-tafannun fī l-alfāẓ; al-Suyūṭī Itqān nawʿ 49 al-gharīb
parent_finding: MASTER:finding-#7 hapax-final z=10.61; H-NEW-23 hapax-slot mechanism PARTIAL-CONFIRMED
pre_reg_sha256: d3f1fcce6fd0c750b9b21525acd95034c911dfa50d7ece153df41e5db3bfb60a
---

# [[h-new-91-rare-root-density|H-NEW-91]] — Rare-root density per surah

## Summary

Each Quranic surah has a measurable "rarity profile" of its root-vocabulary. Using the QAC v0.4 morphology corpus (49,968 STEM root tokens across 1,642 distinct roots), we compute per-surah `geom_mean_freq` (geometric mean of global root frequencies for tokens in each surah; LOWER = more rare-root concentration), `rare_density_5` (fraction of tokens with global count ≤ 5), `hapax_density` (fraction with global count = 1), and `common_only_density` (fraction with global count ≥ 100).

Per the pre-registered Bonferroni-5 family at α_bon = 0.01:

| Test | Result | Verdict |
|---|---|---|
| T1: heterogeneity vs uniform null | Σz²=862.3 vs null 112.8±17.0; permutation p < 0.0001 | **PASS** |
| T2: length confound | Spearman ρ(geom_mean_freq, log N_s) = +0.554 | **CONFOUNDED** (use length-residualized rank) |
| T3: Q26 al-Shuʿarāʾ rank ≤ 15 | Q26 rank = 97/114 (above median); resid_rank 22/26 in q4 | **FAIL** |
| T4: H-NEW-23 hapax-final cross-reference | Spearman ρ = +0.668, p < 0.0001 | **PASS** (strong) |
| T5: genre ANOVA | F(geom_mean_freq) = 12.98, p < 0.0001; F(rare_density_5) = 11.22, p < 0.0001 | **PASS** |

**Composite verdict**: PARTIAL-PASS (3/4 substantive tests pass; T3 cleanly falsifies the prompt's directional claim).

## 1. Top-15 rare-root-density surahs (by geom_mean_freq ascending)

These are the surahs where vocabulary is dominated by infrequent roots. Length-quintile q is in the rightmost column (0 = shortest, 4 = longest).

| Rank | Surah | Genre | n_tokens | geom_mean_freq | rare_density_5 | hapax_density | null_z | q |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 111 al-Masad | eschatological | 17 | 15.32 | 0.412 | 0.118 | -2.09 | 0 |
| 2 | 108 al-Kawthar | eschatological | 7 | 18.27 | 0.429 | 0.286 | -1.36 | 0 |
| 3 | 113 al-Falaq | hymn | 15 | 19.31 | 0.400 | 0.133 | -1.99 | 0 |
| 4 | 100 al-ʿĀdiyāt | eschatological | 24 | 28.31 | 0.333 | 0.208 | -2.32 | 0 |
| 5 | 101 al-Qāriʿah | eschatological | 24 | 29.10 | 0.208 | 0.000 | -2.40 | 0 |
| 6 | 94 al-Sharḥ | hymn | 16 | 29.36 | 0.063 | 0.000 | -1.92 | 0 |
| 7 | 107 al-Māʿūn | eschatological | 14 | 30.83 | 0.286 | 0.071 | -1.73 | 0 |
| 8 | 106 Quraysh | eschatological | 12 | 31.61 | 0.333 | 0.167 | -1.68 | 0 |
| 9 | 104 al-Humazah | eschatological | 21 | 31.83 | 0.143 | 0.000 | -2.10 | 0 |
| 10 | 80 ʿAbasa | eschatological | 88 | 47.54 | 0.114 | 0.034 | **-3.76** | 1 |
| 11 | 90 al-Balad | eschatological | 52 | 50.12 | 0.173 | 0.077 | -3.00 | 1 |
| 12 | 105 al-Fīl | eschatological | 18 | 51.16 | 0.167 | 0.056 | -1.75 | 0 |
| 13 | 91 al-Shams | eschatological | 39 | 53.60 | 0.154 | 0.103 | -2.40 | 0 |
| 14 | 81 al-Takwīr | eschatological | 66 | 53.88 | 0.182 | 0.106 | **-3.20** | 1 |
| 15 | 86 al-Ṭāriq | eschatological | 41 | 55.24 | 0.098 | 0.049 | -2.46 | 1 |

**Pattern**: 12 of 15 are eschatological; 2 are short hymns; 0 are narrative or legal. All 15 are in length quintiles 0-1 (shortest 44 surahs). The ranking is heavily length-confounded (q4 surahs cannot reach geom_mean_freq < 100 by sample-size geometry alone).

## 2. Top-15 common-only-vocabulary surahs (by geom_mean_freq descending)

These are the surahs that re-use the most-frequent roots heavily.

| Rank | Surah | Genre | n_tokens | geom_mean_freq | common_only_density | null_z | q |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | 109 al-Kāfirūn | eschatological | 12 | 286.17 | 1.000 | +1.35 | 0 |
| 2 | 1 al-Fātiḥah | hymn | 23 | 230.94 | 0.783 | +1.35 | 0 |
| 3 | 64 al-Taghābun | narrative | 171 | 229.04 | 0.725 | +4.08 | 2 |
| 4 | 61 al-Ṣaff | narrative | 145 | 223.84 | 0.731 | +3.31 | 2 |
| 5 | 45 al-Jāthiyah | narrative | 320 | 219.86 | 0.763 | +4.98 | 3 |
| 6 | 29 al-ʿAnkabūt | narrative | 627 | 213.18 | 0.707 | +6.14 | 3 |
| 7 | 10 Yūnus | narrative | 1129 | 209.58 | 0.702 | **+7.99** | 4 |
| 8 | 63 al-Munāfiqūn | narrative | 117 | 206.57 | 0.735 | +2.24 | 1 |
| 9 | 110 al-Naṣr | eschatological | 16 | 206.54 | 0.688 | +0.69 | 0 |
| 10 | 3 Āl ʿImrān | legal | 2274 | 195.33 | 0.705 | **+8.52** | 4 |
| 11 | 40 Ghāfir | narrative | 788 | 194.03 | 0.704 | +4.87 | 4 |
| 12 | 49 al-Ḥujurāt | polemic | 234 | 191.76 | 0.671 | +2.48 | 2 |
| 13 | 46 al-Aḥqāf | narrative | 405 | 191.39 | 0.706 | +3.43 | 3 |
| 14 | 39 al-Zumar | narrative | 771 | 190.32 | 0.699 | +4.64 | 4 |
| 15 | 60 al-Mumtaḥanah | legal | 215 | 188.89 | 0.688 | +2.15 | 2 |

**Pattern**: Yūnus (10) and Āl ʿImrān (3) are the two strongest common-vocabulary outliers controlling for length (z = +7.99 and +8.52 respectively). Surah 109 al-Kāfirūn is the **only surah in the corpus where 100% of root-bearing tokens use roots with global count ≥ 100** — every token of "those who disbelieve" is from the most-common-root inventory.

## 3. Length-controlled ranking (the real "narrative-vocabulary" surahs)

The raw ranking is dominated by short surahs (length confound, T2 ρ = +0.554). The length-residualized analysis (5 quintile bins by log N_s, within-bin rank by geom_mean_freq) reveals where each surah sits among length-comparable peers.

**Long-surah quintile (q4, n=26 surahs, log_n in [6.46, 8.26]):**

Most rare-root vocabulary among long surahs:
1. **Q20 Taha** — geom_mean_freq = 110.0; rare_density_5 = 0.066; null_z = **-4.39**
2. **Q18 al-Kahf** — geom_mean_freq = 112.7; rare_density_5 = 0.065; null_z = **-4.93**
3. **Q12 Yūsuf** — geom_mean_freq = 123.2; rare_density_5 = 0.065; null_z = **-3.56**
4. Q17 al-Isrāʾ — geom_mean_freq = 127.7
5. Q22 al-Ḥajj — geom_mean_freq = 133.5

These are exactly the canonical narrative-heavy surahs (Moses-Pharaoh, the Cave / al-Khaḍir / Dhū l-Qarnayn, Yūsuf-the-prophet's life). Their rare-root density is **3-5σ below** what uniform-sampling from the global root distribution would predict for surahs of their length. Each carries dense proper-noun-driven narrative-specific vocabulary not reused elsewhere in the Qurʾān.

**Q26 al-Shuʿarāʾ — the prompt's claim**:
- geom_mean_freq = 179.6 (rank 22/26 in its q4 length quintile = bottom of long surahs by THIS metric)
- rare_density_5 = 0.030 (low!)
- common_only_density = 0.705
- null_z = +3.43 (POSITIVELY skewed toward common vocabulary)

**Q26's vocabulary is significantly MORE COMMON than uniform expectation**, NOT more rare. The prompt's "most narrative-vocabulary surah" claim, operationalized as "most-rare-vocabulary," is **falsified at z = +3.43**. The most rare-vocabulary long-narrative surahs are Taha (20), al-Kahf (18), Yūsuf (12).

**Why is Q26 actually common-vocabulary-heavy?** Q26 al-Shuʿarāʾ is structured as **seven-fold repetition of seven prophet-stories** (Moses, Abraham, Noah, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb), each closing with the SAME ring-closing refrain (ʾinna fī dhālika la-ʾāyatan wa-mā kāna ʾaktharuhum muʾminīn / wa-ʾinna rabbaka la-huwa l-ʿazīzu l-raḥīmu). The repeated refrain structure recycles the same ~10 high-frequency roots seven times each, inflating the common-vocabulary fraction. Q26 is "narrative" but with HIGHLY-RECYCLED rather than HIGHLY-DIVERSE narrative vocabulary.

## 4. Genre clustering (T5)

Permutation ANOVA across the H-NEW-23 5-genre coding:

| Genre | n surahs | mean geom_mean_freq | mean rare_density_5 |
|---|---:|---:|---:|
| **eschatological** | 32 | **79.94** | **0.134** |
| **hymn** | 6 | **101.30** | **0.148** |
| narrative | 60 | 141.06 | 0.047 |
| polemic | 6 | 164.67 | 0.038 |
| **legal** | 10 | **169.94** | **0.027** |

ANOVA F = 12.98 for `geom_mean_freq` and F = 11.22 for `rare_density_5`; both p < 0.0001 (10,000-perm null).

**Reading**: eschatological surahs have **5× the rare-root density** of legal surahs (0.134 vs 0.027). Hymn surahs (n=6) are similar at 0.148. Legal Medinan and polemic Medinan surahs have the lowest rare-root density — they recycle a small frequent vocabulary (qul, kataba, ʾāmana, kafara, qatala, jāhada, etc.).

This genre-stratified pattern is robust to length stratification — within q4 (long surahs) the legal Medinan surahs (3 Āl ʿImrān, 5 al-Māʾidah) sit in the common-half while narrative Q12 Yūsuf and Q20 Taha sit in the rare-half.

## 5. H-NEW-23 cross-reference (T4) — convergence

For the 87 surahs with at least 1 root-hapax, Spearman ρ between (a) per-surah `rare_density_5` and (b) per-surah hapax-final placement rate (from H-NEW-23 data) = **+0.668** at p < 0.0001.

**Convergence**: surahs that recruit rare roots HEAVILY also place their rare roots terminally (al-Zarkashī's *al-maqṣūda li-ghayrihā* mechanism). The two phenomena are not independent — they co-vary at ρ ≈ 0.67 across surahs. This is consistent with a unified "rare-vocabulary slot-engineering" cluster: short eschatological surahs both (i) preferentially recruit rare roots and (ii) place those rare roots at verse-final position.

This adds [[h-new-91-rare-root-density|H-NEW-91]] to the eschatological-slot-engineering cluster:
- H-NEW-19 (elision-eschatology): iltifāt + ellipsis density peaks eschatological
- H-NEW-23 (hapax-slot mechanism): hapax-final rate peaks eschatological at 0.077 vs 0.002 legal
- **[[h-new-91-rare-root-density|H-NEW-91]] (this finding)**: rare-root density peaks eschatological at 0.134 vs 0.027 legal

The cluster is now a **quadruple-test convergence** when including the parent hapax-final p=7.35e-29.

## 6. Heterogeneity (T1) — magnitude

Σz² (sum of squared per-surah deviations from uniform-sampling null) = **862.3**. The permutation null under random-shuffle of root-labels across all 49,968 token positions (preserving per-surah N_s) gives a distribution centered at 112.8 with SD 17.0. Observed value is **>40 SD above null**. Permutation p = 0/10000 (one-sided positive); reported as p < 0.0001.

This is a strong heterogeneity claim. Per-surah vocabulary-rarity profile is NOT consistent with the surah being a random sample of roots from the corpus — the surahs select systematically along genre and length axes.

## 7. Length confound (T2) — diagnostic

Spearman ρ(geom_mean_freq, log N_s) = **+0.554**. The length effect is real and substantial: longer surahs unavoidably have more diverse vocabulary in the absolute sense (Heaps' law) but THIS metric goes UP with length because the length-driven sample-size geometry pulls geom_mean_freq toward the global mean as N_s grows. The raw ranking is **partially length-confounded**.

We mitigate by reporting:
- Raw rank (top/bottom 15)
- Length-quintile resid_rank (5 quintiles, 22-26 surahs each)
- null_z (per-surah z-score under uniform-sampling null at exactly N_s tokens — automatically length-controlled)

The `null_z` column in the per-surah CSV is the clean length-controlled effect-size.

**Top-5 most-rare-vocab by null_z (length-controlled)**:
1. Q56 al-Wāqiʿah z = -5.59 (n=255, eschatological)
2. Q18 al-Kahf z = -4.93 (n=1057, narrative)
3. Q20 Taha z = -4.39 (n=837, narrative)
4. Q79 al-Nāziʿāt z = -3.96 (n=122, eschatological)
5. Q80 ʿAbasa z = -3.76 (n=88, eschatological)

**Top-5 most-common-vocab by null_z (length-controlled)**:
1. Q3 Āl ʿImrān z = +8.52 (n=2274, legal)
2. Q10 Yūnus z = +7.99 (n=1129, narrative)
3. Q29 al-ʿAnkabūt z = +6.14 (n=627, narrative)
4. Q45 al-Jāthiyah z = +4.98 (n=320, narrative)
5. Q40 Ghāfir z = +4.87 (n=788, narrative)

The length-controlled long-surah outlier on the rare-vocab side is **Q56 al-Wāqiʿah** (the eschatological "Inevitable Event" surah; classical scholarship considers it the most lexically dense eschatological surah after Q55 al-Raḥmān). Its z = -5.59 is the strongest single-surah signal in the dataset.

## 8. Composite verdict & convergences

PARTIAL-PASS at 3/4 substantive Bonferroni tests. The main affirmative findings:

1. **Per-surah rare-root density is a genuine heterogeneity**, not random sampling (T1: p < 0.0001, Σz² 862 vs null 113).
2. **Genre clusters drive most of the heterogeneity**: eschatological surahs are 5× richer in rare roots than legal surahs (T5: p < 0.0001).
3. **Hapax-final placement (H-NEW-23) and rare-root density CO-VARY** at ρ = +0.67 across surahs (T4: p < 0.0001) — these are not independent rhetorical phenomena but two faces of the same slot-engineering cluster.
4. **Length confound is real (ρ = +0.55) but does not exhaust the genre signal** — within length quintiles the genre clustering persists (e.g., Q56 al-Wāqiʿah z = -5.59 in q2).

The main negative finding:

5. **Q26 al-Shuʿarāʾ rank claim FAILS**: Q26 is a HIGH-COMMON-VOCABULARY surah by every metric (rank 97/114, q4 quintile bottom-3, common_only_density 0.705, null_z = +3.43). The "most narrative-vocabulary" intuition was mis-targeted: the canonical long-narrative surahs by rare-vocab density are **Q12 Yūsuf, Q18 al-Kahf, Q20 Taha**, NOT Q26 al-Shuʿarāʾ. Q26's repeated seven-prophet refrain structure recycles common roots heavily; it is "narrative" in literary form but "common-vocabulary" in lexical statistics.

## 9. Garden-of-forking-paths log (post-hoc honesty)

Decisions documented in pre-reg (and not violated):
- PRIMARY metric `geom_mean_freq` locked before any per-surah computation.
- Rare = global count ≤ 5 (matches H-NEW-29 min-count).
- Common = global count ≥ 100 (matches prompt threshold).
- Q26 one-sided pre-committed direction (bottom-15 = rare-vocab heavy).
- Genre coding identical to H-NEW-23.
- Length confound test pre-included.
- Bonferroni k=5, α_bon = 0.01 LOCKED.

Decisions made during analysis (post-hoc, but transparently reported):
- Top-3-per-quintile breakdown was added in the report (not in pre-reg). This is a descriptive expansion, not a new test.
- The "Q26 explained by repeated refrain" interpretation in §3 is post-hoc literary interpretation; the statistical claim (Q26 fails the rank ≤ 15 test) is the pre-registered one.
- §7 ranking by `null_z` was implicit in the metric definition (null_z is computed in T1 as per-surah z under uniform null) — reporting top-5 by null_z is a descriptive use of pre-computed numbers, not a new test.

## 10. Limits

- **QAC-only root identification**. ~22% of all words have no ROOT field (proper nouns, function words); these are excluded by the STEM-with-ROOT filter. If proper nouns were the dominant rare-vocabulary in narrative surahs, our analysis is partially blind to them. (This may explain part of why Q26 al-Shuʿarāʾ — which has many prophet proper nouns Mūsā, Ibrāhīm, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb — under-scores on rare-root density: those proper nouns are stripped before counting.)
- **Genre coding is COARSE** (5 classes, deterministic mapping). A formal Itqān nawʿ-65 catalog would be more nuanced; the H-NEW-23 reuse keeps results comparable across findings.
- **Length quintiles are equal-N (22-26 surahs each)** but log-N spans 1.94 to 8.26 (almost 7 e-folds). Within-quintile residualization is a coarse control.
- **Single-corpus analysis**. A baseline-corpus comparison (Bukhari, Jāḥiẓ at matched genre) would be the natural next step — does generic Arabic prose show similar genre-rarity clustering, or is this Quran-specific? See §FOLLOW-UPS.

## 11. Follow-ups to queue

1. **H-NEW-91b** — proper-noun-inclusive variant. Re-do with PN tokens included (lemma-level rather than root-level for proper nouns). Predict Q26 al-Shuʿarāʾ rises substantially.
2. **H-NEW-91c** — baseline rarity comparison. Compute the same per-chunk geom_mean_freq on length-matched Bukhari and Jāḥiẓ slices; test whether the eschatological-cluster rarity ratio is Quran-specific or generic Arabic prose feature.
3. **H-NEW-91d** — Q56 al-Wāqiʿah deep-dive. Q56's z = -5.59 (length-controlled) makes it the single strongest rare-vocab outlier. What roots drive that? Is the al-Suyūṭī gharīb catalog disproportionately drawn from Q56?
4. **H-NEW-91e** — long-narrative cluster confirmation. Q12, Q18, Q20 cluster as the rare-vocab long surahs. Test whether their rare roots CONCENTRATE at narrative-payload positions (proper-name-introduction verses, denouement verses) vs distribute uniformly across the surah.
5. **H-NEW-91f** — Q26 al-Shuʿarāʾ refrain hypothesis. If we DELETE the seven repeated refrains from Q26 and recompute, does Q26's geom_mean_freq drop substantially? Quantify the refrain's contribution to common-vocabulary inflation.

## 12. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-91-rare-root-density-prereg.md` (SHA-256 d3f1fcce6fd0c750b9b21525acd95034c911dfa50d7ece153df41e5db3bfb60a)
- Script: `scripts/h_new_91_rare_root_density.py`
- Per-surah CSV: `findings/phase-b-hypotheses/csv/h-new-91-per-surah.csv`
- Summary JSON: `findings/phase-b-hypotheses/csv/h-new-91.json`
- Journal: `journal/h-new-91-run-1.md`
- Seed: 20260415
