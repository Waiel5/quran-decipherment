---
prereg_id: H-NEW-3050
title: The muqaṭṭaʿāt length floor — no letter-opened surah is short, under three length metrics
author: Waiel Al-Shujaa
date: 2026-08-09
phase: B
status: PRE-REGISTRATION — see §6.0, this is a PARTIALLY DISCLOSED specification, not a blind one
parent_observation: findings/AUDIT-H-NEW-206-LENGTH-CONFOUND.md §4
duplicate_of: H-NEW-46 cell 4 (see §0.1 — this is the single most important fact in this file)
method_parent: [H-NEW-46, H-NEW-46.1, H-NEW-67]
corpus: quran-text/quran-no-tashkeel.json
null_type: exact combinatorial (hypergeometric); NO permutation
tests_in_family: 3
alpha_bonferroni: 0.0166667
---

# Pre-registration — H-NEW-3050

## 0. Why this file exists, and what it must not be allowed to claim

`AUDIT-H-NEW-206-LENGTH-CONFOUND.md` §4 withdrew H-NEW-206's taxonomy inference and retained
one observation:

> **No muqaṭṭaʿāt surah is short.** Zero of the 29 fall among the 40 shortest surahs.
> `P = C(74,29)/C(114,29) = 3.063 × 10⁻⁷`

The audit flagged it POST-HOC and UNVERIFIED-NOVELTY, and asked for the tafsīr corpus to be
searched before any novelty claim. That search is reported in §6.2. But the search that
mattered most was not of the tafsīr corpus.

### 0.1 The observation is not new to this project. It is H-NEW-46 cell 4.

`findings/phase-b-hypotheses/h-new-46-muqattaat-vs-surah-length.md`, pre-registered
**2026-04-16** and published STRONG-PASS 4/4, contains:

| Cell | Stat | Observed | Null mean | p (empirical) |
|:--|:--|--:|--:|--:|
| 4 | **Bottom-29 shortest count** (one-sided lower) | **0/29** | 7.37 | **3.0×10⁻⁵** |

That is the same fact, on the same corpus, with the same label set, in the same direction —
differing from the audit's statement only in the threshold (29 vs 40) and in the null
(10⁵-permutation vs exact). H-NEW-46's own pre-registration says cell 4 was *not*
eyeball-derived; it was designed as a dual to the top-K cell. **It is a properly
pre-registered, still-standing result.** No demotion, reversal, or audit of H-NEW-46 exists in
`findings/`; the file still carries `status: STRONG-PASS (4/4 cells)`. It is not merely
un-retracted but load-bearing:

- `H-NEW-46.1` showed the effect survives Meccan/Medinan stratification (OLS β = +56.4 verses,
  p_HC1 = 2.1×10⁻⁵).
- `UNIT-DRIFT-DEFECT.md` treats the muqaṭṭaʿāt/length confound as established project fact,
  citing H-NEW-46, and names the muqaṭṭaʿāt split "the trap to watch."
- `H-NEW-570-REVERSAL-2026-08-07.md` §57–59 — dated **two days before this file** — rests an
  argument on it directly: "Bin 3 of 5 requires 14 donors and the 85 non-muqaṭṭaʿāt contain 9.
  This is `h-new-46`'s STRONG-PASS result — muqaṭṭaʿāt concentrate in long surahs — restated as
  an impossibility."

**That last citation narrows §5.1's novelty further, and the narrowing is recorded here rather
than left for a later audit to find.** H-NEW-570-REVERSAL's bins are quintiles of **log word
count** — metric M2. So the length effect has already been observed under a word-count metric,
in a different statistic (quintile occupancy rather than minimum rank). M2 is therefore not
virgin territory either; only M3 and the threshold-free statistic are.

**Consequence for this file.** The audit's §4 observation cannot be published as a new
finding. It is a re-derivation. This pre-registration therefore does **not** govern "a new
result about muqaṭṭaʿāt and length." It governs three things that H-NEW-46 did not do:

1. **Metric robustness.** H-NEW-46's rules-tuple is `(no-tashkeel, hafs-kufan, verse-count
   metric)` — *verse count only*. §6.2 establishes empirically that verse count is **not**
   the classical measure of surah length. The result must be shown to survive word and
   character metrics or its rules-tuple is too narrow to support the claim it is used for.
2. **Removal of the arbitrary threshold.** Both 29 and 40 are chosen cutoffs. §3 replaces
   them with a threshold-free statistic.
3. **A control battery that has never been run** (§5.2, §5.3) — the only genuinely blind
   content in this file.

---

## 1. Frozen inputs

| path | role |
|:--|:--|
| `quran-text/quran-no-tashkeel.json` | corpus — 114 surahs, literal `verses` array |
| `data/hafs-verse-counts.tsv` | Ḥafṣ/Kūfan verse counts, cross-check on metric M1 |
| `findings/phase-b-hypotheses/csv/h-new-46.json` | H-NEW-46 published values, for the duplication assertion |

The harness asserts `len(surahs) == 114`, `sum(len(s.verses)) == 6236`, and that metric M1
computed from the JSON matches `data/hafs-verse-counts.tsv` for all 114 surahs. It exits on
mismatch.

**Label set — locked, 29 surahs:**
`{2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42,
43, 44, 45, 46, 50, 68}`

This is the standard 29 and matches al-Suyūṭī's own count — *al-Itqān* nawʿ 60 states the
letters open **تسع وعشرين سورة**, twenty-nine surahs (§6.2.1). The set is identical to the one
used by H-NEW-46, H-NEW-570, H-NEW-2820 and H-NEW-2840.

---

## 2. The hypothesis, stated as a length claim

> **H-NEW-3050.** The 29 muqaṭṭaʿāt-opened surahs occupy a strict **upper region** of the
> corpus length distribution: the shortest of them is far longer than chance placement of 29
> labels among 114 surahs would allow, and this holds under every reasonable measure of
> "length."

**What this claim is not.** It is not a claim that the muqaṭṭaʿāt mark a thematic, generic,
or taxonomic class. The moment it is restated that way it inherits exactly the confound that
`AUDIT-H-NEW-206` documented — a clustering built partly on `surah_length` predicting a label
that is 3.3× longer at the median. **Any downstream use of this file that converts it into a
content claim is a misuse of it**, and §8 binds the write-up to say so.

It is also not a claim about *why*. Three mechanisms remain open and this design does not
separate them: chronology (partly excluded by H-NEW-46.1), muṣḥaf position (**not** excluded —
see §5.3), and compositional/mnemonic function.

---

## 3. Instrument — the threshold-free statistic

Let `L_floor` = the length of the **shortest muqaṭṭaʿāt surah**, and let

```
S_below = #{ surahs whose length is STRICTLY LESS than L_floor }
```

**Test statistic: `S_below`. Direction: one-sided upper (large `S_below`).**
Equivalently: all 29 muqaṭṭaʿāt surahs lie within the `114 − S_below` longest surahs.

### 3.0 Tie-break — locked to the value, not to a rank

`S_below` counts **strictly shorter** surahs. Any surah tied with the floor surah at exactly
`L_floor` is **excluded** from the count. This is the conservative choice — it is the tie
handling least favourable to the hypothesis — and it is locked here because **the boundary tie
is load-bearing, not cosmetic**:

Under metric M1 (verse count) the floor surah is **Q 32 al-Sajda at 30 verses, and three
surahs are tied at 30**: Q 32, Q 67 al-Mulk, Q 89 al-Fajr. Two ranks are therefore defensible
for Q 32 — 49th shortest if it is ordered first among the tied three, 51st if last — and the
choice moves the exact p-value by a factor of **3.2** (4.380×10⁻⁹ vs 1.360×10⁻⁹). A rank-based
statistic silently inherits whichever tie-break the sort happened to use. `S_below` does not:
48 surahs are strictly shorter than 30 verses, unambiguously, and that is the number used.

Metrics M2 and M3 have **no tie** at the boundary (floor surah Q 68 al-Qalam under both), so
the rule binds only on M1 — which is precisely where it is needed.

### 3.1 Why direction is locked upper, and why that is legitimate here

The direction was fixed by H-NEW-46 in April 2026, pre-registered before its null was run,
and confirmed at 4/4 cells. A one-sided upper test is the correct dual of an established
directional finding. Locking it two-sided would be a pretence of ignorance the project does
not have.

### 3.2 Why this replaces the "40 shortest" cutoff

"Zero of 29 in the bottom-40" is `R_min ≥ 41` stated with a chosen 40. Any cutoff `T` below
`R_min` yields count 0, and the exact p-value falls monotonically as `T` rises (§6.1 curve).
A threshold picked after seeing where the zeros stop is a **maximally-selected** statistic and
its nominal p-value is not valid.

`R_min` has no such freedom. It is defined before the data are seen; its observed value
*determines* the tail. `P(R_min ≥ r)` is an ordinary exact one-sided p-value with no selection
to correct for. This is a strict methodological improvement over both H-NEW-46's `T = 29` and
the audit's `T = 40`.

---

## 4. The null — exact, and why no permutation is run

Under H₀ the 29 labels are a uniformly random 29-subset of the 114 surahs, independent of
length. The event `{R_min ≥ r}` is exactly the event that all 29 labels avoid the `r − 1`
shortest surahs. Counting subsets directly:

```
P(R_min ≥ r) = C(114 − (r − 1), 29) / C(114, 29)
```

**No permutation null is run, and this is a deliberate design choice, not an omission.**
The null is a finite exact combinatorial enumeration over a 114-element set: no asymptotic
approximation, no distributional assumption, no parameter, no seed, no resampling error. A
permutation null here would be a Monte-Carlo *estimate of a number already known in closed
form*, and a worse one — H-NEW-46 reported cell 4 at `p = 3×10⁻⁵` against a 10⁵-permutation
resolution floor of `1×10⁻⁵`, whereas the exact value at its `T = 29` is `4.388×10⁻⁵`. The
permutation estimate was floor-limited; the exact value is not.

The harness computes `C(·)` with `math.comb` (exact integer arithmetic) and performs the
division in `fractions.Fraction` before converting to float, so no intermediate rounding
enters the reported p.

**Positive control on the arithmetic (pre-locked):** substituting the 29 *longest* surahs as
a synthetic label set must return `R_min = 86` and `p = C(29,29)/C(114,29) = 1/C(114,29)`;
substituting the 29 *shortest* must return `R_min = 1` and `p = 1.0` exactly. Both are checked
by assertion; the run aborts on either failure.

---

## 5. Pre-registered inferences

### 5.1 Primary — metric robustness (three locked rules-tuples)

Length is computed three ways from `quran-text/quran-no-tashkeel.json`:

| id | metric | definition |
|:--|:--|:--|
| **M1** | verse count | `len(s.verses)` — Ḥafṣ/Kūfan numbering; H-NEW-46's tuple |
| **M2** | word count | `Σ len(v.text.split())` over the surah |
| **M3** | character count | `Σ len(v.text.replace(' ',''))` — no-tashkeel consonantal skeleton |

Rules-tuple: `(no-tashkeel, hafs-kufan, {M1 | M2 | M3})`. Three inferences, Bonferroni k = 3,
**α_bon = 0.0166667**. The three metrics are strongly correlated, so k = 3 is conservative;
it is used anyway because tightening is self-verifying and loosening is not.

**Why three metrics and not one — the empirical justification.** This is not a routine
robustness gesture. §6.2.2 shows that al-Suyūṭī's own comparative length judgement about
three muqaṭṭaʿāt surahs is **false under verse count and true under word and character
count**. The classical notion of surah length that any novelty claim must be judged against is
therefore *not* verse count. H-NEW-46's single-metric tuple is too narrow, and M2/M3 are the
metrics closer to the classical measure.

**Decision rule — locked:**

| outcome | verdict |
|:--|:--|
| `p < α_bon` under **all three** metrics | **ROBUST** — the length floor is not a metric artefact |
| `p < α_bon` under **two** metrics | **PARTIAL** — report which metric dissents and its `R_min` |
| `p < α_bon` under **one or zero** metrics | **METRIC-DEPENDENT** — H-NEW-46's tuple is withdrawn as too narrow |

Per §0.1 this decides *metric robustness only*. **No outcome of §5.1 makes the underlying
length fact a new finding.** A ROBUST verdict widens H-NEW-46's rules-tuple; it does not add a
result to the ledger.

### 5.2 Control A — is the floor specific to the muqaṭṭaʿāt? (BLIND — not yet computed)

The obvious alternative: *any* opening-formula class predicts length, and the muqaṭṭaʿāt are
unremarkable among them. The control is classically grounded — al-Suyūṭī, *al-Itqān* nawʿ 60,
partitions all 114 surahs into **ten** opening types and gives the count of each (§6.2.1).
The muqaṭṭaʿāt are his type 2.

For each of the other nine types, compute `R_min` and its exact p under all three metrics,
using the same formula with the class's own size `k` in place of 29.

**Reported statistic: the survivor count** — how many of the ten opening classes clear
α = 0.05 on `R_min` in the upper direction. This is the intersection question, not a
union of ten separate tests: if six of ten classes show a length floor, "the letters mark long
surahs" is a fact about *surah openings and length* generally and the muqaṭṭaʿāt lose their
claim to be special. If the muqaṭṭaʿāt are the sole or near-sole survivor, the specificity
holds. **The survivor count is published whatever it is**, and no threshold on it is
pre-declared as a pass/fail gate, because its interpretive weight is continuous.

Assigning the other nine classes requires a surah-to-opening-type mapping that does not yet
exist in the repository. It is built from al-Suyūṭī's own enumeration, which names the surahs
of each type explicitly for types 3 and 5–10 and lists incipits for type 4. Cases his text
leaves ambiguous are recorded in the run manifest with the reason, and the control is
reported both with and without them.

### 5.3 Control B — muṣḥaf position (BLIND — not yet computed)

**This is the confound H-NEW-46.1 did not address.** It controlled chronology; it did not
control position in the muṣḥaf. The muqaṭṭaʿāt surahs sit overwhelmingly in the front of the
codex, and the codex is loosely ordered long-to-short. A length floor could be a positional
floor wearing a length label — the same failure mode as H-NEW-206, one level up.

Statistic: `R_min` recomputed on **position-residualised length**. Regress length on muṣḥaf
index (`surah_id`) by LOESS, take residuals, re-rank, recompute `R_min`. Because
residualisation destroys the exact-null argument (the residual ranks are no longer exchangeable
under a simple subset null), this arm alone uses a **permutation null**: 10⁵ uniform random
29-subsets, seed **20260809**, empirical one-sided upper p.

**This arm is explicitly interpretive and is not part of the k = 3 family.** It is reported
with its own α = 0.05, unadjusted, and labelled as such. A failure here does not retract §5.1;
it bounds what §5.1 may be said to mean.

---

## 6. Garden-of-forking-paths log

### 6.0 Disclosure — this file is not blind, and the reason is my own sequencing error

**The §5.1 statistics were computed before this file was written.** While verifying al-Suyūṭī's
length claim for the novelty search (§6.2.2) I went beyond what that verification required and
computed `R_min` and the full threshold curve under all three metrics. The observed values are
therefore known at pre-registration time and are disclosed in full in §6.1 rather than hidden.

**Consequence, stated plainly: §5.1 is a disclosed re-analysis, not a confirmatory test.** It
cannot be reported as confirmatory and the write-up must not describe it as such. Given §0.1 —
where the underlying fact is already an established in-project result — the cost of this error
is small, but it is a real defect in this file and it is recorded rather than papered over.

**§5.2 and §5.3 are genuinely blind.** Neither has been computed in any form. They are the
only content here that carries confirmatory weight.

### 6.1 The threshold sensitivity curve — the whole curve, as required

Count of muqaṭṭaʿāt surahs among the `T` shortest, and the exact p when that count is 0:

| T | M1 verse: cnt / p | M2 word: cnt / p | M3 char: cnt / p |
|--:|:--|:--|:--|
| 10 | 0 / 4.60e-02 | 0 / 4.60e-02 | 0 / 4.60e-02 |
| 20 | 0 / 1.46e-03 | 0 / 1.46e-03 | 0 / 1.46e-03 |
| **29** | 0 / **4.39e-05** | 0 / 4.39e-05 | 0 / 4.39e-05 |
| 30 | 0 / 2.89e-05 | 0 / 2.89e-05 | 0 / 2.89e-05 |
| 35 | 0 / 3.26e-06 | 0 / 3.26e-06 | 0 / 3.26e-06 |
| **40** | 0 / **3.06e-07** | 0 / 3.06e-07 | 0 / 3.06e-07 |
| 45 | 0 / 2.32e-08 | 0 / 2.32e-08 | 0 / 2.32e-08 |
| 48 | 0 / 4.38e-09 | 0 / 4.38e-09 | 0 / 4.38e-09 |
| 50 | 1 / — | 0 / 1.36e-09 | 0 / 1.36e-09 |
| 52 | 1 / — | 0 / 4.01e-10 | 0 / 4.01e-10 |
| 53 | 2 / — | 1 / — | 0 / 2.14e-10 |
| 55 | 3 / — | 1 / — | 1 / — |
| 60 | 4 / — | 2 / — | 3 / — |

Bold rows are the two thresholds already in the literature of this project: H-NEW-46's 29 and
the audit's 40.

**What the curve shows.** The count is 0 at every `T ≤ 48` under all three metrics; the p-value
falls smoothly and monotonically; nothing distinguishes 40. **The result does not depend on the
threshold — it depends on there being no muqaṭṭaʿāt surah below rank 49.** That is precisely
what `R_min` measures directly, which is why §3 discards the cutoff.

**The audit's 40 was conservative, not favourable.** The threshold-free statistic is two orders
of magnitude more extreme than the number the audit reported. Had 40 been chosen to flatter the
result, it would have been chosen at 48.

Observed values, disclosed: `R_min` = **49** (M1, Q 32 al-Sajda), **53** (M2, Q 68 al-Qalam),
**54** (M3, Q 68 al-Qalam). The identity of the floor surah is itself metric-dependent — a
further reason the single-metric tuple was too narrow.

### 6.2 Novelty search of the classical corpus — what was searched and what was found

Method: diacritic- and orthography-normalised co-occurrence search over ~200 MB of classical
Arabic, run in **both** directions — (a) muqaṭṭaʿāt term near a length term, (b) every passage
where ≥2 of the four classical length classes co-occur, checked for any muqaṭṭaʿāt term.
Muqaṭṭaʿāt terms: `المقطعة، مقطعة، مقطعات، حروف التهجي، التهجي، فواتح السور، أوائل السور، هجاء،
حروف المعجم، هذه الحروف`. Length terms: `الطوال، السبع الطوال، المئين، المثاني، المفصل، طوال،
طويلة، أطول، أقصر، قصار، القصار، قصيرة، الطول، طولها`.

Searched, with paths verified present on disk:

| source | path | result |
|:--|:--|:--|
| al-Suyūṭī, *al-Itqān* (complete, 80 nawʿ) | `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` | 2 fwd hits, both false positives; see §6.2.1–3 |
| al-Rāzī, *Mafātīḥ al-ghayb* | `raw/razi-mafatih-al-ghayb.openiti.raw.txt` | 0 fwd; 3 length-class passages, none mentions the letters |
| al-Qurṭubī, *al-Jāmiʿ* | `raw/qurtubi-jami-ahkam.openiti.raw.txt` | 3 fwd, all false positives |
| al-Ṭabarī, *Jāmiʿ al-bayān* | `raw/tabari-jami-bayan.openiti.raw.txt` | 1 fwd, false positive |
| al-Zamakhsharī, *al-Kashshāf* | `raw/zamakhshari-kashshaf.openiti.raw.txt` + `zamakhshari-kashshaf/…djvu.txt` | 0 fwd |
| al-Biqāʿī, *Naẓm al-durar* | `raw/biqai-nazm-al-durar.openiti.raw.txt` | 3 fwd — **1 genuine**, §6.2.4 |
| Ibn Kathīr | `raw/ibn-kathir-tafsir-quran.openiti.raw.txt` | 3 fwd, all false positives |
| al-Thaʿlabī, al-Ṭabarsī, al-Suyūṭī *al-Durr al-manthūr* | `raw/{thaclabi,tabarsi,suyuti-durr}…raw.txt` | 6 fwd, all false positives |
| Ibn ʿĀshūr, *al-Taḥrīr wa'l-Tanwīr* | `spa5k-tafsir-api/ar-tafseer-tanwir-al-miqbas/` (mislabelled folder — see `MISLABELLED-TANWIR-FOLDER.md`) | 0 fwd |
| al-Baghawī, al-Wāsiṭ, al-Saʿdī, al-Muyassar, Ibn Kathīr, al-Qurṭubī, al-Ṭabarī | `spa5k-tafsir-api/ar-*` | 3 fwd, all false positives |

**Could not be searched, stated as such:** `zarkashi-al-burhan-fi-ulum-al-quran.pdf` is a
**scanned bitonal image PDF** (`Producer: Adobe Acrobat 7.05 Image Conversion Plug-in`, JBIG2
images, no text layer; `pdftotext` yields 1,568 bytes of nothing). `biqai-nazm-al-durar.pdf` is
likewise image-only (0 extractable characters) — though al-Biqāʿī's text *was* searched via the
OpenITI transcription above. **No claim in this file rests on al-Zarkashī's *al-Burhān*, and
none should be made until it is OCR'd.** `suyuti-al-itqan-fi-ulum-al-quran-english.pdf` is a
**partial draft** translation by Muneer Fareed — "some twenty chapters of excerpts" — not the
full Itqān; the complete Arabic OpenITI text was used instead.

**Recall limits, stated honestly.** Term-based search under-recalls this question, because the
tafsīrs discuss the letters *inline* at each surah opening rather than under a technical label
(al-Rāzī's 29 MB yields only 177 label hits). A statement of the form "these surahs are long,"
made without any of the search terms, could be missed. The negative result below is strong but
it is not a proof of absence.

#### 6.2.1 al-Suyūṭī, *al-Itqān*, nawʿ 60 — the openings taxonomy, with counts and no lengths

`النوع الستون: في فواتح السور` (vol. 3, pp. 361–365 in the Abū al-Faḍl Ibrāhīm edition;
`PageV03P361`–`PageV03P365`). Al-Suyūṭī partitions all 114 surah openings into ten types and
**gives the count of surahs in each**: praise (5 + 2 + 7), **`الثاني: حروف التهجي في تسع وعشرين
سورة`** — "the second: the spelling-letters, in twenty-nine surahs" — vocative (10),
declarative (23), oath (15), conditional (7), imperative (6), interrogative (6), supplication
(3), causal (1).

This is the closest the tradition comes to the present question, and it is decisive as a
negative: **al-Suyūṭī is counting surahs by opening class, and says nothing whatever about the
length of the surahs in any class.** He refers the reader elsewhere for the letters' meaning:
`وقد مضى الكلام عليها مستوعبا في نوع المتشابه`.

**Reverse check, and it is the strongest single result of the search.** In nawʿ 18
(`في جمعه وترتيبه`), where the fourfold length classification is laid out in full, the terms
`المقطعة`, `التهجي`, `فواتح السور` occur **zero times**. In nawʿ 43 (`في المحكم والمتشابه`),
which carries al-Suyūṭī's *complete* treatment of the muqaṭṭaʿāt, the terms `الطوال`, `المئين`,
`المثاني`, `المفصل`, `طويلة`, `قصار` occur **zero times**. The two discussions do not touch.

#### 6.2.2 al-Suyūṭī, *al-Itqān*, nawʿ 18 — muqaṭṭaʿāt surahs compared BY LENGTH

Vol. 1, pp. 218–219 (the passage falls between markers `PageV01P218` and `PageV01P219`).
Arguing that the surah order is divinely fixed (*tawqīfī*):

> قلت: ومما يدل على أنه توقيفي كون **الحواميم** رتبت ولاء وكذا **الطواسين** ولم ترتب المسبحات
> ولاء بل فصل بين سورها وفصل بين **طسم** الشعراء و**طسم** القصص **بطس** **مع أنها أقصر منهما**
> ولو كان الترتيب اجتهاديا لذكرت المسبحات ولاء وأخرت طس عن القصص.

"…and among the things indicating that it is *tawqīfī* is that the **ḥawāmīm** are arranged
consecutively, and likewise the **ṭawāsīn**… and Ṭā-Sīn-Mīm of al-Shuʿarāʾ [Q 26] and
Ṭā-Sīn-Mīm of al-Qaṣaṣ [Q 28] are separated by Ṭā-Sīn [Q 27] **even though it is shorter than
both of them**…"

**This is the tradition reasoning explicitly about the length of muqaṭṭaʿāt surahs.** It is not
the present hypothesis — it is an argument about ordering *within* the letter-groups, and it
presupposes rather than asserts a descending-length principle. But it forecloses any claim that
the classical scholars never thought about these surahs' lengths.

**And it constrains the rules-tuple, which is why §5.1 locks three metrics.** Verified against
the corpus:

| | Q 26 | Q 27 | Q 28 | is Q 27 "shorter than both"? |
|:--|--:|--:|--:|:--|
| verses | 227 | 93 | 88 | **NO** (93 > 88) |
| words | 1353 | 1215 | 1520 | **YES** |
| characters | 5663 | 4846 | 6012 | **YES** |

**Al-Suyūṭī's statement is false under verse count and true under word and character count.**
The classical measure of surah length is not verse count. H-NEW-46 tested verse count only.

#### 6.2.3 al-Suyūṭī, *al-Itqān*, nawʿ 17 khātima — letters and length-classes in ONE taxonomy

`PageV01P200`–`PageV01P201`. Immediately after the Wāthila b. al-Asqaʿ ḥadīth that establishes
the fourfold division (`أعطيت مكان التوراة السبع الطول وأعطيت مكان الزبور المئين وأعطيت مكان
الإنجيل المثاني وفضلت بالمفصل`), al-Suyūṭī quotes *Jamāl al-qurrāʾ*:

> وفي جمال القراء: قال بعض السلف في القرآن ميادين وبساتين ومقاصير وعرائس وديابيج ورياض
> **فميادينه ما افتتح بـ الم وبساتينه ما افتتح بـ "الر"** ومقاصيره الحامدات وعرائسه المسبحات
> وديباجه آل عمران **ورياضه المفصل** وقالوا **الطواسيم والطواسين وآل حم والحواميم**.

"…the Qurʾān has fields, gardens, chambers, brides, brocades and meadows: **its fields are what
opens with *Alif-Lām-Mīm*, its gardens what opens with *Alif-Lām-Rā*,** its chambers the
*ḥāmidāt*, its brides the *musabbiḥāt*, its brocade Āl ʿImrān, **and its meadows the
*mufaṣṣal*** — and they say: the *ṭawāsīm*, the *ṭawāsīn*, the *āl ḥā-mīm* and the *ḥawāmīm*."

**This is the single most relevant classical passage found.** Muqaṭṭaʿāt groups and a length
class (*al-mufaṣṣal*) appear as **co-ordinate members of one taxonomy of the Qurʾān**, adjacent
to the fourfold length ḥadīth. The scheme treats them as parallel and implicitly disjoint
categories. But it makes **no length statement about the letter-groups** — the *mufaṣṣal* is
one bin among six, not a property predicated of the others.

#### 6.2.4 al-Biqāʿī, *Naẓm al-durar* — the letters tied to the mufaṣṣal boundary

`PageV18P347`–`PageV18P349`, at the head of sūrat al-Ḥujurāt. Al-Biqāʿī closes Q 48 with
`وهذا آخر القسم الأول من القرآن، **وهو المطول**` — "this is the end of the first division of the
Qurʾān, **which is the lengthened one**" — then opens Q 49 as `أول المفصل`, and writes:

> **وابتدئ ثاني المفصل بحرف من الحروف المقطعة كما ابتدئ ثاني ما عداه بالحروف المقطعة**

"**and the second of the *mufaṣṣal* was begun with a letter of the disconnected letters, just
as the second of what is other than it was begun with the disconnected letters**" — i.e. Q 50
Qāf stands to the *mufaṣṣal* as Q 2 al-Baqara stands to the long division.

**This is a genuine, explicit classical linkage between the muqaṭṭaʿāt and a length-based
partition of the Qurʾān**, and it is the only one the search found. It is *positional*, not
metric: al-Biqāʿī claims the letters mark the **second surah of each division**. Note that it
cuts *against* the present hypothesis rather than for it — he is drawing attention to a
muqaṭṭaʿāt surah sitting **inside** the short division.

#### 6.2.5 The false-positive generator, recorded so it is not rediscovered

The search returned **21** forward co-occurrences in total. **Nineteen are spurious**; the
remaining two are adjacent hits on the single genuine al-Biqāʿī passage of §6.2.4.

Five of the nineteen share one cause: **`ذي الطول`** — "Possessor of Bounty," a divine name at
Q 40:3 — sits three words from `حم` in every commentary on the ḥawāmīm, and the same phrase
carries the `طه`/`طسم` divine-name derivation (`الطاء من ذي الطول`). Stripped of diacritics,
`الطَّوْل` (bounty) is indistinguishable from `الطُّول` (length). Remaining false positives:
`هجاء` as "satire" (al-Qurṭubī on Kaʿb b. Zuhayr; al-Ṭabarsī), `مقطعات النيران` as "garments of
fire" (al-Ṭabarsī), `المفصل` as "elaborated" from Q 11:1 `ثم فصلت` rather than the length class
(Ibn Kathīr, al-Biqāʿī), `المثاني` in its Q 39:23 sense (Ibn Kathīr), `النخل طوالا` — "tall
palm trees," Q 50:10, adjacent to the Qāf muqaṭṭaʿāt note (al-Muyassar), `مدها وطولها` of the
alif's shape (al-Thaʿlabī), `أطول الكلم` — the longest *word* in the Qurʾān, beside a note that
the Kufans count `الم` as a verse (al-Qurṭubī) — and, in al-Ṭabarsī, `مدة ملك محمد قصيرة`,
"short" describing a **reign** in the *ḥisāb al-jummal* tradition.

**Any future search of this corpus must exclude `ذي الطول` explicitly or it will drown.**

### 6.3 Verdict on novelty

| claim | status |
|:--|:--|
| Muqaṭṭaʿāt surahs are systematically long / none is short | **NOT NOVEL to this project** — H-NEW-46 cell 4, pre-registered 2026-04-16 (§0.1) |
| That claim stated explicitly in the classical corpus searched | **NOT FOUND.** No source states it. The letters-discussion and the length-class discussion are disjoint in al-Suyūṭī, who is the scholar most likely to have joined them |
| Classical awareness that muqaṭṭaʿāt surahs *have* comparable lengths | **PRESENT** — al-Suyūṭī nawʿ 18 (§6.2.2) |
| Classical placement of letter-groups and length-classes in one scheme | **PRESENT** — *Jamāl al-qurrāʾ* via al-Itqān nawʿ 17 (§6.2.3) |
| Classical linkage of the letters to a length-division boundary | **PRESENT** — al-Biqāʿī (§6.2.4), positional not metric, and pointing the other way |
| The exact combinatorial null on `R_min` | **Novel so far as this search reached** — and it is a modern statistical object, not the kind of claim the tradition makes |
| Metric-robustness of the floor under M2 (word count) | **Partly pre-empted** — `H-NEW-570-REVERSAL` already binned by log word count (§0.1) |
| Metric-robustness of the floor under M3 (character count) | **Not previously tested** |

**Bottom line: the observation is not novel. Both facts — that the letters open 29 surahs, and
that surahs fall into length classes — are ancient and are found side by side in one passage
(§6.2.3), but the overlap between the two sets is never remarked on.** What is new is narrow
and worth exactly what it is: the exact null, the threshold-free statistic, and the metric
robustness. That is a methodological contribution to an existing finding, not a discovery.

---

## 7. What is published regardless of outcome

- All three `R_min` values and exact p's, and the full §6.1 curve recomputed by the harness.
- The §5.2 survivor count across all ten of al-Suyūṭī's opening classes, whatever it shows —
  **including the outcome in which the muqaṭṭaʿāt are unremarkable among them.**
- The §5.3 position-residualised result, **including a failure**, which would mean the length
  floor is a muṣḥaf-position floor and would bound §5.1 accordingly.
- §0.1 and §6.3 reproduced in the finding file at equal prominence to any result. A write-up
  of this test that omits the H-NEW-46 duplication is not publishable.

## 8. Binding constraints on the write-up

1. The finding must state in its TL;DR that this is a **re-test of H-NEW-46 cell 4 under wider
   metrics**, not a new result.
2. The finding must state that it is a **length** result and must not be cited as evidence for
   any thematic or taxonomic property of the muqaṭṭaʿāt (§2).
3. The finding must carry §6.0's disclosure that §5.1 was computed before locking.
4. No claim may be attributed to al-Zarkashī's *al-Burhān*, which could not be read (§6.2).

---

## 9. Integrity

- Directions locked in §3.1 before any §5.2/§5.3 statistic was computed; justified from
  H-NEW-46's April 2026 pre-registration rather than from the present data.
- Bonferroni k = 3 declared in §5.1. It is conservative given metric correlation; per project
  standing rule, tightening self-verifies and loosening would require ratification.
- Exact null (§4) — no seed, no resampling error, no multiplicity from a chosen threshold.
  The one permutation arm (§5.3) carries seed 20260809 and is excluded from the k = 3 family.
- §6.0 discloses that the primary statistics were computed before this file was written, which
  demotes §5.1 from confirmatory to disclosed re-analysis. §5.2 and §5.3 remain blind.
- Every classical citation in §6.2 carries a verified on-disk path and a page marker from the
  source text. Sources that could not be read are named as unread rather than omitted.
