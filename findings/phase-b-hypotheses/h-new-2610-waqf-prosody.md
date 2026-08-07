---
id: H-NEW-2610
title: The Sajāwandī waqf grades — a boundary hierarchy visible only in the channel that shares the grammarian's ancestry
date: 2026-08-07
author: Waiel Al-Shujaa
status: H1a NULL (the new information) · H1b PASS but RECLASSIFIED as the second-tuple replication H-NEW-2560 queued — not independent support · H2 NULL and INSTRUMENT-FAILED · H3 PASS but reducible to verse length
prior_art: H-NEW-2560 H5 + R9 — discovered after this file's pre-registration was locked and both runs completed; §0.5 discloses it and retracts two claims
prereg: prereg-h-new-2610-waqf-prosody.md
prereg_sha256: d776473ea75dd6500ac4c204ac47fce534e59ab7de78caefac2b963746891b80
run: runs/h-new-2610/20260807T010205Z/ and runs/h-new-2610/20260807T010933Z/ (both retained, result.json byte-identical)
seed: 20260509
seed_replication: 20260519
family: WAQF-2026-08-07-A
---

# H-NEW-2610 — The waqf grades, measured

**Verdict in one line: the marks land at real boundaries with enormous selectivity, but
the *grade ordering* among them is recovered only by the dependency treebank — the one
instrument that inherits al-Sajāwandī's own grammatical tradition. The annotation-free
instrument returns a flat null, and the prosodic hypothesis that would have made this
interesting is doubly null.**

> **Correction notice (2026-08-07), issued after both runs completed.** A parallel test,
> **H-NEW-2560**, landed with a waqf arm I did not know about when I locked this
> pre-registration. It had already published the monotone grade ladder, and it had
> already discovered the text-file divergence I present in §7. **Two claims in the
> original version of this file are retracted below, and H1b is demoted from an
> independent result to a replication.** §0.5 is that disclosure. Nothing was changed to
> make this finding look better; every correction weakens it.

This is the first test in this project to treat the waqf marks as data. Every prior
test stripped them. `grep -rlE '06[Dd][6-9ABCabc]'` over `scripts/` and
`findings/phase-b-hypotheses/scripts/` returns **41 files when I ran it — 40 excluding
this test's own script**; `HANDOFF/FRONTIER-MAP-2026-08-07.md` counted 39, and the
difference is scripts added since (h-new-2570 and this one). In every prior case the
range sits inside a stripping regex. `findings/phase-b-hypotheses/scripts/h-new-2490.py`
line 52 is the clearest: `PAUSE = set(chr(c) for c in range(0x06D6, 0x06EE))`, defined
under the comment *"locked PAUSE set: waqf / codex annotation glyphs U+06D6..U+06ED"*
and used only by a `norm()` that removes them.

Pre-reg SHA-256 `d776473e…891b80`, runtime-verified. 10,000 permutations per null,
seeds 20260509–20260514, replications at +10. Family of **8** registered inferences;
Bonferroni α = 0.00625, project novelty rule stricter, so the **raw decision gate is
0.000625**.

---

## 0. What these marks are, before any number

The four glyphs are a **twelfth-century editorial layer**. They descend from
**al-Sajāwandī (d. 560/1165)**. They are **not part of the revealed text** — the
consonantal rasm carries none of them, and neither do the earliest muṣḥafs. Nothing
below claims otherwise. Every result here is a result about **a reciting tradition's
analysis of the text**, not about the text.

The pre-registration's own §1 said plainly that a positive H1 was close to guaranteed a
priori: a grammarian who analyses clause boundaries and then prints symbols at them
will of course produce symbols correlated with clause boundaries. H1 was registered as
*calibration*, not discovery. That framing is what makes the actual result readable.

### 0.1 Classical anchor — verified, and the project's own citation corrected

`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` line 5092:
`### | النوع الثامن والعشرون: في معرفة الوقف والابتداء`.

**The brief and `HANDOFF/FRONTIER-MAP-2026-08-07.md` both cite *al-Itqān* nawʿ 27. In
the recension on disk it is nawʿ 28**, because that recension merges nawʿ 22–27 under
a single heading at line 4631. I cite the number I verified and make no claim about
editions I did not open. **al-Sajāwandī's own *ʿIlal al-wuqūf* is not on disk**;
everything here is mediated by al-Suyūṭī.

Line 5147, al-Suyūṭī quoting al-Sajāwandī directly:

> وقال السجاوندي: الوقف على خمس مراتب: لازم، ومطلق، وجائز، ومجوز لوجه، ومرخص ضرورة.

Five **marātib** — ranks. **The ordinality tested here is al-Sajāwandī's own claim, not
an imposition of mine.** And his definitions, as al-Suyūṭī reports them, fix the two
anchor rungs:

- *lāzim* — `ما لو وصل طرفاه غير المراد`, "that which, if its two sides are joined, is
  not the intended meaning." His worked example is `{وما هم بمؤمنين}` before
  `{يخادعون الله}` (Q 2:8→9): joined, *yukhādiʿūna llāha* would read as an adjective
  qualifying *muʾminīn*, and the deceit would be negated along with the belief.
- *jāʾiz* — `ما يجوز فيه الوصل والفصل لتجاذب الموجبين من الطرفين`, "joining and
  separating both permitted, because the two sides pull against each other."
  **Definitionally the balance point** — which is what licenses putting *al-waqf awlā*
  above it and *al-waṣl awlā* below it.

The printed glyph inventory is **not** a one-to-one rendering of those five ranks;
`صلى` and `قلى` are terms of the later muṣḥaf-printing tradition. Stated in the pre-reg
before computing, restated here.

---

## 0.5 Prior art — H-NEW-2560 H5 and R9, and what it costs this finding

**This section was written after both runs completed. It is a post-run disclosure, not a
pre-registration amendment, and it is dated and labelled as such.** The reason the
pre-registration itself was left untouched is given in §9.1b.

`prereg-h-new-2560-fasila-clause-seal.md` (SHA `4432e6fa…`) tested the fāṣila as a clause
seal against EQTB. Its **H5** arm is a classical waqf validation, and its **R9**
robustness item is the full grade ladder. I verified every number below against
`runs/h-new-2560/20260807T004157Z/result.json` rather than accepting them as reported.

**H5 as computed:** STOP-PREFERRED (*mīm* + *qlà*, n = 625) vs CONTINUE-PREFERRED
(*ṣlà* + *lā*, n = 1,749); Δ = **+0.16918**; null mean Δ = 0.00016;
p = 9.999×10⁻⁵, Bonferroni 5.999×10⁻⁴; replicated at seed 20260511, p = 9.999×10⁻⁵;
sealed-rate continue-preferred = 0.73642, stop-preferred = 0.9056. All confirmed.

**Critically, `SEALED(k)` is defined at `prereg-h-new-2560` line 174 as `CROSS(k) == 0`.
2560's `CROSS` is my `XC`. We are using the same instrument** — theirs binarised at zero
and contrasted across a binary class split, mine as a continuous count in a rank
correlation across four ordered grades.

### Retraction 1 — the monotone ladder was already published

2560's R9, at `h-new-2560-fasila-clause-seal.md` lines 82–96, tabulates mean crossing
arcs for every grade and states in terms: *"The ordering is monotone across the entire
classical ladder."* Its column reads **0.103 → 0.136 → 0.193 → 0.306 → 0.662 → 1.000**
(qlà, mīm, jīm, ṣlà, lā, muʿānaqa).

**My H1b is therefore not the first observation of the ordering.** What is genuinely mine
is narrower: 2560 registered R9 as *"descriptive; no p-values, no addition to k"*, so the
monotonicity was never **tested**. H1b supplies the direction-locked, two-null, gated
test. That is a real but modest increment, and it is all I claim.

### Retraction 2 — the text-file divergence was already found, and found first

§7 of the original version of this file said the divergence was something *"nobody in
this project had noticed."* **That is false and is withdrawn.**
`h-new-2560-fasila-clause-seal.md` lines 330–352 already tabulate all three variants,
already state that `quran-full-tashkeel.json` contains **zero** *lā* marks, 92 fewer
*qlà* and 111 more *jīm*, and already label H5 **SINGLE-TUPLE** on that basis. 2560 found
it first and disclosed it against its own result. §7 below is rewritten accordingly.

### What H1b actually is: the replication 2560 declared required

2560 used **`quran-text/quran-no-tashkeel.json`** (`h-new-2560.py:453`, SHA
`253f72f3…`) — a **third** text file, distinct from both of mine. It closes with:
*"A second-tuple replication is queued as required work, not optional."*

**H1b is that replication.** Cross-tuple comparison of mean crossing arcs:

| grade | H-NEW-2560 (no-tashkeel) | **H-NEW-2610 (full-tashkeel)** |
|:--|--:|--:|
| ۗ qlà | 0.1028 (n=603) | **0.0744** (n=511) |
| ۘ mīm | 0.1364 (n=22) | **0.0952** (n=21) |
| ۚ jīm | 0.1927 (n=1,972) | **0.1506** (n=2,083) |
| ۖ ṣlà | 0.3058 (n=1,681) | **0.2679** (n=1,651) |
| ۙ lā | 0.6618 (n=68) | **absent from this file** |

**The ladder survives the second tuple.** Same ordering, same upward break at *mīm*,
uniformly lower absolute values. 2560's H5 can be relabelled from SINGLE-TUPLE to
two-tuple-replicated on the strength of this — which is the most useful thing this
finding does for the project.

