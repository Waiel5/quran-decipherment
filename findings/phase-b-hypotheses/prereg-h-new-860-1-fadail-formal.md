---
id: H-NEW-860.1
title: "Pre-registration — replacing H-NEW-860's hand-built fadāʾil rubric with a formal per-verse ḥadīth count over the full on-disk corpus"
date: 2026-08-08
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE any correlation with UAS, with H-NEW-590 outlier strength, or with the published rubric was computed
family: RECEPTION-2026-08-08
repairs: H-NEW-860 (its §7.1 absence claim is FALSE per findings/ABSENCE-CLAIMS.md §6 FALSE #3)
parent_data: H-NEW-840 (UAS), H-NEW-590 (outlier spectrum), H-NEW-2900 (the corpus census)
seed: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 18
alpha_bonferroni: 0.00277778
---

# Pre-registration — H-NEW-860.1

**Nothing here may be amended after the SHA-256 is embedded in
`findings/phase-b-hypotheses/scripts/h-new-860-1.py`.** The matching procedure is locked in
§3, the counting rules in §4, the statistics and their drift declarations in §5, and the
decision rules in §6. The runner's verdict logic will be diffed against §6 and printed
before any verdict is declared.

---

## 1. Why this test exists

H-NEW-860 §7.1 states:

> *"A formal corpus-wide hadith-mention count requires a hadith-database (Maktaba Shamela,
> sunnah.com index) which is not present on disk in this project."*

**That absence claim is FALSE.** The on-disk corpus at
`data/literature/hadith/ahmedbaset-json/` **is** a sunnah.com scrape: 50,884 records across
17 books, with per-book and per-chapter indices, Arabic + English + narrator fields,
committed 2026-04-28. Verified here by direct enumeration (§8.1). It is catalogued as
FALSE #3 in `findings/ABSENCE-CLAIMS.md` §6.

H-NEW-860 substituted a **hand-built 0–10 "rough rubric"** over 36 surahs and published a
correlation with the Unified Architectural Significance Score on top of it. This replaces
the eyeballed proxy with a count.

**A result that weakens or reverses H-NEW-860 is a success of this test.** The rubric was a
stopgap resting on a false absence claim; establishing that it misled is the point.

### 1.1 What this test can and cannot conclude — stated before it is run

H-NEW-860's correlation has **two** sides and this repairs only one of them.

The other side, UAS, carries a standing correction reproduced in H-NEW-860's own header:
H-NEW-840's frontmatter reads `status: SYNTHESIS`; it is a composite ranking with **no null
hypothesis and no test statistic**, and two of its three inputs are themselves corrected
(H-NEW-2680, H-NEW-2720).

**Therefore, and irrespective of what this run returns: no claim about the corpus may rest
on the correlation, in either direction.** What is being tested is strictly whether
**H-NEW-860's stated result reproduces when its own weakest input is replaced**. That is a
claim about H-NEW-860, not about the Qurʾān, and the finding will say so in those words.

The reusable output is the instrument, not the inference (§7).

---

## 2. What is already published, and therefore not pre-registrable

H-NEW-860's numbers are on the record. They are **compared against**, not predicted:

| quantity | published |
|:--|--:|
| Spearman ρ(rubric, UAS_rank), N = 36 — **the headline** | **+0.330**, p = 0.050 |
| Pearson r(rubric, UAS_rank), N = 36 | +0.297, p = 0.079 |
| Pearson r(rubric, UAS_value), N = 36 | −0.135, p = 0.431 |
| Pearson r(rubric, UAS_value), N = 114, unlisted-as-zero | +0.210, p = 0.025 |
| Pearson r(rubric, UAS_rank), N = 114 | −0.065, p = 0.495 |
| Spearman ρ(rubric, UAS_value), N = 114 | +0.161, p = 0.086 |

Sign convention, carried verbatim from H-NEW-860: **UAS_rank 1 = most architecturally
distinct**, so a **positive** ρ with rank means *more ḥadīth attention → worse architectural
rank* = **ANTI-alignment**. This is counter-intuitive and is the single most common way to
misread the finding; the runner prints the convention beside every coefficient.

**No correlation of any formal count with UAS, with UAS rank, with H-NEW-590 outlier
strength, or with the published rubric has been computed.** §8 lists everything that was
inspected before locking.

---

## 3. The matching procedure — LOCKED

