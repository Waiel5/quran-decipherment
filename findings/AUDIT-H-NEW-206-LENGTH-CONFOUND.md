# Audit: H-NEW-206 inference (b) is length-confounded

**Status:** DEMOTED — inference (b) withdrawn as a taxonomy result; retained as a length result.
**Found by:** the tied-outcome triage of [[TIED-OUTCOME-DEFECT]] §7.3, which reduced the whole
project's parametric risk surface to ten scripts and then to one.
**Date:** 2026-08-09

---

## 1. How the screen reached this file

`TIED-OUTCOME-DEFECT.md` §7.3 grepped every script in the project for a parametric test:

| | |
|:--|--:|
| scripts using `pearsonr` · `ttest_` · `chi2_contingency` · `f_oneway` · `linregress` | 10 |
| scripts using permutation / shuffle / seeded resampling | 454 |

Of the ten, one used a parametric test with **zero** permutation calls anywhere in the file:
`scripts/h_new_206_semi_supervised_taxonomy.py`.

The other nine all clear, and it is worth saying why, because the reasons differ:

- `h_new_150_liturgical_hub` — `linregress` is used **for residualisation**, not as a test
  (`linregress_residuals(y, x)` at line 127). The regression removes a length confound; the
  inference is one of 8 permutation calls. This is the correct pattern.
- `h_new_200_name_class_predictor` — `chi2_contingency` is **hand-written** (defined at line 60,
  not imported), and used as a *test statistic* whose null comes from 18 permutation calls. Also
  the correct pattern: a χ² number with a permutation null is not a parametric test.
- `canonical_order_followup` — `linregress` on a continuous outcome, permutation present.
- `h_new_112_spectral_network` — `chi2_contingency` present but backed by 4 permutation calls.
- `Q029_F_03_ankabut_corpus_singleton` — false positive of the keyword screen.
- `h-new-2920` / `h-new-860-1` and their post-hocs — this week's work, both routes already reported.

**A χ² statistic is not a parametric test. A χ² *p-value* is.** That distinction is what separated
one script from nine.

---

## 2. What H-NEW-206 published

From `findings/phase-b-hypotheses/h-new-206-semi-supervised-taxonomy.md` lines 27–28:

> - Inference (a) silhouette > 0.2 at α_bon = 0.0250: **PASS**
> - Inference (b) χ²(cluster × is-muq): p = 2.15e-12 at α_bon = 0.0250: **PASS**

The contingency table, from `csv/h-new-206.json`:

| cluster | non-muqaṭṭaʿāt | muqaṭṭaʿāt | % muq |
|:--|--:|--:|--:|
| 0 | 22 | 1 | 4.3% |
| 1 | 11 | **25** | **69.4%** |
| 2 | 52 | 3 | 5.5% |

Base rate is 29/114 = 25.4%. Cluster 1 is 69.4% muqaṭṭaʿāt. χ² = 53.73, dof = 2, p = 2.15×10⁻¹².

The χ² approximation itself is **valid** — minimum expected cell count is 5.85, above the
conventional 5. **The tied-outcome defect does not apply here.** This file is not that defect.

---

## 3. The actual defect: the outcome is a clustering feature

`scripts/h_new_206_semi_supervised_taxonomy.py` line 353 — `FEATURE_NAMES` contains:

```
"surah_length"
```

The clusters are built **partly on surah length**. And muqaṭṭaʿāt surahs are systematically long:

| | muqaṭṭaʿāt (29) | other (85) |
|:--|--:|--:|
| median verse count | **85** | **26** |

A ratio of **3.3×**. Nineteen of the 29 are among the 40 longest surahs.

So inference (b) reads, in substance: *surahs grouped partly by length associate with a class of
surahs that is systematically long.* That is close to circular. The p-value of 2×10⁻¹² is real
arithmetic on a question that partly answers itself.

**This is consistent with the project's standing result**, recorded four separate times, that the
muqaṭṭaʿāt axis is orthogonal to the content axis. H-NEW-206 looked like the one exception. It is
not an exception; it is a length measurement wearing a taxonomy label.

### 3.1 A second, independent flag on inference (a)

`best_silhouette` = 0.21440, tested against a fixed threshold of 0.2. But it is the **maximum over
seven candidate k values**, and the other six are:

