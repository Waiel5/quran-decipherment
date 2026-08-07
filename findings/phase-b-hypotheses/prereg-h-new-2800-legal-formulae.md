---
title: "Pre-registration — H-NEW-2800: the legal-formula frames, a closed inventory with positional structure"
author: Waiel Al-Shujaa
date: 2026-08-07
status: PRE-REGISTERED — locked before any computation
finding_id: H-NEW-2800
frontier_item: F-15
seed_primary: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 5
alpha_bonferroni: 0.010
---

# Pre-registration — H-NEW-2800

**This file is locked before any statistic is computed.** Its SHA-256 is embedded in
`findings/phase-b-hypotheses/scripts/h-new-2800.py` and verified at runtime with
`SystemExit` on mismatch.

---

## 0. What this test is, and what it is not

The claim under test is that **a small closed set of legal frames accounts for most
legal-register verse onsets, and that those frames occupy characteristic positions within
their surahs**.

Two structural properties of this target are the reason it was chosen and must be stated
first.

1. **It need not be a ratio statistic.** A formula census is a set of exact counts at exact
   locations. A positional test on *relative* position within a surah is a rank statistic
   whose denominator is held identical between observation and null by construction. Where a
   rate is nevertheless used, `findings/UNIT-DRIFT-DEFECT.md` §5 is discharged explicitly in
   §4 below.
2. **The census is the deliverable regardless of what any test says.** A complete, located
   inventory of a closed formula set has standing descriptive value. Every registered
   inference below may fail and the census still publishes.

---

## 1. The two defects declared before computing

### 1.1 The register label is defined by two of the frames — declared circularity

I was directed to reuse the register labels verbatim from
`findings/phase-b-hypotheses/csv/h-new-2530.json`. That file does not carry the labels
itself; its `genre_proxy_source` field reads
`"h-new-2500.json genre_proxy.surah_genre (reused verbatim)"`. Following that pointer,
`findings/phase-b-hypotheses/csv/h-new-2500.json` → `genre_proxy.decision_procedure` reads:

```
1 legal_medinan: medinan AND (O-believers + kutiba-alaykum)>=1
2 narrative: qala-density>=1.0/100w
3 eschatological_mufassal: s>=78 OR eschat-density>=1.5/100w
4 liturgical_didactic: residual
```

and `genre_proxy.legal_markers` reads `["يا أيها الذين آمنوا", "كتب عليكم"]`.

**The `legal_medinan` label is therefore assigned to a surah *because* it contains
`kutiba ʿalaykum` or `yā ayyuhā alladhīna āmanū` — two of the frames in the inventory under
test.** Every `legal_medinan` surah contains at least one of them **by construction**. This
is a definitional guarantee, not a finding, and it is declared here before any count is
taken.

Consequences, locked:

- The **presence** half of the claim is not testable against this label at all.
- Every register-dependent inference is computed twice: on the **full** locked inventory
  (contaminated; reported for completeness) and on the **purged** inventory
  = locked inventory **minus** {A1 `kutiba ʿalaykum`, B2 `yā ayyuhā alladhīna āmanū`}. **The
  purged number is the inference of record.**
- The **positional** inferences (H3, H4) are *not* contaminated in the same way, and the
  reason is stated in §5.3: the label rule constrains *presence per surah*, never *position
  within a surah*, and the within-surah permutation null holds per-surah counts fixed, which
  absorbs the conditioning entirely. H3/H4 therefore run on the full inventory, corpus-wide,
  and do not use the register labels at all.

### 1.2 al-Zarkashī's *al-Burhān* cannot be cited from disk — data gap

`data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf` is on disk
(29,545,336 bytes) but `pdfinfo` reports
`Producer: Adobe Acrobat 7.05 Image Conversion Plug-in` and `pdftotext -layout` returns a
1,568-byte file with **zero lines of text**. It is an image-only scan with no text layer and
no OCR on disk.

