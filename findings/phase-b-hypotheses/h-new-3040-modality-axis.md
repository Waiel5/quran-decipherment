---
id: H-NEW-3040
title: The modality axis — a RE-DERIVATION of H-NEW-2640 on a different estimator; the deontic half is DIRECTIONAL not established, the orthogonality claim fails, and the epistemic half reproduces H-NEW-2640's directional failure once narrative is put back
date: 2026-08-09
phase: B
author: Waiel Al-Shujaa
frontier_item: F-10 (HANDOFF/FRONTIER-MAP-2026-08-07.md lines 248-254) — the map listed
  F-10's prior as CONFIRMED and "genuinely orthogonal to what has been done." Both are wrong.
verdict: >
  H1 DEONTIC SEPARATION — DIRECTIONAL, not PASS. The pre-registered arm passes (p = 0.0021)
  but only 3 of 8 length-control arms clear alpha_bon = 0.025, the locked channel was NOT
  the dominant one for this grouping, and H-NEW-2640's own channel pair returns p = 0.0649.
  H2 ORTHOGONALITY — NOT SUPPORTED and NOT REFUTED. rho = -0.2797, 95% CI
  [-0.4407, -0.1062], perm p = 0.0032; equivalence INDETERMINATE at every bound.
  Agrees with H-NEW-2640's I3: cross-finding-028 gets no fifth modality column.
status: RE-DERIVATION of H-NEW-2640 · H1 DIRECTIONAL · H2 NOT SUPPORTED
replicates: H-NEW-2640 (I1, I3, and the §5-P4 post-hoc pooled estimator)
prereg: findings/phase-b-hypotheses/prereg-h-new-3040-modality-axis.md
prereg_sha256: 48e02a04a252e91dac41cd747968e769c6a28379a1cbd85582bf2a2161e353df
script: findings/phase-b-hypotheses/scripts/h-new-3040.py
run: findings/phase-b-hypotheses/runs/h-new-3040/20260809T070448Z/
posthoc_runs:
  - runs/h-new-3040/20260809T070806Z-posthoc/
  - runs/h-new-3040/20260809T070853Z-posthoc-densities/
  - runs/h-new-3040/20260809T071637Z-posthoc-channels/
parents: [H-NEW-2640, cross-finding-028-formal, H-NEW-2530, H-NEW-3010]
seed: 20260509
n_perm: 10000
---

# H-NEW-3040 — The modality axis

> ## ⛔ PRIOR WORK — READ BEFORE THE VERDICT: this is largely a RE-DERIVATION of H-NEW-2640
>
> **`h-new-2640-modality-register.md`, dated 2026-08-07, pre-registered and rejected this
> hypothesis already.** Ledger §10.148. Its title is *"The ṭalab/khabar division, measured and
> not found."* Its verdict is **NULL on all four registered inferences**, and its closing line
> is *"cross-finding-028-formal still has no mood feature, and on this evidence it should not
> have one."* **I did not grep for it before designing this test.** The frontier map listed
> F-10's prior as *CONFIRMED* and *"genuinely orthogonal to what has been done"*; it was neither.
>
> **The two runs agree on the instrument, to within 5 tokens.** Independent
> reimplementations of the jussive trigger split:
>
> | | prohibitive `lā` | lām al-amr | *lam*-negation | deontic total | deontic % of 1,418 |
> |:--|--:|--:|--:|--:|--:|
> | H-NEW-2640 | 330 | 78 | 351 | 408 | 28.8 % |
> | **H-NEW-3040 (this run)** | **335** | **78** | **355** | **413** | **29.1 %** |
>
> **They agree on the orthogonality answer.** H-NEW-2640's I3 found modality makes the
> cross-finding-028 classifier *worse* (Δ = −0.0879, direction reversed). This run finds the
> two axes significantly *correlated* (ρ = −0.2797, p = 0.0032). Different statistics, same
> conclusion: **cross-finding-028 gets no fifth column.**
>
> **They disagree on the deontic half, and §4 shows the disagreement is a length-channel
> artefact plus an estimator change — not new evidence.**
>
> **What is genuinely new here, and it is narrow:**
> 1. **The Arabic Itqān locus.** H-NEW-2640 cited the English translation (pp. 127, 249) and
>    recorded al-Sakkākī as absent. The Arabic *Itqān* **nawʿ 57 *fī al-khabar wa-l-inshāʾ*,
>    vol. III pp. 255–257** is on disk, unused, and is the primary-source locus for the
>    division. §6.
> 2. **The pre-registered version of H-NEW-2640's post-hoc P4.** Its §5 said the pooled
>    deontic result *"licenses a new pre-registration, not a rescued verdict."* This is that
>    pre-registration — and §4 shows what it actually returns, which is weaker than P4 implied.
> 3. **Orthogonality stated as an equivalence test with a locked bound and a confidence
>    interval**, rather than as a classifier delta. §5.
> 4. **The `f_iltifat_type` grammatical-entailment analysis.** §2.
> 5. **The channel-dominance ranking for the legal↔eschatological grouping.** §4.1.
>
> **What is NOT new, and I published it as though it were:** the three QAC field corrections
> in §3.1 (`POS:EMPH` does not exist; `POS:FUT` = 42 of 161; `POS:PRO` substring-matches
> `POS:PRON` at 3,633). **H-NEW-2640 §7 published all three on 2026-08-07**, including the
> 10.9× inflation figure. My §3.1 is an independent confirmation, not a discovery, and my
> first report of this work described it as a correction I had found. That is recorded in §8.

