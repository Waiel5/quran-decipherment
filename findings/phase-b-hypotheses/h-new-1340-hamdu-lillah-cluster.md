---
id: H-NEW-1340
title: al-ḥamdu li-llāh opener 5-cluster Fisher-Rao cohesion
date_locked: 2026-05-09
date_run: 2026-05-09
verdict: NULL (both cells; PC passed)
seed: 20260509
n_perm: 10000
prereg_sha: 9f5b5e9427e02c0ba6b7be5742071d3ecb1bd8375b1e646604b2bdfd6d6fa788
---

# H-NEW-1340 — al-ḥamdu li-llāh opener cluster Fisher-Rao cohesion

## Verdict: NULL — answers OQ-3 candidate as NEGATIVE

The 5 surahs opening *al-ḥamdu li-llāh* {Q 1, 6, 18, 34, 35} do NOT form a Fisher-Rao cohesive cluster on root-distribution.

| Cell | Result | p | Pass |
|:--|--:|--:|:-:|
| A — uniform null | obs 0.9902 vs null mean ~0.92 | 0.7485 | NO |
| B — length-matched | obs 0.9902 vs null p5 ~0.85 | 0.4975 | NO |
| MW-5 PC (H-NEW-1190 5-of-10) | passed at 0.021 ✓ | 0.0210 | YES |

The cluster is actually MORE typical than 75% of random 5-surah samples. Cluster verse-counts span Q 1 (7v) to Q 6 (165v) — too heterogeneous for length-matched control to rescue.

## Implication for OQ-3

OQ-3 (HANDOFF/05-OPEN-QUESTIONS): "Are there other introduction-marker classes besides muqaṭṭāʿat? *al-ḥamdu li-llāh* openers are a candidate." 

**Answer: NEGATIVE on this candidate.** The al-ḥamdu li-llāh opener does NOT function as a second introduction-marker-class on root-distribution Fisher-Rao. This is consistent with cross-finding-025 marker-thickness: a single phrase + 1-verse co-locator is too thin to drive surah-aggregate FR cohesion. The muqaṭṭāʿat remains corpus-uniquely the multi-axis-correlation marker class.

Other introduction-marker candidates for OQ-3 still pending: (a) the 5 *qul*-opener surahs {Q 72, 109, 112, 113, 114} (H-NEW-74 confirmed cohesive at FR level — already a 2nd-class candidate); (b) the 5 idhā-cosmic-opener surahs (H-NEW-1200 sub-A confirmed); (c) the *yā ayyuhā al-nabī* vocative cluster (untested).

## Connection to existing findings

- **Cross-finding-008** muqaṭṭāʿat (p≤10⁻¹²): the muqaṭṭāʿat retains its uniqueness as a multi-axis-correlation marker class. al-ḥamdu li-llāh has only 1 surface-axis (the opener phrase) and inherits no other shared structural axes that would force root-distribution similarity.
- **Cross-finding-025** marker-thickness: ANOTHER NULL on a thin marker — adds a 4th NULL data point (with H-NEW-1301 IMPV-qrA, H-NEW-1310 Christ-narrative, H-NEW-1330 sajda) supporting the "thin markers don't cohere on root-FR" rule.
- **Cross-finding-012** Late-Meccan apparatus: 4 of 5 cluster members are Late Meccan; if the apparatus drove surah cohesion, expect cohesion. NULL here suggests scripture-announcement is a phase-co-located feature, not a per-surah latent driver — same conclusion as H-NEW-141.
- **Q 1 al-Fātiḥa** is sui-generis (cluster-isolated per H-NEW-89); inclusion of Q 1 may pull the cluster mean upward (Q 1's mean-FR to corpus is ~1.0). Replication excluding Q 1 (4-surah cluster {6, 18, 34, 35}) is queued as H-NEW-1341.

## Honest limits

- **PC PASS at 0.021** confirms instrument validity. Substantive NULL.
- Q 1 inclusion may bias upward; H-NEW-1341 follow-up could test 4-of-4 without Q 1.
- Other feature spaces (rhyme, char-4-gram) untested.
- Single planned test, single-test α=0.05.

## Verdict

**NULL — al-ḥamdu li-llāh opener is NOT a 2nd introduction-marker class on root-distribution FR. cross-finding-025 marker-thickness rule reinforced.**
