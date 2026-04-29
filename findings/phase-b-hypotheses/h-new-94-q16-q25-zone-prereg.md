---
id: H-NEW-94
title: Q 16-25 cluster-empty zone deep-dive — isolate-count reconciliation + shadow-cluster hunt
phase: B
status: PRE-REGISTERED 2026-04-17
spec_locked_at: 2026-04-17 (BEFORE running content-similarity / permutation test)
agent: h-new-94-specialist
parent_findings:
  - H-NEW-89 (meta-cluster network; Q 16-25 identified as largest cluster-empty stretch with 8/10 isolates)
  - H-NEW-66 (verse-twin network; corpus-wide top-50 edges)
  - H-NEW-58c (musabbiḥāt; includes Q 17-adjacent "subḥāna alladhī asrā" motif)
  - cross-finding-008 (muqaṭṭāʿat as book-introduction markers; Q 19, 20 are singleton openers)
  - OQ-2 (open question: what is special about the Q 16-25 zone?)
bonferroni_family: h-new-94-cluster-empty-zone
bonferroni_k: 2
alpha_bon: 0.025
direction_A: "count-correction expected (0 discovered = real cluster-empty, 2+ = deflation); descriptive cell, α=0.025 not applied"
direction_B: "Q16-25 internal-similarity HIGHER than random 10-surah windows (one-sided upper)"
acceptance_window: "cell-B is PRIMARY and inferential; cell-A is DESCRIPTIVE reconciliation"
seed: 20260417
n_perm: 10000
rules_tuple: "(no-tashkeel; whitespace-tokenized with recitation-marks filtered; root-membership taken from data/morphology/surah-root-graph.json; cluster-membership rule-set identical to H-NEW-89's locked ≥2-surah classical multi-surah clusters)"
---

# [[h-new-94-q16-q25-zone|H-NEW-94]] — Q 16-25 cluster-empty zone deep-dive (Pre-registration)

## Context and motivation

[[h-new-89-meta-cluster-network|H-NEW-89]] (Meta-Cluster Network Synthesis, 2026-04-15) reported that the
Q 16-25 stretch contains 8 of 10 isolate surahs (the largest
cluster-empty contiguous region in the Quran). However, Q 19 Maryam
opens with muqaṭṭāʿat كهيعص and Q 20 Ṭā-Hā with طه — neither can
literally be "isolated from the muqaṭṭāʿat cluster system" in any
naïve reading.

[[h-new-89-meta-cluster-network|H-NEW-89]]'s locked rule list resolves this: a cluster in that study
requires ≥2 surahs sharing the same muqaṭṭāʿat opener. كهيعص and طه
are classical singletons (no other surah shares their letter
sequence), so under the ≥2-member rule they belong to no
muqaṭṭāʿat cluster, making them isolates by definition.

This pre-reg (i) makes that reconciliation explicit and (ii) tests a
downstream question: if we set aside the "big classical cluster"
systems and instead ask about CONTENT-similarity density, does
Q 16-25 exhibit a SHADOW cluster — an internally-dense subnetwork
invisible to the [[h-new-89-meta-cluster-network|H-NEW-89]] cluster taxonomy?

## Question

Two pre-committed test cells:

### Cell A — Isolate-count reconciliation (descriptive)

Recompute the isolate count under [[h-new-89-meta-cluster-network|H-NEW-89]]'s exact cluster-membership
rule set (11 locked clusters, ≥2-surah classical multi-surah clusters
only). Confirm or correct the count. If discovered errors change the
count, update downstream.

### Cell B — Shadow-cluster hunt (primary inferential)

For the 10-surah window Q 16-25, compute pairwise content-similarity
and test whether its internal density is higher than random 10-surah
windows elsewhere in the mushaf.

## Locked data + preprocessing

- **Corpus**: `quran-text/quran-no-tashkeel.json` via `analysis.tools.loader.load_quran("no-tashkeel")`.
- **Per-surah root multisets**: `data/morphology/surah-root-graph.json`
  (bipartite surah × root graph, 1642 roots, counts per surah — from
  the Quranic Arabic Corpus morphology 0.4). This is the operationalization
  of root-Jaccard.
- **Verse-twin network**: pre-computed top-50 edges in
  `findings/phase-b-hypotheses/csv/h-new-66.json`. Used AS-IS for
  the verse-twin-count axis of the similarity matrix. No re-computation.
- **Character 5-gram ([[h-new-66-verse-twins-network|H-NEW-66]] operationalization) at the SURAH level**:
  concatenate all verses of a surah with single-space separators, strip
  recitation marks U+06D6..U+06ED, collapse whitespace, compute length-5
  character n-gram multisets. This is the third similarity axis.

