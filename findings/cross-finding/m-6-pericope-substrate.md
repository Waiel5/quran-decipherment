---
memo_id: m-6-pericope-substrate
type: cross-finding synthesis
date: 2026-04-13
status: META-PATTERN STANDING (promoted audit-024 per 5-path threshold)
parent: findings/team-discovery-synthesis.md §META-PATTERN M-6
rules_tuple: (no-tashkeel, orthographic-token & lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
author: computational-tester
---

# M-6 Pericope-Substrate Synthesis Memo

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

## Operative framing (auditor audit-024, verbatim)

> "Pericope-level topic-coherence as the Quran's dominant structural
> substrate — not surah-level or ring-level composition. Adjacent-verse
> continuity, global topic-clumping, and genre-specific rhetorical
> features (elision, hapax-placement, eschatological clustering) all
> point to pericope as the minimal semantic unit. Downstream analyses
> at the surah or macro scale should first test whether the effect is
> pericope-mediated."

This reframes the project's analytical default: instead of "does the
Quran have surah-level composition features?" the question becomes "is
this feature pericope-mediated?" For any future surah- or macro-scale
signal, the first-line null is now a block-preserving within-pericope
randomization, not a bag-of-verses shuffle.

## The five parallel paths

M-6 was promoted from CANDIDATE → STANDING when the auditor's
pre-registered 4-path threshold was crossed by a 5th converging leg.
Each path is independent in its scale, statistic, and null model.

### Path 1 — [[h-new-2-iltifat-catalog-rho|H-NEW-2]] pronoun-chain coherence

- **Claim:** pronoun reference chains show within-surah coherence above
  the bag-of-verses shuffle baseline.
- **Signal scale:** word-to-verse (pronoun→antecedent hops).
- **M-6 leg:** the original audit-013 diagnostic, "chain/adjacency
  coherence finding + null that destroys ALL structure not just the
  hypothesised structure → inflated Z," was first stated here. The
  revised within-pericope block-null is the gate for confirmation.
- **Status:** audit-013 revision pending; counts as provisional leg
  under the standing M-6 call.

### Path 2 — H-NEW-18 pair-distance pericope enrichment

- **Claim:** semantically related verse pairs are distance-enriched at
  pericope-scale gaps.
- **Signal scale:** verse-pair distance distribution within surah.
- **M-6 leg:** directly operationalises "pericope as the minimal
  semantic unit" — the pair-distance peak at sub-surah scale is the
  fingerprint of pericope-block cohesion.

### Path 3 — H-NEW-20 al-Rāzī adjacent-verse autocorrelation

- **Claim:** adjacent verses share roots at rates far above
  within-surah shuffle. IV-weighted Stouffer Z = +22.78 (primary);
  short-stratum Z = +9.57.
- **Signal scale:** verse-to-verse root overlap.
- **M-6 leg:** audit-021 dual-label. Local-verse-pair coherence at
  pericope scale is precisely the M-6-predicted carrier of al-Rāzī's
  linear *naẓm* doctrine.

### Path 4 — H-NEW-29 al-Jāḥiẓ root-renewal CV

- **Claim:** root-renewal coefficient of variation is elevated; the
  top-10 clumped roots map one-to-one onto topic-specific pericopes.
- **Signal scale:** root-distribution across surahs.
- **M-6 leg:** audit-022 promotion evidence. The clumping pattern —
  *sjn* → Yūsuf, *Tlq* → al-Ṭalāq, *nkH* → marriage, *Avm* → sin,
  *Hlf* → oath — is pericope-block substrate observed from the
  lexical side.

### Path 5 — [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] letter-multiset surah-boundary detection

- **Claim:** surah boundaries are recoverable from letter-multiset
  features alone. Optimal K=200; multiset contribution +174.5 %,
  length +3.2 %, ordering −74.5 %.
- **Signal scale:** sub-lexical (letter-level).
- **M-6 leg:** audit-024 5th-path promotion evidence. The multiset
  signal at the letter layer is pericope-substrate manifested at the
  sub-lexical scale — pericope blocks produce characteristic
  letter-frequency fingerprints that bleed across surah boundaries
  where topic-continuity straddles.

## Side-finding (hypothesis-generating): letter-ordering suppression

[[h-new-24-b1-b2-orthogonalization|H-NEW-24]]'s within-layer decomposition returned a **negative
contribution from letter ordering: −74.5 %**. This is orthogonal to
the multiset signal and has no pre-registered M-6 position. It is
registered here as an **M-6-adjacent hypothesis-generating
side-finding at surah scale**, not as a promotion leg.

**What it means operationally.** Once the multiset (what letters are
present in what counts) is known, knowing the order they appear in
*reduces* the boundary-detection AUC. Three non-exclusive mechanism
candidates:

1. **Word-boundary redundancy.** Arabic root morphology and
   template-driven word formation create predictable letter-order
   runs; once multiset is conditioned on, order is redundant and adds
   noise.
2. **Repeated-phrase smoothing.** Formulaic phrases (basmala-adjacent
   formulas, *inna llāha*, *allāhumma*) repeat verbatim across
   surahs; their ordering is highly constrained and identical at
   boundary and non-boundary locations.
3. **Stylometric cross-surah matching.** Ordering at fine scale may
   be doing stylistic fingerprinting that tracks genre across the
   corpus — Meccan vs Medinan, legal vs narrative — rather than
   boundary itself, and under the boundary-detection objective that
   manifests as negative weight.

Filed as **hypothesis-generating** per discipline: this side-finding
was not pre-registered as an M-6 prediction and must not be
back-propagated as M-6 supporting evidence without an independent
pre-registration that targets it specifically.

## What M-6 implies for future work

1. **Default null upgrade.** Any future finding whose statistic is
   computed across verses or surahs should have its primary null
   changed from bag-of-verses shuffle to block-preserving
   within-pericope randomisation. The old null persists only as a
   secondary comparison.
2. **Scale-first inspection.** When a signal appears, first ask
   whether it is pericope-mediated. If the effect survives a
   block-null, it is pericope-transcending; if it collapses, the
   effect was substrate.
3. **Re-auditing queue.** Any historical finding whose diagnostic
   signature matches M-6 (chain/adjacency coherence + global null)
   triggers an automatic re-audit probe. This is the standing
   protocol from audit-013, now active under STANDING status.

## Relationship to M-5

M-5 (classical-doctrine operationalisation ≠ recovery) and M-6
(pericope-substrate) are **convergent, not redundant**. M-5 describes
the relationship between classical texts and our operationalisations;
M-6 describes the phenomenological substrate beneath the operationalised
signal. A finding may fire both simultaneously ([[h-new-2-iltifat-catalog-rho|H-NEW-2]] does) without
double-counting.

## What M-6 does NOT claim

- It does **not** claim the Quran lacks surah-scale or ring-level
  structure. Several tests have returned NULL at those scales; M-6 is
  a positive claim about where the signal *does* live, not a negative
  claim about where it doesn't.
- It does **not** claim pericope-substrate is unique to the Quran.
  The prose-baseline comparison for pericope-substrate has not been
  run on Bukhari or Jāḥiẓ; that is a standing follow-up before any
  Quran-distinctiveness claim under M-6.
- It does **not** supersede iltifāt or al-Rāzī's *munāsaba*; it
  reframes them as higher-level rhetorical descriptions of a
  lower-level block-structured substrate.

## Reproduction pointers

- Parent paragraph: `findings/team-discovery-synthesis.md` §META-PATTERN M-6 (lines 1944-2022).
- Promotion audit: `findings/team-audits/audit-024.md`.
- Five underlying findings:
  - [[h-new-2-iltifat-catalog-rho|H-NEW-2]]: `findings/phase-b-hypotheses/pronoun-chain-coherence.md` (revision pending).
  - H-NEW-18: `findings/phase-b-hypotheses/pair-distance-pericope.md`.
  - H-NEW-20: `findings/phase-b-hypotheses/razi-adjacent-verse-autocorrelation.md`.
  - H-NEW-29: `findings/phase-b-hypotheses/root-renewal-cv.md`.
  - [[h-new-24-b1-b2-orthogonalization|H-NEW-24]]: `findings/phase-b-hypotheses/h-new-24-letter-ordering-suppression.md`
    (side-finding registered there as well).

## Update protocol

This memo is a **synthesis snapshot**, not a living ledger. When a
new path is added or a leg is demoted, update the parent paragraph
in `team-discovery-synthesis.md` first; re-issue this memo with an
incremented date only when the operative framing or standing status
changes.
