---
id: H-NEW-1500
title: Christ-narrative pericope-scale flip — H-NEW-1310 NULL flips to PASS-DIRECTED at pericope scale (z=+4.25, p≤10⁻⁴)
date: 2026-05-09
status: PASS-DIRECTED
verdict: PASS-DIRECTED (Christ-narrative root-Jaccard cohesion z=+4.25; corpus-extreme at pericope scale; second confirming finding-pair for scale-of-aggregation axis under cross-finding-025)
direction_lock: TIGHTER (J_mean > null_mean)
direction_match: TRUE
pre_commit_violation: FALSE
pre_reg_sha: 74626141b16e345be4ec5feb35b8217b92423afbe0a6432e1d885cb31e95bea7
seed: 20260509
n_perm: 10000
bonferroni_k: 1
alpha_bon: 0.05
rules_tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
aggregation_scale: PERICOPE (locked verse range)
---

# H-NEW-1500 — Christ-narrative pericope-scale flip test for H-NEW-1310 NULL


> ## ⛔ CORRECTION NOTICE — 2026-08-07
>
> **This finding's own numbers reproduce exactly and are not retracted.** What was corrected is the
> law it feeds. Under the project's first genre control (`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`), the
> pericope-flip test applied to five best-shot marker classes flips **5/5 on pre-Islamic poetry and
> 4/5 on al-Bukhārī** — length-matched 114-block partitions, instrument-matched pipeline. The
> mechanism is topical burstiness, which every text has and which this project already identified
> (H-NEW-2330). The statistic is additionally **invariant under every redactional randomisation**
> (marker labels, reading order, titles — verified 25/25), so it carries no weight in any conjunction
> of the pillar laws.
>
> **The pericope-scale rule remains correct methodology** — a whole-surah NULL is not a terminal
> verdict, and re-testing at the scale where structure operates is still project discipline.
> **What must stop is citing a flip as evidence that this corpus is structurally unusual.**
> Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


## Headline

The 9 Christ-narrative pericopes (Q 3:33-63, Q 3:64-89, Q 4:155-172, Q 5:17, Q 5:46-48, Q 5:72-75, Q 5:109-120, Q 19:16-40, Q 19:88-93) exhibit mean pairwise root-Jaccard **J_mean = 0.156031** against a length-matched null mean of **0.085168 ± 0.016671** (10,000 permutations, seed 20260509). The observed value sits at **z = +4.25** with strict one-tailed permutation **p = 0.0001** (1 of 10,000 perms ≥ observed; reportable upper bound ≤ 10⁻⁴ at this resolution).

**Flip verdict: NULL → PASS-DIRECTED.** The Christ-narrative cluster, which NULLed at whole-surah scale in H-NEW-1310 (Cell A uniform p=0.481; Cell B length-matched p=0.187; PC sub-sample valid at p=0.041), passes at pericope scale at corpus-extreme magnitude. This is the second confirming finding-pair for the scale-of-aggregation axis under cross-finding-025 (the first being the Iblīs-narrative H-NEW-039 NULL ↔ H-NEW-1380 PASS at z=+4.76).

