---
surah: 55
surah_name_ar: الرحمن
surah_name_translit: al-Raḥmān
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — empirical profile integrated from all H-NEW artifacts
---

# Q 55 al-Raḥmān — Empirical Profile

## Headline

Q 55 is the **single most paradoxical surah** under the project's iʿjāz typology:
- It is **rank 7/114 in UAS** (top decile) — high overall architectural significance.
- Yet it has the **corpus-MINIMUM iʿjāz_signature_A** (rank 114/114, sig_A = -3.173) — the LOWEST iʿjāz al-fawāṣil in the entire Quran.
- Its UAS score is propelled almost entirely by the **+14.26pp content-outlier strength** and the **|sig_A| = 3.17** loading on absolute-iʿjāz-magnitude (z=|sig_A| flips sign).

Read directly: Q 55 is structurally unique not because it has rich rhyme variety, but because it *renounces* rhyme variety in favor of an extreme refrain-monorhyme regime — and its content vocabulary is unusually distinct from its mushaf neighbors. **Bride-of-the-Quran status is REFRAIN-DENSITY, not fāṣila-variety.**

## 1. UAS composite (H-NEW-840)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json` (Q55 entry).

| Metric | Value | Source |
|:--|:--|:--|
| **UAS rank** | **7 / 114** | top_15 entry |
| UAS score | 4.097 | composite |
| abs_outlier (Δ-pp) | 14.26 | from H-NEW-590 |
| max_neighbor_TSP_cost | 0.0949 | from H-NEW-720 |
| abs_iʿjāz_signature | 3.173 | from H-NEW-750 |

Q 55 sits with Q 33 (rank 1), Q 1, Q 2, Q 9, Q 24, Q 12 in the top-7 — these are the structurally-most-distinctive surahs of the corpus.

## 2. Outlier-strength (H-NEW-590)

Source: `findings/phase-b-hypotheses/csv/h-new-590.json` (`candidate_results[X=55]`).

| Metric | Value |
|:--|:--|
| Window | [Q 52, 53, 54, 55, 56, 57, 58] |
| d_W (with Q 55) | 1.0511 |
| d_W minus Q 55 | 1.0022 |
| pct_W (with Q 55) | 97.81%ile |
| pct_W minus Q 55 | 83.55%ile |
| **Δ-pp** | **+14.26pp** |
| p_greater_W | 0.0219 |
| Classification | **MODERATE_OUTLIER** |

Removing Q 55 from its 7-window drops the cluster's content-distance percentile from 97.81 → 83.55, a 14.26pp improvement. Q 55 is content-distinct against Q 52-Q 58.

Cross-reference: H-NEW-390 used a chronology-restricted Meccan-only Q 50-56 cell and reported +32.62pp, more than 2× the standardized-window result. The methodological gap is documented in [[Q055-F-05-h390-replication]] — H-NEW-590 is the rules-tuple-consistent figure.

## 3. iʿjāz signature (H-NEW-750)

Source: `findings/phase-b-hypotheses/csv/h-new-750.json` (`per_surah[surah=55]`).

| Metric | Value | Rank |
|:--|:--|:--|
| n_verses | 78 | — |
| **rhyme_entropy_nats (Shannon)** | **0.4187** | low (corpus mean ≈ 1.7) |
| top_final_letter | ن | — |
| top_final_letter_frac | 0.8846 (88.46%) | corpus-extreme monorhyme |
| mean_content_distance | 1.181 | high (z=+2.54) |
| local_cohesion | 0.856 | low (z=-0.90) |
| z_rhyme_entropy | -0.636 | low |
| **sig_A** | **-3.173** | **rank 114/114 — corpus minimum** |
| sig_B | -1.538 | rank 102/114 |

Q 55's sig_A = -3.173 means it is the corpus's STRUCTURALLY LOWEST iʿjāz al-fawāṣil signature: high content distinctness (z=+2.54 above mean) combined with very low rhyme entropy (z=-0.64 below mean). This is the algebraic OPPOSITE of al-Bāqillānī's classical iʿjāz al-fawāṣil claim, which posits a balance of content variety + rhyme variety.

