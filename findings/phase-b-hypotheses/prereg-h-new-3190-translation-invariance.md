---
id: prereg-H-NEW-3190
title: "Pre-registration — Does an Arabic near-twin distinction survive translation? Ten-language test of whether lexical difference outlasts morphological difference"
date: 2026-08-09
author: Waiel Al-Shujaa
frontier_item: F-18
status: LOCKED — written before any inferential statistic was computed
seed: 20260509
permutations: 10000
family: TRANSLATION-2026-08-09-A
bonferroni_k: 3
alpha_bonferroni: 0.016666667
rules_tuple: (no-tashkeel Arabic, orthographic-token, waqf-marks-stripped, cross-surah-only, Hafs-Kufan, QAC-v0.4-ROOT, basmala-counted-only-in-Q1)
run_dir: findings/phase-b-hypotheses/runs/h-new-3190/<UTC>/
script: scripts/h-new-3190.py
---

# Pre-registration — H-NEW-3190 (frontier item F-18)

## §0. Prior-work check, run BEFORE any design work

Required by the binding rule in `HANDOFF/FRONTIER-MAP-2026-08-07.md`. **This check determines
whether to run at all, and it belongs before the checks about how to run.**

`bash scripts/check-frontier-staleness.sh` → F-18 is **absent** from the list of frontier items with
a finding on disk. Then grepped `findings/` and `MASTER-FINDINGS-LEDGER.md` for: *translation
invariance, translation, ten translations, h-new-710, sahih international, en.sahih, cross-lingual,
verse-twin × translation.*

**Result: F-18 is OPEN. The dispatch screen's H-NEW-710 flag is a false positive.**

| | H-NEW-710 | this lane |
|:--|:--|:--|
| object | the H-NEW-660 **compression-tail** (a per-surah, length-ordered gradient) | **near-twin verse pairs** |
| instrument | top-200-stem cosine on K=15 window-d̄ curves | token-Levenshtein + QAC root identity |
| languages | 1 (Sahih International) | 10 |
| verdict | NULL — English slope +0.00612, wrong sign; r(Arabic, English) = −0.91 | — |

`h-new-167-verse-twin-graph.md`, `h-new-1770-verse-twin-graph-deep.md` and
`h-new-2380-near-twin-census.md` were grepped for `translat|english`: **zero hits**. No verse-twin
finding carries a translation arm. No `h-new-3190` exists in `findings/` or in
`findings/phase-b-hypotheses/runs/`.

**H-NEW-710 is a prior, not an answer — and a discouraging one.** It is used below as a
direction-locking anchor. The map's *Prior* line (PARTIAL, "I expect 15–30%") is **not** used; it
refers to NM-41's top-50 Jaccard design, which this lane does not adopt.

### §0.1 Edition-identity audit, performed before locking

The repo has previously found one tafsīr folder misattributed by ~1,300 years and another that was
72% a different author. Every edition was therefore checked on disk before use.

**(a) The English arm is not an independent draw.** `dist/quran_en.json` is the **same translation**
as `data/translations/en.sahih.txt`, which H-NEW-710 already used: 6,236 / 6,236 verses match at
**100.00%** after NFKC + casefold + punctuation-strip. (Raw equality is only 7.76% because the risan
build drops the terminal full stop.) `en.sahih.txt` carries 6,247 non-empty lines against 6,236
verses — **11 trailing lines beyond the corpus**, so positional readers must truncate, not zip.
*Consequence: at most NINE of the ten languages are new to this project, and the English arm is not
independent evidence relative to H-NEW-710.*

**(b) The README's sources are not the fetch targets.** `README.md` lines 107–120 state each
translation is "sourced from tanzil.net". `scripts/download.js` fetches **none** of them from
tanzil; every edition comes from
`https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/<slug>.json`. The tanzil URLs are
**code comments**. The bytes on disk are therefore one aggregator removed from the named source, and
the translator names are the packager's assertion about that aggregator's slugs.

**These are recorded as slug-level attributions, NOT as verified translator identities:**

