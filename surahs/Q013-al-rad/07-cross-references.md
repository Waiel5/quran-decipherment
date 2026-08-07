---
surah: 13
surah_name_ar: الرعد
surah_name_translit: al-Raʿd
file_type: cross-references
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE
---

# Q 13 al-Raʿd — Cross-References


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

## 1. Direct mushaf neighbours

### Q 12 Yūsuf → Q 13 al-Raʿd (left seam)

- **TSP cost: 0.2158 length-units** ([[h-new-720-canonical-adjacency-cost|H-NEW-720]] s=12). **Top-15 expensive in corpus** (rank ≈ 11/113).
- Letter-family change: **ALR (Q 12) → ALMR (Q 13)** — the only such transition in the corpus.
- Register shift: Q 12 is a continuous-narrative outlier (UAS rank 6/114, sig_A rank 109/114, top-rāwī ن at 84%); Q 13 is a didactic-cosmological surah (UAS rank 21, sig_A rank 19, multi-rāwī ب at 36%). The architectural reversal is sharp.
- al-Biqāʿī's *munāsabah*: thematically connected (from prophetic-narrative to cosmological-theological reflection on prophetic revelation) — al-Biqāʿī's *Naẓm al-durar* on Q 12-13 frames the seam as a thematic progression. The empirical metric flags it as costly, indicating that thematic-progression and architectural-cohesion are different axes.
- The mushaf "pays" the Q 12→Q 13 cost as part of the price of seating Q 13 at mushaf-position 13 (entering the cosmological/theological cohort).

### Q 13 al-Raʿd → Q 14 Ibrāhīm (right seam)

- **TSP cost: 0.0497 length-units** (very cheap; bottom-quartile).
- Letter-family change: **ALMR (Q 13) → ALR (Q 14)** — back into ALR cluster.
- Register similarity: Q 13 and Q 14 are **architectural twins** at 4-axis distance d = 0.486 (Q013-F-05 result). Both are head-mushaf cosmological-theological surahs with high rhyme entropy and moderate-positive sig_A.
- al-Biqāʿī's *munāsabah*: from corporate cosmological reflection (Q 13) to personal-prophetic prayer (Q 14, Ibrāhīm's invocation). Empirically vindicated: the seam is near-free in TSP-cost AND near-zero in 4-axis distance.
- **Q 14 is Q 13's overall FR-NEAREST surah in the corpus** (FR=0.7838).

## 2. Letter-family clusters

### ALMR — corpus-singleton

Q 13's letter-family is **ALMR — corpus-unique 4-letter combination**. There is no ALMR cluster (no other surah opens with these 4 letters).

### ALR cluster — Q 13's MUSHAF-NEIGHBORHOOD context

Q 13 is mushaf-positioned IN-BETWEEN the ALR cluster:
- Left of Q 13: Q 10 Yūnus, Q 11 Hūd, Q 12 Yūsuf (ALR).
- Right of Q 13: Q 14 Ibrāhīm, Q 15 al-Ḥijr (ALR).

| Surah | Letter-family | Verses | Notes |
|:--|:--|:-:|:--|
| Q 10 Yūnus | ALR | 109 | Multi-prophet narrative + theology |
| Q 11 Hūd | ALR | 123 | Multi-prophet narrative |
| Q 12 Yūsuf | ALR | 111 | Single-protagonist continuous narrative |
| **Q 13 al-Raʿd** | **ALMR (corpus-unique)** | **43** | **Didactic-cosmological + iʿjāz declaration** |
| Q 14 Ibrāhīm | ALR | 52 | Cosmological-theological + Ibrāhīm prayer |
| Q 15 al-Ḥijr | ALR | 99 | Multi-prophet vignette + Iblīs |

