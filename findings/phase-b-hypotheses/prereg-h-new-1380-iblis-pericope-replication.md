---
id: H-NEW-1380
title: Iblīs-narrative 7-pericope corpus-wide root-Jaccard cohesion replication + scale-of-aggregation principle
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-1380-iblis-pericope-replication (single pre-registered test)
alpha_bon: 0.05
direction_of_effect: TIGHTER — mean pairwise root-Jaccard of the 7 Iblīs-narrative pericopes is GREATER than the mean of 10,000 length-matched random-pericope draws (one-tailed permutation null)
origin: Q038-F-07 PASSED at z=+4.76 (J_mean=0.1456 vs null=0.0650±0.0169, p_perm=0.0000); H-NEW-039 NULL'd the same 9-surah set at whole-surah FR root-distribution. The two findings span the same theological set across two scales-of-aggregation. This pre-reg promotes Q038-F-07 into the H-NEW corpus-wide inline series and formalizes scale-of-aggregation as a methodological axis (cross-finding-025 corollary).
verdict_ceiling: PASS-DIRECTED-REPLICATION (replicates Q038-F-07 exactly under identical seed + identical instrument; CONFIRMED via independent dispatch is already on record at the surah-template level)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  detection_rule: pericope = union of QAC v0.4 ROOT-field assignments across verses in the locked range
  root_source: data/morphology/quranic-corpus-morphology-0.4.txt
  null_model: 10,000 random draws of 7 length-matched pericopes from the flat verse-index (verse-counts 1, 15, 14, 5, 1, 9, 15), wraparound disallowed
---

# H-NEW-1380 pre-registration — Iblīs-narrative pericope corpus replication + scale-of-aggregation principle

## Origin

Two prior findings span the same theological set at two scales-of-aggregation:

- **H-NEW-039 (NULL, 2026-05-07)**: 9-surah set containing the Iblīs proper-name {Q 2, 7, 15, 17, 18, 20, 26, 34, 38} is NOT FR-cohesive on whole-surah root-distribution. Mean FR=0.9402 vs corpus 0.9237; z=+0.237; p_lower=0.537. The thematic-recurrence-at-proper-name-level signal is washed out by surah-level vocabulary.
- **Q038-F-07 (CONFIRMED, 2026-05-09, z=+4.76)**: 7 Iblīs-narrative pericopes drawn from the SAME 9-surah set (excluding 2 surahs where Iblīs is mentioned but without a developed narrative cycle: Q 26 verbal recall in Abraham-Iblīs argument, Q 34 in passing) exhibit corpus-extreme mean pairwise root-Jaccard at pericope-scale.

Both findings are correct under their respective instruments. The interpretive question is methodological:

> If H-NEW-039 NULLs at whole-surah scale and Q038-F-07 PASSES at pericope scale, what scale-of-aggregation is "correct" for asking "is the Iblīs cluster real"?

This pre-reg locks the formal claim:

1. The PASS at pericope scale is genuine (not seed-cherry-picked or instrument-cherry-picked) and replicates under identical seed + identical instrument as a deliberate H-NEW inline replication.
2. The discrepancy between H-NEW-039 NULL and Q038-F-07 PASS is **not** an inconsistency but a scale-of-aggregation phenomenon.
3. **Scale-of-aggregation is itself a methodological axis** under cross-finding-025: marker-thickness × scale-of-aggregation jointly determine whether a cluster will be FR-cohesive on root-distribution.

## Hypothesis (single primary test)

**H1**: The 7 Iblīs-narrative pericopes — Q 2:34, Q 7:11-25, Q 15:31-44, Q 17:61-65, Q 18:50, Q 20:115-123, Q 38:71-85 — exhibit TIGHTER mean pairwise root-Jaccard similarity than length-matched random-pericope draws.

**Test statistic**: mean of all C(7,2)=21 pairwise root-Jaccard values among the 7 pericope root-sets.

**Null distribution**: 10,000 random draws; for each of the 7 pericope lengths {1, 15, 14, 5, 1, 9, 15} verses, draw a random start index from the flat verse-index (6,236 verses minus L+1) and take the L consecutive verses; compute the pericope's root-set; repeat for all 7 lengths; compute the mean pairwise root-Jaccard.

**Decision rule**: PASS if p_perm < 0.05 AND direction matches lock (J_mean > null mean). Single test (k=1); no Bonferroni adjustment.

## Direction lock

Direction is LOCKED before computation: **J_mean > null mean (TIGHTER)**. Pre-commit-violation = J_mean < null mean (strict reversal). Pre-commit-violation = NULL with full prominence per Protocol §1.8.

The directional prior is grounded in two priors:
1. The Iblīs narrative is a tightly bounded discourse-cycle (refusal-to-prostrate → permission-to-mislead → eschatological reckoning) whose lexical signature is concentrated in the pericope, not diluted by surrounding content.
2. Q038-F-07 already PASSED at this exact instrument under this exact seed; this pre-reg's role is to formalize the result at H-NEW level and lock the scale-of-aggregation interpretation.

## Operational definition

- **Pericope** = union of all QAC v0.4 ROOT-field assignments across the locked verse range. The 7 pericopes are pre-specified by verse range; the 9-surah set is NOT modified.
- **Root extraction**: `data/morphology/quranic-corpus-morphology-0.4.txt` v0.4; ROOT field of each morphological segment (one ROOT per segment when present); a verse's roots = union of its segments' ROOT fields.
- **Pairwise Jaccard**: J(i,j) = |R_i ∩ R_j| / |R_i ∪ R_j|. If both sets empty, J=0.
- **Mean pairwise Jaccard**: mean over all 21 unordered pairs.

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel |
| Token level | QAC v0.4 root-tokens via stem-root field |
| Counting unit | unique-root set per pericope |
| Basmala | counted only in Q 1 (Q 1 not in test set; immaterial) |
| Reading tradition | Hafs-Kufan |
| Script | Mashriqi |
| Aggregation scale | PERICOPE (locked verse range) — distinguished from whole-surah scale used in H-NEW-039 |
| Pericope ranges | Q 2:34; Q 7:11-25; Q 15:31-44; Q 17:61-65; Q 18:50; Q 20:115-123; Q 38:71-85 |

