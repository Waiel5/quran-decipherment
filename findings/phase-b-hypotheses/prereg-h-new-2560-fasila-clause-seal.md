---
id: H-NEW-2560
title: Is the fāṣila a clause seal? Verse-boundary versus syntactic-constituent alignment in the Extended Quranic Treebank
date: 2026-08-07
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
family: SYNTAX-2026-08-07-A
seed: 20260509
seed_replication: 20260510
n_permutations: 10000
tests_in_family: 6
alpha_bonferroni: 0.008333
corrected_novelty_gate: 0.005
raw_p_gate: 0.000833
rules_tuple: "(no-tashkeel for the waqf join, EQTB segment-token, dependency arcs, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# PRE-REGISTRATION — H-NEW-2560 — Does Quranic syntax close at the āya boundary?


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

This file is written and SHA-256-locked **before** any sealed-rate, crossing-arc count,
register contrast or waqf contrast has been computed. The SHA-256 of this file is
embedded as a fixed literal in `findings/phase-b-hypotheses/scripts/h-new-2560.py` and
verified at runtime; the run aborts on mismatch.

---

## 1. The question, and why it is open

Classical Quranic scholarship treats the verse-end (*fāṣila*) as simultaneously a
phonological, rhetorical and **syntactic** resting place:

- **al-Bāqillānī, *Iʿjāz al-Qurʾān*** — the chapter on *al-fawāṣil*, arguing that the
  Quranic verse-end is not the forced rhyme-terminal of *sajʿ* but a juncture where sense
  and sound complete together.
- **al-Rummānī, *al-Nukat fī iʿjāz al-Qurʾān*** — *al-fawāṣil* as one of the seven
  aspects of *iʿjāz*, distinguished from *asjāʿ* precisely by the claim that meaning
  governs the break rather than the break governing meaning.
- **al-Dānī, *al-Muktafā fī al-waqf wa-l-ibtidāʾ*** and **al-Sajāwandī, *ʿIlal
  al-wuqūf*** — the science of pause and resumption, which grades every candidate pause
  position in the text by whether the syntax may legitimately stop there.

In Arabic poetics the converse defect has a name: *taḍmīn*, running the sentence past the
line-end, is a blemish. The classical claim is therefore empirically sharp and, as far as
the project's literature survey shows, **never quantified**: do āya boundaries actually
coincide with completed syntactic constituents more than chance positions do?

The Extended Quranic Treebank (EQTB) supplies, for the first time, a full dependency
annotation over the whole corpus, which makes the question computable.

---

## 2. Everything inspected before this lock (full disclosure)

Only **format, census and join-feasibility** facts were inspected. No sealed-rate, no
crossing-arc count, no true-versus-pseudo comparison, no register contrast and no waqf
contrast was computed or viewed. The following were:

### 2.1 EQTB structure
- 139,376 rows; 128,219 real (`location != '_'`) and 11,157 synthetic/elided.
- 11,693 sentences; `tid` is globally monotone; `token_id` is sentence-local; zero
  duplicate `(sentence_id, token_id)` pairs; zero `ref_token_id` values pointing outside
  their own sentence.
- **0 sentences span more than one surah.**
- **838 sentences span more than one verse.** Verses-per-sentence: 10,855 sentences cover
  1 verse, 601 cover 2, 140 cover 3, 46 cover 4, 26 cover 5, and a tail reaching 31.
- **6,769 of 11,693 sentences (57.9%) begin mid-verse** (first real token has
  `word_id > 1`); 4,924 begin at a verse-initial word.
- Roots per sentence: 10,143 sentences have exactly 1, 1,550 have 2 or more (max 27);
  89 have none. 1,336 sentences contain ≥2 dependency components of size ≥2.
- 35,625 self-loop arcs (`root`, `NonRel`) which by construction cross nothing.

### 2.2 Corpus census
- 6,236 verses across 114 surahs, hence **6,122 internal verse boundaries**.
- 291 verses have a synthetic row as their last row.

### 2.3 Waqf-mark join feasibility
- `quran-text/quran-no-tashkeel.json` carries the muṣḥaf pause-mark system, U+06D6–U+06DC:
  1,972 *jīm*, 1,682 *ṣlā*, 603 *qlā*, 68 *lā*, 22 *mīm*, 12 *muʿānaqa*, 5 *saktah*
  = 4,364 marks.
- Every mark is a standalone whitespace-separated token, and **every mark is mid-verse**
  (only 2 *saktah* sit on a verse-final word). EQTB's own token columns carry no waqf
  marks, so the join must come from the text.
- After one declared merge rule (below), **6,233 of 6,236 verses align 1:1** with EQTB
  `word_id`; 3 verses are excluded (20:94, 37:130, 72:16). **4,361 of 4,364 marks** land
  on a verse-interior EQTB word boundary and are usable.

