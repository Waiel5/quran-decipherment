---
id: H-NEW-3180
title: "Pre-registration — do the Sajāwandī pause grades order the length of the unit they close? The one F-1 channel that is parser-free and unrun"
date: 2026-08-09
author: Waiel Al-Shujaa
status: PRE-REGISTERED — locked before any grade-conditional statistic was computed
family: WAQF-2026-08-09-B
seed: 20260509
seed_replication: 20260519
n_permutations: 10000
tests_in_family: 12
alpha_bonferroni: 0.0041666666666666666
raw_gate: 0.0004166666666666667
---

# Pre-registration — H-NEW-3180

## 0. Scope, and why this is not H-NEW-2610 again

**Frontier item F-1 is already answered and this pre-registration does not re-open it.** The
Step-0 search found the answer before any design work. Recorded here so that no future reader
mistakes this file for the F-1 test:

| F-1 clause | already answered by | verdict on disk |
|:--|:--|:--|
| grades → boundary hierarchy, **annotation-free** channel | H-NEW-2610 **H1a**, ρ = −0.0075, n = 4,266, p = 0.691 / 0.410 | **NULL** |
| …same, **consensus inventory, 5 rungs incl. lā** | H-NEW-2610 §7 `sensitivity_min_tashkeel_5rung`, ρ = −0.0150, n = 4,347 | **NULL** (ungated) |
| grades → boundary hierarchy, **syntactic** channel | H-NEW-2610 **H1b** ρ = −0.1564, p = 9.999×10⁻⁵ ×2 | PASS, but a second-tuple replication of H-NEW-2560 H5/R9, which is itself demoted CIRCULARITY-DOMINATED (ledger §10.142) |
| grades → **verse-final rhyme-class stability** | H-NEW-2610 **H2**, T = +3.41×10⁻⁴, p = 0.458 / 0.405; registered instrument control failed its own gate at 87.72 % < 90 %; post-hoc repair T = +1.83×10⁻⁴, p = 0.491 / 0.430 | **DOUBLY NULL + INSTRUMENT-FAILED** |
| grades → **clause-length distribution** | H-NEW-2610 **H3**, JT = 2,361, p = 9.999×10⁻⁵ | PASS, then **reducible to verse length**, r(density, mean verse length) = 0.913 |

Every figure in that table was read out of
`findings/phase-b-hypotheses/runs/h-new-2610/20260807T010205Z/result.json` and
`…/runs/h-new-2560/20260807T004157Z/result.json`, not out of the prose of either finding.

**What is left, and it is one thing.** H-NEW-2610's H3 measured *marks per 100 words, at sūra
level, by register*. **Nobody has measured the length of the segment each grade actually
terminates, at the locus level.** That is a different quantity from H3, it is the literal reading
of F-1's second clause, and it is the only remaining channel that is simultaneously
**parser-free, EQTB-free, register-free and able to include lā**. H-NEW-2610's only other clean
channel (verse-boundary resemblance) returned a flat null, so this is the second and last
opportunity for the grades to show themselves outside the annotation that shares al-Sajāwandī's
own ancestry.

**Honest prior, stated before the lock:** the most likely outcome is another length law. This
project has now watched a register effect (H-NEW-2610 H3), a chronology effect
(H-NEW-3120) and a tafsīr-attention effect (H-NEW-2620) all dissolve into verse length. I am
running this because a NULL here is *more* informative than a PASS — see §7.3 — not because I
expect it to pass.

---

## 1. Hypothesis

**H1 (singleton inventory).** Over all graded waqf loci in
`quran-text/quran-full-tashkeel.json`, the Spearman rank correlation between **stop-strength
grade** and the **length of the segment the mark terminates** is **positive**.

**H2 (consensus inventory).** The same, over `quran-text/quran-min-tashkeel.json`, with the
prohibition grade **lā (U+06D9)** present as the bottom rung.

### 1.1 Direction lock and its justification — from published anchors, not from the map

The frontier map's Prior line is **not** used. It scores 1-for-7 with every optimistic prior
failing. The direction ρ > 0 is locked from two independent anchors, both already on disk:

1. **al-Sajāwandī's own definitions**, as al-Suyūṭī reports them at *al-Itqān* **nawʿ 28**
   (`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` line 5147; the heading
   is at line 5092. **The map and the F-1 brief both cite nawʿ 27; the recension on disk merges
   nawʿ 22–27 under one heading at line 4631, so it is nawʿ 28.** H-NEW-2610 §0.1 established
   this and I am carrying its correction, not re-deriving it). *lāzim* is
   `ما لو وصل طرفاه غير المراد` — "that which, if its two sides are joined, is not the intended
   meaning", i.e. the two sides are **distinct completed propositions**. *waṣl awlā* is the
   opposite: continuing is preferable, so the mark falls **inside** a unit still in progress. A
   mark that closes a completed proposition closes a **larger** span than a mark that interrupts
   one mid-flight. Hence stop-strength should rise with the length of the closed segment.