## Pre-registered design

Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-1500-christ-pericope-replication.md` (SHA256 `74626141b16e345be4ec5feb35b8217b92423afbe0a6432e1d885cb31e95bea7`). Direction LOCKED before computation: J_mean > null_mean (TIGHTER). The 9 pericope ranges were locked from MASTER-LEDGER §10.51.3 (which had sketched 3 narrower pericopes) widened by direct grep of the canonical Arabic surface-forms {عيسى, مريم, مسيح, حواري, انجيل} over `quran-text/quran-no-tashkeel.json`. The widening to 9 was pre-committed (not post-hoc), with the justification documented in the pre-reg's garden-of-forking-paths disclosure.

| # | Pericope | Verses | L | Unique roots | Anchor terms (grep-verified) |
|:--|:--|:--|:--|:--|:--|
| 1 | Q 3:33-63 | 33–63 | 31 | 151 | maryam[36,37,42,43,44,45]; ʿīsā[45,52,55,59]; masīḥ[45]; ḥawārī[52] |
| 2 | Q 3:64-89 | 64–89 | 26 | 115 | ʿīsā[84]; Christological-polemic discourse |
| 3 | Q 4:155-172 | 155–172 | 18 | 101 | ʿīsā[157,163,171]; maryam[156,157,171]; masīḥ[157,171,172] |
| 4 | Q 5:17 | 17 | 1 | 16 | masīḥ[17]; maryam[17] |
| 5 | Q 5:46-48 | 46–48 | 3 | 37 | ʿīsā[46]; maryam[46]; injīl |
| 6 | Q 5:72-75 | 72–75 | 4 | 36 | masīḥ[72,75]; maryam[72,75] |
| 7 | Q 5:109-120 | 109–120 | 12 | 92 | ʿīsā[110,112,114,116]; maryam[110,112,114,116]; ḥawārī[111,112] |
| 8 | Q 19:16-40 | 16–40 | 25 | 107 | maryam[16,27,34]; ʿīsā[34] |
| 9 | Q 19:88-93 | 88–93 | 6 | 20 | walad-denial pericope (Christological-by-content) |

Total verses: 126. Total surahs spanned: 4 (Q 3 Medinan, Q 4 Medinan, Q 5 Medinan, Q 19 Meccan).

## Result

| Quantity | Value |
|:--|:--|
| Observed mean pairwise Jaccard (36 pairs) | **0.156031** |
| Null mean (10,000 length-matched perms) | 0.085168 |
| Null std | 0.016671 |
| Null 95th percentile | 0.113972 |
| z-score | **+4.251** |
| p_perm (strict, one-tailed, ≥ obs) | **0.0001** (1/10000) |
| Reportable upper bound | ≤ 10⁻⁴ |
| Direction match | TRUE (J_obs > null_mean ✓) |
| Verdict | **PASS-DIRECTED** |
| Flip verdict | **NULL → PASS** (Christ-narrative flips at pericope scale) |

## Per-pair structure

The 36 pairwise Jaccards span 0.049–0.321, mean 0.156. The TIGHTEST pairs are the inter-surah ḥawāriyyīn-bridges and the intra-Q3 narrative-polemic pair:

| Rank | Pair | J | Inter / Union |
|:--|:--|:--|:--|
| 1 | Q 3:33-63 ↔ Q 5:109-120 | **0.321** | 59 / 184 |
| 2 | Q 3:64-89 ↔ Q 4:155-172 | 0.301 | 50 / 166 |
| 3 | Q 3:64-89 ↔ Q 5:109-120 | 0.286 | 46 / 161 |
| 4 | Q 3:33-63 ↔ Q 3:64-89 | 0.273 | 57 / 209 |
| 5 | Q 3:33-63 ↔ Q 4:155-172 | 0.273 | 54 / 198 |
| 6 | Q 4:155-172 ↔ Q 5:109-120 | 0.270 | 41 / 152 |

The Q 3:33-63 ↔ Q 5:109-120 pair (J=0.321) is the densest cross-surah root-overlap between the Maryam-birth+ʿĪsā-birth+ḥawāriyyīn opening (Q 3) and the ḥawāriyyīn-table+ʿĪsā's-final-response closer (Q 5) — both share the *byn / ʾtw / qwl / Eyy / mry / ḥwr / Allāh / qdr / ʿbd* root-stratum.

The LOOSEST pairs all involve the short walad-denial pericope Q 19:88-93 (the only Christological-by-content pericope without a proper-name carrier):

| Pair | J |
|:--|:--|
| Q 4:155-172 ↔ Q 19:88-93 | 0.071 |
| Q 5:17 ↔ Q 19:16-40 | 0.070 |
| Q 3:33-63 ↔ Q 5:17 | 0.064 |
| Q 5:72-75 ↔ Q 19:88-93 | 0.057 |
| Q 3:33-63 ↔ Q 19:88-93 | 0.049 |

The walad-denial pericope's lexicon (centered on *rḥmn / wld / ittakhadha / smwt / ʾrḍ / Edd*) is content-cohesive on Trinitarian denial but lexically distinct from the proper-name-carrying narrative pericopes. Even so, the headline mean is dominated by the 6 high-overlap pairs (J≥0.27) plus moderate tails.

## Comparison to H-NEW-1310 (whole-surah scale)

| Axis | H-NEW-1310 (whole-surah) | H-NEW-1500 (pericope) |
|:--|:--|:--|
| Set | {Q 3, Q 5, Q 19} surahs | 9 Christ-narrative pericopes across {Q 3, Q 4, Q 5, Q 19} |
| Instrument | Fisher-Rao on root-distribution | root-Jaccard on root-set |
| Aggregation | full surah | pericope (locked verse range) |
| Cell A (uniform) | p=0.481 | — |
| Cell B (length-matched) | p=0.187 | **p=0.0001** |
| z | ~0.9 (cell A) | **+4.25** |
| Verdict | NULL (with PC sub-sample MW-5 valid at p=0.041) | **PASS-DIRECTED** |
| Effect direction | Toward cohesion but weak | **Corpus-extreme cohesion** |

The whole-surah NULL is genuine — the Christ-narrative content is diluted across long-Medinan surahs (Q 3 has 200 verses, Q 4 has 176 verses, Q 5 has 120 verses) whose jurisprudential / political-community content overwhelms the proportionally-small Christological pericopes. The pericope-scale signal, by contrast, isolates the Christological lexicon and reveals corpus-extreme cohesion.

## Comparison to H-NEW-1380 (Iblīs-narrative — first finding-pair under scale-of-aggregation axis)

| Cluster | Whole-surah | Pericope | z (pericope) | Flip verdict |
|:--|:--|:--|:--|:--|
| **Iblīs-narrative** (H-NEW-039 ↔ H-NEW-1380) | NULL (p=0.537) | PASS (p≤10⁻⁴) | **+4.76** | NULL→PASS ✓ |
| **Christ-narrative** (H-NEW-1310 ↔ H-NEW-1500, THIS finding) | NULL (cell-B p=0.187) | PASS (p≤10⁻⁴) | **+4.25** | NULL→PASS ✓ |

Both clusters show the same pattern: NULL at whole-surah scale and PASS at pericope scale at z-scores around +4.5. This is the second confirming finding-pair under the scale-of-aggregation axis (cross-finding-025 second methodological axis, per MASTER-LEDGER §10.51).

Per §10.51.3:
> If 2 or more of these flip from NULL to PASS at pericope-scale, cross-finding-025-formal gains its replication-cluster set and graduates from PRELIMINARY-SYNTHESIS.

**This finding satisfies the 2-flip graduation criterion.** Cross-finding-025-formal can now graduate from PRELIMINARY-SYNTHESIS to CONFIRMED (or an interim level pending the other 2 queued re-tests for additional power).

## Theoretical implication: the Christ-narrative is a true root-coherent textual cycle at pericope scale

The Christ-narrative is a tightly bounded discourse-cycle in the Quran with at least four lexical attractors:
- *mry* (root for Maryam) — concentrated in 7 of 9 pericopes
- *Eyy* (root for ʿĪsā) — concentrated in 7 of 9 pericopes
- *msḥ* (root for al-Masīḥ) — in 4 of 9 pericopes
- *ḥwr* (root for ḥawāriyyīn) — in 2 of 9 pericopes (Q 3:33-63, Q 5:109-120)

Plus the secondary stratum: *byn ʾḥd* (Trinitarian denial), *wld* (walad-denial), *rwḥ* (ruḥ al-qudus), *rbb* (lord-relation), *qlb* (heart-discourse), *ʿbd* (servanthood), *Aʾl* (god/family-of-ʿImrān).

This four-attractor lexical concentration is precisely what root-Jaccard at pericope scale detects, and which whole-surah FR root-distribution dilutes. The classical commentators have long noted the Christ-narrative as a recurrent rhetorical cycle (e.g., al-Rāzī *Mafātīḥ al-ghayb* on Q 3:42-47 explicitly cross-references Q 19:16-22 and Q 5:110; al-Biqāʿī *Naẓm al-durar* treats the cycle as a deliberate textual-recurrence). The empirical result quantitatively supports the classical reading at corpus-extreme magnitude, with the methodological clarification that the correct unit-of-aggregation is the PERICOPE, not the SURAH.

## Classical context

al-Rāzī (*Mafātīḥ al-ghayb*, commentary on Q 3:42, Q 5:110, Q 19:16-22) explicitly treats the Christ-narrative as a single rhetorical cycle recurring across three principal surah-locations with characteristic lexicon (*idhā / qālat / al-rūḥ / waḍaʿtu / al-masīḥ / al-ḥawāriyyīn*).

al-Biqāʿī (*Naẓm al-durar*) treats Q 3, Q 5, Q 19 as cross-linked Christological discourses, with Q 19 establishing the prophetic-genealogical frame (Zakariyyāʾ → Yaḥyā → Maryam → ʿĪsā), Q 3 establishing the kalāmic-juridical frame (āl-ʿImrān → Maryam → ʿĪsā → ḥawāriyyīn → polemic), and Q 5 establishing the eschatological-final-response frame (mā idhdh-tu lahum illā mā amartanī bih).

al-Suyūṭī (*al-Itqān*, nawʿ 49 *fī tanāsub al-āyāt wa-l-suwar*) treats inter-surah narrative-recurrence as a deliberate compositional feature. H-NEW-1500 provides quantitative correlate: the Christ-narrative recurrence-cycle is corpus-extreme on root-Jaccard cohesion at pericope scale (z=+4.25) — second only to the Iblīs-narrative cycle (z=+4.76) among tested narrative cycles to date.

## Honest limits

- **Seed 20260509 is shared with H-NEW-1380** (instrument-uniformity across the scale-of-aggregation queued re-test family). A different-seed run is queued as **H-NEW-1500b** for genuine seed-independent replication.
- **Pericope boundaries are interpretive**. The 9 ranges are LOCKED in the pre-reg from §10.51.3 + grep verification, but ±2-verse boundary sensitivity is queued.
- **Length-matched null does not control for prose-type** (narrative vs polemic vs eschatological). A prose-type-matched null is a follow-up.
- **The 4-surah set {Q 3, Q 4, Q 5, Q 19} widens H-NEW-1310's 3-surah set** by adding Q 4. This is pre-committed and justified structurally (Q 4:155-172 is the longest single Christological pericope), but the inclusion of Q 4 is the most defensible single methodological decision in this pre-reg. A sensitivity test excluding Q 4 is queued.
- **No independence of pericope-attestations**: the 9 pericopes are not independent draws — they are constrained by the textual structure of the Quran. The null model controls for surface-length but not for textual-clustering.
- **Single-seed numerical result; no LOOCV**. The high z-score (+4.25) with 1/10,000 perms ≥ obs is robust to single-seed variation only by analogy to H-NEW-1380's identical-seed numerical replication; a seed-sensitivity sweep (10 seeds × 10K perms each) is queued.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-1500-christ-pericope-replication.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-1500.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-1500.json`
- finding: `findings/phase-b-hypotheses/h-new-1500-christ-pericope-replication.md` (this file)

