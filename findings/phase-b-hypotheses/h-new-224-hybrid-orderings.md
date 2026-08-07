---
finding_id: h-new-224
title: Hybrid mushaf+Nöldeke orderings — mushaf's Fisher-Rao advantage is BACK-driven
parent: h-new-111, h-new-212
status: PASS-DESCRIPTIVE (surprising)
date: 2026-04-17
seed: 20260419
bonferroni_k: 1
alpha_bon: 0.05
pre_reg_sha256: 3389a9b47e4eab0a96b86bdadcbd6109b963d4148acd09588ebf6eff1a42e05e
---

# [[h-new-224-hybrid-orderings|H-NEW-224]] — Hybrid orderings: which half carries mushaf's Fisher-Rao advantage?

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

## Headline

The mushaf's Fisher-Rao path-length advantage over Nöldeke lives almost
entirely in the **BACK** (mufaṣṣal + short-surah bracket), NOT in the
front (ṭiwāl + muqaṭṭaʿāt blocks). In fact, **a hybrid that splices
Nöldeke's first 86 surahs onto the mushaf's last 28 (hybrid D) is
SHORTER than pure mushaf** (L_D = 85.09 vs L_mushaf = 85.76, Δ = −0.67,
−0.41 null-SDs). The front half of mushaf is not "design-shaped" for
Fisher-Rao coherence; the back half is.

## Numbers

| Ordering | L | z vs null | p (1-sided lower) | vs mushaf (null-SDs) |
|---|---|---|---|---|
| **Hybrid D** (Nöldeke[0:86] + mushaf tail) | **85.0898** | −11.834 | 0.0001 | **−0.411** |
| Mushaf (reference) | 85.7597 | −11.423 | 0.0001 |  0.000 |
| Hybrid B (Nöldeke[0:57] + mushaf tail) | 86.1132 | −11.205 | 0.0001 | +0.217 |
| Hybrid C (mushaf[0:28] + Nöldeke tail) | 86.9646 | −10.682 | 0.0001 | +0.740 |
| Nöldeke (reference) | 87.2321 | −10.518 | 0.0001 | +0.905 |
| Hybrid A (mushaf[0:57] + Nöldeke tail) | 87.5290 | −10.335 | 0.0001 | +1.088 |

Null (10 000 perms, seed 20260419): mean = 104.35, SD = 1.63. All six
orderings clear p < 10⁻⁴ one-sided vs random — **every hybrid is still
non-random**, but their ranking reveals the decomposition.

## Decomposition verdict

Pre-registered criteria:
- Criterion-FRONT (mushaf front drives advantage): L_A < L_B AND L_C < L_D
- Criterion-BACK (mushaf back drives advantage): L_B < L_A AND L_D < L_C

**Result: BACK-DRIVEN** (both comparisons favor the back):
- 57/57 split: L_B (86.11) < L_A (87.53) — keeping mushaf's **back** 57
  surahs produces a shorter path than keeping its front 57.
- 28/86 split: L_D (85.09) < L_C (86.96) — keeping mushaf's **back** 28
  surahs produces a shorter path than keeping its front 28. Margin is
  **1.87 units = 1.15 null-SDs**, enormous at this scale.

## Surprising extras

1. **Hybrid D beats pure mushaf.** Nöldeke's front 86 (roughly: all but
   the short mufaṣṣal) followed by mushaf's last 28 surahs (Q 87–114,
   the short-surah tail) gives L_D = 85.09 — 0.67 shorter than pure
   mushaf. This is the first ordering we've tested that is shorter than
   mushaf on this axis. It is still ~9.8% above the 2-opt TSP bound
   (77.47), so not an optimum, but it is a *non-trivial* improvement
   over the canonical text.

2. **Hybrid A (mushaf-front + Nöldeke-tail) is the LONGEST of all six**
   (L_A = 87.53, even longer than pure Nöldeke at 87.23). Mushaf's
   front arc + a chronology-based tail is strictly worse than either
   pure ordering. This is consistent with "mushaf back is the
   designed-for-coherence part; mushaf front is neutral or adversarial
   on this axis."

3. **The "back 28" of mushaf = Q 87–114** is the short-surah mufaṣṣal
   bracket (Sabbiḥ, Ghāshiya, Fajr, Balad, ...). These end-of-mushaf
   surahs evidently share vocabulary with their neighbors enough to
   give Hybrid D its edge when they follow Nöldeke's early-Meccan block.

