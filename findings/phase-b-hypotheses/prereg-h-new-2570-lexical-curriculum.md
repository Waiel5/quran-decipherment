---
prereg_id: H-NEW-2570
title: Is the mushaf order a lexical curriculum? Vocabulary-introduction geometry under Heaps' law
author: Waiel Al-Shujaa
date_locked: 2026-08-07
phase: B+
status: LOCKED — written before any hypothesis statistic was computed
seed_primary: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 12
alpha_corrected: 0.0041667
---

# PRE-REGISTRATION — H-NEW-2570

## Vocabulary-introduction geometry: is the mushaf order a lexical curriculum?

**This document is locked before computation. Its SHA-256 is embedded in
`findings/phase-b-hypotheses/scripts/h-new-2570.py` and verified at runtime; the script
aborts on mismatch.**

---

## 0. The question

[[h-new-111-fisher-rao-mushaf|H-NEW-111]] established pillar law #2: the mushaf ordering of
the 114 surahs is information-geodesic-optimal under Fisher-Rao distance on surah
root-distributions (L_mushaf = 85.760, z = −11.46, 0/10000 permutations shorter;
L_mushaf < L_Nöldeke = 87.232 < L_Tanzil = 89.530). That instrument is a **content-distribution**
instrument: it measures *pairwise* similarity between adjacent surahs.

The orthogonal **lexical** question has not been asked on this corpus: as a reader moves
through the mushaf from token 1 to token 49,968, **at what rate is new vocabulary
introduced, and is that rate smooth?**

Heaps' law states that vocabulary size grows as V ≈ K·N^β. Every ordering of the 114 surahs
produces a curve V(N) with the **same two endpoints** — V(0) = 0 and V(N_tot) = (total types),
because the multiset of tokens is identical under any permutation. Orderings therefore differ
**only in the shape of the path between fixed endpoints.** The residual structure around the
fitted Heaps curve is the object of interest.

A *curriculum* introduces new material at a controlled, steady rate: it does not dump the
whole lexicon in chapter one, nor stall and then flood. The empirical content of "is the
mushaf a lexical curriculum?" is therefore: **is the mushaf's V(N) smoother — less bursty
around its own Heaps law — than orderings that are otherwise comparable?**

---

## 1. THE PRIMARY THREAT TO VALIDITY (named first, by design)

### T-1 — SURAH LENGTH

**The mushaf is roughly long-to-short ordered.** Any statistic computed on the token axis is
sensitive to the length profile of the ordering. A uniform random permutation scatters the
long surahs; the mushaf front-loads them. Therefore **any length-sensitive statistic will
separate the mushaf from a uniform-permutation null trivially, with no lexical content
whatsoever.**

### T-2 — SURAH-BOUNDARY DENSITY

Vocabulary introduction spikes at surah boundaries (a new surah brings a new topic, hence
unseen roots — [[h-new-2330-lexical-burstiness|H-NEW-2330]]: content roots are topically
clumped ~170× beyond chance). The *total* number of boundaries (113) is invariant, but their
*distribution along the token axis* is not: long-to-short ordering makes boundaries sparse
early and dense late. This is a pure length artifact and would drive a smoothness statistic
on its own.

### CONSEQUENCE — the primary null is length-preserving

**The uniform-permutation null (N1) is registered but is explicitly declared INSUFFICIENT.**
The **primary null is N2, a length-stratified permutation null that preserves the base
ordering's length profile at every position** (§4.2).

**Decision rule, locked:**

| Cell 1 (vs N2, length-preserving) | Cell 2 (vs N1, uniform) | Published headline |
|:--|:--|:--|
| PASS | PASS | Finding: mushaf is a smoother lexical curriculum than length-matched chance |
| **FAIL** | **PASS** | **NULL — LENGTH ARTIFACT.** Headline states the effect is length-driven. |
| FAIL | FAIL | NULL |
| PASS | FAIL | Anomalous; report as NULL pending diagnosis |

A result that survives only the naive null is **not a finding** and will not be presented as one.

---

## 2. Rules-tuples

Raw substring counting is invalid on this corpus; all lexical work uses QAC v0.4 annotation.

| Tuple | Definition | Tokens | Types |
|:--|:--|--:|--:|
| **T1 (primary)** | (QAC v0.4, Buckwalter **ROOT** field, root-bearing STEM segments only, token order = (verse, word, segment) ascending, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi) | 49,968 | 1,642 |
| **T2 (replication)** | (QAC v0.4, **LEM** field, lemma-bearing segments only, otherwise identical) | 74,608 | 4,832 |
| T3 (descriptive only, §7) | (no-tashkeel, normalized orthographic word-form, whole-token) | — | — |