The negative sign of sig_A says: Q 55 is anti-iʿjāz-al-fawāṣil. Yet its UAS rank is 7 because abs|sig_A| is among the highest |loading| in the corpus.

**Interpretation**: Q 55 is content-distinct + monorhyme-locked. It is *iʿjāz al-takrīr* (refrain inimitability), not *iʿjāz al-fawāṣil*. Classical scholarship's "ʿarūs" honorific tracks the refrain-density (cf. al-Biqāʿī below), not the rhyme variety.

## 4. Final-letter distribution and rhyme structure

Computed from `quran-text/quran-no-tashkeel.json` (per Q055-F-01 script normalization):

| Final letter | Count | Fraction |
|:--|:--|:--|
| ن (nūn) | 69 | 88.5% |
| م (mīm) | 7 | 9.0% |
| ر (rāʾ) | 2 | 2.6% |

Of the 69 nūn-final verses, **31 are the refrain itself** (verifying Q055-F-01) and the remaining ≈ 38 are paired-verses (ـان dual ending: *al-jannāt-ān*, *baḥr-ān*, *muḍāhāmm-atān*, etc.). The dual-ending phonological constraint binds nearly the entire surah into a single sonic frame.

## 5. Phoneme density (computed from quran-full-tashkeel)

Q 55 consonantal-skeleton letter count: 1,628.

| Phoneme class | Density |
|:--|:--|
| Emphatic (ص ض ط ظ) | 1.54 / 100 letters |
| Pharyngeal (ع ح) | 1.90 / 100 letters |
| Sibilant (س ش ص ز ذ) | 5.96 / 100 letters |
| Glottal (ء ه) | 4.73 / 100 letters |

The refrain word *tukadhdhibān* contributes ذ (a sibilant-emphatic) repeatedly, but corpus-wide Q 55 is not a phoneme outlier under H-NEW-700's standardized phoneme axes.

## 6. Canonical-adjacency TSP cost (H-NEW-720)

Source: `findings/phase-b-hypotheses/csv/h-new-720.json` (per_adjacency).

| Adjacency | δ (Fisher-Rao distance) | fraction of TSP residual |
|:--|:--|:--|
| Q 54 → Q 55 (al-Qamar → al-Raḥmān) | 0.0248 | 0.30% |
| Q 55 → Q 56 (al-Raḥmān → al-Wāqiʿa) | **0.0949** | **1.14%** |

Q 54-Q 55 is one of the corpus's CHEAPEST adjacencies (top-12% cheapest). Q 55-Q 56 is mid-cost (the "bigger" jump is from Q 55 to Q 56's eschatological-creedal expansion).

This means: Q 55 sits on a CHEAP-IN, MID-COST-OUT mushaf seam. The flanking content-Meccan-mufaṣṣal context (Q 54 al-Qamar's dhikr-refrain "yassarna al-Qurʾān li-l-dhikr" 4×, Q 56 al-Wāqiʿa's eschatological creed) is content-cohesive *with* Q 55's cosmic-mercy frame.

## 7. Position in compression-tail laws (H-NEW-660 / H-NEW-700 / H-NEW-770)

Q 55 is at s = 55, just past the s=50 Hijra-kink. Predicted values (from the four laws):

| Law | Equation | Predicted at s=55 | Actual (from H-NEW-700) |
|:--|:--|:--|:--|
| Content compression | d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50) | 0.900 | varies by window |
| Rhyme dispersion | d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50) | 0.380 | — |
| Phoneme dispersion | d̄_phoneme(s) ≈ 0.001 + 0.00089·max(0, s−75) | 0.001 (kink not yet reached) | — |

Q 55 deviates from the local compression-tail prediction (mean_content_distance=1.181 ≫ 0.900). This is precisely what makes it a window-7 outlier under H-NEW-590.

