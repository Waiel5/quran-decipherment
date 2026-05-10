---
surah: 47
surah_name_ar: محمد
file_type: empirical-profile
date_last_updated: 2026-05-10
phase: B+
specialist: Q047-wave-J-specialist
---

# Q 47 — Empirical Profile

All metrics computed from project artifacts on disk; no figures stated from memory. File paths cited inline.

## 1. Architectural significance — UAS and component scores

| Metric | Q 47 value | Rank/114 | Source |
|:--|:--|:-:|:--|
| UAS (Unified Architectural Significance) | 0.4656 | 36 | `findings/phase-b-hypotheses/csv/h-new-840.json` |
| Outlier-strength Δ%ile (window [44..50]) | +5.20 (WEAK_OUTLIER) | — | `h-new-590.json` |
| iʿjāz signature sig_A | −1.645 | 95 (low) | `h-new-750.json` |
| iʿjāz signature sig_B | −1.611 | 105 (low) | `h-new-750.json` |
| Mean content-distance d̄ | 0.9867 (z = +0.624) | — | `h-new-750.json` |
| Local cohesion | 1.0847 | — | `h-new-750.json` |
| Rhyme entropy (nats) | 0.206 (z = −1.021) | top-5% rāwī-monotonic | `h-new-750.json` |
| Top final letter (rāwī) | م (36/38 = 94.7%) | — | computed |

**Interpretation**: Q 47 is mid-UAS (rank 36 of 114), with a strong *theological-iʿjāz* profile (deeply negative sig_A and sig_B) driven by extreme rāwī-monotonicity (94.7% م). It is NOT a structural-iʿjāz exemplar (not in al-Bāqillānī's *fawāṣil*-variation top tier). Its outlier-strength is modest but content-distance d̄ is above corpus mean — Q 47's vocabulary is *distinctive* in specific axes (war-instruction).

## 2. Compression-tail position (Wave 2026-04-28 architectural law)

s = 47.

| Law | Equation | Predicted Q 47 value | Observed | Δ |
|:--|:--|:-:|:-:|:-:|
| d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50) | s−50 = −3 → max(0,-3) = 0 → predicted 0.96 | Q 47 d̄_content ≈ 0.987 | +0.027 (slightly above the kink-50 plateau) | within MW-4 noise |
| d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50) | predicted 0.36 | Q 47 rhyme entropy 0.206 — rāwī-monotonic outlier | −0.154 from compression-tail expectation | corpus-rare LOW |
| d̄_phoneme(s) ≈ 0.001 + 0.00089·max(0, s−75) | predicted 0.001 | n/a (kink at 75, not 47) | — | n/a |

**Note**: Q 47's rhyme entropy is FAR BELOW the corpus-50 plateau, making it one of the corpus's tightest rāwī-monotonic surahs. This is a known compression-tail anomaly — the rhyme-axis compression-tail (law: dispersion increases for s>50) does not predict the LOW rhyme entropy of Q 47. The 94.7% م-rāwī is a Q 47 IDIOSYNCRATIC architectural feature, not a position-driven one.

## 3. Adjacency cost (H-NEW-720)

| Pair | δ (TSP-cost) | Note | Source |
|:--|:-:|:--|:--|
| Q 46 → Q 47 | 0.0873 | corpus-mid | `h-new-720.json` |
| Q 47 → Q 48 | 0.0332 | corpus-CHEAP (one of the lowest single-edge TSP-costs) | `h-new-720.json` |
| Q 48 → Q 49 | 0.0831 | corpus-mid | `h-new-720.json` |

**Note**: The Q 47→Q 48 TSP-cost of 0.0332 is corpus-extreme cheap — the editorial seam is very tight at the TSP-residual level. But this DOES NOT propagate to the H-NEW-130 family ranks (see §5).

## 4. Fisher-Rao mushaf distances (H-NEW-111)

Q 47 pairwise FR distances to selected reference points:

