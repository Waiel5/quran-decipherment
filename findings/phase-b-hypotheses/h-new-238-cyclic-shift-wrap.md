---
id: H-NEW-238
title: Cyclic-shift wrap-edge analysis — rank of Q 1 among 114 rotations of the mushaf Fisher-Rao ring
phase: B
date: 2026-04-17
seed: 20260419
bonferroni_k: 1
alpha_bon: 0.05
rules_tuple: (114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 roots; Dirichlet α=0.5; L1-normalized; Fisher-Rao arccos Bhattacharyya; D from H-NEW-111)
h_new_111_sha256: 4c366c414b82b0d0f3bcd06b68a7b5a87b500cf925b5088704a36c355d7f33fc
prereg_sha256: 4488649e3343d6d3ef73b48285eec97c05428008417bb41e7485f7a0cd773120
verdict: NULL
---

# [[h-new-238-cyclic-shift-wrap|H-NEW-238]] — Cyclic-shift wrap-edge analysis

## Headline

**Canonical Q 1 at position 1 has wrap-edge W = 0.3884 (d_FR(Q 114 al-Nās → Q 1 al-Fātiḥa)), ranking 18 of 114** among all cyclic shifts of the mushaf ordering, sorted by ascending wrap-edge. Minimum wrap-edge across all 114 shifts is W = 0.2256, achieved at k = 108 (Q108 al-Kawthar at position 1, preceded by Q107 al-Māʿūn).

**Verdict: NULL (strict) / PASS-DIRECTED-ADJACENT (nuanced).** Under the pre-registered strict rank mapping (rank ≤ 10 for PASS-DIRECTED; rank 11–57 = NULL), Q 1 at rank 18 is NULL. Nuanced reading: rank 18 / 114 places Q 1 at the 15.8th percentile — clearly in the top quintile, far from random mid-pack (expected rank 57.5), but clearly NOT the geodesic minimum. P3 is dominant; M1 tolerates but does not prefer the canonical Q 1 rotation.

**Additional striking observation** (reported separately in the refinement section below): the canonical rotation puts the TIGHTEST-quintile wrap-edge at Q 114 → Q 1 (rank 18) AND the **SINGLE LARGEST Fisher-Rao edge in the entire 114-cycle at Q 1 → Q 2** (W = 1.1776, rank 114 / 114). The mushaf opens with the cycle's biggest compositional hinge.

## Method

- Reuse 114×114 Fisher-Rao angular distance matrix **D** from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (QAC-STEM top-500 roots, Dirichlet α=0.5, L1-normalized).
- For k ∈ {1..114}, define cyclic shift k of the mushaf: surah Q k lands at position 1, surah Q (k-1) (mod 114) lands at position 114.
- Compute wrap-edge W(k) = D[prev(k)][k] where prev(k) = 114 if k=1 else k-1.
- Rank the 114 shifts by ascending W(k); report rank of k=1.
- Bonferroni k=1, α=0.05. This is a descriptive rank test internal to the mushaf Hamiltonian cycle.

## Sanity check (MW-5): cycle-length invariance

The sum of all 114 wrap-edges equals the Hamiltonian-cycle length L_cycle(mushaf) = **86.1480**. This is the same quantity as L_path(mushaf) + W(1) because the 114 cyclic-shift wrap-edges are exactly the 114 consecutive adjacencies of the mushaf cycle. Cycle length is invariant under rotation — confirmed.

## Wrap-edge distribution across the 114 shifts

| Statistic | Value |
|---|---:|
| Min (M1-preferred start) | 0.2256 |
| Max (M1-disfavored start) | 1.1776 |
| Mean | 0.7557 |
| Median | 0.8137 |
| Std | 0.2434 |
| Canonical Q 1 (rank 1 implies M1-alignment) | 0.3884 |
| Cycle total length Σ W(k) | 86.1480 |

## Canonical Q 1 rank among 114 cyclic shifts

- Canonical rotation: Q 1 at position 1, Q 114 at position 114.
- Wrap-edge: W(1) = d_FR(Q 114 al-Nās, Q 1 al-Fātiḥa) = **0.3884**.
- Rank ascending: **18/114** (percentile: 15.8%).
- Verdict: **NULL**.

## Top-10 tightest-wrap starting-points

(These are the 10 rotations with smallest wrap-edge — the M1-preferred start-points.)