---

## 1. Verdicts

| | claim | verdict |
|:--|:--|:--|
| **H1** | legal register is more deontic than eschatological | **DIRECTIONAL** — locked arm p = 0.0021, but **3 of 8** length-control arms clear α_bon |
| **H2** | the modality axis is orthogonal to cross-finding-028's axis | **NOT SUPPORTED** (ρ ≠ 0 at p = 0.0032) **and NOT REFUTED** (equivalence INDETERMINATE at every bound) |

`INVESTIGATION-PROTOCOL.md` §8: *if any gate fails, the verdict is DIRECTIONAL or NULL, not
CONFIRMED.* H1 fails the length gate under five of eight controls, so it is **DIRECTIONAL**.
My first report called it PASS. That was wrong, and §8 records it.

---

## 2. THE FEATURE INTERSECTION — the gating check, reported first

### 2.1 cross-finding-028's exact feature list

Verbatim from `csv/h-new-2530.json` → `features` / `feature_sources`:

| # | feature | definition as frozen | token class read |
|:-:|:--|:--|:--|
| 1 | `f_idh` | `h-new-2520.json per_surah.idh / V`; word-1 `POS:T`, `LEM` exactly `<i*` | time-adverb إذ |
| 2 | `f_lamma` | `h-new-2520.json per_surah.lamma / V`; word-1 `POS:T LEM:lam~aA` | time-adverb لمّا |
| 3 | `f_qalu` | `h-new-2520.json per_surah.qalu / V`; word-1 `POS:V ROOT:qwl LEM:qaAla PERF 3MP` | perfect verb قالوا |
| 4 | `f_idha_cascade` | `h-new-2250.json runs.idha Σlength / V`; word-1 `POS:T LEM:<i*aA` | time-adverb إذا |
| 5 | `f_doubling` | `h-new-2490.json verse_grain_roster membership (binary)` | surah-level binary, 6 surahs |
| 6 | `f_iltifat_type` | `h-new-2390.json all_loci, 2500 type_tags: (n31−n23)/(n31+n23)` | **person and number** of any person-bearing word |

Features 1–3 re-derived from QAC against the frozen vectors: **342/342 cells, 0 mismatches.**

### 2.2 The intersection, with sizes

| level | size |
|:--|--:|
| feature-name intersection | **0** |
| **segment-level intersection** (all 28 pairs, features 1–4 × modality features) | **0 segments** |
| word-level intersection with features 1–4 | **1 word of 77,429** (one `f_qalu` word also carrying `l:EMPH`) |
| modal verbs governed by an إذ / لمّا / قالوا / إذا marker | **0** |
| modal verbs with such a marker within 5 preceding words | 21 of 1,418 (1.5 %) |
| **word-level intersection with `f_iltifat_type`** | **1,013 / 1,418 jussives (71.4 %)**; 1,001 / 1,330 subjunctives (75.3 %) |

**The intersection with features 1–5 is EMPTY. The intersection with feature 6 is NOT, and I
say so plainly.**

The 71.4 % is at base rate — 68.8 % of all verbs and 64.3 % of all imperfect verbs are
iltifāt-locus endpoints, because the feature is computed over every person-bearing word. **So
the count is not the problem. The grammar is:**

