---
id: H-NEW-2990
title: "A corpus-wide per-verse structural profile for all 6,236 verses — the instrument this project lacked"
author: Waiel Al-Shujaa
date: 2026-08-09
kind: INSTRUMENT — infrastructure. No hypothesis, no null model, no verdict.
status: DELIVERED — 33 columns × 6,236 verses; 2 columns labelled LENGTH-DOMINATED; 1 composite member dropped by its locked gate
prereg: findings/phase-b-hypotheses/prereg-h-new-2990-verse-profile.md
prereg_sha256: 7a155da65a96eed918d2debf8f324df5b3e225d0ed8b4c8adde1ef70afe510ee
script: findings/phase-b-hypotheses/scripts/h-new-2990.py
posthoc_script: findings/phase-b-hypotheses/scripts/h-new-2990-posthoc.py
run: findings/phase-b-hypotheses/runs/h-new-2990/20260808T225517Z
deliverable: findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv
declarations: findings/phase-b-hypotheses/csv/h-new-2990-column-declarations.csv
method_parents: [findings/UNIT-DRIFT-DEFECT.md, findings/PROXY-CLAIMS.md]
occasioned_by: findings/phase-b-hypotheses/OPEN-H-NEW-2980-reception-residual.md
---

# H-NEW-2990 — a per-verse structural profile for all 6,236 verses

**There is no verdict here and nothing was confirmed.** This is an instrument. Its value is
entirely in being correct, honestly documented, reusable, and in **not silently encoding verse
length as if it were structure**.

## 1. What now exists

`findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv` — **6,236 rows × 33 columns**, one
row per verse, every column a function of that verse's own segments and its own text.

`findings/phase-b-hypotheses/csv/h-new-2990-column-declarations.csv` — the same columns with
their kind, their denominator, and **four correlations each**, so a downstream user can see what
a column is before using it.

### Why it did not exist before

`OPEN-H-NEW-2980` scanned every `csv/*.json` artifact in this repository and found **no per-verse
structural score anywhere**. `h-new-590.json` (outlier strength) and `h-new-840.json` (UAS) are
**per-SURAH**; `h-new-92.json` covers a hand-picked target set for one test. *"Is this verse
structurally unusual?"* was therefore a question this project could not ask.

**The shortcut this instrument exists to refuse** is assigning each verse its surah's score. That
produces a number for every verse and measures surah membership — the unit-mismatch artefact of
exactly the class `UNIT-DRIFT-DEFECT.md` §3 Screen B catalogues, and the reason the H-NEW-2980
rosters were ruled ill-posed rather than improvised. **It is not built here.** Every column
satisfies the pre-registered verse-locality rule (prereg §0.1 C0): computable for a verse
presented in isolation, given corpus-wide constants, and taking nothing from its surah, its
neighbours, its juzʾ or its position.

---

## 2. The length declaration — the whole point of the exercise

Every non-identity column, with its Spearman ρ against the primary length variable `n_words`.
**The 0.70 threshold and the labelling rule were fixed in the pre-registration before any ρ was
computed** (prereg §4 R2), and **no column was removed on the strength of its ρ** (R3).

*(Spearman is invariant under monotone transforms, so ρ against `n_words` and against
log `n_words` are the same number exactly. The word-count / log-word-count distinction that is
decisive for a fitted model is immaterial for every figure in this table.)*

