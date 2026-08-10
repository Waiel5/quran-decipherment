---
finding_id: H-NEW-3090
title: Biological-kinship vs affiliative vocabulary across the Hijra — NULL, in the wrong direction, on an inventory that is 32% valid
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
verdict: NULL
---

# H-NEW-3090 — kinship vs affiliation across the Hijra

**Verdict: NULL.** Rung 1 of the pre-registered ladder. Not one of the 24 verdict-bearing cells
passed. The pre-registered verdict **RESTATES THE HIJRA** was never reached, because the effect it
would have explained away **does not exist to begin with** at the lemma level.

---

## ⛔ CORRECTION — I got a root identification wrong in my own Step-0 report, and it is in the pre-registration

**Before anything else.** My Step-0 report to the lead, and §0, §2.1, §5.3 and §9 of the
pre-registration, state that H-NEW-267 already lists **`mwl`, "the root of *mawlā*"**, among its six
sharp stable roots toward Medinan. **That is wrong.**

- **`mwl` is the root of *māl* / *amwāl* — "wealth, property".** Verified: 86 STEM tokens in QAC
  v0.4, **all** carrying `LEM:maAl`; commonest surface forms `>amowa`li` (26), `>amowa`la` (19),
  `>amowa`lu` (10).
- ***mawlā* carries `ROOT:wly`**, verified directly on `LEM:mawolaY\``.

So H-NEW-267's Medinan marker band — `Avm` (sin), `nfq` (hypocrisy/spending), `nsw` (women),
`mwl` (**wealth**), `jnH` (blame), `qtl` (killing) — is a legal/financial/combat cluster, which is
a more coherent reading than the one I gave it. **H-NEW-267 does not already own *mawlā*, and F-20
was therefore *less* pre-empted than I reported.**

**What this does and does not change.** It was one of four independent grounds for the locked
direction (§5.3 ground 3); the other three stand and the direction lock is unaffected. It touches
no statistic, no null, no decision rule and no cell. **The verdict is unchanged.** Per the standing
rule, the pre-registration is **not** edited — the correction lives here.

---

## 1. Step-0 prior-art grep (run before any design)

| # | Found | Bearing |
|:--|:--|:--|
| 1 | **No dedicated finding** for kinship-vs-affiliation in `findings/` or the ledger. | F-20 is **not** a re-derivation. The staleness warning's failure mode did not recur here. |
| 2 | **H-NEW-267** — Hijra frontier at AUC 1.000 both directions. | Pre-empts *the boundary*, not this contrast. **And see the correction above** — its `mwl` is *māl*, not *mawlā*. |
| 3 | **H-NEW-277** — broad-root ablation on the same frontier. | The frontier is already ablation-tested at root level. |
| 4 | `kinship-vocabulary.md` **H-K1**: *walad* is the "abstract theological offspring-word"; the denial cluster is its largest single use. | **Prior art inside this project already contradicted F-20's premise.** Confirmed below at 18/56 tokens. |

`grep` output is reproduced in prereg §0; the whole entry is forking-paths log item 1.

## 2. Headline numbers

**Pooled affiliation share, `AFF / (AFF + BIO)`, R1 lemma-literal, all 114 sūras:**

| | AFF | BIO | share |
|:--|--:|--:|--:|
| Meccan | 56 | 33 | **0.6292** |
| Medinan | 58 | 38 | **0.6042** |

**Δ = −0.0250** — the affiliative class is *marginally lower* in Medinan. The locked direction was
Δ > 0. **The observed sign is wrong in 3 of 4 channels at T1 and in 4 of 4 at T2.**

### 2.1 Channel table — all four channels, worst is headline (mandatory)

`p` is a one-sided permutation p, 10 000 perms, seed 20260509. α_bon = 0.00208333 (k = 24).

**T1 FULL (N = 114) · R1**

| channel | observed Δ | null mean | p | pass |
|:--|--:|--:|--:|:--|
| RATIO | **−0.025047** | +0.002238 | 0.5932 | fail |
| PER_WORD | +0.000167 | −0.000001 | 0.3536 | fail |
| PER_VERSE | +0.003347 | −0.000001 | 0.3246 | fail |
| MVL_RESID | **−0.000187** | −0.000002 | 0.6537 | fail |

