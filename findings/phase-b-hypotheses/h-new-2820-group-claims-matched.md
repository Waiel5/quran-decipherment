---
finding_id: H-NEW-2820
title: The two highest-citation flagged claims are group comparisons — one collapses to its denominator, the other reverses into a real cluster
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
target_claims: [H-NEW-126 Cell A, H-NEW-570 PRIMARY]
prereg: findings/phase-b-hypotheses/prereg-h-new-2820-group-claims.md
prereg_sha256: 45abd95012bbf520070685646af909428a183781d94c58c4638353281764b5f1
run: findings/phase-b-hypotheses/runs/h-new-2820/20260807T085952Z/
run_posthoc: findings/phase-b-hypotheses/runs/h-new-2820-posthoc/20260807T090239Z/
rule_applied: findings/UNIT-DRIFT-DEFECT.md §3 Screen B (grouping form), §6.1, §6.3, §7, §8
method_parent: [H-NEW-2790, H-NEW-2770, H-NEW-2760, H-NEW-2720, H-NEW-2680, H-NEW-2810]
seeds: 20260509 primary / 20260519 replication
n_perm: 10000 Quran arms / 2000 per baseline offset / 200 offsets per baseline
status: >-
  Both claims reproduce exactly — 43 of 43 checks, including every registered distinguishing
  output, two of them to fifteen significant digits. Under a null that permutes group membership
  within quantile bins of the group's own dominant imbalance channel, the two claims move in
  OPPOSITE directions. H-NEW-126 Cell A DOES-NOT-SURVIVE: its 2.64x enrichment falls to 1.002x
  and p rises from 0.0009 to 0.459. H-NEW-570's published NULL REVERSES-CLUSTERED: the
  muqattaat-29 fall from the 65.62nd percentile to the 0.45th, crossing the claim's own 10%
  bar, and the hawamim-7 from 20.90 to 0.05.
verdict: >-
  H-NEW-126 Cell A is its denominator. Cutting al-Bukhari or al-Jahiz at the same five surah
  slots reproduces the effect at z = +3.19 and +3.55 against the Quran's +3.79, and 79% of the
  published enrichment is delivered by the mechanical Jaccard ceiling min|R|/max|R| using no
  vocabulary overlap at all. H-NEW-570 is the opposite error and the more consequential one:
  its size-blind null never once drew a set as large as the muqattaat (0 of 10,000), so it
  priced a comparison that does not exist. Matched, the muqattaat ARE a content cluster and the
  hawamim strongly so. "Muqattaat is ORTHOGONAL to content", "al-Suyuti EMPIRICALLY VINDICATED"
  and "al-Biqai empirically UNSUPPORTED" are withdrawn as empirical results.
---

# H-NEW-2820 — Two group claims, one matched null, two opposite answers

**Pre-reg SHA-256 `45abd950…64b5f1`, runtime-verified. Eleven frozen inputs SHA-verified.
The H-NEW-2680 partition code is lifted verbatim by the H-NEW-2720 mechanism, three fragments
SHA-checked before `exec`. Both matrix paths are asserted **bit-identical** to the published
routines at startup (`0.341385569426902`, `0.938813123152709` — exact equality, not a
tolerance). Run 40 s. Written under the corrected write-once rule: the run directory is created
with `exist_ok=False`, every file in it is opened with mode `'x'`, and `results.json` is written
exactly once at completion.**

---

## 0. Why this batch exists

`findings/UNIT-DRIFT-DEFECT.md` §8 records the most transferable result of the day: two audit
lanes applied the same three screens to the same repository, **agreed on every claim they both
saw**, and were both structurally blind to an entire class. Screen B asked only about
*orderings*. The two highest-citation flagged claims in the repository compare **groups** —
H-NEW-126 at 32 external citing files, H-NEW-570 at 30. **Fifty-nine citations' worth of
load-bearing claims sat outside the screen's reach while the screen reported clean
convergence.**

Neither had ever met a null that holds unit size fixed. H-NEW-126's own file names the confound
and queues the test as "H-NEW-126.1"; **H-NEW-126.1 has no script and no JSON and was never
run.** This finding discharges it, and does the same for H-NEW-570.

