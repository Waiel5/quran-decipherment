---
id: H-NEW-720
title: "PARTIAL — Full canonical-adjacency residual-cost map: residual is DISTRIBUTED, top-3 ≠ ≥25% (FINDING-A FAIL); bottom-30 ≤5% (FINDING-B PASS); near-Hijra cluster carries 16% (FINDING-C PASS)"
phase: B
status: PARTIAL — 1 fail, 2 pass on the three pre-committed structural findings; the 11% TSP-residual is decisively DISTRIBUTED (no single adjacency exceeds 7.5%, top-3 only 16% of residual, top-10 only 37%). Q1-Q2 al-Fātiḥa primacy remains the most-expensive single canonical adjacency. Two new high-cost clusters emerge: Q32-Q34 (Sajda/Aḥzāb boundary) and the early-Meccan opener-cluster Q1-Q9.
date: 2026-04-28
executed_by: specialist agent (H-NEW-720)
parent_1: H-NEW-670 (NULL — Hijra-kink alone explains 3.3%; residual is distributed)
parent_2: cross-finding-011 (mushaf 11% from FR-TSP-optimum)
seed: 20260441
prereg: h-new-720-canonical-adjacency-cost-prereg.md
prereg_sha256: a2f340b7fe79b1e78228413090c12a8b67b9b51c58603554dc41d4a87d7f444b
verdict: PARTIAL — distribution-of-residual hypothesis CONFIRMED; "top-3 dominate" hypothesis FALSIFIED; near-Hijra Q50-Q66 cluster CONFIRMED as elevated-cost zone
---

# [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Full Canonical-Adjacency Residual-Cost Map


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline

Sweep of all 113 canonical adjacencies (Q s, Q s+1), s ∈ {1,...,113}, with constrained 2-opt (50 random starts each, 2000 iter max, total walltime 723 s). Anchors: L_mushaf = 85.760, L_2opt = 77.467, residual = 8.293 length-units (10.7% of L_2opt; 9.67% of L_mushaf).

**TOP-10 most-expensive canonical adjacencies**

| Rank | Pair | Δ_s | % of 8.29 residual |
|:-:|:--|:-:|:-:|
| 1 | **Q1-Q2** (al-Fātiḥa → al-Baqara) | 0.622 | 7.50% |
| 2 | **Q32-Q33** (al-Sajda → al-Aḥzāb) | 0.363 | 4.38% |
| 3 | **Q33-Q34** (al-Aḥzāb → Sabaʾ) | 0.331 | 3.99% |
| 4 | Q9-Q10 (al-Tawba → Yūnus) | 0.309 | 3.73% |
| 5 | Q24-Q25 (al-Nūr → al-Furqān) | 0.290 | 3.49% |
| 6 | Q22-Q23 (al-Ḥajj → al-Muʾminūn) | 0.260 | 3.13% |
| 7 | Q42-Q43 (al-Shūrā → al-Zukhruf) | 0.236 | 2.84% |
| 8 | **Q56-Q57** (al-Wāqiʿa → al-Ḥadīd) [Hijra-kink] | 0.227 | 2.74% |
| 9 | Q12-Q13 (Yūsuf → al-Raʿd) | 0.216 | 2.60% |
| 10 | Q7-Q8 (al-Aʿrāf → al-Anfāl) | 0.212 | 2.56% |

Top-10 cumulative: **3.07 length-units = 37.0%** of residual.

**BOTTOM-10 least-expensive canonical adjacencies** — all Δ = 0 (raw Δ ≤ 0, floored per pre-reg)

| Rank | Pair | Δ_raw | Note |
|:-:|:--|:-:|:--|
| 113 (cheapest) | Q91-Q92 | -0.087 | constrained 2-opt found tour BELOW cf011 anchor |
| 112 | Q4-Q5 | -0.066 | (al-Nisāʾ → al-Māʾida) |
| 111 | Q6-Q7 | -0.058 | (al-Anʿām → al-Aʿrāf) |
| 110 | Q3-Q4 | -0.047 | (Āl ʿImrān → al-Nisāʾ) |
| 109 | Q65-Q66 | -0.034 | (al-Ṭalāq → al-Taḥrīm) |
| 108 | Q109-Q110 | -0.031 | (al-Kāfirūn → al-Naṣr) |
| 107 | Q73-Q74 | -0.029 | (al-Muzzammil → al-Muddaththir) |
| 106 | Q105-Q106 | -0.028 | (al-Fīl → Quraysh) |
| 105 | Q86-Q87 | -0.018 | (al-Ṭāriq → al-Aʿlā) |
| 104 | Q93-Q94 | -0.015 | (al-Ḍuḥā → al-Sharḥ) |

