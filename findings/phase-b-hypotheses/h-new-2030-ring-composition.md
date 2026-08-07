---
finding_id: h-new-2030
title: "Within-surah ring-composition / chiastic-symmetry detection"
specialist: h-new-2030-ring-composition-specialist
date: 2026-05-29
verdict: "NULL (corpus-wide); Farrin Q 2 and Cuypers Q 5 verse/block-level claims NOT supported"
prereg: findings/phase-b-hypotheses/prereg-h-new-2030-ring-composition.md
prereg_sha256: 0999b43f0ce72b084f51584124ef4d2f142b2793ece904b61535649de9b39a8e
script: findings/phase-b-hypotheses/scripts/h-new-2030.py
json: findings/phase-b-hypotheses/csv/h-new-2030.json
seed: 20260509
perms: 10000
bonferroni_k: 114
alpha_bon: 0.000438596
rules_tuple: "(no-tashkeel, QAC v0.4 STEM-ROOT tokens, content-root Jaccard, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-2030 — Within-surah ring-composition / chiastic-symmetry detection


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
> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> ## ⛔ CORRECTION NOTICE — 2026-08-07: anti-chiasmus is a property of Arabic prose, not of this corpus
>
> The finding **reproduces** — an independently written ring statistic returns mean
> permutation-z = −0.136 against the published −0.15. But all four matched corpora are
> anti-chiastic: poetry **−0.120**, this corpus **−0.136**, al-Bukhārī **−0.146**, and
> **al-Jāḥiẓ −0.209**. Adab prose is *more* anti-chiastic than this corpus, and roughly a
> third of windows are positive in every corpus (0.339–0.370).
>
> **Honest limit, for this law specifically — and it runs the other way.** This statistic is
> **boundary-sensitive**: arbitrary cuts *destroy* real unit boundaries and should make ring
> structure *harder* for a baseline. A baseline exceeding this corpus under that handicap is
> **strong** evidence, not weak. This is the most robust reversal in the sweep.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Question

