---
id: H-NEW-2610
title: Do the Sajāwandī waqf grades encode an ordered prosodic-syntactic boundary hierarchy, and do they carry prosody beyond syntax?
date: 2026-08-07
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
family: WAQF-2026-08-07-A
seed: 20260509
seed_replication: 20260519
n_permutations: 10000
tests_in_family: 8
alpha_bonferroni: 0.00625
corrected_novelty_gate: 0.005
raw_p_gate: 0.000625
---

# PRE-REGISTRATION — H-NEW-2610 — The waqf grades as a boundary hierarchy


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

This file is written before any statistic relating a waqf grade to any outcome
variable has been computed. §2 lists exhaustively what was inspected before this
lock. The final SHA-256 of this file is embedded as a fixed literal in
`findings/phase-b-hypotheses/scripts/h-new-2610.py` and verified at runtime; the
run must abort with `SystemExit` on mismatch.

---

## 1. The object of study, and the confound that defines the whole test

The Uthmānī muṣḥaf carries a set of small superscript glyphs that instruct a reciter
where stopping is obligatory, preferable, permissible, or dispreferred. They descend
from the *ʿilal al-wuqūf* tradition of **Abū ʿAbd Allāh Muḥammad b. Ṭayfūr
al-Sajāwandī (d. 560/1165)**.

**THE CENTRAL CONFOUND, stated first and stated plainly.** These marks are a **later
editorial layer**. They are a twelfth-century grammarian's analysis printed on top of
a seventh-century text. They are **not part of the revealed text** and nothing in this
pre-registration or in any finding derived from it may claim otherwise. The
consonantal rasm carries no waqf marks; neither do the earliest muṣḥafs.

The consequence for inference is severe and must be carried through every verdict:

> **Any positive H1 result is fully compatible with the marks merely re-encoding
> al-Sajāwandī's own grammatical analysis.** A grammarian who analyses a clause
> boundary and then prints a symbol at that boundary will of course produce symbols
> that correlate with clause boundaries. H1 confirming is *nearly guaranteed a priori*
> and is therefore weak evidence about the text. It is a **calibration** of the
> instrument, not a discovery.

This is exactly why **H2 is the hypothesis that carries the intellectual weight**. H2
asks whether grade predicts a **phonological** property of the text *after* the
syntactic boundary has been conditioned out. Syntax is what a grammarian analyses;
the sound of the word before the stop is not. If H2 is NULL, the honest conclusion is
that the marks are competent syntactic commentary and nothing more. Both outcomes are
publishable and will be published with equal prominence.

A second, deeper caution that no permutation test can address: al-Sajāwandī and every
modern Arabic treebank annotator inherit **the same Baṣran/Kūfan grammatical
tradition**. Agreement between the marks and a modern dependency parse may reflect
shared grammatical theory rather than independent convergence on a property of the
text. This is not leakage; it is common ancestry, and it caps how much H1 can ever
mean.

### 1.1 Classical anchor — verified on disk, with the citation corrected

`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, **line 5092**,
heading: `### | النوع الثامن والعشرون: في معرفة الوقف والابتداء`.

**Correction to the brief and to `HANDOFF/FRONTIER-MAP-2026-08-07.md`:** both cite
*al-Itqān* **nawʿ 27**. In the OpenITI recension on disk this nawʿ is
**al-nawʿ al-thāmin wa-l-ʿishrūn = nawʿ 28**, because that recension merges nawʿ
22–27 under one heading at line 4631 (`النوع الثاني والثالث والرابع والخامس والسادس
والسابع والعشرون: معرفة المتواتر والمشهور والآحاد والشاذ والموضوع والمدرج`). I cite
the number I verified. Numbering differs across printed editions; I make no claim
about editions I have not opened.

At line 5147 al-Suyūṭī reports al-Sajāwandī's own scheme verbatim:

> وقال السجاوندي: الوقف على خمس مراتب: لازم، ومطلق، وجائز، ومجوز لوجه، ومرخص ضرورة.
>
> "al-Sajāwandī said: the waqf has **five ranks** (*marātib*): *lāzim*, *muṭlaq*,
> *jāʾiz*, *mujawwaz li-wajh*, and *murakhkhaṣ ḍarūratan*."

