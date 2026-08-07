---
surah: 6
surah_name_ar: الأنعام
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — all 6 H-NEW metrics integrated; Q 6 is a "creedal-genealogical-Meccan-ṭiwāl" exemplar with mid-rank UAS but unique LIST-FORM prophet-density signature
---

# Q 6 al-Anʿām — Empirical Architectural Profile


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

## 1. UAS rank and components ([[h-new-840-unified-architectural-score|H-NEW-840]])

| Component | Value | Rank |
|:--|--:|--:|
| **UAS** | **−0.132** | **52 / 114** |
| z(|outlier|) — H-NEW-590 | 2.34 | 51 / 114 |
| z(max_neighbor_TSP_cost) — H-NEW-720 | 0.0424 | 99 / 114 (very cheap) |
| z(|sig_A|) — H-NEW-750 | 1.894 | 20 / 114 (above mean for |sig_A|) |

UAS is the standardized z-mean of the three components. Q 6's UAS = −0.132 places it in the **41–60th percentile cluster** — below the corpus mean. Q 6 is **architecturally unremarkable** by the composite UAS metric, despite its classical *fadāʾil* elevation.

## 2. Outlier-strength ([[h-new-590-outlier-spectrum|H-NEW-590]])

- **Δ%ile = +2.34 pp**, classification **WEAK_OUTLIER** (rank 51 / 114).
- Q 6 is essentially indistinguishable from its 7-window neighbourhood (Q 3-9).
- For comparison: Q 33 (rank 1, +31 pp), Q 1 (rank 2, +27 pp), Q 9 (rank 4, +21 pp).

The mid-rank outlier-strength is consistent with Q 6 being a *long-Meccan polemic* that neighbors other long-Meccan polemics — it does NOT punctuate its neighborhood the way the corpus-top outliers do.

## 3. iʿjāz signature ([[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]])

| Component | Value | Rank |
|:--|--:|--:|
| n_verses | 165 | — |
| **rhyme_entropy_nats** | **0.513** | **101 / 114 (LOW)** |
| top_final_letter | **ن** (nūn) | — |
| top_final_letter_frac | **0.873** | (high uniformity) |
| mean_content_distance | 1.068 | — |
| local_cohesion | 1.107 | — |
| z_rhyme_entropy | −0.465 | — |
| z_mean_content_distance | +1.429 | — |
| z_local_cohesion | −0.560 | — |
| **sig_A** = z_rhyme_entropy − z_mean_content_distance | **−1.894** | **101 / 114** |
| sig_B = z_local_cohesion − z_mean_content_distance | −1.025 | 81 / 114 |

**Q 6 is in the anti-iʿjāz quadrant by sig_A** (rank 101/114). Translation: Q 6 has high content-distance (its words are spread out, lots of unique vocabulary) BUT its rhyme is uniform (87% nūn-rhyme — a near-monorhymic surah). This is the OPPOSITE of the *iʿjāz al-fawāṣil* signature (which would be high content + high rhyme variety). Q 6's vocabulary diversity is NOT matched by fāṣila virtuosity.

