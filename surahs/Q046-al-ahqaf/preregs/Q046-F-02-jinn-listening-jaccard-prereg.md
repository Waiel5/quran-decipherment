---
prereg_id: Q046-F-02
title: Q 46:29-32 (jinn-listening) ↔ Q 72 al-Jinn root Jaccard distinctness
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T03:10:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q046-F-02 — Q 46:29-32 ↔ Q 72 jinn-listening lexical signature

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The root-Jaccard between Q 46:29-32 (the jinn-listening verses) and Q 72 al-Jinn is **ABOVE** the root-Jaccard between random 4-verse Q 46 windows and Q 72.

Rationale: classical exegesis (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr ad Q 46:29-32 + Q 72) treats these passages as a thematically-paired corpus-pair. If empirically real, the lexical signature should be detectable as elevated Jaccard.

## 2. Null

**H0**: Q 46:29-32 ↔ Q 72 Jaccard is in the random-4-verse-window ↔ Q 72 distribution (no elevation).

## 3. Operationalization

- **Tashkeel level**: no-tashkeel (default rules-tuple).
- **Root operationalization**: QAC v0.4 stem-root annotations from `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.
- **Q 46:29-32 set**: union of distinct roots in verses 29, 30, 31, 32.
- **Q 72 set**: union of distinct roots in all 28 verses.
- **Jaccard**: |intersection| / |union|.
- **Permutation null**: 10000 random selections of 4 contiguous verses from Q 46 (excluding the 29-32 window itself), each compared to Q 72. p-value = fraction of nulls ≥ observed.

## 4. Direction lock

Pre-committed direction: **observed Jaccard > median(null)**.

If reversed: **NULL with pre-commit violation flag**.

## 5. Bonferroni

This is a single test (k=1). α = 0.05.

## 6. Success / failure criteria

- **VINDICATED**: observed > median(null) AND p_perm < 0.05.
- **DIRECTIONAL**: observed > median(null) but p_perm ≥ 0.05.
- **NULL with pre-commit violation**: observed ≤ median(null).

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q046-F-02.json` with: Q 46:29-32 root-set, Q 72 root-set, intersection, Jaccard, null distribution stats, p-value, top shared roots.

## 9. Notes

Classical anchors:
- al-Ṭabarī, al-Qurṭubī, Ibn Kathīr ad Q 46:29 and Q 72:1 — both explicit in framing the two passages as paired.
- The root *n-f-r* (*nafar* "party") is shared between Q 46:29 and Q 72:1; both are 18-attestation corpus rare-root.
- The root *s-m-ʿ* (listen) and *j-n-n* (jinn) are dense in both passages.