| code | slug fetched | attribution claimed | verification status |
|:--|:--|:--|:--|
| bn | `ben-muhiuddinkhan` | Muhiuddin Khan | slug + comment only |
| **en** | `eng-ummmuhammad` | Umm Muhammad / Saheeh International | **CONFIRMED** — 100% match to `en.sahih.txt` |
| es | `spa-muhammadisagarc` | Muhammad Isa García | slug + comment only |
| **fr** | `fra-muhammadhamidul` | Muhammad Hamidullah | **corroborated** — Q1:1 matches Hamidullah's canonical rendering |
| id | `ind-indonesianislam` | Indonesian Islamic Affairs Ministry (committee) | slug + comment only |
| ru | `rus-elmirkuliev` | Elmir Kuliev | slug + comment only |
| sv | `swe-knutbernstrom` | Knut Bernström | slug + comment only |
| tr | `tur-diyanetisleri` | Turkish Diyanet (committee) | slug + comment only |
| ur | `urd-abulaalamaududi` | Abul Aʿlā Mawdūdī | slug + comment only |
| zh | `zho-muhammadmakin` | Muhammad Ma Jian (Makin) | slug + comment only |

**No translator identity beyond `en` is asserted as verified anywhere in the resulting finding.**

File integrity is clean: all ten have exactly 114 surahs / 6,236 verses / 0 empty translations, and
no two languages share more than 2% byte-identical verses.

**(c) The editions are lexically non-comparable by construction.** `es` renders the deity "Dios" and
`sv` "GUD", where `en`/`fr` keep "Allah"; `sv` sets Q1:1 in full caps; `zh` totals 245,051 characters
against a 775k–1.07M range for the others — a 3–4× unit difference that is **pure script, not
content**. *This is why no statistic below is computed on raw cross-language magnitudes.* Every
per-language quantity is converted to a **within-language percentile rank** before pooling, so the
unit incommensurability cancels.

**(d) Non-independence.** Per the map's confound line, these are a **correlated family, not ten
independent draws**: three are committee productions (`id`, `tr`, and `en`, itself a three-person
committee), and Bernström's Swedish is widely described as leaning on Muhammad Asad's English. **That
last claim cannot be checked from disk** — the repo holds no Asad text — and is therefore recorded as
an *unverified external claim, not evidence.* The design responds by reporting a **single pooled
statistic** and treating the per-language arm (I3) as a consistency check, never as ten independent
tests.

### §0.2 The contamination I must declare at full prominence

**I ran an exploratory probe that showed me the marginal direction of the effect before this document
was written.** `scratchpad/probe2.py` computed the median pooled normalized translation distance by
Arabic class and returned:

| Arabic class | n | median pooled normalized translation distance |
|:--|--:|--:|
| exact twins (d = 0) | 59 | 0.333 |
| same-root substitutions only | 17 | 0.442 |
| different-root substitutions only | 210 | 0.817 |

I had derived the *direction* from H-NEW-2380's published taxonomy before running the probe (§2), but
**I cannot prove to a reader the order in which my own reasoning happened**, and the honest
assumption is the unfavourable one.

**Consequence, applied as a scoping decision rather than a caveat: the marginal
lexical-versus-morphological gradient is NOT registered as an inference.** It is already seen, and it
is reported below only as a descriptive, pre-lock quantity. **All three registered inferences are
quantities the probe did not compute** — the *d*-stratified contrast, its behaviour across the three
length rules, and per-language consistency.

### §0.3 Everything inspected before this lock

`check-frontier-staleness.sh`; `HANDOFF/FRONTIER-MAP-2026-08-07.md` F-18 + §C scorecard;
`HANDOFF/05-OPEN-QUESTIONS.md` OQ-14; `HANDOFF/03-NEXT-MOVES.md` NM-41;
`h-new-710-translation-invariance.md` + its prereg; `h-new-3160-tafsir-disagreement.md`;
`cross-finding-029-the-deciding-parameter.md`; `cross-finding-030-three-ways-a-control-fails.md`;
`h-new-2380-near-twin-census.md`; `h-new-167-verse-twin-graph.md`;
`h-new-1770-verse-twin-graph-deep.md`; `h-new-3090-kinship-affiliation.md` §κ (the shared-inheritance
warning); the risan `README.md`, `package.json`, `scripts/download.js`; and scratchpad probes
`size_pool.py`, `probe_outcome.py`, `probe2.py`, `probe3.py`.

---

## §1. Hypothesis

