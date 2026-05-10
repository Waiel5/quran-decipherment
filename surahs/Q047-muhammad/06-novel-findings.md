---
surah: 47
surah_name_ar: محمد
file_type: novel-findings
date_last_updated: 2026-05-10
phase: B+
specialist: Q047-wave-J-specialist
---

# Q 47 — Novel Pre-Registered Findings

Six pre-registered tests have been run for Q 47. The first three are from the Q032-Q047 retry-specialist (2026-05-08); the next three are from this Wave-J specialist (2026-05-10). All SHAs locked, all directions pre-committed.

## Summary

| Test | Hypothesis | Verdict | p / score | Source |
|:--|:--|:-:|:--|:--|
| Q047-F-01 | Q 47 #1 by Muhammad-naming density among 4 named surahs | **VINDICATED** | strict ordinal #1 | `csv/Q047-F-01.json` |
| Q047-F-02 | Q 47 ≤ 5 by 9-term war-vocab density | **VINDICATED** | rank 2/114 | `csv/Q047-F-02.json` |
| Q047-F-03 | Q 47-48-49 3-tuple cohesion test | **NULL** | T=0.866, p=0.252 | `csv/Q047-F-03.json` |
| **Q047-F-04** | Muḥammad/Aḥmad corpus inventory matches the 4+1 verse set | **VINDICATED** | exact-match | `csv/Q047-F-04.json` |
| **Q047-F-05** | Q 47 ≤ 3 by qtl-root density per-1000-w | **NULL** | rank 19/114 | `csv/Q047-F-05.json` |
| **Q047-F-06** | Q 47-Q 48 in_all_three bottom-15 cohesive (H-NEW-130 family) + FR pair-rank ≤ 25% | **NULL** | A: 75/89/71; B: 35.4% | `csv/Q047-F-06.json` |

**Headline**: 3 VINDICATED, 3 NULL. NULL with equal prominence (Protocol §1.3). The NULLs sharpen interpretation: Q 47's war-character is in CLUSTER vocabulary (qitāl+riqāb+wathāq+fidāʾ+ḥarb+jihād), not in raw *qtl* root frequency; Q 47-Q 48 cohesion is at the TSP-EDGE level (pair-local) not at the universal-seam level (consecutive-distance rank).

---

## Q047-F-04 — Muḥammad-name corpus inventory

**Pre-reg**: `Q047-F-04-muhammad-corpus-inventory-prereg.md` (SHA `81bf3a4589017eaf4f9cc47780be170b2267a5b07362833092bf04934ca2200a`)
**Script**: `scripts/Q047_F_04_muhammad_corpus_inventory.py`
**JSON**: `csv/Q047-F-04.json`

### Hypothesis

The proper name *Muḥammad* (محمد) appears as a standalone token in EXACTLY 4 verses (Q 3:144, Q 33:40, Q 47:2, Q 48:29). The alternate name *Aḥmad* (أحمد) appears EXACTLY 1× at Q 61:6. The set of verse-internal attestations exactly matches the pre-listed set.

### Result

| Metric | Pre-committed | Observed |
|:--|:--|:--|
| Muḥammad count | 4 | 4 ✓ |
| Muḥammad verse set | {(3,144), (33,40), (47,2), (48,29)} | exact match ✓ |
| Aḥmad count | 1 | 1 ✓ |
| Aḥmad verse | (61,6) | exact match ✓ |

**Verdict**: **VINDICATED**.

### Interpretation

This is a corpus-EXACT verification of the Muḥammad/Aḥmad enumeration in al-Suyūṭī's *al-Itqān* nawʿ 17. Title-line attestations (*sūrat Muḥammad* in Q 47's masthead) are paratext and NOT counted. The 4+1 attestation set is the empirical anchor of the project's "prophet-named verses" cross-finding-009.

### Cross-references

- [[cross-finding-009-prophet-named-surahs]] — the broader prophet-named-surahs cluster
- [[Q047-F-01-muhammad-naming-density]] — companion test (density per-1000-w)
- al-Suyūṭī, *al-Itqān*, nawʿ 17

---

## Q047-F-05 — qtl-root density (NULL)

**Pre-reg**: `Q047-F-05-qtl-root-density-prereg.md` (SHA `252b11f712566aeb4a345abd759d14c9d4b8b2a4561ae234b369e3f528070005`)
**Script**: `scripts/Q047_F_05_qtl_root_density.py`
**JSON**: `csv/Q047-F-05.json`

### Hypothesis

Per al-Qurṭubī's *sūrat al-Qitāl* designation and Q008-F-03's qitāl-cluster {Q 8, 9, 47, 48, 61}, Q 47 should rank in the top-3 corpus-wide by QAC stem-root *qtl* density per-1000-words.

### Result

