---
finding_id: Q071-F-03
title: H-NEW-49.1 prophet-named hypergeometric replication anchored at Q 71
parent_finding: H-NEW-49.1 (prophet-named muqaṭṭaʿāt enrichment)
date_pre_registered: 2026-05-09
seed: 20260509
agent: Q 71 Nūḥ specialist (Waiel Al-Shujaa)
test_type: closed-form hypergeometric (no permutation)
bonferroni_family: Q071-novel-tests-2026-05-09
bonferroni_k: 5
alpha_bon: 0.01
direction_locked: 8 prophet-named ⊃ 6 muq + 2 non-muq, hypergeometric P(X≥6) ≤ alpha_bon
acceptance_window: P_hypergeom ≤ alpha_bon = 0.01 AND Q 71 verified in non-muq cell
mw5_positive_control: Q 12 Yūsuf — prophet-named-muq with 25/1777 hits (already established)
mw7_internal_check: re-verify the conservative-8 prophet-named list against Tanzil + Buckwalter
---

# Q071-F-03 — Prophet-named hypergeometric (H-NEW-49.1 replication anchored at Q 71)

## 1. Hypothesis

The 8 conservative-prophet-named surahs (Q 10 Yūnus, Q 11 Hūd, Q 12 Yūsuf,
Q 14 Ibrāhīm, Q 19 Maryam, Q 31 Luqmān, Q 47 Muḥammad, Q 71 Nūḥ) are enriched
in muqaṭṭaʿāt openings (6 of 8 = 75%) at hypergeometric significance under the
parent H-NEW-49.1 framework. Q 71 is verified as one of the 2 non-muq members
(alongside Q 47 Muḥammad).

## 2. Pre-committed direction

P(X ≥ 6 | n=8 draws, K=29 muq surahs, N=114 total) ≤ α_bon. Direction = enrichment
(more muq among prophet-named than expected by uniform sampling).

Q 71's specific cell-membership: NON-MUQ + PROPHET-NAMED.

## 3. Method

- **Population**: N = 114 canonical Hafs-Kūfan surahs.
- **K = 29 muqaṭṭaʿāt-opener surahs** = {Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19,
  20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}.
- **n = 8 conservative-prophet-named** = {Q 10, 11, 12, 14, 19, 31, 47, 71}.
- **k_obs = 6** muq-prophet-named = {Q 10, 11, 12, 14, 19, 31}.
- **Test statistic**: P(X ≥ 6 | hypergeom(N=114, K=29, n=8)).

## 4. Acceptance window

- p_hypergeom ≤ α_bon = 0.01 → **PASS-DIRECTED**.
- p_hypergeom ≤ 0.05 only → **DIRECTIONAL** (replicates parent without surviving
  this surah's stricter Bonferroni-5 cutoff).
- p_hypergeom > 0.05 → **NULL** (would refute the parent finding; expected p ≈ 0.0033).

Q 71 must verify as non-muq + prophet-named to satisfy the cell-membership check.

## 5. Garden-of-forking-paths

- The conservative-8 list is locked at H-NEW-49.1 publication. The alternative
  PROPHET_PERSON-11 taxonomy (which adds Q 3 Āl ʿImrān, Q 21 al-Anbiyāʾ, Q 34
  Sabaʾ) yields P(X ≥ 7 | n=11) = 0.00563 (also PASS at α=0.05 single-test). We
  honor the conservative-8 framing for this surah-specific replication.
- Q 71 is unambiguously PROPHET_PERSON (named after Nūḥ); ALSO unambiguously NON-MUQ
  (opens with "إنا أرسلنا" not a muq-letter sequence). Cell membership is locked.

## 6. Independent-replication notes

This test is a replication-in-context of H-NEW-49.1. An independent replication
on a distinct dimension is not requested by this pre-reg.

## 7. Honest disclosure

- The 6/8 = 75% pattern survives extreme Bonferroni (15-test correction yields
  p_corrected ≈ 0.05 still — see H-NEW-49.1 result file). No re-doing of the
  parent test; this is verification of Q 71's location within the established cell.
- Q 71's NON-MUQ status is a STRUCTURAL FEATURE — short late-Meccan surah in the
  muqaṭṭaʿāt-free zone Q 69-114. The 2 non-muq prophet-named (Q 47 Muḥammad +
  Q 71 Nūḥ) are TYPOLOGICALLY DISTINCT from the 6 muq-prophet-named:
  - Q 47 = Medinan, command/legal
  - Q 71 = late Middle Meccan, dedicated single-prophet petition-narrative

  Both are SHORT relative to the muq-prophet-named cohort (mean length: muq = ~118v,
  non-muq = ~52v). This length-asymmetry is a known correlate (H-NEW-46/46.1).

## 8. Cross-references

- [[h-new-49-1-prophet-enrichment|H-NEW-49.1]] — parent finding, p=0.0033.
- [[h-new-49-surah-name-class|H-NEW-49]] — class taxonomy.
- [[h-new-86-surah-name-as-key-root|H-NEW-86]] — Q 71 in PROPHET_PERSON 11-list.
- [[Q047-muhammad/00-overview|Q 47 Muḥammad]] — the OTHER non-muq prophet-named surah.
- 06-novel-findings.md Q071-F-03 — result.
