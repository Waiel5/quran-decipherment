---
id: H-NEW-3080
frontier_id: F-14
title: "Does quantifier scope (kull vs baʿḍ) separate the community-legal register from the universal-address register?"
author: Waiel Al-Shujaa
date: 2026-08-09
status: PRE-REGISTERED — locked before any computation of the primary statistic
seed: 20260509
n_perm: 10000
---

# PRE-REGISTRATION — H-NEW-3080 — Quantifier scope and register

**This file is locked BEFORE any computation that crosses a quantifier count with a register
label, an address label, or any grouping variable.** Everything computed before the lock was
register-blind and address-blind and is itemised, with its numbers, in §9 (garden of forking
paths). Nothing in §9 could reveal the direction or magnitude of any registered contrast.

**Immutability.** Per the standing rule of 2026-08-08, this file is never edited after its run,
for any reason including to correct an error in it. Corrections go in the finding.

---

## 0. STEP 0 — THE PRIOR-WORK CHECK, RUN BEFORE THE DESIGN

The frontier map's own binding rule (`HANDOFF/FRONTIER-MAP-2026-08-07.md`, staleness warning added
2026-08-09) requires the "does this already exist?" check to precede the "how do I run it?"
checks. It was run first, and its result is recorded here rather than only in §9 because it is the
check that decides whether to run at all.

**Searches executed** (repo root `/Users/grey/Downloads/quran/`, 2026-08-09):

| target | command shape | result |
|:--|:--|:--|
| `findings/` + ledger | `grep -ril "quantifier"` | 11 files, **all** incidental — H-NEW-2230/2270 use the word for *numerical* claims, not quantifier words |
| `findings/` + ledger | `grep -rilE "(ʿumūm\|umum\|ʿāmm\|khuṣūṣ\|khusus\|khāṣṣ)"` | 6 files: `balagha-mapping.md`, `99-names-wazn-classification.tsv`, `asbab-nuzul.md`, `prereg-h-new-330…`, `naskh-catalog.md`, `classical-lataif.md` — none a test |
| ledger | `grep -inE "kull\|kul~"` | 5 hits. Lines 6227–6234 are a lexical note on *kullan / kilā* glosses; line 6375 is H-NEW-2230's balanced-word rerun; the rest are unrelated strings inside surah summaries. **No register test.** |
| ledger | `grep -inE "partitive\|universal quant\|scope"` | no quantifier-scope test |
| `findings/` | `grep -ril "particularis"` | exactly one file: `ethical-universalism.md` itself |
| filenames | `ls findings/phase-b-hypotheses/ \| grep -iE "quant\|scope\|univers\|particul\|amm\|khass\|umum"` | 14 hits, all unrelated (`h-new-250-quantitative-equation`, `h-new-2690-quantitative-scansion`, `h-new-142-universal-hinges` = a chronology study, `ethical-universalism.md`) |
| run dirs | `find . -type d -name "h-new-30*"` | 3000, 3010, 3020, 3030, 3040 — **no 3080, no quantifier run** |
| prereg files | `ls … \| grep "^prereg-h-new-30"` | 3000, 3010, 3020, 3030, 3040, 3050 — **none on quantifiers** |
| the adjacent-design check | read `prereg-h-new-2530-register-grammar.md` §2 feature list | the six register features are `f_idh`, `f_lamma`, `f_qalu`, `f_idha_cascade`, `f_doubling`, `f_iltifat_type`. **No quantifier feature exists in the register-grammar axis.** |

**The complete roster of prior register × QAC-lemma tests** (this design is the sixth member of
that family and must not silently re-derive any of them):

| id | axis | verdict | date |
|:--|:--|:--|:--|
| H-NEW-2530 | function-word + person-grammar, joint | CONFIRMED | 2026-08-07 |
| H-NEW-2630 | realis vs irrealis conditionals | **NOT register-coded** | 2026-08-07 |
| H-NEW-2640 | ṭalab / khabar division | NULL on all four | 2026-08-07 |
| H-NEW-2700 / 3020 | loanword donor strata | NULL, 3 reversed | 2026-08-07 / 09 |
| H-NEW-3010 | conditionals, re-derivation | 0 of 12 clear; p swings ~70× on length channel | 2026-08-09 |
| H-NEW-3040 | modality (deontic vs epistemic) | 3 PASS / 5 NULL of eight; verdict FLIPS on channel | 2026-08-09 |

**STEP-0 VERDICT: F-14 has NOT been executed. It is clean to run.** What is *not* clean is the
prior on it: two of the five siblings above returned NULL and two more had their verdict decided
by a length channel rather than by the hypothesis. This design is written against that record.

---

## 1. THE HYPOTHESIS

The frontier map states F-14 as: *kull* (universal) vs *baʿḍ* / *min* (partitive) distribution
separates the ethical-universalist register from the community-legal register, giving an
independent handle on `findings/phase-b-hypotheses/ethical-universalism.md`.

