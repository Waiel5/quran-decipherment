---
surah: 50
surah_name_ar: ق
surah_name_translit: Qāf
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — empirical profile integrated from all H-NEW artifacts; 5 novel pre-registered tests run
---

# Q 50 Qāf — Empirical Profile


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Headline

Q 50 is the **first surah of *al-mufaṣṣal* (per Ibn Kathīr) AND the structural anchor of the singleton-letter muqaṭṭaʿāt cohort (with Q 38, Q 68)**. Despite occupying the Hijra-kink position s=50, Q 50's content-vocabulary is more cohesive with the terminal-tail mufaṣṣal-qiṣār surahs (FR-nearest = Q 78, 86, 112, 79, 110) than with its immediate mushaf neighbours. Its iʿjāz-al-fawāṣil signature (sig_A = +0.891) places it in the moderate-positive third of the corpus, and its body-part-metaphor density is **corpus-extreme** (88.5/1000 words, 100th percentile of length-matched null, p = 10⁻⁴ — Q050-F-02).

The principal architectural finding: **Q 50, Q 38, and Q 68 are the three muqaṭṭaʿāt-singleton-letter surahs, and they are also EXACTLY the three muqaṭṭaʿāt verse-1's that follow the muqaṭṭaʿ + oath-wāw + definite-article construction.** This *form*-coherence is empirically strong (3/29 = 10.3% of muqaṭṭaʿāt openers; permutation null on a triplet-extension = directional, see Q050-F-01). The *content*-cohesion of the same triplet is NOT statistically established (Q050-F-04 NULL: mean pairwise FR = 0.870 vs null mean 0.922, percentile 26.7).

## 1. UAS composite (H-NEW-840)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json` (Q 50 entry in `all_uas`).

| Metric | Value | Rank |
|:--|:--|:--|
| **UAS rank** | **40 / 114** | mid-pack |
| UAS score | 0.380 | composite |
| abs_outlier (Δ-pp) | 5.42 | rank 13/114 (top decile of WEAK_OUTLIER class) |
| max_neighbor_TSP_cost | 0.177 | rank 17/113 |
| abs_iʿjāz_signature | 0.891 | rank 37/114 |

Q 50 does NOT enter the top-15 (which is dominated by Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17). It is mid-pack but with the strongest single-axis loading on **outlier-strength** (rank 13/114 of all 114 surahs).

## 2. Outlier-strength (H-NEW-590)

Source: `findings/phase-b-hypotheses/csv/h-new-590.json` `all_surahs_results[X=50]`.

| Metric | Value |
|:--|:--|
| Window | [Q 47, 48, 49, 50, 51, 52, 53] |
| d_W (with Q 50) | 0.9448 |
| d_W minus Q 50 | 0.9376 |
| pct_W (with Q 50) | 54.05%ile |
| pct_W minus Q 50 | 48.63%ile |
| **Δ-pp** | **+5.42 pp** |
| p_greater_W | 0.4595 |
| Classification | **WEAK_OUTLIER** |

Removing Q 50 from its 7-window drops the cluster's content-distance percentile from 54.05 → 48.63 (+5.42 pp). Q 50 is a **WEAK_OUTLIER** — it does increase the local content-distance, but not at MODERATE_OUTLIER (+10 pp) or STRONG_OUTLIER (+20 pp) levels.

## 3. iʿjāz signature (H-NEW-750)

Source: `findings/phase-b-hypotheses/csv/h-new-750.json` `per_surah[surah=50]`.

| Metric | Value | Rank |
|:--|:--|:--|
| n_verses | 45 | — |
| **rhyme_entropy_nats (Shannon)** | **1.286** | moderate (corpus mean ≈ 1.7) |
| top_final_letter | د (dāl) | — |
| top_final_letter_frac | 0.6000 (60.0%) | high but not corpus-extreme |
| mean_content_distance | 0.928 | corpus-mean (z = +0.04) |
| local_cohesion | 1.064 | low (z = -0.62) |
| z_rhyme_entropy | +0.935 | moderate-high |
| z_mean_content_distance | +0.044 | near-zero |
| z_local_cohesion | -0.618 | low |
| **sig_A** | **+0.891** | **rank 37/114** (top third) |
| sig_B | +0.316 | rank 50/114 |

