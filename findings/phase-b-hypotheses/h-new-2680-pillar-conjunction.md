---
finding_id: H-NEW-2680
title: The joint improbability of the four pillar laws — a defensible joint null exists, and it shows the conjunction is not measurable and not what it appears
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
prereg: findings/phase-b-hypotheses/prereg-h-new-2680-pillar-conjunction.md
prereg_sha256: 012ca709fad64bc8369313486095cc092e30414eccf45b1eca4e1b978fd08f94
seeds: 20260509 primary / 20260519 replication
rules_tuple: (no-tashkeel, QAC v0.4 ROOT/STEM-ROOT, orthographic-token for baselines, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)
status: >-
  MIXED — a valid single joint null EXISTS (NULL-C, post-hoc but forced by the
  pre-registered invariance analysis); the joint p is bounded only by simulation
  resolution at p < 5×10⁻⁴; the four published p-values MAY NOT be multiplied; and the
  baseline control shows 3 of the 4 laws are satisfied by pre-Islamic poetry.
verdict: >-
  CONJUNCTION SUBSTANTIALLY COLLAPSES. Only Pillar 1 survives the genre control.
  Pillar 2's magnitude is an artefact of block size and textual contiguity, and a
  published sanity anchor of H-NEW-111 is mis-transcribed against its own JSON.
  Pillar 3 is invariant under every redactional null and is exhibited by both baselines.
  Pillar 4 was withdrawn independently during this session; the conjunction now has
  three standing pillars, not four.
related: [h-new-2670-joint-conjunction, h-new-2710-title-density-retest, h-new-111-fisher-rao-mushaf, cross-finding-008, cross-finding-025-formal, cross-finding-026-formal]
---

# H-NEW-2680 — What is the joint improbability of the four pillar laws holding of one book?

## Headline

**A defensible single joint null does exist.** It is not either of the two pre-registered ones; it is their composition (NULL-C, §4). Under it all four pillar laws are simultaneously valid, non-degenerate test statistics, and **0 of 2 000 synthetic corpora satisfy all four** — but that is a statement about simulation resolution, not about the corpus: `p_joint < 5×10⁻⁴` (rule-of-three 95 % upper bound 1.5×10⁻³), and it cannot be pushed lower by any feasible amount of compute, because **a single one of the four laws already reduces the survivor count to zero**.

> **Status note added on completion.** While this test was running, Pillar 4 (`h-new-1820`) was **withdrawn** by a separate line of work and replaced by [[h-new-2710-title-density-retest]], which cites this study's D4 diagnostic as the prior art that triggered the withdrawal and then refines it (§9.1). **The conjunction therefore now has three standing pillars, not four.** Everything below reports L4 as tested, because that is what the pre-registration locked; the finding is strengthened, not weakened, by the withdrawal.

Three findings matter more than the number.

1. **The four published p-values may not be multiplied, and the one multiplication that *is* exactly valid involves only two of the four.** Under the redactional null, Pillars 1 and 2 are functions of *disjoint, independently drawn* randomisation layers, so they are exactly independent — verified at φ = +0.0003. Their p-values multiply legitimately: `p(L1 ∧ L2) ≤ 3.17×10⁻¹² × 10⁻⁴ ≈ 3×10⁻¹⁶`. Pillars 3 and 4 cannot be joined to that product, because under the null that makes 1 and 2 exactly independent, **Pillar 3 is mathematically invariant** (marginal 1.000, verified) and **Pillar 4 is destroyed from below** (marginal 0.000).

2. **The baseline control collapses the conjunction.** Under an instrument-matched surface-word instrument, a length-matched 114-block partition of **pre-Islamic poetry satisfies 3 of the 4 transported laws**, and one of **al-Bukhārī satisfies 2**. Pre-registered decision language for a baseline at 3 is that "the laws are measuring properties of structured Arabic prose or verse rather than of the Qurʾān specifically, and the conjunction claim collapses." **Only Pillar 1 is not satisfied by either baseline.**