### 3.1 Normalisation

Applied identically to Qurʾān and ḥadīth text.

1. Unicode NFC.
2. **Delete** U+0610–U+061A, U+064B–U+065F, U+0670, U+06D6–U+06ED, U+0640 (Arabic marks,
   ḥarakāt, superscript alif, Qurʾānic annotation signs, tatweel).
3. **Map** U+0622, U+0623, U+0625, U+0671 → U+0627 (alif); U+0649 → U+064A; U+0629 → U+0647;
   U+0624 → U+0648; U+0626 → U+064A.
4. **Delete** every character outside U+0621–U+064A and space.
5. Collapse whitespace; split on space.

> **Implementation constraint, locked because it silently destroyed a probe run.** Arabic
> literals inside a regex character-class range are **reordered by bidirectional text
> handling when the source file is written**, which rewrote `[U+0610-U+061A U+064B-U+065F …]`
> into a range covering U+0621–U+064A and stripped every Arabic letter in the corpus. The
> run script builds all character classes **from integer codepoints**, and asserts at runtime
> that `norm()` of a fixed Qurʾānic string returns a fixed expected string.

### 3.2 Sources

- Qurʾān: `quran-text/quran-no-tashkeel.json` — 114 surahs, **6,236 verses**, verified.
  The imlāʾī (not Uthmānī-rasm) orthography is chosen deliberately: it is the orthography
  the ḥadīth corpus is written in.
- Ḥadīth: `data/literature/hadith/ahmedbaset-json/db/by_book/`. **The nine books
  (`the_9_books/`, 40,943 records) are the primary universe** (§4.1).
- Only the `arabic` field of each record is searched. Chapter titles (`chapters`) are **not**
  searched — al-Bukhārī's *Kitāb al-Tafsīr* bāb headings quote verses, and including them
  would count an editor's index as reception.

### 3.3 The link rule

A ḥadīth record **R** is linked to verse **v** iff R's normalised text contains, at word
boundaries, a contiguous word-span **S** such that:

- **(a)** S is a contiguous span of v of length `n = min(N, |v|)` words;
- **(b)** `|v| ≥ 4` words — verses shorter than 4 words are **INELIGIBLE**, not zero;
- **(c)** S is **distinctive**, defined by the level of the count:
  - **verse level** — S occurs, as a contiguous span, in **exactly one verse** of the Qurʾān;
  - **surah level** — every verse in which S occurs belongs to **one surah**.

**N = 5 is the primary.** N = 4 and N = 6 are pre-registered sensitivity arms.

**Ownership is computed across every span length in play, from every verse.** A 4-word span
drawn from a 4-word verse is checked against its occurrence *inside longer verses* too. This
matters: without it `بسم الله الرحمن الرحيم` appears verse-unique to Q 1:1 because Q 27:30's
spans are longer, and Q 1:1 acquires 49 spurious "citations" that are the invocation formula.
Under the locked rule Q 1:1 and Q 1:2 are **non-distinctive** and receive no verse-level
count. This is correct: no instrument reading text alone can tell a ḥadīth's basmala from a
citation of Q 1:1.

### 3.4 Why distinctiveness is in the rule, and what it costs

Measured before locking (§8.3). Without it, the highest-count "verses" are artefacts of
shared formulae: one ḥadīth saying `يا ايها الذين امنوا لا …` links to **twenty** verses at
once, and at N = 4 the top verse is Q 21:87 with 302 records driven by `ان لا اله الا` — the
shahāda fragment, 247 of them.

**The cost is declared: a verse that is entirely formulaic gets no verse-level count.** Such
verses are reported as `eligible = false` with their **ambiguous** count in a separate
column, never as zero. Q 55's `فباي الاء ربكما تكذبان` refrain is the type case — 31
occurrences within one surah, so it is non-distinctive at verse level and **distinctive at
surah level**, which is exactly why the two levels are computed separately.

### 3.5 Partial quotations

A span of `n` words out of a longer verse **counts as a link**. Reception of a verse
includes reception of its famous clause. Two things are published so this is auditable:
the **driving span** (the single span contributing most records) and the **maximum matched
span length**, per verse, in the deliverable table.

### 3.6 The naming instrument (co-primary at surah level only)