**F-18 restated so that it is falsifiable.** A near-twin verse pair differs from its partner in one
to three tokens. Some of those differences are **morphological** — the same root in a different
derived form, `najjaynākum ↔ anjaynākum`, form II against form IV of *n-j-w*, both "We saved you".
Others are **lexical** — a different root altogether, `yudhabbiḥūna ↔ yuqattilūna`, "slaughtering"
against "killing". Both examples are H-NEW-2380's own published exemplars from the same verse pair
(Q 2:49 ↔ Q 7:141).

> **H-NEW-3190.** Per differing token, a **lexical** difference moves the ten translations further
> apart than a **morphological** difference does, *after the total number of differing tokens is held
> fixed.* Morphological difference is the surface-Arabic artefact; lexical difference is the
> meaning-level signal.

**Why this is the F-18 question and not a tautology.** A translation is a function of its source, so
"translation similarity tracks Arabic similarity" is true by construction and worth nothing. The
registered claim is **conditional on the amount of Arabic difference**: given that two verses differ
by exactly *d* tokens, does it matter *which kind* of difference those are? Nothing about translation
being source-derived answers that. A translator can render form II and form IV differently
("delivered" / "saved"), and can render two distinct roots identically — the probe already shows both
happening (Turkish and Bengali both collapse *rasūl* / *nabī* to one word; Chinese renders *yaraw*
"see" as 知道 "know").

**The trap this design is built around.** A lane last week measured κ = 0.468 between a translation
and a rule-based classifier and found both raters wrong on Q 49:10 — the clearest confessional
*brotherhood* token in the corpus. **Agreement is not accuracy**, because a translator read this text
inside the tradition that makes the obvious reading obvious. This design never uses a translation as
a *rater of the Arabic*. It uses translations only as **ten noisy re-encodings whose disagreement
with each other is the measurement.** Nothing here computes agreement between a translation and an
Arabic-derived label. Where an agreement-like statistic does appear (I3), it is reported as an
**upper bound** and hand-checked in both directions per §7.4.

## §2. Direction lock, and the published anchors it comes from

**Locked: β(n_lex) > β(n_morph), strictly positive contrast.** Justification, from published findings
on disk — **not** from the frontier map's Prior line:

1. **H-NEW-2380 §"The differing-token patterns"** publishes the taxonomy this lane inherits and
   labels its categories itself: *"Near-synonym lexical substitution. Theologically equivalent
   verbs/nouns swapped"* against *"najjaynākum ↔ anjaynākum (same root, II vs IV form)"*. A derived-form
   alternation of one root has one lexical meaning; a root substitution has two. **The direction is
   entailed by the inherited taxonomy, before any measurement.**
2. **H-NEW-710 (NULL)** found the compression-tail is *Arabic-FR-roots-specific* and does not survive
   into English — slope reversed, r = −0.91. That is a published statement that **Arabic
   morphological structure is translation-invisible**, i.e. β(n_morph) ≈ 0. It **supports** the locked
   direction rather than opposing it.
3. **Counter-anchor, recorded as required.** I searched for a published anchor pointing the other way
   — a finding in which Arabic morphology survives translation better than lexis does — and **found
   none.** The absence is recorded here so that a reader knows the lock is one-sided by evidence, not
   by omission. If the run returns the reverse sign at magnitude, §6.3 fires.

## §3. Instruments

### §3.1 The pool

Cross-surah verse pairs *(v₁, v₂)* with **token-Levenshtein distance d ≤ 3** and **both verses ≥ 5
lexical tokens**, over `quran-text/quran-no-tashkeel.json`.

- **Waqf/pause marks stripped before tokenizing**, inheriting H-NEW-2380's disclosed instrument
  correction. **Locked codepoint set: U+06D6–U+06DE inclusive, plus U+06E9.**
- **Blocking is exact, not heuristic.** Each verse contributes its **4 rarest tokens** as blocking
  keys. If two verses of ≥ 5 tokens differ in at most 3 positions, at least one of any 4 chosen
  tokens must be shared, so **no qualifying pair can be missed**. (A prior draft blocked on tokens
  appearing in ≤ 400 verses, which had no such guarantee; it is discarded and disclosed in §9.)
- **Cross-surah only.** Same-surah repetition is the domain of H-NEW-2310/2330.
- **Measured pool size: n = 417**, distributed *d* = 0 : 59, 1 : 62, 2 : 69, 3 : 227.
  The *d* = 0 stratum is **59 exact Arabic twins** and supplies the translator-noise floor.

