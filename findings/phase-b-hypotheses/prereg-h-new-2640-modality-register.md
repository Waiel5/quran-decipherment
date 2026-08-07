---
id: H-NEW-2640
title: Pre-registration — Does the mood/modality system separate deontic command from epistemic certainty across the three Quranic registers?
date: 2026-08-07
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE any register-split computation
family: MODALITY-2026-08-07-A
seed: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 4
alpha_bonferroni: 0.0125
parents: [H-NEW-2500, H-NEW-2530, cross-finding-028-formal]
---

# Pre-registration — H-NEW-2640

**Nothing in this file may be amended after the SHA-256 below is embedded in
`scripts/h-new-2640.py`.** Direction is locked in §5. Failure conditions are locked in §9.
A reversed direction is a pre-commit violation and will be published as NULL with equal
prominence, not redefined.

---

## 1. The claim

Arabic grammar divides utterance into **ṭalab** (demand — the speaker seeks the
realization of something not yet real) and **khabar** (assertion — the speaker reports
something as true or certain). The narrow, testable consequence:

> **H-NEW-2640.** *Deontic* modality (command, prohibition) and *epistemic/alethic*
> modality (certainty, emphatic assertion, future prediction) are not distributed alike
> across the three Quranic registers of cross-finding-028-formal. Deontic marking
> concentrates in **legal-Medinan**; epistemic marking concentrates in
> **eschatological-mufaṣṣal**. The two indices carry register information that the
> existing six-feature vector of H-NEW-2530 does not already contain.

If it holds, modality is a **fifth, orthogonal column** for cross-finding-028-formal,
which at present has **no mood feature at all**.

## 1.1 What this test is NOT

Conditionals are **out of scope by construction**. H-NEW-2250 owns the *idhā* cascade;
a parallel registered test (H-NEW-2630) owns *in* / *law*. The conditional jussive
classes defined in §3.3 are computed **only in order to be excluded** from the deontic
index, and are reported as a residual bucket. No conditional statistic is registered here.

---

## 2. Instrument (MW-1 — locked before observation)

### 2.1 Source and matching discipline

Single morphological source: `data/morphology/quranic-corpus-morphology-0.4.txt`
(QAC v0.4, 128,219 annotation rows, SHA-256 in §8).

**Matching is on QAC feature *atoms*, never on substrings.** The `FEATURES` column is
split on `|` and matched by **exact atom equality**. Substring matching on this file is
demonstrably wrong, and the demonstration is registered here as a standing project
exhibit:

| test | result |
|:--|--:|
| `'POS:PRO' in FEATURES` (substring) | **3,633** |
| `'POS:PRO' in FEATURES.split('|')` (atom) | **332** |

The 3,301-token excess is `POS:PRON` — *pronoun* — of which `POS:PRO` is a prefix.
A substring count of the prohibition particle would have been **10.9× too large**.

### 2.2 Two corrections to the counts as reported in the frontier map

Both were verified against the file before this pre-registration was locked. **The
totals are right; the labels are wrong**, and the labels matter because they name
feature strings that do not exist.

| frontier-map label | reality in QAC v0.4 |
|:--|:--|
| `POS:EMPH` 1,244 | **There is no `POS:EMPH` tag in QAC.** EMPH is a *clitic* tag: prefix atom `l:EMPH+` = **1,001** (lām al-tawkīd) plus suffix atom `+n:EMPH` = **243** (nūn al-tawkīd). 1,001 + 243 = 1,244. |
| `POS:FUT` 161 | `POS:FUT` alone = **42** (all `LEM:sawof`). The other **119** are the prefix atom `sa+`. 42 + 119 = 161. |

Verified and unchanged: `MOOD:JUS` 1,418 · `MOOD:SUBJ` 1,330 · `POS:CERT` 414 ·
`POS:PRO` 332.

### 2.3 Unit, denominator, population

- **Unit of analysis:** the surah.
- **Population:** the **91** surahs carrying one of the three registers (§4).
- **Denominator:** distinct QAC orthographic word-tokens `(surah, verse, word)` in the
  surah. Corpus total **77,429** over **6,236** verses and **114** surahs. QAC counts the
  basmala **only in Q 1** (verified: `(2:1:1:1)` is `Al^m^`, not `bi`), which is the
  project's default rules-tuple.
- **Density** = markers per **1,000** word-tokens.

---

