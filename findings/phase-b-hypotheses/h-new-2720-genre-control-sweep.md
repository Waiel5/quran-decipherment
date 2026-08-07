---
finding_id: H-NEW-2720
title: The genre-control sweep — nine standing laws met a matched Arabic control for the first time, and none of them discriminates
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
prereg: findings/phase-b-hypotheses/prereg-h-new-2720-genre-control-sweep.md
prereg_sha256: 24a5bc8dd2352151f6557a0415cb177f69e60f8fca5f1ccf39ff3c57b2e0040d
seeds: 20260509 primary / 20260519 replication
parent: H-NEW-2680
status: >-
  0 of 9 testable laws DISCRIMINATE. Four are REVERSED (a matched baseline is more
  extreme than the Qurʾān), four are GENRE-SHARED, one is DEGENERATE-BY-CONSTRUCTION.
  One axis survives as GENRE-SHARED-BUT-LARGER: the post-kink content-compression
  SLOPE, steeper than 200/200 ḥadīth and 198/200 adab-prose partitions.
verdict: >-
  The compression-tail family and the iʿjāz anti-twin do not distinguish the Qurʾān from
  length-matched partitions of al-Bukhārī or al-Jāḥiẓ. The anti-twin is REVERSED: the
  Qurʾān sits at the 14th percentile of ḥadīth and the 3rd of adab prose. H-NEW-740's
  Δ Fisher-z = −6.42 is an artefact of comparing the Qurʾān's unequal surahs to poetry's
  equal 30-bayt blocks — under a matched partition poetry reaches r = −0.872 against the
  Qurʾān's −0.870. Half the anti-twin and 91.5 % of the compression tail are explained by
  unit SIZE alone.
---

# H-NEW-2720 — The genre-control sweep

**Pre-reg SHA-256 `24a5bc8d…040d`, runtime-verified. Six frozen inputs plus the 14-file
poetry corpus SHA-verified. The pseudo-surah construction is lifted verbatim from
H-NEW-2680 and its source text is SHA-checked at runtime, so the partition cannot drift
from the one 2680 used.**

---

## Headline

H-NEW-2680 ran this project's first genre control and pre-Islamic poetry satisfied 3 of
the 4 pillar laws. The obvious inference was that every other standing law was suspect for
the same reason, because almost none had ever met a matched Arabic control. **This sweep
ran nine of them against three matched corpora — pre-Islamic poetry, al-Bukhārī, and
al-Jāḥiẓ's *Kitāb al-Ḥayawān*, a third genre 2680 did not use — and not one law
discriminates.**

| # | law | Qurʾān (surface) | poetry | al-Bukhārī (200 cuts) | al-Jāḥiẓ (200 cuts) | verdict |
|:--|:--|--:|--:|--:|--:|:--|
| **G1** | H-NEW-660 content compression-tail, R² | **0.9887** | 0.8633 | 0.9577 [0.893–0.990] | 0.9686 [0.927–0.991] | **GENRE-SHARED** (Qurʾān at 99.5 / 99.0 pctile) |
| **G1b** | …its post-kink **slope** β | **−0.01343** | −0.0133 | −0.0101 [−0.0113, −0.0088] | −0.0124 [−0.0136, −0.0114] | **GENRE-SHARED-BUT-LARGER** — steeper than 200/200 and 198/200 |
| **G2** | H-NEW-700 rhyme dispersion-tail, R² | 0.7983 | 0.6842 | 0.7941 [0.648–0.903] | 0.7972 [0.643–0.914] | **GENRE-SHARED** (51st / 50.5th pctile — dead centre) |
| **G3** | H-NEW-700 phoneme dispersion-tail, R² | 0.9329 | **0.9332** | 0.8846 [0.549–0.981] | 0.8904 [0.543–0.972] | **GENRE-SHARED** |
| **G4** | H-NEW-770 verse-length tail (letters), R² | 0.8073 | **0.8113** | 0.8098 [0.790–0.827] | 0.8107 [0.792–0.826] | **REVERSED** — 137/200 and 135/200 baselines exceed |
| **G4w** | …the words-per-verse arm | 0.8115 | 0.8105 | 0.8105 (all 200 identical) | 0.8105 (all 200 identical) | **DEGENERATE-BY-CONSTRUCTION** |
| **G5** | H-NEW-730/740 iʿjāz anti-twin, r | −0.8700 | **−0.8718** | **−0.9107** [−0.976, −0.775] | **−0.9311** [−0.986, −0.850] | **REVERSED** — Qurʾān at 14th / **3rd** percentile |
| **G6** | cf-026 anti-chiasmus, mean ring-z | −0.1363 | −0.1200 | −0.1458 | **−0.2095** | **REVERSED** — adab prose is more anti-chiastic |
| **G7** | cf-028 register separability, lift | 1.658 | **1.842** | 1.289 | 1.421 | **REVERSED** (capped — surrogate labels) |
| **G8** | H-NEW-840 UAS | 1.166 | **1.267** | 1.076 | 1.118 | **NOT-A-DISCRIMINATION-CLAIM** |
| **G9** | cf-025 pericope-flip | 5/5, max z +24.7 | 5/5, max z +22.4 | 4/5, max z +6.9 | 5/5, max z +12.0 | **GENRE-SHARED** (confirms + extends 2680) |
| **G10** | cf-027 eponymy-independence | — | — | — | — | **NOT-TRANSPORTABLE** |

