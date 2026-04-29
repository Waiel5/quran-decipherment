---
id: H-NEW-96.2
title: Rhyme-feature predictor for muqaṭṭaʿāt letter-set identity (OQ-1 phonological attack)
phase: B
status: PRE-REGISTERED (locked)
date: 2026-04-17
agent: h96-wrapper
parent: H-NEW-88 (RF LOOCV top-1 = 0.414, baseline)
parent_predictor_null: H-NEW-96 (92-feature content extension NULL; 0.379 < 0.414)
data_anchor: H-NEW-139 (muq → fāṣila rhyme correlation PASS-DIRECTED, z = +5.96)
open_question: OQ-1 (why does each muqaṭṭaʿāt surah get its specific letter-set?)
seed: 20260417
bonferroni_k: 2
bonferroni_family: h-new-96-2-rhyme-predictor
alpha_bon: 0.025
direction_primary: "top-1 LOOCV > 0.414 (strictly > H-NEW-88 baseline, per team-lead T-R spec)"
direction_secondary: "≥1 of 8 singletons correctly predicted"
acceptance_window: "permutation p < 0.025 for primary AND observed top-1 > 0.414"
rules_tuple: "(no-tashkeel; canonical 14 distinct letter-sets; hafs-kufan; locked 14-feature rhyme-one-hot matrix; LOOCV on 29 surahs; RF primary, logistic secondary; seed 20260417)"
---

# H-NEW-96.2 — Rhyme-feature predictor for muqaṭṭaʿāt letter-set identity

## Classical / project anchor

- **Parent NULL**: [[h-new-96-predictor-extension|H-NEW-96]] extended [[h-new-88-letter-set-predictor|H-NEW-88]]'s 18 content-features to 92 features, verdict NULL (RF top-1 = 0.379 < 0.414). Content features are exhausted.
- **Parent PASS-DIRECTED**: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] showed muq-opening-letters ∩ top-3-fāṣila-letters overlap at z = +5.96, p < 10⁻⁴. The muq letters predict the rhyme scheme.
- **This hypothesis**: invert [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]. Use the rhyme (top-3 verse-final letters per surah) as a PREDICTOR of letter-set identity. If OQ-1 has a phonological rather than semantic answer, rhyme features should outperform content features.

## Hypothesis (pre-registered)