| deontic category | 1st person | 2nd person | 3rd person |
|:--|--:|--:|--:|
| prohibition (لا الناهية), n = 335 | 0 (0.0 %) | **308 (91.9 %)** | 27 (8.1 %) |
| command (لام الأمر), n = 78 | 1 (1.3 %) | 0 (0.0 %) | **77 (98.7 %)** |

`f_iltifat_type = (n31 − n23)/(n31 + n23)` is a 3↔1-versus-2↔3 **person** contrast, and Arabic
prohibition is 2nd-person by default while lām al-amr is 3rd-person by default. **Token sets
disjoint; grammar not.** This is the H-NEW-206 shape — a feature partly predicting itself —
and it is labelled here rather than published around.

### 2.3 What I did about it — decided before any correlation was computed

Two arms, locked in prereg §3.5:

- **ARM B — 5 features, `f_iltifat_type` dropped. Carries the orthogonality verdict.**
- **ARM A — all 6 features. The axis cross-finding-028 actually uses. Reported in full; may
  NOT establish an orthogonality verdict.**

**The data confirmed the reason for the split:**

| | ARM B | ARM A |
|:--|--:|--:|
| marginal ρ(M, R) | −0.2797 | **−0.3712** |
| ρ(R, log word count) | +0.6601 | +0.5591 |
| partial ρ controlling log word count | −0.0807 | −0.2340 |
| **share of marginal removed by length** | **71.1 %** | **37.0 %** |

Arm A correlates *more* while being *less* length-driven. The excess is person — the channel
§2.2 predicted from grammar before the number existed. **Had feature 6 been left in, the
orthogonality test would have read a grammatical entailment as an empirical association.**

---

## 3. The instrument

### 3.1 QAC counts — verified; the field corrections are NOT novel (see banner)

All six frontier-map counts are correct: `MOOD:JUS` 1,418 · `MOOD:SUBJ` 1,330 · `PRO` 332 ·
`CERT` 414 · `FUT` 161 · `EMPH` 1,244. Corpus: 128,219 segments, 77,429 words, 6,236 verses.
Counted as `POS:*` they fail — `POS:FUT` → 42, `POS:EMPH` → 0, `POS:PRO` → 3,633 (matches
`POS:PRON`, 10.9× inflation). **H-NEW-2640 §7 established all three on 2026-08-07.** Also:
`MOOD:IND` = 0, so QAC marks mood only where SUBJ or JUS.

### 3.2 The jussive trigger split (W = 5), and how it differs from H-NEW-2640

| trigger | n | % |
|:--|--:|--:|
| `negation_lam` (لم / لمّا) — no modal content | 355 | 25.0 % |
| `conditional` | 343 | 24.2 % |
| **`prohibition_la` — deontic** | **335** | 23.6 % |
| unassigned | 297 | 20.9 % |
| **`command_lam_amr` — deontic** | **78** | 5.5 % |
| `sub_an_kay` | 10 | 0.7 % |

Window-insensitive where it matters: across W ∈ {3, 5, 8, 40} the deontic pole moves only
330 → 337 and `command_lam_amr` is constant at 78.

**The pole compositions differ substantially from H-NEW-2640, and this is half the reason the
two runs disagree:**

| | H-NEW-2640 | H-NEW-3040 (this run) |
|:--|:--|:--|
| **D** | `IMPV (1,876) + prohibitive (330) + lām al-amr (78) + IMPN (2)` = **2,286** | `prohibitive (335) + lām al-amr (78)` = **413** — **no imperative verbs** |
| **E** | `CERT + l:EMPH + n:EMPH + FUT + inna (1,682)` = **3,501** | `CERT + FUT + l:EMPH + lan-SUBJ` = **1,684** — **no nūn al-tawkīd, no *inna*** |
| statistic | unweighted mean of per-surah per-1,000-token densities | `M = log((D + 0.5)/(E + 0.5))` — no unit count in the denominator |
| test | 3-way ANOVA argmax over narrative / legal / eschatological | 2-group contrast, **legal vs eschatological only** |

My D is **18 %** of theirs and my E is **48 %** of theirs.

---

## 4. H1 — and the length control, which is where it breaks

### 4.1 The channel I locked was NOT the dominant one for this grouping

`UNIT-DRIFT-DEFECT.md` §5: *rank the candidate nuisance channels on the data before locking
one as primary*, and *a control that does not use the strongest channel is not a control*.
Prereg §6.1 ranked the channels against **cross-finding-028's features**. It did **not** rank
them against **the grouping**. Post-hoc, over the 45 labelled surahs:

