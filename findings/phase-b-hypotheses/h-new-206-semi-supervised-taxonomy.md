> **DEMOTED 2026-08-09 — BOTH INFERENCES WITHDRAWN.** Inference (b) is length-confounded:
> `surah_length` is one of the clustering features, and muqaṭṭaʿāt surahs are 3.3x longer at the
> median (85 vs 26 verses), so the chi-square partly answers itself. Inference (a) is a
> max-over-7 silhouette (0.2144) against a fixed 0.2 cutoff with no multiplicity correction;
> the other six k values all fall below it. See [[AUDIT-H-NEW-206-LENGTH-CONFOUND]].
> One fact survives, as a LENGTH result and POST-HOC: no muqatta'at surah is among the 40
> shortest (0/29, exact P = 3.06e-7).

# [[h-new-206-semi-supervised-taxonomy|H-NEW-206]] — Semi-supervised surah taxonomy (results)

**seed**: 20260419 | **Bonferroni k** = 2 | α_bon = 0.0250

## Silhouette scores (k-means)

| k | silhouette | Calinski-Harabasz | inertia |
|---:|---:|---:|---:|
| 3 | 0.2144 | 27.89 | 1593.30 |
| 4 | 0.1327 | 21.76 | 1502.49 |
| 5 | 0.1843 | 18.96 | 1411.87 |
| 6 | 0.1664 | 17.41 | 1325.47 |
| 7 | 0.1477 | 16.55 | 1241.60 |
| 8 | 0.1615 | 15.67 | 1176.60 |
| 10 | 0.1692 | 15.00 | 1041.80 |

## HDBSCAN

| min_cluster_size | n_clusters_found | n_noise | silhouette |
|---:|---:|---:|---:|
| 3 | 7 | 69 | 0.3030 |
| 5 | 2 | 66 | 0.4113 |
| 7 | 0 | 114 | nan |

**Best k (silhouette)** = 3, silhouette = 0.2144

- Inference (a) silhouette > 0.2 at α_bon = 0.0250: **PASS**
- Inference (b) χ²(cluster × is-muq): p = 2.15e-12 at α_bon = 0.0250: **PASS**

## Cluster centers (interpretation)

### Cluster 0 — size 23

**Best classical match**: musabbiḥāt (F1 = 0.33)
**Feature tags**: long-verse, legal-heavy, eschatology-heavy

Top distinctive features (|Δ from grand mean|):

| feature | cluster mean | grand mean | Δ |
|---|---:|---:|---:|
| allah_density | 119 | 37.8 | +80.9 |
| noldeke_order | 101 | 57.5 | +43.8 |
| legal_density | 25.1 | 11.2 | +13.9 |
| divine_name_density | 19.2 | 9.38 | +9.83 |
| mean_verse_length | 19.9 | 10.9 | +9.07 |
| surah_length | 45.8 | 54.7 | -8.92 |

**Members** (first 15): 4, 5, 8, 9, 22, 24, 31, 33, 35, 47, 48, 49, 57, 58, 59 … (+8 more)

Classical-label overlaps:

| label | inter | target-size | recall | precision |
|---|---:|---:|---:|---:|
| ṭiwāl | 3 | 7 | 0.43 | 0.13 |
| mi'ūn | 0 | 8 | 0.00 | 0.00 |
| mathānī | 8 | 32 | 0.25 | 0.35 |
| mufaṣṣal | 12 | 66 | 0.18 | 0.52 |
| ḥawāmīm | 0 | 7 | 0.00 | 0.00 |
| musabbiḥāt | 5 | 7 | 0.71 | 0.22 |
| al-R-cluster | 0 | 5 | 0.00 | 0.00 |

### Cluster 1 — size 36

**Best classical match**: mathānī (F1 = 0.68)
**Feature tags**: prophet-narrative-heavy, muq-rich

Top distinctive features (|Δ from grand mean|):

| feature | cluster mean | grand mean | Δ |
|---|---:|---:|---:|
| surah_length | 103 | 54.7 | +48.5 |
| noldeke_order | 72.7 | 57.5 | +15.2 |
| eschat_density | 19.4 | 13 | +6.43 |
| allah_density | 33.5 | 37.8 | -4.26 |
| qul_density | 8.2 | 4.41 | +3.79 |
| prophet_density | 7 | 3.3 | +3.69 |

**Members** (first 15): 2, 3, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 … (+21 more)

Classical-label overlaps:

| label | inter | target-size | recall | precision |
|---|---:|---:|---:|---:|
| ṭiwāl | 4 | 7 | 0.57 | 0.11 |
| mi'ūn | 8 | 8 | 1.00 | 0.22 |
| mathānī | 23 | 32 | 0.72 | 0.64 |
| mufaṣṣal | 1 | 66 | 0.02 | 0.03 |
| ḥawāmīm | 6 | 7 | 0.86 | 0.17 |
| musabbiḥāt | 1 | 7 | 0.14 | 0.03 |
| al-R-cluster | 5 | 5 | 1.00 | 0.14 |

### Cluster 2 — size 55

**Best classical match**: mufaṣṣal (F1 = 0.88)
**Feature tags**: short-verse

Top distinctive features (|Δ from grand mean|):

| feature | cluster mean | grand mean | Δ |
|---|---:|---:|---:|
| allah_density | 6.75 | 37.8 | -31 |
| noldeke_order | 29.2 | 57.5 | -28.3 |
| surah_length | 26.7 | 54.7 | -28 |
| eschat_density | 5.91 | 13 | -7.1 |
| divine_name_density | 2.98 | 9.38 | -6.41 |
| mean_verse_length | 4.85 | 10.9 | -6.02 |

**Members** (first 15): 1, 44, 50, 51, 52, 53, 54, 55, 56, 68, 69, 70, 71, 72, 73 … (+40 more)

Classical-label overlaps:

| label | inter | target-size | recall | precision |
|---|---:|---:|---:|---:|
| ṭiwāl | 0 | 7 | 0.00 | 0.00 |
| mi'ūn | 0 | 8 | 0.00 | 0.00 |
| mathānī | 1 | 32 | 0.03 | 0.02 |
| mufaṣṣal | 53 | 66 | 0.80 | 0.96 |
| ḥawāmīm | 1 | 7 | 0.14 | 0.02 |
| musabbiḥāt | 1 | 7 | 0.14 | 0.02 |
| al-R-cluster | 0 | 5 | 0.00 | 0.00 |

## Hub surah cluster membership

| surah | name | primary? | cluster | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 | k=10 |
|---:|---|:-:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | Al-Baqarah | yes | 1 | 1 | 3 | 1 | 0 | 4 | 7 | 2 |
| 3 | Ali 'Imran | yes | 1 | 1 | 3 | 1 | 0 | 4 | 7 | 2 |
| 59 | Al-Hashr | yes | 0 | 0 | 1 | 3 | 3 | 2 | 0 | 5 |
| 62 | Al-Jumu'ah | yes | 0 | 0 | 1 | 3 | 3 | 2 | 0 | 5 |
| 18 | Al-Kahf | no | 1 | 1 | 0 | 2 | 2 | 1 | 1 | 6 |
| 36 | Ya-Sin | no | 1 | 1 | 0 | 2 | 2 | 1 | 1 | 6 |
| 50 | Qaf | no | 2 | 2 | 0 | 2 | 2 | 0 | 1 | 0 |
| 68 | Al-Qalam | no | 2 | 2 | 2 | 0 | 1 | 0 | 2 | 1 |