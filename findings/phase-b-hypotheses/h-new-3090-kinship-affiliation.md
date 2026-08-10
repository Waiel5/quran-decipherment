---
finding_id: H-NEW-3090
title: "F-20 dissolves on its own vocabulary: ikhwa is 6/7 biological, mawla is 11/18 divine — the hypothesis is not testable on these six terms, and the tests that ran are NULL in the wrong direction"
author: Waiel Al-Shujaa
date: 2026-08-09
frontier_item: F-20
prereg: findings/phase-b-hypotheses/prereg-h-new-3090-kinship-affiliation.md
prereg_sha256: c163a0b27c63628a16a313c0d54fab8948dce9d40605036e9bfd12bda76721b8
run: runs/h-new-3090/20260809T080047Z
seed: 20260509
n_perms: 10000
k_bonferroni: 24
alpha_bon: 0.00208333
verdict: NULL (rung 1) — but the primary result is the denotation failure, not the NULL
---

# H-NEW-3090 — kinship vs affiliation across the Hijra

## Abstract

F-20 asks whether biological-kinship terms (*walad*, *raḥim*, *nasab*) and affiliative terms
(*ikhwa*, *awliyāʾ*, *mawlā*) are in complementary distribution across the Hijra. **The answer is
that the question cannot be asked of these six words, because they do not denote what the
hypothesis assumes.**

> ***ikhwa* has 7 tokens in the Qurʾān. Four are Joseph's brothers (Q 12:5, 12:7, 12:58, 12:100).
> Two are inheritance law (Q 4:11, Q 4:176). Exactly one — Q 49:10 — is confessional. The flagship
> "affiliative" term is 6/7 biological.**

The rest of the inventory fails the same way: ***mawlā* is 11/18 a divine epithet** (*Allāhu
mawlākum*), ***walad* is 18/56 the Christological denial** — which this project's own
`kinship-vocabulary.md` said in April 2026 — and ***awliyāʾ* is dominated by *prohibited* alliance**
(Q 5:51, Q 60:1). **A prohibition is not an affiliation.** Across 185 tokens, **60 (32.4 %)** survive
a two-rater sense audit.

The pre-registered tests were run anyway and are reported in full: **verdict NULL at rung 1, 0 of 24
verdict-bearing cells passing, with the observed sign wrong in 4 of 4 headline channels.** The
pre-registered CBM verdict **RESTATES THE HIJRA** was never reached, because there is no effect to
explain away.

**The frontier map's prior for F-20 — "CONFIRMED but CBM-leaning… it may simply restate the Hijra" —
anticipated the wrong failure.** The worry was that the result would be true but trivial. The actual
failure is upstream of that: **the word list does not denote the construct**, so neither a pass nor a
CBM verdict was ever available.

---

## ⛔ CORRECTION — a root identification I got wrong, which also voids one directive I was given

**Stated first, because I put it into the pre-registration and into my own Step-0 report.**

I reported that H-NEW-267 lists **`mwl`, "the root of *mawlā*"**, among its six sharp stable roots
toward Medinan (stable 1.641, log-odds 1.760, 8 Late-Meccan vs 54 Medinan), and concluded that
H-NEW-267 "already owns *mawlā*". **That is wrong.**

- **`mwl` is the root of *māl* / *amwāl* — "wealth, property".** Verified: 86 STEM tokens in QAC
  v0.4, **all** carrying `LEM:maAl`; commonest forms `>amowa`li` (26), `>amowa`la` (19),
  `>amowa`lu` (10).
- ***mawlā* carries `ROOT:wly`** — verified directly on `LEM:mawolaY\``.

H-NEW-267's Medinan band — `Avm` (sin), `nfq` (hypocrisy/spending), `nsw` (women), `mwl`
(**wealth**), `jnH` (blame), `qtl` (killing) — is a legal/financial/combat cluster, a more coherent
reading than the one I gave it.

**Consequences, stated plainly:**

1. **H-NEW-267 does *not* already own *mawlā*.** F-20 was **less** pre-empted than I reported.
2. **The instruction to "declare in the prereg, before the run, that *mawlā* is inherited from
   H-NEW-267" rests on my error and there is nothing to declare.** As it happens the prereg did
   carry that declaration (§0, §2.1, §5.3 ground 3, §9) — so the directive was satisfied ex ante,
   with a false premise. The *mawlā*-ablation arm (§7, arm 6.1) ran regardless and is reported.