3. **Pillar 2's 11.46 σ is largely an artefact of block size and textual contiguity, not of the surah division or its order.** Cutting the same Qurʾānic verse stream into 114 blocks of the *same size profile* but at *arbitrary offsets that ignore every surah seam* gives z = −11.23, −13.18, −12.92, −12.33, −12.62; the canonical surah boundaries give −11.50. And a published sanity anchor turns out to be mis-transcribed: `h-new-111-fisher-rao-mushaf.md` reports length-sorted orderings at L = 107.27 ("confirms MW-1 length control is working"), while **its own `csv/h-new-111.json` records 91.03 / 90.30**, independently reproduced here. Sorting the real surahs by length alone, using no vocabulary at all, reaches **z = −8.66**. The mushaf's margin over pure length is **2.80 σ**, not 11.46 σ (§8.1).

---

## 1. Why the four p-values may not be multiplied — the invariance analysis

Locked in the pre-registration before any null was coded. Each law's test statistic has a different invariance group:

| Operation | L1 muqaṭṭaʿāt | L2 Fisher-Rao | L3 pericope | L4 title-density |
|---|:-:|:-:|:-:|:-:|
| permute surah **order** | invariant | **moves** | invariant | invariant |
| permute verses **across** surahs | moves | **moves** | **moves** | **moves** |
| permute verses **within** a surah | opener only | invariant | **moves** | invariant |
| reassign the 29 marker **labels** | **moves** | invariant | invariant | invariant |
| reassign the 89 **titles** | invariant | invariant | invariant | **moves** |

**Surah-order permutation — the null of the strongest pillar — leaves the other three exactly unchanged.** That is the whole difficulty in one line, and it is why two nulls were pre-registered rather than one.

---

## 2. Canonical reproduction (the instrument check)

Every statistic was recomputed from the frozen inputs through the code paths this study reuses.

| Law | Reproduced here | Published | Source of published |
|---|---|---|---|
| L1 | 24/29 marker surahs with kitāb/qurʾān in vv 1–3; K = 35; **p = 9.48×10⁻¹²** | 24/29, K = 34, p = 3.17×10⁻¹² | `h_new_56_five_exceptions.py`, cross-finding-008 |
| L2 | **L = 85.7597**, z = −11.70, ratio 1.1063 | L = 85.760, z = −11.46, ratio 1.107 | `h-new-111-fisher-rao-mushaf.md` |
| L3 | 5/5 pass: z = +4.77 / +2.65 / +6.49 / +3.90 / +6.25 | +4.76 / +2.685 / +6.41 / +3.86 / +6.008 | H-NEW-1380/1510/1520/1750/1760 |
| L4 | rank-1 **43/89**, binomial p = 0.832 | 42/89 (JSON), 41/89 (corrected text) | `csv/h-new-1820.json` |

L1 differs by one non-marker surah (K = 35 vs 34) and L4 by one to two surahs on tie-handling; L2's path length reproduces to 4 decimal places. The instruments are the published ones.

**Canonical satisfaction: 4/4 LENIENT.** The run would have aborted otherwise.

### A pre-registration defect, disclosed
The STRICT tier for L2 was locked as `p_perm < 1/2001`. With the standard `(n_le+1)/(n_perm+1)` estimator the smallest attainable p **is** 1/2001, so the criterion is unsatisfiable by construction — the canonical corpus fails its own STRICT L2 cell, and the STRICT 4-way joint is therefore **void, not zero**. It is reported here and not quoted. Repairing it (`≤` instead of `<`) would be a *loosening* and is not applied; it is flagged for ratification. The LENIENT tier was pre-registered as primary and is unaffected.

---

## 3. The two pre-registered nulls — and why neither is valid for all four

Marginal satisfaction rate of each law, LENIENT tier. A **valid** null reproduces the published axis: a marginal near the nominal α = 0.05. A marginal of 1.000 means the null cannot fail the law; 0.000 means it can never pass it.

| | N | L1 | L2 | L3 | L4 | joint |
|---|--:|--:|--:|--:|--:|--:|
| **NULL-A** redactional (labels + order + titles randomised) | 10 000 | **0.0490** ✓ | **0.0446** ✓ | 1.0000 ✗ | 0.0000 ✗ | 0/10 000 |
| **NULL-B** verses after v1 reallocated | 2 000 | 0.8315 ✗ | 1.0000 ✗ | **0.0020** ✓ | 0.0000 ✗ | 0/2 000 |
| **NULL-B′** all verses reallocated | 2 000 | **0.0315** ✓ | 1.0000 ✗ | **0.0005** ✓ | 0.0000 ✗ | 0/2 000 |

Replication at seed 20260519 reproduces every cell (L1 0.0467 / 0.8245 / 0.0300; L2 0.0493 / 1.0 / 1.0; L3 1.0 / 0.0005 / 0.0; L4 0.0 throughout).

