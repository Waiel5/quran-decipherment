---
id: H-NEW-2720
title: "PRE-REGISTRATION — The genre-control sweep: do the remaining standing laws discriminate the Qurʾān from matched Arabic corpora?"
type: pre-registration
status: LOCKED-BEFORE-COMPUTATION
date: 2026-08-07
author: Waiel Al-Shujaa
phase: C
seed: 20260509
seed_replication: 20260519
parent: H-NEW-2680
---

# PRE-REGISTRATION — H-NEW-2720

**Nothing in this file may be amended after the SHA-256 below is computed.** The run
script embeds it as a literal and exits non-zero on mismatch. Seed 20260509, replication
20260519. Immutable run directory
`findings/phase-b-hypotheses/runs/h-new-2720/<UTC timestamp>/`, manifest paths
repo-relative so the directory is committable. **Run directories are never deleted.**

---

## 0. Why, and what the honest expectation is

H-NEW-2680 ran the control that should have existed years ago. Partitioning
`data/baseline-corpora/` into 114 pseudo-surahs matched to the Qurʾān's verse
word-length and verse-count profile, and re-running the four pillar laws through an
instrument-matched surface pipeline, **pre-Islamic poetry satisfied 3 of the 4**. Pillar 2
inverted outright: Qurʾān z = −11.50, al-Bukhārī −13.84, poetry −15.13 — both baselines
*more* "optimal" than the Qurʾān, the whole effect an artefact of textual contiguity and
block size.

**The inference is obvious and it is the reason for this test: almost every other standing
law in this project has never been run against a matched Arabic control either.** This
sweep runs them.

**Honest expectation, locked here:** I expect **most of these laws not to discriminate**,
and I expect at least one **reversal** (a baseline more extreme than the Qurʾān), because
the length-matched partition hands the baselines the Qurʾān's own size profile, and 2680
showed that the size profile alone generates much of what these instruments measure.
I also expect **at least one law to survive as GENRE-SHARED-BUT-LARGER**, and that
outcome must not be collapsed into "worthless" — an over-retraction is as dishonest as
the original overclaim. Both directions are pre-registered as reportable.

---

## 1. Frozen inputs (SHA-256, verified at runtime; mismatch ⇒ exit)

| Path | SHA-256 |
|:--|:--|
| `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |
| `quran-text/quran-min-tashkeel.json` | `87aaab41f78d1b148c8051b8afc1ee5fa66fd6d45f2f7a2984e3f9192c458b36` |
| `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| `data/baseline-corpora/raw/bukhari-noquran.txt` | `0169b60de7585a51fc340161488534c4d909370c3dcc8951ca2ae3818c44a100` |
| `data/baseline-corpora/raw/jahiz-hayawan.txt` | `419095484df4e315eba889d38a9c2f6edff55c2f10f481ed9ad024e07bbff0cd` |
| poetry: the 14 `muallaqa-*.txt` + `diwan-*.txt` files, concatenated in sorted order | `f6c5525ddfa8d06ca974cbc937ad1f7f96839418e2eabdd3b94f8fce66fb983a` |
| `findings/phase-b-hypotheses/scripts/h-new-2680.py` (partitioning code reused) | `57d6b214344ea81433e9f840524e6259953657fbf60e8fd54fdd8d2706b88497` |

---

## 2. Corpora and partition — reused from H-NEW-2680, not re-implemented

`normalise_words()` and `build_pseudo_corpus()` are **copied verbatim** from
`scripts/h-new-2680.py` (strip diacritics and taṭwīl, drop non-Arabic, split on
whitespace; cut the word stream into 6,236 units matching the Qurʾān's verse word-length
profile *in order*; group into 114 pseudo-surahs by the canonical verse-count profile).
Comparability with 2680 is the point; re-implementing would introduce differences that
muddy the comparison. The run asserts byte-identity of the two function bodies against
the frozen 2680 source.

| id | corpus | partitions |
|:--|:--|:--|
| **QURAN-SURF** | the Qurʾān's real 114 surahs, **surface-word instrument** | 1 (canonical) |
| **BL-POETRY** | pre-Islamic poetry, 14 files (7 muʿallaqāt + 7 dīwāns) | **1 only** |
| **BL-BUKHARI** | al-Bukhārī (`bukhari-noquran.txt`) | **200** seeded offsets |
| **BL-JAHIZ** | al-Jāḥiẓ, *Kitāb al-Ḥayawān* — **a third genre 2680 did not use** | **200** seeded offsets |