| column | kind | denominator | ρ vs `n_words` | ρ vs `n_letters_rasm` | ρ vs `mushaf_index` | partial ρ vs mushaf, `n_words` held | n defined |
|:--|:--|:--|--:|--:|--:|--:|--:|
| **`n_words`** | COUNT | — | *1.0000* | 0.9846 | −0.5545 | — | 6236 |
| **`n_segments`** | COUNT | — | *0.9794* | 0.9891 | −0.5633 | −0.1202 | 6236 |
| **`n_letters_rasm`** | COUNT | — | *0.9846* | *1.0000* | −0.5660 | −0.1373 | 6236 |
| **`n_root_tokens`** | COUNT | — | *0.9638* | 0.9689 | −0.5378 | −0.0148 | 6236 |
| **`n_lemma_tokens`** | COUNT | — | *0.9947* | 0.9827 | −0.5523 | −0.0083 | 6236 |
| **`n_pos_segments`** | COUNT | — | *0.9995* | 0.9840 | −0.5548 | −0.0195 | 6236 |
| `n_hapax_root_tokens` | COUNT | — | +0.0213 | +0.0208 | +0.0303 | +0.0506 | 6236 |
| `frac_hapax_root_tokens` | RATE | `n_root_tokens` | **+0.0105** | +0.0099 | +0.0366 | +0.0512 | 6214 |
| `n_hapax_lemma_tokens` | COUNT | — | +0.0995 | +0.1043 | +0.0223 | +0.0935 | 6236 |
| `frac_hapax_lemma_tokens` | RATE | `n_lemma_tokens` | **+0.0010** | +0.0065 | +0.0816 | +0.0990 | 6216 |
| `mean_log10_root_freq` | INVARIANT | — | +0.2333 | +0.2177 | −0.2328 | −0.1273 | 6214 |
| `median_log10_root_freq` | INVARIANT | — | +0.2190 | +0.2064 | −0.2047 | −0.1021 | 6214 |
| `min_root_freq` | COUNT-LIKE | — | −0.2678 | −0.2751 | +0.0756 | −0.0920 | 6214 |
| `mean_root_surprisal_bits` | INVARIANT | — | −0.2333 | −0.2177 | +0.2328 | +0.1273 | 6214 |
| **`sum_root_surprisal_bits`** | COUNT | — | **+0.9411** ⚠ | +0.9500 | −0.5116 | +0.0454 | 6214 |
| `frac_root_tokens_freq_le5` | RATE | `n_root_tokens` | +0.0692 | +0.0702 | +0.0230 | +0.0744 | 6214 |
| **`n_root_types`** | COUNT | — | **+0.9508** ⚠ | +0.9568 | −0.5277 | −0.0016 | 6236 |
| `ttr_root` | RATE | `n_root_tokens` | −0.5170 | −0.5135 | +0.2835 | −0.0064 | 6214 |
| `root_simpson_repeat` | INVARIANT | — | +0.4436 | +0.4395 | −0.2480 | −0.0093 | 6095 |
| `rime_pausal` | CATEGORICAL | — | *η² = 0.1048* | *η² = 0.1009* | — | — | 6236 |
| `rime_class_size` | INVARIANT | — | +0.1427 | +0.1657 | **−0.2629** | **−0.2231** | 6236 |
| `fasila_readable` | BOOLEAN | — | +0.0979 | +0.0979 | −0.0027 | +0.0623 | 6236 |
| `share_nominal` | RATE | `n_pos_segments` | −0.1360 | −0.1025 | +0.1008 | +0.0308 | 6236 |
| `share_verbal` | RATE | `n_pos_segments` | +0.0562 | +0.0900 | −0.0773 | −0.0555 | 6236 |
| `share_pronominal` | RATE | `n_pos_segments` | +0.2606 | +0.2346 | −0.1628 | −0.0228 | 6236 |
| `share_particle` | RATE | `n_pos_segments` | +0.0963 | +0.0342 | −0.0278 | +0.0308 | 6236 |
| `segments_per_word` | RATE | `n_words` | −0.0893 | +0.0241 | −0.0459 | −0.1151 | 6236 |
| `frac_derived_stems` | RATE | `n_root_tokens` | +0.0577 | +0.0971 | −0.0831 | −0.0615 | 6214 |
| `struct_z_composite` *(secondary)* | DERIVED | — | −0.1824 | −0.1836 | +0.2742 | +0.2114 | 6214 |
| `struct_z_composite_resid` *(secondary)* | DERIVED | — | +0.2382 | +0.2281 | +0.0464 | +0.2221 | 6214 |

*Italic* = the six B columns, which **are** length and are exempt from the flag by prereg §3.B.
They ship because a downstream user recomputing or re-normalising any rate needs its denominator
visible.

### 2.1 The two LENGTH-DOMINATED columns

> **`sum_root_surprisal_bits` (ρ = +0.9411) and `n_root_types` (ρ = +0.9508) are
> LENGTH-DOMINATED. Do not use either as a measure of structure.**