**The nuisance parameter for a group comparison is compositional imbalance, not drift.** A
grouping needs no monotone trend to carry the defect. It only needs the groups to differ.

---

## 1. Both claims reproduce — 43 of 43 checks, including the distinguishing outputs

Per H-NEW-2810, reproducing a headline scalar is not reproducing a computation. Every
distinguishing output registered in pre-reg §4 was checked. **None failed.**

| claim | check | published | recomputed |
|:--|:--|--:|--:|
| **126 Cell A** | mean pairwise root-Jaccard | 0.3414 | **0.341385569426902** |
| 126 Cell A | null mean / p | 0.1291 / 0.0009 | 0.12909 / 0.00090 |
| 126 Cell A | MW-5 ḥawāmīm {40–44} obs / p | 0.3062 / 0.0046 | 0.30623 / 0.00460 |
| 126 Cell C | obs / null / p | 5.32 / 14.83 / 0.0157 | 5.3223 / 14.8295 / 0.01570 |
| 126 Cell C | MW-5 musabbiḥāt obs / p | 16.08 / 0.6732 | 16.0791 / 0.67323 |
| 126 Cell D | all five top-extremity axes and percentiles | — | **identical** |
| 126 profile | verse counts, mean verse lengths, root counts (5 surahs) | — | **identical** |
| **570 PRIMARY** | d̄ | 0.9388131231527093 | **0.938813123152709** |
| 570 PRIMARY | percentile | 65.62 | 65.62 |
| 570 MW-5 | ḥawāmīm-7 d̄ / pct | 0.8672422857142857 / 20.90 | 0.867242285714286 / 20.90 |
| 570 MW-6 | non-muq-29 d̄ / pct | 1.0228183201970442 / 100.00 | 1.022818320197044 / 100.00 |

**Neither claim is UNVERIFIABLE and neither is `REPRODUCTION-PARTIAL`.** Nothing below says any
published arithmetic is wrong. What is challenged is what the numbers measure.

**One correction to the queue's description of H-NEW-570, made before the test was designed.**
H-NEW-2790 §12 lists its statistic as *"eight density measures, muq vs non-muq"* with
denominator *"verse count"*. The script computes **one** statistic — a mean pairwise Fisher–Rao
distance over root distributions — and its exposure is unit size entering the smoothed
distribution, not a verse-count division. The test here is built on the actual statistic.

---

## 2. The imbalance, quantified — and one channel that cannot be matched at all

Measured on the 114 surahs before any null was designed, as the standing rule requires.

| channel | **core-5** | other 109 | ratio of medians | Cohen's *d* | | **muq-29** | non-muq-85 | ratio | *d* |
|:--|--:|--:|--:|--:|:-:|--:|--:|--:|--:|
| mean verse length | 11.64 | 8.11 | **1.44×** | 0.58 | | 14.17 | 5.00 | **2.84×** | 0.82 |
| verse count | 112.0 | 36.0 | **3.11×** | 1.08 | | 85.0 | 26.0 | **3.27×** | 1.20 |
| word count | 1174 | 312 | **3.76×** | 1.03 | | 853 | 200 | **4.27×** | 1.26 |
| unique root-set size | 284 | 112 | **2.54×** | 1.05 | | 225 | 91 | **2.47×** | 1.18 |
| Nöldeke rank | 66 | 55 | 1.20× | 0.56 | | 74 | 44 | 1.68× | 0.55 |
| mushaf position | 22 | 60 | 0.37× | −1.17 | | 29 | 72 | 0.40× | −1.38 |
| proportion Medinan | 0.200 | 0.248 | — | −0.05 | | 0.103 | 0.294 | — | **−0.19** |

*(These use `real_words()`, the tokenizer H-NEW-126's own profile table uses, which §1 validates.
Under the whitespace tokenizer H-NEW-2790 §12 used, the muqaṭṭaʿāt ratios reproduce that
section **exactly** — 2.980× / 3.269× / 4.336× against its 2.98 / 3.27 / 4.34. The two
tokenizers are both correct and the difference is worth naming rather than papering over.)*