3. It was 1 of 4 independent grounds for the locked direction; the other three stand. **It touches
   no statistic, no null, no decision rule and no cell. The verdict is unchanged.**

Per the standing rule the pre-registration is **not** edited. The correction lives here.

**The irony is the point, and I am recording it rather than smoothing it:** §3 of this finding
audits unvalidated hand assignment, and §0 of its own pre-registration committed exactly that
defect — I asserted a root identity instead of computing it, in the one lane where that was the
subject.

---

# PART I — THE PRIMARY RESULT: the vocabulary does not denote the construct

## 1. The census

F-20's six terms are a **hand-assigned word list** — a category whose assignment rule is prose
(`findings/PROXY-CLAIMS.md` §5). All three of §4's standing requirements are met here.

**Operating range: 185 tokens.** That is the entirety of what this inventory scores; it leaves the
other **77 244** words of the corpus at zero.

| term | F-20 class | tokens | **agreed in F-20 class** | agreed in the *other* class | flagged DIVINE |
|:--|:--|--:|--:|--:|--:|
| `waliY~` (*walī / awliyāʾ*) | AFF | 86 | 39 (**45.3 %**) | 0 | 33 |
| `walad` | BIO | 56 | 15 (**26.8 %**) | 0 | 18 |
| `mawolaY\`` (*mawlā*) | AFF | 18 | 3 (**16.7 %**) | 0 | **11** |
| `>aroHaAm` (*arḥām*) | BIO | 12 | 3 (**25.0 %**) | 0 | 2 |
| `<ixowapN` (*ikhwa*) | AFF | 7 | **0 (0.0 %)** | **5** | 0 |
| `nasab` | BIO | 3 | **0 (0.0 %)** | 0 | 0 |
| `mawa\`liY` / `mawa\`liy` (*mawālī*) | AFF | 3 | **0 (0.0 %)** | 2 | 0 |
| **total** | | **185** | **60 (32.4 %)** | **7** | **64 (34.6 %)** |

**Of the six terms F-20 names, none is unambiguous in the sense the hypothesis requires.**