## Locked operationalizations (Cell B)

Three pairwise surah-similarity metrics, computed for all 114 × 114
surah pairs:

### S1 — Root-Jaccard

For surahs i, j, let R_i, R_j be the SETS of roots occurring ≥1×
(binary membership; count ignored). Jaccard(i, j) = |R_i ∩ R_j| / |R_i ∪ R_j|.
Range [0, 1].

### S2 — Character 5-gram Dice coefficient

For each surah, build a multiset M_i of length-5 character windows
over the normalized concatenation. Define

  Dice(i, j) = 2 · |M_i ∩ M_j|_multiset / (|M_i| + |M_j|)

where |·|_multiset is the sum of min-counts. Normalizes for surah
length. Range [0, 1].

### S3 — Verse-twin-edge count ([[h-new-66-verse-twins-network|H-NEW-66]])

Count the number of top-50 [[h-new-66-verse-twins-network|H-NEW-66]] edges with one verse in surah i
and the other in surah j. Small-integer count.

### Aggregate similarity — S_agg

Each pair (i, j) with i ≠ j gets a **rank-averaged** aggregate score:

  S_agg(i, j) = mean( rank_S1(i,j), rank_S2(i,j), rank_S3(i,j) )

where rank_Sk(i, j) is the rank of that pair's Sk value among all
C(114, 2) = 6,441 pairs (higher rank = higher similarity; ties
averaged). Rank-averaging prevents any one axis from dominating
due to scale.

Length-residualization note (MW-1): S1 (root-Jaccard on sets) and
S2 (Dice coefficient) are inherently length-normalized; S3 is
count-based but is already constrained by the fixed top-50 budget.
No additional length-residualization is applied in primary test. As
a robustness follow-up (not a primary cell), we will report the
Spearman correlation between S_agg and verse-count-product |v_i|·|v_j|.

## Locked test statistic (Cell B)

**T = mean of S_agg over all C(10, 2) = 45 pairs with both surahs in
{16, 17, 18, 19, 20, 21, 22, 23, 24, 25}.**

## Locked null (Cell B)

Permutation null over 10-surah contiguous windows. For each of 10,000
permutations with seed 20260417:

1. Draw a start position a uniformly from {1, 2, ..., 105}
   (so the 10-surah window {a, a+1, ..., a+9} fits in Q 1-114).
2. Compute T_null = mean of S_agg over all 45 pairs inside window.
3. Collect {T_null}.

Empirical p (one-sided upper) = (1 + |{T_null ≥ T_observed}|) / (1 + N_perm).

**DIRECTION PRE-COMMITTED**: Q 16-25 internal similarity HIGHER than
random 10-surah windows (one-sided upper).

## Bonferroni declaration (family = [[h-new-94-q16-q25-zone|h-new-94]]-cluster-empty-zone)

- `bonferroni_k: 2` (Cell A + Cell B)
- `alpha_bon: 0.025` (= 0.05 / 2)
- Cell A is DESCRIPTIVE reconciliation; Cell B is PRIMARY inferential.
- Even though Cell A is descriptive, we declare k=2 as a conservative
  family to match PRE-REG-STANDARD-04. Cell B must clear α_bon = 0.025.

## MW-5 positive control (mandatory)

The null is internally sound only if, applied to a window where a
shadow cluster is KNOWN to exist, the test fires positive. Positive
control: **the musabbiḥāt stretch Q 57-64**. Though non-contiguous
in a literal sense (Q 58, 60, 63 are NOT musabbiḥāt), the 8-surah
window Q 57-64 contains 5 of 5 musabbiḥāt. Under [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] this
is a confirmed-content-cluster at p=0.0001.

**MW-5 expectation**: compute the same test statistic for the
Q 57-64 window (8-surah window) against the same null (8-surah
contiguous windows). If positive-control fails (p > 0.05), the
instrument is broken and Cell B result is NULL-BROKEN regardless
of Q 16-25's outcome.

Additional MW-5 window: **Q 40-46** (the 7 ḥawāmīm). Same reasoning.

## Garden-of-forking-paths log (disclosed BEFORE running)

1. **Prior exposure to [[h-new-89-meta-cluster-network|H-NEW-89]] result.** The pre-reg author has
   already seen [[h-new-89-meta-cluster-network|H-NEW-89]]'s isolate list (including the 8/10 Q 16-25
   count). This is the post-hoc origin of the zone choice. Cell B is
   designed AS A FORMAL TEST of a pattern that was eye-ball-noticed
   in [[h-new-89-meta-cluster-network|H-NEW-89]]'s isolate zone. Under the post-hoc-noticed-findings
   protocol (discipline §post-hoc), direction is locked HERE before
   running Cell B, and a single-test α=0.05 cap would apply; we
   apply the TIGHTER Bonferroni α=0.025 because of the 2-cell family.

