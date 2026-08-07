---
title: H-NEW-570 reversal notice — a published NULL that was an artefact of its own null, and what it does and does not license
author: Waiel Al-Shujaa
date: 2026-08-07
status: CANONICAL CORRECTION NOTICE — additive; no prior claim has been deleted anywhere
source: findings/phase-b-hypotheses/h-new-2820-group-claims-matched.md
independence_run: findings/phase-b-hypotheses/runs/h-new-2830-independence/20260807T095124Z/
---

# H-NEW-570 reversal notice

**Every other correction on 2026-08-07 moved in one direction: a claim was weaker than
published. This one moves the other way.** H-NEW-570 was published as a NULL — the 29
muqaṭṭaʿāt surahs do *not* form a content cluster — and thirty external files inherited that
NULL as **evidence of absence**. H-NEW-2820 established that the null it was scored against
was structurally incapable of detecting the effect it tested for.

Read this whole notice before citing either the old claim or the new one. **The reversal is
narrower than it sounds, and over-retraction in the positive direction would be the same error
that produced the original overclaim.**

---

## 1. What was claimed

H-NEW-570 computed the mean pairwise Fisher–Rao distance `d̄` between the whole-surah root
distributions of the 29 muqaṭṭaʿāt surahs and scored it against 10,000 random 29-subsets drawn
uniformly from all 114 surahs.

| set | `d̄` | published %ile | published verdict |
|:--|--:|--:|:--|
| muqaṭṭaʿāt-29 | 0.9388 | **65.62** | NULL — "median-level" |
| ḥawāmīm-7 {Q 40–46} | 0.8672 | **20.90** | NULL — "moderate only, not corpus-extreme" |

From those two percentiles the finding asserted four things
(`findings/phase-b-hypotheses/h-new-570-muqattaat-content-cluster.md:16,29,37,47,59`):

> *"Muqaṭṭaʿāt-axis is ORTHOGONAL to content-axis"* · *"al-Suyūṭī/al-Rāzī epistemic-humility
> EMPIRICALLY VINDICATED"* · *"al-Biqāʿī content-*munāsaba* claim empirically UNSUPPORTED"* ·
> ḥawāmīm *"moderate-cohesive only, not corpus-extreme"*

---

## 2. What the size-matched null shows

`d̄` rises steeply with set size — ρ = **+0.8998** against mean log word count, measured on the
published null's own draws (`h-new-2820-group-claims-matched.md:119-124`). The muqaṭṭaʿāt
surahs are **4.27× the median word count** of the other 85. A null that draws 29 surahs
uniformly from 114 therefore draws, overwhelmingly, *smaller* sets — and smaller sets have
larger `d̄`.

**Two facts settle it before any p-value** (`h-new-2820-group-claims-matched.md:130-142`):

1. **The published null never once drew a set as large as the muqaṭṭaʿāt.** Restricting it to
   draws whose mean log word count reaches the group's leaves **`n = 0` of 10,000**. The null
   against which "median-level" was scored contains no comparison set of comparable size at all.
2. **A size-matched comparison group cannot be built from the non-muqaṭṭaʿāt.** Bin 3 of 5
   requires 14 donors and the 85 non-muqaṭṭaʿāt contain 9. This is `h-new-46`'s STRONG-PASS
   result — muqaṭṭaʿāt concentrate in long surahs — restated as an impossibility.

Under a null that permutes muqaṭṭaʿāt membership *within quintile bins of log word count*:

| set | published %ile | **matched %ile (A2-k5)** | k = 10 | × period | verdict |
|:--|--:|--:|--:|--:|:--|
| muqaṭṭaʿāt-29 | 65.62 | **0.45** | 0.82 | 5.44 | crosses the claim's own 10 % bar |
| ḥawāmīm-7 | 20.90 | **0.05** | 0.02 | 0.21 | corpus-extreme in every arm |

**The sets ARE clustered.** The muqaṭṭaʿāt-29 are **3.6 % tighter** in root content than
size-matched surah sets; the ḥawāmīm-7 **10.7 % tighter**. Identical classification at the
replication seed. H-NEW-2820's verdict is **`REVERSES-CLUSTERED`**.

**Three qualifications travel with the verdict and are not separable from it.**

- **A third of the matched effect is Meccan/Medinan composition, not size.** Adding period to
  the stratification attenuates z from −2.426 to −1.639 and moves the percentile from 0.45 to
  5.44. **5.44 is the number to quote when only one can be.**
