---
id: H-NEW-1380
title: Iblīs-narrative 7-pericope corpus-wide root-Jaccard cohesion replication + scale-of-aggregation principle (cross-finding-025 corollary)
date: 2026-05-09
verdict: PASS-DIRECTED-REPLICATION
agent: inline-h-new-1380
parent_finding: Q038-F-07 (specialist-scale CONFIRMED, z=+4.76)
sibling_finding: H-NEW-039 (whole-surah-scale NULL)
cross_finding: cross-finding-025 (marker-thickness rule) — adds scale-of-aggregation axis as second methodological dimension
prereg: prereg-h-new-1380-iblis-pericope-replication.md
prereg_sha256: b7e02919d77be823205670f807a144b0419182b4be0f23ca660efd7a5ed29d20
script: scripts/h-new-1380.py
json: csv/h-new-1380.json
seed: 20260509
n_perm: 10000
rules_tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# H-NEW-1380 — Iblīs-narrative pericope cluster: CORPUS-EXTREME at pericope-scale even though host surahs do not cohere at whole-surah scale


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


## 1. The headline

The 7 Iblīs-narrative pericopes — Q 2:34 (refusal to prostrate), Q 7:11-25 (full creation + temptation cycle), Q 15:31-44 (refusal + permission to mislead), Q 17:61-65 (refusal + threat), Q 18:50 (Iblīs as one of the jinn), Q 20:115-123 (Adam-temptation), Q 38:71-85 (full origin + permission) — have **mean pairwise root-Jaccard J_mean = 0.1456**, against a length-matched permutation null mean **0.0650 ± 0.0169** over 10,000 draws.

- **z = +4.76**
- **p_perm (one-tailed, ≥ obs) = 0.0000 strict; reportable upper bound ≤ 10⁻⁴**
- direction matches pre-commit lock (TIGHTER): ✓
- numerical replication of Q038-F-07 (specialist scale): **exact** (J, null_mean, null_std, p all match to floating-point precision).

The pre-commit-locked direction held; the verdict per pre-reg is **PASS-DIRECTED-REPLICATION**. This promotes Q038-F-07's specialist-scale CONFIRMED status into the H-NEW corpus-wide inline series.

## 2. The interesting finding is not the PASS — it's the PAIRING

The same theological set has been tested under two scales-of-aggregation and produces two different verdicts:

| Scale | Finding | Set | Statistic | Result |
|:--|:--|:--|:--|:--|
| Whole-surah | H-NEW-039 | 9 surahs containing *Iblīs* {Q 2, 7, 15, 17, 18, 20, 26, 34, 38} | FR root-distribution cohesion vs corpus | mean FR=0.9402 vs corpus 0.9237; z=+0.24; p=0.537 → **NULL** |
| Pericope | H-NEW-1380 | 7 Iblīs-narrative pericopes (locked verse ranges) | root-Jaccard cohesion vs length-matched null | J_mean=0.1456 vs 0.0650±0.0169; z=+4.76; p≤10⁻⁴ → **PASS-DIRECTED-REPLICATION** |

Both results are correct under their respective instruments. The discrepancy is NOT an inconsistency. It is a SIGNAL about the relationship between marker-thickness, unit-of-aggregation, and FR/Jaccard cohesion.

## 3. The scale-of-aggregation principle (corollary to cross-finding-025)

> **Scale-of-aggregation axis** (formalization claim, supported by this finding-pair): For a thematic set C ⊆ corpus, FR/Jaccard cohesion is a function of BOTH (a) marker-thickness within each unit of aggregation AND (b) the unit of aggregation itself (verse / pericope / surah / multi-surah block). A NULL at one scale does NOT entail a NULL at all scales. A PASS at a narrower scale does NOT entail a PASS at broader scales. Methodologically, the scale-of-aggregation must be pre-specified in the pre-reg, and discrepancies across scales are FIRST-CLASS findings, not contradictions.

This corollary is the **second methodological axis** added to cross-finding-025 (the first being marker-thickness). The two axes together generate a 2×2 prediction-grid:

| Marker thickness within aggregation unit | Cohesion verdict prediction |
|:--|:--|
| THICK (≥30% of unit content) at unit-of-aggregation | PASS expected (e.g. muqaṭṭāʿat, refrain-saturated surahs) |
| THIN (<10% of unit content) at unit-of-aggregation | NULL expected (e.g. sajda single-verse, Christ-narrative sub-block, *yā-ayyuhā al-nabī* discourse-marker) |
| Iblīs narrative concentrated in PERICOPE of length L | THICK at pericope-scale → PASS; THIN at whole-surah scale → NULL |