## Interpretation

[[h-new-111-fisher-rao-mushaf|H-NEW-111]] framed the mushaf's Fisher-Rao shortness as a global property.
[[h-new-224-hybrid-orderings|H-NEW-224]] localizes it: **the coherence signal is concentrated in the
short-surah mufaṣṣal bracket (Q 87–114), not in the long ṭiwāl/muqaṭṭaʿāt
opening (Q 2–57)**. In the ṭiwāl block, mushaf ordering is actually
*worse* than Nöldeke chronology on Fisher-Rao — using Nöldeke's order
in the front yields shorter hybrids (B beats A; D beats C).

Why might this be? Speculatively:
- The mushaf's front arc is organized by a different principle (length,
  topic, legal-vs-narrative mixing, muqaṭṭaʿāt grouping) that *trades
  away* Fisher-Rao coherence for other properties.
- The mufaṣṣal back, by contrast, runs through thematically-tight
  short surahs (e.g. Q 87 → Q 88 → Q 89 chain of early-Meccan exhortation,
  Q 113 → Q 114 muʿawwidhatayn pair) where vocabulary continuity and
  canonical ordering are aligned.
- Classical tradition explicitly treats the mufaṣṣal as a late-revealed,
  thematically-grouped unit; this is consistent with canonical-order
  coherence being higher there.

## Caveats / honest limits

1. **Descriptive, not causal**. The −0.67 margin of hybrid D over
   mushaf is 0.41 null-SDs — non-trivial but not a formal
   statistical dominance test. A proper test would permute across
   a family of "splice surgeries" to ask how many produce shorter
   paths than mushaf; not done here.

2. **Single feature set**. Fisher-Rao on QAC STEM root top-500 only.
   Robustness to char-4-gram features ([[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]) or verse-length
   features ([[h-new-111c-fisher-rao-verselen|H-NEW-111c]]) is NOT tested. If the decomposition reverses
   on those features, the back-driven interpretation weakens.

3. **The "splice" procedure is one of many plausible choices**. Taking
   donor-order for the tail (preserving Nöldeke's internal order) is
   one way; another is to sort the tail by arbitrary rule (length
   etc). No forking-paths coverage.

4. **Hybrid D being shorter than mushaf does NOT imply mushaf is
   suboptimally ordered**. The 2-opt TSP upper bound (77.47) is still
   ~7.6 below hybrid D. There are many orderings below mushaf; we just
   found one concrete, interpretable example.

5. **"Nöldeke front-86" includes surahs that are chronologically
   Medinan in Nöldeke's scheme** (e.g. Q 2, 3, 4, 5 in Nöldeke's
   late-Medinan phase). So hybrid D is not "Meccan front + short
   back" — it is "Nöldeke's full 86-deep chronological reading +
   canonical-short tail". The interpretation is about ORDERING
   mechanics, not content-class.

## Connections

- Contradicts a strong reading of [[h-new-111-fisher-rao-mushaf|H-NEW-111]] that "mushaf is
  globally optimized": the optimization is regional (back 28
  surahs), not uniform.
- Consistent with earlier intuitions about the mufaṣṣal being a
  distinct structural unit in the canonical text (see classical
  tradition in `data/literature` on ṭiwāl vs mufaṣṣal divisions).
- Queue: H-NEW-224.1 extending to char-4-gram ([[h-new-111b-fisher-rao-char-4gram|h-new-111b]]) D matrix.
- Queue: H-NEW-224.2 — which specific mushaf-tail surahs drive D's
  advantage? (Leave-one-out on the last 28.)

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-224-hybrid-orderings-prereg.md`
- Script: `scripts/h_new_224_hybrid_orderings.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-224.json`

## Verdict

**PASS-DESCRIPTIVE — BACK-DRIVEN.**

Both pre-registered criteria fire: L_B < L_A (by 1.42) AND L_D < L_C
(by 1.87). Mushaf's Fisher-Rao advantage is localized to the back
(mufaṣṣal + short surahs), not the front (ṭiwāl + muqaṭṭaʿāt).
Surprise bonus: hybrid D (Nöldeke-front-86 + mushaf-tail-28) is
0.67 shorter than pure mushaf.
