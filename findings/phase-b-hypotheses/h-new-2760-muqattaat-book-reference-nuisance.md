---
finding_id: H-NEW-2760
title: The muqaṭṭaʿāt book-reference law survives its nuisance parameter — the first standing claim in this project to do so — at a rate ratio between 1.27 and 2.58, not the published 3.17 × 10⁻¹²
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
prereg: findings/phase-b-hypotheses/prereg-h-new-2760-muqattaat-book-reference-nuisance.md
prereg_sha256: a1e4419a674d254d3bf5f243d2891bafcd17986611eff94b31f6e35b8e5b9b3a
run: findings/phase-b-hypotheses/runs/h-new-2760/20260807T040526Z/
posthoc_run: findings/phase-b-hypotheses/runs/h-new-2760/20260807T040825Z-posthoc/
seed: 20260509
seed_replication: 20260519
n_perm: 10000
tests_in_family: 6
alpha_bonferroni: 0.00833333
raw_p_gate: 0.00083333
target_claim: H-NEW-53 / cross-finding-008 / Pillar 1 (H-NEW-2680 L1)
defect_diagnosed: "null does not match the nuisance parameter — the H-NEW-740 shape"
status: >-
  DISCRIMINATES under the locked decision rule — H1 exact, H3 (primary) passes at
  rate ratio 2.580, H5 passes, observation outside the Null B 95 % band. Carried with
  three qualifications published at equal prominence: H2 FAILED its gate, so the
  nuisance channel named primary was the weaker of the two available; against the
  stronger channel the rate ratio is 1.694; and the G1 poetry arm is a PRE-COMMIT
  VIOLATION.
verdict: >-
  The law survives. The published p = 3.17 × 10⁻¹² does not — it is an artefact of a
  null that treats 114 surahs as exchangeable. Every matched null still places the
  observation outside its 95 % band, but the honest effect size is a rate ratio
  between 1.27 and 2.58 rather than a 12-order-of-magnitude tail. The sharpest arm is
  positional and length-free: all 29 muqaṭṭaʿāt surahs mention the Book, and they
  place the first mention at 0.0996 of the surah against 0.3403 for the other 40
  Book-mentioning surahs.
---

# H-NEW-2760 — Pillar 1, against a null that matches its nuisance parameter

**Pre-reg SHA-256 `a1e4419a…9b3a`, runtime-verified with `SystemExit` on mismatch.
Seed 20260509, replication 20260519, 10,000 permutations per null. Family of 6
registered inferences; Bonferroni α = 0.00833333, project novelty rule stricter, so the
raw decision gate is p < 0.00083333. Eighteen frozen inputs SHA-256-recorded. Both run
directories retained; manifest paths are repository-relative.**

---

## 0. Why this claim, and not one of the three more-cited ones

Stated first because the next audit takes the second item and the reasoning is the
deliverable.

Three claims carry more raw citations than this one — H-NEW-720 at 314, H-NEW-750 at 271,
H-NEW-590 at 264, against H-NEW-53's 48 and cross-finding-008's 192. **All three feed
structures that were corrected earlier on 2026-08-07 and no longer carry an inference.**
H-NEW-720 decomposes the residual of the Fisher-Rao geodesic, whose optimality reading was
withdrawn. H-NEW-750 and H-NEW-590 are two of the three inputs to UAS, which H-NEW-2720 G8
ruled `NOT-A-DISCRIMINATION-CLAIM`. Supplying a null for a statistic whose parent inference
is already retracted buys very little.

**The muqaṭṭaʿāt book-reference law is the only standing claim that neither baseline
satisfies** — H-NEW-2680 §7 has al-Bukhārī at 2/4 and pre-Islamic poetry at 3/4, with L1
the sole law failing for both. `STATE-OF-THE-PROJECT-2026-08-07.md` §1.1 lists it first
among four survivors. If it fell, the project would have no discriminating law left; if it
held under a properly matched null, it would be the first claim here to have done so.
Both outcomes were worth more than the alternatives.