**No page of al-Zarkashī will be cited in this finding.** The project has a documented
history of unverifiable *nawʿ* numbers for exactly this work — `classical-iltifat-catalog.md`
line 15, `classical-quantitative-claims-audit.md` line 159 and
`abjad-residue-fasila-mechanism.md` line 10 all carry `nawʿ PENDING` retraction markers. A
fourth is not being added. The classical anchor used instead is verified line-by-line in §2.

---

## 2. Classical anchor — verified on disk

**Primary anchor.** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, **nawʿ 65**
(`النوع الخامس والستون: في العلوم المستنبطة من القرآن`), ed. Muḥammad Abū al-Faḍl Ibrāhīm,
1394 AH / 1974 CE, **vol. 4 pp. 39–40**.

File: `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`
(OpenITI/Shamela_0011728; `#META# 040.EdEDITOR :: محمد أبو الفضل إبراهيم`;
`#META# 041.EdNUMBER :: 1394هـ/ 1974 م`).
Locations: nawʿ heading at line **20725**; page markers `# PageV04P039` and `# PageV04P040`.

Two passages are load-bearing.

**(a) The size of the legal-verse set (line 20976, vol. 4 p. 39):**

> قال الغزالي وغيره: آيات الأحكام خمسمائة آية وقال بعضهم مائة وخمسون قيل ولعل مرادهم المصرح
> به فإن آيات القصص والأمثال وغيرها يستنبط منها كثير من الأحكام.

*"al-Ghazālī and others said: the āyāt al-aḥkām are five hundred verses; some said a hundred
and fifty. It is said: perhaps they meant the explicitly stated ones, since much law is
derived from the verses of narrative, parable and the rest."*

This supplies a **classical prior on the denominator**: 500 explicit legal verses out of
6,236 is 8.0 %; 150 is 2.4 %. Both are reported against the measured closure.

**(b) The frames themselves (vol. 4 p. 40), quoting ʿIzz al-Dīn b. ʿAbd al-Salām,
*Kitāb al-Imām fī adillat al-aḥkām*:**

> قال: ويستدل على الأحكام تارة بالصيغة وهو ظاهر وتارة **بالإخبار** مثل **{أحل لكم}**
> **{حرمت عليكم الميتة}** ، **{كتب عليكم الصيام}**

*"He said: rulings are inferred sometimes from the **form** (ṣīgha) — which is obvious — and
sometimes from **declarative statement** (ikhbār), such as {uḥilla lakum}, {ḥurrimat ʿalaykum
al-mayta}, {kutiba ʿalaykum al-ṣiyām}."*

**This is an independent classical source for the frame list.** A 7th/13th-century jurist
enumerates exactly three declarative legal frames, and all three are in the inventory below.
F-15's own confound note demanded precisely this — *"Frame list selection is post-hoc unless
drawn from an independent source"* — and this discharges it for Class A. The frames are not
analyst-chosen; they are Ibn ʿAbd al-Salām's own enumeration of the *ikhbār* mode.

**Secondary witness.** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*,
`data/literature/classical-tafsir/raw/qurtubi-jami-ahkam.openiti.raw.txt` — the canonical
*āyāt al-aḥkām* commentary, 20,485,460 bytes on disk. The three Class-A strings occur 90
times in it as objects of legal discussion. This is recorded as corroboration of genre, not
as a measurement.

---

## 3. Rules-tuple and frozen inputs

**Rules-tuple:**
`(no-tashkeel for surface display; QAC v0.4 morphological feature strings as the ONLY matching
layer — never raw substring matching; orthographic-word for word indices; verse as the unit;
basmala-counted-only-in-Q1; Hafs-Kufan; Mashriqi)`

**Substring matching on Arabic is forbidden by standing project rule and is not used anywhere
in this test.** Every frame is specified as a conjunction of QAC feature-string predicates
over consecutive orthographic words, and the exact predicate strings are reported in the
finding.

**Frozen inputs, SHA-256 recorded in the run manifest with repo-relative paths:**

