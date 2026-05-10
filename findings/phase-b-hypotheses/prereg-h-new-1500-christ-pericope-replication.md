---
id: H-NEW-1500
title: Christ-narrative pericope-scale flip test for H-NEW-1310 NULL — 9-pericope root-Jaccard cohesion
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-1500-christ-pericope-replication (single pre-registered test)
alpha_bon: 0.05
direction_of_effect: TIGHTER — mean pairwise root-Jaccard of the 9 Christ-narrative pericopes is GREATER than the mean of 10,000 length-matched random-pericope draws (one-tailed permutation null); equivalently, observed J_mean > 95th-percentile of the length-matched null
origin: H-NEW-1310 (2026-05-09 morning) NULLed the Christ-narrative {Q 3, Q 5, Q 19} cluster at whole-surah Fisher-Rao root-distribution scale (Cell A uniform p=0.481; Cell B length-matched p=0.187; PC sub-sample {Q 69, 97, 101} valid at p=0.041). H-NEW-1380 (2026-05-09 PM) demonstrated that the Iblīs-narrative cluster NULLs at whole-surah FR scale (H-NEW-039 p=0.537) but PASSes at pericope scale (z=+4.76, p≤10⁻⁴). This pre-reg applies the H-NEW-1380 scale-of-aggregation principle (cross-finding-025 corollary, MASTER-LEDGER §10.51) to the Christ-narrative set: re-test the same theological cluster at pericope scale with the same Q038-F-07/H-NEW-1380 instrument.
verdict_ceiling: PASS-DIRECTED (if pericope J_mean > 95th-pctile null and direction matches lock) → NULL-AT-PERICOPE-SCALE (if NULL holds across scales — Christ-narrative differs from Iblīs-narrative on the scale-of-aggregation axis)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  detection_rule: pericope = union of QAC v0.4 ROOT-field assignments across verses in the locked range
  root_source: data/morphology/quranic-corpus-morphology-0.4.txt
  null_model: 10,000 random draws of 9 length-matched pericopes from the flat verse-index (verse-counts 31, 26, 18, 1, 3, 4, 12, 25, 6), wraparound disallowed
---

# H-NEW-1500 pre-registration — Christ-narrative pericope-scale flip test

## Origin

H-NEW-1310 NULLed the Christ-narrative {Q 3, Q 5, Q 19} cluster at whole-surah FR (MASTER-LEDGER §10.44.7):
- Cell A uniform p=0.481
- Cell B length-matched p=0.187
- PC sub-sample {Q 69, 97, 101} valid at p=0.041 (MW-5 PASSED)
- Substantive verdict: Q 3↔Q 5 sub-pair (FR=0.698) is real but driven by long-Medinan jurisprudence, not Christ-narrative; Q 19 isolated by prophet-cycle catalog.

H-NEW-1380 (MASTER-LEDGER §10.51) established the scale-of-aggregation principle as a methodological axis under cross-finding-025: a theological set may NULL at whole-surah scale and PASS at pericope scale. The Iblīs-narrative is the seed pair (H-NEW-039 NULL at whole-surah; H-NEW-1380/Q038-F-07 PASS at pericope, z=+4.76).

Section §10.51.3 of MASTER-LEDGER explicitly lists the Christ-narrative re-test as the FIRST queued candidate:
> H-NEW-1310 (Christ-narrative {Q 3, 5, 19}) — re-test as Christ-pericope-set {Q 3:42-63 + Q 5:110-118 + Q 19:1-37}.

This pre-reg widens the queued pericope set to the FULL Christological-discourse inventory across the corpus (including Q 4) verified by direct grep of the canonical Arabic surface-forms عيسى / مريم / مسيح / حواري / انجيل over `quran-text/quran-no-tashkeel.json`. The widened set is methodologically more defensible than the §10.51.3 sketch (which omitted Q 4:155-172, the longest single Christological pericope in the Quran) and is fully pre-committed below.

## Hypothesis (single primary test)

**H1**: The 9 Christ-narrative pericopes — Q 3:33-63, Q 3:64-89, Q 4:155-172, Q 5:17, Q 5:46-48, Q 5:72-75, Q 5:109-120, Q 19:16-40, Q 19:88-93 — exhibit TIGHTER mean pairwise root-Jaccard similarity than length-matched random-pericope draws.

