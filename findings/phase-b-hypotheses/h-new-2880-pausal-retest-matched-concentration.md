---
id: H-NEW-2880
title: "The pausal fāṣila, re-tested against a null matched on class CONCENTRATION — the question H-NEW-2870 left open, closed"
phase: B
date: 2026-08-07
author: Waiel Al-Shujaa
frontier_item: F-16
parent: H-NEW-2870
verdict: "PASS — under a null whose chance floor has exactly zero variance, the observed pausal rhyme agreement sits outside the entire support of every construction tried: 0 / 10,000 in all twelve gating arms (three constructions x two tuples x two seeds), and in the four non-gating N-A arms as well. MUST be cited with §10: the deliberately wrong pausal tuple also clears its own exact null, so the discrimination within the pausal family is quantitative, not categorical."
prereg: prereg-h-new-2880-pausal-retest.md
prereg_sha256: 87083f50d56cd9802a5656ebc3049da98ee0397e6a0dda657e4d3dbbebe052ab
run: runs/h-new-2880/20260807T141104Z/
seed: 20260509
seed_replication: 20260519
n_perm: 10000
n_recut: 2000
bonferroni_k: 18
alpha_bonferroni: 0.00277778
---

# H-NEW-2880 — the pausal fāṣila at matched concentration

**One-line summary.** H-NEW-2870's NULL came from a null model whose winning draws were,
every one of them, coarser merges than *waqf* performs. Rebuilt so that **every draw carries
the identical class-size multiset — hence the identical chance floor, to the last bit** — the
observed pausal rhyme agreement sits **0 / 10,000 outside the null in all twelve gating arms**
— three independent constructions of the null × two pausal tuples × two seeds — and in the four
non-gating N-A arms as well. The locked verdict is **PASS**. What distinguishes the null it
rests on is that the confound channel has **exactly zero variance by construction**, rather
than being matched on average or corrected for analytically.

**What is genuinely new here is not the delta — the parent published it — but the
instrument.** The parent's two nulls are re-implemented verbatim and audited: **both** were
systematically more concentrated than the real partition, and the one the parent called clean
was the *worse* of the two on that channel.

**And one thing the PASS does not license, established post-hoc in §10 and flagged here so it
travels with the headline:** the deliberately *wrong* pausal tuple also clears its own exactly
matched null at 0 / 10,000. What the exact null separates is the **pausal family** from random
regrouping. Within that family the correct rules are stronger by measurement — z = +15.0
against +9.0, Δ = +0.187 against +0.088 — and **55.4 % of the pairs *waqf* merges require the
one rule the wrong tuple lacks**.

---

## 1. Gates — reported before any test statistic

The instrument is the parent's, **pinned by SHA-256** (`h-new-2870.py` =
`9765a448…07d2dde`) and executed verbatim, so the two findings cannot drift apart. Nothing in
the phonemiser, the conventions, the rime extractors or the gates was changed.

- **Gate A — orthography. PASS.** All six tanwīn marks verified against Tanzil Uthmani v1.1
  under 1:1 verse alignment: **2,534 tanwīn-bearing words, zero mismatches**, rate 1.0000 on
  each of the six. 77.7 % of the corpus's tanwīn is encoded with three codepoints whose
  Unicode names do not describe their function; the parent's remap is inherited.
- **Gate B — instrument. 6/6 PASS** against H-NEW-2240 (Q18 110/110 open `-ā`; Q112 4/4 `-ad`;
  Q108 3/3 `-ar`; Q114 6/6 `-ās`; Q1 all seven in {`-īm`,`-īn`}; Q55 modal `-ān`).

---

## 2. RESULT 1 — the class-collapse magnitude. Reported before any headline number.

Reproduces the parent exactly. Rime definition **R2** (tanwīn-transparent), which is the sound
instrument and the only one under which the new nulls are defined (§3.1).

| | classes **K** | effective classes **K_eff** | chance floor Σpᵢ² | A |
|:--|--:|--:|--:|--:|
| **C** — citation (waṣl) | **397** | **37.03** | 0.10681 | 0.3484 |
| **P1** — pausal, minimal | **116** | **10.87** | **0.16871** | 0.5353 |
| P2 — pausal, full (ة → h) | 115 | 10.82 | 0.16876 | 0.5364 |
| P3 — truncation only (deliberately wrong) | 213 | 16.89 | 0.14154 | 0.4360 |