Are surahs built as **content chiasms** — concentric ABCB'A' rings in which
verse *i* mirrors verse *(n+1−i)*, "the meaning in the middle"? Raymond Farrin
(*The Muslim World* 100, 2010) claims Q 2 al-Baqara is a nine-section ring with
the qibla-change pivot at 2:143; Michel Cuypers (*The Composition of the
Qur'an*, 2015; *Le Festin*, 2007) claims Q 5 al-Māʾida is ring-structured via
"Semitic rhetoric"; Nicolai Sinai ("Going Round in Circles", *JQS* 19, 2017)
is sceptical that most proposed rings are falsifiable. The project had never
tested ring-composition WITHIN surahs at verse granularity. This is the
within-surah analogue of the mushaf-level ring tested in
[[h-new-185-ring-laplacian|H-NEW-185]], and the natural generalisation of the
single-pair Medinan first↔last inclusio of [[h-new-189-medinan-inclusio|H-NEW-189]].

## Method (pre-registered, SHA-locked)

Pre-reg SHA-256 `0999b43f0ce72b084f51584124ef4d2f142b2793ece904b61535649de9b39a8e`,
verified at runtime. For each surah of *n* verses:

- Each verse → its set of QAC v0.4 STEM-level ROOT codes (content roots only;
  particles/prefixes without a ROOT field excluded).
- Verse-pair similarity = Jaccard `|R_i ∩ R_j| / |R_i ∪ R_j|`.
- **Chiasm-score** `C(s)` = mean Jaccard over the ⌊n/2⌋ disjoint mirror pairs
  `(i, n+1−i)`; the central verse of odd-*n* surahs is excluded (self-pair).
- **Null**: 10,000 within-surah verse-order permutations (Fisher–Yates,
  seed 20260509, per-surah child seed), recomputing `C` under the same mirror
  rule. One-sided `p = (1 + #{C_perm ≥ C_obs}) / 10001`. This null exactly
  preserves the multiset of verse-root-sets and surah length, destroying only
  ORDER — the correct null for "is the order chiastic".
- **Bonferroni** k=114, α_bon = 0.05/114 = 4.39×10⁻⁴.
- Surahs with n<4 (Q 103, 108, 110) flagged DEGENERATE and excluded from the
  "significant" count.
- **Secondary S3 (Farrin/Cuypers fairness control)**: re-run at the granularity
  the scholars actually argue — partition each surah into B contiguous equal
  blocks (B ∈ {5, 7, 9}), pool each block's roots, test block-mirror Jaccard vs
  block-order permutation.

## Result — NULL

| Test | Outcome |
|:--|:--|
| Surahs significant at Bonferroni (α=4.39×10⁻⁴) | **0 of 111** valid surahs |
| Surahs significant at raw α=0.05 | **5** (Q 11, 16, 46, 59, 69) — fewer than the ~5.6 expected by chance |
| Corpus mean p-value | **0.639** (a true global null gives ≈0.50; the corpus skews *away* from chiasm) |
| Corpus mean z-score | **−0.205** (centred slightly NEGATIVE — mirror pairs are, on average, marginally *less* similar than random order) |

The primary hypothesis (≥3 Bonferroni-significant chiastic surahs) **FAILS**.
The pre-reg's `PARTIAL` band is triggered only by the 5 raw-α hits, but those 5
are at or below the chance expectation for 111 tests and none clears even
2.5×10⁻² × correction — so the honest reading is a **corpus-wide NULL**:
verse-level content-root chiasmus is not a systematic feature of the mushaf.
This empirically supports **Sinai's scepticism** over the strong Farrin/Cuypers
ring program, at the verse-level operationalisation.

### Top-10 surahs by chiasm-score (none significant)

| Rank | Surah | C(obs) | null mean | z | p (1-sided) | n |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | Q 109 al-Kāfirūn | 0.667 | 0.400 | +2.00 | 0.199 | 6 |
| 2 | Q 55 al-Raḥmān | 0.175 | 0.174 | +0.15 | 0.421 | 78 |
| 3 | Q 114 al-Nās | 0.150 | 0.181 | −0.86 | 1.000 | 6 |
| 4 | Q 102 al-Takāthur | 0.125 | 0.125 | +0.36 | 0.431 | 8 |
| 5 | Q 113 al-Falaq | 0.125 | 0.153 | −0.53 | 0.873 | 5 |
| 6 | Q 63 al-Munāfiqūn | 0.108 | — | +1.11 | 0.145 | 11 |
| 7 | Q 112 al-Ikhlāṣ | 0.100 | 0.075 | +0.47 | 0.663 | 4 |
| 8 | Q 49 al-Ḥujurāt | 0.098 | — | +0.90 | 0.175 | 18 |
| 9 | Q 48 al-Fatḥ | 0.089 | — | +1.15 | 0.130 | 29 |
| 10 | Q 59 al-Ḥashr | 0.083 | 0.048 | +2.53 | 0.033 | 24 |

The high raw scores (Q 109, 112, 113, 114) are short refrain/creedal surahs
whose **null means are equally high** — their verses repeat the same few roots
regardless of order, so the chiasm-score is large but the z-score (the
order-specific signal) is near zero or negative. This is exactly the artefact
the permutation null is designed to remove: raw similarity ≠ chiastic order.

## Verdict on Farrin's Q 2 al-Baqara ring — NOT SUPPORTED

Farrin, *The Muslim World* 100 (2010), 17–32, argues Q 2 is a nine-section
concentric ring (sections 1↔9, 2↔8, 3↔7, 4↔6, pivot at the qibla-change
2:142–152).

- **Verse-level**: C(Q2) = 0.0465, null mean 0.0466, **z = −0.07, p = 0.519**.
  No chiastic signal whatsoever — observed mirror-pair similarity is identical
  to random verse order.
- **Block-level (S3, the granularity Farrin uses)**: at B=5 z=−0.06 (p=0.467);
  B=7 z=−0.57 (p=0.708); **B=9 z=−0.82 (p=0.787)**. At Farrin's own nine-section
  granularity Q 2 is, if anything, mildly anti-chiastic.

Farrin's ring is built on **thematic/lexical motif** correspondences
(faith/unbelief, creation, law, covenant) chosen and bounded by the reader, not
on shared content-root density between mirror sections. The content-root
operationalisation — which is blind, reproducible, and null-tested — finds no
trace of it. The claim is **NOT supported** under any pre-registered
granularity; it survives only as an interpretive (non-quantitative,
non-falsifiable-as-posed) reading.

## Verdict on Cuypers' Q 5 al-Māʾida ring — NOT SUPPORTED (mildly ANTI-chiastic)

Cuypers (*The Composition of the Qur'an*, 2015; *Le Festin*, 2007) reads Q 5 as
a ring via Semitic-rhetoric symmetry.

- **Verse-level**: C(Q5) = 0.0499, null mean 0.0640, **z = −2.01, p = 0.988**.
  Mirror pairs are significantly LESS similar than random verse order — the
  opposite of a chiasm.
- **Block-level (S3)**: B=5 z=+0.36 (p=0.405); B=7 z=+0.15 (p=0.445);
  **B=9 z=−1.27 (p=0.898)**. No block size yields a significant ring.

Cuypers' Q 5 claim is **NOT supported** and at fine granularity runs
counter-direction. As with Farrin, the rhetorical-analysis method depends on
analyst-selected parallelisms (echo words, phrase forms) rather than measurable
content-root mirroring.

## Corpus block-level enrichment (S3) — also NULL

Testing all surahs at Farrin's 9-section granularity: only **2 of 96** surahs
reach raw α=0.05, against **~4.8 expected by chance**. Block-level ring
composition is no more present corpus-wide than verse-level. The Farrin/Cuypers
program does not generalise.

## Interpretation

1. **Strong (verse/block content-root) ring composition is empirically absent**
   from the mushaf as a systematic feature, and absent specifically from the two
   flagship cases (Q 2, Q 5). The corpus z-distribution is centred slightly
   negative — surahs are, on the whole, *front-loaded / progressive* rather than
   concentric in content-root space.

2. This does **not** refute every notion of Quranic symmetry. It refutes the
   specific, measurable claim that *mirror verses (or mirror equal-blocks) share
   more content-roots than chance*. Farrin's and Cuypers' rings live in
   thematic-motif space and in reader-bounded section divisions; those are not
   falsifiable in the form posed and are not recovered by a blind metric.
   [[h-new-189-medinan-inclusio|H-NEW-189]] already showed the ONE chiastic pair
   that IS real corpus-wide — the outermost first↔last inclusio in Medinan
   surahs — but that single-pair edge-effect does not extend inward into a full
   ring (Q 59 al-Ḥashr, the H-NEW-189 leader, here ranks #10 with z=+2.53,
   p=0.033, raw-only — its signal is the outer pair, not a concentric ring).

3. The result triangulates with [[h-new-660-compression-tail-gradient|the
   compression-tail laws]]: content cohesion is governed by *adjacency* and
   *length-driven compression*, not by *positional mirroring*. The mushaf's
   architecture is geodesic/progressive (H-NEW-111, H-NEW-185 mushaf ring),
   not concentric within surahs.

## Honest limits

- **Operationalisation gap**: Farrin/Cuypers argue at the level of thematic
  pericopes and rhetorical echo, not content-root density. A verse/block
  content-root NULL falsifies the *measurable* version of their claim, not the
  *interpretive* version (which, as Sinai notes, is hard to falsify at all).
  This is disclosed, not hidden: the finding refutes ring-composition **as a
  reproducible content-similarity signal**.
- **Feature space**: a single feature (QAC STEM-roots). MW-5 replication on a
  char-4-gram feature space was pre-registered as the gate for any CONFIRMED
  upgrade; since the verdict is NULL, replication is moot (one would replicate a
  null). A future test could try rhyme-class or phoneme mirroring, but the prior
  after this result is low.
- **5 raw-α hits** (Q 11, 16, 46, 59, 69) are reported transparently; they do
  not exceed chance expectation and none survives Bonferroni. They are NOT
  promoted.
- **Short-surah degeneracy**: Q 103/108/110 (n<4) excluded; the high raw scores
  of other short surahs are null-corrected away (their permutation nulls are
  equally high).

## Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2030-ring-composition.md`
  (SHA-256 `0999b43f0ce72b084f51584124ef4d2f142b2793ece904b61535649de9b39a8e`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2030.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2030.json`
- Parents: [[h-new-185-ring-laplacian|H-NEW-185]] (mushaf ring),
  [[h-new-189-medinan-inclusio|H-NEW-189]] (first-last inclusio = outer chiasm pair).
- Classical / scholarly anchors: Farrin 2010, Cuypers 2015, Sinai 2017 (PDFs in
  `data/literature/farrin-cuypers/`).