The quotation instrument detects *quotation*. H-NEW-860's rubric scored *fadāʾil* — praise
of a surah, which typically **names** it without quoting it. Counting only quotation would
be a rigged comparison. So a second surah-level instrument is locked:

- Arabic: the normalised token `سوره` followed by optional `ال` and the surah's normalised
  name from the corpus file, at word boundaries.
- **No alias table.** `فاتحه الكتاب`, `الزهراوين`, `المعوذتين`, `براءه` and the rest are
  **not** counted. An alias list is a researcher degree of freedom with no principled
  stopping point, and every alias added is a choice made while looking at the surahs whose
  counts it would raise. The cost — that Q 1, Q 2, Q 9, Q 113 and Q 114 are undercounted by
  the naming channel — is declared here in advance and repeated in the finding.
- The union arm **U = Q ∪ N** (records linked by either) is the third instrument.

---

## 4. Counting rules — LOCKED

### 4.1 The multi-book rule: **PER RECORD, in the nine books**

A ḥadīth appearing in both al-Bukhārī and Muslim counts **twice** — once per book-instance.

**Why, stated before seeing any count.** Textual de-duplication across books requires a
matn-similarity threshold, and a threshold is a free parameter chosen while looking at the
records it would merge. Per-record counting has none. Independent attestation in two
collections is also, on the tradition's own terms, *more* reception, not the same reception.

Two companion columns make the alternative readings recoverable without a threshold:

- `n_books` — the number of **distinct books** (0–9) citing the verse. Bounded, insensitive
  to any one collection's verbosity, and parameter-free.
- per-book counts, all nine, published in the table.

**Universe = the nine books, 40,943 records.** The remaining eight (Riyāḍ al-Ṣāliḥīn,
Mishkāt al-Maṣābīḥ, Bulūgh al-Marām, al-Adab al-Mufrad, Shamāʾil, and the three Forties;
9,941 records) are **anthologies drawn from the nine** and would multiply-count exactly the
most famous material. A tertiary all-17 count is reported and is **not verdict-bearing**.

**Declared data gap:** Musnad Aḥmad is present at 1,374 records; chapters 8–30 are absent
from the upstream scrape (source README). Aḥmad is therefore under-weighted throughout. The
per-book table makes the size of this visible.

### 4.2 Aggregation to surah level

`surah_count(s)` = the number of **distinct records** linked to **at least one verse of s**
under the **surah-level** distinctiveness rule. A record citing three verses of al-Baqara
counts **once** for al-Baqara. This is the quantity that replaces the rubric score.

---

## 5. Statistics, and the drift each one must declare

`findings/UNIT-DRIFT-DEFECT.md` applies in full. Per §5, every channel is **ranked on the
data before locking**, and the measurements are in §8.4.

### 5.1 Counts, not rates — and why

**No reception density is computed anywhere in this test.** Not per verse, not per word, not
per 100 verses. Mushaf position correlates with log word count at ρ = −0.934
(UNIT-DRIFT §3), so any reception *rate* compared across mushaf order measures size. The
headline quantities are **exact counts** and every inferential statistic is **rank-based**.

### 5.2 Declared drift of the instrument itself

Measured pre-lock (§8.4) and reported beside every coefficient:

| quantity | ρ |
|:--|--:|
| verse-level count × verse word count | **+0.180** |
| surah-level count × surah **word** count | **+0.485** ← the channel to control |
| surah-level count × surah **verse** count | +0.328 |
| naming count × surah word count | **+0.660** |

**Word count is the stronger surah channel and is therefore the one controlled**, in
agreement with UNIT-DRIFT §3's mushaf block. **The naming instrument is the more
length-confounded of the two**, which is declared here so it cannot later be presented as
the cleaner channel.

### 5.3 No means

Per the task's own constraint and §7's concentration result, **every reported inferential
statistic is rank-based (Spearman ρ, Kendall τ)**. Pearson r is reported **only** for
like-for-like comparison against H-NEW-860's published Pearson figures, and is never
verdict-bearing.

### 5.4 The nulls

1. **Partial Spearman** controlling `log(surah word count)`.
2. **Stratified permutation** — permute UAS within bins of `log(surah word count)`,
   10,000 draws, seed 20260509. Per UNIT-DRIFT §6.1, **two bin widths are declared**:
   **k = 5 (quintiles) primary** and **k = 10 (deciles) stricter**. Both are reported; if
   they disagree the finer bin is the honest one and the disagreement is itself the result.
   §6.1's caveat that stratified permutation is *not* decisive for a fitted model does not
   apply here — the statistic is a correlation, which holds no size column.
