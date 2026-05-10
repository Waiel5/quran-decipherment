---
id: H-NEW-1520
title: yā-ayyuhā al-nabī prophet-vocative pericope-scale flip test — PASS-DIRECTED (z = +6.41, p_perm < 10⁻⁴)
date: 2026-05-09
status: PASS-DIRECTED
prereg_sha: 7d4dce4952bb47dfba71fb173230e43032df45ed59f2a56293981920925dbb1e
parent_findings: [H-NEW-1360, H-NEW-1380]
cross_finding: cross-finding-025
verdict: PASS-DIRECTED (whole-surah NULL → pericope-window PASS — flip confirmed)
---

# H-NEW-1520 — yā-ayyuhā al-nabī prophet-vocative pericope-scale flip test

## Headline

The 13 yā-ayyuhā al-nabī attestations — when re-tested at the **3-verse pericope-window scale** that captures the divine directive following each vocative — cohere on root-Jaccard at **J_mean = 0.1260 vs null = 0.0488 ± 0.0120, z = +6.41, p_perm < 10⁻⁴ (0/10,000 perms ≥ observed)**.

This **flips** the H-NEW-1360 whole-surah Fisher-Rao NULL into a pericope-window PASS-DIRECTED, replicating the H-NEW-1380 (Iblīs-narrative) scale-of-aggregation principle on an **independent target set**. The discourse-marker interpretation of H-NEW-1360 — that the vocative's content is the immediately-following directive, not the host surah — is empirically vindicated.

## Test in one line

For 13 vocative pericope-windows (each = vocative-verse and the next 2 verses, truncated in-surah for Q 60:12), mean pairwise root-Jaccard (78 pairs, QAC v0.4 ROOT-field union) was compared against 10,000 length-matched random-window draws (seed = 20260509).

## Numerical result

| Quantity | Value |
|:--|:--|
| Observed J_mean (78 pairs) | **0.1260** |
| Null mean | 0.0488 |
| Null std | 0.0120 |
| z-score | **+6.41** |
| p_perm (strict, one-tailed ≥ obs) | **0.0000** (0/10,000) |
| p_reportable upper bound | < 1.0 × 10⁻⁴ |
| Direction lock | TIGHTER (J_mean > null) — MATCHED |
| Verdict | **PASS-DIRECTED** |

## Cross-scale comparison — the flip

| Scale | Finding | Set | Statistic | p-value | Verdict |
|:--|:--|:--|:--|:--|:--|
| Whole-surah | **H-NEW-1360** | 6 surahs {Q 8, 9, 33, 60, 65, 66} | FR_mean = 0.9532 (corpus 0.9240) | Cell A p = 0.5734; Cell B p = 0.5835; MW-5 PC valid p = 0.0445 | **substantive NULL** |
| Pericope-window | **H-NEW-1520** (this) | 13 vocative pericope-windows | J_mean = 0.1260 (null 0.0488) | p_perm < 10⁻⁴; z = +6.41 | **PASS-DIRECTED** |

The flip is dramatic: z = +6.41 at pericope-window scale vs effectively zero signal at whole-surah scale. The marker's "content" — read as the immediately-following divine directive — is genuinely cohesive across all 13 attestations. The host-surahs are not.

## Per-window summary

| # | Window | Verses | N_unique_roots |
|:--|:--|:--|:--|
| 1 | Q 8:64-66 | 3 | 20 |
| 2 | Q 8:65-67 | 3 | 27 |
| 3 | Q 8:70-72 | 3 | 34 |
| 4 | Q 9:73-75 | 3 | 34 |
| 5 | Q 33:1-3 | 3 | 16 |
| 6 | Q 33:28-30 | 3 | 27 |
| 7 | Q 33:45-47 | 3 | 13 |
| 8 | Q 33:50-52 | 3 | 47 |
| 9 | Q 33:59-61 | 3 | 27 |
| 10 | Q 60:12-13 | 2 | 29 |
| 11 | Q 65:1-3 | 3 | 42 |
| 12 | Q 66:1-3 | 3 | 22 |
| 13 | Q 66:9-11 | 3 | 32 |

## Strongest pairwise Jaccards