### 2.4 Register labels
Reused verbatim from `findings/phase-b-hypotheses/csv/h-new-2500.json`
→ `genre_proxy.surah_genre`: 40 `eschatological_mufassal`, 31 `narrative`,
23 `liturgical_didactic`, 20 `legal_medinan`.

---

## 3. THE CIRCULARITY PROBLEM — stated head-on before any result

**The threat.** If EQTB annotators segmented sentences *at* āya boundaries, then "no arc
crosses the boundary" would be true by annotation fiat, and H1 would measure the
annotation convention rather than the text.

**Why the threat is real and not merely hypothetical.** A dependency analysis of a
sentence is largely connected. If a verse boundary falls strictly inside a sentence whose
graph is connected across it, at least one arc *must* cross. Therefore, up to the 1,336
sentences with ≥2 non-trivial components, **SEALED is close to — though not identical
with — "this verse boundary is also an EQTB sentence boundary."** Any reader of the
finding must be told this in plain words, and the finding will say it.

**What the pre-lock census establishes.** Sentence segmentation is *not* a relabelling of
verse segmentation:
- 57.9% of sentences begin mid-verse. Verse-driven segmentation would give ≈0%.
- 838 sentences run past a verse boundary, one of them across 31 verses. Verse-driven
  segmentation would give 0.

So the annotators split on syntactic grounds. What **cannot** be excluded from the data is
the weaker contamination: that annotators used the āya boundary as a *tie-breaking prior*,
splitting there when the syntax permitted it. Nothing in EQTB distinguishes that from a
genuine textual property.

**Consequence for the verdict, locked now.** H1a is **circularity-exposed** and can never
by itself license a claim about the text. The family is therefore built so that the weight
falls on three progressively less exposed instruments:

| Inference | Exposure to the annotation convention |
|:--|:--|
| H1a (arc-sealing vs within-verse pseudo-boundaries) | **High** — near-equivalent to sentence-boundary coincidence |
| H1b (within-sentence segment permutation) | **Low** — restricted to sentence-internal boundaries by construction, but expected to be low-powered and possibly degenerate |
| H4 (constituent integrity) | **Lower** — constituent spans are sub-sentential |
| H5 (classical waqf grades) | **None from EQTB sentence segmentation** — evaluated only at mid-verse positions, against a 12th-century annotation with no dependency-grammar provenance |

**H5 is the decisive test of the instrument.** If EQTB arc-crossing tracks al-Sajāwandī's
pause grades at positions that are not verse boundaries at all, then the crossing measure
is measuring syntax, not verse layout. If H5 fails, the whole family is
CIRCULARITY-LIMITED and will be reported as such regardless of H1a.

---

## 4. Frozen inputs (SHA-256)

1. EQTB `Quranic.csv`, UTF-16, tab-delimited, via the UD-Quran reproducibility package —
   `a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7`.
   Provenance and licence: `data/syntax/UD-QURAN-SOURCE.md`.
2. `quran-text/quran-no-tashkeel.json` (waqf marks + word sequence) —
   `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a`.
3. `findings/phase-b-hypotheses/csv/h-new-2500.json` (register labels, reused verbatim) —
   `a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25`.

EQTB is authoritative for tokenisation, dependency arcs and constituent spans. The Quran
text is used only to carry waqf marks and to verify the word-index join.

---

## 5. Deterministic extraction

### 5.1 Linear position and cuts
Within each surah, order **all** EQTB rows (real and synthetic) by `tid` → index
`0 … N−1`. Every row carries `chapter_id`/`verse_id`/`word_id`.

A **cut** `k` is the gap between index `k` and `k+1`. One rule fixes every cut used
anywhere in this study — *the index immediately before the first row of the next unit* —
which deterministically attaches synthetic rows to the left:

- **True boundary** after verse `v` (`v = 1 … V_c−1`): `k = (first row index of verse v+1) − 1`.
- **Interior word boundary** after word `j` of verse `v` (`j = 1 … n_v−1`):
  `k = (first row index of word j+1 of verse v) − 1`.

Pseudo-boundaries are drawn only from interior **word** boundaries, matching the true
boundary, which is always a word boundary. Cuts never fall inside a word.

### 5.2 Arcs, sealing, crossing
Each row contributes the arc `token_id → ref_token_id` within its `sentence_id`;
self-loops are dropped. `(sentence_id, token_id)` maps to a surah linear index. An arc
crosses cut `k` iff `min(idx_a, idx_b) ≤ k < max(idx_a, idx_b)`.

- `CROSS(k)` = number of arcs crossing `k`.
- `SEALED(k)` = `CROSS(k) == 0`.

### 5.3 Constituent spans
Rows with `is_constituent == 1` carry `constituents_loc` of the form `[a-b]` (sentence-local
`token_id` range). `SPLITS(k)` = at least one constituent span `[a,b]` has
`idx(a) ≤ k < idx(b)`.