Its prior is **CBM (confirmed-but-meaningless)**, on the named ground that *kull* is heavily
formulaic. This pre-registration takes that prior seriously enough to make the formula question a
**locked axis of the design** rather than a caveat: the effect is computed at four pre-declared
exclusion levels and both the unexcluded and the excluded result are headline, not appendix.

---

## 2. DIRECTIONS — LOCKED AND JUSTIFIED BEFORE ANY COMPUTATION

### 2.1 The locked direction

> **LOCKED: the universal-to-partitive ratio is HIGHER in the universal-address register than in
> the community-legal register.**
>
> With the statistic defined in §6.1 as
> `LOR = log[ (U_LEGAL + ½)(P_UNIV + ½) / ((P_LEGAL + ½)(U_UNIV + ½)) ]`,
> the locked direction is **LOR < 0**.

A result with `LOR ≥ 0` at the primary cell is a **PRE-COMMIT VIOLATION** and is published as
NULL-REVERSED at full prominence. It is never re-read as a two-sided finding.

The same locked sign applies to ARM 2 (§5.2) with UNIVERSAL-ADDRESS in place of UNIV.

### 2.2 Why this direction, and not the reverse — the verified classical anchor

**On disk, read, line-numbered.** `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`,
al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*. The nawʿ label below is **derived from the locator's own
header text**, not typed alongside it, per cross-finding-029 §3.1 item 5.

- **line 14254** — section header: `### | النوع الخامس والأربعون: في عامه وخاصه`
  ("the forty-fifth nawʿ: on its general (*ʿāmm*) and its particular (*khāṣṣ*)"). The ordinal in
  the header text is *al-khāmis wa-l-arbaʿūn* = 45.
- **lines 14255–14256** — the definition, and the reason *kull* is the right instrument:
  «العام لفظ يستغرق الصالح له من غير حصر وصيغته "كل" مبتدأة نحو: {كل من عليها فان} أو تابعة نحو:
  {فسجد الملائكة كلهم أجمعون}» — *the ʿāmm is an expression that exhausts what it applies to
  without limit, and its form (ṣīgha) is «kull», either initial … or following …*.
  **al-Suyūṭī names *kull* as the paradigm form of ʿumūm.** This is the anchor for the choice of
  instrument, not merely for the direction.
- **lines 14277–14281** — al-Bulqīnī: the general that *remains* on its generality is *ʿazīz*
  (rare), «إذ ما من عام إلا ويتخيل فيه التخصيص», with {حرمت عليكم الميتة} given as a general that
  is specified (by necessity, by fish and locust carrion).
- **lines 14282–14284** — al-Zarkashī in *al-Burhān* is cited to the contrary: it is *frequent*,
  e.g. {وأن الله بكل شيء عليم}, {إن الله لا يظلم الناس شيئا}.
- **lines 14285–14287** — al-Suyūṭī resolves the disagreement, and the resolution **is the
  hypothesis**: «قلت: هذه الآيات كلها في غير الأحكام الفرعية فالظاهر أن مراد البلقيني أنه عزيز في
  الأحكام الفرعية» — *these verses are all in matters other than branch-legal rulings, so what
  al-Bulqīnī means is that it is rare in the branch-legal rulings*. He then reports that he had to
  hunt to find a single legal verse with no specification at all ({حرمت عليكم أمهاتكم}).

So the classical *uṣūl* position, verified on disk, is that **unrestricted universality survives
outside the legal register and is hunted-for inside it**. That fixes the sign before any count is
taken. It also predicts, independently, that the *kull shayʾ* formula (al-Zarkashī's own first
example) should sit on the non-legal side — which is why §4 must report the effect with and
without it.

**Second, structural.** al-Suyūṭī's list of the five *connected* specifiers (*muttaṣil*) at lines
14294 onward — istithnāʾ, waṣf, sharṭ, and the rest — is illustrated almost entirely from legal
verses. Legal discourse in this corpus is built from carve-outs; carve-outs are the grammar of the
partitive.

**Third, from the document this test is meant to give a handle on.**
`findings/phase-b-hypotheses/ethical-universalism.md` §0 states its own organising principle as
verses that "state a moral universal without ethnic or confessional gating", and its §1 and §4
turn on address to *al-nās* rather than to *alladhīna āmanū*. If that document is describing a
real register, quantification over the unrestricted set is its signature.

### 2.3 UNVERIFIED ANCHOR — declared as such

The frontier map names al-Shāfiʿī's *Risāla* and al-Ghazālī's *Mustaṣfā* as the *uṣūl* anchor.
**Neither is on disk.** They are recorded here as an **UNVERIFIED ANCHOR** and **no page, chapter,
bāb, or passage of either is cited anywhere in this pre-registration or in the finding.** The
entire weight of the classical anchor rests on §2.2, which was read directly.

---

## 3. THE INSTRUMENT (LOCKED)

### 3.1 Source