- `data/morphology/quranic-corpus-morphology-0.4.txt`
- `quran-text/quran-no-tashkeel.json`
- `findings/phase-b-hypotheses/csv/h-new-2530.json`
- `findings/phase-b-hypotheses/csv/h-new-2500.json`
- `data/baseline-corpora/raw/bukhari-noquran.txt`
- `data/revelation-order.csv`
- `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`

Run directory: `findings/phase-b-hypotheses/runs/h-new-2800/<UTC-stamp>/`, immutable, with
`manifest.json` carrying repo-relative paths. **No run directory is ever deleted.**

---

## 4. Unit-drift declaration (UNIT-DRIFT-DEFECT.md §5, discharged in full)

**§5.1 — what the denominator is, as a quantity.** The closure statistic's denominator is the
**number of verse onsets**, which equals the number of verses. It is a count of
*opportunities*, not of size: a verse presents exactly **one** onset whether it is 3 words
long or 130. Lengthening a verse does not create a second onset.

**§5.2 — the drift of that denominator across the ordering under test, measured on the data.**
Not asserted. The run computes and reports, before any inference:

- mean verse length (words) for each of the four register classes;
- Spearman ρ(register-class ordinal ranked by mean verse length, mean verse length);
- Spearman ρ(surah verse count, register indicator for `legal_medinan`);
- for every frame, the per-1000-**word** rate alongside the per-onset rate, so the reader can
  see both normalisations.

The `legal_medinan` surahs are known to be long; that is not a reason to trust the per-onset
statistic without measurement, and the measurement is reported whatever it shows.

**§5.3 — which null holds unit size fixed.**

- **H2** — register-label permutation **stratified within surah verse-count quintiles**. This
  is H-NEW-2760's device and is a Screen-C-qualifying control: the permuted labels carry the
  same verse-count profile as the observed ones by construction.
- **H3, H4** — **within-surah** permutation. Relative position is defined
  `rel(i) = (i − 0.5) / n_verses` for 1-based verse index `i`. Its expectation under a uniform
  draw is exactly **0.5 for every n**, so the statistic is scale-free by construction; and
  because the permutation is *within* a surah, the observed and permuted values share the
  **identical** denominator `n_verses`. Verse-count drift cannot act on this comparison — not
  because normalisation was assumed to confer invariance (STATE §4.8 forbids that assumption),
  but because the denominator is literally the same number on both sides of the comparison.
  The run verifies `E[rel] = 0.5` numerically on the permutation draws and reports the value.
- **H5, H6** — matched partition: the baseline arm's verse word-length profile and per-surah
  verse-count profile are **identical to this corpus's by construction** (H-NEW-2680's
  `build_pseudo_corpus`).

**§5.4 — the strongest channel, ranked on the data before locking.** Per UNIT-DRIFT-DEFECT §5
clause 1, the run measures both candidate nuisance channels (surah verse count; surah mean
verse length) against the `legal_medinan` indicator *and reports both*, and H2's stratifier is
locked here to **verse count**, on the stated ground that the closure denominator is the verse
count itself. If mean verse length turns out to be the stronger channel, the run also reports
H2 stratified on mean-verse-length quintiles as a declared secondary, and **both numbers are
published** — H-NEW-2760's failure mode is not repeated by silence.

---

## 5. The locked frame inventory

**No frame is removed for any reason, including a count of zero.** Removing a low-count frame
after seeing its count is the selection channel this pre-registration exists to close. Every
frame below is reported with its exact count, zero included.

Notation: `w` is an orthographic word index within a verse; a *word* is the set of QAC
segments sharing `(surah:verse:word)`. A predicate on a word is satisfied if **any** of its
segments satisfies it. `2P` means any segment carrying `PRON:2MP|2MS|2FS|2FP|2MD|2FD` (SUFFIX
form) or `POS:PRON` together with one of those person-number fields (STEM form) — both
encodings are attested in QAC and both are accepted.