## 1. The claim, and the defect

> **24 of 29 muqaṭṭaʿāt-opened surahs (82.8 %) reference *kitāb* or *qurʾān* within their
> first 3 verses. Only 10 of 85 non-muqaṭṭaʿāt-opened surahs (11.8 %) do. Hypergeometric
> P(X ≥ 24 | n = 29, K = 34, N = 114) = 3.17 × 10⁻¹².**
> — `h-new-53-muqattaat-book-reference.md:17,19,110`

**Defect (b), the H-NEW-740 shape: the claim has a null and the null is wrong.** The
hypergeometric draws 29 surahs **uniformly from 114**, which is correct only if the 29 are
exchangeable with the other 85 on everything that affects the outcome. **They are not, and
this project established that itself:** `h-new-46-muqattaat-vs-surah-length.md:3` is a
STRONG-PASS on all four length axes — muqaṭṭaʿāt surahs concentrate in **long** surahs — and
`h-new-46-1-chronology-disentangle.md` separates that from chronology at 6/7.
`cross-finding-012` makes scripture-announcement a Late-Meccan register. H-NEW-53 has **no
honest-limits section at all**, is self-declared post-hoc-noticed (`:22-37`), and nowhere
mentions surah length.

**Nuisance parameters, named in pre-reg §4 before any null was built:** N1 opening-window
token budget (words in verses 1–3 — the literal denominator of the substring search);
N2 revelation phase; N3 the surah's own target-token base rate; N4 whole-surah length.
**N1 was locked as primary. That was the wrong call, and §3 reports it.**

## 2. The registered result

Instrument taken **verbatim** from `scripts/h-new-2680b.py` — the same `AR_DIAC`, `NON_AR`,
`NARROW`, `normalise_words` and `cut_to_profile` the pillar-conjunction control ran.
Nothing was re-designed.

| # | inference | locked direction | observed | p | gate | verdict |
|---|---|:-:|--:|--:|:-:|:--|
| **H1** | reproduction | exactly 24/29 | **24/29** | — | exact | **EXACT** |
| **H2** | the nuisance is real | ρ > 0 | ρ = **+0.1678** | 0.0381 | ✗ | **FAILS gate** (direction held) |
| **H3** | **primary** — survives N1 | obs > null mean | **24 vs 9.304** | **1.0×10⁻⁴** | ✓ | **PASS** |
| **H4** | survives N1 × N2 | obs > null mean | **24 vs 18.972** | **1.0×10⁻⁴** | ✓ | **PASS** |
| **H5** | front-loading, length-free | muqaṭṭaʿāt earlier | **Δ = −0.2407** | **5.0×10⁻⁴** | ✓ | **PASS** |
| **G1** | genre control | ρ > 0 in baselines | 2 of 3 positive | — | ✗ | **0/3 pass; poetry REVERSED** |

**H1 reproduces the muqaṭṭaʿāt count exactly at 24 of 29.** The non-muqaṭṭaʿāt count is
**11 of 85, not 10**, so K = 35 rather than 34 — an instrument divergence between H-NEW-53's
unstated pattern list and 2680b's `NARROW`, **disclosed in pre-reg §5 before locking**. The
published hypergeometric reproduces to the digit under its own K: `p_published_K34 =
3.1697 × 10⁻¹²`. Under the 2680b instrument it is 9.484 × 10⁻¹².

### 2.1 H3, the primary — the law survives its named nuisance

Null B permutes the muqaṭṭaʿāt label **within** opening-window-size quintiles, so every
draw takes exactly as many surahs from each size stratum as the real set does. The
opening-window profile is **identical by construction** — the thing H-NEW-740 failed to do.
No stratum is degenerate (muqaṭṭaʿāt per quintile: 3, 7, 7, 8, 4).

**Observed 24 against a null mean of 9.304 (sd 2.096): rate ratio 2.580, z = +7.01,
p = 1.0 × 10⁻⁴, 95 % band [5, 13].** Replication at seed 20260519 gives null mean 9.355,
p = 1.0 × 10⁻⁴. The observation is eleven above the band top.

