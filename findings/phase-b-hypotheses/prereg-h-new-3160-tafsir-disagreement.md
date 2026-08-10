---
id: H-NEW-3160
title: Pre-registration — per-verse cross-edition exegetical divergence against the per-verse structural profile
date: 2026-08-09
author: Waiel Al-Shujaa
status: PRE-REGISTRATION — locked before any outcome-to-predictor association was computed
parent: H-NEW-2620 (surah-level, NULL 0/6); H-NEW-2990 (the per-verse instrument this test requires)
family: TAFSIR-2026-08-09-A
bonferroni_k: 3
alpha_bonferroni: 0.01666667
seed: 20260509
permutations: 10000
rules_tuple: (no-tashkeel for verse text, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Pre-registration — H-NEW-3160

## §0. Prior-work check, run BEFORE any design work

This section exists because `HANDOFF/FRONTIER-MAP-2026-08-07.md`'s binding rule requires the
check that determines *whether to run at all* to precede the checks about *how to run*, and
because H-NEW-3010's forking-paths log had sixteen entries about instrument choices and not one
asking whether the work already existed.

**Greps run:** `tafsir disagreement`, `contested verse`, `exegetical divergence`,
`commentary length`, `twelve edition`, `12-edition`, `per-verse tafsir`, `2620`, `3160`,
`spa5k-tafsir-api`, `2990-verse-profile`, over `findings/` and `MASTER-FINDINGS-LEDGER.md`.

**Result: F-11 is PARTLY ANSWERED. H-NEW-2620 is its direct parent and returned a NULL.**

H-NEW-2620 (2026-08-07) built three channels over the eight Arabic editions and tested six
inferences — {ATTENTION, DISAGREEMENT, DISPUTE}_resid × {S590, S840} — as **partial Spearman
correlations across the 114 SURAHS**, controlling mushaf position and log surah token count.
**Zero of six passed.** Bare ρ(ATTENTION, S590) = +0.3045 collapsed to −0.1793 once length and
lexical difficulty were residualised; ρ(ATTENTION, verse length) = **+0.787**; length and
difficulty absorbed **R² = 0.6112** of ATTENTION.

**What H-NEW-2620 explicitly left undone — its §9 limit 4, quoted verbatim:**

> *"The structural axis is at surah resolution; the exegetical axis at verse resolution. Every
> roster entry inherits its surah's structural score. **There is no verse-level structural
> measurement here, and building one is a separate piece of work.**"*

**That separate work now exists and did not on 2026-08-07.** H-NEW-2990 (2026-08-08) published
`csv/h-new-2990-verse-profile.csv` — 6,236 verses × 33 columns, each computed from the verse
itself and never inherited from its surah — together with
`csv/h-new-2990-column-declarations.csv`, which gives every column its correlation against word
count, letter count and mushaf position, and flags **only 2 of 33 as length-dominated**.

**Verified un-run.** `grep -rl spa5k-tafsir-api scripts/ findings/phase-b-hypotheses/scripts/`
returns three scripts (`Q058_F_03_najwa_abrogation.py`, `h-new-2620.py`, `h-new-3120.py`);
`grep -rl 2990-verse-profile` returns eight files. **The two sets are disjoint.** H-NEW-3000
joined the verse profile to *ḥadīth* reception, not to tafsīr. No script in this repository has
ever joined the tafsīr corpus to a per-verse structural measurement.

**Conclusion: the verse-level form of F-11 is open, and it is the form F-11 actually states**
(*"verses where the tradition splits are structurally distinguishable from verses where it does
not"* — a verse-level claim). The surah-level form is answered and this pre-registration does
not re-litigate it.

**This pre-registration is NOT blind.** H-NEW-2620 is published, I have read it in full, and I
inherit its marker set and its amortisation rule deliberately. Concealing that would be worse
than the non-blindness. §0.3 records exactly what was known before the lock.

### §0.1 Instrument audit performed before locking — the three brief warnings

**Warning 1, truncation — DISCHARGED.** Full census computed
(`scratchpad/coverage_audit.py`): all **twelve tafsīr editions carry 114 surah directories, 228
top-level entries, 6,236 verse files, and 6,236 non-empty texts.** Per-verse coverage across the
twelve is a **single point mass at 12**: 6,236 / 6,236 = **100.00%** of verses have a comment in
**all twelve**; **zero** verses have a comment in only one; **zero** in none. Cross-edition
dispersion in this tree cannot be manufactured by uneven coverage.

`en-asbab-al-nuzul-by-al-wahidi` is confirmed truncated — **152 top-level entries against the
siblings' 228**, 1,089 verses, 75 surah directories, and **39 surahs with no verse directory at
all: 78-114 continuous, plus 72 and 77.** It is not a tafsīr, was excluded by H-NEW-2620 before
any computation, and is **not used here**.

**Warning 2, misattribution — AUDITED FOR ALL THIRTEEN AND INDEPENDENTLY REPRODUCED.** The
death-date test was already applied to every directory by H-NEW-2970 and published at
`findings/PROXY-CLAIMS.md`. I re-ran it rather than trust it. Load-bearing results reproduced,
and the decisive one is stronger than the record: **`ar-tafseer-tanwir-al-miqbas` signs its own
colophon** — at Q 2:271 «وقال الشيخ **ابن عاشور جدي**» (*"Shaykh Ibn ʿĀshūr, my grandfather"*),
and at Q 114:6, the last verse of the book, «يقول **محمد الطاهر ابن عاشور**: قد وفيت بما نويت».
Ibn ʿAbbās (d. 68 AH) cannot sign a book as Muḥammad al-Ṭāhir Ibn ʿĀshūr (d. 1393 AH / 1973 CE).

**Verified composition of the "twelve", which the hypothesis as briefed misstates:**

| stratum | editions | count |
|:--|:--|--:|
| pre-modern Arabic | al-Ṭabarī (310), al-Baghawī (516), al-Qurṭubī (671), Ibn Kathīr (774) | **4** |
| modern Arabic | al-Saʿdī (1376/1956), **Ibn ʿĀshūr (1393/1973)**, al-Wasīṭ (20th c.), al-Muyassar (King Fahd committee, 2007) | **4** |
| English | al-Jalālayn (864/911), Ibn Kathīr abridged (**duplicate of the Arabic edition**), Tanwīr al-Miqbās (ascribed 68), Maʿārif al-Qurʾān (Shafīʿ, 1396/1976) | **4** |

**At most 11 distinct works; half the Arabic set is 20th-century; one is a 2007 committee
paraphrase.** "Twelve tafsīr traditions" is not a description this corpus supports, and no claim
in this pre-registration uses that phrase. **H-NEW-2620's "classical-only (5 pre-modern)"
sensitivity row is four pre-modern editions plus one from 1973** — an error that finding itself
flags. §7.1 below runs that sensitivity correctly for the first time.

**The death-date test's own failure mode, found by applying it.** Three of my probes produced
confident false positives at scale, caught only by reading contexts:
- al-Qurṭubī (d. 671) appeared to cite **"ابن كثير" ×292** — impossible. Every hit is a *qirāʾa*
  citation («قراءة ابن كثير», «وقرأ نافع وابن كثير وأبو عمرو»): this is **ʿAbdallāh ibn Kathīr
  al-Makkī, one of the seven canonical readers (d. 120 AH)**, a different man. al-Qurṭubī is clean.
- al-Baghawī and Ibn Kathīr appeared to cite **"محمد عبده"** — both hits are the shahāda formula
  «ومحمدٌ **عبدُه** ورسولُه» at Q 85:22. Ordinary Arabic, not a name. Both clean.
- al-Ṭabarī's single "رشيد رضا" hit is **Aḥmad Shākir's modern editorial apparatus**, a footnote.

**Recorded as a standing caution: a raw hit count is not evidence; a read context is.** A name
that is also an ordinary Arabic phrase, or that is shared with an earlier man in a different
discipline, produces a false accusation at ×292, not ×1.

**Warning 3, length — this design is built around it.** See §4 and §6.2. All three length
channels are carried in the nuisance block, and the effect-size floor is *defined* by how much
variance the arbitrary choice among them commands.

### §0.2 A correction to my own pre-lock work, recorded because it nearly changed the design

My first marker implementation omitted H-NEW-2620's rule that a leading و / ف is stripped before
matching, so it missed «وقيل» and «فقيل». Coverage came out uniformly low and **al-Saʿdī fell to
4.27%, below the 5% eligibility gate, which would have silently dropped an edition.** With the
correct rule the eight per-edition coverages reproduce H-NEW-2620's published figures **exactly
to two decimals** — al-Qurṭubī 61.79, al-Ṭabarī 46.50, al-Baghawī 35.15, Tanwīr 31.61,
al-Wāsiṭ 28.53, Ibn Kathīr 19.76, al-Saʿdī 5.82, al-Muyassar 1.80 — and the eligible set is the
same seven. **This was my bug, not a rules-tuple finding**, and it is recorded so that the exact
reproduction below is read as a replication and not as a coincidence.

### §0.3 Everything inspected before this lock

Outcome **marginals only**. **No outcome-to-predictor association of any kind was computed** —
not against the structural columns, and not against length. Every correlation in this design is
computed for the first time inside the run.

1. File counts, coverage, non-empty counts, top-level entry counts for all 13 directories.
2. Per-edition dispute-marker coverage (the eight figures above) and the eligibility gate outcome.
3. Shared-commentary-block structure per edition (distinct blocks, % of verses in shared blocks).
4. Death-date probes and their contexts, for attribution only.
5. **Tie fractions of all five candidate outcome channels** (§3.4), as the brief mandates.
6. `csv/h-new-2990-column-declarations.csv` in full — which is a *predictor*-side document
   containing no outcome of mine.

---

## §1. Hypothesis

**H.** Per-verse cross-edition exegetical divergence is related to the verse's own structural
profile, **beyond what verse length explains**.

**Mechanism, stated so it can fail.** Lexically extraordinary verses — those carrying hapax
roots, rare roots, or low-frequency vocabulary — present the exegete with a word whose meaning is
genuinely underdetermined, and the tradition responds by reporting multiple views. H-NEW-2620's
own rosters are consistent with this: *aḥqāb* (Q 78:23), *abābīl* (Q 105:3) and *ʿiḍīn* (Q 15:91)
all surface near the top of its disagreement and dispute rosters, and all three are lexical
cruxes in the literal sense.

**If H is false**, the channels below measure editorial verbosity, house style, digitisation
depth, isnād retention, and which verses an editor chose to segment separately — see §4.

---

## §2. The central trap: what is actually being measured

**Disagreement is not directly observable.** Every quantity below is a hand-built proxy in the
sense of `findings/PROXY-CLAIMS.md`, and each is declared here with what it would *also* be
measuring if H were false.

| channel | what it counts | what it is ALSO measuring if H is false |
|:--|:--|:--|
| **DISPUTE** | classical disputation formulae per verse | how much an edition **reports** rather than adjudicates; genre convention; al-Ṭabarī's isnād-stacking style; digitisation depth |
| **DIVERGENCE-L** | dispersion of commentary **length** across editions | disagreement about *how much attention to give*, **not about meaning** — H-NEW-2620 §3 says this in terms; also API segmentation |
| **DIVERGENCE-V** | pairwise vocabulary dissimilarity across editions | register and house style; a terse gloss and a long excursus share few words even in perfect agreement; **length asymmetry mechanically inflates it** |

**None of these measures disagreement about meaning.** The DISPUTE channel measures *reported*
disagreement, which is the closest observable available in this corpus and is still one step
removed. **This limitation is not removable by any analysis choice** and is restated in the
finding regardless of outcome.

**Two contaminations found post-hoc by H-NEW-2620 are pre-registered as controls here**, rather
than discovered again:
- **Lemma echo (2620 §7.3).** Editions quote the verse before commenting, so a verse whose own
  Qurʾānic text contains *ikhtalafa* or *qīla* inflates its own marker count. 70 verses (1.12%)
  are affected and **10 of 2620's top-30 DISPUTE roster** were such verses. Enters the nuisance
  block as a binary covariate, and a sensitivity drops them entirely.
- **Repetition (2620 §7.1).** A mufassir who comments on a refrain the first time does not
  comment again, and the instrument reads that as neglect; 2620's Roster B was **~73% repetition
  artefact**. A binary "verse text occurs earlier in the corpus" covariate enters the nuisance
  block, and a sensitivity restricts to first occurrences.

---

## §3. Instruments

### §3.1 Editions used

**Arabic only for the primary.** The four English editions are excluded from every confirmatory
inference: one duplicates the Arabic Ibn Kathīr, translation inflates and deflates length by
translator policy, and `en-tafisr-ibn-kathir` is **92.19% shared blocks** (1,895 distinct blocks
for 6,236 verses). They appear in one non-confirmatory sensitivity only.

- **DIVERGENCE-L and DIVERGENCE-V:** all **8** Arabic editions.
- **DISPUTE:** the **7** Arabic editions clearing H-NEW-2620's locked ≥5% marker-coverage gate.
  **al-Muyassar (1.80%) is excluded** — a modern paraphrase that almost never reports alternative
  views. The gate and its threshold are inherited unchanged from 2620 §2.5; **I have not retuned
  it**, and retuning it is forbidden after this lock.

### §3.2 Amortisation (inherited from H-NEW-2620, locked)

Several editions assign one commentary block to a run of verses and the API replicates it into
every verse file in the run. Every per-verse quantity is therefore **amortised**: the block value
divided by *g*, the number of verses sharing that block. Measured shared-block rates, Arabic:
al-Ṭabarī 1.33%, al-Baghawī 1.33%, al-Qurṭubī 2.36%, Tanwīr 2.65%, al-Wāsiṭ 5.74%,
Ibn Kathīr 8.60%, al-Saʿdī 13.68%, al-Muyassar 29.30%.

### §3.3 The marker set (inherited verbatim from H-NEW-2620 §2.5, NOT retuned)

Matched on whitespace-delimited Arabic words after NFD decomposition, combining-mark removal, and
the folding {أ إ آ ٱ → ا, ى → ي, ة → ه, ؤ → و, ئ → ي}, with a leading و / ف stripped from each
word. Whole-word matching, never substring — this is what stops *thaqīl* being counted as *qīla*.

**Unigrams:** اختلف, اختلفوا, اختلفت, اختلاف, الاختلاف, قيل, قولان, القولان, قولين, اقوال,
الاقوال, وجهان, الوجهان, وجهين, مذهبان.
**Bigrams:** (قال, اخرون), (قال, بعضهم), (قالت, طايفه), (قال, قوم).

### §3.4 Outcome channels, with tie fractions measured before the lock

| channel | definition | modal tie |
|:--|:--|--:|
| **C1 DISPUTE-rank** | mean over the 7 eligible editions of the within-edition mid-rank of the amortised marker count (**2620's I5 channel, inherited**) | **17.32%** |
| **C2 DISPUTE-density** | mean over the 7 of markers per 1,000 characters of that edition's commentary (**the length-honest counterpart; new**) | **17.32%** |
| **C3 DIVERGENCE-L** | interquartile range across the 8 Arabic editions of the within-edition mid-rank of amortised commentary length (**2620's D, inherited**) | **0.10%** |
| **C4 DIVERGENCE-V** | mean pairwise Jaccard **distance** of commentary word-type sets across the 8 Arabic editions (**new**) | **0.02%** |

**Maximum modal tie fraction across all channels: 17.32%**, which is the fraction of verses
carrying **zero** disputation markers in **all seven** eligible editions. **This is below 50%, so
the >50% exact-test trigger does not fire** — but exact permutation is used throughout anyway,
per protocol and because H-NEW-3000's parametric route ran **57× too liberal** on a tied outcome.
No parametric p is reported as a verdict-bearing quantity anywhere in this design.

### §3.5 Structural block — the predictor (pre-declared, from H-NEW-2990)

Five columns, chosen by the §1 mechanism, **every one flagged `length_dominated = False`** in
`csv/h-new-2990-column-declarations.csv`, and **every one a RATE or an INVARIANT — never a
COUNT**:

| column | family | kind | ρ vs n_words (declared) |
|:--|:--|:--|--:|
| `frac_hapax_root_tokens` | C hapax | RATE | 0.0105 |
| `frac_hapax_lemma_tokens` | C hapax | RATE | 0.0010 |
| `mean_root_surprisal_bits` | D rarity | INVARIANT | −0.2333 |
| `frac_root_tokens_freq_le5` | D rarity | RATE | 0.0692 |
| `root_simpson_repeat` | E repetition | INVARIANT | 0.4436 |

**The two length-dominated columns (`sum_root_surprisal_bits` ρ=0.941, `n_root_types` ρ=0.951)
are excluded, as are all six B-family length columns and both H-family composites.** The
composites are excluded deliberately: their own declaration calls them *"secondary to the
columns, never a replacement for them"*, and `struct_z_composite_resid` carries ρ = +0.2382
against word count, which is larger than three of my five chosen columns.

### §3.6 Nuisance block (M0)

`n_words`, `n_letters_rasm`, `n_segments` (**all three length channels, per warning 3**),
`mushaf_index`, `lemma_echo` (binary; the verse's own Qurʾānic text contains a marker word),
`is_repeat` (binary; the verse's normalised text occurs earlier in the corpus).

---

## §4. Why this design is not a p-value test

**At n = 6,236 a correlation of ρ = 0.05 gives p < 0.0001.** H-NEW-2620 already measured
ρ(DISPUTE_raw, hapax count) = **+0.1332** at verse level. **A significant result is therefore
close to guaranteed and means nothing on its own.** The binding constraint in this design is
deliberately the effect size, not the p-value, and this is stated now so that a small-p /
small-ΔR² outcome cannot later be presented as a pass.

**Statistic.** Y is normal-score transformed. M0 = nuisance block. M1 = M0 + structural block.
**ΔR² = R²(M1) − R²(M0)**, by OLS.

**Null.** The structural block's rows are permuted **within deciles of `n_words`**. This
preserves length-mediated association under the null, so **only length-independent structural
signal can produce a significant ΔR².** A naive whole-column shuffle would break the
structure–length relation too and would let length leak back in through the structural block as
apparent signal; that null is rejected here and must not be substituted. 10,000 permutations,
seed 20260509.

**The floor, defined by the project's own deciding-parameter lesson.** `cross-finding-029` found
across five lanes that the quantity fixing the verdict was not the quantity under test, and
H-NEW-3010 saw its p swing ~70× on which length channel was controlled. So the floor is not
picked, it is **computed**: let **ΔR²_lengthrule** be the variance gained by adding the second
and third length channels to a model already containing the first. That is the variance
commanded by the arbitrary choice among three near-identical length rules.

> **If the structural block adds less variance than the choice of length rule, it is not a
> finding.**

---

## §5. Registered inferences (k = 3)

Bonferroni α = 0.05 / 3 = **0.01666667**.

| | outcome | predictor block | direction |
|:--|:--|:--|:--|
| **I1** | **DISPUTE** — reported as the **worse** of C1 and C2 | §3.5 structural block | positive |
| **I2** | **DIVERGENCE-L** (C3) | §3.5 structural block | positive |
| **I3** | **DIVERGENCE-V** (C4) | §3.5 structural block | positive |

**I1 is headlined by the WORSE of its two length rules**, per the brief's warning 3 (*"three
length channels all run, worst as headline, dominant named"*). Both are reported; the dominant
one is named in the finding.

**Direction lock, justified from published anchors — NOT from the frontier map's Prior line**,
which is 1-for-6 and whose every optimistic prior has failed. ΔR² is non-negative by
construction, so the direction is carried by a signed quantity: the **partial correlation of
`frac_hapax_root_tokens` with Y given the nuisance block**, locked **POSITIVE**. Anchors, both
published, both verse-level, both positive:
- H-NEW-2620 §4: ρ(DISPUTE_raw, hapax count) = **+0.1332**
- H-NEW-2620 §4: ρ(ATTENTION_raw, hapax count) = **+0.1141**

**A counter-anchor is recorded, because it cuts against me:** H-NEW-2620 §4 also measured
ρ(ATTENTION, mean root rarity) = **−0.0205**, essentially flat, and concluded *"classical
commentary volume tracks how much text there is, not how rare its vocabulary is."* **That is
evidence against this hypothesis and it is on the record before the run.**

---

## §6. Decision rule

### §6.1 PASS requires all three of the following, per inference

- **(a)** permutation p(ΔR²) **< 0.01666667**
- **(b)** **ΔR² ≥ 0.01** — the absolute floor
- **(c)** **ΔR² > ΔR²_lengthrule** — the computed floor of §4
- **(d)** the signed partial correlation of `frac_hapax_root_tokens` with Y given M0 is
  **positive**

Failing any one of (a)–(d) is **NULL for that inference**. There is no partial pass.

### §6.2 Verdict

- **SUPPORTED** — all three inferences PASS.
- **PARTIAL** — one or two PASS. The finding must name which, and must state that the channels
  are three proxies for one construct, so a split among them is evidence of proxy sensitivity and
  not of a graded effect.
- **NULL** — zero PASS.

**Conjunction, not union.** Bonferroni answers a union question. The three channels are three
proxies for a **single** construct, so if H is true they should move **together**. The finding
must report the **survivor count** (how many of 3 pass) alongside the per-channel verdicts, and
a survivor count of 1 must not be reported as support for H.

### §6.3 Reverse direction

If (d) fails and the signed partial is negative at p < 0.01666667 in the reverse direction, a
**REVERSE-DIRECTION flag** is raised and reported at full prominence. It is **not** a pass and
does not convert a NULL into a finding.

### §6.4 If NULL

MDE and power are reported, **including the untestable branch** per H-NEW-3030 §3.5: the smallest
ΔR² clearing α (**ΔR²\***) is computed and compared against the **attainable ceiling
ΔR²_max** — the ΔR² of the *full* 31-clean-column block. If ΔR²\* > ΔR²_max the design is
**UNTESTABLE-AT-THIS-N** and the NULL carries no evidential weight; if ΔR²\* ≤ ΔR²_max the design
could have rejected and the NULL is informative down to ΔR²\*.

**Register labels are not used in this design**, so the effective-n / phase-degenerate-strata
requirement does not apply. This is recorded rather than silently omitted.

### §6.5 If the criteria disagree

Where the p-gate and the two effect-size floors disagree, **the more severe verdict is taken.**
Locked here, before any number exists, exactly as H-NEW-3030 §6.5 locked it — so that a
disagreement cannot be resolved in whichever direction proves convenient.

---

## §7. Sensitivities — NON-CONFIRMATORY, reported whatever they show

1. **§7.1 classical-only, run correctly for the first time.** The **four verified pre-modern
   Arabic editions** — al-Ṭabarī (310), al-Baghawī (516), al-Qurṭubī (671), Ibn Kathīr (774).
   H-NEW-2620's row of this name contained Ibn ʿĀshūr (1393) and is not this quantity.
2. **modern-only**: al-Saʿdī, Ibn ʿĀshūr, al-Wasīṭ, al-Muyassar.
3. **lemma-echo verses dropped** entirely, rather than covaried.
4. **first-occurrence verses only.**
5. **leave-one-edition-out**, all 8.
6. **full 31-clean-column structural block** in place of the 5-column mechanism block.
7. **raw un-amortised** lengths and marker counts.
8. **English 4 editions** (weak; two are not independent witnesses).

---

## §8. Frozen inputs and abort conditions

**Inputs, SHA-256 verified at runtime; any mismatch aborts:**
`data/literature/classical-tafsir/spa5k-tafsir-api/` by manifest over the 74,832 Arabic +
English tafsīr verse files actually read; `findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv`;
`csv/h-new-2990-column-declarations.csv`; `quran-text/quran-no-tashkeel.json`.

**Abort conditions, all fail-fast:**
1. Pre-registration SHA-256 ≠ `EXPECTED_PREREG_SHA` embedded in the script.
2. Any input hash mismatch.
3. Any edition not carrying exactly 6,236 non-empty verse texts.
4. Marker coverage not reproducing H-NEW-2620's eight published figures to 0.01 pp.
5. Eligible-edition count ≠ 7.
6. Verse profile not carrying 6,236 rows and all 33 declared columns.
7. Any structural column used that is flagged `length_dominated` ≠ False in the declarations file.
8. Permutation null mean of ΔR² not within 3 permutation-SEs of the analytic expectation.
9. Run directory already exists (`os.makedirs(exist_ok=False)`); every output opened `'x'`.

**Missing data.** Rows where any M0 or M1 column is undefined are dropped; the count and the
identity of every dropped verse are written to the run directory. 22 verses lack root-family
values in the profile (`n_defined = 6214` for the rarity columns), so the analysis n is expected
to be **6,214**, and the realised n is reported.

**Run directory:** `findings/phase-b-hypotheses/runs/h-new-3160/<UTC>/`, created with
`exist_ok=False`. **No run directory is ever deleted.**

---

## §9. Forking-paths log — every choice made before the lock

| # | choice | alternatives rejected | why |
|--:|:--|:--|:--|
| 1 | **run at all** — verse-level form of F-11 | abandon as duplicate of H-NEW-2620 | 2620 is surah-level and names the verse-level test as *"a separate piece of work"*; the enabling instrument post-dates it |
| 2 | verse unit, n=6,236 | surah unit | 2620 did surah; verse is the open question and the resolution F-11 states |
| 3 | marker set inherited verbatim | retune for better coverage | retuning after seeing coverage is a forking path; inheritance makes this a replication |
| 4 | ≥5% coverage gate inherited | drop the gate, or move it | same |
| 5 | Arabic-only primary | pool all 12 | English adds a duplicate work and a 92.19%-shared-block edition |
| 6 | amortisation on | raw lengths | 2620 locked it before outcomes; raw is sensitivity 7 |
| 7 | 5-column mechanism block | all 31 clean columns; the composites | mechanism-motivated and pre-declared; 31-column is sensitivity 6; composites carry more length than the columns |
| 8 | ΔR² incremental | bare correlation | at n=6,236 a bare correlation is guaranteed significant and uninformative |
| 9 | **within-decile permutation** | whole-column shuffle | a whole-column shuffle lets length leak back as apparent signal |
| 10 | floor = max(0.01, ΔR²_lengthrule) | p-value only | cross-finding-029: the deciding parameter is usually not the one under test |
| 11 | worse-of-two-length-rules headline for I1 | best; or average | brief warning 3 |
| 12 | k=3 | k=4 counting C1 and C2 separately | C1 and C2 are two length rules on one construct, not two constructs |
| 13 | conjunction reported with survivor count | Bonferroni alone | Bonferroni answers a union question |
| 14 | lemma-echo and repetition as covariates | ignore | both were 2620 post-hoc discoveries; pre-registering them is the whole point |
| 15 | direction from 2620 §4 | from the map's Prior line | the map is 1-for-6 and the protocol forbids citing it |
| 16 | counter-anchor recorded | omit it | ρ(ATTENTION, root rarity) = −0.0205 cuts against H and belongs on the record before the run |

---

## §10. What would make me wrong

- If ΔR² clears the floors on all three channels but **collapses** under sensitivity 3
  (lemma-echo dropped), the effect is the contamination 2620 found, not structure.
- If it collapses under sensitivity 4 (first occurrences only), it is the repetition artefact.
- If DIVERGENCE-V passes while DISPUTE fails, the likely explanation is length asymmetry between
  a terse gloss and a long excursus, **not** disagreement.
- If the classical-only sensitivity (§7.1) reverses against the primary, then whatever is being
  measured is a property of 20th-century Arabic exegetical prose and not of the tradition.

---

*Locked before any outcome-to-predictor association was computed.*

*Bismillāhi al-Raḥmāni al-Raḥīm.*