> **Collapse C → P1: 3.422× on K, 3.405× on K_eff. The chance floor rises 0.1068 → 0.1687, so
> the collapse buys +0.0619 of adjacent-verse agreement for free.** Observed Δ = **+0.1869**:
> **33.1 % arithmetic, 66.9 % compositional.**

The arithmetic third is stated first, in the reporting order the pre-registration locked,
because presenting the delta first would misrepresent an arithmetic effect as a compositional
one. **Everything that follows is about the remaining two thirds.**

---

## 3. RESULT 2 — the anti-gaming audit. This is the finding.

### 3.1 Why the new null is defined under R2 and not under R1

Every null here permutes the assignment of **citation types** to **pausal classes**, which is
defined only if the pausal partition is a coarsening of the citation partition. Measured, and
decided in the pre-registration before any draw:

| rime | citation types split across pausal classes | verses in split types | block sizes reconstruct from type sizes |
|:--|--:|--:|:--|
| **R2** | **0** | **0 (0.00 %)** | **yes, exactly** |
| R1 | 2 | 1,059 (16.98 %) | **no** — off by 710 verses |

R1 fails the parent's own §12 condition. It is carried only for the controls that do not need
the map (§5), and it gates nothing.

### 3.2 The parent's two nulls, re-implemented verbatim and measured

Both are re-run here as **diagnostics; they gate nothing.** The N1-a figures reproduce the
parent's §9 **exactly** — 57 winning draws, mean floor 0.2879, 57/57, ρ = +0.6805 — which is
the evidence that this harness computes the same thing the parent did.

| | **N1-a** (verse-profile matched) | **N1-b** (cardinality matched) | **N-EXACT** (this finding) |
|:--|--:|--:|--:|
| the real partition's floor | 0.16871 | 0.16871 | 0.16871 |
| null floor, mean | **0.2071** | **0.2398** | **0.16871** |
| null floor, sd | 0.0319 | 0.0958 | **0.00000** |
| null floor, range | 0.1385 – 0.3276 | — | **0.16871 – 0.16871** |
| **draws within ±2 % of the real floor** | **6.40 %** | **4.15 %** | **100.00 %** |
| **corr(A_null, floor_null)** | **+0.6805** | **+0.9485** | **undefined — zero variance** |
| draws beating the observation | 57 | 0 | **0** |
| their mean floor | 0.2879 | — | — |
| **more concentrated than the real partition** | **57 / 57 = 100 %** | — | — |

Three things follow, and the middle one is new.

1. **N1-a's upper tail is a coarser merge, not a better one.** Confirmed at bit-level against
   the parent. Under P2 the figure is 54/54.
2. **N1-b — the null the parent called "not confounded by concentration" — was the *more*
   confounded of the two.** Its draws track their own floor at **ρ = +0.9485**, against N1-a's
   +0.6805, and its mean floor sits **42 % above** the real partition's. It reached the right
   answer by subtracting the floor analytically, not by matching it. **A statistic that
   corrects for a confound is not a null that controls it**, and the parent's §9 did not
   distinguish the two.
3. **Neither parent null can draw the thing it compares against.** 6.40 % and 4.15 % of draws
   land within ±2 % of the real partition's concentration. `UNIT-DRIFT-DEFECT.md` §4.1 names
   this as the cheapest decisive diagnostic in the repository, and it settles both nulls before
   any p-value is read from them.

### 3.3 The new null, and why it cannot be gamed by concentration

Each draw assigns all 397 citation types to blocks whose verse-counts equal the observed
n₁ … n_K **exactly**. Three constructions were pre-registered, all processing types
largest-first with random tie-breaking and differing only in how the receiving block is chosen:
**S2** (probability ∝ remaining capacity — primary, chosen before locking as the least
mutually structured), **S1** (largest remaining capacity), **S5** (best fit).

**The gates, printed before any p-value:**

