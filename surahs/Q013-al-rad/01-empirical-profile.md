---
surah: 13
surah_name_ar: الرعد
surah_name_translit: al-Raʿd
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE
---

# Q 13 al-Raʿd — Empirical Architectural Profile

Rules-tuple: `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan, Mashriqi)`. Every numerical value below is computed from data files cited in §10 or pulled directly from H-NEW-XXX artifacts.

## 1. Headline architectural metrics

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **1.043** | **21 / 114** (mid-pack) | [[h-new-840-unified-architectural-score\|H-NEW-840]] all_uas[surah=13] |
| Outlier-strength Δ%ile | **−3.85 pp** | **NULL** classification — Q 13 is NOT a content outlier in window {Q 10-16} | [[h-new-590-outlier-spectrum\|H-NEW-590]] all_surahs_results[X=13] |
| iʿjāz signature sig_A | **+1.323** | **rank 19 / 114** — moderately structural-iʿjāz-positive | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| iʿjāz signature sig_B | **+1.111** | **rank 28 / 114** — moderately above corpus mean | H-NEW-750 |
| Mean Fisher-Rao distance to corpus | **0.9637** | very close to corpus mean 0.9235 | computed from [[h-new-111-fisher-rao-mushaf\|H-NEW-111]] |
| Local cohesion (1-step adjacency) | 1.070 | z = −0.610 (modestly less cohesive than median) | H-NEW-750 |
| Rhyme entropy (Shannon, nats) | **1.7164** | **z = +1.721 — high-rhyme-diversity** | H-NEW-750 |
| Top final letter (rāwī) | **ب (bāʾ)** | **35.7% of 42 letter-final verses** (Q13:15 sajda excluded) | computed |
| Q 12→Q 13 canonical-adjacency cost | **0.2158 length-units** | rank ≈ 11/113 (top-15 expensive) | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] s=12 |
| Q 13→Q 14 canonical-adjacency cost | **0.0497 length-units** | very cheap (bottom-quartile) | H-NEW-720 s=13 |
| max neighbor canonical-adjacency cost | 0.2158 | the LEFT boundary (Q 12→Q 13) | H-NEW-720 |
| Verse count | 43 | mufaṣṣal-ṭiwāl-class | Hafs-Kufan |
| Word count (no-tashkeel) | 928 | computed | |
| Letter count (no-tashkeel) | 3,545 | computed | |

## 2. The architectural signature: structural iʿjāz-positive + cluster anchor

Q 13's empirical profile is markedly different from its mushaf-neighbor Q 12 Yūsuf:

| Axis | Q 12 Yūsuf | Q 13 al-Raʿd |
|:--|:--:|:--:|
| UAS rank | **6/114** (top decile) | **21/114** (mid-pack) |
| Outlier Δ%ile | +14.26 pp (MODERATE_OUTLIER) | **−3.85 pp (NULL)** |
| sig_A rank | 109/114 (very low — anti-iʿjāz) | **19/114 (high — pro-iʿjāz)** |
| Top rāwī | ن at 84% (near-monorhyme) | **ب at 36% (multi-rāwī)** |
| Rhyme entropy z | −0.428 (low) | **+1.721 (high)** |

Q 12 is a continuous-narrative outlier with low rhyme-diversity (the *aḥsan al-qaṣaṣ* signature). **Q 13 is the empirical opposite**: modest content-distinctiveness, HIGH rhyme-diversity, MODERATE structural-iʿjāz-positive sig_A. The Q 12→Q 13 transition (the most-expensive single canonical adjacency in the Q 10-15 band at 0.2158 length-units) is **driven by the architectural signature reversal**, not just by the muqaṭṭaʿāt letter-family change.

**Substantive claim**: Q 13's architectural placement at mushaf-position 13 sits right after the Q 12 narrative-outlier and right before the Q 14 Ibrāhīm cosmological-prayer surah. The mushaf "pays" the Q 12→Q 13 cost to switch register from continuous-narrative to didactic-cosmological + multi-rāwī rhyme structure. Q 13→Q 14 is then near-free because Q 14 inherits Q 13's signature pattern (see §3 — Q 13 and Q 14 are 4-axis architectural twins, d_arch = 0.486).