## Connection to existing findings

- **H-NEW-1310 NULL** (MASTER-LEDGER §10.44.7): same theological-set core, whole-surah FR root-distribution → NULL. Inverted at pericope scale.
- **H-NEW-1380 PASS-DIRECTED-REPLICATION** (MASTER-LEDGER §10.51): same instrument, same seed, different theological set (Iblīs). Sister finding-pair.
- **H-NEW-039 NULL**: whole-surah baseline for Iblīs. Pairs with H-NEW-1380. Structural analog of H-NEW-1310 NULL ↔ H-NEW-1500.
- **cross-finding-025** (PRELIMINARY-SYNTHESIS): scale-of-aggregation axis is the second methodological axis. H-NEW-1500 is the second confirming finding-pair; cross-finding-025-formal can now graduate.
- **MASTER-LEDGER §10.51.3 queue**: H-NEW-1500 satisfies the FIRST queued re-test (Christ-narrative). Three remaining: H-NEW-1330 sajda, H-NEW-1340 al-ḥamdu, H-NEW-1360 *yā-ayyuhā al-nabī*.

## Predictions for the remaining 3 queued re-tests

Based on the marker-thickness × scale-of-aggregation joint axis (cross-finding-025):
- **H-NEW-1330 sajda** (14 sajda-verse-pericopes, ±2-verse windows): PREDICT NULL — the sajda marker is a single-verse ritual cue, not a discourse-cycle; pericope-widening to ±2 verses incorporates incongruent surrounding content.
- **H-NEW-1340 al-ḥamdu li-llāh opener** (5 opener-pericopes): PREDICT DIRECTIONAL or weak PASS — opener-pericopes share a few liturgical roots but otherwise diverge into surah-specific content.
- **H-NEW-1360 *yā-ayyuhā al-nabī*** (13 vocative-attestation verses ± context): PREDICT NULL or weak DIRECTIONAL — the vocative is a discourse marker not a content marker; the divergent sub-region structure (long-Medinan-polity vs short-Medinan-domestic) noted in H-NEW-1360 will persist.