Two things follow, and both are load-bearing for this pre-registration:

1. **The ordinality is al-Sajāwandī's own claim, not my imposition.** He calls them
   *marātib* — ranks. H1 tests a hierarchy the classical source itself asserts.
2. **al-Suyūṭī's definitions fix the semantics of the two anchor grades:**
   - *lāzim*: `ما لو وصل طرفاه غير المراد` — "that which, if its two sides are joined,
     is not the intended meaning." Joining destroys the sense. **Strongest stop.** His
     worked example is `{وما هم بمؤمنين}` before `{يخادعون الله}` (Q 2:8→2:9): without
     the stop, *yukhādiʿūna llāha* would read as an adjective qualifying *muʾminīn*.
   - *jāʾiz*: `ما يجوز فيه الوصل والفصل لتجاذب الموجبين من الطرفين` — "that in which
     joining and separating are both permitted, because the two sides pull against
     each other." **Definitionally the balance point.**

   That *jāʾiz is the balance point* is what licenses placing *al-waqf awlā* above it
   and *al-waṣl awlā* below it in §3's ladder.

**Honest limit on the anchor.** The printed glyph inventory is **not** a one-to-one
rendering of al-Sajāwandī's five *marātib*. `ج` (jāʾiz) and `مـ` (lāzim) correspond to
two of his ranks by name; `صلى` (*al-waṣl awlā*) and `قلى` (*al-waqf awlā*) are terms
of the later muṣḥaf-printing tradition that descend from, but are not identical to,
his *mujawwaz li-wajh* / *murakhkhaṣ ḍarūratan*. I have **not** verified
al-Sajāwandī's *ʿIlal al-wuqūf* itself — **it is not on disk** — so every claim about
his system here is mediated by al-Suyūṭī. I cite only what I read.

Supporting material verified in the same nawʿ, cited because it establishes that the
tradition treats waqf as *prosodic* and not only syntactic — which is the premise H2
tests:

- Line 5106, Ibn al-Jazarī (*al-Nashr*), quoted by al-Suyūṭī: `لما لم يمكن القارئ أن
  يقرأ السورة أو القصة في نفس واحد ... وجب حينئذ اختيار وقف للتنفس والاستراحة` — "since
  the reciter cannot recite the sūra or the narrative in a single breath … it became
  obligatory to choose a stopping place for breath and rest." **Breath, not syntax.**
- Line 5112, al-Nakzāwī: `لأنه لا يتأتى لأحد معرفة معاني القرآن ... إلا بمعرفة
  الفواصل` — waqf knowledge is tied to knowledge of **al-fawāṣil**. This is the
  classical warrant for H2's choice of outcome variable.
- Line 5104, ʿAlī b. Abī Ṭālib on `{ورتل القرآن ترتيلا}`: `الترتيل تجويد الحروف
  ومعرفة الوقوف` — "*tartīl* is perfecting the letters and knowing the stops."

### 1.2 Does the H-NEW-2540 §7.2 EQTB contamination reach this question?

I read `findings/phase-b-hypotheses/h-new-2540-form-v-valency.md` §7.2 before writing
this. Its finding: EQTB's syntax was initially generated by a BiLSTM parser whose
inputs included POS tags and fine-grained morphological-feature embeddings, EQTB
carries `verb_form` among those columns, and human validation was **not**
form-blinded. For H-NEW-2540 the outcome variable was an EQTB `Obj` edge and the
predictor was verb form — a documented circularity.

**My honest assessment for H-NEW-2610, given before computing anything:**

**The machine pathway is absent.** Waqf marks are not in QAC morphology and are not a
parser input feature. The parser could not have been cued by them.

**The human pathway is materially weakened, and I checked this rather than assuming
it.** I counted every character of EQTB's `uthmani_token` and `imlaai_token` columns
across all 128,219 real token rows: **the U+06D6/06D7/06D8/06DA grade glyphs appear
zero times.** The only waqf-range glyph present anywhere is U+06DC (saktah), twice.
EQTB's working text representation does not carry the pause grades. Human validators
working from that representation did not see them. This is a checkable fact, not a
reassurance.