### Consequences, applied

1. **H1b is reclassified as a replication and is NOT citable as independent support**
   for the proposition that the waqf grades track syntactic boundary strength. It
   corroborates 2560 H5/R9 on a second tuple; it does not add an independent confirmation.
2. **The Bonferroni family stays at k = 8.** Dropping H1b would raise the raw gate from
   0.005/8 = 6.25×10⁻⁴ to 0.005/7 = 7.14×10⁻⁴ — a **loosening**, which this project
   requires be ratified rather than self-applied. Keeping H1b in the family is the
   conservative choice and it costs the other arms nothing they did not already survive.
3. **H1a and H2 are untouched by 2560 and are where this finding's information now
   sits.** 2560's entire six-inference family is EQTB-based: it has no annotation-free
   channel and no phonological outcome. §3's null and §5's double null are new, and the
   contrast between them and H1b is sharper for the prior art, not weaker — 2560 showed
   the marks agree with a dependency parse; this file shows they do **not** order on a
   parse-free boundary proxy, and carry no rhyme information once syntax is fixed.
4. **H3 measures a different quantity** from 2560's H2 and is not superseded — see §6.

---

## 1. Results

| | instrument | locked direction | observed | Null A | Null B | verdict |
|:--|:--|:--:|--:|--:|--:|:--|
| **H1a** | verse-boundary resemblance (**annotation-free**) | ρ > 0 | **ρ = −0.0075** | p = 0.691 | p = 0.410 | **NULL** |
| **H1b** | EQTB dependency arc-crossing | ρ < 0 | **ρ = −0.1564** | **p = 9.999×10⁻⁵** | **p = 9.999×10⁻⁵** | **PASS** |
| **H2** | rhyme match \| syntax held fixed | T > 0 | T = +3.4×10⁻⁴ | p = 0.458 | p = 0.405 | **NULL + INSTRUMENT-FAILED** |
| **H3** | mark density × register (JT trend) | eschat < narr < legal | **JT = 2361** | **p = 9.999×10⁻⁵** | **p = 9.999×10⁻⁵** | **PASS, but see §5** |

All four replications at seeds +10 agree with their primaries to the same decision.
Both H1b and H3 sit at the Monte-Carlo floor under both nulls and both replications.

---

## 2. The calibration ladder — the most important number in this finding

Mean values by juncture type. This is descriptive and was registered as such
(prereg §8.1), and it carries more information than any p-value here.

| juncture type | n | VBR (annotation-free) | arc-crossing XC | rhyme-match rate |
|:--|--:|--:|--:|--:|
| **āya boundary** | 6,235 | **−1.727** | — | — |
| ۖ ṣlà — *waṣl awlā* | 1,651 | −4.858 | 0.2679 | 0.0369 |
| ۚ jīm — *jāʾiz* | 2,083 | −4.852 | 0.1506 | 0.0442 |
| ۗ qlà — *waqf awlā* | 511 | −5.010 | 0.0744 | 0.0333 |
| ۘ mīm — *lāzim* | 21 | −5.424 | 0.0952 | 0.0476 |
| ۜ saktah *(excluded)* | 5 | −5.275 | 0.4000 | — |
| ۛ muʿānaqa *(excluded)* | 6 | −6.165 | 0.6667 | — |
| matched random control | 4,266 | −7.187 | 1.3542 | 0.0631 |
| **all unmarked junctures** | 66,918 | **−7.203** | **1.3720** | 0.0670 |

**Read the extremes, not the middle.** Pooling all 4,266 marked loci: mean XC =
**0.1866** against **1.3720** at unmarked junctures — **7.35× fewer dependency arcs
crossing** — and mean VBR = **−4.876** against **−7.203**, i.e. **2.33 nats** closer to
āya-edge behaviour. On both instruments the marks land, overwhelmingly, at genuine
boundaries, and they sit squarely between an ordinary word juncture and a verse end.
**That placement fact is large, robust, and visible in both channels.**

What is *not* large is the ordering **among** the four grades. On the annotation-free
instrument the whole grade range spans 0.57 nats against a 5.5-nat gap from unmarked to
āya-edge — about 10% of the ladder.

*(Instrument gap, disclosed: XC is not reported for āya boundaries. The arc-crossing
instrument is defined over the verse-internal juncture list and verse boundaries were
never entered into it. That row is blank because it was not computed, not because it
was zero.)*

---

## 3. H1a — NULL. The annotation-free instrument does not order the grades

**ρ = −0.0075** over 4,266 loci. The locked direction was ρ > 0. **Direction not
supported, and the magnitude is indistinguishable from zero** (p = 0.691 under free
permutation, 0.410 under within-sūra permutation; replications 0.690 / 0.402). Dropping
the thin *lāzim* rung changes nothing: ρ = −0.0061 over 4,245 loci.

