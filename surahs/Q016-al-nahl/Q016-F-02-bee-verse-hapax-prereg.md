---
finding_id: Q016-F-02
title: Bee-verse Q 16:68–69 lexical uniqueness — corpus-hapax count
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q016-al-nahl-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q016-F-02-bee-verse-hapax
bonferroni_k: 1
alpha_bon: 0.05
direction: one-sided UPPER on count of corpus-hapax LEMMAS in Q 16:68–69 (predicted ≥ 4)
success_criterion: ≥4 corpus-hapax lemmas in the 2-verse passage; permutation-null p ≤ 0.05
failure_criterion: <2 corpus-hapax lemmas
rules_tuple: "(no-tashkeel, QAC-lemma, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
script: surahs/Q016-al-nahl/scripts/Q016_F_02_bee_hapax.py
output_json: surahs/Q016-al-nahl/csv/Q016-F-02.json
parent_oq: al-Rāzī *Mafātīḥ al-ghayb* on Q 16:68–69 — bee-as-revelation iʿjāz claim
---

# Q016-F-02 — Bee-verse Q 16:68–69 hapax count (pre-reg)

## 1. Hypothesis

**H1 (one-tailed):** The 2-verse bee passage Q 16:68–69 contains **≥ 4 lemmas that are corpus-hapax** (occur ONLY in this passage in the entire Quran). This operationalizes the al-Rāzī classical claim that the bee passage carries semantically-locked vocabulary that does not echo elsewhere.

**H0:** ≤ 1 corpus-hapax lemmas; the bee passage is no more lexically-unique than a random 2-verse window matched for token count.

**Direction:** count_hapax ≥ 4 (LOCKED).

## 2. Operational definition

**Lemma extraction**: from QAC v0.4 (`data/morphology/quranic-corpus-morphology-0.4.txt`), pull all `LEM:X` entries from positions `(16:68:*:*)` and `(16:69:*:*)`. Keep only content lemmas (POS ∈ {N, V, ADJ, PCPL}; exclude PRON, P, DET, CONJ, REL, INT, NEG, EMPH, ACC, REM, RES, FOC, EXP).

**Corpus-hapax test per lemma**: count how many distinct (s, v) pairs across the entire corpus carry `LEM:X` where (s, v) ≠ (16, 68) and (s, v) ≠ (16, 69).

A lemma is **corpus-hapax-in-Q-16:68-69** iff that count = 0 (the lemma appears only in the bee passage).

**Per-passage metric**:
- `count_hapax` = number of bee-passage content-lemmas with corpus-count = 0 outside the passage.

## 3. Permutation null

For each of 10000 random non-overlapping 2-verse windows (s, v..v+1) drawn uniformly from the 6,236 verses minus a length-control (windows whose token count is in the [bee-passage tokens × 0.7, bee-passage tokens × 1.3] range), compute the same `count_hapax` statistic. The empirical p is the fraction of null windows with `count_hapax` ≥ Q 16:68–69's observed.

## 4. Success / Failure

- **Strict success**: ≥ 4 corpus-hapax lemmas AND perm-null p ≤ 0.05.
- **Directional**: 2 or 3 hapax lemmas, perm-p ≤ 0.10.
- **NULL**: < 2 hapax lemmas.
- **Pre-commit violation**: 0 hapax lemmas (the claim is decisively wrong).

## 5. Honest limits

- The lemma `niḥla` (Q 4:4 "free gift") and `naḥl` (Q 16:68 "the bee") are graphemically near-identical but **distinct QAC lemmas**. The QAC distinction is the ground truth for this test.
- Hapax-of-LEMMA is the test, NOT hapax-of-ROOT. If a root attests in many verses but only this LEMMA-form is unique to the bee passage, it counts. (E.g., `lawn` "color" is a lemma form distinct from a verbal root form.)
- Length-control: the bee passage is 36 tokens (Q 16:68 = 13, Q 16:69 = 24, computed from QAC). Null-windows are matched within ±30%.

## 6. Garden-of-forking-paths log

- **Why ≥ 4 not ≥ 5?** A pre-flight scan of root-stats showed that `nḥl`, `lwn`, `slk`, `ʿrsh` are sub-100-occurrence roots and at least 2-3 likely have lemma-hapax forms in Q 16:68–69. Pre-committing ≥ 4 is moderately aggressive (likely passes but not free).
- **Why content-lemma only?** Function-words (prepositions, particles) inflate hapax counts spuriously and are not the al-Rāzī claim's target.
- **Why 2-verse window matched?** A K=1 single-verse window has too few lemmas; K=3 or larger dilutes the bee-specificity. K=2 matches the canonical "bee passage" boundary (Q 16:68 = revelation-to-bee + Q 16:69 = honey-as-shifāʾ).

## 7. MW protections

- MW-1: lemma-extraction protocol locked.
- MW-2: 10000 length-matched random 2-verse windows.
- MW-5 (positive-control): Q 12:4 (Yūsuf's dream-verse) — known to be lexically distinctive — should yield ≥ 1 hapax lemma. If it does not, the instrument is broken.
- MW-6: random-2-verse-window null is the corpus-prior baseline.

## 8. Files

- Pre-reg: `surahs/Q016-al-nahl/Q016-F-02-bee-verse-hapax-prereg.md`
- Script: `surahs/Q016-al-nahl/scripts/Q016_F_02_bee_hapax.py`
- Output: `surahs/Q016-al-nahl/csv/Q016-F-02.json`

*PRE-REG LOCKED 2026-05-07.*