### 5.4 Waqf marks
Parse each verse of `quran-no-tashkeel.json`. A token composed only of U+06D6–U+06ED is an
annotation mark, not a word; the waqf subset U+06D6–U+06DC records a pause grade attached
to the cut **after the preceding real word**. One declared orthographic merge rule is
applied because QAC/EQTB joins proclitics that the text writes separately: a token in
`{يا, ويا, ها, فيا}` is merged with the following token. A verse enters the waqf analysis
only if its resulting word count equals its EQTB `word_id` count exactly; otherwise it is
excluded and counted. (Pre-lock: 3 verses excluded, 4,361 of 4,364 marks retained.)

Pause grades, per the muṣḥaf convention descended from al-Sajāwandī's *ʿIlal al-wuqūf* as
standardised in the King Fahd Complex muṣḥaf:

| Mark | Symbol | Meaning | Class |
|:--|:-:|:--|:--|
| *mīm* | ۘ | *waqf lāzim* — obligatory stop | STOP-PREFERRED |
| *qlā* | ۗ | *al-waqf awlā* — stopping preferable | STOP-PREFERRED |
| *ṣlā* | ۖ | *al-waṣl awlā* — continuing preferable | CONTINUE-PREFERRED |
| *lā* | ۙ | *lā waqf* — do not stop | CONTINUE-PREFERRED |
| *jīm* | ۚ | *waqf jāʾiz* — permissible, explicitly neutral | EXCLUDED (reported descriptively) |
| *muʿānaqa*, *saktah* | ۛ ۜ | embracing pause, brief silence | EXCLUDED |

---

## 6. Registered inferences, with directions locked

Six inferences. Bonferroni `α_bon = 0.05/6 = 0.008333`. The project novelty rule
(`docs/statistical-rigor-protocol.md` §5: corrected `p < 0.005`) is stricter and governs,
so the **raw decision gate is `0.005/6 = 0.000833`**. All Monte-Carlo nulls use 10,000
draws; the attainable floor is `p = 1/10001 ≈ 9.999 × 10⁻⁵`, below the gate.

One-sided `p = (1 + #{null ≥ observed}) / 10001` throughout, in the locked direction.

### H1a — the fāṣila seals more often than a matched within-verse word boundary
Universe `U_A`: true internal verse boundaries whose host verse has ≥2 EQTB words.
`s_true` = sealed-rate over `U_A` (deterministic). Each null draw places, for every
boundary in `U_A`, one pseudo-cut uniformly among the interior word boundaries of the
**same** verse — so the null is length-matched at the verse level by construction.
- **Locked direction:** `s_true > mean_b(s_pseudo^(b))`.
- Seed 20260509.

### H1b — sealing survives permutation of segment lengths inside a sentence
Universe `U_B`: true internal verse boundaries strictly inside an EQTB sentence. For each
sentence spanning `m ≥ 2` verses, the `m−1` internal boundaries cut it into `m` row
segments; a null draw permutes the multiset of segment lengths and reads off the new cuts.
- **Locked direction:** `s_true(U_B) > mean_b(s_perm^(b))`.
- Seed 20260510.
- **Pre-registered expectation:** low power, and possibly degenerate at 0 on both sides
  because a connected sentence graph forces a crossing at every internal cut. A null here
  is anticipated and is not evidence against H1a; it is evidence about the instrument, and
  will be reported as such.

### H2 — the eschatological register seals more than the legal register
Register labels reused verbatim from `h-new-2500.json`. Over all true internal verse
boundaries, `Δ_H2 = s(eschatological_mufassal) − s(legal_medinan)`.
Null: permute the 114 surah→register labels, preserving the label multiset.
- **Locked direction:** `Δ_H2 > 0`.
- Seed 20260509.

### H3 — the effect is not a verse-length artefact
Strata by host-verse EQTB word count `n_v`, bins fixed here a priori:
`[2–4], [5–8], [9–15], [16–30], [31+]`. Using the H1a machinery and the same 10,000 draws,
`Δ_stratum = s_true(stratum) − mean_b(s_pseudo^(b), stratum)`. The H3 statistic is the
**equal-weight mean of `s_true` across strata with ≥100 eligible boundaries**, compared
against the equal-weight mean of each null draw, so that no single stratum dominates.
- **Locked direction:** equal-weight `s_true > ` equal-weight null mean.
- Seed 20260509.
- **If H1a passes and H3 fails, the effect is a verse-length artefact and the finding must
  say exactly that.** Per-stratum Δ and per-stratum p are reported descriptively.

### H4 — āya boundaries break fewer phrases than chance word boundaries
`SPLITS` rate over `U_A`, H1a machinery and draws.
- **Locked direction:** `split_rate(true) < mean_b(split_rate(pseudo^(b)))` — i.e. the
  true boundary is the *less* disruptive one. Note this direction is the reverse sign of
  H1a's, and is locked deliberately.
