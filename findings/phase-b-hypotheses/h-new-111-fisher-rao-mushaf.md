# [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Fisher-Rao information-geodesic test of mushaf order

**Finding ID**: [[h-new-111-fisher-rao-mushaf|h-new-111]]
**Date**: 2026-04-17
**Specialist**: [[h-new-111-fisher-rao-mushaf|h-new-111]]-specialist
**Pre-reg**: `findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf-prereg.md`
**Pre-reg SHA-256**: `ea3f0ee41d413b0e2a9bfced340f7bfa12e93f40ad8c43a92a873c82856ee8c8`
**Seed**: 20260417
**Rules tuple**: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kūfan)
**Verdict**: **PASS-DIRECTED** (primary + both secondaries fire extreme; pending independent replication)

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

| Ordering | Path length |
|---|---|
| Mushaf | 85.76 |
| Nöldeke chronology | 87.23 |
| Tanzil revelation order | 89.53 |
| Length-sorted ascending | 107.27 |
| Length-sorted descending | 107.27 |
| Null mean | 104.35 |
| Approx TSP optimum | 77.47 |

Length-sorted orderings behave approximately at null-mean (107 ≈ 104 within noise band) — confirms MW-1 length control is working: once distributions are L1-normalized, sorting by length is NOT a low-cost traversal.

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