- **About one arbitrary baseline partition in six clears the 10 % bar under matching**, so the
  bar is loose. What carries the verdict is the margin: the Qurʾān sits at 0.45 (root
  instrument) and 0.60–0.80 (surface instrument), **beyond 98–99.5 % of baseline offsets**, and
  the baselines' median matched percentiles are mid-range (44.28, 37.72) — stratification does
  not by itself push an arbitrary partition into the tail.
- **Conditioning on size may remove mechanism, not only confound.** Holding length fixed removes
  part of what the muqaṭṭaʿāt *are*. **The correct reading is narrow: given surah sets of the
  same size profile, the muqaṭṭaʿāt set is measurably tighter in root content.**

---

## 3. What this does NOT license

**This is the half of the notice most likely to be skipped, and it is the half that matters.**

1. **It does not vindicate al-Biqāʿī.** It removes an empirical falsification. A 3.6 %
   content-tightening relative to size-matched peers is not *munāsaba* between a letter-opening
   and a surah's themes.
2. **It does not refute al-Suyūṭī.** *Allāh aʿlam bi-murādihi* is a claim about the *meaning* of
   the letters. **Nothing here decodes anything.** What is withdrawn is the assertion that this
   statistic *empirically vindicated* that stance — the statistic was measuring surah size.
3. **It does not restore "muqaṭṭaʿāt ⊥ content" in reverse.** "The axes are not orthogonal" is
   not "the axes are the same axis." The measured effect is small and partly compositional.
4. **It does not license a joint claim with Pillar 1.** See §5.

---

## 4. The propagation inventory

Counted under the `findings/UNIT-DRIFT-DEFECT.md` §6.2 rule: `.md` files under `findings/` and
`surahs/`, excluding `/runs/`, `/scripts/`, `prereg` filenames and the claim's own family.
Files outside that scope that assert the NULL are listed separately, because they are part of
the project record even though they do not enter the count.

**Classification.** **(a)** merely cites the NULL; **(b)** *depends* on it as evidence of
absence; **(c)** *contradicts* it now that the direction has flipped; **(d)** is not a citation
of this claim at all.

### (c) — contradicts; the file asserts what the matched null denies

| file:line | what it asserts | what changes |
|:--|:--|:--|
| `findings/phase-b-hypotheses/h-new-570-muqattaat-content-cluster.md:3,5,16,29,37,47,59,119-125` | the claim itself | all four assertions withdrawn as empirical results |
| `findings/phase-b-hypotheses/h-new-600-letter-families.md:3,5,18,70,72,113,119-124,163,198,203` | "H-NEW-570 generalization VINDICATED"; 65.62 and 20.90 quoted as NULL rows | the two inherited rows are withdrawn; H-NEW-600's **own** ALM-6 / ALR-5 nulls are the same size-blind design and are **untested**, not cleared |
| `findings/cross-finding/cross-finding-025-multi-axis-architecture.md:109-120,132-135` | "NULL at 4 independent scales"; "the muqaṭṭaʿāt-axis is the most orthogonal" | two of the four scales reverse; the orthogonality claim no longer has four supports |
| `findings/phase-b-hypotheses/h-new-1395-hawamim-cluster.md:6,10,17,55,67` | its dedicated ḥawāmīm test "demotes that signal to formal NULL" | **its own Cell B already saw the effect move** — see §4.1 |
| `findings/phase-b-hypotheses/h-new-580-five-factor-regression.md:5,9,124-136,203,229` | "formula_share confirmed orthogonal to muqaṭṭaʿāt-axis (H-NEW-570 replicated at OOS scale)" | the parent it replicates is reversed; the OOS-5 arm is an independent 5-subset test and is **untested**, not cleared |
| `findings/phase-b-hypotheses/h-new-910-alif8-cluster.md:256` | "letter-axis ⊥ content-axis now confirmed across ... full-29, HM-7" | two of the four confirmations reverse |
| `findings/phase-b-hypotheses/h-new-1010-singleton-cohort-form-coherence.md:231,261` | 570's NULL listed as one of four instantiations of letter-axis ⊥ content-axis | one of the four reverses |
| `surahs/Q002-al-baqara/03-tafsir-survey.md:173-186` | "falsified 4 times"/"vindicated 4 times"; "one of the clearest classical-vindication cases in the project" | the count and the characterisation both fall |
| `surahs/Q002-al-baqara/07-cross-references.md:105` | "FALSIFIED 4 times ... full-29 NULL at 65.62%ile ... ḥawāmīm-7 NULL" | two of the four reverse |
| `surahs/Q012-yusuf/03-tafsir-survey.md:85,133` | "FALSIFIED 4 times ... the wide muqaṭṭaʿāt content-clustering program is not [supported]" | the falsification count falls |
| `surahs/Q040-ghafir/01-empirical-profile.md:75` | "sharpens the *muqaṭṭaʿāt-axis ⊥ content-axis* finding by adding a third orthogonality" | the finding it sharpens is reversed |
| `surahs/Q044-al-dukhan/05-classical-claims-audit.md:194` · `06-novel-findings.md:140,202` | Q 44 "replicat[es] H-NEW-600 and H-NEW-570 NULL findings" | Q 44's own per-surah result is a different statistic and stands; the inherited framing does not |
| `surahs/Q046-al-ahqaf/05-classical-claims-audit.md:156` | *dībāj* "rhetorically supported by HM-7's internal cohesion (20%ile)" | **this one strengthens** — 20.90 → 0.05 |
| `KNOWLEDGE-GRAPH.md:236,243,291,297` | "FALSIFIED 5 times"/"VINDICATED 5 times" | two of the five reverse; a third (H-NEW-901) is the same size-blind null re-run |
| `MASTER-FINDINGS-LEDGER.md:1574,1582,1586,5232` | the 570, 580 and 600 ledger entries | as above |
| `poem/research/01-findings-harvest.md:227` · `05-false-trails-and-letters.md:155-156` | "al-Biqāʿī content-*munāsaba* FALSIFIED 5×" | the count falls; **the poem's verse is untouched** |