2. **Contiguous window null (not random 10-surah subsets).**
   Because the zone of interest is a CONTIGUOUS 10-surah stretch,
   the null must sample CONTIGUOUS 10-surah windows, not arbitrary
   10-surah subsets. Otherwise the null would measure within-window
   mushaf-proximity effects. This matches the "zone" framing of the
   hypothesis.

3. **Three similarity axes aggregated by rank-mean.**
   Single-axis tests are possible but lose power if the signal is
   distributed across axes. Rank-mean is the classical robust
   aggregation that doesn't privilege one axis's scale. Axes were
   chosen before running: S1 and S2 are the two axes named in the
   task specification; S3 (verse-twin-count) is added because
   [[h-new-66-verse-twins-network|H-NEW-66]] is explicitly called out in the task data list.

4. **Root-Jaccard via the morphology 0.4 root-index** (not a
   hand-coded stemmer). This is the project's canonical root source.

5. **Q 16-25 is the literal inclusive window** (surahs 16, 17, ...,
   25 = 10 surahs). Not Q 16-24 or Q 17-25. Matches [[h-new-89-meta-cluster-network|H-NEW-89]]'s
   explicit count.

6. **We do NOT "drop" Q 19 or Q 20** from the window. The goal is
   to ask about the ZONE, not about "the remaining 8 isolates".
   All 10 surahs participate in the primary test.

7. **Singleton-muqaṭṭāʿat rule choice (Cell A).**
   Under [[h-new-89-meta-cluster-network|H-NEW-89]]'s ≥2-member cluster rule, Q 19 (كهيعص) and Q 20
   (طه) belong to no multi-member muqaṭṭāʿat cluster and are
   therefore correctly counted as isolates. An ALTERNATIVE ruleset
   that counts singletons as self-clusters would demote them from
   isolate status. We report BOTH readings in Cell A and do NOT
   alter the [[h-new-89-meta-cluster-network|H-NEW-89]] verdict.

8. **Window-count correction.** Under Cell A, we recompute the
   isolate count under [[h-new-89-meta-cluster-network|H-NEW-89]]'s exact ruleset, not under any
   alternative. The ruleset is the one specified in the [[h-new-89-meta-cluster-network|H-NEW-89]]
   pre-reg and hardcoded in `scripts/h_new_89_meta_cluster_network.py`.

## Anti-HARK pre-commitments

- Both cells reported regardless of significance.
- Cell A: exact isolate list + count reported.
- Cell B: observed T, null mean/median, p one-sided upper, and
  rank-within-null (e.g., "observed T ranks at percentile X").
- MW-5 positive-control: if either Q 57-64 or Q 40-46 fires p > 0.05,
  Cell B declared NULL-BROKEN.
- If Cell B PASS: exploratory SUB-structure within Q 16-25 (highest
  pairwise similarities among the 45 pairs) reported separately as
  POST-HOC descriptive.

## Expected outcomes (pre-specified, not results)

- **Cell A likely outcome**: isolate count is correct as-reported.
  Q 19 and Q 20 are singletons and the [[h-new-89-meta-cluster-network|H-NEW-89]] count stands at 21.
- **Cell B priors**: uncertain. The zone is IDENTIFIED as
  cluster-empty, but that does not mean it's content-UNIFORM.
  Q 19 (Maryam), Q 20 (Ṭā-Hā), Q 21 (al-Anbiyāʾ), and Q 26 narrative
  surahs share prophet-narrative content; Q 22 is legal (Medinan
  outlier). Q 24 is legal + light-verse. Q 16 al-Naḥl has the
  "honey-bee" natural-theology content.
  Prior-prob of PASS at α=0.025 is moderate: prophet-narrative
  concentration could lift internal similarity above random windows,
  but the Meccan-vs-Medinan mix (Q 22 is Medinan) and the
  legal-vs-narrative mix could dilute it.

## Files to produce

1. Pre-reg: `findings/phase-b-hypotheses/h-new-94-q16-q25-zone-prereg.md` (this file)
2. Script: `scripts/h_new_94_q16_q25_zone.py`
3. JSON: `findings/phase-b-hypotheses/csv/h-new-94.json`
4. Findings: `findings/phase-b-hypotheses/h-new-94-q16-q25-zone.md`
5. Journal: `journal/h-new-94-run-1.md`

## Status
PRE-REGISTERED 2026-04-17 BEFORE script execution.
