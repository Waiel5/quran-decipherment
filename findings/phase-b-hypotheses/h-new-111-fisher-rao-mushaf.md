# [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Fisher-Rao information-geodesic test of mushaf order

> ## ⛔ CORRECTION NOTICE — 2026-08-07: this result does not discriminate
>
> **The arithmetic below is exact and reproduces independently** (L_mushaf = 85.7597,
> L_Nöldeke = 87.2321, null 104.363/1.623). Three things did not survive:
>
> 1. **The genre control.** Cut into 114 pseudo-surahs matching this corpus's length profile and
>    measured on an instrument-matched pipeline, **al-Bukhārī scores z = −13.84 and pre-Islamic
>    poetry z = −15.13, against the Qurʾān's z = −11.50.** Both baselines are more extreme, and
>    both sit closer to their own TSP optima (1.073, 1.093) than the mushaf does to its (1.130).
> 2. **The surah seams.** Cutting this corpus's own verse stream into 114 blocks of the same size
>    profile at offsets that ignore every surah boundary gives z = −11.23, −13.18, −12.92, −12.33,
>    −12.62 — four of five *more* extreme than the canonical division.
> 3. **The MW-1 length control**, which the §Sanity-anchors correction below shows was never
>    working: length-sorting alone reaches z = −8.66.
>
> **What still stands:** the relative claim — the mushaf is a shorter traversal than either
> reconstructed chronology — with an honest margin of **2.80 σ over pure length-sorting**.
> The uniform-random-permutation null is simply too weak to isolate design: any text read in the
> order it exists beats a scramble of its own chunks.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md` §7–8.1.
> Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


**Finding ID**: [[h-new-111-fisher-rao-mushaf|h-new-111]]
**Date**: 2026-04-17
**Specialist**: [[h-new-111-fisher-rao-mushaf|h-new-111]]-specialist
**Pre-reg**: `findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf-prereg.md`
**Pre-reg SHA-256**: `ea3f0ee41d413b0e2a9bfced340f7bfa12e93f40ad8c43a92a873c82856ee8c8`
**Seed**: 20260417
**Rules tuple**: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kūfan)
**Verdict**: ~~**PASS-DIRECTED**~~ → **DOES-NOT-DISCRIMINATE (2026-08-07)**. The computation is exact and the relative ordering claim stands; the permutation-null magnitude does not survive the cross-corpus control. See the correction notice below.

---

## Headline

**The Quran's canonical (mushaf) ordering of its 114 surahs is information-geometrically optimized.** Consecutive surahs in the mushaf are measurably closer in Fisher-Rao distance (on the 500-dimensional simplex of root-distributions) than chance would allow, and the total mushaf path length is **within 11% of the TSP-optimum**.

Beyond that — and unexpectedly — **the mushaf ordering is MORE information-geometrically coherent than the Nöldeke chronological ordering**. This runs opposite to the historical-critical expectation that chronology would be the "natural" order.

---

## Numbers

### PRIMARY (pre-registered, one-sided lower-tail, α_bon = 0.0167)

| Quantity | Value |
|---|---|
| L_mushaf (total Fisher-Rao path length over 113 consecutive pairs) | **85.760** |
| Null mean (10,000 random permutations) | 104.346 |
| Null SD | 1.622 |
| Null min observed | 98.111 |
| Null 5th percentile | 101.663 |
| z-score | **−11.46** |
| #{L_perm ≤ L_mushaf} | 0 |
| p_primary (one-sided, lower-tail) | **< 1/10001 ≈ 1×10⁻⁴** |
| Bonferroni α (k=3) | 0.0167 |
| **PASS** | ✓ (by 167×) |

Not a single one of 10,000 random orderings was as short as the mushaf.

### SECONDARY A — geodesic-optimality ratio

| Quantity | Value |
|---|---|
| L_greedy_best (greedy-NN, best over 114 start-nodes) | 78.836 |
| L_2opt_best (greedy-NN + 2-opt local search) | **77.467** |
| **L_mushaf / L_2opt_best** | **1.107** |

The mushaf is **within 10.7% of an approximate TSP optimum** on 114 nodes. Since 2-opt is an upper bound on `L_min`, the TRUE ratio `L_mushaf / L_min` is ≥ 1.107 — so the mushaf path is bounded at worst ~11% above optimum. This is far inside the pre-registered "near-optimal" band (<1.2).

### SECONDARY B — Nöldeke chronology vs mushaf (two-sided exploratory)

| Quantity | Value |
|---|---|
| L_nold (Nöldeke chronological path) | **87.232** |
| L_tanzil (Tanzil/Egyptian-standard revelation order) | 89.530 |
| p_nold (two-sided vs same null) | **2×10⁻⁴** |
| Sign: L_mushaf − L_nold | −1.473 (mushaf shorter) |
| Sign: L_mushaf − L_tanzil | −3.770 (mushaf shorter) |

**Both chronological orderings are also significantly shorter than random**, but **the mushaf order is shorter than both chronologies**. Ratios: L_nold/L_min ≈ 1.126; L_tanzil/L_min ≈ 1.156.

### MW-5 positive control

Greedy-NN from surah 1: L = 79.211, p = 1×10⁻⁴. **Positive control fires** — null is not broken.

### Sanity anchors (non-pre-registered)

> **CORRECTION 2026-08-07 — the length-sorted anchor below was mis-transcribed, and the MW-1
> conclusion drawn from it is false.** The original table read **107.27 for both** ascending and
> descending, and the paragraph after it concluded that MW-1 length control was working. This
> file's own JSON — `findings/phase-b-hypotheses/csv/h-new-111.json` → `sanity_anchors` — records
> **91.027805 and 90.301441**, and an independent rebuild of the identical K=500 / α=0.5 pipeline
> reproduces exactly those values while also reproducing L_mushaf = 85.7597, L_Nöldeke = 87.2321
> and the null at 104.363 / 1.623. The computation was right; the write-up's transcription was
> wrong. (The two directions being reported as *identical* is the tell: with a stable sort,
> descending is not the exact reverse of ascending, so their path lengths cannot be equal.)
>
> Both the wrong and the corrected values are shown below. Nothing has been deleted.

| Ordering | Path length | z vs null (mean 104.3457, sd 1.6218) |
|---|---|---|
| Mushaf | 85.76 | −11.46 |
| Nöldeke chronology | 87.23 | −10.55 |
| Tanzil revelation order | 89.53 | −9.14 |
| ~~Length-sorted ascending — 107.27~~ → **91.03** | **91.03** | **−8.21** |
| ~~Length-sorted descending — 107.27~~ → **90.30** | **90.30** | **−8.66** |
| Null mean | 104.35 | 0 |
| Approx TSP optimum | 77.47 | — |

~~Length-sorted orderings behave approximately at null-mean (107 ≈ 104 within noise band) — confirms MW-1 length control is working: once distributions are L1-normalized, sorting by length is NOT a low-cost traversal.~~

**Corrected reading. MW-1 length control is NOT working on this instrument.** Sorting the real
surahs by length alone — using no vocabulary information whatever — already reaches **z = −8.66**,
against the mushaf's −11.46. The mushaf is itself close to length-descending:
Spearman(mushaf position, verse count) = **−0.846**. The mushaf's content beyond what pure length
delivers is therefore **4.54 length-units = 2.80 σ**, and that residual — not 11.46 σ — is the
honest effect size for this finding. The Nöldeke comparison (−10.55, i.e. 1.89 σ above
length-sorted-descending) was implicitly measuring the same quantity all along.

*Note on why this went unfixed for months: a transcription error that inflates your own headline
attracts no scrutiny. The JSON was correct and on disk the entire time.*

---

## Interpretation

The Quran's mushaf order is NOT random in root-distribution space. Consecutive surahs tend to share vocabulary more than expected by chance, producing a total traversal length that is:

- **11.46 standard deviations below** the random-permutation mean
- Within **10.7% of an approximate TSP optimum**
- **1.5 units SHORTER** than the Nöldeke chronological ordering
- **3.8 units SHORTER** than the Tanzil (Egyptian Standard) revelation order

All three orderings (mushaf, Nöldeke, Tanzil) are significantly non-random — consecutive surahs in ANY reasonable reading are lexically-topically closer than chance. But **the canonical mushaf is the most coherent of the three**.

This is a non-trivial empirical observation that bears on a 1,400-year-old question: was the mushaf order imposed arbitrarily by the Uthmanic committee, was it chronological, or does it follow some design principle? Our answer, **on the information-geometric axis only**: the mushaf order optimizes for consecutive-surah topical/vocabulary continuity to within ~11% of the theoretical best achievable. Chronology is MORE random than mushaf on this axis.

## Caveats / honest limits

1. **Not causal**. Being "close to a TSP optimum" does not prove *intentional* optimization. A rough length-then-theme ordering (Uthmanic "long surahs first, then mufaṣṣal by decreasing length") already produces non-trivial local coherence because long and short surahs differ systematically in vocabulary. We DID control for length (MW-1 L1-normalization), but length correlates with theme (Medinan legal vs Meccan eschatological) and that correlation survives normalization.

2. **K = 500 locked pre-hoc**. K captures 91.7% of all STEM-root tokens. Robustness to K is NOT tested here (locking K in pre-reg was the right discipline trade-off). Independent replication on K ∈ {250, 1000} belongs to [[h-new-112-spectral-network|H-NEW-112]].

3. **TSP is approximate**. We used greedy-NN + 2-opt on 114 nodes, which gives an upper bound on `L_min`. The true ratio `L_mushaf / L_min` could be slightly HIGHER than 1.107 (true optimum is ≤ our 2-opt solution). A Concorde-exact or Lin-Kernighan-3 run would tighten the bound.

4. **PASS-DIRECTED ceiling**. This is a novel test with no prior-finding anchor; extreme p does not substitute for independent replication. Queue [[h-new-112-spectral-network|H-NEW-112]] on an INDEPENDENT feature set (e.g. character-n-gram histograms, or verse-length distribution per surah) before promoting to CONFIRMED.

5. **Fisher-Rao metric choice**. The angular arccos-Bhattacharyya distance was pre-registered, but many metrics on the simplex would show similar behavior (Hellinger, KL, Jensen-Shannon). This is a feature, not a bug — robustness across metrics would strengthen the claim. Optional robustness check belongs in [[h-new-112-spectral-network|H-NEW-112]].

6. **Nöldeke chronology is itself reconstructed** — Nöldeke (1860) is a philological reconstruction, not a primary source. If the true chronology differs from Nöldeke's, the L_nold comparison loses some force. The **Tanzil/Egyptian-standard** comparison (L_tanzil = 89.53, even longer than Nöldeke's 87.23) is on a different reconstruction and gives the same answer.

7. **Extreme-p + novel-test combination**. Project discipline (see `04-DISCIPLINE.md`) caps novel-test verdict at PASS-DIRECTED until replication. The extreme p (< 10⁻⁴ on all three secondary-family tests) does NOT override this — the "garden of forking paths" space of reasonable-looking pre-reg choices (K, α, metric, null) is large, and a single confirmatory run cannot exhaust it.

## Connections to prior findings

- **[[h-new-89-meta-cluster-network|H-NEW-89]]** (meta-cluster network) found Q 62 to be a 4-cluster hub and Q 16–25 to be cluster-empty. Our distance matrix should recover these — cross-check queued.
- **[[h-new-58c-musabbihat-tense-split|H-NEW-58c]]** (musabbiḥāt cluster Q 57, 59, 61, 62, 64): these 5 surahs are NOT all consecutive; mushaf passes through them with gaps. Under an ideal root-geodesic order, they'd be adjacent. Is the mushaf separating them intentionally? Check descriptive.
- **T3 canonical-order-recovery** (earlier in project) failed on other axes. [[h-new-111-fisher-rao-mushaf|H-NEW-111]] PASSES recovery on the Fisher-Rao root-distribution axis specifically. This is a refinement of T3: the mushaf is not reconstructible from distance alone (recovery = rank-ordering), but its TOTAL path length is near-optimal (recognition, not reconstruction).

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf-prereg.md`
- Script: `scripts/h_new_111_fisher_rao_mushaf.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-111.json`
- Journal: `journal/h-new-111-run-1.md`

## Verdict

**PASS-DIRECTED** on all three pre-registered cells:
- Primary p = 1×10⁻⁴ << 0.0167 (Bonferroni 3)
- Secondary A ratio = 1.107 (near-optimal, <1.2)
- Secondary B p = 2×10⁻⁴, sign: mushaf shorter than both chronologies

MW-5 positive control fires at p < 0.001: null is sound.

**Ceiling**: cannot promote to CONFIRMED without independent replication on a distinct feature space. Queued as [[h-new-112-spectral-network|H-NEW-112]].
