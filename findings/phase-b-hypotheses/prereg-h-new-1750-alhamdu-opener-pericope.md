---
id: H-NEW-1750
title: al-ḥamdu li-llāh opener-pericope flip-test (H-NEW-1340 NULL → ?)
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-1750-alhamdu-opener-pericope (single pre-registered test)
alpha_bon: 0.05
direction_of_effect: TIGHTER — mean pairwise root-Jaccard of the 5 al-ḥamdu li-llāh opener-pericope windows (first 3 verses of each of {Q 1, 6, 18, 34, 35}) is GREATER than the mean of 10,000 length-matched random opener-pericope draws sampled as the first 3 verses of randomly-chosen surahs (or, alternatively, of length-3 windows from the flat verse-index) — one-tailed permutation null.
origin: H-NEW-1340 (whole-surah Fisher-Rao cohesion of the 5-surah opener set {Q 1, 6, 18, 34, 35}) NULL'd at corpus baseline (Cell A uniform p = 0.7485; Cell B length-matched p = 0.4975; MW-5 PC valid at p = 0.0210). cross-finding-025-formal (2026-05-09 PM) established the pericope-scale flip law: 3 prior thin-marker NULLs at whole-surah scale (H-NEW-039 Iblīs, H-NEW-1330 sajda, H-NEW-1360 yā-ayyuhā al-nabī) all flipped to PASS-DIRECTED at pericope scale (H-NEW-1380, H-NEW-1510, H-NEW-1520). H-NEW-1340 is queued in cross-finding-025-formal §"What this means for the project" item 1 as the next target. This pre-reg locks the al-ḥamdu opener-pericope test.
verdict_ceiling: PASS-DIRECTED (single pre-registered test; INDEPENDENT REPLICATION required for CONFIRMED promotion — queued as H-NEW-1750b at a different seed if needed)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  detection_rule: opener-pericope = the first 3 verses of each cluster member
  root_source: data/morphology/quranic-corpus-morphology-0.4.txt
  null_model: 10,000 random draws of 5 length-3 windows from the flat verse-index (Q 1:1 .. Q 114:6); wraparound disallowed; window must not cross the last verse of the corpus
  cluster_definition: 5-surahs-with-opening-formula-al-hamdu-lillah {Q 1, 6, 18, 34, 35}
---

# H-NEW-1750 pre-registration — al-ḥamdu li-llāh opener-pericope flip-test

## Origin

H-NEW-1340 (2026-05-09) NULL'd the 5-surah al-ḥamdu li-llāh opener cluster {Q 1, 6, 18, 34, 35} at whole-surah Fisher-Rao root-distribution scale:

- Cell A (uniform null, 10000 perms, seed 20260509): obs 0.9902 vs null mean ~0.92, p = 0.7485 — cluster MORE typical than 75% of random 5-surah draws.
- Cell B (length-matched): p = 0.4975.
- MW-5 PC (H-NEW-1190 sub-sample): PASSED at p = 0.0210 — instrument validity confirmed; the surah-scale NULL is substantive.

H-NEW-1340 §"Honest limits" explicitly noted the thinness of the marker (a single phrase + 1-verse co-locator) and predicted under cross-finding-025 marker-thickness that pericope-scale should be tested separately.

cross-finding-025-formal (2026-05-09 PM, after H-NEW-1380 / H-NEW-1510 / H-NEW-1520) codifies the **pericope-scale flip law**: thin-marker whole-surah NULLs flip to PASS at pericope-scale under the SAME instrument (root-Jaccard, seed 20260509, 10000 perms). 3 of 3 thin-marker pairs flipped (Iblīs +4.76σ, sajda +2.685σ, prophet-vocative +6.41σ). The cross-finding-025-formal "What this means for the project" §item 1 lists H-NEW-1340 al-ḥamdu opener as the next queued target — explicitly naming "opener pericope = first 1-3 verses" as the operational unit.

This pre-reg locks the al-ḥamdu opener-pericope test at the 3-verse first-window granularity for direct comparability with the prior three pericope-flip tests (which used 3-verse windows centered on or starting at the marker-attestation).

## Hypothesis (single primary test)