## 3. THE CONFOUND, and the split that neutralises it

### 3.1 Statement of the confound

`MOOD:JUS` is **not** a modality feature. It is a morphosyntactic case-form triggered by
several unrelated governors, the largest of which is ***lam* + past-negation** — pure
negation with no modal content whatsoever. **Testing raw `MOOD:JUS` measures negation,
not modality, and any result from it is worthless.** The split below is therefore
mandatory and is locked before any register-split computation.

### 3.2 The governor rule (locked verbatim; this is the whole rule)

For each segment *i* carrying atom `MOOD:JUS`:

1. If any segment preceding *i* **inside the same orthographic word** `(s,v,w)` carries
   atom `l:IMPV+` → **`D_lam_amr`**.
2. Otherwise scan *j* = *i*−1 downward while `(s,v)` is unchanged:
   - `FEATURES` starts with `PREFIX|` → if it carries `l:IMPV+` → **`D_lam_amr`**, stop;
     else continue scanning (conjunctive/resumptive prefixes are transparent).
   - `FEATURES` starts with `SUFFIX|` → continue scanning.
   - otherwise it is a `STEM`: read its `POS:` and `LEM:` atoms and **stop**, assigning
     - `POS:PRO` ∧ `LEM:laA` → **`D_pro_la`** (prohibitive *lā tafʿal*)
     - `POS:NEG` ∧ `LEM:lam` or `LEM:l~am~aA` → **`N_lam`** (the confound)
     - `POS:NEG` ∧ `LEM:laA` → **`X_neg_la`** (ambiguous; see §7 tuple T2)
     - `POS:COND` → **`C_cond`**
     - `POS:REL` ∧ `LEM:man` or `LEM:maA` → **`C_cond_rel`**
     - anything else → unresolved, go to 3.
3. Unresolved: rescan the whole verse before *i* —
   - any earlier `POS:COND`, or `POS:REL` ∧ `LEM ∈ {man, maA}` → **`C_apodosis`**
   - else any earlier segment carrying `IMPV` or `l:IMPV+` → **`C_jawab_talab`**
   - else → **`R_other`**

### 3.3 The locked split (corpus-wide calibration — computed BEFORE any register split)

| class | n | modal content | goes into |
|:--|--:|:--|:--|
| `N_lam` | **351** | none — past negation | **excluded (the confound)** |
| `D_pro_la` | **330** | prohibition | **DEONTIC** |
| `C_cond` | **220** | conditional protasis | excluded — H-NEW-2630's turf |
| `C_apodosis` | **189** | conditional apodosis | excluded — H-NEW-2630's turf |
| `X_neg_la` | **110** | ambiguous *lā* (see T2) | **excluded under T1**, deontic under T2 |
| `D_lam_amr` | **78** | 3rd-person command (lām al-amr) | **DEONTIC** |
| `C_jawab_talab` | **67** | apodosis of a demand | excluded |
| `C_cond_rel` | **45** | conditional relative | excluded — H-NEW-2630's turf |
| `R_other` | **28** | unresolved | excluded |
| **total** | **1,418** | | |

**Only 408 of 1,418 jussives (28.8%) are deontic.** 351 are negation. Raw `MOOD:JUS`
is 71.2% not-modality; this is the confound made quantitative.

### 3.4 The indices

**DEONTIC index D(s)** — markers per 1,000 word-tokens:

| | atom condition | n |
|:--|:--|--:|
| D1 | `POS:V` ∧ `IMPV` (imperative verb) | 1,876 |
| D2 | `MOOD:JUS` classed `D_pro_la` | 330 |
| D3 | `MOOD:JUS` classed `D_lam_amr` | 78 |
| D4 | `POS:IMPN` (imperative verbal noun) | 2 |
| | **total** | **2,286** |

**EPISTEMIC index E(s)** — markers per 1,000 word-tokens:

| | atom condition | n |
|:--|:--|--:|
| E1 | `POS:CERT` (*qad* and the taḥqīq set) | 414 |
| E2 | `l:EMPH+` ∨ `+n:EMPH` (lām / nūn al-tawkīd) | 1,244 |
| E3 | `POS:FUT` ∨ `sa+` (*sawfa* / *sa-*) | 161 |
| E4 | `POS:ACC` ∧ `LEM:<in~` (*inna*, ḥarf tawkīd) | 1,682 |
| | **total** | **3,501** |