```
k=4: 0.1327   k=5: 0.1843   k=6: 0.1664   k=7: 0.1477   k=8: 0.1615   k=10: 0.1692
```

Every one falls below the threshold. The winner clears it by 0.0144. A max-over-7 statistic
compared to a fixed cutoff with **no multiplicity accounting** is not a 0.025-level test. Inference
(a) is withdrawn as well.

---

## 4. What survives — and it is worth keeping

Strip the taxonomy claim and one fact remains, stated as what it actually is:

> **No muqaṭṭaʿāt surah is short.**
> Zero of the 29 fall among the 40 shortest surahs in the corpus.

Exact hypergeometric probability under random placement of 29 labels among 114 surahs:

```
P = C(74,29) / C(114,29) = 3.063 × 10⁻⁷        (about 1 in 3,265,000)
```

This is a **clean combinatorial fact with no model, no clustering, no parameter, and no chosen k**.
It needs no permutation null because the null is exact.

### 4.0 Threshold sensitivity — "40" was not a chosen number

A result that holds at exactly one arbitrary cutoff is a chosen threshold, not a finding. So the
cutoff was swept. `muq_in_bottom_k` is the number of the 29 falling among the *k* shortest surahs:

| k | muqaṭṭaʿāt in the k shortest | exact P | odds |
|--:|--:|--:|--:|
| 20 | 0 | 1.460×10⁻³ | 1 in 684 |
| 25 | 0 | 2.197×10⁻⁴ | 1 in 4,551 |
| 30 | 0 | 2.891×10⁻⁵ | 1 in 34,588 |
| 35 | 0 | 3.258×10⁻⁶ | 1 in 306,956 |
| 40 | 0 | 3.063×10⁻⁷ | 1 in 3,265,129 |
| 45 | 0 | 2.323×10⁻⁸ | 1 in 43,050,392 |
| **50** | **0** | **1.360×10⁻⁹** | **1 in 735,283,455** |
| 51 | 1 | — | claim fails here |

**The claim holds continuously for every k from 1 to 50 and fails only at 51.** There is no
threshold-shopping: 40 was *conservative*. The boundary is set by a single surah —

> **Q 32 (al-Sajda), 30 verses, length-rank #64 of 114** — the shortest surah in the corpus that
> opens with the disconnected letters.

So the maximal honest form of the statement is:

> **All 29 muqaṭṭaʿāt surahs fall within the 64 longest surahs of the Quran.**
> Not one of them lies in the shorter 44% of the corpus.
> Exact P = 1.360×10⁻⁹ — about **1 in 735 million**.

This is the form that should be pre-registered, because it is threshold-free: it is a statement
about where the *minimum* sits, and it quotes the surah that sets it.

### 4.1 Three honest limits on it

1. **It is a length fact, not a content fact.** Saying so is precisely what makes it survivable.
   The moment it is restated as "the muqaṭṭaʿāt mark a thematic class," it inherits the confound
   this file just documented.
2. **It is POST-HOC.** It was computed *after* seeing the confound, in the course of diagnosing it.
   Under the protocol it is an observation, not a finding. To be published as a finding it must be
   pre-registered and run on a locked rules-tuple.
3. **Novelty is UNVERIFIED.** That the muqaṭṭaʿāt open predominantly long surahs is the kind of
   thing the classical tradition may well have noted — the *exact combinatorial null* is the part
   likely to be new, not the observation. No novelty claim is made here until the tafsīr corpus at
   `data/literature/classical-tafsir/` has been searched for it.

---

## 5. The transferable rule

**If the thing you are predicting is already one of the features you clustered on, the association
you find is partly your own construction.**

Check before any cluster-versus-label test: *is the label correlated with a feature in the matrix?*
Here `surah_length` was in `FEATURE_NAMES` and the label was 3.3× longer at the median. That single
check, run before the χ², would have caught this.

This joins the four diagnosed defect classes as a specific instance of the family they share:
[[UNIT-DRIFT-DEFECT]] (a density divided by a drifting unit), [[ABSENCE-CLAIMS]] (nothing downstream
fails when an absence is wrong), [[PROXY-CLAIMS]] (a hand-assigned quantity), [[TIED-OUTCOME-DEFECT]]
(a parametric p on a mostly-tied outcome), and now this — **a feature predicting itself**.

All five are the same underlying failure: **the measurement and the thing measured were not kept
apart.**