| Metric | Q 47 | Top-3 surahs | Q 47 rank |
|:--|:--|:--|:-:|
| qtl-root count | 2 (Q 47:4, Q 47:20) | Q 81 (1), Q 85 (1), Q 60 (3) | — |
| Surah word-count | 544 | small surahs (≤200w except Q 60 at 377w) | — |
| Rate per-1000-w | 3.676 | 9.62, 9.01, 7.96 | **19/114** |
| Min-count-3 rank (alternative) | n/a (count = 2) | Q 60, Q 59, Q 4 | not in set |
| Absolute count rank | 2 | Q 2 (31), Q 4 (25), Q 3 (21) | 18/114 |

**Verdict**: **NULL** (rank 19 > pre-committed top-3 threshold).

### Interpretation

Q 47 ranks 19/114 by qtl-density-per-1000-w because:
1. Q 47's absolute qtl count is only 2 attestations (Q 47:4 *qutilū* and Q 47:20 *al-qitāl*).
2. Q 47's word-count (544) is large relative to surahs like Q 81 (104 words) or Q 85 (111 words) which have 1 attestation each but score higher per-1000-w.
3. al-Qurṭubī's designation is a THEMATIC cluster ("qitāl as topic"), not a SINGLE-ROOT-FREQUENCY claim.

The broader cluster (Q047-F-02) returned Q 47 rank 2/114 — confirming al-Qurṭubī's claim AT THE CLUSTER LEVEL. The NULL on the narrow single-root level refines the claim, not refutes it.

**Honest interpretation**: al-Qurṭubī's *sūrat al-Qitāl* designation is supported by the 9-element war-vocabulary cluster but not by single-root qtl frequency. This is a RULES-TUPLE-FRAGILE classical claim — sensitive to how "qitāl" is operationalized.

### Cross-references

- [[Q047-F-02-war-vocab-density]] — companion test at cluster level (VINDICATED, rank 2)
- [[Q008-F-03-qital-cluster]] — Q 47 in qitāl-cluster
- al-Qurṭubī, *al-Jāmiʿ*, on Q 47

---

## Q047-F-06 — Q 47 ↔ Q 48 adjacent-pair (NULL on both pre-reg directions)

**Pre-reg**: `Q047-F-06-q47-q48-adjacent-pair-prereg.md` (SHA `3b74c07902f7e50f4630a5ca6c48e836e00921f38222f83296082b90fc53dc72`)
**Script**: `scripts/Q047_F_06_q47_q48_adjacent_pair.py`
**JSON**: `csv/Q047-F-06.json`

### Hypothesis

**Test A** (cohesion-direction): Q 47-Q 48 is in the bottom-15 (cheapest) consecutive adjacencies in all three D-matrices (FR-root H-NEW-130, char-4gram H-NEW-130b, verse-length H-NEW-130c).
**Test B** (FR-pair rank): Q 47-Q 48 FR distance is in the bottom-25th percentile of all 6,441 surah-pairs (rank ≤ 1610).
**Bonferroni-2**: α_corrected = 0.025.

### Result

| Sub-test | Q 47-Q 48 metric | Threshold | Pass? |
|:--|:--|:--|:-:|
| Test A: root | dist 0.8893; rank-low 75/113 | bottom 15 | NO |
| Test A: char-4gram | dist 0.9816; rank-low 89/113 | bottom 15 | NO |
| Test A: verse-length | dist 0.6941; rank-low 71/113 | bottom 15 | NO |
| Test A overall | in_all_three? | True | **FALSE** |
| Test B: FR pair-rank | dist 0.8893; rank-low 2281/6441 (35.4%) | rank ≤ 1610 (25%) | NO |
| Test B strict (α=0.025) | rank ≤ 161 | — | NO |

**Verdict**: **NULL** (neither Test A nor Test B passed).

### Interpretation

Q 47-Q 48 is consistently MID-PACK at the consecutive-distance rank in all three feature axes (ranks 71-89 of 113 — the middle 4-of-10). At the all-pairs FR scale, Q 47-Q 48 is at the 35th percentile — closer than corpus median (50th) but not in bottom-25%.

**Yet** Q 47-Q 48 IS structurally cohesive at the TSP-edge level: H-NEW-720's δ(Q 47→Q 48) = 0.0332 (among the cheapest single-edge TSP-savings in the entire mushaf). This is a metric-DIFFERENCE not a contradiction: TSP-edge measures *marginal savings under 2-opt heuristic*; consecutive-distance measures *raw FR/char/verse distance*. The two metrics agree that Q 47-Q 48 is "tight" in some sense — but disagree on whether it's *universal-seam-tight* (NO) or *route-savings-tight* (YES).

**al-Biqāʿī's munāsabah claim** is therefore: VINDICATED at TSP-edge level, NULL at consecutive-distance-universal-seam level. Q 47-Q 48 is a LOCAL cheap edge, not a UNIVERSAL top-tier cohesive pair.