### 2.1 Dominant channel, ranked on the data before use (pre-reg §3.1)

ρ between each published-null draw's statistic and that draw's mean log channel value:

| H-NEW-126 (`J̄`) | ρ | | H-NEW-570 (`d̄`) | ρ |
|:--|--:|:-:|:--|--:|
| **log root-set size** | **+0.9398** | | **log word count** | **+0.8998** |
| log word count | +0.9219 | | log root-set size | +0.8554 |
| log verse count | +0.7926 | | log verse count | +0.8395 |
| log mean verse length | +0.7688 | | log mean verse length | +0.6509 |

**The strongest channel is a different variable for each claim, exactly as it is for the two
orderings.** Both statistics rise steeply with set size — `d̄` at ρ = +0.90, confirming
H-NEW-2720's `r(d̄_content, log size) = +0.956` in a different design.

### 2.2 Two facts that settle H-NEW-570 before any p-value

**(a) The published null never drew a set as large as the muqaṭṭaʿāt. Not once in 10,000.**
The A1 conditional-exceedance arm restricts the published null to draws whose mean log word
count reaches the group's. For the muqaṭṭaʿāt, `n_restricted = 0`. **The null against which
"median-level" was scored contains no comparison set of comparable size at all.**

**(b) The muqaṭṭaʿāt cannot be size-matched from the non-muqaṭṭaʿāt at all.** The A2d
sensitivity arm — donor pool restricted to the 85 non-muqaṭṭaʿāt — returns `NOT-ESTIMABLE`:
**bin 3 of 5 requires 14 donors and contains 9.** The muqaṭṭaʿāt so dominate the upper size
range that a 29-surah size-matched non-muqaṭṭaʿāt comparison group does not exist in this
corpus. This is `h-new-46`'s STRONG-PASS result stated as an impossibility rather than a
correlation, and it is the sharpest available form of the imbalance.

---

## 3. The result — every arm, direction and magnitude

Seed 20260509. `ratio` = observed ÷ null mean. **No arm is reported as pass/fail alone.**

### 3.1 H-NEW-126 Cell A — the enrichment is the root-set size

| arm | null mean | **ratio** | z | **p** |
|:--|--:|--:|--:|--:|
| published null (regenerated draw-for-draw) | 0.12909 | **2.644×** | +3.792 | **0.00090** |
| A1 conditional exceedance *(n = 14, underpowered)* | 0.31746 | 1.075× | +0.912 | 0.20000 |
| **A2-k5 stratified — PRIMARY** | **0.34062** | **1.002×** | **+0.038** | **0.45885** |
| A2-k10 stratified (finer) | 0.33581 | 1.017× | +0.329 | 0.35736 |
| A2b caliper w = 11 (strictest) | 0.33615 | 1.016× | +0.288 | 0.36306 |
| A2c cross-stratified × period | 0.34189 | 0.999× | −0.026 | 0.48195 |

Observed `J̄ = 0.34139` throughout. **Under matching the null mean rises from 0.129 to 0.341 —
it becomes the observed value.** The published "2.64× enrichment, p = 0.0009" becomes
**1.002×, p = 0.459**, and under the cross-stratified arm the core-5 fall marginally *below*
their own null mean. **Every arm agrees**; there is no lenient/strict split to adjudicate.

### 3.2 H-NEW-570 PRIMARY — the null reverses

| arm | null mean | ratio | z | **percentile** |
|:--|--:|--:|--:|--:|
| published null (regenerated) | 0.92353 | 1.017× | +0.455 | **65.62** |
| A1 conditional exceedance | — | — | — | **no draw qualifies (n = 0/10,000)** |
| **A2-k5 stratified — PRIMARY** | **0.97385** | **0.964×** | **−2.426** | **0.45** |
| A2-k10 stratified (finer) | 0.97061 | 0.967× | −2.232 | **0.82** |
| A2c cross-stratified × period | 0.95794 | 0.980× | −1.639 | **5.44** |
| A2d pool = 85 non-muqaṭṭaʿāt | — | — | — | **NOT-ESTIMABLE** (§2.2b) |

