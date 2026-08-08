---
id: H-NEW-2620
title: Cross-edition exegetical attention and disagreement as a measurable per-verse score, and its relation to structural extremeness
type: pre-registration
status: LOCKED — written before any outcome computation
date: 2026-08-07
author: Waiel Al-Shujaa
seed: 20260509
n_perm: 10000
family: TAFSIR-2026-08-07-A
bonferroni_k: 6
alpha_bonferroni: 0.00833333
rules_tuple: (no-tashkeel for verse text, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi; tafsir text as distributed by the spa5k tafsir_api snapshot on disk)
---

# Pre-registration — H-NEW-2620

> # ⛔ THIS PRE-REGISTRATION WAS EDITED AFTER PUBLICATION — TWICE — AND ITS SHA LOCK IS BROKEN
>
> **`scripts/h-new-2620.py` can no longer run.** Its line 26 hard-codes
> `EXPECTED_PREREG_SHA = 8826da50…bc63` and lines 114-116 abort on mismatch. This file now hashes
> `7c7fc5fb…9736`.
>
> | commit | prereg SHA | state |
> |:--|:--|:--|
> | `b0cf8a09a` — publication | `8826da50…bc63` | ✅ matches the script |
> | `b76ec401f` — 2026-08-07, the 702-file genre-control propagation | `b4a17e28…` | ❌ **broken here** |
> | `81db39027` — 2026-08-08, the attribution-correction block | `7c7fc5fb…9736` | ❌ broken again |
>
> **Both edits were mine, and both were well-intentioned corrections.** The first swept this file
> up in a bulk propagation across 702 files; the second added an attribution-correction block. Each
> was *content*-correct and *procedurally* wrong.
>
> **A pre-registration is the one document in this project that must never be edited after its
> run.** Its entire evidential value is that it is fixed before the data is seen — a SHA lock that
> can be invalidated by a later correction is not a lock. **The correct place for every one of
> those corrections was the FINDING file, which is exactly where such notices belong and where the
> attribution block should have gone alone.**
>
> **The stale hash is still asserted as "runtime-verified"** at `h-new-2620-tafsir-contested.md:8`
> and `:68`, `csv/h-new-2620.json:3`, and `MASTER-FINDINGS-LEDGER.md:6813`. Those assertions were
> true when written and are false now. **H-NEW-2620's NULL verdict is unaffected** — the numbers
> were computed under the original prereg, before either edit — but the run is no longer
> reproducible without reverting this file to `b0cf8a09a`.
>
> **STANDING RULE, added to `findings/UNIT-DRIFT-DEFECT.md` §7's family: never edit a
> pre-registration after its run, for any reason, including to correct an error in it. Corrections
> go in the finding. If a pre-registration itself is wrong, that fact is a finding — record it, do
> not repair it.**