E4 takes ***inna* only**. `POS:ACC` also contains `>an~` (362, complementizer),
`laEal~`/`l~aEal~` (129, hope), `la`kin~`/`la`kin` (65, adversative), `ka>an~` (29,
simile), `layot` (14, wish) and `wayoka>an~` (2) — none of which assert certainty.
Adding `>an~` is registered as tuple T2, not as a free choice.

**CONFOUND index J(s)** — raw `MOOD:JUS` density, all 1,418, the naive instrument.
Registered **only** as the comparator in I4.

### 3.5 Length control (MW-1)

Legal discourse lives in long surahs. Every index is residualised by ordinary least
squares on the design matrix `[1, log(n_verses(s)), mean_words_per_verse(s)]` fitted over
the 91 surahs. **The residual is the primary variable.** Raw densities are reported
alongside, always, in the same tables.

Null B (§6) adds a second, non-parametric length control on top of this.

---

## 4. Register labels — reused, never re-derived

Labels are taken through the pointer H-NEW-2530 itself records:
`csv/h-new-2500.json` → `genre_proxy.surah_genre`, cited in `csv/h-new-2530.json` as
*"h-new-2500.json genre_proxy.surah_genre (reused verbatim)"*. No label is invented,
re-derived or adjusted. Class names are used with H-NEW-2530's exact spelling:
`narrative` · `legal_medinan` · `eschatological_mufassal` (+ residual
`liturgical_didactic`, excluded from the primary as in H-NEW-2530).

Locked marginals: **31 / 20 / 40 / 23**, N = **91** for the primary.

---

## 5. Registered inferences and LOCKED directions

Family of **four**. Bonferroni **k = 4**, **α_bon = 0.05 / 4 = 0.0125**.

### I1 — DEONTIC × register
Statistic: one-way ANOVA **F** of `D_resid` across the three registers.
**PASS requires** perm-p < 0.0125 **AND** `argmax` of the per-register `D_resid`
centroid == **`legal_medinan`**.
*Justification of direction:* legal discourse is the register whose speech-act is
ṭalab — obligation and prohibition — and cross-finding-028-formal already identifies
legal-Medinan by its 2↔3 direct-community-address grammar, which is the person-deixis of
commanding. Command marking should follow the addressee.

### I2 — EPISTEMIC × register
Statistic: one-way ANOVA **F** of `E_resid` across the three registers.
**PASS requires** perm-p < 0.0125 **AND** `argmax` of the per-register `E_resid`
centroid == **`eschatological_mufassal`**.
*Justification of direction:* the eschatological register asserts the certainty of a
future event against denial. That is exactly the environment of *qad*, of the oath-lām
and nūn al-tawkīd, of *inna*, and of *sa-/sawfa*. It is khabar under contestation, which
is where classical rhetoric places the emphatic apparatus.

### I3 — ORTHOGONALITY (the real deliverable)
Statistic: **Δ = LOO₈ − LOO₆**, leave-one-out nearest-centroid accuracy of the
H-NEW-2530 vector extended with `[D_resid, E_resid]` minus the published six-feature
accuracy. Pipeline, z-scoring, tie-break and confusion accounting are byte-identical to
`scripts/h-new-2530.py`.
Null: permute `(D_resid, E_resid)` **as a bound pair** across the 91 surahs — this
destroys the register link while preserving the six features and the D–E correlation.
**PASS requires** perm-p < 0.0125 **AND** Δ ≥ 0.
Secondary, descriptive, **not** a fifth inference: legal_medinan LOO recall, currently
**8/20**.
*Justification of direction:* if modality is a genuinely new axis the added features must
buy accuracy; a nearest-centroid classifier is *hurt* by noise dimensions, so Δ ≥ 0 is a
real hurdle, not a formality.

### I4 — THE CONFOUND, DEMONSTRATED
Statistic: **Δ_F = F(D_resid) − F(J_resid)** — the split instrument's separating power
minus the naive raw-jussive instrument's.
Null: register-label shuffle, recomputing **both** F's on the permuted labels.
**PASS requires** perm-p < 0.0125 **AND** Δ_F > 0.
Locked descriptive prediction, reported either way: `argmax` of the `J_resid` centroid
is **NOT** `legal_medinan`.
*Justification of direction:* 71.2% of raw `MOOD:JUS` is negation and conditional syntax.
If the split is doing real work, stripping that must raise separating power. If Δ_F ≤ 0
the split was pointless and I must say so.