**What remains, and it is not small.** (i) Validators are human beings who have
memorised the muṣḥaf; the marks can be known without being displayed. (ii) The common
grammatical ancestry of §1 is untouched by any of this. (iii) EQTB's own sentence
segmentation (11,693 sentences over 6,236 verses) is an editorial judgment of clause
structure by people trained in the same tradition.

**Consequence, locked in advance.** The EQTB channel (H1b) is **secondary** and is
reported as an annotation-internal association. The **primary H1 instrument (H1a) is
annotation-free** — computed from the running text and the canonical āya division
alone, with no parse, no POS tag and no human syntactic judgment anywhere in it. This
is a deliberate inversion of H-NEW-2540's architecture, adopted because that finding's
audit showed the parser-free channel was the one that survived.

---

## 2. What was inspected before this lock — exhaustive

Only structural and integrity facts were computed. **No statistic relating any grade
to any outcome variable was computed, viewed, or estimated.**

1. Glyph census of `quran-text/quran-full-tashkeel.json`, independently re-verified
   against the frontier map's counts. All six match exactly: U+06DA jīm 2,083;
   U+06D6 ṣlà 1,651; U+06D7 qlà 511; U+06D8 mīm 21; U+06DC saktah 8; U+06DB muʿānaqa
   6. Corpus: 114 sūras, 6,236 verses, 77,429 whitespace-delimited words.
2. Mark attachment geometry: every one of the 4,266 grade marks is appended directly
   to the final character of a word and followed by a space. **No grade mark stands on
   a verse-final word** — all 4,266 sit at verse-internal junctures. Of the 8 saktah,
   4 are word-internal and 2 verse-final, so saktah is geometrically unlike the grades.
3. Word-count agreement per verse: EQTB vs QAC v0.4 — **0 mismatches**, 77,429 words
   each. `quran-full-tashkeel.json` vs both — 10 verses differ in word segmentation
   ((2,72), (2,181), (8,6), (13,37), (15,7), (27,20), (36,22), (37,130), (37,164),
   (41,47)); totals are identical, so the differences are compensating splits/joins.
   **5 grade marks (1 ṣlà, 4 jīm) fall in those 10 verses** = 0.12% of the corpus.
4. EQTB schema, and the waqf-glyph audit of its token columns reported in §1.2.
5. EQTB structure: 139,376 rows, 11,157 synthetic, 128,219 real; `(sentence_id,
   token_id)` unique; 11,693 sentences over 6,236 verses — sentences both split verses
   (max 23 per verse) and span them (max 31 verses).
6. **A rules-tuple divergence between text files, discovered during these checks and
   registered in advance as a sensitivity (§8.1).** `quran-min-tashkeel.json` carries a
   *different* mark inventory: ṣlà 1,682 · jīm 1,972 · qlà 603 · mīm 22 · saktah 7 ·
   muʿānaqa 12 · **and 68 instances of U+06D9 (lā, *waqf mamnūʿ*) which are entirely
   absent from `quran-full-tashkeel.json`.** Its word segmentation also differs in
   2,721 verses. The two files disagree about the muṣḥaf's pause apparatus.
7. al-Itqān nawʿ location and text, as quoted in §1.1.
8. h-new-2240.json field structure (`per_surah[].dominant_class`) and the `classify()`
   source of `findings/phase-b-hypotheses/scripts/h-new-2240.py`.
9. Register membership lists in h-new-2500.json / h-new-2530.json.

---

## 3. The locked ladder

Grades in **increasing stop-strength**, with integer ranks used as the predictor:

| rank | glyph | codepoint | term | n | al-Suyūṭī's semantics |
|:-:|:-:|:--|:--|--:|:--|
| 1 | ۖ ṣlà | U+06D6 | *al-waṣl awlā* — joining preferable | 1,651 | below the balance point |
| 2 | ۚ jīm | U+06DA | *jāʾiz* — either permitted | 2,083 | **the balance point** (`تجاذب الموجبين`) |
| 3 | ۗ qlà | U+06D7 | *al-waqf awlā* — stopping preferable | 511 | above the balance point |
| 4 | ۘ mīm | U+06D8 | *lāzim* — obligatory stop | 21 | joining destroys the sense |

