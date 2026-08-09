---
id: PREREG-H-NEW-3000
title: "Pre-registration — the reception-residual rosters, per-verse structure against formal ḥadīth reception"
author: Waiel Al-Shujaa
date: 2026-08-09
status: LOCKED BEFORE ANY OUTCOME-PREDICTOR ASSOCIATION WAS COMPUTED
parent_open_question: findings/phase-b-hypotheses/OPEN-H-NEW-2980-reception-residual.md
structural_instrument: findings/phase-b-hypotheses/h-new-2990-verse-profile.md
reception_instrument: findings/phase-b-hypotheses/h-new-860-1-fadail-formal-count.md
method_parents: [findings/UNIT-DRIFT-DEFECT.md, findings/PROXY-CLAIMS.md]
analogue: findings/phase-b-hypotheses/h-new-2620-tafsir-contested.md
seed: 20260509
seed_replication: 20260519
bonferroni_k: 6
alpha_bonferroni: 0.00833333
expected_verdict: NULL
---

# Pre-registration — H-NEW-3000

**The two rosters are the deliverable and stand independent of any inference.** They are
written to disk before any correlation, permutation or verdict is computed (§7 order of
operations). The inferential arm is secondary, and its expected outcome is **NULL**: the
tafsīr analogue H-NEW-2620 returned NULL on all six registered inferences once length was
residualised, and nothing here is expected to differ.

---

## §0 Pre-lock inspection log

Everything inspected before this file was hashed. **No outcome–predictor association was
computed or viewed.** The quantities below are predictor-side or purely descriptive.

1. **The two files join at the same unit.** `h-new-2990-verse-profile.csv` (6,236 rows) and
   `h-new-860-1-reception-weights.csv` (6,236 rows) share all 6,236 `(surah, verse)` keys
   exactly. No unit mismatch; this is the condition that made these rosters ill-posed until
   2026-08-09.
2. **The two files carry different word counts, and the difference is real.** The profile's
   `n_words` is computed from `quran-full-tashkeel.json`; the reception file's from
   `quran-no-tashkeel.json`. They disagree on **364 of 6,236 verses**, by at most 2 words,
   at **ρ = 0.99959**. The cause is orthographic: the imlāʾī text splits some units the
   ʿuthmānī text writes joined. §2.3 locks which one is the length control and registers the
   other as a sensitivity arm. *(This is a predictor–predictor measurement. No reception or
   structural outcome entered it.)*
3. **The reception file's eligibility field is inherited, not recomputed.** 5,371 verses
   `eligible = 1`; 865 ineligible — 600 under four words, 265 with no distinctive span.
4. **The composite is defined on every eligible verse.** All 5,371 eligible verses carry a
   non-empty `struct_z_composite`. The 22 root-less verses of H-NEW-2990 §5.2 are all
   already ineligible on the reception side, so the intersection loses nothing.
5. **Decile structure of the analysis set** under the locked length variable (profile
   `n_words`, range 3–128, median 12), value-based decile cut: bin sizes
   814 / 330 / 613 / 590 / 586 / 492 / 420 / 482 / 510 / 534, word ranges
   3–5 / 6 / 7–8 / 9–10 / 11–12 / 13–14 / 15–16 / 17–19 / 20–25 / 26–128. Ten non-empty bins.
6. **Repetition census, corpus-wide:** 272 of 6,236 verses have a normalised no-tashkeel text
   that occurs more than once. Registered in §5.3 as a roster annotation, never a filter.
7. **The column declarations were read before any column was chosen.** §2.1 records the
   choice and its justification against that file.

---

## §1 Frozen inputs

Verified by SHA-256 at runtime, embedded as literals in
`findings/phase-b-hypotheses/scripts/h-new-3000.py`. **A mismatch aborts before any run
directory is created.**