**H1**: The 5 al-ḥamdu li-llāh opener-pericope windows — each the FIRST 3 VERSES of {Q 1, 6, 18, 34, 35} — exhibit TIGHTER mean pairwise root-Jaccard similarity than length-matched random 3-verse-window draws from the flat verse-index.

**5 opener-pericope windows (LOCKED)**:

| # | Surah | Opener verse | Window (first 3 verses) | Verse count of surah |
|:--|:--|:--|:--|:--|
| 1 | Q 1 al-Fātiḥa | 1 | Q 1:1-3 | 7 |
| 2 | Q 6 al-Anʿām | 1 | Q 6:1-3 | 165 |
| 3 | Q 18 al-Kahf | 1 | Q 18:1-3 | 110 |
| 4 | Q 34 Sabaʾ | 1 | Q 34:1-3 | 54 |
| 5 | Q 35 Fāṭir | 1 | Q 35:1-3 | 45 |

All 5 surahs have ≥3 verses; no truncation needed. Window lengths = [3, 3, 3, 3, 3].

**On Q 1's pericope content (locked):** Q 1's first 3 verses are (i) bi-smi llāhi al-raḥmāni al-raḥīm, (ii) al-ḥamdu li-llāhi rabbi al-ʿālamīn, (iii) al-raḥmāni al-raḥīm. Under the locked rules-tuple basmala-counted-only-in-Q1, Q 1:1 IS the basmala verse, which contains the basmala-roots (s-m-y, ʾ-l-h, r-ḥ-m). Q 1:3 repeats r-ḥ-m. This is the operationally correct "first-3-verses" of Q 1 under our basmala policy. For Q 6, Q 18, Q 34, Q 35, the basmala is NOT counted as a separate verse — so each surah's v 1 is its first content-bearing verse (the actual al-ḥamdu phrase). This asymmetry is INHERENT to the basmala policy locked in our rules-tuple; it is NOT a post-hoc choice. We do NOT normalize across surahs by, e.g., starting Q 1 at v 2.

**Test statistic**: mean of all C(5, 2) = 10 pairwise root-Jaccard values among the 5 opener-pericope window root-sets.

**Null distribution**: 10,000 random draws; for each of the 5 windows, draw a length-3 window from the flat verse-index (Q 1:1 .. Q 114:6 flattened to ~6,236 verses; window must not cross the last verse of the corpus); compute each window's root-set; compute the mean pairwise root-Jaccard over the 10 unordered pairs.

**Decision rule**: PASS-DIRECTED if p_perm < 0.05 AND direction matches lock (J_mean > null mean). Single test (k = 1); no Bonferroni adjustment.

## Direction lock

Direction is LOCKED before computation: **J_mean > null mean (TIGHTER)**. Pre-commit violation = J_mean < null mean (strict reversal). Pre-commit violation = NULL with full prominence per Protocol §1.8.

The directional prior is grounded in three reasons:

1. **Shared opening-formula roots**: ḥ-m-d (al-ḥamdu) + l-h-h (al-llāh) appear by construction in 5 of 5 openers. These two roots alone force a non-zero baseline pairwise Jaccard.
2. **Shared theological-cosmological vocabulary in 4 of 5**: Q 6, Q 18, Q 34, Q 35 all use *alladhī* + creation/possession/scripture-cosmology framing in v 1; the immediate post-opener vocabulary (s-m-w samāwāt, ʾ-r-ḍ arḍ, k-l-q khalaqa, l-l-h Allāh-pronoun-references) is highly likely to overlap. Q 1's v 2-3 use Allāh + rabb + ʿālamīn + raḥmān + raḥīm — partial overlap with the others' theological framing.
3. **cross-finding-025-formal triple-flip-confirmed pericope-scale law**: 3/3 prior thin-marker NULLs flipped to PASS at pericope-scale under the same instrument/seed/n_perm protocol. This pre-reg is the 4th independent test of that principle on a 4th thin-marker class (the al-ḥamdu opener). The principle predicts PASS; failure-to-flip would be the first non-flip and would refine the principle.

## Operational definition

