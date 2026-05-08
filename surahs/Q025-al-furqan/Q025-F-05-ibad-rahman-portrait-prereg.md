---
finding_id: Q025-F-05
title: ʿIbād al-Raḥmān (Q 25:63-77) self-similarity and its structural twin in Q 23:1-11
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q025-al-furqan-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q025-F-05-ibad-rahman
bonferroni_k: 3
alpha_bon: 0.01666
direction: Cell A — HIGHER intra-block self-similarity vs surah-internal random null; Cell B — HIGHER (Q25:63-77, Q23:1-11) cross-block similarity than random equal-length cross-surah blocks; Cell C — DESCRIPTIVE on shared *alladhīna* relative-clause-of-attributes structure
success_criterion: Cell A passes at p ≤ α_bon; Cell B passes at p ≤ α_bon; Cell C verifies descriptively
rules_tuple: "(no-tashkeel, orthographic-token, IDF-cosine on Q-internal then cross-Q vocab, Hafs-Kufan, Mashriqi)"
script: surahs/Q025-al-furqan/scripts/Q025_F_05_ibad_rahman.py
output_json: surahs/Q025-al-furqan/csv/Q025-F-05.json
---

# Q025-F-05 — *ʿIbād al-Raḥmān* portrait + Q23 twin (pre-reg)

## Hypothesis

Q 25:63-77 is the famous *ʿibād al-Raḥmān* (Servants of the Most-Merciful) catalog — a 15-verse block enumerating the attributes of true believers, structured as a chain of *alladhīna yamshūn / yabītūn / yaqūlūn / yunfiqūn / lā yadʿūna / lā yashhadūna / yaqūlūna* relative clauses, terminating in eschatological reward (v. 75-76: *ulāʾika yujzawna al-ghurfata*).

Q 23:1-11 is a structurally similar 11-verse block opening Q 23 al-Muʾminūn — a cascade of *alladhīna hum / wa-alladhīna hum* relative clauses describing the believers (*qad aflaḥa al-muʾminūn / alladhīna hum fī ṣalātihim khāshiʿūn...*), terminating in eschatological reward (v. 10-11: *ulāʾika hum al-wārithūn*).

Both Q 23 and Q 25 are members of the H-NEW-126 true-isolate core. The *ʿibād al-Raḥmān* / *muʾminūn* portrait may be a SHARED RHETORICAL GENRE locking these two together.

## Three test cells

**Cell A — Intra-block self-similarity**: Compute the mean pairwise cosine similarity (TF-IDF on Q 25-internal vocabulary) of the 15 verses Q 25:63-77 against (i) Q 25's other 62 verses, taken as a within-surah null. Permutation null: 1000 random size-15 contiguous (or non-contiguous, both reported) windows from Q 25's other verses.
- Direction: pre-committed HIGHER.

**Cell B — Cross-block twin similarity**: Compute the mean pairwise cosine similarity (TF-IDF on the union of Q 23-internal and Q 25-internal vocabularies) between the 15 verses Q 25:63-77 and the 11 verses Q 23:1-11 (15×11 = 165 cross-pairs). Compare against null = mean similarity for random pairs (equal-size verse blocks drawn from across the corpus, matched on block-length).
- Direction: pre-committed HIGHER.

**Cell C — Shared structural marker**: count occurrences of the relative pronoun *alladhīna* (الذين) in each block. Descriptive: report counts and per-verse density.

## Bonferroni accounting

k = 3 cells. α_bon = 0.05 / 3 = 0.01666.

## Acceptance / failure

- Cell A and Cell B BOTH pass at p ≤ α_bon AND Cell C verifies descriptively ⇒ **PASS-DIRECTED**: Q 25:63-77 is a self-cohesive block AND structurally twinned with Q 23:1-11. Candidate twin signature for cross-finding-028.
- Cell A passes alone OR Cell B passes alone ⇒ **DIRECTIONAL**.
- Neither passes ⇒ **NULL**.

## Direction is locked HIGH

Direction is HIGHER. Reversed direction (block is internally LESS similar than within-surah random, OR cross-block is LESS similar than random pairs) is a pre-commit violation.

## MW protections

- MW-1 (instrument-prior): TF-IDF cosine specified; window-size and block boundaries pre-registered.
- MW-2 (corpus-prior): 10000-permutation null per cell.
- MW-5 (positive-control): the analogous 11-verse Q 23:1-11 block should ALSO show high intra-block self-similarity vs Q 23-internal random (≥ p=0.05 one-sided upper). If Q 23:1-11 fails its own self-similarity test under the same procedure, the instrument is NULL-BROKEN.
- MW-6 (instrument-control): a CONTROL pair = (Q 25:63-77, Q 70:22-35 — the parallel *muṣallīn*-portrait in al-Maʿārij). If Q70 control passes Cell-B-style test at the same significance, the test is detecting a genuine portrait-genre, not a Q23/Q25 idiosyncrasy. (Reported descriptively.)

## Garden-of-forking-paths log

- Block boundaries 63-77 for Q25 and 1-11 for Q23 are TAFSIR-CANONICAL (not chosen for fit).
- The third candidate portrait Q 70:22-35 is a known *muṣallīn*-catalog and serves as MW-6 control. We do NOT pre-register it as a primary cell because it would inflate Bonferroni; we report it descriptively.
- TF-IDF on the union vocabulary for Cell B (not just one surah's vocab) controls for vocabulary-set asymmetry.

## Files

- Pre-reg: `surahs/Q025-al-furqan/Q025-F-05-ibad-rahman-portrait-prereg.md`
- Script: `surahs/Q025-al-furqan/scripts/Q025_F_05_ibad_rahman.py`
- Output: `surahs/Q025-al-furqan/csv/Q025-F-05.json`

*PRE-REG LOCKED 2026-05-07.*