**Eligible loci: the 4,266 verse-internal junctures carrying exactly one of these four
glyphs.** Saktah (8) and muʿānaqa (6) are **excluded from every gated test** and
reported descriptively only: saktah is a breath-suppressed silence rather than a stop
grade and is geometrically unlike the four (§2.2); muʿānaqa is a *disjunctive pair*
(stop at one of two, never both) and is not a point on a stop-strength scale.
Excluding them is a decision made before computation and stated here so it cannot be
mistaken for a post-hoc filter.

---

## 4. Frozen inputs (SHA-256, verified at runtime; any mismatch aborts)

| # | path | SHA-256 |
|:-:|:--|:--|
| 1 | `quran-text/quran-full-tashkeel.json` | `382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715` |
| 2 | `quran-text/quran-min-tashkeel.json` | `87aaab41f78d1b148c8051b8afc1ee5fa66fd6d45f2f7a2984e3f9192c458b36` |
| 3 | `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| 4 | EQTB `Quranic.csv` (UTF-16, tab-separated) | `a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7` |
| 5 | `findings/phase-b-hypotheses/csv/h-new-2240.json` | `cce458614dec9aa75c30faa3b46eab8d748d60aeea1caf83a47253bdbade7a88` |
| 6 | `findings/phase-b-hypotheses/csv/h-new-2500.json` | `a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25` |
| 7 | `findings/phase-b-hypotheses/csv/h-new-2530.json` | `5ca17050c20b15734ad9a734e7bad7b938b616c924ec53dfcd24814a1473b68c` |

Input 4 is not committed (50 MB, CC BY 4.0); provenance and re-acquire recipe are in
`data/syntax/UD-QURAN-SOURCE.md`. Its hash is the one H-NEW-2540 registered before the
file was ever on this machine, and the containing archive re-verified to
`6ae1da54a801939cfaf52c05b01e5858ab26b147543806cccb46df4ea4fbdcb3` on re-download.

**Rules-tuple (locked):** `(full-tashkeel primary text, orthographic whitespace-
delimited token, verse-internal juncture as unit, Sajāwandī four-grade glyph set
{U+06D6, U+06D7, U+06D8, U+06DA} only, basmala counted as Q1:1 only, Ḥafṣ-Kūfan 6236,
Mashriqī)`.

---

## 5. Instruments

### 5.1 Instrument A — verse-boundary resemblance (VBR). Annotation-free. Primary.

The one boundary in this corpus whose strength is uncontested, and which is centuries
older than al-Sajāwandī, is the **āya division**. VBR asks, for a juncture, how much
the material on each side looks like the material at an āya edge.

Type normalisation `norm(w)`: map U+0670 (dagger alif) and U+0671 (alef wasla) to
U+0627; keep only codepoints in [U+0621, U+064A] ∪ {U+0649, U+0629}; drop everything
else (all harakāt, tanwīn, shadda, sukūn, tatweel, and the whole U+06D6–U+06ED range).
Derived from the full-tashkeel word itself, so word segmentation is identical by
construction.

For a juncture between word `w_L` and `w_R` in verse `(c,v)`, with `t = norm(·)`:

```
VBR = log( (F_end(t_L) + 0.5) / (N(t_L) - 1 + 1.0) )
    + log( (F_beg(t_R) + 0.5) / (N(t_R) - 1 + 1.0) )
