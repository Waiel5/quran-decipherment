---
finding_id: Q018-F-04
title: "Q 18 Mūsā-Khaḍir block (vv. 60-82) — surah-internal lexical hapax signature"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 18004
n_perm: 10000
bonferroni_k: 1
alpha_raw: 0.05
direction: positive (N3 has more block-internal-hapax roots than random 23-verse spans)
---

# Q018-F-04 — Mūsā-Khaḍir block (N3) lexical hapax signature

## Hypothesis

The Mūsā-Khaḍir narrative (Q 18:60-82, length 23 verses) uses a vocabulary that is largely *closed within the block* — a high count of roots that appear ONLY in this block among Q 18's four narratives. This corresponds to the qualitative claim that the four narratives are lexically near-disjoint.

**Direction (LOCKED)**: N3's block-internal-hapax count (roots appearing in N3 and NOT in N1/N2/N4 or any of the bridge/frame blocks within Q 18) is **higher** than the median of 10,000 random 23-verse spans drawn from Q 18.

## Operational definition

1. Define narrative blocks per H-NEW-268 / classical reading:
   - N1: vv. 9-26 (18 verses)
   - N2: vv. 32-44 (13 verses)
   - N3: vv. 60-82 (23 verses)
   - N4: vv. 83-101 (19 verses; using classical endpoint v. 101)
   - Bridge/frame: vv. 1-8, 27-31, 45-59, 102-110 (= remaining 37 verses)

2. From `data/morphology/quranic-corpus-morphology-0.4.txt`, extract Q 18 per-verse roots.

3. For block N3, compute:
   - `roots_N3_only` = roots appearing in N3 but NOT in N1 ∪ N2 ∪ N4 ∪ bridge/frame.
   - `count_N3_only` = |roots_N3_only|.

4. Random null: draw 10,000 random non-overlapping 23-verse spans from Q 18's 110 verses. For each random span, compute the same `count_random_only` (roots appearing in the random span and not elsewhere in Q 18 EXCEPT possibly in other random spans — implementation: each random span is treated as N3-replacement, with the rest of Q 18 = "elsewhere").

   Note: random spans need not be contiguous (sample 23 random verse-IDs from 1-110). This is a simpler null than contiguous-span.

5. p-value = P(count_random ≥ count_N3) one-tailed.

## Direction (LOCKED)

`count_N3_only > median(count_random)` and p < 0.05.

## Success criteria

- p_one_tailed < α = 0.05: **CONFIRMED**.
- p in [0.05, 0.10]: **DIRECTIONAL**.
- p > 0.10: **NULL**.
- count_N3_only < median(random): pre-commit violation, NULL with prominence.

## Failure criteria

- N3's hapax count is not above random: NULL.

## Rules-tuple

`(no-tashkeel, QAC-stem-roots, QAC v0.4 morphological annotations, basmala-counted-only-in-Q1, Hafs-Kufan)`.

## Expected behavior under H1

The Mūsā-Khaḍir narrative deploys a distinctive vocabulary: *baḥr* (sea), *ḥwt* (fish), *ṣbr* (patience), *ʿbd* (servant in *ʿabdan*-of-God-sense), *ladun* (presence-of), *ʿilm* (with *ladun-nā* construction), *qaryah* (settlement), *jidār* (wall), *kanz* (treasure), *yatīm* (orphan), *afsada* (corrupt), *istaṭāʿa* (be able to). Many of these are not deployed in N1, N2, or N4 of Q 18.

If the test confirms, this is empirical evidence for narrative-block-lexical-isolation — supporting the qualitative claim that Q 18's four narratives are lexically near-disjoint.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q018_F_04_musa_khadir_hapax.py`.
- JSON: `csv/Q018-F-04.json`.
- Findings: `06-novel-findings.md` Q018-F-04 section.