| i | j | Jaccard | Intersection / Union |
|:--|:--|:--|:--|
| Q 8:64-66 | Q 8:65-67 | 0.621 | 18 / 29 |
| Q 9:73-75 | Q 66:9-11 | 0.245 | 13 / 53 |
| Q 8:70-72 | Q 60:12-13 | 0.212 | 11 / 52 |
| Q 8:64-66 | Q 33:1-3 | 0.200 | 6 / 30 |
| Q 8:70-72 | Q 66:1-3 | 0.192 | 9 / 47 |
| Q 8:70-72 | Q 33:50-52 | 0.191 | 13 / 68 |
| Q 33:50-52 | Q 66:1-3 | 0.190 | 11 / 58 |
| Q 8:70-72 | Q 66:9-11 | 0.179 | 10 / 56 |
| Q 33:50-52 | Q 33:59-61 | 0.175 | 11 / 63 |
| Q 9:73-75 | Q 33:28-30 | 0.173 | 9 / 52 |

Note: the strongest pair (Q 8:64-66 × Q 8:65-67) is mechanically overlapping by two verses; this inflates the statistic slightly but is part of the locked design (overlapping windows arose because two vocatives in Q 8 are only one verse apart). Even setting this single inflated pair to its non-overlapping pseudo-equivalent would still leave 77 independent pairs with mean ≈ 0.119, comfortably above null. The headline z > 6 is not driven by this single pair.

The Q 9:73-75 × Q 66:9-11 second-place pair is non-trivially informative: these two windows share the *jihād-against-disbelievers-and-hypocrites* directive ({j-h-d, g-l-Z, k-f-r, n-f-q, ...}) verbatim — Q 9:73 and Q 66:9 are textual near-twins.

## Weakest pairwise Jaccards (for honesty)

| i | j | Jaccard |
|:--|:--|:--|
| Q 33:45-47 | Q 33:50-52 | 0.053 |
| Q 66:1-3 | Q 66:9-11 | 0.059 |
| Q 33:45-47 | Q 66:1-3 | 0.061 |
| Q 65:1-3 | Q 66:1-3 | 0.067 |
| Q 33:1-3 | Q 33:50-52 | 0.068 |

The eschatological-witness pericope Q 33:45-47 (the Prophet as *shāhid* / *mubashshir* / *nadhīr*) is lexically the most distinct sub-block — and even its lowest-pair Jaccard (0.053) sits at the null-MEAN, not below it.

## Interpretation

H-NEW-1360 explicitly predicted this outcome in its NULL-interpretation paragraph (MASTER-FINDINGS-LEDGER §10.44.7):

> yā-ayyuhā al-nabī is a DISCOURSE marker (direct second-person prophetic command), NOT a content-cohesion marker — exact opposite of yā-ayyuhā alladhīna āmanū which concentrates in Q 49 and clusters with Q 49 target-set.

This pre-reg promotes that descriptive prediction into a falsifiable test, and the prediction holds. The vocative + 3-verse directive carries a small high-frequency core of injunction roots ({q-w-l, ʾ-m-r, k-f-r, n-s-ʾ, n-f-q, j-h-d, ḥ-l-l, ḥ-r-m, ʿ-l-m, r-ḥ-m, w-l-y, …}) that recurs across 13 attestations spanning legal, military, marital, eschatological, and admonitory directives — even though the host surahs span heterogeneous topics.

## Cross-finding-025 scale-of-aggregation principle — second supporting pair

H-NEW-1380 (Iblīs-narrative whole-surah NULL → pericope PASS) established the scale-of-aggregation axis as a methodological finding under cross-finding-025 (MASTER-FINDINGS-LEDGER §10.51.2). The codification threshold at cross-finding-025-formal is two supporting finding-pairs. This is the **second supporting pair**:

| Pair | Whole-surah scale | Pericope scale | Flip? |
|:--|:--|:--|:--|
| Iblīs-narrative (set: {Q 2,7,15,17,18,20,26,34,38}) | H-NEW-039 NULL (FR z = +0.24, p = 0.537) | H-NEW-1380 PASS (J z = +4.76, p < 10⁻⁴) | YES |
| yā-ayyuhā al-nabī (set: {Q 8, 9, 33, 60, 65, 66}) | H-NEW-1360 NULL (FR Cell A p = 0.573) | **H-NEW-1520 PASS (J z = +6.41, p < 10⁻⁴)** | **YES** |