| path | SHA-256 |
|:--|:--|
| `findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv` | `f4ca4377fe0fe4b7bf2b1cf34f8afa8632f61427e8bcd1d393d1afe8795d90de` |
| `findings/phase-b-hypotheses/csv/h-new-2990-column-declarations.csv` | `61f7b6d12490214abb8857a5e76b532968ee64ae6c33018e29bc23769897a3a2` |
| `findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv` | `f6bf5f744025d65d47d6b3f4d2ba7425531e56c048e5c75baa25f85f0f0b26c0` |
| `quran-text/quran-full-tashkeel.json` | `382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715` |
| `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |

This pre-registration's own SHA-256 is embedded in the script as `EXPECTED_PREREG_SHA` and
checked first of all. **This file is never edited after the run, for any reason, including to
correct an error in it** (`findings/UNIT-DRIFT-DEFECT.md` §9). Corrections go in the finding.

---

## §2 The structural measure — named before computing

### 2.1 Which columns, and why

`csv/h-new-2990-column-declarations.csv` was read before this choice. It flags exactly **two**
columns as `length_dominated = True`:

> **`sum_root_surprisal_bits` (ρ = +0.9411) and `n_root_types` (ρ = +0.9508) are excluded.**
> Both are raw sums that scale with length by construction. Neither is used here as structure,
> in any arm, primary or sensitivity.

**Also excluded, and for stated reasons:**

- The six columns flagged `IS_LENGTH` — `n_words`, `n_segments`, `n_letters_rasm`,
  `n_root_tokens`, `n_lemma_tokens`, `n_pos_segments`. They **are** length. One of them is the
  length control (§2.3); none is a structural measure.
- **`struct_z_composite_resid`.** H-NEW-2990 §3.3 measured that the OLS-on-rank residualisation
  makes the column *worse* — Spearman against `n_words` moves from −0.1824 (composite) to
  **+0.2382** (residual), because a linear-in-rank subtraction fitted to means over-corrects a
  distribution with skewness +3.63. Its own finding says: *"Use `struct_z_composite`, not
  `struct_z_composite_resid`."* This pre-registration follows that instruction. **Length is
  controlled here by stratification and by partial correlation, not by that column.**

### 2.2 The locked primary structural score

> **PRIMARY: `struct_z_composite`**, the equal-weight mean of four sign-aligned z-scores.
> **Its four members are named here, as H-NEW-2990 §8 condition 2 requires** — *"structurally
> extreme" is not a quantity*:
>
> | member | sign | denominator | ρ vs `n_words` |
> |:--|:--:|:--|--:|
> | `frac_hapax_root_tokens` | + | `n_root_tokens` | +0.0105 |
> | `mean_root_surprisal_bits` | + | *(per-token mean — invariant, no denominator column)* | −0.2333 |
> | `frac_root_tokens_freq_le5` | + | `n_root_tokens` | +0.0692 |
> | `log10(rime_class_size)` | − | *(corpus constant keyed by the verse's own fāṣila)* | +0.1427 |
>
> A fifth member, `root_simpson_repeat`, was **dropped by H-NEW-2990's own locked gate G1**
> at ρ = +0.4436 and is not present in the composite. It is not reinstated here.
>
> **`struct_z_composite` is not length-free** (ρ = −0.1824 with `n_words`) and is never
> described as such in this work. That is why every arm below carries a length control.

**Direction convention, locked:** higher `struct_z_composite` = **structurally more unusual**
(rarer roots, more hapaxes, smaller rhyme class). Lower = **structurally more ordinary**.

### 2.3 The length control

> **LOCKED: `n_words` as published in `h-new-2990-verse-profile.csv`.**

Justification, fixed before any outcome was computed: that file's own declarations name it
`PRIMARY LENGTH VARIABLE`, and **every ρ published in the instrument's length declaration is
measured against it.** Using the instrument's own declared length variable is the only choice
that keeps this test's length control commensurable with the instrument's published table.

**The alternative is registered as a sensitivity arm, not left undisclosed:** the reception
file's `n_words` (from the imlāʾī text) is re-run through the identical pipeline as arm S1.
The two disagree on 364 verses at ρ = 0.99959 (§0.2), so the arms are expected to agree; the
arm exists so that the choice is a measured degree of freedom rather than an invisible one.

### 2.4 Every rate's denominator, declared

Per `findings/UNIT-DRIFT-DEFECT.md` §5.1. `frac_hapax_root_tokens` and
`frac_root_tokens_freq_le5` divide by **`n_root_tokens`** (the verse's own root-bearing token
count). `mean_root_surprisal_bits` is a per-root-token mean of −log₂ of corpus root frequency.
`rime_class_size` is a corpus-wide count of verses sharing the verse's P2 pausal rime — it has
no denominator and is not a rate. **The reception count `n_hadith` is never divided by
anything**: it is used raw and ranked, per §3.2.

---

## §3 The reception measure

### 3.1 The locked column

> **PRIMARY: `n_hadith`** — H-NEW-860.1's locked N = 5 verse-level distinctive quotation count
> over the nine canonical books (40,943 of 50,884 records). Range 0–102.

Sensitivities, **non-confirmatory**, reported whatever they show: `n_hadith_all17` (all
seventeen books) and `n_books` (0–9 distinct books, a breadth rather than a volume measure).

### 3.2 Rank statistics only — a measured constraint, not a precaution

`OPEN-H-NEW-2980` measured it: of 5,371 eligible verses only **749 (13.9 %) carry any
citation**, the **top 20 carry 21.3 % of all reception**, Gini over eligible verses = 0.938,
and **Q 112:1 alone carries 102**.

> **No mean of `n_hadith` is computed anywhere in this work, in any arm.** Every statistic is
> a rank statistic. Every percentile is a mid-rank percentile. The raw top-20 counts are
> reported so the concentration stays visible.

### 3.3 Ineligible verses are excluded, never zeroed

The 865 verses with `eligible = 0` **cannot receive a verse-level count** — 600 are under four
words, 265 have no span distinctive to them. **A zero there would be an instrument floor
misread as neglect.** They are dropped from the analysis set and from both rosters, and their
exclusion is reported.

**Analysis set: the 5,371 verses with `eligible = 1`.** All carry a defined
`struct_z_composite` (§0.4).

---

## §4 Length stratification

Deciles of the locked length variable (§2.3), computed **over the analysis set only**, by
value-based quantile cut: boundaries are the 10th…90th percentiles of `n_words`, deduplicated,
and a verse is assigned by its own `n_words` value. **Verses of equal length are never split
across bins** — that is the point of stratifying, and a rank-position cut would break it.

Bins and sizes are printed by the runner and published in the finding. From §0.5 there are ten
non-empty bins of 330–814 verses each.

**Both bin widths are pre-registered and both are reported**, per `UNIT-DRIFT-DEFECT.md` §6.1
requirement 2:

- **k = 10 deciles — PRIMARY.**
- k = 5 quintiles — reported alongside.

**k = 10 is primary here, and the reason is registered.** §6.1's caveat — that a stratified
permutation is not decisive for a *fitted model containing the stratifying variable* — does
not apply: **every statistic in this work is a correlation, which holds no size column**, and
for a correlation §6.1 states stratified permutation *"is decisive and remains so"*. The finer
bin holds length more nearly fixed and is therefore the stricter test. **Choosing the stricter
of two pre-registered settings tightens the test and requires no ratification.** If the two
disagree, both are reported and the k = 10 result is the one the verdict rests on.

---

## §5 The rosters — the deliverable, locked in full

### 5.1 The mismatch score

For each verse *v* in the analysis set, within its length decile *d*:

- **S(v)** = mid-rank percentile of `struct_z_composite` among **all** n_d verses of decile
  *d*: `S = (midrank − 0.5) / n_d`, range (0, 1). Higher = structurally more unusual **for a
  verse of its length**.
- **R(v)** = **0 exactly** if `n_hadith = 0`; otherwise the mid-rank percentile of `n_hadith`
  among the **m_d cited verses** of decile *d*: `R = (midrank_cited − 0.5) / m_d`,
  range (0, 1). Higher = more heavily cited **for a verse of its length**.
- **M(v) = S(v) − R(v)**, range (−1, 1).

> **Why R collapses the zero block to exactly 0, fixed before computing.** 86 % of eligible
> verses carry no citation. A plain mid-rank percentile over the whole decile assigns every
> one of them ≈ 0.43 and a *singly*-cited verse ≈ 0.87 — so a verse with one ḥadīth would
> outrank Q 112:1's 102 by a hair's breadth of structural difference, and the "heavily cited"
> roster would fill with once-cited verses. **The concentration measured in §3.2 is a property
> of the object, and the instrument encodes it rather than being distorted by it.** Under the
> locked definition, *rarely cited* means **not cited**, and *heavily cited* is graded only
> among verses the tradition cites at all.

### 5.2 The two rosters

> **ROSTER 1 — structurally unusual, rarely cited.** The **top 30 by M descending**.
>
> **ROSTER 2 — heavily cited, structurally ordinary.** The **top 30 by M ascending**.

One ordering, two tails. Ties are broken by `mushaf_index` ascending — deterministic, and
independent of both scores.

### 5.3 Roster columns, locked

`surah`, `verse`, `reference` (`Q s:v`), `surah_name`, **`verse_text`** (full tashkeel),
`n_words`, `length_decile`, `decile_word_range`, `struct_z_composite`, **`struct_rank`**
(1 = most structurally unusual of the 5,371), `S_within_decile`, `n_hadith`,
**`reception_rank`** (1 = most cited of the 5,371, mid-rank for ties), `R_within_decile`,
`M`, `n_books`, `n_hadith_all17`, `driver_span`, the four composite members
(`frac_hapax_root_tokens`, `mean_root_surprisal_bits`, `frac_root_tokens_freq_le5`,
`rime_class_size`), and two annotations:

- **`text_repeats`** — the verse's normalised no-tashkeel text (NFC, whitespace collapsed)
  occurs more than once in the corpus;
- **`is_later_occurrence`** — it is not the first occurrence in mushaf order.

**These two are annotations, never filters.** H-NEW-2620 §7.1 found its own "ignored" roster
was **~73 % repetition artefact** and discovered it only post-hoc. Publishing the flag with
the roster is that lesson applied in advance. **No verse is removed on the strength of it**,
and the fraction of each roster carrying it is reported.

### 5.4 The rosters are written before any inference

Locked as an ordering of operations, not a preference — see §7.

---

## §6 The inferential arm — six registered inferences

**Family:** RECEPTION-2026-08-09-A. **k = 6. Bonferroni α = 0.05 / 6 = 0.00833333.**

**Direction locked POSITIVE for all six**, before computing: the substantive hypothesis — the
one the classical *iʿjāz* tradition would predict and the one worth testing — is that the
ḥadīth tradition cites structurally unusual verses **more**. A result in the opposite
direction is reported but claims nothing unless it clears the same corrected α.

| | outcome | structural variable | statistic |
|:--|:--|:--|:--|
| **I1** | `n_hadith` | `struct_z_composite` | partial Spearman, controlling `n_words` |
| **I2** | `n_hadith` | `struct_z_composite` | Spearman under the **stratified permutation null**, k = 10 (k = 5 reported) |
| **I3** | `n_hadith` | `frac_hapax_root_tokens` | partial Spearman, controlling `n_words` |
| **I4** | `n_hadith` | `mean_root_surprisal_bits` | partial Spearman, controlling `n_words` |
| **I5** | `n_hadith` | `frac_root_tokens_freq_le5` | partial Spearman, controlling `n_words` |
| **I6** | `n_hadith` | `−log10(rime_class_size)` | partial Spearman, controlling `n_words` |

I3–I6 are the composite's four members, **sign-aligned as in §2.2**, tested individually. This
discharges H-NEW-2990 §8 condition 2 in its strongest form: the composite is named *and* every
member is named and separately tested, so nothing is laundered by averaging.

**Partial Spearman** is the first-order partial correlation computed on mid-ranks:
`ρ(x,y|z) = (ρxy − ρxz·ρyz) / sqrt((1−ρxz²)(1−ρyz²))`. Its p-value is the two-sided t-test on
n − 3 degrees of freedom; the one-sided p in each direction is reported. **The runner
self-tests this identity against a direct OLS-residual computation on the ranks and aborts on
disagreement beyond 1e-9.**

**Permutation null (I2):** `n_hadith` is permuted **within** length bins, 10,000 permutations,
seed 20260509, replicated at seed 20260519. Statistic: plain Spearman
ρ(`struct_z_composite`, `n_hadith`) over the analysis set. One-sided
p = (1 + #{ρ_perm ≥ ρ_obs}) / (1 + 10000) in the locked positive direction, and the mirror in
the reverse. **The plain Spearman is the correct statistic under this null** — the null itself
removes the length channel, which is the H-NEW-2770 design.

### 6.1 The verdict rule, fixed here

```
PASS_i      <- rho_i > 0  and  p_one_sided_positive_i < 0.00833333
REVERSE_i   <- rho_i < 0  and  p_one_sided_negative_i < 0.00833333
NULL_i      <- neither
VERDICT     <- "SUPPORTED"  if any PASS_i
               "REVERSED"   if no PASS_i and any REVERSE_i
               "NULL"       if all six are NULL_i
