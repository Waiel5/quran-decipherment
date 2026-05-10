---
id: H-NEW-1510
title: Sajda 15-verse pericope-scale root-Jaccard cohesion replication (H-NEW-1330 flip test)
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-1510-sajda-pericope-replication (single pre-registered primary test)
alpha_bon: 0.05
direction_of_effect: TIGHTER — mean pairwise root-Jaccard of the 15 sajda-verse pericopes (each sajda verse ± 2 verses, clipped to surah boundaries) is GREATER than the mean of 10,000 length-matched random-pericope draws from the flat 6,236-verse index (one-tailed permutation null)
origin: H-NEW-1330 NULLed the 14-surah sajda cluster at whole-surah Fisher-Rao scale (Cell A p=0.571, Cell B p=0.110, PC passed p=0.00020). Per H-NEW-1380 scale-of-aggregation principle (cross-finding-025 corollary), this pre-reg re-tests the same theological set at the pericope-scale — the scale at which the sajda-marker operates (a single liturgical-prostration trigger verse and its immediate context). This pre-reg formally re-tests whether shifting from whole-surah to pericope scale flips the NULL to a PASS, providing a second finding-pair (alongside H-NEW-039 / H-NEW-1380) for the scale-of-aggregation axis.
verdict_ceiling: PASS-DIRECTED (single pre-registered direction; k=1)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1 (Q 1 not in test set; immaterial)
  verse_numbering: hafs-kufan
  detection_rule: pericope = union of QAC v0.4 ROOT-field assignments across verses in the locked range (±2 verses around sajda verse, clipped to surah boundaries)
  root_source: data/morphology/quranic-corpus-morphology-0.4.txt
  null_model: 10,000 random draws of 15 length-matched pericopes from the flat 6,236-verse index; for each pericope length L in the observed length-vector (clipped per surah boundary), draw start ~ Uniform[0, N - L]; wraparound disallowed; no requirement that null draws lie within the same surah
---

# H-NEW-1510 pre-registration — Sajda 15-verse pericope-scale root-Jaccard cohesion

## Origin

H-NEW-1330 (2026-05-09) NULLed the 14-surah sajda cluster {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96} on whole-surah Fisher-Rao root-distribution cohesion (Cell A p=0.571, Cell B length-matched p=0.110, MW-5 PC passed at p=0.00020). Its honest interpretation: "the sajda-trigger is the thinnest possible marker — one verse out of 19 to 206 — and cannot move the surah's root-distribution centroid relative to corpus."

H-NEW-1380 (2026-05-09 PM) formalized scale-of-aggregation as a methodological axis under cross-finding-025. The Iblīs cluster NULLed at whole-surah scale (H-NEW-039) but PASSED at pericope scale (z=+4.76, p≤10⁻⁴). The pre-reg explicitly queued the sajda case as a candidate re-test at pericope scale (MASTER-FINDINGS-LEDGER §10.51.3 bullet 2).

This pre-reg executes that queued re-test. The motivating prior: at whole-surah scale a single sajda verse is diluted by 19–206 verses of heterogeneous content. At verse ± 2 scale (the actual liturgical-recitation unit, since the prostration is triggered by the verse-in-its-immediate-context), the lexical signature of the prostration cue — *sjd* and its companion roots (*kbr*, *Hmd*, *sbH*, *xrr*, *rbb*) — has a chance to dominate the local root-set.

## Hypothesis (single primary test)

**H1**: The 15 sajda-verse pericopes — each defined as the sajda verse ± 2 verses (5-verse window centered on the sajda verse, clipped to surah boundaries) — exhibit TIGHTER mean pairwise root-Jaccard similarity than length-matched random-pericope draws from the flat 6,236-verse corpus index.

**Test statistic**: mean of all C(15,2) = 105 pairwise root-Jaccard values among the 15 pericope root-sets.