| channel | ρ with the LEGAL/ESCHAT grouping | ρ with `M` |
|:--|--:|--:|
| **mean verse length** | **+0.8400 ← dominant** | −0.1138 |
| log word count ← **what I locked** | +0.6423 | −0.3372 |
| mushaf position | −0.6176 | +0.2898 |
| verse count / log verse count | +0.1147 | −0.3743 |

**I locked the second-strongest channel.** This is the same error `UNIT-DRIFT-DEFECT.md` §3
records against its own drift table.

### 4.2 The swing — 58×, and 5 of 8 arms fail

Post-hoc, prompted by H-NEW-3010 (F-3), which found a 70× swing on the same kind of contrast:

| length control | Δ | p | verdict at α_bon = 0.025 |
|:--|--:|--:|:--|
| none (raw) | +0.392 | 0.1226 | NULL |
| **log word count — THE PRE-REGISTERED PRIMARY** | **+27.858** | **0.0021** | **PASS** |
| mushaf position | +25.660 | 0.0040 | PASS |
| **mean verse length — the dominant channel** | **+22.536** | **0.0098** | **PASS** |
| verse count | +18.678 | 0.0266 | NULL — fails by 0.0016 |
| log verse count | +18.678 | 0.0266 | NULL |
| **all four channels together** | +15.867 | **0.0496** | **NULL** |
| **H-NEW-2640's own pair [log V, mean words/verse]** | +14.403 | **0.0649** | **NULL** |

**p ranges 0.0021 → 0.1226, a 58× swing. 3 of 8 arms PASS.**

Two things must be said in the same breath.

- **In favour:** the direction is Δ > 0 in **all eight** arms — no pre-commit violation
  anywhere, and the sign is completely stable. And the **dominant** channel passes
  (p = 0.0098), which is the arm `UNIT-DRIFT-DEFECT.md` §5 says a control must use.
- **Against, and decisive for the verdict:** the two **multi-channel** controls fail
  (0.0496, 0.0649), and **H-NEW-2640's exact channel pair returns p = 0.0649** — so the
  disagreement between this run and its parent is substantially *which channel was locked*,
  not new evidence. Per `UNIT-DRIFT-DEFECT.md` §6 rule 6 — *if two nulls disagree, report both
  and take the stricter* — the stricter arms fail.

**H1 is DIRECTIONAL. It is not established.**

### 4.3 The rules-tuple fragility — H1 rides on one particle

| tuple | change | Δ | p | verdict |
|:--|:--|--:|--:|:--|
| RT-1 primary | — | +27.858 | 0.0021 | PASS |
| RT-2 | cross-finding-028's own labels | +26.875 | 0.0006 | PASS |
| **RT-3** | **`E` excludes `l:EMPH`** | **+6.130** | **0.2656** | **NULL** |
| RT-4 | trigger window W = 40 | +27.695 | 0.0021 | PASS |
| RT-5 | bounded contrast | +27.858 | 0.0021 | **tautology — see §7.1** |

Leave-one-component-out on the epistemic pole, and per-1,000-word densities by register:

| epistemic pole | E | Δ | p | | component | LEGAL (17) | ESCHAT (28) | L/E |
|:--|--:|--:|--:|:-:|:--|--:|--:|--:|
| full | 1,684 | +27.858 | 0.0021 | | `D` prohibition | 6.486 | 1.526 | **4.25×** |
| drop `CERT` | 1,270 | +35.184 | 0.0004 | | `D` command | 1.730 | 0.954 | 1.81× |
| drop `FUT` | 1,523 | +27.427 | 0.0021 | | `E` CERT (قد) | 5.228 | 4.960 | 1.05× |
| **drop `l:EMPH`** | **683** | **+6.130** | **0.2656** | | `E` FUT (س/سوف) | 1.690 | 1.908 | 0.89× |
| drop `lan`-SUBJ | 1,576 | +29.220 | 0.0019 | | `E` `l:EMPH` (لـ) | 8.020 | 12.591 | **0.64×** |
| | | | | | `E` `lan`-SUBJ | 2.005 | 0.572 | **3.50× reversed** |

**The deontic pole behaves as predicted** (prohibition 4.25×, command 1.81×). **The epistemic
pole does not**: قد flat, س/سوف flat, لن-subjunctive **backwards**. Only `l:EMPH` carries
register information, and removing it destroys H1.

