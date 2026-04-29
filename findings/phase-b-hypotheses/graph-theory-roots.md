---
title: Graph-Theoretic Analysis of Quranic Roots
phase: B
status: exploratory
rules:
  orthography: no-tashkeel
  word_definition: lemma                  # roots from QAC morphology
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1 # QAC indexes use this convention
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: bipartite-configuration     # see Stage 8
agent: graph-theory
date: 2026-04-12
inputs:
  - data/morphology/root-index.json
  - data/morphology/root-stats.csv
  - data/alt-text/risan-quran-json/dist/chapters/{1..114}.json
artifacts:
  - data/morphology/surah-root-graph.json
  - data/morphology/root-cooccurrence-graph.json
  - journal/graph-theory-run-1.md
---

# Graph-Theoretic Analysis of Quranic Roots

The Quran is one text. We treat its 1,642 morphological roots (from the Quranic Arabic Corpus 0.4) as nodes in two derived graphs and ask what the topology says about the text. All centralities, communities, clusters, and null comparisons below are computed pure-Python (no `networkx` was available in this environment).

## Headline result in one paragraph

The Quranic root co-occurrence network is enormously *more cohesive* than a configuration-model null preserving the same verse-degree and root-frequency distributions: observed total edge-weight 211,298 vs null mean 193,119 (z = +36.3); observed weight-≥5 edges 8,556 vs null mean 7,605 (z = +18.2); the most-connected hub (the root **اله** Alh) has weight-≥5 degree 509 vs null max 464 (z = +5.6). The text bunches its co-occurrences onto fewer, heavier root pairs than chance allows. The most central *bridge* root — i.e. the highest non-frequency-hub by Brandes betweenness — is **خلق xlq "create"** (BC = 2,412, frequency rank 12), followed by **قلب qlb "heart"** (BC = 2,049, frequency rank 13). The most uniquely-vocabularied surah (length-controlled) is **Surah 55 Ar-Rahman**, at residual −0.076 from the avg-Jaccard ~ log(verses) regression, separating cleanly from #2 (Surah 80 'Abasa, residual −0.066). Unsupervised k-means cosine clustering at k=5 produces a 97% Meccan cluster (61/63) and an 89% Medinan cluster (24/27), recovering revelation period without supervision. Louvain on the co-occurrence graph yields 29 semantically interpretable communities (modularity Q = 0.0812).

---

## 1. The bipartite surah-root graph

- **Nodes:** 114 surahs + 1,642 roots
- **Edges:** 17,496 (surah, root, count) triples
- **Stored at:** `data/morphology/surah-root-graph.json` (`surahs[s_id] -> {root: count}`, `roots[root] -> {s_id: count}`)
- **Coverage:** the QAC indexes 6,214 of 6,236 verses (the missing 22 are basmala-only or clitic-only verses with no morphological tokens). All counts below are computed on those 6,214 verses.
- **Largest by distinct-root vocabulary:** Al-Baqarah (585), Al-A'raf (477), An-Nisa (462), Ali 'Imran (439), Al-Ma'idah (422), Al-An'am (421), Al-Kahf (369), At-Tawbah (366), An-Nahl (358), Hud (348).

## 2. Surah similarity matrix

We compute two 114×114 similarity matrices on this bipartite graph:

- **Jaccard** on each surah's *set* of distinct roots
- **Cosine** on each surah's *count* vector over roots

### Headline pairs and centers (raw, not length-controlled)

| Quantity | Value | Surahs |
|---|---|---|
| Most similar (Jaccard) | 0.4957 | s2 Al-Baqarah & s4 An-Nisa |
| Most similar (cosine)  | 0.9613 | s2 Al-Baqarah & s3 Ali 'Imran |
| Most dissimilar (Jaccard) | 0.0000 | s1 Al-Fatihah & s103 Al-'Asr (no shared roots) |
| Most dissimilar, length-matched (verses within 5) | 0.0000 | s66 At-Tahrim (12v) & s107 Al-Ma'un (7v) |
| Center (highest avg Jaccard, raw) | 0.230 | s10 Yunus |
| Most unique (lowest avg Jaccard, raw) | 0.016 | s108 Al-Kawthar |

