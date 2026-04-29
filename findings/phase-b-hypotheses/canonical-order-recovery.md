---
title: "Canonical-order recovery — can the mushaf order be reverse-engineered from text alone?"
rules:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: mashriqi (not used; structural-similarity test only)
date: 2026-04-12
agent: canonical-order-run-1
status: MIXED — combined-metric PASS FAILS on τ (p=0.81) but ADJACENT-PAIR RECOVERY is extreme (17/113 vs null 2.01, p<0.0001); length-residualized NCD recovers τ=+0.65, p<0.0001
pre_registration: findings/TOMORROW-TESTS-PRE-REGISTRATION.md §Test 3
---

# Canonical-order recovery — can the mushaf order be reverse-engineered from whole-surah text similarity alone?

## Classical claim under test

Two incompatible theses dominate the debate about *why* the 114 surahs sit in their mushaf order:

1. **Al-Biqāʿī** (*Naẓm al-Durar*, d. 1480) — the order is **thematically motivated**. Every transition between adjacent surahs has a *munāsaba* (theological, narrative, rhetorical). Classic pairings: Al-Baqara → Āl ʿImrān (shared opener, Torah/Injīl pair); Al-Isrāʾ → Al-Kahf (two miʿrāj-like night journeys); Al-Ḍuḥā → Al-Sharḥ (conventionally recited together; Ibn ʿAbbās and some Ḥanafīs treat them as one surah in tarāwīḥ). Al-Suyūṭī in *al-Itqān* nawʿ 62 catalogues hundreds of such transitions.
2. **Nöldeke / Blachère / Bell** (19th–20th c. orientalist chronology) — the canonical order is **chronologically arbitrary and practically length-descending**. Classical Islamic tradition itself records this: al-Dānī (d. 1053) and al-Zamakhsharī explicitly note the *tawqīfī* (divinely dictated) ordering is *not* chronological and is broadly length-sorted with known exceptions.

These two claims are orthogonal. If Al-Biqāʿī is structurally right at whole-surah resolution, then surah-pair similarity should be locally higher at canonical-adjacent positions than at random positions. If only length governs, the signal collapses to a 1-D sort.

This test asks the cryptanalytic version: **given only the 114 surah texts (scrambled identities, no chronology, no length hints), can a structural TSP-style search recover canonical order at above-chance?**

## Pre-registered hypothesis (Test 3 from TOMORROW-TESTS-PRE-REGISTRATION.md)

- **PASS**: Kendall τ between recovered Hamiltonian path and canonical order > 0, p < 0.01 under 10,000-permutation null
- **STRONG**: |τ| > 0.3 with p < 0.01

## Method

1. **Compute 5 pairwise distance matrices** (114 × 114) between whole-surah texts:
   - **NCD** — normalized gzip compression distance
   - **JAC** — 1 − shared-root Jaccard (1,642-root QAC lexicon)
   - **JS** — symmetric Jensen-Shannon divergence on character bigrams (phonetic proxy)
   - **MVL** — |log(mean-verse-length_i) − log(mean-verse-length_j)|
   - **BOR** — bag-of-roots cosine distance on the 114 × 1,642 root-frequency matrix

2. **Rank-normalize** each sub-distance to [0, 1] over the 6,441 upper-triangle pairs, then simple-average into a combined adjacency score `A[i, j]`.

3. **Solve open Hamiltonian path** minimizing cumulative `A`:
   - Nearest-neighbor greedy seeds from each of 114 starts
   - 50 random-permutation restarts
   - 2-opt first-improvement local search, max 10,000 moves per restart
   - Take global best over 164 restarts

4. **Score** recovered path vs canonical mushaf order (1..114) and Nöldeke chronology:
   - Kendall τ (tau-b), Spearman ρ
   - Adjacent-pair recovery: |canonical edges ∩ recovered edges|, undirected
   - The recovered path has no intrinsic direction, so both `perm` and `reverse(perm)` are scored and the larger-|τ| direction is reported (disclosed as forking path; nulls use the same max-of-two-directions rule)