**NULL-A is valid for L1 and L2 and useless for L3.** L3's invariance was verified rather than assumed: 25/25 draws return the identical 5/5 result, as they must — NULL-A randomises marker labels, reading order and title assignment, and none of the three is an argument of the L3 statistic.

**NULL-B is invalid for both L1 and L2.** Pinning verse 1 hands L1 most of its signal (marginal 0.83; releasing verse 1 in NULL-B′ drops it to 0.0315, which *is* valid). And L2's marginal of 1.000 has a diagnosable cause:

| | canonical corpus | under NULL-B (n = 200) |
|---|--:|--:|
| rank corr( Fisher-Rao distance , \|Δ log surah size\| ) | 0.308 | **0.625** |
| L(mushaf) | 85.76 | 83.54 |
| L(length-sorted) | **91.03** (longer) | **82.14** (shorter) |
| fraction of draws with L(mushaf) < L(length-sorted) | — | **0.00** |

Reallocation homogenises every surah into a sample from the same global root distribution, so the Fisher-Rao geometry becomes a near-pure function of surah **size**. The mushaf order is roughly size-ordered, so it rides that manufactured geometry and "passes" every time (z distribution: mean −9.27, sd 0.32, max −8.22 — never once failing). **NULL-B and NULL-B′ are not valid nulls for L2**, exactly as pre-reg §6(b) provides for.

---

## 4. NULL-C — the composed null, and the one that works

*Post-hoc, and labelled as such (MW-7 single-test ceiling). It was not pre-registered, but it is the direct consequence of the pre-registered §1 invariance table: compose the two operations.*

L2's invalidity under reallocation has a single cause — the mushaf order was held fixed while the content was homogenised. **Randomising the order as well cancels it**, because a random order of any distance matrix has z ~ N(0,1) by construction. NULL-C therefore reallocates all 6 236 verses **and** randomises the marker labels, the titles and the reading order.

| NULL-C | N | L1 | L2 | L3 | L4 | joint |
|---|--:|--:|--:|--:|--:|--:|
| seed 20260509 | 2 000 | 0.0405 ✓ | 0.0525 ✓ | 0.0000 | 0.0000 | **0 / 2 000** |
| seed 20260519 | 2 000 | 0.0380 ✓ | 0.0535 ✓ | 0.0000 | 0.0000 | **0 / 2 000** |

L2's z-distribution under NULL-C is mean −0.043, sd 1.000 — the confound is gone. L1 and L2 both sit at the nominal α. **This is a valid joint null for all four laws simultaneously.**

`p_joint < 5×10⁻⁴`, 95 % upper bound 1.5×10⁻³. **This is the honest joint p and it is a resolution floor, not a measurement.**

---

## 5. The dependence matrix, and the effective number of constraints

φ (mean-square contingency) between the four binary indicators. `—` means undefined: the marginal is degenerate (constant), so no correlation is estimable.

| | NULL-A | NULL-B | NULL-B′ | NULL-C |
|---|--:|--:|--:|--:|
| L1 × L2 | **+0.0003** | — | — | +0.0199 / −0.0356 |
| L1 × L3 | — | +0.0202 | −0.0040 | — |
| all other pairs | — | — | — | — |

**Every estimable pair is uncorrelated.** For L1 × L2 under NULL-A this is not merely an estimate but an exact fact: σ_muq and σ_order are drawn independently, the L1 statistic is a function of σ_muq alone and the L2 statistic of σ_order alone, so **L1 ⊥ L2 exactly**. Observed L1 ∧ L2 = 22/10 000 = 0.00220 against the independence prediction 0.0490 × 0.0446 = 0.00219.