Observed `d̄ = 0.93881`. The claim's own locked threshold is `pct ≤ 10.0`. **It is crossed in
every estimable matched arm, at both bin widths, in both seeds.** The muqaṭṭaʿāt are **3.6 %
tighter in content than size-matched surah sets**, which is a small effect, and it sits at the
0.45th percentile of a properly-matched null, which is a strong one.

**A third of the matched effect is Meccan/Medinan composition, not size.** Adding period to the
stratification moves z from −2.426 to −1.639 — a **32 % attenuation** — and the percentile from
0.45 to 5.44. The verdict holds under the strictest arm, at reduced strength, and that reduced
strength is the number a reader should carry.

### 3.3 H-NEW-570 MW-5 — the ḥawāmīm are not "moderate only"

| arm | null mean | ratio | z | percentile |
|:--|--:|--:|--:|--:|
| published null | 0.92301 | 0.940× | −0.690 | **20.90** |
| A1 conditional exceedance *(n = 442, powered)* | 0.99563 | 0.871× | −3.176 | **0.00** |
| **A2-k5 — PRIMARY** | 0.97124 | **0.893×** | **−2.736** | **0.05** |
| A2-k10 (finer) | 0.96901 | 0.895× | −2.662 | **0.02** |
| A2c cross-stratified × period | 0.94430 | 0.918× | −2.576 | **0.21** |

The ḥawāmīm-7 are **10.7 % tighter** than size-matched sets and sit below the 0.25th percentile
in every arm including the parameter-free one. The finding's §4 reads *"MODERATE cohesion —
above-null but not corpus-extreme"*; **against a size-matched null they are corpus-extreme.**

### 3.4 Replication

**Every classification is identical at seed 20260519.** 126: p = 0.45455 / 0.34657 / 0.35866 /
0.47975 across the four matched arms. 570: percentile 0.39 / 0.66 / 5.48. MW-5: 0.06 / 0.06 /
0.37. Nothing here is `SEED-FRAGILE`.

---

## 4. The genre control — and it splits the two claims cleanly

`build_pseudo_corpus` cuts each baseline to **the Qurʾān's exact verse word-length profile** and
`group_matched` applies **the Qurʾān's exact surah verse counts**, so the pseudo-group taken at
the *same surah indices* has **identical verse counts, identical verse lengths and identical
word counts to the real group, to the token**. Same imbalance, no content mechanism. 200 offset
partitions per baseline. Surface word types in all three corpora, since no baseline has a
morphological analyser — the Qurʾān's own surface-word values are the like-for-like reference.

### 4.1 H-NEW-126: the baselines reproduce it, and after matching they beat the Qurʾān

| | Qurʾān (surface) | al-Bukhārī (200 offsets) | al-Jāḥiẓ (200 offsets) |
|:--|--:|--:|--:|
| observed `J̄` | 0.1330 | 0.1050 / **0.1462** / 0.2018 | 0.0743 / **0.0910** / 0.1092 |
| **unmatched p** | **0.0020** | 0.0005 / **0.0015** / 0.1094 | 0.0005 / **0.0010** / 0.0185 |
| unmatched z | +3.816 | +1.337 / **+3.190** / +5.866 | +2.439 / **+3.553** / +5.067 |
| offsets clearing p < 0.0125 | — | **91.0 %** | **97.5 %** |
| **matched p** (log word count) | **0.0930** | 0.0005 / **0.0347** / 0.9290 | 0.0005 / **0.0215** / 0.7721 |
| offsets clearing matched p < 0.0125 | — | **34.5 %** | **40.0 %** |
| offsets with matched p ≤ the Qurʾān's | — | **67.5 %** | **72.5 %** |

*(min / median / max across offsets.)*

**Cutting a ḥadīth collection or a book of adab zoology at the same five slots produces the same
"shared-vocabulary core" — at z = +3.19 and +3.55 against the Qurʾān's +3.79, and 91–98 % of
arbitrary offsets clear the claim's own bar.** After matching, **the baselines are the more
extreme ones**: two-thirds to three-quarters of offsets have a *smaller* matched p than the
Qurʾān's, and a third of them still clear α_bon while the Qurʾān clears it in neither instrument.
This is the H-NEW-2680 shape, and a pass/fail report would have hidden it.