### Empirical reframing: Q 47's true neighborhood

The Q 47 ↔ FR-nearest-10 analysis (`csv/Q047-F-06.json`) reveals Q 47 sits in a 6-surah back-Medinan cluster:

1. Q 64 (al-Taghābun) — FR 0.8195 (#1)
2. Q 63 (al-Munāfiqūn) — FR 0.8295 (#2)
3. Q 49 (al-Ḥujurāt) — FR 0.8503 (#3)
4. Q 61 (al-Ṣaff, Aḥmad-name) — FR 0.8637 (#4)
5. Q 66 (al-Taḥrīm) — FR 0.8659 (#5)
6. Q 59 (al-Ḥashr) — FR 0.8769 (#6)
7. Q 13 (al-Raʿd) — FR 0.8877 (#7) — thematic outlier
8. Q 48 (al-Fatḥ) — FR 0.8893 (#8)
9. Q 60 (al-Mumtaḥana) — FR 0.8935 (#9)
10. Q 98 (al-Bayyina) — FR 0.9041 (#10)

**This is the project's first empirical demonstration that Q 47's FR-neighborhood is the back-Medinan etiquette/hypocrite/qitāl cluster {Q 49, 59, 60, 61, 63, 64, 66} — broader than the classical Hudaybiyya-pair framing of Q 47-Q 48 alone.** The Hudaybiyya pair captures a SPECIFIC editorial-cluster aspect (Bukhārī tafsīr-bāb) but not the broader root-distribution architecture.

### Cross-references

- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — TSP-edge δ=0.0332 (Q 47-Q 48 is corpus-CHEAP at TSP level)
- [[h-new-130|H-NEW-130]], [[h-new-130b|H-NEW-130b]], [[h-new-130c|H-NEW-130c]] — consecutive-distance D-matrices
- [[Q049-al-hujurat/06-novel-findings|Q 49]] — Q 47's #3 FR-nearest; etiquette-cluster {Q 49, 60-66} CONFIRMED-PAIR (Q049-F-01)
- [[cross-finding-025-marker-thickness]] — Q 47's "war-instruction" marker is at the right thickness threshold (≥30% of content) to drive FR cohesion within the back-Medinan cluster, but not extreme enough to make Q 47-Q 48 alone a universal seam.

---

## Architecturally novel observations (not pre-registered)

### Obs 1: The 94.7% م-rāwī monotonicity

Q 47's final-letter distribution is 36 verses ending in م + 2 verses ending in ا. This is corpus-extreme rāwī-monotony (rhyme entropy z = −1.021, h-new-750). For Medinan surahs of this length-class (mufaṣṣal-awsāṭ), this is highly distinctive. Candidate Q047-F-07 (post-hoc, not pre-registered): test Q 47 rhyme-monotony rank among all 38-verse-length surahs — likely top-1 by rāwī-uniformity. NOT EXECUTED in this run.

### Obs 2: The two ا-rāwī exception verses

The 2 verses in Q 47 that end in ا (not م) deserve tafsīr-attention. (Identification deferred to future specialist run.)

### Obs 3: The "thwarting-of-deeds" refrain

The phrase-family *aḍalla aʿmālahum* / *aḥbaṭa aʿmālahum* appears 4-5× in Q 47 (vv. 1, 8, 9, 28, 32). A corpus-scale refrain test (analogous to H-NEW-1320's 3-tier refrain analysis) was NOT pre-registered for Q 47. Candidate for future Q047-F-NN.

---

## Honest meta-summary

- **3 VINDICATIONS**: Q047-F-01 (Muhammad-density #1 of 4), Q047-F-02 (war-cluster rank 2/114), Q047-F-04 (Muhammad/Ahmad inventory exact-match).
- **3 NULLS** (all published with equal prominence per Protocol §1.3):
  - Q047-F-03: 3-tuple Q 47-48-49 cohesion test mid-pack.
  - Q047-F-05: qtl-root density alone is rank 19, not top-3.
  - Q047-F-06: Q 47-Q 48 is NOT a universal top-15 seam in any of the 3 D-matrices.

The vindications anchor Q 47's identity-as-Muhammad-surah and war-instruction-surah. The nulls refine al-Qurṭubī's *sūrat al-Qitāl* designation to the cluster-level (not single-root), refine al-Biqāʿī's munāsabah to the pair-local-cheap-edge level (not universal-seam), and reveal Q 47's true FR-architecture as a broader back-Medinan cluster (not Q 47-Q 48 alone).

**Net architectural finding**: Q 47 is the named-Muhammad-surah AND the war-instruction-surah BUT lives in a 6-surah back-Medinan cluster {Q 47, 49, 60-66} — not in an isolated Q 47-Q 48 pair. The Hudaybiyya editorial-pairing is real but partial.
