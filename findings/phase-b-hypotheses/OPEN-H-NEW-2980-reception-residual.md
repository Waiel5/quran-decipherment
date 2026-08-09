---
id: OPEN-H-NEW-2980
title: "CLOSED — the reception-weight residual rosters, run as H-NEW-3000 on 2026-08-09"
status: "CLOSED 2026-08-09 by findings/phase-b-hypotheses/h-new-3000-reception-residual-rosters.md. Both rosters delivered. Inferential arm: locked verdict SUPPORTED, NULL under exact tests."
date: 2026-08-08
updated: 2026-08-09
closed_by: findings/phase-b-hypotheses/h-new-3000-reception-residual-rosters.md
author: Waiel Al-Shujaa
instrument_ready: findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv
structural_instrument: findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv
---

> # ✅ CLOSED — 2026-08-09, by H-NEW-3000
>
> **`findings/phase-b-hypotheses/h-new-3000-reception-residual-rosters.md`. Both rosters exist:**
>
> - `csv/h-new-3000-roster-1-structurally-unusual-rarely-cited.csv`
> - `csv/h-new-3000-roster-2-heavily-cited-structurally-ordinary.csv`
>
> 30 rows each, with verse text, both scores, both ranks, the four composite members and two
> repetition flags. Structural score: **`struct_z_composite`** and its four named members;
> `sum_root_surprisal_bits` and `n_root_types` excluded as LENGTH-DOMINATED. Length control:
> stratification into ten `n_words` deciles plus partial Spearman.
>
> **The concentration census below is reproduced exactly** by that run from the locked
> instruments — 13.9 %, top-20 at 21.3 %, Q 112:1 at 102.
>
> **Inferential verdict: SUPPORTED under the locked rule, NULL under exact tests.** Three of six
> arms cleared Bonferroni α on parametric p-values; `n_hadith` is 86 % tied at zero and those
> p-values are **13–57× too liberal**. Under an exact permutation null with the same statistic
> only `−log10(rime_class_size)` survives, and it collapses when surah-mean-centred
> (ρ +0.0883 → +0.0284, p 0.0001 → 0.0193, 53 % of variance retained). **Nothing verse-level
> survives.** See H-NEW-3000 §6.
>
> **This file's ill-posedness ruling was vindicated in an unexpected form.** The unit mismatch it
> refused to improvise came back through a column that *is* verse-local by definition but carries
> **41 % of its variance between surahs**. **Verse-locality of a definition does not make a
> column's variance verse-level**, and η² by the coarser unit belongs beside ρ-against-length in
> any future instrument's declarations.
>
> **The text below is preserved unchanged as the record of what was known before the run.**

---

# OPEN — the reception-residual rosters have NOT been produced

**No result exists. Nothing may be cited from this test.** This file exists so the question is not
silently lost — the same mechanism that got `OPEN-H-NEW-2940` eventually run after three lanes
died on it, and which turned a soft extrapolated 3.63× into a measured 6.08×.

## The question

H-NEW-860.1 built `csv/h-new-860-1-reception-weights.csv` — a **formal per-verse reception weight
for all 6,236 verses**, derived from the full 50,884-record ḥadīth corpus. It replaced a hand-built
rubric that carried no discriminative information. **It has been used for exactly one correlation
and nothing else.**

Cross it against the structural instruments (`csv/h-new-590.json` outlier strength,
`csv/h-new-840.json` UAS) and produce two rosters, top 30 each with verse text and both ranks:

1. **Structurally extreme, rarely cited** — verses the instruments flag as extraordinary that the
   ḥadīth tradition passes over.
2. **Heavily cited, structurally ordinary** — verses the tradition dwells on that the instruments
   find unremarkable.

**The rosters are the deliverable and stand independent of any inference.**

## Constraints, already established and not to be rediscovered

- **A handful of verses dominate** — al-Fātiḥa, āyat al-kursī, the muʿawwidhāt. **Rank statistics
  only, no means.** Report the top-20 raw counts so the concentration is visible.
- **Unit drift applies** if reception is expressed as a rate: mushaf position correlates with log
  word count at ρ = −0.934. Prefer exact counts and ranks; residualise on verse length before
  calling anything a residual.
- **Expected verdict on the inferential arm: NULL.** H-NEW-2620 asked the same question of the
  tafsīr corpus and returned NULL on all six registered inferences once length was residualised.
  **A clean NULL alongside a good roster is a complete result.**

## Why it is unrun

One lane, failed on `API Error: Unable to connect to API (ENOTFOUND)` before producing any
artifact. **Four lanes were lost to connection errors on 2026-08-08** across this and the
H-NEW-2940 family. **The failures are infrastructure, not scope** — narrowing briefs between
attempts, as was done for 2940, was treating the wrong cause. The task as briefed is small and
should complete on a stable connection.

## To run it

Pre-register, SHA-lock, immutable run directory (mode `'x'`, `exist_ok=False`, checkpoints
outside), never delete a run directory, never edit the pre-registration after the run —
`scripts/verify-prereg-locks.sh` enforces the last.

---

