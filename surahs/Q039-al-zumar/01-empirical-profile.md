---
surah: 39
file_type: empirical-profile
metric_sources:
  - findings/phase-b-hypotheses/csv/h-new-111.json
  - findings/phase-b-hypotheses/csv/h-new-590.json
  - findings/phase-b-hypotheses/csv/h-new-700.json
  - findings/phase-b-hypotheses/csv/h-new-720.json
  - findings/phase-b-hypotheses/csv/h-new-750.json
  - findings/phase-b-hypotheses/csv/h-new-840.json
  - findings/phase-b-hypotheses/csv/h-new-950.json
  - findings/phase-b-hypotheses/csv/h-new-111b.json
---

# Q 39 al-Zumar — Empirical Profile

This document integrates every available H-NEW per-surah metric for Q 39 against canonical project findings. All values cite the source JSON file; numerical claims are computed, not asserted from memory.

## 1. Anchor counts

| Metric | Q 39 value | Source |
|:--|:--|:--|
| Verses | 75 | `quran-text/quran-no-tashkeel.json` (verified) |
| Orthographic words (waqf-stripped, tashkeel-stripped) | 1,177 | computed |
| Arabic-letter graphemes | 4,869 | computed |
| Mean verse-length (words) | 15.69 | computed |
| Median verse-length | 14 | computed |
| Verse-length stdev | 8.02 | computed |
| Min / Max verse-length | 4 / 36 | computed |

## 2. Fisher-Rao distance metrics (root-distribution, h-new-111)

The Fisher-Rao 114×114 root-distribution distance matrix from `findings/phase-b-hypotheses/csv/h-new-111.json` (CONFIRMED-revolutionary anchor, z = -11.46, the mushaf is information-geodesic-optimal) provides Q 39's full geometric profile:

### 2.1 Mean and median FR distance

| Statistic | Value |
|:--|:--|
| Mean FR distance to all 113 other surahs | 1.0149 |
| Median FR distance | 1.0210 |
| Max FR distance | 1.3088 |
| **FR-centroid rank** | **91 / 114** |

Q 39 sits at the periphery of the Fisher-Rao centroid — only 23 surahs are MORE peripheral. This is consistent with Q 39's specialized tawḥīd-eschatology profile (intensive divine-name + sincere-devotion + zumar-throng vocabulary creates a distinctive root-signature relative to the corpus).

### 2.2 Q 39's nearest neighbors

| Rank | Surah | FR distance | Note |
|:--|:--|:--|:--|
| 1 | Q 16 al-Naḥl | 0.7538 | Late Meccan, broad tawḥīd-eschatology |
| 2 | Q 40 Ghāfir | 0.7953 | next mushaf-surah, Hawamim, tanzīl-cluster co-member |
| 3 | Q 10 Yūnus | 0.8003 | Late Meccan, tawḥīd + qul-cluster |
| 4 | Q 6 al-Anʿām | 0.8035 | Late Meccan, longest pre-Hawamim |
| 5 | Q 29 al-ʿAnkabūt | 0.8215 | Late Meccan, ʿibāda + ikhlāṣ |
| 6 | Q 13 al-Raʿd | 0.8253 | Medinan/Late Meccan, scriptural |
| 7 | Q 41 Fuṣṣilat | 0.8278 | Hawamim, tanzīl-cluster |
| 8 | Q 3 Āl ʿImrān | 0.8285 | Medinan, scripture-themed |
| 9 | Q 14 Ibrāhīm | 0.8412 | Late Meccan |
| 10 | Q 45 al-Jāthiya | 0.8513 | Hawamim, tanzīl-cluster |