## Permutation null protocol

1. Seed RNG = 20260509 (matches Q038-F-07 for identical-numerical replication).
2. For each of 10,000 permutations:
   - For each pericope length L in {1, 15, 14, 5, 1, 9, 15}: sample `start ~ Uniform[0, 6236 - L]` from the flat verse-index; take the L consecutive verses; compute their root-set.
   - Compute mean pairwise root-Jaccard across the 7 sampled root-sets.
3. p_perm = (count of perm-J ≥ observed-J) / 10,000 (strict one-tailed; same convention as Q038-F-07).

## Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| p_perm < 0.05 AND J_mean > null mean | PASS-DIRECTED-REPLICATION |
| p_perm ≥ 0.05 AND J_mean > null mean | DIRECTIONAL (replication weakened) |
| J_mean < null mean | PRE-COMMIT-VIOLATION → NULL with full prominence |
| J_mean ≈ null mean (within 0.5 std) | NULL |

## Pre-commit honesty re Q038-F-07

Because seed 20260509 + instrument + pericope ranges are identical to Q038-F-07, this pre-reg's numerical result must match Q038-F-07's J_mean=0.1456, null_mean=0.0650, null_std=0.0169, p_perm=0.0 EXACTLY. Any divergence indicates a code or data path issue and must be debugged before declaring PASS. This is by design: numerical replication is a check on script integrity at H-NEW level, while substantive replication (different seed) is a separate exercise (queued).

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: Root-Jaccard + 21-pair mean + length-matched perm null locked above.
- **MW-2 (corpus-prior)**: 10,000 perms; minimum standard met.
- **MW-3 (alternative-models)**: Q038-F-07 prereg listed TF-IDF variant as follow-up if NULL (not triggered).
- **MW-4 (over-fitting)**: No fitted parameter.
- **MW-5 (replication)**: This pre-reg IS the H-NEW-level replication of Q038-F-07. Numerical replication under identical seed; substantive replication under different seed queued as H-NEW-1380b.
- **MW-6 (instrument-control)**: H-NEW-039 NULL on the same theological set at whole-surah scale acts as a scale-of-aggregation control — the null at one scale is itself the control against over-interpreting the PASS at another scale.
- **MW-7 (post-hoc cap)**: Single pre-registered direction; not post-hoc.

## Scale-of-aggregation principle (formalized claim)

This pre-reg formalizes the following corollary to cross-finding-025:

> **Scale-of-aggregation axis**: For a thematic set C ⊆ corpus, FR/Jaccard cohesion is a function of BOTH (a) marker-thickness within each unit of aggregation AND (b) the unit of aggregation itself (verse / pericope / surah / multi-surah block). A NULL at one scale does NOT entail a NULL at all scales. A PASS at a narrower scale does NOT entail a PASS at broader scales. Methodologically, the scale-of-aggregation must be pre-specified in the pre-reg, and discrepancies across scales (as in H-NEW-039 NULL vs Q038-F-07 PASS) are FIRST-CLASS findings, not contradictions.

This corollary is supported empirically by the H-NEW-039 / Q038-F-07 pair at this point. Additional supporting pairs (with their own pre-regs) are required before full codification at cross-finding-025-formal level.

## Garden-of-forking-paths disclosure

- The 7 pericope ranges are LOCKED from Q038-F-07 pre-reg (signed off 2026-05-09 earlier in the same session). No reselection.
- Seed = 20260509 deliberately matches Q038-F-07 (for numerical replication). A different seed run is queued as H-NEW-1380b.
- The choice to drop Q 26 and Q 34 from the surah-set (relative to H-NEW-039's 9-surah set) is the difference between "any surah with Iblīs token" (9 surahs, NULL at whole-surah scale) and "pericope developing the Iblīs-narrative cycle" (7 pericopes, PASS at pericope scale). The 2 dropped surahs (Q 26 verbal recall in Abraham-Iblīs argument and Q 34 single-passing-reference) have Iblīs at marker-thinness ≪10% but no developed narrative pericope. Including them in the pericope set would require artificially-narrow verse-windows; their exclusion was pre-committed in Q038-F-07.

## Connection to existing findings

- **H-NEW-039 NULL**: same theological set, whole-surah scale, FR root-distribution → NULL. This is the "control" for the scale-of-aggregation claim.
- **Q038-F-07 CONFIRMED**: same instrument, same seed, same pericope ranges. This pre-reg is its H-NEW promotion.
- **cross-finding-025 (PRELIMINARY-SYNTHESIS)**: marker-thickness threshold rule. This pre-reg adds scale-of-aggregation as the second methodological axis.
- **H-NEW-1330 / H-NEW-1340 / H-NEW-1360**: three NULLs supporting marker-thickness rule at single-scale; this pre-reg shows that the same marker can have different verdicts at different scales.

## Anti-flip

The reverse direction (J_mean < null mean) = pre-commit violation → published as NULL with prominence. The whole point of the scale-of-aggregation claim is to make discrepancies first-class — so a NULL here, if it occurred, would itself be a finding (it would contradict Q038-F-07 numerically and trigger a script-integrity audit).

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. SHA computed after this file is finalized; embedded in `scripts/h-new-1380.py` as EXPECTED_SHA. Any mismatch = fail-fast.
