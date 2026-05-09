---
test_id: Q072-F-02
title: Q 72 corpus-rank-1 in jinn-lemma density (strict LEM:jin~ from QAC v0.4)
hypothesis_class: lexical-density-ranking
date_locked: 2026-05-09
seed: 20260509
n_perm: 0
rules_tuple: "(no-tashkeel, QAC v0.4 morphological lemma filter, LEM:jin~ strict (excludes jin~ap=garden, jaA^n~=alt-form, junnap=shield, majonuwn=mad, jan~ap=garden-pl, jan~a=cover-verb), per-surah word-count from quran-no-tashkeel.json, basmala-counted-only-in-Q1, Hafs-Kufan)"
bonferroni_k_local: 1
alpha_local: 0.05
---

# Q072-F-02 — Q 72 is corpus-rank-1 in jinn-lemma density

## Hypothesis

Q 72 al-Jinn — the surah named for the jinn — has the **highest density of the jinn-being lemma per 1000 tokens** of any surah in the corpus.

## Empirical lens

QAC v0.4 lists 8 distinct lemmas under root `jnn`: jin~ (the jinn-beings), jin~ap (garden), jan~ap (gardens-pl), jaA^n~ (the rare poetic synonym for jinn-beings, primarily in Q 55 *al-jaAn~*), junnap (shield), jan~a (cover-verb), majonuwn (one possessed/mad), >ajin~ap (gathered). The semantically primary jinn-being lemma is **LEM:jin~** (22 tokens corpus-wide).

The pre-committed lens is the **strict LEM:jin~** filter. The rationale: (1) this is the unambiguous "the jinn" beings lemma, (2) Q 72's named-referent is *al-jinn* not *al-jaAn~*, and (3) the test asks whether the surah-named-for-the-jinn-beings has the highest density of THAT specific lemma. Including LEM:jaA^n~ would bias the test toward Q 55 (which contains 4 of the 7 corpus jaA^n~ tokens, with the refrain *khalaqa l-jaAn~a min mAriji-n-min nAri-n*).

## Pre-committed prediction

**Direction: PASS** — Q 72 ranks 1 of 114 in LEM:jin~ tokens per 1000 surah-tokens.

## Counting protocol

For each surah s ∈ {1, ..., 114}:
- jin_count(s) = number of QAC tokens with `LEM:jin~` AND `ROOT:jnn` in surah s.
- words(s) = sum over verses of len(text.split()) using the no-tashkeel JSON.
- density(s) = jin_count(s) / words(s) * 1000.

Sort 114 surahs by density descending; report Q 72's rank.

## Success criteria

- **PASS (PRIMARY)**: Q 72 rank = 1 / 114.
- **DIRECTIONAL**: Q 72 in top-3.
- **NULL**: Q 72 rank ≥ 4.

## Sensitivity check

A secondary, post-hoc-flagged rank is also computed under the **expanded lens** LEM:jin~ + LEM:jaA^n~ (combined jinn-being lemmas). This is reported but does NOT enter the primary verdict. Pre-committed prediction for the secondary lens: Q 72 rank ≥ 2 (because Q 55's jaA^n~ density is high).

## Honest limit

A density-ranking is descriptive, not inferentially permuted (n_perm = 0). The test functions as a corpus-EXACT empirical verification of the surah-name → primary-lemma alignment. The expected verdict is informationally weak (the surah is named for the jinn, so density-ranking it #1 is a low-surprise outcome) but verifying the ALIGNMENT between liturgical-naming convention and corpus-lexical-distribution is itself a finding: it tests whether Quranic surah-naming is content-faithful (PASS) or descriptive-conventional (FAIL).

This is also a deliberate corpus-rank-1 anchor test: if Q 72 is NOT rank-1 in *jinn*-density, the surah-name → primary-lemma faithfulness is FALSIFIED for at least one surah, which would be a corpus-level finding.
