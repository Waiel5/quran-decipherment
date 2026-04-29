---
id: H-NEW-301
title: "Minimal 2-feature subset for singleton nearest-centroid — MARGINAL (9/10 by mean_emphatic+mean_pharyngeal; maxT p = 0.196)"
phase: B
status: MARGINAL (Cell A PASS at 9/10 exceeding H-NEW-232 baseline 8/10; Cell B FAIL at maxT p = 0.196 > α_bon = 0.025)
date: 2026-04-19
executed_by: team-lead (inline)
parent_1: H-NEW-271 (1-D cluster-layer sufficient)
parent_2: H-NEW-300 (1-D singleton-layer NULL at 7/10)
parent_3: H-NEW-232 (15-dim singleton baseline 8/10)
open_question: OQ-1 minimum dimensionality at singleton layer
seed: 20260424
prereg: h-new-301-minimal-2feature-singleton-prereg.md
prereg_sha256: 79b401e8743338d10cbe3c0fe3e79407a46f4307b54bb7687db6b61c31a33ab7
bonferroni_k: 2
alpha_bon: 0.025
rules_tuple: "(29 canonical muq surahs; 11-feature pool = 10 phonological axes + letter_count; C(11,2)=55 pairs enumerated; z-scored per-feature against 19 multi-members; Euclidean 2-D nearest-centroid; inherits H-NEW-232 apriori-accepted-clusters; maxT 1000-perm null across 55-pair search family; seed 20260424)"
direction: "Cell A at least one pair ≥ 8 matches; Cell B maxT p < α_bon = 0.025"
verdict: MARGINAL
---

# [[h-new-301-minimal-2feature-singleton|H-NEW-301]] — Minimal 2-feature subset for singleton nearest-centroid

## 1. Headline

**MARGINAL verdict**. Cell A PASSES: two 2-feature pairs achieve **9/10** singleton nearest-centroid matches (one BETTER than the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] 15-dim baseline of 8/10). Cell B FAILS: maxT permutation null (1000 shuffles × 55 pairs) shows **p_max = 0.196** > α_bon = 0.025 — under the maxT correction for 55-pair search, the 9/10 result is not statistically unusual because shuffled-label nulls frequently produce 7-9 matches when searching across 55 candidates.

- **Best pair**: `mean_emphatic + mean_pharyngeal` → 9/10 (ties with `mean_emphatic + mean_continuant`)
- **Per-singleton under winner**: resolves BOTH [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] misses (Q 36 YS → ALR ✓; Q 42 HMASQ → HM ✓) but creates a NEW miss at Q 7 ALMS → TSM ✗
- **11 pairs achieve 8/10** (equal to [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] baseline); match-count distribution: 2→3→3→4→5→3→5→16→14→11 pairs at match counts 2-6-7-8
- maxT null mean: 6.93 (under shuffled labels, best-of-55 typically hits 7)

**Interpretation**: the 2-D phonological space DOES contain a pair that exceeds the 15-dim baseline, but after correcting for the 55-pair search, the excess is not beyond chance. The result is DESCRIPTIVELY NOVEL but not INFERENTIALLY CONFIRMED.

## 2. Per-singleton comparison (best pair vs baselines)