### 4.4 THE SELF-REFUTATION — H1 survives only because narrative was excluded

H-NEW-2640's §5-P4 found the epistemic half fails on **direction**: narrative, not
eschatological, is the most emphatically-marked register. **My design excluded narrative** —
H1 compares 17 legal against 28 eschatological surahs and leaves 69 out.

**Put narrative back, with my own pole definitions, on cross-finding-028's own labels
(pooled per 1,000 words):**

| index | narrative | legal | eschatological | argmax | vs H-NEW-2640's lock |
|:--|--:|--:|--:|:--|:--|
| `D` deontic | 4.42 | **7.77** | 2.92 | legal | ✓ matches |
| **`E` epistemic** | **26.65** | 16.88 | 23.98 | **NARRATIVE** | ✗ **fails, exactly as H-NEW-2640 found** |

Surah-unweighted, `E` gives eschatological 28.26 > narrative 26.21 — but pooled it reverses.
**My own data reproduces H-NEW-2640's epistemic directional failure.** My H1 does not
contradict it; **my H1 never tested against the register that falsifies it.**

That is the honest reading of the DIRECTIONAL verdict: *what survives is the deontic half —
legal contexts are denser in prohibition and command. The epistemic half is not supported by
this run either, and the appearance that it was came from a design that excluded its
strongest counterexample.*

---

## 5. H2 — orthogonality, with the bound and the interval

**Locked equivalence bound: δ = 0.25** (prereg §7.2), with δ = 0.20 and δ = 0.30 also
reported. Three-way rule, locked before the run: **ORTHOGONAL** iff the whole 95 % CI lies
inside [−δ, +δ]; **NOT-ORTHOGONAL** iff it lies wholly outside; **INDETERMINATE** otherwise.

| arm | ρ | bootstrap 95 % CI | Fisher CI | perm p | δ = 0.20 / 0.25 / 0.30 |
|:--|--:|:--|:--|--:|:--|
| **ARM B** (verdict-bearing) | **−0.2797** | **[−0.4407, −0.1062]** | [−0.4499, −0.0899] | **0.0032** | INDETERMINATE ×3 |
| ARM A (fidelity only) | −0.3712 | [−0.5306, −0.1996] | [−0.5277, −0.1902] | 0.0001 | INDETERMINATE ×3 |

**The interval excludes zero → F-10's orthogonality claim does not stand. The interval is not
wholly outside any bound → "the correlation is negligible" is not established either.** Both
readings unavailable; the locked name for that is INDETERMINATE.

**Arm A misses NOT-ORTHOGONAL at δ = 0.20 by 0.000424** (CI high −0.199576 against −0.200000).
At that resolution the answer is bootstrap noise; the honest reading is that Arm A sits on the
boundary.

**The power limit, computed and published BEFORE the run.** At n = 114 the Fisher-z 95 %
half-width is 0.19720, so ρ̂ = 0 yields CI [−0.1947, +0.1947]. Equivalence could pass only if
|ρ̂| ≤ **0.0055** (δ = 0.20), ≤ **0.0582** (δ = 0.25), ≤ **0.1119** (δ = 0.30). **n = 114
surahs cannot establish orthogonality below ≈ 0.20 whatever the data say.** That is ignorance,
and it is reported as ignorance.

**What the two axes share is length, not register:**

| control | ARM B ρ | CI | covers 0 |
|:--|--:|:--|:--|
| none | −0.2797 | [−0.4407, −0.1062] | no |
| **log word count** | **−0.0807** | **[−0.2768, +0.1206]** | **yes** |
| verse count | −0.0697 | [−0.2709, +0.1389] | yes |
| mean verse length | −0.2577 | [−0.4179, −0.0819] | no |
| mushaf position | −0.1316 | [−0.3246, +0.0701] | yes |
| **register (3-level)** | **−0.2556** | **[−0.4261, −0.0711]** | **no** |

Length removes 71.1 %; register removes almost nothing. Product-of-loadings from length alone,
(−0.3372) × (+0.6601) = −0.2226, is **79.6 %** of the observed −0.2797.

**Per-feature** (k = 6, α = 0.008333): `f_iltifat_type` −0.3301 (p = 0.0006)✓,
`f_qalu` −0.3270 (0.0004)✓, `f_lamma` −0.2615 (0.0050)✓, `f_idh` −0.1276 (0.1755),
`f_idha_cascade` −0.0375 (0.7007), `f_doubling` +0.0024 (0.9841). Max |ρ| = 0.3301.