```

`F_end(t)` = number of verses whose final word normalises to `t`; `F_beg(t)` = number
whose first word does; `N(t)` = total corpus occurrences of `t`. The `−1` is a
leave-one-out correction removing the focal token from its own denominator (the focal
tokens are verse-internal and so never enter `F_end`/`F_beg`). Add-0.5 smoothing.

Higher VBR = the juncture looks more like an āya edge = stronger boundary. No POS tag,
no parse, no lemma, no human syntactic judgment enters this number.

### 5.2 Instrument B — dependency arc-crossing count. EQTB. Secondary, contaminated.

Order all real EQTB tokens by `(chapter_id, verse_id, word_id, tok_id)` into a corpus-
linear index. A dependency edge is the pair (token, its `ref_token_id` head) where both
are real tokens (`location != '_'`) in the same `sentence_id`. For a juncture after
word `w` of verse `(c,v)`, let `cut` be the linear index of the last token of word `w`.
An edge `(a,b)` **crosses** iff `min(lin_a, lin_b) <= cut < max(lin_a, lin_b)`.

`XC` = number of crossing edges. **Lower XC = stronger boundary** (fewer dependencies
span the point; XC = 0 means no syntactic material bridges it at all).

The 10 word-segmentation-discrepant verses of §2.3 are **excluded** from every
EQTB-channel computation. Cost: 5 of 4,266 loci. Word-count agreement between EQTB and
QAC must be 100% at runtime or the run aborts.

### 5.3 Outcome for H2 — fāṣila rhyme match. Annotation-free, phonological.

`classify()` is **ported verbatim** from `findings/phase-b-hypotheses/scripts/
h-new-2240.py` (lines 49–120): the deterministic pausal-rime assonance class
(*ridf* long vowel + *rāwī* consonant, with the open-ending, hamza and tāʾ-marbūṭa
cases). Applied to the **pre-pause word** `w_L` rather than to a verse-final word.

`RM = 1` iff `class(w_L)` equals sūra `c`'s dominant fāṣila class, else 0. The
dominant class is read from frozen input 5 (`h-new-2240.json` `per_surah[].
dominant_class`) — the project's existing instrument, not re-derived.

**Instrument control (MW-6), gated as an abort condition.** I recompute the per-sūra
dominant class with my ported `classify()` over verse-final words of the full-tashkeel
text and compare against h-new-2240.json's (which was computed on min-tashkeel).
Agreement is reported. If agreement is **< 90 %** of 114 sūras, H2 is declared
**NULL-INSTRUMENT-FAILURE** and its p-values are not interpreted. This threshold is
set now, before seeing the number.

Why this outcome is the right one for H2: it is a property of the **sound** of the
word before the stop. A grammarian's clause analysis does not encode it, a dependency
parse does not represent it, and al-Nakzāwī (§1.1) ties waqf knowledge to *al-fawāṣil*
explicitly.

---

## 6. Registered hypotheses, locked directions, and nulls

The statistic for H1a/H1b is the **Spearman rank correlation** `ρ` between grade rank
(§3) and the instrument, over eligible loci. One statistic, two permutation schemes.

- **Null A** — permute grade labels freely across all eligible loci.
- **Null B** — permute grade labels **within sūra**, preserving each sūra's grade
  composition exactly. Strictly stronger: removes every sūra-level confound (length,
  register, mark density). Sūras whose eligible loci carry a single grade are
  degenerate blocks contributing no variance; this is conservative and expected.

Null A uses `random.Random(20260509)`; Null B uses `random.Random(20260510)`. 10,000
draws each. One-sided `p = (1 + #{stat_perm >= stat_obs}) / 10001` in the locked
direction. Monte-Carlo floor = 9.999×10⁻⁵.

### H1a — grade is monotonic in annotation-free boundary strength (PRIMARY)

**Locked direction: `ρ(grade_rank, VBR) > 0`.** Stronger stop-grade ⇒ higher
verse-boundary resemblance.

### H1b — grade is monotonic in dependency boundary strength (SECONDARY, contaminated)

**Locked direction: `ρ(grade_rank, XC) < 0`.** Stronger stop-grade ⇒ fewer dependency
arcs cross. Test statistic `−ρ` so the one-sided form is uniform.

### H2 — grade carries phonology beyond syntax (THE PRIZE)

Strata: `XC` bucketed as `{0, 1, 2, 3, 4, 5, ≥6}` — **7 buckets, fixed now**.

```
T_H2 = Σ_s n_s · cov_s(grade_rank, RM) / Σ_s n_s
```

where `cov_s` is the within-stratum covariance over loci in stratum `s`.

**Locked direction: `T_H2 > 0`.** Conditional on the syntactic boundary being held
fixed, a stronger stop-grade still predicts that the pre-pause word rhymes with the
sūra's fāṣila.

**Justification of the direction, locked before observation.** A pause mark is an
instruction to a reciter about where a stop is *acoustically* acceptable. In the
fawāṣil system the canonical acoustic stopping point is the rhyme. If the marks encode
prosody as well as syntax, the strong-stop grades should preferentially land on
rhyme-matching words. If they encode only a clause analysis, grade is conditionally
independent of rhyme once the syntactic boundary is fixed, and `T_H2 ≈ 0`.

- **Null A** — permute grade **within XC stratum**. `random.Random(20260511)`.
- **Null B** — permute grade **within (sūra × XC stratum)**. `random.Random(20260512)`.

Null B is the valid null and carries the inference: it holds the syntactic boundary
*and* the sūra's rhyme base-rate fixed simultaneously. Null A is reported for
completeness.

### H3 — waqf density is register-ordered

Registers reused **verbatim** from `h-new-2530.json` → `genre_proxy_source` →
`h-new-2500.json` `genre_proxy.members`. The gated test uses the **3-register primary**
of H-NEW-2530 (`primary_3register.classes`), n = 91 sūras: `narrative` (31),
`legal_medinan` (20), `eschatological_mufassal` (40). `liturgical_didactic` (23) is
the residual class excluded from H-NEW-2530's own primary and excluded here; the
4-class version is reported as robustness. No new label is invented.

Density `D(s)` = grade marks per 100 words in sūra `s` (full-tashkeel word count).

**Locked direction — Jonckheere–Terpstra trend over the pre-committed order**

```
eschatological_mufassal  <  narrative  <  legal_medinan
```

**Justification, locked before observation.** Pause guidance is needed where a reciter
cannot take the verse in one breath (Ibn al-Jazarī, §1.1) and where the syntax is
embedded enough that a wrong stop distorts sense (al-Suyūṭī's *lāzim*, §1.1).
Legal-Medinan verses are the longest and most embedded — conditions, exceptions,
relative clauses. Eschatological-mufaṣṣal verses are short, and their dense āya
boundaries already supply stopping points. Hence the order above.

- **Null A** — permute register labels freely across the 91 sūras.
  `random.Random(20260513)`.
- **Null B** — permute register labels **within verse-count tertile**, removing the
  sūra-length confound. `random.Random(20260514)`.

---

## 7. Decision gates

Family = **8 registered inferences**: {H1a, H1b, H2, H3} × {Null A, Null B}.

- Bonferroni α = 0.05 / 8 = **0.00625**.
- The project novelty rule (`docs/statistical-rigor-protocol.md` §170) is stricter:
  corrected p < 0.005. Therefore the **raw decision gate is 0.005 / 8 = 0.000625**,
  equivalently `min(1, 8p) < 0.005`.

**A hypothesis PASSES iff its observed direction matches the lock AND both of its raw
p-values are < 0.000625.** Direction reversed, or either null failing, ⇒ NULL. No
rescue by threshold change, by dropping a null, or by substituting a sensitivity for a
primary.

Replication (MW-5): every permutation test is re-run at seeds +10 (20260519, 20260520,
20260521, 20260522, 20260523, 20260524). Reported; a replication that disagrees in
direction is disclosed and downgrades the verdict to DIRECTIONAL.

### 7.1 Decision language, fixed now

- **H1a PASS, H2 PASS** → `GRADED BOUNDARY HIERARCHY WITH PROSODIC RESIDUAL`. Even
  then, this is a property of **al-Sajāwandī's editorial layer**, and describes the
  reciting tradition's analysis of the text, not the revealed text.
- **H1a PASS, H2 NULL** → `HIERARCHY CONFIRMED; MARKS ARE SYNTACTIC COMMENTARY`. The
  expected outcome. It says the twelfth-century grammarian analysed clause structure
  competently. That is a real result about the *tradition* and a NULL about the text.
- **H1a NULL** → the marks do not form an ordered boundary hierarchy under this
  instrument. Publish as NULL; do not rescue with H1b.
- **H1b PASS in isolation** may **never** be reported as independent confirmation, for
  the reasons in §1.2.

---

## 8. Robustness, controls, and sensitivities (reported; never replace §6)

1. **Descriptive calibration ladder.** Mean VBR and mean XC at: verse boundaries; each
   of the four grades; saktah; muʿānaqa; and unmarked verse-internal junctures. This is
   what makes any effect size interpretable, and it is the honest way to show whether a
   "significant" grade ordering is large or trivial next to the āya boundary.
2. **MW-6 instrument control.** 4,266 verse-internal junctures drawn without
   replacement, matched to the observed per-sūra mark counts, seed 20260515, used as a
   non-mark control sample for the ladder.
3. **MW-6 rhyme-instrument control.** §5.3's dominant-class agreement against
   h-new-2240.json, with the 90 % abort threshold.
4. **Per-grade pairwise contrasts** (ṣlà vs jīm, jīm vs qlà, qlà vs lāzim), reported
   with Bonferroni over 3 but explicitly **not gated** — the ladder, not the rungs, is
   the registered claim.
5. **H1a with lāzim dropped**, since n = 21 could dominate a rank correlation's tail.
6. **H3 residualised on mean verse length** (OLS, descriptive) — pre-empting "it is
   only verse length." Length is the hypothesised *mechanism*, so this is reported as
   decomposition, not as a competing model.
7. **H2 with XC strata replaced by EQTB sentence-boundary status** (binary), as an
   alternative syntactic control.
8. **Position control.** Normalised within-verse position of each mark, reported per
   grade, to check whether any effect is positional rather than grade-driven.

### 8.1 Registered rules-tuple sensitivity — the min-tashkeel divergence

Because §2.6 found that `quran-min-tashkeel.json` carries a **different Sajāwandī
apparatus** — including 68 U+06D9 (*lā*, prohibited stop) marks entirely absent from
the primary file — the full H1a analysis is re-run on min-tashkeel with a **five-rung
ladder** `lā < ṣlà < jīm < qlà < lāzim`. Registered **before computation** as a
sensitivity, **not** as a gated inference and **not** as a replacement for the primary.
Its purpose is disclosure: this project's own rules-tuple discipline holds that a
result which does not survive a change of analytical lens must say so. The primary
file's apparatus is **incomplete** relative to a printed muṣḥaf, and the finding must
state that plainly.

---

## 9. Honest limits, written before the result exists

1. **The marks are not the Quran.** Twelfth-century editorial apparatus over a
   seventh-century text. No finding may say otherwise.
2. **H1 confirming is close to a priori guaranteed** and is calibration, not
   discovery (§1).
3. **Common grammatical ancestry** between al-Sajāwandī and modern annotators caps
   H1b's meaning regardless of any p-value (§1.2).
4. **The EQTB channel is contaminated by construction** for morphology-adjacent
   questions; I argue in §1.2 that the specific pathway is weaker here and I checked
   the token columns rather than assuming — but "weaker" is not "absent," and human
   validators may know the marks without seeing them.
5. **Not Quran-specific.** No matched Classical-Arabic control corpus carries waqf
   marks; there is nothing to compare against. This is Quran-internal throughout, and
   cannot be a full Phase-B cross-corpus finding under
   `docs/statistical-rigor-protocol.md` §3.
6. **lāzim n = 21.** The top rung is thin. Any claim resting on it is underpowered and
   §8.5 tests exactly that.
7. **The rhyme instrument was built for verse-final words** and is here applied to
   verse-internal ones. Its pausal-rime logic is position-independent by construction,
   but it was never validated in this position, and §5.3's control is a consistency
   check, not a validation.
8. **The primary text's waqf apparatus is incomplete** (§2.6, §8.1).
9. **No human review of any annotation** has been performed for this finding.
10. **The permutation tests condition on the mark placements as given.** They cannot
    detect error, inconsistency, or regional variation in the muṣḥaf's own mark
    placement, of which there is real historical variation across printing traditions.

---

## 10. Required immutable run record

The run creates a new directory
`findings/phase-b-hypotheses/runs/h-new-2610/<UTC timestamp>/` containing:

- `result.json`
- `manifest.json` — command, git commit, prereg/script/input SHA-256, Python version,
  seeds, platform.

**Nothing in any run directory may ever be overwritten or deleted, including an
uncommitted or superseded one.** This restates the standing correction recorded at
`h-new-2540-form-v-valency.md` §8.1 after that clause was violated in this project.
A run whose path cannot be committed is handled by re-running to an **additional**
directory and retaining both.

The runner emits no interpretive prose. The human-readable finding is written
afterwards, in the parent findings directory.