**Both were declared as raw counts before the run and neither is a surprise.** They are in the
deliverable because R3 forbids removing a column for measuring badly, and because
`sum_root_surprisal_bits` was included **deliberately as the instrument's own calibration case**
(prereg §3.D): it differs from `mean_root_surprisal_bits` by exactly one division by
`n_root_tokens`, and the pair measures what that division buys —

| | ρ vs `n_words` |
|:--|--:|
| `sum_root_surprisal_bits` (total) | **+0.9411** |
| `mean_root_surprisal_bits` (per token) | **−0.2333** |

**One division moves a column from +0.94 to −0.23, and flips its sign.** That is the unit-drift
rule in a single row of a table, on this corpus, at this unit.

### 2.2 The mushaf-position column, which is the one worth reading twice

`n_words` correlates with `mushaf_index` at **ρ = −0.5545** at the verse level — the verse-level
analogue of the surah-level −0.9342 that `UNIT-DRIFT-DEFECT.md` §3 records for log word count.
The drift is real at this unit too, and weaker.

**After holding `n_words` fixed, one column keeps most of its positional signal:**

> **`rime_class_size`: raw ρ with mushaf position −0.2629, partial ρ −0.2231.** Verses later in
> the mushaf sit in **smaller** rhyme classes, and 85 % of that association survives length
> control.

Every other column's partial falls below |ρ| = 0.14. **This is the only per-verse column in the
instrument with substantial length-independent positional structure**, and it is offered as an
observation about the instrument, not as a claim: it is exactly the kind of thing this instrument
exists to let someone else test properly.

---

## 3. Three things a single ρ hides — and the second one is the most important number here

**Only 1 of 19 non-length columns is monotone in its length-decile means** (`fasila_readable`).
A Spearman ρ compresses a great deal of shape, and on this corpus the compression is not benign.
Post-hoc, `runs/h-new-2990-posthoc/20260808T225657Z`.

### 3.1 `frac_hapax_root_tokens` is length-clean by ρ and its conditional mean falls 8×

| `n_words` decile | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| words | 1–3 | 4 | 5 | 6–7 | 8–9 | 10–11 | 12–14 | 15–17 | 18–23 | 24–128 |
| mean `frac_hapax_root_tokens` | **0.0462** | 0.0245 | 0.0157 | 0.0125 | 0.0066 | 0.0059 | 0.0067 | 0.0047 | 0.0055 | **0.0056** |

**ρ = +0.0105. The decile means fall by a factor of 8.2.**

The mechanism is ties: **94.3 % of verses contain no hapax root at all**, so the rank correlation
is dominated by a vast block of tied zeros, while the mean is set by the minority that do — and
in a 3-word verse one hapax root is a third of the content, in a 30-word verse a thirtieth.

> **The column is not thereby disqualified — but ρ alone does not certify it.** Anyone using
> `frac_hapax_root_tokens` to compare short verses against long ones is comparing 0.046 against
> 0.006. Use it **within** a length stratum, or model the count with an exposure offset.

This generalises `UNIT-DRIFT-DEFECT.md` §5's *"normalisation is not invariance"* one step
further: **a near-zero ρ is not invariance either.** For a zero-inflated rate, the rank
correlation and the conditional mean can point in different directions, and the instrument's
headline table would have shown only the reassuring one.

### 3.2 `ttr_root` and `root_simpson_repeat` — the length-honest counterpart is not length-free

The pair was pre-registered to make exactly this comparison.

| | ρ vs `n_words` | decile-1 mean | decile-10 mean |
|:--|--:|--:|--:|
| `ttr_root` (types ÷ tokens) | **−0.5170** | 0.9700 | 0.8263 |
| `root_simpson_repeat` (per-pair, unbiased) | **+0.4436** | 0.0649 | 0.0230 |

**Both are length-entangled, and they disagree in sign.** `ttr_root` falls with length as declared
a priori. `root_simpson_repeat` **rises** in rank while its **mean falls** — the same tie
mechanism as §3.1, and sharper: `root_simpson_repeat` is exactly 0 for **80.4 %** of verses with
≤ 4 words and for only **5.3 %** of verses with ≥ 24 words, because a 3-word verse usually cannot
repeat a root at all. `ttr_root` is exactly 1.0 for **59.1 %** of verses.

