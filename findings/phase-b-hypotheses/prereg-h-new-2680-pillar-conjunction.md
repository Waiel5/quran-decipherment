---
finding_id: H-NEW-2680
title: Pre-registration — joint improbability of the four pillar laws holding of one book
author: Waiel Al-Shujaa
date: 2026-08-07
status: PRE-REGISTERED — locked before any synthetic-corpus statistic was evaluated
phase: C
seed_primary: 20260509
seed_replication: 20260519
rules_tuple: (no-tashkeel, QAC v0.4 ROOT/STEM-ROOT, orthographic-token for baselines, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)
---

# H-NEW-2680 — Pre-registration

## 0. The question

The project holds four standing pillar laws (MASTER-FINDINGS-LEDGER §10.72):

| # | Law | Anchor | Published strength |
|:-:|---|---|---|
| **L1** | Muqaṭṭaʿāt are book-introduction markers | `findings/cross-finding/muqattaat-book-introduction-marker-synthesis.md` (cross-finding-008), H-NEW-53/56 | hypergeometric p = 3.17×10⁻¹² |
| **L2** | Mushaf order is information-geodesic-optimal under Fisher-Rao | `findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf.md`, `csv/h-new-111.json` | z = −11.46, 0/10 000 perms shorter |
| **L3** | Content structure is pericope-scoped, not surah-scoped | `cf-025-formal` (`cross-finding-025-formal-scale-of-aggregation-law.md`), as bounded by `cf-026-formal` | 5/5 cross-pericope marker-cohesion flips |
| **L4** | Title-density independence | `h-new-1820-title-density-independence-formal.md` | 48/89 non-rank-1 (corrected 2026-08-07 from 47/89) |

Each was established separately. **The probability that one book satisfies all four simultaneously has never been evaluated.** This pre-registration locks the attempt.

### 0.1 Why the four p-values may not be multiplied

Stated here so that the prohibition is on the record before any number is produced:

1. All four are computed on the **same 6 236 verses**. They are not independent draws.
2. Surah length, chronology and genre feed several of them.
3. L2 and L3 both concern content-distribution geometry and are plausibly correlated.
4. **The four nulls are not commensurable in kind.** L1's null randomises a *label*; L2's null randomises an *order*; L3's null re-draws *windows*; L4 has **no null model at all** — its published statement ("independent at p ≈ 50:50") is a point estimate against an unstated reference.

Item 4 is the deepest problem and is addressed head-on in §1.

### 0.2 Roster note on L3 — 5, not 6

`cf-026-formal` (2026-05-29) reclassified the 6th member of the pericope-flip roster (ring-composition, Q002-F-07) as a single-instance existence proof rather than a generalising flip, on the evidence of H-NEW-2220 (0/6 541 windows survive Bonferroni; corpus anti-chiastic) and H-NEW-2290. **This pre-registration therefore operationalises L3 on the 5 surviving cross-pericope marker-cohesion classes, not 6.** Using 6 would test a member the project has already retired.

---

## 1. The invariance analysis that governs the design

Before choosing a null, we state the **invariance group of each law's test statistic**. This is the fact that determines whether any single null can move all four.

| Operation on the corpus | L1 | L2 | L3 | L4 |
|---|:-:|:-:|:-:|:-:|
| Permute surah **order** (positions 1…114) | invariant | **moves** | invariant | invariant |
| Permute verses **across** surahs | moves | **moves** | **moves** | **moves** |
| Permute verses **within** a surah | moves (opener only) | invariant | **moves** | invariant |
| Reassign the 29 marker **labels** | **moves** | invariant | invariant | invariant |
| Reassign the 89 **titles** | invariant | invariant | invariant | **moves** |

**Consequence, locked before observation:** there is **no single one-parameter exchangeability group under which all four laws are simultaneously non-degenerate tail statistics.** Surah-order permutation — the null of the strongest pillar, L2 — leaves the other three *exactly* unchanged. Only cross-surah verse reallocation moves all four, and it does so by destroying the corpus rather than re-randomising an assignment within it.

We therefore pre-register **two** null-generating processes rather than one, and we commit in advance to reporting both. Reporting only one would conceal the fact above.

---

## 2. The two joint nulls

Both preserve: 114 surahs; the exact canonical verse-count profile per surah; the canonical mushaf position of every surah slot; the complete corpus vocabulary; every verse's own wording and length.

### NULL-A — redactional (label-and-order) randomisation. N = 10 000.

The corpus text and its verse→surah assignment are held **exactly canonical**. Three editorial assignment layers are randomised jointly and independently:

- **σ_order** — a uniformly random permutation of the 114 surahs supplies the reading order (drives L2).
- **σ_muq** — a uniformly random 29-subset of the 114 surahs carries the muqaṭṭaʿāt marker label (drives L1).
- **σ_title** — a uniformly random permutation of the 89 tested title-roots over the 89 tested surahs (drives L4).