**Out of sample the axes are near-independent:** multiple R = 0.3054 (Arm B), R² = 0.0933,
**LOOCV R² = 0.0080**. Arm A: 0.3948 / 0.1559 / 0.0550. **The five-feature axis predicts 0.8 %
of the modality axis out-of-sample** — the strongest thing sayable in F-10's favour, and it is
a *predictive* statement, not the correlational one F-10 made. PC1 explains only 34.4 %
(B) / 32.4 % (A) of feature variance, so `R` is a weak scalar.

**This agrees with H-NEW-2640's I3** (Δ = −0.0879, modality makes the classifier worse,
p = 0.9622). Two different statistics, one conclusion: **cross-finding-028 gets no fifth
modality column.**

---

## 6. Classical anchor — the one genuinely new contribution

`find data findings -iname "*sakkak*" -o -iname "*miftah*"` → **no results.** al-Sakkākī is
genuinely absent; H-NEW-2640 said so and it is right. H-NEW-2640 then used the **English**
Itqān PDF (pp. 127, 249). The **Arabic** Itqān is on disk and has the dedicated nawʿ:

> **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, النوع السابع والخمسون: في الخبر والإنشاء
> (nawʿ 57), vol. III pp. 255–257.**
> `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, heading line 17808;
> `PageV03P255` (17807), `PageV03P256` (17824), `PageV03P257` (17841).

- «وقال كثيرون ثلاثة خبر وطلب وإنشاء قالوا لأن الكلام إما أن يحتمل التصديق والتكذيب أو لا
  الأول الخبر» — *khabar* is what admits affirmation or denial.
- «إن أفاد بالوضع طلبا … والأول الاستفهام والثاني الأمر والثالث النهي» — ṭalab is
  interrogation, **amr**, **nahy**: exactly the deontic pole.
- «الخبر الكلام الذي يدخله الصدق والكذب» — attributed to al-Qāḍī Abū Bakr and the Muʿtazila.

**And the same passage supplies this test's sharpest limit**, locked in the prereg rather than
found afterwards: «القصد بالخبر إفادة المخاطب **وقد يرد بمعنى الأمر** نحو: {والوالدات يرضعن}
{والمطلقات يتربصن} **وبمعنى النهي** نحو: {لا يمسه إلا المطهرون}». Khabar form routinely
carries amr and nahy force, and al-Suyūṭī's examples (Q 2:233, 2:228, 56:79) are core legal
verses in indicative form. **This instrument measures form; the source documents that legal
force travels in non-deontic form, disproportionately in the legal register.** That biases H1
toward the null.

---

## 7. Controls — one was arithmetic, one could have killed the finding and did not

### 7.1 RT-5 is a tautology, withdrawn

The bounded contrast and the smoothed log-ratio give Δ = +27.858, p = 0.0021 — identical to
RT-1 to five decimals. Checked: **identical ranking of all 114 surahs, 0 differing,
ρ = 1.00000000.** Every rank statistic must agree by construction. **RT-5 is withdrawn as
evidence of robustness.** RT-2's H2 numbers are likewise identical to RT-1's by construction,
H2 using no register label. **Effective independent rules-tuples: 3, not 5.**

### 7.2 The oath tautology — checked, REFUTED

Eight of 28 eschatological surahs carry *oath* in their own label (51, 52, 77, 79, 81, 85, 86,
89), and jawāb al-qasam takes the emphatic lām, which is 59.4 % of the epistemic pole.
Removing all eight makes H1 **stronger** (Δ +27.858 → +31.038, p 0.0025), and `l:EMPH` is
**depleted** there (0.80×). A control that could have destroyed the finding did not.

---

## 8. What I got wrong — at full prominence

1. **I did not grep for prior work before designing the test.** H-NEW-2640 answered this
   hypothesis on 2026-08-07 with a NULL, and I re-derived it. This is the third instance in
   two days (F-3 → H-NEW-2630; the lead's H-NEW-46 re-derivation).
2. **I reported H1 as PASS. It is DIRECTIONAL.** Five of eight length-control arms fail
   α_bon, including both multi-channel arms and H-NEW-2640's own pair.
3. **I locked one length channel a priori, and it was not the dominant one.** Mean verse
   length is dominant for this grouping (ρ = +0.8400); I locked log word count (+0.6423). I
   ranked channels against cross-finding-028's *features* and never against *the grouping*.
   H-NEW-3010 published the 70× swing warning **the same day**, and my prereg cites
   `UNIT-DRIFT-DEFECT.md` §5 while committing the error it names.
4. **I presented three QAC field corrections as findings.** H-NEW-2640 §7 published all three,
   including the 10.9× figure, two days earlier.
5. **I excluded narrative and did not flag that this removes the epistemic half's strongest
   counterexample.** §4.4 shows my own data reproduces H-NEW-2640's directional failure once
   narrative is restored.
6. **My first report cited "14.9 %" for W = 40 unassigned jussives; it is 15.1 %.** Corrected.

---

## 9. Honest limits

1. H1 is DIRECTIONAL, not established (§4.2). H2's orthogonality is neither supported nor
   refuted (§5).
2. H1 rides on one particle class, `l:EMPH` (§4.3). Two of the four modal-particle classes
   F-10 named carry no register information; `lan`-subjunctive runs backwards.
3. Effective independent rules-tuples: 3, not 5 (§7.1).
4. `M` is not length-free in practice (ρ = −0.3372 with log word count) despite carrying no
   unit count in its denominator. *Normalisation is not invariance.*
5. Form, not force — al-Suyūṭī's own qualification (§6).
6. 20.9 % of jussives are `unassigned` at W = 5 (15.1 % at W = 40); they enter neither pole.
7. Register labels are surah-scale; Q 2 is both legislative and narrative.
8. Three of cross-finding-028's six features were consumed from frozen JSON without
   re-derivation (`f_idha_cascade`, `f_doubling`, `f_iltifat_type`). Features 1–3 matched
   342/342.
9. `f_doubling` is a 6-surah binary; its PC1 contribution is near-degenerate.
10. H1 and H2 are computed on different samples (45 labelled vs all 114).
11. **NO CROSS-CORPUS BASELINE WAS RUN.** Nothing here distinguishes this corpus from ḥadīth,
    adab prose or pre-Islamic poetry.
12. cross-finding-028 carries a live correction notice (2026-08-07); its six feature vectors
    reproduce and are not retracted, which is all this run used, **but no result here may be
    reported as evidence that this corpus is structurally unusual.**

---

## 10. What this changes

- **F-10 must not become a fifth pillar for cross-finding-028.** Two independent runs on
  different statistics now say so — H-NEW-2640's I3 and this run's H2.
- **The frontier map's F-10 entry is wrong on both counts** ("Prior. CONFIRMED. Genuinely
  orthogonal to what has been done"). It was already executed, and it was NULL.
- **The surviving claim is narrow and pooled:** prohibition (لا الناهية) is **4.25×** denser
  in the legal register than the eschatological per 1,000 words, and **2.66×** on
  cross-finding-028's labels. That is a *deontic-marker* claim, not a mood-system claim, and
  it should be tested directly rather than through a ratio against an epistemic pole that
  does not separate.
- **`UNIT-DRIFT-DEFECT.md` §3 gains a grouping row:** legal↔eschatological, dominant channel
  **mean verse length ρ = +0.8400**, median word count 539 against 173 (3.12×).
- **The standing rule that should be added:** *rank nuisance channels against the GROUPING or
  ORDERING under test, not against the covariates.* Prereg §6.1 ranked correctly-but-uselessly.

---

## 11. Files

- Prereg: `findings/phase-b-hypotheses/prereg-h-new-3040-modality-axis.md`
  (SHA-256 `48e02a04a252e91dac41cd747968e769c6a28379a1cbd85582bf2a2161e353df`, runtime-verified;
  re-verified intact after commit `eb6a40d0e`). **Never edited after the run** — every
  correction above is in this file.
- Scripts: `scripts/h-new-3040.py`, `scripts/h-new-3040-posthoc.py`.
- Runs, write-once, none deleted:
  `runs/h-new-3040/20260809T070448Z/` (primary) ·
  `…070806Z-posthoc/` · `…070853Z-posthoc-densities/` · `…071637Z-posthoc-channels/`
- Parent: `h-new-2640-modality-register.md` (§10.148), `prereg-h-new-2640-modality-register.md`.

---

*H-NEW-3040 completed 2026-08-09 by Waiel Al-Shujaa. The prior work existed, the locked channel
was the wrong one, and the half that looked strongest survived only because its counterexample
was outside the design. Bismillāhi al-Raḥmāni al-Raḥīm.*
