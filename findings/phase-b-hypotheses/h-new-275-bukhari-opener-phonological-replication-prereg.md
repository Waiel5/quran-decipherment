---
id: H-NEW-275
title: Bukhari bāb-opening phonological predictor replication of the H-NEW-165 idea
phase: B
status: PRE-REGISTERED (locked after corpus-frequency scan only)
date: 2026-04-18
agent: codex
parent: H-NEW-165
comparison_corpus: data/baseline-corpora/raw/bukhari-noquran.txt
seed: 20260418
bonferroni_k: 1
alpha_bon: 0.05
rules_tuple: "(Bukhari-noquran top-114 inherited bab segmentation from H-NEW-145/H-NEW-258; first-token opener classes with n>=2 only; H-NEW-165-style 15-d classical phonological aggregate extended to full Arabic alphabet; LOOCV RF primary, logistic descriptive, length-only RF comparator; 1000 label permutations; seed 20260418)"
prereg_scope_note: "Locked after inspecting only opener frequency counts needed to avoid LOOCV singleton impossibility. No phonological feature vectors, no classifier scores, and no permutation outputs were viewed before lock."
---

# [[h-new-275-bukhari-opener-phonological-replication|H-NEW-275]] — Bukhari bāb-opening phonological predictor replication

## Question

[[h-new-165-phonological-predictor|H-NEW-165]] showed that a classical-tajwīd phonological feature vector predicts
Quranic muqaṭṭaʿāt letter-set identity at RF LOOCV top-1 = 0.6552, exactly the
Quran task's multi-member ceiling. The open cross-corpus question is whether
that result reflects a generic Arabic opener phenomenon or something more
specifically Quranic.

This study asks a bounded analogue on a non-Quranic corpus:

**Can a [[h-new-165-phonological-predictor|H-NEW-165]]-style phonological aggregate predict repeated Bukhari bāb
first-word opener identity?**

If yes at strong levels, the basic predictor idea is at least partly generic.
If no, the Quranic result is harder to dismiss as a general Arabic heading
artifact.

## Corpus and retention rule

Use the exact inherited Bukhari segmentation already on disk in the [[h-new-145-muq-code-decoding|H-NEW-145]] /
[[h-new-258-bukhari-mh-replication|H-NEW-258]] lineage:

1. Read `data/baseline-corpora/raw/bukhari-noquran.txt`.
2. Strip Quranic-style diacritics only.
3. Split on the token `باب`.
4. Tokenize on whitespace.
5. Sort segments by token count descending.
6. Retain the top 114 segments in that inherited order.

For each retained segment, define its **opener token** as the first whitespace
token after `باب`.

LOOCV cannot predict a class absent from the training fold, so this replication
retains only opener-token classes with frequency `n >= 2` in the inherited
top-114 corpus. The frequency scan needed for that retention rule was viewed
before lock; nothing downstream was viewed.

## Feature family — [[h-new-165-phonological-predictor|H-NEW-165]]-style, extended to full Arabic alphabet

Each opener token is converted to a 15-dim phonological aggregate:

Per-letter classical features:

- `makhraj` ordinal in the [[h-new-165-phonological-predictor|H-NEW-165]] 8-tier backness scheme
- `voice`
- `manner`
- `emphatic`
- `pharyngeal`
- `sonorant`
- `continuant`
- `idhlaq`
- `vowel_carrier`

Aggregate features:

- `letter_count`
- `frac_emphatic`
- `frac_pharyngeal`
- `frac_sonorant`
- `frac_idhlaq`
- `has_qalqala`

The category logic inherits [[h-new-165-phonological-predictor|H-NEW-165]]'s classical-tajwīd feature family. Since
Bukhari opener words use the full Arabic alphabet rather than only the 14 muq
letters, the letter table is extended to the full alphabet using the same
classical categories:

- hams letters = `فحثهشخصسكت` => `voice = 0`; all others `voice = 1`
- emphatic letters = `{خ, ص, ض, ط, ظ, غ, ق}`
- pharyngealized / guttural family = `{خ, ص, ض, ط, ظ, غ, ق, ع, ح}`
- sonorants = `{ا, ل, م, ر, ي, ن, و}`
- stops = `{ك, ط, ق, ب, د, ت, ء, ج}`
- idhlāq = `{ف, ر, م, ن, ل, ب}`
- vowel carriers = `{ا, و, ي}`

Normalization before coding:

- `أإآٱ` -> `ا`
- `ىئ` -> `ي`
- `ؤ` -> `و`
- `ة` -> `ه`

No other stemming or lexical normalization is allowed.

## Models

Primary:

- RandomForestClassifier with `n_estimators = 200`, `random_state = 20260418`
- LOOCV top-1, top-3, top-5
- 1000 label permutations on the RF top-1 metric

Descriptive secondary:

- LogisticRegression with `C = 1.0`, `penalty = l2`, `solver = lbfgs`,
  `max_iter = 2000`

Comparator baseline:

- RF LOOCV using `letter_count` alone

Feature standardization is done inside each LOOCV fold using the training fold
mean and standard deviation, exactly as in [[h-new-165-phonological-predictor|H-NEW-165]].

## Primary inferential test

One locked inferential test:

- **H1**: RF full-phonology LOOCV top-1 exceeds the [[h-new-165-phonological-predictor|H-NEW-165]] absolute benchmark
  `0.6552` and has permutation `p < 0.05`.

Rationale: on this retained Bukhari task all classes repeat, so the structural
ceiling is 1.0. Failing to clear the Quran's absolute 0.6552 benchmark on an
easier ceiling would count against genericity.

## Descriptive comparator

`letter_count` is not inferentially tested, but the full phonological model must
beat the length-only RF baseline by a noticeable margin to count as a genuine
phonology replication rather than a word-length artifact.

Locked descriptive lift threshold:

- `delta_top1 = top1_full - top1_length_only`
- interpret `delta_top1 >= 0.10` as a meaningful phonological lift

## Verdict rule

- `GENERIC-STRONG`: RF full top-1 > 0.6552, permutation `p < 0.05`, and
  `delta_top1 >= 0.10`
- `GENERIC-WEAK`: RF full top-1 significant at `p < 0.05` but either does not
  clear 0.6552 or does not clear the `+0.10` length-only lift threshold
- `QURAN-SPECIFIC / NO STRONG GENERIC REPLICATION`: RF full permutation
  `p >= 0.05` or RF full top-1 <= length-only top-1

## Garden-of-forking-paths disclosure

1. Only the opener-frequency scan was viewed before lock; no model outputs were.
2. The retained task is **first-token opener identity**, not topic prediction.
   This is intentionally narrow and only addresses whether the phonological
   predictor idea itself generalizes.
3. The inherited top-114 segmentation is reused verbatim for comparability with
   earlier Bukhari work; no alternate Bukhari segmenter is allowed in this run.
4. The class-retention rule `n >= 2` is structural, not tuned.
5. The primary comparison benchmark is [[h-new-165-phonological-predictor|H-NEW-165]]'s absolute top-1 = 0.6552.
   That benchmark is intentionally conservative because the Bukhari retained
   task has ceiling 1.0.
6. The length-only model is descriptive, not a second inferential family.

## Files

- Pre-reg: this file
- Script: `scripts/h_new_275_bukhari_opener_phonological_replication.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-275.json`
- Findings: `findings/phase-b-hypotheses/h-new-275-bukhari-opener-phonological-replication.md`
- Journal: `journal/h-new-275-run-1.md`