**Test statistic**: mean of all C(9,2)=36 pairwise root-Jaccard values among the 9 pericope root-sets.

**Null distribution**: 10,000 random draws; for each of the 9 pericope lengths {31, 26, 18, 1, 3, 4, 12, 25, 6} verses, draw a random start index from the flat verse-index (6,236 verses minus L+1) and take the L consecutive verses; compute the pericope's root-set; repeat for all 9 lengths; compute the mean pairwise root-Jaccard.

**Decision rule**: PASS if p_perm < 0.05 AND direction matches lock (J_mean > null mean). Single test (k=1); no Bonferroni adjustment.

## Direction lock

Direction is LOCKED before computation: **J_mean > null mean (TIGHTER)**. Pre-commit-violation = J_mean < null mean (strict reversal). Pre-commit-violation = NULL with full prominence per Protocol §1.8.

The directional prior is grounded in three priors:
1. The Christ-narrative cycle has a tightly-bounded discourse-cycle (Maryam-birth → ʿĪsā-birth → ḥawāriyyīn-table → Trinitarian-rejection) whose lexical signature should concentrate at pericope scale.
2. The cycle has TWO bounded proper-name attractors (Maryam, ʿĪsā) and one bounded title (Masīḥ) and one bounded sociological term (ḥawāriyyīn) — all four are concentrated within the 9 pericopes by construction (verified via grep below).
3. H-NEW-1380 demonstrated this exact flip mechanism (whole-surah NULL → pericope PASS, z=+4.76) on the Iblīs-narrative. The directional prior here is that the Christ-narrative behaves like the Iblīs-narrative.

The alternative (no flip → NULL holds across scales) would itself be a first-class finding: it would show that the scale-of-aggregation axis is itself thematically conditional, not universal. Per §10.51.3, 2+ flips out of the 4 queued candidates {Christ, sajda, al-ḥamdu, *yā-ayyuhā al-nabī*} graduate cross-finding-025 from PRELIMINARY-SYNTHESIS.

## Operational definition

- **Pericope** = union of all QAC v0.4 ROOT-field assignments across the locked verse range. The 9 pericopes are pre-specified by verse range below; the {Q 3, Q 4, Q 5, Q 19} surah-set is NOT modified post-observation.
- **Root extraction**: `data/morphology/quranic-corpus-morphology-0.4.txt` v0.4; ROOT field of each morphological segment (one ROOT per segment when present); a verse's roots = union of its segments' ROOT fields.
- **Pairwise Jaccard**: J(i,j) = |R_i ∩ R_j| / |R_i ∪ R_j|. If both sets empty, J=0.
- **Mean pairwise Jaccard**: mean over all 36 unordered pairs.

## Locked pericope inventory (verified by direct grep)

| # | Pericope | Verses | Length | Anchor terms verified by grep |
|:--|:--|:--|:--|:--|
| 1 | Q 3:33-63 | 33–63 | 31 | maryam[36,37,42,43,44,45]; ʿīsā[45,52,55,59]; masīḥ[45]; ḥawārī[52] — Maryam-birth + ʿĪsā-birth + ḥawāriyyīn |
| 2 | Q 3:64-89 | 64–89 | 26 | ʿīsā[84] — Q 3 polemic against Christological claims (People-of-the-Book disputation) |
| 3 | Q 4:155-172 | 155–172 | 18 | ʿīsā[157,163,171]; maryam[156,157,171]; masīḥ[157,171,172] — Jewish-rejection of ʿĪsā + Christological clarifications + denial of ittakhadha-walad |
| 4 | Q 5:17 | 17 | 1 | masīḥ[17]; maryam[17] — Christological response (Allāh ≠ al-Masīḥ ibn Maryam) |
| 5 | Q 5:46-48 | 46–48 | 3 | ʿīsā[46]; maryam[46] — Injīl-revelation passage |
| 6 | Q 5:72-75 | 72–75 | 4 | masīḥ[72,75]; maryam[72,75] — Trinitarian rejection (kufru alladhīna qālū inna Allāha huwa al-Masīḥ ibn Maryam) |
| 7 | Q 5:109-120 | 109–120 | 12 | ʿīsā[110,112,114,116]; maryam[110,112,114,116]; ḥawārī[111,112] — ḥawāriyyīn-table + ʿĪsā's final response |
| 8 | Q 19:16-40 | 16–40 | 25 | maryam[16,27,34]; ʿīsā[34] — Maryam pericope + ʿĪsā cradle-speech |
| 9 | Q 19:88-93 | 88–93 | 6 | denial of ittakhadha al-raḥmān waladā (Q 19:88: *wa-qālū ittakhadha al-raḥmān waladā*); Christological-by-content (no proper-name carrier — the densest *walad*-denial in the corpus) |