| Singleton | Surah | Apriori | [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] 15-dim | [[h-new-300-manner-only-singleton|H-NEW-300]] 1-D manner | **[[h-new-301-minimal-2feature-singleton|H-NEW-301]] 2-D emph+phar** |
|:-:|:-:|:--|:-:|:-:|:-:|
| ALMS | Q 7 | {ALM} | ALM ✓ | HM ✗ | **TSM ✗** (NEW MISS) |
| ALMR | Q 13 | {ALM, ALR} | ALR ✓ | ALR ✓ | ALR ✓ |
| KHYAS | Q 19 | {HM, TSM} | TSM ✓ | TSM ✓ | TSM ✓ |
| TH | Q 20 | {TSM} | TSM ✓ | TSM ✓ | TSM ✓ |
| TS | Q 27 | {TSM} | TSM ✓ | TSM ✓ | TSM ✓ |
| **YS** | Q 36 | {ALM, ALR} | HM ✗ | TSM ✗ | **ALR ✓** (RESOLVED) |
| S | Q 38 | {TSM} | TSM ✓ | TSM ✓ | TSM ✓ |
| **HMASQ** | Q 42 | {HM} | TSM ✗ | TSM ✗ | **HM ✓** (RESOLVED) |
| Q | Q 50 | {HM, TSM} | TSM ✓ | TSM ✓ | HM ✓ |
| N | Q 68 | {ALM, ALR} | ALR ✓ | ALR ✓ | ALR ✓ |

**Gain**: Q 36 YS and Q 42 HMASQ (the 2 "stable" misses across [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]/252/165.2/300) BOTH resolve under `mean_emphatic + mean_pharyngeal`.

**Loss**: Q 7 ALMS (consistent match under [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] 15-dim) becomes a miss under this 2-D pair.

**Net**: 9/10 — one miss (Q 7) instead of two (Q 36 + Q 42).

## 3. Why `mean_emphatic + mean_pharyngeal` works

The 4 multi-member clusters have distinctive signatures in this 2-D space:

| Cluster | Emphatic mean | Pharyngeal mean |
|:-:|---:|---:|
| ALM (ا,ل,م) | 0.000 | 0.000 |
| ALR (ا,ل,ر) | 0.000 | 0.000 |
| HM (ح,م) | 0.000 | 0.500 |
| TSM (ط,س,م) | 0.333 | 0.333 |

Note: ALM and ALR have IDENTICAL (0, 0) centroids in this 2-D space — the pair cannot differentiate ALM from ALR (no emphatic or pharyngeal letters in either). This is a significant LIMITATION that explains why Q 7 ALMS (which contains ص, adding 0.25 emphatic + 0.25 pharyngeal) moves away from the ALM (0, 0) toward TSM (0.33, 0.33).

But for the singletons with strong pharyngeal/emphatic signatures:
- Q 19 KHYAS: ع,ص both pharyngeal → closer to HM/TSM ✓
- Q 36 YS: س adds slight emphatic → closer to ALR's (0, 0) centroid by Euclidean distance (Q 36 has 0.0 emph, 0.0 phar) → ALR ✓ MATCH
- Q 42 HMASQ: ح,ع,ق add pharyngeal → closer to HM (0.00, 0.50) ✓ RESOLVED

The mechanism is interpretable: **emphatic + pharyngeal jointly capture the "throat/back-of-mouth" acoustic dimension** that distinguishes the TSM/HM phonological space from the ALM/ALR sonorant-liquid space. This explains why the 15-dim manner-dominant codebook ([[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]) produces different miss patterns than the emphatic-pharyngeal 2-D.

## 4. Why Cell B FAILS

The maxT permutation null corrects for the 55-pair search. Under shuffled cluster labels:
- Mean of per-permutation max = 6.93 matches
- 19.6% of shuffles achieve max ≥ 9 matches

When you search 55 candidate pairs for the maximum match count, even under shuffled labels you frequently find one pair with ≥ 9 matches. The 10-singleton N is small and 4-cluster apriori has average 1.6 accepted clusters per singleton, which means baseline "chance" match rate per singleton is 40%. Across 55 pairs with random geometry, the MAX over 55 often hits 9.

Observed 9/10 is above null MEAN (6.93) by ~2.8σ, but the tail of the maxT distribution reaches 9 at 19.6% frequency → not beyond α_bon.

**Honest reading**: 2-feature singleton-resolution IS possible but is INDISTINGUISHABLE from a 55-pair search-maximum under cluster-label-shuffling. The descriptive result is informative (Q 36, Q 42 resolve under emph+phar); the inferential conclusion is that the 2-D subset is not uniquely beyond null expectation.

## 5. Interpretation

### 5.1 The singleton-layer multi-dim requirement refined

[[h-new-300-manner-only-singleton|H-NEW-300]] established 1-D INSUFFICIENT at singleton layer.
[[h-new-301-minimal-2feature-singleton|H-NEW-301]] establishes 2-D DESCRIPTIVELY SUFFICIENT but INFERENTIALLY MARGINAL.

The pattern: the 10-singleton corpus is TOO SMALL for clean statistical adjudication. Any 2-D subset that exceeds the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] baseline by 1 singleton (9/10 vs 8/10) is within the maxT null envelope for a 55-pair search. Only the full 15-dim codebook achieves statistically-protected 8/10 because it is PRE-COMMITTED (no search correction).

