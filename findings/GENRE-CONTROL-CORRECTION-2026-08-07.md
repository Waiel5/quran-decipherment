---
title: Genre-control correction notice — which of the remaining standing laws survived a matched Arabic control, which did not, and where every affected file is
author: Waiel Al-Shujaa
date: 2026-08-07
status: CANONICAL CORRECTION NOTICE — additive; no prior claim has been deleted anywhere
source: findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md
companion: findings/PILLAR-LAW-CORRECTION-2026-08-07.md (the four pillar laws, same day)
---

# Genre-control correction notice

On 2026-08-07, H-NEW-2680 put the four "pillar laws" through this project's first genre
control and three of them did not survive. The obvious inference was that **every other
standing law was suspect for the same reason**, because almost none had ever met a matched
Arabic control. **H-NEW-2720 ran nine more of them.**

Three corpora were cut into 114 pseudo-surahs matching this corpus's verse-count and
verse-word-length profile exactly, using **the partition code from H-NEW-2680, lifted
verbatim and SHA-checked at runtime** so it cannot drift: pre-Islamic poetry (1 partition —
the corpus has only 145 words of slack), **al-Bukhārī** (200 seeded offset partitions), and
**al-Jāḥiẓ's *Kitāb al-Ḥayawān*** — a third genre, 3rd/9th-century adab prose, that 2680 did
not use. Every law ran on surface word-types for all four corpora, and this corpus was
compared to the baselines only through that identical instrument, never against a
QAC-root headline.

**Not one of the nine discriminates.** This notice is the single authoritative statement of
what changed. It is linked from every corrected file. **Nothing was deleted:** the original
claims remain in place with a notice beside them, because the record of what was believed
and when is itself data.

Full evidence, all run artefacts, and every honest limit:
**`findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`**
Pre-registration SHA-256 `24a5bc8dd2352151f6557a0415cb177f69e60f8fca5f1ccf39ff3c57b2e0040d`,
seeds 20260509 / 20260519, runs under `findings/phase-b-hypotheses/runs/h-new-2720/`.

---

## The one-paragraph version

**The iʿjāz anti-twin is REVERSED** — this corpus sits at the 3rd percentile of adab prose
on the very statistic al-Bāqillānī's *iʿjāz al-fawāṣil* was said to be vindicated by, and
**H-NEW-740's cross-corpus control was not a control**, because it did not match the
nuisance parameter. **The compression-tail family is GENRE-SHARED and 91.5 % explained by
unit size.** The rhyme tail sits at the 51st percentile of ḥadīth. The verse-length tail is
below the baseline mean. Anti-chiasmus is a property of Arabic prose, more so than of this
corpus. **One axis survives**: the post-kink content-compression *slope*, steeper than
200/200 ḥadīth and 198/200 adab partitions — genre-shared-but-larger, a difference of
degree, not a discrimination.

---

## The result table

| law | this corpus | poetry | al-Bukhārī (200 cuts) | al-Jāḥiẓ (200 cuts) | verdict |
|:--|--:|--:|--:|--:|:--|
| **G1** content compression-tail R² (H-NEW-660) | 0.9887 | 0.8633 | mean 0.9577, **99.5 pctile** | mean 0.9686, **99.0 pctile** | **GENRE-SHARED** |
| **G1b** its post-kink slope β | **−0.01343** | −0.0133 | steeper than **200/200** | steeper than **198/200** | **GENRE-SHARED-BUT-LARGER** |
| **G2** rhyme dispersion-tail R² (H-NEW-700) | 0.7983 | 0.6842 | **51st pctile** | **50.5th pctile** | **GENRE-SHARED** |
| **G3** phoneme dispersion-tail R² (H-NEW-700) | 0.9329 | **0.9332** | 76.5th pctile | 73rd pctile | **GENRE-SHARED** |
| **G4** verse-length tail, letters (H-NEW-770) | 0.8073 | **0.8113** | **31.5th** (137/200 exceed) | **32.5th** (135/200) | **REVERSED** |
| **G4w** its words-per-verse arm | 0.8115 | 0.8105 | 0.8105 ×200 | 0.8105 ×200 | **DEGENERATE-BY-CONSTRUCTION** |
| **G5** iʿjāz anti-twin r (H-NEW-730/740) | **−0.8700** | **−0.8718** | mean **−0.9107**, **14th pctile** | mean **−0.9311**, **3rd pctile** | **REVERSED** |
| **G6** anti-chiasmus mean ring-z (cf-026) | −0.1363 | −0.1200 | −0.1458 | **−0.2095** | **REVERSED** |
| **G7** register separability lift (cf-028) | 1.658 | **1.842** | 1.289 | 1.421 | **REVERSED** (capped) |
| **G8** UAS (H-NEW-840) | 1.166 | **1.267** | 1.076 | 1.118 | **NOT-A-DISCRIMINATION-CLAIM** |
| **G9** pericope-flip (cf-025) | 5/5, max z +24.7 | 5/5, max z **+22.4** | 4/5, +6.9 | 5/5, +12.0 | **GENRE-SHARED** |
| **G10** eponymy-independence (cf-027) | — | — | — | — | **NOT-TRANSPORTABLE** |