Total verses: 126.
Total surahs spanned: 4 (Q 3, Q 4, Q 5, Q 19) — three Medinan + one Meccan; H-NEW-1310's {Q 3, Q 5, Q 19} surah-set is REPLACED here by the four-surah set {Q 3, Q 4, Q 5, Q 19} because the Q 4:155-172 Christological clarifications pericope (the longest single Christological discourse-unit in the Quran) is a load-bearing structural pericope.

The 9-pericope inventory is LOCKED in this pre-reg; no re-selection post-observation.

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel |
| Token level | QAC v0.4 root-tokens via ROOT field |
| Counting unit | unique-root set per pericope |
| Basmala | counted only in Q 1 (Q 1 not in test set; immaterial) |
| Reading tradition | Hafs-Kufan |
| Script | Mashriqi |
| Aggregation scale | PERICOPE (locked verse range) — distinguished from whole-surah scale used in H-NEW-1310 |
| Pericope ranges | Q 3:33-63; Q 3:64-89; Q 4:155-172; Q 5:17; Q 5:46-48; Q 5:72-75; Q 5:109-120; Q 19:16-40; Q 19:88-93 |

## Permutation null protocol

1. Seed RNG = 20260509 (matches Q038-F-07 / H-NEW-1380 for instrument-uniformity across the scale-of-aggregation queued re-test family).
2. For each of 10,000 permutations:
   - For each pericope length L in {31, 26, 18, 1, 3, 4, 12, 25, 6}: sample `start ~ Uniform[0, 6236 - L]` from the flat verse-index; take the L consecutive verses; compute their root-set.
   - Compute mean pairwise root-Jaccard across the 9 sampled root-sets.
3. p_perm = (count of perm-J ≥ observed-J) / 10,000 (strict one-tailed; same convention as H-NEW-1380 and Q038-F-07).

## Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| p_perm < 0.05 AND J_mean > null mean | PASS-DIRECTED (Christ-narrative flips NULL→PASS at pericope scale) |
| p_perm ≥ 0.05 AND J_mean > null mean | DIRECTIONAL (Christ-narrative trends tighter but not significant) |
| J_mean < null mean | PRE-COMMIT-VIOLATION → NULL with full prominence |
| J_mean ≈ null mean (within 0.5 std) | NULL-AT-PERICOPE-SCALE (Christ-narrative differs from Iblīs-narrative on scale-of-aggregation axis) |

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: Root-Jaccard + 36-pair mean + length-matched perm null locked above. Instrument identical to Q038-F-07 / H-NEW-1380; this is what makes cross-set comparison meaningful.
- **MW-2 (corpus-prior)**: 10,000 perms; minimum standard met.
- **MW-3 (alternative-models)**: H-NEW-1310's whole-surah FR is itself the alternative-aggregation-scale model; relationship between scales is the substantive interest.
- **MW-4 (over-fitting)**: No fitted parameter.
- **MW-5 (replication)**: H-NEW-1310 NULL at whole-surah scale is the cross-scale replication baseline. Same theological set, different instrument and scale.
- **MW-6 (instrument-control)**: H-NEW-1380's pericope-scale PASS on a DIFFERENT theological set (Iblīs) controls the pericope-instrument against the suspicion that pericope-scale will always PASS — if Christ-narrative NULLs at pericope scale even though Iblīs-narrative PASSes, the instrument is differential.
- **MW-7 (post-hoc cap)**: Single pre-registered direction; not post-hoc. The pericope set is locked from §10.51.3 + grep verification, not from result-peeking.

