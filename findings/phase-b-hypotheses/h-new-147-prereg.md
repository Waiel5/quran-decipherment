---
finding_id: h-new-145
title: "T-L.4 Bukhārī cross-corpus Fisher-Rao near-optimality test"
specialist: specialist-a
date_prereg: 2026-04-17
seed: 20260420
bonferroni_k: 2
bonferroni_family: h-new-145-bukhari-cross-corpus
alpha_bon: 0.025
alpha_raw: 0.05
direction_primary: "Bukhārī's canonical bab-ordering Fisher-Rao PATH ratio L_bukhari / L_2opt_bukhari is LARGER than Quran's mushaf-ordering ratio 1.107. Testing: is the Quran's near-optimality CORPUS-SPECIFIC, or does any coherent Arabic religious corpus show it? If Bukhārī's ratio ≈ 1.1, the Quranic finding is NOT exceptional. If Bukhārī's ratio is much larger (e.g., > 1.5), the Quranic finding IS exceptional."
direction_secondary_perm: "Bukhārī's bab-ordering Fisher-Rao path is SHORTER than random permutation of its 114 longest bab-segments, at one-sided lower-tail p < 0.025."
K_top_roots: 500
dirichlet_alpha: 0.5
rules_tuple: "(Bukhārī 114-longest-bab-segments, QAC-STEM roots via light-stemming, basmala excluded, bab-canonical order, Fisher-Rao arccos-Bhattacharyya)"
verdict_ceiling: "PASS-DIRECTED (novel cross-corpus test)"
parent_claim: "cross-finding-011's mushaf-FR-near-optimality is Quran-specific"
---

# [[h-new-145-muq-code-decoding|H-NEW-145]] — Bukhārī cross-corpus Fisher-Rao near-optimality test

## Motivation

[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] established that the Quran's mushaf-ordering is
Fisher-Rao-near-optimal (L/L_2opt = 1.107) and that this is not a
length-sort artifact. [[cross-finding-013-mushaf-topological-ring|Cross-finding-013]] extended to the cyclic ring
claim.

These findings are strong WITHIN the Quran, but the question remains:
**is this corpus-specific**, or does ANY coherent Arabic religious
corpus of 114 chapter-equivalent segments show Fisher-Rao-near-optimality
under its canonical ordering?

To address, we test the SAME methodology on Ṣaḥīḥ al-Bukhārī — the
largest and most-authoritative classical hadith collection, totaling
526K tokens and segmented into ~4,080 bab-chapters under al-Bukhārī's
9th-century editorial arrangement.

The null hypothesis (corpus-specificity of the Quranic finding) would
be CONFIRMED if Bukhārī's bab-ordering is MUCH LESS near-optimal than
the Quran's mushaf-ordering. The alternative (any well-ordered Arabic
religious text is near-optimal) would be CONFIRMED if Bukhārī's ratio
is near 1.1.

## Hypothesis

**Primary (H1)**. Bukhārī's ratio L_bukhari_path / L_2opt_bukhari is
SIGNIFICANTLY DIFFERENT from Quran's 1.107. Specifically:
- If ratio > 1.5 → Bukhārī's ordering is NOT near-optimal → Quranic
  finding is CORPUS-SPECIFIC (supports the exceptionality claim).
- If ratio < 1.2 → Bukhārī is ALSO near-optimal → Quranic finding is
  GENRE-GENERAL (weakens the exceptionality claim).
- If 1.2 ≤ ratio ≤ 1.5 → Bukhārī is STRUCTURED but not optimal →
  intermediate interpretation.

Direction locked: **we expect Bukhārī's ratio > 1.3** (i.e., LESS
near-optimal than Quran), based on the theory that legal-topical
ordering (Bukhārī) is DIFFERENT from content-geodesic ordering
(Quran).

**Secondary (H2)**. Bukhārī's bab-ordering Fisher-Rao path length
is SIGNIFICANTLY SHORTER than random permutation of the same 114
segments. Tests whether any "meaningful" ordering outperforms random,
even if it's not near-TSP-optimal.

## Method

### Data

- Bukhārī corpus: `data/baseline-corpora/raw/bukhari-noquran.txt`
  (4,079 bab-markers, 522K tokens excluding Quran-quotations).
- **Bab-segmentation**: split on the literal string "باب" (bab).
  This is a crude approximation — bab is a common word in Arabic
  and some splits may be spurious. Honest caveat: 4,080 segments
  may over-count; the largest 114 are used to ensure meaningful
  segments (each ≥ 475 tokens).
- **Segment selection**: take the 114 LONGEST bab-segments (by
  whitespace-token count). Matches Quran's 114-surah count; avoids
  trivially-short "باب" embeddings.