## PARTIAL RESULT — the concentration census, computed 2026-08-08 (the rosters remain unrun)

Computed directly after a **fifth** consecutive lane died on a connection error. This is the half
that needed no structural join; **the two rosters still require one and are still open.**

**Reception is extraordinarily concentrated.** Of 5,371 eligible verses, only **749 (13.9%) carry
a single ḥadīth citation**. The top 20 verses carry **670 of 3,147 citations — 21.3% of all
reception**.

Top-20 raw counts, reported rather than averaged away:

| verse | citations | books | |
|:--|--:|--:|:--|
| **112:1** | **102** | 9 | *qul huwa Llāhu aḥad* |
| 87:1 | 63 | 8 | *sabbiḥ isma rabbika l-aʿlā* |
| 109:1 | 55 | 7 | *qul yā ayyuhā l-kāfirūn* |
| 64:1 | 54 | 8 | *yusabbiḥu li-Llāhi mā fī l-samāwāt* |
| 65:2 | 36 | 9 | the ṭalāq witness verse |
| 3:77 | 34 | 7 | those who sell God's covenant cheaply |
| 33:21 | 33 | 6 | *uswatun ḥasana* |
| 25:68 | 32 | 5 | the ʿibād al-Raḥmān prohibitions |
| 1:7 | 30 | 8 | *ṣirāṭa lladhīna anʿamta* |
| 2:158 | 27 | 8 | Ṣafā and Marwa |

Then 2:125, 113:1, 2:187, 2:196, 24:37, 4:95, 48:2, 88:1, 92:5, 114:1.

**Q 112:1 alone carries 102 citations across all nine books** — the single most received verse in
the canonical ḥadīth corpus by this measure, and by a factor of 1.6 over the next.

**This vindicates the rank-only constraint empirically rather than by assumption.** With 86% of
eligible verses at zero and a fifth of all reception in twenty verses, any mean-based statistic on
this distribution would be meaningless.

### Still open
The two rosters — *structurally extreme but rarely cited*, and *heavily cited but structurally
ordinary* — require joining to `csv/h-new-590.json` and `csv/h-new-840.json`, **both of which are
per-SURAH while reception is per-VERSE.** That mapping is a design decision, not a mechanical
join, and must be pre-registered rather than improvised. **Not attempted here.**

---

## THE ROSTERS ARE ILL-POSED AS BRIEFED — established 2026-08-09

**The two rosters cannot be computed with the instruments in this repository, and the reason is
structural rather than technical.**

A scan of every `csv/*.json` artifact for a **per-verse** structural score found none.
`h-new-590.json` (outlier strength) and `h-new-840.json` (UAS) are **per-SURAH**. The only file
carrying verse-level keys is `h-new-92.json`, whose `target_scores` cover a hand-picked target set
for one test — not a corpus-wide instrument.

**So "structurally extreme verses" is not a quantity this project can currently measure.** The
brief asked for a roster of them, and it cannot be built.

### Why improvising it would be wrong

The available shortcut is to assign each verse its **surah's** structural score. That would
produce a roster — and it would be measuring surah membership while labelled as measuring verses.
Every verse in a high-UAS surah would appear "structurally extreme" regardless of its own
properties, and the resulting residual against a genuinely per-verse reception count would be
**a unit-mismatch artefact of exactly the class `findings/UNIT-DRIFT-DEFECT.md` catalogues.**

**Recording the question as unanswerable is the correct outcome, not a failure to deliver.**

### What would make it answerable

A corpus-wide **per-verse** structural instrument, which does not exist here. Building one is a
separate registered piece of work, not a preliminary step to be improvised inside this test.

> #### ✅ BUILT — 2026-08-09, as H-NEW-2990
>
> **`findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv` — 6,236 rows × 33 columns**,
> every column a function of the verse's own segments and its own text, with each column's
> Spearman ρ against verse length published alongside it in
> `csv/h-new-2990-column-declarations.csv`. It joins to
> `csv/h-new-860-1-reception-weights.csv` on `(surah, verse)` at the **same unit**, so the
> unit mismatch that made these rosters ill-posed no longer applies.
>
> Finding: `findings/phase-b-hypotheses/h-new-2990-verse-profile.md`.
>
> **The rosters remain unrun**, and three conditions from that finding's §8 bind whoever runs
> them:
>
> 1. **Rank statistics only on the reception side** — unchanged by the new instrument.
> 2. **Name the column, or name the composite's four members.** *"Structurally extreme"* is
>    still not a quantity; `frac_hapax_root_tokens` and `mean_root_surprisal_bits` are.
> 3. **Stratify on `n_words`.** No column is length-free, and the cleanest one by ρ (+0.0105)
>    still has an **8.2× drift in its conditional mean** across the length deciles.
>
> Two columns are labelled **LENGTH-DOMINATED** and must not be used as structure:
> `sum_root_surprisal_bits` (ρ = +0.9411) and `n_root_types` (ρ = +0.9508).

### What this does NOT retract

The **concentration census above stands** — it needed no structural join. 13.9% of eligible verses
carry any citation; the top 20 carry 21.3% of all reception; Q 112:1 carries 102 across all nine
books.