- **Opener-pericope window** = the first 3 consecutive verses of each cluster-member surah. Per the basmala policy locked in our rules-tuple, Q 1:1 is the basmala-verse and Q 1:1-3 is therefore (basmala, ḥamd, raḥmān-raḥīm). For Q 6, 18, 34, 35, v 1 is the first content-bearing verse (the al-ḥamdu phrase itself); v 1-3 spans the opener phrase plus the two verses following.
- **Root extraction**: `data/morphology/quranic-corpus-morphology-0.4.txt` v0.4; ROOT field of each morphological segment (one ROOT per segment when present); a verse's roots = union of its segments' ROOT fields. Identical to H-NEW-1380 / H-NEW-1510 / H-NEW-1520's protocol.
- **Pairwise Jaccard**: J(i, j) = |R_i ∩ R_j| / |R_i ∪ R_j|. If both sets empty, J = 0.
- **Mean pairwise Jaccard**: mean over all 10 unordered pairs.

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel |
| Token level | QAC v0.4 root-tokens via ROOT field |
| Counting unit | unique-root set per opener-pericope window |
| Basmala | counted only in Q 1 (per default tuple) — Q 1's pericope therefore INCLUDES the basmala-verse |
| Reading tradition | Hafs-Kufan |
| Script | Mashriqi |
| Aggregation scale | PERICOPE-WINDOW (opener-pericope = first 3 verses of each surah) — distinguished from whole-surah scale used in H-NEW-1340 |
| Cluster definition | The 5 surahs whose opening formula is *al-ḥamdu li-llāh* — exactly {Q 1, 6, 18, 34, 35} per H-NEW-1340 pre-reg verbatim |
| Cluster size | 5 attestations across 5 distinct surahs |
| Window lengths | [3, 3, 3, 3, 3] — all 5 surahs have ≥3 verses, no truncation |

## Permutation null protocol

1. Seed RNG = 20260509 (matches H-NEW-1340, H-NEW-1380, H-NEW-1510, H-NEW-1520 — for cross-test seed-uniformity across the cross-finding-025-formal pericope-flip family).
2. For each of 10,000 permutations:
   - For each window length L in [3, 3, 3, 3, 3]: sample `start ~ Uniform[0, 6236 - L]` from the flat verse-index; take the L consecutive verses; compute their root-set.
   - Compute mean pairwise root-Jaccard across the 5 sampled root-sets (10 pairs).
3. p_perm = (count of perm-J ≥ observed-J) / 10,000 (strict one-tailed; same convention as H-NEW-1380 / H-NEW-1510 / H-NEW-1520).

## Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| p_perm < 0.05 AND J_mean > null mean | PASS-DIRECTED |
| p_perm ≥ 0.05 AND J_mean > null mean | DIRECTIONAL |
| J_mean < null mean (strict reversal) | PRE-COMMIT-VIOLATION → NULL with full prominence |
| J_mean ≈ null mean (within 0.5 std) | NULL |

## Cross-scale comparison embedded in output JSON

The output JSON will explicitly compare:

- **Whole-surah scale (H-NEW-1340 NULL)**: 5-surah set {Q 1, 6, 18, 34, 35}; obs intra-mean FR = 0.9902; Cell A p = 0.7485; Cell B p = 0.4975.
- **Opener-pericope scale (H-NEW-1750 this finding)**: 5 opener-pericope windows of length 3; J_mean = ?; null mean = ?; z = ?; p_perm = ?.