---

## 6. Nulls, seeds, permutations

- **Null A (primary).** Register-label shuffle preserving class sizes 31/20/40.
  seed **20260509**, **10,000** permutations. p = (#{stat_perm ≥ stat_obs} + 1) / (n_perm + 1).
- **Null B (MW-3, alternative model).** Label shuffle **stratified within surah-length
  tertiles** — tertiles of `n_verses` over the 91 surahs, cut at the 33.3rd and 66.7th
  percentiles, computed once and fixed. This controls length non-parametrically *in
  addition to* the OLS residualisation of §3.5. Same statistics, same seed.
- **MW-5 replication.** Every statistic re-run at seed **20260519**.
- **MW-6 instrument controls.** Fail-fast at runtime; see §8.
- **MW-7 post-hoc cap.** Anything not in the k=4 family is descriptive only, ceiling
  α = 0.05 single-test, and labelled as such in the finding.

---

## 7. Rules-tuples (≥2 required; three declared)

**T1 — PRIMARY.**
`(QAC-v0.4 pipe-atom exact matching, orthographic-word-token denominator,
basmala-counted-only-in-Q1 as QAC encodes it, D = IMPV + D_pro_la + D_lam_amr + IMPN,
E = CERT + EMPH{l:EMPH+ , +n:EMPH} + FUT{POS:FUT , sa+} + ACC∧LEM:<in~,
OLS residualisation on [log n_verses, mean words/verse], Ḥafṣ-Kūfan, Mashriqī)`

**T2 — SENSITIVITY-A (tagging ambiguity).** QAC's split of prohibitive *lā* between
`POS:PRO` and `POS:NEG` is not consistent — e.g. Q 2:102:34 `laA takofuro` is tagged
`POS:NEG` though it is plainly prohibitive. T2 moves all **110** `X_neg_la` jussives into
D (D total 518), and adds `LEM:>an~` (362) to E4 (E total 3,863).

**T3 — SENSITIVITY-B (denominator).** Density per **verse** rather than per word-token.

**Fragility rule, locked:** if T1 passes an inference and **both** T2 and T3 fail it, the
verdict for that inference is downgraded to **RULES-TUPLE-FRAGILE**, never CONFIRMED.

---

## 8. Frozen inputs and fail-fast controls

SHA-256, verified at runtime; any mismatch is `SystemExit`.

| file | SHA-256 |
|:--|:--|
| `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| `findings/phase-b-hypotheses/csv/h-new-2530.json` | `5ca17050c20b15734ad9a734e7bad7b938b616c924ec53dfcd24814a1473b68c` |
| `findings/phase-b-hypotheses/csv/h-new-2500.json` | `a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25` |
| `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |

MW-6 assertions, all abort on failure:

1. Genre marginals == `{narrative:31, legal_medinan:20, eschatological_mufassal:40, liturgical_didactic:23}`.
2. The six-feature LOO reproduces **0.76923** and the published confusion matrix
   **exactly**, including legal recall **8/20**. *(Verified reproducible before locking.)*
3. Marker totals reproduce §2.2/§3.4: `MOOD:JUS` 1418 · `MOOD:SUBJ` 1330 · `POS:CERT` 414 ·
   `POS:PRO` 332 · `IMPV` 1876 · `POS:IMPN` 2 · `l:EMPH+` 1001 · `+n:EMPH` 243 ·
   `POS:FUT` 42 · `sa+` 119 · `POS:ACC∧LEM:<in~` 1682 · `POS:ACC∧LEM:>an~` 362.
4. Jussive split reproduces §3.3 exactly, summing to 1418.
5. Word-tokens 77,429 · verses 6,236 · surahs 114.
6. Substring-vs-atom exhibit reproduces 3,633 vs 332.

**Run immutability.** Results are written to
`findings/phase-b-hypotheses/runs/h-new-2640/<UTC timestamp>/` with `result.json` and
`manifest.json`. **No run directory may ever be deleted or overwritten, including an
uncommitted or superseded one.** If a manifest records a non-portable path, the remedy is
to re-run into an **additional** directory and **retain both**, recording why. This clause
has no exception; it is written in response to the self-reported breach at
`h-new-2540-form-v-valency.md` §8.1.

---

## 9. Failure conditions (locked)

- perm-p ≥ 0.0125 on a registered inference → that inference is **NULL**, reported with
  equal prominence.
- **Direction reversed** — D argmax ≠ legal_medinan, or E argmax ≠ eschatological, or
  Δ < 0, or Δ_F ≤ 0 — → **pre-commit violation**, published as **REVERSED/NULL** with full
  prominence. The hypothesis is not to be redefined to fit.
- Any MW-6 assertion failing → **abort**, no result reported.
- Overall verdict: **CONFIRMED** only if all four inferences pass *and* the tuple-fragility
  rule of §7 is clear. Otherwise **PARTIAL**, **RULES-TUPLE-FRAGILE**, or **NULL**.

---

## 10. Classical anchoring — and what is NOT available

The anchor is the **ṭalab / khabar** division in balāgha.

**Not on disk, therefore not cited.** al-Sakkākī, *Miftāḥ al-ʿulūm*, is listed in
`KNOWLEDGE-GRAPH.md` but the text is **not in the repository**. No passage from it is
quoted here or in the finding.

**On disk but not readable, therefore not cited.** al-Zarkashī, *al-Burhān fī ʿulūm
al-Qurʾān*, `data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf`
(29.5 MB, 1,568 pp) is an **image-only scan** — `pdfinfo` reports Producer *"Adobe Acrobat
7.05 Image Conversion Plug-in"*, and `pdftotext -layout` returns 1,568 page breaks and
**zero characters of text**. There is no text layer and no OCR on disk. **No passage is
cited from it.** Acquiring an OCR'd or OpenITI *Burhān* is logged as a data gap.

**Actually citable, verified by opening it.** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*,
English translation by A. J. W. Mol,
`data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`:

- **p. 127**, on Q 2:124, al-Suyūṭī reporting Ibn Abī al-Iṣbaʿ and then giving his own
  preferred analysis: the verse "combines **the message and the requisition**, the
  affirmation and the negation, the emphasis and the omission, good news and a warning,
  and the promise and the threat." *Message* = khabar, *requisition* = ṭalab. This is the
  division this test operationalizes, in al-Suyūṭī's own words as rendered by Mol.
- **p. 249**, on Q 7:31 — the verse "encompasses the basis of speech, including the
  interjection, the generalization, the specification, **the imperative**, the lawful, the
  unlawful, and **the communication**" — and on Q 28:7, citing Ibn al-ʿArabī, that it
  "contains two each of **the imperative, the prohibitive, the communicative, and the
  annunciative forms**." The four-way amr / nahy / khabar / ibhār taxonomy, which maps
  directly onto D (imperative + prohibitive) and E (communicative + annunciative).

*(The extracted text of this PDF carries interleaved host-site watermark fragments; the
quoted sentences are continuous and legible, and page numbers refer to PDF pages.)*

The classical tradition asserts the ṭalab/khabar division qualitatively. It does **not**
assert that the two halves are *unevenly distributed by register*. That distributional
claim is what is being tested, and it can fail.

---

## 11. Honest limits, stated in advance

1. **The genre proxy is coarse** — H-NEW-2500's surah-scale *dominant*-register surrogate.
   Q 2 is both legislative and narrative. Inherited from the parent; not fixable here.
2. **Surah-scale aggregation** — cross-finding-025's standing prescription is a
   pericope-scale re-test. Not run here.
3. **Modality ≠ marker.** The indices count *morphological exponents* of modality. A
   command can be issued by a nominal (*ʿalaykum anfusakum*), a khabar-form (*kutiba
   ʿalaykum*), or a rhetorical question; certainty can be asserted with no particle at
   all. The measurement is of overt marking, not of speech-act.
4. **The E index co-occurs with itself.** *la-qad* carries both `l:EMPH+` and `POS:CERT`
   and is counted twice. This is a marker-token count, not a clause count, and it is
   disclosed rather than corrected.
5. **QAC annotation-limited**, and QAC's PRO/NEG treatment of *lā* is inconsistent —
   which is exactly why T2 exists.
6. **Not Quran-specific.** No matched Classical-Arabic control corpus is registered. Any
   result is **QURAN-INTERNAL** and may reflect Classical Arabic register generally.
7. **I3 reuses H-NEW-2530's published vector**, so it inherits every limitation of that
   finding's six features, including the sparsity of two of them.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any register-split computation.
Bismillāhi al-Raḥmāni al-Raḥīm.*