`data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4), SHA-256
`a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46`. The `LEM:` field of the
`FEATURES` column. Segments are grouped to **words** by the `(s:v:w:g)` locator; a word counts for
a lemma if any of its segments carries that lemma. Raw substring counting is forbidden by the
project's standing rule and is not used.

### 3.2 The universal pole U

**U = lemma `kul~`.** Register-blind corpus count: **359 word-tokens** (§9-B1).

### 3.3 The partitive pole P — RULES-TUPLE AXIS A (LOCKED)

- **RT-A1 (PRIMARY): P = lemma `baEoD`.** Register-blind count **157 word-tokens**.
- **RT-A2 (ROBUSTNESS ONLY): P = `baEoD` ∪ `min`-partitive-proxy**, where the proxy is a `min`
  word-token whose immediately following word carries the definite-article prefix `Al+`.

**Why `min` cannot be primary, stated before the run.** The map's phrasing is "*baʿḍ* / *min*
(partitive)". `min` occurs 3,226 times and is overwhelmingly ablative/directional
(*min al-samāʾ*, *min baʿdi*), not partitive. Separating *min al-tabʿīḍiyya* from
*min al-ibtidāʾiyya* is a syntactic judgement, and the only parse on disk (EQTB) is recorded in
this project's own notes as parser-contaminated for morphology-conditioned questions. Admitting
3,226 tokens against 157 would make the statistic a `min`-density statistic wearing a quantifier
label. RT-A2 is therefore declared a **crude proxy**, is reported in full, and **may not establish
or overturn any verdict.**

### 3.4 Counting rule — RULES-TUPLE AXIS B (LOCKED)

- **RT-B1 (PRIMARY): word-token counts.**
- **RT-B2 (ROBUSTNESS): verse-presence counts** — each lemma contributes at most 1 per verse.

**Why B2 exists, and why it is not primary.** Register-blind measurement (§9-B3): **135 of the 157
`baʿḍ` tokens (86.0%) sit in verses containing two or more `baʿḍ`** — the reciprocal frame
*baʿḍuhum … baʿḍ* ("one another"), whose most frequent right-neighbour is `baEoD` itself (22).
That frame is arguably not a partitive quantifier at all. RT-B2 collapses it (157 → 86 verses) and
applies the identical rule to `kull` so the treatment is symmetric. It is robustness rather than
primary because the collapse also destroys genuine repeated partitives
(*faḍḍalnā baʿḍahum ʿalā baʿḍ*), and no rule that is right for one is right for both.

### 3.5 Rules-tuple disclosure (Protocol §1.4)

`RT-1 = (no-tashkeel, QAC v0.4 LEM field, word-grouped by (s:v:w) locator, Ḥafṣ-Kūfan, Mashriqī,
basmala counted only in Q1, U = kul~, P = baEoD, token counts, formula-exclusion EX-2,
register = Neuwirth–Sinai sinai_genre mechanical mapping MAP-1)`. Axes A, B, C (§4) and D (§5.1)
are the four declared sensitivity axes; ≥ 2 is the standing requirement and four are run.

---

## 4. THE NAMED CONFOUND: FORMULAE — RULES-TUPLE AXIS C (LOCKED BEFORE ANY CROSSING)

The frontier map's prior on F-14 is CBM specifically because *kull* is formulaic. The exclusion
list is therefore built **now**, from register-blind corpus frequency alone, and locked.

### 4.1 The register-blind collocation inventory (computed 2026-08-09, before this lock)

Frequency of the lemma of the word immediately following each of the 359 `kull` tokens, within the
same verse (§9-B2). Top of the distribution:

| following lemma | count | share of all `kull` |
|:--|--:|--:|
| `$aYo'` (*shayʾ*) | **121** | 33.7 % |
| `nafos` (*nafs*) | **23** | 6.4 % |
| `>um~ap` (*umma*) | 15 | 4.2 % |
| `vamara`t`, `min`, `zawoj` | 6 each | 1.7 % each |
| everything else | ≤ 5 each | — |

Most frequent trigrams: *kull shayʾ qadīr* 35, *kull shayʾ ʿalīm* 20, *kull nafs mā …* 13,
*kull shayʾ shahīd* 8, *kull ummatin shahīd* 4, *kull shayʾ ʿilm* 4, *kull ṣabbār shakūr* 4,
*kull nafs dhāʾiqat …* 3.

### 4.2 The locked exclusion ladder

A `kull` token is excluded at a given level iff the lemma of its immediately following word is in
that level's set. `baʿḍ` is never excluded by axis C.

| level | excluded head lemmas | rule that generated the set | `kull` retained |
|:--|:--|:--|--:|
| **EX-0** | — | no exclusion | 359 |
| **EX-1** | {`$aYo'`} | bigram frequency ≥ 100 | 238 |
| **EX-2 (PRIMARY)** | {`$aYo'`, `nafos`} | **the two formula heads named by the frontier map itself** (`kull shayʾ qadīr`, `kull nafs dhāʾiqat al-mawt`); independently the top two by frequency | 215 |
| **EX-3** | {`$aYo'`, `nafos`, `>um~ap`} | bigram frequency ≥ 15 | 200 |

