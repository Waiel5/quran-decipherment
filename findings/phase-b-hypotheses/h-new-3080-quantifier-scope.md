---
title: "H-NEW-3080 — F-14's quantifier contrast is real and it is NOT the formulae: deleting kull's own most formulaic material makes the effect STRONGER, and the whole result rests on three baʿḍ tokens"
author: Waiel Al-Shujaa
date: 2026-08-09
status: CONFIRMED on the locked rule — 2 of 6 registered cells clear; the map's CBM prior is refuted in the opposite direction
frontier_item: F-14 (HANDOFF/FRONTIER-MAP-2026-08-07.md:324-330)
prior_work_on_this_item: NONE — see §0
prereg_path: findings/phase-b-hypotheses/prereg-h-new-3080-quantifier-scope.md
prereg_sha256: 2e2cde58e7fc2e66f34d27d007c3ed8be19d6eeb30550c6a88ec24f7cc4443e4
script_path: findings/phase-b-hypotheses/scripts/h-new-3080.py
script_sha256: be392cd3a1424984bc6f74432674efbcf2bc75082ddebcf5ae807ea3d0a0561d
run_dir: findings/phase-b-hypotheses/runs/h-new-3080/20260809T080957Z
posthoc_run_dir: findings/phase-b-hypotheses/runs/h-new-3080/POSTHOC-20260809T081641Z-strata-occupancy
git_commit_at_lock: e94186a0a15b849089d27067637e282de19b468b
seed: 20260509
n_perm: 10000
k_family: 6
alpha_bonferroni: 0.0083333
method_parents:
  - findings/UNIT-DRIFT-DEFECT.md
  - findings/phase-b-hypotheses/cross-finding-029-the-deciding-parameter.md
  - findings/ABSENCE-CLAIMS.md
sibling_findings:
  - findings/phase-b-hypotheses/h-new-3070-deictic-gradient.md
  - findings/phase-b-hypotheses/h-new-3010-conditional-register.md
  - findings/phase-b-hypotheses/h-new-3040-modality-axis.md
  - findings/phase-b-hypotheses/h-new-2800-legal-formulae.md
gives_a_handle_on: findings/phase-b-hypotheses/ethical-universalism.md
---

# H-NEW-3080 — quantifier scope and register

## 0. STEP-0 FIRST — F-14 had not been executed, and this is the family's first PASS

The frontier map's own binding rule puts the "does this already exist?" check before the design.
It was run first, and its result is §0 of the pre-registration, not an afterthought.

**F-14 had not been executed.** No finding, no pre-registration, no script, no run directory.
The map says so itself at `HANDOFF/FRONTIER-MAP-2026-08-07.md:154` —
*"quantifiers | UNTOUCHED | `quantifier` matches 5 of 906 files, none as topic."* An independent
census lane, dispatched in parallel and blind to my design, returned the same answer.

**Three prior lanes cross the QAC `LEM` field with the Neuwirth–Sinai TSV specifically:**
H-NEW-3010 (conditionals, NULL), H-NEW-3040 (modality, 3 PASS / 5 NULL), and this one. Four more —
H-NEW-2630, H-NEW-2640, H-NEW-2700, H-NEW-3020 — run the same *shape* of test against the project's
own H-NEW-2500 register proxy rather than the TSV. The pre-registration's §0 roster lists all six
under "prior register × QAC-lemma tests" and does not draw that distinction; the distinction is
drawn here rather than by editing a locked file.

> **The base rate matters more than any of this, and it points at my own result.** Of the six
> primary registered lemma-vs-register hypotheses in this family — 2630, 2640, 2700, 3010, 3020,
> 3040 — **six of six returned NULL or reversed. H-NEW-3080 is the first PASS.** That cuts both
> ways and both belong here: it rules out a lane where everything passes, and it makes a lone
> CONFIRMED the one result in the family that deserves the hardest look. Read it alongside §6.

**Nothing had ever counted *kull* corpus-wide for its own sake.** The one incidental prior count is
`findings/phase-b-hypotheses/word-pair-lemma-counts.csv` row 28, a 2026-04-12 byproduct of an
unrelated word-pair-symmetry study, which gives `kul~` = **359** and row 67 gives `baEoD` = **157**.
Those are exactly this finding's census figures, arrived at through a third independent code path.

