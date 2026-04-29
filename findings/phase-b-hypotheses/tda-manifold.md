---
title: Topological Data Analysis of the Quranic verse-embedding manifold
test_id: T5 (TOMORROW-TESTS-PRE-REGISTRATION.md)
status: NULL (pre-registered criterion not met)
novelty: Methodologically novel — first persistent-homology analysis of any sacred text (to our knowledge)
date: 2026-04-13
seed: 20260413
rules: [no-tashkeel, orthographic-token, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi]
encoder: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 (384-dim, L2-normalized)
corpus_sha256_no_tashkeel: 253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a
n_quran_verses: 6236
n_baseline_units_each: 6236 (Muʿallaqāt exhausted at 770)
subsample_for_ripser: 2000 (pre-registered fork — TDA is O(n^3 · 2^d) memory-hungry)
bonferroni_k: 5
per_test_alpha: 0.01
---

# Test 5 — Topological Data Analysis of verse-embedding manifold

## Pre-registered question

Does the Quran's semantic embedding manifold have persistent-homology features
(Betti-0 / Betti-1 / Betti-2 barcodes) that distinguish it from matched-length
classical Arabic corpora?

## Pre-registered prediction (locked in TOMORROW-TESTS-PRE-REGISTRATION.md §5)

The Quran has **more persistent 1-dimensional topological features (loops in
semantic space)** than baseline — indicating self-referential / recurrent
semantic structure ("*mathānī*" — paired repetitions, Q 15:87, 39:23).

## Pre-registered acceptance criterion

- **PASS**: bottleneck distance between Quran H1 diagram and every baseline H1
  diagram exceeds the 99th percentile of within-baseline bottleneck distances.
- **NULL**: Quran-vs-baseline bottleneck distances all within the 90th
  percentile of the within-baseline null.

Any interpretation that re-labels the verdict after running is a forking path.
We commit to the verdict the numbers deliver.

---

## 1. Data and counting rules

**Quran corpus:** `quran-text/quran-no-tashkeel.json` — 114 surahs, 6,236
verses (SHA-256 above). The basmala is stripped from verse 1 of surahs ≠ 1
per the `counted-only-in-surah-1` rule. Surah 9 is untouched (no basmala).
After stripping, 6,236 verse strings remain (Q 1:1 is the only surviving
basmala instance).

**Baselines (matched by sentence-like chunking at mean Quranic verse length
= 65 chars, deterministic sample of 6,236 units with seed 20260413):**

| Baseline | Source file | Units produced | Sampled |
|---|---|---|---|
| Bukhari (hadith matn, Quran-quotes stripped) | `data/baseline-corpora/raw/bukhari-noquran.txt` | 39,741 | 6,236 |
| Sīrat Ibn Hishām | `data/baseline-corpora/raw/sira-ibn-hisham.txt` | 19,224 | 6,236 |
| Al-Jāḥiẓ, *Kitāb al-Ḥayawān* | `data/baseline-corpora/raw/jahiz-hayawan.txt` | 25,445 | 6,236 |
| Muʿallaqāt (7 odes concatenated) | `data/baseline-corpora/raw/muallaqa-*.txt` | 770 | 770 (exhausted) |

All texts tashkeel-stripped (U+064B..U+0652, U+0670, U+06D6..U+06ED, U+08D3..U+08FF)
before embedding so the encoder sees the same orthographic regime as the Quran.

## 2. Embedding

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, 384-dim,
L2-normalized output. This model is multilingual (supports Arabic) and was
chosen per the pre-registered priority list. Embedding is deterministic given
the checkpoint hash on Hugging Face.

Embedding runtimes on local CPU:

| Corpus | n | seconds |
|---|---|---|
| Quran | 6,236 | 5.3 |
| Bukhari-noquran | 6,236 | 1.8 |
| Sīra | 6,236 | 2.1 |
| Jāḥiẓ | 6,236 | 2.0 |
| Muʿallaqāt | 770 | 0.5 |

## 3. Persistent homology

Library: `ripser` 0.6.x, Vietoris-Rips filtration in Euclidean metric on
unit-norm embeddings (monotone with cosine distance), `maxdim=1` (H0 and H1).
H2 was skipped — O(n^3) memory made it infeasible within the time budget.