### (b) — depends on the NULL as evidence of absence

| file:line | the dependency |
|:--|:--|
| `findings/phase-b-hypotheses/h-new-1760-hawamim-opener-pericope.md:3,35,144` | its entire frame is "whole-surah NULL → rescued at pericope scale". The whole-surah result is not a NULL, so the *contrast* the flip is built on weakens — independently of the ⛔ notice the file already carries |
| `surahs/Q040-ghafir/02-content-analysis.md:82` · `Q046-al-ahqaf/02-content-analysis.md:164` | read HM-7's thematic tightness as "consistent with **moderate** FR-roots cohesion" — using 20.90 %ile as a **ceiling** on how tight the block may be |
| `findings/phase-b-hypotheses/h-new-600-letter-families.md:126` | explains HM-7's 20.90 % as a "chronology+adjacency artifact" *because* ALR-5 fails to replicate it. The premise was that 20.90 % is weak |

### (a) — merely cites

`surahs/Q040-ghafir/00-overview.md:98` · `Q040-ghafir/06-novel-findings.md:98` (cites 570 only
for the HM-7 **cluster definition**) · `Q040-ghafir/07-cross-references.md:74` ·
`Q041-fussilat/02-content-analysis.md:48` (cites §6's multi-axis framing; its Q 41:53 claim does
not rest on the null) · `Q042-al-shura/00-overview.md:115`, `01-empirical-profile.md:135`,
`02-content-analysis.md:120`, `07-cross-references.md:71` · `Q044-al-dukhan/07-cross-references.md:76` ·
`Q045-al-jathiyah/07-cross-references.md:80` · `Q046-al-ahqaf/07-cross-references.md:97` ·
`Q002-al-baqara/07-cross-references.md:172` · `findings/UNIT-DRIFT-DEFECT.md:314,430` (cites it
only as a citation-count example) · `findings/phase-b-hypotheses/h-new-2790-flagged-batch-size-matched.md:629,643,711`
(the queue that flagged it; its description of the statistic was corrected by H-NEW-2820 §1
before the test was designed).

### (d) — not a citation of this claim

`h-new-540-mufassal-awsat-middle.md:55,102` · `h-new-550-mufassal-tiwal-completion.md:81` ·
`h-new-560-meccan-tiwal.md:105` link `[[h-new-570-muqattaat-content-cluster|H-NEW-570]]` while
describing **entirely different queued tests** — "mufaṣṣal-awsāṭ × qiṣār boundary sensitivity",
"Medinan-only ṭiwāl {Q 57–66}", "oath-openers-subset cohesion". These are placeholder IDs from
before H-NEW-570 was assigned its topic. **They are wikilink collisions, not inheritances**, and
no notice is warranted. `journal/h-new-590-run-1.md:17` cites 570 as a file-convention template.
`journal/h-new-600-run-1.md` is a run log and is left as the historical record it is.

