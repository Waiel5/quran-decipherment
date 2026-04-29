---
id: H-NEW-281
title: True-isolate core within-zone exact Jaccard test
phase: B
status: PASS-DIRECTED
date: 2026-04-18
agent: codex
parent_1: H-NEW-126
parent_2: H-NEW-168
open_question: OQ-18
seed: 20260418
prereg: findings/phase-b-hypotheses/h-new-281-true-isolate-core-within-zone-jaccard-prereg.md
script: scripts/h_new_281_true_isolate_core_within_zone_jaccard.py
json: findings/phase-b-hypotheses/csv/h-new-281.json
journal: journal/h-new-281-run-1.md
rules_tuple: "(QAC v0.4 root sets via surah-root-graph.json; exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25; primary statistic = mean pairwise root-set Jaccard; one-sided upper-tail)"
---

# [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] — True-isolate core within-zone exact Jaccard test

## Headline

[[h-new-126-isolate-core|H-NEW-126]] already showed that the true-isolate core
`{Q16, Q21, Q22, Q23, Q25}` shares more root vocabulary than random
5-surah sets drawn from the whole corpus, but that result carried a real
length-confound caveat because the null was global and length-unmatched.

[[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] removes that weakness in the smallest honest way:

- hold the comparison zone fixed to **Q16..Q25**
- enumerate **all** `C(10,5) = 252` five-surah subsets
- ask whether the true-isolate core is unusually cohesive **within its
  own meso-concentrator community**

The answer is positive.

- primary observed mean pairwise root-Jaccard = **`0.3413855694`**
- exact upper-tail rank = **`8 / 252`**
- exact one-sided `p = 0.0317460317`
- overall verdict = **PASS-DIRECTED**

So the true-isolate core is not just a random 5-subset inside the
Q16-25 zone. It is the **semantic nucleus** of that already-confirmed
concentrator community.

## Why this test matters

This is the cleanest bounded OQ-18 follow-up now available on disk.

- [[h-new-168-q16-q25-dispersion|H-NEW-168]] had already shown that **Q16-25 as a whole** is a real
  internally-similar concentrator zone.
- [[h-new-126-isolate-core|H-NEW-126]] had already shown that the **5-surah true-isolate core**
  shares unusually high root overlap versus a global random-5 null.
- [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] connects those two findings directly.

Instead of comparing the core to arbitrary Quran-wide 5-sets, it asks:

> inside the one zone where these surahs actually live, is the
> [[cross-finding-010-extended-network|cross-finding-010]] true-isolate core still unusually cohesive?

That is exactly the right next question for OQ-18.

## Primary exact result

Target subset:

- `Q16 al-Naḥl`
- `Q21 al-Anbiyāʾ`
- `Q22 al-Ḥajj`
- `Q23 al-Muʾminūn`
- `Q25 al-Furqān`

Primary statistic:

- mean pairwise root-set Jaccard across the 10 within-subset pairs

Exact null:

- all `252` five-surah subsets of `Q16..Q25`
- one-sided upper-tail

### Numbers

| Quantity | Value |
|---|---:|
| exact space size | `252` |
| observed mean pairwise Jaccard | `0.3413855694` |
| exact rank (descending) | `8 / 252` |
| subsets `>=` observed | `8` |
| exact upper-tail `p` | `0.0317460317` |
| null mean | `0.3189327902` |
| null median | `0.3192074801` |
| null min | `0.2942835973` |
| null max | `0.3458587132` |
| verdict | `PASS-DIRECTED` |

This is not an overwhelming separation, but it is real and exact.

The target subset sits near the very top of its own local comparison
space, not merely above a global random baseline.

## Secondary descriptive context

The shared-root-spine count was kept secondary.

- observed shared-root spine count = **`80`**
- exact rank = **`11 / 252`**
- exact upper fraction for context = **`0.06746`**

That is directionally strong but less discriminative than the primary
mean-Jaccard statistic. It is useful as context, not as the family
driver.

## Interpretation

[[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] refines OQ-18 in a concrete way.

### What now looks established

1. **The Q16-25 zone is real at the meso scale.**
   [[h-new-168-q16-q25-dispersion|H-NEW-168]] already established that.
2. **The true-isolate core is real at the local-subset scale.**
   [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] now shows the core is unusually cohesive even when judged
   only against other 5-subsets drawn from the same zone.
3. **The core is therefore the semantic nucleus of the zone, not just a
   topological artifact of the 20-cluster inventory.**

### What this does not yet solve

It does **not** yet explain the name-class question in a fully formal
way. The corpus-wide naming taxonomy on disk is not yet locked in a form
that cleanly tests the broader "concept/object-name" mechanism.

So OQ-18 is now sharper:

- the root-level nucleus is real
- the next blocker is not "is there any local cohesion?" anymore
- the next blocker is the higher-level interpretation of why these
  particular surahs form that nucleus

## Bottom line

The true-isolate core `{Q16, Q21, Q22, Q23, Q25}` is not just a strange
5-surah residue inside the Q16-25 concentrator zone.

Under the exact within-zone null, it ranks **8th of 252** on mean
pairwise root-Jaccard and passes at **`p = 0.031746`**.

That makes it the best current candidate for the **semantic nucleus** of
the Q16-25 zone.