Q 13 sits in this band **as a structural pivot**: the ALR cluster's 5 surahs surround Q 13, but Q 13's content register is more cosmological than narrative-prophet (which is the ALR cluster's signature per [[h-new-97]]). Per Q013-F-04 (ALR-cluster membership test): Q 13's mean FR distance to ALR siblings (0.930) is comparable to ALR-internal pairwise mean (0.955), but the difference is not statistically distinctive. **Q 13 fits the ALR neighborhood pattern but does not distinctively cluster with ALR siblings on FR-content axis.**

### ALM cluster — surprising direction

Per Q013-F-01 result: **Q 13 is empirically FR-CLOSER to the ALM cluster (d̄ = 0.891) than to the ALR cluster (d̄ = 0.930)**. The 4-letter combination الم + ر may encode a content-vector that aligns more with ALM (cosmological-theological-creedal: Q 2 al-Baqara, Q 3 Āl ʿImrān, Q 29-32 cosmological cohort) than with ALR (prophet-narrative). This is consistent with [[h-new-610-letter-families]] (letter-family-content-NULL framework) — the directional asymmetry is one of many possible cluster-relationships and is not Q13-distinctive at strict significance.

## 3. Architectural-twin pair: Q 13 ↔ Q 14

Per Q013-F-05 (the strongest finding of the run):

```
v(Q 13) = [+0.398, +0.950, +0.868, +1.721]
v(Q 14) = [+0.520, +1.110, +1.144, +2.066]
‖v(13) − v(14)‖ = 0.486
```

Q 13 and Q 14 are **architectural twins** in 4-axis Euclidean space. Both are:
- Head-mushaf zone (z_FR_mean modest-positive +0.4 to +0.5).
- Moderately structural-iʿjāz-positive (z_sig_A +0.95 to +1.11; rank ≤ 25/114).
- Above-mean sig_B (z_sig_B +0.87 to +1.14).
- Extreme-high rhyme entropy (z_rhyme +1.72 to +2.07).

The Q 13 ↔ Q 14 architectural twin pair is the **strongest single empirical anchor for the chronology-architecture-dissociation framework on Q 13** — regardless of whether Q 13 is classically Meccan or Medinan, its empirical signature is near-identical to Q 14 (uncontested Meccan rev #72).

This twin-pair-by-architecture is distinct from the *Structural-twin-pair* cell (Q 24, Q 33) defined in [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.6. Q 24-Q 33's twin signature is "high outlier + bracketed top-15 adjacency BOTH sides + LOW sig_A". Q 13-Q 14's twin signature is "head-mushaf zone + moderate sig_A + extreme rhyme entropy". This is a NEW (proposed) sub-cell of the iʿjāz-architecture typology — see §6 below.

## 4. FR-content cluster: Q 13's 5 nearest neighbours

Per `01-empirical-profile.md` §3:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 1 | Q 14 Ibrāhīm | 0.7838 | architectural twin |
| 2 | Q 40 Ghāfir | 0.7983 | ḤM-cluster, theology of judgment |
| 3 | Q 16 al-Naḥl | 0.8037 | cosmological-signs (bees, fruits) |
| 4 | Q 22 al-Ḥajj | 0.8195 | cosmology + judgment |
| 5 | Q 39 al-Zumar | 0.8253 | theology of Day of Judgment |

Q 13's **FR-content cluster is the "didactic-cosmological-theological" register**, NOT the muqaṭṭaʿāt letter-family. Q 14 (ALR), Q 40 (ḤM), Q 16 (no muqaṭṭaʿāt), Q 22 (no muqaṭṭaʿāt), Q 39 (no muqaṭṭaʿāt) — the signal is content, not letter-family. This is consistent with [[h-new-610-letter-families]] muqaṭṭaʿāt-content-NULL.

## 5. FR-distance contrast: Q 13's farthest = Q 55 (also Q 12's farthest)

Q 13's FR-FARTHEST surah is **Q 55 al-Raḥmān at FR = 1.2713**. By comparison, Q 12 Yūsuf's FR-farthest is also Q 55 (at FR = 1.4185). The consistent finding (Q 55 distant from both Q 12 and Q 13) is a structural fact about Q 55's *theological-iʿjāz / refrain-saturated* register being orthogonal to the *prophet-narrative-cosmological* register that anchors the Q 12-Q 13-Q 14 cluster.

## 6. Cross-finding-026 §13 architectural cell typology

Q 13 fits the proposed **iʿjāz-al-fawāṣil-pure-extended-into-head-mushaf** sub-cell, with Q 14 Ibrāhīm as the architectural twin:

| Cell | Surahs | Defining signature |
|:--|:--|:--|
| All-axis | Q 1 | high outlier + high TSP + high sig_A; *umm al-Kitāb* |
| Structural-twin-pair | Q 24, Q 33 | high outlier + bracketed top-15 adjacency BOTH sides + LOW sig_A |
| Structural-twin-pair-of-one | Q 55 | corpus-min sig_A + rank-1 refrain |
| iʿjāz-al-fawāṣil-pure (corpus-tail) | Q 86, 89, 100, 106, 113 | high sig_A, moderate outlier; corpus-tail |
| iʿjāz-al-maʿnā (extreme) | Q 112, 114 | low UAS, max FR-roots centrality |
| iʿjāz-al-maʿnā (mild) | Q 36, 67, 18 | mid UAS + high *fadāʾil* |
| anti-iʿjāz | Q 18 (per Q 18 specialist proposal) | sig_A rank 110 + monolithic alif-monorhyme |
| **(NEW PROPOSED) iʿjāz-al-fawāṣil head-mushaf twin-pair** | **Q 13, Q 14** | **head-mushaf zone + moderate-positive sig_A + extreme rhyme entropy + cheap Q 13→Q 14 seam** |

The proposed Q 13-Q 14 sub-cell is supported by:
- Empirical 4-axis twin signature at d = 0.486 (Q013-F-05).
- Cheap Q 13→Q 14 canonical-adjacency cost (0.0497, bottom-quartile).
- Both surahs are mid-pack UAS (Q 13: 21; Q 14: 38) — NOT in the all-axis or structural-twin-pair cells.
- Both surahs are head-mushaf (s ≤ 50, pre-Hijra-kink), NOT in the corpus-tail iʿjāz-al-fawāṣil-pure cell.
- Both surahs have extreme-high rhyme entropy (z > 1.7) — directly on the iʿjāz al-fawāṣil axis but in a different mushaf zone than the corpus-tail cell.

This expansion is QUEUED for cross-finding-026 §13.X amendment if validated by further investigation (e.g., a corresponding test on Q 14 from a Q 14 specialist).

## 7. Cross-references to project-level findings

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 13 FR-nearest Q 14; FR-farthest Q 55.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 13 X=13 row: NULL classification (delta_pct = −3.85, p_greater_W = 0.526). Architecture-invariance evidence.
- [[h-new-610-letter-families|H-NEW-610]] — ALR-5 NULL on whole-surah FR cohesion (56.25%ile); ALMR is a singleton, untested as a letter-family in this work but consistent with the cluster-NULL framework.
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 13 at s=13 in the head-cohort plateau d̄_content ≈ 0.96; Q 13 observed 0.9637 — spot-on prediction.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 13 fits the head-rhyme-low-dispersion pole, with the SHEAR being its multi-rāwī (z_rhyme = +1.72 — high relative to its head-zone position, indicating Q 13 is a mid-mushaf rhyme-anomaly: a high-rhyme-entropy surah in the head-zone where rhyme-entropy is generally low. This is the iʿjāz-positive signature of the proposed Q 13-Q 14 sub-cell.)
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 12→Q 13 expensive (rank 11); Q 13→Q 14 cheap.
- [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] — Q 13 fits the iʿjāz anti-twin pattern (modest-positive z_FR + extreme-positive z_rhyme).
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 13 sig_A rank 19; sig_B rank 28.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 13 UAS rank 21/114.
- [[h-new-97-ALR-prophet-name-cluster|H-NEW-97]] — Q 13's ALMR is NOT the ALR family; Q 13 is named after a NATURAL PHENOMENON (al-raʿd, thunder), an exception in the band of prophet-named surahs Q 10/11/12/14/15 (Yūnus, Hūd, Yūsuf, Ibrāhīm, al-Ḥijr).
- [[cross-finding-008-muqattaat-book-intro-markers|cross-finding-008]] — Q 13:1 *tilka āyātu al-kitāb* fits the muqaṭṭaʿāt → book-reference pattern (same as Q 10:1, Q 12:1, Q 15:1, Q 27:1, Q 28:2, Q 31:2, Q 41:1-2, Q 43:2-3, Q 45:2). Q 13 is one of the prototypical examples of this pattern.
- [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] — Q 12-Q 13 adjacency cost contributes ~2.6% of the 11% TSP residual.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13 — proposed Q 13-Q 14 head-mushaf iʿjāz-al-fawāṣil twin-pair sub-cell.

## 8. Cross-references to per-surah investigations

- [[Q005-al-maida/06-novel-findings|Q 5 al-Māʾida — Q005-F-05]]: chronology-architecture dissociation framework. Q 13 is the **first replication test on a contested-chronology surah**; Q013-F-05 CONFIRMED 3/3 sub-tests.
- [[Q012-yusuf/06-novel-findings|Q 12 Yūsuf — Q012-F-01..F-04]]: Q 12 narrative-purity rank 1/114; Yūsuf-token concentration 92.6%. Q 12-Q 13 mushaf seam is the project's most-expensive ALR→ALMR canonical adjacency.
- [[Q012-yusuf/05-classical-claims-audit|Q 12 audit Claim 4]]: Q 12 self-frames with q-s-s root at head-and-tail. The Q 12-Q 13 seam is structurally the boundary between the q-s-s-bracketed continuous-narrative and the cosmological-theological reflection.
- [[Q009-al-tawba/06-novel-findings|Q 9 al-Tawba — Q009-F-03]]: Q 9-Q 10 boundary is the 4th-most-expensive canonical adjacency (3.73% of TSP residual). The Q 12-Q 13 boundary is similarly costly (2.6%). Both are register-shift seams; the mushaf "pays" structural-cohesion cost at register-shift boundaries.
- [[Q024-al-nur/01-empirical-profile|Q 24 al-Nūr — empirical profile §3]]: Q 24's *Structural-twin-pair* signature differs from Q 13's *iʿjāz-al-fawāṣil head-mushaf twin-pair* signature. Q 24 has LOW sig_A; Q 13 has HIGH sig_A. The two cells are distinguishable empirically.

## 9. Future investigation queue

- **Q 14 Ibrāhīm specialist run** would directly test the Q 13-Q 14 architectural-twin claim from the Q 14 side. Expected: Q 14 is similarly a head-mushaf high-rhyme-entropy moderate-sig_A surah, and Q 14's nearest FR-neighbor is Q 13.
- **Q 76 al-Insān specialist run** would clarify whether the F-05 Q 76 reference is robust (Q 76 is the closest Medinan surah by verse-count to Q 13; testing whether Q 76's signature is empirically Medinan-like).
- **F-03 follow-on**: re-run with M = mean(v(Q6), v(Q7)) only (excluding Q 5). Pre-reg pending. This is a follow-on test on a distinct centroid construction; queueing as a new pre-reg.
- **ALMR letter-family lattice — content-axis hypothesis**: F-01 found Q 13 closer to ALM than to ALR. A pre-registered test on whether the 4-letter combination الم + ر encodes ALM-leaning content (e.g., does Q 13's vocabulary share more roots with Q 2/3/29-32 than with Q 10/11/12/14/15?) is queued.
