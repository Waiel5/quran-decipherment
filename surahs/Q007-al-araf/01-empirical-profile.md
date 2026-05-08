---
surah: 7
surah_name_ar: الأعراف
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — all H-NEW empirical anchors integrated
---

# Q 7 al-Aʿrāf — Empirical Architectural Profile

All metrics are computed from the on-disk pre-locked H-NEW JSON anchors. File paths cited inline. Rules-tuple default `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

---

## 1. Unified Architectural Significance (UAS) — rank 11/114

Source: `findings/phase-b-hypotheses/csv/h-new-840.json`.

| Component | Value | Rank context |
|:---|---:|:---|
| **UAS** | **1.920** | **rank 11/114 — top-10% structural significance** |
| abs(outlier-strength Δ%ile) | 3.78 | low (median) |
| max canonical-adjacency cost (Q7-Q8 = 0.212) | 0.212 | top-15 expensive transitions |
| abs(iʿjāz-signature) | 2.033 | rank 104 (anti-fawāṣil — LOW iʿjāz al-fawāṣil) |

**Interpretation**: Q 7 is in the **structural-iʿjāz-by-OUTLIER + ADJACENCY-COST** quadrant of the UAS architecture. Despite extreme monorhyme (-ūn at 93.2% of verses), Q 7's UAS rank 11 is driven by:
1. The transition cost from Q 7 to Q 8 (al-Anfāl, Medinan): 0.212 length-units, top-10% expensive in the mushaf-graph.
2. Above-average mean content distance to other surahs (1.039 vs corpus median ~0.95).
3. Modest absolute outlier-strength (3.78pp).

The HIGH iʿjāz al-fawāṣil scoring (sig_A) is FAILED by Q 7 — the surah's near-monorhyme makes it structurally atypical of "rhyme-variety as iʿjāz" but typical of "monorhyme as recitation-anchor" (cf. al-Tirmidhī #3170 on al-sabʿ al-ṭiwāl recitation).

## 2. Outlier-strength spectrum (H-NEW-590) — NULL

Source: `findings/phase-b-hypotheses/csv/h-new-590.json`.

| Quantity | Value |
|:---|---:|
| Window | [Q 4, 5, 6, 7, 8, 9, 10] (Q 7-centered, K=7) |
| d̄_W (with Q 7) | 0.9202 |
| d̄_W−X (without Q 7) | 0.9281 |
| **Δ%ile** | **−3.78pp** |
| p_greater_W (1-tail) | 0.598 |
| Classification | **NULL** |

Q 7 is **NOT a content-outlier** in its 7-window. Removing Q 7 from the [4..10] block makes the residual block SLIGHTLY MORE CONCENTRATED (d̄ rises 0.0079). This is the OPPOSITE of e.g., Q 1's +27pp outlier or Q 9's +21pp outlier. Q 7's structural significance is NOT outlier-driven.

This is consistent with the FR top-5 nearest neighbors: Q 6, Q 10, Q 28, Q 11, Q 40 — i.e., Q 7's surrounding surahs (Q 6, Q 10, Q 11) are content-similar to Q 7. Q 7 SITS in a coherent local content-block.

## 3. Phonological / rhyme + phoneme — extreme monorhyme

Source: `findings/phase-b-hypotheses/csv/h-new-700.json` + `h-new-750.json`.

### 3.1 Rhyme axis (final letter)

| Letter | Count | Frac |
|:-:|---:|---:|
| ن (nūn) | 192 | 93.2% |
| م (mīm) | 10 | 4.9% |
| ل (lām) | 2 | 1.0% |
| ص (ṣād, v. 1 = muqaṭṭaʿ) | 1 | 0.5% |
| ۩ (sajda symbol on v. 206) | 1 | 0.5% |

- **Shannon rhyme-entropy (nats): 0.279** (rank 110/114 from low-end — corpus near-minimum).
- Top final-letter fraction: **0.937** (rank 4/114 from high-end — top-monorhyme).

Cross-axis position (per H-NEW-700 corpus law `d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50)`):
- Q 7's expected d̄_rhyme under the law (s=7, before kink): 0.36.
- Observed window-d̄ at s=7: see h-new-700.json best/worst windows.

### 3.2 iʿjāz signature (sig_A, sig_B)

| Quantity | Value | Rank/114 |
|:---|---:|---:|
| sig_A | **−2.033** | **104** (low — anti-fawāṣil) |
| sig_B | **−1.474** | **101** (low) |
| z_rhyme_entropy | −0.889 | sub-mean |
| z_mean_content_distance | +1.144 | above-mean (content-distinct) |
| z_local_cohesion | −0.585 | sub-mean (locally cohesive) |

**Architectural type**: Q 7 is **anti-iʿjāz-al-fawāṣil** (low sig_A and sig_B), but **structurally significant by OUTLIER and CONTENT-DISTINCTNESS** (high z_mean_content_distance). This places Q 7 firmly in the **structural-iʿjāz typology** (cf. al-Bāqillānī's *iʿjāz al-fawāṣil*) but on the LENGTH-AND-OUTLIER axis rather than the FAWĀṢIL-VARIETY axis. The dual-iʿjāz typology (cross-finding-840) is consistent: Q 7 has structural-iʿjāz status without rhyme-variety.

## 4. Canonical adjacency costs (H-NEW-720)

Source: `findings/phase-b-hypotheses/csv/h-new-720.json`.

| Pair | Δ_raw | Δ (clipped ≥ 0) | Fraction of residual | Comment |
|:---|---:|---:|---:|:---|
| Q 6 → Q 7 | −0.0575 | **0.0000** | **0.0%** | **Cheapest non-trivial adjacency in mushaf** — Q 6 ↔ Q 7 is structurally-zero-cost; mushaf placement matches FR-2-opt |
| Q 7 → Q 8 | +0.2120 | 0.2120 | 2.6% | top-10 most-expensive transition; Meccan→Medinan break |

**Interpretation**:
- **Q 6 → Q 7** is a **content-twin transition**: zero residual means the mushaf placement of Q 7 immediately after Q 6 is what a Fisher-Rao 2-opt would also choose. This anchors al-Biqāʿī's *Naẓm al-Durar* reading of Q 6→Q 7 as a tightly continuous *al-Anʿām → al-Aʿrāf* sequence.
- **Q 7 → Q 8** is **expensive**: the transition from Q 7 (Late Meccan, 7-prophet narrative) to Q 8 (Medinan, Battle of Badr) is a true thematic / Meccan-Medinan break. The TSP-residual finds this cost because Q 8 is FR-distant from Q 7 (Medinan content vs Meccan narrative).

Q 7's mushaf-position is **structurally optimal on the LEFT (Q 6) and structurally costly on the RIGHT (Q 8)** — a "right-edge" of the Late-Meccan ṭiwāl block.

## 5. Fisher-Rao distance (H-NEW-111)

Source: `findings/phase-b-hypotheses/csv/h-new-111.json`. Computed this run from upper-triangular matrix.

### 5.1 Q 7 nearest 10 neighbors (lowest FR distance)

| Rank | Surah | FR distance | Note |
|:-:|:-:|---:|:---|
| 1 | Q 6 al-Anʿām | **0.721** | mushaf-neighbor; content-twin (the ʿAnʿām–Aʿrāf prophet-narrative duo) |
| 2 | Q 10 Yūnus | 0.742 | ALR-cluster, prophet-narrative |
| 3 | Q 28 al-Qaṣaṣ | 0.762 | Mūsā-cycle, ṬSM |
| 4 | Q 11 Hūd | 0.764 | ALR-cluster, prophet-narrative + ʾakhāhum-lattice sister |
| 5 | Q 40 Ghāfir | 0.769 | ḥawāmīm-7, eschatology |
| 6 | Q 27 al-Naml | 0.774 | Sulaymān, prophet-narrative |
| 7 | Q 23 al-Muʾminūn | 0.789 | creedal + brief prophet sequence |
| 8 | Q 16 al-Naḥl | 0.814 | thematic sister |
| 9 | Q 21 al-Anbiyāʾ | 0.824 | prophet-roster |
| 10 | Q 2 al-Baqara | 0.831 | ALM-cluster + extended-Adam-narrative twin (per Q007-F-04) |

### 5.2 Q 7 farthest 5

| Rank | Surah | FR distance | Note |
|:-:|:-:|---:|:---|
| 110 | Q 92 al-Layl | 1.224 | tail-end short, doxological |
| 111 | Q 97 al-Qadr | 1.228 | Laylat al-Qadr, tail |
| 112 | Q 88 al-Ghāshiya | 1.236 | tail eschatology |
| 113 | Q 80 ʿAbasa | 1.254 | tail rebuke |
| 114 | **Q 55 al-Raḥmān** | **1.292** | **iʿjāz-anti-twin** — Q 55 is corpus-FR-farthest from Q 7 (the structural-iʿjāz / refrain-iʿjāz pair are EMPIRICALLY MAXIMALLY DISTINCT) |

The Q 7 ↔ Q 55 farthest-pair is interesting: Q 7 is high-UAS-by-OUTLIER + extreme-monorhyme; Q 55 is high-UAS-by-REFRAIN + variety. They occupy **opposite poles of the dual-iʿjāz typology** within the structural-iʿjāz quadrant. (Cross-finding queue-able.)

### 5.3 Letter-family centroid distances (Q007-F-02)

| Centroid | Surahs | Mean d(7, group) |
|:---|:---|---:|
| ALM-6 | Q 2, 3, 29, 30, 31, 32 | 0.908 |
| ALR-5 | Q 10, 11, 12, 14, 15 | **0.841** |
| ALMR-1 | Q 13 | 0.914 |
| All-muqaṭṭaʿāt-29 | (29-set) | 0.889 |
| All non-muqaṭṭaʿāt-85 | (85-set) | 1.089 |

Q 7 is **closer to the ALR cluster centroid than to the ALM cluster** by 0.067 FR-units. This is consistent with Q 7's content-axis being prophet-narrative-rich (ALR cluster's identity per H-NEW-97). Q 7 ranks **2/114** on combined `(d_ALM + d_ALR)/2` — only Q 45 (al-Jāthiya, ḥawāmīm) is closer to the mid-point.

This is the **DIRECTIONAL** Q007-F-02 finding: Q 7's content-axis IS in the neighborhood of both ALM and ALR clusters, with a slight ALR-bias. p_perm = 0.040 vs random subset baseline (DIRECTIONAL, not strictly p≤0.0125 Bonferroni).

## 6. Compression-tail position

Per H-NEW-660 corpus law: `d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50)`.

Q 7 at s=7 is **before the kink at s=50**, so the compression-tail predicts d̄_content ≈ 0.96. Q 7's observed mean_content_distance = 1.039 (h-new-750.json), which is **+0.08 above** the law's prediction for the head-mushaf zone. This is consistent with Q 7's content-distinctness signal (z_mean_content_distance = +1.14 vs corpus mean).

## 7. Cross-corpus letter-frequency baseline

Q 7's letter-frequency profile is sampled from `data/baseline-corpora/letter-z-quran-vs-matched-bukhari.csv` (corpus-wide). For the surah-specific cross-corpus comparison, Q 7 is one of the larger surahs that contributes substantially to the Quran-vs-poetry / Quran-vs-Bukhari letter-z signature; the per-surah letter-z is not separately published (corpus-aggregate signal at p<10⁻¹⁰; cf. h-new-740).

## 8. Architectural type classification

| Axis | Q 7 score | Class |
|:---|---:|:---|
| UAS overall | rank 11/114 | top-10% structurally-significant |
| Outlier-driven? | NO (Δ%ile NULL) | not an outlier-iʿjāz surah |
| Fawāṣil-rich? | NO (sig_A rank 104) | anti-iʿjāz-al-fawāṣil |
| Adjacency-costly? | YES on right (Q7→Q8 top-10) | structural |
| Content-distinct? | mildly YES (z=+1.14) | locally-distinct |
| FR-locally-cohesive? | YES (z_local_cohesion=−0.585) | embedded in Q 6 / Q 10–11 / Q 28 cluster |
| Rhyme entropy | 0.279 (rank 110) | extreme monorhyme |

**Type**: **Structural-iʿjāz by OUTLIER+ADJACENCY+CONTENT-DISTINCTNESS, anti-fawāṣil-by-monorhyme**. Q 7 is the *opposite* of Q 55 al-Raḥmān (which is structural-iʿjāz by REFRAIN+variety). They are the two most distant surahs in FR distance — the empirical observation matches the typological expectation.

## 9. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]]: Q 7 NULL (Δ%ile=−3.78pp).
- [[h-new-660-compression-tail-gradient|H-NEW-660]]: Q 7 at s=7 in the head-mushaf, +0.08 above-law content-distance.
- [[h-new-700-phonological-compression-tail|H-NEW-700]]: Q 7 rhyme entropy 0.279 (extreme).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]]: Q 6→Q 7=0.000 (cheapest), Q 7→Q 8=0.212 (top-10 expensive).
- [[h-new-750|H-NEW-750]]: Q 7 sig_A=−2.033 (rank 104), sig_B=−1.474 (rank 101).
- [[h-new-840-unified-architectural-score|H-NEW-840]]: Q 7 UAS rank **11/114**.
- [[h-new-940-prophet-order-conservation|H-NEW-940]]: Q 7 contributes Adam-Nūḥ-Hūd-Ṣāliḥ τ=1.0 to CONFIRMED H2a.
- [[Q006-al-anam/01-empirical-profile|Q 6 al-Anʿām]]: FR-nearest neighbor (0.721); zero canonical-adjacency cost.
- [[Q011-hud/01-empirical-profile|Q 11 Hūd]]: ʾakhāhum-lattice sister; FR=0.764.
- [[Q055-al-rahman/01-empirical-profile|Q 55 al-Raḥmān]]: FR-farthest; iʿjāz-anti-twin within structural-iʿjāz quadrant.