| gate | requirement | measured |
|:--|:--|:--|
| **G1 exactness** | every draw's floor identical to the observed; redraw rate < 1 %; p(E) = p(A) | **PASS** — max deviation **0.00 × 10⁰ across all 160,000 draws**; **0 redraws**; p(E) = p(A) in every arm |
| **G2 teeth** | the diagnostic must detect the known defect, ρ ≥ +0.50 on N1-a | **PASS** — ρ = **+0.6805** |
| **G3 non-degeneracy** | mean ARI vs the real partition < 0.10; sd(A_null) > 0.001 | **PASS** — max mean ARI **+0.0697**; min sd(A_null) **0.00208** |
| **G4 in-band** | share of draws within ±2 % of the real floor | **PASS — 100.0 %** in every arm (worst case over both tuples: N1-a **6.40 %**, N1-b **4.07 %**) |

**corr(A_null, floor_null) for the exact nulls is *undefined*, and that is the strongest
possible form of the diagnostic rather than a convenient zero: the chance floor has exactly
zero variance across draws.** Because the whole block-size multiset is held identical, so are
K, K_eff, the maximum class size and the Simpson index. **No draw can win by being coarser,
because no draw is coarser.** The only thing that varies between draws is which citation
endings share a class — which is precisely the phonological content under test.

**G3 is the clause that stops this from being conditioning-on-the-answer.** Mean adjusted Rand
index between a draw and the real pausal partition is **−0.008 to +0.022** for S2/S1/S5: the
draws are, by that measure, unrelated to the partition *waqf* produces.

---

## 4. RESULT 3 — the primary result

Primary statistic **E = A − Σpᵢ²**, pre-registered as primary *before* any output rather than
reached for after a failure. Under an exactly-matched null E and A are the same test, and the
runner verifies that their p-values are identical in every arm.

**Observed E: 0.36657 (P1), 0.36767 (P2).** α_bon = 0.00277778, k = 18.

| null | tuple | null E mean | sd | **null max** | #≥obs / 10,000 | **p** | z |
|:--|:--|--:|--:|--:|--:|--:|--:|
| **S2** (primary) | **P1** | 0.2266 | 0.0093 | 0.2635 | **0** | **0.0001** | **+15.03** |
| **S2** | **P2** | 0.2264 | 0.0092 | 0.2653 | **0** | **0.0001** | **+15.38** |
| S1 | P1 | 0.2298 | 0.0021 | 0.2387 | **0** | 0.0001 | +63.86 |
| S1 | P2 | 0.2300 | 0.0022 | 0.2386 | **0** | 0.0001 | +62.25 |
| S5 | P1 | 0.2604 | 0.0029 | 0.2712 | **0** | 0.0001 | +36.16 |
| S5 | P2 | 0.2688 | 0.0030 | 0.2788 | **0** | 0.0001 | +33.43 |

**Replication at seed 20260519 returns p = 0.0001 in all six arms**, with z within 0.3 of the
primary everywhere.

Stated in raw agreement rather than excess, which is easier to read: the corpus's adjacent
verse-ends rhyme in pause at **A = 0.5353**. Ten thousand regroupings of its own citation
endings, **identical in every measure of coarseness**, average **0.3953** and the best of them
reaches **0.4322**. The observation is 0.103 above the best of 10,000.

### 4.1 N-A — the exact within-size-class bound (non-gating, low power by declaration)

Pre-registered as a bound because its freedom was measured before locking: 370 of 397 types
movable (93.2 %) but carrying only **1,538 of 6,236 verses (24.7 %)**. The four largest
citation types have unique sizes and are frozen — the largest (1,656 verses) sits in the only
block whose total (1,751) can hold it, so **no exact-sum exchange can move it at all.**

Even holding three quarters of the verse mass in place: null E mean 0.2896, sd 0.0056, max
0.3084, **0 / 10,000, p = 0.0001, z = +13.74 (P1) / +13.92 (P2)**, both seeds.

### 4.2 N-STEM — the lexical-repetition control (non-gating)

*Waqf* merges the case-variants of one stem, and a stem recurs within a surah for lexical
reasons. Restricting to the **3,453 adjacent pairs whose two ends differ under the
truncation-only tuple P3** — pairs that no bare truncation of a shared skeleton can merge, and
whose merging requires the transformational rule *−an → ā*:

| tuple | observed merge rate | null mean | sd | null max | #≥obs | p |
|:--|--:|--:|--:|--:|--:|--:|
| P1 | **0.1836** | 0.0672 | 0.0160 | 0.1355 | **0 / 10,000** | **0.0001** |
| P2 | **0.1856** | 0.0670 | 0.0158 | 0.1352 | **0 / 10,000** | **0.0001** |

**2.7× the null, outside its entire support.** The effect is not an artefact of the same stem
recurring in different cases.

---

## 5. RESULT 4 — the three control texts

### 5.1 Positive control — pre-Islamic poetry. Behaves exactly as locked.

Pooled readable pairs, n = 234, from the three muʿallaqāt selected by the parent's
pre-declared ≥ 0.9 line-final vocalisation threshold.

| | A(C) | A(P1) | Δ |
|:--|--:|--:|--:|
| Imruʾ al-Qays (n = 71) | 0.4507 | 0.4930 | +0.0423 |
| Zuhayr (n = 61) | 0.5082 | 0.5082 | **0.0000** |
| ʿAmr b. Kulthūm (n = 102) | **0.9804** | **1.0000** | +0.0196 |
| **pooled** | **0.6966** | 0.7179 | **+0.0214** |
| *Qurʾān* | *0.3484* | *0.5353* | ***+0.1869*** |

- **D4a passes: poetry rhymes twice as well as this corpus at citation form** (0.6966 vs
  0.3484). It is monorhymed by construction and does not need pausal reduction.
- **D4b: Δ_Qurʾān − Δ_poetry = +0.1655 (P1) / +0.1666 (P2), p = 0.0001**, both seeds.

**The R1 arms of D4b FAIL at α — p = 0.0257 and 0.0233 — and are reported as failures.** They
are non-gating by pre-registration, and the reason they fail is understood: R1 reads the tanwīn
nūn as the rāwī and so understates this corpus's Δ roughly threefold (+0.0657 against
+0.1869), which shrinks the gap to poetry. Two of the eighteen registered inferences do not
clear α, and they are named here rather than left in the JSON.

### 5.2 Negative control — prose. **The delta is still not computable, and that is unchanged.**

> ## ⛔ CORRECTION NOTICE — 2026-08-07, same day: THIS SECTION'S CONCLUSION IS WRONG
>
> **"A census of all 36 baseline corpora on disk found no vocalised prose at all" is true as
> written and false as reasoned. The census enumerated `data/baseline-corpora/` only.**
> A repository-wide ḥarakāt census run for H-NEW-2890 found
> `data/literature/hadith/ahmedbaset-json/`, committed since 2026-04-28: **50,884 fully
> vocalised ḥadīth across nine canonical books**, at ḥarakāt densities of 0.7702–0.8829
> against this corpus's own **0.7801**. **The control could be run, and H-NEW-2890 runs it.**
>
> - **Every number in this section stands.** The `baseline-corpora` files really do carry zero
>   ḥarakāt, so the skeleton level comparison below is unaffected.
> - **The conclusion "the delta is not computable" does not stand.** It should have read: not
>   computable *from the baseline corpora*.
> - The error is mine, it is a scope error in a census rather than a fault in any measurement,
>   and the lesson is the cheap one: **an absence claim is only as wide as the search that
>   produced it — state the search, not just the absence.**
>
> **The control's result, for anyone reading this section for it:** vocalised ḥadīth prose gains
> **Δ = +0.030 to +0.033** at its own composed boundaries, against this corpus's **+0.1869** —
> about one sixth — and its excess over its own exactly-matched null is **z = +1.3 to +3.2**
> against this corpus's **z = +15.03**. **The control behaves.** See
> `h-new-2890-vocalised-prose-control.md`.

Re-measured: `bukhari-noquran.txt` carries **0** ḥarakāt over 2,056,880 Arabic characters;
`jahiz-hayawan.txt` **0** over 1,422,374. A census of all 36 baseline corpora on disk found no
vocalised prose at all (`sira-ibn-hisham.txt` 0 over 1,090,188; `bukhari.txt` 0.61 %,
scattered). **The citation form cannot be recovered from a text that never wrote its final
short vowels**, and automatic vocalisation would substitute a model's output for data.

**This remains a gap in the evidence, not a result.** What is computable is a **level**
comparison on the skeleton instrument, length-matched, 200 cuts:

| text | A(skeleton) | |
|:--|--:|:--|
| poetry | 0.8917 | monorhyme |
| **Qurʾān** | **0.5521** | |
| al-Bukhārī | 0.0849 (max 0.0944) | Qurʾān at percentile **1.000** |
| al-Jāḥiẓ | 0.0754 (max 0.0869) | Qurʾān at percentile **1.000** |

**That is a statement about rhyme density, not a control on the delta, and it is not described
as one.**

### 5.3 The within-corpus re-cut — the effective negative control on the delta

Re-cut each surah's own word stream into the same number of units whose lengths are a random
permutation of that surah's own verse lengths. Identical text, vocabulary, orthography,
vocalisation and length profile; only the boundaries are not composed. **No baseline text is
used, so no genre-matching objection reaches it.**

| rime | tuple | observed Δ | re-cut mean | sd | re-cut max | #≥obs / 2,000 | p | z |
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
| **R2** | P1 | **+0.1869** | +0.0284 | 0.0022 | +0.0354 | **0** | **0.0005** | **+70.7** |
| R2 | P2 | +0.1880 | +0.0297 | 0.0023 | +0.0379 | **0** | 0.0005 | +69.1 |
| R1 | P1 | +0.0657 | +0.0161 | 0.0024 | +0.0230 | **0** | 0.0005 | +21.0 |
| R1 | P2 | +0.0668 | +0.0175 | 0.0024 | +0.0243 | **0** | 0.0005 | +20.5 |

12.84 % of re-cut boundaries coincidentally land on a true verse end. **Arabic word-final
morphology gives Δ ≈ +0.028 wherever you cut; the fāṣila positions give +0.187.** All four
arms replicate.

---

## 6. RESULT 5 — per-surah

Under R2, across 114 surahs: **Δ > 0 in 94, Δ = 0 in 20, Δ < 0 in none.** Mean Δ = **+0.2147**.

| surah | n | A(C) | A(P1) | Δ | classes C → P1 |
|:--|--:|--:|--:|--:|:--|
| Q65 al-Ṭalāq | 12 | 0.000 | 1.000 | +1.000 | 9 → 1 |
| Q108 al-Kawthar | 3 | 0.000 | 1.000 | +1.000 | 3 → 1 |
| Q112 al-Ikhlāṣ | 4 | 0.000 | 1.000 | +1.000 | 3 → 1 |
| **Q18 al-Kahf** | **110** | **0.110** | **1.000** | **+0.890** | **53 → 1** |
| Q48 al-Fatḥ | 29 | 0.179 | 1.000 | +0.821 | 9 → 1 |
| Q33 al-Aḥzāb | 73 | 0.167 | 0.972 | +0.806 | 17 → 2 |
| Q105 al-Fīl | 5 | 0.000 | 0.750 | +0.750 | 4 → 2 |
| Q4 al-Nisāʾ | 176 | 0.194 | 0.943 | +0.749 | 28 → 5 |

**Q18 al-Kahf needs no p-value.** Read with full iʿrāb, its 110 verse-ends fall into 53 rime
classes and 11 % of adjacent pairs rhyme. Read in pause they fall into one class and every
adjacent pair rhymes. The rescued set is not the short mufaṣṣal — Q4 (176 verses), Q33 and Q48
are long Medinan surahs.

---

## 7. Verdict — diffed against the pre-registration before declaration

The runner printed prereg §8's grid verbatim, then its computed decisions, then the verdict.

| registered inference | result |
|:--|:--|
| D1 — Δ > 0 under P1 and P2 | **True** (+0.1869, +0.1880) |
| D4a — poetry out-rhymes this corpus at citation form | **True** (0.6966 vs 0.3484) |
| **tests 1–6 — D2 under {S2, S1, S5} × {P1, P2}** | **all True, p = 0.0001 each, both seeds** |
| tests 7–8 — N-A (non-gating) | True, p = 0.0001 |
| tests 9–10 — N-STEM (non-gating) | True, p = 0.0001 |
| tests 11–12 — D3 re-cut, R2 | True, p = 0.0005 |
| tests 13–14 — D3 re-cut, R1 | True, p = 0.0005 |
| tests 15–16 — D4b poetry, R2 | True, p = 0.0001 |
| tests 17–18 — D4b poetry, **R1** | **False**, p = 0.0257 / 0.0233 — non-gating, §5.1 |