### 4.2 H-NEW-570: the baselines do NOT reproduce the reversal

| | Qurʾān (surface) | al-Bukhārī | al-Jāḥiẓ |
|:--|--:|--:|--:|
| observed `d̄` | 0.9417 | 0.8434 / **0.9135** / 0.9628 | 0.9149 / **0.9478** / 0.9843 |
| unmatched percentile | 86.10 | 5.25 / **50.80** / 97.45 | 93.25 / **99.32** / 100.00 |
| **matched percentile** (log word count) | **0.80** | 0.00 / **44.28** / 99.30 | 0.80 / **37.72** / 100.00 |
| offsets with matched pct ≤ 10 | — | **16.5 %** | **16.0 %** |
| offsets with matched pct ≤ the Qurʾān's | — | **2.0 %** | **0.5 %** |

**The registered `-GEOMETRIC` modifier does not fire.** Pre-reg §6.2 suffixes a reversal
`-GEOMETRIC` if a baseline's **median** matched percentile lands in the same tail. Neither does:
al-Bukhārī 44.28, al-Jāḥiẓ 37.72, both mid-range. **The stratification does not, by itself, push
an arbitrary partition into the tail.**

**The honest caveat, stated at full weight: about one arbitrary partition in six does land at
`pct ≤ 10`.** The claim's own 10 % bar is therefore loose against this design, and a reversal
that merely cleared 10 % would be worth little. The Qurʾān is at **0.45** (root instrument) and
**0.60–0.80** (surface instrument) — **beyond 98–99.5 % of baseline offsets**, in two
independent instruments. That margin, not the bar, is what carries the verdict.

**The reversal also holds in a second instrument.** Root-level Fisher–Rao gives 0.45; surface
word-type Fisher–Rao gives 0.60 and 0.80. The published statistic and an instrument built for
the baselines agree.

---

## 5. Post-hoc, descriptive, quarantined — computed after the verdicts

Not pre-registered, enters no decision rule, moves nothing. Own run directory.

**(a) 79 % of H-NEW-126's published enrichment is the mechanical ceiling.** Jaccard is bounded
above by `min(|R_a|,|R_b|) / max(|R_a|,|R_b|)`, which uses **no vocabulary overlap at all**.

| | core-5 | random-5 null | ratio |
|:--|--:|--:|--:|
| observed `J̄` | 0.34139 | 0.12866 | **2.653×** |
| **mechanical ceiling** `min\|R\|/max\|R\|` | **0.83761** | **0.39792** | **2.105×** |
| "fill" (observed ÷ own ceiling) | 0.40757 | 0.32281 | 1.263× |

**2.105 / 2.653 = 79.3 %.** The core-5 are five surahs of similar, large root-set size, and
similarity of size alone delivers four-fifths of the published effect. *(This null is a fresh
10,000-draw sample rather than the published RNG's, so its mean is 0.12866 against §3.1's
0.12909 and its enrichment 2.653× against 2.644×; the two agree to Monte-Carlo error and the
ceiling ratio is unaffected.)*

**(b) The instrument is not simply dead — it still fires on a real cluster after matching.**
H-NEW-126's own MW-5 positive control, the ḥawāmīm {40–44}, run through the identical matched
arms:

| arm | ratio | z | p |
|:--|--:|--:|--:|
| published null | 2.360× | +3.104 | 0.00460 |
| A1 conditional exceedance *(n = 640)* | 1.214× | +1.577 | 0.07176 |
| A2-k5 | 1.176× | +2.179 | **0.02120** |
| A2-k10 | 1.212× | +3.485 | **0.00010** |
| A2b caliper | 1.140× | +1.907 | 0.04770 |
| A2c × period | 1.136× | +1.912 | 0.04320 |

**The ḥawāmīm keep a real residual under matching (1.14–1.21×) while the core-5 fall to
1.002×.** This matters for how §3.1 should be read: the matched null is not so strict that
nothing can pass it. It still detects a cluster the tradition independently names — and detects
nothing whatever for the isolate core. *(The k = 5 / k = 10 arms disagree in strength here,
0.0212 against 0.0001; both are reported and neither is decisive, since this arm carries no
verdict.)*