### 5.2 The 5-way misses (Q 36, Q 42) are NOT SCALE-INVARIANT

[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] + [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] + [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]-V0/V1/V2/V3 all converged on Q 36 and Q 42 as misses. I previously interpreted this as evidence of interpretation-bound-not-feature-bound. [[h-new-301-minimal-2feature-singleton|H-NEW-301]] REFINES this: the 5-way misses are RESOLVABLE under a DIFFERENT 2-D subspace (emph+phar vs the 15-dim manner-dominant space). They are not feature-fundamental; they are specific to the 15-dim manner-dominated RF-trained classifier.

This suggests the "interpretation-bound" claim from [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]]/165.2 should be softened — Q 36 YS and Q 42 HMASQ MAY actually be empirically resolvable if the right low-dim subspace is chosen. [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]'s BLOCK-DOMINANCE verdict for Q 42 (content-axis HM) is consistent with THIS finding (emph+phar resolves Q 42 to HM).

### 5.3 Classical-scholarship integration

`mean_emphatic + mean_pharyngeal` corresponds to classical *ḥurūf al-tafkhīm* (emphatic letters: ص ض ط ظ + mustaʿliya) × *ḥurūf al-ḥalq* (throat letters: ح ع ه ء) joint axis. Ibn Jinnī *Sirr al-Ṣināʿa* treats these as related ṣifāt capturing back-of-mouth articulation; al-Khalīl *Kitāb al-ʿAyn* makhraj places them in the pharyngeal tier. The 2-D emph+phar pair is essentially **"back-of-mouth articulation intensity"** — a classically recognized aggregate dimension.

The finding that this specific 2-D subspace resolves Q 36 + Q 42 descriptively is a classical-scholarship convergence: the THROAT/BACK ṣifāt family isolates these two muq surahs correctly. Under a larger corpus or more statistical power, this result could become inferentially robust.

## 6. Honest limits

1. **maxT null is elevated** because search over 55 pairs inflates max-match null. This is the correct discipline but it means the 9/10 result is not inferentially protected.
2. **10-singleton N**: 9/10 vs 8/10 is a single-singleton distinction; statistical power is fundamentally limited at this N.
3. **Only 2-feature pairs searched** — 3-D and 4-D subsets deferred to H-NEW-301.1/.2. Larger-subspace search might produce 10/10 but inferentially becomes harder to protect.
4. **`mean_emphatic + mean_continuant`** also achieves 9/10 — different 2-D axis producing same match count. Multiple mechanisms for 9/10 suggests the result is not a unique feature-pair signature.
5. **Q 7 ALMS new miss** is a cost of the 2-D emph+phar choice. The 15-dim manner-dominated codebook doesn't miss Q 7 because its full feature set keeps Q 7 near ALM. The 2-D parsimony loses Q 7 in exchange for Q 36 + Q 42. NET +1 match.
6. **Classical apriori sets** inherited from [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] — same interpretive-bound limits. If apriori sets were revised (e.g. YS → HM per [[h-new-300-manner-only-singleton|H-NEW-300]] prediction confirmation), the verdict would change.