**0 DISCRIMINATES · 4 REVERSED · 4 GENRE-SHARED · 1 DEGENERATE · 1 not-a-claim · 1
not-transportable.** Every headline number reproduces at seed 20260519 (§7.1).

The pre-registration's expectation — "most of these laws will not discriminate, and I
expect at least one reversal" — is what happened, and it is recorded at SHA `24a5bc8d…`
from before any baseline value was computed.

---

## 1. What was controlled, and how

The partition is **H-NEW-2680's, not a re-implementation**: `normalise_words()` and
`build_pseudo_corpus()` are extracted from the frozen 2680 source at runtime, their source
text SHA-checked against the values recorded when this script was written, and executed.
Each baseline word-stream is cut into 6,236 units matching the Qurʾān's verse word-length
profile in order, then grouped into 114 pseudo-surahs on the canonical verse-count profile.
Every law runs on **surface word-types for all four corpora**, and the Qurʾān is compared
to the baselines only through that identical surface instrument — never through a published
QAC-root headline. This is 2680's rule and it is retained.

**Two improvements on 2680.** (i) A **third genre**: al-Jāḥiẓ's *Kitāb al-Ḥayawān*
(340,213 words), 3rd/9th-century adab prose, which is neither verse nor ḥadīth. (ii)
**Bands instead of points**: al-Bukhārī (526,250 words) and al-Jāḥiẓ each support **200
seeded offset partitions**, so each baseline law has a distribution rather than a single
value, and the Qurʾān can be given a percentile within it. Pre-Islamic poetry cannot —
it totals 82,520 words against the 82,375 the partition consumes, leaving **145 words of
slack**, so poetry is a single deterministic point estimate with no band. That is stated
wherever a poetry number is used.

### Instrument controls (MW-6), all fail-fast, all passed

- The QAC-root instrument **reproduces H-NEW-660 exactly**: R² = **0.9860**, β = **−0.01237**
  against the published 0.9860 / −0.01237.
- The surface instrument reproduces the published values closely: G1 R² 0.9887 (QAC 0.9860),
  G4-letters 0.8073 (published 0.807), G5 r −0.8700 (published −0.8643), G6 mean-z −0.136
  (H-NEW-2220 published −0.15). **The surface transport is faithful, which is what makes a
  baseline matching it meaningful.**
- 114 surahs, 6,236 verses, 82,375 partition words asserted.
- The three lifted 2680 code fragments SHA-verified.

---

## 2. The two laws that matter most, and the mechanism that explains both

### 2.1 The compression tail is a unit-SIZE effect

Three independent lines converge.

**(a) A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
average R² = 0.9686 and reach 0.9913; al-Bukhārī's average 0.9577 and reach 0.9903. The
Qurʾān's 0.9887 sits at the **99.5th percentile of ḥadīth and the 99.0th of adab prose** —
genuinely high, and **1 of 200 and 2 of 200 draws still exceed it**. It fails the
pre-registered bar (outside the full 200-draw range of both) by one and two draws
respectively. That near-miss is reported rather than rounded in either direction.