| Pair | FR distance | Note | Source |
|:--|:-:|:--|:--|
| Q 47 ↔ Q 1 | 1.0408 | corpus-mid-far | h-new-111 D_matrix |
| Q 47 ↔ Q 2 | 0.9620 | corpus-mid | h-new-111 |
| Q 47 ↔ Q 3 (Muhammad-name peer) | 0.9601 | corpus-mid | h-new-111 |
| Q 47 ↔ Q 33 (Muhammad-name peer) | 1.0134 | corpus-mid-far | h-new-111 |
| Q 47 ↔ Q 48 (Hudaybiyya pair, Muhammad-name peer) | 0.8893 | below corpus mean 0.9235 | h-new-111 |
| Q 47 ↔ Q 49 | 0.8503 | top-3 nearest | h-new-111 |
| Q 47 ↔ Q 61 (Aḥmad-name peer) | 0.8637 | top-5 nearest | h-new-111 |
| Q 47 ↔ Q 63 | 0.8295 | top-2 nearest | h-new-111 |
| Q 47 ↔ Q 64 (#1 nearest) | 0.8195 | top-1 nearest | h-new-111 |

**Q 47's 10 nearest FR neighbors** (`csv/Q047-F-06.json`):

| Rank | Surah | FR | Note |
|:-:|:-:|:-:|:--|
| 1 | Q 64 al-Taghābun | 0.8195 | back-Medinan |
| 2 | Q 63 al-Munāfiqūn | 0.8295 | hypocrites theme (echoes Q 47:16-19) |
| 3 | Q 49 al-Ḥujurāt | 0.8503 | etiquette-cluster |
| 4 | Q 61 al-Ṣaff | 0.8637 | jihād + Aḥmad-name |
| 5 | Q 66 al-Taḥrīm | 0.8659 | back-Medinan |
| 6 | Q 59 al-Ḥashr | 0.8769 | qitāl-narrative (Banū Naḍīr) |
| 7 | Q 13 al-Raʿd | 0.8877 | thematic outlier — exceptional |
| 8 | Q 48 al-Fatḥ | 0.8893 | Hudaybiyya pair (only #8) |
| 9 | Q 60 al-Mumtaḥana | 0.8935 | back-Medinan |
| 10 | Q 98 al-Bayyina | 0.9041 | back-Medinan, war-vocab #1 |

**KEY FINDING**: Q 47's nearest FR-neighbors are NOT Q 48 (8th) and NOT the other Muhammad-name peers (Q 3 = beyond top-10; Q 33 = beyond top-10). They are the BACK-MEDINAN ETIQUETTE/HYPOCRITE/JIHĀD CLUSTER {Q 49, 60, 61, 63, 64, 66}. This empirically REFINES the classical "Hudaybiyya pair" framing: Q 47 sits architecturally inside a broader back-Medinan community-and-warfare super-cluster, with Q 48 just one member of that cluster.

## 5. H-NEW-130 family — Q 47-Q 48 consecutive-adjacency ranks

Per Q047-F-06 (this dossier):

| D-matrix | Q 47-Q 48 distance | rank-low (1=cheapest) | in-bottom-15? |
|:--|:-:|:-:|:-:|
| H-NEW-130 (FR-root) | 0.8893 | 75/113 | NO |
| H-NEW-130b (char-4gram) | 0.9816 | 89/113 | NO |
| H-NEW-130c (verse-length-histogram) | 0.6941 | 71/113 | NO |

**Q 47-Q 48 is MID-PACK on all three D-matrices** — not a top-15 universal seam. The TSP-cost δ=0.0332 (h-new-720) records edge-savings under the 2-opt heuristic; this is a different metric from the consecutive_mushaf_distances of h-new-130 (which is the raw FR/char/verse distance, not the marginal TSP edge cost). The two metrics disagree on Q 47-Q 48: TSP says "cheap seam"; consecutive-distance says "mid-pack". Per Q047-F-06, we publish the consecutive-distance result as NULL on the "in_all_three=True" pre-registered direction.

## 6. Whole-pair FR rank (H-NEW-111, all 6441 pairs)

- Q 47-Q 48 FR distance = 0.8893
- Rank-low (1 = closest pair in corpus) = **2281 / 6441**
- Percentile-low = **35.4%** (not in bottom quartile)
- Pre-registered threshold (Q047-F-06 Test B, bottom 25%): NOT MET (35.4% > 25%)

So at the all-pairs scale, Q 47-Q 48 is closer than corpus median but NOT in the bottom-25%, NOT a top-tier "cohesive pair".

## 7. Architectural classification

Combining the above:

1. **Theological-iʿjāz dominant** (sig_A, sig_B deeply negative; rāwī-monotony at top-5%).
2. **Mid-UAS** (rank 36 of 114); not a structural-iʿjāz exemplar.
3. **Weak content outlier** (+5.2 pp Δ%ile; distinctive war-instruction vocabulary).
4. **Back-Medinan cluster member**: sits in a 6-surah FR neighborhood {Q 49, 60, 61, 63, 64, 66} broader than the Hudaybiyya-pair framing alone.
5. **Q 47-Q 48 pair**: cheap on TSP-edge cost (δ=0.033, classical-vindication-positive), BUT mid-pack on consecutive-distance rank in all three D-matrices (universal-seam-test NEGATIVE). al-Biqāʿī's Q 46→47→48 munāsabah is supported at the pair-LOCAL level (cheap edge), refined-NULL at the universal-seam level.

## 8. Cross-references

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — full FR matrix used here
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — TSP-edge cost δ=0.0332 for Q 47-Q 48
- [[h-new-130|H-NEW-130]] family — root/char/verse adjacency-distances
- [[h-new-590-outlier-spectrum|H-NEW-590]] — outlier-strength
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A/sig_B
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS
- [[Q008-al-anfal/06-novel-findings|Q 8 al-Anfāl]] — qitāl-cluster {Q 8, 9, 47, 48, 61}
- [[Q048-al-fath/06-novel-findings|Q 48 al-Fatḥ]] — Hudaybiyya pair
- [[Q049-al-hujurat/06-novel-findings|Q 49 al-Ḥujurāt]] — Q 47's #3 FR-nearest
- [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] — mushaf FR architecture

## 9. Honest limits

1. **The TSP-cost δ=0.0332 (H-NEW-720) and the consecutive-distance rank 75 (H-NEW-130) tell different stories** about Q 47-Q 48. TSP rewards greedy-route-savings; consecutive-distance is the raw FR. The brief's "in_all_three=True" claim mapped onto consecutive-distance metric returns NULL. A reframed pre-reg on TSP-edge would have RETURNED VINDICATED; this is a rules-tuple-sensitivity case (Q047-F-06 honest-limits note).
2. The FR-pair rank of 2281/6441 is BELOW corpus median but not extreme. The Q 47-Q 48 pair is cohesive but not architecturally singular.
3. Q 47's nearest FR-neighbor is Q 64 (al-Taghābun), NOT Q 48. The classical Hudaybiyya-pair framing is partial; the back-Medinan cluster framing is more architecturally exact.