> ### ⛔ ATTRIBUTION CORRECTION 2026-08-08 — the "classical-only" sensitivity was never run
>
> **`ar-tafseer-tanwir-al-miqbas/` is Ibn ʿĀshūr's *al-Taḥrīr wa'l-Tanwīr* (d. 1393 AH / 1973 CE),
> NOT *Tanwīr al-Miqbās* attributed to Ibn ʿAbbās (d. 68 AH).** The folder cites al-Zamakhsharī
> ×249, al-Qurṭubī ×220, al-Sakkākī ×75, Ibn Mālik ×70, al-Raḍī ×69. See
> `data/literature/classical-tafsir/MISLABELLED-TANWIR-FOLDER.md`.
>
> **The load-bearing consequence.** This file's sensitivity row labelled
> **"classical-only (5 pre-modern)"** is **4 pre-modern editions plus one from 1973.** The
> accompanying sentence — *"Dropping the three modern editions does not rescue the hypothesis"* —
> **is false as written: only three of FOUR modern editions were dropped.** Four of the eight
> primary Arabic editions are modern, not three.
>
> **And the mislabelled edition is the most influential single edition in the set** — the
> leave-one-edition-out range is carried by it at **−0.2096**.
>
> **A further error in the same family:** this file states that `en-tafsir-ibn-abbas` is an English
> translation of the Arabic slug and that the English set holds ~2 independent witnesses. **They
> are unrelated works** — the English edition is the genuine short Ibn ʿAbbās recension (962 chars
> at Q 2:1 against the Arabic slug's 17,227), and the English set holds **3** independent
> witnesses.
>
> **What does NOT change: the NULL verdict stands.** Every number was computed on whatever text
> was in the folder, and those computations are correct. What changes is **whose exegetical
> behaviour was measured**, and the claim that a classical-only sensitivity was ever performed.
> That sensitivity has not been run and is queued.



> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

**Nothing in this file may be amended after the first execution of
`scripts/h-new-2620.py`. The SHA-256 of this file is embedded as a literal in that
script and verified at runtime; a mismatch aborts the run.**

---

## 0. What was looked at before locking (garden-of-forking-paths log)

Full disclosure of every inspection performed **before** this file was locked. All of it
concerns the *instrument* — file counts, coverage, encoding, segmentation artefacts. **No
relation between any commentary quantity and any structural, chronological or architectural
variable was computed or viewed.** The outcome-to-predictor association is unobserved as of
this lock.

What I looked at:

1. Directory listing and `editions.json` of `data/literature/classical-tafsir/spa5k-tafsir-api/`.
2. Per-edition JSON file counts, empty-text counts, short-text (<20 char) counts,
   distinct-text counts, median text length.
3. The *duplicate-block* structure — how many verses in each edition share byte-identical
   commentary text with another verse, and what the largest such groups look like
   (inspected for `ar-tafsir-muyassar` only).
4. Presence and raw frequency of eight candidate Arabic dispute-marker strings per edition.
5. Two sample commentary texts (`ar-tafseer-al-saddi/2/2.json`,
   `ar-tafsir-al-wasit/2/2.json`) read in order to identify the works, because the API's
   author labels are ambiguous.
6. Structure of `csv/h-new-590.json`, `csv/h-new-840.json`, `quran-text/quran-no-tashkeel.json`,
   and the QAC morphology file header.

Four locked design decisions below (§2.2 amortisation, §2.3 within-edition ranking,
§2.5 dispute-marker boundary handling, §1.3 exclusion of the *Asbāb* edition) are direct
consequences of items 2–5. They are **instrument corrections made with the outcome
unobserved**, not adjustments made to a result.

---

## 1. Data — frozen inputs

### 1.1 Freeze method for the tafsīr tree

Hashing 77,437 files individually inside the run script is impractical to record inline, so
the tree is frozen by **manifest**:

- `findings/phase-b-hypotheses/data/h-new-2620-tafsir-manifest.tsv` — one row per `*.json`
  file under the tafsīr root, columns `relpath`, `sha256`, `bytes`, header row first, rows
  sorted ascending by `relpath` (Python default string sort), UTF-8, `\n` line endings.
- **Rows: 77,437. Total bytes covered: 407,169,153.**
- **Manifest SHA-256: `2ce03c91087fad7a357c130a496e2557a07dd6a6a1b6e8df8e8b7d15cf1bcff6`**

The run script verifies the manifest's own SHA-256, then verifies that **every file it
actually reads** matches its recorded per-file SHA-256 in the manifest. Any mismatch, or any
file read that is absent from the manifest, aborts the run. This is a full freeze of the read
set, not a sample.

### 1.2 Other frozen inputs (SHA-256 verified at runtime)

| Input | SHA-256 |
|:--|:--|
| `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |
| `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| `findings/phase-b-hypotheses/csv/h-new-590.json` | `cf69308553ad2d60fee4a456c0979892e1b4f45bb36e8e044d40e261c1f4c476` |
| `findings/phase-b-hypotheses/csv/h-new-840.json` | `e16a0f70aa842fbe650f2b14874a3f27b176193b86d7964fa9c6b76620ff2aa0` |

### 1.3 Editions — locked roster

Directory-verified. `editions.json` is the API's own metadata; where its author label is
ambiguous or wrong, the disambiguation and its evidence are stated. **No author or work name
here is asserted beyond what the files support.**

**PRIMARY — 8 Arabic editions**, each with exactly 6,236 verse files, zero empty texts:

| # | Slug | Scholar / body | Work |
|:-:|:--|:--|:--|
| 1 | `ar-tafsir-al-tabari` | Abū Jaʿfar Muḥammad b. Jarīr al-Ṭabarī (d. 310/923) | *Jāmiʿ al-bayān ʿan taʾwīl āy al-Qurʾān* |
| 2 | `ar-tafseer-al-qurtubi` | Abū ʿAbd Allāh Muḥammad b. Aḥmad al-Qurṭubī (d. 671/1273) | *al-Jāmiʿ li-aḥkām al-Qurʾān* |
| 3 | `ar-tafsir-ibn-kathir` | Ismāʿīl b. ʿUmar Ibn Kathīr (d. 774/1373) | *Tafsīr al-Qurʾān al-ʿaẓīm* |
| 4 | `ar-tafsir-al-baghawi` | al-Ḥusayn b. Masʿūd al-Baghawī (d. 516/1122) | *Maʿālim al-tanzīl* |
| 5 | `ar-tafseer-tanwir-al-miqbas` | ascribed to Ibn ʿAbbās via al-Kalbī; compilation traditionally attributed to al-Fīrūzābādī (d. 817/1414) | *Tanwīr al-Miqbās min tafsīr Ibn ʿAbbās* |
| 6 | `ar-tafseer-al-saddi` | ʿAbd al-Raḥmān b. Nāṣir **al-Saʿdī** (d. 1376/1956) | *Taysīr al-Karīm al-Raḥmān fī tafsīr kalām al-Mannān* |
| 7 | `ar-tafsir-al-wasit` | **author not determinable from disk** — a modern *al-Tafsīr al-Wasīṭ* | *al-Tafsīr al-Wasīṭ* |
| 8 | `ar-tafsir-muyassar` | committee work, King Fahd Complex (`editions.json` author field: `المیسر`) | *al-Tafsīr al-Muyassar* |

**Two disambiguations, with evidence:**

- **#6.** The API label is `Saddi` / `ar-tafseer-al-saddi`, which reads as al-Suddī
  (Ismāʿīl b. ʿAbd al-Raḥmān al-Suddī, d. 127/745). It cannot be him: al-Suddī's tafsīr does
  not survive as an independent 6,236-verse book, only in quotation (chiefly through
  al-Ṭabarī). The text at `ar-tafseer-al-saddi/2/2.json` is modern didactic prose
  (*wa-hādhihi qāʿida mufīda…*). Identified as **al-Saʿdī**, *Taysīr al-Karīm al-Raḥmān*.
- **#7.** The title *al-Wasīṭ* invites identification with al-Wāḥidī (d. 468/1076),
  *al-Wasīṭ fī tafsīr al-Qurʾān al-majīd*. It cannot be him: the text at
  `ar-tafsir-al-wasit/2/2.json` quotes *ṣāḥib al-Kashshāf* — al-Zamakhsharī, d. 538/1144 —
  who died **seventy years after al-Wāḥidī**. It is therefore a modern *al-Tafsīr al-Wasīṭ*.
  Which one (Majmaʿ al-Buḥūth al-Islāmiyya of al-Azhar, or Ṭanṭāwī) **is not determinable
  from the files and is not asserted**.

**Consequence, locked as a limit before any result:** three of the eight primary editions
(#6 al-Saʿdī, #7 al-Wasīṭ, #8 al-Muyassar) are **modern**, not classical. The primary score
is therefore *not* a measure of the classical tradition. §6.1 registers a classical-only
sensitivity over editions #1–#5.

**SECONDARY — 4 English editions** (6,236 verse files each, zero empty):
`en-al-jalalayn` (al-Maḥallī d. 864/1459 + al-Suyūṭī d. 911/1505, *Tafsīr al-Jalālayn*,
altafsir.com translation); `en-tafisr-ibn-kathir` (Ibn Kathīr, abridged English);
`en-tafsir-ibn-abbas` (*Tanwīr al-Miqbās*, altafsir.com translation);
`en-tafsir-maarif-ul-quran` (Muftī Muḥammad Shafīʿ, d. 1976, *Maʿārif al-Qurʾān*, English).

**EXCLUDED — `en-asbab-al-nuzul-by-al-wahidi`** (al-Wāḥidī, d. 468/1076, *Asbāb al-nuzūl*,
altafsir.com translation). Three reasons, all locked before any outcome computation:
(i) it is an occasions-of-revelation work, not a tafsīr; (ii) its coverage is **1,089 verses
across 75 surahs** — 17.5% of the corpus — and the gap is *by design*, since most verses
have no recorded sabab; (iii) including a structurally partial edition in a cross-edition
dispersion measure would manufacture dispersion, exactly the failure mode this
pre-registration is built to avoid. It carries its own `empty_ayahs.json` index files
(70 of them), which are excluded from all reads. Its coverage is reported in the findings
file as a datum; it belongs to F-12, not here.

**Cross-edition non-independence, declared:** `en-tafisr-ibn-kathir` is an English
abridgement of `ar-tafsir-ibn-kathir`, and `en-tafsir-ibn-abbas` is an English translation
of `ar-tafseer-tanwir-al-miqbas`. Because Arabic and English are analysed **separately**,
this does not contaminate the primary; it does mean the English set contains only ~2 fully
independent witnesses and is reported as such.

---

## 2. H1 — score construction (definitional, no inference)

### 2.1 Text normalisation

For a verse file's `text` field: strip leading/trailing whitespace, collapse every run of
Unicode whitespace to a single space. Call the result *T*. Length is `len(T)` in Unicode
code points. Arabic and English lengths are **never mixed**.

### 2.2 Amortisation of shared commentary blocks — mandatory correction

Several editions assign **one commentary block to a run of verses** and the API replicates
that block into every verse file in the run. Measured before locking, as a count of verses
whose normalised text is byte-identical to at least one other verse in the same edition:

| Edition | verses in shared blocks | % of 6,236 | distinct blocks |
|:--|--:|--:|--:|
| `ar-tafsir-al-tabari` | 83 | 1.3% | 6,186 |
| `ar-tafsir-al-baghawi` | 83 | 1.3% | 6,171 |
| `ar-tafseer-al-qurtubi` | 147 | 2.4% | 6,116 |
| `ar-tafseer-tanwir-al-miqbas` | 165 | 2.6% | 6,080 |
| `ar-tafsir-al-wasit` | 358 | 5.7% | 6,035 |
| `ar-tafsir-ibn-kathir` | 536 | 8.6% | 5,894 |
| `ar-tafseer-al-saddi` | 853 | 13.7% | 5,753 |
| `ar-tafsir-muyassar` | 1,827 | 29.3% | 5,018 |
| `en-tafisr-ibn-kathir` | **5,749** | **92.2%** | 1,895 |
| `en-tafsir-maarif-ul-quran` | 4,344 | 69.7% | 3,037 |
| `en-al-jalalayn` | 82 | 1.3% | 6,171 |
| `en-tafsir-ibn-abbas` | 36 | 0.6% | 6,209 |

Taking raw length would credit each verse of a 14-verse block with the whole block. **Locked
primary treatment: amortised length** = `len(T) / g`, where *g* is the number of verses in
that edition sharing byte-identical *T*. Raw (un-amortised) length is registered as a
sensitivity (§6.2), not as the primary.

This is also the second reason the English set is secondary: at 92% and 70% block coverage,
the English score would measure the API's segmentation more than any exegete's attention.

### 2.3 Within-edition rank normalisation

Editions differ by an order of magnitude in scale (median normalised length: al-Baghawī 288,
al-Muyassar 189, al-Ṭabarī 1,283, Tanwīr al-Miqbās 1,748). Raw lengths are not comparable
across editions and means over them are meaningless. **Locked: within each edition, convert
the 6,236 amortised lengths to percentile ranks** `r ∈ (0,1)` using mid-ranks for ties, and
`r = (mid_rank − 0.5) / 6236`. Every statistic below is built from these ranks. No means of
raw lengths are computed anywhere.

### 2.4 The two length-derived scores

For verse *v*, over the 8 Arabic editions:

- **ATTENTION** `A(v) = mean_e r(e,v)` — total exegetical attention, rank-aggregated.
- **DISAGREEMENT** `D(v) = IQR({r(e,v)}_e)` — the interquartile range of the 8 within-edition
  percentile ranks (linear-interpolation quantiles, `numpy`-free implementation specified in
  the script). This is the *cross-edition dispersion in attention*.

**Naming discipline, locked:** `D` measures **disagreement in how much attention an edition
gives a verse**. It does **not** measure disagreement about meaning. Calling it "contested" is
an interpretive hypothesis about the cause, not a description of the measurement, and the
findings file must not blur the two. §2.5 registers the channel that does address content.

**Mechanical coupling, and the correction for it.** `A` and `D` are not independent by
construction: if all eight ranks sit near 0 or near 1, the IQR is forced small. `D` is
therefore residualised on `A` **and** `A²` in addition to the difficulty covariates (§3.2).
Without this, any `D` result would be partly a floor/ceiling artefact.

### 2.5 The dispute-marker channel (DISPUTE)

A second, content-bearing channel: the classical formulae by which a mufassir signals that
the tradition holds more than one position. Locked marker set, matched **after** Arabic
normalisation (strip all Unicode combining marks; `أ إ آ ٱ → ا`; `ى → ي`; `ة → ه`;
`ؤ → و`; `ئ → ي`), on words extracted by `[ء-ي]+`, with a single leading `و` or
`ف` stripped before comparison:

- **Unigrams:** `اختلف`, `اختلفوا`, `اختلفت`, `اختلاف`, `الاختلاف`, `قيل`, `قولان`,
  `القولان`, `قولين`, `اقوال`, `الاقوال`, `وجهان`, `الوجهان`, `وجهين`, `مذهبان`
- **Bigrams** (adjacent normalised words): `قال اخرون`, `قال بعضهم`, `قالت طايفه`, `قال قوم`

Exact whole-word matching is required, which is why the list is given in normalised form and
why word extraction precedes matching: substring matching would count `ثقيل` (*thaqīl*,
"heavy") as `قيل` (*qīla*). The marker count per verse block is amortised by *g* exactly as
length is (§2.2), then rank-normalised within edition (§2.3).

**Edition eligibility gate, locked:** an edition contributes to DISPUTE only if **≥5% of its
6,236 verses carry ≥1 marker**. Editions below the gate are near-constant at zero, contribute
only ties, and would dilute the aggregate. The gate is applied by the script at runtime; the
qualifying set is reported, not chosen by hand.

`DISPUTE(v) = mean_e r_marker(e,v)` over qualifying Arabic editions.

---

## 3. H2 — residualisation. **This is the whole test.**

Commentary length tracks verse length and mundane lexical difficulty. If the H3 effect
lives only in the raw score and vanishes in the residual, **that is a NULL and it is
published as the headline result.** The raw-score version of every H3 statistic is computed
and reported as a **diagnostic only** and is explicitly non-confirmatory.

### 3.1 Covariates (verse level)

1. `len_char` — code points of the verse in `quran-text/quran-no-tashkeel.json`,
   whitespace-collapsed.
2. `len_word` — whitespace-delimited token count of the same.
3. `n_hapax` — number of tokens in the verse whose QAC `ROOT` field is a **corpus hapax
   root** (root attested exactly once across all root-bearing tokens in QAC v0.4). The root
   inventory and hapax set are recomputed from
   `data/morphology/quranic-corpus-morphology-0.4.txt`, matching the census method of
   H-NEW-2320 (395 hapax roots of 1,642 distinct roots over 49,968 root-bearing tokens);
   the script asserts these four totals and aborts on mismatch, which makes the hapax
   instrument independently verified against a prior committed finding.
4. `rarity` — mean over the verse's root-bearing tokens of `−log2(corpus_root_frequency)`;
   0 if the verse has no root-bearing token. This is the general rare-word burden, of which
   hapax count is only the extreme tail.

### 3.2 Residualisation procedure

All variables (outcome and covariates) are converted to **van der Waerden normal scores**:
`z_i = Φ⁻¹(mid_rank_i / (n+1))`, mid-ranks for ties. This keeps the analysis rank-based
(monotone-invariant, no dependence on the raw length distribution's heavy tail) while
permitting ordinary least squares. Then:

- `A_resid` = OLS residual of `z(A)` on `[1, z(len_char), z(len_word), z(n_hapax), z(rarity)]`
- `D_resid` = OLS residual of `z(D)` on `[1, z(len_char), z(len_word), z(n_hapax), z(rarity), z(A), z(A)²]`
- `DISPUTE_resid` = OLS residual of `z(DISPUTE)` on the same design as `A_resid`

Fitted over all 6,236 verses. Solved by normal equations with Gaussian elimination
(stdlib only, per Protocol §7.1).

### 3.3 Reported H2 quantities

R² of each residualisation, and the Spearman ρ of each raw score with each covariate. If
R²(A) is very high the residual is thin and the H3 tests are correspondingly low-powered;
that is reported, not hidden.

---

## 4. H3 — the registered inferences

### 4.1 Cross-level structure

The structural instruments are **per-surah** (114 values); the exegetical scores are
**per-verse** (6,236 values). Verses within a surah are not independent, so no verse-level
test is run. **Locked: aggregate to the surah, test at the surah.**

`R_s` = **median** over the verses of surah *s* of the verse-level residual (median, not
mean: rank-based statistics only, per the standing constraint).

### 4.2 The position confound, and the partial

Commentary volume declines through the mushaf, and surah number is correlated with both
structural instruments (the top-UAS surahs are low-numbered). A bare correlation would be
confounded by mushaf position. **Locked primary statistic: partial Spearman**

> `ρ_partial(R_s, S_s | rank(s), rank(total tokens in surah s))`

computed as: normal-score both `R_s` and `S_s`, OLS-residualise each on
`[1, z(rank of surah number), z(rank of surah token count)]`, then Pearson correlation of
the two residual vectors over the 114 surahs. The bare (unpartialled) Spearman is reported
alongside as a diagnostic only.

### 4.3 Structural variables

- `S590(s) = |delta_pct|` from `csv/h-new-590.json` → `all_surahs_results`. Absolute value,
  matching the `abs_outlier` construction that H-NEW-840 itself uses — extremeness in either
  direction (strong outlier *or* cohesion anchor).
- `S840(s) = UAS` from `csv/h-new-840.json` → `all_uas`.

### 4.4 The six registered inferences and their locked direction

| # | Outcome | Structural | Locked direction |
|:-:|:--|:--|:--|
| I1 | `A_resid` | `S590` | **positive** |
| I2 | `A_resid` | `S840` | **positive** |
| I3 | `D_resid` | `S590` | **positive** |
| I4 | `D_resid` | `S840` | **positive** |
| I5 | `DISPUTE_resid` | `S590` | **positive** |
| I6 | `DISPUTE_resid` | `S840` | **positive** |

**Why positive, argued before computing.** The only mechanism I can articulate linking
distributional structural extremeness to exegetical behaviour runs positive: a surah whose
root-distribution departs sharply from its mushaf neighbourhood is lexically and thematically
distinctive; distinctive material invites glossing, and glossing invites disagreement. I can
articulate **no** mechanism for a negative relation — nothing makes exegetes systematically
*avoid* structurally extreme material. Note that this same mechanism is a lexical-difficulty
pathway, and §3 is built to remove exactly that pathway. **My honest prior is therefore that
all six come back NULL after residualisation**, and locking positive is what prevents a
negative outcome from being re-read as a discovery. A negative significant result is a
pre-commit violation under §1.8 of the Investigation Protocol and will be published as such.

### 4.5 Null and gate

- **Null:** permute `S_s` across the 114 surahs; recompute the *entire* partial-correlation
  pipeline (including re-residualisation on the nuisance ranks) on each permutation.
  10,000 permutations. Seed **20260509** for I1, and `20260509 + i` for inference *i*
  (I1…I6 → 20260509…20260514), each a fixed literal in the script.
- **p:** one-sided upper tail, `p = (1 + #{null ≥ observed}) / (1 + n_perm)`.
- **Bonferroni:** k = 6, **α = 0.05 / 6 = 0.00833333**.
- **Verdict rule:** an inference is CONFIRMED only if `p < 0.00833333` **and** the observed
  partial is positive. Positive-but-not-significant → NULL. Negative and significant
  two-sided → **PRE-COMMIT VIOLATION**, published with full prominence.
- **Family verdict:** if zero of six pass, H3 is reported as **NULL** and that is the
  headline of the findings file, with the H4 roster as the deliverable.

---

## 5. H4 — rosters (descriptive; no inference, no p-values)

Produced regardless of H3's outcome.

- **Roster A — most exegetically contested.** Top 30 verses by `D_resid` (cross-edition
  disagreement in attention, residualised). Reported with each verse's `A_resid`,
  `DISPUTE_resid`, the 8 per-edition ranks, verse length and hapax count.
- **Roster A′ — most disputed by marker.** Top 30 verses by `DISPUTE_resid`. Included
  because it is the channel that actually addresses exegetical *content*.
- **Roster B — structurally extreme, exegetically ignored.** Locked rule: restrict to verses
  in the **top quartile of surahs by `S590`** (28 surahs of 114 — the 114/4 = 28.5 boundary
  is rounded **down** to 28, locked here); within that restriction, the **30 verses with the
  lowest `A_resid`**. Ties broken by ascending surah, then ascending verse.
- **Roster B′ — same, using `S840` (UAS) top quartile.**

Rosters are output to the run directory and to `csv/h-new-2620.json`.

---

## 6. Registered sensitivities (non-confirmatory; reported whatever they show)

1. **Classical-only.** Recompute `A`, `D`, `DISPUTE` and all six inferences over the five
   pre-modern Arabic editions (#1–#5) only. Reported as a separate block. Not part of the
   Bonferroni family; no CONFIRMED verdict may be issued from it.
2. **Raw (un-amortised) length.** All of §2.4 without the `/g` amortisation.
3. **Token-count length** instead of character count.
4. **Mean instead of median** for the surah aggregation `R_s`.
5. **English set (4 editions).** Full pipeline, reported separately, with the 92%/70%
   block-coverage caveat attached. Registered as a weak replication channel.
6. **Leave-one-surah-out** stability of the primary partial for I1 and I3: min/max over the
   114 refits.
7. **Leave-one-edition-out** stability of `A` and the I1 partial: 8 refits.
8. **Positive control (MW-6).** Spearman ρ(raw `A`, `len_char`) over 6,236 verses. If the
   instrument works at all this must be strongly positive; if it is not, the instrument is
   broken and the run is reported as instrument-failure.
9. **Coverage report.** Per-edition verse coverage of the 6,236, empty and short-text counts,
   block-group statistics, and marker-eligibility — printed to the run directory.

---

## 7. Abort conditions (fail-fast)

The run aborts, with no results written, if any of:

1. This file's SHA-256 ≠ the literal embedded in `scripts/h-new-2620.py`.
2. The manifest's SHA-256 ≠ `2ce03c91087fad7a357c130a496e2557a07dd6a6a1b6e8df8e8b7d15cf1bcff6`.
3. Any tafsīr file read is absent from the manifest, or its SHA-256 differs from the recorded one.
4. Any of the four §1.2 inputs fails its SHA-256.
5. Any of the 8 primary Arabic editions does not supply exactly 6,236 verse files
   (surahs 1–114, verse numbering matching `quran-no-tashkeel.json`).
6. `h-new-590.json` `all_surahs_results` or `h-new-840.json` `all_uas` does not cover all 114 surahs.
7. The QAC hapax census does not reproduce H-NEW-2320's four totals
   (49,968 root-bearing tokens; 1,642 distinct roots; 395 hapax roots; hapax fraction 24.1%).

---

## 8. Run discipline

- Output directory: `findings/phase-b-hypotheses/runs/h-new-2620/<UTC timestamp>/`,
  created fresh per execution.
- **Nothing in any run directory may be overwritten, and no run directory may ever be
  deleted — including an uncommitted or superseded one.** This is the standing correction
  recorded at H-NEW-2540 §8.1. A run that must be re-executed produces an *additional*
  directory; both are retained and the reason is recorded in the findings file.
- Each run writes `manifest.json` (UTC timestamp, python version, platform, all verified
  input hashes, the script's own SHA-256, and the seed schedule), `result.json`,
  `coverage.tsv`, `verse-scores.tsv`, and the four rosters.
- Every seed is a fixed integer literal in the script. No wall-clock or entropy seeding.

---

## 9. Scope of any claim this test can support

Whatever the outcome, the following are **not** claimed and the findings file must say so:

1. **The edition set is not a sample of the exegetical tradition.** It is what one public
   API happened to carry. Five pre-modern Arabic tafsīrs and three modern ones is not a
   stratified sample of a genre with hundreds of members; al-Rāzī, al-Zamakhsharī, al-Ṭabarsī,
   al-Biqāʿī, al-Thaʿlabī and al-Suyūṭī's *al-Durr al-manthūr* are all present elsewhere in
   this repository and all absent here.
2. **Length is a proxy for attention, not for contestation.** A long entry may be a long
   isnād chain, a grammatical excursus, or a repeated pericope, not a controversy.
3. **The structural axis is at surah resolution.** Any verse-level roster entry inherits its
   surah's structural score; it is not a verse-level structural measurement.
4. **Digitisation is an uncontrolled layer.** Text lengths reflect the API's editorial
   choices — which print edition, whether isnāds were retained, whether tashkeel was kept —
   and none of that is recoverable from the files.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any outcome computation.*

*Bismillāhi al-Raḥmāni al-Raḥīm.*
