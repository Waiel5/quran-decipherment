---
finding: H-NEW-2470
title: Ordering-by-dispersion as a formal corpus law — per-surah similar-pair adjacency-depletion generator
type: pre-registration
date: 2026-05-30
author: Waiel Al-Shujaa
seed: 20260509
nperm: 10000
status: LOCKED-BEFORE-INFERENCE
---

# H-NEW-2470 — Pre-registration: ORDERING-BY-DISPERSION as a formal corpus law

## 0. Why this finding exists (the 3-finding convergence to be formalised)

Three independently pre-registered findings already converge on a single mechanism — that the
canonical verse-order SPACES near-identical / repeated verses rather than stacking them:

- **H-NEW-2310 (§10.93)** — refrain / exact-repeated-verse census: refrain spacing is more
  *regular* than chance (5/9 refrain-pairs metronomic); Q55 *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān*
  is the paradigm of a metronomically interleaved refrain.
- **H-NEW-2420 (§10.108)** — within-surah sequential naẓm: corpus adjacent-cohesion Z=+18.70, but the
  standout REVERSAL is **Q55 al-Raḥmān z=−5.32** — its 31 refrains are interleaved so that ZERO are
  adjacent; shuffling clumps them, so canonical order is *anti-adjacent by design*.
- **H-NEW-2450 (§10.125)** — adjacent near-verbatim reprise: H1 ("adjacent more than chance")
  REVERSED → NULL — the corpus is adjacent-DEPLETED. The diagnostic isolated the cause:
  **Q55 alone supplies 12.1 of the 17.3 within-surah-shuffle null mean — 465 near-identical
  unordered verse-pairs, ZERO adjacent**; then Q77, Q26, Q37, Q54, all 0 adjacent.

H-NEW-2450 measured ONE global statistic (a single N_low band, char-edit ≤ 3). This finding
PROMOTES that observation to a **per-surah generator**: for every surah, it computes the full set
of near-identical / repeated verse-pairs and runs a *per-surah permutation test of
adjacency-depletion*. It converts a single global reversal + a hand-noted diagnostic into a
direction-locked, Bonferroni-corrected, per-surah corpus law with an explicit roster of which
surahs most strongly disperse.

## 1. Definitions (LOCKED)