**Every law is computed on QURAN-SURF through the identical surface instrument, and the
baselines are compared to that value only — never to a published QAC-root headline.**
Published QAC values are quoted for reference and are never the comparator. This is
2680's rule and it is retained.

**The poetry corpus supports exactly one partition.** It totals 82,520 words against the
82,375 the partition consumes — 145 words of slack. No offset resampling is possible, so
poetry yields a single point estimate with no band. Bukhārī (526,250 words) and al-Jāḥiẓ
(340,213) support 200 offsets each, drawn uniformly from the admissible range at seed
20260509, giving a genuine null band per law. **This is an improvement on 2680, which used
single partitions throughout.**

### 2.1 Arm 2 — the length-confound isolator (locked here, not post-hoc)

The length-matched partition hands every baseline the Qurʾān's own surah-size profile, and
the Qurʾān's surahs shorten toward the end (2680 §8.1: Spearman(position, verse count)
= −0.846). Several of the laws under test are gradients *in position*, so the partition
could manufacture them. **Arm 2 therefore re-cuts every corpus — including the Qurʾān's own
verse stream — into 114 pseudo-surahs of UNIFORM verse-count (54 or 55 each, order
preserved), and re-runs the gradient laws G1–G4.** If the Qurʾān's own compression tail
survives its surah boundaries being replaced by equal-size cuts, the law is about the text;
if it vanishes, the law is about the size profile. This is the direct analogue of 2680 §8's
offset-cut diagnostic and it is pre-registered, not discovered.

---

## 3. The target list — locked before any computation

Ten laws. Seven are testable; three are declared non-testable *here*, with reasons, rather
than silently dropped.

| id | law | test statistic (transported) | published Qurʾān value | source |
|:--|:--|:--|:--|:--|
| **G1** | H-NEW-660 content compression-tail | R² and slope β of `d̄ = α + β·max(0, s−50)` fitted to d̄_content over the 100 K=15 surah-windows; d̄ = mean pairwise Fisher-Rao distance, Dirichlet α=0.5, top-500 types | R² = 0.9860, β = −0.01237 | `h-new-660` |
| **G2** | H-NEW-700 rhyme dispersion-tail | same fit to d̄_rhyme = mean pairwise cosine distance on the 28-letter unit-final-letter vector | R² = 0.789, β > 0 | `h-new-700` |
| **G3** | H-NEW-700 phoneme dispersion-tail | same fit, **kink at s=75**, to d̄_phoneme = cosine on the 4-class phoneme-proportion vector (emphatic / pharyngeal / sibilant / glottal) | R² = 0.946 | `h-new-700` |
| **G4** | H-NEW-770 verse-length compression-tail | same fit (kink 50) to mean **letters per unit**; the words-per-unit arm is **DEGENERATE BY CONSTRUCTION** (see §5) | R² = 0.807 (letters) | `h-new-770` |
| **G5** | H-NEW-730/740 iʿjāz anti-twin | Pearson r(d̄_content, d̄_rhyme) across the 100 windows | r = −0.8643 | `h-new-730` |
| **G6** | cf-026-formal, mechanism 2 — anti-chiasmus | mean permutation-z of the pericope-window ring score over all windows of sizes {5,7,9,11,13} | mean z ≈ −0.15 (corpus anti-chiastic) | `h-new-2220` |
| **G7** | cf-028-formal register separability | leave-one-out nearest-centroid accuracy of a 6-feature thin-grammar vector over a 3-way partition, reported as **lift over that partition's majority baseline** | 0.7692 / 0.4396 = **1.75×** | `h-new-2530` |
| **G8** | H-NEW-840 UAS | **NOT A DISCRIMINATION CLAIM** — a composite ranking index with no null hypothesis. Diagnostic only: dispersion (sd) of the index across the 114 units | — | `h-new-840` |
| **G9** | cf-025-formal pericope-flip | **already controlled by H-NEW-2680** (poetry 5/5, Bukhārī 4/5). Extended here with al-Jāḥiẓ and with **flip magnitudes**, not counts | 5/5 flips | `cf-025-formal` + 2680 §7 |
| **G10** | cf-027-formal eponymy-independence | **NOT TRANSPORTABLE** — its title-density arm was withdrawn and replaced by H-NEW-2710; its remaining arm is a 5-cycle centrality claim with no baseline analogue (pseudo-surahs have no eponyms). Declared, not tested | — | `cf-027-formal` |

