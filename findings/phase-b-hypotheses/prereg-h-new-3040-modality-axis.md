---
finding_id: H-NEW-3040
title: Pre-registration — the modality axis (deontic vs epistemic/alethic) and its orthogonality to the cross-finding-028 function-word axis
author: Waiel Al-Shujaa
date: 2026-08-09
phase: B
status: PRE-REGISTERED — locked before any primary statistic was computed
frontier_id: F-10
seed: 20260509
n_perm: 10000
bonferroni_k_primary: 2
alpha_bonferroni_primary: 0.025
---

# Pre-registration — H-NEW-3040

## 0. What was measured BEFORE this file was written, and what was not

This section exists because the honesty of everything below depends on it.

**Measured before locking (all of it mandated, and each measurement named here):**

1. **The six QAC counts named in the frontier map**, re-verified by me from
   `data/morphology/quranic-corpus-morphology-0.4.txt` (§2.1). One is wrong in the frontier map
   and the correction is recorded there.
2. **cross-finding-028's exact feature list and its frozen per-surah vectors**, and the
   token-level intersection of those with every candidate modality feature (§3). The task
   design requires this to be enumerated *first*, because an orthogonality claim between two
   axes that share an input is not measurable.
3. **The nuisance-channel ranking for cross-finding-028's six features** against log word
   count, verse count, mean verse length and mushaf position (§6.1). `UNIT-DRIFT-DEFECT.md` §5
   requires candidate channels to be ranked *on the data* before one is locked as primary; §3
   of that document records that the repository's own drift table got this wrong for months by
   ranking on intuition.
4. **The trigger-window sensitivity of the jussive split** (§4.3) and **the number of surahs on
   which an unsmoothed contrast would be undefined** (§4.4). Both were measured because they
   determine whether the statistic is well defined at all; both changed the design, and both
   changes are recorded in the forking-paths log (§10).

**NOT measured before locking — no value of any of these has been seen:**

- the per-surah modality contrast `M` for any surah;
- ρ(M, R) in any arm, marginal or partial;
- ρ(M, any length channel);
- the H1 legal-vs-eschatological contrast, in any form;
- any p-value, confidence interval, or verdict.

---

## 1. Hypothesis

> **H-NEW-3040.** The Qurʾānic mood-and-modal-particle system separates **deontic** contexts
> (legal command, prohibition) from **epistemic/alethic** ones (assertion of certain future
> event), and this separation is **orthogonal** to the function-word axis that
> `cross-finding-028-formal-register-coded-discourse-grammar.md` already uses.

The claim decomposes into two sub-claims that are tested separately and reported separately.

- **H1 — separation.** Surahs whose register is *legal* carry a modality profile shifted toward
  the deontic pole relative to surahs whose register is *eschatological*.
- **H2 — orthogonality.** The per-surah modality axis is uncorrelated with the per-surah
  cross-finding-028 function-word axis.

**H1 and H2 are in tension, and that tension is declared here rather than discovered later.**
cross-finding-028's own claim is that its six features separate the same three registers
(LOO accuracy 0.7692, `csv/h-new-2530.json`). If H1 holds and cross-finding-028 holds, both
axes carry register information, and two axes that both track register are correlated *through*
register. Marginal orthogonality is therefore a **strong** claim, not a weak one, and §7.4
pre-registers the conditional (register-partialled) form alongside it. A reader should treat
the marginal and the partial arms as answering different questions and should not read either
as the other.

---

## 2. Data, verified on disk

### 2.1 The six QAC counts — verified, with one frontier-map correction

All from `data/morphology/quranic-corpus-morphology-0.4.txt` (6,309,503 bytes; 128,219
segments; 77,429 words; 6,236 verses — all three re-counted by me).

| tag | frontier map | **verified here** | how counted |
|:--|--:|--:|:--|
| `MOOD:JUS` | 1,418 | **1,418** ✓ | substring `MOOD:JUS` in the FEATURES field |
| `MOOD:SUBJ` | 1,330 | **1,330** ✓ | substring `MOOD:SUBJ` in the FEATURES field |
| `POS:PRO` | 332 | **332** ✓ | TAG field (field 3) `== PRO` |
| `POS:CERT` | 414 | **414** ✓ | TAG field `== CERT` |
| `POS:FUT` | **161** | **161** ✓ | TAG field `== FUT` |
| `POS:EMPH` | 1,244 | **1,244** ✓ | TAG field `== EMPH` |

**Correction to the frontier map's stated method, not to its numbers.** The frontier map writes
these as `POS:PRO`, `POS:CERT`, `POS:FUT`, `POS:EMPH`. Only `POS:CERT` reproduces that way.
The others do not, and two of them fail in opposite directions:

- `grep -c "POS:FUT"` returns **42**, not 161. `FUT` splits across a prefix segment (`sa`,
  n = 119, FEATURES `PREFIX|sa+`, which carries no `POS:` field at all) and a stem segment
  (`sawofa`, n = 42, which carries `POS:FUT`). Only the stem is findable by the stated string.
- `grep -c "POS:EMPH"` returns **0**. Every `EMPH` in the corpus is an affix — 1,001 prefix
  `l:EMPH+` (لـ) and 243 suffix `+n:EMPH` (نون التوكيد) — and affix segments carry no `POS:`.
