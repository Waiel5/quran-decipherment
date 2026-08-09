---
title: "Pre-registration — H-NEW-2990: a corpus-wide per-verse structural profile for all 6,236 verses"
author: Waiel Al-Shujaa
date: 2026-08-09
status: PRE-REGISTERED — locked before any column was computed over the corpus
kind: INSTRUMENT — infrastructure, not a hypothesis test. There is no verdict and nothing to confirm.
method_parents: [findings/UNIT-DRIFT-DEFECT.md, findings/PROXY-CLAIMS.md]
occasioned_by: findings/phase-b-hypotheses/OPEN-H-NEW-2980-reception-residual.md
script_path: findings/phase-b-hypotheses/scripts/h-new-2990.py
deliverable: findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv
seed_primary: 20260509
seed_replication: 20260519
---

# H-NEW-2990 — pre-registration

## 0. What this document locks, and what it deliberately does not

**This is an instrument, not a test.** It has no hypothesis, no direction, no null model and no
p-value. Registering it is therefore not the usual protection against a forking analysis; it is a
protection against a *different* failure, which is the one this repository has actually suffered:

> **an instrument whose columns silently encode verse length, published as if its columns
> encoded structure.**

`findings/UNIT-DRIFT-DEFECT.md` records five claims lost to that mechanism in one week. So what
this document locks is **the column set and the honesty requirements attached to each column,
fixed before any column was computed over the corpus** — because the temptation an instrument
faces is to quietly drop the columns that turn out to be embarrassing, and to describe the
survivors as if the set had always been that.

**Every column declared in §3 will appear in the deliverable, including any that turns out to be
length-dominated.** A column is never dropped for measuring badly. It is labelled.

### 0.1 Why the instrument is needed at all

`OPEN-H-NEW-2980-reception-residual.md` established, by scanning every `csv/*.json` artifact,
that **no per-verse structural score exists in this repository.** `h-new-590.json` (outlier
strength) and `h-new-840.json` (UAS) are per-SURAH; `h-new-92.json` covers a hand-picked target
set for one test. The question *"is this verse structurally unusual?"* is therefore one this
project cannot currently ask, and that blocks the reception-residual rosters and every other
verse-level residual analysis.

**The shortcut this design exists to refuse:** assigning each verse its surah's score. That
produces a number for every verse and measures surah membership. It is the unit-mismatch artefact
of exactly the class `UNIT-DRIFT-DEFECT.md` §3 Screen B catalogues, and it is not built here.

> **Locked constraint C0 — the verse-locality rule.** Every column in §3 is a function of
> **that verse's own segments and its own text**, together with corpus-wide constants
> (root frequencies, the rime-class census). **No column may take any value from the verse's
> surah, its neighbours, its juzʾ, or its position.** A column that could not be computed for a
> verse presented in isolation, given the corpus-wide constants, is out of scope by construction.

The one boundary case is stated so it cannot be argued later: **`rime_class_size` is a
corpus-wide constant looked up by the verse's own fāṣila**, exactly as `mean_log10_root_freq` is a
corpus-wide constant looked up by the verse's own roots. It is not inherited from the surah; two
verses in the same surah routinely carry different values. It is in scope.

### 0.2 What was looked at before locking — the garden-of-forking-paths log

Recorded so it cannot be discovered later (`feedback_specialist_judgment_overrides_team_lead_method`
discipline; the model is `prereg-h-new-2960` §0).

| looked at | why it is not peeking |
|:--|:--|
| QAC v0.4 totals: 128,219 segments, 6,236 verses, 49,968 root-bearing tokens, 1,642 distinct roots | instrument calibration — these are the denominators, and they are already published in `h-new-2320-hapax-census.md` |
| **395 roots occur exactly once**, reproduced from QAC and matching `hapaxes-full-list.csv` exactly | reuse-and-verify of a published artifact, per brief; the count is already public in H-NEW-2320 |
| the QAC `POS:` inventory and its 34 tag counts | determines which POS groups are large enough to be worth a column |
| that QAC marks derived stems `(II)`…`(XII)` and leaves Form I unmarked | determines whether `frac_derived_stems` is computable at all |
| `quran-text/quran-full-tashkeel.json` holds 6,236 verses with sequential ids | alignment check for the text-derived columns |
| the pausal rime instrument of H-NEW-2870 runs on this text and yields **115 distinct P2 classes**, with `readable` true for 99.6 % of fāṣilas; **R1 ≡ R2 under P2**, so the rime-definition fork of H-NEW-2870 REPAIR-3 does not exist here | instrument calibration — it removes a researcher degree of freedom rather than exercising one, and the class *sizes* are the census itself |
| **not looked at:** any per-verse value of any column; any correlation of any column with any other; any correlation of any column with length | — |