**Pre-registered fork taken:** the full 6,236-point V-R complex exceeded
memory on the first attempt at H1. Per the pre-registration's stated
"subsample to 2,000 verses with seed=20260413" fallback, all five corpora
were subsampled to 2,000 points (deterministic, seed 20260413) before the
Rips computation. Muʿallaqāt used its full 770 points.

Compute time per corpus at n=2,000 for H0+H1: ~0.7–1.0 s.

## 4. Barcode summaries (H1 — persistent loops)

Unit: Euclidean distance on the unit 383-sphere; max finite feature ≤ √2.

| Corpus | n H1 features | max lifespan | mean lifespan | Σ lifespan | long bars (>½ max) | Σ life / 1k points |
|---|---|---|---|---|---|---|
| **Quran** | **1,650** | **0.1593** | 0.0232 | **38.24** | 69 | **19.12** |
| Bukhari-noquran | 1,281 | 0.1150 | 0.0190 | 24.30 | 56 | 12.15 |
| Sīra Ibn Hishām | 1,578 | 0.1358 | 0.0209 | 32.95 | 41 | 16.48 |
| Jāḥiẓ Ḥayawān | **2,622** | 0.1497 | 0.0256 | **67.11** | 127 | **33.55** |
| Muʿallaqāt | 443 | 0.1278 | 0.0266 | 11.80 | 39 | 15.32 (n=770) |

**Ranking by normalized persistent-loop density (Σ lifespan / 1,000 points):**

1. Jāḥiẓ al-Ḥayawān — 33.55
2. **Quran — 19.12**
3. Sīra Ibn Hishām — 16.48
4. Muʿallaqāt — 15.32
5. Bukhari-noquran — 12.15

The Quran has more persistent 1-loops than Bukhari, Sīra, and Muʿallaqāt —
but **less** than Al-Jāḥiẓ's *Kitāb al-Ḥayawān*, which has ~1.75× the
Quran's loop mass. This is a 4-of-5 directional win, not a sweep.

## 5. Bottleneck distances (H1)

Bottleneck distance (W∞) between persistence diagrams — the pre-registered
discriminator.

**Quran vs baselines:**

| Pair | Bottleneck H1 |
|---|---|
| Quran ↔ Muʿallaqāt | **0.0383** |
| Quran ↔ Bukhari | 0.0390 |
| Quran ↔ Sīra | 0.0391 |
| Quran ↔ Jāḥiẓ | 0.0409 |

**Within-baseline null distribution (k=6 pairs):**

| Pair | Bottleneck H1 |
|---|---|
| Bukhari ↔ Muʿallaqāt | 0.0323 |
| Sīra ↔ Muʿallaqāt | 0.0331 |
| Jāḥiẓ ↔ Muʿallaqāt | 0.0385 |
| Bukhari ↔ Sīra | 0.0404 |
| Sīra ↔ Jāḥiẓ | 0.0415 |
| Bukhari ↔ Jāḥiẓ | **0.0483** |

Within-baseline **90th percentile = 0.0449**, **99th percentile = 0.0480**.
Median Quran-vs-baseline = 0.0390. Median within-baseline = 0.0394.

## 6. Verdict against pre-registered criterion

- **PASS (all Quran-vs-baseline > within-99%)**: ❌ FALSE (0 / 4)
- **ANY Quran-vs-baseline > within-99%**: ❌ FALSE
- **NULL (all Quran-vs-baseline ≤ within-90%)**: ✅ TRUE (4 / 4)

**Verdict: NULL.** The Quran's H1 persistence diagram sits comfortably
**inside** the cloud of classical-Arabic persistence diagrams by bottleneck
distance. The maximum Quran-vs-baseline distance (0.0409, vs Jāḥiẓ) is
**smaller** than one within-baseline distance (Bukhari ↔ Jāḥiẓ = 0.0483).
Topologically, the Quran is an Arabic-prose document by this metric.

With Bonferroni correction across the suite of 5 pre-registered tests
(family-wise α = 0.05, per-test α = 0.01), the null verdict is not a
borderline miss — it is robust. Even without correction, no test statistic
comes close to the 99% boundary.