Iblīs-narrative and Christ-narrative are **narrative cycles** (sustained multi-verse story-arcs); the remaining 3 are **liturgical/discourse markers** (single-verse cues without sustained story-arcs). The prediction is that the scale-of-aggregation flip is specific to narrative cycles, not generic to all thematic clusters.

If 1+ of the 3 remaining queued re-tests also flips, the principle extends beyond narrative cycles; if all 3 NULL, the principle is **narrative-cycle specific** — itself a refinement of cross-finding-025, distinguishing narrative-cycle clusters (PASS at pericope) from liturgical-marker clusters (NULL at all scales).

## Statement

The Christ-narrative cluster is a true root-coherent textual cycle in the Quran at pericope scale at corpus-extreme magnitude (z=+4.25, p≤10⁻⁴). The H-NEW-1310 whole-surah NULL is not a NULL of the Christ-narrative cluster as such; it is a NULL of the whole-surah scale-of-aggregation as the right instrument for detecting narrative-cycle cohesion. The classical reading of the Christ-narrative as a deliberate textual recurrence (al-Rāzī, al-Biqāʿī, al-Suyūṭī) is quantitatively confirmed at the pericope scale.

## Post-hoc update — parallel landings expand the cross-scale roster to 4 pairs

Three sister-findings landed concurrently in the same PM continuation:
- **H-NEW-1510** (sajda 15-pericope set, MASTER-LEDGER §10.55): PASS at z=+2.685, p=0.0058
- **H-NEW-1520** (*yā-ayyuhā al-nabī* 13-vocative-pericope set, §10.57 (third instance)): PASS at z=+6.41, p<10⁻⁴
- **H-NEW-1500** (Christ-narrative 9-pericope set, THIS finding, §10.58): PASS at z=+4.25, p≤10⁻⁴

Combined with H-NEW-1380 (Iblīs-narrative 7-pericope set, z=+4.76), the scale-of-aggregation axis now has FOUR independent confirming finding-pairs. The prediction in §"Predictions for the remaining 3 queued re-tests" that *yā-ayyuhā al-nabī* would be weak DIRECTIONAL or NULL is FALSIFIED — it produced the strongest flip of all four (z=+6.41). The narrative-cycle-specific refinement is FALSIFIED on multiple fronts: both a liturgical marker (sajda) and a discourse marker (vocative) flip alongside narrative cycles.

The empirical residual question (still open after these 4 confirmations) is whether the al-ḥamdu opener (H-NEW-1530, queued) also flips. If so, ALL four queued re-tests will have flipped, and the scale-of-aggregation axis applies UNIVERSALLY across thematic-marker classes — not only to narrative cycles or to liturgical markers, but to any pre-registered thematic set under the standard rules-tuple.

Cross-finding-025 graduates from PRELIMINARY-SYNTHESIS to CONFIRMED on the 4-pair criterion at minimum; pending confirmation of H-NEW-1530, the principle may strengthen to UNIVERSAL.
