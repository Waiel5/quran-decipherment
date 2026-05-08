---
finding_id: Q025-F-01
title: True-isolate persistence of Q 25 across 8 alternative similarity instruments
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q025-al-furqan-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q025-F-01-true-isolate-instruments
bonferroni_k: 8
alpha_bon: 0.00625
direction: one-sided LOWER on "mean similarity to nearest 3 surahs" (i.e., Q 25 is LOW = isolated)
success_criterion: ≥6 of 8 instruments place Q 25 in the bottom-quartile (rank ≤ 28/114) of mean-top-3-neighbor similarity. STRICT: 6/8 with all individual permutation p ≤ α_bon = 0.00625.
failure_criterion: <4/8 instruments place Q 25 in bottom-quartile.
rules_tuple: "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
script: surahs/Q025-al-furqan/scripts/Q025_F_01_true_isolate_persistence.py
output_json: surahs/Q025-al-furqan/csv/Q025-F-01.json
parent_oq: OQ-2 (Q 16-25 cluster-empty zone)
parent_finding: H-NEW-126 (true-isolate core {Q 16, 21, 22, 23, 25})
---

# Q025-F-01 — True-isolate persistence (pre-reg)

## Hypothesis

H-NEW-126 identified Q 25 as a member of the 5-surah true-isolate core {Q 16, 21, 22, 23, 25} — surahs invisible to all 20 cluster-taxonomy systems mapped in cross-finding-010. The natural follow-up is to ask whether Q 25's isolate-ness is **instrument-fragile** (an artifact of which similarity metric was used) or **instrument-robust** (a fundamental feature of Q 25's relationship to the rest of the corpus, independent of which similarity tool you pick up).

**Pre-committed direction**: under each of 8 alternative similarity instruments (defined below), Q 25's mean similarity to its 3 nearest non-self neighbors places Q 25 in the bottom-quartile (rank ≤ 28/114) of the corpus.

## Why this question is the right next step on OQ-2

OQ-2 status (HANDOFF/05-OPEN-QUESTIONS.md) is "ANSWERED via H-NEW-168 concentrator-mode" for the **Q 16-25 zone as a whole**, but the per-surah question — *is Q 25 specifically still an isolate after we change instruments?* — has not been bounded. Q025-F-01 closes that.

Q021, Q022, Q016, Q023 have parallel specialists running. The corpus-wide isolate-persistence test for Q 25 is non-overlapping with those per-surah deep-dives.

## The 8 instruments

For each instrument, build a 114×114 surah-similarity matrix (or its equivalent), then for each surah s compute `mean_top3_sim(s)` = mean similarity to its 3 most-similar non-self surahs. Lower values = more isolated.

1. **I1 — root-Jaccard** (QAC v0.4 stems): Jaccard of unique-root sets per surah.
2. **I2 — content-cosine** (no-tashkeel orthographic tokens, IDF-weighted): standard TF-IDF cosine.
3. **I3 — char-trigram-Dice**: Dice coefficient on character 3-gram sets (no-tashkeel concatenated surah text).
4. **I4 — Fisher-Rao distance** on QAC-root probability vectors (from h-new-111). SIMILARITY = `1 / (1 + d_FR)`.
5. **I5 — rhyme final-letter cosine**: per-surah final-letter (last graphemic letter of each verse) probability vector, cosine similarity.
6. **I6 — root Zipf-overlap**: weight each shared root by `1 / log(1 + corpus_freq)` (rare-roots count more), Jaccard-style normalization.
7. **I7 — divine-name overlap**: per-surah count vector over the 99 names of Allah (data/asma-al-husna.txt), Jaccard on attested-name sets.
8. **I8 — character-5-gram NCD-proxy**: 1 − Dice of character 5-gram sets (no-tashkeel).

For each instrument, compute Q 25's `mean_top3_sim` rank, and a permutation null on the rank under random-relabeling of the 114 surah identities.

## Bonferroni accounting

k = 8 instruments. α_bon = 0.05 / 8 = 0.00625.

## Acceptance / failure window

- ≥6/8 instruments place Q 25 in bottom-quartile (rank ≤ 28) AND each passes per-instrument permutation null at α_bon ⇒ **CONFIRMED isolate-persistence** (PASS-DIRECTED ceiling under post-hoc cap; CONFIRMED if independent replication).
- 4-5/8 ⇒ **DIRECTIONAL** (pattern present but not sweep).
- <4/8 ⇒ **NULL / RULES-TUPLE-FRAGILE** (isolate verdict was instrument-specific).

## Direction is locked LOW

Pre-committed direction: Q 25 has LOW `mean_top3_sim` (= is isolated). Reverse direction (Q 25 in TOP quartile of similarity) is a pre-commit violation per PRE-REG-STANDARD-01 and would be published with full prominence as NULL.

## MW protections

- MW-1 (instrument-prior): all 8 instruments specified ABOVE pre-reg lock.
- MW-2 (corpus-prior): per-instrument 10000-permutation null on the rank-statistic.
- MW-3 (alternative-models): test family inherently spans 8 distinct mathematical instruments.
- MW-5 (positive-control): MW-5 test = within the same null framework, the ḥawāmīm cluster {Q 40-44} should NOT be in the bottom-quartile of `mean_top3_sim` for I1 (root-Jaccard) and I2 (content-cosine), since H-NEW-126 MW-5 already established it FIRES at α=0.05 on root-Jaccard cluster cohesion. If ḥawāmīm-mean ranks in bottom-quartile on either, the instrument is NULL-BROKEN.
- MW-6 (instrument-control): the bottom-quartile threshold is corpus-relative, not absolute, so corpus-prior baseline is implicit.
- MW-7 (post-hoc cap): the `rank ≤ 28` threshold is PRE-REGISTERED, not chosen post-observation.

## Garden-of-forking-paths log

- **Why 8 instruments not 5 or 10?** The 8 are project-canonical instrument families (root-set, content-token, char-grams, FR-roots, rhyme, weighted-roots, divine-names, longer-char-grams) that span the project's existing tooling. 5 would under-power the sweep claim; 10 would force tighter Bonferroni without adding orthogonal instruments. 8 is locked.
- **Why nearest-3 not nearest-5 or nearest-1?** Nearest-1 is too noisy (single-pair effects). Nearest-5 conflates with neighborhood-density. Nearest-3 is the standard project default (used in H-NEW-111 top-K coverage at K=3).
- **Why bottom-quartile not bottom-decile?** Bottom-decile (rank ≤ 11/114) would be too tight given the post-hoc nature of the test; bottom-quartile (rank ≤ 28) is conservative and matches the "isolate" semantics in cross-finding-010.

## Files

- Pre-reg: `surahs/Q025-al-furqan/Q025-F-01-true-isolate-persistence-prereg.md`
- Script: `surahs/Q025-al-furqan/scripts/Q025_F_01_true_isolate_persistence.py`
- Output: `surahs/Q025-al-furqan/csv/Q025-F-01.json`

*PRE-REG LOCKED 2026-05-07 — SHA256 to be computed and embedded in run script.*