## Scale-of-aggregation principle (this is the test of the principle)

This pre-reg is the FIRST queued re-test under MASTER-LEDGER §10.51.3 / cross-finding-025 second methodological axis. Per §10.51.3:

> If 2 or more of these flip from NULL to PASS at pericope-scale, cross-finding-025-formal gains its replication-cluster set and graduates from PRELIMINARY-SYNTHESIS.

This test counts as 1 of the 2+ required for graduation. Outcome:
- PASS-DIRECTED here = 1 confirmed flip toward 2-flip graduation
- NULL-AT-PERICOPE-SCALE here = first counter-example to the scale-of-aggregation axis being universal; cross-finding-025 retains thematic-conditionality

Both outcomes are first-class findings.

## Garden-of-forking-paths disclosure

- The 9 pericope ranges were drawn from MASTER-LEDGER §10.51.3 (which sketched Q 3:42-63 + Q 5:110-118 + Q 19:1-37) and widened by direct grep over `quran-text/quran-no-tashkeel.json` for the canonical Arabic surface-forms {عيسى, مريم, مسيح, حواري, انجيل}. The widening from 3 to 9 pericopes is justified by: (a) including the structurally load-bearing Q 4:155-172 Christological clarifications, omitted from the §10.51.3 sketch; (b) splitting Q 3 into Maryam/ʿĪsā-narrative (33-63) and Christological-polemic (64-89) sub-pericopes because they are textual-form distinct; (c) splitting Q 5 into four pericopes (17, 46-48, 72-75, 109-120) per natural discourse boundaries with the proper-name attestations; (d) adding Q 19:88-93 walad-denial pericope as Christological-by-content even though no proper-name carrier appears.
- All splits are LOCKED before computation. No verse-range reselection post-observation.
- Seed = 20260509 deliberately matches H-NEW-1380 for instrument-uniformity. A different-seed run is queued as H-NEW-1500b for genuine seed-independent replication.
- The 4-surah set {Q 3, Q 4, Q 5, Q 19} differs from H-NEW-1310's 3-surah set {Q 3, Q 5, Q 19} by addition of Q 4. This is documented in the pre-reg (above) as a structural inclusion of the Q 4 Christological pericope, NOT a post-hoc add to chase signal.

## Connection to existing findings

- **H-NEW-1310 NULL** (MASTER-LEDGER §10.44.7): same theological-set core ({Q 3, Q 5, Q 19}), whole-surah FR root-distribution → NULL. This is the cross-scale baseline.
- **H-NEW-1380 PASS-DIRECTED-REPLICATION** (MASTER-LEDGER §10.51): same instrument (root-Jaccard pericope-scale), same seed (20260509), on a DIFFERENT theological set (Iblīs-narrative). This established the scale-of-aggregation principle and queued the Christ-narrative re-test.
- **cross-finding-025** (PRELIMINARY-SYNTHESIS): marker-thickness × scale-of-aggregation joint axis. This test is one of 4 queued re-tests under the scale-of-aggregation principle.
- **H-NEW-039 NULL**: Iblīs whole-surah NULL — pairs with H-NEW-1380 on Iblīs-narrative cycle; structural analog of H-NEW-1310 NULL ↔ H-NEW-1500 on Christ-narrative cycle.

## Anti-flip

The reverse direction (J_mean < null mean) = pre-commit violation → published as NULL with prominence. A pre-commit violation would itself be a finding: it would indicate the Christ-narrative pericopes are LESS internally cohesive than length-matched random pericopes, which would mean the cycle's lexicon is so dispersive (Maryam in Q 3:36-44 birth-stratum vs ḥawāriyyīn in Q 5:111-112 table-stratum vs walad-denial in Q 19:88-93) that the cycle is not a single root-vocabulary cluster but a discourse-cluster organized at a different linguistic level.

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. SHA computed after this file is finalized; embedded in `scripts/h-new-1500.py` as EXPECTED_SHA. Any mismatch = fail-fast.