**The last row is the one that matters.** The length correlations in §4 are the numbers this
document exists to constrain, and none of them had been computed when it was written.

---

## 1. Sources, frozen

| path | role |
|:--|:--|
| `data/morphology/quranic-corpus-morphology-0.4.txt` | QAC v0.4 — the sole source of segmentation, `ROOT:`, `LEM:`, `POS:` and stem-form |
| `quran-text/quran-full-tashkeel.json` | the fully-vocalised text — sole source of the fāṣila and of `n_letters_rasm` |
| `findings/phase-b-hypotheses/hapaxes-full-list.csv` | the published hapax census (H-NEW-1540 / H-NEW-2320), **reused rather than re-derived**, and cross-checked against a fresh QAC derivation |

All three are SHA-256 hashed into the manifest. This pre-registration's own SHA-256 is embedded
as a literal in the script and verified at runtime; a mismatch aborts **before any run directory
is created**.

**Never raw substring matching on Arabic for lexical identity.** Roots and lemmas come from the
QAC `ROOT:` and `LEM:` fields only. The one place text is read directly is the fāṣila
phonemiser (§3.F), which reads *phonology*, not lexis, and is a verbatim port of an instrument
already validated in H-NEW-2870.

### 1.1 The hapax reuse, and how a disagreement will be handled

`hapaxes-full-list.csv` is the registered source for hapax membership. The script also derives
the singleton sets directly from QAC. **If the two disagree, the run does not silently prefer
one.** It writes both counts and the symmetric difference into the result, uses the
**published CSV** for the deliverable column, and the disagreement is reported in the finding as
a defect of one of the two artifacts. It is not repaired inside this run.

---

## 2. The unit, and the primary length variable

**Unit: the verse.** All 6,236 verses of the Ḥafṣ–Kūfan numbering, keyed `(surah, verse)`, with
`mushaf_index` running 1…6,236 in mushaf order. Every verse gets a row; no verse is dropped for
any reason. Columns that are undefined for a verse are written **empty**, never zero.

> **Locked: the primary length variable is `n_words`** — the QAC word count of the verse.

Chosen over character count because `UNIT-DRIFT-DEFECT.md` §3 identifies **log word count** as
the dominant size channel in this repository (ρ = −0.9342 with mushaf position, size-only
R² = 0.8377), and because word count is the denominator most of the rate columns actually use.

**A note on log.** Spearman ρ is invariant under any monotone transform, so
ρ(x, `n_words`) ≡ ρ(x, log `n_words`) exactly. The distinction between word count and log word
count, which is decisive for a fitted model, is **immaterial for every number reported by this
instrument.** It is stated here so no reader thinks a choice was made.

`n_letters_rasm` is reported as a **secondary** length variable for every column, because a
column can be flat in words and steep in characters.

---

## 3. The column set — locked

Thirty-one columns. **Every one is length-declared in the table itself**, using exactly three
kinds:

- **COUNT** — a raw count. Scales with the verse. *Expected to be length-dominated; that is not a
  defect, it is what the column is.*
- **RATE** — a ratio. **The denominator is named.** `UNIT-DRIFT-DEFECT.md` §5 applies in full:
  the divisor is part of the claim.
- **INVARIANT** — intended to be free of verse length: a mean, a per-token statistic, or a
  categorical label. **"Intended" is the operative word — §4 measures it and the measurement
  decides.** `UNIT-DRIFT-DEFECT.md` §5: *"Normalisation is not invariance."* `d_min` divided by
  unit length and was called length-invariant by construction; length alone explained 28.7 % of
  its variance.

### A — identity (3 columns, not measurements)

| column | kind | definition |
|:--|:--|:--|
| `surah` | — | 1…114 |
| `verse` | — | verse number within surah |
| `mushaf_index` | — | 1…6,236, mushaf order |

### B — length (6 columns, COUNT by declaration)

| column | kind | definition |
|:--|:--|:--|
| `n_words` | COUNT | max QAC word index in the verse. **The primary length variable.** |
| `n_segments` | COUNT | QAC segments in the verse (prefixes, stems, suffixes) |
| `n_letters_rasm` | COUNT | Arabic letters in the verse text after removing every non-letter codepoint (diacritics, pause marks, spaces). Superscript alef `U+0670` is a diacritic and is **removed**; it is not in the written skeleton. |
| `n_root_tokens` | COUNT | segments carrying a `ROOT:` field — the denominator of the root family |
| `n_lemma_tokens` | COUNT | segments carrying a `LEM:` field — the denominator of the lemma family |
| `n_pos_segments` | COUNT | segments carrying a `POS:` field — the denominator of the morphology family |

