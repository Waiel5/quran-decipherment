---
finding_id: h-new-2290
title: "Verse-pair chiasmus / antithetical-mirror generator (adjacent-verse scale)"
specialist: h-new-2290-verse-pair-chiasmus-specialist
date_prereg: 2026-05-29
seed: 20260509
perms: 10000
bonferroni_k: 2
bonferroni_family: "h-new-2290 two-subtest family {chiasmus, antithetical-density}"
alpha_raw: 0.05
alpha_bon: 0.025
rules_tuple: "(no-tashkeel, QAC v0.4 STEM-ROOT tokens with word-order preserved by segment index, content-root sequence, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
parent_findings:
  - H-NEW-2030 (within-surah mirror-pair ring; whole-surah scale; PARTIAL/NULL)
  - Q002-F-07 / cross-finding-025 (ring at pericope/block scale; PASS)
  - H-NEW-2070 (al-fawāṣil divine-name verse-final grammar; finest positional scale)
  - H-NEW-189 (Medinan first↔last inclusio; the outermost pair of a chiasm)
verdict_ceiling: "PASS (not CONFIRMED); CONFIRMED requires replication on an independent feature space (char-n-gram order for chiasmus; an alternative antonym lexicon for antithetical) AND survival under the triplet variant"
---

# H-NEW-2290 — Verse-pair chiasmus / antithetical-mirror generator

## Motivation and scale-placement

The project has tested ring composition at three scales: whole-surah verse-mirror
(H-NEW-2030, PARTIAL/NULL), pericope/block (Q002-F-07 → cross-finding-025, PASS),
and the verse-FINAL divine-name bigram (H-NEW-2070, PASS). This finding works at
the **finest content scale below the block**: the **consecutive verse-pair**
(and verse-triplet). Two distinct micro-structures are scanned, each with its own
pre-registered test, as a Bonferroni family of **k = 2**:

- **(a) Word-order chiasmus** (AB↔BA): do shared content-roots appear in
  *reversed* linear order across an adjacent verse-pair? If verse *i* mentions
  roots in order […X…Y…] and verse *i*+1 mentions them […Y…X…], that ordered
  pair (X,Y) is a *reversed-order root pair* — a micro-chiasmus crossing the
  fāṣila. This is the verse-pair analogue of classical *radd al-ʿajuz ʿalā
  al-ṣadr* / *taʿakkus* (al-Zarkashī, *al-Burhān*, nawʿ on *al-badīʿ*;
  al-Suyūṭī, *al-Itqān*, nawʿ 59 on *al-jinās wa-l-radd*).

- **(b) Antithetical parallelism** (*muqābala* / *ṭibāq*): does the verse-pair
  juxtapose two **opposed semantic fields** — believers↔disbelievers,
  paradise↔hellfire, light↔darkness, guidance↔misguidance, good↔evil,
  reward↔punishment? Classical *ʿilm al-badīʿ* names this *al-ṭibāq* (antithesis)
  and *al-muqābala* (al-Suyūṭī, *al-Itqān*, nawʿ 59; al-Sakkākī, *Miftāḥ
  al-ʿulūm*, on *al-muḥassināt al-maʿnawiyya*; al-Zarkashī, *al-Burhān*).

## Data sources (all from disk)

- Verse text & order, surah type, mushaf position, verse counts:
  `quran-text/quran-no-tashkeel.json`.
- Ordered content-roots per verse: `data/morphology/quranic-corpus-morphology-0.4.txt`,
  field `ROOT:` on `STEM` segments only, **ordered by the (word:segment) index**
  inside each verse so that linear word-order is preserved (required for (a)).
- Antonym-field lexicon: locked below, themed from `data/asma-al-husna.txt`
  (al-Tirmidhī 99-names list) opposed-attribute pairs + standard opposed
  root/lemma sets, all verified to attest in the QAC root inventory.

## §A — Word-order chiasmus (sub-test 1)