### 1.1 Rules-tuple
`(no-tashkeel, QAC-v0.4-ROOT + orthographic-graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.
Two similarity channels are combined (root-set and orthographic), each grounded in a canonical
artefact on disk. Default project tuple otherwise.

### 1.2 Verse text + tokenization (the H-NEW-2380/2450 waqf lesson — LOCKED)
Verse text from `quran-text/quran-no-tashkeel.json`. NFC-normalise, then STRIP every codepoint in
the locked PAUSE set (waqf / codex annotation glyphs U+06D6–U+06ED, i.e. the 24 codepoints
`range(0x06D6, 0x06EE)`), then whitespace-split into lexical tokens. Identical to H-NEW-2450 §1.3.

### 1.3 Verse root-sets (the H-NEW-2420/2280 instrument — LOCKED)
Per-verse root-set `R(s,v)` = set of QAC v0.4 ROOT tags for that verse, taking the FIRST ROOT-tagged
feature per morphological segment, from `data/morphology/quranic-corpus-morphology-0.4.txt`.
This is byte-identical to the instrument that produced the Q55 z=−5.32 result (H-NEW-2420).

### 1.4 Substantive filter (LOCKED)
A verse is **substantive** if it has ≥ 3 lexical tokens (matches H-NEW-2450 SUB=3). Only
substantive verses participate in the similar-pair set (this excludes muqaṭṭaʿāt-only and ultra-short
verses whose tiny edit distances / empty root-sets are artefacts, not "reprise"). Non-substantive
verses still occupy their canonical positions (they are valid shuffle slots) but are never counted as
similar-pair members.

### 1.5 Similar-pair definition (the GENERATOR core — LOCKED, PRE-REGISTERED THRESHOLD)
For each surah, consider every UNORDERED pair of distinct substantive verses {u, w} (u ≠ w, any
distance). The pair is **SIMILAR** iff EITHER channel fires:

- **Root channel:** root-Jaccard `J(R_u, R_w) = |R_u ∩ R_w| / |R_u ∪ R_w| ≥ J_THR`, with **J_THR = 0.80**.
- **Orthographic channel:** char-level Levenshtein over the two verses' concatenated token-strings
  (tokens joined with no separator, the Q094-F-01 / H-NEW-2450 `.replace(' ','')` convention)
  `c_ed ≤ C_THR`, with **C_THR = 5**.

The UNION (`J ≥ 0.80 OR c_ed ≤ 5`) is the primary similar-pair set. Both thresholds are locked here
BEFORE any computation. Rationale: J_THR=0.80 captures refrains and near-verbatim repeats (≥80% of the
combined root inventory shared) while excluding merely-thematically-related verses; C_THR=5 captures
near-verbatim orthographic reprises (the connective-prepend / fāṣila-swap family from H-NEW-2380/2450)
that root-Jaccard can miss when re-tuning changes a rhyme word's root. The two channels are
complementary (root = semantic skeleton; char = surface form).

### 1.6 Adjacency (LOCKED)
A similar-pair {at canonical verse-positions p, q} is **ADJACENT** iff `|p − q| = 1` (immediate
neighbours in canonical Hafs-Kufan within-surah order). Cross-surah junctions are irrelevant (pairs
are within-surah by construction). A secondary **NEAR-ADJACENT** count (`|p − q| ≤ 2`) is reported as
a descriptive robustness lens but the LOCKED test statistic uses strict adjacency `=1`.

## 2. The per-surah test statistic + null (LOCKED)

For each surah s with `m_s` substantive verses and similar-pair set `S_s`:
- **Observed statistic** `A_obs(s)` = number of pairs in `S_s` that are ADJACENT in canonical order.
- **Null:** within-surah verse-order SHUFFLE — randomly permute the positions of ALL the surah's verses
  (substantive and non-substantive alike; the non-substantive verses are real slots that can separate
  reprise members), recompute how many of the SAME unordered similar-pairs `S_s` land adjacent.
  This preserves the surah's exact verse multiset, length, and the similar-pair *set* itself; it
  isolates "did the composer place similar verses next to each other" from the pair set's size.
  10,000 permutations, seed 20260509.
- `null_mean(s)` = mean adjacent-count under shuffle; `p_left(s)` = (#{null ≤ A_obs} + 1)/(nperm+1)
  (LEFT tail — depletion); `z(s) = (A_obs − null_mean)/null_std`.
- A surah is **DISPERSING** iff `A_obs(s) < null_mean(s)` (fewer-adjacent than chance).

### Eligibility for the per-surah significance family
A surah enters the Bonferroni family iff it has `|S_s| ≥ 1` similar-pair AND `null_std(s) > 0`
(i.e. the shuffle null is non-degenerate — there must be ≥1 pair that *can* be moved). Surahs with no
similar-pairs are reported (count 0) but carry no test. The family size `k` is computed from data at
runtime; **Bonferroni α = 0.05 / k**, reported alongside raw p.

## 3. Pre-registered hypotheses (DIRECTION-LOCKED, family of 2 hypothesis-arms)

### H1 — CORPUS-WIDE DISPERSION (PRIMARY)
**Locked claim:** corpus-wide, similar verse-pairs are LESS adjacent than chance — the canonical
order DISPERSES look-alikes.

- **Aggregate statistic:** `A_total_obs = Σ_s A_obs(s)` vs the within-surah-shuffle null total
  `Σ_s A_perm(s)` accumulated per permutation across all surahs (a single 10,000-perm corpus null on
  the summed adjacency count). Direction LOCKED: `A_total_obs < null_mean_total`. One-sided LEFT-tail
  p = (#{null ≤ obs}+1)/(nperm+1).
- **Per-surah corroboration:** sign-test on the eligible family — the number of DISPERSING surahs
  (`A_obs < null_mean`) should EXCEED the number of CLUMPING surahs; and a Stouffer combination of the
  per-surah LEFT-tail p-values should be significant in the depletion direction.
- **PASS:** `A_total_obs < null_mean_total` AND aggregate p < 0.025 (Bonferroni over the 2 arms) AND
  the sign-test direction holds (more dispersing than clumping).
- **REVERSED → NULL with full prominence:** if `A_total_obs ≥ null_mean_total` (similar-pairs are
  adjacent more than / as much as chance), this is a pre-commit violation, published as NULL. This is
  the *direct contradiction* of the 3-finding convergence and would falsify the dispersion law.

### H2 — REFRAIN/REPETITION-HEAVY CONCENTRATION (SECONDARY)
**Locked claim:** the dispersion effect is CONCENTRATED in refrain/repetition-heavy surahs, named
a-priori as **{Q55, Q77, Q26, Q37, Q54}** (the exact set the task pre-specifies, matching the
H-NEW-2450 diagnostic top-dispersers).

- **Statistic:** Δ = mean per-surah depletion magnitude `D(s) = null_mean(s) − A_obs(s)` over the named
  set MINUS the mean `D(s)` over all other eligible surahs. Direction LOCKED: Δ > 0 (named set depletes
  MORE in absolute pairs-dispersed).
- **Null:** 10,000 label-permutations — shuffle which 5 eligible surahs carry the "named" label,
  recompute Δ. Seed 20260509+2. One-sided p = (#{null ≥ obs}+1)/(nperm+1).
- **PASS:** Δ > 0 AND p < 0.025 (Bonferroni). **REVERSED → NULL** if Δ ≤ 0.
- Note: because the named set is pre-specified from a PRIOR finding's diagnostic (H-NEW-2450), this
  arm is partially confirmatory of that diagnostic; it is reported as SECONDARY and the primary
  law-claim rests on H1, which uses NO hand-picked surahs.

## 4. Rules-tuple robustness (MW-3 alternative-models — LOCKED variants)
The verdict must survive threshold perturbation. Re-run H1 (aggregate only) under each locked variant:
- **V1 (tight root):** `J_THR = 0.60 OR c_ed ≤ 3` (looser root, tighter char — different balance).
- **V2 (root-only):** `J_THR = 0.80`, NO char channel.
- **V3 (char-only):** `c_ed ≤ 5`, NO root channel.
- **V4 (near-adjacent):** primary thresholds but adjacency = `|p−q| ≤ 2`.
All four report `A_total_obs`, `null_mean_total`, `p_left`. The primary verdict is the UNION/strict-adjacent
spec (§1.5/§1.6); variants establish robustness. If the sign of the effect FLIPS across variants the
disagreement is reported prominently and the primary (union/strict) governs.

## 5. MW protections
- **MW-1 (instrument-prior):** similarity channels, thresholds, adjacency, substantive filter, PAUSE
  set all defined here BEFORE running.
- **MW-2 (corpus-prior):** 10,000-perm permutation nulls (aggregate + per-surah + H2 label-perm).
- **MW-3 (alternative-models):** 4 locked threshold/adjacency variants (§4).
- **MW-5 (replication):** H1 aggregate replicated at a second seed (20260509+10).
- **MW-6 (instrument-control):** the substantive ≥3-token filter controls for ultra-short / muqaṭṭaʿāt
  artefacts; the within-surah shuffle (not global) controls for surah-length homogeneity; H2
  label-shuffle is the genre control.
- **MW-7 (post-hoc cap):** the named H2 set is pre-registered (not post-hoc); the near-adjacent ≤2 lens
  is descriptive robustness, the strict =1 band is the locked test.

## 6. Failure / honesty conditions
- Reversed direction on H1 = pre-commit violation → NULL with full prominence (no massaging, no silent
  re-lock). H1 reversal would directly falsify the dispersion law and would RETRACT the cross-finding-028
  promotion recommendation.
- If H1 PASSES but H2 reverses, the law stands as a CORPUS-WIDE effect that is NOT specially concentrated
  in the named refrain set (reported honestly; the named-set claim is demoted).
- Genre / register language (refrain-heavy) is a structural-class observation, not a theological claim.

## 7. Cross-finding-028 promotion (conditional, drafted in advance)
IF H1 PASSES: recommend promoting **cross-finding-028 — the repetition-spacing (ordering-by-dispersion)
law** on the 4-finding convergence (H-NEW-2310 + 2420-Q55 + 2450 + THIS). Draft statement is written in
the findings file's final section. IF H1 reverses, NO promotion; the recommendation is withdrawn.

## 8. Anti-hallucination
Every count, coordinate, root-set, Arabic string and p-value is computed at runtime from
`quran-text/quran-no-tashkeel.json` and `data/morphology/quranic-corpus-morphology-0.4.txt`.
Region tags from the JSON `type` field; named-set membership is the literal 5-surah set in §3-H2.
No numerical value is asserted from memory.

Seed 20260509. 10,000 permutations. This file is SHA-256-locked; the run script embeds the hash and
fails fast on mismatch.