**Architectural type**: by the [[cross-finding-026-iʿjāz-architecture#13.2-the-expanded-4-cell-typology|cross-finding-026 §13.2 4-cell typology]], Q 6's profile (high outlier-strength rank 51, low sig_A rank 101, mid-rank UAS) is closest to the **anti-iʿjāz al-fawāṣil-with-monolithic-rhyme** sub-cell — similar in shape to Q 18 al-Kahf (which has the same architectural diagnosis: sig_A rank 110, sustained ن-rhyme) but with weaker outlier-strength.

## 4. Canonical-adjacency costs ([[h-new-720-canonical-adjacency-cost|H-NEW-720]])

| Adjacency | delta_raw | fraction_residual | Rank |
|:--|--:|--:|--:|
| Q 5 → Q 6 | 0.0424 | 0.51% | 72 / 113 |
| **Q 6 → Q 7** | **0.000** | **0.00%** | **103 / 113** (literally free — *delta_raw NEGATIVE*) |

⭐ **Q 6 → Q 7 is one of the corpus's MOST cohesive canonical adjacencies** — the canonical mushaf ordering is more efficient than the local 2-opt unconstrained tour for this pair. This is a striking property: Q 6 transitions seamlessly into Q 7 al-Aʿrāf despite Q 7 introducing the المص muqaṭṭaʿāt and shifting from Meccan-ḥujja to Meccan-narrative register. The Q 9 specialist's investigation ([[Q009-al-tawba/06-novel-findings|Q009-F-03]]) used Q 6→Q 7 as the muqaṭṭaʿāt-onset-control: even though Q 7 introduces المص, the boundary cost is essentially zero — falsifying the muqaṭṭaʿāt-cluster-onset-cost hypothesis.

The Q 5 → Q 6 cost (rank 72) is moderate-cheap; the Medinan-legal Q 5 transitions naturally into Meccan-creedal Q 6 despite chronological-jump (Q 5 = revelation #112, Q 6 = revelation #55).

## 5. Compression-tail position

For position s = 6 (head of mushaf), Q 6 is in the **head-ṭiwāl** zone where:
- d̄_content(s) ≈ 0.96 (corpus-extreme dispersion of content roots) — Q 6 fits.
- d̄_rhyme(s) ≈ 0.30 (uniform monorhyme zone) — Q 6's 87.3% ن fits.
- d̄_phoneme(s) ≈ 0.0013 (uniform phoneme distribution) — Q 6 fits.

**Q 6 conforms to the head-ṭiwāl architectural law** ([[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §3, *iʿjāz architecture*): dispersed content + uniform monorhyme + uniform phoneme. This pole is the *opposite* of the terminal-qiṣār (Q 100-114) pole, where content compresses and rhyme diversifies.

## 6. FR-distance neighborhood ([[h-new-111-fisher-rao-mushaf-confirmed|H-NEW-111]])

Q 6's 5 nearest FR-roots-distance neighbors:

| Rank | Surah | FR-distance |
|:-:|:-:|:-:|
| 1 | Q 7 al-Aʿrāf | 0.7208 |
| 2 | Q 10 Yūnus | 0.7396 |
| 3 | Q 16 al-Naḥl | 0.7815 |
| 4 | Q 39 al-Zumar | 0.8035 |
| 5 | Q 2 al-Baqara | 0.8081 |

- **Q 6 mean-d-to-5-nearest = 0.7707** (corpus median = 0.7524, mean = 0.6538).
- **Q 6 isolation rank: 51 / 114** — exactly mid-corpus on isolation.

**Q 6 is NOT a true-isolate** (contrast Q 21's rank 18, Q 1's rank ~2-3). Q 6 sits comfortably within a long-Meccan polemic-narrative neighborhood. The 5 nearest are all long Meccan or Meccan-Medinan-mixed surahs (Q 7, 10, 16, 39, 2) — i.e., al-sabʿ al-ṭiwāl + ALR cluster + Q 39.

This empirically grounds the "Q 6 is the central long-Meccan polemic" intuition: its neighbors ARE the long-Meccan polemic family.

## 7. Pre-Islamic poetry comparison

(See `data/baseline-corpora/letter-freqs.csv` — Q 6 vs muʿallaqāt baseline.)

Q 6 letter-freq distribution conforms to Quranic baseline (high ن, ل, م from inflectional + ḥamd-formula fronting); not visibly distinct from al-sabʿ al-ṭiwāl baseline. Cross-corpus pre-Islamic poetry control is OFF — Q 6 is a Quranic-baseline surah.

## 8. Cross-references to H-NEW findings

| H-NEW | Q 6 entry | Architectural meaning |
|:--|:--|:--|
| [[h-new-111-fisher-rao-mushaf-confirmed|H-NEW-111]] | mean-d-to-5-nearest = 0.7707, rank 51/114 | mid-isolation; long-Meccan polemic neighborhood |
| [[h-new-590-outlier-spectrum|H-NEW-590]] | Δ=+2.34 pp, WEAK_OUTLIER | mid-rank outlier; long-Meccan polemic neighbors are similar |
| [[h-new-700-phonological-compression-tail|H-NEW-700]] | head-ṭiwāl, low rhyme/phoneme dispersion | conforms to head-ṭiwāl law |
| [[h-new-720-canonical-adjacency-cost|H-NEW-720]] | Q 6→Q 7 = rank 103/113 (FREE), Q 5→Q 6 = rank 72/113 | Q 6→Q 7 is one of corpus's MOST cohesive adjacencies |
| [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] | sig_A = −1.894, rank 101/114 | anti-iʿjāz quadrant by sig_A |
| [[h-new-770-verse-length-compression-tail|H-NEW-770]] | words/verse = 20.0 | long-Meccan band |
| [[h-new-840-unified-architectural-score|H-NEW-840]] | UAS = −0.132, rank 52/114 | architecturally unremarkable composite |
| [[h-new-940-prophet-order-conservation|H-NEW-940]] | Q 6 in 8-surah analysis (16/18 prophets — rank-1 distinct) | LIST-FORM prophet-MAX (per [[Q021-al-anbiya/06-novel-findings|Q021-F-01 NULL]]) |

## 9. Architectural classification (summary)

Q 6 al-Anʿām is **a creedal-genealogical-Meccan-ṭiwāl exemplar**:
- Conforms to head-ṭiwāl law: dispersed content + uniform ن-monorhyme + uniform phoneme.
- Mid-rank UAS (52/114): not architecturally distinguished by the composite metric.
- Anti-iʿjāz al-fawāṣil quadrant (sig_A rank 101): vocabulary-diverse but rhyme-uniform — the OPPOSITE of the *iʿjāz al-fawāṣil* signature.
- Most-cohesive Q 6 → Q 7 canonical adjacency: cheap-bridge from Meccan-ḥujja to Meccan-narrative.

**The architectural distinctiveness of Q 6 lies NOT in its composite UAS but in its [LIST-FORM prophet-density](Q006-F-01-prophet-density-per-verse-prereg.md) and [livestock-vocabulary](Q006-F-02-livestock-vocab-prereg.md) signatures** — both of which are **corpus-MAX** (Q006-F-01 Cell B = 1/49; Q006-F-02 = 1/114). See `06-novel-findings.md` for the per-test verdicts.

## 10. Honest limits

- The H-NEW metric suite is single-pipeline (FR-on-stem-roots-top-500-Dirichlet-0.5 + final-letter-rhyme + 4-phoneme-group). Alternative metrics may shift Q 6's rankings.
- Q 6's high content-distance (rank ~10 from corpus-mean = 1.068 vs ~0.93) is partly length-driven (longer surahs naturally have more vocabulary diversity); compression-tail compensates partially but not fully.
- The "anti-iʿjāz" classification is per the H-NEW-750 sig_A metric. al-Bāqillānī never claimed Q 6 had *iʿjāz al-fawāṣil*; his Q 6 attribution is to *iʿjāz al-tawḥīd* (Q 6:103 — see [[Q006-F-05-q6v103-tawhid-ijaz-prereg]] CONFIRMED-UNIQUE-MAX). The two iʿjāz axes are orthogonal.

## 11. Cross-references

- [[00-overview]] §7 (architectural summary).
- [[Q006-F-01-prophet-density-per-verse-prereg]] (prophet-density per verse — LIST-FORM MAX).
- [[Q006-F-02-livestock-vocab-prereg]] (livestock cluster density — corpus MAX).
- [[Q006-F-04-q6-q21-antipodal-prereg]] (FR-distance Q 6 ↔ Q 21).
- [[Q006-F-05-q6v103-tawhid-ijaz-prereg]] (Q 6:103 4-cell tawḥīd-iʿjāz audit).
- [[Q021-al-anbiya/06-novel-findings|Q 21 narrative-form complement]].
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13 (4-cell typology — Q 6 fits the *anti-iʿjāz al-fawāṣil + monolithic rhyme* sub-cell).