> **The pre-registered expectation that `root_simpson_repeat` would be the length-honest
> counterpart of `ttr_root` is not borne out.** It is unbiased for the repetition rate *given a
> sample*, and at verse lengths of 2–4 root tokens the sample is too small for that to translate
> into length-independence. **Neither column should be used across length strata.** Recorded here
> rather than quietly softened, because it is a prediction this pre-registration made and missed.

### 3.3 The composite's residualisation makes it worse, and the residual column should not be used

`struct_z_composite_resid` is the OLS residual of the composite on `rank(n_words)`, locked in
prereg §5. It does exactly what OLS promises and **that turns out not to be what was wanted**:

| | value |
|:--|--:|
| Pearson(resid, rank `n_words`) — what the OLS optimises | **−8.6 × 10⁻⁹** |
| **Spearman(resid, `n_words`)** | **+0.2382** |
| Spearman(composite, `n_words`) — before correction | **−0.1824** |

The composite is heavily skewed (skewness **+3.63**, excess kurtosis **+21.1**). A linear-in-rank
subtraction is fitted to *means* that the short-verse right tail dominates — decile 1's composite
mean is +0.6403 against a median of +0.2143 — so the correction over-shoots the bulk. The
residual medians then climb monotonically across the upper half of the length range
(−0.34 → +0.11).

> **Use `struct_z_composite` (ρ = −0.182), not `struct_z_composite_resid` (ρ = +0.238).**
> The residual column ships because prereg R3 forbids deleting a column for measuring badly, and
> because *"the residualised version"* is precisely the column a future reader would otherwise
> assume was the safe one.

---

## 4. The composite — secondary, gated, and one member was dropped

**The columns are the deliverable. The composite is not a substitute for them, and a downstream
user who wants one number should be told which columns produced it.**

Members and signs were locked in prereg §5 before any ρ existed. **Gate G1 drops any member with
|ρ| > 0.30 against `n_words`:**

| member | sign | ρ vs `n_words` | G1 |
|:--|:--:|--:|:--|
| `frac_hapax_root_tokens` | + | +0.0105 | kept |
| `mean_root_surprisal_bits` | + | −0.2333 | kept |
| `frac_root_tokens_freq_le5` | + | +0.0692 | kept |
| `root_simpson_repeat` | − | **+0.4436** | **DROPPED** |
| `log10(rime_class_size)` | − | +0.1427 | kept |

Four of five survived, clearing G2's minimum of three, so `struct_z_composite` is emitted:
the equal-weight mean of the four sign-aligned z-scores, defined on **6,214** of 6,236 verses
(the 22 exceptions carry no root-bearing token — see §5.2).

**The gate is stricter than the 0.70 labelling threshold for a stated reason: a composite
launders its members.** A length signal visible in a named column becomes invisible once averaged
into a score called "structural". `root_simpson_repeat` at +0.44 would have been a labelled,
inspectable column inside a score with no label at all.

**`struct_z_composite` is not length-free** (ρ = −0.182) and must not be described as such.

---

## 5. Verification

### 5.1 The hapax census reproduces exactly, by three independent routes

Prereg §1.1 registered `hapaxes-full-list.csv` (H-NEW-1540 / H-NEW-2320) as the source and
required any disagreement with a fresh derivation to be reported rather than repaired.
**There was none:**

| | published census | fresh QAC derivation | symmetric difference |
|:--|--:|--:|--:|
| root hapaxes | 395 | 395 | **0** |
| lemma hapaxes | 1,994 | 1,994 | **0** |

A **third** route — counting the published census's own `surah`/`verse` location fields per verse,
rather than looking up membership through QAC's `ROOT:`/`LEM:` fields — reproduces every verse's
two hapax counts with **0 mismatches across all 6,236 verses**.

### 5.2 Corpus census