**No locked formula-exclusion list existed anywhere.** F-14's own text is the only place that
demands one. The nearest precedent is H-NEW-2800 (F-15), whose legal-formula census was drawn from
al-Qurṭubī's headings and whose shape was *census stands, inferences NULL*.

**And `ethical-universalism.md` had been waiting for this.** That document (2026-04-12) is
qualitative, hand-estimates ">300" universal verses, and explicitly flags a quantitative count as
unfinished work. Nothing ever picked it up. This is the first quantitative handle on it.

---

## 1. Verdict in one paragraph

**CONFIRMED on the locked rule, and the map anticipated the wrong failure mode.** The universal
quantifier *kull* stands to the partitive *baʿḍ* at a far higher ratio in the eschatological /
exhortative / admonitory register than in the community-legal register: pooled log odds ratio
**−2.6959** with the formulae excluded and **−2.2895** with them kept, both against a locked
direction fixed from al-Suyūṭī before any count was taken, and both clearing α_Bonferroni =
0.0083333 at their **worst** length channel (p = 0.00080 and 0.00150). The frontier map predicted
**CBM — "likely dominated by the formulae."** It is not. Deleting `kull shayʾ` and `kull nafs` —
144 of *kull*'s 359 tokens, the most formulaic material the word has — **makes the effect larger,
not smaller**, because those formulae are concentrated in the *legal* register. It is not the only
map CBM prior to fall: H-NEW-3070 refuted F-4's on the same day
(`h-new-3070-deictic-gradient.md`, whose title states outright that the deictic shift "is not
formulaic"). That is the one sibling case I verified myself; the lane coordinator reports a third,
which this finding does not independently confirm and does not count.
**Four of the six registered cells do not clear**, and one of the two register
mappings does not support the headline at all. And the entire ARM-1 contrast pivots on a cell
containing **three tokens**, two of which are the two halves of a single reciprocal idiom in one
verse. §5 and §6 are not the limits section; they are half the result.

---

## 2. What was measured

### 2.1 The census, plainly

| quantity | count |
|:--|--:|
| `kul~` word-tokens (universal pole U) | **359** |
| `baEoD` word-tokens (partitive pole P, RT-A1 PRIMARY) | **157** |
| `min` + definite-article partitive proxy (RT-A2, robustness only) | **677** |
| `min` total in corpus, for scale | 3,226 |

`min` is not primary and never could have been. It is overwhelmingly ablative, separating
*min al-tabʿīḍiyya* from *min al-ibtidāʾiyya* needs a parse, and the only parse on disk (EQTB) is
recorded in this project's own notes as parser-contaminated for morphology-conditioned questions.
Admitting 3,226 tokens against 157 would have produced a `min`-density statistic wearing a
quantifier label. The 677-token proxy runs as declared robustness and carries no verdict.

**One trap avoided, worth recording because it would have doubled the partitive pole with a word
that is not a quantifier.** `word-pair-lemma-counts.csv` row 55 shows `baEod` (بَعْد, "after") at
**199** tokens — a different lemma from `baEoD` (بَعْض, "some"). In unvocalised text substring
counting merges بعد with بعض. The QAC lemma field keeps them apart; this extraction keyed on
`baEoD`.

### 2.2 The locked formula-exclusion list, and what each level removed

Built **before the lock** from register-blind collocation frequency — the lemma of the word
immediately following each of the 359 *kull* tokens, within the same verse — and hashed with the
pre-registration.

| level | excluded head lemmas | rule that generated the set | removed | `kull` retained |
|:--|:--|:--|--:|--:|
| **EX-0** | — | no exclusion | 0 | **359** |
| EX-1 | `$aYo'` (*shayʾ*) | bigram frequency ≥ 100 | 121 | 238 |
| **EX-2 PRIMARY** | `$aYo'`, `nafos` (*shayʾ*, *nafs*) | **the two formula heads named by the frontier map itself**, independently the top two by frequency | 144 | **215** |
| EX-3 | + `>um~ap` (*umma*) | bigram frequency ≥ 15 | 159 | 200 |

Top collocates: *shayʾ* 121 (33.7 % of all *kull*), *nafs* 23, *umma* 15, then nothing above 6.
Top trigrams: *kull shayʾ qadīr* 35, *kull shayʾ ʿalīm* 20, *kull nafs mā…* 13, *kull shayʾ
shahīd* 8. EX-2 is primary because its set is **externally specified** — the map named those two
formulae before this design existed. EX-1 and EX-3 exist so the *threshold*, the classic deciding
parameter, is varied rather than chosen.

### 2.3 The two register mappings, and ARM 2

Both use LEGAL-precedence containment over `sinai_genre` in
`findings/classical-sources/neuwirth-sinai-genre-labels.tsv`.

- **MAP-1 (PRIMARY)** — `LEGAL` if the label contains `legal`; else `UNIV` if it contains
  `eschatolog`, `exhort` or `admonit`. **17 LEGAL, 42 UNIV, 55 dropped.**
- **MAP-2** — H-NEW-3010's `map_M1` verbatim: `LEGAL` if `legal`; else `UNIV` if `eschatolog` or
  `polemic`. **17 LEGAL, 36 UNIV, 61 dropped.**

**ARM 2** reads the Qurʾān's own vocative addressee instead of a modern scholar's genre label:
*yā ayyuhā al-nās* / *al-insān* (23 openers, UNIVERSAL) against *yā ayyuhā alladhīna āmanū*
(89 openers, COMMUNITY), blocks running to the next delimiting opener or surah end — **489 and 939
verses**, 112 blocks. 38 of the 150 `>ay~uhaA` tokens are non-delimiting. The runner asserts all
five integers against the data and exits non-zero on mismatch.

### 2.4 The statistic, and why it has no unit count in its denominator

`LOR = log[ (U_LEGAL + ½)(P_UNIV + ½) / ((P_LEGAL + ½)(U_UNIV + ½)) ]`, pooled across units, with
the pole label permuted across units and per-unit counts held fixed. Locked direction **LOR < 0**.

Under `UNIT-DRIFT-DEFECT.md` **Screen B fires hard** — median word count is **539** for LEGAL
against **137** for UNIV, a **3.9× gap** — but **Screen A does not**, because the statistic is a
ratio of two counts drawn from the same text and has no per-verse, per-word or per-surah divisor.
That was the reason for choosing it, stated in the pre-registration before any count.

---

## 3. The primary result, and the channel table that governs it

Length is at least three variables. No channel is locked; all four run and **`p_cell` is the
maximum over the non-degenerate channels — the worst.** Under cross-finding-029 the deciding
channel is itself a reportable quantity, so the argmax is named for every cell.

| cell | grouping | excl | LOR | C0 unstrat. | C1 log-words | C2 verse-count | C3 mean-verse-len | **p_cell** | argmax | Fisher | verdict |
|:--|:--|:--|--:|--:|--:|--:|--:|--:|:--|--:|:--|
| **1 PRIMARY** | MAP-1 | EX-2 | **−2.6959** | 0.00010 | **0.00080** | 0.00010 | 0.00070 | **0.00080** | **C1** | 2.9×10⁻⁸ | **PASS** |
| 2 | MAP-1 | EX-0 | −2.2895 | 0.00010 | **0.00150** | 0.00020 | 0.00010 | **0.00150** | **C1** | 4.3×10⁻⁷ | **PASS** |
| 3 | MAP-2 | EX-2 | −1.2270 | 0.00020 | 0.00260 | 0.00010 | **0.18598** | 0.18598 | **C3** | 9.2×10⁻⁵ | NULL |
| 4 | MAP-2 | EX-0 | −0.9009 | 0.00050 | 0.01370 | 0.00130 | **0.27537** | 0.27537 | **C3** | 8.8×10⁻⁴ | NULL |
| 5 | ARM 2 | EX-2 | −1.1946 | 0.04480 | 0.02180 | 0.02790 | **0.06059** | 0.06059 | **C3** | 2.3×10⁻³ | NULL |
| 6 | ARM 2 | EX-0 | −0.7860 | **0.09579** | 0.08409 | 0.08709 | 0.09499 | 0.09579 | **C0** | 2.0×10⁻² | NULL |

**The dominant channel is mean verse length in all three groupings** — Spearman ρ against the LEGAL
indicator: **+0.7516** (MAP-1), **+0.7796** (MAP-2), **+0.2410** (ARM 2). It beats log word count
(+0.6131, +0.5523) and verse count (+0.2297, +0.1348) in both maps.

**So the length gap is large and the design already absorbs it — by construction, not by choice.**
`p_cell` is the worst channel, so length is controlled by taking the least favourable control
rather than a selected one. Cells 1 and 2 clear α at *every* channel including C3, the strongest.
Cells 3 and 4 are killed by C3 alone: p swings from 0.00020 to 0.18598, a **930×** swing, larger
than the ~70× that put H-NEW-3010 into cross-finding-029. §6.2 is about what that C3 control
actually is.

No channel was flagged DEGENERATE. Max tie fraction across all six cells was **0.0121**, far below
the 0.50 that would have forced the exact test; Fisher's exact was computed and reported anyway.

**Independent recount.** The primary 2×2s were recomputed through a separate code path written
after the run: EX-0 gives (89, 74, 41, 3) and LOR = −2.2895; EX-2 gives (39, 74, 27, 3) and
LOR = −2.6959. Exact agreement.

---

## 4. With and without the formulae — the map anticipated the wrong failure mode

This is the decisive arm the brief named, and it is the interesting half of the result.

| | U_LEGAL | P_LEGAL | U_UNIV | P_UNIV | LOR | odds ratio |
|:--|--:|--:|--:|--:|--:|--:|
| **EX-0** — all 359 *kull* | 89 | 74 | 41 | 3 | −2.2895 | 9.87 |
| **EX-2** — 144 formula tokens deleted | 39 | 74 | 27 | 3 | **−2.6959** | **14.82** |

**Removing the formulae strengthens the effect by 0.41 log-odds.** The mechanism is legible in the
margins: *kull* falls **89 → 39 in LEGAL (−56 %)** but only **41 → 27 in UNIV (−34 %)**. The
formulae live disproportionately in the long legal surahs, so excluding them removes more universal
quantification from the register that had less of it to spare. The ladder is monotone in the same
direction — EX-1 −2.6803, EX-2 −2.6959, EX-3 −2.7216 — and every one of the fourteen MAP-1
robustness cells carries the locked sign at p_worst between **0.00090 and 0.01380**.

**The map's prior was CBM. The correct verdict is the opposite of CBM: the formulae were masking
the effect, not manufacturing it.** F-14's confound was real, named correctly, and pointed the
wrong way.

There is a wrinkle worth stating, because it cuts against the neat story. al-Suyūṭī's own
discussion (§7) cites *{wa-anna Allāha bi-kulli shayʾin ʿalīm}* as a paradigm of *unrestricted*
generality and locates such verses outside the legal material. At surah granularity the opposite
holds — *kull shayʾ* is denser in the long legal surahs — because register here is a property of
the surah, not of the verse. **The classical claim and this measurement are not in contradiction;
they are at different scales, and this measurement cannot adjudicate the verse-level claim.**

---

## 5. The four cells that did not clear — at equal prominence

Four of six is a fact about the result's breadth, not a footnote.

### 5.1 MAP-2 does not support the headline (cells 3, 4)

**The effect is present under MAP-1 and absent under MAP-2, and the headline rests on MAP-1.**
Both mappings put the same 17 surahs in LEGAL. The difference is entirely the UNIV pole: MAP-2 adds
the polemical surahs, and `P_UNIV` goes from **3 to 23**. Descriptively — and this is post-hoc,
not registered — polemic is *partitive* discourse: it sorts people into groups, *baʿḍuhum … wa-baʿḍuhum*.
Eschatology, exhortation and admonition address the undivided set. Whether that reading is right or
not, the arithmetic fact stands: **adding polemic to the universal pole multiplies its partitive
count by nearly eight and the contrast stops clearing.**

### 5.2 The addressee arm points the same way and does not clear (cells 5, 6)

ARM 2 uses no genre labels at all — only the Qurʾān's own vocative. Both cells carry the locked
sign (LOR −1.1946 and −0.7860, Fisher 2.3×10⁻³ and 2.0×10⁻²) and neither clears α at its worst
channel (0.06059, 0.09579).

> **These two cells are contaminated by my own error and must be read as weaker evidence than cells
> 1–4.** Pre-registration §9-D1 records it: my second smoke test was rebuilt from changed source and
> I dropped the ARM-2 pole scramble, so four ARM-2 *window* robustness cells ran on real poles and
> their line was in the console output I read. **I saw the sign and rough magnitude of the ARM-2
> contrast before locking.** It was disclosed in the pre-registration *before* the lock, no
> parameter changed afterwards, and ARM 1 is clean — genre labels were scrambled in both smokes.
> But the disclosure travels with the cells it affects, which is here.

### 5.3 The MDEs, and why two of the four are worthless

Every NULL states its MDE per cross-finding-029 §3.2.

| cell | MDE at 80 % power | usable? |
|:--|:--|:--|
| 3 | 1.1 | **no — see below** |
| 4 | 1.1 | **no — see below** |
| 5 | 3.0 | as a floor only |
| 6 | 4.0 | as a floor only |

**The MDE procedure I pre-registered is wrong, and I am reporting it rather than patching it.** It
binomially thins the **observed** LEGAL counts, so every simulated dataset carries the observed
effect *multiplied by* the injected one. Reported power is therefore an over-estimate and the
reported MDE an under-estimate. It also runs on the **C0** null while the decision rule uses the
**worst** channel, so it does not describe the rule that produced the NULL at all.

- **Cells 3 and 4 return MDE = 1.1 with power = 1.000 at every one of the nine grid points.** That
  is the signature of the defect, not a finding. **Do not quote those MDEs.** Their NULL is not a
  power failure; it is C3 (§6.2).
- **Cells 5 and 6's MDEs are floors.** The true values are **at least** 3.0 and 4.0. Against this
  corpus's strongest surviving law — a rate ratio of 1.27–2.58 — both are **underpowered against
  the effect scale the corpus actually produces**. Their power curves rise sanely (cell 5:
  0.005 at OR 1.3, 0.419 at 2.0, 0.917 at 3.0; cell 6: 0.023 at 2.0, 0.594 at 3.0, 0.935 at 4.0),
  which is why they are reported as floors rather than discarded.

---

## 6. What went against me — at full prominence

### 6.1 The whole ARM-1 contrast pivots on three tokens

`P_UNIV = 3`. Across the entire 42-surah universal register there are **three** *baʿḍ* tokens:

- **Q 52:25** — وأقبل بعضهم على بعض يتساءلون — *two* tokens, the two halves of one reciprocal
  frame ("they turn to one another, questioning"), which is arguably not a partitive quantifier at
  all.
- **Q 69:44** — ولو تقول علينا بعض الأقاويل — one genuine partitive.

So the universal register contains *baʿḍ* in **two verses of the Qurʾān**, and exactly **one**
unambiguous partitive. Haldane's +½ is doing real work in the denominator. This is the single
largest threat to the finding and no amount of p-value repairs it.

Two pre-registered robustness arms attack it directly and both survive, though neither may carry a
verdict:

| arm | what it fixes | LOR | p_worst | Fisher |
|:--|:--|--:|--:|--:|
| RT-A2 (adds 677 `min`-definite proxy tokens) | removes the small-cell problem entirely | −1.5504 | 0.00110 | 4.5×10⁻⁷ |
| RT-B2 (verse-presence; collapses the Q 52:25 reciprocal) | removes the reciprocal idiom | −2.3609 | 0.00120 | 2.7×10⁻⁵ |
| both together | both | −1.2872 | 0.00380 | 3.0×10⁻⁵ |

That is the strongest thing that can be said in the finding's favour, and it is still robustness,
not verdict.

### 6.2 The mean-verse-length control is nearly saturated — and it is the deciding parameter for MAP-2

Post-hoc diagnostic, written to `runs/h-new-3080/POSTHOC-20260809T081641Z-strata-occupancy/`,
computed after the run and changing no verdict.

Under **both** maps, all 17 LEGAL surahs sit in the **top two** mean-verse-length quintiles and
**none** in the bottom three — LEGAL-per-stratum `[0, 0, 0, 7, 10]`.

| map | C3 stratum sizes | LEGAL per stratum | exact distinct arrangements | distinct sampled in 10,000 draws |
|:--|:--|:--|--:|--:|
| MAP-1 | 12, 12, 12, 12, 11 | 0, 0, 0, 7, 10 | **8,712** | 5,906 |
| MAP-2 | 11, 11, 10, 11, 10 | 0, 0, 0, 7, 10 | **330** | 330 |

MAP-2's top quintile is **10 of 10 LEGAL** and therefore **frozen** — those ten labels are never
permuted. Only `C(11,7) = 330` arrangements exist in the entire C3 null. For contrast, the same
maps' C1 nulls admit 3.4×10⁷ and 1.1×10⁸ arrangements, and C2 nulls 4.3×10⁹ and 8.8×10⁹.

**The pre-registered degeneracy floor was 100 distinct label vectors and 330 did not trip it.**
That floor is the deciding parameter for the MAP-2 arm:

- had the floor been **500**, C3 would have been excluded and **cell 3 would have flipped to PASS**
  (max of C0/C1/C2 = 0.00260 < α);
- **cell 4 would still be NULL** (0.01370 > α).

The floor was fixed before any computation and is honoured as written. But a reader is entitled to
know that MAP-2's verdict was set by a 330-point null in which more than half the treated units
were held constant. **Two readings follow and both are true.** (i) The register grouping is very
heavily confounded with mean verse length — that is what ρ = +0.78 and `[0,0,0,7,10]` mean, and it
is the honest headline about the data. (ii) MAP-1's cell 1 clears α **at C3 anyway**, p = 0.00070
against its own 8,712-arrangement null, so the primary contrast survives a nearly-saturated length
control.

### 6.3 The per-surah secondary is UNINFORMATIVE BY CONSTRUCTION and is not support

It must not be read as a non-significant trend.

| map | eligible surahs (`U+P ≥ 5`) | of which UNIV | mean difference | Mann–Whitney | C0 | C1 | C2 | C3 | p_worst |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| MAP-1 | **10** | **2** | −3.2637 | U = 0 | 0.0213 | 0.2454 | 0.2441 | **1.0000** | **1.0000** |
| MAP-2 | 12 | 4 | −1.7304 | U = 0 | 0.0022 | 0.0573 | 0.0270 | 0.3336 | 0.3336 |

**Two surahs.** Quintile stratification over ten units with two in the treated group leaves
essentially no permutation freedom, which is what a p of exactly 1.000 means. The direction is
consistent — perfect separation, U = 0 — and that is all that can be said. The reason for the
thinness was known and pre-registered: 41 surahs contain no *kull*, 76 contain no *baʿḍ*, 40
contain neither, and only 40 of 114 reach `U + P ≥ 5`. That is why the pooled 2×2 is primary.

### 6.4 The unit-drift-flagged density view, reported because it exists

Both screens fire on this statistic; it is never a verdict input. It is included because a reader
will otherwise compute it themselves.

| map | pole | *kull* / 1000w | *baʿḍ* / 1000w | words |
|:--|:--|--:|--:|--:|
| MAP-1 | LEGAL | 1.533 | 2.909 | 25,438 |
| MAP-1 | UNIV | **3.737** | **0.415** | 7,226 |
| MAP-2 | UNIV | 3.626 | 1.986 | 11,583 |

Both poles move in the locked direction: *kull* is 2.4× denser and *baʿḍ* 7.0× sparser in MAP-1's
universal register.

### 6.5 A coverage number moved when the rule was written down

A first pass at ARM 2 coverage, run before the block rule was committed to prose, treated the four
non-*āmanū* `alladhīna` vocatives as delimiters and returned 926 COMMUNITY verses rather than 939.
Disclosed in pre-registration §9-B4 before the lock, and the runner now asserts the locked integers.

---

## 7. Gates, and the verdict-rule diff

**The verdict-rule diff was run and is reported rather than assumed**, because a CONFIRMED with 2 of
6 cells clearing is the exact shape of the H-NEW-2600 failure of 2026-08-07, where a script
implemented something looser than its pre-registration's gate and published a verdict that failed
it. `verdict_finding()` and `verdict_cell()` in `scripts/h-new-3080.py` were compared line by line
against pre-registration §7.2 and §7.3. **§7.3 makes CONFIRMED conditional on cell 1 PASS and cell
2 PASS and on nothing else**; cells 3–6 are same-status family members for multiplicity and carry
no headline authority, and §7.3 says explicitly that they "may not create" a verdict. Cell 1
p = 0.00080 and cell 2 p = 0.00150, both under α_Bonferroni = 0.0083333. **The rule is honoured as
written.**

That diff was performed *before* the run and it caught three genuine mismatches, all fixed pre-lock:
a missing `+CELL-2-REVERSED` branch in §7.3, three RNGs where the pre-registration said one, and a
per-surah secondary that was missing the four channel nulls §7.5 requires.

Other gates: pre-registration SHA-256 embedded as a literal and verified at runtime with
`SystemExit` (the failure path was tested); `scripts/verify-prereg-locks.sh` reports **19 locks,
0 broken**; `os.makedirs(exist_ok=False)` and every file opened `'x'`; no run directory deleted;
direction locked from §7's classical source before any computation; runtime assertions on the
pre-registered census (359 / 238 / 215 / 200 and 157) and on the five ARM-2 block integers
(23 / 89 / 38 / 489 / 939); all six cells carry the locked sign, so there is no pre-commit
violation anywhere in the family.

---

## 8. The classical anchor — one verified, one declared unverified

**UNVERIFIED ANCHOR, stated as such.** The frontier map names al-Shāfiʿī's *Risāla* and
al-Ghazālī's *Mustaṣfā* as the *uṣūl* anchor for `ʿumūm` / `khuṣūṣ`. **Neither is on disk**, a
separate census lane confirmed their absence, and **no page, chapter, bāb or section of either is
cited in this finding or in its pre-registration.** Two wrong *nawʿ* citations of a single *Itqān*
passage were found in this repository on 2026-08-09; this is not a third.

**VERIFIED ANCHOR, read directly, with line numbers.**
`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`. The *nawʿ* number is derived
from the locator's own header text, not typed beside it.

- **line 14254** — `### | النوع الخامس والأربعون: في عامه وخاصه`. The ordinal in the header is
  *al-khāmis wa-l-arbaʿūn* = **45**.
- **lines 14255–14256** — the definition, and the warrant for the instrument:
  «العام لفظ يستغرق الصالح له من غير حصر وصيغته "كل" مبتدأة … أو تابعة …» — *the ʿāmm is an
  expression that exhausts what it applies to without limit, and its form (ṣīgha) is «kull»*.
  **al-Suyūṭī names *kull* as the paradigm form of ʿumūm.** The pole is his, not mine.
- **lines 14277–14281** — al-Bulqīnī: a general that *remains* general is *ʿazīz*, rare.
- **lines 14282–14284** — al-Zarkashī in *al-Burhān*, to the contrary: it is frequent, e.g.
  *{wa-anna Allāha bi-kulli shayʾin ʿalīm}*.
- **lines 14285–14287** — al-Suyūṭī's resolution, which is the hypothesis stated classically:
  «قلت: هذه الآيات كلها في غير الأحكام الفرعية فالظاهر أن مراد البلقيني أنه عزيز في الأحكام
  الفرعية» — *these verses are all in matters other than branch-legal rulings, so what al-Bulqīnī
  means is that it is rare in the branch-legal rulings*. He then reports hunting for a single legal
  verse with no specification at all.

**A stated limit on the instrument, not discovered afterwards.** Lines 14257–14274 list the *other*
ʿumūm forms — `alladhī`/`allatī` with their duals and plurals, `ayy`/`mā`/`man`, the annexed plural,
the `al`-definite, the annexed generic noun, and the indefinite under negation, prohibition,
condition or *imtinān*. A maximal instrument would use all of them. This one does not, because they
are ambiguous between generic and specific reference in ways `kull` is not. **This is a test of
*kull*-marked ʿumūm, not a test of ʿumūm.**

---

## 9. What this settles, and what it queues

**Settles.** F-14's named confound is real and points the wrong way: the *kull*/*baʿḍ* contrast is
not formulaic, and the map's CBM prior is refuted. `ethical-universalism.md` has its first
quantitative handle — in the register it describes, the universal quantifier outweighs the partitive
by an odds ratio near 15, and the partitive is very nearly absent.

**Does not settle.** Whether the contrast is a property of *register* or of *verse length*. ρ = +0.75
between mean verse length and the LEGAL indicator, with all 17 LEGAL surahs in the top two
quintiles, is close to the grouping itself; cell 1 survives that control, but the control is
nearly saturated (§6.2). Nor whether the result generalises past the MAP-1 pole definition — MAP-2
does not support it.

**Queues, in priority order.**

1. **Replicate at pericope or verse scale, where the length confound is not the grouping.** This is
   the one test that would separate register from verse length, and it is also the scale at which
   al-Suyūṭī's own claim (§4, the wrinkle) can finally be adjudicated.
2. **A partitive pole that does not rest on three tokens.** RT-A2's 677-token proxy already shows
   the effect survives a larger pole; a properly disambiguated *min al-tabʿīḍiyya* set would make
   that a verdict rather than robustness.
3. **Re-run ARM 2 uncontaminated**, by a lane that has not seen §5.2's numbers.
4. **Fix the MDE procedure repo-wide.** Thinning observed counts inflates power in *any* finding
   that uses this pattern; a null-calibrated baseline is required. This is a methods defect, not a
   defect of this finding alone.
5. **Raise the degeneracy floor, or replace it with a floor on the *fraction* of units free to
   permute.** A count of 100 distinct vectors did not catch a null in which 10 of 17 treated units
   were frozen.

---

## Sources

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-3080-quantifier-scope.md`
  (SHA-256 `2e2cde58e7fc2e66f34d27d007c3ed8be19d6eeb30550c6a88ec24f7cc4443e4`)
- Runner: `findings/phase-b-hypotheses/scripts/h-new-3080.py`
  (SHA-256 `be392cd3a1424984bc6f74432674efbcf2bc75082ddebcf5ae807ea3d0a0561d`)
- Run: `findings/phase-b-hypotheses/runs/h-new-3080/20260809T080957Z/`
  (`manifest.json`, `results.json`, `verdict.txt`)
- Post-hoc strata diagnostic:
  `findings/phase-b-hypotheses/runs/h-new-3080/POSTHOC-20260809T081641Z-strata-occupancy/`
- Data: `data/morphology/quranic-corpus-morphology-0.4.txt`
  (`a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46`);
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`
  (`16ec35b2793922bd007767ccddfb6d7aeb5ca53e48394792984f88b49164572a`);
  `data/hafs-verse-counts.tsv`
  (`e1818fb04ac26b863ce1ade50193390d481345a3971919aeb120daf8946212ba`)
- Classical, read: `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`
  lines 14254–14287 (*nawʿ* 45, *fī ʿāmmihi wa-khāṣṣihi*)
- Classical, UNVERIFIED and uncited: al-Shāfiʿī *al-Risāla*; al-Ghazālī *al-Mustaṣfā* — not on disk
- Frontier item: `HANDOFF/FRONTIER-MAP-2026-08-07.md:154` (census) and `:324-330` (F-14)
- Method: `findings/UNIT-DRIFT-DEFECT.md`;
  `findings/phase-b-hypotheses/cross-finding-029-the-deciding-parameter.md`;
  `findings/ABSENCE-CLAIMS.md`
- Siblings: `h-new-3070-deictic-gradient.md` (F-4 CBM prior refuted the same day);
  `h-new-3010-conditional-register.md`; `h-new-3040-modality-axis.md`;
  `h-new-2800-legal-formulae.md` (formula-census precedent)
- Incidental prior count corroborating the census:
  `findings/phase-b-hypotheses/word-pair-lemma-counts.csv` rows 28, 55, 67
