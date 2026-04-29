---
id: H-NEW-264
title: Q 1 "connects everything" follow-up — ḥā-mīm subset root-profile test
phase: B
status: CONFIRMED — Q 1's root profile is anomalously concentrated in Q 40-46 under a matched null
date: 2026-04-18
specialist: specialist-B (quran-equation-solvers)
parent_findings: [h-new-89, h-new-155, h-new-193, h-new-137, h-new-138]
seed: 20260420
rules_tuple: "(QAC v0.4 STEM roots via surah-root-graph.json; target subset fixed as Q40-46 ḥm muqaṭṭāʿat; null preserves exact period composition and coarse verse-count bins <10/10-29/30-59/60-99/100+; Hafs-Kūfan; basmala-counted-only-in-surah-1)"
bonferroni: k=2 α_bon=0.025 family=h-new-264-q1-connects-everything
pre_reg: findings/phase-b-hypotheses/h-new-264-q1-connects-everything-prereg.md
prereg_sha256: 8a29c8088271b6bbeb39f561e8083e3d4504219c377d0b82e4a031f287c96497
script: scripts/h_new_264_q1_connects_everything.py
output_json: findings/phase-b-hypotheses/csv/h-new-264.json
verdict: CONFIRMED — Q 1 shares 73.8% of its 18 roots with the average ḥā-mīm surah, versus a matched-null mean of 54.6% (z=+3.16, p=0.0001). The stricter IDF-weighted recall also passes (50.5% vs 35.4%, z=+3.13, p=0.0005). MW-5 positive control Q 62→musabbiḥāt passes on both cells.
---

# [[h-new-264-q1-connects-everything|H-NEW-264]] — Q 1 root-profile linkage to Q 40-46

## Headline

This bounded "Q 1 connects everything" follow-up **confirms a specific
subset-level connection**:

**Q 1 al-Fātiḥa's QAC-STEM root profile is anomalously concentrated in
the ḥā-mīm block Q 40-46**, even after the null is forced to match the
subset's Meccan-only composition and its coarse verse-count profile.

This does **not** establish that Q 1 connects to every subset or that
the ḥā-mīm block is uniquely maximal. It establishes one tighter claim:

**despite being structurally isolated in [[h-new-89-meta-cluster-network|H-NEW-89]]'s membership taxonomy,
Q 1 is root-profile-linked to the classical ḥā-mīm subset on a
non-membership axis.**

## Locked results

| Cell | Statistic | Observed | Matched-null mean | z | p | Verdict |
|---|---|---:|---:|---:|---:|:--:|
| A | mean unweighted Q 1-root recall across Q 40-46 | **0.7381** | 0.5463 | **+3.16** | **0.0001** | **PASS** |
| B | mean IDF-weighted Q 1-root recall across Q 40-46 | **0.5049** | 0.3543 | **+3.13** | **0.0005** | **PASS** |

Bonferroni family: `k=2`, `α_bon=0.025`. Both cells pass comfortably.

## What the effect means in raw root terms

Q 1 has **18 distinct STEM roots**. The average ḥā-mīm surah contains
**13.29** of those 18 roots.

Per-surah shared-root counts:

| Surah | Shared Q 1 roots | Recall |
|---|---:|---:|
| Q 40 | 15 | 0.8333 |
| Q 41 | 14 | 0.7778 |
| Q 42 | **17** | **0.9444** |
| Q 43 | 14 | 0.7778 |
| Q 44 | 9 | 0.5000 |
| Q 45 | 11 | 0.6111 |
| Q 46 | 13 | 0.7222 |

Roots present in **all 7** ḥā-mīm surahs:
- `Alh`
- `Elm`
- `qwm`
- `rHm`
- `rbb`
- `smw`
- `ywm`

Additional roots present in **6 of 7**:
- `Dll`
- `Ebd`
- `hdy`
- `mlk`
- `nEm`

The stricter IDF-weighted cell matters because it downweights the most
ubiquitous roots. That weighted cell still passes at p=0.0005, so the
signal is not reducible to `Alh` / `rbb` / `rHm` alone.

## Why this matters for the Q 1 tension

The earlier Q 1 picture was split:

1. **[[h-new-89-meta-cluster-network|H-NEW-89]]**: Q 1 is structurally isolated in the classical
   cluster-membership network.
2. **[[h-new-155-q1-sui-generis|H-NEW-155]]**: Q 1's root vocabulary is unusually dispersed across
   the corpus.
3. **[[h-new-193-q1-attractors|H-NEW-193]]**: the verse-level "Q 1 touches many surahs" palette
   claim failed under phrase-neighboring.

[[h-new-264-q1-connects-everything|H-NEW-264]] refines that tension in a bounded way:

- the all-purpose phrase-level attractor claim still fails,
- but a **specific root-profile linkage** to Q 40-46 survives a
  conservative matched null.

So the honest update is not "Q 1 connects everything." It is:

**Q 1 is structurally isolated at the membership level, widely
dispersed at the corpus level, and specifically over-connected to the
ḥā-mīm block at the root-profile level.**

## MW-5 positive control

The same machinery was run on a known cluster-linked case:

- anchor: **Q 62**
- target subset: **{57, 59, 61, 64}** musabbiḥāt inner-5 excluding the anchor

| MW-5 cell | Observed | Null mean | z | p |
|---|---:|---:|---:|---:|
| unweighted recall | 0.4704 | 0.3968 | +2.81 | 0.0001 |
| IDF-weighted recall | 0.3098 | 0.2433 | +3.45 | 0.0001 |

**MW-5 PASS.** The instrument recovers a known within-cluster linkage,
so the Q 1 → ḥā-mīm result is not a dead-pipeline artifact.

## Interpretation

The result supports a **specific, not universal** connectivity claim.
Among pre-locked classical subsets, Q 40-46 provides one concrete place
where Q 1's small root palette reappears at anomalously high rates.

This is consistent with the ḥā-mīm block functioning as a dense
theological-discursive region that repeatedly reuses Q 1's core roots
of lordship, mercy, knowledge, guidance, accountability, and opposition.

The finding is deliberately modest:
- it does not claim exclusivity of the ḥā-mīm block,
- it does not rank all subsets,
- it does not rescue the [[h-new-193-q1-attractors|H-NEW-193]] phrase-level null,
- it does not replace the already-confirmed terminal-triad closure
  result of [[h-new-137-wrap-around-closure|H-NEW-137]] / [[h-new-138-wrap-around-feature-robustness|H-NEW-138]].

## Honest limits

1. **One subset only.** We did not scan all classical clusters or all
   contiguous blocks. This is a confirmatory test of one locked subset,
   not a ranking of all possibilities.

2. **Root presence/absence only.** The cells ignore within-surah token
   frequencies except through the IDF penalty. A fuller distributional
   metric could change the magnitude.

3. **Coarse length matching.** The null matches only broad verse-count
   bins, not exact root-count, exact verse-count, or chronology-phase.
   The match is conservative, but not maximal.

4. **Shared substrate across cells.** The two Bonferroni-counted cells
   are correlated because they operate on the same subset and root set.
   The family correction is therefore conservative rather than
   independence-exact.

5. **No uniqueness claim.** A different pre-locked subset might also
   pass. This finding should not be read as "ḥā-mīm is the only place
   Q 1 connects."

## Bottom line

**CONFIRMED.** Under a period- and length-matched null, the classical
ḥā-mīm subset Q 40-46 contains substantially more of Q 1's root profile
than expected by chance. This is a clean, bounded, non-vague answer to
the "Q 1 connects everything" prompt: not everything, but yes, one
specific classical subset does show anomalous linkage.
