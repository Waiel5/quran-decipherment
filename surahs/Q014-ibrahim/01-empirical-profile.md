---
surah: 14
surah_name_ar: ابراهيم
surah_name_translit: Ibrāhīm
file_type: empirical-profile
date_last_updated: 2026-05-08
phase: B+
verdict: COMPLETE
---

# Q 14 Ibrāhīm — Empirical Architectural Profile

Rules-tuple: `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan, Mashriqi)`. Every numerical value below is computed from data files cited in §10 or pulled directly from H-NEW-XXX artifacts.

## 1. Headline architectural metrics

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **1.245** | **20 / 114** (mid-pack; one rank above Q 13 at 21) | [[h-new-840-unified-architectural-score\|H-NEW-840]] all_uas[surah=14] |
| Outlier-strength Δ%ile | **−4.28 pp** | **NULL** classification — Q 14 is NOT a content outlier in window {Q 11-17} | [[h-new-590-outlier-spectrum\|H-NEW-590]] all_surahs_results[X=14] |
| iʿjāz signature sig_A | **+1.546** | **rank 14 / 114** — top-15 structural-iʿjāz-positive | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| iʿjāz signature sig_B | **+1.464** | **rank 15 / 114** — top-15 | H-NEW-750 |
| z_mean_content_distance | +0.520 | above corpus mean — modestly content-distinct | H-NEW-750 |
| z_local_cohesion | −0.603 | modestly below corpus median — diverse 1-step adjacencies | H-NEW-750 |
| **z_rhyme_entropy** | **+2.066** | **top tier** — multi-rāwī (د / ر / ن / م mixed) | H-NEW-750 |
| Mean Fisher-Rao distance to corpus | **0.9762** | corpus mean 0.9235 | computed from [[h-new-111-fisher-rao-mushaf\|H-NEW-111]] |
| Top final letter (rāwī) | **د (dāl)** | **23.9% of 46 letter-final verses** | H-NEW-750 |
| Q 13→Q 14 canonical-adjacency cost | **0.0497** | bottom-quartile — CHEAP seam | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] s=13 |
| Q 14→Q 15 canonical-adjacency cost | **0.1988** | rank ≈ 13 / 113 — top-15 EXPENSIVE seam | H-NEW-720 s=14 |
| max neighbor canonical-adjacency cost | 0.1988 | the RIGHT boundary (Q 14→Q 15) | H-NEW-720 |
| Verse count | 52 | mufaṣṣal-ṭiwāl-class | Hafs-Kufan |
| Word count (no-tashkeel) | 885 | computed | |
| Letter count (no-tashkeel) | 3,594 | computed | |

## 2. The architectural signature: structural iʿjāz-positive head-mushaf cluster anchor

Q 14's empirical profile pairs naturally with Q 13's. Both surahs share a 4-axis signature that places them in a small head-mushaf "didactic-cosmological-iʿjāz-positive" sub-cell of the iʿjāz architecture. Side-by-side:

| Axis | Q 13 al-Raʿd | Q 14 Ibrāhīm | corpus mean / scale |
|:--|:--:|:--:|:--:|
| z_FR_mean | +0.398 | +0.520 | 0 / 1 |
| sig_A rank | 19 / 114 | **14 / 114** | midrank 57 |
| sig_B rank | 28 / 114 | **15 / 114** | midrank 57 |
| z_rhyme_entropy | +1.721 | **+2.066** | 0 / 1 |
| Top-rāwī fraction | ب @ 36% | **د @ 24%** (more diffuse) | 0.50 (median monorhyme) |
| Outlier classification | NULL | NULL | (40% of corpus is NULL) |
| UAS rank | 21 / 114 | **20 / 114** | midrank 57 |

**Both surahs are above-mean on every axis except local_cohesion**, where they are mildly below mean. Q 14 is **slightly stronger than Q 13 on every iʿjāz axis** — higher rhyme entropy, higher sig_A, higher sig_B, modestly higher z_FR. The pair (Q 13, Q 14) is the head-mushaf zone's "high-rhyme-entropy + structural-iʿjāz-positive twin pair", with Q 14 the slightly stronger member.