### Operationalisation (LOCKED)

For each surah, build for every numbered verse *i* the **ordered list of content
roots** `seq_i` = roots of STEM segments in (word, segment) order, with immediate
adjacent duplicates collapsed (a root repeated in consecutive segments counts
once for ordering; non-adjacent repeats kept). For each **consecutive verse-pair
(i, i+1)** within the same surah:

1. Let `S = set(seq_i) ∩ set(seq_{i+1})` be the **shared roots** (must be ≥ 2 to
   admit any ordered pair).
2. For each unordered pair {X, Y} ⊆ S, determine the order of first occurrence in
   `seq_i` and in `seq_{i+1}`. The pair is a **reversed-order (chiastic) root
   pair** iff the relative order of (X, Y) in verse *i*+1 is the reverse of their
   relative order in verse *i* (AB → BA). It is a **same-order pair** otherwise
   (AB → AB, parallel).
3. **Verse-pair chiasm count** = number of reversed-order root pairs over all
   {X,Y} ⊆ S. **Same-order count** = number of same-order pairs.

**Corpus reversed-order rate** `R_obs` = (Σ reversed pairs) / (Σ reversed + Σ
same-order pairs), over all consecutive verse-pairs in all 114 surahs (pairs with
|S| < 2 contribute 0 to both numerator and denominator).

### Null (MW-2) and hypothesis (DIRECTION LOCKED — two-sided around 0.5,
prominence on reversed)

Under a **within-surah verse-order shuffle** the multiset of verse-root-sequences
and the surah length are preserved but adjacency is destroyed. For each
permutation: Fisher–Yates shuffle the order of the verses *within each surah*
(numpy `default_rng`, seed **20260509**), then recompute `R` over the new
consecutive pairs. Repeat **10,000** times. This null asks: *is the rate of
reversed-order shared-root pairs across genuinely adjacent verses different from
what random adjacency produces?*

- **DIRECTION LOCKED**: the chiastic hypothesis predicts `R_obs > R_null`
  (genuine adjacency produces MORE order-reversal than random adjacency — the
  text "crosses" roots across the fāṣila more than chance). The natural chance
  baseline for the reversed-vs-same ratio is ≈ 0.5; a genuine *parallel*
  tendency would give `R_obs < 0.5` and `R_obs < R_null`.
- A result with `R_obs ≤ R_null` (adjacency produces NO excess reversal, or a
  parallel/same-order excess) is a **pre-commit-relevant reversal** and is
  published as NULL with full prominence. A *parallelism* signal
  (`R_obs < R_null`, significant) is reported as the honest opposite finding, not
  spun as a win.
