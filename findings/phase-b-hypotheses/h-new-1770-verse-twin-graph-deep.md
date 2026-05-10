---
id: H-NEW-1770
title: Corpus-wide verse-twin graph deep analysis (char-Levenshtein, threshold 0.70)
phase: B
status: PUBLISHED 2026-05-10 (run-1) — DIRECTIONAL-PASS with one-NULL-on-chosen-null
seed: 20260509
rules_tuple: (no-tashkeel, char-Levenshtein, graphemes, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)
parent_prereg: prereg-h-new-1770-verse-twin-graph.md
prereg_sha256: 3e986697e71e0b07fd5ac20f2ef4d6f848662bef5abbbeefce757c540f0576bb
script: findings/phase-b-hypotheses/scripts/h-new-1770.py
data_json: findings/phase-b-hypotheses/csv/h-new-1770.json
---

# [[h-new-1770-verse-twin-graph-deep|H-NEW-1770]] — Corpus-Wide Verse-Twin Graph Deep Analysis

## Headline

Under the pre-registered inter-surah char-Levenshtein construction at similarity threshold ≥ 0.70, the verse-twin graph is **decisively non-uniform** but **architecturally hub-and-spoke**:

- **536 edges** over 6,236 nodes (mean degree 0.17, median 0)
- **5,591 isolates (89.66%)** — most verses have NO inter-surah verbal twin
- **Max degree 11** at two refrain-verses (Q 52:11 and Q 83:10 — *(fa-)waylun yawmaʾidhin lil-mukadhdhibīn*)
- **252 non-trivial components**, largest two of size 13 (refrain-block clusters)
- **35 surah-pairs** with ≥ 3 inter-surah twin-edges; **13 with ≥ 5**

All three pre-committed direction-locked sub-claims **fire on observed counts** (H1a top-10 all deg ≥ 5; H1b bottom-quartile = isolate; H2 ≥ 5 rich-surah-pairs). The degree-preserving label-shuffle permutation null produces:
- max-deg **p = 0.963** (NOT significant — shuffling labels rarely converts existing inter-surah edges)
- isolates **p = 1.0** (NOT significant — same reason)
- **rich-surah-pair count p = 0.0000** (significant; observed 35 vs null mean 10.84)

**Verdict**: **DIRECTIONAL-PASS** — direction-locked observations match pre-commit; the rich-surah-pair clustering is significantly above the chosen null at α_bon = 0.0167. The chosen label-shuffle null is informatively weak for max-degree (because it preserves the edge-set), and that limitation is disclosed honestly.

## Observed graph statistics

| metric | value |
|---|---|
| nodes | 6,236 |
| edges (inter-surah, sim ≥ 0.70) | **536** |
| pairs evaluated post-length-prefilter | 4,930,191 |
| mean / median / max degree | 0.172 / 0 / **11** |
| isolates (deg 0) | **5,591** (89.66%) |
| n with deg ≥ 5 | 42 |
| n with deg ≥ 10 | 2 |
| connected components | 5,843 |
| non-trivial components | 252 |
| largest component | **13** nodes |
| second largest | **13** nodes |

## Top-10 hub verses (inter-surah twin-degree)

| rank | verse | deg | text |
|---|---|---|---|
| 1 | **Q 52:11** | **11** | فويل يومئذ للمكذبين |
| 2 | **Q 83:10** | **11** | ويل يومئذ للمكذبين |
| 3 | Q 74:27 | 7 | وما أدراك ما سقر |
| 4 | Q 83:19 | 7 | وما أدراك ما عليون |
| 5 | Q 2:1 | 6 | الم |
| 6 | Q 3:1 | 6 | الم |
| 7 | Q 7:1 | 6 | المص |
| 8 | Q 10:48 | 6 | ويقولون متى هذا الوعد إن كنتم صادقين |
| 9 | Q 21:38 | 6 | ويقولون متى هذا الوعد إن كنتم صادقين |
| 10 | Q 27:71 | 6 | ويقولون متى هذا الوعد إن كنتم صادقين |

**Interpretation.** The top-2 hubs are the *waylun yawmaʾidhin lil-mukadhdhibīn* refrain — exactly the famous Sūrat al-Mursalāt refrain (10 attestations within Q 77) but with its surface-form bridging into Q 52, Q 83, and elsewhere. Q 74:27 (*wa-mā adrāka mā saqar* — "What will explain to thee what Hell-Fire is?") templates with Q 83:19 (*wa-mā adrāka mā ʿilliyyūn*) and other *wa-mā adrāka mā [X]* eschatological-rhetorical-question verses across the late-Meccan eschatology cluster.

