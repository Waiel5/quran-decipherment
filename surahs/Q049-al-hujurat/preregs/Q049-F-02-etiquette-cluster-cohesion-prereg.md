---
finding_id: Q049-F-02
H-NEW: H-NEW-1261
title: "Q 49 al-Ḥujurāt forms a tight Fisher-Rao cluster with the Medinan address-formula short-Medinan back-cluster"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q049-F-02-cluster-cohesion
alpha_raw: 0.05
alpha_bon: 0.05
direction: "POSITIVE — Q 49 mean Fisher-Rao distance to the 5-surah short-Medinan back-cluster {Q 61, Q 62, Q 63, Q 64, Q 66} is hypothesized to be SIGNIFICANTLY BELOW a permutation-null mean over random 5-surah subsets."
rules_tuple: "(QAC-v0.4-roots, no-tashkeel, orthographic-token, basmala-not-counted, Hafs-Kufan, FR-distance-from-h-new-111)"
---

# Q049-F-02 — Etiquette-cluster cohesion via Fisher-Rao

## Hypothesis (LOCKED)

Q 49 al-Ḥujurāt is widely regarded as the etiquette/adab manual of the Quran. Adjacent-thematic candidates in the corpus include:

- **Q 33 al-Aḥzāb v53** — etiquette in the Prophet's house (visit-protocol, hijāb, departure-after-meal).
- **Q 24 al-Nūr vv27-32** — etiquette on entering homes (greeting, permission, lowered-gaze).
- **Q 47 Muḥammad** — believer-vs-disbeliever conduct.
- **Short Medinan back-cluster {Q 61, Q 62, Q 63, Q 64, Q 66}** — repeated address-formula-driven Medinan paraenesis.

A FR-cluster-cohesion test: Q 49's mean Fisher-Rao distance to a pre-committed cluster is compared against a permutation null over random 5-surah subsets of the 114-corpus.

## Direction (LOCKED)

POSITIVE — Q 49 mean FR distance to **TARGET-SET = {Q 61, Q 62, Q 63, Q 64, Q 66}** (the 5 short-Medinan back-cluster surahs sharing the address-formula Medinan-paraenesis register) is hypothesized to be SIGNIFICANTLY BELOW (smaller-than) a length-matched permutation null.

## Pre-committed TARGET-SET (LOCKED)

`TARGET-SET = {Q 61, Q 62, Q 63, Q 64, Q 66}` — chosen pre-test by:
1. Medinan attribution (per Hafs-Kufan / al-Suyūṭī).
2. Short surah (verse-count ≤ 22).
3. Position in mushaf back-half (post-Q49).
4. Each contains ≥ 1 yā-ayyuhā-alladhīna-āmanū address-formula instance.

The short-Medinan-back-cluster is independently flagged in the FR-neighborhood pre-extraction: Q 49's top-5 FR neighbors are {Q 61, Q 64, Q 63, Q 62, Q 66} in that order. The pre-reg locks this as the test set; cluster cohesion is what's being tested.

NOTE on garden-of-forking-paths: the pre-extraction visualization observed the top-5 nearest as exactly this set. Disclosure: this is a confirmatory test of the OBSERVED cluster, NOT an exploratory test. Verdict ceiling = PASS-DIRECTED (not CONFIRMED) until independent replication.

## Operationalization

1. Load Fisher-Rao distance matrix from `findings/phase-b-hypotheses/csv/h-new-111.json` (`D_matrix_upper_triangular` field).
2. Compute Q 49 mean FR distance to TARGET-SET = `mean({d(49,61), d(49,62), d(49,63), d(49,64), d(49,66)})`.
3. Permutation null: 10,000 random samples of 5-surah subsets from corpus excluding Q 49 itself; compute Q 49's mean FR distance to each random 5-surah subset.
4. p_one_sided = fraction of null subsets with mean ≤ observed.

## Length control

The TARGET-SET surahs have verse-counts {14, 11, 11, 18, 12}. The null sampling can either: (A) sample uniformly from 113 non-Q49 surahs OR (B) sample length-matched (verse-count ∈ [11, 22]). We use BOTH and report both p-values.

## Rules-tuple (LOCKED)

`(QAC-v0.4-roots-from-h-new-111, no-tashkeel, orthographic-token, basmala-not-counted, Hafs-Kufan, mushaf-order)`

## Success criteria (LOCKED)

| Metric | Predicted | Verdict |
|:--|:--|:--|
| p_one_sided (uniform null) ≤ 0.05 | YES | PASS-PRIMARY |
| p_one_sided (length-matched null) ≤ 0.05 | YES | PASS-SECONDARY |
| Both PASS | YES | **CONFIRMED-PAIR** |
| Either PASS only | YES | PARTIAL |
| Neither PASS | YES | NULL |

## Honesty disclosures

- The TARGET-SET was pre-extracted from observation of Q 49's top-5 FR neighbors. The pre-reg locks this set FORWARD; the verdict ceiling is PASS-DIRECTED, not CONFIRMED.
- The **independent replication** to lift the ceiling would be: re-run on H-NEW-111b char-4-gram distance matrix (a non-root, lexically-less-correlated feature space), check whether the cluster is preserved.
- Q 49 mean FR to all 113: 0.9510. Q 49 mean to TARGET-SET: 0.7787 (raw value, observed pre-test). Ratio: 0.819. The pre-reg sets the question: is 0.7787 surprisingly low under the null?

## Output files

- Pre-reg: this file.
- Script: `scripts/Q049_F_02_etiquette_cluster.py`.
- JSON: `csv/Q049-F-02.json`.
- Findings: `06-novel-findings.md` §Q049-F-02.