Both pairs flip in the same direction (whole-surah NULL → pericope PASS), with effect sizes comparable in magnitude (z = +4.76 vs +6.41). The principle now has 2/2 supporting pairs and is eligible for codification at cross-finding-025-formal.

## Honest limits

1. **Seed dependence**: seed 20260509 matches H-NEW-1360 / H-NEW-1380 / Q038-F-07 (within-session consistency). A different-seed replication run (H-NEW-1520b at e.g. seed = 20260601) is queued; the null mean and std should match to ~3 decimal places, the observed J_mean is invariant under seed, and the z-score should remain z > 5 under any reasonable seed.
2. **One overlapping-window pair**: Q 8:64-66 × Q 8:65-67 share two verses by construction (two vocatives one verse apart inside Q 8). This inflates one of 78 pairs; we showed the headline remains z > 5 even when this pair is removed. The locked design accepts the overlapping pair because the pre-reg fixed the window scheme before observation.
3. **The instrument's "PASS" is a relative comparison to length-matched random windows**: it is not a claim that ALL prophet-vocative directives are about the SAME thing. The directives span legal (Q 65:1, Q 66:1), military (Q 8:64, 8:65, 8:70, 9:73), marital (Q 33:28, 33:50, 60:12, 66:9), eschatological-role (Q 33:45), and admonitory (Q 33:1, Q 33:59) themes. The PASS says: across this thematic heterogeneity, the directive-windows still share a high-frequency injunction-root core at root-Jaccard level that random 3-verse windows of the corpus do not.
4. **Window-size sensitivity not yet run**: the 3-verse window was the pre-locked default. A sensitivity arm at window = 2 and window = 5 (H-NEW-1520-sens) is queued. The prediction is monotone-decreasing z as window grows beyond ~4 verses (host-surah noise re-enters).
5. **The flip pattern is NOT universal**: cross-finding-025 documents three thin-marker NULLs (H-NEW-1310 Christ-narrative, H-NEW-1330 sajda, H-NEW-1340 al-ḥamdu) that have not yet been re-tested at pericope scale. The principle says "scale-of-aggregation matters and discrepancies are first-class," not "every whole-surah NULL flips at pericope scale." Predictions for those three thin-marker re-tests should be made before computation.

## Classical context

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 51 (*fī khiṭābātihi*) catalogs the direct-address forms of the Quran and identifies *yā-ayyuhā al-nabī* as a Medinan direct-address form addressed exclusively to the Prophet. al-Suyūṭī's catalog describes the form's distribution (host surahs and verses) but does NOT predict root-level cohesion of the immediately-following directives — that prediction is a project-internal empirical claim emerging from H-NEW-1360's discourse-marker interpretation. The empirical result here is consistent with the descriptive Medinan-direct-address grouping; it adds quantitative discourse-cohesion to the classical descriptive claim.

al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, in the section on *al-khiṭāb*, similarly catalogs the direct-address forms without predicting root-distribution cohesion of the directive-window.

The project-internal empirical claim emerging from H-NEW-1520 is therefore a refinement of the classical descriptive observation: the prophet-vocative is not just a recognizable direct-address form but a **discourse-cohesion node** whose 3-verse directive-window carries an injunction-root core distinct from the corpus baseline.

## Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-1520-prophet-vocative-pericope.md` (SHA `7d4dce4952bb47dfba71fb173230e43032df45ed59f2a56293981920925dbb1e`).
- Script: `findings/phase-b-hypotheses/scripts/h-new-1520.py`.
- JSON: `findings/phase-b-hypotheses/csv/h-new-1520.json`.

## Cross-references

- **H-NEW-1360** — whole-surah NULL (the parent NULL this flips).
- **H-NEW-1380** — Iblīs-narrative pericope PASS (first supporting pair for scale-of-aggregation principle).
- **H-NEW-039** — Iblīs whole-surah NULL (companion to H-NEW-1380).
- **H-NEW-1260** — yā-ayyuhā alladhīna āmanū sister-construction (CONFIRMED whole-surah).
- **cross-finding-025** — marker-thickness × scale-of-aggregation joint methodological synthesis.
- MASTER-FINDINGS-LEDGER §10.44.7 (H-NEW-1360 NULL) and §10.51 (H-NEW-1380 + scale-of-aggregation).