**Null distribution**: 10,000 random draws; for each of the 15 pericope lengths (determined by clipping ±2-verse windows to surah boundaries), draw a start index from the flat 6,236-verse index uniformly and take L consecutive verses; compute the pericope's root-set; repeat for all 15 lengths; compute the mean pairwise root-Jaccard.

**Decision rule**: PASS-DIRECTED if p_perm < 0.05 AND direction matches lock (J_mean > null mean). Single primary test (k=1); no Bonferroni adjustment.

## Pericope inventory (locked, classical-Sunnī 14 surahs + Q 22 double sajda = 15 sajda verses)

Sources cross-verified: (i) ۩ glyph attestation in `quran-text/quran-no-tashkeel.json` for each verse; (ii) sajda root (*sjd*) or near-companion root attestation in QAC v0.4. Q 22 carries TWO sajdas per `surahs/Q022-al-hajj/Q022-F-06-double-sajda-singleton-prereg.md` (verses 18 and 77). The list below matches H-NEW-1330's 14 surahs with Q 22:77 added as the 15th sajda verse.

| # | Sajda verse | Surah length | ±2 window (clipped) | Window length L |
|:-:|:--|:-:|:--|:-:|
| 1 | Q 7:206  | 206 | [204..206] | 3 |
| 2 | Q 13:15  | 43  | [13..17]   | 5 |
| 3 | Q 16:50  | 128 | [48..52]   | 5 |
| 4 | Q 17:109 | 111 | [107..111] | 5 |
| 5 | Q 19:58  | 98  | [56..60]   | 5 |
| 6 | Q 22:18  | 78  | [16..20]   | 5 |
| 7 | Q 22:77  | 78  | [75..78]   | 4 |
| 8 | Q 25:60  | 77  | [58..62]   | 5 |
| 9 | Q 27:26  | 93  | [24..28]   | 5 |
| 10 | Q 32:15 | 30  | [13..17]   | 5 |
| 11 | Q 38:24 | 88  | [22..26]   | 5 |
| 12 | Q 41:38 | 54  | [36..40]   | 5 |
| 13 | Q 53:62 | 62  | [60..62]   | 3 |
| 14 | Q 84:21 | 25  | [19..23]   | 5 |
| 15 | Q 96:19 | 19  | [17..19]   | 3 |

Length-vector L = (3, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 3, 5, 3); sum = 68 verses across 15 pericopes; pairwise comparisons = 105.

**Edge-clipping policy** (locked): for sajda verses within 2 verses of a surah boundary (Q 7:206 last verse of 206; Q 22:77 second-to-last of 78; Q 53:62 last verse of 62; Q 96:19 last verse of 19), the window is **clipped at the surah boundary — no cross-surah bleed**. This is the conservative choice: it preserves surah integrity (no cross-surah contamination of the pericope root-set) and uses the observed clipped length L in the null model so the null exactly matches the observed length-vector.

## Direction lock

Direction is LOCKED before computation: **J_mean > null mean (TIGHTER)**. Pre-commit-violation = J_mean < null mean (strict reversal). Pre-commit-violation = NULL with full prominence per Protocol §1.8.

The directional prior is grounded in three priors:
1. The sajda-trigger verse and its 2-verse context typically include the *sjd* root (or its semantic companion roots *kbr*, *xrr*, *Hmd*, *sbH*, *rbb*) in concentrated form — these are the lexical cues that trigger the prostration in the classical recitation tradition.
2. H-NEW-1380 demonstrated that thin-marker NULLs at whole-surah scale can flip to PASSes at pericope scale (Iblīs case: z=+0.24 NULL → z=+4.76 PASS).
3. al-Bāqillānī *Iʿjāz al-Qurʾān* and al-Suyūṭī *al-Itqān* nawʿ on sujūd al-tilāwa both describe the sajda-recitation context as a discrete liturgical unit (not a whole-surah category) — implying pericope is the correct unit of aggregation for liturgical-marker cohesion.

## Operational definition