## 8. Architectural type classification

**Anti-iʿjāz-al-fawāṣil + structural-singleton:**

Q 55 belongs to the structural class identified in H-NEW-750 as the *bottom_10_A* — surahs that have HIGH content distinctness PLUS LOW rhyme entropy. Other members of this anti-iʿjāz family include Q 17, 18, 33, 48, 54. They are content-and-rhetoric-distinctive but rhetorically locked into monorhyme/refrain regimes — the OPPOSITE pole from Q 84-100, 113 (the iʿjāz al-fawāṣil archetype).

In the dual-iʿjāz typology of H-NEW-840:
- **structural-iʿjāz** (al-Bāqillānī): Q 33, 1, 2, 9, 24 — high UAS via content + rhyme balance.
- **theological-iʿjāz** (al-Khaṭṭābī): Q 112, 114 — low UAS, high *thuluth* status.
- **refrain-iʿjāz** (NEW class proposed by this profile): **Q 55** — high UAS via content + REFRAIN-density (not rhyme variety). This is a third axis.

A discrete extension of the dual-iʿjāz typology. Cross-reference [[cross-finding-026-iʿjāz-architecture]] to evaluate whether the new third class warrants formal codification at the project level.

## 9. Cross-references to all H-NEW findings touching Q 55

| Finding | Q 55 role |
|:--|:--|
| [[h-new-111-fisher-rao-distance-matrix]] | source of mean_content_distance=1.181 |
| [[h-new-390-q55-outlier-exclusion]] | window-conditional +32.6pp (Meccan-only Q 50-56) |
| [[h-new-590-outlier-spectrum]] | standardized +14.26pp, MODERATE_OUTLIER |
| [[h-new-700-phonological-compression-tail]] | rhyme entropy = 0.4187 nats (low) |
| [[h-new-720-canonical-adjacency-cost]] | Q 54-55 = 0.025; Q 55-56 = 0.095 |
| [[h-new-750-per-surah-iʿjāz-signature]] | sig_A = -3.173 (rank 114/114), corpus-MINIMUM |
| [[h-new-840-unified-architectural-score]] | UAS rank 7/114 |
| [[h-new-860-hadith-architectural-alignment]] | Q 55 *ʿarūs* falls in mid-UAS / mid-fadāʾil zone |

## 10. Honest limits

- **Rules-tuple sensitivity NOT YET tested**: full-tashkeel rhyme-entropy may differ from no-tashkeel; the 0.4187 figure is from H-NEW-750's no-tashkeel pipeline.
- **The +32.6pp vs +14.26pp gap is methodological, not contradictory**: pre-Hijra-restricted windows amplify Q 55's outlier signature; standardized windows diminish it. The MODERATE_OUTLIER classification (+14.26pp) is the rules-tuple-consistent figure.
- **The "anti-iʿjāz / refrain-iʿjāz" naming is provisional**: H-NEW-750 places Q 55 in the *bottom_10_A* group; whether this constitutes a third iʿjāz axis or just an extreme of the existing dual-iʿjāz axis is an open question. See [[06-novel-findings]] §"refrain-iʿjāz typology".
- **Phoneme metrics computed locally; no Bonferroni-controlled corpus comparison was run** for Q 55's phoneme density. They are presented for descriptive context only.

## 11. Verdict

Q 55 is empirically a **MODERATE_OUTLIER** with an extreme refrain-density signature. UAS rank 7/114 places it in the corpus's top decile of architectural significance. Its iʿjāz al-fawāṣil signature is the corpus minimum, but its absolute architectural impact is high. **The "ʿarūs al-Qurʾān" classical honorific maps onto refrain-density + cosmic-mercy theme + dual-pronoun extreme — NOT onto iʿjāz al-fawāṣil**.

Empirical-architecturally, Q 55 is the corpus's most paradigmatic *refrain-iʿjāz* surah.