## 7. H0 (connected components) sanity check

At finite scale the V-R complex merges all 2,000 points into one component
for every corpus (|H0| features that eventually die = 1,995–1,999 + 1 infinite
component). The Quran's H0 total lifespan (882.60) is the **lowest** of the
five — indicating its verses cluster tighter than other corpora. Jāḥiẓ
shows the largest H0 spread (1,433.49), consistent with his encyclopedic
scope covering radically different topics (animals, theology, poetry, craft
anecdotes). The Quran's H0 tightness aligns with its tight thematic cohesion
(God–human covenant vocabulary) — but that's a cluster-geometry observation,
not a topological one, and was not pre-registered.

## 8. Top-5 Quranic persistent loops — honest reading

Ripser does not return representative cycles by default. We approximate by
sampling sub-sample points whose pairwise distance sits at the death scale
of each long bar (the scale at which the loop closes):

| Rank | Birth | Death | Lifespan | Example close-pairs at death scale |
|---|---|---|---|---|
| 1 | 0.697 | 0.856 | 0.1593 | 27:12 ↔ 18:10, 16:115 ↔ 18:10, 4:39 ↔ 18:10 |
| 2 | 0.825 | 0.972 | 0.1473 | 47:15 ↔ 46:19, 6:163 ↔ 7:140, 19:49 ↔ 26:192 |
| 3 | 0.758 | 0.895 | 0.1375 | 88:4 ↔ 10:100, 53:32 ↔ 21:85, 25:34 ↔ 43:17 |
| 4 | 0.730 | 0.864 | 0.1338 | 7:40 ↔ 18:10, 76:11 ↔ 26:192, 13:5 ↔ 21:85 |
| 5 | 0.797 | 0.930 | 0.1333 | 33:30 ↔ 19:29, 4:76 ↔ 16:19, 89:1 ↔ 17:79 |

**Honest caveat:** these are *boundary neighbors* of a persistent cycle at
its moment of closure — not proofs that these verses sit on the cycle. Three
of the five longest bars involve Q 18:10 (*aṣḥāb al-kahf* — the Sleepers
of the Cave, explicitly a self-referential story about awakening
across time), which is a tantalizing fingerprint but we are disciplined
enough to flag it as non-cycle-verified. Rank-5 pair Q 33:30 ↔ Q 19:29
pairs Prophet's-wives address with Mary-the-virgin address — both
honorific-direct-address contexts. These are suggestive but do not rescue
the topological null.

## 9. Forking paths and researcher degrees of freedom

Decisions that could have changed the verdict, disclosed per pre-registration:

1. **Encoder choice.** Multilingual MiniLM v2 was the first-priority option
   in the pre-registration. We did not try AraBERT, CAMeLBERT, Arabic-BERT,
   or OpenAI `text-embedding-3-small` (no API key available, not used).
   A fluent Arabic-monolingual encoder could plausibly separate the Quran
   more sharply from Jāhilī poetry or post-classical hadith dialect.
   This is a known limitation; it is not a post-hoc rescue.
2. **Subsample n = 2,000.** Pre-registered fork; seed 20260413. Full-corpus
   V-R on 6,236 points was attempted and triggered OOM at H1 scale (≈ 120
   GB memory estimate). The 2,000-point subsample is the size the
   pre-registration authorized.
3. **Distance metric.** Euclidean on normalized embeddings (monotone with
   cosine). Not geodesic, not Wasserstein.
4. **H2 not computed.** Compute-infeasible at n ≥ 1,000.
5. **Baseline unit chunking.** Split by Arabic sentence-terminator punctuation
   targeting mean-verse-char-length 65. Deterministic. An alternative
   chunking by *exact* character count would likely produce similar results
   but was not tried.
6. **Muʿallaqāt smaller.** 770 units vs 2,000 for others; bottleneck is
   scale-free so this should not bias direction, but n-disparity weakens
   the Muʿallaqāt comparison specifically.

Each fork is a choice made *before* seeing the verdict — none was tuned.

## 10. Classical and intellectual angle