Three of the H-NEW-1100 tanzīl-cluster co-members (Q 40, 41, 45) appear in Q 39's top-10 FR-neighbors — supporting the cluster's content-cohesion claim (which DIRECTIONAL at corpus level: cluster mean FR 0.8244 vs random 0.9235 at z=−1.105, p=0.129 per MASTER-LEDGER §10.24). The other two tanzīl-cluster members (Q 32, Q 46) are ranked 11 (Q 46) and outside top-10 (Q 32 ranks farther due to Q 32's α-l-m muqaṭṭāʿat-induced root profile).

### 2.3 Mushaf-adjacency (h-new-720 per_adjacency)

| Pair | FR distance | TSP-residual | Note |
|:--|:--|:--|:--|
| Q 38 → Q 39 | 0.9364 | 0.0992 (frac 0.0120) | medium |
| **Q 39 → Q 40** | **0.7953** | **0.0339 (frac 0.0041)** | **near-optimal: in top 5% smoothest mushaf-edges** |

The Q 39 → Q 40 transition is among the cheapest in the entire mushaf: only 0.41% above what a TSP-optimal local re-arrangement would yield. This locks Q 39 as the frictionless-onramp into the Hawamim cluster. Q 38 → Q 39 has higher residual (1.20%) — the mushaf "spends FR-cost" entering Q 39 and "recovers" smoothly into Q 40.

This is consistent with H-NEW-130 (CONFIRMED): 15/15 of the largest consecutive-surah FR jumps in mushaf order land at structural boundaries. Q 38 → Q 39 is NOT among those top-15 jumps; Q 39 → Q 40 is among the smallest residuals. Q 39 is thus a *transition surah*, gluing the post-Ṣād content-block (Q 38) into the Hawamim block (Q 40+) without major FR-discontinuity.

## 3. Outlier-strength signature (h-new-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`, Q 39's outlier-strength entry:

| Field | Value |
|:--|:--|
| X (target surah) | 39 |
| Window | [36, 37, 38, 39, 40, 41, 42] |
| Window minus X | [36, 37, 38, 40, 41, 42] |
| d_W (with Q 39) | 0.9032 |
| d_W minus X | 0.9139 |
| pct_W | 32.3 |
| pct_W minus X | 37.54 |
| **delta_pct** | **−5.24** |
| p_greater_W | 0.677 |
| **classification** | **WEAK_ANCHOR** |
| **outlier-rank** | **100 / 114** |

Negative delta_pct means: removing Q 39 from its 7-window neighborhood IMPROVES local FR cohesion. Q 39 is therefore a WEAK ANCHOR — its content profile is heterogeneous enough that the local 7-surah window is more cohesive WITHOUT Q 39. This is an honest signature of Q 39's distinctiveness within its own neighborhood (despite Q 39 → Q 40 being smooth, Q 39 itself doesn't "anchor" the 7-surah window the way Q 33 al-Aḥzāb (rank 1, +31.46%) or Q 1 al-Fātiḥa (rank 2, +27.09%) do.

This is consistent with Q 39's UAS rank (see §5).

## 4. Phonological / iʿjāz signature (h-new-750)

From `findings/phase-b-hypotheses/csv/h-new-750.json`, Q 39's per-surah entry:

| Field | Value |
|:--|:--|
| n_verses | 75 |
| **rhyme_entropy_nats** | **1.0948** |
| top_final_letter | ن (nūn) |
| **top_final_letter_frac** | **0.7067** (53/75) |
| mean_content_distance | 1.0149 (matches §2.1) |
| local_cohesion | 1.1482 |
| z_rhyme_entropy | +0.5885 |
| z_mean_content_distance | +0.9023 |
| z_local_cohesion | −0.5041 |
| sig_A | −0.3138 |
| sig_B | +0.0844 |
| **rank_A** | **69 / 114** |
| **rank_B** | **56 / 114** |

Q 39's rhyme-entropy (1.0948 nats) is MODERATE — the surah uses a dominant nūn-rhyme (70.7%) with secondary letters (ر 8%, م 7%, ب/د 5% each, ل 3%, ي 1%). Compare:

- Monorhymed surahs (like Q 55 al-Raḥmān, Q 113 al-Falaq): rhyme-entropy ~0.0-0.5 nats.
- Highly variegated (like long Medinan surahs): rhyme-entropy ~1.5-2.5 nats.

Q 39 is in the moderate-entropy zone consistent with Late Meccan tawḥīd-iʿtiqād surahs that maintain a dominant fāṣila but allow controlled variation.

The mean_content_distance (1.0149) is ABOVE corpus mean (0.92) at +0.90σ; Q 39 is content-distant from corpus center, supporting the FR-centroid rank 91 finding.

local_cohesion (1.1482) is BELOW corpus median at -0.50σ; Q 39's content-cohesion within its mushaf-neighborhood is ROBUST despite the surah itself being a weak anchor. This is the same observation as the cheap Q 39 → Q 40 mushaf-adjacency: Q 39 fits *into* its neighborhood smoothly even if it doesn't *anchor* it.

## 5. UAS — Unified Architectural Score (h-new-840)

From `findings/phase-b-hypotheses/csv/h-new-840.json`, Q 39's UAS entry:

| Field | Value |
|:--|:--|
| UAS | −1.1485 |
| abs_outlier | 5.24 |
| max_cost | 0.0992 |
| abs_ijaz | 0.3138 |
| **UAS rank** | **78 / 114** |

Q 39 is in the bottom-half of UAS — below the "architectural anchor" tier dominated by Q 33, Q 1, Q 24, Q 9, Q 12, Q 55, Q 8, Q 26 (top-8). Q 39's contribution to the corpus's architectural skeleton is modest. This is consistent with WEAK_ANCHOR classification: the surah is NOT an architectural pivot.

What Q 39 IS, per the Q039-F-01 + Q039-F-02 + Q039-F-03 tests (this work), is a corpus-EXACT FORM-CARRIER for: (a) the tanzīl-opener cluster, (b) the *xlS* sincere-devotion root, (c) the *zumar* throng motif. These are FORM-level signatures, not ARCHITECTURAL-anchor signatures. Q 39 has its own specialty within the corpus's geometry.

## 6. Spectral signature (h-new-950)

From MASTER-LEDGER (H-NEW-950 NULL, divine-name-spectral periodicity test):

> Q 39 al-Zumar 6.87 [Lomb-Scargle peak power] at T=19 verses, p=0.046 [post-hoc, MW-7 single-test α=0.05]; Q 22 al-Ḥajj 6.54 at T=23, p=0.064.

Q 39 is the **2nd-strongest** spectral-peak surah in the corpus-wide H-NEW-950 NULL (rank 2 after Q 33). The peak at T=19 verses suggests a possible quasi-periodic recurrence of divine-name density at ~19-verse intervals. Under the strict Bonferroni-150 correction (50 long surahs × top-3 peaks), this fails (α_bon = 3.33×10⁻⁴). Under post-hoc single-test α=0.05, it survives marginally.

This is honest: the divine-name placement in Q 39 is NOT spectrally-rhythmic at the strict-test level. The T=19 quasi-periodicity is descriptive only and not pre-registered. It is logged here as a feature of Q 39's profile that future independent replication could test.

## 7. Per-surah top-K root coverage (h-new-111)

`per_surah_topk_coverage` for Q 39 = **0.9468** — Q 39's root-distribution is 94.68% covered by the corpus-global top-K=500 roots. This is a MODEST-HIGH coverage (corpus mean 0.917, range typically 0.80-0.98). Q 39 uses common Quranic vocabulary; it does not introduce many rare roots beyond the corpus default. This is consistent with the surah's didactic register — repetitive *qul*, divine names, *kfr/ʾmn* polarity, *ʿbd/dīn/khlṣ* axis.

## 8. cross-finding-013 ring-topology placement

cross-finding-013 (CONFIRMED) establishes the mushaf as a topological ring with universal hinges at Q 14→15, Q 49→50, Q 56→57. Q 39 is NOT a ring-hinge surah: Q 39 → Q 40 is a SMOOTH transition (frac_residual 0.0041), and Q 38 → Q 39 has only modest residual (0.0120, not in top-15 jumps).

Q 39 is positioned in the back-half of the ring (post-Q 14→15 hinge, pre-Q 49→50 hinge), in what cross-finding-026 + cross-finding-020 describe as the **"ḥawāmīm zone"** of the architecture — late-Meccan tawḥīd-eschatology surahs grouped roughly Q 32 onward through Q 49. Q 39 sits adjacent to the Hawamim entry-point (Q 40), making it the gateway-non-muqaṭṭāʿat-opener into the Hawamim cluster.

## 9. cross-finding-012 Pattern-B placement

cross-finding-012 (PASS-DIRECTED) identifies 5 Pattern-B Late-Meccan Scripture-Announcement Apparatus axes:

| Pattern-B axis | Q 39 status |
|:--|:--|
| Book-reference in v.1-3 | YES (v.1 *al-kitāb*) |
| qul-imperative density | HIGH (15 *qul* tokens — see §10) |
| Eschatological closure | YES (vv. 71-75 zumar-throng cycle) |
| Tawḥīd-imperative explicit | YES (*mukhliṣan lahu al-dīn* vv. 2, 11, 14) |
| Cosmic-power statement | YES (v. 67 *al-arḍu jamīʿan qabḍatuhu*) |

Q 39 has FULL Pattern-B compliance — all 5 axes attested. Combined with its Nöldeke rank 80 (within the B6 marker peak), Q 39 is a paradigmatic Pattern-B carrier. Q039-F-01 (PASS-DIRECTED, p_var=0.0003) confirms the H-NEW-1100 tanzīl-cluster (which Q 39 anchors) is chronologically concentrated in the Late-Meccan B6/B7 zone.

## 10. Qul-imperative count (QAC v0.4)

From QAC morphology `data/morphology/quranic-corpus-morphology-0.4.txt`: Q 39 contains **15 imperative *qul* tokens** (root *qwl*, POS=V, IMPV) at vv. 8, 9, 10, 11, 13, 14, 15, 38 (×2), 39, 43, 44, 46, 53, 64.

Compare to corpus baseline (332 *qul* imperatives across 114 surahs per H-NEW-74; mean 2.91 per surah). Q 39's 15 *qul* tokens place it at **5.15× the corpus mean** — among the densest *qul*-clusters in the corpus.

## 11. Specialty roots — empirical attestations

From QAC morphology v0.4 trace of Q 39:

### *xlS* (sincere-devotion) — 4 tokens
- v.2 *muxoliSFA* (mukhliṣan)
- v.3 *xaAliSu* (al-khāliṣ)
- v.11 *muxoliSFA*
- v.14 *muxoliSFA*

Q 39's xlS density = 3.40/1000 words vs rest-corpus 0.35/1000 = **9.65× rest-of-corpus density**. Per Q039-F-02 (this work, PASS-DIRECTED, perm-p = 0.0011), Q 39's xlS-density is RANK 4 of 114 surahs by per-1000-word density.

### *zmr* (throng) — 2 tokens, both Q 39
- v.71 *zumarFA* (zumaran, in-throngs to Hell)
- v.73 *zumarFA* (zumaran, in-throngs to the Garden)

The eponymous root is corpus-EXACT to Q 39. Per Q039-F-03 (PASS-DIRECTED, H2 confirmed), the *wa-sīqa alladhīna* paired-incipit construction repeats EXACTLY in Q 39 vv. 71 and 73, and is corpus-EXACT (no other surah has the construction repeated).

### Top 30 roots in Q 39 by token count

| Root | Count | Note |
|:--|:--|:--|
| Alh (Allāh) | 61 | divine-name dominant |
| qwl (qāla, *qul*) | 29 | dialogue + 15 *qul* imperatives |
| rbb (rabb) | 18 | divine-Lord |
| kwn (kāna) | 18 | universal copula |
| Ebd (ʿabd, ʿibāda) | 16 | servitude |
| ArD (arḍ) | 12 | earth |
| Elm (ʿilm) | 12 | knowledge |
| qwm (qiyāma) | 12 | resurrection-day |
| kfr (kufr, kāfirūn) | 10 | disbelief polarity |
| smw (samāʾ) | 10 | heavens |
| hdy (hudā) | 9 | guidance |
| wqy (taqwā) | 9 | God-fearing |
| Hqq (ḥaqq) | 8 | truth |
| xlq (khalq) | 8 | creation |
| Eml (ʿamal) | 8 | deeds |
| Hsn (ḥasan) | 8 | goodness |
| ywm (yawm) | 8 | day |
| nzl (tanzīl) | 7 | revelation |
| nfs (nafs) | 7 | soul |
| Dll (ḍalāl) | 7 | misguidance |
| swA (istiwāʾ) | 7 | equivalence (e.g., Q 39:9 *hal yastawī…*) |
| dwn (dūna) | 6 | "instead of" (in *min dūnihi*) |
| byn (bayn) | 6 | "between" |
| Zlm (ẓulm) | 6 | injustice |
| Axr (ākhira) | 6 | hereafter |
| qbl (qabla) | 6 | "before" |
| rAy (raʾā) | 6 | seeing |
| Aty (atā) | 6 | "comes" |
| ... | ... | (230 distinct roots total) |

Total Q 39 morphology tokens: 1,862 (versus 1,177 orthographic words, due to QAC counting prefixes/suffixes as separate sub-tokens).

## 12. Cross-finding-026 and §13 Structural-twin-pair status

cross-finding-026 §13 lists Structural-twin-pair surahs by FR-content-twin signature. Q 39 is NOT in the §13 Structural-twin-pair set; it is not paired with another single surah by FR-distance enough to reach structural-twin status. Its 3 nearest neighbors (Q 16, Q 40, Q 10) are in the d=0.75-0.80 range — close but not in the d<0.50 twin-pair zone.

## 13. Summary metric panel

| Metric | Q 39 | Rank | Source |
|:--|:--|:--|:--|
| Verses | 75 | -- | corpus |
| Words | 1,177 | -- | corpus |
| FR-centroid rank | -- | 91/114 | h-new-111 |
| UAS | −1.149 | 78/114 | h-new-840 |
| Outlier delta_pct | −5.24% (WEAK_ANCHOR) | 100/114 | h-new-590 |
| Mean FR distance | 1.015 | -- | h-new-750 |
| Local cohesion z | −0.504 | -- | h-new-750 |
| Rhyme entropy (nats) | 1.095 | mid | h-new-750 |
| Top-letter rhyme | ن at 70.7% | -- | computed |
| Q→Q+1 frac_residual | 0.0041 | top-5% smooth | h-new-720 |
| Spectral peak (post-hoc) | T=19, p=0.046 | rank 2 | h-new-950 |
| qul imperatives | 15 | high | QAC v0.4 |
| xlS root density | 3.40/1k | 4/114 | Q039-F-02 (this work) |
| zmr root tokens | 2 (corpus-EXACT) | -- | QAC v0.4 |

## 14. Honest synthesis

Q 39 is a **content-distinctive Late Meccan tawḥīd-eschatology surah** with a strong FORM-level signature (tanzīl-opener at v.1; xlS-mukhliṣ doctrinal anchor; zumar-throng eponym at vv. 71-73; rabb-al-ʿālamīn closure echoing Q 1:2) that is NOT an architectural anchor in the project's UAS / outlier-strength sense. Its specialty is *being the FORM-carrier* — corpus-EXACT positioning of the tanzīl-cluster opener at v.1 (uniquely), corpus-EXACT zumar-throng eponym, corpus-EXACT *wa-sīqa* paired-incipit. Its mushaf placement at the gateway to the Hawamim cluster (smooth Q 39 → Q 40 transition) makes it structurally functional as the non-muqaṭṭāʿat onramp into the most concentrated muqaṭṭāʿat-and-tanzīl block of the corpus.

The Q039-F-01 + Q039-F-02 + Q039-F-03 tests of this work all PASS-DIRECTED at α_bon = 0.0125, confirming the surah's distinctive FORM-level signatures empirically. Q039-F-04 NULL means the formal cohesion of the self-ring claim (tanzīl-opener + hamd-closer) does not survive Bonferroni-4 — consistent with the small effect-size of the rabb-al-ʿālamīn-closer cluster (3 surahs).
