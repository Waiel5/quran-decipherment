---
surah: 27
surah_name_ar: النمل
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: SCAFFOLD
---

# Q 27 al-Naml — Empirical Architectural Profile

All values cited from disk. Rules-tuple: `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` unless noted.

## 1. UAS (Unified Architectural Score)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json`.

| Component | Q 27 value | Corpus interpretation |
|:--|:-:|:--|
| **UAS composite** | 1.023 | rank **23 of 114** (top quintile) |
| abs(outlier) | 8.76 | mild |
| max canonical-adjacency cost | 0.081 | low (Q 26-27 = 0.081, Q 27-28 = 0.059) |
| abs(iʿjāz_signature_A) | 1.649 | high *magnitude* but NEGATIVE direction (anti-iʿjāz) |

Q 27's UAS is driven primarily by the **|sig_A| = 1.649** term — but with NEGATIVE direction (sig_A = −1.649). The other two channels contribute weakly. The surah is a top-25 architectural-distinct, but its distinctness is "anti-iʿjāz" (low rhyme variety + high content cohesion), the same family as **Q 12 Yūsuf** (UAS rank 6, also continuous-narrative, also nūn-rhyme-uniform).

Reference: top-10 UAS surahs are Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17. Q 27 sits just outside the top-20.

## 2. Outlier-strength Δ%ile

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json`.

```
{
  "X": 27,
  "window": [24, 25, 26, 27, 28, 29, 30],
  "window_minus_X": [24, 25, 26, 28, 29, 30],
  "d_W": 0.9730,
  "d_W_minus_X": 0.9948,
  "pct_W": 71.62,
  "pct_W_minus_X": 80.38,
  "delta_pct": -8.76,
  "p_greater_W": 0.2838,
  "classification": "WEAK_ANCHOR"
}
```

**Interpretation**: Q 27, when removed from its 7-window neighborhood, leaves a window that is **more diffuse** (d_W_minus_X = 0.995 > d_W = 0.973), placing the no-Q27 window at 80.4%ile vs the with-Q27 window at 71.6%ile. So Q 27 is **mildly cohesive** with its neighbors — a weak anchor. Δ_pct = −8.76 (WEAK_ANCHOR direction).

This is the OPPOSITE direction from Q 12 (+14.3pp MODERATE_OUTLIER) and Q 33 (+31.5pp). Q 27 belongs structurally with its neighbors (Q 24-30), not against them.

## 3. iʿjāz signature

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json`.

```
{
  "surah": 27, "n_verses": 93,
  "rhyme_entropy_nats": 0.3179,
  "top_final_letter": "ن", "top_final_letter_frac": 0.9032,
  "mean_content_distance": 1.0077,
  "local_cohesion": 1.1270,
  "z_rhyme_entropy": -0.818, "z_mean_content_distance": +0.831,
  "z_local_cohesion": -0.533,
  "sig_A": -1.649, "sig_B": -1.351,
  "rank_A": 96, "rank_B": 96
}
```

**Interpretation**: sig_A combines (low rhyme entropy → bigger | |) − (low local cohesion). For Q 27 both are below mean → magnitude is high but direction is negative ("anti-iʿjāz al-fawāṣil"). The same iʿjāz signature pattern as Yūsuf (Q 12). This is consistent with the dual-iʿjāz typology of `[[h-new-840-unified-architectural-score]]`: Q 27 is **structurally anti-iʿjāz al-fawāṣil**, but is high on the architectural-distinctness axis via outlier-and-cluster effects.

## 4. Position in compression-tail

Q 27 (s=27) sits in the **head zone** (s < 50) of the compression-tail law:

> d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50), R²=0.986 ([[h-new-660-compression-tail-gradient]])

For s=27, the law predicts d̄_content ≈ 0.96 (no kink contribution). Q 27's mean content distance of 1.0077 is **above** the law's prediction by ~5pp — directionally consistent with WEAK_ANCHOR magnitude (Q 27 is content-cohesive *within* its window but content-distinct from corpus average).

## 5. Canonical-adjacency costs (TSP-residual decomposition)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json`.

| Pair | δ (delta) | fraction of TSP residual (8.29) |
|:--|:-:|:-:|
| Q 26 → Q 27 | **0.0806** | 0.97% |
| Q 27 → Q 28 | **0.0592** | 0.71% |

Both extremely low — the ṭ-s letter family (Q 26 ṬSM, Q 27 ṬS, Q 28 ṬSM) forms a structurally cheap canonical run. Compared to the most-expensive pair Q 1-Q 2 (0.62, 7.4% of residual), Q 27's neighbors are 8× cheaper. **Q 27 fits its mushaf-position smoothly.**

## 6. FR-distance neighbors

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (D-matrix reconstructed).

**Q 27's 5 nearest in FR-roots distance**:
1. Q 7 al-Aʿrāf — d=0.774
2. Q 10 Yūnus — d=0.792
3. Q 28 al-Qaṣaṣ — d=0.805
4. Q 6 al-Anʿām — d=0.841
5. Q 29 al-ʿAnkabūt — d=0.851