**Onset normalisation, locked:** a frame is *at the onset* of a verse if it begins at word 1
after skipping any leading conjunction/resumption prefix segments (`w:CONJ+`, `w:REM+`,
`f:CONJ+`, `f:REM+`, `f:RSLT+`, `f:CAUS+`, `f:SUP+`, `w:CIRC+`, `w:SUP+`). This is a
mechanical orthographic normalisation — Arabic writes these as bound prefixes — and it is
declared before counting. The strict no-strip variant is reported as robustness.

### Class A — the classical *ikhbār* frames
*Source: ʿIzz al-Dīn b. ʿAbd al-Salām via al-Suyūṭī, Itqān nawʿ 65, vol. 4 p. 40 (§2b above).*

| id | frame | QAC predicate |
|:--|:--|:--|
| **A1** | *kutiba ʿalaykum* | word `w`: `POS:V` ∧ `PERF` ∧ `PASS` ∧ `ROOT:ktb`; word `w+1`: (`POS:P` ∧ `LEM:EalaY`) ∧ `2P` |
| **A2** | *ḥurrimat ʿalaykum* | word `w`: `POS:V` ∧ `PERF` ∧ `PASS` ∧ `ROOT:Hrm`; word `w+1`: (`POS:P` ∧ `LEM:EalaY`) ∧ `2P` |
| **A3** | *uḥilla lakum* | word `w`: `POS:V` ∧ `PERF` ∧ `PASS` ∧ `ROOT:Hll`; word `w+1`: (`l:P+` ∨ (`POS:P` ∧ `LEM:li`)) ∧ `2P` |

### Class B — the frontier-map frames
*Source: `HANDOFF/FRONTIER-MAP-2026-08-07.md` item F-15 line 284, plus the dispatch brief.
Both were written before this pre-registration and neither was authored during it.*

| id | frame | QAC predicate |
|:--|:--|:--|
| **B1** | *fa-man lam yajid* | word `w`: `POS:COND` ∧ `LEM:man`; word `w+1`: `POS:NEG` ∧ `LEM:lam`; word `w+2`: `POS:V` ∧ `IMPF` ∧ `ROOT:wjd` |
| **B2** | *yā ayyuhā alladhīna āmanū* | word `w`: `LEM:>ay~uhaA`; word `w+1`: `POS:REL` ∧ `LEM:{l~a*iY`; word `w+2`: `POS:V` ∧ `PERF` ∧ `ROOT:Amn` |
| **B3** | *wa-lakum fī … ḥayāt* | word `w`: `w:`-prefix ∧ (`l:P+` ∨ `LEM:li`) ∧ `2P`; word `w+1`: `POS:P` ∧ `LEM:fiY`; and some segment with `POS:N` ∧ `ROOT:Hyy` in words `w+2 … w+4` |

### Class G — generative structural rules
*Declared as rules, not as lists, so they cannot be tuned after seeing counts. Each is a
proper superset of a Class-A or Class-B frame. Reported separately and never merged into
Class A ∪ B without a label.*

| id | rule | QAC predicate |
|:--|:--|:--|
| **G1** | the *ikhbār* template generalised | word `w`: `POS:V` ∧ `PERF` ∧ `PASS`; word `w+1`: ((`POS:P` ∧ `LEM:EalaY`) ∨ `l:P+` ∨ (`POS:P` ∧ `LEM:li`)) ∧ `2P` |
| **G2** | the vocative address generalised | word `w`: `LEM:>ay~uhaA`; word `w+1`: `POS:REL` ∨ `POS:N` |
| **G3** | the conditional protasis | word `w`: `POS:COND` (any lemma) |

**Broadening a generative rule mechanically raises coverage.** G1–G3 are reported so the
reader can see the coverage/precision trade-off explicitly; a high G-class coverage is **not**
evidence for a *closed* inventory and will not be reported as such.

### Exploratory extension — excluded from every registered inference
The 20 most frequent verse-onset bigrams of the `legal_medinan` surahs, reported descriptively
in an appendix and **excluded from H1–H6**. A post-hoc frame list guarantees high coverage and
is worthless as an inference; it is published only so the reader can see what a post-hoc list
would have looked like.