**T2 LEGAL-ABLATED (N = 99; 15 legal sūras dropped) · R1 — the headline within-register test**

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

**Which channel is dominant for this grouping?** *None is.* T2/R1 spans p = 0.709 → 0.969, a **1.37×**
range; T1/R1 spans 0.325 → 0.654, a **2.0×** range. Against H-NEW-3010's 70× swing and H-NEW-3040's
3-PASS/5-NULL flip, **the length channel does not decide this verdict.** Formally the "furthest from
median" channel is RATIO and the worst is MVL_RESID, but the ranking is not load-bearing.

### 2.2 The deciding parameter really is something else (cross-finding-029 §3)

**The parameter this verdict is most sensitive to is `lemma` versus `root`.**

| tuple | T1 RATIO p | tokens |
|:--|--:|--:|
| **R1 lemma-literal** | **0.5932** | 71 BIO / 114 AFF |
| **R2 root-literal** (contamination diagnostic) | **0.0047** | 444 BIO / 328 AFF |

**A 126× p-swing from one convention.** R2 still fails α_bon (0.0047 > 0.00208) and fails even a
looser k = 12 threshold (0.00417), so nothing is rescued — but the whole of the apparent signal
lives at root level, i.e. in ***raḥma*/*al-Raḥmān* (327 of root `rHm`'s 339 tokens are not
*arḥām*) and *tawallā* (78 of root `wly`'s 232)** — divine mercy and turning-away, neither of which
is a kinship or affiliation term. **Counted at root level, F-20 measures the wrong words**, and it
is the only level at which it looks like anything.

## 3. The within-register result

### 3.1 The confound cannot be fully controlled at sūra granularity — and that is a finding

Computed from the two label files before locking, no outcome variable involved:

| coarsened register | Meccan | Medinan | |
|:--|--:|--:|:--|
| NARRATIVE | 27 | 0 | **degenerate — zero permutable information** |
| LEGAL | 0 | 15 | **degenerate — zero permutable information** |
| ESCHATOLOGICAL | 23 | 2 | mixed |
| HYMNIC_OATH | 14 | 2 | mixed |
| SCRIPTURE | 11 | 1 | mixed |
| EXHORT_POLEM | 11 | 8 | mixed |

**The two registers the F-20 confound is about are perfectly collinear with phase.** 42 of 114
sūras cannot contribute to any within-stratum permutation. This is why the headline arm is an
**ablation** rather than a stratification — the design change is logged as forking-paths item 2.

### 3.2 The affiliative rise, such as it is, is entirely inside the legal register

| register | phase | AFF | BIO | share |
|:--|:--|--:|--:|--:|
| LEGAL | Medinan | 40 | 22 | 0.645 |
| NARRATIVE | Meccan | 28 | 17 | 0.622 |
| SCRIPTURE | Meccan | 28 | 12 | 0.700 |
| SCRIPTURE | Medinan | 2 | 1 | 0.667 |
| EXHORT_POLEM | Meccan | **0** | **4** | 0.000 |
| EXHORT_POLEM | Medinan | 16 | 15 | 0.516 |
| ESCHATOLOGICAL | either | 0 | 0 | — |
| HYMNIC_OATH | either | 0 | 0 | — |

Three things to read off this table:

1. **Remove the legal register and the contrast goes *more* negative** (Δ: −0.0250 → −0.0998).
   The Medinan affiliative mass is 40 of 58 AFF tokens, and it sits in the legal sūras. So the
   register explanation is not merely *available* — it is the only place the Medinan affiliative
   vocabulary lives. There is simply no non-legal Medinan rise to defend.
2. **The one stratum that runs in the predicted direction is EXHORT_POLEM, and its Meccan cell
   holds four tokens** — Q 23:91 (*walad*), Q 23:101 (*nasab*), Q 31:33 (*walad*), Q 31:34
   (*arḥām*). T3's whole +0.213 comes from a 0.000-vs-0.516 share contrast built on those four.
   The weighted arithmetic checks exactly: (43 × −0.033 + 35 × +0.516) / 78 = **+0.213**. p = 0.152.
3. **41 sūras — every ESCHATOLOGICAL and HYMNIC_OATH one — contain zero tokens of either class.**
   Q 112 al-Ikhlāṣ contributes nothing, because *lam yalid wa-lam yūlad* is the **verb** `walada`,
   not the noun lemma `walad`. The vocabulary is absent from the registers that make up a third of
   the corpus.

## 4. The proxy census — the inventory is 32.4 % valid, and the audit itself is fallible

F-20's six terms are a **hand-assigned word list**: a category whose assignment rule is prose
(`findings/PROXY-CLAIMS.md` §5). All three §4 requirements are met below.

**Operating range: 185 tokens** — that is the whole of what the inventory scores; the other 77 244
words of the corpus it leaves at zero.

**Two independent raters** (prereg §3): Rater A = QAC co-occurrence rule; Rater B = the Sahih
International translator's word choice, read by a keyword rule. Alignment positively controlled at
Q 1:1, Q 2:255, Q 114:1 — 3/3 pass.

> **κ(A, B) = 0.4683 over the operating range** (n = 160, raw agreement 0.6312);
> **κ = 0.3776 over the full set** (n = 185).

For scale, H-NEW-3020's Jeffery-vs-al-Suyūṭī donor agreement was **κ = 0.386**. This inventory is no
better resolved than that one was.

### 4.1 Per-term (the number the verdict turns on)

| term | F-20 class | tokens | **agreed in F-20 class** | agreed in the *other* class | flagged DIVINE |
|:--|:--|--:|--:|--:|--:|
| `waliY~` (*walī/awliyāʾ*) | AFF | 86 | 39 (**45.3 %**) | 0 | 33 |
| `walad` | BIO | 56 | 15 (**26.8 %**) | 0 | 18 |
| `mawolaY\`` (*mawlā*) | AFF | 18 | 3 (**16.7 %**) | 0 | 11 |
| `>aroHaAm` (*arḥām*) | BIO | 12 | 3 (**25.0 %**) | 0 | 2 |
| `<ixowapN` (*ikhwa*) | AFF | 7 | **0 (0.0 %)** | **5** | 0 |
| `nasab` | BIO | 3 | **0 (0.0 %)** | 0 | 0 |
| `mawa\`liY` / `mawa\`liy` | AFF | 3 | **0 (0.0 %)** | 2 | 0 |
| **total** | | **185** | **60 (32.4 %)** | **7** | **64 (34.6 %)** |

**Answering the brief's question directly: of the six terms F-20 names, *none* is unambiguous.**

- ***ikhwa* is the collapse.** All 7 tokens: Q 12:5, 12:7, 12:58, 12:100 (Joseph's **biological**
  brothers), Q 4:11, 4:176 (**inheritance law**, biological siblings), Q 49:10 (*innamā
  al-muʾminūna ikhwatun*). **Six of seven are biological**, and Rater B glossed all seven "brothers".
- ***mawlā* is the dual-class term you flagged, and it is worse than dual — it is mostly divine.**
  11 of 18 tokens are DIVINE by at least one rater (Q 2:286, 3:150, 8:40, 22:78, 47:11, 66:2, 66:4
  — *Allāhu mawlākum*). Rater A: 10 DIVINE / 7 AFF / 1 BIO.
- ***walī/awliyāʾ*** carries 33 DIVINE of 86, and much of the remainder is *prohibited* alliance
  (Q 5:51, 60:1) — a prohibition against affiliation, entered as evidence of affiliation.
- ***walad*** is 18 DIVINE of 56 — the *walad*-denial. **`kinship-vocabulary.md` H-K1 said this in
  April 2026 and F-20 was designed as if it had not.**
- ***nasab*** is 3 tokens, one of them theological (Q 37:158, a *nasab* between God and the jinn).

### 4.2 The audit is fallible, and I can show exactly where

**Both raters label Q 49:10 — the single clearest confessional-brotherhood token in the Qurʾān —
as BIOLOGICAL, and they agree with each other while doing it.** Rater A because the verse also
contains *akhawaykum* (another `Axw` token, which trips its kin-root clause); Rater B because the
English word is "brothers" whether the brotherhood is metaphorical or uterine.

**Agreement is not accuracy.** κ = 0.468 measures how often two rules coincide, and here they
coincide on a confident error. So **32.4 % is not a validated validity rate** — it is the fraction
on which two fallible channels concur, and the one case where ground truth is beyond dispute is a
case they both get wrong. The honest conclusion is stronger than the number: **the biological /
affiliative distinction cannot be made reliable by any channel available on disk**, and F-20 is not
testable as stated without a sense-annotated corpus this project does not have.

### 4.3 Size loading — the one defect that is *absent* here

| | ρ vs log word-count | ρ vs log verse-count | ρ vs log MVL |
|:--|--:|--:|--:|
| AFF | **+0.7293** | +0.5837 | +0.6194 |
| BIO | **+0.6957** | +0.5356 | +0.6157 |

Both classes load **positively and near-identically** on every size channel. This is the opposite of
H-NEW-860, where ρ(UAS, log wc) = +0.608 met ρ(rubric, log wc) = −0.522 and manufactured a
correlation about neither variable. Here the loadings differ by 0.034, so a *difference* statistic
cancels almost all of it. **The unit-drift leg of the three-defect chain does not apply to this
finding** — the failure is in the class assignment, not in the denominator.

## 5. Power — this is a NULL, so the MDE is mandatory

MDE at 80 % power, α_bon = 0.00208333, for the headline test **T2 under R1**, by parametric
simulation (200 sims × 2 000 permutations per grid point):

| channel | MDE @ 80 % | achieved power | observed Δ | MDE as multiple of \|observed\| |
|:--|--:|--:|--:|--:|
| RATIO | **0.360** (share difference) | 0.890 | −0.0998 | **3.61×** |
| PER_WORD | 0.0036045 | 0.825 | −0.000895 | 4.03× |
| PER_VERSE | 0.0523760 | 0.865 | −0.012161 | 4.31× |
| MVL_RESID | 0.0037810 | 0.815 | −0.001049 | 3.60× |

**Read the RATIO row as the honest statement of what this test could see.** The Meccan baseline
share is 0.6292; to be detected, the Medinan share would have had to reach ≈ **0.99**. On 185 tokens
spread over 114 sūras, **only a near-total replacement of one class by the other was detectable.**

**Therefore this NULL is weak as evidence of absence and strong as evidence of untestability.** The
correct reading is *not* "kinship and affiliation are proven not to shift". It is:

> On the six terms F-20 names, at lemma level, there is **no detectable shift, and what shift there
> is runs the wrong way** — and the instrument was never capable of resolving anything smaller than
> a 3.6× larger effect. F-20 as specified is **underpowered by roughly 3.6–4.3× in every channel**,
> and no design change short of a different word list fixes that, because the word list is the
> sample size.

## 6. Descriptive ablations (prereg §6 — no Bonferroni slots; none changed the verdict)

| ablation | T1 RATIO Δ (p) | T2 RATIO Δ (p) |
|:--|--:|--:|
| **6.1** drop *mawlā* | −0.0715 (0.734) | −0.1738 (0.807) |
| **6.2** drop Sūra 12 (Yūsuf) | −0.0103 (0.526) | −0.0850 (0.672) |
| **6.3** drop DIVINE *walad* | −0.0409 (0.667) | −0.0793 (0.677) |

Removing *mawlā* makes the contrast **more** negative, so the Medinan-affiliative story is not even
carried by the one term that had an out-of-sample prior. 6.3's best cell is T1 PER_VERSE at
p = 0.077 — the closest anything came to the predicted direction, still 37× above α_bon.

## 7. Classical anchor — declared change of role, and what it was used for

The *muʾākhāt*. `data/baseline-corpora/raw/sira-ibn-hisham.txt` had only ever been read by this
project as a **corpus baseline**. Reading it as a historical source is a change of role and was
declared as such in prereg §8 before the run.

Located and opened: line **8582**, chapter heading `المؤاخاة بين المهاجرين والأنصار`; lines
**8583–8623**, the pericope opening `قال ابن إسحاق: وآخى رسول الله ﷺ بين أصحابه`; lines
**23313–23315**, a second notice naming pairs. Per the death-date rule, the passage is attributed
**in the text itself** to Ibn Isḥāq (d. 150/767) within Ibn Hishām's (d. 218/833) recension.

**It was used for exactly one thing** — to make the locked direction a prediction rather than a
guess, by establishing that the brothering tradition exists in the sīra and is placed after the
Hijra. It is not evidence about Qurʾānic vocabulary, it is not independently dated, and **no
historicity claim is made**. No citation is reported that was not opened at the line given, and
nothing is cited that I did not read.

## 8. Gates

| gate | status |
|:--|:--|
| Pre-registration written **before** design of the run, SHA-256 `c163a0b2…21b8` | PASS |
| SHA embedded as `EXPECTED_PREREG_SHA`, verified at runtime with `SystemExit` | PASS — verified in `run.log` line 2 |
| Step-0 prior-art grep before design, logged as forking-paths item 1 | PASS |
| Verdict function diffed line-by-line against prereg §7 before the run | PASS — rung-for-rung, reproduced in the run transcript |
| Permutation null, seed 20260509, 10 000 perms | PASS |
| Immutable run dir, `os.makedirs(exist_ok=False)`, all writes `open(…, 'x')` | PASS |
| No run directory deleted | PASS — one directory, retained |
| Rules-tuple ≥ 2 | PASS — R1, R3 verdict-bearing; R2 diagnostic |
| All length channels run, worst is headline | PASS — 4 channels × 3 tests × 3 tuples = 36 cells |
| Direction locked and justified before run | PASS — 4 grounds, one since corrected (§ correction) |
| Bonferroni | PASS — k = 24, α_bon = 0.00208333, tighter than the union question needs |
| Tie rule (> 50 % ties ⇒ exact test) | Checked in every cell; **max tie fraction never exceeded the threshold, so no cell fell back to Fisher.** |
| NULL states MDE **and** power | PASS — §5 |
| Every reported number machine-checked against `results.json` | PASS |
| Pre-registration edited after the run | **NO** — the `mwl` error is corrected here, not there |

## 9. What I got wrong, at full prominence

1. **The `mwl` misidentification.** I told the lead, and wrote into the pre-registration, that
   H-NEW-267's Medinan marker `mwl` is the root of *mawlā*. **It is *māl*, "wealth" — 86 tokens, all
   `LEM:maAl`.** *mawlā* is `wly`. I asserted a root identity instead of computing it, in a lane
   whose entire subject is unvalidated hand assignment. The irony is the point: **§4 of this finding
   audits exactly the defect §0 of its own pre-registration committed.** It changed no statistic and
   no verdict, and it made F-20 look more pre-empted than it was.
2. **I designed Rater A's kin-root clause without excluding the token's own root**, which is why it
   labels Q 49:10 BIO on the strength of *akhawaykum*. I did not anticipate that the two raters
   would agree on a wrong answer, and §4.2 exists because they did. Had I not happened to know
   Q 49:10 by hand, κ = 0.468 would have gone into the record unqualified as a validity estimate.
3. **The pre-registration's ladder had no rung for "the effect runs the wrong way".** The ladder is
   exhaustive over pass/fail, so it correctly returned NULL, but "NULL" undersells a result in which
   **4 of 4 headline channels carry the opposite sign**. A sign-reversal rung would have been more
   informative and I did not write one.

## 10. Bottom line

**F-20 is NULL at rung 1, and its own frontier-map prior — "CONFIRMED but CBM-leaning" — was wrong
in the more interesting direction.** The worry was that the hypothesis would pass for a trivial
reason. It does not pass at all.

Three separable results, in descending order of what I would defend:

1. **The inventory does not measure the construct.** 32.4 % of 185 tokens survive a two-rater sense
   audit; 34.6 % are divine-referent; ***ikhwa* is 6/7 biological** and ***mawlā* is 11/18 divine**.
   The two terms F-20 leans on hardest are the two that fail hardest.
2. **There is no non-legal Medinan affiliative rise to explain.** 40 of the 58 Medinan AFF tokens
   are in legal sūras, and ablating that register drives the contrast further negative. The
   register confound is not a competing explanation here; it is the **entire location** of the
   phenomenon.
3. **The test was underpowered by 3.6–4.3× before it was run**, and a 185-token inventory over 114
   sūras cannot be made powerful by a better statistic.

**What would make F-20 testable**: a sense-annotated kinship corpus, or a per-token disambiguation
validated against something other than a second rule. Neither exists on disk. **That is a
NOT-YET-DERIVED, not an absence** — the 12-edition per-verse tafsīr (77 437 files) could in
principle carry the sense annotation, and building that table is real future work rather than a
rescue arm. It was deliberately **not** built here, because inventing a sense classifier mid-lane is
the defect this lane was auditing.