**Matching on N1 moved the expected count only from 8.90 to 9.30.** The opening-window
budget is a real nuisance and a nearly irrelevant one.

### 2.2 H5, the sharpest arm — and the one no length channel can produce

H5 conditions on **each surah's own verse count and its own number of Book-bearing
verses**, then asks where the first one falls. Length, opening-window budget and vocabulary
volume are all held fixed by construction.

**All 29 muqaṭṭaʿāt surahs contain target vocabulary somewhere** — against 40 of the other
85. Among the 69 surahs that have any:

| | n | mean normalised position of the FIRST Book-mention |
|:--|--:|--:|
| **muqaṭṭaʿāt** | 29 | **0.0996** |
| non-muqaṭṭaʿāt | 40 | **0.3403** |

**Δ = −0.2407** against a within-surah null mean of −0.0783 and a 95 % band of
[−0.1715, +0.0149]; **p = 5.0 × 10⁻⁴**, replication 3.0 × 10⁻⁴. Both clear the
0.00083333 gate.

This is a better statement of the law than the original. Not *"muqaṭṭaʿāt surahs mention
the Book"* — every one of them does, and so do 40 others — but ***"muqaṭṭaʿāt surahs
announce it at the top."***

### 2.3 H2 failed, and it means I ranked the nuisance channels wrong

**Published at equal prominence because it is a defect in my own design, not in the claim.**