These six are **not** flagged as length-dominated in §4 even though they will be. They *are*
length. They are in the deliverable because every rate column's denominator must be visible to a
downstream user who wants to recompute or re-normalise, and because §4's correlations are only
interpretable against them.

### C — hapax content (4 columns)

Reuses the published census per brief.

| column | kind | denominator | definition |
|:--|:--|:--|:--|
| `n_hapax_root_tokens` | COUNT | — | tokens in the verse whose `ROOT:` occurs exactly once corpus-wide |
| `frac_hapax_root_tokens` | RATE | `n_root_tokens` | the same, as a share of the verse's root-bearing tokens |
| `n_hapax_lemma_tokens` | COUNT | — | tokens whose `LEM:` occurs exactly once corpus-wide |
| `frac_hapax_lemma_tokens` | RATE | `n_lemma_tokens` | the same, as a share of the verse's lemma-bearing tokens |

*A hapax root occurs once by definition, so for these columns token count and type count
coincide. Stated so nobody re-derives it.*

### D — root rarity (6 columns)

Let `f(r)` be the corpus frequency of root `r` over the 49,968 root-bearing tokens, and
`p(r) = f(r)/49,968`.

| column | kind | denominator | definition |
|:--|:--|:--|:--|
| `mean_log10_root_freq` | INVARIANT | — | mean of `log10 f(r)` over the verse's root-bearing tokens |
| `median_log10_root_freq` | INVARIANT | — | median of the same |
| `min_root_freq` | COUNT-LIKE | — | `f` of the rarest root in the verse. **Declared length-sensitive a priori by extreme-value logic**: a longer verse draws more roots and so has more chances at a rare one. Included precisely because that expectation is testable in §4. |
| `mean_root_surprisal_bits` | INVARIANT | — | mean of `−log2 p(r)` over the verse's root-bearing tokens |
| `sum_root_surprisal_bits` | COUNT | — | the **total** of `−log2 p(r)`. **Length-dominated by construction.** Included deliberately as the instrument's own calibration case: it and `mean_root_surprisal_bits` differ by exactly a division by `n_root_tokens`, so §4 measures what that division buys. |
| `frac_root_tokens_freq_le5` | RATE | `n_root_tokens` | share of root tokens whose root occurs ≤ 5 times corpus-wide |

### E — lexical repetition within the verse (3 columns)

| column | kind | denominator | definition |
|:--|:--|:--|:--|
| `n_root_types` | COUNT | — | distinct roots in the verse |
| `ttr_root` | RATE | `n_root_tokens` | type–token ratio. **Declared mechanically length-dependent a priori** — TTR falls with sample size for any non-degenerate distribution. Reported because it is the standard measure and a downstream user will look for it, and labelled so nobody mistakes it for a structural property. |
| `root_simpson_repeat` | INVARIANT | — | `Σ nᵢ(nᵢ−1) / (N(N−1))` over root counts `nᵢ`, `N = n_root_tokens` — the probability that two root tokens drawn without replacement from the verse share a root. Unbiased for the underlying repetition rate under an i.i.d. draw, and therefore the **length-honest** counterpart of `ttr_root`. **Empty when `n_root_tokens < 2`.** |

**E is the pair that makes the instrument's point.** `ttr_root` and `root_simpson_repeat` measure
the same phenomenon; one is a rate whose denominator is the length, the other is not. §4 reports
both correlations side by side.

### F — the fāṣila (3 columns)

The pausal-rime instrument of H-NEW-2870 (`scripts/h-new-2870.py` §§1–2), **ported verbatim** —
`normalize`, `phonemes`, `apply_convention`, `rime_parts`, `rime2_parts`, `final_word`,
`rime_of`, `readable_of`. No parameter is changed. Provenance is declared in the script header,
following that script's own idiom of declaring its port from `h-new-2690.py`.

**Convention locked: P2** — the fullest pausal realisation (final short vowel and tanwīn dropped,
tanwīn fatḥ → `ā`, tāʾ marbūṭa → hāʾ). Chosen because H-NEW-2870's finding is that the fāṣila is
organised at pausal phonology, and P2 is its fullest form. **Under P1/P2 the R1 and R2 rime
definitions coincide** (verified: identical on all 6,236 verses), so H-NEW-2870's REPAIR-3 fork
does not exist at this convention and no choice between them is being made.