### Outside the counted scope, and load-bearing

- **`findings/phase-b-hypotheses/h-new-901-hm7-cohesion-prereg.md` + `csv/h-new-901-hm7-cohesion.json`.**
  H-NEW-901 re-runs the **identical** ḥawāmīm statistic — `d_observed = 0.8672422857142857`, the
  same value to sixteen digits — against the **same size-blind uniform-7 null**, obtains
  percentile 21.21, and records `"verdict": "NULL"`. It is a third instance of the same defect,
  and `KNOWLEDGE-GRAPH.md:243` counts it as an independent falsification. **The pre-registration
  is SHA-locked and has not been edited.** This entry is the notice.

### 4.1 H-NEW-1395's Cell B — the one prior test that looked, and what it saw

H-NEW-1395 is the sharpest (c) site because **it already contains the evidence**. Its Cell B
draws a length-matched null (`findings/phase-b-hypotheses/scripts/h-new-1395.py:60-70`) and the
matching moved the answer:

| H-NEW-1395 arm | null mean | p (one-tailed lower) |
|:--|--:|--:|
| Cell A — uniform 7-of-114, size-blind | 0.9230 | **0.2086** |
| Cell B — length-matched ±20 % | 0.9511 | **0.0514** |
| *(H-NEW-2820 A2-k5, log word count, stratified)* | *0.9712* | *%ile 0.05* |

**Each strengthening of the match raises the null mean and drives p down**, monotonically, in
exactly the direction the size-confound predicts. Cell B missed its Bonferroni α = 0.025 by two
percentage points and the finding recorded NULL.

Two defects explain why Cell B under-recovered the effect. It matches on **verse count** — the
*third*-ranked channel for `d̄` (ρ = +0.8395) rather than the dominant log word count
(ρ = +0.8998) — and it matches the **sum** over the 7-set rather than the per-surah size
profile, so a draw of one very long surah plus six short ones satisfies the constraint while
having nothing like the ḥawāmīm's size composition. `d̄` depends on the individual surahs'
sizes, not their total. This is `UNIT-DRIFT-DEFECT.md` §5's "a control that does not use the
strongest channel is not a control", occurring a year before that clause was written.

---

## 5. Does this bear on Pillar 1? — assessed, and the answer is no, in either direction

**Pillar 1 is the only pillar law that survived the 2026-08-07 genre controls.** H-NEW-570's
reversal is new positive evidence about the *same 29 surahs*, so the question had to be asked.
It was, and the answer is that **the two results do not combine, do not confound each other, and
do not move Pillar 1's strength**.

### 5.1 The mechanism-overlap hypothesis, tested and refuted

The two statistics share a vocabulary. The Fisher–Rao instrument runs over the top-500 QAC
roots, and Pillar 1's two marker roots are both inside it: **`ktb` at rank 23** (319 tokens) and
**`qrA` at rank 127** (88 tokens). If the muqaṭṭaʿāt surahs' shared Book-vocabulary — used
throughout, not only in the opening — were what pulls their root distributions together, the
clustering would be Pillar 1 measured a second time and the two would double-count.

**Method.** The H-NEW-111 matrix was rebuilt from QAC v0.4 and verified **bit-identical to the
stored matrix at every one of its 6,441 pairs** (max entry difference exactly `0.0`), reproducing
`d̄`(muq-29) `= 0.938813123152709` and `d̄`(ḥawāmīm-7) `= 0.867242285714286`. A leave-out matrix
was then built with the `ktb` and `qrA` columns **dropped before smoothing** (498 dimensions,
not 500 with two zeroed columns — a zeroed smoothed column is identical across surahs and would
compress every distance uniformly). H-NEW-2820's A2-k5 stratified null was re-run on both.
Because removing *any* two roots perturbs the matrix, 200 frequency-matched control pairs were
drawn — each partner within ±20 % of `ktb`'s and `qrA`'s token counts — giving a reference
distribution for the shift produced by removing two arbitrary roots of the same weight.

| set | matched %ile, full 500 | Book roots removed | shift | control shift (200 pairs) | controls shifting at least as far |
|:--|--:|--:|--:|--:|--:|
| muqaṭṭaʿāt-29 | 0.45 | 0.49 | **+0.04** | mean +0.01, sd 0.04, max +0.15 | **26 %** |
| ḥawāmīm-7 | 0.05 | 0.05 | **0.00** | mean −0.005, sd 0.007, max +0.01 | **62.5 %** |