---

## 6. Verdicts

**Diffed clause-by-clause against pre-registration §6 before declaring, and again after.**

| claim | published | **locked verdict** | the one number |
|:--|:--|:--|:--|
| **H-NEW-126 Cell A** | PASS-DIRECTED, p = 0.0009, 2.64× | **`DOES-NOT-SURVIVE`** | matched enrichment **1.002×**, p **0.459**; the null mean rises to equal the observed value |
| **H-NEW-570 PRIMARY** | NULL, 65.62 %ile, "orthogonal" | **`REVERSES-CLUSTERED`** | matched percentile **0.45** against its own 10 % bar; the size-blind null drew a comparable set **0 times in 10,000** |
| H-NEW-570 MW-5 ḥawāmīm-7 | "MODERATE only", 20.90 %ile | *(distinguishing output)* | matched percentile **0.05**; **10.7 % tighter** than size-matched sets |

Both classifications are identical at the replication seed. Neither is `SEED-FRAGILE`.

### 6.1 Two gaps between the runner and the pre-registration, found by doing the diff

Disclosed because the diff is what found them, which is the argument for doing it.

1. **The `-GEOMETRIC` modifier of §6.2 is not implemented in the runner.** I applied it by hand
   from the recorded baseline medians (44.28, 37.72 — neither in the lower tail), so **it does
   not fire**, and §4.2 shows the determination. Had a baseline median landed in the tail, the
   runner would have returned an unsuffixed verdict and been wrong.
2. **The runner collapses §6.1's `GENRE-SHARED-BUT-LARGER` / `GENRE-SHARED-AND-SMALLER` into a
   single `GENRE-SHARED` label, and adds a `SURVIVES-PRIMARY-ONLY` label §6.2 does not name.**
   Both branches are unreached — H-NEW-126 exits at `DOES-NOT-SURVIVE`, H-NEW-570 at
   `REVERSES-CLUSTERED`, and both of those clauses match the pre-registration exactly.

