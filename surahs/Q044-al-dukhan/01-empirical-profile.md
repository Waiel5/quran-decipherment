---
surah: 44
surah_name: al-Dukhān
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: HM-7 minimum UAS (97/114); shortest; only 2 rhyme letters
---

# Q 44 al-Dukhān — empirical profile

## 1. Headline metrics

| Metric | Value | Provenance |
|:--|:--|:--|
| UAS score | −1.882 | h-new-840 |
| UAS rank | **97 / 114** (HM-7 minimum) | h-new-840 |
| |outlier| | 1.44 | h-new-840 |
| max neighbor TSP cost | 0.1112 | h-new-840 |
| |iʿjāz signature| | 0.167 (low) | h-new-840 |
| sig_A (signed) | −0.17 (near-zero) | brief |
| Outlier Δ (signed) | +1.44 (mild outlier) | brief |
| Rhyme entropy | 0.818 bits | computed |
| Top rāwī | ن (44/59, 75%) | computed |
| Distinct rhyme letters | **2 only (ن, م)** | computed |

## 2. Why UAS=97 (HM-7 minimum)?

UAS = z(|outlier|) + z(max_TSP_cost) + z(|iʿjāz|).

For Q 44:
- z(|outlier|) ≈ near-zero (1.44 is small)
- z(max_TSP_cost) ≈ negative (0.1112 is below corpus mean)
- z(|iʿjāz|) ≈ strongly negative (0.167 is among the lowest in corpus)

Net: −1.882, ranking 97/114.

The dominant factor is **iʿjāz signature near-zero** (|sig|=0.167). Q 44 has the lowest iʿjāz signature magnitude in HM-7 — its rhetorical-fawāṣil pattern is essentially flat (neither pro nor anti-iʿjāz). This is consistent with its **2-letter monorhyme**: a near-uniform rhyme cannot generate either positive or negative iʿjāz signature.

## 3. Word-count compression

Q 44: 364 words / 59 verses = **6.17 words/verse**.

Compare to other HM-7 surahs:
- Q 40 Ghāfir: 1296 / 85 = 15.25 words/verse
- Q 41 Fuṣṣilat: 838 / 54 = 15.52
- Q 42 al-Shūrā: 932 / 53 = 17.58
- Q 43 al-Zukhruf: 870 / 89 = 9.78
- Q 44 al-Dukhān: 364 / 59 = **6.17 — HM-7 minimum**
- Q 45 al-Jāthiyah: 512 / 37 = 13.84
- Q 46 al-Aḥqāf: 676 / 35 = 19.31

Q 44 is **the most compressed HM-7 surah** (shortest verses on average). This is consistent with its content register: rapid-fire eschatological warning + compact narrative + paradise/hellfire description — content modes that favor short verses.

The compression also explains the low rhyme entropy (0.818): short verses have fewer terminal-vowel options, biasing toward dominant rhyme suffixes.

## 4. Cohesion within HM-B

HM-B {Q 43, 44, 45, 46}: d̄_FR = 0.8665 at 24.29%ile.

Q 44 is content-cohesive with HM-B. It shares the eschatological-paraenetic register with the rest of HM-B and the warning-cosmic block with Q 41 (across the bifurcation).

## 5. iʿjāz signature

- sig_A = −0.17 (essentially zero)
- |iʿjāz| = 0.167 (low magnitude)

The near-zero sig_A is informative: Q 44 sits at the **iʿjāz-axis origin**, neither pro nor anti-Bāqillānī fawāṣil. Functionally, the surah's prosody is so uniform (2 rhymes, monorhyme-dominant) that the iʿjāz instrument (designed to detect verse-end rhetorical *variation*) returns near-zero.

## 6. Compression-tail position (s=44, intra-50)

Q 44 lies in the *intra-50* region. Its content compression (6.17 words/verse) is **already well below the s>50 compression-tail kink**. Q 44 is therefore a **pre-compression-tail-zone exception** — a surah at s=44 (where the compression-tail laws have not yet kicked in) that nonetheless exhibits compression-tail-like properties.

This is **a novel observation (this session, post-hoc, MW-7 capped)**: Q 44 may be a *pre-tail-zone compression outlier* — short verses, low-entropy rhyme, low iʿjāz — features that empirically dominate s>75 surahs but already manifest in Q 44. Replication needed via word-count verse-length analysis.

## 7. Adjacency

max neighbor TSP cost = 0.1112 (mid-low). Q 44 fits canonically between Q 43 and Q 45 cheaply — the HM-B internal adjacency is uniform.

## 8. Architectural classification

| Axis | Position |
|:--|:--|
| Structural-iʿjāz | **flat** (sig_A=−0.17 near-origin; UAS rank 97) |
| Theological-iʿjāz (al-Khaṭṭābī) | not specifically anchored |
| Compression-tail | NOT s>50, but pre-compression-tail compression-like properties |
| Outlier | mild (Δ=+1.44) |
| Cluster role | **HM-B middle; shortest HM-7 surah; densest** |

## 9. Honest limits

1. UAS rank 97 places Q 44 in the **lower 15%** of the corpus — the surah is empirically un-distinctive on UAS. Its theological/narrative significance (Layla al-Qadr, smoke-sign, zaqqūm imagery) is NOT captured by UAS.
2. The "pre-compression-tail" observation is post-hoc; needs MW-7 replication.
3. The 2-letter rhyme alphabet may be partially driven by short-verse mechanics (less terminal-vowel diversity in short verses), not by intentional monorhyme choice.

## 10. Cross-references

- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]]
- [[Q043-al-zukhruf/01-empirical-profile|Q 43]] — opening-formula twin
- [[Q045-al-jathiyah/01-empirical-profile|Q 45]] — following HM-B neighbor
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 97
- [[h-new-770-verse-length-compression-tail|H-NEW-770]] — compression-tail context