This is the *direct joint generalisation of the published single-axis nulls*: L1's hypergeometric null **is** label randomisation, and L2's permutation null **is** order randomisation. Its marginals must therefore reproduce the published p-values, and that reproduction is the validity check.

**L3 is exactly invariant under NULL-A.** Its marginal is 1.000 by construction. This is not a defect to be patched; it is the finding that NULL-A exists to expose, and it is pre-registered as an expected outcome.

### NULL-B — length-profile-preserving verse reallocation. N = 2 000.

- Verse 1 of every surah is **pinned** in place. This preserves the muqaṭṭaʿāt marker system and the opener genre as real textual features.
- The remaining 6 122 verses are uniformly permuted across all non-first slots, respecting each slot's canonical verse count.
- Marker labels, titles and mushaf order stay canonical.

This destroys per-surah root bags (L2), pericope co-location (L3), title-root concentration (L4), and the vv 2–3 portion of the book-reference signal (L1). It is **conservative in favour of the laws**: pinning v1 hands L1 whatever signal lives in verse 1 for free.

### NULL-B′ — sensitivity arm, all verses free. N = 2 000.

Identical to NULL-B except verse 1 is **not** pinned; all 6 236 verses are reallocated. Marker labels remain attached to the canonical 29 surah *slots* (a label is metadata, not text). This quantifies how much of L1 lives in verse 1. Declared as a sensitivity arm, not the primary.

---

## 3. Law-satisfaction criteria — locked

Every criterion is applied identically to the canonical corpus and to every synthetic corpus, by the same function. A criterion is admissible only if the canonical corpus satisfies it; canonical satisfaction is verified at runtime and a failure aborts the run.

Two criterion tiers are pre-registered for L1–L3. **The LENIENT tier is primary.** Rationale, locked in advance: "satisfies the law" should mean "exhibits the phenomenon the law names". Setting the bar at the corpus's own observed extremity guarantees near-zero synthetic survivors by construction and manufactures an impressive joint number out of nothing. The STRICT tier is reported as a declared secondary so a reader can see both.

### L1 — muqaṭṭaʿāt → book-introduction
Statistic: one-sided hypergeometric P(X ≥ x), N = 114, n = 29, where x = number of marker-labelled surahs whose verses 1–3 (concatenated, no-tashkeel) match the **narrow** kitāb/qurʾān regex pair of `scripts/h_new_56_five_exceptions.py` (`NARROW_MARKERS`), and K = number of all 114 surahs matching.
- **LENIENT**: p_hyper < 0.05.
- **STRICT**: p_hyper ≤ 1×10⁻¹¹.

### L2 — Fisher-Rao geodesic optimality
Statistic: L(order) = Σ D[o_i, o_{i+1}] on the corpus's **own** 114×114 Fisher-Rao matrix (QAC STEM roots, K = 500 top roots of the canonical corpus, Dirichlet α = 0.5, L1-normalised — the H-NEW-111 instrument), against 2 000 uniformly random orderings of that same matrix.
- **LENIENT**: p_perm < 0.05, one-sided lower tail.
- **STRICT**: p_perm < 1/2001 **and** z ≤ −11.46.

*The optimality ratio L/L_2opt is deliberately EXCLUDED from both criteria and reported descriptively only.* Locked reason: under a homogenising null every path length converges, so the ratio → 1.0 and would spuriously certify "near-optimal" on a corpus with no structure at all. Excluding it is a tightening, not a loosening.

### L3 — pericope-scoping
The five `cf-026-formal`-surviving cross-pericope marker classes, windows exactly as locked in their own pre-regs:

| Class | Anchor | Windows |
|---|---|---|
| Iblīs narrative | H-NEW-1380 | 7 fixed pericopes |
| Sajda | H-NEW-1510 | 15 sajda verses, ±2, clipped |
| yā-ayyuhā al-nabī | H-NEW-1520 | 13 attestations, [v, v+2], clipped |
| al-ḥamdu opener | H-NEW-1750 | 5 surahs, vv 1–3 |
| Ḥawāmīm opener | H-NEW-1760 | 7 surahs, vv 1–3 |

Per class: observed mean pairwise root-Jaccard (QAC v0.4 ROOT, all segments) against 1 000 draws of length-matched random contiguous windows from the flat reading sequence. Class PASSES iff J_obs > null mean **and** p_greater < 0.05.
- **LENIENT**: ≥ 4 of 5 classes PASS.
- **STRICT**: 5 of 5 PASS.

### L4 — title-density independence
Statistic: r = number of the 89 tested eponymous surahs holding **rank 1** in their own title-root by within-surah density (count of title-root ÷ total STEM-root tokens in that surah; rank 1 = no other surah strictly higher). Title-root map taken verbatim from `csv/h-new-1820.json`.
- **SINGLE criterion, both tiers**: two-sided exact binomial test of r against p = 0.5 on n = 89 gives **p_binom > 0.05** — i.e. the corpus is *consistent with a coin flip*.