---

## 6. Registered inferences

**Bonferroni family: k = 5** (H2, H3, H4, H5, H6). **α_bonferroni = 0.05 / 5 = 0.010.**
H1 is a descriptive threshold with no p-value and is not counted in k.
10,000 permutations; primary seed **20260509**; replication seed **20260519**.

### H1 — CLOSURE (descriptive, threshold locked)

`closure = (# legal_medinan verse onsets matched by the inventory) / (# legal_medinan verses)`

Locked reading of *"accounts for most legal-register verse onsets"*: **closure ≥ 0.50**.

| closure | label |
|:--|:--|
| ≥ 0.50 | CLOSURE-SUPPORTED |
| 0.20 – 0.50 | CLOSURE-PARTIAL |
| < 0.20 | **CLOSURE-FALSE** |

Reported for: full inventory; purged inventory; Class A alone; Class B alone; Class A ∪ B;
Class G alone; and for each of the four registers, so the legal figure has a within-corpus
reference. Also reported against al-Ghazālī's 500 (8.0 % of 6,236) and the rival 150 (2.4 %).

### H2 — ENRICHMENT of the purged inventory in `legal_medinan`

**Direction locked: POSITIVE.** The purged-inventory onset count in `legal_medinan` surahs
exceeds the null mean.

**Null:** permute the 114 register labels **within surah verse-count quintiles**, 10,000 draws.
Statistic: number of onset-matched verses in the surahs labelled `legal_medinan`.

**PASS** iff `p ≤ 0.010` **and** observed > null mean. Otherwise **FAIL**.

The same test on the **full** inventory is reported alongside and is **explicitly not
evidence**, for the reason in §1.1.

### H3 — POSITION, location

**Direction locked: LATER.** The mean relative position of frame-bearing verses within their
surah is **greater than 0.5**.

Population: **corpus-wide** — every surah containing ≥ 1 occurrence of the full locked
inventory (Classes A ∪ B). Register labels are not used. A verse bearing several frames counts
once per frame type.

Statistic: mean of `rel(i) = (i − 0.5)/n_verses` over all frame-bearing verses.

**Null:** within each surah, permute which verses carry frames, holding the per-surah frame
count fixed. 10,000 draws.

**PASS** iff `p ≤ 0.010` **and** observed mean > 0.5.
**A reversed sign is a pre-commit violation and is published as NULL with full prominence.**

*Direction justification, with the counter-evidence disclosed.* Legal prescription in the
Medinan surahs is characteristically preceded by address, creed or polemic, and the *sabab
al-nuzūl* structure places prescriptive material after a setup; the long Medinan surahs carry
their legal blocks after an opening section. **Disclosed prior familiarity (garden-of-forking-
paths, §8):** I am aware from general reading — not from any computation performed for this
test — that `kutiba ʿalaykum` occurs late in Q 2 and that `ḥurrimat ʿalaykum` / `uḥilla lakum`
occur at the very top of Q 5. These pull in **opposite** directions, so the lock is a genuine
bet and not a foregone conclusion.

Robustness arms (reported, not additional inferences): onset-only occurrences;
`legal_medinan`-only population; purged inventory.

### H4 — POSITION, clustering

**Direction locked: MORE CLUSTERED.** Frame-bearing verses sit closer together within a surah
than a within-surah random placement of the same count.

Statistic: mean of `|i_{j+1} − i_j| / n_verses` over all consecutive pairs of frame-bearing
verses, pooled across all surahs with ≥ 2 such verses.

**Null:** identical within-surah permutation, 10,000 draws.

**PASS** iff `p ≤ 0.010` **and** observed < null mean.

*Direction justification.* The *āyāt al-aḥkām* genre presupposes that legal verses are
locatable as blocks — a book of aḥkām verses is only compilable if they run together. That is
the classical claim's positional content, and it predicts clustering.