### 3.1 G7's surrogate labels — declared, because it is the weakest transport here

cf-028's law needs a 3-way register partition. The baselines have no register ground
truth, so a **surrogate** 3-way label is used and named as such: for BL-POETRY the three
largest source dīwāns; for BL-BUKHARI and BL-JAHIZ three contiguous thirds of the stream
(which track different *kutub* / *abwāb* topics). The six features are computed by surface
match on `إذ`, `لما`, `قالوا`, `إذا`, `ثم`, and first/second/third-person pronoun-shift
density. **A surrogate label is not a register label**, so G7's verdict is capped: it can
show that the lift is *reachable* on ordinary Arabic, which is the discriminating question,
but it cannot show that baselines have registers.

---

## 4. Decision language — locked, every outcome

For each law, `Q` is the Qurʾān's surface-instrument value and the baseline comparison is
made against **all three** baselines.

| verdict | condition |
|:--|:--|
| **DISCRIMINATES** | `Q` is more extreme, in the pre-locked direction, than BL-POETRY **and** than the full 200-draw range of BL-BUKHARI **and** BL-JAHIZ |
| **GENRE-SHARED-BUT-LARGER** | at least one baseline satisfies the law's qualitative form, but `Q`'s magnitude exceeds every baseline value by the pre-locked margin below. **This is a real, reportable, intermediate outcome and is NOT collapsed into "does not discriminate."** |
| **GENRE-SHARED** | at least one baseline's value lies within the pre-locked margin of `Q` |
| **DOES-NOT-DISCRIMINATE-REVERSED** | at least one baseline is **more extreme than the Qurʾān**. Published with full prominence — this was 2680's most damaging finding shape and a binary pass/fail would have hidden it |
| **NOT-TRANSPORTABLE** | no baseline analogue exists; reason stated |
| **DEGENERATE-BY-CONSTRUCTION** | the partition forces the baseline value to equal `Q` |

**The pre-locked margin.** For R²-valued laws (G1–G4): `Q` counts as materially larger iff
`R²_Q − max(R²_baseline) ≥ 0.10`. For correlation-valued laws (G5): iff
`|r_Q| − max|r_baseline| ≥ 0.20` (the same margin H-NEW-740 effectively used: 0.86 vs 0.48).
For z-valued (G6) and lift-valued (G7): iff `Q` lies outside the baseline's full 200-draw
range **and** differs by ≥ 25 % of the Qurʾān's own magnitude.

**Direction lock.** For every law the pre-registered alternative is that the **Qurʾān is
more extreme than the baselines**. That is what each law is cited as showing. Any baseline
exceeding the Qurʾān is a **pre-commit direction reversal**, published as such per Protocol
§1.8, not massaged and not re-pointed.

**Reporting rule.** Every law reports **direction and magnitude**, never pass/fail alone.
2680's most damaging finding was that the baselines were *more* extreme, and a binary
verdict would have concealed it.

---

## 5. Degeneracies declared in advance

- **G4 words-per-unit is degenerate.** `build_pseudo_corpus` cuts every baseline into units
  matching the Qurʾān's verse word-length profile *exactly and in order*. Words-per-unit is
  therefore **identical** across all four corpora by construction, and the H-NEW-770
  words/verse arm **cannot be controlled by this design**. Only the letters-per-unit arm is
  testable, and even it inherits the word-count profile. Stated now so it cannot later look
  like a finding.
- **Every G1–G4 baseline inherits the Qurʾān's surah-size profile**, which is exactly the
  confound Arm 2 exists to isolate. A baseline reproducing a gradient law is therefore
  evidence that the gradient rides on size, not that the baseline "also has the law".
- **G6's ring statistic is invariant to word identity within a unit** for some
  formulations; the transported version uses the unit-level token-set Jaccard mirror score,
  which is not.

---

## 6. Nulls, seeds, replication