T1 token/type counts reproduce [[h-new-2320-hapax-census|H-NEW-2320]] exactly (49,968 / 1,642),
confirming the extraction path.

**Every inferential cell is run under BOTH T1 and T2.** A verdict of CONFIRMED requires the
locked direction to hold under both. Divergence between T1 and T2 is reported as
rules-tuple fragility with equal prominence.

---

## 3. Statistics

For an ordering π of the 114 surahs, concatenate the per-surah token sequences in order and
let V(N) = number of distinct types among the first N tokens.

**Evaluation points.** M = 50 **geometrically spaced** token counts
N_j = round(N₀ · r^(j−1)), j = 1…M, with N₀ = 500 and r = (N_tot/N₀)^(1/(M−1)).

*Why geometric and not equal-N blocks.* Heaps' law implies dV/dN ∝ N^(β−1), a steeply
decaying function. On **equal-N** blocks the second differences of V are therefore dominated
almost entirely by the first few blocks — an equal-N jerk statistic would measure "how abrupt
is the very start" and little else, and the start is exactly where the length confound (T-1)
bites hardest. On **geometric** points, log N_j is evenly spaced, so a pure power law
V = K·N^β gives log V exactly linear with **zero** second differences at every scale. The
statistic then measures departure from the power law **evenly across all scales**. This is a
mathematical property of Heaps' law, not an observation about the mushaf; the choice is made
here, before computation. (The equal-N-block jerk named in the task brief is retained and
reported as robustness variant J_lin, §6.)

### Statistic J — power-law-residual jerk (PRIMARY)

J = Σ_{j=2}^{M−1} ( log V_{j+1} − 2·log V_j + log V_{j−1} )²

**Lower J = smoother vocabulary introduction across scales = more curriculum-like.**

### Statistic A — mean absolute deviation from the fitted Heaps curve (SECONDARY)

Fit (log K, β) by OLS of log V_j on log N_j over the same M points, per ordering. Then

A = (1/M) Σ_j | log V_j − (log K + β·log N_j) |

This is the "area between V(N) and the fitted Heaps curve" of the task brief, in log space.
**Lower A = closer to a pure Heaps law.**

### Statistic β — fitted Heaps exponent (TERTIARY, deferral test)

β = the OLS slope above. Because V(N_tot) is **identical for every ordering**, β is a pure
measure of *when* the vocabulary arrives: an ordering that front-loads novel vocabulary has
large K and small β; an ordering that **defers** novel vocabulary has small K and **large β**.

---

## 4. Null models

All nulls: 10,000 draws, seed 20260509; full replication at seed 20260519.

### 4.1 N1 — UNIFORM permutation (registered, declared insufficient)

Uniform random permutation of the 114 surahs.

### 4.2 N2 — LENGTH-STRATIFIED permutation (**PRIMARY NULL**)

1. Let ℓ(s) = token count of surah s under the active tuple.
2. Sort all 114 surahs by (ℓ(s) descending, s ascending); rank ρ(s) ∈ {0…113}.
3. Stratum g(s) = ρ(s) // 6, giving **19 strata of exactly 6 surahs** (114 = 19 × 6).
4. Given a base ordering π₀ (mushaf for cells 1/6/11; revelation order for cells 4/9), for
   each stratum g collect the positions P_g = { i : g(π₀[i]) = g } and the members
   M_g = { π₀[i] : i ∈ P_g }. Permute M_g uniformly at random and re-assign to P_g in order.

**Every position receives a surah from the same length stratum it originally held.** The
ordering's length profile — and hence its surah-boundary-density profile (T-2) — is preserved
to within one stratum at every position. The identity permutation (the base ordering itself)
is in the support of N2, so the p-value is an exact rank-based permutation p-value.
Support size = (6!)^19 ≈ 10^49; 10,000 draws sample it without collision risk.

N2′ denotes N2 with the revelation order as base ordering.

### 4.3 N3 — CONTENT-SCRAMBLED control (MW-6 instrument control)

Uniformly permute the entire corpus token stream, then re-cut it at the mushaf's surah-length
boundaries in mushaf order. Preserves total tokens, the per-position length profile, and the
exact corpus type-frequency spectrum; destroys topical clumping and all ordering.

A globally homogenized stream is the smoothest possible realization of Heaps' law. Real
text, being bursty ([[h-new-2330-lexical-burstiness|H-NEW-2330]]), must therefore score
**HIGHER** on J and A than N3. **This control is expected to fire trivially; its purpose is
to prove the statistics respond to lexical content and not merely to the length profile.**
If it fails, the whole instrument is invalid and the finding is void.

---

## 5. Registered inferences — directions LOCKED

Orderings tested: **mushaf** (1…114) and **revelation order** (Tanzil / Egyptian standard,
`revelation_order` column of `data/revelation-order.csv`; Nöldeke as robustness, §6).