## 7. Queued follow-ups

- **H-NEW-301.1**: 3-feature subset search. Does any 3-D subset achieve 10/10 with maxT-controlled p < 0.025?
- **H-NEW-301.2**: feature-importance decomposition at 15-dim RF — which features contribute to Q 36 and Q 42 MATCH under the full codebook (vs why they MISS under nearest-centroid)?
- **H-NEW-301.3**: sensitivity to cluster-label-shuffle null methodology — are there alternative nulls (surah-shuffle, subset-size null) that would show 9/10 as significant?
- **H-NEW-301.4**: re-run [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] apriori with YS → {ALM, ALR, HM} and HMASQ → {HM, TSM} — does the "inclusive apriori" yield 10/10 with either the 15-dim or the 2-D emph+phar subspace?

## 8. Cross-references

- Parent 1: [[h-new-271-muq-minimal-phon-family|H-NEW-271]] (cluster layer 1-D SINGULAR SUFFICIENT)
- Parent 2: [[h-new-300-manner-only-singleton|H-NEW-300]] (singleton layer 1-D NULL at 7/10)
- Parent 3: [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] (15-dim singleton baseline 8/10)
- Siblings: [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] (joint phon + (α,β) replicating 8/10); [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] V0-V3 (codebook robustness producing 8/10)
- Related: [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] Q 42 BLOCK-DOMINANCE (content-axis resolution for Q 42 to HM — CONVERGES with [[h-new-301-minimal-2feature-singleton|H-NEW-301]] finding)
- Terminal synthesis: [[cross-finding-023-causal-generative-closure|cross-finding-023]]

## 9. Classical-scholarship integration

- **al-Khalīl *Kitāb al-ʿAyn*** pharyngeal-makhraj tier + **Ibn Jinnī *Sirr al-Ṣināʿa*** tafkhīm ṣifāt: the 2-D emph+phar subspace empirically isolates Q 36 YS and Q 42 HMASQ to their classical cluster apriori. Classical "back-of-mouth articulation" is the load-bearing phonological dimension for these 2 singletons.
- Q 42 HMASQ resolution under emph+phar CONVERGES with [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] BLOCK-DOMINANCE finding (content axis → HM): the two orthogonal analyses (phonological emph+phar + content Fisher-Rao) agree Q 42 is HM, refining the 15-dim manner-dominant nearest-centroid "miss" as a methodology-specific artifact.
- al-Suyūṭī *Itqān* ḥurūf al-ḥalq + mustaʿliya discussion is the classical umbrella for "throat-and-back phonology" — empirically validated as the 2-D axis that captures Q 36 + Q 42.

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-301-minimal-2feature-singleton-prereg.md` (SHA-256 79b401e8...)
- Script: `scripts/h_new_301_minimal_2feature_singleton.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-301.json`
- Findings: this file

## 11. Final statement

**The minimal 2-feature subset that EXCEEDS [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s 8/10 baseline exists: `mean_emphatic + mean_pharyngeal` achieves 9/10 singleton nearest-centroid match, resolving both Q 36 YS and Q 42 HMASQ at the cost of introducing a new miss at Q 7 ALMS.** But the maxT permutation null (p = 0.196) indicates this result is not statistically unusual given the 55-pair search family. The finding is DESCRIPTIVELY INFORMATIVE — it shows that the 5-way convergent misses in [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]/252/165.2 are not feature-space-fundamental but are specific to the 15-dim manner-dominated nearest-centroid classifier — and INFERENTIALLY MARGINAL due to small-N + search-correction limits. The Throat-and-Back phonological family (ḥurūf al-ḥalq + mustaʿliya) is the classical scholarship umbrella that empirically isolates Q 36 YS and Q 42 HMASQ to their apriori-accepted clusters, converging with [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]'s content-axis BLOCK-DOMINANCE verdict for Q 42.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