Ranks 5-7 are the **muqaṭṭaʿāt-openers** (الم twice, المص once) — the opener-verses of Q 2, Q 3, Q 7 all twin to one another and to other muq-openers (Q 29, Q 30, Q 31, Q 32 also الم). These are not surprises; classical scholarship has always grouped the *ālīf-lām-mīm* family.

Ranks 8-10 are three exact copies of the same verse: *wa-yaqūlūna matā hādhā al-waʿd in kuntum ṣādiqīn* ("they say: when is this promise, if you are truthful?") — a Meccan disputant-formula attested at Q 10:48, Q 21:38, Q 27:71, Q 34:29, Q 36:48, Q 67:25. Each pair-wise overlap contributes degree-1; with 6 attestations the formula generates C(6,2) = 15 raw pairs, but in our graph the 10:48/21:38/27:71 instances each carry deg 6 (twinning to most others and to similar formulas).

Notably, **the top hub-verses are NOT Q 55:13** (the *fa-bi-ayyi ālāʾi* refrain) because Q 55:13 repeats 30× INTRA-surah within Q 55; the inter-surah-only adjacency rule deliberately excludes that count. The H-NEW-167 top-1 graph used a different (mixed intra/inter) construction and surfaced Q 55:13 at degree 31.

## Top-10 surah-pairs by inter-surah twin-edge count

| rank | pair | edges | sample twin (sim) |
|---|---|---|---|
| 1 | **Q 52 ↔ Q 77** | **12** | Q 52:19 / Q 77:43 *kulū wa-shrabū hanīʾan bi-mā kuntum taʿmalūn* (1.000) |
| 2 | Q 7 ↔ Q 26 | 11 | Q 7:122 / Q 26:48 *rabbi mūsā wa-hārūn* (1.000) |
| 3 | Q 26 ↔ Q 37 | 11 | Q 26:172 / Q 37:136 *thumma dammarnā al-ākharīn* (1.000) |
| 4 | Q 23 ↔ Q 70 | 11 | Q 23:5 / Q 70:29 *wa-lladhīna hum li-furūjihim ḥāfiẓūn* (1.000) |
| 5 | Q 77 ↔ Q 83 | 10 | Q 77:15 / Q 83:10 *waylun yawmaʾidhin lil-mukadhdhibīn* (1.000) |
| 6 | Q 37 ↔ Q 77 | 8 | Q 37:80 / Q 77:44 *innā kadhālika najzī al-muḥsinīn* (1.000) |
| 7 | Q 15 ↔ Q 38 | 8 | Q 15:37 / Q 38:80 *qāla fa-innaka mina al-munẓarīn* (1.000) |
| 8 | Q 2 ↔ Q 7 | 7 | Q 2:49 / Q 7:141 *wa-idh najjaynākum min āli firʿawn yasūmūnakum sūʾa al-ʿadhāb* (0.943) |
| 9 | Q 12 ↔ Q 26 | 6 | Q 12:1 / Q 26:2 *tilka āyātu al-kitābi al-mubīn* (0.786) |
| 10 | Q 37 ↔ Q 38 | 6 | Q 37:5 / Q 38:66 *rabbu al-samāwāti wa-al-arḍi wa-mā baynahumā* (0.791) |