## 3. Fisher-Rao distance row (Q 13 vs all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` D matrix.

**Five FR-nearest neighbors** (Q 13 is closest to medium-length didactic-prophet surahs):

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 1 | **Q 14 Ibrāhīm** | **0.7838** | mushaf-adjacent ALR cluster member; cosmological-prayer + Ibrāhīm-prayer |
| 2 | Q 40 Ghāfir | 0.7983 | ḤM-cluster + theology of judgment |
| 3 | Q 16 al-Naḥl | 0.8037 | post-mushaf-neighbor (cosmological-signs structure: bees, fruits, animals) |
| 4 | Q 22 al-Ḥajj | 0.8195 | cosmology + judgment + creedal |
| 5 | Q 39 al-Zumar | 0.8253 | theology + Day of Judgment |

The FR-nearest neighbor is **Q 14 Ibrāhīm at 0.7838** — the FR-content cluster is the "didactic-cosmological" register, NOT the muqaṭṭaʿāt letter-family. Q 14 (ALR) is closest, then Q 40 (ḤM), then Q 16 (no muqaṭṭaʿāt), then Q 22 (no muqaṭṭaʿāt), then Q 39 (no muqaṭṭaʿāt). **The signal is content, not letter-family** — consistent with [[h-new-610-letter-families|H-NEW-610]] muqaṭṭaʿāt-content-NULL.

**Five FR-farthest neighbors**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 110 | Q 54 al-Qamar | 1.0784 | refrain-iterative narrative |
| 111 | Q 77 al-Mursalāt | 1.0971 | oath-driven eschatology |
| 112 | Q 26 al-Shuʿarāʾ | 1.1213 | iterative prophet-narrative |
| 113 | Q 56 al-Wāqiʿa | 1.1382 | eschatological-3-class taxonomy |
| 114 | **Q 55 al-Raḥmān** | **1.2713** | refrain-saturated nominal-doxological (corpus-most-distant) |

**Q 55 is Q 13's farthest neighbor — and Q 55 is also Q 12's farthest neighbor.** This consistent finding (Q 55 at FR-distance 1.27 from Q 13; 1.42 from Q 12) is a structural fact about Q 55's *theological-iʿjāz* register being orthogonal to the *prophet-narrative-cosmological* register that anchors Q 12-Q 13-Q 14.

## 4. Outlier window structure (H-NEW-590, full Q 10-16 window)

The window {10, 11, 12, 13, 14, 15, 16} (size-7 centered on Q 13) yields:

| Removed surah | d̄_W | d̄_W−X | Δ pp | classification | source |
|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 13 | 0.9330 | 0.9427 | **−3.85** | **NULL** | H-NEW-590 X=13 |

The full window with Q 13 has d̄_W = 0.933 (47.4%ile); without Q 13, d̄_W = 0.943 (51.3%ile). **Removing Q 13 makes the window MORE FR-distant on average** — i.e. Q 13 is FR-CLOSE to its neighbors in the window. This is the signature of a CLUSTER ANCHOR, NOT an outlier. Q 13 fits its prophet-narrative-cosmological mushaf cohort.