Every verdict reproduces at seed 20260519; percentiles move by at most 3 points.

---

## Law by law

### The iʿjāz anti-twin, r = −0.8643 (`H-NEW-730`, controlled by `H-NEW-740`) — **REVERSED**

Claimed: window-level Pearson r(content-cohesion × rhyme-dispersion) = −0.8643, "al-Bāqillānī
*iʿjāz al-fawāṣil* empirically vindicated at law-strength", with H-NEW-740 reporting
pre-Islamic poetry at r = −0.4801 and a Fisher-z gap of −6.42 at p = 1.3 × 10⁻¹⁰.

**The arithmetic reproduces** — the surface rebuild gives r = −0.8700 against the published
−0.8643. Three things did not survive.

1. **Both prose baselines are more anti-twinned than this corpus.** al-Bukhārī mean −0.9107
   (this corpus at the **14th percentile**, 172 of 200 cuts more extreme); al-Jāḥiẓ mean
   −0.9311 (**3rd percentile**, 194 of 200). Poetry under a matched partition reaches
   **−0.8718**.
2. **H-NEW-740's control did not match the nuisance parameter.** It cut poetry into **equal
   30-bayt blocks** and compared them to this corpus's **wildly unequal surahs** (10 words to
   6,140). The size profile is the driver:
   r(d̄_content, log unit size) = **+0.9564**; r(d̄_rhyme, log unit size) = **−0.8376**.
   Small units simultaneously have low content-distance (sparse vectors pulled toward the
   Dirichlet prior) and high rhyme-distance (few verses, so near-one-hot final-letter vectors
   that are almost orthogonal). **A dispersed size profile manufactures an anti-twin; equal
   blocks suppress it.**
3. **About half the correlation is unit size.** Partialling out log unit size gives
   **r = −0.4318**; re-cutting this corpus's own verses into equal-size blocks gives
   **−0.3375**. The size-controlled residual is statistically indistinguishable from what
   H-NEW-740 measured for *poetry* (−0.48) and called the genre baseline.

H-NEW-740's own honest-limits §3 identified block size as a risk and reasoned that it
*"biases AGAINST detecting strong content×rhyme structure, again favoring the iʿjāz
inference."* **That direction-of-bias reasoning was wrong**: the driver is size *dispersion*,
not size *level*, and equal-size blocks suppress the effect rather than merely attenuating
it. This is the single most valuable methodological finding of the audit — see §"Lessons".

**Honest limit, for this law specifically.** The baselines are arbitrary cuts of a continuous
stream, not composed books. For a **contiguity-sensitive** statistic like this one, arbitrary
cuts *preserve* local continuity and therefore make the law *easier* for a baseline — so the
reversal is **weaker evidence against the law than the percentile alone suggests.** The size
decomposition in (2) and (3), however, does not depend on the baselines at all and is the
stronger evidence.

**What is not claimed.** al-Bāqillānī's qualitative claim about *fawāṣil* is not refuted; it
was never a claim about window-level correlation coefficients. What is withdrawn is its
stated *empirical vindication*.

### The compression-tail family (`H-NEW-660`, `H-NEW-700`, `H-NEW-770`) — **GENRE-SHARED**, and largely a unit-SIZE effect

Claimed: d̄_content(s) ≈ 0.9603 − 0.01237·max(0, s−50) at **R² = 0.9860**; a rhyme
dispersion-tail at R² = 0.789; a phoneme dispersion-tail at R² = 0.946; a verse-length tail
at R² ≈ 0.81. Cited throughout as "4 architectural laws" and as 98.6 % of mushaf
cohesion-variance reduced to one parameter.

**The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860 and β = −0.01237.
Three independent lines undo the interpretation.

1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
   average R² = 0.9686 and reach 0.9913; al-Bukhārī's average 0.9577 and reach 0.9903. This
   corpus's 0.9887 sits at the **99.5th / 99.0th percentile** — genuinely high, and still
   inside the band, with 1 and 2 of 200 arbitrary cuts exceeding it (1 and 5 on replication).
2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
   **log(window mean word-count) and nothing else** — no position information whatever —
   gives **R² = 0.9147**, with r = +0.9564. Adding size to the published kink model raises it
   only from 0.9887 to 0.9918. The two predictors are largely redundant.