### H5 — GENRE CONTROL, arbitrary matched partition of al-Bukhārī

**Bukhārī is the hard case: ḥadīth is legal discourse too.** If its onsets are as formulaic,
the claim is about legal or formulaic Arabic and not about this text.

Method: H-NEW-2680's `build_pseudo_corpus` **reused verbatim** — cut `bukhari-noquran.txt`
into 6,236 pseudo-verses on this corpus's verse word-length profile, group into 114
pseudo-surahs on this corpus's verse-count profile, take the 20 pseudo-surahs occupying the
`legal_medinan` positions. 200 starting offsets.

**Statistic — frame-list-free by design:** **top-8 onset-bigram concentration** = the fraction
of an arm's unit onsets covered by that arm's **own** 8 most frequent onset bigrams (first two
words after the same conjunction-strip). Each corpus gets its own best 8; the baseline is
never forced to use this corpus's frames, which would rig the comparison. k = 8 is locked here
because the locked inventory has 6 named frames and 8 gives it room; the full curve
k ∈ {1,2,4,8,16,32} is reported descriptively. Onset **trigram** concentration is reported as
a robustness variant.

**Direction locked: POSITIVE** — this corpus's `legal_medinan` arm **exceeds** al-Bukhārī's
matched arm. **PASS** iff the one-sided offset p ≤ 0.010.

*Regime declaration (STATE §4.7).* Onset formulaicity is a **boundary-sensitive** statistic.
Arbitrary cuts **destroy** al-Bukhārī's real onsets, so this arm **handicaps the baseline**: a
baseline pass here is **strong** evidence against the claim, and a baseline failure here is
**weak** evidence for it. That is why H6 exists.

### H6 — GENRE CONTROL, al-Bukhārī with its real boundaries

Split the `bukhari-noquran.txt` word stream at isnād openers
(`حدثنا`, `حدثني`, `أخبرنا`, `أخبرني`), **drop the splitting token** so the comparison is not
circular in the splitter, keep units of ≥ 3 words, and subsample to the same unit count as the
`legal_medinan` arm. Same top-8 onset-bigram concentration, 200 subsamples.

**Direction locked: POSITIVE** — this corpus's `legal_medinan` arm exceeds al-Bukhārī's
real-boundary arm. **PASS** iff the one-sided p ≤ 0.010.

*Regime declaration.* This arm gives ḥadīth its **real authored boundaries** and therefore
deliberately handicaps **this corpus**. A baseline pass here is strong evidence against the
claim. Both regimes are run because neither alone settles it.

### Replication
H2, H3, H4 re-run at seed **20260519**; H5, H6 re-run with a different offset/subsample grid
seed. A registered inference is **replicated** only if its PASS/FAIL verdict is unchanged.

---

## 7. Verdict rule — LOCKED

Evaluated on the **purged** inventory for H1 and H2, and the full inventory for H3–H6, exactly
as specified above. The run script implements this rule literally and prints a side-by-side
diff of the computed verdict against this section.

```
CLOSED-INVENTORY-WITH-POSITION  iff  H1_purged >= 0.50
                                AND  H2 PASS
                                AND  (H3 PASS OR H4 PASS)
                                AND  H5 PASS AND H6 PASS

POSITIONED-BUT-NOT-CLOSED       iff  H1_purged < 0.50
                                AND  H2 PASS
                                AND  (H3 PASS OR H4 PASS)

GENRE-SHARED                    iff  H2 PASS
                                AND  (H3 PASS OR H4 PASS)
                                AND  (H5 FAIL OR H6 FAIL)

NULL                            iff  H2 FAIL
```

Precedence, locked: `CLOSED-INVENTORY-WITH-POSITION` > `GENRE-SHARED` >
`POSITIONED-BUT-NOT-CLOSED` > `NULL`. A verdict is **not** upgraded by any unregistered
statistic. **A clean descriptive census plus a NULL is a fully acceptable outcome and the
census publishes in every branch.**

---

## 8. Garden-of-forking-paths log — written before the run