| column | kind | denominator | definition |
|:--|:--|:--|:--|
| `rime_pausal` | INVARIANT (categorical) | — | the P2 pausal rime string of the verse's final word |
| `rime_class_size` | INVARIANT (corpus constant) | — | number of the 6,236 verses sharing this verse's `rime_pausal`. **A corpus-wide lookup keyed by the verse's own fāṣila** — see C0. |
| `fasila_readable` | INVARIANT (boolean) | — | H-NEW-2870's readability criterion: whether the citation rime can be read off the text at all (false when no nucleus is written, or the apparent coda exceeds two consonants) |

### G — morphological composition (6 columns, all RATE)

POS groups are an **exhaustive four-way partition** of `POS:`-bearing segments, so the four shares
sum to 1 by construction:

- **NOMINAL** — `N`, `PN`, `ADJ`
- **VERBAL** — `V`, `IMPN`
- **PRONOMINAL** — `PRON`, `DEM`, `REL`
- **PARTICLE** — every other `POS:` tag (`P`, `NEG`, `ACC`, `T`, `COND`, `CONJ`, `SUB`, `LOC`,
  `RES`, `INTG`, `CERT`, `PRO`, `PREV`, `RET`, `EXP`, `INC`, `EXL`, `AMD`, `INT`, `FUT`, `ANS`,
  `EXH`, `SUR`, `AVR`, `INL`, `SUP`)

The partition is defined by the NOMINAL / VERBAL / PRONOMINAL membership lists and a
**catch-all**, so a QAC tag not anticipated here lands in PARTICLE rather than silently
disappearing.

| column | kind | denominator | definition |
|:--|:--|:--|:--|
| `share_nominal` | RATE | `n_pos_segments` | |
| `share_verbal` | RATE | `n_pos_segments` | |
| `share_pronominal` | RATE | `n_pos_segments` | |
| `share_particle` | RATE | `n_pos_segments` | |
| `segments_per_word` | RATE | `n_words` | morphological density — how much agglutination each word carries |
| `frac_derived_stems` | RATE | `n_root_tokens` | share of root-bearing stems carrying a derived-form marker `(II)`…`(XII)`. QAC leaves Form I unmarked, so absence of a marker is read as Form I. |

`share_definite` and `letters_per_word` were considered and are **not** included: the first is a
near-duplicate of `share_nominal`, the second is a ratio of two length columns and would carry no
information the two of them do not already carry. Recorded so their absence is a decision rather
than an oversight.

---

## 4. The length declaration — the requirement that makes this an instrument

> **Locked reporting requirement R1.** For **every** column in C, D, E, F and G, the finding
> reports the Spearman ρ against `n_words` **and** against `n_letters_rasm`, computed on the
> 6,236-verse population, on the rows where the column is defined.

> **Locked labelling rule R2.** A column with **|ρ| > 0.70** against `n_words` is labelled
> **LENGTH-DOMINATED** in the finding, in the companion declarations file, and in this
> instrument's every future citation. The threshold is fixed here, before any ρ was computed.

> **Locked rule R3 — no column is removed on the strength of its ρ.** Every column in §3 ships.
> A length-dominated column is a column that measures length, which is a fact a downstream user
> needs, not a column to hide.

`rime_pausal` is categorical and has no ρ. Its dispersion against length is reported instead as
**η² of `n_words` across rime classes** — the share of length variance explained by rime-class
membership — which answers the same question for a categorical column and is subject to the same
0.70-equivalent scrutiny in prose.

**A second, stricter diagnostic, locked here and reported for every column:** the
**partial Spearman ρ of each column against `mushaf_index`, controlling `n_words`.** Mushaf
position is the ordering this repository's claims most often run across, and a column's raw
correlation with it is exactly the quantity `UNIT-DRIFT-DEFECT.md` §3 was written about. Both the
raw and the partial are reported so a reader can see how much of each column's positional signal
is its length.

---

## 5. The composite — secondary, conditional, and gated

**A well-documented column set with no composite is a complete deliverable.** The columns are
what unblock downstream work. The composite is built because a ranking is what
`OPEN-H-NEW-2980` actually needs, and it is defined mechanically here so that no post-hoc
freedom exists.

**Members, with signs locked so that HIGHER = MORE UNUSUAL:**