3. **Equalise the sizes and the law nearly vanishes.** Re-cutting **this corpus's own verse
   stream** into 114 equal-verse blocks, order preserved, drops R² from **0.9887 to 0.3388**
   and flattens the slope **nine-fold** (−0.01343 → −0.00151). The mechanism is elementary:
   the surahs shorten toward the end (Spearman(position, verse count) = −0.846); short units
   have sparse word-type vectors; Dirichlet smoothing pulls them toward the prior; Fisher-Rao
   distances shrink. **d̄ falls at the end of the mushaf because the surahs are short.**

**The rhyme tail (H-NEW-700) is the cleanest non-result in the sweep**: R² = 0.7983 at the
**51st percentile** of ḥadīth and the **50.5th** of adab prose — the middle of the
distribution, not a near miss. The **phoneme tail** is at the 76.5th / 73rd percentile and is
edged by poetry (0.9332 vs 0.9329). The **verse-length tail (H-NEW-770)** is **REVERSED** —
at the 31.5th / 32.5th percentile, with 137 and 135 of 200 baseline cuts more extreme — and
its **words-per-verse arm is degenerate by construction**, since the partition copies this
corpus's verse word-length profile verse by verse, so all 200 draws of both prose baselines
return exactly 0.8105. That degeneracy was declared in the pre-registration before the run.

**What survives, at its true strength.** Holding the size profile *identical* by construction,
this corpus's post-kink content-compression **slope** β = −0.01343 is steeper than **all 200**
ḥadīth partitions and **198 of 200** adab-prose partitions (196/200 on replication). Its
content-distance falls about a third faster than al-Bukhārī's under the same size profile.
That is a **real residual content effect and the only axis in the entire sweep where this
corpus leads** — but it is **genre-shared-but-larger**: a difference of degree on one axis of
one law, not the R² = 0.986 headline the law is cited for, and not a discrimination.

**Honest limit, for this law specifically.** As with the anti-twin, arbitrary cuts of a
continuous stream preserve local continuity and make a contiguity-sensitive gradient *easier*
for a baseline, so the baseline reproduction is the weaker of the three arguments. The size
regression (2) and the equal-cut collapse (3) involve no baseline at all.

### Within-pericope anti-chiasmus (`cross-finding-026-formal`, `H-NEW-2220`) — **REVERSED**

Claimed: the corpus is anti-chiastic in aggregate (mean permutation-z = −0.15; only 33 % of
windows positive; 0 of 6,541 windows survive Bonferroni). **This reproduces** — an
independently written ring statistic returns mean z = −0.136.

It is simply not a property of *this* corpus. All four are anti-chiastic: poetry −0.120,
this corpus −0.136, al-Bukhārī −0.146, **al-Jāḥiẓ −0.209**. Adab prose is more anti-chiastic
than the Qurʾān. Roughly a third of windows are positive in every corpus (0.339–0.370).
cf-026's cohesion arm already carried a correction notice from H-NEW-2680; **its chiasmus arm
now needs one too.**

**Honest limit, for this law specifically — and it runs the other way.** This statistic is
**boundary-sensitive**: arbitrary cuts *destroy* real unit boundaries and should make ring
structure *harder* to find for a baseline. A baseline exceeding this corpus under that
handicap is therefore **strong** evidence, not weak. This reversal is the most robust in the
sweep.

### Register-coded discourse grammar (`cross-finding-028-formal`) — **REVERSED, verdict capped**

cf-028's own numbers are **not challenged**. What was transported is the *shape* of its
claim: the leave-one-out nearest-centroid lift of a 6-feature thin-grammar vector over a
3-way partition, computed identically for all four corpora using contiguous thirds. This
corpus 1.658; **poetry 1.842**; al-Bukhārī 1.289; al-Jāḥiẓ 1.421.

**Two cautions, both pre-registered.** The baselines' 3-way labels are **surrogates**
(contiguous thirds), not registers; and this corpus's 1.658 is its own contiguous-thirds
lift, **not** cf-028's 1.75, which used real register labels. What this shows is only that a
~1.7× lift from thin grammar over a 3-way split of Arabic text is **reachable without
registers at all** — which is the discriminating question — not that the baselines have
registers.

### The UAS ranking (`H-NEW-840`) — **NOT A DISCRIMINATION CLAIM**

H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking index with
no null hypothesis and no test statistic, so it can neither pass nor fail a control, and **no
discrimination claim may rest on it**. Two of its three inputs are now corrected: the
Fisher-Rao geodesic (H-NEW-2680) and the iʿjāz-signature/compression family (this notice).
The one transportable diagnostic — how differentiated the 114 units are — puts this corpus at
sd = 1.166 against **poetry's 1.267**, so even descriptively it is not the most differentiated
of the matched corpora. *(A first implementation of that diagnostic was wrong —
`np.eye(114) * np.nan` is NaN everywhere, because 0 × NaN = NaN — and the bug ran in the
flattering direction, making this corpus look highest. Corrected before the run.)*