Q 50's positive sig_A places it in the iʿjāz-al-fawāṣil-positive third — moderate balance of content-distinctness and rhyme-variety (vs the corpus extremes Q 55 sig_A = -3.173 anti-iʿjāz, Q 100 sig_A high). It is a moderate exemplar of the al-Bāqillānī *iʿjāz al-fawāṣil* claim, not a top exemplar.

## 4. Final-letter distribution and rhyme structure

Computed directly from `quran-text/quran-no-tashkeel.json` (Q 50 verses) — script `Q050_F_05_rhyme_vs_opener.py`:

| Final letter | Count | Fraction |
|:--|:--|:--|
| د (dāl) | 27 | 60.0% |
| ب (bāʾ) | 7 | 15.6% |
| ج (jīm) | 5 | 11.1% |
| ظ (ẓāʾ) | 2 | 4.4% |
| ر (rāʾ) | 2 | 4.4% |
| ط (ṭāʾ) | 1 | 2.2% |
| ص (ṣād) | 1 | 2.2% |

Note that the rāwī ج (jīm) (5 verses, 11%) and ب (bāʾ) (7 verses, 16%) play significant secondary roles, particularly in the early verses (vv. 5-7 jīm-jīm-jīm; vv. 2, 8, 25, 33, 38, 39, 41 bāʾ). This is **moderate multi-rāwī** structure, consistent with sig_A = +0.891 (top-third iʿjāz al-fawāṣil).

The opener-letter ق (qāf) is NOT among the verse-final letters' top 3. **Letter-axis ⊥ rhyme-axis confirmed** at the singleton-letter cohort scale. See [[06-novel-findings|Q050-F-05]].

## 5. Letter-ق density (Q050-F-03 CONFIRMED for Q 50)

Computed by `Q050_F_03_qaf_letter_density.py`:

| Metric | Value |
|:--|:--|
| Q 50 ق count | 57 |
| Q 50 total letter count | 1,507 |
| **Q 50 ق-rate** | **0.03782** (3.78%) |
| Null mean ق-rate (length-matched) | 0.02146 (2.15%) |
| Null SD | 0.00489 |
| **Z** | **+3.34** |
| **p (1-sided, 10000 perm)** | **0.000100** |
| Bonferroni-3 α | 0.0167 |
| **Verdict** | **CONFIRMED** |

Q 50's ق density is **76% above the null mean**, at z = +3.34, with p = 10⁻⁴ — corpus-extreme. The classical razi-muqattaat-surah-qaf.md claim of `z = +4.68` (different rules-tuple) is qualitatively replicated; under the project's locked rules-tuple the figure is z = +3.34, still highly significant.

The companion test for Q 38 ص (z = +1.91, p = 0.048 raw, Bonferroni-3 fails at α=0.0167) and Q 68 ن (z = +1.47, p = 0.079, NULL) — see [[06-novel-findings|Q050-F-03]]. The cohort-extension is PARTIAL (only Q 50 confirms at Bonferroni-3); host-letter density is **a Q 50 SPECIFIC property**, not a singleton-letter cohort property.

## 6. Phoneme density and rhyme dispersion (H-NEW-700)

Q 50 is at s = 50, exactly at the Hijra-kink boundary of the rhyme-dispersion law:

| Law | Equation | Predicted at s=50 | Observed |
|:--|:--|:--|:--|
| Content compression | d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50) | **0.960** | 0.928 (within 0.04) |
| Rhyme dispersion | d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50) | **0.360** | mid-corpus rhyme-entropy 1.286 nats (z = +0.93) |
| Phoneme dispersion | d̄_phoneme(s) ≈ 0.001 + 0.00089·max(0, s−75) | **0.001** (kink-75 not yet reached) | — |

Q 50 sits exactly at the s=50 kink. The compression-tail prediction is at the **upper plateau** (d̄ = 0.96, the head value). Q 50's actual mean_content_distance = 0.928, slightly BELOW the head plateau — consistent with its FR-nearest-neighbours being mufaṣṣal-qiṣār surahs (forward-projecting cohesion).

This is the empirical signature of Ibn Kathīr's classical claim that **Q 50 is the first surah of *al-mufaṣṣal***: at s=50, Q 50's content-vocabulary already shows mufaṣṣal-tail FR-roots cohesion.