- `grep -c "POS:PRO"` returns **3,633**, an order of magnitude too many, because `POS:PRON`
  contains `POS:PRO` as a substring. This is the raw-substring failure the project's standing
  rules already warn about (`HANDOFF/CONTINUE-PROMPT.md`: "raw substring-counting LIES, use QAC
  lemma").

**All six of the frontier map's numbers are correct.** What is wrong is the field they are
attributed to, and one of the three failure modes would have inflated a count by 11×. This
pre-registration counts from **field 3 (TAG)** for the four particle classes and from the
FEATURES field for the two moods, and that is the locked rule.

### 2.2 Supporting counts, verified here

| quantity | value |
|:--|--:|
| `V` segments total | 19,356 |
| of which `IMPF` (the mood-bearing class) | 8,330 |
| of which `PERF` | 9,150 |
| of which `IMPV` (imperative form) | 1,876 |
| `MOOD:IND` | **0** — QAC marks mood only when SUBJ or JUS |
| `EMPH` prefix `l:EMPH` / suffix `n:EMPH` | 1,001 / 243 |
| `FUT` `sa` / `sawfa` | 119 / 42 |
| `CERT` `qad` (all three orthographies) / other | 406 / 8 |
| `PRO` (لا الناهية) | 332 |
| `NEG` `lam`+`lammā` / `lan`+`lan-` | 347 / 101 |
| jussive verbs carrying the `l:IMPV+` prefix (لام الأمر) | **78** |

`MOOD:IND = 0` is load-bearing: it forecloses the natural denominator
`JUS/(IND+SUBJ+JUS)` and is one reason §4.4 uses a ratio between the two poles rather than a
proportion within the mood system.

### 2.3 cross-finding-028's frozen artefacts

- `findings/phase-b-hypotheses/csv/h-new-2530.json` — `raw_feature_vectors`, 114 surahs × 6
  features, and `feature_sources`, the authoritative definition of each feature.
- `findings/phase-b-hypotheses/csv/h-new-2390.json` — `all_loci`, 16,998 iltifāt loci.
- `findings/phase-b-hypotheses/csv/h-new-2500.json` — `genre_proxy.surah_genre`, 114 labels.
- `findings/phase-b-hypotheses/scripts/h-new-2520.py`, `h-new-2250.py` — the detector code.

**Reproduction check performed before locking:** I re-derived `f_idh`, `f_lamma` and `f_qalu`
from QAC using the detector definitions in `h-new-2520.py:118–124` and compared all 342 cells
against the frozen vectors. **0 mismatches.** The frozen vectors are therefore not being taken
on trust; they are reproducible from the corpus. (`f_idha_cascade`, `f_doubling` and
`f_iltifat_type` are taken verbatim from the frozen JSON and are not re-derived; see §11.)

### 2.4 Register labels

`findings/classical-sources/neuwirth-sinai-genre-labels.tsv` — 114 surah rows, columns
`surah_number, surah_name_translit, neuwirth_phase, neuwirth_genre, sinai_genre,
jurjani_predicted_asyndeton_tier, mw5_confidence, notes`. Sources declared in its own header:
Neuwirth *Frühmekkanische Suren* (1981), Neuwirth *Der Koran als Text der Spätantike* (2010),
Sinai *The Qurʾān: A Historical-Critical Introduction* (2017).

---

## 3. THE FEATURE INTERSECTION — computed before locking, reported whatever it is

This is the check that decides whether an orthogonality claim is measurable at all. It is the
`AUDIT-H-NEW-206-LENGTH-CONFOUND.md` rule applied forwards: *if the thing you are predicting is
already one of the features you clustered on, the association you find is partly your own
construction.*

### 3.1 cross-finding-028's exact feature list

Verbatim from `csv/h-new-2530.json` → `features` and `feature_sources`:

| # | feature | definition, verbatim from the frozen JSON | token class it reads |
|:-:|:--|:--|:--|
| 1 | `f_idh` | `h-new-2520.json per_surah.idh / V` — verse word-1 segment `POS:T`, `LEM` exactly `<i*` | time-adverb إذ |
| 2 | `f_lamma` | `h-new-2520.json per_surah.lamma / V` — verse word-1 segment `POS:T LEM:lam~aA` | time-adverb لمّا |
| 3 | `f_qalu` | `h-new-2520.json per_surah.qalu / V` — verse word-1 `POS:V ROOT:qwl LEM:qaAla PERF 3MP` | perfect verb قالوا |
| 4 | `f_idha_cascade` | `h-new-2250.json runs.idha Σlength / V` — verse word-1 `POS:T LEM:<i*aA` | time-adverb إذا |
| 5 | `f_doubling` | `h-new-2490.json verse_grain_roster membership (binary)` | **surah-level binary**, 6 surahs {74, 75, 78, 82, 94, 102} |
| 6 | `f_iltifat_type` | `h-new-2390.json all_loci, 2500 type_tags: (n31−n23)/(n31+n23)` | **person and number** of any person-bearing word |

### 3.2 The candidate modality feature list

| feature | token class it reads |
|:--|:--|
| `JUS_prohibition` | imperfect verb, `MOOD:JUS`, governed by a `PRO` particle |
| `JUS_command` | imperfect verb, `MOOD:JUS`, carrying the `l:IMPV+` prefix (لام الأمر) |
| `JUS_negation_lam` | imperfect verb, `MOOD:JUS`, governed by `NEG` لم/لمّا |
| `JUS_conditional` | imperfect verb, `MOOD:JUS`, governed by a `COND` particle |
| `SUBJ_lan` | imperfect verb, `MOOD:SUBJ`, governed by `NEG` لن |
| `SUBJ_an_kay`, `SUBJ_purpose` | imperfect verb, `MOOD:SUBJ`, governed by `SUB`/purpose |
| `PRO`, `CERT`, `FUT`, `EMPH_pref`, `EMPH_suf` | the particle/affix segments themselves |

### 3.3 The intersection, measured

**Name-level intersection: ∅.** No feature name appears in both lists.

**Segment-level intersection: 0 segments.** Every ordered pair
(cross-finding-028 feature 1–4) × (modality feature) was intersected on QAC segment
locations `(surah, verse, word, segment)`. Total overlap across all 28 pairs: **0**.

**Word-level intersection with features 1–4: 1 word of 77,429.** Relaxing to the word level
(same word, different segment) finds exactly one hit — a single word counted by `f_qalu` that
also carries an `l:EMPH` prefix. This is 0.1 % of the `f_qalu` roster and 0.001 % of
`EMPH_pref`.

**Word-level intersection with `f_iltifat_type`: LARGE, and it is the one real finding of this
section.**

| modality feature | words that are also iltifāt-locus endpoints |
|:--|:--|
| `MOOD:JUS` | 1,013 / 1,418 = **71.4 %** |
| `MOOD:SUBJ` | 1,001 / 1,330 = **75.3 %** |
| `EMPH_suf` (نون التوكيد) | 205 / 243 = **84.4 %** |
| `FUT` | 98 / 161 = **60.9 %** |
| `EMPH_pref` | 316 / 1,001 = **31.6 %** |
| `PRO` | 0 / 332 = **0.0 %** |
| `CERT` | 0 / 414 = **0.0 %** |

**Against the base rate this overlap is unremarkable**: 68.8 % of *all* verbs and 64.3 % of all
imperfect verbs are iltifāt-locus endpoints, because `f_iltifat_type` is computed over every
person-bearing word in the corpus. Jussives at 71.4 % are at base rate, not enriched.

**But the count is the wrong diagnostic here, and the mechanism is the right one.** The two
features read *different properties* of an overlapping word population — mood versus person —
which by itself is legitimate. What is not merely incidental is that **Arabic grammar ties the
two properties together in exactly the deontic pole**:

| deontic category | 1st person | 2nd person | 3rd person |
|:--|--:|--:|--:|
| `JUS_prohibition` (n = 335) | 0 (0.0 %) | **308 (91.9 %)** | 27 (8.1 %) |
| `JUS_command` (n = 78) | 1 (1.3 %) | 0 (0.0 %) | **77 (98.7 %)** |

Prohibition is 2nd-person by default; لام الأمر is 3rd-person by default. And
`f_iltifat_type = (n31 − n23)/(n31 + n23)` is precisely a 3↔1-versus-2↔3 person contrast. A
surah dense in prohibitions supplies 2nd-person words that feed `n23`. **This is a grammatical
entailment linking the deontic pole to feature 6, and no token-disjointness argument dissolves
it.**

### 3.4 Governance and adjacency

| | same verse as any of features 1–4 | feature 1–4 marker within 5 words before | immediately before |
|:--|--:|--:|--:|
| `MOOD:JUS` (n = 1,418) | 85 (6.0 %) | 21 (1.5 %) | **0** |
| `MOOD:SUBJ` (n = 1,330) | 115 (8.6 %) | 30 (2.3 %) | **2** |

No modal verb in the corpus is governed by an إذ / لمّا / قالوا / إذا marker. The apparent
risk — that `f_lamma` might count the *negative* لمّا, which governs the jussive — does not
arise: `h-new-2520.py:121` requires `POS:T LEM:lam~aA`, the temporal adverb, whereas the
negative لمّا is tagged `NEG` (74 tokens).

### 3.5 What follows for the design — LOCKED

Per the instruction "*if the intersection is non-empty either drop those features or abandon
the orthogonality framing*":

- **Features 1–5 are token-disjoint from every modality feature.** They are retained.
- **Feature 6 (`f_iltifat_type`) is not entailment-disjoint from the deontic pole.** It is
  therefore **dropped from the arm that carries the orthogonality verdict.**

Two arms are locked, and both are reported with equal prominence:

- **ARM B (5 features: `f_idh`, `f_lamma`, `f_qalu`, `f_idha_cascade`, `f_doubling`) — this arm
  carries the H2 orthogonality verdict.** It is the arm on which "orthogonal" is a measurable
  claim.
- **ARM A (all 6 features, `f_iltifat_type` included) — the fidelity arm.** It is the axis
  cross-finding-028 actually uses. Its result is reported in full and is **not** permitted to
  establish an orthogonality verdict, because §3.3's entailment means a correlation there is
  partly guaranteed and a non-correlation there is partly luck.

**If Arm A and Arm B disagree, both are published and the Arm-B number is the one the verdict
is stated from.** Arm A's number is reported in the abstract of the finding alongside it.

---

## 4. The modality instrument — locked definitions

### 4.1 The named confound: the jussive is mostly not modal

`HANDOFF/FRONTIER-MAP-2026-08-07.md` F-10 names it: "*Jussive is heavily driven by lam +
past-negation, a purely syntactic trigger with no modal content. Must split lam-jussive from
imperative-jussive from conditional-jussive.*" Measured before locking, at window W = 5:

| trigger | n | share of `MOOD:JUS` |
|:--|--:|--:|
| `negation_lam` (لم / لمّا) — **no modal content** | 355 | 25.0 % |
| `conditional` (COND particle) — alethic/hypothetical | 343 | 24.2 % |
| `prohibition_la` (لا الناهية) — **deontic** | 335 | 23.6 % |
| unassigned | 297 | 20.9 % |
| `command_lam_amr` (لام الأمر) — **deontic** | 78 | 5.5 % |
| `sub_an_kay` | 10 | 0.7 % |

**Only 29.1 % of jussives are deontic.** A test using raw `MOOD:JUS` would be 25 % a test of
past negation. The split is mandatory and is locked below.

### 4.2 Trigger assignment rule — LOCKED

For a verb word at `(s, v, w)` carrying `MOOD:JUS` or `MOOD:SUBJ`:

1. If the word itself carries an `l:IMPV+` prefix segment → `command_lam_amr` (distance 0).
2. Otherwise scan backwards `d = 1 … W` word positions **within the same verse**. At the first
   distance `d` at which any trigger is found, return the highest-priority trigger present at
   that distance. Priority order, fixed:
   `prohibition_la` > `negation_lam` > `negation_lan` > `conditional` > `sub_an_kay` > `purpose`.
   - `prohibition_la` ⇐ a segment with TAG `PRO`
   - `negation_lam` ⇐ TAG `NEG` and FORM ∈ {`lamo`, `l~amo`}
   - `negation_lan` ⇐ TAG `NEG` and FORM ∈ {`lan`, `l~an`}
   - `conditional` ⇐ TAG `COND`
   - `sub_an_kay` ⇐ TAG `SUB`
   - `purpose` ⇐ TAG `P` with LEM exactly `kay` or `Hat~aY`
3. If nothing is found, and the verb word carries an `l:PRP` or `l:P` prefix → `purpose`.
4. Otherwise `unassigned`.

`W = 5` primary; `W = 40` (effectively whole-verse) as rules-tuple RT-4.

### 4.3 Window sensitivity — measured before locking

| W | prohibition | command | negation_lam | conditional | unassigned |
|--:|--:|--:|--:|--:|--:|
| 3 | 330 | 78 | 350 | 291 | 362 |
| **5** | **335** | **78** | 355 | 343 | 297 |
| 8 | 336 | 78 | 356 | 378 | 251 |
| 40 | 337 | 78 | 360 | 399 | 214 |

**The deontic pole is window-insensitive**: 330 → 337 over a 13× window change, and
`command_lam_amr` is exactly constant at 78 because it is verb-internal. The window is a free
parameter that does not touch the quantity the hypothesis is about. All the movement is between
`conditional` and `unassigned`, neither of which enters either pole.

### 4.4 The two poles — LOCKED

**Deontic** — ṭalab in al-Suyūṭī's sense (§9), the command/prohibition pole:

```
D(s) = #{ MOOD:JUS verbs in surah s with trigger prohibition_la }
     + #{ MOOD:JUS verbs in surah s with trigger command_lam_amr }
```

Corpus total D = **413**. `PRO` particle count (332) is a cross-check on the prohibition arm,
not an addend; counting both would double-count one speech act.

**Epistemic/alethic** — khabar and its intensifiers, the certain-assertion pole:

```
E(s) = #{ CERT segments } + #{ FUT segments } + #{ EMPH segments with l:EMPH prefix }
     + #{ MOOD:SUBJ verbs with trigger negation_lan }
```

Corpus total E = **1,684**.

**Excluded from E, with reasons locked here:** the `n:EMPH` suffix (نون التوكيد, 243) is
excluded because it attaches freely to *imperative and prohibitive* verbs
(`wa-lā taḥsabanna`) and is therefore not a clean epistemic marker; including it would import
deontic tokens into the epistemic pole.

**The contrast:**

```
M(s) = log( (D(s) + 0.5) / (E(s) + 0.5) )
```

Haldane–Anscombe-corrected log ratio. Three properties, each locked for a stated reason:

1. **It has no unit count in its denominator.** Word count, verse count and surah length cancel
   exactly. This is `UNIT-DRIFT-DEFECT.md` §6's per-word re-normalisation taken to its limit:
   the divisor is not a unit count at all, it is the other pole. The correlation of `M` with
   every length channel is nevertheless measured and reported before the primary test (§6),
   because *normalisation is not invariance*.
2. **It is defined on all 114 surahs.** Measured before locking: `D + E = 0` on **14** surahs
   (1, 88, 94, 97, 99, 101, 105, 107, 108, 109, 110, 112, 113, 114), all short, and **four of
   them (88, 97, 99, 101) are in the eschatological register**. An unsmoothed contrast would
   have deleted 14 % of the corpus non-randomly, and 14 % of the eschatological arm. That
   measurement is why the smoothing is here; see the forking-paths log (§10).
3. **It avoids the tie-mass of a bounded contrast.** `D = 0` on 45 surahs and `E = 0` on 17;
   `(D−E)/(D+E)` would pile 62 surahs onto exactly two values, which a rank statistic cannot
   use. RT-5 runs the bounded form anyway as a robustness arm.

### 4.5 The cross-finding-028 axis scalar — LOCKED

```
R = first principal component of the z-scored feature matrix over all 114 surahs,
    sign fixed so that the loading on f_qalu is POSITIVE.
```

`f_qalu` is chosen as the sign anchor because it is cross-finding-028's strongest feature
(ANOVA F = 33.54, `csv/h-new-2530.json` → `anova_F_per_feature`), fixed before running. `R_B`
uses the 5 Arm-B features; `R_A` uses all 6.

Two assumption-free companions are also locked, so that no verdict rests on PC1 alone:
- the six per-feature Spearman correlations ρ(M, f_j), Bonferroni k = 6, α = 0.008333;
- the multiple correlation of `M` on the feature set (OLS on z-scores), with LOOCV R².

### 4.6 Register labels — LOCKED mechanical mapping

From `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`, column 5 (`sinai_genre`),
case-insensitive substring:

- contains `legal` → **LEGAL** — n = **17**: {2, 3, 4, 5, 8, 9, 24, 33, 47, 49, 58, 59, 60, 62, 65, 66, 98}
- contains `eschatolog` → **ESCHAT** — n = **28**: {44, 50, 51, 52, 54, 56, 67, 69, 70, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 97, 99, 101, 104}
- both → 0 surahs (verified; the rule is unambiguous)
- neither → 69 surahs, excluded from H1

RT-2 substitutes `csv/h-new-2500.json` → `genre_proxy.surah_genre`, i.e.
cross-finding-028's own labels (`legal_medinan` n = 20 vs `eschatological_mufassal` n = 40).

---

## 5. Directions — LOCKED AND JUSTIFIED

**H1 direction: Δ = mean(M | LEGAL) − mean(M | ESCHAT) > 0.**

Justification, in three independent registers, all locked before running:

1. **Classical.** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 57 *fī al-khabar wa-l-inshāʾ*
   (§9) divides all discourse into *khabar* — that which admits *taṣdīq wa-takdhīb*, being
   affirmed true or false — and *ṭalab/inshāʾ*, of which *amr* and *nahy* are the two
   non-interrogative species. Legal discourse is the home of amr and nahy; eschatological
   discourse is khabar about a certain future, and khabar is what قد, لـ and س/سوف intensify.
2. **Grammatical.** The deontic pole is constituted by لا الناهية and لام الأمر, whose
   discourse function *is* legislation. The epistemic pole is constituted by the classical
   *muʾakkidāt al-khabar*.
3. **Empirical, from this project.** cross-finding-028 already reports that the eschatological
   register is marked by the إذا conditional cascade and the ثمّ doubling intensifier — both
   assertoric — and that the legal register is keyed by يا أيها الذين آمنوا, a vocative that
   introduces commands.

**A reversed Δ is a pre-commit violation and will be published as NULL with full prominence,
under the label PRE-COMMIT VIOLATION, per `INVESTIGATION-PROTOCOL.md` §1.8.** It will not be
reframed as "an unexpected direction".

**H2 direction: none.** H2 is an equivalence claim and is two-sided by construction. There is
no direction to violate. What replaces the direction lock is the equivalence bound in §7.2,
which is locked here for exactly the same reason.

---

## 6. The named confound — length — and how it is handled

### 6.1 Channel ranking, measured before locking

Spearman ρ of each cross-finding-028 feature with each length channel, all 114 surahs:

| feature | log word count | verse count | mean verse length | mushaf position |
|:--|--:|--:|--:|--:|
| `f_idh` | **+0.4879** | +0.4647 | +0.3439 | −0.4806 |
| `f_lamma` | **+0.5731** | +0.5699 | +0.3262 | −0.5096 |
| `f_qalu` | +0.5672 | **+0.6113** | +0.2762 | −0.5285 |
| `f_idha_cascade` | −0.0529 | +0.0283 | **−0.1233** | +0.0550 |
| `f_doubling` | −0.2017 | −0.1039 | **−0.2668** | +0.1910 |
| `f_iltifat_type` | +0.2325 | **+0.3539** | +0.0169 | −0.1823 |

Channel-versus-channel: ρ(log word count, mushaf position) = **−0.9331**, reproducing
`UNIT-DRIFT-DEFECT.md` §3's −0.9342 to three decimals; ρ(log word count, verse count) = +0.9102;
ρ(verse count, mushaf position) = −0.8446, reproducing that table's −0.8446 exactly.

**Three of cross-finding-028's six features carry a length correlation near +0.5 to +0.6.**
The winning channel is not the same for all six — log word count for `f_idh` and `f_lamma`,
verse count for `f_qalu` and `f_iltifat_type`, mean verse length for the two sparse features.
`UNIT-DRIFT-DEFECT.md` §5 requires ranking on the data rather than carrying a channel across,
so **no single channel is locked as *the* nuisance channel. All four are run.**

### 6.2 What is locked

1. **Before the primary test the run prints, and the results JSON records first**, ρ of every
   feature used — the six cross-finding-028 features, `D`, `E`, `M`, `R_A`, `R_B` — against all
   four channels. This block is written before any primary statistic is computed, and its
   position in the output file is part of the lock.
2. **`M` is by construction free of a unit-count denominator** (§4.4). This is an argument, not
   a measurement, and §6.1's own closing line — *normalisation is not invariance* — is why the
   measurement is run anyway.
3. **Every primary statistic is computed twice: raw, and rank-residualised on the length
   channel.** Rank-residualisation: replace `x` by the residual of `rank(x)` regressed on
   `rank(c)` by OLS. For H2 this yields the partial Spearman correlation. All four channels are
   run; **all four are reported; none is selected after the fact.**
4. **For H1 the length-residualised statistic is the PRIMARY one** (§7.1), because the legal
   register is systematically long and the eschatological register systematically short, and a
   raw contrast between them is partly a contrast between long and short surahs.

---

## 7. Primary tests, null models and the exact decision rule

Seed **20260509**, **10,000** permutations, everywhere. No parametric p-value is a primary
test anywhere in this pre-registration.

### 7.1 H1 — separation

- **Statistic** `Δ = mean(M_resid | LEGAL) − mean(M_resid | ESCHAT)`, where `M_resid` is `M`
  rank-residualised on **log surah word count**.
- **Null** — permute the LEGAL/ESCHAT labels among the 45 labelled surahs, unstratified,
  10,000 draws, seed 20260509. Unstratified is correct *here* because the length channel has
  already been removed from the statistic; stratifying as well would control it twice.
- **p** one-sided in the locked direction, `p = (#{Δ_perm ≥ Δ_obs} + 1)/(n_perm + 1)`.
- **Secondary nulls, all reported:** (a) raw `M`, permutation stratified within **quintiles**
  of log word count; (b) raw `M`, stratified within **deciles**; (c) raw `M`, unstratified.
  Two bin widths are mandatory under `UNIT-DRIFT-DEFECT.md` §6.1 clause 2.
- **Degeneracy check, mandatory and reported whatever it shows** — for each stratified null,
  record the number of *distinct* label vectors drawn in 10,000 attempts and the fraction
  differing from the observed. `UNIT-DRIFT-DEFECT.md` §4.1: *a null that cannot draw the thing
  it compares against is not a comparison.* If a stratified null yields **fewer than 100
  distinct labellings**, it is declared **DEGENERATE** and reported as such; it does not
  contribute to any verdict, and the degeneracy is itself reported as a finding about the
  register–length confound.

### 7.2 H2 — orthogonality: the equivalence bound, locked with its power stated

- **Statistic** `ρ = Spearman(M, R_B)` over all 114 surahs (Arm B; Arm A reported alongside).
- **Interval** 10,000-resample percentile bootstrap 95 % CI, seed 20260509, resampling surahs.
  The Fisher-z analytic interval is reported as a cross-check, not as the primary interval.
- **EQUIVALENCE BOUND, LOCKED: δ = 0.25.** Also reported at δ = 0.20 (strict) and δ = 0.30
  (lenient). Where they disagree the stricter is taken, per `UNIT-DRIFT-DEFECT.md` §6 rule 6.

**The power of this bound, computed and stated here BEFORE the run.** At n = 114 the Fisher-z
standard error is 1.06/√111 = 0.10061 and the 95 % half-width is 0.19720, so a point estimate of
exactly zero yields a CI of [−0.1947, +0.1947]. Therefore:

| δ | equivalence can pass only if | verdict on the bound's usability |
|--:|:--|:--|
| 0.20 | \|ρ̂\| ≤ **0.0055** | essentially unattainable at n = 114 |
| **0.25** | \|ρ̂\| ≤ **0.0582** | **attainable but demanding — this is the locked primary** |
| 0.30 | \|ρ̂\| ≤ **0.1119** | comfortable, but 9 % shared variance is weak orthogonality |

**This is disclosed before the run so that no reader need wonder whether the bound was chosen
after seeing ρ̂.** It also states the honest limit up front: **n = 114 surahs cannot establish
orthogonality at any bound tighter than ≈ 0.20, no matter what the data say.** That is a fact
about the design, not about the corpus, and it will be repeated in the finding.

- **DECISION RULE — three-way, per bound δ, per arm:**
  - **ORTHOGONAL** iff `CI_low ≥ −δ AND CI_high ≤ +δ` (the whole interval inside the bound)
  - **NOT-ORTHOGONAL** iff `CI_low > +δ OR CI_high < −δ` (the whole interval outside the bound)
  - **INDETERMINATE** otherwise — *and this is the honest label for a wide interval straddling
    zero.* A non-significant p is not orthogonality.
- **Companion permutation test**, reported but not the equivalence verdict: two-sided
  permutation p for `ρ ≠ 0`, permuting `M` against `R`, 10,000 draws, seed 20260509.
- **Length control:** partial Spearman ρ(M, R | c) for each of the four channels, each with its
  own bootstrap CI and its own three-way verdict at each δ.

### 7.3 Bonferroni

- **Primary family, k = 2**: {H1 (§7.1), H2 companion permutation on Arm B (§7.2)}.
  **α_bon = 0.025.**
- **Secondary family, k = 6**: the six per-feature ρ(M, f_j). **α = 0.008333.**
- The equivalence tests are interval-based and are not p-value tests; no Bonferroni applies to
  them. Reporting three δ values is a sensitivity display, not a multiple test, and the primary
  δ is locked at 0.25 regardless of what the other two show.
- Rules-tuple arms RT-2 … RT-5 are **robustness only**, reported uncorrected, and **may not
  establish or overturn a verdict.**

### 7.4 The conditional form of the orthogonality claim

Because §1 declares H1 and H2 to be in tension, the register-partialled correlation is
pre-registered as a distinct, separately-reported quantity — **not** as a fallback if the
marginal fails:

`ρ(M, R_B | register)`, computed by rank-residualising both `M` and `R_B` on the
three-level Neuwirth–Sinai register indicator (LEGAL / ESCHAT / neither), with its own bootstrap
CI and its own three-way verdict at each δ.

**Its interpretation is fixed here:** marginal orthogonality asks *are the two axes unrelated?*;
conditional orthogonality asks *do the two axes carry unrelated information once register is
known?* They are different claims and the finding will report both under their own names. A
pass on one may not be reported as a pass on the other.

---

## 8. Rules-tuples

**RT-1 (PRIMARY):** `(no-tashkeel, QAC-v0.4 TAG-field + FEATURES-field, per-surah, trigger
window W = 5, E includes l:EMPH prefix and excludes n:EMPH suffix, register = Neuwirth–Sinai
sinai_genre mechanical mapping, M = smoothed log-ratio, basmala-counted-only-in-Q1, Hafs-Kufan,
Mashriqi)`

Each robustness tuple changes **exactly one** element of RT-1:

| tuple | the single change |
|:--|:--|
| **RT-2** | register labels ← `csv/h-new-2500.json` `genre_proxy.surah_genre` (cross-finding-028's own) |
| **RT-3** | `E` excludes the `l:EMPH` prefix (E = CERT + FUT + SUBJ_lan only) |
| **RT-4** | trigger window `W = 40` (whole verse) |
| **RT-5** | `M = (D − E)/(D + E + 1)` (bounded contrast) instead of the log-ratio |

Five tuples in total, exceeding the ≥ 2 requirement. A verdict that flips between RT-1 and any
robustness tuple is reported as **RULES-TUPLE-FRAGILE** in the finding's abstract, not buried.

---

## 9. Classical anchor — verified on disk, correcting a false absence

`HANDOFF/FRONTIER-MAP-2026-08-07.md` F-10 gives the anchor as al-Sakkākī's *Miftāḥ al-ʿulūm*
and adds "*I did not find the text on disk*."

**I re-ran that search rather than inheriting it**, per `ABSENCE-CLAIMS.md` §1 ("*an absence
claim may not be inherited*") and §3 Screen C ("*grep the findings you cite as parents*"):

```
find data findings -iname "*sakkak*" -o -iname "*miftah*" -o -iname "*miftaH*"   →  no results
```

**al-Sakkākī is genuinely absent, and F-10's absence claim is TRUE.** But the anchor it was
reaching for is on disk under a different author, with page numbers:

> **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, النوع السابع والخمسون: في الخبر والإنشاء
> (nawʿ 57, "On khabar and inshāʾ"), vol. III pp. 255–257.**
> `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, heading at line 17808;
> page markers `PageV03P255` (line 17807), `PageV03P256` (17824), `PageV03P257` (17841).

The passage supplies the division this hypothesis operationalises, in al-Suyūṭī's own words:

- The tripartite scheme and its criterion — «**وقال كثيرون ثلاثة خبر وطلب وإنشاء قالوا لأن
  الكلام إما أن يحتمل التصديق والتكذيب أو لا الأول الخبر**» — *khabar* is what admits
  affirmation or denial; *ṭalab* and *inshāʾ* are what do not.
- The sub-division of *ṭalab* — «**إن أفاد بالوضع طلبا فلا يخلو إما أن يكون بطلب ذكر الماهية أو
  تحصيلها أو الكف عنها والأول الاستفهام والثاني الأمر والثالث النهي**» — ṭalab is
  interrogation, **command (amr)**, or **prohibition (nahy)**. The second and third are exactly
  the deontic pole of §4.4.
- The definition of khabar by truth-evaluability, «الخبر الكلام الذي يدخله الصدق والكذب»
  attributed to al-Qāḍī Abū Bakr [al-Bāqillānī] and the Muʿtazila, with the objection that
  God's khabar is only ever true — which is the epistemic pole of §4.4 in its Qurʾānic form.

**And the same passage supplies this test's sharpest limit, so it is locked here rather than
discovered later.** al-Suyūṭī writes «القصد بالخبر إفادة المخاطب **وقد يرد بمعنى الأمر** نحو:
{والوالدات يرضعن} {والمطلقات يتربصن} **وبمعنى النهي** نحو: {لا يمسه إلا المطهرون}» — *khabar
form routinely carries amr and nahy force*, and his three examples (Q 2:233, Q 2:228, Q 56:79)
are core legal verses in indicative form. Ibn al-ʿArabī's dissent from this is recorded in the
same passage.

**The consequence for H1, stated before the run: this instrument measures grammatical FORM, and
al-Suyūṭī documents that legal FORCE is routinely carried by non-deontic form, disproportionately
in the legal register.** `D` therefore under-counts legal deontic force where legal deontic
force is densest. **This biases H1 toward the null**, which makes a pass conservative and makes
a failure genuinely ambiguous between "no effect" and "form is the wrong instrument". That
ambiguity is a limit of the test and will be stated as one.

---

## 10. Garden-of-forking-paths log

Every choice made between receiving the hypothesis and locking this file.

| # | decision | when | why, and what it was decided against |
|:-:|:--|:--|:--|
| 1 | Count particles from TAG field 3, not `POS:` substrings | before lock | `POS:PRO` matches `POS:PRON` (3,633 vs 332, 11× inflation); `POS:EMPH` returns 0; `POS:FUT` returns 42 of 161. Discovered while verifying §2.1. |
| 2 | Split `MOOD:JUS` by governing trigger | before lock | F-10's own named confound. Measured: only 29.1 % of jussives are deontic. |
| 3 | `W = 5` primary, `W = 40` robustness | before lock, after measuring §4.3 | The deontic pole moves 330→337 across W ∈ {3,…,40}; W is a free parameter that does not touch the quantity under test. Had it moved, W would have been a declared researcher degree of freedom. |
| 4 | Exclude `n:EMPH` (نون التوكيد) from `E` | before lock | It attaches to imperatives and prohibitives (`wa-lā taḥsabanna`), so it would import deontic tokens into the epistemic pole. Decided on grammar, before any per-surah count. |
| 5 | `M` = smoothed **log-ratio**, not a bounded contrast | before lock, after measuring §4.4 | `D+E = 0` on 14 surahs, 4 of them eschatological; `D = 0` on 45 and `E = 0` on 17 would pile 62 surahs on two values. Unsmoothed and bounded forms are kept as robustness arms (RT-5 and §4.4 note), not discarded. |
| 6 | Drop `f_iltifat_type` from the verdict-bearing arm | before lock, after measuring §3.3 | Prohibition is 91.9 % 2nd-person and لام الأمر 98.7 % 3rd-person; `f_iltifat_type` is a 2↔3-versus-3↔1 contrast. Grammatical entailment, not token overlap. Arm A retained and reported. |
| 7 | Run all four length channels rather than lock one | before lock, after measuring §6.1 | The winning channel differs across the six features. `UNIT-DRIFT-DEFECT.md` §3's own table was wrong on this for months. |
| 8 | H1 primary statistic is length-**residualised** | before lock | Legal surahs are long, eschatological short; stratified permutation with 17 vs 28 units risks a degenerate null. Stratified arms are run anyway with an explicit degeneracy count. |
| 9 | δ = 0.25 primary, with the power table stated in §7.2 | before lock | Computed from n = 114 alone, with no data-dependent input. δ = 0.20 and 0.30 also reported. |
| 10 | Classical anchor moved from al-Sakkākī to al-Suyūṭī nawʿ 57 | before lock | al-Sakkākī verified absent by my own `find`; al-Suyūṭī's *khabar/inshāʾ* nawʿ is on disk with page numbers and is the better anchor. |
| 11 | Two arms (A and B) rather than one | before lock | See row 6. Locking a single arm would have forced a choice between fidelity to cross-finding-028 and measurability of orthogonality. |

**Nothing in this table was decided after seeing any primary statistic**, and §0 lists exactly
what has and has not been computed.

---

## 11. Declared limits, locked before the run

1. **n = 114 caps the equivalence test.** §7.2's power table is the statement of this. The
   surah is the unit because cross-finding-028's features are frozen at surah scale; a
   pericope-scale re-run would need all four parent detectors rebuilt and is out of scope here.
2. **Form, not force.** §9. The single largest limit, and it comes from the classical source.
3. **`f_idha_cascade`, `f_doubling`, `f_iltifat_type` are consumed from frozen JSON and not
   re-derived.** `f_idh`, `f_lamma`, `f_qalu` **were** re-derived and matched 342/342 cells.
   Any error inside the three unre-derived features propagates into `R`.
4. **`f_doubling` is a 6-surah binary.** Its contribution to PC1 is near-degenerate and its
   ρ with anything is dominated by 6 units.
5. **The register labels are surah-scale.** cross-finding-028's own §"Honest qualifications"
   already flags this: Q 2 is both legislative and narrative. A surah-dominant label smears
   every within-surah register alternation.
6. **cross-finding-028 carries a live correction notice** (2026-08-07) recording that the
   pericope-flip test built on it flips 5/5 on pre-Islamic poetry and 4/5 on al-Bukhārī. **Its
   own six numbers reproduce and are not retracted** — which is all this test needs, since this
   test uses the feature vectors, not the flip claim. **No result here may be reported as
   evidence that this corpus is structurally unusual**; no cross-corpus baseline is run.
7. **No cross-corpus control is run at all.** Nothing here discriminates this corpus from any
   other. The finding will say so in its abstract.
8. **The 69 surahs labelled neither LEGAL nor ESCHAT are excluded from H1** but retained in H2.
   The two sub-claims are therefore computed on different samples, which is stated in the
   finding rather than smoothed over.

---

## 12. Deliverables and integrity

- Script: `findings/phase-b-hypotheses/scripts/h-new-3040.py`, with the SHA-256 of **this file**
  embedded as `EXPECTED_PREREG_SHA` and verified at runtime with `SystemExit` on mismatch.
- Run directory: `findings/phase-b-hypotheses/runs/h-new-3040/<UTC timestamp>/`, created with
  `os.makedirs(..., exist_ok=False)`, every file opened with mode `'x'`. **Written once, at
  completion; never overwritten** (`UNIT-DRIFT-DEFECT.md` §7). **Never deleted**, including if
  superseded (STANDING RULE 2).
- Finding: `findings/phase-b-hypotheses/h-new-3040-modality-axis.md`.
- **This file is never edited after the run**, for any reason, including to correct an error in
  it (`UNIT-DRIFT-DEFECT.md` §9). Corrections go in the finding.
- The verdict function in the script must be diffed against §7 line by line before running
  (STANDING RULE 1).

---

*Pre-registered 2026-08-09 by Waiel Al-Shujaa. The intersection was enumerated before the axis
was named, and the bound was locked before the correlation was seen. Bismillāhi al-Raḥmāni
al-Raḥīm.*