This is the **architecture-invariance evidence** for the chronology debate: the al-Suyūṭī Medinan classification (rev #96) does NOT manifest as architectural outlier-ness in Q 13's mushaf-window. Whether the chronology is Meccan or Medinan, Q 13's empirical signature fits its mushaf cohort, not its chronological cohort.

## 5. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Interpretation |
|:--|:--:|:--:|:--|
| `mean_content_distance` | 0.9637 | +0.398 | slightly above corpus mean — modestly content-distinct |
| `local_cohesion` | 1.0703 | −0.610 | modestly below corpus median — diverse 1-step adjacencies |
| `rhyme_entropy_nats` | **1.7164** | **+1.721** | **HIGH rhyme diversity** — multi-rāwī (ب, ر, ل, ن, د, ق, ع) |
| `sig_A` (raw) | 1.3231 | z = +0.95 (computed) | **rank 19/114 — moderately structural-iʿjāz-positive** |
| `sig_B` (raw) | 1.1106 | z = +0.87 (computed) | **rank 28/114** |

**Q 13 is on the structural-iʿjāz side of the al-Bāqillānī axis** — a multi-rāwī surah with moderate content-distinctness. This puts Q 13 in the *iʿjāz-al-fawāṣil-positive* zone of the dual-iʿjāz typology — specifically the "head-mushaf high-rhyme-entropy" sub-cell shared with Q 14 Ibrāhīm.

## 6. The 4-axis signature: Q 13 ≈ Q 14 architectural twin

Per Q013-F-05 verification (`csv/Q013-F-05.json`):

```
v(Q 13) = [+0.398, +0.950, +0.868, +1.721]   (z_FR, z_sig_A, z_sig_B, z_rhyme)
v(Q 14) = [+0.520, +1.110, +1.144, +2.066]
v(Q 76) = [-0.148, -0.894, -1.374, -1.394]   (al-Insān, mufaṣṣal Medinan reference)

‖v(13) - v(14)‖ = 0.486   ← Q 13 ≈ Q 14
‖v(13) - v(76)‖ = 4.293   ← Q 13 ≠ Q 76 (Medinan-similar-length reference)
```

**Q 13 is the architectural twin of Q 14 Ibrāhīm**, separated by 0.486 in 4-axis Euclidean space. By contrast, Q 76 al-Insān (a clearly-Medinan surah of broadly similar verse count) is at distance 4.293 — nearly **9× further away**. The architectural-twin signal between Q 13 and Q 14 is empirically:
- Both head-mushaf zone (z_FR ≈ +0.4 to +0.5)
- Both moderately structural-iʿjāz-positive (z_sig_A ≈ +0.9 to +1.1)
- Both above-mean sig_B (z_sig_B ≈ +0.9 to +1.1)
- Both extreme-high rhyme entropy (z_rhyme ≈ +1.7 to +2.1)

This is the **strongest single empirical anchor for the chronology-architecture-dissociation framework on Q 13**: regardless of whether Q 13 is Meccan (Ibn ʿAbbās/Mujāhid/Nöldeke) or Medinan (al-Suyūṭī), its architectural signature is empirically near-identical to Q 14 (uncontested Meccan, rev #72). The architecture is determined by mushaf-position + length + content-class, not by chronology.

## 7. Canonical-adjacency profile (H-NEW-720)

| Pair | TSP-cost (length-units) | Rank /113 | Interpretation |
|:--|:--:|:--:|:--|
| Q 12 → Q 13 | **0.2158** | ≈ 11/113 (top-15 EXPENSIVE) | Yūsuf→Raʿd: continuous-narrative → didactic-cosmological transition; ALR → ALMR letter-family change |
| Q 13 → Q 14 | **0.0497** | bottom-quartile (CHEAP) | Raʿd→Ibrāhīm: nearly-free transition; both didactic-cosmological + cosmological-prayer cluster, both high rhyme entropy |

The mushaf "pays" the Q 12→Q 13 cost to seat Q 13 at mushaf-position 13 (entering the cosmological-cluster band Q 13-Q 16) at the cost of leaving the Yūsuf continuous-narrative behind. The Q 13→Q 14 transition is then near-free, as predicted by the 4-axis-twin relationship.

**Q 13's mushaf placement is structurally a "register-pivot"**: it shifts the mushaf from continuous-narrative (Q 10/11/12) to didactic-cosmological (Q 13/14/15/16). Q 13's high-rhyme-entropy + structural-iʿjāz-positive signature is the empirical anchor of this register transition.

## 8. Architectural-cell typology (per cross-finding-026 §13)

By the 7-cell typology in [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.6:

- UAS rank 21/114 — NOT in the top-10 *All-axis* / *Structural-twin-pair* cells.
- sig_A z = +0.95 (rank 19) — moderately positive on the *iʿjāz al-fawāṣil* axis.
- Rhyme entropy +1.721 — among the HIGHEST in the corpus.
- Outlier strength NULL — NOT an outlier.

Q 13 fits the **iʿjāz-al-fawāṣil-pure-extended** cell or a *transitional cell between iʿjāz-al-fawāṣil-pure and the mid-mushaf prophet-narrative cohort*. Specifically:

| Cell | Q 13 fit? |
|:--|:--|
| All-axis (Q 1) | NO — UAS only 21 |
| Structural-twin-pair (Q 24, 33) | NO — sig_A is high-positive, not low-negative |
| Structural-twin-pair-of-one (Q 55) | NO — Q 13 is content-typical, not refrain-saturated |
| iʿjāz-al-fawāṣil-pure (Q 86, 89, 100, 106, 113) | PARTIAL — Q 13 has high sig_A but is not in the corpus tail |
| iʿjāz-al-maʿnā-extreme (Q 112, 114) | NO — Q 13 is not the FR centroid |
| iʿjāz-al-maʿnā-mild (Q 36, 67, 18) | NO — Q 13 is not high-fadāʾil |
| anti-iʿjāz (Q 18) | NO |

**Proposed cell (specialist refinement)**: Q 13 + Q 14 form a **"didactic-cosmological-iʿjāz-positive twin-pair"** in the head-mushaf zone — a sub-cell of *iʿjāz-al-fawāṣil-pure* extended into the head-mushaf rather than the corpus-tail. This refines the typology by recognizing that *iʿjāz al-fawāṣil*-positive surahs occur in BOTH the head-mushaf zone (Q 13/Q 14) AND the terminal qiṣār zone (Q 86/89/100/106/113). The unifying signature is high rhyme-entropy + moderate-to-high sig_A.

## 9. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 13 NULL classification (X=13, delta_pct=−3.85, p_greater_W=0.5256).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 12→Q 13 expensive (rank 11), Q 13→Q 14 cheap.
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A=+1.32 rank 19, sig_B=+1.11 rank 28.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 21/114, UAS=1.043.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 13 FR-nearest = Q 14 (0.784); FR-farthest = Q 55 (1.27).
- [[h-new-97-ALR-prophet-name-cluster]] — Q 13's letter-set is ALMR not ALR; Q 13 falls outside the strict ALR cluster but is a STRUCTURAL ANALOGUE.
- [[cross-finding-008-muqattaat-book-intro-markers]] — Q 13:1 *tilka āyātu al-kitāb* fits the muqaṭṭaʿāt → book-reference pattern (same as Q 10, 12, 15, etc.)
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13 — proposed "didactic-cosmological-iʿjāz-positive head-mushaf sub-cell" with Q 13+Q 14 as exemplar.
- `surahs/Q005-al-maida/06-novel-findings.md` Q005-F-05 — chronology-architecture dissociation framework (REPLICATED by Q013-F-05; F-03 direction-reversed).

## 10. Data-source paths

- `findings/phase-b-hypotheses/csv/h-new-111.json` (FR D matrix)
- `findings/phase-b-hypotheses/csv/h-new-590.json` (outlier-spectrum, all_surahs_results[X=13])
- `findings/phase-b-hypotheses/csv/h-new-720.json` (per-adjacency, s=12 and s=13)
- `findings/phase-b-hypotheses/csv/h-new-750.json` (per-surah iʿjāz signature[surah=13])
- `findings/phase-b-hypotheses/csv/h-new-840.json` (UAS all_uas[surah=13])
- `quran-text/quran-no-tashkeel.json` (verse text, word/letter counts)
- `data/revelation-order.csv` Q 13 row (chronology — Tanzil Egyptian Standard Medinan rev #96; Wikipedia Nöldeke Late Meccan #90)
- `data/hafs-verse-counts.tsv` line 13 (43 verses)