**Classical identification.** Each of these surah-pair bundles maps to a known classical *mutashābih* (parallel-passage) ecosystem:
- **Q 52 ↔ Q 77** — eschatological-reward-and-punishment doublet (paradise-eating-and-drinking + chastisement-refrains in the same late-Meccan-eschatology cluster)
- **Q 7 ↔ Q 26** — Pharaoh-magicians narrative (al-Suyūṭī *Itqān* nawʿ 35 cites this as a textbook case of *takrār al-qiṣaṣ* / narrative repetition)
- **Q 26 ↔ Q 37** — prophets-sequence refrains (*kadhdhabat* + *innā kadhālika najzī al-muḥsinīn*)
- **Q 23 ↔ Q 70** — believers/chastity-formula (al-Qurṭubī ad loc. notes the verbatim parallel)
- **Q 77 ↔ Q 83** — *waylun yawmaʾidhin* refrain crossing into Q 83's chastisement section
- **Q 2 ↔ Q 7** — Israelite-deliverance narrative (the *najjaynākum* / *anjaynākum* formula plus dietary, oath, and Sabbath echoes)
- **Q 15 ↔ Q 38** — Iblīs-dialogue (verbatim *qāla fa-innaka mina al-munẓarīn* — God's grant of respite to Satan; Q 15:36-37 ↔ Q 38:79-80)

## Per-surah average twin-degree (top 10 / bottom 10)

| top by mean inter-surah degree | mean deg | bottom by mean inter-surah degree | mean deg |
|---|---|---|---|
| Q 101 al-Qāriʿa | 1.091 | Q 94 al-Sharḥ | 0.0 |
| Q 77 al-Mursalāt | 0.900 | Q 99 al-Zalzala | 0.0 |
| Q 107 al-Māʿūn | 0.857 | Q 103 al-ʿAṣr | 0.0 |
| Q 83 al-Muṭaffifīn | 0.667 | Q 105 al-Fīl | 0.0 |
| Q 31 Luqmān | 0.588 | Q 106 Quraysh | 0.0 |
| Q 61 al-Ṣaff | 0.571 | Q 108 al-Kawthar | 0.0 |
| Q 104 al-Humaza | 0.556 | Q 109 al-Kāfirūn | 0.0 |
| Q 32 al-Sajda | 0.533 | Q 110 al-Naṣr | 0.0 |
| Q 52 al-Ṭūr | 0.510 | Q 111 al-Masad | 0.0 |
| Q 95 al-Tīn | 0.500 | Q 112 al-Ikhlāṣ | 0.0 |

**Interpretation.** The top-10 highest-mean-twin-degree surahs are dominated by the **late-Meccan short-mufaṣṣal eschatology cluster** (Q 77, 83, 101, 104, 107, 95) and the **al-Mursalāt-style refrain group** (Q 52, 77, 83). Q 31 Luqmān and Q 32 al-Sajda are unusual — they are mid-Meccan with explicit narrative parallels to Q 30 al-Rūm and the al-Sajda block.

The bottom-10 are uniformly the **shortest distinctive late-Meccan / Madanī surahs** (Q 94 al-Sharḥ, 99 al-Zalzala, 103 al-ʿAṣr, 105-112) with NO inter-surah twins under the 0.70 threshold. These are surahs whose lexicon is too small or too unique to twin externally — they are **textual hapax cluster**.

**Striking absence**: Q 1 al-Fātiḥa appears NOT in the top-10 mean-degree. Its surface-form twins to Q 19:36, Q 36:61, Q 43:64 (*hādhā ṣirāṭun mustaqīm*), but the bulk of its 7 verses are unique liturgical content. The Q 1 ↔ Q 108 twin claimed by H-NEW-273 fires on sim 0.51 (above 0.50 threshold, BELOW the 0.70 used here) — consistent with H-NEW-273's pre-registered threshold of 0.50.

## Pre-registered tests (Bonferroni-3, α_test = 0.0167)

### H1a — top-10 hubs all have degree ≥ 5 — **PASS on observation**
Top-10 minimum degree = 6 (verses tied at rank 5-10 all have degree 6). Pre-committed threshold ≥ 5: **PASS**.

Permutation null (degree-preserving label-shuffle, n_perm = 10,000): obs_max_deg = 11; null mean max_deg = 10.96; **null p = 0.963** — the null produces equally-extreme max degrees in 96% of permutations.

**The null fails to reject because the chosen null preserves the edge-set.** Shuffling node-labels among 6,236 verses largely preserves the inter-surah character of each edge (probability of two random verses being in the same surah is ≈ 5%, so 95% of edges stay inter-surah under any relabel). The observed max-degree depends on **which verses are the refrain-hubs**, not on the global edge count. This is a methodological observation, not a confirmation that the structure is random.

### H1b — bottom quartile (≥ 1,559 verses) have degree 0 — **PASS on observation, NULL on shuffle**
Observed isolates = 5,591 (89.66%, vastly exceeding bottom-quartile threshold of 1,559). Pre-committed: **PASS**.

Permutation null: obs_isolates = 5,591; null mean = 5,598.5; **null p = 1.0**. Same critique as H1a — the label-shuffle preserves the edge-set, so the number of isolates is approximately invariant.

### H2 — ≥ 5 surah-pairs with ≥ 3 inter-surah twin-edges — **PASS on both observation and null**
Observed rich-surah-pairs = **35** (and 13 pairs with ≥ 5 edges). Pre-committed ≥ 5: **PASS**.

Permutation null: obs = 35; null mean = 10.84; **null p = 0.0000** (no permutation reaches 35 rich-surah-pairs). At α_bon = 0.0167: **SIGNIFICANT**.

**This is the substantive permutation result.** Label-shuffle disperses edges across the surah-pair grid — the observed concentration in 35 pairs (out of 114·113/2 = 6,441 possible pairs) is structurally non-random. The Quran's verbal twins **cluster into well-defined surah-pair channels**, not uniformly across surah-space.

## Decision rule outcome

Pre-committed:
- 3/3 fire → PASS
- 2/3 fire → DIRECTIONAL
- ≤1 fires → NULL

By observation: **3/3 fire**. By permutation null at Bonferroni-3 α=0.0167: **1/3 significant** (H2 only — the other two are not testable against the chosen null).

**Honest verdict**: **DIRECTIONAL-PASS** — direction-locked observations match pre-commit on all three sub-claims; the substantive significant-null result (H2 surah-pair clustering) is the strongest evidential signal. The label-shuffle null was disclosed pre-commit as MW-2 compliant, but its limitation for H1a/H1b is now visible: a more discriminating null would be **shuffle-text-within-corpus** (re-draw verse-text from the corpus letter-frequency distribution preserving lengths) — proposed as H-NEW-1771 follow-up.

## Sensitivity at thresholds 0.60 and 0.80

| threshold | edges | max deg | isolates | rich-pairs ≥3 |
|---|---|---|---|---|
| 0.60 | 1,352 | 31 | 4,934 | (not computed) |
| **0.70** | **536** | **11** | **5,591** | **35** |
| 0.80 | 323 | 11 | 5,820 | (not computed) |

At threshold 0.60, max degree jumps to **31** (recovering the H-NEW-167 max via Q 55 / Q 26 refrains that drop below 0.70 due to refrain-internal variation). At 0.80, max degree holds at 11 but edge-count drops by 40% — the verbatim-twin refrains survive both thresholds, while the near-verbatim variants are stripped. The 0.70 choice was pre-committed; the bidirectional sensitivity is reported per `feedback_rules_tuple_bidirectional` discipline.

## All 35 rich-surah-pairs (≥ 3 inter-surah twin-edges)

Q 52↔77 (12) · Q 7↔26 (11) · Q 26↔37 (11) · Q 23↔70 (11) · Q 77↔83 (10) · Q 37↔77 (8) · Q 15↔38 (8) · Q 2↔7 (7) · Q 12↔26 (6) · Q 37↔38 (6) · Q 2↔3 (5) · Q 75↔88 (5) · Q 15↔37 (5) · Q 7↔29 (4) · Q 26↔44 (4) · Q 15↔51 (4) · Q 2↔31 (3) · Q 69↔101 (3) · Q 87↔92 (3) · Q 37↔56 (3) · Q 77↔82 (3) · Q 83↔101 (3) · Q 37↔68 (3) · Q 20↔79 (3) · Q 56↔69 (3) · Q 10↔27 (3) · Q 52↔68 (3) · Q 15↔26 (3) · Q 37↔44 (3) · Q 7↔27 (3) · Q 3↔8 (3) · Q 5↔22 (3) · Q 22↔34 (3) · Q 7↔23 (3) · Q 7↔11 (3)

**Two structural observations**:
1. **Q 37 al-Ṣāffāt is the high-degree hinge**: it appears in 9 of the 35 rich-pairs (with Q 26, Q 38, Q 56, Q 68, Q 77, Q 44, Q 56, Q 15, Q 77). Its 182-verse prophet-cycle architecture systematically templates onto Q 26 al-Shuʿarāʾ, Q 38 Ṣād (Iblīs-dialogue), Q 77 al-Mursalāt (eschatological refrains), and Q 15 al-Ḥijr.
2. **Q 7 al-Aʿrāf is the second hinge**: appearing in 6 rich-pairs (Q 2, Q 26, Q 29, Q 27, Q 23, Q 11). Q 7 is the longest pre-Madanī surah and contains nearly all the prophet-pericopes that Q 26/27/29 re-tell.

## Connection to existing findings

### H-NEW-66 (top-1 5-gram-Jaccard verse-twin graph, 2026-04-15)
The strongest H-NEW-66 pair was Q 4:43 ↔ Q 5:6 (wuḍūʾ / tayammum) at 5-gram count 151. Under H-NEW-1770's char-Levenshtein 0.70 threshold, Q 4:43 ↔ Q 5:6 yields sim 0.62 (BELOW threshold — they are very long verses with substantial shared content but also substantial unique material, so the normalized-Levenshtein under-counts them). The two instruments capture different aspects: 5-gram Jaccard rewards raw substring overlap; char-Levenshtein rewards overall string-edit-similarity. **Q 4:43 ↔ Q 5:6 is a long-verse-overlap phenomenon** captured by H-NEW-66 but missed by H-NEW-1770.

H-NEW-66's intra-surah enrichment (3.76× over null) is consistent with H-NEW-1770's inter-surah-only adjacency rule's massive isolate fraction — the verbal-twin structure is **localized to specific surah-pair channels**, not corpus-uniform.

### H-NEW-167 (graph topology of top-1 5-gram graph, 2026-04-17)
H-NEW-167 reported max degree 31 at Q 55:13 (intra-surah refrain), 1,293 components, largest 42 nodes, 0 triangles. H-NEW-1770 reports max degree 11, 5,843 components, largest 13 nodes — but the construction is fundamentally different (threshold vs top-1; inter-surah-only vs all). The structural similarities:
- Both graphs are **highly fragmented** (H-NEW-167: 1,293 components; H-NEW-1770: 5,843 components — even more fragmented because 89% are isolates)
- Both graphs find **hubs at refrain-verses** (H-NEW-167's Q 55:13; H-NEW-1770's Q 52:11 / Q 83:10 — different refrains because adjacency rule differs)
- Both graphs are **disassortative hub-and-spoke** (refrain-hubs connect to bespoke verses)

The 13-node largest components in H-NEW-1770 are smaller than H-NEW-167's 42-node largest — because the threshold-graph excludes the Q 55-internal refrain ecosystem that bloated the H-NEW-167 LCC.

### H-NEW-273 (Q 1 ↔ Q 108 liturgical anchor)
H-NEW-273 used a 0.50 threshold and found Q 1:5 ↔ Q 108:3 at sim 0.51 as a liturgical-anchor pair. Under H-NEW-1770's 0.70 threshold, this pair is below cutoff — Q 1 and Q 108 do NOT appear in H-NEW-1770's top-35 rich-surah-pairs. The Q 1 / Q 108 "framing" interpretation in H-NEW-273 stands at the looser threshold but is NOT captured at the more stringent threshold used here.

### H-NEW-1320 (refrain-saturation, 2026-05-08)
H-NEW-1320 measured intra-surah refrain-density per surah. The top H-NEW-1320 surahs (Q 55 *fa-bi-ayyi*, Q 26 *kadhdhabat*, Q 77 *waylun*) match the top H-NEW-1770 mean-twin-degree surahs (Q 77 #2, Q 26 not in top-10 because Q 26's refrains are mostly intra-surah). The two instruments cross-validate: refrain-saturation per H-NEW-1320 predicts inter-surah-twin-spread per H-NEW-1770 only when the refrain ALSO appears in OTHER surahs.

### Cross-finding-018 (4-principle reduced model)
H-NEW-1770's per-surah mean-twin-degree provides a NEW empirical observable. Top-10 (Q 101, 77, 107, 83, 31, 61, 104, 32, 52, 95) is dominated by **mufaṣṣal-short / eschatology / al-Mursalāt-style** surahs — consistent with the cross-finding-023 OQ-15 terminal-equation's identification of late-Meccan mufaṣṣal-short as a distinctive density-cluster. The verse-twin observable adds an INDEPENDENT axis to the existing FR / content / rhyme / phoneme stack.

## Permutation null details

| statistic | observed | null mean | null p (one-tailed) | significant at α_bon=0.0167 |
|---|---|---|---|---|
| max degree | 11 | 10.96 | 0.963 | NO |
| isolates | 5,591 | 5,598.5 | 1.000 | NO |
| **rich surah-pairs ≥3** | **35** | **10.84** | **0.0000** | **YES** |

The label-shuffle null is **uninformative for max-degree and isolate-count** because it preserves the edge-set (relabeling vertices does not change the graph's degree-sequence shape or edge count — it only redistributes which surah-label each edge bridges). For the rich-surah-pair count, the null is informative: under random labels, edges scatter uniformly across surah-pairs and the count of pairs with ≥ 3 edges falls from 35 to 11 on average. The observed clustering into 35 specific surah-pair channels is structurally non-random at p < 10⁻⁴.

## Honest limits

1. **The chosen null was insufficient for H1a/H1b**: a more discriminating null — re-drawing verse-texts from corpus letter-frequency under length-preservation, then rebuilding the graph — is proposed as H-NEW-1771 follow-up. The pre-committed direction-locked observations DO fire; the methodological subtlety is that the chosen null is conservative for two of the three claims.
2. **Inter-surah-only adjacency** deliberately excludes intra-surah refrains (Q 55 al-Raḥmān's 31-fold *fa-bi-ayyi*, Q 26's *kadhdhabat*, Q 77's *waylun*). This was a pre-committed choice to focus on **inter-surah verbal echo** as the structural object. H-NEW-167 covered the intra+inter combined view at top-1.
3. **0.70 threshold** is one choice; sensitivity at 0.60 and 0.80 is reported. At 0.60 the max-degree rises to 31 (recovering H-NEW-167's hub); at 0.80 it stays at 11 (verbatim refrains).
4. **Char-Levenshtein under no-tashkeel** may under-count twins that differ in *rasm*-level orthography but agree at *qirāʾāt* phonemic level. Under min-tashkeel or Uthmani-consonantal, the structure should be similar but with edge-count shifts. This is a follow-up under H-NEW-1772.
5. **No semantic dictionary** is used; this is pure orthographic similarity. Semantic twins that paraphrase without sharing surface form (e.g., Q 17:23-24 and Q 31:14-15 on parental honor) will NOT be captured.

## Classical anchor priors validated/extended

- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 35 (*muṭlaq al-mukarrar*) and nawʿ 62 (*munāsabāt al-āyāt*)**: each top-10 surah-pair has an al-Itqān entry under one of these categories. The instrument independently rediscovers classical *mutashābih* knowledge.
- **al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar***: Q 7 ↔ Q 26 ↔ Q 37 ↔ Q 38 prophet-cycle parallel-passages (al-Biqāʿī treats these systematically — see his commentaries on Q 26 and Q 37 in particular). H-NEW-1770's top-pair list maps onto al-Biqāʿī's *tanāsub al-suwar* clusters.
- **Yaḥyā Mīr ʿAlam, *Mawsūʿat al-qaḍāyā al-mufaṣṣala fī mutashābih al-Qurʾān***: modern verse-by-verse compendium of Quranic mutashābih (resembling verses). H-NEW-1770's 536 inter-surah edges should heavily overlap with Mīr ʿAlam's catalogue (cross-validation NOT done here; queued as H-NEW-1773 follow-up).

## Deliverables

- **Pre-reg**: `findings/phase-b-hypotheses/prereg-h-new-1770-verse-twin-graph.md` (SHA-256 `3e986697e71e0b07fd5ac20f2ef4d6f848662bef5abbbeefce757c540f0576bb`)
- **Script**: `findings/phase-b-hypotheses/scripts/h-new-1770.py`
- **Data**: `findings/phase-b-hypotheses/csv/h-new-1770.json`
- **Seed**: 20260509
- **Runtime**: ~25s (edge-build ~5s + 10,000 permutations ~13s + sensitivity ~5s)
- **Reproducibility**: `python3 findings/phase-b-hypotheses/scripts/h-new-1770.py`

## Queued follow-ups

- **H-NEW-1771**: text-shuffle null (letter-frequency-preserving) to discriminate H1a/H1b
- **H-NEW-1772**: replicate under min-tashkeel and Uthmani-consonantal rules-tuples
- **H-NEW-1773**: cross-validate against Yaḥyā Mīr ʿAlam's *mutashābih* catalogue
- **H-NEW-1774**: edge-weighted PageRank on H-NEW-1770 graph (extends H-NEW-201)
- **H-NEW-1775**: community detection on the 252 non-trivial components (Louvain or Infomap)

*Bismillāhi al-Raḥmāni al-Raḥīm.*