- One-sided p (chiastic) = (1 + #{R_perm ≥ R_obs}) / (10001).

### Census output

Enumerate, with coordinates, every consecutive verse-pair carrying ≥ 1
reversed-order root pair (surah, i, i+1, shared roots, the reversed (X,Y) tuples).

## §B — Antithetical parallelism (sub-test 2)

### The antonym-field lexicon (LOCKED — built BEFORE computation)

Eight opposed semantic fields. Each pole is a set of **root codes** (Buckwalter,
QAC v0.4) UNLESS marked `LEMMA:` (used when one root conflates both poles, e.g.
`nwr` = both *nār* "fire" and *nūr* "light"; `Zlm` = both *ẓulm* "wrong" and
*ẓulumāt* "darkness"). All codes verified to attest in the QAC root inventory.

| # | Field | Pole + (positive) roots | Pole − (negative) roots |
|:-:|:--|:--|:--|
| F1 | Faith vs disbelief | `Amn` (īmān/muʾmin) | `kfr` (kufr/kāfir), `nfq` (munāfiq), `Srk` (shirk) |
| F2 | Guidance vs misguidance | `hdy` (hudā) | `Dll` (ḍalāl) |
| F3 | Paradise vs hellfire | `jnn` LEMMA `jan~ap` (janna) | `jHm` (jaḥīm), `sEr` (saʿīr), `Hmm` LEMMA `Hamiym` (ḥamīm), `nwr` LEMMA `naAr` (nār), `Hwy` LEMMA `haAwiyap`, `sqr` (saqar), `lZy` (laẓā) |
| F4 | Light vs darkness | `nwr` LEMMA `nuwr`/`m~uniyr` (nūr) | `Zlm` LEMMA `Zuluma`t` (ẓulumāt) |
| F5 | Reward vs punishment | `vwb` (thawāb), `jzy` LEMMA reward-context `jazaY`/`jaza`'`, `>jr` (ajr) | `Eqb` LEMMA `Eaqaba`/`Eiqaab`/`Euquwbap` (ʿiqāb/ʿaqaba), `Evb` `Ev` not-attested→excluded |
| F6 | Righteous-deed vs corruption | `SlH` (ṣāliḥāt), `brr` (birr) | `fsd` (fasād), `swA` LEMMA `suw^'`/`say~i}ap` (sūʾ/sayyiʾa) |
| F7 | Good (ṭayyib) vs foul (khabīth) | `Tyb` (ṭayyib) | `xbv` (khabīth) |
| F8 | Life vs death | `Hyy` (ḥayāt/ḥayy) | `mwt` (mawt/mayyit) |

A verse is tagged with field F's **positive pole** if it contains ≥ 1 root from
F's pole + set (lemma-restricted where marked), and with F's **negative pole**
analogously. (`jzy` is assigned to F5-positive only when its lemma is the
reward sense; the script applies the lemma restriction listed; ambiguous
non-listed lemmas are not tagged.)

### What counts as an antithetical verse-pair (LOCKED)

A **consecutive verse-pair (i, i+1)** (same surah) is an **antithetical pair**
iff there exists at least one field F such that one of the two verses carries F's
positive pole and the other carries F's negative pole (cross-verse contrast: the
two opposed poles of the *same* field appear in the two *different* verses of the
pair). Within-verse-only contrasts do NOT count (this is a *verse-pair* mirror
test). The **antithetical-pair count** of a surah/region = number of such
consecutive pairs; the **density** = count / (number of consecutive pairs in that
region) = count / (n_verses − 1) summed appropriately.

### Hypothesis (DIRECTION LOCKED — ONE direction, BEFORE computing)

> **LOCKED DIRECTION**: antithetical verse-pair density is **NOT uniform** across
> the corpus; it is **HIGHER in the short eschatological mufaṣṣal surahs
> (mushaf position ≥ 78, i.e. Q 78–114, the *juzʾ ʿamma* warning-surahs) than in
> the long surahs (mushaf position ≤ 49)**.

This is the "stated genre" lock: the juzʾ-ʿamma short surahs are dominated by the
*indhār* (warning) register that pits paradise against hellfire and the saved
against the damned in tight successive verses (e.g. Q 101 al-Qāriʿa heavy↔light
scales; Q 92 al-Layl gives-and-fears↔withholds; Q 88 al-Ghāshiya faces
downcast↔faces joyful). The long surahs interleave law, narrative and creed over
longer spans, diluting adjacent-pair antithesis.

- **Region A** = surahs with mushaf id ∈ [78, 114] (short mufaṣṣal eschatological).
- **Region B** = surahs with mushaf id ∈ [1, 49] (long surahs).
- **Test statistic** = `Δ = density(A) − density(B)` where density is the
  pooled rate (Σ antithetical pairs in region) / (Σ consecutive pairs in region).
- **DIRECTION LOCKED**: `Δ > 0` (A > B). A result `Δ ≤ 0` is a pre-commit-relevant
  reversal published as NULL with full prominence.

### Null (MW-2)