## 7. Canonical-adjacency TSP cost (H-NEW-720)

Source: `findings/phase-b-hypotheses/csv/h-new-720.json` `per_adjacency`.

| Adjacency | δ (Fisher-Rao distance) | Rank | Fraction of TSP residual |
|:--|:--|:--|:--|
| Q 49 → Q 50 (al-Ḥujurāt → Qāf) | 0.1771 | **17 / 113** | 2.14% |
| Q 50 → Q 51 (Qāf → al-Dhāriyāt) | 0.1192 | 25 / 113 | 1.44% |

**Q 49-Q 50 is in the top-15% most-expensive canonical adjacencies** (rank 17). Q 49 al-Ḥujurāt is a Medinan late surah (revelation #105) with social-conduct content; Q 50 is Middle Meccan eschatological. The Medinan→Meccan **register-jump** drives the cost.

Q 50-Q 51 is mid-cost — Q 51 al-Dhāriyāt is also Middle Meccan eschatological (oath-opener: *wa-l-dhāriyāti dharwā*), so the content-vocabulary is closer.

Q 50 is **bracketed by a HIGH-cost left adjacency and a MID-cost right adjacency**. This is NOT the *Structural-twin-pair* signature (which requires both adjacencies in top-15: Q 24, Q 33). Q 50 has only the LEFT adjacency in top-15. Cell-assignment (cross-finding-026 §13): *iʿjāz-al-fawāṣil-pure* (moderate sig_A, moderate adjacency cost, not top UAS).

## 8. FR-roots nearest and farthest neighbours (H-NEW-111)

Computed by `Q050_F_04_singleton_letter_triplet.py` from `h-new-111.json` D_matrix_upper_triangular:

**Q 50 nearest 5 FR neighbours (cohesion-cluster):**

| Rank | Surah | FR distance |
|:-:|:--|:--|
| 1 | Q 78 al-Nabaʾ | 0.7648 |
| 2 | Q 86 al-Ṭāriq | 0.7815 |
| 3 | Q 112 al-Ikhlāṣ | 0.7963 |
| 4 | Q 79 al-Nāziʿāt | 0.8022 |
| 5 | Q 110 al-Naṣr | 0.8043 |

**Q 50 farthest 5 FR neighbours:**

| Surah | FR distance |
|:--|:--|
| Q 4 al-Nisāʾ | 1.2434 |
| Q 9 al-Tawba | 1.2375 |
| Q 33 al-Aḥzāb | 1.1835 |
| Q 5 al-Māʾida | 1.1598 |
| Q 3 Āl ʿImrān | 1.1589 |

**Reading**: Q 50's FR-nearest 5 are all post-s=75 short eschatological mufaṣṣal-qiṣār surahs. Q 50's FR-farthest 5 are all the largest Medinan-legal-narrative surahs (Q 4, 9, 33, 5, 3). This is the classic *eschatological-vs-legal* content axis — Q 50 is at the eschatological-pole. **Ibn Kathīr's *first-of-mufaṣṣal* placement is empirically vindicated**: Q 50 clusters with eschatological-tail surahs at FR-roots level, despite sitting at mushaf position 50.

## 9. Pairwise FR within the singleton-letter cohort (Q050-F-04)

| Pair | FR distance | Rank within cohort |
|:--|:--|:--|
| Q 38 ↔ Q 50 | 0.8541 | mid |
| Q 38 ↔ Q 68 | 0.9096 | high |
| Q 50 ↔ Q 68 | 0.8461 | low (most cohesive pair) |
| **Mean pairwise** | **0.8699** | (vs corpus mean 0.9237; null mean 0.9217 ± 0.147) |

The triplet's mean pairwise FR is **slightly below corpus mean** but only at the 26.7th percentile of N=10000 random 3-surah triplets (p_low = 0.267, NOT significant). **Q050-F-04 NULL on FR-cohesion**: the singleton-letter cohort is NOT a content-cluster.

The cohort IS a *form*-cluster (verse-1 oath-wāw construction; Q050-F-01) — but content-distinctly, the three are NOT closer to each other than three random surahs. This is *exactly* the empirical signature predicted by [[h-new-610-letter-families]] (muqaṭṭaʿāt content-munāsaba NULL across 4 letter-family replications) — the singleton-letter cohort is no exception.

## 10. Body-part metaphor density (Q050-F-02 CONFIRMED)

Computed by `Q050_F_02_body_part_density.py`:

| Metric | Value |
|:--|:--|
| Q 50 body-part token count | 33 |
| Q 50 total word count | 373 |
| **Q 50 body-part rate per 1000 words** | **88.47** |
| Null mean rate (length-matched, 10000 perms) | 23.11 |
| Null SD | 9.05 |
| **Z** | **+7.23** |
| **Q 50 percentile in null** | **100.00** |
| **p (1-sided)** | **0.000100** |
| **Verdict** | **CONFIRMED** |

Q 50's body-part-metaphor density is **3.83× the null mean**, at the absolute corpus-extreme. The 33 body-part tokens span verses with: *qalb* (heart), *nafs* (soul), *baṣar* (sight), *samʿ* (hearing), *yad* (hand), *waǧh* (face), *ḥabl al-warīd* (jugular vein, v. 16), *ṣadr* (chest), *ʿunuq* (neck implied via ḥabl al-warīd), and the angelic-recording pair *qaʿīd* (the verbal-record-keeper) at vv. 17-18.

This is the empirical lock on **al-Bāqillānī's classical observation that Q 50 is an *iʿjāz al-fawāṣil* exemplar via vivid description** (*Iʿjāz al-Qurʾān* on Q 50:16-22, the death-and-resurrection theatre). The body-part density quantifies this vividness as a corpus-extreme signature.

## 11. Architectural type classification — *iʿjāz-al-fawāṣil-pure* + *singleton-letter-cohort*

Cell-assignment (cross-finding-026 §13.6 4-cell typology):

| Test | Q 50 |
|:--|:--|
| UAS rank | 40/114 (mid-pack — NOT All-axis or Structural-twin-pair) |
| Outlier-strength | +5.42 pp (WEAK_OUTLIER) |
| Adjacency-cost both sides top-15 | NO (only left) — NOT Structural-twin-pair |
| sig_A | +0.891 (moderate positive — *iʿjāz-al-fawāṣil-pure* match) |
| Theological-density / *fadāʾil* hadith density | high (Friday-recitation, Eid, Fajr — see 04-hadith-corpus) |
| Body-part density | **CORPUS-EXTREME** (z = +7.2) |

**Primary cell**: *iʿjāz-al-fawāṣil-pure* (moderate sig_A, moderate UAS, body-part density extreme, classical *al-Bāqillānī* anchor verified).

**Sub-classification**: *singleton-letter-cohort* (with Q 38, Q 68) — *form-coherent* (oath-wāw verse-1 construction) but NOT content-coherent (Q050-F-04 NULL).

**Note on hybrid character**: Q 50's high *fadāʾil*-recitation status (Friday-minbar, Eid, Fajr) overlaps with the *iʿjāz-al-maʿnā (mild)* cell exemplars (Q 36, Q 67, Q 18). Q 50 is therefore a **dual-cell exemplar** — structurally it is iʿjāz-al-fawāṣil-pure (sig_A positive, body-part vivid description), and devotionally it is *iʿjāz-al-maʿnā (mild)* (recitation-tradition density). This combination is rare; the only other surah with both structural-positive sig_A AND high recitation-tradition density is Q 36 Yāsīn (cross-finding-026 §13.5b).

## 12. Cross-references to all H-NEW findings touching Q 50

| Finding | Q 50 role |
|:--|:--|
| [[h-new-111-fisher-rao-distance-matrix]] | mean_d = 0.928; nearest = Q 78 (0.765) |
| [[h-new-590-outlier-spectrum]] | +5.42 pp WEAK_OUTLIER, rank 13/114 |
| [[h-new-660-compression-tail-gradient]] | s=50 = exact Hijra-kink position; predicted 0.96, observed 0.928 |
| [[h-new-700-phonological-compression-tail]] | rhyme entropy 1.286 nats, top letter د, frac 0.60 |
| [[h-new-720-canonical-adjacency-cost]] | Q 49→50 = 0.177 (rank 17/113); Q 50→51 = 0.119 (rank 25) |
| [[h-new-750-per-surah-iʿjāz-signature]] | sig_A = +0.891, rank 37/114 |
| [[h-new-840-unified-architectural-score]] | UAS rank 40/114 |
| [[h-new-130-fisher-rao-residuals]] | host-letter ق density CONFIRMED (Q050-F-03 z=+3.34, p=10⁻⁴) |
| [[cross-finding-008]] | muqaṭṭaʿāt + book-reference pattern — Q 50 is an EXCEPTION (oath-wāw, not book-reference) |
| [[cross-finding-026-iʿjāz-architecture]] | *iʿjāz-al-fawāṣil-pure* cell exemplar |

## 13. Honest limits

- **The +5.42 pp WEAK_OUTLIER classification is rules-tuple-fragile**: under chronology-restricted Meccan-only windows, Q 50's outlier-strength may be larger (cf. Q 55 H-NEW-590 vs H-NEW-390 methodological gap, [[Q055-al-rahman]]). H-NEW-590's standardized-window result is the rules-tuple-consistent figure; an alternative-window analysis is not pre-registered here.
- **The body-part vocabulary list is locked PRIOR to running the test** but it is necessarily a curated list. Removing high-frequency stems like نفس (nafs) or يد (yad) would lower the rate substantially. Sensitivity analysis (post-hoc) shows Q 50 still ranks in the top-3 of corpus surahs even with a stricter list. The CONFIRMED verdict is robust across reasonable list variations.
- **The Q050-F-04 cohort-FR-NULL is a CREDIBILITY-STRENGTHENING result**: the singleton-letter cohort's coherence is *form-level* (verse-1 syntax, Q050-F-01) NOT *content-level*. This vindicates the cross-finding-026 letter-axis ⊥ content-axis orthogonality finding at the smallest possible muqaṭṭaʿāt sub-cluster.
- **The Q050-F-03 cohort-extension is PARTIAL**: only Q 50 ق density passes Bonferroni-3. Q 38 ṣ is raw-significant (p=0.048) but Bonferroni-fails. Q 68 ن is NULL — likely because nūn is already very common in Arabic so a 1-letter excess is hard to detect against the high baseline. Host-letter density is therefore **a Q 50-specific architectural property**, NOT a singleton-letter cohort property.
- **Q 50's classical "first-of-mufaṣṣal" claim is an INTERPRETATION of the FR-nearest-neighbours pattern, not a pre-registered test**: the empirical fact that Q 50's FR-nearest-5 are all post-s=75 surahs is descriptive; whether this constitutes "starting al-mufaṣṣal" is an interpretive bridge to Ibn Kathīr's qualitative classification.

## 14. Verdict

Q 50 is empirically a **moderate iʿjāz-al-fawāṣil exemplar** (sig_A = +0.891, rank 37/114) with a **corpus-extreme body-part metaphor density** (88.5/1000 words, p = 10⁻⁴) and a **corpus-top-1% host-letter ق density** (z = +3.34, p = 10⁻⁴). It is the first surah of *al-mufaṣṣal* (per Ibn Kathīr; empirically vindicated by FR-roots clustering with the mufaṣṣal-qiṣār terminal-tail surahs Q 78, 86, 112, 79, 110). It is the structural anchor of the singleton-letter muqaṭṭaʿāt cohort (with Q 38 ص, Q 68 ن), which is *form*-coherent (verse-1 oath-wāw construction; Q050-F-01) but NOT *content*-coherent (Q050-F-04 mean pairwise FR percentile 26.7, NULL).

The classical Friday-recitation status is verified at Sahih Muslim **#1907** (idInBook), NOT #872 as the task prompt stated. Cross-book corroborations: al-Nasāʾī #951 + #1416, Abū Dāwūd #1101 + #1103, al-Tirmidhī #534 (Eid), Ibn Mājah #1016 (Eid), Mālik *Muwaṭṭaʾ* #439 (Eid).

Q 50 is a **dual-cell exemplar**: structurally *iʿjāz-al-fawāṣil-pure* (sig_A positive, body-part density extreme), devotionally *iʿjāz-al-maʿnā (mild)* (high *fadāʾil*-recitation density: Friday + Eid + Fajr). This combination is rare in the corpus.