Every methodological decision taken while writing this file, and everything I looked at.

1. **QAC format probes.** Before writing the predicates in §5 I inspected the QAC segment
   encoding of Q 2:178, 2:179, 2:180, 2:183, 2:187, 2:196, 5:3, 5:5, and enumerated QAC's POS
   tag inventory, its `PRON` feature shapes, and its `f:` / `w:` / `l:` prefix vocabulary.
   These probes fixed the *spelling* of the predicates. They could not select the frame list,
   because the frame list is externally fixed (§5) and §5 forbids dropping any frame.
2. **One count was seen during probing.** The probe that validated B1's predicate returned its
   three locations — Q 2:196 w45, Q 4:92 w48, Q 5:89 w26, all mid-verse. This is disclosed
   because it is the one census figure known to me before the run. It cannot have influenced
   the inventory (B1 stays regardless) or any direction lock (H3/H4 are corpus-wide over
   A ∪ B; three mid-verse tokens do not determine the mean).
3. **Register labels.** I did not derive them. I followed `h-new-2530.json`'s own
   `genre_proxy_source` pointer to `h-new-2500.json` and read the decision procedure, which is
   how the circularity in §1.1 was found. Reading the label's definition before using it is a
   requirement, not a forking path.
4. **Classical anchor substitution.** al-Zarkashī was the anchor named in the dispatch; his PDF
   has no text layer (§1.2), so al-Suyūṭī *Itqān* nawʿ 65 was substituted. I searched the
   *Itqān* raw for `آيات الأحكام` / `خمسمائة` and read the surrounding passage. The
   Ibn ʿAbd al-Salām quotation naming three of the frames was found **after** the frame list
   was already fixed by F-15 and the dispatch brief — it corroborates a list I did not choose,
   and it did not add or remove a frame.
5. **H2 stratifier.** Locked to **verse count** on the stated ground that the closure
   denominator *is* the verse count. Mean verse length is also measured and H2 is additionally
   reported stratified on it (§4.4). Both are published whichever is stronger.
6. **k = 8 in H5/H6.** Locked from the inventory size (6 named frames), before any
   concentration was computed. The full k-curve is reported so the choice is auditable.
7. **What I have not computed.** No closure fraction, no enrichment, no positional mean, no
   concentration, and no Bukhārī statistic of any kind has been computed at the time this file
   is sealed.

---

## 9. Honest limits, stated in advance

1. **The register label is coarse and circular.** It is a *surah*-level label, so the closure
   denominator includes every verse of Q 2, Q 4, Q 5, Q 9 — narrative, polemic and creed
   alike. A low closure fraction is therefore partly a statement about the denominator's
   dilution, not only about the frames. And per §1.1 the label was assigned using two of the
   frames. Both facts bound H1 and H2 and neither is repairable within the instruction to
   reuse the labels verbatim.
2. **A partition is not a composed book.** H5's pseudo-surahs are arbitrary cuts of a
   continuous stream. §6 declares the regime for each control arm rather than using the caveat
   as a blanket excuse.
3. **`bukhari-noquran.txt` is a single 4.6 MB line** with no preserved unit boundaries; H6
   recovers boundaries from isnād openers, which is a reconstruction and not the editor's own
   segmentation.
4. **One baseline genre.** al-Jāḥiẓ and the dīwāns are not run here: adab prose and pre-Islamic
   poetry are not legal discourse, so they cannot answer the question H5/H6 asks. The
   consequence is that this test can distinguish this corpus from **ḥadīth** and from nothing
   else.
5. **QAC annotation is an instrument.** Every count inherits QAC v0.4's morphological
   decisions. There is no second Arabic morphological annotation of this corpus on disk to
   cross-check against.
6. **The Class-G rules are supersets by construction.** Their higher coverage is arithmetic,
   not evidence.

---

*Sealed 2026-08-07 by Waiel Al-Shujaa before any statistic was computed. Bismillāhi
al-Raḥmāni al-Raḥīm.*