**H1 (primary)**: Rhyme-feature matrix (14-dim one-hot, one feature per muq letter indicating whether that letter is in the top-3 fāṣila of the surah) predicts letter-set identity at RF LOOCV top-1 > 0.414 (strictly better than [[h-new-88-letter-set-predictor|H-NEW-88]]'s content-feature baseline). This would be the FIRST positive OQ-1 signal suggesting letter-set identity is phonologically rather than semantically determined.

**H2 (secondary)**: With rhyme-specific features, at least 1 of the 8 singleton letter-sets (ص, ق, ن, طه, يس, طس, كهيعص, حمعسق) will be correctly predicted in LOOCV.

## Feature space (LOCKED before model training)

14 features, one per muqaṭṭaʿāt letter. For each surah s ∈ 29 muq-opened surahs, and each letter L ∈ {ا, ل, م, ر, ص, ك, ه, ي, ع, ط, س, ح, ن, ق}:

  `rhyme_contains_L(s) = 1 if L ∈ top-3 most-frequent verse-final letters of s (excluding v1) else 0`

**Feature matrix**: 29 × 14 (one-hot per letter).

### Top-3 rhyme extraction (deterministic, matches [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]])

For each surah:
1. For each verse v ∈ surah (v ≥ 2 for muq-opened surahs, to skip v1 muqaṭṭaʿāt-token):
2. Extract final CHARACTER of the verse text after whitespace-strip, after tashkeel-strip (already no-tashkeel in source).
3. Count frequencies of all final-letters; take top-3.
4. Set `rhyme_contains_L = 1` for each of those top-3 letters if L ∈ muq-letter vocab; else 0.

**[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] reproduces with seed 20260417; this script uses the same extraction rule and will be sanity-checked against the [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] per-surah table before model training.**

## Procedure (locked)

1. Build 29 × 14 design matrix X (rhyme one-hot), label vector y (14 muq letter-set classes).
2. LOOCV with RandomForestClassifier(n_estimators=200, random_state=20260417) as PRIMARY.
3. LOOCV with LogisticRegression(C=1.0, L2, lbfgs, max_iter=2000) as SECONDARY.
4. Compute top-1, top-3, top-5 accuracy.
5. Per-class recall (14 entries); per-singleton accuracy (8 entries).
6. Permutation null: shuffle y 1000×, redo LOOCV; compute top-1 distribution.
7. **MW-5 positive control**: cheat_surah_id alone → expected LOOCV top-1 = 1.0 on unique-id (same as [[h-new-96-predictor-extension|H-NEW-96]]).
8. **[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] sanity check**: verify per-surah top-3 rhyme table matches [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s published table (29 surahs).
9. Report all metrics BEFORE interpretation.

## Verdict decision rule (locked)

Per team-lead T-R spec:
- **PASS**: RF LOOCV top-1 > 0.414 AND permutation p < 0.025 → letter-set is partially predictable from rhyme features (positive OQ-1 phonological signal)
- **PASS-STRONG**: top-1 > 0.50 AND perm p < 0.025 → strong phonological signal
- **OQ-1-PROGRESS**: ≥1 singleton correctly predicted → first positive singleton hit
- **JOINT-PASS**: PASS-STRONG AND OQ-1-PROGRESS
- **NULL**: top-1 ≤ 0.414 OR perm p ≥ 0.025 — phonological features don't beat content-feature baseline

MW-5 positive control MUST pass (top-1 ≥ 0.50 on cheat id) for any other verdict to stand. (Note: LOOCV structural ceiling on cheat_surah_id from [[h-new-96-predictor-extension|H-NEW-96]] was 0.517, not 1.0, because duplicate/near-duplicate ids don't exist — the ceiling is bounded by structural LOOCV itself.)

## Bonferroni correction

- `bonferroni_k = 2` (primary top-1 threshold + secondary singleton-hit)
- `alpha_bon = 0.025`
- `bonferroni_family = h-new-96-2-rhyme-predictor`

## Garden-of-forking-paths log

1. **Feature definition pre-committed**: 14 one-hot rhyme-letter features, one per muq-alphabet letter. No post-hoc expansion to ALL-28-letter alphabet.
2. **Top-3 rhyme cutoff**: matches [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] exactly; NOT re-tuned. Top-5 or top-1 variants NOT tested as primary (queue as H-NEW-96.2a if needed).
3. **Primary classifier is RF** (matches [[h-new-88-letter-set-predictor|H-NEW-88]] / [[h-new-96-predictor-extension|H-NEW-96]] parent for direct comparability).
4. **Seed 20260417** (same as [[h-new-96-predictor-extension|H-NEW-96]], consistent within this session's handoff).
5. **Circularity caveat**: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] showed muq-opening ∩ rhyme overlap; using rhyme to predict letter-set risks weak self-reference. Mitigation: we use the FULL 14-letter rhyme one-hot vector, not just the overlap indicator. LOOCV holds the target surah out, so the model must generalize rhyme-pattern → letter-set mapping from other surahs.
6. **Singleton-LOOCV ceiling is still 0.655** (8 singletons cannot vote their own class in LOOCV). Reader calibration note carries over from [[h-new-96-predictor-extension|H-NEW-96]] pre-reg (audit-036 noted this).
7. **Permutation null**: 1000 shuffles, seed 20260417.
8. **Singleton secondary test**: chosen because singleton-prediction is the substantive OQ-1 question, same as parent pre-reg.
9. **No feature selection post-hoc**. The 14 features are fixed.
10. **No per-fold rhyme recomputation**: the rhyme top-3 is computed ONCE per surah from the full surah text; for the held-out surah the rhyme is computed from the full held-out surah (this is leakage-free because rhyme is a SURAH-INTRINSIC signal derived from the surah's own verses, NOT from other surahs' labels).

## Expected outcome (pre-committed)

Given that:
- [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] showed muq-letters ∩ top-3-rhyme overlap at z=+5.96 (21/29 match ≥1 letter)
- The top-3 rhyme set is typically size 2-3, so each surah's 14-dim rhyme vector has 2-3 ones
- Within the 29-surah training set, rhyme patterns DO cluster (per [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]): ALM surahs mostly rhyme on ن/م/ر; HM surahs mostly rhyme on ن/م/ر; ALR surahs on ن/م/ل; the singletons (Q 19, 20) are long-vowel ى/ا/ي.

If rhyme structure drives letter-set, we expect:
- Good discrimination among ALM/ALR/HM clusters (they have different rhyme signatures)
- Possibly correct prediction of long-vowel-rhyme singletons (Q 19 كهيعص and Q 20 طه both have ى/ا/ي rhyme — unique signature)
- Q 68 نّ (single-letter ن, rhyme = ن/م) might hit because the rhyme contains its own letter

**Honest default expectation**: top-1 ~0.35-0.50 (comparable to or modest improvement over [[h-new-88-letter-set-predictor|H-NEW-88]] baseline 0.414). Singleton hits UNLIKELY but POSSIBLE for Q 19/20 (shared rhyme mode as singletons in different letter-sets — LOOCV may fail here too). Report full result either way.

## MW-5 positive control

Cheat_surah_id → RF LOOCV top-1 — expected 0.517 (same structural ceiling as [[h-new-96-predictor-extension|H-NEW-96]]).

If MW-5 positive control yields a value wildly different from parent's 0.517 (e.g., 0.0), pipeline is broken → report NULL-BROKEN-PIPELINE.

## Files

- Pre-reg: this file
- Script: `scripts/h_new_96_2_rhyme_predictor.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-96-2.json`
- Findings: `findings/phase-b-hypotheses/h-new-96-2-rhyme-predictor.md`
- Journal: `journal/h-new-96-2-run-1.md`

## Cross-references

- Parent baseline: [[h-new-88-letter-set-predictor|H-NEW-88]] (content features, top-1 = 0.414)
- Parent NULL: [[h-new-96-predictor-extension|H-NEW-96]] (92-feature extension, top-1 = 0.379)
- Data anchor: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] (rhyme overlap PASS-DIRECTED)
- OQ-1 (open question being probed: phonological rather than semantic answer)
- Queued after PASS/NULL: T-R.1 (combine rhyme + [[h-new-88-letter-set-predictor|H-NEW-88]] features)
