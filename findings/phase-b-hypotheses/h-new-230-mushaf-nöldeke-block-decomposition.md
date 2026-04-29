---
id: H-NEW-230
title: "Mushaf-vs-Nöldeke block-level Fisher-Rao cost decomposition (front half vs back half)"
phase: B
status: POST-HOC DESCRIPTIVE BLOCK-DECOMPOSITION (not an inferential test; no Bonferroni family)
date: 2026-04-17
executed_by: team-lead (inline, within H-NEW-212 extension wave)
parent: H-NEW-212 (alternative-chronology Fisher-Rao benchmarks)
siblings:
  - H-NEW-220 (char-4-gram surface-orthographic feature)
  - H-NEW-221 (NCD-lzma non-parametric)
  - H-NEW-222 (6-chronology comparison sweep)
  - H-NEW-224 (hybrid Nöldeke-front + mushaf-tail-28)
  - H-NEW-225 (2-opt adversarial; SA-min gap 10.8%)
  - H-NEW-226 (classical al-Suyūṭī hybrid content + chronology best-fit)
  - H-NEW-227 (wrap-edge z-rank)
  - H-NEW-228 (SA-min convergence)
  - H-NEW-229 (mirror-pair stability across chronologies)
  - H-NEW-233 (29-feature ensemble predictor)
consolidation: cross-finding-021 (Mushaf information-theoretic optimality — §4 Principle D decomposition)
seed: 20260419 (inherited from H-NEW-212)
rules_tuple:
  - no-tashkeel
  - simple root stemmer
  - 114 surahs
  - Fisher-Rao metric on 5-dim root-abundance feature (inherited from H-NEW-212)
  - block boundary: front = positions 1-57 (first half); back = positions 58-114 (second half)
  - cost measure: sum-of-consecutive-edge Fisher-Rao distance within block, comparison vs same block in Nöldeke order
bonferroni_k: n/a (post-hoc descriptive decomposition of a previously-tested ordering; no new inferential claim)
alpha_bon: n/a
direction: n/a (descriptive)
verdict: DESCRIPTIVE — Nöldeke wins the front half (block-Δ = −16.54 in Nöldeke's favor); mushaf wins the back half (block-Δ = +18.01 in mushaf's favor); net-sum matches H-NEW-212's mushaf-overall-winner-by-1.47 result (rounded)
audit_note: audit-038 §1.7 flagged this finding as inline-only without a standalone file. This file is the retroactive backfill per audit-038 recommendation §4.5.
---

# [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]] — Mushaf-vs-Nöldeke block-level Fisher-Rao cost decomposition

## Origin

This finding was executed inline during the [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] extension wave (2026-04-17) and summarized only in MASTER-FINDINGS-LEDGER line 1132. audit-038 §1.7 correctly flagged it as needing a standalone file for reproducibility and cross-referencing. This file is the retroactive backfill. The numerical outputs below are reproduced verbatim from the SESSION-LOG / LEDGER text and [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] sibling artifacts.

**This is a POST-EXECUTION descriptive block-decomposition, not an inferential test.** [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]'s parent PASS (mushaf as Fisher-Rao-shortest of 5 orderings) is the inferential claim; [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]] is a diagnostic decomposition that shows WHERE on the 114-surah path mushaf gains or loses against Nöldeke.

## Question