The label "is this verse-pair antithetical" depends on which fields its two
verses carry. To test whether the *concentration in region A* exceeds chance, we
use a **region-label permutation**: pool all consecutive verse-pairs of the whole
corpus, each tagged antithetical/not by the fixed rule above; then randomly
**reassign the region labels** by permuting which surahs are "A-sized vs B-sized"
is fixed by mushaf id, so instead we permute the **antithetical/not labels across
all corpus verse-pairs** (numpy `default_rng`, seed **20260509**, 10,000
permutations) holding the number of A-pairs and B-pairs fixed, and recompute
`Δ_perm = density_A − density_B`. One-sided p (A>B) =
(1 + #{Δ_perm ≥ Δ_obs}) / (10001). This is the hypergeometric-style null: under
H0 the antithetical pairs are spread uniformly over all consecutive pairs
regardless of region.

### Census output

Enumerate every antithetical consecutive verse-pair with coordinates (surah, i,
i+1), the field(s) F triggered, and which verse carried which pole.

## Bonferroni (k = 2)

Family = {sub-test 1 chiasmus, sub-test 2 antithetical-density}. α_bon = 0.05 / 2
= **0.025** (one-sided each, in the locked direction). Both raw and Bonferroni
p reported.

## Success / failure criteria

- **PASS-chiasmus**: `R_obs > R_null` with one-sided p < 0.025 (adjacency
  produces a significant EXCESS of reversed-order shared-root pairs).
- **PASS-antithetical**: `Δ_obs > 0` with one-sided p < 0.025 (region-A density
  significantly exceeds region-B).
- **PASS (overall)**: both sub-tests PASS at α_bon.
- **PARTIAL**: exactly one sub-test passes at α_bon.
- **NULL**: neither passes at α_bon; any reversed-direction result published with
  full prominence and an explicit pre-commit-violation flag.

## MW protections

- **MW-1 (instrument-prior)**: ordered-root chiasmus rule, antonym lexicon, and
  region definition all fixed in this file before any computation; SHA-locked.
- **MW-2 (corpus-prior)**: 10,000 permutations per sub-test, seed 20260509.
- **MW-3 (alternative-models)**: chiasmus also reported on a **triplet** variant
  (windows of 3 consecutive verses, reversed-order over the union) as a secondary
  aggregation; antithetical also reported with the **mufaṣṣal-only [≥ 78] vs
  ṭiwāl-only [1–9]** sharper contrast as a robustness check (does not change the
  pre-registered verdict, which uses [78,114] vs [1,49]).
- **MW-4 (over-fitting)**: no fitted free parameters in either primary test.
- **MW-5 (replication)**: chiasmus to be re-run on a char-4-gram ordered feature
  (independent of QAC) and antithetical on an alternative antonym lexicon (e.g.
  swapping the F5 reward/punishment lemma split) before any CONFIRMED upgrade;
  PASS-ceiling until then.
- **MW-6 (instrument-control)**: the within-surah verse-shuffle (chiasmus) and the
  label permutation (antithetical) ARE the matched controls; additionally the
  global mean reversed-vs-same ratio under shuffle should sit at ≈ 0.5 (sanity).
- **MW-7 (post-hoc cap)**: any individual surah or verse-pair noticed as striking
  that was not pre-specified carries single-test α = 0.05 and is reported as
  illustrative census, not as a confirmatory claim.

## Anti-confirmation commitment

The honest prior: (a) order-reversal of shared roots across adjacent verses may
be at or below chance — much of Quranic adjacency is *parallel* (same-order
anaphora, e.g. `al-ladhīna…`), so a `R_obs < R_null` PARALLELISM result is
genuinely plausible and will be reported as the honest opposite finding. (b) The
genre-concentration of antithesis in the juzʾ-ʿamma is a strong classical
intuition but the *density* could be dominated instead by the long Medinan
surahs (Q 2–9) which also pit believers vs disbelievers constantly; that would
reverse `Δ` and is published as NULL. A reversed or NULL outcome on either
sub-test is a fully publishable, equal-prominence result.