```

**The runner prints this logic with the observed numbers substituted, before declaring
anything.** The declaration in the finding is diffed against that printout.

### 6.2 Expected verdict, stated in advance

> **NULL.** H-NEW-2620 asked this of the tafsīr corpus and returned NULL on all six registered
> inferences once length was residualised, with the bare positive association turning out to be
> entirely a length-and-position confound. H-NEW-860.1 found no relationship in either
> direction between ḥadīth reception and structure at surah level once size was held fixed.
> **A clean NULL alongside good rosters is a complete result, and no arm here will be extended,
> re-cut or re-stratified in search of significance.** Sensitivities are declared in §6.3 and
> are the only variants that will be run.

### 6.3 Sensitivities — non-confirmatory, declared in advance, reported whatever they show

| arm | change |
|:--|:--|
| **S1** | length control = the reception file's `n_words` instead of the profile's (§2.3) |
| **S2** | reception = `n_hadith_all17` instead of `n_hadith` |
| **S3** | reception = `n_books` instead of `n_hadith` |
| **S4** | analysis set restricted to first occurrences (`is_later_occurrence = false`) |
| **S5** | analysis set restricted to cited verses only (`n_hadith ≥ 1`, n ≈ 749) |
| **S6** | stratified permutation at k = 5 (§4) |

**No sensitivity can produce a PASS.** They diagnose; they do not decide.

---

## §7 Order of operations — registered, not cosmetic

Six lanes were lost to connection errors on 2026-08-08, one after being told to persist its
deliverable first. **Inside a fragile lane the order of work is part of the registration.**

1. Verify this file's SHA-256 and all five frozen input SHA-256s. **Abort before creating any
   run directory on any mismatch.**
2. Numerical self-tests (§6 partial-correlation identity; mid-rank percentile behaviour).
3. Build the analysis set, the deciles, S, R, M.
4. Create the immutable run directory: `os.makedirs(..., exist_ok=False)`, every file opened
   mode `'x'`.
5. **WRITE BOTH ROSTERS TO DISK AND PUBLISH THEM TO `csv/`.** Nothing inferential has been
   computed at this point.
6. Only then: the six inferences, the permutation nulls, the sensitivities.
7. Write `result.json` **once**, at completion. Write `manifest.json` **once**.

**No file inside the run directory is ever overwritten** (`UNIT-DRIFT-DEFECT.md` §7). If a
checkpoint is needed it goes outside the run directory. **A run directory is never deleted**,
including one left empty by a failed attempt. Manifest paths are repo-relative.

---

## §8 Declared limits, before seeing any result

1. **`struct_z_composite` cannot certify that a verse is *interesting*.** H-NEW-2990 §7.1 is
   explicit, and its worked example is decisive: **Q 1:1 scores −0.531, near the ordinary
   end**, because the basmala is built from three of the corpus's most frequent roots. A verse
   this instrument calls *ordinary* may be central to the tradition for reasons the instrument
   does not measure. **Roster 2 is therefore not a list of verses the tradition was wrong to
   dwell on**, and will not be described as one.
2. **No column is length-free, and near-zero ρ is not invariance.** H-NEW-2990 §3.1:
   `frac_hapax_root_tokens` has ρ = +0.0105 and an **8.2× drift in its conditional mean**
   across the length deciles, because 94.3 % of verses contain no hapax root at all and the
   rank correlation is dominated by tied zeros. Stratification (§4) is the response; it
   reduces the problem and does not abolish it.
3. **Power is low by construction.** 86 % of the analysis set is tied at `n_hadith = 0`. A
   Spearman over an 86 %-tied variable has little power, and **a NULL here is weak evidence of
   absence, not strong evidence** (`findings/ABSENCE-CLAIMS.md`).
4. **Reception is verbatim quotation and nothing else.** H-NEW-860.1 §10.1: this instrument
   does not measure allusion, paraphrase, thematic commentary, or *asbāb al-nuzūl*
   attribution, and §9.3 of that finding shows the gap reaches an order of magnitude for
   Q 19. **`n_hadith` is not "how much the tradition cares".**
5. **`n_hadith` inherits the N = 5 span choice**, which H-NEW-860.1 §6.2 discloses as a real
   researcher degree of freedom — at N = 4 that finding would have read REVERSES rather than
   UNDETERMINED. The alternative spans are not on disk per verse and are **not** re-derived
   here; this test inherits the locked column as published.
6. **Chain grade is not modelled.** A *mawḍūʿ* chain counts as a *ṣaḥīḥ* one.
7. **Musnad Aḥmad is incomplete upstream** (chapters 8–30 absent from the source scrape), so
   Aḥmad is under-weighted throughout.
8. **The rosters are descriptive.** No p-value attaches to any roster entry, and none will be
   computed for one.

---

*Locked 2026-08-09 by Waiel Al-Shujaa, before any association between structure and reception
was computed. The rosters are the deliverable; the verdict is expected to be NULL, and a NULL
is a complete result. Bismillāhi al-Raḥmāni al-Raḥīm.*