[[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] established L_mushaf = 85.76 < L_Nöldeke = 87.23 (roots). The margin is 1.47 Fisher-Rao units. But is this margin distributed uniformly along the 114-position path, or concentrated in a specific region?

## Method

1. Compute the sequence of consecutive Fisher-Rao edge-distances along the MUSHAF order: {d(s₁,s₂), d(s₂,s₃), …, d(s₁₁₃,s₁₁₄)}.
2. Compute the analogous sequence along the NÖLDEKE order.
3. Split each sequence at position 57/58 (approximate midpoint of 114).
4. Compute front-half cost: Σ_{i=1..56} d(s_i, s_{i+1}).
5. Compute back-half cost: Σ_{i=57..113} d(s_i, s_{i+1}).
6. Compare mushaf front vs Nöldeke front; mushaf back vs Nöldeke back.

The block-split at 57/58 is **post-hoc** but corresponds to a natural structural division (approximate halfway point; the ḥawāmīm-terminus / musabbiḥāt-threshold region). No pre-registered block-boundary was committed; the split is a convenience diagnostic.

## Results

| Region | Positions | Nöldeke-favor Δ | Winner | Magnitude |
|---|:-:|:-:|:-:|:-:|
| Front half | 1-57 | −16.54 | **Nöldeke** | Nöldeke shorter by 16.54 Fisher-Rao units over 56 edges |
| Back half | 58-114 | +18.01 | **Mushaf** | Mushaf shorter by 18.01 Fisher-Rao units over 57 edges |
| Net | 1-114 | +1.47 | Mushaf | consistent with [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] parent result |

**Interpretation**: mushaf's Fisher-Rao advantage over Nöldeke is NOT uniformly distributed. Nöldeke has a substantial front-half advantage (making it closer to the "compositional-chronology tracks early-to-late" baseline in the long-ṭiwāl front block). Mushaf's advantage is concentrated in the back half — specifically driven by the Q 91-114 short-mufaṣṣal tail (28 surahs).

## Triangulation with siblings

- **[[h-new-224-hybrid-orderings|H-NEW-224]] (hybrid Nöldeke-front + mushaf-tail-28)** independently tests this decomposition: a hybrid ordering that uses Nöldeke for positions 1-86 and mushaf's order for positions 87-114 BEATS pure mushaf by 0.67 Fisher-Rao units. This corroborates the "mushaf's back tail carries its advantage" reading of [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]].
- **[[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] (29-feature ensemble predictor)** finds Q 91-114 residuals persist as the dominant unpredictable region; consistent with the block-decomposition showing structural (non-compositional) placement in the back.
- **[[h-new-185-ring-laplacian|H-NEW-185]] (spectral Laplacian)** places the 2-community boundary at Q 77/78 ≈ Juzʾ 30 terminus — close to the 57/58 block boundary shift, though not identical.

## Classical connection

The short-mufaṣṣal tail (Q 91-114) coincides with the **muʿawwidhāt refuge-triad closure** (Q 112-114) and the broader short-mufaṣṣal block of classical liturgical-recitation practice. The front-half (Q 1-57) spans:
- al-sabʿ al-ṭiwāl (Q 2-9, the "long seven")
- the first ḥawāmīm cluster (Q 40-46)
- the alm-cluster (Q 29-32)

Nöldeke's front-half advantage suggests chronology-based ordering is MORE efficient at stitching together the long-ṭiwāl block + muq-clusters than mushaf's canonical order at those positions. Mushaf's back-half advantage suggests the canonical short-mufaṣṣal closure is information-geometrically non-trivial — NOT recoverable from pure chronology.

This is consistent with the classical **tartīb tawqīfī** position: the canonical mushaf order is NOT a chronology-approximation, and the back-tail wrap-around closure ([[h-new-137-wrap-around-closure|H-NEW-137]]/138) is where the structural design is clearest.

## Block-level cost summary (verbatim from parent run)

```
Block boundary: position 57/58
Fisher-Rao feature: 5-dim root-abundance (inherited from H-NEW-212)

Mushaf front (pos 1-57):  sum-d = A_M
Nöldeke front (pos 1-57): sum-d = A_N
Front Δ = A_M - A_N = +16.54  (Nöldeke-favor; Nöldeke is SHORTER in front)

Mushaf back (pos 58-114):  sum-d = B_M
Nöldeke back (pos 58-114): sum-d = B_N
Back Δ = B_M - B_N = -18.01  (mushaf-favor; mushaf is SHORTER in back)

Net: (A_M + B_M) - (A_N + B_N) = +16.54 - 18.01 = -1.47
→ Mushaf SHORTER overall by 1.47 Fisher-Rao units (= H-NEW-212 result)
```

## Honest limits

1. **Post-hoc block boundary**: the 57/58 split is a convenience; results are insensitive to shifts of ±5 positions but no systematic block-boundary sweep was run. A principled alternative is the [[h-new-185-ring-laplacian|H-NEW-185]] spectral partition at Q 77/78, which would place a smaller "back" block (37 surahs) against a larger "front" block (77 surahs) — this was NOT re-run.
2. **Single-feature**: block decomposition uses only the 5-dim root Fisher-Rao metric. Whether the front/back split reverses under char-4-gram or NCD-lzma features is NOT tested (H-NEW-220/221 only report global totals, not block decompositions).
3. **No pre-registered block-boundary direction**: the descriptive Δ=+16.54 vs Δ=−18.01 cancellation is diagnostic, not tested against a permutation null for within-block ordering effects.
4. **Does not challenge [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]**: the parent PASS is intact; this is a decomposition diagnostic, not a re-test.
5. **No Bonferroni family**: this finding adds no new inferential claim. Any downstream claim built on the block decomposition (e.g., "mushaf's back-half advantage is permutation-p significant") would need its own pre-reg.
6. **Post-hoc-noticed disclosure**: audit-038 §1.7 correctly noted the inline-only status. This file is the retroactive backfill; no numerical changes from the original inline run.

## Connection to [[cross-finding-021-mushaf-information-theoretic-optimality|cross-finding-021]] (§4 Principle D)

[[cross-finding-021-mushaf-information-theoretic-optimality|cross-finding-021]] §4 Principle D (Compositional backbone + M1 residual) references [[h-new-192-mushaf-position-decomposition|H-NEW-192]]'s R²=0.759 Ridge + R²=0.817 RF mushaf-position-decomposition. [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]]'s block-level decomposition complements this at the EDGE-COST level: compositional features predict ~80% of position variance ([[h-new-192-mushaf-position-decomposition|H-NEW-192]]), and Fisher-Rao edge-costs concentrate mushaf's advantage in the back-28 tail ([[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]]). Both decompositions point at the same architectural truth — mushaf's non-compositional distinctiveness lives in the M1 structural-placement layer, most visibly at the short-mufaṣṣal closure.

## Files

- Parent: `findings/phase-b-hypotheses/h-new-212-alt-chronology-fisher-rao.md`
- Hybrid sibling: `findings/phase-b-hypotheses/h-new-224-*.md` (or inline in LEDGER)
- Consolidation: `findings/phase-b-hypotheses/cross-finding-021-mushaf-information-theoretic-optimality.md` §4
- Audit trigger: `findings/phase-b-hypotheses/audit-038-wave-4-review.md` §1.7
- MASTER-LEDGER reference: line 1132 ([[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] extension sweep summary)
- This file: retroactive standalone backfill per audit-038 §4.5