The Iblīs case operationalizes the principle: the Iblīs narrative has high marker-thickness at the PERICOPE unit-of-aggregation (the narrative is the entire pericope) and low marker-thickness at the WHOLE-SURAH unit-of-aggregation (the narrative occupies ~10-15% of the host surah's verses in Q 7 and Q 38, and <5% in Q 17 and Q 18). The same theological set therefore shifts verdicts when the aggregation scale shifts.

## 4. Per-pericope root counts and per-pair Jaccards

The 7 pericopes range in length 1-15 verses; the per-pericope unique-root counts are {7, 74, 36, 35, 16, 42, 37}. The 21 pairwise Jaccards span 0.066-0.214 with mean 0.1456.

| Pair | inter | union | J |
|:--|--:|--:|--:|
| Q 2:34 — Q 7:11-25 | 5 | 76 | 0.066 |
| Q 2:34 — Q 15:31-44 | 4 | 39 | 0.103 |
| Q 2:34 — Q 17:61-65 | 3 | 39 | 0.077 |
| Q 2:34 — Q 18:50 | 4 | 19 | 0.211 |
| Q 2:34 — Q 20:115-123 | 4 | 45 | 0.089 |
| Q 2:34 — Q 38:71-85 | 6 | 38 | 0.158 |
| Q 18:50 — Q 20:115-123 | 6 | 52 | 0.115 |
| Q 18:50 — Q 38:71-85 | 5 | 48 | 0.104 |
| Q 20:115-123 — Q 38:71-85 | 8 | 71 | 0.113 |

(Full 21-pair table: `csv/h-new-1380.json` → `pairwise_jaccards`.)

The TIGHTEST pair is **Q 2:34 ↔ Q 18:50** at J = 0.211 (4 shared roots in a union of 19). Both are SINGLE-VERSE pericopes with the smallest unions; their high Jaccard reflects the verbal compression of the "Iblīs refused" minimal-narrative form. The LOOSEST pair is **Q 2:34 ↔ Q 7:11-25** at J = 0.066, driven by Q 7's 15-verse vocabulary expansion (74 roots, the largest pericope) over which the minimal Q 2:34 vocabulary set is diluted.

The narrative-cycle backbone — *sjd* (prostrate), *Aby* (refuse), *kbr* (be-haughty), *Edw* (enemy), *qwl* (say), *Amr* (command), *Edn* (Eden) — appears in 5-7 of the 7 pericopes and is the structural source of the +4.76 z.

## 5. What this REFINES (not refutes)

H-NEW-039 (2026-05-07) correctly NULL'd the whole-surah-scale claim that surahs-containing-Iblīs form a cohesive FR cluster. That NULL was published with equal prominence per Protocol §1.3 and remains correct.

H-NEW-1380 (this finding) does NOT contradict H-NEW-039. It establishes that the Iblīs narrative IS a cohesive thematic-vocabulary signature at the PERICOPE unit-of-aggregation, while the host surahs (in which the narrative occupies a small fraction of total content) do NOT cohere.

This is the right way to interpret the H-NEW-039 NULL: it is a marker-thickness-too-thin verdict at whole-surah scale, not a verdict against the Iblīs narrative being a coherent textual unit. The Iblīs narrative IS coherent — the right instrument for detecting that coherence is pericope-scale root-Jaccard, not whole-surah-FR.

## 6. What changes in the cross-finding-025 framework

cross-finding-025 PRELIMINARY-SYNTHESIS (commit `f10deed23`, 2026-05-09) stated the marker-thickness rule:

> A subset C of surahs is FR-cohesive on root-distribution iff the surahs share multiple independent structural features. Sharing a single thematic marker, liturgical trigger, or imperative event is necessary but not sufficient.

H-NEW-1380 augments this with the scale-of-aggregation corollary:

> The unit of aggregation matters. A NULL at one scale (e.g., whole-surah) does not entail a NULL at another (e.g., pericope). The scale must be pre-registered. Discrepant verdicts across scales are first-class findings.

The combined principle is:

> **FR/Jaccard cohesion of a thematic set is jointly determined by (marker-thickness × scale-of-aggregation × instrument). Pre-registration must specify all three.**

## 7. Implications for future pre-regs

- Thin-marker thematic sets (Christ-narrative, sajda, IMPV-qrA, *yā-ayyuhā al-nabī*) that NULL'd at surah-scale (H-NEW-1310, H-NEW-1330, H-NEW-1301/Q073-F-04, H-NEW-1360) should be RE-TESTED at pericope-scale where the marker thickness becomes high. The NULLs at surah-scale do not preclude PASSes at pericope-scale.
- Conversely, pericope-scale PASSes do not automatically promote to surah-scale claims. The scale on which a cluster coheres is itself the right resolution at which to make architectural claims about that cluster.
- Pre-regs going forward should pre-specify aggregation scale alongside the rules-tuple.

## 8. Hadith / classical context

The 7 Iblīs-narrative pericopes form the corpus's core treatment of the prostration-refusal etiology. al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 65 (*fīmā nazala muqarranan*), discusses thematic pairs and clusters but does not separately treat the Iblīs-narrative as a corpus-wide cluster. al-Rāzī, *Mafātīḥ al-ghayb* (commentary on Q 2:34), reads the Iblīs-refusal scene as a kalām-foundational pericope and explicitly notes its parallel occurrences in Q 7, 15, 17, 18, 20, 38. al-Biqāʿī, *Naẓm al-durar*, similarly treats the recurrence as deliberate thematic recurrence rather than mere repetition.

al-Bukhārī, ḥadīth #3326 (Anbiyāʾ, bāb khalq Ādam wa-dhurriyyatihi) treats the prostration scene as primary cosmogonic event; the Iblīs narrative is structurally embedded in the angels-vs-Iblīs taxonomic discourse and not given separate isolated treatment.

The empirical result here — corpus-extreme root-Jaccard at pericope-scale — quantitatively supports the classical reading of the Iblīs narrative as a coherent textual cycle, with the caveat that the right unit-of-aggregation for that coherence is the pericope, not the surah.

## 9. Honest limits

- **Numerical replication, not seed-independent replication**: Seed = 20260509 matches Q038-F-07 deliberately, so the numerical agreement is a script-integrity check, not seed-independent corroboration. A different-seed run is queued as H-NEW-1380b for genuine seed-independence.
- **Set is post-hoc inclusion-criterion-locked**: The 9-surah set (whole-surah) and the 7-pericope set (pericope) differ by 2 surahs (Q 26, Q 34 dropped from pericope set because no developed narrative cycle there). This is the difference in inclusion-criteria across scales. It is fair under Protocol because both inclusion-criteria are pre-registered and operationalized differently for each scale.
- **Pericope ranges are interpretive choices**: A different exegete might bound Q 7:11-25 as 11-27, or Q 38:71-85 as 71-88. The sensitivity of J_mean to ±2 verses on each boundary is a robustness question (queued).
- **Length-matched null does not control for narrative-prose vs eschatological-prose vs lyrical-prose**: The null draws from any 6,236-verse contiguous window; it does not condition on prose-type. A prose-matched null is a follow-up.
- **Root-Jaccard discards root-frequency**: A TF-IDF variant would preserve frequency information; deferred unless a follow-up motivates it.
- **The scale-of-aggregation claim is supported by ONE finding-pair (H-NEW-039 + H-NEW-1380)**. Full codification at cross-finding-025-formal requires at least 2 more finding-pairs with the same pattern (NULL at one scale + PASS at another, same theological set).

## 10. Connection to existing findings (Obsidian links)

- [[h-new-039|H-NEW-039]] — NULL at whole-surah scale (the paired finding for this corollary)
- [[surahs/Q038-sad/Q038-F-07-iblis-narrative-cohesion|Q038-F-07]] — specialist-scale CONFIRMED, identical seed + instrument
- [[cross-finding-025|cross-finding-025]] — marker-thickness rule; this finding adds scale-of-aggregation axis
- [[h-new-1310|H-NEW-1310]] (Christ-narrative whole-surah NULL), [[h-new-1330|H-NEW-1330]] (sajda whole-surah NULL), [[h-new-1340|H-NEW-1340]] (al-ḥamdu li-llāh whole-surah NULL), [[h-new-1360|H-NEW-1360]] (*yā-ayyuhā al-nabī* whole-surah NULL) — candidates for pericope-scale re-test (queued)
- [[h-new-1010|H-NEW-1010]] (letter-axis ⊥ content-axis) — same principle at a different methodological level: the "axis" matters; the "scale" matters

## 11. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-1380-iblis-pericope-replication.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-1380.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-1380.json`
- finding (this file): `findings/phase-b-hypotheses/h-new-1380-iblis-pericope-replication.md`

## 12. Citation

> H-NEW-1380 (2026-05-09): Iblīs-narrative 7-pericope corpus-wide root-Jaccard cohesion replicates at z=+4.76, p≤10⁻⁴ (numerical replication of Q038-F-07, seed 20260509). Formalizes scale-of-aggregation as a second methodological axis under cross-finding-025: the same theological set NULLs at whole-surah scale (H-NEW-039) and PASSes corpus-extreme at pericope scale (this finding). Discrepant verdicts across scales are first-class findings; pre-regs must specify aggregation scale alongside rules-tuple. Quran Decipherment Project, MASTER-FINDINGS-LEDGER §10.51.