### The pericope-flip (`cross-finding-025-formal`) — **GENRE-SHARED**, now with magnitudes

Already corrected by H-NEW-2680 (poetry 5/5, al-Bukhārī 4/5). Extended here with a third
genre and with the z-magnitudes 2680 did not report:

| corpus | flips | marker classes and z |
|:--|:-:|:--|
| **this corpus** | 5/5 | وكان +9.4 · واتقوا +10.6 · قومه +10.0 · **فبأي +24.7** · مؤمنين +9.1 |
| poetry | 5/5 | عبل +22.4 · أي +16.1 · عبلة +19.4 · والجمع +11.4 · عبس +16.4 |
| al-Jāḥiẓ | 5/5 | الكتاب +9.4 · الكتب +10.3 · العلم +9.6 · النساء +8.4 · الخصي +12.0 |
| al-Bukhārī | 4/5 | الإمام +6.9 · الإيمان +4.6 · الماء +1.6 · والذي +3.3 · ماء +2.7 |

The flip tracks **genre**, not scripture: the two verse-like corpora produce large z, the two
prose corpora smaller ones. Incidentally but usefully, al-Jāḥiẓ's best marker classes include
**الكتاب** and **الكتب** — adab prose talks about "the book" constantly, which bears directly
on the H-NEW-2680 §11.5 caveat that Pillar 1's baseline failure was partly a fact about
self-referential vocabulary rather than about marker engineering.

### Eponymy-independence (`cross-finding-027-formal`) — **NOT TRANSPORTABLE**

Its title-density arm was withdrawn the same day and replaced by H-NEW-2710; its
transportable form was already run as H-NEW-2680's L4. What remains is a 5-cycle centrality
claim, and pseudo-surahs have no eponyms, so there is no baseline analogue. Declared untested
rather than given a manufactured verdict.

---

## The standing honest limit, and why it is stated per law rather than once

**A partition is not a composed book.** The pseudo-surahs are arbitrary cuts of a continuous
stream; the baseline units were never authored as units. A law failing to discriminate against
an artificial partition is therefore **weaker evidence against the law than it first appears**.

But the direction of that weakness is **not uniform**, and each verdict above states which
regime it is in:

- **Contiguity-sensitive statistics** (G1 compression-tail, G5 anti-twin): arbitrary cuts
  *preserve* local continuity, making the law **easier** for a baseline. A baseline pass is
  **weak** evidence against the law. → G1 and G5 are discounted accordingly, and their
  size-decomposition evidence, which uses no baseline at all, carries the weight instead.
- **Boundary-sensitive statistics** (G6 anti-chiasmus, G9 pericope-flip): arbitrary cuts
  *destroy* real boundaries, making the law **harder** for a baseline. A baseline pass is
  **strong** evidence. → G6's reversal is not discounted.

Two further limits apply to everything above. **Three genres are not "Arabic in general"** —
poetry, ḥadīth and adab prose are the only matched corpora on disk. And **the surface
instrument is shallower than QAC**, since no baseline has root annotation; that biases
baseline content statistics *weaker*, so a baseline matching or exceeding this corpus would do
so more strongly under better morphology. That bias runs *against* the conclusions drawn here,
which is the conservative direction.

---

## Lessons that must not be re-learned

1. **A control that does not match the nuisance parameter is not a control.** H-NEW-740 is
   the case study: a real cross-corpus control, properly pre-registered, that compared
   equal-size poetry blocks to unequal surahs and therefore measured the size profile rather
   than the genre. Its honest-limits section named the variable and got its sign backwards.
   **Direction-of-bias reasoning is not a substitute for matching.**
2. **Audit the strongest claim first, not last.** The compression-tail R² = 0.986 was the
   project's most-cited number and among its least-examined; it had stood since 2026-04-28
   without a control.
3. **Never assert a robustness property — compute it.** "MW-1 length control is working"
   (H-NEW-111) and "block size biases against us" (H-NEW-740) were both asserted, and both
   were false.
4. **Check every control for tautology before trusting it.** The words-per-verse arm of
   H-NEW-770 is identical across all four corpora by construction. That was caught in
   pre-registration; it would have looked like a striking confirmation if it had not been.

---

## Where the affected files are

The full inventory, with per-file reference counts and correction status, is at
**`findings/GENRE-CONTROL-INVENTORY-2026-08-07.md`**.

The companion notice for the four pillar laws, corrected the same day from H-NEW-2680, is at
**`findings/PILLAR-LAW-CORRECTION-2026-08-07.md`**.

The single orientation document for anyone arriving new is
**`STATE-OF-THE-PROJECT-2026-08-07.md`** at the repository root.

---

*Logged 2026-08-07 by Waiel Al-Shujaa. Nothing here says any published computation was wrong.
What was wrong was the inference from an uncontrolled number. Bismillāhi al-Raḥmāni al-Raḥīm.*