- ***ikhwa* — the collapse, and it is checkable in thirty seconds.** All seven tokens: Q 12:5, 12:7,
  12:58, 12:100 (**Joseph's biological brothers** — Sūrat Yūsuf holds four of the seven), Q 4:11 and
  Q 4:176 (**inheritance law**, biological siblings), and Q 49:10 (*innamā al-muʾminūna ikhwatun*).
  **Six of seven are biological.** The one term that carries F-20's whole thesis is, in the text,
  overwhelmingly a term for brothers by birth.
- ***mawlā* — dual-class, and mostly neither class.** 11 of 18 tokens are DIVINE by at least one
  rater: Q 2:286, 3:150, 8:40, 22:78, 47:11, 66:2, 66:4 — *Allāhu mawlākum*, "God is your patron".
  Rater A returns 10 DIVINE / 7 AFF / 1 BIO. The patron/client-versus-ally ambiguity is real, and it
  is dominated by a third sense that is neither.
- ***walī / awliyāʾ* — a prohibition entered as an affiliation.** 33 of 86 tokens are DIVINE. Much of
  the remainder is the *forbidding* of alliance — Q 5:51 (*lā tattakhidhū al-yahūda wa-l-naṣārā
  awliyāʾ*), Q 60:1. Counting a prohibition against affiliation as evidence of rising affiliation
  inverts the sign of the very thing being measured.
- ***walad* — the Christological denial, already published here.** 18 of 56 tokens are DIVINE.
  **`kinship-vocabulary.md` H-K1 stated this on 2026-04-12** ("the theological-denial cluster is the
  largest single use of `walad`"), and F-20 was designed as though it had not.
- ***nasab* — 3 tokens**, one of them theological (Q 37:158, a *nasab* asserted between God and the
  jinn).

## 2. The second rater is SEMI-independent, and κ is an UPPER BOUND

**Rater A** = a QAC co-occurrence rule (Arabic morphology only). **Rater B** = the Sahih
International translator's word choice, read by a declared keyword rule. Verse alignment positively
controlled at Q 1:1, Q 2:255, Q 114:1 — **3/3 pass**, asserted in code, not assumed.

> **κ(A, B) = 0.4683 over the operating range** (n = 160, raw agreement 0.6312)
> **κ(A, B) = 0.3776 over the full set** (n = 185)

**The correction I must state, and it changes how this number is read.** A translation is **not**
independent the way H-NEW-3020's raters were. Jeffery and al-Suyūṭī worked roughly a millennium
apart from different source traditions. **The Sahih International translator read this same text and
worked inside the same tafsīr tradition that makes the "obvious" reading obvious** — so agreement
between Rater B and any morphology-driven rule is inflated by shared inheritance rather than by two
parties independently being right.

> **Therefore κ = 0.4683 is an UPPER BOUND on true annotator agreement, not an estimate of it.**

That is what makes it usable: **an upper bound that comes out low is decisive.** Even granting the
inflation, the two channels concur on well under half the inventory beyond chance — and the true
figure is lower. The comparison to H-NEW-3020's κ = 0.386 should therefore be read as *this
inventory is no better resolved than the donor-language one, and probably worse.*

## 3. The audit is itself fallible, and I can name the case

**Both raters label Q 49:10 — *innamā al-muʾminūna ikhwatun*, the single clearest confessional-
brotherhood token in the Qurʾān — as BIOLOGICAL, and they agree with each other while doing it.**

- **Rater A** because the verse also contains *akhawaykum*, another `Axw` token, which trips its
  kin-root clause. **A design error of mine: the clause does not exclude the target token's own
  root.**
- **Rater B** because the English word is "brothers" whether the brotherhood is metaphorical or
  uterine. A gloss-reading rule cannot see the referent.

**Agreement is not accuracy.** κ measures how often two rules coincide; here they coincide on a
confident error, in the one case where ground truth is beyond dispute. So **32.4 % is not a
validated validity rate** — it is the fraction on which two fallible channels concur, one of them
semi-independent, and it is demonstrably wrong at least once in the direction that matters most.

**The honest conclusion is stronger than any of the numbers:** the biological/affiliative
distinction **cannot be made reliable by any channel available on disk**, and F-20 is not testable
as stated without sense annotation this project does not have.

## 4. Size loading — the one classic defect that is *absent* here

| | ρ vs log word-count | ρ vs log verse-count | ρ vs log MVL |
|:--|--:|--:|--:|
| AFF | **+0.7293** | +0.5837 | +0.6194 |
| BIO | **+0.6957** | +0.5356 | +0.6157 |

Both classes load **positively and near-identically** on every size channel — they differ by 0.034,
so a *difference* statistic cancels almost all of it. This is the opposite of H-NEW-860, where
ρ(UAS, log wc) = +0.608 met ρ(rubric, log wc) = −0.522 and manufactured a correlation about neither
variable. **The unit-drift leg of the three-defect chain does not apply to this finding.** The
failure is in the class assignment alone.

---

# PART II — THE REGISTER AXIS IS DEGENERATE AGAINST PHASE
### (this section generalises well beyond F-20 and is written to be lifted)

## 5. Prior work: this is already an audit, and it credits F-20's Step-0

**`findings/AUDIT-REGISTER-PHASE-COLLINEARITY.md` (2026-08-09) already exists** and records its
provenance as *"Found: in F-20's Step-0 report; independently recomputed here before publication."*
Its headline: **"'control for register' is undefined against phase for 43 % of the corpus."**

**Its structural conclusion is correct and reproduces.** What follows is a reconciliation, because
my parse and its parse disagree on the cell counts, and the disagreement has a diagnosable cause.

## 6. The 115th row is the header

The audit discloses in its own §4 that *"115 rows parsed against 114 surahs, so one row is
spurious"*. **The spurious row is the header line.** `neuwirth-sinai-genre-labels.tsv` carries `#`
comment lines followed by a column-name row; stripping only the `#` lines leaves 115 records of
which the first is `surah_number | surah_name_translit | neuwirth_phase | …`. My parse drops it and
asserts `len == 114`, which passes.

The audit's published table also sums to **113**, not to its stated 115 — two rows unaccounted.

## 7. Reconciliation, on a verified 114-row parse

**Under the audit's own head-term coarsening and apparent precedence (eschat before oath):**

| register | Meccan | Medinan | | audit published |
|:--|--:|--:|:--|:--|
| eschat | 26 | 2 | | 24 / 1 |
| hymn | 5 | 2 | | 6 / 1 |
| **legal** | **0** | **15** | **one phase only** | **0 / 15 — reproduces exactly** |
| **narrative** | **23** | **0** | **one phase only** | 26 / 0 |
| **oath** | **8** | **0** | **one phase only** | **8 / 0 — reproduces exactly** |
| polemic | 5 | 3 | | 5 / 3 — reproduces exactly |
| other | 19 | 6 | | 18 / 6 |
| **total** | **114** | | **degenerate = 46 (40.4 %)** | published 49 (43 %) |

**The three degenerate registers the audit identifies — legal, narrative, oath — all reproduce as
single-phase.** Per-cell counts differ in the non-load-bearing rows; the structure does not.

**And the degeneracy fraction is itself coarsening-dependent**, which the audit's §4 predicted:

| coarsening | degenerate surahs | share |
|:--|--:|--:|
| H-NEW-3090's 6-class (LEGAL, NARRATIVE, ESCHATOLOGICAL, SCRIPTURE, HYMNIC_OATH, EXHORT_POLEM) | 42 / 114 | **36.8 %** |
| audit's head-term, audit's precedence, verified parse | 46 / 114 | **40.4 %** |
| audit's published figure | 49 / 115 | 43 % |
| finer head-term, oath checked before eschat, verified parse | **65 / 114** | **57.0 %** |

**The audit is right and, if anything, understates the problem.** Its §4 reasoning — that a finer
partition can only make strata smaller and so degeneracy generally increases — is confirmed: the
same file yields 36.8 % to 57.0 % degeneracy depending purely on where the coarsening cuts.
**Coarsening choice is a deciding parameter in the cross-finding-029 sense and should be declared by
anyone running a register-stratified test.**

## 8. What this constrains, beyond F-20

The crosstab under H-NEW-3090's own coarsening:

| coarsened register | Meccan | Medinan | |
|:--|--:|--:|:--|
| NARRATIVE | 27 | 0 | **degenerate — zero permutable information** |
| LEGAL | 0 | 15 | **degenerate — zero permutable information** |
| ESCHATOLOGICAL | 23 | 2 | mixed |
| HYMNIC_OATH | 14 | 2 | mixed |
| SCRIPTURE | 11 | 1 | mixed |
| EXHORT_POLEM | 11 | 8 | mixed |

**A stratum with one phase level has nothing to permute** — every permutation returns the observed
value, so those surahs sit in the reported *n* while contributing zero to the null. Mixed strata
here hold **59 Meccan against 13 Medinan**; the effective comparison is far smaller and far more
lopsided than "N = 114, stratified on register" suggests.

**This is not a fact about kinship vocabulary.** It applies to **every test in this project that
stratifies on the Neuwirth–Sinai labels while testing against Meccan/Medinan phase.** Files that
read the label file: `h-new-3010` (conditional register), `h-new-3040` (modality axis), `h-new-3080`
(quantifier scope), the `h-new-127-*` family (Jurjānī tier bridge, phase structure, coarse-class
localization), and this finding.

**And the collinearity is substantive, not accidental.** Legal discourse *is* Medinan; narrative and
oath openings *are* Meccan. That is the content of the periodisation, not a sampling artefact — so
*"does X track phase independently of register?"* is **not answerable** for those surahs by any
amount of stratification. The available honest options are **ablation** (drop the collinear
registers, report reduced *n* and its MDE) or **reframe** (accept the two variables are partly the
same here). What is not available is to run the stratified test and report register as controlled.

**H-NEW-3090 took the ablation option**, which is why its headline arm (T2) drops the legal register
outright rather than stratifying — forking-paths item 2, logged before the run.

---

# PART III — THE TESTS, REPORTED IN FULL

## 9. Step-0 prior-art grep (run before any design)

| # | Found | Bearing |
|:--|:--|:--|
| 1 | **No dedicated finding** for kinship-vs-affiliation in `findings/` or the ledger. | F-20 is **not** a re-derivation. The staleness failure did not recur. |
| 2 | **H-NEW-267** — Hijra frontier, AUC 1.000 both directions. | Pre-empts *the boundary*, not this contrast. **And see the correction** — its `mwl` is *māl*. |
| 3 | **H-NEW-277** — broad-root ablation on the same frontier. | Frontier already ablation-tested at root level. |
| 4 | `kinship-vocabulary.md` **H-K1**. | **Prior art inside this project already contradicted F-20's premise.** Confirmed at 18/56 tokens. |

## 10. Verdict: NULL — 0 of 24 verdict-bearing cells passed

**Pooled affiliation share, `AFF / (AFF + BIO)`, R1 lemma-literal, all 114 sūras:**

| | AFF | BIO | share |
|:--|--:|--:|--:|
| Meccan | 56 | 33 | **0.6292** |
| Medinan | 58 | 38 | **0.6042** |

**Δ = −0.0250 — the wrong sign.** The locked direction was Δ > 0.

### 10.1 Channel table — all four channels, worst is headline

One-sided permutation p, 10 000 perms, seed 20260509, α_bon = 0.00208333 (k = 24).

**T1 FULL (N = 114) · R1**

| channel | observed Δ | null mean | p | pass |
|:--|--:|--:|--:|:--|
| RATIO | **−0.025047** | +0.002238 | 0.5932 | fail |
| PER_WORD | +0.000167 | −0.000001 | 0.3536 | fail |
| PER_VERSE | +0.003347 | −0.000001 | 0.3246 | fail |
| MVL_RESID | **−0.000187** | −0.000002 | 0.6537 | fail |

**T2 LEGAL-ABLATED (N = 99) · R1 — the headline within-register test**

| channel | observed Δ | null mean | p | pass |
|:--|--:|--:|--:|:--|
| RATIO | **−0.099802** | −0.005701 | 0.7092 | fail |
| PER_WORD | **−0.000895** | −0.000003 | 0.9465 | fail |
| PER_VERSE | **−0.012161** | −0.000046 | 0.9454 | fail |
| MVL_RESID | **−0.001049** | −0.000003 | **0.9692** ← worst | fail |

**T3 REGISTER-STRATIFIED (N = 72, 4 mixed strata) · R1**

| channel | observed Δ | p | pass |
|:--|--:|--:|:--|
| RATIO | +0.213220 | 0.1517 | fail |
| PER_WORD | −0.000749 | 0.5736 | fail |
| PER_VERSE | −0.007358 | 0.4862 | fail |
| MVL_RESID | −0.000919 | 0.6398 | fail |

**Dominant channel: none is.** T2/R1 spans p = 0.709 → 0.969 (**1.37×**); T1/R1 spans 0.325 → 0.654
(**2.0×**). Against H-NEW-3010's 70× swing and H-NEW-3040's 3-PASS/5-NULL flip, **the length channel
does not decide this verdict.** Formally the furthest-from-median channel is RATIO and the worst is
MVL_RESID, but the ranking carries no weight here.

### 10.2 The deciding parameter is lemma-versus-root

| tuple | T1 RATIO p | tokens |
|:--|--:|--:|
| **R1 lemma-literal** | **0.5932** | 71 BIO / 114 AFF |
| **R2 root-literal** (contamination diagnostic) | **0.0047** | 444 BIO / 328 AFF |

**A 126× p-swing from one convention.** R2 still fails α_bon and even a looser k = 12 threshold, so
nothing is rescued — but every trace of apparent signal lives at root level, i.e. in
***raḥma*/*al-Raḥmān*** (327 of root `rHm`'s 339 tokens are not *arḥām*) and ***tawallā*** (78 of
root `wly`'s 232). Divine mercy and turning-away. **Counted at root level, F-20 measures the wrong
words — and that is the only level at which it looks like anything.**

## 11. Where the Medinan affiliative mass actually sits

| register | phase | AFF | BIO | share |
|:--|:--|--:|--:|--:|
| LEGAL | Medinan | 40 | 22 | 0.645 |
| NARRATIVE | Meccan | 28 | 17 | 0.622 |
| SCRIPTURE | Meccan | 28 | 12 | 0.700 |
| SCRIPTURE | Medinan | 2 | 1 | 0.667 |
| EXHORT_POLEM | Meccan | **0** | **4** | 0.000 |
| EXHORT_POLEM | Medinan | 16 | 15 | 0.516 |
| ESCHATOLOGICAL / HYMNIC_OATH | either | **0** | **0** | — |

1. **Ablating the legal register drives the contrast further negative** (−0.0250 → −0.0998). **40 of
   the 58 Medinan AFF tokens are in legal sūras.** The register confound is not a competing
   explanation here — it is the **entire location** of the phenomenon. There is no non-legal Medinan
   rise to defend.
2. **The one stratum running in the predicted direction is EXHORT_POLEM, and its Meccan cell holds
   four tokens** — Q 23:91 (*walad*), Q 23:101 (*nasab*), Q 31:33 (*walad*), Q 31:34 (*arḥām*). T3's
   whole +0.213 comes from that 0.000-vs-0.516 contrast. Arithmetic checks:
   (43 × −0.033 + 35 × +0.516) / 78 = **+0.213**. p = 0.152.
3. **41 sūras — every ESCHATOLOGICAL and HYMNIC_OATH one — contain zero tokens of either class.**
   Q 112 al-Ikhlāṣ contributes nothing: *lam yalid wa-lam yūlad* is the **verb** `walada`, not the
   noun lemma `walad`.

## 12. Power — mandatory, since this is a NULL

MDE at 80 % power, α_bon = 0.00208333, for T2 under R1 (200 sims × 2 000 permutations per grid point):

| channel | MDE @ 80 % | achieved power | observed Δ | MDE ÷ \|observed\| |
|:--|--:|--:|--:|--:|
| RATIO | **0.360** (share difference) | 0.890 | −0.0998 | **3.61×** |
| PER_WORD | 0.0036045 | 0.825 | −0.000895 | 4.03× |
| PER_VERSE | 0.0523760 | 0.865 | −0.012161 | 4.31× |
| MVL_RESID | 0.0037810 | 0.815 | −0.001049 | 3.60× |

**Read the RATIO row as the honest statement of reach.** The Meccan baseline share is 0.6292; to be
detected, the Medinan share had to reach ≈ **0.99**. On 185 tokens across 114 sūras, **only a
near-total replacement of one class by the other was detectable.**

> **This NULL is weak evidence of absence and strong evidence of untestability.** F-20 as specified
> is underpowered by **3.6–4.3× in every channel**, and no design change short of a different word
> list fixes it — **the word list is the sample size.**

## 13. Descriptive ablations (prereg §6 — no Bonferroni slots; none changed the verdict)

| ablation | T1 RATIO Δ (p) | T2 RATIO Δ (p) |
|:--|--:|--:|
| **6.1** drop *mawlā* | −0.0715 (0.734) | −0.1738 (0.807) |
| **6.2** drop Sūra 12 (Yūsuf) | −0.0103 (0.526) | −0.0850 (0.672) |
| **6.3** drop DIVINE *walad* | −0.0409 (0.667) | −0.0793 (0.677) |

Removing *mawlā* makes the contrast **more** negative. 6.3's best cell is T1 PER_VERSE at p = 0.077
— the closest anything came to the predicted direction, still **37×** above α_bon.

## 14. Classical anchor — declared change of role, and the limits of what I verified

`data/baseline-corpora/raw/sira-ibn-hisham.txt` had only ever been read by this project as a
**corpus baseline** — a bag of Arabic prose for length- and register-matching. **Reading it as a
historical source is a change of role, declared in prereg §8 before the run.**

**Verified by opening the file at the lines given, and reported as line locators only:**

- line **8582** — chapter heading `المؤاخاة بين المهاجرين والأنصار`
- lines **8583–8623** — the pericope, opening `قال ابن إسحاق: وآخى رسول الله ﷺ بين أصحابه`
- lines **23313–23315** — a second notice naming pairs

**What I did not verify, and therefore do not assert:** no page number, no edition, no printed
chapter number, and no ḥadīth or *nawʿ* index. **The death dates conventionally given for Ibn Isḥāq
and Ibn Hishām are not derivable from this file and I have not verified them from any on-disk
source; I therefore do not state them as established here.** What the death-date rule *does* require
and what I *did* check is internal attribution: the passage is attributed **in the text itself** to
Ibn Isḥāq, by the string `قال ابن إسحاق` at line 8584.

**Used for exactly one thing** — to make the locked direction a prediction rather than a guess, by
establishing that the brothering tradition exists in the sīra and is placed after the Hijra. It is
**not** evidence about Qurʾānic vocabulary, **not** independently dated, and **no historicity claim
is made**.

## 15. Gates

| gate | status |
|:--|:--|
| Pre-registration written before design of the run, SHA-256 `c163a0b2…21b8` | PASS |
| SHA embedded as `EXPECTED_PREREG_SHA`, verified at runtime with `SystemExit` | PASS — `run.log` line 2 |
| Step-0 prior-art grep before design, logged as forking-paths item 1 | PASS |
| Verdict function diffed line-by-line against prereg §7 before the run | PASS — rung for rung |
| Permutation null, seed 20260509, 10 000 perms | PASS |
| Immutable run dir, `makedirs(exist_ok=False)`, all writes `open(…, 'x')` | PASS |
| No run directory deleted | PASS — one directory, retained |
| Rules-tuples ≥ 2 | PASS — R1, R3 verdict-bearing; R2 diagnostic |
| All length channels run, worst is headline, dominant named | PASS — 4 channels × 3 tests × 3 tuples = 36 cells |
| Direction locked and justified before run | PASS — 4 grounds, one since corrected |
| Bonferroni | PASS — k = 24, tighter than the union question needs |
| Tie rule (> 50 % ties ⇒ exact test) | Checked in all 36 cells; **max tie fraction 0.0037**, no cell fell back to Fisher |
| NULL states MDE **and** power | PASS — §12 |
| Second rater's independence characterised | PASS — **semi-independent; κ reported as an upper bound** (§2) |
| Classical source: role change declared, locators only, nothing unverified asserted | PASS — §14 |
| Every reported number machine-checked against `results.json` | PASS |
| Pre-registration edited after the run | **NO** |

## 16. What I got wrong

1. **The `mwl` misidentification** (see correction above). Asserted, not computed, in a lane about
   unvalidated assertion.
2. **Rater A's kin-root clause does not exclude the target token's own root**, which is why Q 49:10
   fails. **I did not anticipate that two raters would agree on a wrong answer.** Had I not happened
   to know Q 49:10 by hand, κ = 0.4683 would have entered the record unqualified as a validity
   estimate — and §3 would not exist.
3. **I described Rater B as independent.** It is **semi-independent**: the translator read this text
   inside the tafsīr tradition that fixes the obvious reading. κ is an upper bound. Corrected in §2.
4. **The verdict ladder had no rung for "the effect runs the wrong way."** It correctly returned
   NULL, but NULL undersells a result with **4 of 4 headline channels carrying the opposite sign**.
5. **My first framing led with the NULL and filed the census as §4.** That inverted the finding: the
   denotation failure is the result, and the NULL is a consequence of it. Restructured here.

## 17. Bottom line

1. **The inventory does not measure the construct.** 32.4 % of 185 tokens survive a two-rater audit
   whose κ is itself an upper bound; ***ikhwa* is 6/7 biological**, ***mawlā* is 11/18 divine**. The
   two terms F-20 leans on hardest fail hardest.
2. **There is no non-legal Medinan affiliative rise to explain.** 40 of 58 Medinan AFF tokens are in
   legal sūras; ablating that register drives the contrast further negative.
3. **The register axis is degenerate against phase for 36.8–57.0 % of the corpus** depending on
   coarsening — a constraint on every register-stratified phase test in this project, not on this
   one.
4. **The test was underpowered by 3.6–4.3× before it ran**, and 185 tokens over 114 sūras cannot be
   rescued by a better statistic.

**What would make F-20 testable**: a sense-annotated kinship corpus, or per-token disambiguation
validated against something other than a second rule. **This is NOT-YET-DERIVED, not absent** — the
12-edition per-verse tafsīr (77 437 files) could in principle carry it, and building that table is
real future work. It was deliberately **not** built here, because inventing a sense classifier
mid-lane is the defect this lane was auditing.

Related: [[AUDIT-REGISTER-PHASE-COLLINEARITY]] · [[cross-finding-029-the-deciding-parameter]] ·
[[PROXY-CLAIMS]] · [[kinship-vocabulary]] · [[h-new-267-mecca-medina-vocabulary-frontier]] ·
[[h-new-3020-loanword-donor-strata]]