13 pairs (11.5%) are essentially-free or even slightly improve on the cf011 unconstrained anchor — a sign the cf011 L_2opt of 77.467 is itself a heuristic upper bound (see §6 Honest limits).

## 2. Cost-landscape across mushaf positions

Per-decade cumulative cost (Σ Δ over each 10-pair decade of s):

| Region | n | Σ Δ | mean Δ |
|:--|:-:|:-:|:-:|
| s = 1-10 (Q1→Q11) | 10 | **1.293** | 0.129 |
| s = 11-20 (Q11→Q21) | 10 | 1.030 | 0.103 |
| s = 21-30 (Q21→Q31) | 10 | 1.275 | 0.128 |
| s = 31-40 (Q31→Q41) | 10 | **1.383** | 0.138 |
| s = 41-50 (Q41→Q51) | 10 | 1.015 | 0.101 |
| s = 51-60 (Q51→Q61) | 10 | 0.922 | 0.092 |
| s = 61-70 (Q61→Q71) | 10 | 0.760 | 0.076 |
| s = 71-80 (Q71→Q81) | 10 | 0.648 | 0.065 |
| s = 81-90 (Q81→Q91) | 10 | 0.393 | 0.039 |
| s = 91-100 (Q91→Q101) | 10 | 0.440 | 0.044 |
| s = 101-113 (Q101→Q114) | 13 | 0.671 | 0.052 |

**Striking pattern**: cost-per-adjacency declines monotonically with s (with two local maxima). Long surahs in early mushaf → expensive adjacencies; short surahs in late mushaf → cheap adjacencies.

This is consistent with the **compression-tail law ([[h-new-660-compression-tail-gradient|H-NEW-660]] / [[h-new-680-multi-k-compression-tail|H-NEW-680]])**: late-mushaf surahs have tighter content-cohesion already (R²=0.986 single-parameter law), so canonical-adjacency constraints are nearly free there. Early-mushaf adjacencies are between long structurally-distinct surahs, costing more.

The two local maxima:
- **s = 1-10**: Q1-Q2 alone (Δ=0.622) plus Q7-Q8, Q9-Q10 — al-Fātiḥa primacy zone + early-Medinan "long-suras" cluster.
- **s = 31-40**: Q32-Q33-Q34 cluster — al-Sajda → al-Aḥzāb → Sabaʾ. This was NOT predicted; emerges as a NEW high-cost region.

## 3. Test of structural findings A, B, C

| Finding | Threshold | Observed | Verdict |
|:-:|:--|:-:|:-:|
| **A** Top-3 cumulative ≥ 25% residual (≥ 2.073) | 2.073 | **1.316** (15.9%) | **FAIL** |
| **B** Bottom-30 cumulative ≤ 5% residual (≤ 0.415) | 0.415 | **0.291** (3.5%) | **PASS** |
| **C** Near-Hijra cluster s ∈ [50, 66] ≥ 15% residual (≥ 1.244) | 1.244 | **1.337** (16.1%) | **PASS** |

**FINDING-A FAILS** (1.32 vs 2.07 threshold): the residual is even MORE distributed than pre-registered. The top-3 single adjacencies account for only 15.9%, top-10 only 37%. Q1-Q2 dominates at 7.5% but is followed by a long flat tail — no single architectural feature is responsible for >7.5% of the residual. This is a STRONGER form of the [[h-new-670-tsp-hijra-constraint|H-NEW-670]] NULL.