3. **The cheapest diagnostic first** (STATE §0): before any p-value, the runner reports
   whether the null ever draws a comparison set resembling the observed one on the nuisance
   channel.

---

## 6. Decision rules — LOCKED

### 6.1 The primary arm

**Exactly one arm carries the verdict**: quotation instrument **Q**, span **N = 5**,
**Cell A** = Spearman ρ(formal surah count, UAS_rank) over the **same 36 surahs H-NEW-860
listed**, at **α = 0.05** — the published bar, so the comparison is like-for-like.

All other arms are sensitivity and are reported at Bonferroni α = 0.05/18 = 0.00277778
(k = 18 = 3 instruments × 3 span settings × 2 cells).

### 6.2 The four verdicts — mutually exclusive and exhaustive

Let ρ_pub = **+0.330** and ρ_f = the primary arm's coefficient.

| verdict | condition |
|:--|:--|
| **REVERSES** | sign(ρ_f) ≠ sign(ρ_pub) **and** p_f < 0.05 |
| **SURVIVES** | sign(ρ_f) = sign(ρ_pub) **and** p_f < 0.05 **and** ρ_f ≥ 0.5 × ρ_pub (≥ +0.165) |
| **WEAKENS** | sign(ρ_f) = sign(ρ_pub) **and** (p_f ≥ 0.05 **or** ρ_f < +0.165) |
| **UNDETERMINED** | sign(ρ_f) ≠ sign(ρ_pub) **and** p_f ≥ 0.05 |

**A SURVIVES verdict is additionally void if the primary arm fails either null in §5.4** —
in which case the verdict is recorded as **WEAKENS (confounded by length)**. A WEAKENS or
REVERSES verdict needs no null: it does not claim anything.

### 6.3 Cell B

Full corpus, N = 114, non-cited surahs at **zero** (they are genuinely zero at surah level —
unlike ineligible verses). Reported against H-NEW-860's published full-corpus figures.
**Not verdict-bearing.**

### 6.4 Rubric-vs-formal agreement — the number with independent value

Reported unconditionally, with no threshold and no verdict attached:

- Spearman ρ and Kendall τ (rubric score, formal count) over the 36 listed surahs;
- the same over all 114 with unlisted-as-zero;
- **top-10 set overlap** and **top-20 set overlap**, rubric vs formal;
- the **ten largest rank disagreements**, named, in both directions.

This calibrates every other eyeballed proxy in the repository and is the deliverable that
does not depend on any verdict.

---

## 7. Deliverables, which stand whatever the inference returns

1. **`findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv`** — all **6,236**
   verses: sura, aya, word count, eligibility and its reason, verse-level distinctive count,
   ambiguous count, `n_books`, the nine per-book counts, all-17 count, driving span, maximum
   matched span length, surah-level count.
2. **The top-20 concentration table**, explicitly, so a reader sees the concentration rather
   than having it averaged away — with the share of all links held by the top 20 and top 100
   verses, and a Gini coefficient over eligible verses.
3. **The residual roster** — structurally extreme but rarely cited, and heavily cited but
   structurally ordinary, by rank residual against **both** H-NEW-590 `delta_pct` and UAS.
   **Descriptive only.** H-NEW-2620's tafsīr analogue returned NULL and no significance is
   expected or will be claimed; no p-value will be attached to the roster.

---

## 8. What was inspected before locking — the garden-of-forking-paths log

Everything below was measured **before** this document was SHA-256'd. **No quantity below
involves UAS, UAS rank, H-NEW-590 outlier strength, or the published rubric.**

### 8.1 The corpus census
17 books enumerated, 50,884 records total; `the_9_books` = 40,943; anthologies = 9,941.
Record schema `{id, idInBook, chapterId, bookId, arabic, english{narrator,text}}` confirmed.
Musnad Aḥmad at 1,374 records against its stated missing chapters 8–30.

### 8.2 Validation sets, and the parameters chosen on them
Two **explicit** citation channels exist in the corpus and were used to calibrate the
matcher. Neither is an outcome variable.