> ## **VERDICT: PASS**
>
> Tests 1–6 all pass and D3 passes under both tuples. Sixteen of eighteen registered
> inferences clear α = 0.00277778; the two that do not are the non-gating R1 poetry arms.

**The fāṣila is materially better defined at pausal phonology than at citation form, and the
margin is not the collapse arithmetic.** Of the +0.1869 delta, +0.0619 (33.1 %) is the free
gain from concentration and +0.1250 (66.9 %) is not — and that remainder lies outside the
entire support of ten thousand regroupings whose concentration is identical to the observed
one by construction, under three different constructions, at two seeds.

> **⚠ Do not cite this verdict without §10.** A post-hoc check run after the verdict was
> locked shows the deliberately **wrong** pausal tuple also clears its own exact null at
> 0 / 10,000. The exact null discriminates the pausal *family* from random regrouping; within
> that family the correct rules are stronger by measurement (z = +15.0 vs +9.0) and not by
> kind.

---

## 8. What this does and does not change about H-NEW-2870

- **H-NEW-2870's locked verdict of NULL is not overturned by fiat and is not being rewritten.**
  It was the correct verdict of its own locked grid, which required the ill-posed N1-a.
- **What is established here is that the arm which produced it could not have returned any
  other answer**, because its winning draws were coarser merges by construction — and,
  additionally, that its *other* null was more floor-confounded still.
- **H-NEW-2870 §10's "my reading, labelled as judgement" is now a measured result.** The
  author declined to overturn a locked verdict on post-hoc grounds and instead named the test
  that would settle it. That was the right call, and this is that test, pre-registered.
- **The parent's descriptive results are untouched and all reproduce**: the 3.42× collapse, the
  33.1 % arithmetic share, the re-cut z = +70.7, and Q18's 53 → 1.

---

## 9. Honest limits

1. **The prose delta is still not computable** (§5.2), and no amount of method fixes it. The
   claim "prose would gain little" remains **untested**. This is the single biggest gap, it was
   the parent's biggest gap, and acquiring a vocalised prose corpus would close it.
2. **A PASS here means *waqf*'s merges group endings that actually stand next to each other in
   the mushaf, where a random regrouping of identical coarseness does not. It does NOT mean
   that only *waqf*'s rules do so — and §10 measures that.** The deliberately **wrong** pausal
   tuple P3 also clears its own exactly-matched null at 0 / 10,000. The discrimination between
   a right and a wrong account of waqf is quantitative (z = +15.0 vs +9.0; Δ = +0.187 vs
   +0.088), not categorical. **Anyone citing §4 must cite §10 with it.** The strongest
   available form of the specific claim is the 55.4 % of merged pairs that require the
   transformational rule *−an → ā*, which P3 lacks.
3. **The exact null conditions on the observed class-size profile, which *waqf* itself
   produces.** That is what a matched null is for — the size profile is the nuisance and the
   assignment is the signal — but it means the result is conditional on that profile and says
   nothing about why the profile is what it is.
4. **N-A's freedom is 24.7 % of the verse mass**, and no exact-sum null can do better: the
   largest citation type is provably immovable. Its pass is real but it is a bound, not a
   second independent test.
5. **The "citation form" is the Ḥafṣ mushaf's written iʿrāb**, itself a recitational tradition
   rather than a neutral pre-recitational baseline. The contrast is waṣl-vs-waqf *within* one
   reading.
6. **No classical anchor is cited, because none is on disk in citable form.** The parent
   established this: al-Suyūṭī's Itqān PDF is Muneer Fareed's partial translation and lacks the
   *waqf* nawʿ entirely; al-Zarkashī's *Burhān*, which has it, is a scan with no text layer
   (`pdftotext` returns 0 characters); no Ibn al-Jazarī *al-Nashr* or al-Dānī is present.
   **No citation was invented.** Acquisition need: a text-layer *al-Burhān* or *al-Nashr* vol. 1.
7. **The pairwise-adjacency statistic ignores rhyme structure beyond immediate neighbours.** A
   surah rhyming ABAB scores 0 and is not distinguished from an unrhymed one.
8. **The poetry arm is 234 pairs from three poems**, four of the seven muʿallaqāt having been
   excluded by the pre-declared vocalisation threshold.