- **Pericope** = union of all QAC v0.4 ROOT-field assignments across the locked verse range (sajda verse ± 2 verses, clipped to surah boundaries).
- **Root extraction**: `data/morphology/quranic-corpus-morphology-0.4.txt` v0.4; ROOT field of each morphological segment (one ROOT per segment when present); a verse's roots = union of its segments' ROOT fields. Same code path as H-NEW-1380 / Q038-F-07.
- **Pairwise Jaccard**: J(i,j) = |R_i ∩ R_j| / |R_i ∪ R_j|. If both sets empty, J=0.
- **Mean pairwise Jaccard**: mean over all C(15,2) = 105 unordered pairs.

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel |
| Token level | QAC v0.4 root-tokens via stem-root field |
| Counting unit | unique-root set per pericope |
| Basmala | counted only in Q 1 (Q 1 not in test set; immaterial) |
| Reading tradition | Hafs-Kufan |
| Script | Mashriqi |
| Aggregation scale | PERICOPE (sajda verse ± 2, clipped to surah boundary) — distinguished from whole-surah scale used in H-NEW-1330 |
| Pericope ranges | 15 ranges locked in inventory table above |
| Sajda inventory | Classical-Sunnī 14 surahs (al-Suyūṭī *al-Itqān*; Bukhārī Kitāb Sujūd al-Qurʾān; Tirmidhī Kitāb al-Witr) + Q 22:77 second sajda (per Q022-F-06; widely held in Shāfiʿī school) = 15 sajda verses. Mālikī exclusion of Q 38:24 not applied. Imāmī 4-mandatory subset not applied. Rules-tuple-sensitivity tests under alternative sajda inventories are out of scope for this pre-reg. |

## Permutation null protocol

1. Seed RNG = 20260509 (matches H-NEW-1380 and Q038-F-07 for cross-finding-comparable instrument; ensures cross-finding compatibility, NOT seed-independent replication).
2. For each of 10,000 permutations:
   - For each pericope length L in (3, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 3, 5, 3): sample `start ~ Uniform[0, 6236 - L]` from the flat verse-index; take the L consecutive verses; compute their root-set.
   - Compute mean pairwise root-Jaccard across the 15 sampled root-sets.
3. p_perm = (count of perm-J ≥ observed-J) / 10,000 (strict one-tailed; same convention as Q038-F-07 / H-NEW-1380).

## Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| p_perm < 0.05 AND J_mean > null mean | PASS-DIRECTED (scale-of-aggregation flip CONFIRMED for sajda) |
| p_perm ≥ 0.05 AND J_mean > null mean | DIRECTIONAL (scale-of-aggregation flip WEAK) |
| J_mean ≈ null mean (within 0.5 std) | NULL (no scale-flip; the sajda marker is genuinely too thin even at pericope scale) |
| J_mean < null mean | PRE-COMMIT-VIOLATION → NULL with full prominence (sajda-pericopes are MORE DISPERSED than random — surprising and structurally informative) |

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: Root-Jaccard + 105-pair mean + length-matched perm null locked above; instrument identical to H-NEW-1380.
- **MW-2 (corpus-prior)**: 10,000 perms; minimum standard met.
- **MW-3 (alternative-models)**: Length-matched permutation null is the primary; TF-IDF and root-cosine alternatives queued as follow-ups if the primary verdict is ambiguous.
- **MW-4 (over-fitting)**: No fitted parameter; pericope ranges fully determined by classical sajda inventory + locked ±2 rule + boundary-clipping rule.
- **MW-5 (replication)**: Cross-scale pair (H-NEW-1330 whole-surah NULL vs this pre-reg's pericope test) is the structural replication unit. Different-seed run queued as H-NEW-1510b if PASS.
- **MW-6 (instrument-control)**: H-NEW-1330 PC at p=0.00020 demonstrates the FR/Jaccard machinery can detect known same-size cohesion; that PC carries forward as a scale-comparable instrument-control.
- **MW-7 (post-hoc cap)**: Single pre-registered direction; not post-hoc.

## Scale-of-aggregation pair logged before computation

| Scale | Finding | Set | Statistic | Verdict (locked or pre-locked) |
|:--|:--|:--|:--|:--|
| Whole-surah | **H-NEW-1330** | 14 sajda-surahs | mean intra-cluster FR | **NULL** (Cell A p=0.571, Cell B p=0.110; PC pass p=0.00020) |
| Pericope | **H-NEW-1510** (this pre-reg) | 15 sajda-verse pericopes (sajda verse ± 2, clipped) | mean pairwise root-Jaccard | **PENDING — direction locked TIGHTER** |

Either verdict will be a first-class finding under the scale-of-aggregation axis. A PASS adds the sajda case to the H-NEW-039/H-NEW-1380 pair (graduating cross-finding-025 toward formalization). A NULL implies the sajda-marker is genuinely too thin to drive cohesion even at the verse-context scale — a substantive refinement of the marker-thickness rule.

## Garden-of-forking-paths disclosure

- The 15 sajda verses are LOCKED from the classical-Sunnī inventory + Q 22:77 (per Q022-F-06 documenting al-Ḥajj's double-sajda status). No reselection.
- The ±2 window is the canonical pericope-window choice (matches Q022-F-08 *sajda-verses-block-boundaries* and standard pericope-analysis literature). No window-width sweep.
- Boundary-clipping (vs cross-surah bleed) is the pre-committed conservative choice. A sensitivity follow-up with cross-surah bleed allowed is queued, NOT run here.
- Seed = 20260509 deliberately matches H-NEW-1380 / Q038-F-07 for instrument-comparable cross-finding inference. A different-seed run (H-NEW-1510b) is queued for genuine seed-independence if this pre-reg PASSes.
- 15 sajda verses vs H-NEW-1330's 14 surahs: the unit count differs because Q 22 has two sajda verses but is one surah. This is the **definitional point of the test**: at pericope scale, the unit is the sajda-verse-with-context, so Q 22 contributes two units. This was pre-locked before computation.

## Connection to existing findings

- **H-NEW-1330 NULL**: same theological set at whole-surah scale, FR root-distribution → NULL. The cross-scale partner of this pre-reg.
- **H-NEW-1380 PASS-DIRECTED-REPLICATION**: Iblīs cluster at pericope-scale, z=+4.76. The methodological precedent that scale-flips can promote NULL→PASS for thin-marker thematic sets.
- **H-NEW-039 NULL**: Iblīs cluster at whole-surah, NULL. The cross-scale partner of H-NEW-1380.
- **cross-finding-025 (PRELIMINARY-SYNTHESIS)**: marker-thickness × scale-of-aggregation joint rule. If this pre-reg flips H-NEW-1330 to a PASS, that yields a second cross-scale finding-pair, advancing cross-finding-025 toward formal codification (which requires 2+ pairs per §10.51.4).
- **Q022-F-06**: Q 22 double-sajda singleton status — basis for including Q 22:77 as the 15th sajda verse.
- **H-NEW-1331 PASS-DIRECTED**: sajda × muqaṭṭāʿat hypergeometric over-representation (7 of 14 sajda surahs muqaṭṭāʿat-opened). Independent of this test but together they begin building a structural profile of the sajda set: hypergeometric structural correlate + (this pre-reg) pericope-scale root cohesion.

## Anti-flip

The reverse direction (J_mean < null mean) = pre-commit violation → published as NULL with full prominence. A reverse outcome would be substantively informative: it would mean sajda pericopes are MORE DISPERSED than random equally-sized pericopes — i.e., the prostration trigger appears in lexically heterogeneous contexts across the corpus, which would refine our understanding of how the trigger functions liturgically (one trigger, many semantic frames). Such an outcome must be published as NULL with prominence per Protocol §1.3 and §1.8.

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. SHA computed after this file is finalized; embedded in `scripts/h-new-1510.py` as EXPECTED_SHA. Any mismatch = fail-fast.