All p-values are one-sided permutation p-values in the locked direction,
p = (1 + #{null at least as extreme}) / (1 + n_perm).

**Bonferroni k = 12, α_corrected = 0.05/12 = 0.0041667.**

| # | Statistic | Ordering | Null | LOCKED DIRECTION | Hypothesis |
|:-:|:--|:--|:--|:--|:--|
| **1** | **J** | **mushaf** | **N2 (length-preserving)** | **mushaf LOWER** | **H1 PRIMARY** |
| 2 | J | mushaf | N1 (uniform) | mushaf LOWER | H1 naive |
| 3 | J | revelation | N1 | revelation LOWER | H2 |
| 4 | J | revelation | N2′ | revelation LOWER | H2 |
| 5 | J | mushaf | N3 (scrambled) | mushaf **HIGHER** | MW-6 control |
| 6 | A | mushaf | N2 | mushaf LOWER | H1 |
| 7 | A | mushaf | N1 | mushaf LOWER | H1 naive |
| 8 | A | revelation | N1 | revelation LOWER | H2 |
| 9 | A | revelation | N2′ | revelation LOWER | H2 |
| 10 | A | mushaf | N3 | mushaf **HIGHER** | MW-6 control |
| 11 | β | mushaf | N2 | mushaf **HIGHER** | H-DEFER |
| 12 | β | mushaf | N1 | mushaf **HIGHER** | H-DEFER |

### 5.1 Justification of each locked direction

**Cells 1–4 (J LOWER for mushaf and for revelation order).**
[[h-new-111-fisher-rao-mushaf|H-NEW-111]] showed that consecutive surahs in the mushaf are
closer in Fisher-Rao distance on root-distributions than chance permits, and that the two
chronological orderings are *also* significantly shorter than random (p_nold = 2×10⁻⁴). Low
Fisher-Rao distance between adjacent surahs means high root-distribution overlap; high overlap
means that on crossing a surah boundary, few of the incoming surah's roots are unseen; few
unseen roots means **no spike in the new-root rate at the boundary**; no spikes means **low
jerk**. The mechanism transfers directly. Both the mushaf and the revelation order are
therefore predicted to be smoother than their respective nulls.

**Cells 6–9 (A LOWER), same mechanism**: an ordering whose boundaries do not produce novelty
bursts tracks its own power law more closely.

**Cells 11–12 (β HIGHER for the mushaf).**
[[h-new-2320-hapax-census|H-NEW-2320]] and [[h-new-1540-hapax-distribution|H-NEW-1540]]
established that corpus-singleton (hapax) roots concentrate overwhelmingly in the short
early-Meccan surahs — Meccan hapax rate 0.02808 vs Medinan 0.00677 (>4×, p = 0.0012); all ten
top-hapax-density surahs are Early Meccan; 31 of the 40 surahs at ≥2× baseline density are
Early Meccan. **The mushaf places those surahs at its END.** The mushaf therefore *defers* its
rarest vocabulary. With V(N_tot) fixed, deferral means the curve sits lower at small N, which
with a free intercept means a **larger** fitted exponent β. Locked: β_mushaf higher than both
nulls.

**Cells 5, 10 (mushaf HIGHER than the scrambled control).** A globally homogenized token
stream is the smoothest attainable Heaps realization; real, topically bursty text
([[h-new-2330-lexical-burstiness|H-NEW-2330]], 22 single-surah burst roots vs null mean 0.13)
must exceed it on both roughness statistics.

### 5.2 Locked SIGN predictions (binary; no p-value, no α — reported HELD or VIOLATED)

These are the H2 "mushaf vs revelation" comparisons proper. A single pair of orderings admits
no permutation p-value; each is a pre-committed binary with a 50% prior, and its evidential
weight comes from holding across all robustness settings of §6, not from an α.

| ID | Prediction | Basis |
|:-:|:--|:--|
| **S1** | J_mushaf < J_revelation | L_mushaf (85.76) < L_Tanzil (89.53) in H-NEW-111 |
| **S2** | A_mushaf < A_revelation | same |
| **S3** | **β_mushaf > β_revelation** | mushaf defers the hapax-rich early-Meccan surahs that the revelation order front-loads (H-NEW-2320) |
| **S4** | z_J(mushaf \| N2) < z_J(revelation \| N2′) | length-controlled form of S1: each ordering scored against its **own** length-matched null, then compared |

**S4 is the decisive form of H2.** The mushaf and the revelation order have genuinely
different length profiles and cannot be length-matched to each other; scoring each against its
own length-matched reference and comparing the standardized deviations is the only
length-controlled comparison available. **A reversal on S4 is a major honest finding and will
be published as the headline if it occurs.**

---

## 6. Robustness sweep (no independent α; stability only)

The locked direction must hold across **all** of the following for a CONFIRMED verdict:

- Tuples: T1 (ROOT) and T2 (LEMMA)
- Seeds: 20260509 and 20260519
- Evaluation grid: M ∈ {30, 50, 80}; N₀ ∈ {200, 500, 1000}
- Alternative chronology: Nöldeke (`noldeke_order`) in place of Tanzil
- Loose strata: 6 strata of 19 in place of 19 strata of 6
- **J_lin**: the equal-N-block jerk named in the task brief,
  J_lin = Σ_{b=2}^{B−1} (V_{b+1} − 2V_b + V_{b−1})² over B equal token-blocks, B ∈ {100, 200, 400},
  same locked directions, reported with its head-domination caveat (§3)

---

## 7. Descriptive deliverable — cross-corpus Heaps exponents (MW-7 capped, NO inference)

Report β, K, R² for:

- Quran, T1 (QAC ROOT), mushaf order
- Quran, T2 (QAC LEM), mushaf order
- Quran, T3 (normalized surface word-form), mushaf order
- **Pre-Islamic poetry**, T3 — `data/baseline-corpora/raw/muallaqa-*.txt` + `diwan-*.txt`
  (14 files, `.raw.`/`.openiti.` excluded), concatenated in sorted filename order
- **al-Bukhārī**, T3 — `data/baseline-corpora/raw/bukhari-noquran.txt` (Quran quotations stripped)

**Heaps β is not comparable across corpora of different size.** All cross-corpus fits are
therefore reported at a **matched N_common = 77,000 surface tokens** (Quran 77,797; poetry
82,520; Bukhari 526,250 — all exceed it), over geometric points from N₀ = 500 to N_common.
Full-corpus fits are reported separately and labelled as non-comparable.

T3 normalization, fixed here: NFC; delete U+0610–U+061A, U+064B–U+065F, U+0670, U+06D6–U+06ED,
U+0640; map U+0622/U+0623/U+0625/U+0671 → U+0627 and U+0649 → U+064A; tokenize on maximal runs
of U+0621–U+064A.

This section is **descriptive**. No hypothesis is registered on it and no p-value is computed
for it.

---

## 8. Success / failure criteria

**CONFIRMED** requires all of:
1. Cell 1 (J, mushaf vs length-preserving N2) passes at p ≤ 0.0041667 in the locked direction;
2. under **both** T1 and T2;
3. across every robustness setting of §6;
4. MW-6 control cells 5 and 10 fire in their locked direction.

**DIRECTIONAL** — cell 1 passes under T1 but not T2, or fails part of the robustness sweep.

**NULL — LENGTH ARTIFACT** — cell 2 passes and cell 1 fails. Published as the headline, with
the length confound named as the cause.

**NULL** — cell 1 fails and cell 2 fails.

**PRE-COMMIT VIOLATION** — any cell whose observed effect runs opposite to the locked
direction is published as a violation with explicit label, with no post-hoc re-direction and
no post-hoc α relaxation. Per §1.8 of the Investigation Protocol the pre-reg is **not** edited
after observation.

---

## 9. Garden-of-forking-paths log (written before the run)

Inspected before locking, to size the computation only:

- QAC segment count (128,219), root-bearing token count (49,968), root type count (1,642),
  lemma-bearing token count (74,608), lemma type count (4,832), per-surah token counts,
  sum-of-per-surah-type-counts (17,496 / 26,636).
- Coverage checks on `data/revelation-order.csv` (114 rows; `mushaf_order`, `revelation_order`
  and `noldeke_order` each a permutation of 1…114).
- Surface-token counts for the three T3 corpora (77,797 / 82,520 / 526,250), to fix N_common.
- One timing benchmark of the curve routine on random permutations.

**No value of J, A, β, or any comparison between orderings was computed before this document
was locked.** The choice of geometric over equal-N evaluation points (§3) was made from the
analytic form of Heaps' law, not from inspection of the mushaf curve.

Deviation from the task brief, declared: the brief proposed the equal-N-block jerk as the
candidate primary statistic. It is demoted to robustness variant J_lin for the reason given in
§3 (equal-N second differences are head-dominated under any power law, and the head is where
the length confound is strongest). The brief's second candidate — area between V(N) and the
fitted Heaps curve — is registered as statistic A.

---

## 10. Files

- Pre-reg (this file): `findings/phase-b-hypotheses/prereg-h-new-2570-lexical-curriculum.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2570.py` (SHA-verified at runtime)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2570.json`
- Findings: `findings/phase-b-hypotheses/h-new-2570-lexical-curriculum.md`

---

*Locked 2026-08-07 by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