2. **The measured ladder already published**, which is a stronger anchor than the tradition
   because it is a number. H-NEW-2560 R9 and H-NEW-2610 H1b both find mean dependency
   arc-crossing falling monotonically with stop-strength (full-tashkeel 0.268 → 0.151 → 0.074;
   no-tashkeel 0.306 → 0.193 → 0.103 for ṣlà → jīm → qlà). Fewer crossing arcs means the mark
   closes a constituent rather than splitting one, and closed constituents are longer than
   fragments. **The published measurement predicts ρ > 0.**

### 1.2 The counter-anchor, named before the lock

The direction is **not** a gimme and two facts already on disk pull against it.

- H-NEW-2610's `calibration_ladder` records normalised in-verse position: ṣlà 0.537, jīm 0.597,
  qlà 0.638, **mīm 0.450**. The top rung sits *earliest* in the verse, breaking the gradient its
  three neighbours make.
- H-NEW-2610 §3 generated a post-hoc reading — that marks concentrate where surface cues
  **mislead**, so a surface instrument should order them **backwards**. That reading is untested
  and MW-7-capped, but if it is right the sign here is negative.

A **REVERSED** verdict is therefore a live, pre-committed outcome with its own decision branch
(§7.1), not an escape hatch.

### 1.3 What a PASS would and would not buy — stated before the number exists

A PASS partly **duplicates the construct** H1b already measured, by a different instrument. It
would be a parser-free corroboration of "the grades track constituent size", which is worth
having precisely because H1b's channel is contaminated — but it is **not** independent of H1b's
construct and must never be cited as if it were. A NULL is the cleaner information: it would
mean the grade ordering fails in **both** clean channels (VBR and segment length) while surviving
only inside the annotation, which converts H-NEW-2610's cautious "syntactic commentary" verdict
into a much harder one.

---

## 2. Everything inspected before this lock — exhaustive

Recorded so the lock is auditable. **No grade-conditional statistic of any kind was computed.**
No per-grade mean, no observed ρ, no per-grade length, no cross-tabulation of grade against
anything.

1. Glyph census of all seven waqf codepoints in all thirteen text files on disk (reproducing
   `findings/AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE.md`).
2. SHA-256 of the three `quran-text/` JSONs: full `382a7341…`, min `87aaab41…`, no `253f72f3…`.
   These match the hashes H-NEW-2610 and H-NEW-2560 recorded.
3. **Mark tokenisation geometry** — full-tashkeel attaches marks to the **end of the preceding
   token** (4,276 such tokens); min-tashkeel carries them as **standalone tokens** (4,364). Two
   marks are **word-internal** in each file and are excluded: U+06DC saktah in Q 2:245
   *wa-yabṣuṭu* and Q 7:69 *baṣṭatan* (3 internal occurrences in full-tashkeel, 2 in min).