**The predictions in pre-reg §5 were two-thirds right and the wrong third is reported as such.**
§5.1 (126 is size) confirmed. §5.2 (570's percentile falls, a reversal is live) confirmed —
65.62 → 0.45. **§5.3 was wrong**: it predicted the genre arm would reproduce whatever survives.
It reproduced H-NEW-126's effect in full and **failed to reproduce H-NEW-570's reversal**, which
is why that reversal stands.

---

## 7. What this means for the two claims

### 7.1 H-NEW-126 — the isolate core is a size class

The five surahs {Q 16, 21, 22, 23, 25} do share more root vocabulary than five surahs drawn at
random. They share almost exactly as much as five surahs of the **same root-set size** drawn at
random — ratio 1.002. The finding's own honest caveat named this and queued the test; the test
returns the caveat's worst case.

What survives is descriptive and was never inferential: the five are concept-or-object-named
(Cell B), and each sits at a high percentile on some axis (Cell D). **Cell D is now the more
interesting cell**, because it says the same thing the null does — three of the five top axes
are `unique_root_count` or `surah_length`. The core was characterised as "maximalist on some
axis"; that is the finding, and Cell A was measuring it a second time.

**Cell C was already `NULL-BROKEN` and Cell A's own positive control is confounded too** — the
ḥawāmīm are long surahs, and the published MW-5 fired at 2.360× where matching leaves 1.18×.
The "VALID DETECTOR" certification in the finding's §"Cell A" is therefore overstated as
written, though §5b shows the detector is not worthless.

### 7.2 H-NEW-570 — the null was an artefact and three classical readings rest on it

This is the consequential half. The published finding uses its null to assert:

> *"Muqaṭṭaʿāt-axis is orthogonal to content-axis"* · *"al-Suyūṭī/al-Rāzī epistemic-humility
> EMPIRICALLY VINDICATED"* · *"al-Biqāʿī's content-munāsaba claim empirically UNSUPPORTED"* ·
> ḥawāmīm *"moderate-cohesive only, not corpus-extreme"*

**All four rest on a percentile computed against a null that never once produced a set of
comparable size.** Matched, the muqaṭṭaʿāt-29 sit at the 0.45th percentile and the ḥawāmīm-7 at
the 0.05th. **Every one of the four is withdrawn as an empirical result.**

Three things must be said precisely, because an over-retraction is as dishonest as the original
overclaim:

1. **This does not vindicate al-Biqāʿī.** It removes an empirical falsification. A 3.6 %
   content-tightening relative to size-matched peers is not *munāsaba* between a letter-opening
   and a surah's themes; it is a small measured cohesion, and it is what the data support.
2. **It does not refute al-Suyūṭī either.** *Allāh aʿlam bi-murādihi* is a claim about the
   *meaning* of the letters. Nothing here decodes anything. What is withdrawn is the assertion
   that this statistic *empirically vindicated* that stance — the statistic was measuring the
   size of the surahs.
3. **Conditioning on size may remove mechanism, not only confound.** `h-new-46` is a STRONG-PASS
   that muqaṭṭaʿāt concentrate in long surahs. Holding length fixed removes part of what the
   muqaṭṭaʿāt *are*, and §2.2b shows the conditioning is severe enough that the natural
   comparison group does not exist. **The correct reading is narrow: given surah sets of the
   same size profile, the muqaṭṭaʿāt set is measurably tighter in root content — 3.6 % for the
   29, 10.7 % for the ḥawāmīm.**

**The ḥawāmīm result is the cleanest thing in this finding.** Its A1 arm is powered (n = 442),
parameter-free, and returns the 0.00th percentile; every arm agrees; the classical
themed-block reading of Q 40–46 is supported at a strength the published 20.90 %ile denied it.

---

## 8. Honest limits

1. **The genre arm cannot use roots.** No morphological analyser exists for the baselines, so
   the cross-corpus comparison is surface-word-type only. The Qurʾān's surface values are
   reported for like-for-like comparison and the two instruments agree on H-NEW-570, but a
   surface result does not automatically transfer to the root layer.
2. **One arbitrary baseline partition in six clears H-NEW-570's own bar under matching** (§4.2).
   The bar is loose; the margin is what carries the verdict, and it is stated as such.
3. **A partition is not a composed book.** Both statistics here are contiguity-insensitive at
   surah scale, which is an argument that the control is fair, not a proof.
4. **H-NEW-126's target is post-hoc**, selected by cross-finding-010 on data including the axis
   tested. No null repairs that; only the size confound was tested.
5. **`d̄` on Dirichlet-smoothed vectors is size-dependent by construction** (ρ = +0.90 measured
   here). That is the mechanism under test and the reason a matched result for H-NEW-570 is a
   size-conditional statement.
6. **A third of H-NEW-570's matched effect is Meccan/Medinan composition** (§3.2), and the
   period-matched arm is the number to quote when only one can be.
7. **Monte-Carlo resolution.** Baseline offsets carry 2,000 draws (≈ 1.1 pp); no verdict here
   sits within 1 SE of its threshold.
8. **The first run of this harness had a defective Qurʾān-surface arm** and is retained, never
   deleted, at `runs/h-new-2820/20260807T085630Z/` — its `quran_surface` entry records
   `insufficient words: have 77797 need 82375`, because the Qurʾān's diacritic-stripped stream
   is shorter than its own whitespace verse-length profile. The Qurʾān is not re-partitioned in
   the corrected run; its real verses are the units, as H-NEW-2720 does. **Every claim-side
   number is identical between the two runs**; only the genre reference changed.

---

## 9. Garden of forking paths

- **Everything in §§2–7 was computed after the lock at SHA `45abd950…64b5f1`.** Recorded in
  pre-reg §9 before the run: both headline numbers, both scripts read in full, H-NEW-570's donor
  pool being all 114, H-NEW-126's unrun 126.1, the muqaṭṭaʿāt size ratios from H-NEW-2790 §12,
  H-NEW-2720's `r = +0.956`, and the §2.2 correction to H-NEW-2790's description of the
  H-NEW-570 statistic — **which was found while reading the script and corrected before any test
  was designed against it.**
- **The dominant channel was ranked on the data by a rule fixed before the correlations
  existed**, and it came out different for the two claims.
- **Both bin widths were pre-registered**, k = 5 primary. They agree on both verdicts.
- **The directional predictions were registered** and one of three was wrong (§6.1).
- **The runner writes `results.json` exactly once, mode `'x'`, into a directory created with
  `exist_ok=False`.** Progress snapshots go to `runs/h-new-2820-progress/`, outside the run
  directory, in files that are never rewritten.
- **No run directory was deleted.** Two primary runs and one post-hoc run are retained.
- **Post-hoc material is confined to §5** and carries no verdict.
- **No commit was made by this lane.**

---

## 10. What should change in the project record

Flagged, not applied — a correction to another finding's file is not mine to make.

- **`h-new-570-muqattaat-content-cluster.md`** needs a correction notice on its headline, its
  §2, §3, §4 and §11. Its verdict line — *"muqaṭṭaʿāt-axis is ORTHOGONAL to content-axis;
  classical al-Suyūṭī/al-Rāzī epistemic-humility vindicated; al-Biqāʿī content-munāsaba
  unsupported"* — should not stand. **Thirty external files inherit it.**
- **`h-new-126-isolate-core.md`**: Cell A's `PASS-DIRECTED` should carry the matched result
  (1.002×, p = 0.459), the genre arm (baselines at z = +3.19/+3.55 and more extreme after
  matching), and the ceiling decomposition (79 %). Its "VALID DETECTOR" sentence needs the
  MW-5 matched numbers beside it. **Thirty-two external files inherit it.**
- **`findings/UNIT-DRIFT-DEFECT.md` §3** — the grouping-channel table should gain two rows:
  *core-5 vs the rest*, dominant channel **log root-set size**, ratio of medians 2.54×; and the
  note that for the muqaṭṭaʿāt split a size-matched comparison group **cannot be built from the
  non-muqaṭṭaʿāt at all** (§2.2b). It should also record that **a size-blind null can be
  disjoint from the observed group on the nuisance channel** — 0 of 10,000 draws — which is a
  cheaper and more decisive diagnostic than any p-value and belongs beside the §6 list.
- **`findings/UNIT-DRIFT-DEFECT.md` §4** — "flagging is not retiring" now has its sharpest case:
  **a flagged NULL can reverse into a positive result.** The screens were built to catch
  overclaims; H-NEW-570 is an *under*claim produced by the same defect.
- **`STATE-OF-THE-PROJECT-2026-08-07.md`** — a §2 row for H-NEW-126, and a §1 entry for the
  size-matched muqaṭṭaʿāt content cohesion at its measured strength (3.6 % for the 29, 10.7 %
  for the ḥawāmīm) and not above it.
- **H-NEW-2790 §12's table** should carry the corrected description of H-NEW-570's statistic.

---

## 11. Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2820-group-claims.md`
  (SHA-256 `45abd95012bbf520070685646af909428a183781d94c58c4638353281764b5f1`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2820.py` — pre-reg SHA-gated; lifts the
  H-NEW-2680 partition code verbatim with three fragment SHA checks; asserts both matrix paths
  bit-identical to the published routines
- Post-hoc script: `findings/phase-b-hypotheses/scripts/h-new-2820-posthoc.py`
- Runs (immutable, never deleted), each with a `manifest.json` recording every frozen input SHA
  in repository-relative form:
  - `findings/phase-b-hypotheses/runs/h-new-2820/20260807T085952Z/` — **primary**
  - `findings/phase-b-hypotheses/runs/h-new-2820/20260807T085630Z/` — first run, defective
    genre reference arm (§8.8), retained
  - `findings/phase-b-hypotheses/runs/h-new-2820-posthoc/20260807T090239Z/`
  - `findings/phase-b-hypotheses/runs/h-new-2820/20260807T085612Z-SMOKE/`

---

*Run 2026-08-07 by Waiel Al-Shujaa. A group comparison has a denominator too, and it is the
composition of the groups. One claim was its denominator; the other was hidden by it.
Bismillāhi al-Raḥmāni al-Raḥīm.*
