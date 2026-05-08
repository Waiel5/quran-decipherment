---
finding_id: Q028-F-05
title: TSM 3-surah joint test (Q 26 + Q 27 + Q 28) Moses-density / prophet-density / narrative-marker cross-correlation
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q028-novel-findings
alpha_bon: 0.01
direction: ONE-SIDED-UPPER (cluster-cohesion claim)
status: PRE-REGISTERED
specialist: Q028-al-qasas-specialist
verdict: TBD
notes: extends Q026-F-02 cohesion design with explicit narrative-density axis, distinct from Q026-F-02 letter-axis test; coordinated with Q026-al-shuara lead specialist
---

# Q028-F-05 — TSM 3-surah joint cohesion test pre-reg

## 1. Hypothesis

The TSM-cluster Q 26-27-28 (each opening `طسم` or `طس`) is the only triple of consecutive surahs sharing the ṬS letter-prefix. We pre-register a multi-axis cohesion test:

**H1 (locked, one-sided upper-tail)**: The cross-surah Spearman correlation across (Q 26, Q 27, Q 28) of three normalised densities — Moses-token density, prophet-naming density, narrative-marker density — exceeds what is expected under random-3-surah selection (10 000 random Meccan-3-tuples, length-matched).

Specifically, define for each surah s:
- `moses_density(s) = count(موسى) / total_tokens(s)`
- `prophet_density(s) = count(prophet-names {موسى, إبراهيم, نوح, هود, صالح, شعيب, لوط, إسماعيل, إدريس, ذو-الكفل, زكريا, يحيى, عيسى, يونس, داود, سليمان, أيوب, يوسف}) / total_tokens(s)`
- `narrative_marker_density(s) = count(narrative markers {قال, قالوا, قالت, فلما, ولما, وإذ, إذ}) / total_tokens(s)`

Compute the centroid `c_TSM = mean of normalised-z-scores of these 3 densities across (Q 26, Q 27, Q 28)` and compare against the centroid of 10 000 random 3-Meccan-surah tuples. If the TSM-centroid exceeds the 95th percentile of the random-tuple distribution, H1 PASSES.

**H2 (locked)**: At least 2 of the 3 individual densities are **above the corpus median** for each TSM surah (i.e., 6 of 9 cells in the 3×3 axis-by-surah matrix). Pre-committed deterministic threshold.

## 2. Direction-locking

H1 direction = TSM-centroid above 95th percentile. Reverse / mid-range = NULL.
H2 direction = ≥ 6 of 9 cells above corpus median. Lower = NULL.

## 3. Method

- Tokenize on orthographic-no-tashkeel, pause-marker stripped.
- Use prefix-tolerant substring match for the prophet-name list.
- 10 000 random 3-tuples drawn from the 86 Meccan surahs (revelation-order CSV — type=meccan).
- Length matching: weight each surah's z-score density by its total-token count (alternative-model: unweighted).
- Spearman correlation across the 3-cell vector — for H1.

## 4. Test family + Bonferroni

Family: Q028-novel-findings, k = 5. α_Bonferroni = 0.01.

## 5. Acceptance / failure

- **PASS (TSM-cohesion-vindicated)** = H1 p_perm < 0.01 AND H2 ≥ 6/9 cells above median.
- **DIRECTIONAL** = exactly one passes.
- **NULL** = 0 of 2 sub-hypotheses pass.

## 6. MW protections

- MW-1: length-weighted sensitivity reported.
- MW-2: 10 000 random Meccan-tuples.
- MW-3: weighted vs unweighted model alternatives.
- MW-5: positive-control = the al-Sabʿ al-Ṭiwāl 7-surah cluster (a known-cohesive cluster) — should pass at top tail.
- MW-6: instrument-control = a random 3-tuple of Meccan surahs of similar revelation-order positions (positions 47-49 in Tanzil revelation order = Q 26 Sh, Q 27 Naml, Q 28 Qaṣaṣ — narrative-grouped by some chronologies) to disentangle "letter-cluster effect" from "revelation-window effect".
- MW-7: not invoked.

## 7. Coordination

This test EXTENDS Q026-F-02 (Moses-cluster cohesion lead by Q026-al-shuara specialist) along the narrative-density axis. It does NOT duplicate Q026-F-02's content-cosine axis. Garden-of-forking-paths log: chosen densities are pre-registered before observation.

## 8. Honest expectation

If H1 / H2 PASS: this would CHALLENGE the established Wave-FALSIFIED §3.7 finding that muqaṭṭaʿāt-letter-clusters ≠ content-clusters; published as DIRECTIONAL with a strict requirement for replication on the next muqaṭṭaʿāt-cluster (e.g., the ALR-5 cluster) before promotion.

If H1 / H2 NULL: this CONSOLIDATES the existing Wave-FALSIFIED §3.7 record on a multi-axis basis.

Either result is a load-cell.

## 9. Pre-reg SHA

To be SHA-256-hashed at file-lock time and embedded in the runner script.