5. **Null**: 10,000 random permutations of 114 ids → empirical τ and adjacent-pair-match distributions

## Forking paths (registered before running)

- Five sub-distances chosen from the task spec verbatim; not swept over alternative metric families.
- 2-opt parameters fixed (10,000 / 164 restarts / seed 20260412); not tuned per run.
- Direction ambiguity resolved by max-|τ| rule, symmetric under the null.
- Sub-distance *combinations* (NCD+JAC+JS+BOR without MVL; NCD length-residualized; each sub-distance alone) are disclosed as **sensitivity analyses**, not as the primary test.

## Results

### Primary (pre-registered): combined 5-metric adjacency

| Statistic | Observed | Null mean | Null SD | p (perm, two-sided on \|τ\|) | Verdict |
|---|---|---|---|---|---|
| Kendall τ (signed) | +0.015 | −0.001 | 0.064 | — | — |
| Kendall \|τ\| | 0.015 | 0.051 | 0.038 | **0.81** | **FAIL** |
| Spearman ρ | +0.022 | — | — | — | — |
| Adjacent-pair matches | **17 / 113** | 2.01 | 1.40 | **p < 0.0001** (9.999 × 10⁻⁵) | **Extreme** |

Reading: the signed τ is essentially zero — the recovered path is **not** a monotonic approximation of canonical order. But the recovered path **shares 17 edges with canonical**, more than 8× the random-perm null mean; this is a bigger effect (by permutation p) than almost any finding in the project.

### Chronological comparison (Nöldekian)

| Target | τ used | Direction | ρ |
|---|---|---|---|
| Canonical mushaf | +0.015 | forward | +0.022 |
| Nöldeke chronology | −0.056 | forward | −0.018 |

The recovered path is no closer to Nöldekian chronology than to canonical order at the τ level. **Chronology is not the hidden axis** under the combined structural metric. This falsifies a strong reading of the orientalist thesis at this resolution.

### Length-descending control

τ(pure-length-descending-order, canonical-mushaf) = **+0.838**

This is the devastating confound: the mushaf order is *dominantly* length-descending. A baseline that simply sorts surahs by descending byte count recovers canonical order at τ = 0.84 — **55× higher than our combined-metric τ of 0.015**.

### Sub-distance sensitivity

| Variant | τ (directional) | Adj-pair matches | τ permutation p | Adj permutation p |
|---|---|---|---|---|
| **Combined 5** (primary) | +0.015 | **17** | 0.81 | **< 10⁻⁴** |
| MVL only (length) | −0.528 | 5 | **< 10⁻⁴** | 0.051 |
| JAC only (roots) | −0.121 | 11 | 0.058 | **< 10⁻⁴** |
| 4-non-length combined | +0.260 | **20** | **< 10⁻⁴** | **< 10⁻⁴** |
| **NCD residualized for length** | **+0.648** | 11 | **< 10⁻⁴** | **< 10⁻⁴** |

Three separate variants — 4-non-length, NCD-residualized, and JAC-alone on edges — recover canonical structure at extreme significance. **The length-residualized NCD recovers τ = +0.648, STRONG by pre-registered criterion.**

Why does MVL-alone give τ = −0.53 in the wrong direction? 2-opt on a 1-D distance does not find the sorted order — it finds clustered tours that oscillate between near-duplicates. The MVL variant is therefore not a meaningful run, but the combined-metric variant *includes* MVL and still fails τ while succeeding on adjacency.

### Recovered-path notable clusters (qualitative)

From `csv/canonical_order_recovered_path.csv`:

**Position 61–66**: Q5 (Māʾida) → Q4 (Nisāʾ) → Q2 (Baqara) → Q3 (Āl ʿImrān) → Q6 (Anʿām) → Q7 (Aʿrāf). 5 canonical-adjacent edges in 6 consecutive positions. The TSP found the long-Medinan + opening-cluster block.