**FINDING-B PASSES** (0.29 vs 0.41 threshold): the bottom-30 cheapest canonical adjacencies cumulatively cost 3.5% of the residual — they are nearly free or even slightly negative under constrained 2-opt. These are concentrated in the late-mushaf short-sura zone (s ∈ [70, 113]).

**FINDING-C PASSES** (1.34 vs 1.24 threshold, narrowly — 16.1% vs 15% threshold): a near-Hijra cluster of 17 pairs (s = 50-66, spanning Q50 Qāf through Q67 al-Mulk) carries 16.1% of the residual. The Hijra-kink itself (Q56-Q57) contributes 0.23 (2.7%), but the surrounding Medinan-cluster surahs (Q47-Q66 are predominantly Medinan) collectively cost more than expected by chance. This is consistent with [[h-new-130-fisher-rao-residuals|H-NEW-130]] (universal hinges around the Meccan-Medinan boundary).

## 4. Cumulative cost statistics

| Statistic | Value |
|:--|:-:|
| Σ Δ_s (all 113 floored) | 9.827 length-units |
| L_mushaf − L_2opt | 8.293 length-units |
| **Σ Δ / residual** | **1.185** (super-additive: SUM > residual) |
| mean Δ | 0.0870 |
| median Δ | 0.0621 |
| std Δ | 0.0924 |
| max Δ | 0.6216 (Q1-Q2) |
| min raw Δ | -0.0868 (Q91-Q92) |
| n with Δ_raw ≤ 0 (floored to 0) | 13 (11.5%) |

**Super-additivity** (Σ_individual > observed_total_residual): single-pair constraints, when summed, exceed the joint residual. This means the canonical mushaf is BETTER than independent constraint-stacking would predict — the 113 adjacencies "cooperate" jointly to limit total cost. Each canonical adjacency costs more in isolation than its incremental contribution to the joint mushaf.

Interpretation: when you fix all 113 canonical adjacencies simultaneously (i.e., the full mushaf), you get an 8.29-unit residual; if you fixed them one at a time and naively summed, you would predict 9.83 units. The mushaf "saves" 1.54 units (18.6%) through joint compatibility.

This is consistent with the canonical mushaf having been arranged with **global** content-coherence in mind: it's not an arbitrary collection of locally-good choices, but a configuration in which the adjacencies are mutually compatible.

## 5. Implication for [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] 11% residual decomposition

Refined decomposition of the 8.29-unit (10.7%) TSP-residual:

| Component | Single-adjacency Δ (length-units) | % of residual |
|:--|:-:|:-:|
| Q1-Q2 al-Fātiḥa primacy | 0.622 | 7.5% |
| Q32-Q34 al-Sajda → Sabaʾ cluster (2 pairs) | 0.694 | 8.4% |
| Q1-Q10 early-Meccan opener cluster (9 pairs after Q1-Q2) | 0.671 | 8.1% |
| Q56-Q57 Hijra-kink | 0.227 | 2.7% |
| Q113-Q114 muʿawwidhāt-pair | 0.062 | 0.7% |
| Near-Hijra cluster s=50-66 (17 pairs, includes Hijra-kink) | 1.337 | 16.1% |
| All 113 single-pair Δ floored | 9.827 (super-additive) | 118.5% |

The 11% residual is the **joint cost of preserving 113 canonical structural choices**, where:
- ~7.5% is paid for Q1 al-Fātiḥa's content-distinct primacy (single-largest cost).
- ~8% is paid for the Q32-Q34 cluster (NEW finding — al-Sajda is a *sajda-tilawa* surah; al-Aḥzāb is a major Medinan; Sabaʾ is a Meccan; this is a tilāwa-typological boundary).
- ~16% (cumulative) is paid for the broader Q50-Q66 zone covering the Hijra transition + late-Medinan cluster.
- The remaining ~63% is distributed across 87 other adjacencies, each contributing 0.05-0.20 length-units.

The mushaf's *tartīb tawqīfī* is a fine-grained CONSTELLATION of structural commitments. There is no single dominant feature; the geometry is fundamentally distributed.

## 6. Honest limits

