---
surah: 40
surah_name: Ghāfir
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: HM-A high-entropy member; structural-iʿjāz mild
---

# Q 40 Ghāfir — empirical profile

## 1. Headline metrics

| Metric | Value | Provenance |
|:--|:--|:--|
| UAS score | -0.868 | h-new-840 |
| UAS rank | 74 / 114 | h-new-840 (re-ranked this session) |
| |outlier| (Δ%ile abs) | 2.37 | h-new-840.all_uas |
| max neighbor TSP cost | 0.1146 | h-new-840 |
| |iʿjāz signature| | 0.796 | h-new-840 |
| sig_A (al-Bāqillānī axis) | +0.80 | brief; consistent w/ h-new-750 |
| Outlier Δ (signed) | −2.37 (anchor-leaning) | brief |
| Rhyme entropy (final-letter, this session) | 2.413 bits | computed min-tashkeel |
| Rhyme entropy (h-new-700, reduced rāwī) | 1.67 bits | brief |
| Top rāwī | ن (38%) | computed |
| Distinct rhyme letters | 8 across 85 verses | computed |
| Top 2-char rhyme suffixes | -ūn (24), -āb (13), -ār (8), -ān (8), -ūd (3) | computed |

## 2. Position in HM-7 cluster (HM-A sub-block)

Q 40 is the **opening surah of the HM-A sub-block** {Q 40, Q 41, Q 42}. The empirical bifurcation finding (this session, [[hawamim-7-cluster-bifurcation]]) places Q 40-42 distinctly above Q 43-46 in rhyme entropy:

| Surah | H (bits, this session) | distinct finals | top final |
|:-:|:-:|:-:|:-:|
| Q 40 | 2.413 | 8 | ن (38%) |
| Q 41 | 2.146 | 10 | ن (56%) |
| Q 42 | 2.565 | 9 | ر (38%) — **only HM-7 surah with non-ن rāwī** |
| — bifurcation midline — | | | |
| Q 43 | 0.594 | 3 | ن (88%) |
| Q 44 | 0.818 | 2 | ن (75%) |
| Q 45 | 0.700 | 2 | ن (81%) |
| Q 46 | 0.952 | 3 | ن (74%) |

Q 40 sits at the high-entropy end (2.413 bits) but with a clean ن rāwī majority. This is the **multi-suffix multi-rāwī pattern**: ن-final but with three distinct *qāfiya* contours (-ūn, -āb, -ār-/-ān-/-ūd) rather than monolithic -ūn.

## 3. Cross-cluster cohesion (FR-roots, h-new-111)

| Set | K | d̄ | %ile in random-K null (10000 perms) |
|:--|:-:|:-:|:-:|
| HM-7 (Q 40-46) | 7 | 0.8672 | 20.11% (moderate-low) |
| HM-A (Q 40-42) | 3 | 0.8624 | 24.72% |
| HM-B (Q 43-46) | 4 | 0.8665 | 24.29% |
| ALR-5 (control) | 5 | 0.9552 | 55.97% |
| ALM-6 (control) | 6 | 0.9257 | 42.86% |

Computed in `/Users/grey/Downloads/quran/scripts/HMM_F_compute.py` (seed 20260428).

**Implication**: Q 40 is content-cohesive with both HM-A and HM-B (similar d̄ ≈ 0.86). The bifurcation is therefore PURELY at the rhyme/prosodic axis, NOT at the FR-roots content axis. This sharpens the *muqaṭṭaʿāt-axis ⊥ content-axis* finding ([[h-new-570-muqattaat-content-cluster|H-NEW-570]], [[h-new-600-letter-families|H-NEW-600]]) by adding a **third orthogonality**: *prosody-axis ⊥ FR-content-axis* even within the most thematically coherent letter-family.

## 4. Compression-tail position (s=40, intra-50)

Q 40 falls in the *intra-50* region (s ≤ 50) where the compression-tail laws have NOT yet kinked downward. From [[h-new-660-compression-tail-gradient|H-NEW-660]]:
- d̄_content(40) ≈ 0.96 (no compression discount yet)
- d̄_rhyme(40) ≈ 0.36 (pre-kink baseline)

Q 40's observed window-d̄ values (per h-new-700) align with the s ≤ 50 baselines — Q 40 is NOT a compression-tail surah, it sits in the prosodically-uniform Meccan-ṭiwāl phase.

## 5. Adjacency cost to neighbors

Per h-new-720 / h-new-840 max_cost data:
- Max neighbor TSP cost = 0.1146.

This is the cost of placing Q 40 between Q 39 and Q 41 in the canonical mushaf order versus an unconstrained 2-opt nearest-neighbor solution. The cost is **moderate** (not extreme) — the canonical placement of Q 40 between Q 39 al-Zumar (a Meccan creedal-confessional surah) and Q 41 Fuṣṣilat (Meccan, ḥawāmīm) is reasonably FR-cheap.

## 6. iʿjāz signature breakdown

- sig_A = +0.80 (positive: al-Bāqillānī *iʿjāz al-fawāṣil* — verse-end rhetorical density above corpus mean)
- |iʿjāz| = 0.796 (modest magnitude)

Q 40's positive sig_A indicates rhetorical-fawāṣil density above mean — consistent with its multi-rāwī rhyme texture (8 distinct finals, multiple suffix shapes). The dramatic-narrative content (Believer-of-Pharaoh monologue) demands rhetorical variation, which the empirical sig_A captures.

## 7. Architectural classification

| Axis | Position |
|:--|:--|
| Structural-iʿjāz (al-Bāqillānī) | mild-positive (sig_A=+0.80, UAS rank 74) |
| Theological-iʿjāz (al-Khaṭṭābī) | not an outlier; not in *thuluth al-Qurʾān* tradition |
| Compression-tail | NOT a tail surah (s=40 ≤ 50) |
| Outlier | mild anchor (Δ=−2.37) |
| Cluster role | **HM-A opener; HM-7 high-entropy lead** |

## 8. Honest limits

1. **UAS=74 is below median** — Q 40 is not a standalone architectural outlier; significance is sub-cluster.
2. **Δ=−2.37 is small** — anchoring is mild, not at the level of Q 1 (+27) or Q 9 (+21).
3. **iʿjāz |sig|=0.80** is mid-magnitude; not a structural-iʿjāz extreme.
4. The bifurcation between HM-A and HM-B is detected at PROSODIC level, not FR-content level — limits the bifurcation to specific axes.

## 9. Cross-references

- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]] — Q 40's role as HM-A opener
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 74
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Δ=−2.37
- [[h-new-750|H-NEW-750]] — sig_A=+0.80
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — pre-kink position s=40
- [[Q041-fussilat/01-empirical-profile|Q 41 empirical-profile]] — adjacent HM-A neighbor