Locked note on what this criterion is: **L4 is an acceptance-of-the-null law.** It is satisfied by moderateness, not extremeness, and a corpus can fail it by being *more* title-aligned as easily as by being less. It is not directionally the same kind of claim as L1–L3, and the report must say so whichever way the numbers fall.

### Diagnostic D4 — the reference L4 has never had
For the canonical corpus only: replace each surah's title-root with a root drawn uniformly at random from the roots actually attested in that surah, matched to the observed title-root corpus-frequency band, 2 000 draws. Report the resulting distribution of r. This supplies the missing reference against which "p ≈ 50:50" can be read. Direction is **not** pre-committed — D4 is descriptive and is reported whatever it shows.

---

## 4. Quantities to be reported (all mandatory, all reported whichever way they fall)

1. **Marginal satisfaction rate of each law under each null**, alongside the published single-axis result, as the null-validity check. *If a marginal fails to reproduce its published axis, the null is declared wrong for that axis and this is stated in the headline.*
2. **Joint satisfaction count and exact joint p** = (survivors + 1)/(N + 1) per null, per tier.
3. **Pairwise dependence matrix**: φ (mean-square-contingency) between all six pairs of the four binary indicators, per null.
4. **Effective number of independent constraints**, by two routes: (a) Nyholt–Cheverud M_eff = 1 + (M−1)(1 − Var(λ)/M) on the φ matrix eigenvalues; (b) the multiplicativity ratio log p_joint ÷ Σ log p_marginal.
5. **Shrinkage curve**: survivors after each prefix, under all 24 orderings of the four laws; min / median / max at each depth.
6. **Baseline-corpora control** (§5).
7. **Simulation-resolution statement**: the smallest joint p distinguishable from zero is 1/(N+1); with 0 survivors the honest report is p < 1/(N+1) with a rule-of-three 95 % upper bound of 3/N. **No joint p smaller than that may be quoted, and the four published p-values may not be multiplied to produce one.**

---

## 5. Baseline-corpora control — the decisive item

**BL-BUKHARI**: `data/baseline-corpora/raw/bukhari-noquran.txt` (Quranic quotation already stripped).
**BL-POETRY**: concatenation in filename-sorted order of the 7 `muallaqa-*.txt` and 7 `diwan-*.txt` files in `data/baseline-corpora/raw/` (pre-Islamic only; `mutanabbi-*` (Abbasid), `jahiz-*` and `sira-*` (prose) excluded).

**Partition**: strip tashkeel and punctuation, whitespace-tokenise, then cut the word stream into 6 236 consecutive units whose word-lengths equal, **in order**, the canonical Quranic verse word-lengths; group into 114 pseudo-surahs with the canonical verse-count profile, in canonical order.

**Instrument matching (mandatory)**: QAC morphology exists only for the Quran, so the baseline arm evaluates all four laws on **surface word-types**. The identical surface-word instrument is therefore also run on the Quran, and **the baseline is compared to that instrument-matched Quran reference, never to the QAC-root headline numbers.**

Law transports, each deliberately **generous to the baseline**:
- **L1-BL**: no muqaṭṭaʿāt exist, so the marker is *searched for*. Every word-type opening between 15 and 45 of the 114 pseudo-surahs is a candidate marker; take the minimum hypergeometric p over candidates against the same kitāb/qurʾān target vocabulary, Bonferroni-corrected by the candidate count. The identical search is run on the Quran (control-of-the-control).
- **L2-BL**: the corpus's own running order (pseudo-surah 1…114) against 2 000 random orders, surface-word-type distributions, same K = 500 / α = 0.5 pipeline.
- **L3-BL**: 5 marker classes = the 5 most frequent content word-types attesting in 5–15 distinct pseudo-surahs; pericope = ±2 units around each attestation (first 15 attestations); same Jaccard-vs-length-matched-window test. Same procedure on the Quran with surface words.
- **L4-BL**: titles drawn uniformly at random from each pseudo-surah's own attested word-types within the Quranic title-frequency band, 200 draws; report the rank-1 distribution and the binomial criterion. Same procedure on the Quran.

**Decision language, locked:**
> If a partitioned ḥadīth or poetry corpus satisfies **3 or 4** of the four transported laws, then the laws are measuring properties of structured Arabic prose or verse rather than of the Qurʾān specifically, **the conjunction claim collapses**, and that is the headline of the finding.
> If a baseline satisfies **2**, the conjunction is materially weakened and the surviving content is only the difference.
> If a baseline satisfies **0 or 1**, the conjunction survives the genre control at the transported-instrument level — subject to every other limitation recorded here.