**(b) Size alone explains 91.5 % of it.** Regressing the Qurʾān's own 100-window d̄ series
on **log(window mean word-count) and nothing else** — no position information whatever —
gives **R² = 0.9147**, with r(d̄, log size) = **+0.9564**. The published two-piece-kink
model gives 0.9887 on the same series; adding size to the kink model raises it only to
0.9918. The two predictors are largely redundant.

**(c) Equalise the sizes and the law nearly vanishes.** Re-cutting **the Qurʾān's own verse
stream** into 114 blocks of equal verse-count, order preserved:

| | R² | post-kink slope β |
|:--|--:|--:|
| real surah boundaries | **0.9887** | **−0.01343** |
| same verses, equal-size cuts | **0.3388** | **−0.00151** |

R² falls by two-thirds and the slope flattens **nine-fold**. The mechanism is elementary:
the mushaf's surahs shorten toward the end (Spearman(position, verse count) = −0.846,
2680 §8.1); short units have sparse word-type vectors; under Dirichlet smoothing their
probability vectors are pulled toward the prior; Fisher-Rao distances between them shrink.
**d̄ falls at the end of the mushaf because the surahs are short, not because they are more
cohesive.**

**What survives.** The arithmetic of H-NEW-660 is exact and is not challenged — it
reproduces to four decimals. And **one axis survives the control**: with the size profile
held *identical* by construction, the Qurʾān's post-kink slope β = −0.01343 is steeper than
**all 200** ḥadīth partitions and **198 of 200** adab-prose partitions. Its content-distance
falls about a third faster than al-Bukhārī's under the same size profile. That is a real
residual content effect, it is the only place in this entire sweep where the Qurʾān leads,
and it is **one axis of one law** — not the R² = 0.986 headline the law is cited for.

### 2.2 The iʿjāz anti-twin is REVERSED, and H-NEW-740's discrimination is an artefact

This is the most consequential result in the sweep.

| corpus | r(d̄_content, d̄_rhyme) | Qurʾān's percentile |
|:--|--:|--:|
| **Qurʾān** (surface, matched) | **−0.8700** | — |
| pre-Islamic poetry, matched partition | **−0.8718** | 0 / 1 |
| al-Bukhārī, 200 cuts | mean **−0.9107** [−0.976, −0.775] | **14th** — 172/200 more extreme |
| al-Jāḥiẓ, 200 cuts | mean **−0.9311** [−0.986, −0.850] | **3rd** — 194/200 more extreme |

**On the statistic that al-Bāqillānī's *iʿjāz al-fawāṣil* was said to be vindicated by, the
Qurʾān sits in the bottom decile of 3rd/9th-century zoological prose.**

H-NEW-740 reported poetry at r = −0.4801 against the Qurʾān's −0.8643, a Fisher-z gap of
−6.42 at p = 1.3 × 10⁻¹⁰, and concluded the claim "empirically vindicated". **Under a
matched partition the same poetry corpus reaches −0.8718.** The difference is not the
corpus; it is the units. H-NEW-740 cut poetry into **equal 30-bayt blocks** and compared
them to the Qurʾān's **wildly unequal surahs** (10 words to 6,140). That is an unmatched
comparison, and the mismatch is precisely what generates the statistic:

- r(d̄_content, log unit size) = **+0.9564** — content-distance rises with unit size
- r(d̄_rhyme, log unit size) = **−0.8376** — rhyme-distance falls with unit size

Small units simultaneously have low content-distance (sparse vectors pulled to the prior)
and high rhyme-distance (few verses, so near-one-hot final-letter vectors that are almost
orthogonal). A corpus with a *dispersed* size profile therefore manufactures an anti-twin;
a corpus of *equal* blocks cannot. Controlling for it:

| | r(content × rhyme) |
|:--|--:|
| raw | **−0.8700** |
| partial, controlling log unit size | **−0.4318** |
| partial, controlling log verse-count | −0.6524 |
| the Qurʾān's own verses re-cut to equal size | **−0.3375** |

**Two independent methods agree that roughly half to two-thirds of r = −0.86 is the size
gradient**, and the size-controlled residual (−0.43) is statistically indistinguishable
from what H-NEW-740 measured for *poetry* (−0.48) and called the genre baseline.