| member | sign | rationale |
|:--|:--:|:--|
| `frac_hapax_root_tokens` | + | corpus-singleton content |
| `mean_root_surprisal_bits` | + | rarer roots per token |
| `frac_root_tokens_freq_le5` | + | rare-root share |
| `root_simpson_repeat` | − | more internal repetition = more ordinary |
| `log10(rime_class_size)` | − | a smaller rhyme class is a rarer fāṣila |

**Construction:** each member z-scored over the 6,236-verse population on the rows where it is
defined, sign-applied, then averaged. A row with fewer than **3** defined members gets an empty
composite.

> **Locked gate G1.** Any member measuring **|ρ| > 0.30** against `n_words` is **dropped from the
> composite**, and the drop is reported in the finding by name and by value. The gate is stricter
> than R2's 0.70 because a composite launders its members: a length signal that is visible in a
> named column becomes invisible once averaged into a score called "structural".

> **Locked gate G2.** If fewer than **3** members survive G1, **no composite is emitted at all**
> and the column is absent from the deliverable. A two-member average is not a composite, and
> shipping one to avoid an empty column would be the exact decoration §5 exists to prevent.

**`struct_z_composite_resid`** is also emitted: the composite's OLS residual on
`rank(n_words)`. Both columns' ρ against `n_words` are reported.

**Locked labelling rule R4.** The composite is described in the finding as SECONDARY, and the
finding states in terms that no column set may be replaced by it: **a downstream user who wants
one number should be told which columns produced it.**

---

## 6. Order of operations — locked, and it is not cosmetic

Six lanes were lost to connection failures on 2026-08-08, one of them after being told to
persist its deliverable first. The order below is part of the registration:

1. Verify the pre-registration SHA and the three input SHAs. **Abort before creating anything on
   a mismatch.**
2. Create the immutable run directory (`os.makedirs(..., exist_ok=False)`).
3. Compute the 31 columns and **write `verse-profile.csv` into the run directory immediately**,
   with `open(..., "x")`.
4. Copy it to `findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv`.
5. **Only then** compute the §4 correlations, the §5 composite, and the diagnostics.
6. Re-write the deliverable **once**, with the composite columns appended, to a **distinct**
   filename in the run directory (`verse-profile-final.csv`) — never overwriting step 3's file —
   and re-copy to `csv/`.
7. Write `column-declarations.csv`, `result.json`, `manifest.json`.

**Step 6 is why two files exist in the run directory.** `UNIT-DRIFT-DEFECT.md` §7: *a run script
must never overwrite a file inside its own run directory.* The pre-composite profile is written
once and never touched again; the composite version is a new path. **The published `csv/` copy is
not inside the run directory and may be replaced** — that is the point of separating them.

---

## 7. Run discipline

- Seed **20260509** (replication seed 20260519 declared and unused — nothing here is stochastic;
  the composite, the correlations and every column are deterministic functions of the inputs).
- Immutable run directory `findings/phase-b-hypotheses/runs/h-new-2990/<UTC-run-id>/`, created
  with `exist_ok=False`; every file opened with mode `'x'`. **Never deleted, never overwritten.**
- Any checkpoint goes **outside** the run directory. This run needs none; it is a single pass
  over 128,219 segments.
- Manifest paths are **repo-relative**.
- This pre-registration is **never edited after the run** — not to correct an error in it.
  Corrections go in the finding (`UNIT-DRIFT-DEFECT.md` §9). `scripts/verify-prereg-locks.sh`
  enforces the SHA lock.
- The finding is **not written to its final path before the run directory exists.**

## 8. What would make this instrument wrong

Stated in advance, because an instrument with no failure condition is not an instrument:

1. **If most INVARIANT columns land above |ρ| = 0.70**, the set is a length instrument wearing a
   structural label, and the finding must say so in its first paragraph rather than in a
   limitations section.
2. **If the hapax reuse disagrees with the fresh QAC derivation**, one of the two published
   artifacts is wrong and the deliverable inherits that error until it is settled.
3. **If `rime_class_size` correlates with length**, the fāṣila columns are partly a length
   measure — plausible, since long verses and short verses do not end alike — and the composite
   loses a member under G1.
4. **The instrument cannot certify that its columns are *interesting*.** It certifies that they
   are per-verse, that they are computed as declared, and that their relationship to length is
   measured and published. Nothing here shows that a verse scoring high on it is remarkable in
   any sense a reader of the Qurʾān would recognise. **That is a separate question and this
   document does not touch it.**

---

*Locked 2026-08-09 by Waiel Al-Shujaa, before any column was computed over the corpus.
An instrument is only worth what its denominators are. Bismillāhi al-Raḥmāni al-Raḥīm.*