- Seed 20260509.

### H5 — EQTB arc-crossing reproduces the classical pause grades (the external validation)
Universe: usable mid-verse waqf-marked word boundaries classed STOP-PREFERRED
(*mīm* + *qlā*) or CONTINUE-PREFERRED (*ṣlā* + *lā*). No verse boundary is in this
universe.
`Δ_H5 = s(STOP-PREFERRED) − s(CONTINUE-PREFERRED)`.
Null: permute the STOP/CONTINUE labels across the marked positions, preserving both counts.
- **Locked direction:** `Δ_H5 > 0` — where the classical tradition says stopping is
  preferable, the dependency structure should be closed; where it says continue, it should
  be open.
- Seed 20260509.
- *jīm* (explicitly neutral) is reported descriptively and is **predicted to fall between**
  the two classes. That prediction carries no p-value and cannot rescue a failed H5.

---

## 7. Robustness, controls and rosters (descriptive; no p-values, no addition to k)

1. **R1** — census of EQTB sentences spanning >1 verse, with the verses-per-sentence
   distribution. This is itself a headline result.
2. **R2 — the circularity exhibit**: the fraction of true boundaries that coincide with an
   EQTB sentence boundary, beside the same fraction for pseudo-boundaries.
3. **R3** — mean and median `CROSS(k)` at true versus pseudo boundaries.
4. **R4** — sealed-rate conditional on the boundary being sentence-internal, true versus
   pseudo. The decontaminated comparison in descriptive form.
5. **R5** — variant with all arcs incident to synthetic rows dropped.
6. **R6 — the exception roster**: the true verse boundaries with the highest `CROSS(k)`,
   reported with surah, verse, register, and the classical waqf context of the host verse.
   These are the corpus's *taḍmīn* points.
7. **R7 — replication**: H1a re-run at seed 20260510 and H5 at seed 20260511.
8. **R8** — sealed-rates for all four registers, not only the two contrasted in H2.
9. **R9** — the full waqf-grade ladder (*mīm*, *qlā*, *jīm*, *ṣlā*, *lā*) with sealed-rate
   and mean `CROSS` per grade, to show whether the ordering is monotone.

---

## 8. Decision language, locked

- **H5 fails** ⇒ the entire family is `CIRCULARITY-LIMITED`, whatever H1a shows. The
  instrument would not have been shown to measure syntax independently of verse layout.
- **H5 passes and H1a passes and H3 passes** ⇒ `FĀṢILA-AS-CLAUSE-SEAL SUPPORTED,
  EQTB-ANNOTATION-LIMITED`, with the explicit rider that H1a is substantially a statement
  about EQTB sentence segmentation and that the residual tie-breaking-prior contamination
  cannot be excluded from this data.
- **H1a passes, H3 fails** ⇒ `LENGTH-ARTEFACT`. The effect is carried by verse length and
  not by boundary placement. Stated plainly, not softened.
- **H1a fails or reverses** ⇒ `NULL`. Do not rescue with H1b, H4 or a changed threshold.
- **H4 reverses** (āya boundaries split *more* phrases) ⇒ published as a pre-commit
  violation with full prominence.
- Every outcome is an **annotation-limited association** in the EQTB dependency profile,
  not a fact about Arabic syntax in general. It is not Quran-specific without a matched
  Classical-Arabic dependency-treebank control, which does not exist on disk; the finding
  will say so.

---

## 9. Deviations from the dispatched specification, logged before the run

The dispatch registered H1, H2 and H3. Two inferences are added, and the reason is
recorded here rather than after seeing results:

- **H4 (constituent integrity)** and **H5 (classical waqf grades)** are added because the
  dispatch identified circularity as the material risk, and §3 shows that H1a alone cannot
  answer it. H4 lowers the exposure; H5 removes it. Adding them *tightens* the family from
  k=4 to k=6 and therefore tightens every gate; no inference is loosened.
- The dispatch's Null A wording "uniformly at random among the interior token positions" is
  implemented at **word** boundaries rather than segment boundaries, because a true verse
  boundary is always a word boundary and a segment-level null would compare unlike with
  unlike. This is a fairness correction to the null, and it makes the null *harder* to beat.
- No other change. H1a, H1b, H2 and H3 are as dispatched, with the seeds as dispatched.

---

## 10. Required immutable run record

`findings/phase-b-hypotheses/runs/h-new-2560/<UTC timestamp>/` containing `result.json` and
`manifest.json` (command, git commit, all input SHA-256, script SHA-256, Python version,
platform, seeds, permutation count). Nothing in an earlier run directory may be
overwritten. The human-readable finding is written afterwards; the runner emits no
interpretive prose.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
