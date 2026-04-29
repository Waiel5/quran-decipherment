---
finding_id: h-new-224
title: Hybrid mushaf+Nöldeke orderings — which half carries the mushaf's Fisher-Rao advantage?
parent: h-new-111 (Fisher-Rao mushaf-order geodesic), h-new-212 (alt-chronology)
status: PRE-REG
date: 2026-04-17
seed: 20260419
bonferroni_k: 1
alpha_bon: 0.05
framing: DESCRIPTIVE (exploratory decomposition; no formal family test)
---

# [[h-new-224-hybrid-orderings|H-NEW-224]] — Hybrid orderings: mix mushaf + Nöldeke halves

## Motivation

[[h-new-111-fisher-rao-mushaf|H-NEW-111]] established that the mushaf's 114-surah ordering has a Fisher-Rao
path-length (L_mushaf = 85.76) that is ~11.46 null-SDs shorter than random,
and 1.47 units shorter than Nöldeke's chronology (L_nold = 87.23). Neither
ordering is optimal (TSP approx = 77.47). The question: **does mushaf beat
Nöldeke EVERYWHERE, or does the advantage come from one half?**

If mushaf's advantage is concentrated in the FRONT (positions 1–57,
containing the ṭiwāl long surahs + most muqaṭṭaʿāt surahs), then the
"design" signal is in the opening-to-middle arc. If the advantage comes
from the BACK (positions 58–114, the mufaṣṣal + short-surah bracket),
the signal is in the closing arc. If neither — if both halves contribute
equally — then the advantage is a global property.

## Method

Compute four hybrid orderings (each still visits all 114 surahs exactly once):

- **A** = mushaf[0:57] + Nöldeke[0:57]\_with\_mushaf-front-removed
- **B** = Nöldeke[0:57] + mushaf[0:57]\_with\_Nöldeke-front-removed
- **C** = mushaf[0:28] + Nöldeke[0:86]\_with\_mushaf-front-28-removed
- **D** = Nöldeke[0:86] + mushaf[0:28]\_with\_Nöldeke-front-86-removed

"Remove" means: if a surah already appeared in the prefix, skip it when
taking the suffix from the other ordering. So the result is always a
permutation of {1..114}.

For each hybrid H ∈ {A, B, C, D}:
- Compute L_H = Fisher-Rao path length (same D matrix as [[h-new-111-fisher-rao-mushaf|H-NEW-111]]/212).
- Compare to L_mushaf = 85.76 and L_nold = 87.23.
- Compute p_one-sided-lower vs same 10 000-perm null (seed 20260419).

## Pre-registered primary descriptive question

Where does the mushaf's advantage live?

- **Criterion-FRONT**: If L_A < L_B AND L_C < L_D, then the mushaf FRONT
  drives the advantage — i.e. keeping mushaf's opening arc (whether 57
  or 28 surahs) produces shorter paths than keeping Nöldeke's opening.
- **Criterion-BACK**: If L_B < L_A AND L_D < L_C, then the mushaf BACK
  drives the advantage.
- **Criterion-MIXED**: neither criterion holds cleanly.

This is DESCRIPTIVE (k=1, α=0.05 Bonferroni trivial). No formal PASS/FAIL —
we report direction + magnitude.

## Secondary descriptive

- How close do hybrids get to mushaf (85.76) or Nöldeke (87.23)?
- Do any hybrids BEAT mushaf? (Not expected; if yes, surprising.)
- z-scores vs null for each hybrid.

## Inherited assumptions

- D matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (SHA-256 pinned in script).
- Rules-tuple: (no-tashkeel, QAC-STEM root tokens, QAC v0.4,
  basmala-counted-only-in-surah-1, Hafs-Kūfan).
- Null: 10 000 uniform permutations, seed 20260419 (matches [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]).
- Nöldeke ordering from `data/revelation-order.csv` sorted by `noldeke_order`.

## Garden of forking paths

- Split points 57/57, 28/86 pre-specified. No other splits tested.
- Tie-break: when walking the suffix from the "other" ordering, skip any
  surah already in the prefix (stable order within the donor ordering).
- Both front-loadings (A, C) vs back-loadings (B, D) are tested symmetrically.

## Files

- Pre-reg: this file.
- Script: `scripts/h_new_224_hybrid_orderings.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-224.json`
- Finding: `findings/phase-b-hypotheses/h-new-224-hybrid-orderings.md`