ρ(opening-window words, opening hit) = **+0.1678, p = 0.0381** — direction held, gate
missed by a factor of 46. Meanwhile **ρ(whole-surah length, opening hit) = +0.4583**.
**N4 is the stronger channel and I made N1 primary.** The pre-registration listed N4 and
explicitly deferred it ("correlated with N1 but not identical… N1 is the sharper control
and is the one locked"). That judgement was wrong on the data.

Null B therefore holds fixed a weaker nuisance than the strongest one available, and
H3's rate ratio of 2.580 must be read with that on its face. §3 bounds it.

### 2.4 G1 — the genre control, and its pre-committed limit

Matched partitions built with `cut_to_profile`: each baseline word stream cut into 6,236
units on this corpus's verse word-length profile, grouped into 114 pseudo-surahs on the
canonical verse-count profile.

| corpus | pseudo-surahs with an opening Book-reference | ρ(opening-window words, hit) | p |
|:--|--:|--:|--:|
| **this corpus** | **35** | +0.1678 | 0.0381 |
| al-Bukhārī | **5** | +0.1283 | 0.0871 |
| al-Jāḥiẓ *Kitāb al-Ḥayawān* | **7** | +0.1784 | 0.0282 |
| pre-Islamic poetry | **1** | **−0.0343** | 0.6415 |

**The poetry arm is a PRE-COMMIT VIOLATION** — locked positive, observed −0.0343. Published
as such, not rescued. **0 of 3 baselines clear the gate; 2 of 3 hold the direction.**

The counts reproduce H-NEW-2680 §7 (6 Bukhārī, 1 poetry) to within the instrument
difference. **Per pre-reg §7.2 this is NOT counted as evidence for the law.** A floor of
1–7 makes the baseline uninformative about marker engineering — there is nothing there to
mark. What G1 does establish is narrower and useful: **the opening-window-size nuisance is
weak in every corpus tested, including this one**, which is why H3's ratio is large.

## 3. What the effect size actually is — the ladder

Every row places the observation outside its own 95 % band. **The effect never vanishes.**
What changes by a factor of two is how big it is. Rows marked *post-hoc* are MW-7 capped
and are **not** confirmatory; they bound the registered result, they do not extend it.

| null | expected hits | **rate ratio** | z | p |
|:--|--:|--:|--:|--:|
| exchangeable — **the published null** | 8.90 | **2.70** | — | 9.5 × 10⁻¹² |
| opening-window quintiles — **H3, registered primary** | 9.30 | **2.580** | +7.01 | 1.0 × 10⁻⁴ |
| whole-surah length quintiles — *post-hoc, the stronger channel* | 14.16 | **1.694** | +5.10 | 1.0 × 10⁻⁴ |
| both length channels — *post-hoc* | 15.01 | **1.599** | +5.18 | 1.0 × 10⁻⁴ |
| surah-length × phase — *post-hoc* | 18.07 | **1.328** | +3.64 | 4.0 × 10⁻⁴ |
| opening-window × phase — **H4, registered** | 18.97 | **1.265** | +3.82 | 1.0 × 10⁻⁴ |

The whole-surah-length row replicates at seed 20260519 (null 14.205, RR 1.690).

**Read the bottom rows with care, because phase is not a clean confounder.** Post-hoc
diagnostic D1: **Late Meccan is 16 of 21 surahs muqaṭṭaʿāt — 76.2 %.** Two of Null C's ten
strata are **100 % muqaṭṭaʿāt** (`ow-tertile-1 × Late Meccan`, n = 8; `ow-tertile-0 ×
Late Meccan`, n = 1) and a third is 83 % (5 of 6). A stratum that is entirely muqaṭṭaʿāt
contributes the same value to the observed count and to every permutation **by
construction**, which drags the null mean toward the observation. **Phase-matched rate
ratios are over-adjusted floors, not effect-size estimates.**

There is a substantive point underneath the arithmetic. If the muqaṭṭaʿāt *are* the marker
system of the Late-Meccan scripture-announcement apparatus (`cross-finding-012`), then
revelation phase is a **mediator**, not a confounder, and conditioning on it removes part of
the mechanism under test. **"Among Late-Meccan surahs, do the muqaṭṭaʿāt ones announce the
Book more?" is a different and harder question than the one H-NEW-53 asked.** It is worth
asking; it is not the audit that was commissioned.

## 4. Verdict

**Locked rule, pre-reg §8, diffed line-by-line against the runner's verdict block before
execution:**

```
DISCRIMINATES              H1 exact AND H3 passes AND H5 passes
                           AND observed outside the Null B 95% band
GENRE-SHARED-BUT-LARGER    H3 passes but Null B rate ratio < 2.0, OR H3 passes while H5 fails
DOES-NOT-DISCRIMINATE      H3 fails its gate
```

H1 exact ✓ · H3 passes at RR 2.580 ✓ · H5 passes ✓ · 24 outside [5, 13] ✓ →
### **DISCRIMINATES**

**One implementation note, recorded because the H-NEW-2600 lesson is about exactly this.**
The locked rule does not name the case "H3 passes, RR ≥ 2.0, H5 passes, but observed inside
the band." The runner's `else` branch routes that case to `GENRE-SHARED-BUT-LARGER` — the
**more conservative** of the two. That is a tightening relative to an unspecified case, not
a loosening, and it did not fire.

**Three qualifications travel with the verdict and are not separable from it:**

1. **H2 failed its gate.** The nuisance channel I made primary is the weaker one. Against
   the stronger channel the rate ratio is **1.694**, and **under the locked rule's own
   RR < 2.0 clause applied to that stratification the verdict would read
   GENRE-SHARED-BUT-LARGER.** I am not substituting a post-hoc statistic for the registered
   primary — that would be the H-NEW-2600 error with the sign flipped — but the reader is
   entitled to both numbers and this is where they are.
2. **DISCRIMINATES is earned on the within-corpus nulls (H3, H5), not on the genre arm.**
   G1 passes nothing and was pre-committed not to count as evidence for the law.
3. **The published p = 3.17 × 10⁻¹² is withdrawn as a description of the law's strength.**
   It is arithmetically correct and inferentially void: it prices an exchangeable null that
   the corpus does not satisfy.

**Honest one-line summary. The law is real, it survives every null that matches its
nuisance parameters, and it is two to four times smaller than it was published as.**

## 5. Honest limits, for this claim specifically

1. **The front-loading arm is not shown to be phase-independent, and that is the largest
   open threat to the headline.** Post-hoc D2 (MW-7 capped, not confirmatory): within
   Middle Meccan the front-loading holds at Δ = −0.2664, p = 0.0054 (n = 10 vs 9); pooled
   over Late + Middle Meccan, Δ = −0.1676, p = 0.0063, replication 0.0051. **Neither clears
   the registered gate of 0.00083333.** Within Late Meccan alone it is p = 0.0797 on
   n_non = 5. So H5 is **consistent with** but **not established as** phase-independent.
   The required next test is a phase-matched H5 with a fresh pre-registration; nothing here
   licenses the claim in advance.
2. **A partition is not a composed book.** This statistic is **boundary-sensitive** — it
   depends on where unit 1 begins — and per `STATE-OF-THE-PROJECT-2026-08-07.md` §4.7
   arbitrary cuts *destroy* real boundaries, so a baseline **pass** would be strong evidence
   against the law while a baseline **failure** is weak evidence for it. The baselines
   failed. **That asymmetry is why the weight of this finding sits on H3 and H5, which use
   no baseline at all.** This is stated as a bound on what G1 proves, not as an excuse.
3. **The §1.1 caveat is untouched.** "Only scripture talks about itself as a book" is still
   not separated from "only this corpus has an engineered marker system." Nothing here
   addresses that, and H5 sharpens rather than resolves it: front-loading is what a marker
   system *and* a self-referential genre would both produce.
4. **K = 35 not 34.** The 2680b instrument finds one more non-muqaṭṭaʿāt hit than H-NEW-53
   reported. H-NEW-53 does not publish its pattern list, so the divergence cannot be
   resolved from disk. Both K values are carried through.
5. **Four Nöldeke phases over 114 surahs.** Null C's strata are thin and five of ten are
   degenerate; the chronology itself is a scholarly reconstruction, not a datum.
6. **Three matched genres.** The reference class is small, as it is for every percentile in
   H-NEW-2720.

## 6. What this means for the findings that cite it

- **`h-new-53-muqattaat-book-reference.md`** — the finding stands; **its p-value does not.**
  Needs a correction notice: the hypergeometric is an exchangeable null, the matched rate
  ratio is 1.27–2.58, and the file has no honest-limits section.
- **`findings/cross-finding/muqattaat-book-introduction-marker-synthesis.md`
  (cross-finding-008, 192 citations)** — the synthesis's central empirical claim survives.
  Its strength statement should be restated as a rate ratio, not as p ≈ 10⁻¹².
- **`h-new-2680-pillar-conjunction.md` L1 / Pillar 1** — **survives, and is now the only
  claim in this project shown to survive a null matched to its nuisance parameter.** The
  §7 caveat about baseline base rates is unchanged and still governs.
- **`STATE-OF-THE-PROJECT-2026-08-07.md` §1.1** — the "stands, and is partly definitional"
  reading is confirmed and can be sharpened: the marker relation is *positional*, and the
  positional form is the part that no length channel explains.
- **The four p-values that "multiply to ~10⁻¹²"** — already ruled non-commensurable by
  H-NEW-2680 §1. This finding removes the L1 factor's magnitude as well: the one licensed
  multiplication, p(L1 ∧ L2), rested on L1 = 3.17 × 10⁻¹².

## 7. Reproduction

`scripts/h-new-2760.py` (registered) and `scripts/h-new-2760-posthoc.py` (MW-7 capped).
Runs `runs/h-new-2760/20260807T040526Z/` and `runs/h-new-2760/20260807T040825Z-posthoc/`,
both retained, manifests repository-relative, 18 frozen inputs SHA-256-recorded.
Pre-registration `prereg-h-new-2760-muqattaat-book-reference-nuisance.md`, SHA
`a1e4419a…9b3a`, verified at runtime. Machine output `csv/h-new-2760.json`.

*A law that has never met a control is a description. This one met a control and is still a
law — smaller than it was, and for the first time today, measured.
Bismillāhi al-Raḥmāni al-Raḥīm.*