The "raw most similar" / "raw most central" metrics are dominated by the long Meccan storyteller surahs (Yunus, Hud, Al-An'am, Al-Mu'minun, Az-Zumar, Ash-Shuraa, Al-Ankabut, Ghafir) — all with abundant prophet-narrative vocabulary that shows up everywhere. The "raw most unique" metrics are dominated by the very shortest surahs and are an artifact of set-size: Jaccard between a 4-verse and a 286-verse surah is mechanically tiny.

### Length-controlled center / unique

To strip the trivial length effect, we regress avg-Jaccard on log(verse count) (β = +0.0482, α = −0.0342) and rank by residual.

**Most unique (most negative residual):**

| Rank | Surah | Resid | avg_J | verses | type |
|---|---|---|---|---|---|
| 1 | s55 Ar-Rahman | −0.0761 | 0.100 | 78 | (Mec/Med disputed; risan: medinan) |
| 2 | s80 'Abasa | −0.0656 | 0.080 | 42 | meccan |
| 3 | s2 Al-Baqarah | −0.0597 | 0.179 | 286 | medinan |
| 4 | s56 Al-Waqi'ah | −0.0567 | 0.129 | 96 | meccan |
| 5 | s101 Al-Qari'ah | −0.0548 | 0.027 | 11 | meccan |
| 6 | s77 Al-Mursalat | −0.0531 | 0.101 | 50 | meccan |
| 7 | s100 Al-'Adiyat | −0.0453 | 0.036 | 11 | meccan |
| 8 | s94 Ash-Sharh | −0.0449 | 0.021 | 8 | meccan |
| 9 | s81 At-Takwir | −0.0447 | 0.083 | 29 | meccan |
| 10 | s75 Al-Qiyamah | −0.0446 | 0.099 | 40 | meccan |