| quantity | value |
|:--|--:|
| verses | 6,236 |
| QAC segments | 128,219 |
| root-bearing tokens | 49,968 |
| distinct roots | 1,642 |
| lemma-bearing tokens | 74,608 |
| distinct lemmas | 4,832 |
| `POS:`-bearing segments | 77,915 |
| pausal (P2) rime classes | **115** |
| fāṣilas readable by H-NEW-2870's criterion | 6,216 of 6,236 (**99.68 %**) |

**22 verses carry no root-bearing token** and their root-family columns are written **empty, never
zero**: the twenty muqaṭṭaʿāt openings (2:1, 3:1, 7:1, 19:1, 20:1, 26:1, 28:1, 29:1, 30:1, 31:1,
32:1, 36:1, 40:1, 41:1, 42:1, 42:2, 43:1, 44:1, 45:1, 46:1) plus **Q 70:15** (*kallā innahā laẓā*)
and **Q 85:18** (*firʿawna wa-Thamūd*), which consist of particles and proper names. A further 119
verses have exactly one root token, so `root_simpson_repeat` is undefined on 141 rows.

### 5.3 The fāṣila instrument, and a fork that does not exist

Ported verbatim from `scripts/h-new-2870.py` §§1–2, no parameter changed. Convention locked at
**P2** — the fullest pausal realisation — following H-NEW-2870's finding that this corpus's
verse-endings are organised at pausal phonology.

H-NEW-2870's REPAIR-3 introduced two rime definitions (R1 and R2) because the tanwīn nūn is
wrongly read as the *rawī* at citation form. **Under P1/P2 the convention has already removed the
tanwīn, so R1 and R2 coincide.** The pre-registration asserted this and the run verified it on the
data: **identical on all 6,236 verses.** No choice between them was made because none existed.

### 5.4 A worked example — the instrument read by inspection

Four verses a reader already knows, so the instrument can be checked rather than trusted:

| column | Q 108:1 | Q 112:1 | Q 1:1 | Q 2:255 |
|:--|--:|--:|--:|--:|
| `n_words` | 3 | 4 | 4 | 50 |
| `n_root_tokens` | 2 | 3 | 4 | 28 |
| `n_hapax_root_tokens` | 0 | 0 | 0 | **2** |
| `mean_root_surprisal_bits` | **10.013** | 6.063 | 6.393 | 8.642 |
| `ttr_root` | 1.000 | 1.000 | 0.750 | 0.821 |
| `rime_pausal` | `aر` | `aد` | `Iم` | `Iم` |
| `rime_class_size` | 44 | **15** | 551 | 551 |
| `share_nominal` | 0.333 | 0.500 | **1.000** | 0.360 |
| `segments_per_word` | 2.333 | 1.000 | 1.750 | 1.580 |
| `struct_z_composite` | +0.511 | −0.030 | −0.531 | +0.335 |

Three checks a reader can make without running anything:

- **Q 2:255's two hapax roots are `wsn` and `Awd`** — *sina* in *lā taʾkhudhuhu **sina**tun wa-lā
  nawm*, and *ya**ʾūdu**hu* in *wa-lā **yaʾūdu**hu ḥifẓuhumā*. Both are corpus singletons, and
  both are among the most-remarked lexical singletons in the Qurʾān. The instrument found them
  from the QAC `ROOT:` field with no list of any kind.
- **Q 1:1 is 100 % nominal** — *bi-smi Llāhi l-Raḥmāni l-Raḥīm* contains no verb, and
  `share_nominal` = 1.000 says so.
- **Q 112:1 sits in a rhyme class of 15** while Q 1:1 and Q 2:255 share the 551-verse *-īm* class.

**And one that should be read as a caution rather than a result:** Q 1:1 scores **−0.531** on the
composite, near the ordinary end. *Bi-smi Llāhi l-Raḥmāni l-Raḥīm* is built from three of the most
frequent roots in the corpus, and by the columns this instrument measures that is what
*structurally ordinary* means. **A verse's importance is not what is being measured here** — see
§7.

---

## 6. Run discipline

- Pre-registration SHA-256 `7a155da65a96eed918d2debf8f324df5b3e225d0ed8b4c8adde1ef70afe510ee`,
  embedded as a literal in the script and verified at runtime; three frozen inputs likewise.
  A mismatch aborts **before** any run directory is created. `scripts/verify-prereg-locks.sh`
  covers this lock.