4. **Marks at verse-initial juncture: 0 in both files. Marks at verse-final position: exactly 2
   in each, both saktah** (Q 18:1, Q 69:28), both outside the graded set. This independently
   confirms H-NEW-2560's statement that the muṣḥaf places no graded waqf mark at any verse end
   (al-Suyūṭī's exemption, nawʿ 28 line 5245).
5. **Instrument reproduction against a prior run** — my parser returns full-tashkeel graded loci
   = 4,266 with {ṣlà 1651, jīm 2083, qlà 511, mīm 21} and min-tashkeel = 4,347 with
   {lā 68, ṣlà 1682, jīm 1972, qlà 603, mīm 22}. Both are **exact matches** to H-NEW-2610's
   `eligible_loci.by_grade` and `sensitivity_min_tashkeel_5rung.by_grade`.
6. **Marginal** segment-length distributions, pooled over all grades, no grade breakdown:
   full-tashkeel L1 median 7 words, mean 8.16, range 1–49, 39 distinct values; L2 median 29
   skeleton chars, mean 33.98; L3 median 55 raw chars, mean 65.47.
7. **Tie fractions** (§4.3) and **ρ_max / ρ_min** (§4.4), both computed as properties of the
   label multisets and the length vector jointly. Neither reveals the observed ρ.
8. An approximate Null-A critical value from a 2,000-permutation batch, used only for the power
   statement in §4.4. A null distribution does not contain the observed statistic.

---

## 3. Instrument

### 3.1 Segmentation

Tokenise each verse on spaces. Strip waqf glyphs, recording for each the word index it follows.
A graded mark following word *i* sits at the juncture *i → i+1*. Boundaries of a verse are
{verse start} ∪ {every graded-mark juncture} ∪ {verse end}. **The segment terminated by a mark at
juncture *i* is the word span from the previous boundary up to and including word *i*.**

Excluded from the graded set, following H-NEW-2610 exactly: **saktah U+06DC** and
**muʿānaqa U+06DB**. They are not rungs of the *marātib* and are not boundaries here either.

### 3.2 Grade ranks

- **H1, full-tashkeel, 4 rungs:** ṣlà 1 < jīm 2 < qlà 3 < mīm 4.
- **H2, min-tashkeel, 5 rungs:** **lā 1** < ṣlà 2 < jīm 3 < qlà 4 < mīm 5.

lā's placement at the bottom is not a free choice: it is *waqf mamnūʿ*, the inventory's only
prohibition, and it is the ordering H-NEW-2610 §7 already used. Adopting it keeps this test
comparable to that one.

### 3.3 Three length channels — all three run, worst reported as the headline

- **L1** = number of words in the segment.
- **L2** = number of characters after removing every combining mark (U+064B–U+065F, U+0670,
  U+06D6–U+06ED, U+0640) — the consonantal skeleton.
- **L3** = number of characters of the segment as stored, spaces excluded.

**The verdict of an arm is taken from its worst channel** (§7.1). The dominant channel — the one
whose removal would change the verdict — is named in the finding.

### 3.4 Statistic

Tie-corrected Spearman ρ between grade rank and segment length, over all graded loci in the file.
One-sided against the locked direction ρ > 0.

---

## 4. Null models, controls, and the limit that cannot be tested

### 4.1 Null A — within-verse label permutation (strict)

Permute the **grade labels** among the marks **of the same verse**, holding every mark
**position** exactly fixed. The segmentation is therefore **identical** in the observed data and
in every permutation. This null asks the only question the hypothesis actually poses: *given
where this verse's marks are and which labels it uses, are the labels assigned in a
length-ordered way?* It cannot be satisfied by mark density, by verse length, by register, or by
any property of where marks fall — all of those are held fixed by construction.

### 4.2 Null B — within-sūra label permutation (loose)

Permute grade labels among all graded marks of the same sūra. Looser: it does not hold the
verse-level mark configuration fixed, so a grade that concentrates in mark-dense (hence
short-segment) verses can move this statistic. Reported alongside, never instead.

### 4.3 Tie fraction — measured, and why the test is already exact

| arm | L1 words | L2 skeleton | L3 raw |
|:--|--:|--:|--:|
| H1 full-tashkeel | **0.9981** | 0.9944 | 0.9899 |
| H2 min-tashkeel | **0.9984** | 0.9940 | 0.9926 |

**Ties are essentially total** — 39 distinct word-lengths across 4,266 segments. The project rule
is that a tie fraction above 50 % requires an exact test. **It is satisfied by construction and
not by exception: every p-value in this design is a permutation p-value.** No asymptotic Spearman
distribution, no *t*-approximation, no χ² is used anywhere, and the ranks are tie-corrected
(midranks). The permutation distribution is computed under exactly the tie structure the data
has. **If any asymptotic p-value appears in the output, the run is void.**

### 4.4 Power, MDE, and the S\* vs S_max branch — including the part that is untestable

Achievable range of ρ under within-verse relabelling, computed exactly (the per-verse
sort-and-match assignment is provably optimal, because the global grade-rank multiset is
invariant under within-verse permutation, so the objective separates across verses):

| arm | channel | **ρ_MAX** | **ρ_MIN** | midpoint |
|:--|:--|--:|--:|--:|
| H1 | L1 words | **+0.3692** | −0.0986 | +0.135 |
| H1 | L2 skeleton | +0.3716 | −0.0944 | +0.139 |
| H1 | L3 raw | +0.3721 | −0.0955 | +0.138 |
| H2 | L1 words | **+0.3595** | −0.1060 | +0.127 |
| H2 | L2 skeleton | +0.3609 | −0.1026 | +0.129 |
| H2 | L3 raw | +0.3659 | −0.0978 | +0.134 |

**This table contains the design's most important limitation and I am stating it before the
run, not after.** The achievable range is **not centred on zero**: its midpoint is about
**+0.13**. Only **43.0 %** of H1's loci (1,834 of 4,266, in 632 of 2,610 marked verses) and
**44.2 %** of H2's (1,923 of 4,347) sit in verses carrying **two or more distinct grades** and
are therefore permutable at all. The remaining ~57 % contribute a **fixed** component to ρ that
**no within-verse permutation can move**.

**Consequence, pre-committed:** Null A tests the *label-assignment* component and is **blind to
the ~+0.13 baseline**. Null A can neither confirm nor reject it. Anyone reading a Null-A PASS as
evidence about the whole ρ would be wrong, and I will not write it that way. Null B is the only
arm with any purchase on the baseline, and it is the loose one. **This is the honest analogue of
the lane that discovered its critical value 119.45 sat above its S_max of 119: here the test is
not untestable, but it is testable over less than half its own data, and the half it cannot see
is pushing in the locked direction.**

ρ_MAX ≈ +0.37 sits far above any plausible Null-A critical value at the gate, so the
**UNTESTABLE branch is not expected to fire** — but it is checked at runtime anyway (§7.1) by
comparing ρ_MAX against the realised (1 − raw_gate) quantile of the Null-A distribution, per
channel, per arm.

**MDE, defined in interpretable units.** Starting from a Null-A draw (so the observed labels are
never touched), optimally length-order the labels within a fraction *f* of permutable verses.
The MDE is the smallest *f* detected at the raw gate, averaged over 20 seeds. Reported in the
finding whatever the verdict, and **reported even if the verdict is PASS**.

### 4.5 The control checked against all three ways a control fails

Per `cross-finding-030-three-ways-a-control-fails.md`:

1. **Does it discriminate?** Yes, and verified pre-lock: relabelling moves ρ across a range of
   about 0.47 (−0.10 → +0.37). A null with real spread. **Not mechanism 1.**
2. **Does it apply?** **Partially — and this is a real, declared, mechanism-2 exposure.** Null A
   is inert on 57 % of loci (§4.4). It is not blind to the feature under test on the 43 % it
   covers, but it does not exercise the rest. Declared, quantified, and the reason Null B exists.
3. **Does it duplicate the treatment?** No. Null A destroys exactly the grade↔length association
   under test while preserving mark positions, mark density, verse length, sūra and register
   identically. **Not mechanism 3.**

### 4.6 Instrument control — pre-set, and it can fail

Before any statistic, the parser must reproduce H-NEW-2610's published loci counts **exactly**:
full-tashkeel `by_grade` = {1:1651, 2:2083, 3:511, 4:21}, n = 4,266; min-tashkeel 5-rung
`by_grade` = {1:68, 2:1682, 3:1972, 4:603, 5:22}, n = 4,347. **Mismatch on any cell aborts the
run with `SystemExit`** — there is no "close enough" branch. This control discriminates (a
segmentation bug changes these counts), applies (it exercises the exact parsing path the test
depends on), and does not duplicate the treatment (it is grade-marginal, not grade-conditional).

---

## 5. Deciding parameters — declared, per `cross-finding-029`

Every one of these could carry the verdict, so every one is named and swept or fixed on record.

| # | parameter | primary | swept? |
|--:|:--|:--|:--|
| **P1** | **source file / waqf inventory** | run under **both**: full-tashkeel (the singleton) and min-tashkeel (the 12-file consensus) | **yes — H1 and H2 are the sweep**; no-tashkeel added ungated as a third tuple |
| **P2** | grade → rank **coarsening** | printed glyphs mapped to ordinal ranks. **This is a coarsening and it is lossy**: the printed inventory is *not* a 1:1 rendering of al-Sajāwandī's five *marātib*, and ṣlà/qlà are terms of the later muṣḥaf-printing tradition (H-NEW-2610 §0.1). | fixed, declared |
| **P3** | lā's rank | bottom (rank 1) | fixed; follows H-NEW-2610 §7 |
| **P4** | which marks are segmentation boundaries | graded marks only; saktah and muʿānaqa excluded | variant reported ungated |
| **P5** | length channel | three; **worst is the headline** | yes |
| **P6** | segment orientation | the segment the mark **closes** (ends at the mark) | variant — the segment it **opens** — reported ungated |

---

## 6. Multiplicity

2 arms × 3 length channels × 2 nulls = **12 registered inferences**. α_Bonferroni = 0.05/12 =
**0.0041667**. Project novelty rule (base α = 0.005): **raw decision gate = 0.005/12 =
0.00041667**. Monte-Carlo floor at 10,000 permutations is 1/10,001 = 9.999×10⁻⁵, which clears the
gate.

**k = 12 is the conservative count.** Counting arms alone would give k = 4 and a looser gate.
Per the project rule that Bonferroni **tightening** is self-verifying while loosening requires
ratification, k = 12 is adopted and will not be reduced after the fact for any reason.

Seeds: 20260509 (Null A H1), 20260510 (Null B H1), 20260511 (Null A H2), 20260512 (Null B H2),
20260513 (MDE), 20260514 (variants). Replication at +10 throughout. 10,000 permutations per null.

---

## 7. Decision rules — the verdict function is written here and the script must match it line by line

### 7.1 Per-arm verdict

For arm X ∈ {H1, H2}, with channels c ∈ {L1, L2, L3} and nulls N ∈ {A, B}:

```
p[X][c][N]      = (1 + #{perm : rho_perm >= rho_obs[X][c]}) / (1 + n_perm)       # locked tail, rho > 0
p_opp[X][c][N]  = (1 + #{perm : rho_perm <= rho_obs[X][c]}) / (1 + n_perm)       # opposite tail
worst_p[X]      = max over c, N of p[X][c][N]
worst_p_opp[X]  = max over c, N of p_opp[X][c][N]
sign_ok[X]      = rho_obs[X][c] > 0 for ALL three c
sign_rev[X]     = rho_obs[X][c] < 0 for ALL three c
rho_crit[X][c]  = the (1 - RAW_GATE) quantile of the Null-A permutation distribution
untestable[X]   = rho_max[X][c] < rho_crit[X][c] for ANY c

VERDICT[X] =
    "UNTESTABLE"           if untestable[X]
    "PASS"                 elif sign_ok[X]  and worst_p[X]     < RAW_GATE
    "REVERSED"             elif sign_rev[X] and worst_p_opp[X] < RAW_GATE
    "NULL"                 otherwise
```

`RAW_GATE = 0.005 / 12 = 0.00041667`. The UNTESTABLE test is evaluated **first** and is not
overridable by a small p-value.

### 7.2 Replication

Every arm is re-run at seed +10. **If the replication verdict differs from the primary for any
arm, that arm is reported as NULL-UNSTABLE regardless of which way the primary went.**

### 7.3 Family verdict, pre-committed both ways

- **Both arms PASS** → `GRADE ORDERS SEGMENT LENGTH (parser-free channel)`. Must be published
  together with §1.3: it corroborates H1b's construct by a second instrument and is **not**
  independent of it. Must also be published together with the §4.4 statement that Null A saw
  57 % of nothing.
- **Both arms NULL** → `SECOND CLEAN-CHANNEL NULL`. Combined with H-NEW-2610 H1a this means the
  grade ordering fails in **every** annotation-free channel yet measured and survives only inside
  the dependency treebank. That hardens the standing verdict and is the outcome I expect.
- **Arms disagree** → the **inventory is the deciding parameter** and that, not the ρ, is the
  finding. It would mean the choice of text file carries a boundary-hierarchy verdict, which is
  the exact conclusion `AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE.md` §5 anticipated.
- **REVERSED** → report at full prominence and hand the §1.2 misleading-surface reading its
  first supporting evidence, while stating that this design was not built to test it.

### 7.4 Reducibility check — pre-committed, and it can demote a PASS

Whatever the verdict, recompute ρ with segment length **residualised on the host verse's word
count**. H-NEW-2610's H3 passed and then dissolved at r = 0.913 against verse length; the same
demotion must be offered a chance here. **If a PASS does not survive residualisation, it is
reported as CBM (confirmed but reducible) in the headline, not in the limits.**

---

## 8. Publication commitments

1. A NULL is published with the same prominence as a PASS, with MDE and the §4.4 blind-fraction
   statement in the headline.
2. All three length channels are tabulated whatever they show; the worst is the headline; the
   dominant one is named.
3. Both inventories are reported. Which inventory is *correct* is **not** settled here and will
   not be settled by preference — that requires a printed-muṣḥaf comparison that is not on disk.
4. Every number in the finding is machine-checked against `result.json`.
5. The run directory is created with `os.makedirs(exist_ok=False)` and all files opened `'x'`.
   **No run directory is ever deleted**, including superseded or uncommitted ones.
6. This pre-registration is **never edited after the run**. Corrections go in the finding.
   (`feedback_prereg_immutability`: one bulk commit broke four SHA locks in this project.)

*Bismillāhi al-Raḥmāni al-Raḥīm.*