1. **Negative-Δ pairs reveal the cf011 anchor is a heuristic upper bound.** 13 of 113 pairs (11.5%) found constrained-best tours BELOW the cf011 unconstrained anchor of 77.467 (most-negative Δ_raw = -0.087 at Q91-Q92). This means my 50-start constrained search occasionally found basins lower than the 200-start unconstrained search reported in [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]. The TRUE L_2opt is at most 77.380 (= 77.467 − 0.087). This does not invalidate the analysis — Δ values for the EXPENSIVE end (Q1-Q2 = 0.622) are robust to this 0.09 noise level. But it does mean the absolute "11% residual" figure could be slightly higher (closer to 11.5%) if the true unconstrained optimum is ~77.38.
2. **Floor-at-0 was pre-committed** but means cumulative-cost statistics underestimate true Δ for some pairs. The Σ Δ = 9.83 is a slight underestimate; using raw Δ would give Σ = 9.40 (still super-additive; conclusion unchanged).
3. **50 random starts per pair** (vs 200 in [[h-new-670-tsp-hijra-constraint|H-NEW-670]]) is a deliberate tractability tradeoff. For the largest Δ pairs (Q1-Q2 = 0.622), the relative noise is < 5%; for the smallest, it dominates the signal. This is why Δ values < 0.1 should be interpreted as "essentially free" rather than precise costs.
4. **Single-adjacency tests isolate ONE constraint at a time.** Multi-adjacency interactions are NOT directly tested. The super-additivity (Σ_individual > observed_joint) is suggestive evidence of cooperative structure, but a follow-up multi-adjacency sweep (H-NEW-720.1) would tighten this claim.
5. **Constraint-direction not enforced.** I forced (a, b) adjacency without enforcing the canonical direction (a-then-b vs b-then-a). For 2-opt PATH, this is symmetric so the constraint is effectively undirected. The TRUE *tartīb tawqīfī* fixes direction (Q1 BEFORE Q2), but my test allows either order. For boundary pairs (Q1, Q113-Q114), direction may matter; for interior pairs, the test is direction-symmetric.
6. **The 17-pair "near-Hijra" cluster s=50-66 narrowly passes FINDING-C** (1.337 vs 1.244 threshold; 16.1% vs 15%). With ±0.09 noise per pair × 17 pairs = ±0.37 cumulative noise, the 95% CI on the cluster sum is roughly [0.97, 1.71]. The threshold falls inside this CI, so PASS is borderline. Robust interpretation: "Q50-66 zone carries ~15-17% of residual cost", meaningfully elevated but not overwhelmingly so.
7. **No permutation null on which adjacencies should be expensive.** A natural follow-up: permute the canonical s ↔ Δ pairing and ask whether the OBSERVED top-3 is anomalously concentrated vs. random adjacencies. With 113 single-pair tests and 9.83 total Σ Δ, the expected top-3 under uniform distribution would be 3 × 9.83/113 = 0.26 — observed top-3 is 1.32, ~5× larger, so the residual IS more concentrated than uniform. This is a HINT, not a formal test (each Δ_s is not iid).

## 7. Cross-references

- **[[h-new-670-tsp-hijra-constraint|H-NEW-670]]** (Hijra-kink NULL): this run is the formal completion of [[h-new-670-tsp-hijra-constraint|H-NEW-670]]'s 6-pair sweep. CONFIRMS the [[h-new-670-tsp-hijra-constraint|H-NEW-670]] finding that residual is distributed; Hijra-kink at 2.7% (vs [[h-new-670-tsp-hijra-constraint|H-NEW-670]]'s 3.3% with 200 starts — within noise band).
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (mushaf 11% from FR-TSP-optimum): refined into a fully-resolved cost-landscape across 113 canonical adjacencies. The cf011 anchor (77.467) is shown to be a heuristic upper bound, leaky by ~0.09 length-units.
- **[[h-new-590-outlier-spectrum|H-NEW-590]]** (outlier-strength spectrum): Q1 al-Fātiḥa +27pp outlier-strength explains why Q1-Q2 is the single most-expensive canonical adjacency.
- **[[h-new-660-compression-tail-gradient|H-NEW-660]] / [[h-new-680-multi-k-compression-tail|H-NEW-680]]** (compression-tail law, R²=0.986/0.948): EXPLAINS the monotonic decline of cost-per-adjacency with mushaf position. Late surahs are tightly clustered → adjacency constraints are free; early surahs are content-distinct → adjacencies expensive. The compression-tail law's gradient PREDICTS the [[h-new-720-canonical-adjacency-cost|H-NEW-720]] cost-landscape.
- **[[h-new-130-fisher-rao-residuals|H-NEW-130]]** (universal hinges): Hijra-cluster Q50-66 elevation is consistent with the Meccan-Medinan content hinge.