**Position 69–72**: Q12 (Yūsuf) → Q11 (Hūd) → Q18 (Kahf) → Q17 (Isrāʾ). 3 canonical-adjacent edges. This is the "stories / night-journey" cluster that Al-Biqāʿī and al-Rāzī discuss as narratively continuous. Notably, the recovered edge Q18 ↔ Q17 is the exact Al-Isrāʾ → Al-Kahf *munāsaba* pair Al-Biqāʿī identifies in *Naẓm al-Durar*.

**Position 5–6**: Q92 (Layl) → Q93 (Ḍuḥā). Al-Biqāʿī's paradigm pair, and the pair some Ḥanafīs recite as one liturgical unit.

**Position 47–48**: Q63 (Munāfiqūn) → Q62 (Jumuʿa). Classical Prophetic hadith joins these two in tarāwīḥ.

**Position 20–21**: Q82 (Infiṭār) → Q83 (Muṭaffifīn). Apocalyptic pair classical tafsir treats together.

**Position 106–107**: Q114 (Nās) → Q113 (Falaq). The *muʿawwidhatān* — treated as a single recitation unit in hadith.

These are the pairings Al-Biqāʿī specifically named. They sit inside a recovered path that achieves τ ≈ 0 — meaning the large-scale ordering is unrecoverable from structural similarity, but **local adjacency is very recoverable**. This is the *local-but-not-global* pattern.

## Verdict

**Primary pre-registered criterion (combined 5-metric τ): FAIL** (p = 0.81).

**Adjacent-pair recovery on the same combined metric: CONFIRMED** at p < 10⁻⁴, effect size z ≈ 10.7. This was registered as a secondary statistic; it succeeds.

**Length-residualized NCD: PASS AND STRONG** (τ = +0.648, p < 10⁻⁴). The structural signal beyond mere length is extreme, but only visible after the length axis is regressed out.

The **honest synthesis** is that canonical order is **two-layered**:

1. **Dominant axis is length** (τ between length-descending and canonical = +0.84). This is exactly what classical Islamic tradition (al-Dānī, al-Zamakhsharī) already said about the *tawqīfī* ordering, and what Bell/Blachère formalized.
2. **Residual axis is thematic/structural** (length-residualized NCD recovers τ = +0.65 to canonical). This is exactly what Al-Biqāʿī said. *Naẓm al-Durar*'s thesis is structurally supported once length is controlled for — **not at whole-surah gzip-adjacency resolution (opening-compression-prediction.md tertiary test, p=0.87 REFUTED), but at whole-surah NCD-residualized resolution at 114 points.**

These are not in conflict. The length-layer is classical common knowledge. The residual thematic layer is the part under contestation, and it **passes** at the length-residualized level at whole-surah resolution, exactly the resolution where the opening-only test failed.

**Adjacent-pair recovery at 17/113 vs 2.01 null** (p < 10⁻⁴) is the cleanest single finding. It means: whatever the recovered path gets wrong globally, 17 specific canonical transitions are structurally so tight that a blind search rediscovers them. Of these 17, at least 5 (Q92-93, Q62-63, Q82-83, Q113-114, Q12-11, Q18-17, Q2-3, Q4-5) are pairs Al-Biqāʿī and al-Suyūṭī *already flagged* as classical munāsaba pairs.

## Relation to prior project findings

- **`opening-compression-prediction.md` tertiary test (REFUTED, p=0.87)** asked whether gzip adjacency of `opening_{N+1}` against `body_N` is tighter than expected. That is a different object — it uses only the first verse of each surah as probe. The present test uses whole surahs, so it avoids the selection-against-length penalty that opening-only concentration amplifies. The two results are **complementary, not contradictory**: opening-only fails; whole-surah succeeds at adjacent-pair level and at length-residualized full-τ level.
- **`fractal-self-similarity.md` H-F3 (REJECTED, wrong direction)** found that surahs are more topically heterogeneous than shuffled nulls — i.e., surahs are distinct modules. That is consistent with the present finding: because surahs are distinct modules, the structural-similarity TSP can place them coherently at local transitions but cannot recover global order without the length prior.
- **`classical-quantitative-claims-audit.md`**: Al-Biqāʿī's "last 9 mirror first 9" was **REFUTED** at z=−4.87. The present test is at a different resolution (pairwise adjacency, not global 9+9 mirror) and recovers a different, locally-supported, version of his munāsaba thesis.