9. **Two of eighteen registered inferences fail at α** (§5.1). They are non-gating and the
   reason is understood, but they are failures and are reported as such.

---

## 10. POST-HOC — the deflation check

*Declared post-hoc. Gates nothing. Run after the locked verdict was computed, printed and
written to the run directory. It was chosen because it can only weaken the headline.*

**Question: does the exact null get beaten by *any* vowel-truncating reduction, or specifically
by the waqf rules?** P3 is the deliberately **wrong** pausal tuple pre-registered by the parent
— it drops tanwīn fatḥ without the compensatory alif, which is not what *waqf* does in any
reading. If P3 also sits far outside its own exactly-matched null, then what §4 establishes is
a property of the whole family of final-vowel-truncating reductions rather than of *waqf*'s
rules, and this finding must say so.

**It does, and this finding says so.** Each tuple is tested against a null matched exactly to
*its own* class-size profile (P3's is a different partition — 213 classes, floor 0.1415 — and
it too is a clean coarsening of the citation partition, 0 split types).

| tuple | K | its own floor | Δ vs citation | E_obs | null E mean | null max | #≥obs | p | **z** |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **P1** — waqf, minimal | 116 | 0.1687 | **+0.1869** | 0.3666 | 0.2266 | 0.2635 | 0 | 0.0001 | **+15.03** |
| **P2** — waqf, full | 115 | 0.1688 | +0.1880 | 0.3677 | 0.2264 | 0.2653 | 0 | 0.0001 | **+15.38** |
| **P3** — deliberately wrong | 213 | 0.1415 | **+0.0876** | 0.2944 | 0.2301 | 0.2663 | **0** | **0.0001** | **+8.99** |

**P3 also clears its own exact null at 0 / 10,000** (replication z = +8.94). **The
discrimination between a correct and an incorrect account of waqf is therefore quantitative,
not categorical**, and §4's result must be read as follows:

> The exact-concentration null is beaten by the **family** of final-vowel-truncating
> reductions, not by *waqf*'s rules uniquely. Within that family the correct rules are
> measurably stronger — **z = +15.0 against +9.0, and Δ = +0.187 against +0.088, a 2.1× larger
> delta** — but a reader must not take §4 as evidence that *only* waqf's rules work.

**Why the gap is where it is.** Splitting the adjacent pairs *waqf* actually merges:

| tuple | cross-type pairs merged by waqf | a bare truncation would also merge these | **require the transformational rule *−an → ā*** |
|:--|--:|--:|--:|
| P1 | 1,144 | 510 | **634 (55.4 %)** |
| P2 | 1,151 | 510 | **641 (55.7 %)** |

**More than half of *waqf*'s merging work is done by the single rule P3 gets wrong** — the one
that turns `naṣīran` into `naṣīrā` and gathers phonologically unlike stems into one open-`ā`
class. That is the same 634 pairs the N-STEM control tests (§4.2), where they beat the null at
2.7× and 0 / 10,000. **The rules-tuple is load-bearing, and it is load-bearing by a measured
55 %**, which is the sharpest form in which this finding supports the specific waqf account
over a generic one.

---

## 11. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2880-pausal-retest.md`
  (SHA-256 `87083f50d56cd9802a5656ebc3049da98ee0397e6a0dda657e4d3dbbebe052ab`, verified at runtime)
- Runner: `findings/phase-b-hypotheses/scripts/h-new-2880.py`
- Post-hoc: `findings/phase-b-hypotheses/scripts/h-new-2880-posthoc.py`
- Run: `runs/h-new-2880/20260807T141104Z/` (`result.json`, `console.log`, `MANIFEST.txt`)
- Checkpoints: `scratch/h-new-2880-checkpoints/` — **outside** the run directory, write-once
- JSON: `findings/phase-b-hypotheses/csv/h-new-2880.json`, `csv/h-new-2880-posthoc.json`
- Parent: `h-new-2870-pausal-rhyme.md` and its pre-registration; instrument pinned by SHA-256
- Method: `findings/UNIT-DRIFT-DEFECT.md` §4.1; `STATE-OF-THE-PROJECT-2026-08-07.md` §§0, 4

*Bismillāhi al-Raḥmāni al-Raḥīm.*