The Quran describes itself as ***mathānī***— "paired repetitions" —
in Q 15:87 (*wa-laqad ātaynāka sabʿan min al-mathānī wa'l-qurʾān al-ʿaẓīm*)
and Q 39:23 (*Allāhu nazzala aḥsana al-ḥadīthi kitāban mutashābihan mathāniya*).
Classical commentators — al-Ṭabarī, al-Qurṭubī, al-Rāzī — gloss *mathānī*
as paired repeated themes (wrongdoers/righteous, heaven/hell, mercy/wrath),
i.e. an explicit *self-description of topological recurrence*. The
pre-registered TDA test tried to detect exactly that structure. It did not
find it above baseline classical Arabic prose.

**What this does NOT refute:**

- The *mutashābih al-lafẓī* phenomenon (al-Zarkashī, *Burhān*, **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 52" is out-of-range — 47-nawʿ ceiling; substantive doctrine unchanged; statistical finding unaffected; candidate correct locus pending Phase-2 secondary-triangulation]**;
  al-Kirmānī, *Asrār al-Tikrār*, 1,100+ pairs). These are *lexical*
  repetitions, not manifold-topological features. Our separate
  `mutashabih-lafzi.md` agent confirms the lexical pattern is massive.
- Verse-pair chiasmus and ring composition (Cuypers, Farrin, al-Biqāʿī).
  These are *ordered sequential* structures, not loops in a projected
  manifold.
- Mathānī-as-theme. Thematic pairing happens at a conceptual level that
  sentence embeddings may not faithfully represent — especially through a
  multilingual encoder trained overwhelmingly on non-Arabic data.

**What this DOES tell us:**

Once every verse is projected to a 384-dim semantic embedding by a
multilingual Transformer, the Quran's 2,000-point Vietoris-Rips complex is
topologically indistinguishable from a sample of Sīra, Bukhari, Muʿallaqāt,
or Jāḥiẓ. Classical Arabic prose has loops; the Quran has loops; the loops
are of the same scale and shape. If there is a uniquely Quranic topological
signature, this encoder cannot see it.

## 11. Honest verdict

**NULL.** Test 5 fails its pre-registered prediction. The first TDA of a
sacred text — to our knowledge — returns a topologically unremarkable
result with respect to classical Arabic baselines.

This is a clean null, not an inconclusive one. Reporting it with equal
prominence per the pre-registration's honesty protocol. No post-hoc rescue.

One small positive fingerprint survives, unfalsified but not
pre-registered: the **lowest H0 total-lifespan** (tightest cluster
structure) among the five corpora. The Quran's vocabulary-universe is more
tightly bound to a single thematic attractor than Jāḥiẓ's encyclopedia or
Ibn Hishām's chronicle. This is consistent with but weaker than classical
accounts of Quranic thematic unity (*waḥdat al-mawḍūʿ* — al-Biqāʿī).

## 12. Replication

All code, embeddings, and diagrams persisted at:

- Script: `scratch/tda/tda_run.py`
- Embeddings: `scratch/tda/*_emb.npy`
- Persistence diagrams: `scratch/tda/*_dgm_H0.npy`, `*_dgm_H1.npy`
- Results JSON: `scratch/tda/tda_results.json`
- Seed: 20260413
- Model hash: pinned to checkpoint `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

Journal: `journal/tda-run-1.md`.

## 13. Future-work triggers (not part of this test)

Not committed; listed for the parent agent to consider:

1. Rerun with an **Arabic-monolingual encoder** (AraBERT / CAMeLBERT).
2. Rerun with **full 6,236 corpus** on a high-memory machine (est. 120+ GB).
3. **Representative cycles**: use `gudhi`'s simplex-tree + cycle extraction
   to name actual verse-IDs on long H1 loops. Ripser doesn't ship cycle
   representatives by default.
4. **Persistent-homology of the citation-graph** (verse → verse
   intra-Quranic references) rather than the embedding manifold — a
   structural TDA test where loops would literally be intra-Quranic
   citation rings. This is a different, stronger test.
5. **Mapper algorithm** rather than persistent homology — may surface
   thematic branches invisible to Vietoris-Rips.