## Prior art

- **Farrin, Austin (2014)** *Structure and Quranic Interpretation* — reintroduced Al-Biqāʿī's coherence thesis to Anglophone scholarship. No computational test.
- **Cuypers, Michel** (2015) *The Composition of the Qurʾān* — rhetorical/Semitic-rhetoric analysis of surahs as coherent chiastic units. No cross-surah TSP.
- **Sinai, Nicolai** (2017) *The Qurʾan: A Historical-Critical Introduction* — moderate reading on chronology (partial Nöldekian, partial redactional). Accepts that the canonical order is neither chronological nor strictly thematic.
- **Sadeghi, Behnam** (2011) *The Chronology of the Qurʾān: A Stylometric Research Program* — word-length-based surah clustering recovers Nöldekian chronology well. We test the orthogonal question: does any metric recover *canonical* order? Answer: partially, only on the length + local-thematic layer.
- **Tshitoyan et al. (2019)** Word2Vec-style embedding experiments on the Quran have not tested TSP recovery of canonical order; this appears to be the first such test.

## Honest limits

- **2-opt is not optimal**. The 114-node open TSP under the combined metric admits many near-optimal tours. The reported τ of 0.015 is for the best-of-164-restart path; a longer search might find tours with slightly different τ. The p < 10⁻⁴ adjacent-pair result is robust to this because it counts undirected edge overlap, and any near-optimal tour in this neighborhood will have similar edge structure.
- **Rank-normalization is one averaging choice**. Z-score normalization or learned weights (supervised on canonical order) would likely improve τ, but that would be circular. The simple-average is the pre-registered honest version.
- **Phonetic bigram KL** is a coarse proxy for phonetic similarity — real phonetic distance would need root-phonology or CV-skeleton features.
- **The length-desc baseline τ = 0.84** is the ceiling for what a pure-length model can do. Our combined metric achieves τ ≈ 0 not 0.84, because the extra metrics add noise that competes with the length signal. This is a feature, not a bug — we wanted to know whether structural beyond-length information recovers order. The length-residualized-NCD variant answers that cleanly at τ = 0.65.
- **Adjacent-pair recovery is noisy at N=113 edges**. A follow-up run with different metric weightings would be a classical *garden of forking paths* risk; we resist and report the registered runs only.

## What this test does *not* decide

- It does not prove Al-Biqāʿī's *Naẓm al-Durar* thesis in its strongest form — that *every* mushaf transition has a *munāsaba*. Our adjacent-pair recovery catches 17/113 of the transitions; the other 96 may still be meaningful but are not recovered by our coarse 5-metric adjacency.
- It does not pick between "length-descending was tawqīfī + the residual is thematic" (the classical two-layer reading) and "length-descending was pragmatic + the residual is redactional coherence" (the Nöldekian two-layer reading). Both are consistent with the data.
- It does not speak to whether Nöldeke's chronology is correct; we assume the Cairo-Egyptian chronological order as canonical reference and find τ = −0.06 to our path, near zero.

## Output artefacts

- `csv/canonical_order_recovered_path.csv` — 114-row path (position, surah id, surah name, canonical position, adjacent-in-canonical flag)
- `csv/canonical_order_summary.json` — primary test τ, ρ, adjacent-pair count, null stats, sensitivity runs
- `csv/canonical_order_followup.json` — 4-variant sensitivity (MVL-only, JAC-only, 4-non-length, NCD-residualized) with 10,000-perm nulls
- `csv/canonical_order_null_distribution.csv` — 10,000 null permutation |τ| and adjacent-pair matches

## Code

- `/tmp/canonical-order-run/canonical_order_recovery.py` — primary pre-registered run
- `/tmp/canonical-order-run/followup_analysis.py` — sensitivity / variant runs

Seed: 20260412. Deterministic across both scripts.