> **Pre-run correction, disclosed.** A first draft of this document reported n = 415 and the
> collinearity and tie figures that go with it. Those were measured under a probe whose waqf set
> **omitted U+06DE**, not under the set locked above. The document was corrected to the locked
> instrument's true numbers **before the SHA was embedded in the script and before any inferential
> statistic was computed** — no run had occurred, so this is a pre-lock correction, not an edit to a
> live registration. The 415-vs-417 pair is retained as sensitivity §7.1.

### §3.2 Predictors, from Levenshtein backtrace + QAC roots

Each pair's edit script is decomposed into three counts summing to *d*:

| predictor | definition | measured distribution |
|:--|:--|:--|
| **n_morph** | aligned **substitutions** where both tokens carry a QAC v0.4 ROOT and the roots are **equal** | 0 : 360, 1 : 50, 2 : 7 |
| **n_lex** | aligned **substitutions** where roots differ, or either root is absent | 0 : 108, 1 : 85, 2 : 95, 3 : 129 |
| **n_indel** | insertions + deletions | 0 : 299, 1 : 86, 2 : 27, 3 : 5 |

**Collinearity, reported here because cross-finding-030 mechanism 3 requires ρ(control, treatment)
beside every p:**

    ρ(n_lex, n_morph) = −0.3212     ρ(n_lex, d)    = +0.7653     ρ(n_morph, d)    = +0.0467
    ρ(n_lex, L_max)   = −0.3951     ρ(n_morph, L_max) = +0.1469  ρ(d, L_max)      = −0.1515

**ρ(n_lex, d) = +0.7653 is the single most dangerous number in this design.** `n_lex` is 77%
collinear with total edit distance, and H-NEW-3120 is the worked example of a control that removes an
effect *because it is the effect* — its p ran 0.0002 → 0.2541 as ρ went 0.00 → 0.91. **This design
therefore does not "control for d" in a regression; it stratifies on d exactly** (§4), so that the
contrast is estimated only among pairs with identical total Arabic difference and collinearity with
*d* cannot bleed in. **ρ(n_lex, d) will be reported beside every reported p.**

### §3.3 The outcome

For each pair and each of the ten languages: **token-Levenshtein distance between the two
translations**, after NFKC, casefold, removal of bracketed `[…]` and parenthetical `(…)` translator
glosses, and punctuation strip. Chinese is tokenized as **character bigrams** (it has no whitespace
word boundary); all others on whitespace. **This is a declared unit-drift exposure** — a Chinese
bigram spans ~2 morphemes where a Swedish token spans one — and it is neutralized by the
within-language ranking in §3.5, never by comparing raw magnitudes.

### §3.4 Three length channels — MANDATORY, worst is the headline

The outcome is an **edit count**, so it faces exactly the choice that moved H-NEW-3160's verdict by
3.96×: rank the count, or divide it by length. All three are run:

| channel | rule | **measured mean per-language tie fraction** |
|:--|:--|--:|
| **L1** | raw edit count | **0.9355** |
| **L2** | ÷ max(len₁, len₂) | 0.6942 |
| **L3** | ÷ mean(len₁, len₂) | 0.5480 |

**The headline is the WORST of L1, L2, L3.** The dominant channel is named in the finding.

**L1 is disclosed in advance as near-degenerate at 93.5% per-language ties, and it is NOT
excluded.** Excluding the worst channel would *raise* the chance of a pass, and per
`feedback_bonferroni_tightening_vs_loosening` a loosening cannot be self-ratified. If L1 decides the
verdict, that fact is the finding — as it was for H-NEW-3160.

### §3.5 Pooling across the ten languages — and the tie problem, measured

Per language, per length channel: values → **within-language percentile rank** (ties averaged). The
pooled outcome is the **median of the ten within-language ranks**. Ranking happens *within* language,
so §0.1(c)'s incommensurable units cancel.

**Tie fractions of the pooled outcome, measured before the lock:**

| channel | pooled-outcome tie fraction | per-language tie fraction |
|:--|--:|--:|
| L1 | 0.2830 | 0.9355 |
| L2 | 0.1607 | 0.6942 |
| L3 | 0.1199 | 0.5480 |

**The pooled outcome is below the 50% threshold on all three channels, so no exact test is mandated
for I1/I2. Every per-language input exceeds it, and L1 exceeds 90%.** Therefore:

- **I3, which operates on per-language quantities, uses an EXACT test** — the exact one-sided
  binomial sign test over the ten languages, which makes no distributional assumption and is
  unaffected by within-language ties.
- I1 and I2 use the **stratified permutation null of §4, which is exact by construction** conditional
  on the observed data. No normal-theory p-value is computed anywhere in this design.
- Tie fractions are recomputed at runtime and written to the run directory. **If any pooled-outcome
  tie fraction exceeds 0.50 at runtime, abort condition 5 fires (§8).**

### §3.6 Length block (nuisance)

`log(L_max)`, `log(L_min)`, `|L₁ − L₂|`, and `d` as a factor. Entered in every model; the contrast of
interest is estimated **within** *d*-strata.

## §4. The null, and why it is not a tautology-machine

**Permutation: within each stratum of *d*, shuffle the (n_morph, n_lex, n_indel) triples across
pairs.** Seed **20260509**, **10,000 permutations**.

Because every triple in a *d*-stratum sums to the same *d*, shuffling **preserves total Arabic
difference exactly** and **preserves the length block's relationship to d**, and breaks *only* the
association between the *composition* of the difference and the outcome. This is the null that makes
the question non-trivial: it asks whether *which kind* of difference matters, given *how much*
difference there is.

**This design is effect-size binding and its p-values are decorative**, exactly as H-NEW-3160
registered and observed. At n = 415 with a strong composition signal the permutation p will very
likely sit at the floor 1/10,001 = 9.999 × 10⁻⁵ on some channels. **A pass requires the effect-size
gates below; p alone can never carry an inference here.**

### §4.1 Control audit against cross-finding-030's three mechanisms

| mechanism | check | result |
|:--|:--|:--|
| **1 — does not DISCRIMINATE** | are the strata homogeneous in the thing they hold fixed? | The stratifier is *d*, an **exact integer count**, not a proxy. A *d* = 2 pair has exactly two differing token positions. There is no merger of unlike members of the kind that pooled `ير` *khayr* with `ير` *khabīr* in H-NEW-3150. Per-stratum outcome means are reported. |
| **2 — does not APPLY** | does the control exercise the feature the treatment does? | The control is the **same 415 pairs, same ten translations, same instrument**, with only the composition labels permuted. It cannot fail to exercise the feature. The *d* = 0 stratum additionally measures the translator-noise floor on **identical Arabic** — the feature at zero treatment. |
| **3 — DUPLICATES the treatment** | ρ(control, treatment)? | **ρ(n_lex, d) = +0.7644, reported beside every p.** This is why *d* is a stratifier and not a regressor. Within a stratum *d* is constant, so its correlation with `n_lex` is exactly **0 by construction** — the duplication is removed by design rather than absorbed by a covariate. |

## §5. Registered inferences (k = 3)

**I1 — PRIMARY. Composition contrast, d-stratified.**
Within-stratum standardized contrast **C = β(n_lex) − β(n_morph)** on the pooled outcome, pooled over
*d*-strata with stratum-size weights. Reported for L1, L2, L3; **headline = worst**.

**I2 — Lexical difference alone.** β(n_lex) > 0 within *d*-strata, `n_indel` and the length block
present. Headline = worst of the three channels.

**I3 — Per-language consistency (the claim ten translations can support and one cannot).** Compute
the I1 contrast **separately in each of the ten languages**. Registered: the contrast is **positive in
≥ 8 of 10** languages. Tested with the **exact one-sided binomial** sign test, H₀ : p = 0.5,
requiring P(X ≥ 8 | n = 10, p = 0.5) = 0.0546875 … which **exceeds α = 0.0166667**, so ≥ 8/10 alone
cannot pass. **The registered threshold is therefore ≥ 9 of 10** (exact p = 0.0107421875 < α). This
correction is made here, before the run, because the 8/10 version is arithmetically incapable of
passing at the family α.

## §6. Decision rule

### §6.1 PASS requires ALL of the following, per inference

1. **Direction** matches §2's lock (positive contrast; positive β for I2).
2. **Permutation p < α = 0.05 / 3 = 0.0166667** on the **worst** of the three length channels.
3. **Effect-size floor:** ΔR² of the composition block over the length + *d* + `n_indel` block
   **≥ 0.01** on the **worst** channel. *Floor inherited verbatim from H-NEW-3160 §6.1; not tuned
   here.*