**Substantive claim**: Q 14's mushaf placement at position 14 sits at a register-stable continuation of Q 13's signature (Q 13→Q 14 seam cost = 0.0497, near-free), then transitions sharply into Q 15's iterative-prophet-narrative register (Q 14→Q 15 seam cost = 0.1988, top-15 expensive). The mushaf achieves a low-cost Q 13→Q 14 transition by paying a high-cost transition out at the Q 14→Q 15 seam. The Q 13-Q 14 pair is structurally bonded; Q 14-Q 15 is structurally separated.

## 3. Fisher-Rao distance row (Q 14 vs all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` D matrix (`D_matrix_upper_triangular`).

**Five FR-nearest neighbours of Q 14**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| **1** | **Q 13 al-Raʿd** | **0.7838** | mushaf-adjacent ALMR-letter-set; bilateral mutual-nearest pair (this is also Q 13's nearest) |
| 2 | Q 40 Ghāfir | 0.8068 | ḤM-cluster + theology of judgment + believer-prayer-block |
| 3 | Q 22 al-Ḥajj | 0.8252 | cosmology + judgment + creedal |
| 4 | Q 35 Fāṭir | 0.8368 | cosmological-creator + believers-vs-disbelievers |
| 5 | Q 71 Nūḥ | 0.8369 | prophet-prayer-saturated short surah (Q 71 has Nūḥ's full prayer block) |

The FR-nearest neighbour is **Q 13 at 0.7838** — confirming the bilateral mutual-nearest pair (Q 13's nearest is also Q 14). The next tier is dominated by the head-mushaf cosmological-theological surahs (Q 40, 22, 35) and one prayer-saturated short prophet-surah (Q 71 Nūḥ), reflecting Q 14's two thematic foci: cosmological theology + prophet-prayer.

**Five FR-farthest neighbours**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 110 | Q 75 al-Qiyāma | 1.0813 | terminal eschatology |
| 111 | Q 77 al-Mursalāt | 1.0948 | oath-driven eschatology |
| 112 | Q 80 ʿAbasa | 1.0979 | brief moral-creation surah |
| 113 | Q 56 al-Wāqiʿa | 1.1669 | eschatological-3-class taxonomy |
| 114 | **Q 55 al-Raḥmān** | **1.2912** | refrain-saturated nominal-doxological (corpus-most-distant) |

**Q 55 is Q 14's farthest neighbour** — the same as Q 13 and Q 12. Q 55's *theological-iʿjāz* register (refrain-saturated, low-content-vocabulary) is consistently orthogonal to the prophet-narrative-cosmological-prayer register that anchors Q 12-Q 13-Q 14. This three-surah convergence on Q 55 as anti-twin is itself a corpus-architectural fact (cf. cross-finding-026 §13 dual-iʿjāz typology).

## 4. Bilateral mutual-nearest pair (Q 13 ↔ Q 14)

Out of 6,441 corpus surah-pairs, the FR distance d(Q13, Q14) = 0.7838 sits at percentile ≈ 7.5% (well into the FR-close tail; corpus pairwise median 0.9567). The pair is **mutually nearest** — Q 13's row's argmin is Q 14, and Q 14's row's argmin is Q 13. This is the **strongest possible bilateral cluster signal** at this metric.

How rare is mutual-nearest? In a corpus with 114 surahs, even with completely random distances, the expected count of mutual-nearest pairs is ≈ 114 × 1/113 ≈ 1.01. The empirical count (computed corpus-wide as a follow-on count, not pre-registered for Q 14) is small and clustered in known-architectural regions (e.g., Q 113-Q 114, Q 1-Q 2, Q 10-Q 11). Q 13 ↔ Q 14 belongs to this rare set of mutual-nearest mushaf-adjacent pairs.

**Q014-F-02 confirms** this bilateral status from Q 14's perspective.

## 5. Outlier window structure (H-NEW-590, full Q 11-17 window)

The window {11, 12, 13, 14, 15, 16, 17} (size-7 centered on Q 14) yields:

| Removed surah | d̄_W | d̄_W−X | Δ pp | classification | source |
|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 14 | 0.9517 | 0.9619 | **−4.28** | **NULL** | H-NEW-590 X=14 |

The full window with Q 14 has d̄_W = 0.952 (58.2%ile); without Q 14, d̄_W = 0.962 (62.5%ile). **Removing Q 14 makes the window MORE FR-distant on average** — i.e. Q 14 is FR-CLOSE to its neighbours in the window, the signature of a **CLUSTER ANCHOR**, NOT an outlier. Q 14 fits its prophet-narrative-cosmological-prayer mushaf cohort.

This is the same NULL pattern as Q 13 (Δ = −3.85, also NULL), reinforcing the cluster-anchor reading: both Q 13 and Q 14 are FR-close to their mushaf-window cohort; both are not outliers; both are anchors that hold the head-mushaf prophet-narrative band together.

## 6. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Interpretation |
|:--|:--:|:--:|:--|
| `mean_content_distance` | 0.9762 | +0.520 | above corpus mean — modestly content-distinct |
| `local_cohesion` | 1.0759 | −0.603 | modestly below corpus median |
| `rhyme_entropy_nats` | **1.9109** | **+2.066** | **TOP-tier rhyme diversity** — multi-rāwī (د/ر/ن/م) |
| `sig_A` (raw) | **1.546** | rank **14 / 114** | **top-15 structural-iʿjāz-positive** |
| `sig_B` (raw) | **1.464** | rank **15 / 114** | **top-15** |

**Q 14 is firmly in the structural-iʿjāz-positive zone of the al-Bāqillānī axis** — high rhyme diversity, modest content-distinctness, top-15 sig_A and sig_B. This puts Q 14 in the *iʿjāz al-fawāṣil-positive* head-mushaf zone, with Q 13 as its near-twin.

## 7. The 4-axis signature: bilateral mutual nearest with Q 13

Per Q014-F-02 (`csv/Q014-F-02.json`):

```
v(Q 14) = [+0.520, +1.110, +1.144, +2.066]   (z_FR, z_sig_A, z_sig_B, z_rhyme)
v(Q 13) = [+0.398, +0.950, +0.868, +1.721]
v(Q 76) = [-0.148, -0.894, -1.374, -1.394]   (al-Insān, mufaṣṣal Medinan reference)

‖v(14) - v(13)‖ = 0.486   ← Q 14 ≈ Q 13 (4-axis)
‖v(14) - v(76)‖ = 4.474   ← Q 14 ≠ Q 76
```

Q 14 is **9.20× closer to Q 13 than to Q 76 al-Insān** (a Medinan similar-length reference). Per Q013-F-05, Q 13 is **8.83× closer to Q 14 than to Q 76**. The bilateral architectural-twin signal between Q 13 and Q 14 is mutual: Q 13 ↔ Q 14 in 4-axis Euclidean signature space, both at d ≈ 0.486, with each ≈ 9× closer than to a Medinan-similar-length reference.

## 8. Canonical-adjacency profile (H-NEW-720)

| Pair | TSP-cost (length-units) | Rank /113 | Interpretation |
|:--|:--:|:--:|:--|
| Q 13 → Q 14 | **0.0497** | bottom-quartile (CHEAP) | Raʿd→Ibrāhīm: nearly-free; both didactic-cosmological-prayer-iʿjāz-positive twin |
| Q 14 → Q 15 | **0.1988** | ≈ 13/113 (top-15 EXPENSIVE) | Ibrāhīm→Ḥijr: didactic-prayer-multi-rāwī (Q 14) → iterative-prophet-near-monorhyme-ن (Q 15); register flip + sig_A flip |

Q 14 sits between a near-free Q 13→Q 14 entry and a top-15-expensive Q 14→Q 15 exit. The mushaf "pays" the 0.20 cost at Q 14→Q 15 to leave the head-mushaf high-rhyme-entropy + sig_A-positive band and enter the Q 15-Q 17 narrative-iterative band (Q 15 is sig_A negative at rank 81/114, with monorhyme on ن at 82%). This Q 14→Q 15 cost is structurally **the boundary of the head-mushaf iʿjāz-positive zone**.

## 9. Architectural-cell typology (per cross-finding-026 §13)

By the 7-cell typology in [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.6:

- UAS rank 20/114 — modestly above the *iʿjāz al-fawāṣil-pure* cell threshold but not in top-10 *All-axis* / *Structural-twin-pair*.
- sig_A z = +0.95 (rank 14) — moderately positive on the *iʿjāz al-fawāṣil* axis.
- Rhyme entropy +2.07 — among the highest in the corpus.
- Outlier strength NULL — NOT an outlier.

| Cell | Q 14 fit? |
|:--|:--|
| All-axis (Q 1) | NO — UAS only 20 |
| Structural-twin-pair (Q 24, 33) | NO — sig_A is high-positive, not low-negative |
| Structural-twin-pair-of-one (Q 55) | NO — Q 14 is content-typical, not refrain-saturated |
| iʿjāz-al-fawāṣil-pure (Q 86, 89, 100, 106, 113) | PARTIAL — Q 14 has high sig_A but is in head-mushaf, not corpus tail |
| iʿjāz-al-maʿnā-extreme (Q 112, 114) | NO — Q 14 is not the FR centroid |
| iʿjāz-al-maʿnā-mild (Q 36, 67, 18) | NO — Q 14 is not high-fadāʾil |

**Proposed cell (specialist refinement, mirroring Q 13's analysis)**: Q 13 + Q 14 form a **"didactic-cosmological-prayer-iʿjāz-positive twin-pair"** in the head-mushaf zone — a sub-cell of *iʿjāz-al-fawāṣil-pure* extended into the head-mushaf. Q 14 is the slightly stronger member of the pair.

This refines the typology by recognizing that *iʿjāz al-fawāṣil*-positive surahs occur in BOTH the head-mushaf zone (Q 13/Q 14) AND the terminal qiṣār zone (Q 86/89/100/106/113). The unifying signature is high rhyme-entropy + moderate-to-high sig_A + content-typical FR distance.

## 10. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 14 NULL classification (X=14, delta_pct=−4.28, p_greater_W=0.4183).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 13→Q 14 cheap (0.050), Q 14→Q 15 expensive (0.199, rank ≈13).
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A=+1.55 rank 14, sig_B=+1.46 rank 15, rhyme_entropy z=+2.07.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 20/114, UAS=1.245.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 14 FR-nearest = Q 13 (0.784); FR-farthest = Q 55 (1.29).
- [[h-new-97-ALR-prophet-name-cluster]] — Q 14 is in the strict ALR cluster {Q 10, 11, 12, 14, 15}.
- [[cross-finding-008-muqattaat-book-intro-markers]] — Q 14:1 *kitābun anzalnāhu ilayka* fits the muqaṭṭaʿāt → book-reference pattern (parallel to Q 12:2, 13:1, 15:1).
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13 — proposed "didactic-cosmological-prayer-iʿjāz-positive head-mushaf sub-cell" with Q 13 + Q 14 as exemplar (Q 14 the stronger member).
- `surahs/Q013-al-rad/06-novel-findings.md` Q013-F-05 — established Q 13 ≈ Q 14 unilaterally; Q014-F-02 verifies bilaterally.

## 11. Data-source paths

- `findings/phase-b-hypotheses/csv/h-new-111.json` (FR D matrix, `D_matrix_upper_triangular`)
- `findings/phase-b-hypotheses/csv/h-new-590.json` (outlier-spectrum, all_surahs_results[X=14])
- `findings/phase-b-hypotheses/csv/h-new-720.json` (per-adjacency, s=13 and s=14)
- `findings/phase-b-hypotheses/csv/h-new-750.json` (per-surah iʿjāz signature[surah=14])
- `findings/phase-b-hypotheses/csv/h-new-840.json` (UAS all_uas[surah=14])
- `quran-text/quran-no-tashkeel.json` (verse text, word/letter counts)
- `data/revelation-order.csv` Q 14 row (Late Meccan, rev #72 Tanzil / #76 Nöldeke)
- `data/hafs-verse-counts.tsv` line 14 (52 verses)