This is a **NULL**, published with the prominence the protocol requires. It is not a
dramatic reversal — it is a flat line.

**But the sub-pattern is worth recording, and it runs against my lock.** The ungated
pairwise contrasts:

| contrast | Δ mean VBR |
|:--|--:|
| ṣlà → jīm | **+0.006** (tied) |
| jīm → qlà | **−0.158** |
| qlà → lāzim | **−0.414** |

The upper three rungs decrease monotonically in verse-boundary resemblance as
stop-strength rises. The omnibus rank correlation washes out because ṣlà and jīm are
**87.5%** of the loci and are effectively tied.

**A post-hoc reading, labelled as such and not tested here.** al-Suyūṭī's own
definition of *lāzim* is that joining the two sides *yields the wrong meaning* — which
is to say the juncture **looks joinable**. That is exactly why a reader must be warned.
Symmetrically, *waṣl awlā* is placed where a reciter would be **tempted** to stop, i.e.
where the surface *does* look boundary-like, in order to tell them not to. On that
reading the marks are concentrated where surface cues **mislead**, and a surface-cue
instrument should order them backwards. This is a hypothesis generated by looking at
the result. It carries an MW-7 single-test ceiling, it is not a finding, and it should
be settled by a fresh pre-registration, not by this file.

---

## 4. H1b — PASS, and why that is the weakest kind of pass

**ρ = −0.1564**, both nulls at the Monte-Carlo floor 9.999×10⁻⁵ (Bonferroni 7.999×10⁻⁴,
gate 6.25×10⁻⁴), both replications identical. Direction matched the lock. Monotone
across the three well-powered rungs: **0.268 → 0.151 → 0.074** crossing arcs for
ṣlà → jīm → qlà. *lāzim* rises slightly to 0.095 on n = 21.

**Reclassified per §0.5: this is the second-tuple replication of H-NEW-2560 H5/R9, not
an independent result.** 2560 published the same ordering on a different text file and
had already declared this replication required work. What H1b adds is the gated test of
monotonicity that 2560 explicitly declined to run, and the demonstration that the ladder
survives the full-tashkeel inventory.

**Beyond that, it must not be read as independent confirmation of anything about the
text, and the pre-registration said so before the number existed (§1.2, §7.1).**

Two reasons, one checked and one uncheckable:

1. **Contamination — the checked part.** Per `h-new-2540-form-v-valency.md` §7.2,
   EQTB's syntax was initially generated by a BiLSTM parser fed POS tags and
   morphological-feature embeddings, with non-blinded human validation. For *this*
   question the machine pathway is absent: waqf marks are not QAC features and were not
   parser inputs. I did not assume that — **I counted every character of EQTB's
   `uthmani_token` and `imlaai_token` columns across all 128,219 real token rows: the
   U+06D6/06D7/06D8/06DA glyphs appear zero times.** The only waqf-range glyph anywhere
   is U+06DC (saktah), twice. EQTB's working text does not display the pause grades.
2. **Common ancestry — the uncheckable part, and the one that matters more.**
   al-Sajāwandī and every modern Arabic treebank annotator inherit the same
   Baṣran/Kūfan grammatical tradition. EQTB's own sentence segmentation — 11,693
   sentences over 6,236 verses, both splitting verses (max 23) and spanning them (max
   31) — is an editorial judgment of clause structure made by people trained in that
   tradition. **No permutation test can separate "both are right about the text" from
   "both apply the same grammar."**

**The structural point, and it is the finding's sharpest.** H-NEW-2540 was rescued by
its parser-free channel (§2b there): the effect survived when the outcome was moved off
parser output. **Here the polarity is inverted.** The parser-free channel is the one
that returns null; the surviving effect lives entirely in the annotation. By the exact
standard H-NEW-2540's audit established, H1b is the kind of result that should be
distrusted, and I am recording it as such rather than banking it.

---

## 5. H2 — the prize. Doubly NULL, and the instrument failed its own gate

**H2 was the hypothesis worth running this test for**: does grade predict a
*phonological* property — whether the pre-pause word rhymes with the sūra's fāṣila
class — once the syntactic boundary is held fixed? Syntax is what a grammarian
analyses; the sound of the word before the stop is not.

**Two independent reasons it returns nothing.**

### 5.1 The pre-registered instrument control FAILED, and I am honouring it

Pre-reg §5.3 set an abort condition **before computing**: recompute each sūra's
dominant fāṣila class with the ported `classify()` and compare against the frozen
`h-new-2240.json`; if agreement < 90% of 114 sūras, H2 is **NULL-INSTRUMENT-FAILURE**
and its p-values are not interpreted.