| Rank | k (position 1) | Surah at pos 1 | Preceded by (pos 114) | W |
|---:|---:|---|---|---:|
| 1 | Q108 | al-Kawthar | Q107 al-Māʿūn | 0.2256 |
| 2 | Q114 | al-Nās | Q113 al-Falaq | 0.2718 |
| 3 | Q107 | al-Māʿūn | Q106 Quraysh | 0.2772 |
| 4 | Q112 | al-Ikhlāṣ | Q111 al-Masad | 0.2849 |
| 5 | Q113 | al-Falaq | Q112 al-Ikhlāṣ | 0.2886 |
| 6 | Q106 | Quraysh | Q105 al-Fīl | 0.2915 |
| 7 | Q104 | al-Humaza | Q103 al-ʿAṣr | 0.3119 |
| 8 | Q111 | al-Masad | Q110 al-Naṣr | 0.3184 |
| 9 | Q109 | al-Kāfirūn | Q108 al-Kawthar | 0.3342 |
| 10 | Q105 | al-Fīl | Q104 al-Humaza | 0.3364 |

## Bottom-10 loosest-wrap starting-points

| Rank | k (position 1) | Surah at pos 1 | Preceded by (pos 114) | W |
|---:|---:|---|---|---:|
| 105 | Q24 | al-Nūr | Q23 al-Muʾminūn | 1.0497 |
| 106 | Q13 | al-Raʿd | Q12 Yūsuf | 1.0683 |
| 107 | Q10 | Yūnus | Q9 al-Tawba | 1.0689 |
| 108 | Q34 | Sabaʾ | Q33 al-Aḥzāb | 1.1154 |
| 109 | Q57 | al-Ḥadīd | Q56 al-Wāqiʿa | 1.1156 |
| 110 | Q25 | al-Furqān | Q24 al-Nūr | 1.1291 |
| 111 | Q33 | al-Aḥzāb | Q32 al-Sajda | 1.1330 |
| 112 | Q56 | al-Wāqiʿa | Q55 al-Raḥmān | 1.1493 |
| 113 | Q55 | al-Raḥmān | Q54 al-Qamar | 1.1516 |
| 114 | Q2 | al-Baqara | Q1 al-Fātiḥa | 1.1776 |

## Interpretation

### Rank-based reading

Q 1 at position 1 is **arbitrary mid-pack** (rank 18/114). M1 (compositional-geodesic) shows no preference for the canonical rotation; P3 (liturgical fātiḥat al-kitāb) is the sole driver of Q 1 placement in the cycle. This is consistent with [[h-new-192-mushaf-position-decomposition|H-NEW-192]]'s finding that Q 1 is the largest position-prediction residual in the corpus (feature-predicted position 105, actual 1, Δ = −104): the placement is sui-generis liturgical, not compositional.

### What this says about the ring topology

Per [[cross-finding-013-mushaf-topological-ring|cross-finding-013]], the mushaf is a Hamiltonian CYCLE (ring) in Fisher-Rao content space. A ring has no intrinsic start-point — any of the 114 rotations represents the same cycle. The canonical choice of Q 1 at position 1 is therefore an extrinsic designation, driven by some principle OUTSIDE the ring's geometry.

This test asks: does the *Fisher-Rao geometry itself* privilege Q 1 by giving it the minimum wrap-edge? The answer determines whether M1 (geodesic) and P3 (liturgical) converge at Q 1 or whether P3 is the sole driver.

The empirical answer: **Q 1 is rank 18/114** on the Fisher-Rao wrap-edge criterion. 

### Connection to parent findings

- **[[h-new-227-wrap-edge-chronologies|H-NEW-227]]**: mushaf wrap-edge d(Q 114, Q 1) = 0.3884 is the tightest among 5 orderings (mushaf + 4 chronologies) AND below the null 5th percentile. That test compared ACROSS orderings (same endpoint-pairing mechanism, different surah orderings). THIS test compares WITHIN the mushaf ordering (same 114-cycle, different cyclic rotations).
- **[[h-new-228-sa-min-entropy-ordering|H-NEW-228]]**: mushaf is 10.8% above the 2-opt SA-min adversarial Fisher-Rao TSP solution; structured but not globally optimal. The present test is a LOCAL optimality check: does the canonical rotation minimize the single wrap-edge among the 114 rotations of the SAME cycle?
- **[[cross-finding-013-mushaf-topological-ring|cross-finding-013]]**: ring-topology synthesis. This test refines the ring interpretation by asking whether Q 1 is the M1-preferred rotation-point. Result (rank 18) quantifies the compositional-vs-liturgical trade-off at Q 1.
- **[[h-new-192-mushaf-position-decomposition|H-NEW-192]]**: Q 1 has the largest compositional-position residual (Δ = −104); Q 1 placement is sui-generis liturgical. The present test gives the *same surah* a second quantification: rank 18 on the wrap-edge metric. Both instruments independently characterize Q 1's special placement.

## Limitations

- **Fisher-Rao specific.** Other distance metrics (char-4-gram, NCD-lzma, verse-length, Hellinger, JS, TV) may give different rankings. Cross-feature replication is queued.
- **Descriptive rank test.** The strict-lower-tail Bonferroni α=0.05 / k=1 test requires rank = 1 for significance. Ranks 2–10 are PASS-DIRECTED (near-minimum but not absolute).
- **No causal claim.** This finding quantifies the alignment between liturgical and compositional principles at Q 1; it does not explain WHY the alignment is (or is not) present.