H-NEW-740 did consider block size, in its own honest-limits §3: *"Block size = 30 bayts vs
Quran median surah ≈ 50 verses. Smaller blocks reduce per-block content variance… This
biases AGAINST detecting strong content×rhyme structure, again favoring the iʿjāz
inference."* **That direction-of-bias reasoning was wrong on this specific point.** The
driver is not the size *level* but the size *dispersion*, and equal-size blocks suppress the
anti-twin rather than merely attenuating it. The honest-limits section anticipated the
variable and got its sign backwards — which is exactly why a matched control, not a
direction-of-bias argument, is the only way to settle these.

---

## 3. The other laws

**G2 rhyme dispersion-tail — GENRE-SHARED, and squarely so.** The Qurʾān's R² = 0.7983 sits
at the **51st percentile** of al-Bukhārī and the **50.5th** of al-Jāḥiẓ. 98 and 99 of 200
arbitrary prose cuts do it better. This is the cleanest non-result in the sweep: not a near
miss, not a reversal — the middle of the distribution.

**G3 phoneme dispersion-tail — GENRE-SHARED.** Qurʾān 0.9329; poetry 0.9332 edges it;
Bukhārī reaches 0.9813 and Jāḥiẓ 0.9721. The Qurʾān is at the 76.5th / 73rd percentile.

**G4 verse-length tail — REVERSED.** Qurʾān 0.8073 at the **31.5th / 32.5th percentile**;
137 and 135 of 200 baseline cuts are more extreme. Note the words-per-verse arm is
**degenerate by construction** — the partition copies the Qurʾān's verse word-length profile
verse by verse, so all 200 draws of both prose baselines return exactly 0.8105. That was
declared in pre-reg §5 before the run so it could not later be mistaken for a finding.

**G6 within-pericope anti-chiasmus — REVERSED.** All four corpora are anti-chiastic
(mean ring-z: Qurʾān −0.136, poetry −0.120, Bukhārī −0.146, **Jāḥiẓ −0.209**), and roughly
a third of windows are positive in each (0.339–0.370). cf-026's finding that the corpus is
anti-chiastic is **correct and reproduces** — the Qurʾān's −0.136 lands near H-NEW-2220's
published −0.15 on an independently written statistic. It is simply not a property of *this*
corpus: adab prose is more anti-chiastic still. **This arm had never been genre-controlled
before.**

**G7 register separability — REVERSED, with its verdict capped.** The transported statistic
is the leave-one-out nearest-centroid lift of a 6-feature thin-grammar vector over a 3-way
contiguous-thirds partition, computed identically for all four corpora. Qurʾān 1.658;
**poetry 1.842**; Bukhārī 1.289; Jāḥiẓ 1.421. **Two cautions, both pre-registered.** The
baselines' three-way labels are *surrogates* (contiguous thirds), not registers; and the
Qurʾān's 1.658 is its own contiguous-thirds lift, **not** cf-028's 1.75, which used the real
register labels. What this shows is only that a ~1.7× lift from thin grammar over a 3-way
split of Arabic text is **reachable without registers at all** — which is the discriminating
question — not that the baselines have registers. cf-028's own numbers are not challenged.

**G8 UAS — not a discrimination claim, and it fails its diagnostic anyway.** H-NEW-840's own
frontmatter reads `status: SYNTHESIS`; it is a composite ranking index with no null
hypothesis, so it cannot pass or fail a control. The one transportable diagnostic — how
differentiated the units are — puts the Qurʾān at 1.166 against **poetry's 1.267**. No
verdict is issued. *(A first implementation of this diagnostic was wrong: `np.eye(114) *
np.nan` is NaN everywhere, not just on the diagonal, because 0 × NaN = NaN, which silently
zeroed one of the three components. Corrected before the run; the uncorrected version made
the Qurʾān look highest, so the bug ran in the flattering direction.)*

**G9 pericope-flip — GENRE-SHARED, now with magnitudes and a third genre.** 2680 reported
counts; this reports the z's, as the task requires:

| corpus | flips | marker classes and z |
|:--|:-:|:--|
| **Qurʾān** | 5/5 | وكان +9.4 · واتقوا +10.6 · قومه +10.0 · **فبأي +24.7** · مؤمنين +9.1 |
| poetry | 5/5 | عبل +22.4 · أي +16.1 · **عبلة +19.4** · والجمع +11.4 · عبس +16.4 |
| al-Jāḥiẓ | 5/5 | الكتاب +9.4 · الكتب +10.3 · العلم +9.6 · النساء +8.4 · **الخصي +12.0** |
| al-Bukhārī | 4/5 | الإمام +6.9 · الإيمان +4.6 · الماء +1.6 · والذي +3.3 · ماء +2.7 |