- **Val A** — 986 explicit `(sura:aya)` references in the English field, over 779 records.
- **Val B** — 2,504 brace-delimited `{…}` Arabic quotations over 1,785 records, of which
  2,186 resolve to at least one verse by direct containment.

Recall of the locked instrument, measured on Val A:

| arm | verse-level | surah-level |
|:--|--:|--:|
| N = 4 | 0.827 | 0.858 |
| **N = 5 (locked primary)** | **0.761** | **0.807** |
| N = 6 | 0.661 | 0.711 |

**N = 5 was chosen against N = 4 on false-positive evidence, not on recall**, and the
evidence is §3.4's driving-span audit. The shortfall to 1.000 is not all error: it includes
allusion without verbatim quotation, and sunnah.com verse-numbering that differs from this
corpus's by one or two āyāt.

### 8.3 The false-positive control
The Qurʾān was matched against **pre-Islamic dīwāns** (`data/baseline-corpora/raw/diwan-*`,
75,971 normalised words, cut to 954 pseudo-records of 80 words). Poetry that **predates the
Qurʾān** cannot cite it, so every link is a formulaic false positive or a transmission
artefact.

| arm | ḥadīth links / Mword | poetry links / Mword | ratio |
|:--|--:|--:|--:|
| N = 4 | 1,674 | 158.0 | 10.6× |
| **N = 5** | **1,175** | **118.5** | **9.9×** |
| N = 6 | 1,003 | 92.1 | 10.9× |

118.5 per Mword is an **upper bound** on the false-positive rate — several poetry hits are a
scribal basmala in the manuscript, which is a real presence of the string, not a matcher
error.

### 8.4 Drift channels, ranked on the data before locking
The four ρ values in §5.2. Ranking before locking is UNIT-DRIFT §5's explicit requirement,
and skipping it is the step that has failed most often in this repository.

### 8.5 Instrument scale, measured pre-lock
At the locked setting: **2,371 of 40,943** records link to at least one verse; 749 verses
carry a verse-level count; 600 verses are ineligible for being under 4 words; 265 further
verses are non-distinctive; ρ(quotation, naming) at surah level = **+0.570**.

### 8.6 One count seen pre-lock, declared
**Q 112:1 `قل هو الله احد` returned 102 records — the highest verse-level count** — during
the character-threshold calibration, where it sits at 11 normalised characters and was the
reason the character floor was dropped in favour of a pure word-count rule. It is named here
because it will be the top row of §7's concentration table and must not appear to be a
discovery of the run.

---

## 9. Run hygiene

- Immutable run directory `runs/h-new-860-1/<UTC>/`, created with
  `os.makedirs(..., exist_ok=False)`; all files opened mode `'x'`.
- **The script never overwrites a file inside its own run directory** (UNIT-DRIFT §7).
  Progress checkpoints are written **per arm** to a path **outside** the run directory.
- **No run directory is ever deleted.**
- **The finding file is not written to its final path until the run directory exists and the
  run has completed.**
- MANIFEST with repo-relative paths and SHA-256 of every input and output.
- This pre-registration's SHA-256 is embedded as a literal in the runner and verified at
  runtime; mismatch aborts.
- Seed 20260509; replication seed 20260519; both reported.

---

## 10. Limits known in advance, so they cannot be presented later as findings

1. **This instrument measures verbatim quotation and explicit naming. It does not measure
   allusion, paraphrase, thematic commentary, or occasion-of-revelation attribution.** A
   ḥadīth whose whole subject is a verse it never quotes is invisible to it.
2. **It cannot separate citation from shared formula for 865 verses** — 600 under four words,
   265 non-distinctive. Those are `eligible = false`, never zero.
3. **Chain grade is not modelled.** A mawḍūʿ chain counts exactly as a ṣaḥīḥ one. The corpus
   carries no grading field. H-NEW-860's rubric had the same property.
4. **Musnad Aḥmad is incomplete upstream** (§4.1).
5. **UAS remains a corrected synthesis index** (§1.1). Nothing here rehabilitates it.
6. **The 36-surah set of Cell A is the rubric's own set**, so Cell A inherits whatever
   selection the rubric performed. That is deliberate — it is the like-for-like comparison —
   and Cell B is reported for the unselected corpus.

---

*Locked 2026-08-08 by Waiel Al-Shujaa, before any coefficient was computed.
A claim of absence is a claim about a search. Bismillāhi al-Raḥmāni al-Raḥīm.*