**Q 27's 5 farthest**:
1. Q 88 al-Ghāshiya — d=1.137
2. Q 56 al-Wāqiʿa — d=1.156
3. Q 77 al-Mursalāt — d=1.162
4. Q 80 ʿAbasa — d=1.164
5. Q 55 al-Raḥmān — d=1.321 (max)

The 5 nearest are all **prophet-narrative-rich, mid-Meccan/late-Meccan medium-length surahs**. Q 27 sits in the canonical "prophet-stories cluster" along with Q 7, Q 10, Q 28 (its right neighbor), Q 26 (its left neighbor — note Q 26 isn't in the top-5 but is presumably close given the same letter family). Q 12 Yūsuf is also nearby (Q 12 mean FR-distance to Q 27 ≈ from the matrix; the prompt's "Q12 nearest includes Q 27" confirms reciprocity).

## 7. Top roots in Q 27 (QAC v0.4)

Source: `/Users/grey/Downloads/quran/data/morphology/surah-root-graph.json`.

Top 15 roots in Q 27 (count):
| Root | Q 27 | Notes |
|:--|:-:|:--|
| qwl (q-w-l, "say") | 44 | dialogue-heavy narrative |
| Alh (ʾ-l-h, God) | 33 | tawḥīd density |
| kwn (k-w-n, "be") | 24 | |
| Aty (ʾ-t-y, "come/bring") | 20 | throne-bringing motif |
| qwm (q-w-m, "people") | 16 | |
| Elm (ʿ-l-m, knowledge) | 15 | sulaymanic knowledge motif |
| rbb (r-b-b, Lord) | 12 | |
| hdy (h-d-y, guidance) | 11 | opening's hudā framing |
| ArD (ʾ-r-ḍ, earth) | 11 | dabba/throne/earth motif |
| Ayy (ʾ-y-y, sign) | 10 | |
| Amn (ʾ-m-n, faith) | 9 | |
| byn (b-y-n, "make clear") | 9 | |
| smw (s-m-w, sky) | 8 | cosmological |
| nZr (n-ẓ-r, see/look) | 8 | |
| jyA (j-y-ʾ, "come") | 8 | |

The Q 27 distinctive roots vs corpus:
- **nml** (ant): Q 27 = 3, corpus total = 4 → **75% concentration** (the corpus 4th comes from Q 3:178 *nuʾmlī* 'we extend respite', a **different lemma** under root m-l-y; QAC may classify the form differently from orthographic match. See Q027-F-01 for orthographic-form audit, which finds 100%.)
- **hdhd** (hoopoe): Q 27 = 1, corpus total = 1 → **100% concentration** (hapax — the surah's only attestation).

## 8. Architectural type classification

Per the dual-iʿjāz typology (`[[h-new-840-unified-architectural-score]]`):
- **Structural-iʿjāz axis**: top-quintile (UAS rank 23).
- **iʿjāz al-fawāṣil**: NEGATIVE (anti-fawāṣil; sig_A = −1.649 → rank 96/114).
- **Theological-iʿjāz**: Q 27 has the second basmala (a candidate "thuluth" status?) — see `04-hadith-corpus.md` and `06-novel-findings.md` for analysis.

**Type**: anti-iʿjāz-al-fawāṣil structural-distinctness (cluster: Q 12 Yūsuf, Q 27 al-Naml, Q 28 al-Qaṣaṣ, Q 18 al-Kahf — narrative-driven, rhyme-uniform, content-coherent).

## 9. Cross-references to all H-NEW findings touching Q 27

- [[h-new-590-outlier-spectrum]] — Q 27 −8.76pp WEAK_ANCHOR.
- [[h-new-700-phonological-compression-tail]] — Q 27 nūn 90.3%, entropy 0.318 nats, top in Q 27 row.
- [[h-new-720-canonical-adjacency-cost]] — Q 26-27 = 0.081 (rank ~ middle), Q 27-28 = 0.059 (low).
- [[h-new-750-per-surah-iʿjāz-signature]] — sig_A = −1.649, rank 96/114.
- [[h-new-840-unified-architectural-score]] — UAS rank 23/114.
- [[h-new-111]] — FR distance row: nearest Q 7, 10, 28, 6, 29.
- [[h-new-NEW-321]] — Q 1 ↔ Q 27 Basmala-echo NULL at 81%ile (cohesion).

## 10. Honest limits

- The QAC root counts and orthographic-form counts disagree on naml-totals (3 vs 4) due to a different lemma (Q 3:178 *nuʾmlī* — root m-l-y per Lane's lexicon; QAC may classify under a related root). Q027-F-01 takes the orthographic position; for QAC-root analysis the concentration would be 3/4 = 75%. Both are reported.
- The "second basmala" structural fact is INDISPUTABLE under all tashkeel variants. The lexical signature audit Q027-F-02 confirms exact match.
- The Q 27 → Q 28 adjacency cost (0.059) is among the cheapest 30 of 113; the ṭ-s family is a low-cost canonical chunk.