**Removing both of Pillar 1's marker roots moves the clustering by less than a typical arbitrary
root pair of the same weight.** The Book vocabulary contributes nothing detectable to it.

### 5.2 What that means — the result cuts both ways, which is why the verdict is "no change"

- **It refutes double-counting.** The clustering is not the Book signal reappearing in a second
  instrument. There is no danger of citing one fact twice.
- **It equally refutes the competing explanation.** The natural worry in the other direction is
  that a topically coherent group of surahs would mention the Book anyway, so Pillar 1's residual
  rate ratio might be topical composition rather than an engineered marker. **That worry does not
  survive the same test:** whatever the 29 share, it is *not* Book-vocabulary. Pillar 1's effect
  is not explained away by the clustering.

The two results are about **disjoint vocabulary on the same group**.

### 5.3 Why they still may not be combined

Lexical disjointness is not statistical independence, and the distinction is the whole of
H-NEW-2670's lesson.

1. **Same group, same selection.** Both are properties of one fixed, non-randomly-chosen set of
   29 surahs. H-NEW-2670 established that given free choice of properties, **roughly one random
   14-letter subset in four** can be made to look as unique as the muqaṭṭaʿāt. Two properties of
   one group are not two independent confirmations of anything, and no null over the space of
   properties one *could* have selected has been constructed — nor may one be constructed
   post-hoc against a result already seen.
2. **Shared conditioning.** Both effects are residuals after holding surah size fixed on the
   same grouping, and H-NEW-2820 §2.2b shows that grouping admits no size-matched comparison
   group at all. Both live in the same conditioned space.
3. **Shared compositional skew.** The muqaṭṭaʿāt are 10.3 % Medinan against 29.4 % for the rest.
   A third of the clustering effect is that skew; Pillar 1 carries the same skew.

**Above all, the clustering is not evidence for the book-marker *function*.** It says the 29 are
mutually closer in root content than size-matched sets. It does not say they announce the Book,
and §5.1 shows it is not even *about* Book-vocabulary. A result on disjoint vocabulary cannot
corroborate a claim whose entire content is Book-reference.

**Verdict: Pillar 1 stands exactly where H-NEW-2760 left it** — rate ratio 2.580 against the
registered nuisance channel, **1.694 against the stronger one**, with its published
`p = 3.17 × 10⁻¹²` withdrawn. **H-NEW-570's reversal changes none of those numbers, and must
not be stacked onto them.**

---

## 6. Files

- Evidence: `findings/phase-b-hypotheses/h-new-2820-group-claims-matched.md`
  (pre-reg SHA-256 `45abd95012bbf520070685646af909428a183781d94c58c4638353281764b5f1`)
- Independence test (§5): script
  `findings/phase-b-hypotheses/scripts/h-new-2830-independence.py`; run
  `findings/phase-b-hypotheses/runs/h-new-2830-independence/20260807T095124Z/results.json`,
  written once with mode `'x'` into a directory created with `exist_ok=False`, progress
  checkpointed outside it under `runs/h-new-2830-progress/`.
  **A first, empty run directory `runs/h-new-2830-independence/20260807T095040Z/` is retained
  and never deleted**: that harness aborted at the reproduction gate because it compared a
  full-precision rebuild against the stored matrix, which H-NEW-111 serialises through
  `round_floats(o, n=6)` (`scripts/h_new_111_fisher_rao_mushaf.py:388`). The 2.2 × 10⁻⁸
  discrepancy was rounding and nothing else; the corrected harness rounds to match and then
  reproduces every entry exactly.
- **Honest limit on the §5 reproduction.** H-NEW-2820's claim arms and this one both build their
  stratified draws with `np.random.default_rng(seed)` at the same point in the stream, so the
  matched percentiles reproduced here (0.45 / 0.05 primary, 0.39 / 0.06 replication) come from
  the **same Monte-Carlo sample**, not an independent one. What is verified is the harness logic
  — matrix construction, binning, stratified draw, statistic, percentile — from separately
  written code. The leave-out comparison is unaffected: full and reduced arms use identical
  draws by construction, which is what makes it a paired test.

---

*Written 2026-08-07 by Waiel Al-Shujaa. A null model that cannot draw the thing it is comparing
against is not a comparison. The muqaṭṭaʿāt were clustered the whole time, and the instrument
was measuring how long the surahs are. Bismillāhi al-Raḥmāni al-Raḥīm.*