**Agreement came in at 100/114 = 87.72%.** Below the threshold. **H2 is therefore
declared NULL-INSTRUMENT-FAILURE by my own lock, and I have not moved the threshold.**

The 14 disagreeing sūras: **11, 12, 14, 22, 24, 31, 34, 35, 42, 49, 57, 60, 64, 88.**
The cause is explicable and is not a coding error: H-NEW-2240 computed its dominant
classes on **min-tashkeel**, where long vowels are written as full letters, while this
test computes the pre-pause word's class on **full-tashkeel**, where some are written
as superscript/small letters that the ported `STRIP_MARKS` removes. The outcome
variable therefore mixed two orthographic conventions — **which is precisely what the
control was built to catch. The control worked.**

### 5.2 The corrected post-hoc variant is also null

Because suppressing the number would be worse than reporting it, I added a
**post-hoc** variant *after* seeing the control fail: both sides of the rhyme
comparison computed from full-tashkeel by the same function, removing the mismatch.
**MW-7 applies — single-test α ceiling 0.05, no replication, not gated, and it cannot
rescue H2.**

| | T | Null A | Null B |
|:--|--:|--:|--:|
| H2 as registered *(instrument failed)* | +3.41×10⁻⁴ | 0.458 | 0.405 |
| H2 post-hoc self-consistent | +1.83×10⁻⁴ | 0.491 | 0.430 |

Both null. **The instrument failure did not conceal a real effect.**

### 5.3 The marginal association runs the wrong way too

From §2: the rhyme-match rate pooled over all 4,266 marked junctures is **0.0401**
(range 0.0333–0.0476 across the four grades), against **0.0670** at unmarked
verse-internal junctures and **0.0631** at the matched random control. Waqf marks land
on words *less* likely to carry the sūra's fāṣila rhyme than chance. Whatever governs
mark placement, it is not attraction to the rhyme.

**Conclusion, and it is the honest one: under this instrument the marks are competent
syntactic commentary and nothing more.** Per pre-reg §7.1 the verdict language is
**`HIERARCHY CONFIRMED (contaminated channel); MARKS ARE SYNTACTIC COMMENTARY`** — with
the further demotion that the hierarchy failed in the clean channel.

The alternative syntactic control (EQTB sentence-boundary status instead of
arc-crossing strata; prereg §8.7) gives T = 7.07×10⁻⁵, also null. 3,315 of 4,261 loci
sit at an EQTB sentence boundary.

---

## 6. H3 — PASS on the locked trend, but it reduces to verse length

Registers reused **verbatim** from `h-new-2530.json` → `h-new-2500.json`
`genre_proxy.members`; the 3-register primary of H-NEW-2530, n = 91 sūras.

| register | n | marks per 100 words |
|:--|--:|--:|
| eschatological_mufaṣṣal | 40 | **1.157** |
| narrative | 31 | **3.693** |
| legal_medinan | 20 | **6.578** |

Jonckheere–Terpstra JT = 2,361 on the pre-committed order. Both nulls and both
replications at the Monte-Carlo floor 9.999×10⁻⁵. **Direction matched. PASS.**
Four-class robustness places liturgical_didactic at 4.493, between narrative and legal.

**And now the honest demotion, which was registered in advance as prereg §8.6.**

`r(density, mean verse length) = **0.913**`. After residualising density on mean verse
length, the register means become **eschatological −0.178, narrative +0.310, legal
−0.123** — no longer ordered, and narrative now sits highest. **Register adds nothing
beyond verse length; the trend is verse length wearing a register label.**