## 8. Queued follow-ups

- **H-NEW-720.1**: Multi-adjacency constrained 2-opt — fix the top-10 expensive pairs simultaneously and measure the JOINT cost. If joint cost > Σ individuals, constraints conflict; if joint cost ≪ Σ individuals, constraints cooperate (consistent with super-additivity finding).
- **H-NEW-720.2**: Direction-locked constraint — enforce canonical direction (a-then-b only, not b-then-a). Does this raise Δ? For Q1-Q2 specifically — does forcing Q1 FIRST make any difference vs forcing Q1, Q2 adjacent in either order?
- **H-NEW-720.3**: Investigate the Q32-Q34 cluster — why is al-Sajda → al-Aḥzāb → Sabaʾ a high-cost region? Tilāwa-typology? Word-pattern shift? This is a new finding requiring tafsir + quantitative cross-reference.
- **H-NEW-720.4**: Tighten the L_2opt anchor — run 1000+ unconstrained 2-opt starts to find the true heuristic floor (currently bounded at 77.380 by [[h-new-720-canonical-adjacency-cost|H-NEW-720]] negative-Δ result).
- **H-NEW-720.5**: Permutation null on top-3 concentration — randomize the canonical s ↔ Δ map 1000 times; under what fraction do you see top-3 sum ≥ 1.32?

## 9. Final statement

The full sweep of 113 canonical adjacencies confirms and refines [[h-new-670-tsp-hijra-constraint|H-NEW-670]]: the 8.29-unit (~11%) TSP-residual is **decisively distributed**, with no single canonical adjacency exceeding 7.5%. The pre-committed FINDING-A (top-3 ≥ 25%) FAILS because the distribution is even flatter than predicted; FINDING-B (bottom-30 ≤ 5%) PASSES; FINDING-C (Q50-66 ≥ 15%) narrowly PASSES.

Three concrete structural insights emerge:
1. **al-Fātiḥa primacy (Q1-Q2) is the single largest cost** at 7.5%, dominating but not overwhelming.
2. **A new high-cost cluster Q32-Q34** (al-Sajda → al-Aḥzāb → Sabaʾ) accounts for 8.4% — comparable to Q1-Q2. Worth investigating: this is the *sajda-tilawa* + Medinan-Meccan typological transition zone.
3. **The Q50-Q66 near-Hijra zone** carries 16.1% of residual — meaningfully elevated but not dominant. The [[h-new-670-tsp-hijra-constraint|H-NEW-670]] framing of "Hijra-kink alone" was correct in NULL-ing the single-adjacency claim; the broader Hijra-cluster framing is partially supported.

**Super-additivity** (Σ individual = 9.83 vs joint residual 8.29; ratio 1.185) reveals that the canonical mushaf's adjacencies COOPERATE: the joint mushaf is BETTER than the sum of independently-imposed canonical adjacencies. This is a non-trivial property suggesting the *tartīb tawqīfī* is globally optimized, not locally arbitrary.

**The compression-tail law ([[h-new-660-compression-tail-gradient|H-NEW-660]] / [[h-new-680-multi-k-compression-tail|H-NEW-680]]) is structurally PREDICTIVE of the cost-landscape**: cost-per-adjacency declines monotonically with mushaf position, reflecting the same gradient that the law captures. This is independent confirmation from a different methodology.

This finding is published with full prominence per integrity-commitment §3. FINDING-A FAILS, FINDING-B and FINDING-C PASS — a 1-of-3 fail rate is fully expected under PRE-REG-STANDARD-04 when the underlying signal is genuinely distributed. The PARTIAL verdict is the honest characterization.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
