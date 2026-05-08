---
surah: 29
test_id: Q029-F-01
title: Q 29:41 spider parable lexical uniqueness (hapax count)
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
alpha_bon: 0.05
hypothesis_anchor: al-Rāzī (*Mafātīḥ al-ghayb* on Q 29:41); al-Biqāʿī (*Naẓm al-durar* on Q 29 → spider as semantic eponym)
verdict_ceiling: PASS-DIRECTED (single-test cap; replication queue prospective)
---

# Q029-F-01 — Pre-registration: ʿankabūt parable lexical uniqueness

## 1. Hypothesis (LOCKED before observation)

**H1:** The Q 29:41 spider-parable verse contains **at least 2 corpus-hapax-or-near-hapax lemmas** (defined as lemma confined to ≤ 2 surahs in QAC v0.4).

Candidate-set (frozen, drawn from Q 29:41 surface): `{Eankabuwt, >awohan, bayot-as-lexical-unit, maval-as-parable-formula, waliY~-as-protector}`.

**H0:** Fewer than 2 hapax-or-near-hapax.

**Direction:** ≥ 2 hapax (LOCKED).

## 2. Operational definition

For each candidate lemma: corpus-wide count of QAC v0.4 attestations + distinct-surah set. Classification as in [[Q030-F-02-rum-prophecy-hapax-prereg|Q030-F-02]].

## 3. Comparison anchor (Q 16:75-76, Q 27:18)

For comparative interpretation only (not part of test), report hapax-count for the candidate lemmas of Q 16:75-76 (the slave/free man parable) and Q 27:18 (the ant-valley narrative).

## 4. Bonferroni

k=1. α=0.05.

## 5. Success / Failure

| Outcome | Verdict |
|:--|:--|
| ≥ 2 hapax-or-near-hapax | **PASS-DIRECTED** |
| 1 hapax | **DIRECTIONAL** |
| 0 hapax | **NULL** |

## 6. Rules-tuple

`(QAC v0.4, LEM tags, hafs-kufan, no-tashkeel)`.

## 7. SHA256 lock

Embedded in `scripts/Q029_F_01_ankabut_parable_hapax.py`.

## 8. Honest a-priori limits

- Same as [[Q030-F-02-rum-prophecy-hapax-prereg|Q030-F-02]] §8 (curated-from-target confound).
- The 5-lemma candidate set deliberately includes `bayot` and `maval` — both common QAC lemmas — to provide "non-hapax controls" within the candidate-set so that the hapax-count is not 5/5 by curation alone.