This is the project's **CBM** category — confirmed but reducible. The pre-registration
anticipated exactly this ("length is the hypothesised *mechanism*, so this is reported
as decomposition, not as a competing model"), and the mechanism is the one Ibn
al-Jazarī gives at *al-Nashr* as quoted by al-Suyūṭī (line 5106): the reciter cannot
take a long verse in one breath, so a stopping place must be chosen. **Longer verses
need more pause marks. That is the whole finding, and it is a sensible one — but it is
not a register effect.**

### 6.1 Relation to H-NEW-2560's reversed register arm

2560's H2 locked `eschatological_mufaṣṣal > legal_medinan` in **sealed-rate** and observed
**−0.1948** — a published pre-commit violation, with legal-Medinan sealing far more
(0.8950 vs 0.7002). **That is a different quantity from mine**: 2560 measured how often a
boundary is syntactically closed; I measured how many marks a sūra carries per 100 words.
Neither supersedes the other.

They do point the same way, and the warning landed. Both arms say legal-Medinan is the
register with the most syntactic closure and the most pause guidance, and in both cases
**verse length is the plausible common cause** — 2560's own H3 found sealing rising
monotonically with verse length (0.62 → 0.92), and my §6 finds r = 0.913 between density
and mean verse length. **The honest joint reading is that register is a proxy for length
on this axis in both tests, and that is why 2560's direction reversed.** Anyone locking a
register direction on waqf or sealing data should residualise on length first.

---

## 7. The rules-tuple divergence — **priority corrected: H-NEW-2560 found this first**

**Retraction.** The original version of this section called the divergence something
"nobody in this project had noticed." **That was false.**
`h-new-2560-fasila-clause-seal.md` lines 330–352 had already tabulated all three
variants, already reported that full-tashkeel carries zero *lā* marks, 92 fewer *qlà* and
111 more *jīm*, and already downgraded its own H5 to SINGLE-TUPLE on that basis. Priority
is 2560's. I registered the sensitivity independently in prereg §8.1 before computing,
but independent arrival is not precedence and I am not claiming it.

**Three text files, and full-tashkeel is the outlier.** Counts I verified directly; the
no-tashkeel column is 2560's, re-verified against its `result.json`.

| glyph | full-tashkeel *(this test)* | min-tashkeel | no-tashkeel *(2560)* |
|:--|--:|--:|--:|
| ۖ ṣlà U+06D6 | 1,651 | 1,682 | 1,681 |
| ۚ jīm U+06DA | 2,083 | 1,972 | 1,972 |
| ۗ qlà U+06D7 | 511 | 603 | 603 |
| ۘ mīm U+06D8 | 21 | 22 | 22 |
| ۜ saktah U+06DC | 8 | 7 | 5 |
| ۛ muʿānaqa U+06DB | 6 | 12 | 12 |
| **ۙ lā U+06D9 — *waqf mamnūʿ*** | **0** | **68** | **68** |

**min-tashkeel and no-tashkeel carry essentially the same apparatus** (differing by one
ṣlà and two saktah). **full-tashkeel is the divergent file** — and it is the one the
frontier map verified, the one this test registered as primary, and one of the files
being routinely stripped. Its Sajāwandī apparatus is **incomplete relative to a printed
muṣḥaf**: the strongest continue-preferred grade is simply absent. It also disagrees with
min-tashkeel on word segmentation in 2,721 verses, and with QAC/EQTB in 10.

**What this test contributes here is the second tuple, not the discovery.** The five-rung
sensitivity on min-tashkeel (`lā < ṣlà < jīm < qlà < lāzim`, n = 4,347) gives **ρ = −0.015**
against VBR — the same flat null as H1a, now with the bottom rung present. **The H1a null
is not an artefact of the primary file's missing grade.** And §0.5's cross-tuple table
shows the *dependency* ladder does survive the switch, which lifts 2560's H5 from
SINGLE-TUPLE to two-tuple-replicated.

**Anyone running a future waqf test must choose the file deliberately and say which.**

---

## 8. Honest limits

1. **The marks are not the Quran.** Twelfth-century apparatus over a seventh-century
   text. Every result here describes a reciting tradition's analysis.
2. **H1b, the only hypothesis that passed cleanly, lives entirely inside the
   contaminated channel** (§4). The parser-free channel is null. This is the inverse of
   what rescued H-NEW-2540 and should be weighted accordingly.
2b. **H1b is also not new** — H-NEW-2560 R9 published the same ordering first, on a
   different text file (§0.5). It is a replication with a gated test attached, and it is
   not citable as independent support. I did not know of 2560 when I locked this
   pre-registration; that explains the duplication but does not excuse citing it as novel,
   and §0.5 retracts the two claims that did.
3. **Common grammatical ancestry** between al-Sajāwandī and modern annotators caps H1b's
   meaning regardless of p-value, and no test in this design can address it.
4. **H2's registered instrument failed its own pre-set gate** (§5.1). The post-hoc
   repair is MW-7-capped and also null.
5. **lāzim n = 21.** The top rung is thin, and its XC (0.095) breaks the monotone
   sequence its three neighbours make. Nothing here should rest on it.
6. **The rhyme instrument was built for verse-final words** (H-NEW-2240) and applied
   here to verse-internal ones. Its pausal-rime logic is position-independent by
   construction but was never validated in this position.
7. **Not Quran-specific.** No matched Classical-Arabic corpus carries waqf marks, so
   there is nothing to compare against. Quran-internal throughout; not a full Phase-B
   cross-corpus finding under `docs/statistical-rigor-protocol.md` §3.
8. **The primary text's waqf apparatus is incomplete** (§7).
9. **No human review of any annotation** was performed.
10. **The permutation tests condition on the mark placements as given** and cannot
    detect error, inconsistency, or regional variation in the muṣḥaf's own placement —
    of which there is real historical variation across printing traditions.
11. **Verse-boundary XC was not computed** (§2), so the ladder's top row is incomplete
    on the dependency instrument.
12. **VBR is not "syntax."** It is verse-boundary resemblance — a text-internal
    boundary proxy. The syntactic control in H2 is the dependency arc-crossing count,
    not VBR.

---

## 9. Provenance, and everything added after the lock

- Pre-registration written and SHA-256'd (`d776473e…891b80`) **before any
  grade-to-outcome statistic was computed**. §2 of the pre-reg lists exhaustively what
  was inspected first: glyph census, mark geometry, word-count join integrity, EQTB
  schema, the min/full divergence, the Itqān location, and the h-new-2240 field
  structure. No grade-conditional statistic was among them.
- **Frozen inputs verified by SHA-256 at runtime**, run aborts on mismatch:
  full-tashkeel `382a7341…`, min-tashkeel `87aaab41…`, QAC v0.4 `a1d12923…`, EQTB
  `Quranic.csv` `a303c24c…`, h-new-2240 `cce45861…`, h-new-2500 `a63aef25…`, h-new-2530
  `5ca17050…`. The EQTB archive re-verified to `6ae1da54…` on re-download, matching
  `data/syntax/UD-QURAN-SOURCE.md`.
- **EQTB↔QAC word-count agreement was 100%** (77,429 words, 6,236 verses, zero
  disagreements); the script aborts otherwise. The 10 verses where full-tashkeel
  segments words differently were excluded from the dependency channel, costing **5 of
  4,266 loci (0.12%)**.
- **Two immutable runs, both retained:**
  `runs/h-new-2610/20260807T010205Z/` and `runs/h-new-2610/20260807T010933Z/`.

### 9.0 Two run directories — the H-NEW-2540 §8.1 standing correction, applied

The first run's `manifest.json` recorded an input path containing session-tooling
identifiers, because the EQTB table was read from a scratch location. That is the
**identical situation** that produced this project's run-immutability breach
(`h-new-2540-form-v-valency.md` §8.1), where the response was to re-run and then delete
the first directory — while an audit was reading it.

The standing correction issued after that breach reads: *"A path that cannot be
committed should be handled by re-running to an additional directory and retaining
both, with the reason recorded — not by removing evidence."* **That is exactly what was
done here, and this is the first application of the correction.**

- EQTB copied to a neutral path, SHA re-verified as `a303c24c…` before re-running.
- Second run executed to a **new** directory.
- **Neither directory was deleted.** Both are on disk.
- **Determinism check: `result.json` is byte-identical across the two runs**, SHA-256
  `65118407ce391e7632de86076fabdc90a553078530b6585d12f8e020e8bc7ca9` for both.
- The manifests differ in exactly three fields: `command`, `utc`, and `git_commit`
  (the repository advanced between the two executions; both commits are recorded).

The first run's manifest is the one that cannot be committed as-is. It is retained
anyway, because the audit trail is the thing being protected.

### 9.1 Garden-of-forking-paths log — three changes made after the lock

Recorded because the value of a pre-registration is exactly that deviations are
visible.

1. **Two correctness smoke runs at 200 permutations**, written to a scratch directory
   *outside* `findings/` so that no official-looking run directory was manufactured, and
   both marked `SMOKE_RUN: true` in their own output. I inspected their structural
   fields (join integrity, instrument control, XC distribution, calibration ladder).
   This means **the descriptive ladder and the observed ρ were visible to me before the
   10,000-permutation run**. No gate, direction, seed, statistic or threshold was
   changed as a result. The deterministic statistics are identical across smoke and
   final run by construction; only the p-values differ.
2. **A conformance bug fixed before the final run.** H3's Jonckheere order had been
   taken from `h-new-2530.json`'s `classes` listing (`narrative, legal_medinan,
   eschatological_mufassal`) rather than the pre-registered trend order
   (`eschatological_mufassal, narrative, legal_medinan`). The pre-registration is the
   authority; the script was brought into conformance and now aborts if the label set
   differs from the lock. **No H3 result was banked under the wrong ordering** — the
   only prior evaluation was a 200-permutation smoke run whose p-values were at the MC
   floor of 1/201 and uninterpretable at a gate of 6.25×10⁻⁴.
3. **Two post-hoc diagnostics added after the smoke run**, both explicitly flagged in
   `result.json`: the opposite-tail p-value for H1a/H1b (symmetric, applied to both, not
   selective), and the self-consistent rhyme variant of §5.2 (`POST_HOC: true`,
   `MW7_alpha_ceiling: 0.05`, `gated: false`). Neither rescues anything; both are null
   or irrelevant to the verdicts.

### 9.1b Prior art disclosed after the runs — and why the pre-registration was NOT amended

H-NEW-2560's waqf arm came to my attention **after** this pre-registration was
SHA-locked and **after** both 10,000-permutation runs had completed. The methodological
guidance for this situation is to amend the pre-registration to disclose prior art and
narrow scope, then re-SHA and record both hashes. **I did not do that, and the reason
matters:**

1. **It would break the verification chain.** `EXPECTED_PREREG_SHA` is a fixed literal in
   `scripts/h-new-2610.py` and is checked at runtime with `SystemExit` on mismatch.
   Re-SHA-ing the pre-reg would make both completed runs unreproducible — anyone
   re-running the committed script against the amended file would get an abort, and the
   manifests' recorded `prereg` hash would match nothing on disk.
2. **A pre-registration amended after results exist is not a pre-registration.** The
   whole force of `d776473e…891b80` is that it is provably prior to computation. A file
   that gains a "prior art" section after the numbers are known has lost exactly the
   property it was created to have, however honest the addition.

**So the disclosure lives here instead, in the findings document, dated and labelled as
post-run.** The lock stays intact and provably prior; the correction is visible and
carries its own timestamp. This is the narrower and more conservative of the two options:
it changes no threshold, no direction, no seed and no family size, and every consequence
in §0.5 weakens this finding rather than strengthening it. Recording the departure here
is part of the departure.

### 9.2 Run immutability

Pre-reg §10 restates the standing correction recorded at
`h-new-2540-form-v-valency.md` §8.1: **run directories are never deleted, including
uncommitted or superseded ones.** **No run directory was deleted in the course of this
work** — see §9.0 for the case where the temptation arose and was declined. The two
200-permutation smoke runs are retained at `smoke-2610/20260807T005712Z/` and
`smoke2-2610/20260807T005937Z/` in the scratch area; they are outside the repository by
design, both self-declare `SMOKE_RUN: true`, and they are named here so their existence
is on the record rather than inferred.

---

## 10. Cross-references

- **[[h-new-2560-fasila-clause-seal]] H5 + R9** — **the direct prior art; read §0.5 before
  citing anything in §4.** 2560 published the monotone grade ladder first, on
  `quran-no-tashkeel.json`, and first disclosed the text-file divergence. This file's H1b
  is the second-tuple replication 2560 declared required work, and it succeeds: the
  dependency ladder holds under the full-tashkeel inventory, so **2560's H5 may be
  relabelled from SINGLE-TUPLE to two-tuple-replicated.** Its H2 register arm reversed;
  see §6.1 for why that and my §6 are the same length confound seen from two angles.
- **[[h-new-2540-form-v-valency]] §2b, §7.2** — the methodological parent. That finding
  survived because its parser-free channel replicated the parser channel. **This finding
  is the mirror image and must be read against it**: here the parser-free channel is the
  null one. The comparison is the most useful thing either file offers about how much
  to trust an EQTB-based result.
- **[[h-new-2240-fasila-assonance-taxonomy]]** — supplied the rhyme instrument and, via
  the min/full orthographic divergence, the instrument failure of §5.1. That divergence
  is a live caveat for any future reuse of `per_surah.dominant_class` against
  full-tashkeel text.
- **[[cross-finding-028-formal]] / [[h-new-2530]]** — supplied the register labels
  verbatim. H3 passes the trend but reduces to verse length, so it adds **no** new
  register-coded grammar; it is a length law, and the register partition is a proxy for
  length here.
- **[[h-new-2220]] / [[cross-finding-026]]** — the anti-chiasmus bound. Same shape of
  result: a classically asserted structure survives as *placement* but not as the
  *graded architecture* the tradition describes.
- **The retirement/vindication ledger** — al-Sajāwandī lands on the **partially
  vindicated** side. His marks demonstrably sit at syntactic boundaries (§2), and his
  own claim that they form *marātib* survives in the dependency channel (§4) while
  failing in the clean one (§3). The prosodic claim implicit in the tradition's own
  framing — al-Nakzāwī tying waqf to *al-fawāṣil* — **does not survive** (§5).

---

## 11. What would settle the open questions

1. **A form-blind, mark-blind human annotation** of clause boundaries at a stratified
   sample of the 4,266 loci. It is the only thing that separates "both are right about
   the text" from "both apply the same grammar," and no amount of permutation gets there.
2. **A fresh pre-registration of the §3 misleading-surface hypothesis**, with the
   direction locked the other way and the reasoning stated first. That reading was
   generated by looking at this result and must not be tested on this result.
3. **A repaired H2** in which the sūra dominant class and the pre-pause word class are
   computed from the same file — registered, not post-hoc. §5.2 suggests it will be
   null, which is the reason to register it properly rather than leave it as a
   diagnostic.
4. **A muṣḥaf-source audit** resolving the §7 divergence: which printing tradition does
   each of the three text files follow, and which is authoritative for waqf work. Both
   this test and H-NEW-2560 are now blocked on the same question, and neither can answer
   it from the corpus alone — it needs the muṣḥaf editions themselves.
5. **Not needed any more:** the second-tuple replication of 2560's H5. §0.5 supplies it.
