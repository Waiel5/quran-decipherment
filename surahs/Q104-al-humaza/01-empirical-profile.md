---
surah: 104
file_type: empirical-profile
date_last_updated: 2026-05-09
---

# Q 104 al-Humaza — Empirical profile

All numbers below are LOCKED from pre-computed H-NEW JSONs (no fresh computation).

## 1. Length / token tallies (no-tashkeel)

| Quantity | Value | Source |
|:--|:--|:--|
| Verses | 9 | `data/hafs-verse-counts.tsv` |
| Words | 34 | `quran-text/quran-no-tashkeel.json` (computed) |
| Letters (ء-ي) | 134 | computed |
| Words / verse (mean) | 3.78 | derived |
| Letters / verse (mean) | 14.9 | derived |

## 2. Per-verse breakdown

| v | words | letters | text | rāwī |
|:-:|:-:|:-:|:--|:-:|
| 1 | 4 | 14 | ويل لكل همزة لمزة | ـة |
| 2 | 4 | 16 | الذي جمع مالا وعدده | ـه |
| 3 | 4 | 15 | يحسب أن ماله أخلده | ـه |
| 4 | 5 | 17 | كلا ۖ لينبذن في الحطمة | ـة |
| 5 | 4 | 16 | وما أدراك ما الحطمة | ـة |
| 6 | 3 | 14 | نار الله الموقدة | ـة |
| 7 | 4 | 18 | التي تطلع على الأفئدة | ـة |
| 8 | 3 | 14 | إنها عليهم مؤصدة | ـة |
| 9 | 3 | 10 | في عمد ممددة | ـة |

Final-letter distribution (raw): ـة × 7, ـه × 2 → top fraction 0.778. Under H-NEW-750 fold-rule (ـة → ـه), top fraction 1.000, rhyme entropy 0.000 nats.

## 3. H-NEW-locked architectural metrics

From `findings/phase-b-hypotheses/csv/h-new-750.json` (per_surah[103]):

| Metric | Value | Rank/114 |
|:--|:--:|:-:|
| rhyme_entropy_nats | 0.000 | tied lowest |
| top_final_letter | ه (post-fold) | — |
| top_final_letter_frac | 1.000 | tied highest |
| mean_content_distance | 0.793 | mid |
| local_cohesion (z) | +3.029 | top decile |
| sig_A | −0.110 | 66/114 |
| sig_B | +0.662 | 39/114 |

From `findings/phase-b-hypotheses/csv/h-new-840.json`:

| Metric | Value | Rank/114 |
|:--|:--:|:-:|
| UAS | −2.162 | 104/114 |
| abs_outlier (Δ%) | 0.00 | NULL (size-7 cluster) |
| max_cost | 0.116 | — |
| abs_ijaz | 0.110 | — |

From `findings/phase-b-hypotheses/csv/h-new-590.json`:

- Window: [101, 102, 103, 104, 105, 106, 107]
- Δ% (W → W − {Q 104}): 0.00 — NULL outlier classification
- p_greater_W: 1.000 (NULL)

H-NEW-590 returns NULL for Q 104 because the [101-107] window is a tight cluster centered on Q 104; removing Q 104 does not shift the window. This is structural, not a Q 104 weakness — Q 104 is INSIDE a tight cluster, so it cannot be the outlier OF that cluster.

## 4. FR-distance neighborhood (from H-NEW-111)

Top-8 FR-roots nearest neighbors:

| Rank | Surah | d_FR |
|:-:|:--|:-:|
| 1 | Q 111 al-Masad | 0.268 |
| 2 | Q 108 al-Kawthar | 0.270 |
| 3 | Q 112 al-Ikhlāṣ | 0.294 |
| 4 | Q 106 Quraysh | 0.305 |
| 5 | Q 103 al-ʿAṣr | 0.312 |
| 6 | Q 94 al-Sharḥ | 0.318 |
| 7 | Q 113 al-Falaq | 0.323 |
| 8 | Q 107 al-Māʿūn | 0.324 |

All top-8 are in Q 93-114 short-mufaṣṣal-tail. Q 104 sits inside a 22-surah continuous tail-cluster.

## 5. H-NEW-1190 cluster membership

H-NEW-1190 = {Q 69, 74, 77, 82, 83, 86, 90, 97, 101, **104**}. Each member contains *wa-mā adrāka mā X* meta-question.

Per-member mean-distance to other 9 cluster members (computed from H-NEW-111 D-matrix):

| Internal rank | Surah | mean d to other 9 |
|:-:|:--|:-:|
| 1 | Q 101 al-Qāriʿah | 0.5232 |
| **2** | **Q 104 al-Humaza** | **0.5262** |
| 3 | Q 97 al-Qadr | 0.5562 |
| 4 | Q 86 al-Ṭāriq | 0.5660 |
| 5 | Q 90 al-Balad | 0.5842 |
| 6 | Q 82 al-Infiṭār | 0.5953 |
| 7 | Q 83 al-Muṭaffifīn | 0.6487 |
| 8 | Q 77 al-Mursalāt | 0.7032 |
| 9 | Q 74 al-Muddaththir | 0.7377 |
| 10 | Q 69 al-Ḥāqqa | 0.7425 |

**Q 104 is rank 2/10** within H-NEW-1190 (only Q 101 al-Qāriʿah is closer to centroid).

Cluster cohesion replication: within-pair mean = 0.6183; uniform-10-of-114 null mean = 0.9232 ± 0.0653; one-sided p = 0.00080 (this session, 10K perms, seed 20260509). Original publication p = 0.00068 — replicates.

## 6. Adjacency profile

From `findings/phase-b-hypotheses/csv/h-new-720.json`:

| Pair | delta_raw | rank/113 | classification |
|:--|:-:|:-:|:--|
| Q 103 → Q 104 | 0.116 | 88/113 | expensive (top-decile) |
| Q 104 → Q 105 | 0.061 | 54/113 | near-median |

Q 103→Q 104 is a relative seam-cost-pump within the otherwise-cheap mufaṣṣal-qiṣār ring. Q 104→Q 105 is unremarkable.

## 7. Lexical hapax-class profile

From `data/morphology/root-index.json`:

| Root | Gloss | Surahs | Total occurrences | Q 104 share |
|:--|:--|:-:|:-:|:-:|
| HTm | "to crush" → al-Ḥuṭamah | 5 | 6 | 33.3% (2/6) |
| hmz | "to slander/strike" | 3 | 3 | 33.3% (1/3) |
| lmz | "to backbite" | 3 | 4 | 25.0% (1/4) |
| Emd | "pillar/column" | 7 | 7 | 14.3% (1/7) |
| ASd | (none — text uses muʾṣadah; root sd or sdy) | — | — | — |
| fAd | "heart/innermost" | 13 | 16 | 6.3% (1/16) |

Q 104 holds the corpus-share lead on three roots simultaneously (HTm, hmz, lmz), each among the rare-vocabulary tier. None is strictly hapax (vs Q 105/106/107) but the cluster-density is high.

## 8. Sources

- `findings/phase-b-hypotheses/csv/h-new-111.json` — Fisher-Rao matrix
- `findings/phase-b-hypotheses/csv/h-new-590.json` — outlier-spectrum
- `findings/phase-b-hypotheses/csv/h-new-720.json` — TSP residuals
- `findings/phase-b-hypotheses/csv/h-new-750.json` — per-surah iʿjāz signatures
- `findings/phase-b-hypotheses/csv/h-new-840.json` — UAS
- `data/morphology/root-index.json` — root index
- `data/morphology/surah-root-graph.json` — surah-root bipartite graph