- Baseline offsets: 200 per resampleable corpus, seeded 20260509 (replication 20260519).
- G6's per-window ring null: 1,000 within-unit order permutations per window, seeded.
- G7's LOO classifier: deterministic; the majority baseline is computed from the same
  label vector.
- No Bonferroni is applied *across* the ten laws, and the reason is stated: this is a
  **control sweep**, not a discovery sweep. Each law is an independent pre-existing claim
  being audited on its own terms, and correcting across them would make it *harder* to
  detect a law's failure — the anti-conservative direction for an audit whose purpose is to
  find failures. Where a single law has internal multiplicity (G6's window family), that
  multiplicity is corrected within the law.

---

## 7. MW-1 … MW-7

- **MW-1** — every statistic, margin, direction and verdict label fixed here before any
  baseline value is computed.
- **MW-2** — 200 offset partitions per resampleable baseline; 1,000 permutations per ring
  window.
- **MW-3** — two partition arms (length-matched, uniform); three baselines spanning three
  genres (verse, ḥadīth, adab prose).
- **MW-4** — no fitted parameters beyond the three model forms the original laws
  themselves compare; kink positions are taken from the published laws, not refitted.
- **MW-5** — replication at seed 20260519.
- **MW-6** — instrument controls, all fail-fast: the partition functions must be
  byte-identical to 2680's; QURAN-SURF must reproduce 2680's `z = −11.50` Fisher-Rao
  anchor to within Monte-Carlo error; the Qurʾān's QAC-instrument G1 fit must reproduce
  R² = 0.986; the corpus must contain 114 surahs and 6,236 verses.
- **MW-7** — any pattern noticed during the run that is not one of the ten declared laws is
  descriptive only, carries no p-value, and cannot change a verdict.

---

## 8. Honest limits, stated in advance

1. **Two — now three — matched corpora is not a corpus of corpora.** Poetry, ḥadīth and
   adab prose are the only matched Arabic texts on disk. Three genres cannot establish
   what "Arabic in general" does.
2. **A partition is not a composed book.** The pseudo-surahs are arbitrary cuts of a
   continuous stream. **A law failing to discriminate against an artificial partition is
   weaker evidence against the law than it first appears** — the baseline units were never
   authored as units, so any structure they show is the more remarkable, but any structure
   they *lack* may be an artefact of their arbitrariness rather than of their genre. This
   asymmetry is stated for every law individually in the finding.
3. **The direction of the partition's bias is not uniform across laws.** For contiguity-
   sensitive statistics (G1, G5) arbitrary cuts of a continuous stream *preserve* local
   continuity and should make the law *easier* for baselines — so a baseline pass is weak
   evidence. For unit-boundary-sensitive statistics (G6) arbitrary cuts *destroy* boundary
   structure and should make the law *harder* — so a baseline pass there is strong
   evidence. Each verdict states which regime it is in.
4. **BL-POETRY has no band.** One partition, 145 words of slack. Its value is a point
   estimate and is treated as such.
5. **The surface instrument is shallower than QAC.** No baseline has root annotation, so
   every arm runs on surface word-types. This biases every content statistic toward
   *weaker* values in the baselines (H-NEW-740 §4.1 made the same declaration), so a
   baseline that matches or exceeds the Qurʾān under this instrument would do so more
   strongly under a better one.
6. **G7's baseline labels are surrogates** (§3.1) and its verdict is capped accordingly.
7. **G8 is not a test.** UAS has no null hypothesis; only a dispersion diagnostic is
   reported and no verdict is issued.
8. **`numpy` is used**, the same disclosed deviation from Protocol §7.1 that H-NEW-2680
   declared, for the Fisher-Rao matrices and permutation arithmetic.

---

## 9. Deliverables

- pre-reg: this file (SHA-256 embedded in the script, verified at runtime)
- script: `findings/phase-b-hypotheses/scripts/h-new-2720.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2720.json`
- run dir: `findings/phase-b-hypotheses/runs/h-new-2720/<UTC timestamp>/` with a
  repo-relative `manifest.json`
- finding: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`

The finding must report, for **every** law: the transported statistic, the Qurʾān's
surface-instrument value, all three baseline values with bands, **the direction and the
magnitude of any gap**, and the verdict from §4 — including every reversal.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any baseline statistic was computed. A law
that has never met a control is a description, not a law. Bismillāhi al-Raḥmāni al-Raḥīm.*