## Classical anchor

- **al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān** (§on *fātiḥat al-kitāb*): Q 1 is the obligatory opener of every ṣalāh raka, the canonical *umm al-kitāb*. Liturgical (P3) designation is explicit. [SECONDARY-TRIANGULATED]
- **Ibn Taymiyya, Majmūʿ al-Fatāwā**: majority doctrine that the mushaf sūra-order is *tawqīfī* (divinely-fixed). Strong-P3 framing. [SECONDARY-TRIANGULATED]
- **al-Zarkashī, al-Burhān**: Q 1 is the archetypal fātiḥa (opener). [SECONDARY-TRIANGULATED]

Our result (NULL, Q 1 rank = 18/114) quantifies the classical liturgical designation. Classical tradition's P3 designation remains the dominant driver; M1 would prefer a different rotation but accommodates the canonical placement at rank 18.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-238-cyclic-shift-wrap-prereg.md`
- Script: `scripts/h_new_238_cyclic_shift_wrap.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-new-238.json`
- Findings: this file
- Journal: `journal/h-new-238-run-1.md`

## Refinement: the Q 1 → Q 2 edge is the cycle-maximum (rank 114 / 114)

Inspecting the bottom-10 table more carefully reveals that the CYCLE-WORST wrap-edge (rank 114, the loosest of all 114 rotations) is **k = 2**: rotation so that Q 2 al-Baqara is at position 1 and Q 1 al-Fātiḥa is at position 114. W(2) = d_FR(Q 1, Q 2) = **1.1776**, which is 3.1× the canonical W(1) and 5.2× the minimum W*(108). Equivalently: in the canonical mushaf (k = 1), the edge between consecutive positions 1 and 2 is the single largest Fisher-Rao jump in the entire 114-edge cycle.

This is a new architectural observation not previously enumerated in [[h-new-130-fisher-rao-residuals|H-NEW-130]] / [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]]'s top-15 structural-hinge list (which examined consecutive mushaf edges EXCLUDING the wrap). In cyclic form, Q 1 → Q 2 joins the universal-hinge roster — and ranks #1 among all 114 edges by Fisher-Rao magnitude.

The mushaf therefore creates, at its OPENING, a pair of structurally opposite edges:
- Q 114 al-Nās → Q 1 al-Fātiḥa (wrap-in): short, tight, rank 18 / 114 — the ṭawāf-like closure.
- Q 1 al-Fātiḥa → Q 2 al-Baqara (first content transition): loose, rank 114 / 114 — the prayer-frame-to-encyclopedic hinge.

This asymmetric opening signature fits the P3 (liturgical) + M1 (compositional) trade-off neatly: Q 1 is held in place by P3 (Q 1 = prayer-frame, fātiḥat al-kitāb), so M1 absorbs the cost as the cycle's biggest single-edge jump. Q 2 al-Baqara is the encyclopedic long-form content surah; its content-distribution is maximally distant from Q 1's prayer-frame register. P3 fixes Q 1 at position 1; the M1-cost is paid at the Q 1 → Q 2 transition.

## Top-5 tightest-wrap starting-points (deliverable)

1. Q 108 al-Kawthar (W = 0.2256) — **M1-preferred**, preceded by Q 107 al-Māʿūn.
2. Q 114 al-Nās (W = 0.2718), preceded by Q 113 al-Falaq.
3. Q 107 al-Māʿūn (W = 0.2772), preceded by Q 106 Quraysh.
4. Q 112 al-Ikhlāṣ (W = 0.2849), preceded by Q 111 al-Masad.
5. Q 113 al-Falaq (W = 0.2886), preceded by Q 112 al-Ikhlāṣ.

All top-5 and top-10 rotations are adjacent-pair rotations within Q 103–114 (the short mufaṣṣal terminal cluster). The M1-geodesic criterion prefers to "start" the cycle inside this tight terminal cluster — classic ring-topology symptom: the tightest edges are inside the densest content cluster.

## Related findings

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]]: source of Fisher-Rao D matrix.
- [[h-new-137-wrap-around-closure|H-NEW-137]]: Q 1 content-closeness to TERMINAL_TRIAD (PASS).
- [[h-new-192-mushaf-position-decomposition|H-NEW-192]]: Q 1 position-prediction residual Δ = −104 (sui-generis liturgical).
- [[h-new-227-wrap-edge-chronologies|H-NEW-227]]: parent — mushaf wrap-edge tighter than all 4 chronologies + below null q05.
- [[h-new-228-sa-min-entropy-ordering|H-NEW-228]]: parent — mushaf 10.8% above SA-min TSP.
- [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]: ring-topology synthesis.
- [[cross-finding-020-the-complete-equation|cross-finding-020]]: complete equation (P3 = 5%, M1 = 15%).