**This licenses exactly one multiplication in the whole study**: `p(L1 ∧ L2) ≤ 3.17×10⁻¹² × 10⁻⁴ ≈ 3×10⁻¹⁶` (L2's factor is capped at its own 10 000-permutation floor). §7 and §8 explain why this number nevertheless carries much less evidential weight than it looks.

### Effective number of independent constraints

- **Nyholt–Cheverud on the φ matrix: M_eff = 4.000 in every arm.** This is an artefact and must not be quoted: two of the four indicators are constant in every arm, so their off-diagonals were set to 0, which forces the answer to 4 mechanically.
- **Multiplicativity route** `log p_joint ÷ mean log p_marginal`: **1.42 (NULL-C), 1.63–2.17 (NULL-B′/B), 2.40 (NULL-A)** — all far below 4, and all floored.
- **The operationally honest count is 1.** Under NULL-C the shrinkage curve reaches zero survivors after a *single* law (see §6). At N = 2 000 the conjunction carries no measurable information beyond its strongest member.

---

## 6. The shrinkage curve

Survivors after each prefix, over all 24 orderings of the four laws (min / median / max).

| depth | NULL-A (N = 10 000) | NULL-B′ (N = 2 000) | NULL-C (N = 2 000) |
|:-:|---|---|---|
| 1 | 0 / 468 / 10 000 | 0 / 32 / 2 000 | **0** / 40.5 / 105 |
| 2 | 0 / 11 / 490 | 0 / 0 / 63 | 0 / 0 / 6 |
| 3 | 0 / 0 / 22 | 0 / 0 / 0 | 0 / 0 / 0 |
| 4 | **0** / 0 / 0 | **0** / 0 / 0 | **0** / 0 / 0 |

The `min` column is the story: **under NULL-C, an ordering that begins with L3 or with L4 has zero survivors at depth 1.** Everything after that is unmeasurable. Multiplying the four marginal *upper bounds* under NULL-C (0.0405 × 0.0525 × 5×10⁻⁴ × 5×10⁻⁴) gives ≲ 5×10⁻¹⁰, so observing even one survivor of the full conjunction needs **N ≳ 2×10⁹** — and that figure already assumes the independence the whole exercise was meant to test. Beyond this point the answer is arithmetic on an assumption, not simulation.

Exact subset counts, NULL-A, N = 10 000 — the only arm with a non-degenerate two-way cell:

```
L1        490      L1&L2      22      L1&L2&L3    22
L2        446      L1&L3     490      L1&L2&L4     0
L3     10 000      L2&L3     446      L1&L3&L4     0
L4          0      any &L4     0      L1&L2&L3&L4  0
```

`L1&L2&L3 = L1&L2` exactly, because L3 is invariant. **Pillar 3 adds literally nothing to this conjunction** — not "little", but zero, as a matter of the statistic's arguments.

---

## 7. The baseline-corpora control — the decisive item

Both baselines were cut into 6 236 units matching the Qurʾān's verse word-length profile in order, then grouped into 114 pseudo-surahs with the canonical verse-count profile. QAC morphology exists only for the Qurʾān, so **all four laws in this arm run on surface word-types, and the Qurʾān was run through the identical surface instrument** — the baselines are compared to that, never to the QAC-root headline numbers.

| | L1 (marker → self-reference) | L2 (Fisher-Rao geodesic) | L3 (pericope-scoping) | L4 (title-density) | **laws satisfied** |
|---|---|---|---|---|:-:|
| **Qurʾān** (surface instrument) | ✓ p_bonf = 4.7×10⁻¹³ | ✓ z = −11.50 | ✓ 5/5 | ✓ 59.5 % of title draws | **4 / 4** |
| **al-Bukhārī** (114 pseudo-surahs) | ✗ no marker class exists | ✓ **z = −13.84** | ✓ 4/5 | ✗ 14 % | **2 / 4** |
| **pre-Islamic poetry** (114 pseudo-surahs) | ✗ no marker class exists | ✓ **z = −15.13** | ✓ 5/5 | ✓ 99.5 % | **3 / 4** |

Poetry at 3/4 triggers the pre-registered collapse language. Reading each law honestly:

- **L2 does not discriminate at all.** Both baselines are *more* extreme than the Qurʾān. Bukhārī z = −13.84, poetry z = −15.13, Qurʾān z = −11.50. Optimality ratios: Bukhārī 1.073, poetry 1.093, Qurʾān 1.130 — the baselines are *closer* to their own TSP optima than the mushaf is to its.
- **L3 does not discriminate.** Poetry 5/5, Bukhārī 4/5. Marker classes that flip in poetry are ordinary content words (`عبلة` — ʿAntara's beloved; `عبس`), and in Bukhārī jurisprudential vocabulary (`الماء`, `الإمام`). This is topical burstiness, which any text has, and the project already names burstiness as the mechanism (H-NEW-2330, cited in `cf-026-formal`). L3 is a property of texts, not of this text.
- **L4 does not discriminate.** Poetry satisfies the "consistent with a coin flip" criterion in 99.5 % of title draws — more comfortably than the Qurʾān.
- **L1 is the only law neither baseline satisfies**, and it fails for them at the root: fed the same generous search, Bukhārī has only 6 pseudo-surahs and poetry only **1** whose first three units mention kitāb or qurʾān. There is no self-referential target vocabulary to mark, and no opening marker class to mark it with.

### An instrument that failed its own control, and its repair
The L1 transport locked in pre-reg §5 searched for a marker made of a **single** opening word-type. Run on the Qurʾān it returned `n_candidates: 0` — it could not find the muqaṭṭaʿāt, because the real marker is a **class of 14** opening types. An instrument that cannot detect the effect in the corpus that has it cannot license a claim about corpora that may not. The unrepaired result stands on disk in the pre-registered run. The repair (`h-new-2680b.py`, greedy marker-class search up to 14 members, Bonferroni-corrected by the 721 hypergeometric evaluations actually performed) **passes its control-of-the-control decisively**: on the Qurʾān it recovers the muqaṭṭaʿāt themselves —

`الر, حم, طسم, الم, المص, المر, سبحان, طه, طس, يس, ص, تنزيل, ق, والطور`

— covering 30 surahs, 27 of them book-referencing, p_raw = 6.5×10⁻¹⁶, **p_bonf = 4.7×10⁻¹³**. Run identically on the baselines it finds nothing at all. The table above uses the repaired transport.

---

## 8. Pillar 2 does not measure what it is taken to measure

The baseline result above is not a quirk of ḥadīth or poetry. Cutting **the Qurʾān's own verse stream** into 114 contiguous blocks with the identical size profile, but at offsets that ignore every surah seam:

| partition of the same 6 236 verses (QAC-root instrument) | L | z | p |
|---|--:|--:|--:|
| **real surah boundaries, mushaf order** | 85.760 | **−11.50** | 5×10⁻⁴ |
| offset cut at verse 137 (ignores all seams) | 85.153 | −11.23 | 5×10⁻⁴ |
| offset cut at verse 37 | 81.378 | **−13.18** | 5×10⁻⁴ |
| offset cut at verse 311 | 87.520 | −12.92 | 5×10⁻⁴ |
| offset cut at verse 1013 | 89.946 | −12.33 | 5×10⁻⁴ |
| offset cut at verse 2579 | 88.321 | −12.62 | 5×10⁻⁴ |
| verses shuffled, then cut identically | 85.536 | −8.44 | 5×10⁻⁴ |

**Arbitrary cuts of the same text score as extreme as the real surah division, and four of the five score *more* extreme.** Even destroying contiguity entirely still leaves z = −8.44, because the block-size profile alone generates structure (§3).

What this does **not** show: H-NEW-111's arithmetic is exact — L_mushaf = 85.7597 reproduces to four decimals. What it does show: **the uniform-random-permutation null is too weak to isolate design.** Any text read in the order it exists beats a scramble of its own chunks, and the surah seams contribute nothing detectable on top of that.

What survives untouched is the *relative* comparison inside H-NEW-111, which never used the random null: **the mushaf is a better traversal of the real surahs than either reconstructed chronology.** That claim stands. The claim that "11.46 σ below random" measures design does not.

### 8.1 A published sanity anchor is mis-transcribed, and the MW-1 conclusion drawn from it is false

`h-new-111-fisher-rao-mushaf.md` reports the length-sorted anchor as **107.27 for both ascending and descending**, and draws this conclusion:

> "Length-sorted orderings behave approximately at null-mean (107 ≈ 104 within noise band) — confirms MW-1 length control is working: once distributions are L1-normalized, sorting by length is NOT a low-cost traversal."

**Its own JSON says otherwise.** `findings/phase-b-hypotheses/csv/h-new-111.json` → `sanity_anchors`:

```json
{"L_length_sorted_ascending": 91.027805, "L_length_sorted_descending": 90.301441}
```

Independently recomputed here from the frozen QAC file through the same K = 500 / α = 0.5 pipeline: **91.0278 and 90.3014** — matching the JSON to four decimals, while the same rebuild reproduces L_mushaf = 85.7597 (published 85.760), L_Nöldeke = 87.2321 (published 87.232) and the null at 104.363 / 1.623 (published 104.346 / 1.622). The rebuild is right and the markdown transcription is wrong. (The two values being reported as *identical* is itself the tell: with a stable sort, descending is not the exact reverse of ascending, so the two paths cannot have equal length.)

Recomputing every anchor against the published null (mean 104.3457, sd 1.6218):

| ordering | L | z |
|---|--:|--:|
| mushaf | 85.760 | **−11.46** |
| Nöldeke chronology | 87.232 | −10.55 |
| Tanzil revelation order | 89.530 | −9.14 |
| **length-sorted, descending** | **90.301** | **−8.66** |
| length-sorted, ascending | 91.028 | −8.21 |

**MW-1 length control is not working on this instrument.** Sorting the real surahs by length alone — using no vocabulary information whatever — already reaches z = −8.66 of the mushaf's −11.46. And the mushaf is itself close to length-descending: Spearman(mushaf position, verse count) = **−0.846**.

The mushaf's content beyond what pure length delivers is therefore **4.54 length-units = 2.80 σ**, not 11.46 σ. That residual is real and is the honest effect size for Pillar 2 — it is also the quantity that the Nöldeke comparison (−10.55, i.e. 1.89 σ above length-sorted-descending) was implicitly measuring all along. Nothing here is fabricated or retracted; the arithmetic of H-NEW-111 was correct and its own JSON recorded the right numbers. What must be corrected is the write-up's transcription and the MW-1 conclusion built on it.

---

## 9. Pillar 4 is not the kind of claim the conjunction needs — and its published framing has no reference

Two separate problems, both pre-registered as reportable.

**(a) It is an acceptance-of-the-null law.** L4 is satisfied by *moderateness*: r = 43 rank-1 out of 89 is consistent with a coin flip (binomial p = 0.83). A corpus fails L4 by being **too** title-aligned exactly as easily as by being too little. Every synthetic corpus in every arm fails it **from below** — mean rank-1 counts of 0.96 (NULL-A), 21.3 (NULL-B), 0.85 (NULL-B′), 0.84 (NULL-C), against the canonical 43. So L4's contribution to the conjunction is real but **directionally opposite** to the design reading of Pillars 1–3: what the nulls lack is *more* title-density alignment, not less. Putting it into a conjunction of design evidence and banking the factor silently would be wrong.

**(b) "Independent at p ≈ 50:50" is measured against no reference at all.** Diagnostic D4 supplies the missing one: replace each surah's title-root with a root drawn at random from the roots that surah actually attests, inside the observed title-root frequency band, 2 000 draws.

| | rank-1 count out of 89 |
|---|--:|
| **canonical title-roots** | **43** |
| random own-vocabulary titles: mean (sd) | **25.7 (3.2)** |
| 5th / 50th / 95th percentile | 21 / 26 / 31 |
| draws reaching 43 | **0 / 2 000** (p = 5.0×10⁻⁴) |

**Against a principled reference, the Qurʾān's titles are density-*dependent*, not independent**: 43 observed against 25.7 expected, a rate ratio of 1.68 at +5.5 σ. The "p ≈ 50:50" reading is an artefact of comparing to an unstated 100 % prior rather than to a null. The corpus does not sit at chance.

### 9.1 Superseded in the same session — read with H-NEW-2710

D4 is not the last word and should not be cited as one. While this test was running, `h-new-1820` was **withdrawn** and replaced by **`h-new-2710-title-density-retest.md`**, which runs the same question with a *tighter* control: D4 matches candidate title-roots on corpus **frequency** only, whereas H-NEW-2710's Null B matches on **frequency and dispersion** — a root concentrates where its topic is discussed, and that must be conditioned on. Under that control:

| control | expected rank-1 | observed | rate ratio |
|---|--:|--:|--:|
| naive uniform (~1/114) | ≈ 1 | 42–43 | huge — the original "independence" law is **wrong** |
| **D4 (this test)** — frequency-matched, own-vocabulary | 25.7 | 43 | **1.68** |
| **H-NEW-2710 Null B** — frequency **and dispersion** matched | 32.7 | 42 | **1.285** |

H-NEW-2710 further finds median rank statistically indistinguishable from its null (2 vs 2.24, p = 0.76). **Its verdict — that the residual is topicality, and that "strongly dependent" is refuted at 1.285× — supersedes D4's 1.68.** D4's number is not wrong; its null was the weaker of the two, and the direction it established (dependence, not independence) is the direction H-NEW-2710 confirms and then quantifies down. That agreement across two independently pre-registered controls is worth more than either alone.

**Consequence for this study.** The pillar count is now **three, not four**. Everything in §§3–6 about L4 stands as a description of how a withdrawn criterion behaved — and it corroborates the withdrawal from a different direction: a criterion that *every* synthetic corpus fails from below, in all four nulls and both seeds, was never a design-direction constraint.

---

## 10. Answers to the questions asked

**The joint null specification.** Two pre-registered (NULL-A redactional; NULL-B/B′ verse reallocation), one post-hoc composition (NULL-C) that is valid for all four at once. Full specification in `prereg-h-new-2680-pillar-conjunction.md` §2 and §4 above.

**Marginals vs published values.** NULL-A reproduces L1 (0.049) and L2 (0.0446) at their nominal α, so it is a valid null for those axes; it is provably useless for L3 and destroys L4. NULL-B fails the reproduction check for L1 (0.83) and L2 (1.00). NULL-B′ fails it for L2 (1.00). NULL-C reproduces L1 (0.041) and L2 (0.053) and leaves L3 and L4 as genuine tails.

**Dependence matrix.** Every estimable pair is uncorrelated (|φ| ≤ 0.036); L1 ⊥ L2 exactly under NULL-A. All other pairs are inestimable because a marginal is degenerate. **The laws are not redundant in the correlational sense. They are non-commensurable in kind**, which is a different and worse problem: two of the four stop being tail statistics under half the nulls.

**Effective independent constraints.** Nyholt = 4.000 but is an artefact of degenerate marginals and must not be quoted. Multiplicativity route: 1.42–2.41. **Operationally 1**, because one law exhausts the survivor count at depth 1.

**Shrinkage curve.** §6. Collapses to zero at depth 1 under NULL-C in any ordering starting with L3 or L4.

**Joint p.** `p < 5×10⁻⁴` (NULL-C, N = 2 000, 95 % upper 1.5×10⁻³). **The four published p-values may not be multiplied to 10⁻¹² or anything like it.** The only exactly-licensed multiplication is L1 × L2 ≈ 3×10⁻¹⁶, and §7–8 show that the L2 factor in it does not carry the evidential meaning it appears to.

**Baseline control.** Poetry 3/4, al-Bukhārī 2/4, Qurʾān 4/4 on the instrument-matched surface instrument. **Only Pillar 1 discriminates.**

---

## 11. Honest limits

1. **N is the binding constraint on the joint p, not the data.** With 0 survivors at N = 2 000 the joint p cannot be reported below 5×10⁻⁴. This is a fact about the method. No amount of compute fixes it while a single law already zeroes the count.
2. **NULL-C is post-hoc.** It was constructed after seeing why the pre-registered nulls fail, though it follows directly from the pre-registered invariance table. MW-7 caps any claim resting on it at a single-test ceiling.
3. **The STRICT tier is void for L2** (§2). Not repaired, because repairing it would be a loosening; flagged for ratification.
4. **The baseline pseudo-surahs are arbitrary cuts, not natural units.** al-Bukhārī has real *kitāb*/*bāb* boundaries that were not used. The asymmetry runs *against* the Qurʾān, though: arbitrary cuts of a continuous stream maximally preserve local continuity, so they should make L2 and L3 *easier* to satisfy for the baselines — and they did. Testing Bukhārī at its natural boundaries is queued.
5. **L1's baseline failure is partly a content fact, not a design fact.** The baselines fail L1 largely because they have almost no self-referential book-vocabulary at unit openings (target sets of 6 and 1). "Only scripture talks about itself as a book" is a weaker claim than "only the Qurʾān has an engineered marker system", and this test does not separate the two.
6. **L3 was operationalised on 5 classes, not 6**, per `cf-026-formal`'s retirement of the ring-composition member. Using 6 would have tested a member the project has already withdrawn.
7. **Tail-level independence was verified at the criterion level (α = 0.05), not at the published extremity**, except for L1 × L2 under NULL-A where independence is exact by construction and needs no verification.
8. **No claim is made here that any pillar law's arithmetic is wrong.** L1's hypergeometric, L2's path length and L3's five flips all reproduce, and L4's rank-1 headcount reproduces to within one surah on tie-handling (43 here against the published 42; the separate `48/89` figure was itself withdrawn during this session as an invalid cross-metric substitution — see §9.1). What is challenged is (i) that the four may be multiplied, (ii) that L2's σ measures design, (iii) that L4 meant independence, and (iv) that the conjunction is Qurʾān-specific.
9. **L4's arm reports a criterion that has since been withdrawn.** It is retained as pre-registered rather than deleted, because deleting it would hide the fact that a withdrawn law was one of the four the conjunction was built on.

---

## 12. What should change in the project record

- **`MASTER-FINDINGS-LEDGER.md` §10.72 "Four project pillar laws now LOCKED"** should carry a cross-reference to this finding. The four are not four independent constraints on one book; on the evidence here they are one discriminating constraint (Pillar 1) plus three that a partitioned dīwān also satisfies.
- **Pillar 2** should be restated as the *relative* claim it can support — the mushaf is a shorter Fisher-Rao traversal than either reconstructed chronology, by **2.80 σ beyond a pure length-sorted baseline** — and the "z = −11.46 below random" figure should carry both the contiguity caveat of §8 and the length caveat of §8.1 wherever it is cited as evidence of design.
- **`h-new-111-fisher-rao-mushaf.md` needs a correction notice.** Its length-sorted sanity anchor reads 107.27 for both directions; its own `csv/h-new-111.json` records 91.0278 / 90.3014, which is what the computation actually produced and what an independent rebuild reproduces. The sentence "confirms MW-1 length control is working" is false as a result and should be replaced by the correct reading: length alone reaches z = −8.66, and the mushaf's margin over pure length-sorting is 2.80 σ. Per project convention the correction gets a visible notice; nothing is silently edited. **This is not mine to apply to another finding's file — flagged for the ledger keeper.**
- **Pillar 4 (H-NEW-1820) — already actioned in this session, independently.** It was withdrawn and replaced by `h-new-2710-title-density-retest.md` while this test ran; the replacement cites D4 as the prior art that triggered the withdrawal and refines its 1.68 rate ratio to 1.285 under dispersion matching. Nothing further is needed here beyond recording that **the conjunction now has three pillars, not four**, and that the withdrawn one was never a design-direction constraint.
- **Pillar 3** should carry the note that it is not a corpus-level tail event under any redactional null — it is a property of verse-level content that survives every editorial randomisation — and that both baseline corpora exhibit it.

## 13. Convergent sibling result — H-NEW-2670

[[h-new-2670-joint-conjunction]] asked the intersection question on a different object (which 14-letter subsets satisfy *all* declared muqaṭṭaʿāt constraints at once) and reached the same methodological conclusion by a different route. Its locked rule returned W = 7 of 40 116 600 subsets, p = 1.745×10⁻⁷, control passing narrowly at q = 0.018 — and then a **stricter post-observation control, letting each random subset pick its own axes from the same attested menu, failed at q′ = 0.248**: one random 14-subset in four becomes as "unique" as the muqaṭṭaʿāt. Its verdict is ARTEFACT-OF-CONSTRAINT-STACKING.

The two studies agree on the load-bearing point from opposite ends. H-NEW-2670 shows that **stacking constraints manufactures apparent uniqueness when the constraints are chosen after looking**; H-NEW-2680 shows that **stacking laws manufactures apparent improbability when their nulls are not commensurable**. Neither the intersection count nor the p-value product is interpretable without first asking what randomisation each constraint is a tail of. Read together they are a single methodological result about conjunction reasoning in this project.

## Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2680-pillar-conjunction.md` (SHA-256 `012ca709fad64bc8369313486095cc092e30414eccf45b1eca4e1b978fd08f94`)
- Scripts: `findings/phase-b-hypotheses/scripts/h-new-2680.py` (pre-registered arms + baselines), `h-new-2680b.py` (repaired L1 transport + contiguity diagnostic), `h-new-2680c.py` (NULL-C, imports the pre-registered code paths verbatim)
- Runs (immutable, never deleted): `findings/phase-b-hypotheses/runs/h-new-2680/20260807T011917Z/`, `runs/h-new-2680b/20260807T012404Z/`, `runs/h-new-2680c/20260807T014327Z/`, and the calibration smoke runs under `runs/h-new-2680-SMOKE/`
- Frozen inputs with SHA-256: each run's `manifest.json`

---

*Run 2026-08-07 by Waiel Al-Shujaa. A conjunction is only as strong as its weakest null. Bismillāhi al-Raḥmāni al-Raḥīm.*
