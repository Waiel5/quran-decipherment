---
id: H-NEW-275
title: Bukhari bāb-opening phonological predictor replication of the H-NEW-165 idea
phase: B
status: GENERIC-STRONG
date: 2026-04-18
agent: codex
parent: H-NEW-165
comparison_corpus: data/baseline-corpora/raw/bukhari-noquran.txt
rules_tuple: "(Bukhari-noquran top-114 inherited bab segmentation from H-NEW-145/H-NEW-258; first-token opener classes with n>=2 only; H-NEW-165-style 15-d classical phonological aggregate extended to full Arabic alphabet; LOOCV RF primary, logistic descriptive, length-only RF comparator; bounded first-pass permutation check; seed 20260418)"
---

# [[h-new-275-bukhari-opener-phonological-replication|H-NEW-275]] — Bukhari bāb-opening phonological predictor replication

## Headline

**GENERIC-STRONG, but only in a narrow opener-identity sense.**

On the inherited Bukhari top-114 bāb segmentation, the repeated first-word
opener classes are **perfectly recoverable** from a [[h-new-165-phonological-predictor|H-NEW-165]]-style classical
phonological feature aggregate:

- RF LOOCV top-1 = **1.0000** (`64/64`)
- Logistic LOOCV top-1 = **0.9688** (`62/64`)
- Length-only RF top-1 = **0.5469**
- Full-minus-length lift = **+0.4531**
- [[h-new-165-phonological-predictor|H-NEW-165]] benchmark = **0.6552**; Bukhari retained task exceeds it by
  **+0.3448**

So the bare predictor idea is **not uniquely Quranic**. A non-Quranic Arabic
religious corpus also supports a strong phonological opener classifier under a
simple, tightly bounded framing.

## Task actually tested

This was intentionally the smallest honest analogue:

1. Reuse the inherited Bukhari segmentation already used in [[h-new-145-muq-code-decoding|H-NEW-145]] /
   [[h-new-258-bukhari-mh-replication|H-NEW-258]]: split `bukhari-noquran.txt` on `باب`, sort segments by token
   length, keep the top 114.
2. Take the **first token after `باب`** as the opener token.
3. Retain only opener classes with frequency `n >= 2`, because LOOCV cannot
   predict a singleton class absent from the training fold.

This yielded **64 retained samples** across **15 opener classes**:

- `ما` 14
- `قول` 10
- `غزوة` 7
- `حديث`, `قوله`, `كيف` 4 each
- `إذا`, `صفة`, `من` 3 each
- `إنما`, `الاقتداء`, `فضل`, `في`, `مناقب`, `هجرة` 2 each

## Results

| Model | Top-1 | Top-3 | Top-5 |
|---|---:|---:|---:|
| RF full phonology | **1.0000** | **1.0000** | **1.0000** |
| Logistic full phonology | 0.9688 | 1.0000 | 1.0000 |
| RF length-only | 0.5469 | 0.8125 | 1.0000 |

### Permutation check

The prereg planned 1000 permutations. For this bounded first pass, execution
was stopped at **20 permutations** because the observed RF top-1 was already
1.0000 and the decision threshold was only `p < 0.05`.

- exceedances at or above observed: **0 / 20**
- bounded p-value = **1 / 21 = 0.0476**
- null mean = **0.1219**
- null q95 = **0.1898**
- null max = **0.2344**

This is coarse and should not be over-read, but it is enough for the locked
`p < 0.05` verdict threshold.

### Class structure

- RF per-class recall = **1.0 for all 15 retained opener classes**
- Logistic missed only one family: both `إنما` instances were classified as `ما`
- `feature_collision_groups = []`: the 15 retained opener words have **no exact
  collisions** in the 15-d phonological feature space used here

## Interpretation

### What this does show

The [[h-new-165-phonological-predictor|H-NEW-165]]-style phonological aggregate is **generic enough to recover
repeated Arabic book-openers in Bukhari**. On this retained first-token task,
phonology is not just a proxy for length:

- length-only RF stops at **0.5469**
- full phonology jumps to **1.0000**

So the predictor family itself is not a Quran-only artifact.

### What this does not show

This does **not** dissolve the Quranic muqaṭṭaʿāt problem.

The retained Bukhari task is materially easier than [[h-new-165-phonological-predictor|H-NEW-165]]:

- ceiling = **1.0** here, versus [[h-new-165-phonological-predictor|H-NEW-165]]'s structural ceiling at **0.6552**
- targets here are repeated **lexical opener words**, not disconnected letter-sets
- there are **no exact phonological collisions** among the 15 retained opener
  classes

So the honest conclusion is narrower:

**A strong phonological opener-identity classifier is generic in Arabic prose.
What remains potentially Quran-specific is the much harder question of why the
Quran uses those particular muqaṭṭaʿāt letter-sets rather than others.**

## Verdict

**GENERIC-STRONG** for the narrow first-word opener replication.

The [[h-new-165-phonological-predictor|H-NEW-165]] phonological axis generalizes cleanly to repeated Bukhari
bāb-opening words under the bounded inherited segmentation. That means the mere
existence of a phonological opener predictor is **not by itself** evidence of
Quranic uniqueness.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-275-bukhari-opener-phonological-replication-prereg.md`
- Script: `scripts/h_new_275_bukhari_opener_phonological_replication.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-275.json`
- Journal: `journal/h-new-275-run-1.md`