---

## 6. Locked decision language for every outcome

**On the joint null itself**
- **(a) Both nulls yield marginals reproducing the published single-axis results, and a joint p is computable.** → Report the joint p with its resolution floor, the dependence matrix and the effective constraint count. Verdict may reach at most **PASS-DIRECTED**; a joint result on the same corpus that generated the four laws cannot be CONFIRMED without out-of-sample material the project does not have.
- **(b) One or more marginals fail to reproduce the published axis.** → Declare the null wrong for that axis, publish the joint result as **INVALID for that law**, and report the conjunction only over the laws whose marginals reproduce.
- **(c) The invariance analysis of §1 is borne out — no single null moves all four, and the two nulls disagree materially.** → Verdict is **NO DEFENSIBLE SINGLE JOINT NULL EXISTS**, published with full prominence, with the two-null decomposition as the substantive deliverable. *This is an acceptable and complete outcome and must be stated as the headline if it is what the numbers show.*
- **(d) The laws are found substantially redundant** (M_eff ≤ 2.5, or joint p within one order of magnitude of the smallest marginal). → Publish **"the four pillar laws are substantially redundant and the conjunction adds little"** as the headline.

**On L4 specifically**
- If L4's marginal under a content-destroying null is near 0, that means synthetic corpora fail L4 **from below** (titles land nowhere near their density peaks). Then L4's contribution to the conjunction is real but **directionally opposite** to the design reading of L1–L3, and the report must say so in the headline rather than bank the factor silently.
- If D4 shows the canonical r is what random own-vocabulary titles produce, then **L4 carries no improbability at all** and must be reported as a triviality of "titles come from the text".

**Pre-commit violations**: any direction reversal is published as NULL with the violation flagged, per INVESTIGATION-PROTOCOL §1.8. The only direction pre-committed here is that the canonical corpus satisfies all four criteria (verified at runtime); no direction is pre-committed for any synthetic or baseline quantity, since the point of the exercise is to measure them.

---

## 7. Discipline

- Seeds: **20260509** primary, **20260519** replication. The full pipeline is run twice; both are reported.
- Frozen inputs, SHA-256 recorded in `manifest.json`: `data/morphology/quranic-corpus-morphology-0.4.txt`, `quran-text/quran-no-tashkeel.json`, `findings/phase-b-hypotheses/csv/h-new-1820.json`, `data/baseline-corpora/raw/bukhari-noquran.txt`, and each poetry file.
- This file's SHA-256 is embedded in `findings/phase-b-hypotheses/scripts/h-new-2680.py` and verified at runtime; mismatch aborts.
- Immutable run directory `findings/phase-b-hypotheses/runs/h-new-2680/<UTC timestamp>/`. **No run directory is ever deleted, including superseded ones.**
- Deviation from INVESTIGATION-PROTOCOL §7.1 (stdlib only): `numpy` is used for the Fisher-Rao matrix and permutation arithmetic. This matches existing practice in 75 project scripts. All statistical logic — hypergeometric, binomial, Jaccard, permutation counting — remains explicit.
- Compute budget: N_A = 10 000, N_B = N_B′ = 2 000, inner permutation counts 2 000 (L2) and 1 000 (L3). Power implication, stated in advance: **the joint p is floored at 1/(N+1)** — 1.0×10⁻⁴ for NULL-A and 5.0×10⁻⁴ for NULL-B. A conjunction "p-value" of 10⁻¹² is **not obtainable by this method and will not be quoted.**

### Garden-of-forking-paths log (entries made before locking)

1. A calibration probe was run before this file was written, for two purposes only: verifying that the four statistics reproduce their published canonical values under the code paths to be reused, and measuring wall-clock so N could be locked. It evaluated **no** law-satisfaction criterion on any synthetic corpus; the two synthetic draws in it were timed and discarded. Reproduction observed: L1 24/29 marker hits (published 24/29) at p = 9.48×10⁻¹² against the published 3.17×10⁻¹² — a one-surah difference in the non-marker hit count (11 vs 10), noted and carried; L2 L = 85.760 exactly as published; L3 z = +4.77/+2.67/+6.69/+3.90/+5.98 against published +4.76/+2.685/+6.41/+3.86/+6.008; L4 r = 43 against the published 42, a tie-rule difference of one surah. N was set from the measured 0.48 s per NULL-B draw.
2. Two nulls rather than one: forced by the §1 invariance table, which was written before any null was coded.
3. LENIENT tier chosen as primary over STRICT: to avoid manufacturing a small joint number by setting each bar at the corpus's own observed extremity.
4. The L2 optimality ratio excluded from the criteria: homogenisation artefact, argued in §3. This is a tightening.
5. L3 operationalised on 5 classes, not 6: `cf-026-formal` already retired the 6th.

---

*Pre-registered 2026-08-07 by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