4. **Length-rule floor:** the effect must exceed **ΔR²_lengthrule** — the variance commanded by the
   arbitrary choice among L1/L2/L3, computed rather than asserted, per cross-finding-029.

For **I3** the gate is the exact binomial threshold of §5 (≥ 9 / 10), and gates 3–4 do not apply.

### §6.2 Verdict

Survivors of {I1, I2, I3}: **3 → CONFIRMED · 2 → SUPPORTED · 1 → PARTIAL · 0 → NULL.**

**I1 is primary. If I1 fails, the ceiling is PARTIAL regardless of I2 and I3.**

### §6.3 Reverse direction

If any channel returns the **reverse** sign with permutation p < α under the mirrored one-sided test,
the finding reports **REVERSED** at full prominence and the hypothesis is refuted, not merely
unsupported.

### §6.4 If NULL — mandatory MDE and power reporting

A NULL must state its MDE and power, per cross-finding-029 §3.2. The finding will report:

- **MDE**: the smallest contrast C detectable at 80% power under the §4 permutation null, by
  simulation on the observed design matrix.
- **The S\* vs S_max branch, computed and not asserted.** `n_morph` takes only the values {0, 1, 2}
  and is non-zero in **57 of 417 pairs**. The design's power to estimate β(n_morph) is bounded by
  that support. The finding will report **S\*** — the observed contrast — against **S_max**, the
  largest contrast attainable on this design matrix under the most favourable assignment of the
  observed outcome values. **If S\* < required floor but S_max also < required floor, the design was
  incapable of rejecting and the result is UNTESTABLE, not NULL.** That distinction will be computed;
  asserting it either way would be wrong.

### §6.5 If the criteria disagree

If p passes and the effect-size floor fails, the verdict is **NULL** and the finding says so in its
first paragraph. The effect size is binding. This is H-NEW-3160's rule and it is inherited unchanged.

## §7. Sensitivities — NON-CONFIRMATORY, reported whatever they show

1. **Waqf codepoint set.** U+06D6–U+06DE + U+06E9 (locked, **n = 417**) against the reading that omits
   U+06DE rub-el-ḥizb (**n = 415**). A 0.5% instrument sensitivity; both reported.
2. **Pool width.** (d ≤ 2, L ≥ 8) — H-NEW-2380's own locked window, **which this lane's rebuild
   reproduces exactly at 32 pairs** — and (d ≤ 3, L ≥ 8) at 64 pairs.
3. **Drop the English arm**, which §0.1(a) shows is not independent of H-NEW-710. Nine-language rerun.
4. **Hand-check, in both directions.** A sample of pairs where the ten translations **AGREE** is
   hand-read, not only where they disagree — *disagreements advertise themselves; shared errors do
   not.* Minimum 10 agreeing pairs and 10 disagreeing pairs, reported with verdicts whatever they show.
5. **Leave-one-language-out**, all ten.
6. **QAC root-absence.** `n_lex` absorbs substitutions where a root is missing. Rerun counting only
   substitutions where **both** tokens carry a root.

## §8. Frozen inputs and abort conditions

**Frozen inputs**, SHA-256 hashed into the run directory: `quran-text/quran-no-tashkeel.json`;
`data/morphology/quranic-corpus-morphology-0.4.txt`; the ten `dist/quran_<lang>.json`.

**Abort — the script exits non-zero and writes no verdict if:**

1. This file's SHA-256 ≠ `EXPECTED_PREREG_SHA` embedded in `scripts/h-new-3190.py`.
2. Any translation file has ≠ 114 surahs or ≠ 6,236 verses, or any empty translation.
3. The pool size is not within 417 ± 5 under the locked waqf set.
4. `n_morph + n_lex + n_indel ≠ d` for any pair.
5. Any pooled-outcome tie fraction exceeds **0.50** at runtime (would mandate a redesign, per §3.5).
6. The run directory already exists (`os.makedirs(exist_ok=False)`); all outputs `open(..., 'x')`.

**No run directory is ever deleted.**

## §9. Forking-paths log — every choice made before the lock

