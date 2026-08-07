---
finding_id: H-NEW-2570
title: Is the mushaf order a lexical curriculum? Vocabulary-introduction geometry under Heaps' law
status: "NULL (primary) + PRE-COMMIT VIOLATION (H2 reversal) + LENGTH ARTIFACT (secondary statistic)"
phase: B+
date: 2026-08-07
author: Waiel Al-Shujaa
seed: 20260509 (replication 20260519)
n_perm: 10000
prereg: findings/phase-b-hypotheses/prereg-h-new-2570-lexical-curriculum.md
prereg_sha256: 6a1cab4cddb21d0621ffff6d9d57aa974bf7eaa76b865da67ac830a3f1f4e29b
amendment: findings/phase-b-hypotheses/prereg-h-new-2570-amendment-01.md
amendment_sha256: 4cd628aaea6c6ce468df47533ffa1a3de80a55366938b6783a2d7cfade49d9ca
parent_finding: H-NEW-123 (corpus-level Heaps β; Cell B ordering-sensitivity NULL)
rules_tuple: "T1 (QAC v0.4 ROOT, root-bearing segments, Hafs-Kūfan) + T2 (QAC v0.4 LEM) + T3 (normalized surface word-form, cross-corpus only)"
bonferroni_k: 12
alpha_corrected: 0.0041667
verdict: NULL
---

# H-NEW-2570 — The mushaf order is **not** a lexical curriculum

## Scope: this is a claim about ORDERING, not about the corpus exponent

The corpus-level Heaps exponent is **not** this finding's subject. It was established on
2026-04-17 by the parent finding [[h-new-123-heap-law|H-NEW-123]] (Qurʾān β = 0.7468, 95% CI
0.729–0.757, N = 77,797, V = 14,870; al-Bukhārī matched-77K β = 0.7472 — a tie, Cell A1 FAIL) and
is recorded in `findings/HONEST-LIMITS-LEDGER.md` §27e as **not Qurʾān-distinctive**.
H-NEW-2570 does not re-derive it. See Amendment 01 for the full prior-art disclosure and scope
narrowing.

What H-NEW-2570 tests is the **sequence of the 114 surahs**. The distinction is exact:

> Every permutation of the surahs uses the **identical token multiset** — identical N, identical
> V(N_tot), identical type-frequency spectrum. **β is precisely the quantity that ordering
> leaves nearly invariant** (H-NEW-123 Cell B, p = 0.3340, NULL). The statistics used here —
> **J** (power-law-residual jerk) and **A** (deviation from the fitted Heaps curve) — measure the
> *shape of the path* V(N) traces between fixed endpoints, which is the information β discards.

Cells 1–10 are therefore orthogonal to H-NEW-123 by construction. Cells 11–12 are not: Amendment
01 §2.2 reclassifies them as a **replication of H-NEW-123 Cell B** at the surah-permutation
level, and their novelty claim is withdrawn.

## Headline

**NULL.** The pre-registered primary hypothesis fails, and it fails cleanly: the rate at which
the mushaf introduces new vocabulary to a reader moving through it from token 1 to token 49,968
is **statistically indistinguishable from chance** — not merely indistinguishable from
length-matched chance, but indistinguishable from a plain uniform permutation of the 114 surahs
as well.

| Primary cell (J, mushaf vs **length-preserving** null) | z | p | α_bonf | |
|:--|--:|--:|--:|:-:|
| T1 (QAC ROOT) | **+0.01** | 0.581 | 0.00417 | FAIL |
| T2 (QAC LEMMA) | **+1.05** | 0.842 | 0.00417 | FAIL |

Both z-scores are on the **wrong side of zero**: the mushaf's vocabulary-introduction curve is
if anything marginally *jerkier* than length-matched chance, not smoother. The replication seed
(20260519) reproduces both (p = 0.591 and 0.842).

And a second, independent negative result carries equal weight:

> **The chronological orderings are the smoother lexical curriculum, not the mushaf.**
> This is a **pre-commit violation** — the direction was locked the other way, on the strength
> of pillar law [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — and it is published here as such.

---

## 1. What was tested

[[h-new-111-fisher-rao-mushaf|H-NEW-111]] established pillar law #2: the mushaf order is
information-geodesic-optimal under Fisher-Rao distance on surah root-distributions
(L_mushaf = 85.760, z = −11.46, 0/10,000 permutations shorter; and
L_mushaf < L_Nöldeke = 87.232 < L_Tanzil = 89.530). That instrument is **pairwise**: it measures
how similar each surah is to the one next to it.

H-NEW-2570 asks the orthogonal **cumulative-lexical** question. For an ordering of the 114
surahs, let V(N) = the number of distinct roots (or lemmas) among the first N tokens. Because
every ordering uses the identical multiset of tokens, **every ordering's curve has identical
endpoints** — V(0) = 0 and V(49,968) = 1,642. Orderings differ only in the *shape of the path
between fixed endpoints*. Heaps' law (V ≈ K·N^β) supplies the expected shape; the residual
around it is the object of interest.

A *curriculum* introduces material at a controlled, steady rate. The empirical content of "is
the mushaf a lexical curriculum?" is therefore: **is its V(N) less bursty around its own Heaps
law than comparable orderings?**

Three statistics, evaluated at M = 50 **geometrically spaced** token counts from N₀ = 500 to
N_tot (so that a pure power law is exactly a straight line with zero second differences at
every scale — see pre-reg §3 for why equal-N blocks were rejected as head-dominated):

- **J** — power-law-residual jerk, Σ (log V_{j+1} − 2 log V_j + log V_{j−1})². Lower = smoother.
- **A** — mean |residual| from the per-ordering OLS Heaps fit. Lower = cleaner power law.
- **β** — the fitted Heaps exponent. Higher = novel vocabulary *deferred* rather than front-loaded.

---

## 2. The length confound, and why the primary null is length-preserving

The pre-registration names surah length as **the** threat to validity (§1) and builds the design
around it, before any computation. The mushaf is roughly long-to-short ordered — the
post-hoc diagnostic quantifies this starkly:

| Ordering | first 10 positions | last 30 positions |
|:--|:--|:--|
| **mushaf** | **18,109 tokens → 1,020 new roots** | 905 tokens → 36 new roots |
| revelation (Tanzil) | 839 tokens → 357 new roots | 20,357 tokens → 207 new roots |
| Nöldeke | 364 tokens → 206 new roots | 24,717 tokens → 234 new roots |

The mushaf spends 36% of the corpus and 62% of the entire root inventory in its first ten
positions; the chronologies invert this completely. **Any statistic on the token axis will
separate these orderings from each other and from a uniform permutation on length alone, with
no lexical content whatsoever.**

The primary null is therefore **N2, a length-stratified permutation null**: surahs are ranked
by token count and cut into 19 strata of 6; positions are re-assigned only *within* strata, so
every position receives a surah of near-identical length to the one it originally held. The
base ordering's length profile — and hence its surah-boundary-density profile — is preserved.
The uniform-permutation null N1 is registered but was **declared insufficient in advance**.

---

## 3. Results — all 12 registered cells

α_corrected = 0.05/12 = 0.0041667. Directions locked in pre-reg §5. Primary seed shown;
the replication seed agrees on every cell to within 0.002 in p.

### T1 — QAC ROOT (49,968 tokens, 1,642 types)

| # | Stat | Ordering | Null | Locked | obs | null mean | z | p | Verdict |
|:-:|:--|:--|:--|:--|--:|--:|--:|--:|:--|
| **1** | J | mushaf | **N2 length-pres.** | lower | 0.014060 | 0.014036 | **+0.01** | 0.581 | **FAIL — direction violated** |
| 2 | J | mushaf | N1 uniform | lower | 0.014060 | 0.014107 | −0.01 | 0.554 | FAIL |
| 3 | J | revelation | N1 uniform | lower | 0.010827 | 0.014107 | −0.80 | 0.211 | FAIL |
| 4 | J | revelation | N2′ length-pres. | lower | 0.010827 | 0.011470 | −0.20 | 0.477 | FAIL |
| 5 | J | mushaf | N3 scrambled | **higher** | 0.014060 | 0.005577 | **+4.97** | **0.00040** | **PASS (control)** |
| 6 | A | mushaf | **N2 length-pres.** | lower | 0.019823 | 0.035949 | −1.63 | 0.064 | FAIL |
| 7 | A | mushaf | N1 uniform | lower | 0.019823 | 0.056784 | −2.34 | **0.00140** | **PASS** |
| 8 | A | revelation | N1 uniform | lower | 0.084657 | 0.056784 | +1.76 | 0.955 | FAIL — direction violated |
| 9 | A | revelation | N2′ length-pres. | lower | 0.084657 | 0.080050 | +0.49 | 0.698 | FAIL — direction violated |
| 10 | A | mushaf | N3 scrambled | higher | 0.019823 | 0.059181 | −6.04 | 1.000 | **FAIL — control direction violated** |
| 11 | β | mushaf | N2 length-pres. | higher | 0.417714 | 0.426083 | −0.74 | 0.691 | FAIL — direction violated |
| 12 | β | mushaf | N1 uniform | higher | 0.417714 | 0.429202 | −0.57 | 0.692 | FAIL — direction violated |

### T2 — QAC LEMMA (74,608 tokens, 4,832 types)

| # | Stat | Ordering | Null | Locked | obs | null mean | z | p | Verdict |
|:-:|:--|:--|:--|:--|--:|--:|--:|--:|:--|
| **1** | J | mushaf | **N2 length-pres.** | lower | 0.017667 | 0.014932 | **+1.05** | 0.842 | **FAIL — direction violated** |
| 2 | J | mushaf | N1 uniform | lower | 0.017667 | 0.016468 | +0.27 | 0.654 | FAIL — direction violated |
| 3 | J | **revelation** | N1 uniform | lower | 0.006896 | 0.016468 | **−2.17** | **0.00120** | **PASS** |
| 4 | J | revelation | N2′ length-pres. | lower | 0.006896 | 0.011393 | −1.47 | 0.042 | FAIL (directional) |
| 5 | J | mushaf | N3 scrambled | **higher** | 0.017667 | 0.004999 | **+8.10** | **0.00010** | **PASS (control)** |
| 6 | A | mushaf | N2 length-pres. | lower | 0.030991 | 0.032428 | −0.13 | 0.420 | FAIL |
| 7 | A | mushaf | N1 uniform | lower | 0.030991 | 0.049723 | −1.24 | 0.102 | FAIL |
| 8 | A | revelation | N1 uniform | lower | 0.093460 | 0.049723 | +2.90 | 0.996 | FAIL — direction violated |
| 9 | A | revelation | N2′ length-pres. | lower | 0.093460 | 0.084850 | +0.92 | 0.820 | FAIL — direction violated |
| 10 | A | mushaf | N3 scrambled | higher | 0.030991 | 0.056016 | −4.03 | 1.000 | **FAIL — control direction violated** |
| 11 | β | mushaf | N2 length-pres. | higher | 0.586220 | 0.588482 | −0.30 | 0.603 | FAIL — direction violated |
| 12 | β | mushaf | N1 uniform | higher | 0.586220 | 0.596271 | −0.56 | 0.692 | FAIL — direction violated |

**Four of 24 tuple-cells pass at α_bonf, and two of those four are the instrument control**
(cell 5, both tuples). The two substantive passes are cell 7 at root level — which its own
length control in cell 6 then kills (§6) — and cell 3 at lemma level, which is a pass for the
**revelation order**, not the mushaf.

---

## 4. H1 — NULL, and not even a length artifact

The pre-registered decision rule (§1 of the pre-reg) anticipated that the effect might survive
the naive null and die under the length-preserving null, in which case the headline was to be
"NULL — LENGTH ARTIFACT". **The J result is weaker than that.** It dies under *both* nulls:

- vs length-preserving N2: T1 z = +0.01, T2 z = +1.05
- vs uniform N1: T1 z = −0.01, T2 z = +0.27

Across the full robustness sweep (5 evaluation grids × 2 tuples = 10 settings), J for the
mushaf against N2 held the locked direction in **4 of 10**, with z ranging from −0.67 to +1.50.
That is exactly what noise looks like. The equal-N-block variant named in the task brief
(J_lin, B ∈ {100, 200, 400}) agrees: against N2, best p = 0.0104 (T1, B=400), all others
0.28–0.87.

**The prediction that failed was a principled one.** H-NEW-111 shows adjacent mushaf surahs are
unusually close in Fisher-Rao root-distribution distance; high overlap at a boundary should mean
few unseen roots arriving at that boundary, hence no spike in the introduction rate, hence low
jerk. **That inference does not hold.** Pairwise distributional similarity between neighbouring
surahs and the smoothness of the cumulative type curve are, on this corpus, **orthogonal
properties**. Pillar law #2 does not propagate to the lexical-accumulation axis.

This is the finding's main contribution, and it is negative: **the mushaf is information-geodesic
but not pedagogic.** Whatever the canonical order optimizes, it is not the reader's rate of
vocabulary acquisition.

---

## 5. H2 — PRE-COMMIT VIOLATION: the chronologies are the smoother curriculum

Locked (pre-reg §5.2, S1/S4): J_mushaf < J_revelation, on the strength of
L_mushaf < L_Tanzil in H-NEW-111. **Observed: the reverse, under both tuples.**

| Ordering | J (T1 ROOT) | J (T2 LEMMA) | smoother than mushaf by |
|:--|--:|--:|:--|
| **mushaf** | 0.014060 | 0.017667 | — |
| revelation (Tanzil) | **0.010827** | **0.006896** | 1.30× (T1), **2.56×** (T2) |
| Nöldeke | **0.006886** | **0.008009** | **2.04×** (T1), 2.21× (T2) |

- **S1 VIOLATED** under both tuples, all 5 evaluation grids, and 5 of 6 J_lin block settings.
- **S4 VIOLATED** under both tuples (each ordering scored against its *own* length-matched null:
  z_mushaf = +0.01 / +1.05 vs z_revelation = −0.20 / −1.47; z_Nöldeke = −0.84 / −0.65).
- At the lemma level the revelation order **clears Bonferroni against the uniform null**
  (cell 3, p = 0.00120, replicated p = 0.00100).

**How much of that is length?** Cell 4 answers it: against its *own* length-matched null the
revelation order's advantage falls from p = 0.0012 to **p = 0.042** — directionally intact,
but no longer surviving correction. The chronologies front-load very short surahs (Nöldeke's
first ten positions total 364 tokens), which mechanically produces a gentler early curve. So the
honest reading is: **the chronological orderings are smoother, a substantial part of that is
their length profile, and the length-conditional remainder is suggestive but uncorrected.**

The pre-registration declared in advance that a reversal here "is a major honest finding and
will be published as the headline if it occurs" (§5.2). It occurred, and it is.

---

## 6. The A statistic — NULL, LENGTH ARTIFACT (the decision rule fires)

The mushaf's V(N) is an extraordinarily clean Heaps power law: **R² = 0.99784** (ROOT) and
**0.99797** (LEMMA), against 0.96356 / 0.98366 for the revelation order and 0.96423 / 0.98115
for Nöldeke. Its mean log-residual A is **4.27× smaller** than the revelation order's at root
level (0.019823 vs 0.084657) and 3.02× smaller at lemma level. S2 HELD under both tuples.

Against the uniform null this is significant at root level (cell 7, p = 0.00140, z = −2.34,
replicated p = 0.00210). **Against the length-preserving null it is not** (cell 6, p = 0.064).
That is precisely row 2 of the pre-registered decision table, and the verdict it prescribes is
**NULL — LENGTH ARTIFACT**.

The artifact is quantifiable. Null means for A at T1:

| Reference | A |
|:--|--:|
| uniform permutation (N1) | 0.056784 |
| **length-matched permutation (N2)** | **0.035949** |
| observed mushaf | 0.019823 |

Simply imposing the mushaf's length profile on random content closes
(0.056784 − 0.035949)/(0.056784 − 0.019823) = **56.4% of the gap**. The remaining 43.6% is
content placement, and it does not clear α_bonf.

**The decisive diagnostic is the stratum-width sweep.** Loosening the length control makes the
result significant; tightening it kills it:

| Length control | strata | A vs N2, T1 |
|:--|:--|--:|
| none (uniform null) | — | p = 0.00140 **PASS** |
| loose | 6 strata of 19 | p = 0.0035 **PASS** |
| **tight (pre-registered primary)** | **19 strata of 6** | **p = 0.064 FAIL** |

Significance that varies inversely with the strength of the length control is the signature of a
length artifact, not of a lexical law. At the lemma level the effect is absent at every level of
control (p = 0.102 / 0.420). The grid sweep confirms non-robustness: A vs N2 at T1 gives
p = 0.064, 0.069, 0.112, 0.151, and 0.735 (direction violated) across the five grids.

**Reported as NULL.** The clean-power-law observation stands as a *description* of the mushaf
curve; it is not established as a property of the ordering's content.

---

## 7. Pre-commit violations, itemised

Per Investigation Protocol §1.8, these are published without re-direction and without post-hoc
α relaxation. The pre-registration has not been edited since it was locked.

| ID | Locked | Observed | Status |
|:--|:--|:--|:--|
| Cell 1 (T1, T2) | J_mushaf below N2 | at/above N2 mean (z = +0.01, +1.05) | **VIOLATED** (ns) |
| Cell 2 (T2) | J_mushaf below N1 | above (z = +0.27) | **VIOLATED** (ns) |
| S1, S4 | J_mushaf < J_revelation | reversed, both tuples, all grids | **VIOLATED** |
| Cells 8, 9 | A_revelation below nulls | above (z = +1.76 … +2.90) | **VIOLATED** |
| Cells 11, 12 | β_mushaf above nulls | below (z = −0.30 … −0.74) | **VIOLATED** (ns) |
| **Cell 10** | **A_mushaf above N3 scrambled** | **far below (z = −6.04, −4.03)** | **VIOLATED — reasoning error** |

### The cell-10 error, stated plainly

The pre-reg argued (§4.3) that a globally shuffled token stream is "the smoothest possible
realization of Heaps' law", so real bursty text must deviate from a power law *more* than its own
shuffled tokens. **That reasoning is wrong.** A shuffled stream's type-accumulation curve is
Σ_i (1 − (1−f_i)^N), a sum of saturating exponentials — not a power law at all — and it bows
systematically away from a log-log straight line. Real text, with its Zipfian and bursty
structure, tracks a power law far *better*. The observed z = −6.04 is that known property of
natural language, not a property of the mushaf.

The control that actually validates the instrument is **cell 5**, and it fires hard: J_mushaf is
2.5–3.5× the scrambled-null mean, z = +4.97 (T1) and +8.10 (T2), p ≤ 0.0004, replicated. The
jerk statistic demonstrably responds to real lexical content — which is what makes the flat null
in cell 1 interpretable as a genuine absence of structure rather than a dead instrument.

### β — cells 11/12 replicate H-NEW-123 Cell B; S3 holds across three instruments

Cells 11/12 fail: the mushaf does **not** defer novel vocabulary relative to random or
length-matched orderings (p = 0.69, direction violated, both tuples). **Per Amendment 01 §2.2
this is a replication, not a novel result.** [[h-new-123-heap-law|H-NEW-123]] Cell B had already
found β insensitive to shuffling the Qurʾān's token stream (0.7468 vs 0.7072, p = 0.3340, NULL),
and `HONEST-LIMITS-LEDGER.md` §27e records β as stream-order invariant. A permutation of surahs
is a weaker perturbation than a full token shuffle, so a null here was the expected outcome, and
it is reported as confirmation of the parent finding rather than as a discovery.

**S3 HELD**, and now across three independent instruments: β_mushaf > β_revelation at
0.41771 vs 0.38674 (QAC ROOT, geometric grid), 0.58622 vs 0.55761 (QAC LEMMA, geometric grid),
and **0.7468 vs 0.6904** (surface form, H-NEW-123's own linear-grid estimator — §8.3). Nöldeke
sits with the revelation order in all three (0.38649 / 0.56804 / 0.6941).

Read correctly this is not the mushaf deferring — it is **the chronologies front-loading**,
exactly as [[h-new-2320-hapax-census|H-NEW-2320]] predicts, since the hapax-rich early-Meccan
surahs the mushaf places last are the ones the chronologies place first. The two facts are
consistent: the mushaf's β exceeds the chronologies' while remaining unremarkable against
permutation nulls.

---

## 8. Cross-corpus Heaps: reconciliation with the parent finding H-NEW-123

**The corpus-level Heaps exponent is [[h-new-123-heap-law|H-NEW-123]]'s result, not this
finding's.** Amendment 01 §2.1 demotes this section from *deliverable* to *consistency check*
and requires it be recomputed with **H-NEW-123's own estimator** — `normalize` / `tokenize` /
`vocab_curve` (linear grid, step = 50, start = 100) / `fit_heap` (log-log OLS), imported directly
from `scripts/h_new_123_heap_law.py` rather than reimplemented. Descriptive, MW-7 capped, no
p-value, no registered inference.

### 8.1 Reproduction — the toolchain reproduces H-NEW-123 exactly

| Corpus | N | V | β (re-run) | β (H-NEW-123 published) | Δβ |
|:--|--:|--:|--:|--:|--:|
| Qurʾān (no-tashkeel, surface-form) | 77,797 | 14,870 | 0.7468 | 0.7468 | **+0.0000** |
| al-Bukhārī, matched-77K window | 77,797 | 12,154 | 0.7472 | 0.7472 | **+0.0000** |
| Muʿallaqāt, 7 poems | 7,285 | 3,843 | 0.8313 | 0.8313 | **+0.0000** |
| al-Jāḥiẓ *al-Ḥayawān*, first 77K | 77,797 | 22,984 | 0.8023 | 0.8023 | **+0.0000** |

All four rows reproduce to four decimal places. H-NEW-123 stands unchanged and remains
authoritative for the corpus-level claim: **the Qurʾān's β is tied with Bukhārī's** (Cell A1
FAIL, p = 0.3826) and the compactness is a genre feature of classical religious prose, not a
Qurʾān-specific signature (`HONEST-LIMITS-LEDGER.md` §27e).

### 8.2 A correction to this finding's own earlier figures

An earlier draft of H-NEW-2570 reported β_Bukhārī = 0.7674 from `bukhari-noquran.txt` under a
tokenizer of my own. Two things differed from H-NEW-123: the source file (H-NEW-123 uses
`matched-bukhari-77k.txt`) and the normalization (mine folded the alif family and alif maqṣūra;
H-NEW-123's does not). Under H-NEW-123's estimator the **same** `bukhari-noquran.txt` file gives
**β = 0.7443, V = 11,766**. The 0.7674 figure was a normalization artifact and is withdrawn.

This matters in H-NEW-123's favour: the Quran-stripped Bukhārī text gives β = 0.7443 against the
Qurʾān's 0.7468 — **closer still to a tie** than H-NEW-123's own 0.7472. Cell A1's FAIL is
strengthened, not weakened, by the alternative source.

### 8.3 β by surah ordering — the ordering-invariance question, on H-NEW-123's instrument

All three rows use the **identical token multiset**, so N and V are fixed by construction and
only β and K can move:

| Ordering | N | V | β | K |
|:--|--:|--:|--:|--:|
| **mushaf** | 77,797 | 14,870 | **0.7468** | 3.311 |
| revelation (Tanzil) | 77,797 | 14,870 | 0.6904 | 6.429 |
| Nöldeke | 77,797 | 14,870 | 0.6941 | 6.238 |

The surah-ordering spread (Δβ = 0.056) is comparable to H-NEW-123's token-shuffle spread
(0.7468 → 0.7072, Δ = 0.040), which its Cell B found non-significant at p = 0.3340. Consistent
with that, cells 11/12 here find β_mushaf unremarkable against 10,000 surah-permutation nulls
(p = 0.69). **What this adds to H-NEW-123 is only the confirmation that S3's direction
(β_mushaf > β_chronologies) survives a third, independent estimator.**

### 8.4 One caveat of H-NEW-123, addressed — with a composition caveat of its own

H-NEW-123's caveats flag a length mismatch it could not remove: its poetry baseline was the
Muʿallaqāt alone at **7,285 tokens** against the Qurʾān's 77,797, *"the early-N region of the
Heap curve, which systematically gives higher β for all corpora."* It reported a post-hoc
matched-at-7.3K figure (β_Q = 0.801 vs Muʿallaqāt 0.831, gap 0.030).

Adding the seven **dīwāns** in `data/baseline-corpora/raw/` — which H-NEW-123 did not use —
gives 82,520 poetry tokens, enough to match the Qurʾān's full 77,797 for the first time:

| Corpus | N | V | β |
|:--|--:|--:|--:|
| Qurʾān | 77,797 | 14,870 | 0.7468 |
| **Pre-Islamic poetry** (7 muʿallaqāt + 7 dīwāns) | 77,797 | **25,410** | **0.9459** |

**Honest limit on this row.** It removes the length mismatch but substitutes a *different
corpus*: a 14-work, multi-author aggregate in place of a 7-poem single-genre set. Aggregating
independent poets inflates the type count because they do not share vocabulary, and V = 25,410
against the Qurʾān's 14,870 at identical N is partly that aggregation effect rather than
per-poet lexical richness. It therefore **does not cleanly resolve H-NEW-123's caveat** — it
trades a length confound for a composition confound.

What is robust is the **direction**, which now holds in all three framings: unmatched
(0.831 vs 0.747), matched-at-7.3K (0.831 vs 0.801), and matched-at-77.8K (0.946 vs 0.747).
Poetry's vocabulary expands faster than the Qurʾān's under every version of the comparison.
That direction is **H-NEW-123's Cell A3 PASS**, and this row confirms it under length-matching
rather than establishing anything new.

---

## 9. MW-protections audit

- **MW-1 (instrument-prior)**: J, A, β, the evaluation grid, and the choice of geometric over
  equal-N spacing were all fixed in the SHA-locked pre-reg before computation.
- **MW-2 (corpus-prior)**: 10,000 permutations per null, four null models.
- **MW-3 (alternative models)**: three statistics, five evaluation grids, three J_lin block
  sizes, two stratum widths, two chronologies.
- **MW-4 (over-fitting)**: β and K are re-fitted independently for every permutation; no
  parameter is carried from the observed data into the null.
- **MW-5 (replication)**: full re-run at seed 20260519 — every cell reproduces its verdict and
  its direction (max |Δp| ≈ 0.010, on cell 1 at T1: 0.581 → 0.591).
- **MW-6 (instrument-control)**: N3 content-scrambled null. Cell 5 fires at z = +4.97 / +8.10;
  cell 10's locked direction was wrong on the theory (§7).
- **MW-7 (post-hoc cap)**: §2's positional diagnostics and §8's cross-corpus table are
  descriptive only and carry no inferential weight.

## 10. Honest limits

1. **A null is not proof of absence.** J has demonstrated sensitivity (cell 5), but a
   *different* smoothness statistic could still separate the mushaf. What is established is that
   this family — jerk and Heaps-residual on the cumulative type curve, at five grids and two
   annotation levels — does not.
2. **The length-preserving null is conservative by construction.** With 19 strata of 6, the
   permutation space is local; a genuine but weak content effect could be absorbed. This is
   exactly why both stratum widths are reported (§6) — and the *direction* of the width effect
   there argues for artifact, not for suppressed signal.
3. **Cell 3 (T2) is a single surviving cell** in a family of 12 under two tuples, and it does not
   replicate at T1 (p = 0.211). It is reported as DIRECTIONAL, not confirmed.
4. **The chronologies are reconstructions.** Both the Tanzil/Egyptian standard and Nöldeke (1860)
   are philological reconstructions, not primary sources. That both give the same reversal
   (J = 0.010827 and 0.006886 vs mushaf 0.014060) strengthens the observation but does not make
   either ordering historically certain.
5. **Arabic surface-form β is normalization-sensitive, demonstrably so.** §8.2 is a worked
   example: the same Bukhārī file gives β = 0.7674 under this finding's original tokenizer and
   0.7443 under H-NEW-123's — a 0.023 shift from folding rules alone, larger than the entire
   Qurʾān-vs-Bukhārī gap being discussed. All §8 figures now use H-NEW-123's estimator so that
   the two findings are comparable; any comparison against a third study would need the same
   care.
6. **The extended poetry corpus trades one confound for another** (§8.4): it removes H-NEW-123's
   length mismatch but substitutes a 14-work multi-author aggregate for a 7-poem single-genre
   set, and multi-author aggregation inflates type counts. It mixes muʿallaqāt with later dīwān
   material of uneven provenance; it is a genre control, not a dated corpus.
7. **Cells 11/12 are a replication, not a test.** Their null outcome was predicted in advance by
   H-NEW-123 Cell B and by `HONEST-LIMITS-LEDGER.md` §27e. Amendment 01 recorded that prior
   before this document was written, precisely so the null could not be presented as a surprise.

## 11. Integration

- **[[h-new-123-heap-law|H-NEW-123]] — PARENT FINDING on this axis.** It owns the corpus-level
  exponent (Qurʾān β = 0.7468, tied with Bukhārī; §27e of the honest-limits ledger:
  not Qurʾān-distinctive). Its **Cell B NULL** — β is near-invariant to shuffling the token
  stream — is the direct prior for H-NEW-2570's result, and it was right: the ordering axis is
  null too. H-NEW-2570's contribution is to test the ordering question with statistics that β
  discards (J, A) rather than with β itself, and under a **length-preserving** null H-NEW-123 did
  not have. The two findings agree. Related: **H-NEW-159** (β per chapter), **H-NEW-172**
  (Zipf α per chapter), **H-NEW-178** ((α, β) manifold), **H-NEW-179** (predictor) — all
  per-chapter, none testing sequence.
- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** — H-NEW-2570 is its orthogonal counterpart, and
  the result is a **boundary condition on pillar law #2**: information-geodesic optimality on the
  pairwise Fisher-Rao axis does **not** imply smoothness on the cumulative-lexical axis. The
  mushaf is optimized in one geometry and unremarkable in the other. Both statements now have
  pre-registered evidence.
- **[[h-new-2320-hapax-census|H-NEW-2320]]**, **[[h-new-1540-hapax-distribution|H-NEW-1540]]** —
  the hapax-Meccan signature is confirmed *from the other side*: the chronological orderings
  front-load the hapax-rich early-Meccan surahs, which is why β_revelation < β_mushaf (S3 HELD)
  and why the chronologies' curves bow away from a power law (A 3–4× the mushaf's).
- **[[h-new-2330-lexical-burstiness|H-NEW-2330]]** — burstiness is the mechanism behind cell 5:
  real Quranic text is 2.5–3.5× jerkier than its own shuffled tokens because content roots are
  topic-locked. H-NEW-123's low Qurʾānic β is the same law at corpus scale.
- **al-Suyūṭī**, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 38 (*al-mufradāt*) and nawʿ 39
  (*al-gharīb*) — the classical rare-vocabulary genre. Its cross-corpus baseline belongs to
  H-NEW-123 (Cells A2/A3 PASS: the Qurʾānic lexicon is narrower than Jāḥiẓ's and the poets');
  §8.4 confirms the poetry leg under length-matching.
- No classical source claims the mushaf order is a vocabulary curriculum; this test invented and
  then falsified a modern hypothesis. The null does not contradict any classical position.

## 12. Files

| Artifact | Path | SHA-256 |
|:--|:--|:--|
| Pre-reg (unchanged, runtime-verified) | `findings/phase-b-hypotheses/prereg-h-new-2570-lexical-curriculum.md` | `6a1cab4cddb21d0621ffff6d9d57aa974bf7eaa76b865da67ac830a3f1f4e29b` |
| **Amendment 01** (prior art + scope narrowing) | `findings/phase-b-hypotheses/prereg-h-new-2570-amendment-01.md` | `4cd628aaea6c6ce468df47533ffa1a3de80a55366938b6783a2d7cfade49d9ca` |

The parent pre-reg is deliberately **not** edited: its hash is embedded in the run script and was
verified at runtime before the executed run, so an edit would permanently break the
reproducibility of that run. Amendment 01 is recorded alongside it as a corrigendum, changes no
threshold, null, direction, or verdict, and only narrows scope (Amendment 01 §0, §3).

- Run script: `findings/phase-b-hypotheses/scripts/h-new-2570.py` (verifies the pre-reg SHA)
- Heaps reconciliation vs H-NEW-123: `findings/phase-b-hypotheses/scripts/h-new-2570-heaps-reconciliation.py`
  (verifies both SHAs; imports the estimator from `scripts/h_new_123_heap_law.py`)
- Diagnostics (post-hoc, descriptive): `findings/phase-b-hypotheses/scripts/h-new-2570-diagnostics.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2570.json`
- Reconciliation JSON: `findings/phase-b-hypotheses/csv/h-new-2570-heaps-reconciliation.json`
- Diagnostics JSON: `findings/phase-b-hypotheses/csv/h-new-2570-diagnostics.json`
- Parent finding: `findings/phase-b-hypotheses/h-new-123-heap-law.md`

---

*H-NEW-2570 logged 2026-08-07 by Waiel Al-Shujaa. The mushaf order is a geodesic, not a syllabus.
Bismillāhi al-Raḥmāni al-Raḥīm.*