- Tokenization: whitespace-split (same as Quran corpus).
- Root extraction: **NO QAC morphology available for Bukhārī** (QAC
  is Quran-specific). Substitute: **light-stemmer** on Bukhārī tokens.
  Use same light-stemming method that would approximate QAC-STEM roots
  for Arabic text. Disclose this methodological asymmetry in the
  findings file.
- Top-K roots: K = 500 (same as parent).
- Dirichlet α = 0.5.

### Light-stemming disclosure (critical caveat)

QAC provides ANNOTATED roots for the Quran. For Bukhārī, no such
annotation exists. We use a **rule-based light-stemmer** (strip common
prefixes ل, و, ب, ال; strip common suffixes ون, ين, ة, ها, هم). This
is an APPROXIMATION and will have higher noise than QAC-STEM.

**This is a known methodological asymmetry.** It may INFLATE
Bukhārī's L ratio (noisier roots → less coherent distribution →
further from optimum). The finding direction (Bukhārī > Quran)
would be consistent with this asymmetry being a confound.

**Mitigation**: apply the SAME light-stemmer to the Quran corpus as
a positive control. Report Quran's ratio under light-stemming
alongside Quran's QAC-STEM ratio from [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]. If light-
stemming inflates Quran's ratio SIGNIFICANTLY vs QAC, the Bukhārī-
Quran comparison must be made using both corpora under light-
stemming (apples-to-apples).

### Procedure

1. Segment Bukhārī at "باب" markers; take top-114 longest segments.
2. Light-stem tokens in each segment.
3. Build per-segment root-distribution (top-500 global Bukhārī roots,
   Dirichlet-0.5 smoothing, L1-normalized).
4. Compute Fisher-Rao D-matrix (arccos-Bhattacharyya) on 114 Bukhārī
   segments.
5. L_bukhari_path = sum of consecutive distances in bab-canonical order.
6. L_2opt_bukhari = 2-opt minimum path (100-iteration patience, 10
   random restarts, seed 20260420+k).
7. R_bukhari = L_bukhari_path / L_2opt_bukhari.
8. Permutation null: 10K random permutations of 114 segments; compare
   L_bukhari to null.
9. Apply SAME light-stemmer to Quran corpus; recompute Quran ratio
   R_quran_lightstem. Compare R_bukhari to R_quran_lightstem (apples-
   to-apples), not to [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s R_quran_qac = 1.107.

### MW-5

Sanity check: apply light-stemmer to Quran; compare R_quran_lightstem
to [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s R_quran_qac = 1.107. If R_quran_lightstem
differs by > 0.15 (i.e., if light-stemming inflates ratio by > 15%),
the methodology has a major confound and the Bukhārī comparison is
not cleanly interpretable.

If MW-5 passes, proceed with primary test.

## Pre-committed acceptance windows

- **PRIMARY CORPUS-SPECIFIC PASS**: R_bukhari > 1.3 AND R_bukhari −
  R_quran_lightstem > 0.15. Quranic finding confirmed as exceptional.
- **PRIMARY GENRE-GENERAL PASS**: R_bukhari < 1.2 AND R_bukhari −
  R_quran_lightstem < 0.05. Quranic finding generalizes; less exceptional.
- **INTERMEDIATE**: R_bukhari in [1.2, 1.3]; or small difference from
  Quran. Report as "qualitative-not-exceptional".
- **SECONDARY**: L_bukhari < random-permutation L at p < 0.025.
- **FAIL MW-5**: light-stemmer inflates Quran ratio by > 15%; test
  inadmissible.

## Honest limits (pre-specified)

1. **Bab-segmentation by literal string** is crude. A proper Bukhārī
   edition separates chapter-headings structurally; my text does not.
2. **114-longest** may bias toward certain thematic areas (the longest
   bab tend to be legal-prescriptive chapters).
3. **Light-stemming** introduces noise that QAC does not. Mitigation
   via apples-to-apples MW-5 is necessary.
4. **"Bukhārī canonical order"** is al-Bukhārī's editorial arrangement,
   not a "revealed" order. Comparison to mushaf is imperfect.
5. **Even if Bukhārī ratio > 1.3, the interpretation is constrained**:
   this says Bukhārī's bab-ordering is LESS near-optimal than Quran
   under this specific method. It does NOT prove the Quran is uniquely
   ordered (only that Bukhārī doesn't match this particular axis).

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_145_bukhari_cross_corpus.py`.
3. JSON `findings/phase-b-hypotheses/csv/h-new-145.json`.
4. Findings file.
5. Journal.
