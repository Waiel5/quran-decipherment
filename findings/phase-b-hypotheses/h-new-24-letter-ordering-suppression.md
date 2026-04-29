---
finding_id: h-new-24-letter-ordering-suppression
parent_finding: h-new-24-b1-b2
phase: B
status: REGISTERED — side-finding pre-registration for follow-up (task #90 closure)
side_finding_type: hypothesis-generating; not a confirmatory claim on its own
date: 2026-04-13
rules_tuple: (no-tashkeel, whitespace-stripped, letter-level, rasm, 31-letter, w=2000, stride=100, min-sep=500, K=113)
bonferroni_k: N/A (registration, not a new test)
seed: 20260413
author: computational-tester
---

# [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] letter-ordering suppression — side-finding registration

## Purpose of this file

This registration formalizes a **hypothesis-generating side-finding** that
emerged from the [[h-new-24-b1-b2-orthogonalization|H-NEW-24]]-B1 orthogonalization (see
`[[h-new-24-b1-b2-orthogonalization|h-new-24]]-b1-b2-orthogonalization.md`). It is NOT a confirmatory claim — the
registration exists so that downstream tests (tentatively labeled H-NEW-24.1,
H-NEW-24.2, ...) can be run against a pre-registered scope rather than
retrofitted onto the [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] parent.

The M-6 synthesis memo will reference this registration when discussing
pericope-substrate claims at surah scale.

## Side-finding statement

**The Quran's real letter sequence is LESS detectable** by a JS-divergence
letter-multiset boundary scanner than its per-surah-shuffled counterparts.
In signal-decomposition terms (from [[h-new-24-b1-b2-orthogonalization|H-NEW-24]]-B1):

| Source                                          | Hits | Excess over chance | Fraction of real signal |
|-------------------------------------------------|------|--------------------|-------------------------|
| Real Quran (w=2000, K=113)                      |   41 | +16.43             | 100 %                   |
| Sub-(e) within-surah shuffle (multiset only)    |   53 | +28.67             | **+174.5 %**            |
| Sub-(f) length-matched i.i.d. (length only)     |   25 |  +0.53             | **+3.2 %**              |
| Residual attributed to letter-ordering          |  −12 | −12.24             | **−74.5 %**             |

The −74.5 % ordering contribution is a **suppression**, not absence: real
ordering actively *masks* a boundary signal that would be sharper under
multiset-only preservation.

## Three candidate mechanisms (H-NEW-24.1, .2, .3)

The registration names these for disciplined follow-up. NONE has been tested;
none has been pre-committed to an effect size. Each would be a separate
confirmatory test under its own Bonferroni budget.

### H-NEW-24.1 — Word-boundary redundancy / templatic smoothing
Classical Arabic uses consonantal triliteral roots with vocalic templates
(e.g., CaCaCa, CaCCīC, CaCūC) that produce local bigram clumpiness. This
clumpiness can average JS windows into smoother unigrams, masking
sharp multiset transitions at surah boundaries.

Pre-registered test spec (not yet implemented):
- Compare the JS-scan boundary-detection F1 on (a) real Quran, (b) Quran
  with all within-word letter-orderings shuffled (cross-word boundaries
  preserved). If (b) F1 ≫ (a), word-internal templatic structure explains
  the ordering suppression.
- Null: within-word shuffle preserves word-boundary positions and per-word
  multisets; destroys templatic order.
- Acceptance: ΔF1 = F1(b) − F1(a) ≥ 0.10 at K=113 with 100-perm p < 0.005.

### H-NEW-24.2 — Shared cross-surah phrasal motifs
Formulaic phrases (*bismillāh al-raḥmān al-raḥīm*, *wa-huwa al-ʿalīmu l-ḥakīm*,
*lā ilāha illā huwa*, divine-name doublets) appear on both sides of surah
boundaries. These recurrent letter-runs reduce JS divergence across a
boundary, dampening detection.

Pre-registered test spec:
- Construct a formula-registry from top-50 most-frequent Quranic n-grams
  (n ∈ {3, 4, 5}) at the word-level.
- Mask these formulae (replace with a neutral placeholder) in one variant;
  leave the Quran unchanged in another.
- Compare K=113 F1 with/without formula masking. If masking raises F1, the
  formula-hypothesis is supported.
- Null: formula-masking provides no F1 improvement (ΔF1 ≤ 0 after 100-perm).

### H-NEW-24.3 — Stylometric cross-boundary coupling
Rhyme-scheme continuity and divine-name-cluster continuity across adjacent
surahs may share letter-level structure that the JS-scanner sees as
"non-boundary." This is M-6 adjacent — adjacent-surah phase-locking at
the letter-multiset level.

Pre-registered test spec:
- For each surah pair (k, k+1), compute per-surah fāṣila-set letter inventory.
- Compute JS(fāṣila_k, fāṣila_{k+1}) — rhyme-slot multiset divergence across
  the boundary.
- Regress boundary-hit-indicator (1 if the scanner detected the k|k+1 break)
  against JS(fāṣila_k, fāṣila_{k+1}). If **low JS at boundary** correlates
  with **missed detection**, stylometric cross-boundary coupling is confirmed.
- Null: ρ(JS_rhyme, detection-indicator) = 0 by permutation, 1000 perms.
- Acceptance: Spearman ρ > 0.20 two-sided p < 0.005.

## Why register now, not test

1. Task #44 (parent [[h-new-24-b1-b2-orthogonalization|H-NEW-24]]) closed CONFIRMED at audit-024. Task #64/65
   (B1+B2 follow-ups) closed CONFIRMED. The three candidate mechanisms
   above are natural continuations but each requires meaningful scope
   commitment — they are H-NEW-scale tests, not addenda.

2. Pre-registering here makes the hypothesis-generating side-finding
   **testable under a pre-committed null spec** rather than retrofitted.
   Each follow-up will be a fresh task with its own bonferroni_k, its own
   acceptance criteria, and its own data commitments.

3. Audit-024 and audit-025 both flagged the −74.5 % ordering suppression as
   "surprising; needs downstream follow-up." Registration is the canonical
   project mechanism for taking that footnote seriously.

## Relation to M-6 pericope-substrate synthesis

M-6 (pericope-block substrate as within-surah chain-coherence explanandum)
is currently a within-surah claim. This side-finding extends M-6 upward to
a **cross-surah** scale: if H-NEW-24.2 or H-NEW-24.3 confirms, the pericope
substrate has phase-locking at surah boundaries as well, not only at
within-surah pericope scale. This would align M-6 with al-Biqāʿī
local-munāsaba (team-discovery-013) at the letter-multiset level.

## Scope restrictions

- This registration ONLY covers the letter-multiset JS-scan operationalization
  at (w=2000, stride=100, min-sep=500, K=113 and 200) and the
  31-letter rasm alphabet under the [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] rules_tuple. It does NOT
  generalize to bigram/trigram/semantic-level ordering claims — those would
  require independent registration.

- "Suppression" here means REDUCED detectability by this specific scanner.
  It does NOT imply the Quran's ordering is deliberately designed to evade
  multiset-boundary detection; naturalistic mechanisms (a), (b), (c) above
  are each sufficient alone.

- The −74.5 % figure depends on the reference point "excess over chance."
  Under a different baseline (e.g., excess over sub-(f) length-only), the
  fractional attribution changes. The QUALITATIVE ordering <br>
  chance < real < within-shuffle is robust across baselines; the
  percentage decomposition is sensitive to the choice of reference.

## Reproducibility

- Source computation: `scripts/h_new_24_b1_b2_orthogonalization.py`
- Registered in MASTER-FINDINGS-LEDGER under §5 letter-scale stratified
  signatures (task #91 pending will add the formal §1 row).
- Seed 20260413 universal for all follow-up registrations.

## Status

- **Registered** as pre-reg on 2026-04-13. Follow-up tasks H-NEW-24.1 / .2 /
  .3 NOT yet dispatched; team-lead prioritization gate applies.
- This file closes task #90 "Register [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] letter-ordering suppression
  side-finding."