A FLIP (whole-surah NULL → opener-pericope PASS) replicates cross-finding-025-formal pericope-scale flip law on a 4th independent target set, taking the count to 4/4 supporting pairs. A NON-FLIP (both NULL) would be the first non-flip and would refine cross-finding-025-formal (the pericope-flip law would become marker-class-dependent, not universal).

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: Root-Jaccard + 10-pair mean + length-matched perm null locked above. Identical instrument to H-NEW-1380 / H-NEW-1510 / H-NEW-1520.
- **MW-2 (corpus-prior)**: 10,000 perms; minimum standard met.
- **MW-3 (alternative-models)**: Not applicable for the single primary test; if PASS-DIRECTED, an alternate-window-size sensitivity arm (window=1, window=5) is queued as H-NEW-1750-sens.
- **MW-4 (over-fitting)**: No fitted parameter. Window size = 3 verses is the default opener-pericope window per cross-finding-025-formal "What this means for the project" §item 1; not tuned on data.
- **MW-5 (replication)**: H-NEW-1340's MW-5 PC already established FR-instrument validity. For this pre-reg, the PC is implicit (H-NEW-1380, H-NEW-1510, H-NEW-1520 are the prior PCs at pericope scale on independent target sets). A different-seed replication is queued as H-NEW-1750b.
- **MW-6 (instrument-control)**: H-NEW-1340 NULL on the same theological set at whole-surah scale acts as the scale-of-aggregation control — the null at one scale is itself the control against over-interpreting a PASS at another scale.
- **MW-7 (post-hoc cap)**: Single pre-registered direction; not post-hoc. The prediction "thin-marker openers should cohere at pericope scale" was already codified at cross-finding-025-formal §"What this means for the project" §item 1 BEFORE this pre-reg was written.

## Garden-of-forking-paths disclosure

- The 5 cluster surahs are LOCKED at {Q 1, 6, 18, 34, 35} verbatim from H-NEW-1340 pre-reg. No re-selection.
- Window size = 3 verses is the default opener-pericope window per cross-finding-025-formal explicit naming. Alternatives (window = 1 or 5) are queued as H-NEW-1750-sens if PASS.
- The basmala-counted-only-in-Q1 policy means Q 1's first-3-verses pericope contains the basmala. This is the operationally-correct interpretation of the rules-tuple; we do NOT shift Q 1 to v 2-4 to "normalize" against the other 4 surahs. Doing so would be a post-hoc adjustment.
- Seed = 20260509 deliberately matches H-NEW-1340 / H-NEW-1380 / H-NEW-1510 / H-NEW-1520 (within-family consistency). A different-seed replication is queued.
- The choice of "length-3 random consecutive verses" as the null model — rather than "first 3 verses of randomly chosen surahs" — is the canonical pericope-null per H-NEW-1380 / H-NEW-1510 / H-NEW-1520. We retain it for cross-family comparability. A surah-opener-restricted null is queued as H-NEW-1750c if PASS, to control for opener-position effects.

## Connection to existing findings

- **H-NEW-1340 NULL** (whole-surah FR on the same 5-surah set): the control that this pre-reg flips. cross-finding-025-formal item 1.
- **H-NEW-1380, H-NEW-1510, H-NEW-1520**: the three prior pericope-flips. This pre-reg is the 4th independent test of the cross-finding-025-formal pericope-scale flip law.
- **cross-finding-025-formal (2026-05-09 PM)**: codifies the pericope-scale flip law. This pre-reg is item 1 of the §"What this means for the project" queue.
- **H-NEW-74** (5 qul-opener surahs FR-cohesive at whole-surah scale): an opener-class that DID cohere at whole-surah scale; this is the contrast case. al-ḥamdu opener is "thinner" than qul opener (qul is a 1-word imperative that lexically uniformly marks DIRECT-DIVINE-SPEECH; al-ḥamdu is a 2-word formula + variable content-completion).
- **H-NEW-89** (Q 1 sui-generis / cluster-isolated): Q 1's mean FR to corpus ≈ 1.0; its inclusion in the 5-surah cluster may PULL the mean DOWNWARD at pericope-scale (because Q 1's v 1-3 is more thematically distinct), or UPWARD (because the basmala-verse + ḥamd-verse + raḥmān-raḥīm-verse contain the canonical opener-roots ḥ-m-d, l-h-h, r-ḥ-m, plus rabb + ʿālamīn — overlap-rich with the other 4 openers).

## Anti-flip

The reverse direction (J_mean < null mean, strict) = pre-commit violation → published as NULL with prominence. Even a clean NULL (J_mean ≈ null mean) is a substantive finding: it would mean the al-ḥamdu opener is the FIRST exception to the pericope-scale flip law, refining cross-finding-025-formal into a marker-class-dependent rule.

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. SHA computed after this file is finalized; embedded in `scripts/h-new-1750.py` as EXPECTED_SHA. Any mismatch = fail-fast.