1. **Whether the work already existed** — checked FIRST, per the binding rule. §0. F-18 open.
2. **NM-41's top-50 Jaccard seed rejected.** Top-50 of ~19.4M pairs is a needle whose null overlap is
   ≈ 0, making its 15%/30% bands unanchored. Replaced with a pair-level design on an exact pool.
3. **Exact-identity "collapse depth" rejected after probing it.** `probe_outcome.py` returned collapse
   depths of 1/10, 0/10, 0/10 on H-NEW-2380's own exemplars — a degenerate, tie-saturated outcome.
   **Discarded before locking.** Had it been locked unprobed, this lane would have reported a
   guaranteed NULL produced entirely by instrument failure.
4. **Blocking rule changed** from "tokens in ≤ 400 verses" (heuristic, no completeness guarantee) to
   "4 rarest tokens per verse" (**provably complete** for d ≤ 3). §3.1.
5. **d as stratifier, not regressor** — chosen because ρ(n_lex, d) = +0.7644 and H-NEW-3120 shows what
   a collinear control does to a p-value. §4.1.
6. **Within-language ranking before pooling** — chosen because §0.1(c) shows raw cross-language
   magnitudes are incommensurable (zh 245k chars vs bn 796k).
7. **L1 retained despite 93.5% ties** — excluding the worst channel would loosen the test.
8. **I3 threshold raised 8/10 → 9/10** before the run, because 8/10's exact binomial p = 0.0547
   cannot clear α = 0.0167. A tightening; self-ratifying per
   `feedback_bonferroni_tightening_vs_loosening`.
9. **Effect-size floor 0.01 inherited from H-NEW-3160, not tuned.**
10. **The §0.2 contamination** — marginal direction seen before locking; handled by removing the
    marginal from the registered set entirely.
11. **Chinese character-bigram tokenization** — declared unit drift, neutralized by ranking (§3.3).
12. **Translator-identity claims restricted to slug level** — §0.1(b).
13. **Pre-run correction of n = 415 → 417**, disclosed inline in §3.1. Made before the SHA was
    embedded and before any inferential statistic existed.
14. **§5's "n_indel … present" clause is ambiguous and is resolved conservatively.** Within a
    *d*-stratum `n_lex + n_morph + n_indel = d` exactly, so an intercept plus all three counts is
    rank-deficient and the clause has no unique reading. Both full-rank readings are computed —
    (a) intercept + `n_lex` + `n_morph`, `n_indel` as omitted reference; (b) no intercept +
    all three — and **I2 takes the WORSE of the two**. **I1 is unaffected: the contrast
    β(n_lex) − β(n_morph) is algebraically identical under both** (in (b), model =
    p·n_lex + q·n_morph + r·n_indel = r·d + (p−r)·n_lex + (q−r)·n_morph, so the contrast is p − q
    either way). ΔR² is a model comparison and is likewise invariant.
15. **"Worst channel" is applied PER GATE**, not by selecting one channel and reading all its gates:
    direction uses the smallest effect, *p* the largest, ΔR² the smallest, each across L1/L2/L3.
    This is the most conservative reading of §3.4 + §6.1 and cannot select a favourable channel.
16. **ΔR²_lengthrule is defined as max − min of ΔR² across L1/L2/L3.** H-NEW-3160 reports the
    quantity but does not pin a formula; this one is declared here as a deciding parameter.

## §10. What would make me wrong

- If the contrast vanishes within *d*-strata while surviving marginally, the §0.2 gradient was **total
  Arabic difference all along**, and the lexical/morphological distinction adds nothing.
- If the contrast is carried by ≤ 2 languages, "ten translations" bought nothing and the honest
  reading is a single-translation artefact — which is why I3 exists.
- If **n_morph pairs are systematically shorter or from a different register** than n_lex pairs, the
  length block will not save the design; §7.2's narrower windows are the check.
- If the *d* = 0 translator-noise floor is as large as the treatment contrast, the instrument cannot
  resolve the question at this pool size, and §6.4's S\* / S_max branch should return **UNTESTABLE**.
- **The deepest limit, stated plainly:** this measures a property of *how ten translators worked*, not
  a property of the Quran. F-18 itself records "no applicable classical anchor; this is a modern
  methodological question." A positive result says Arabic root-level distinctions are the ones that
  survive re-encoding by human translators. It does **not** say the morphological distinctions are
  meaningless in Arabic — only that they are invisible at translation granularity.