- Immutable run directory `runs/h-new-2990/20260808T225517Z/`, `exist_ok=False`, every file
  opened mode `'x'`. **Nothing inside it was overwritten.**
- **The instrument was written to disk before any correlation, composite or diagnostic was
  computed** (prereg §6 steps 3–4). Six lanes were lost to connection failures on 2026-08-08, one
  after being told to persist first; the order of work inside a fragile lane is part of the
  registration, not a preference.
- The composite is appended to a **distinct** filename (`verse-profile-final.csv`); the
  pre-composite file is written once and never touched again. `UNIT-DRIFT-DEFECT.md` §7: *a run
  script must never overwrite a file inside its own run directory.* The published `csv/` copies
  live outside the run directory and are replaceable — that is the point of separating them.
- Deterministic: nothing here is stochastic. Seed 20260509 declared; the replication seed is
  declared and unused.
- The pre-registration has not been edited since the run and will not be. Everything in this
  section that corrects or disappoints it — §3.2 and §3.3 — is recorded **here**, in the finding.

---

## 7. Honest limits

1. **This instrument cannot certify that its columns are interesting.** It certifies that they are
   per-verse, that they are computed as declared, and that their relationship to length is
   measured and published. **Nothing here shows that a verse scoring high on it is remarkable in
   any sense a reader of the Qurʾān would recognise.** Q 1:1 scores below average. That is a fact
   about the column set, not about Q 1:1, and the gap between the two is the instrument's main
   limitation.
2. **No column is length-free.** The best are near-zero in ρ, and §3.1 shows that near-zero ρ is
   compatible with an 8× drift in the conditional mean. **Every downstream use should stratify on
   length or carry length as a competing predictor.** This instrument makes that possible; it does
   not make it unnecessary.
3. **The column set is one defensible choice among many.** `share_definite` and `letters_per_word`
   were considered and excluded (prereg §3.G) — the first as a near-duplicate of `share_nominal`,
   the second as a ratio of two length columns. Syntactic-dependency features from QAC's syntax
   layer, phonotactic features, and any semantic feature are absent entirely. **A wider set would
   be a different instrument, not a better version of this one**, and would need its own
   registration.
4. **`rime_class_size` is a corpus-wide constant.** It changes if the corpus changes. So do the
   root frequencies and the hapax sets. Every column of this instrument is defined against
   **this** corpus and is not portable to a baseline text without recomputing the constants — a
   point that matters for any future cross-corpus control, where a matched partition must
   recompute its own frequencies rather than inherit these.
5. **`frac_derived_stems` reads QAC's Roman-numeral form markers and treats their absence as
   Form I.** That is QAC's own encoding convention and not an inference, but it means the column
   inherits any QAC annotation error in the form field silently.

---

## 8. What this unblocks

`OPEN-H-NEW-2980`'s two reception-residual rosters — *structurally extreme but rarely cited*, and
*heavily cited but structurally ordinary* — were ruled **ill-posed** because no per-verse
structural instrument existed. **One exists now**, and it joins to
`csv/h-new-860-1-reception-weights.csv` on `(surah, verse)` at the same unit, with no unit
mismatch.

Three conditions any such use must meet, and they follow from §§2–3 rather than from caution:

1. **Rank statistics only on the reception side.** 13.9 % of eligible verses carry any ḥadīth
   citation and the top 20 carry 21.3 % of all reception (`OPEN-H-NEW-2980`). That constraint is
   unchanged by this instrument.
2. **Name the column, or name the composite's four members.** *"Structurally extreme"* is not a
   quantity. `frac_hapax_root_tokens` is, and so is `mean_root_surprisal_bits`.
3. **Stratify on `n_words`, or carry it as a competing predictor.** §3.1 is the reason: the
   column that looks cleanest by ρ has an 8× conditional-mean drift across the length range.

**The rosters are still not run and nothing in this finding should be read as running them.**
This is the instrument they needed and no more than that.

---

*Built 2026-08-09 by Waiel Al-Shujaa. An instrument is only worth what its denominators are.
Bismillāhi al-Raḥmāni al-Raḥīm.*