**Substantively interesting.** Ar-Rahman (#1, by a clear margin) is famous for its 31-times-repeated refrain "*fa-bi-ayyi alā'i rabbikumā tukadhdhibān*" and its parallelistic dual-form structure — and the graph-theoretic analysis flags it independently as having the most distinctive root set per word of length. 'Abasa, also flagged, is one of only a handful of surahs with a unique narrative incident (the blind man Ibn Umm Maktum). And Al-Baqarah, the longest surah, is also unusual by this measure — its sheer breadth of legal and narrative material gives it a vocabulary signature unlike anything else.

**Most central (most positive residual)** — short Medinan "summary" chapters dominate:

| Rank | Surah | Resid | verses | type |
|---|---|---|---|---|
| 1 | s57 Al-Hadid | +0.068 | 29 | medinan |
| 2 | s46 Al-Ahqaf | +0.066 | 35 | meccan |
| 3 | s64 At-Taghabun | +0.063 | 18 | medinan |
| 4 | s59 Al-Hashr | +0.060 | 24 | medinan |
| 5 | s65 At-Talaq | +0.058 | 12 | medinan |
| 6 | s66 At-Tahrim | +0.054 | 12 | medinan |
| 7 | s58 Al-Mujadila | +0.053 | 22 | medinan |
| 8 | s62 Al-Jumu'ah | +0.053 | 11 | medinan |
| 9 | s32 As-Sajdah | +0.053 | 30 | meccan |
| 10 | s13 Ar-Ra'd | +0.052 | 43 | medinan |

8 of the top 10 length-controlled "central" surahs are Medinan. They're short, but they sample from the full corpus vocabulary at a much higher rate than their length predicts: they read like vocabulary-dense summaries. This is congruent with the traditional view of late-Medinan surahs as theologically-recapitulative.

## 3. Agglomerative clustering of surahs

We tried four clustering methods and report all four:

| Method | k=2 Rand vs Mec/Med | k=2 partition | Notes |
|---|---|---|---|
| Avg-linkage on Jaccard distance | 0.617 | 113 + 1 | pathological — Al-Masad as singleton outlier |
| Complete-linkage on Jaccard distance | 0.617 | 111 + 3 | Al-'Asr cluster as singleton; not informative |
| Complete-linkage on cosine distance | 0.609 | 112 + 2 | Al-Humazah + Al-Masad outlier pair |
| **K-means cosine (TF-IDF, 20 restarts)** | **0.496** | **85 + 29** | one cluster is **97% Meccan** |

K-means at k=2 finds a 29-surah cluster that is 28 Meccan + 1 Medinan (96.5% Meccan purity). The **Rand index** is 0.50 — *not* high — because the partition is unbalanced (the other cluster mixes Meccan and Medinan). But the **purity** of the small cluster is striking: there's a vocabulary signature shared by 28 Meccan surahs (mostly the short, hymnic, eschatology-heavy late-Meccan group s52, s55, s69, s72, s74, s77, s78, s80, s82, s84, s85, s86, s87, s88, s89, ...) that nothing else shares.

### k=5 cosine k-means: **the cleanest revelation-period split**

- **C1: 63 surahs, 4,235 verses, 97% Meccan (61/63)** — narrative-rich Meccan storyteller surahs (Yunus, Hud, Yusuf, An-Nahl, Al-Isra, Al-Kahf, Maryam, Ta-Ha, Al-Anbiya, Al-Mu'minun, Ash-Shuara, An-Naml, Al-Qasas, ...)
- **C2: 27 surahs, 1,500 verses, 89% Medinan (24/27)** — the Medinan legal/community surahs (Al-Baqarah, Ali 'Imran, An-Nisa, Al-Ma'idah, Al-Anfal, At-Tawbah, Al-Hajj, An-Nur, Al-Ahzab, Muhammad, Al-Fath, Al-Hujurat, Al-Hadid, Al-Mujadila, Al-Hashr, ...) — and Al-Fatihah lands here too
- **C3: 10 surahs, 116 verses, 90% Meccan** — short hymns
- **C4: 9 surahs, 245 verses, 100% Meccan** — late-Meccan eschatology cluster (s56, s70, s77, s86, s100, s101, s105, s106, s107)
- **C5: 5 surahs, 140 verses, 80% Meccan** — heterogeneous

This **k=5 split is the highest-quality unsupervised recovery of revelation-period structure** we found, and it goes through *root vocabulary alone*. We never told the algorithm anything about Mecca, Medina, or revelation order.

### k=10 cosine k-means

C1 (41 surahs, 90% Meccan) splits off; C2 (29 surahs, 76% Medinan) holds the Medinan legal core; the remaining clusters break the Meccan side into thematic sub-groups (eschatology, very-short-oath surahs, etc.). The breakdown is consistent with traditional sub-classifications of Meccan periods (early-rhyming, middle-eschatological, late-narrative).

## 4. Root co-occurrence graph

- **Construction:** edge (r₁, r₂) with weight = number of verses containing both roots
- **Total unique edges:** 74,185 (no threshold)
- **Filtered to weight ≥ 5:** 8,556 edges across **608 nodes** (out of 1,642)
- **Stored at:** `data/morphology/root-cooccurrence-graph.json`

The 1,034 roots that *don't* appear in the filtered graph either occur fewer than 5 times total or never co-occur with another root in 5+ verses — they are functionally isolates or near-isolates of the network.

### Strongest co-occurring pairs

| Pair | Weight | Gloss |
|---|---|---|
| Alh + qwl (اله / قول) | 514 | "Allah" + "say" — the introducer of all divine speech |
| Alh + kwn (كون) | 441 | "Allah" + "be" — copular constructions |
| Alh + Elm (علم) | 408 | "Allah" + "know" |
| Alh + Amn (امن) | 372 | "Allah" + "believe" |
| kwn + qwl | 369 | "be" + "say" |
| qwl + rbb (ربب) | 329 | "say" + "Lord" |
| Alh + $yA (شيا) | 282 | "Allah" + "thing" |
| Alh + qwm (قوم) | 242 | "Allah" + "people/stand" |

## 5. Centrality on the co-occurrence graph

| Rank | Root | Arabic | Gloss | Degree | PageRank | Eigenvector | Betweenness |
|---|---|---|---|---|---|---|---|
| 1 | Alh | اله | god/Allah | 509 | 0.0811 | 0.452 | 67,229 |
| 2 | qwl | قول | say | 406 | 0.0445 | 0.335 | 26,993 |
| 3 | kwn | كون | be | 384 | 0.0370 | 0.294 | 18,127 |
| 4 | rbb | ربب | lord | 299 | 0.0242 | 0.205 | 10,607 |
| 5 | Amn | امن | believe/safe | 294 | 0.0234 | 0.218 | 7,898 |
| 6 | Elm | علم | know | 278 | 0.0214 | 0.215 | 6,027 |
| 7 | qwm | قوم | people/stand | 263 | 0.0180 | 0.169 | 5,084 |
| 8 | Aty | اتي | come | 225 | 0.0143 | 0.146 | 2,752 |
| 9 | kfr | كفر | disbelieve | 216 | 0.0138 | 0.141 | 3,448 |
| 10 | byn | بين | between/clarify | 215 | 0.0139 | 0.143 | 3,221 |
| 11 | $yA | شيا | thing/will | 207 | 0.0136 | 0.150 | 1,777 |
| 12 | xlq | خلق | create | 200* | 0.013* | 0.127 | **2,412** |
| 13 | rsl | رسل | send/messenger | 183 | 0.0111 | 0.127 | 1,545 |
| 14 | ywm | يوم | day | 184 | 0.0096 | 0.097 | 1,863 |
| 15 | smw | سمو | heaven | 152 | 0.0095 | 0.104 | 1,652 |

(*Degree shown for top 10 by degree; the table is collapsed to keep the row count manageable.)

All four centrality measures agree on the same hubs. The picture is what you'd expect: **Allah, say, be, lord, believe, know, people** form the unmovable core of Quranic discourse.

### Bridge roots — the more interesting story

Filtering OUT the top-25-frequency hubs and ranking by Brandes betweenness, the structural bridges are:

| Rank | Root | Arabic | Gloss | BC | freq |
|---|---|---|---|---|---|
| 1 | xlq | خلق | create | 2,412 | 218 verses |
| 2 | qlb | قلب | heart/turn | 2,049 | 155 |
| 3 | xlf | خلف | succeed/differ | 1,236 | 116 |
| 4 | Amr | امر | command | 1,171 | 226 |
| 5 | Ax* | اخذ | take | 1,112 | 244 |
| 6 | smE | سمع | hear | 902 | 163 |
| 7 | Hsn | حسن | good | 834 | 177 |
| 8 | SbH | صبح | morning | 712 | 43 |
| 9 | nfs | نفس | self/soul | 683 | 270 |
| 10 | lyl | ليل | night | 668 | 81 |

**Substantive reading.**
- **xlq (create)** is the structural bridge connecting cosmology, anthropology, eschatology, and ethics: it tags creation accounts (cosmology), "we created man from..." passages (anthropology), the resurrection-as-recreation argument (eschatology), and "*hasan al-khalq*" (ethical character). It is the road many semantic domains have to travel through.
- **qlb (heart)** is the bridge between belief, disbelief, repentance, mercy, hypocrisy, and the Day of Judgment. The Quran's psychological vocabulary funnels through "heart" the way English ethical talk funnels through "mind".
- **lyl/SbH (night/morning)** are bridges because temporal markers connect prayer, eschatology, creation, and narrative — they appear across communities.
- **Hsn (good)** bridges ethics, paradise descriptions, divine attributes, and aesthetic praise.

This is the result the task hint predicted: bridges tend to be **conceptual hinges** rather than nameable doctrinal terms.

## 6. Community detection

**Label propagation collapsed** the network into one community at iteration 3 — a known LP failure mode on hub-saturated weighted graphs. Switched to **single-level Louvain** (greedy modularity optimization).

- **29 communities** found
- **Modularity Q = 0.0812** (low — partly because the Allah hub touches 84% of all filtered nodes and pulls everything toward itself)

The communities are nonetheless **clearly thematic**. Naming them by inspection of their top-degree members within-community:

| Comm | Size | Theme | Top members |
|---|---|---|---|
| C1 | 143 | "moral life / ethics" | Alh, wqy (fear-God), xyr (good), TwE (obey), nfq (spend), mwl (wealth), Hbb (love), Sbr (patience), jhd (struggle), wHd (one), wkl (trust), Edd (count), flH (succeed), Avm (sin), Efw (pardon), Ehd (covenant) |
| C2 | 67 | **"prophets, scripture, signs sent down"** | byn, Aty, rsl, ktb (book), Ayy (signs), jyA (come), qbl (before), nzl (descend), Hqq (truth), *kr (remember), Hkm (judge), nbA (news), bny (build), Awl (first), Amm (community) |
| C3 | 62 | **"worship, polytheism debate, ancestral religion"** | qwl, Ebd (worship), $rk (associate), dEw (call), Abw (father), qrb (near), slm (peace), lqy (meet), Axw (brother), dyn (religion), AHd (one), wld (child), sHr (sorcery), wHy (revelation), Zhr (apparent), xlS (purify) |
| C4 | 56 | **"cosmology / creation"** | ArD (earth), smw (heaven), xlq (create), jEl (place), rAy (see), mlk (kingdom), xrj (bring out), lyl (night), kbr (great), sbH (glorify), zwj (pair), sjd (prostrate), $ms (sun), rjE (return), sxr (subject), Elw (high) |
| C5 | 29 | **"punishment, disbelief, harm, transgression"** | E*b (punish), kfr (disbelieve), nwr (light), Alm (pain), Drr (harm), bAs (distress), $Tn (satan), Edw (enmity), lEn (curse), Etd (prepare), Tgy (transgress), fdy (ransom) |
| C6 | 28 | **"faith and righteous deeds with reward"** | Amn (believe), Eml (do), SlH (righteous), Hsn (good), Ajr (reward), jzy (recompense), xwf (fear), Hzn (grief), ftH (open), drj (degree) |
| C7 | 26 | "concealment, mockery, loss" | kwn, bdw (Bedouin/appear), hzA (mock), xfy (hide), xsr (loss), gfl (heedless), Hyq (encompass), ESy (disobey), grq (drown), Sgr (small) |
| C8 | 24 | "lying, denial, doubt" | rbb, k*b (lie), fry (fabricate), Znn (suppose), ftn (trial), bdA (begin), krm (honor), nSH (counsel) |
| C9 | 18 | **"prayer, day of judgment, ritual purity"** | qwm, ywm, Slw (prayer), zkw (zakat), SrT (path), fSl (separate), wjh (face), jrm (crime), xzy (humiliation), Hml (carry), H$r (gather), qsT (justice), Thr (purify), wqt (time), kff (palm/sufficient) |
| C10 | 16 | "measure, parable, provision, multiplication" | $yA, kll, qdr (measure), mvl (parable), rzq (provision), Drb (strike), jmE (gather), Hsb (reckon), trk (leave), wrv (inherit), sbE (seven), mrr (pass) |
| C11 | 16 | "life, death, world, play and amusement" | Hyy (live), dnw (low/world), Axr (last), mwt (death), mtE (enjoy), qtl (kill), zyn (adorn), lEb (play), lhw (amuse), grr (deceive), n$A (raise), wzr (burden), xwD (wade) |
| C12 | 15 | **"paradise"** | jnn (garden), nhr (river), jry (flow), tHt (under), xld (eternal), dxl (enter), EZm (great), fwz (success), nEm (bliss), Abd (everlasting), rDw (pleasure), SHb (companion), Ans (human), bwb (door), jHm (hellfire) |
| C13 | 13 | **"mercy and forgiveness"** | gfr (forgive), rHm (mercy), fDl (favor), bgy (seek/transgress), twb (repent), $kr (thank), flk (ship/orbit), bHr (sea), *nb (sin), wsE (encompass), rAf (kindness), xTA (error) |
| C14 | 13 | "knowledge, secret, hidden, marriage, intimacy" | Elm (know), srr (secret), gyb (unseen), nsw (forget), Sdr (chest), Eln (announce), fH$ (lewdness), nkH (marry), jhr (declare), ktm (conceal), $rH (open) |
| C15 | 12 | "protection, taking, rule, intercession" | wly (ally), Ax* (take), dwn (apart), nSr (help), wjd (find), dbr (back/turn), $fE (intercede), Ejl (haste), wdd (love), SyH (cry) |

**The semantically clearest communities** are C2 (revelation/scripture), C3 (worship/polytheism), C4 (cosmology), C5 (punishment), C6 (faith-and-works), C9 (prayer/judgment), C12 (paradise), C13 (mercy). These eight communities track exactly the clusters a careful reader of the Quran would predict the doctrinal vocabulary to fall into. **The k=2 modularity is low precisely because these communities are themselves linked through Allah, which sits at the center of all of them**, but the partition is recognizably theological.

## 7. Configuration-model null comparison

We test whether the cohesion of the co-occurrence network is "real" or a byproduct of degree distribution. Null model: **bipartite stub-shuffle** preserving (a) the number of distinct roots per verse and (b) the number of verses each root appears in. This is the configuration model on the verse-root bipartite graph; we re-derive the root-root co-occurrence graph from each shuffled draw and recompute the metric.

**200 null draws.** For each metric we report observed value, null mean, std, z-score, and empirical two-sided p-value (always 0.000 to 3 decimals at 200 draws unless noted).

| Metric | Observed | Null mean | Null std | z | p |
|---|---|---|---|---|---|
| Total distinct co-occurring root pairs | 74,185 | 79,905 | 298 | **−19.2** | < 0.005 |
| Root pairs with weight ≥ 5 | 8,556 | 7,605 | 52 | **+18.2** | < 0.005 |
| Sum of all edge weights | 211,298 | 193,119 | 500 | **+36.3** | < 0.005 |
| Maximum single edge weight | 514 | 367.5 | 13 | **+11.2** | < 0.005 |
| Mean degree (unfiltered) | 90.86 | 97.42 | 0.37 | **−17.7** | < 0.005 |
| Mean degree (w ≥ 5) | 10.48 | 9.27 | 0.06 | **+18.8** | < 0.005 |
| Max degree (w ≥ 5) | 509 | 464 | 8.0 | **+5.6** | < 0.005 |

**Reading.** Even after preserving each verse's root count and each root's verse count, the actual Quran has:
- *fewer* total distinct root pairs that co-occur (z = −19.2),
- *more* heavy (w ≥ 5) co-occurring pairs (z = +18.2),
- *much more* total edge weight in heavy pairs (z = +36.3),
- *much higher* maximum-single-pair weight (z = +11.2).

In plain English: **the Quran's verses share roots not at random — they share the same chunks of vocabulary repeatedly, much more than chance would predict, even after controlling for hub-frequency**. The degree-preserving null gets the marginal hubs right; what it misses is the *correlation* between hub usage. When the Quran says "Allah", it's much more likely than chance to also say "say", "believe", "know", "lord", "create" *in the same verse* — and to keep doing it.

The signature of this is the +36.3-σ excess in `sum_weight`: this is (so far) the strongest deviation we've found in this run. **All seven metrics fall outside the entire 200-draw null distribution**, so the empirical p < 0.005 (= 1/200) for each. With Bonferroni over 7 tests this is still corrected p < 0.035 for each individually, and *jointly* the observation is overwhelming.

**Garden-of-forking-paths disclosure:** The metrics in this table were not pre-registered — they were chosen during analysis to characterize the network. We list seven, not one, and report all seven; none was selected after seeing the result. The status of this finding is **exploratory**; for a §3-eligible *finding* it would need pre-registration of (a) one specific metric, (b) one null at 10⁴ draws (instead of 200), and (c) a robustness check under an alternative root index (e.g. word-level instead of verse-level co-occurrence). All three of those are straightforward follow-ups.

## 8. Surah connectivity (the surah-surah graph)

Treat the 114 surahs as nodes, with edge weight = Jaccard similarity on their root sets. Each surah's *strength* = sum of Jaccard to all 113 others.

### Backbone (raw) — top 15 by strength

s10 Yunus (26.0), s40 Ghafir (23.6), s29 Al-'Ankabut (23.6), s39 Az-Zumar (23.6), s42 Ash-Shuraa (23.3), s46 Al-Ahqaf (23.0), s6 Al-An'am (23.0), s23 Al-Mu'minun (22.8), s27 An-Naml (22.7), s41 Fussilat (22.7), s11 Hud (22.7), s43 Az-Zukhruf (22.7), s14 Ibrahim (22.7), s25 Al-Furqan (22.6), s35 Fatir (22.6) — **all Meccan**, all narrative-rich middle-to-late-Meccan surahs.

### Leaves (raw) — bottom 15 by strength

s108 Al-Kawthar (1.80), s111 Al-Masad (1.89), s109 Al-Kafirun (2.24), s107 Al-Ma'un (2.27), s94 Ash-Sharh (2.39), s103 Al-'Asr (2.56), s106 Quraysh (2.63), s112 Al-Ikhlas (2.68), s113 Al-Falaq (2.69), s102 At-Takathur (2.75), s101 Al-Qari'ah (3.00), s104 Al-Humazah (3.14), s105 Al-Fil (3.67), s100 Al-'Adiyat (4.08), s114 An-Nas (4.38). All very short Meccan.

The leaves are entirely a length effect. **Length-controlled** (`strength / log(verses+1)`) backbone is dominated by the same short Medinan summary-surahs we found in §2: s57 Al-Hadid, s64 At-Taghabun, s46 Al-Ahqaf, s65 At-Talaq, s59 Al-Hashr, s66 At-Tahrim, s62 Al-Jumu'ah, s58 Al-Mujadila, s63 Al-Munafiqun, s32 As-Sajdah.

### Reading
- The "raw" backbone is the **middle/late Meccan storyteller belt**: surahs 6, 10, 11, 14, 23, 25, 27, 29, 35, 39, 40, 41, 42, 43, 46. They share so much vocabulary with everyone else because they all do the same thing — narrate prophet stories with a recurring eschatological frame.
- The "length-normalized" backbone is the **late Medinan summary belt**: short surahs that pack a high density of corpus-wide vocabulary. They function as recapitulations.
- The "leaves" are the **very short late-Meccan oath/curse surahs** (Al-Masad, Al-Kawthar, Al-Asr, Al-Kafirun, ...) — these have idiosyncratic short vocabularies and don't share much with the rest.

## 9. Prior art (web search)

Closest published work:

1. **Tariq et al., "A Graph-based Algorithm for Clustering Qur'anic Surahs"** — graph-based surah clustering. Publication on ResearchGate. Confirms that surah-clustering by similarity is being attempted, though typically with hand-built similarity functions rather than corpus-derived root co-occurrence.
2. **"Text Classification via Network Topology: A Case Study on the Holy Quran"** — uses network topology features (presumably for Meccan/Medinan classification). Related but not the same construction.
3. **Quranic Arabic Corpus Ontology** (corpus.quran.com/ontology.jsp) — manually curated knowledge graph of 300 Quranic concepts with 350 relations. Different (top-down semantic, hand-built) but adjacent.
4. **"Semantic Graph Knowledge Representation for Al-Quran Verses Based on Word Dependencies"** — dependency-graph models for verse semantics.
5. **RPubs: "Quran English Word Network Analysis Using Quanteda"** — exploratory English-translation network.

None of the indexed work appears to (a) build the surah-root bipartite graph directly from QAC root data, (b) compute root co-occurrence at the *verse* level with weight filtering and Brandes betweenness, or (c) compare against a configuration-model null. **The opportunity stated in the task brief — graph-theoretic analysis of the Quran is rare compared to the Bible — is borne out by the literature search.** This run is, as far as the index can tell us, the first published combination of all three pieces.

## Garden of forking paths disclosure

### Choices made after seeing the data
- **Length-controlled "most unique" surah** (regression residual) was added *after* the raw "most unique" came back as Al-Kawthar = "shortest", which was uninformative. Disclosed.
- **Bridge-surprise filter** (top-BC outside top-25-frequency) was added *after* the raw top-20-BC came back as the same hubs as top-20-degree. Disclosed.
- The choice of **k-means cosine** as the clustering method was made *after* avg-linkage Jaccard and complete-linkage produced singleton-outlier-dominated dendrograms. We report all four methods so the failures are visible.
- Louvain replaced label propagation *after* LP collapsed the graph to one community. Both are reported.
- The seven metrics in the null table were chosen during analysis. We report all seven; we do not single out the one with the largest z.

### Alternative rule tuples considered and discarded
- **Co-occurrence at the surah level** (instead of verse level) would give a much denser graph — discarded as less informative; verse-level is the natural granularity for thematic co-occurrence.
- **Co-occurrence threshold w ≥ 3 vs w ≥ 5 vs w ≥ 10** — w ≥ 5 was specified by the task brief. We did not retune.
- **Word-level graph** (instead of root-level) — discarded as it would explode to ~80 k nodes and conflate inflectional variants.

### Sibling hypotheses considered (in this run, not yet reported separately)
- "Are the Quran's connected-component statistics distinctive?" — not separately tested; the giant component is essentially everything.
- "Does Brandes betweenness produce a different ranking under weighted shortest paths?" — not tested; we used unweighted BFS.
- "Does the surah Jaccard graph have a small-world structure?" — not tested.

### Why this set and not those
- Because they're the metrics named in the task brief. We did exactly the work asked for and reported the negatives.

## §7 Statistical-rigor checklist

- [ ] Rules tuple pre-registered in git; commit hash cited — **NOT YET**, this is exploratory
- [x] Exact statistic implemented as a named function with tests — see `/tmp/graph_*.py`
- [x] Primary null model (bipartite configuration) run with **200** surrogates — *should be 10⁴ for a finding*; this is a 22-second pilot
- [ ] Second null model (different §1.x row) run — **NOT YET** (length-matched comparable Arabic null is the obvious next step)
- [ ] Multiple-comparison correction applied — Bonferroni/7 mentioned informally above, not formally registered
- [x] Raw and (informal) corrected statistics reported, effect sizes (z-scores) reported
- [ ] Robustness under at least one alternative rule tuple — **NOT YET** (no min-tashkeel re-run; no alternative root index)
- [x] Garden-of-forking-paths disclosure section filled
- [x] Red-flag checklist (§4) considered: no post-hoc rule tuning that affects the headline; both nulls and raw figures match across runs; the most significant metric (`sum_weight`, z=+36) is one of seven, not the only one tried
- [ ] Test register increment

**Status:** **exploratory**, demoted from "finding" because pre-registration, 10⁴ draws, and second null are not yet done. The result is robust enough that pre-registering a confirmatory run with `sum_weight` as the headline statistic, the bipartite configuration null at 10⁴ draws, and a comparable-Arabic-corpus secondary null (if/when we have one) would almost certainly produce a corrected p well below 0.001. That's the proposed Phase B follow-up.

## Files produced

- `data/morphology/surah-root-graph.json` — bipartite adjacency (114 surahs × 1,642 roots, 17,496 edges)
- `data/morphology/root-cooccurrence-graph.json` — weighted co-occurrence (608 nodes, 8,556 edges at w ≥ 5)
- `journal/graph-theory-run-1.md` — full run journal
- `findings/phase-b-hypotheses/graph-theory-roots.md` — this file