The Qurʾān's largest flip (فبأي, the *al-Raḥmān* refrain, z = +24.7) and poetry's largest
(عبل, ʿAntara's beloved, z = +22.4) are the same order of magnitude. The flip tracks
**genre**, not scripture: the two verse-like corpora produce large z, the two prose corpora
smaller ones. A wholly incidental note worth recording: al-Jāḥiẓ's best marker classes
include الكتاب and الكتب — adab prose talks about "the book" constantly, which bears on
2680 §11.5's caveat that Pillar 1's baseline failure was partly a content fact about
self-referential vocabulary.

**G10 cf-027 eponymy-independence — NOT-TRANSPORTABLE, and mostly already withdrawn.** Its
title-density arm was withdrawn during the 2026-08-07 session and replaced by H-NEW-2710
(which refined the rate ratio to 1.285 under dispersion matching); its transportable form
was already run as 2680's L4 (poetry 99.5 %, Bukhārī 14 %). What remains is a 5-cycle
centrality claim, and pseudo-surahs have no eponyms, so there is no baseline analogue. It is
declared untested here rather than given a manufactured verdict.

---

## 4. What falls and what survives

**Falls.**
- **The iʿjāz anti-twin as a Qurʾān-specific signature.** Two matched prose corpora exceed
  it and matched poetry equals it; half of it is unit size. H-NEW-740's Δ Fisher-z = −6.42
  does not survive a matched partition. The *classical* claim (al-Bāqillānī on *fawāṣil*) is
  not thereby refuted — it was never a claim about window-level correlation coefficients —
  but its stated empirical vindication is withdrawn.
- **The compression-tail family as content architecture.** 91.5 % size-explained, reproduced
  by adab prose, and nine-fold flattened when the Qurʾān's own verses are cut to equal size.
- **The rhyme and phoneme dispersion-tails**, at the 51st and 76th percentile of matched
  prose.
- **The verse-length tail**, below the baseline mean.
- **Anti-chiasmus as a property of this corpus** (it is a property of Arabic prose, more so).

**Survives.**
- **Every law's arithmetic.** Nothing here says any published computation is wrong. The QAC
  instrument reproduces H-NEW-660 to four decimals and the surface instrument reproduces
  four more published values closely.
- **The post-kink content-compression slope**, steeper than 200/200 ḥadīth and 198/200 adab
  partitions holding the size profile identical. One axis, one law, modest margin — but real,
  and it would have been erased by a binary pass/fail verdict.
- **cf-025's and cf-026's methodological rules**, which were never corpus claims: test at the
  scale where structure operates; the null model decides. Both stand.
- **cf-028's own numbers**, which are not challenged; only the *genre-specificity* of the
  lift is, and only under surrogate labels.

---

## 5. Honest limits — read these before citing anything above

1. **A partition is not a composed book.** The pseudo-surahs are arbitrary cuts of a
   continuous stream. **A law failing to discriminate against an artificial partition is
   weaker evidence against the law than it first appears**, because the baseline units were
   never authored as units. This is the single most important caveat in this finding and it
   applies to every row of the table.
2. **The direction of that weakness is not uniform, and each verdict must be read in its own
   regime.** For contiguity-sensitive statistics (G1, G5) arbitrary cuts of a continuous
   stream *preserve* local continuity and make the law *easier* for baselines — so a baseline
   pass there is **weak** evidence against the law. For boundary-sensitive statistics (G6,
   G9) arbitrary cuts *destroy* real boundaries and make the law *harder* — so a baseline
   pass there is **strong** evidence. G5's reversal is partially discounted by this; G6's is
   not.
3. **Three genres are not "Arabic in general."** Poetry, ḥadīth and adab prose are the only
   matched corpora on disk. Nothing here establishes what all Arabic does.
4. **Poetry has no band.** One partition, 145 words of slack. Its numbers are point estimates
   and are treated as such throughout; no percentile is quoted for poetry.
5. **The surface instrument is shallower than QAC** — no baseline has root annotation. This
   biases baseline content statistics *weaker*, so baselines matching or exceeding the Qurʾān
   would do so more strongly under better morphology. The bias runs against the conclusions
   drawn here, which is the conservative direction.
6. **G1's verdict is a one-draw and two-draw near miss.** The Qurʾān's R² is beaten by 1 of
   200 ḥadīth cuts and 2 of 200 adab cuts. Under an unprotected α = 0.05 that would read as
   significant (p_offset ≈ 0.010 and 0.015); under the pre-registered "outside the full
   200-draw range" bar it is not. Both readings are given; the pre-registered one governs.
7. **G7's labels are surrogates** and its verdict is capped accordingly (§3).
8. **G6's ring statistic is a re-implementation**, not H-NEW-2220's code — token-set Jaccard
   over mirror-paired units rather than root-set overlap. It lands near 2220's published mean
   (−0.136 vs −0.15), which is reassuring but not identity.
9. **No Bonferroni across the ten laws**, by pre-registration §6: this is an audit whose
   purpose is to *detect* failures, and correcting across laws would make failure harder to
   detect — the anti-conservative direction for this purpose.
10. **`numpy` is used**, the same disclosed Protocol §7.1 deviation H-NEW-2680 declared.

---

## 6. Garden of forking paths

- **Choices made after seeing data: none that affect a verdict.** The target list, the
  statistics, the margins, the direction lock and all six verdict labels were fixed at SHA
  `24a5bc8d…` before any baseline value existed.
- **One bug fixed between smoke and run**, disclosed in §3 (G8): the NaN-diagonal error ran
  in the *flattering* direction, so fixing it removed the sweep's only apparent
  Qurʾān-leading result. Fixed before the primary run.
- **Two MW-7-capped diagnostics** were added after seeing that G1 and G5 both reproduce in
  baselines: the log-size regression (§2.1b) and the size-partial correlation (§2.2). Both
  are descriptive, carry no p-value, add no cell, and change no verdict — they explain a
  result the pre-registered arms had already produced. The pre-registered uniform arm (§2.1c)
  was locked in advance and reaches the same conclusion independently.
- **al-Jāḥiẓ was added to the target list in the pre-registration**, before any baseline
  value was computed, on noticing that `jahiz-hayawan.txt` was on disk and unused by 2680.
- **Run directories are never deleted**; the smoke runs are retained alongside the primary
  and replication runs.

---

## 7. Replication and files

### 7.1 Replication (MW-5), seed 20260519

*(filled from the replication run — see §8)*

### 7.2 What should change in the project record

- **`h-new-740-preislamic-poetry-control.md`** needs a correction notice. Its Δ Fisher-z =
  −6.42 rests on comparing equal 30-bayt poetry blocks to the Qurʾān's unequal surahs; under
  a matched partition the same poetry corpus reaches r = −0.8718 against the Qurʾān's
  −0.8700. Its honest-limits §3 identified block size as the risk and assigned it the wrong
  sign. **This is not mine to apply to another finding's file — flagged for the ledger
  keeper**, as 2680 flagged the H-NEW-111 transcription error.
- **`h-new-730-content-rhyme-anticorrelation.md`** should carry the size-decomposition:
  r = −0.870 raw, **−0.432 controlling for unit size**.
- **`h-new-660` / `700` / `770`** should carry the size caveat and the uniform-cut collapse
  (0.9887 → 0.3388), exactly as 2680 §8 asked for Pillar 2.
- **`cross-finding-026-formal`** already carries a correction notice for its cohesion arm;
  it now needs one for its **chiasmus** arm too — the corpus is anti-chiastic, and so is
  every matched baseline, al-Jāḥiẓ more than the Qurʾān.
- **`findings/PILLAR-LAW-CORRECTION-2026-08-07.md`** should be extended from the four pillar
  laws to this sweep's nine.

### 7.3 Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2720-genre-control-sweep.md`
  (SHA-256 `24a5bc8dd2352151f6557a0415cb177f69e60f8fca5f1ccf39ff3c57b2e0040d`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2720.py` (SHA-gated; lifts 2680's
  partition code verbatim under a fragment-SHA check)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2720.json`
- Runs (immutable, never deleted):
  `findings/phase-b-hypotheses/runs/h-new-2720/` — primary, replication, and the smoke runs,
  each with a repo-relative `manifest.json` recording every frozen input SHA

---

*Run 2026-08-07 by Waiel Al-Shujaa. A law that has never met a control is a description.
Nine met one. Bismillāhi al-Raḥmāni al-Raḥīm.*