**EX-2 is primary because its set is externally specified.** It was named in
`HANDOFF/FRONTIER-MAP-2026-08-07.md` §F-14 before this design existed, and the frequency inventory
merely confirms the same two heads. EX-1 and EX-3 exist so that the *threshold* — the classic
deciding parameter of cross-finding-029 — is varied rather than chosen.

### 4.3 The reporting commitment, stated in advance

**EX-0 and EX-2 are both primary-family cells (§7).** The finding's abstract will state the verdict
at both. If the contrast is present at EX-0 and absent at EX-2, **the headline of the finding is
that the effect is the formula**, and it will be written that way — not relegated to a limits
section.

---

## 5. THE GROUPINGS (LOCKED)

### 5.1 ARM 1 — register labels — RULES-TUPLE AXIS D

Source: `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`, SHA-256
`16ec35b2793922bd007767ccddfb6d7aeb5ca53e48394792984f88b49164572a`, column `sinai_genre`, all 114
surahs non-empty. Both maps use **LEGAL precedence containment**: a label containing `legal`
is LEGAL regardless of what else it contains.

- **MAP-1 (PRIMARY).** `LEGAL` if the lowercased label contains `legal`; else `UNIV` if it contains
  `eschatolog` **or** `exhort` **or** `admonit`; else `OTHER` (dropped).
  Sizes: **17 LEGAL, 42 UNIV, 55 OTHER**.
- **MAP-2 (SECONDARY, cross-lane comparability).** H-NEW-3010's `map_M1` **verbatim**: `LEGAL` if
  contains `legal`; else `UNIV` if contains `eschatolog` or `polemic`; else `OTHER`.
  Sizes: **17 LEGAL, 36 UNIV, 61 OTHER**.

**Why two maps and why MAP-1 is primary.** There is no "universalist" genre in the Neuwirth–Sinai
scheme, so the pole must be constructed, and constructing it is a forking path. MAP-1 selects the
genres in which moral address to the unrestricted set actually lives (eschatological, exhortative,
admonitory). MAP-2 reuses an already-locked mapping from a sibling lane unchanged, so that a
divergence between the two is attributable to the mapping and not to the lane. Both were fixed
before any quantifier count was crossed with them.

### 5.2 ARM 2 — addressee scope, independent of the genre labels

This is the arm that gives `ethical-universalism.md` a handle that does not route through a modern
scholar's genre labels: it reads the Qurʾān's own vocative addressee.

Blocks are delimited mechanically. An **opener** is a word-token whose FORM contains `>ay~uhaA`.
Its type is fixed by the next one or two lemmas in the same verse:

- **UNIVERSAL-ADDRESS** — next lemma is `n~aAs` (*yā ayyuhā al-nās*) or `<insa`n`
  (*yā ayyuhā al-insān*). **23 openers.**
- **COMMUNITY-ADDRESS** — next lemma is `{l~a*iY` and the one after is `'aAmana`
  (*yā ayyuhā alladhīna āmanū*). **89 openers.**
- Every other `>ay~uhaA` token — *yā ayyuhā al-nabī* (13), *al-malaʾ* (5), *al-rasūl* (3),
  `alladhīna` followed by anything other than *āmanū* (4), and the remaining singletons —
  is **NON-DELIMITING**: it is neither a pole nor a boundary. **38 of the 150 `>ay~uhaA` tokens
  are non-delimiting**; 23 + 89 + 38 = 150.

A **block** runs from its opener's verse to the verse before the next **delimiting** opener in the
same surah, or to the end of the surah. Address-blind coverage: **489 verses in 23 UNIVERSAL
blocks, 939 verses in 89 COMMUNITY blocks**, 1,428 of 6,236 verses (§9-B4). Verses in no block are
excluded. **The runner asserts these five integers (23, 89, 38, 489, 939) against the data and
exits non-zero on any mismatch**, so the block rule cannot drift between this file and the run.

Window sensitivity, robustness only, not in the primary family: fixed windows of the opener verse
plus W following verses, W ∈ {3, 5}, truncated at surah end and at the next opener.

**Power is stated in advance because it is poor.** Under the null, the expected `kull` counts in
these blocks are ≈ 28 (UNIVERSAL) and ≈ 54 (COMMUNITY), and `baʿḍ` ≈ 12 and ≈ 24. A 2×2 of that
size detects only a large odds ratio. §8 pre-commits to computing and publishing the MDE for this
arm whatever it returns.

---

## 6. THE STATISTIC AND THE NULL (LOCKED)

### 6.1 The statistic

For a grouping with poles `LEGAL` and `UNIV` (ARM 1) or `COMMUNITY` and `UNIVERSAL` (ARM 2), pool
the retained token counts across all units in each pole and form the 2×2 table

|            | universal `U` | partitive `P` |
|:--|--:|--:|
| **LEGAL**  | `U_L` | `P_L` |
| **UNIV**   | `U_V` | `P_V` |

and take the Haldane–Anscombe-corrected log odds ratio

```
LOR = log( ((U_L + 0.5) * (P_V + 0.5)) / ((P_L + 0.5) * (U_V + 0.5)) )
```

**Why this statistic and not a density.** It is a ratio of two counts drawn from the *same* text,
so there is **no unit count in its denominator**. Under `findings/UNIT-DRIFT-DEFECT.md` Screen A it
is not a per-verse, per-word, per-surah or per-window density and does not pass Screen A, so the
defect cannot fire on it — which matters here because Screen B *would* fire: the LEGAL surahs are
the long surahs and the two groups differ several-fold in size.

### 6.2 The null

**Permutation, seed 20260509, 10000 draws.**

- **ARM 1:** the pole label is permuted across the labelled surahs (59 under MAP-1, 53 under
  MAP-2), holding each surah's own `U` and `P` counts fixed. The surah is the exchangeable unit.
- **ARM 2:** the block-type label is permuted across the 112 blocks, holding each block's counts
  fixed.

One-sided p in the locked direction:
`p = (#{LOR_perm ≤ LOR_obs} + 1) / (n_perm + 1)`.

**RNG (locked).** Permutations are drawn with `random.Random(20260509)` and
`rng.shuffle` on a Python list of labels — the same machinery as the sibling lanes H-NEW-3010 and
H-NEW-3040 — and the statistic is evaluated in pure Python. A single generator is created once and
consumed in the fixed cell order of §7.1, so the whole grid is reproducible from the seed alone.
The MDE simulation of §8 is the one exception and declares its own generator there.

### 6.3 THE LENGTH CHANNELS — MANDATORY, ALL RUN, WORST REPORTED

Length is at least three variables. H-NEW-3010 saw a ~70× p-swing across channels and H-NEW-3040
saw its verdict flip. **No single channel is locked.** Every cell's null is run under four
permutation regimes:

| id | regime |
|:--|:--|
| `C0` | unstratified |
| `C1` | permute within quintiles of **log word count** |
| `C2` | permute within quintiles of **verse count** |
| `C3` | permute within quintiles of **mean verse length** (words per verse) |

ARM 2 uses the same three channels computed over blocks (block word count, block verse count,
block mean verse length).

- **All four p-values are reported for every cell.** None is omitted.
- **The cell's headline p is `p_cell = max over the non-degenerate channels`** — the worst.
- **The DOMINANT channel is reported**: the channel `c` maximising `|ρ_Spearman(c, pole indicator)|`
  over the labelled units, computed and written to the results object **before** any primary
  statistic (ordering enforced in code).
- **Degeneracy guard** (from H-NEW-3040): for each stratified channel, count distinct permuted
  label vectors. **Fewer than 100 distinct → the channel is DEGENERATE**, is reported as such, and
  is **excluded from the max**. If all three stratified channels are degenerate the cell's headline
  is `C0` alone and the finding must say so in the abstract.

### 6.4 Ties

The tie fraction `#{LOR_perm == LOR_obs} / n_perm` is computed and reported **per channel**, and a
cell's tie fraction is the **maximum over its four channels** — the conservative reading, the one
most likely to force the exact test.
**If it exceeds 0.50 for a primary-family cell, the permutation p is discarded for that cell and
Fisher's exact test (one-sided, in the locked direction) on the pooled 2×2 is the required
substitute**, reported as `p_exact` and used in the decision rule in place of `p_cell`.
`p_exact` is computed and reported for **every** cell regardless, as a companion. The same
substitution rule is applied to the verdict-inert robustness cells for consistency; since they can
carry no verdict, this cannot affect any outcome.

---

## 7. DECISION RULE (LOCKED — the runner's verdict function must match this LINE BY LINE)

### 7.1 The primary family

**k = 6 cells.** α_Bonferroni = 0.05 / 6 = **0.0083333…**

| # | arm | map / grouping | exclusion | tuple |
|:--|:--|:--|:--|:--|
| 1 | ARM 1 | MAP-1 | **EX-2** | RT-A1, RT-B1 |
| 2 | ARM 1 | MAP-1 | **EX-0** | RT-A1, RT-B1 |
| 3 | ARM 1 | MAP-2 | EX-2 | RT-A1, RT-B1 |
| 4 | ARM 1 | MAP-2 | EX-0 | RT-A1, RT-B1 |
| 5 | ARM 2 | address blocks | EX-2 | RT-A1, RT-B1 |
| 6 | ARM 2 | address blocks | EX-0 | RT-A1, RT-B1 |

**Cell 1 is THE PRIMARY TEST.** Everything else in the family is a same-status member for
multiplicity purposes but the headline verdict of H-NEW-3080 is cell 1's.

### 7.2 Per-cell verdict

For each of the 6 cells, in this order:

1. If `LOR_obs ≥ 0` → **`PRE-COMMIT VIOLATION`**. Stop for that cell; no p-value is consulted.
2. Else if the tie fraction > 0.50 → use `p_exact` (§6.4) in place of `p_cell`.
3. Else `p_cell = max{ p_c : c ∈ {C0,C1,C2,C3}, c not DEGENERATE }`.
4. `LOR_obs < 0` **and** `p_cell < 0.0083333` → **`PASS`**.
5. `LOR_obs < 0` **and** `p_cell ≥ 0.0083333` → **`NULL`**.

### 7.3 The finding-level verdict

- **CONFIRMED** — cell 1 PASS **and** cell 2 PASS. (Effect present both with and without the
  formulae.)
- **CONFIRMED-FORMULAIC** — cell 2 PASS and cell 1 NULL. **The effect is the formula.** This
  verdict's one-line summary is *"the contrast is carried by `kull shayʾ` / `kull nafs` and does
  not survive their removal"*, and it goes in the abstract.
- **CONFIRMED-NON-FORMULAIC** — cell 1 PASS and cell 2 NULL.
- **NULL** — cells 1 and 2 both NULL.
- **NULL-REVERSED** — cell 1 is a PRE-COMMIT VIOLATION. Published at full prominence; the locked
  direction and the classical reasoning of §2.2 are reported as having failed.
- **Cell 2 reversed while cell 1 is not.** Cell 1 alone fixes the base verdict (PASS →
  CONFIRMED-NON-FORMULAIC; NULL → NULL) and the string carries the suffix **`+CELL-2-REVERSED`**,
  which must appear in the abstract. A cell-2 violation cannot by itself make the finding
  NULL-REVERSED, because cell 2 is the *unexcluded* count and a reversal there with cell 1 clean
  would mean the formulae carry the reversal — which is a statement about the formulae, not about
  the hypothesis.

Cells 3–6 qualify the verdict; **they may not create one.** If cell 1 is NULL and cell 3 PASSes,
the finding is NULL with a disclosed map-sensitivity, not a PASS.

### 7.4 The robustness set — reported in full, uncorrected, verdict-inert

RT-A2 (`min`-proxy), RT-B2 (verse-presence), EX-1, EX-3, ARM 2 windows W ∈ {3,5}, and the per-surah
secondary of §7.5. **None of these may establish or overturn a verdict**, in either direction.
Every one is printed with its p-value whatever it shows.

### 7.5 Two secondaries that are computed and reported but are verdict-inert

- **Per-surah view.** For surahs with `U + P ≥ 5`, the smoothed per-surah log-ratio
  `log((U_s + ½)/(P_s + ½))`; two-sample Mann–Whitney by pole, plus the same four channel-stratified
  permutation nulls. Register-blind coverage says this is thin: **41 surahs have no `kull` at all,
  76 have no `baʿḍ`, 40 have neither, and only 40 surahs reach `U + P ≥ 5`** (§9-B5). Reported so
  that the pooled statistic is not the only view, flagged as underpowered by construction.
- **The density view, FLAGGED.** `kull` and `baʿḍ` per 1000 words by pole. This statistic **does**
  hit UNIT-DRIFT Screens A and B and is reported carrying that flag explicitly in its own table
  caption. It exists to show the reader what the naive measure says; it is never a verdict input.

---

## 8. IF A NULL IS PUBLISHED, IT STATES ITS MDE AND POWER

Binding, per cross-finding-029 §3.2. For **every** cell returning NULL:

1. **MDE.** By simulation: for a target odds ratio `r` on the grid
   `OR ∈ {1.1, 1.2, 1.3, 1.5, 1.75, 2.0, 2.5, 3.0, 4.0}` (locked here), each LEGAL-pole unit's
   `kull` count is binomially thinned with retention probability `1/r` — injecting a true effect of
   exactly `r` in the locked direction while preserving the observed per-unit dispersion — and the
   cell's one-sided permutation test is re-run on the synthetic data. **1000 simulated datasets per
   grid point; 2000 inner permutations each; unstratified (`C0`) null only; α = 0.0083333.** Power
   at `r` is the fraction of the 1000 that reject. The MDE is the smallest grid `r` reaching
   **80 %**. Declared separately because it is not the primary machinery: the simulation uses
   `numpy.random.default_rng(20260509)` for both the thinning and the inner permutations, and its
   inner permutation count is 2000 rather than 10000 — 2000 gives a minimum attainable p of
   1/2001 ≈ 0.0005, comfortably below α, so the reduction cannot inflate the reported power.
   If no grid point reaches 80 %, the MDE is reported as `> 4.0`.
2. **The comparison that makes the MDE legible.** The MDE is reported against this project's own
   strongest surviving law, whose honest effect is a rate ratio of **1.27–2.58** (muqaṭṭaʿāt
   book-reference, per the 2026-08-07 correction notice). If the MDE exceeds 2.58 the NULL is
   explicitly labelled **underpowered against this corpus's own effect scale**.
3. **The power curve** is written to the run directory as a reusable artefact.

---

## 9. GARDEN OF FORKING PATHS

Every choice considered, and how it was resolved. Entries **B1–B5** are computations that were run
**before** this lock; each is register-blind and address-blind by construction, and none can carry
information about any registered contrast.

**A. The check that decides whether to run at all**

- **A1 — the Step-0 prior-work grep.** Executed before any design work, recorded in full in §0.
  Result: no prior execution of F-14; five sibling register×lemma tests found and listed; no
  quantifier feature in the register-grammar axis. **This entry exists because H-NEW-3010's
  forking-paths log had sixteen entries about instrument choice and not one about whether the work
  already existed.**

**B. Register-blind computations run before the lock**

- **B1** — lemma census of the whole QAC file. `kul~` 359, `baEoD` 157, `min` 3226, `jamiyE` 53.
  Used to choose the poles. No grouping variable involved.
- **B2** — the `kull` right-collocate frequency table of §4.1, and the trigram table. **This is the
  computation the frontier map explicitly required before the run** ("build it by frequency from
  the corpus, lock it, hash it, and then run"). Register-blind.
- **B3** — the `baʿḍ` reciprocal measurement: 86 verses contain `baʿḍ`, 64 contain ≥ 2, and 135 of
  157 tokens live in those 64 verses. This is what motivated RT-B2. Register-blind.
- **B4** — ARM 2 block coverage: 23 / 89 delimiting openers, 38 non-delimiting, 489 / 939 verses.
  This is a property of the ARM 2 *grouping*, not of any quantifier count crossed with it; no
  `kull` or `baʿḍ` count was computed per block before this lock. Used only to state power honestly
  in §5.2. **A first pass at this number, run before the block rule was written down, treated the
  four non-*āmanū* `alladhīna` vocatives as delimiters and returned 926 rather than 939 for the
  COMMUNITY pole.** The rule in §5.2 is the one that is locked and the one the runner asserts; the
  discrepancy is recorded here rather than silently overwritten, because a coverage number that
  changed when the rule was written down is exactly the kind of free parameter cross-finding-029
  is about.
- **B5** — per-surah coverage of the poles: 41 surahs with zero `kull`, 76 with zero `baʿḍ`, 40 with
  neither, 40 with `U+P ≥ 5`. Not crossed with any label. **This is why the pooled 2×2 is primary
  and the per-surah view is secondary** — a per-surah log-ratio would be the smoothing constant for
  two-thirds of the corpus.

**C. Design choices**

- **C1 — pooled 2×2 vs per-surah.** Chosen: pooled, on B5. The per-surah view survives as a
  verdict-inert secondary rather than being dropped, so the reader sees both.
- **C2 — LOR vs densities.** Chosen: LOR, because it has no unit count in the denominator and the
  LEGAL/UNIV grouping has a several-fold size gap (UNIT-DRIFT Screen B). The density view is kept
  as an explicitly flagged secondary rather than suppressed.
- **C3 — the partitive pole.** Considered: `baʿḍ` alone; `baʿḍ` ∪ `min`; `min` alone; a
  syntactically filtered `min`. Rejected `min`-inclusive as primary for the reason in §3.3.
  Rejected an EQTB-parsed `min` outright: the treebank is recorded in this project's own notes as
  parser-contaminated, and a contaminated parse in the primary instrument is exactly the defect
  H-NEW-2540's own pre-registration flagged.
- **C4 — the universal pole.** Considered adding `jamīʿ` (53) and `kilā`/`kull` variants.
  **Rejected**: `jamīʿ` is predominantly adverbial (*jamīʿan*, "all together") rather than a
  quantifier over a restriction set, and admitting it would blend two constructions. Recorded as a
  deliberate narrowing, not an oversight.
- **C5 — al-Suyūṭī's wider ʿumūm inventory.** Itqān nawʿ 45 (lines 14257–14274) lists further
  ʿumūm forms: `alladhī/allatī` and their duals and plurals; `ayy`, `mā`, `man` as conditional,
  interrogative and relative; the annexed plural; the `al`-definite; the annexed generic noun; and
  the indefinite under negation, prohibition, condition or *imtinān*. **A maximal instrument would
  use all of them. This design does not, and that is a stated limit rather than a silent one:**
  those forms are ambiguous between generic and specific reference in ways `kull` is not, and
  operationalising them needs the parse §3.3 rejects. The finding will say that the test is of
  *kull*-marked ʿumūm, not of ʿumūm.
- **C6 — the formula threshold.** The classic deciding parameter. Resolved by declaring the
  externally-named set (EX-2) primary and varying the threshold across EX-0/1/3 rather than
  choosing one.
- **C7 — the register pole.** Two maps, both fixed before crossing (§5.1). MAP-1 is not MAP-2 with
  `polemic` swapped for `exhort`+`admonit` by accident: polemic addresses opponents and is not the
  universalist register, but it *is* what the sibling lane locked, so both run.
- **C8 — the run directory.** The brief says `runs/h-new-3080/<UTC>/`. The repository has two
  `runs/` trees: `runs/` (2600–2900 series) and `findings/phase-b-hypotheses/runs/` (the entire
  3000 series: 3000, 3010, 3020, 3030, 3040). **Chosen: `findings/phase-b-hypotheses/runs/h-new-3080/<UTC>/`,
  matching its siblings.** Recorded here so the deviation from the brief's literal string is a
  disclosed choice.
- **C9 — one-sided vs two-sided.** One-sided, because §2.2 fixes the sign from a source read before
  the design. The cost is pre-committed: a reversal is a PRE-COMMIT VIOLATION published as such,
  not a two-sided rescue.
- **C10 — family size.** k = 6: the cells that can produce a verdict. The channel sweep is *inside*
  each cell via the max rule (§6.3), which is conservative, rather than being 24 separate family
  members, which would be double-counting a robustness requirement as a multiplicity.

**D. A PARTIAL PRE-LOCK PEEK, DISCLOSED AT FULL PROMINENCE**

- **D1 — I saw four real ARM 2 robustness numbers before this file was locked. This is a
  self-reported pre-commit hygiene failure and it is recorded here rather than in the finding
  because it happened before the lock and the reader is entitled to weigh it.**

  The runner was smoke-tested twice against scrambled labels so that the plumbing could be
  exercised without revealing any registered statistic. The **first** smoke scrambled both the
  genre labels *and* the ARM 2 block poles. The **second**, rebuilt from the updated source after
  the §7.5 and §7.4 fixes, **re-applied the genre scramble and dropped the ARM 2 pole scramble** —
  my error in reconstructing the patch. The four ARM 2 **window** robustness cells therefore ran on
  real poles, and their output line was inside the tail of the console output I read:

  | cell | LOR | p (worst channel) | Fisher |
  |:--|--:|--:|--:|
  | `ARM2\|W3\|EX-0` | −2.8300 | 0.0328 | 0.0083 |
  | `ARM2\|W3\|EX-2` | −3.1864 | 0.0820 | 0.0081 |
  | `ARM2\|W5\|EX-0` | −2.8660 | 0.0328 | 0.0056 |
  | `ARM2\|W5\|EX-2` | −3.2452 | 0.0492 | 0.0052 |

  Those runs used **N_PERM = 60**, so their p-values have no resolution below 1/61 and are not
  the pre-registered quantities. **What leaked is a sign and an order of magnitude on ARM 2.**

  **What this cannot have contaminated.** The locked direction (§2.1) was fixed from al-Suyūṭī
  before any code was written. Every parameter in §§3–8 — poles, exclusion ladder, maps, block
  rule, statistic, null, channels, family size, α, decision rule — was written into this file
  **before** the smoke ran, and **not one of them was changed afterwards**. The only edit made after
  the peek is this paragraph.

  **What it does contaminate.** ARM 2 cells 5 and 6 are the same grouping as these window cells with
  wider blocks. I have seen the sign and rough size of that contrast. **Cells 5 and 6 should
  therefore be read as weaker evidence than cells 1–4**, and the finding must repeat this. Cells
  1–4 (ARM 1) are unaffected: the genre labels were scrambled in both smokes and no real ARM 1
  statistic was ever displayed.

  **The general lesson, for the next lane:** a scrambled-label smoke test is the right technique,
  and rebuilding the scramble patch by hand from a changed source is how it fails. The scramble
  belongs behind an environment flag inside the real script, not in a hand-maintained copy.

---

## 10. WHAT WOULD FALSIFY THIS

- `LOR_obs ≥ 0` at cell 1 — the locked direction is wrong and the classical reasoning of §2.2 fails
  empirically. Published as NULL-REVERSED.
- Cell 1 NULL with cell 2 PASS — the map's CBM prior is vindicated; the finding's headline becomes
  the formula.
- All three stratified channels DEGENERATE — the design cannot control length at this n and says so.
- `p_cell` driven by a single channel while the other three disagree — reported as fragile, with
  the dominant channel named, in the shape H-NEW-3010 established.

## 11. OUTPUTS

Run directory `findings/phase-b-hypotheses/runs/h-new-3080/<UTC>/`, created with
`os.makedirs(..., exist_ok=False)`; every file opened with mode `'x'`. Never deleted.

- `manifest.json` — prereg path + SHA-256, script path + SHA-256, frozen-input SHA-256s, seed,
  n_perm, k_family, alpha, python version, `write_once: true`.
- `results.json` — the full grid: every cell × every channel, with `LOR_obs`, all four p-values,
  tie fractions, degeneracy flags, dominant channel, the 2×2 tables, the robustness set, the
  secondaries, and the MDE/power block for every NULL.
- `verdict.txt` — the per-cell verdicts and the finding-level verdict, computed by a function that
  mirrors §7 line by line.

## 12. FROZEN INPUTS

| path | SHA-256 |
|:--|:--|
| `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| `findings/classical-sources/neuwirth-sinai-genre-labels.tsv` | `16ec35b2793922bd007767ccddfb6d7aeb5ca53e48394792984f88b49164572a` |
| `data/hafs-verse-counts.tsv` | `e1818fb04ac26b863ce1ade50193390d481345a3971919aeb120daf8946212ba` |

Classical anchor read at `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`,
lines 14254–14287 (§2.2). Not a computational input; cited only.

---

*Locked 2026-08-09 by Waiel Al-Shujaa, before any computation crossing a quantifier count with a
grouping variable.*
