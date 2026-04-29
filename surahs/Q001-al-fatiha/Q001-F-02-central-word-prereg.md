---
surah: 1
test_id: Q001-F-02
title: Central-word identification in Q 1 (29 words → position 15)
file_type: pre-registration
date_locked: 2026-04-28
seed: 14102
---

# Q001-F-02 — Pre-registration: Central-word identification

## 1. Hypothesis

**H1 (locked):** If Q 1 has 29 words (no-tashkeel, orthographic-word, basmala counted), then word #15 is the unique median word. We pre-register that word #15 will be in verse 5 (*iyyāka naʿbudu wa-iyyāka nastaʿīn*) — a classical claim that v5 is the pivotal verse.

## 2. Test

Compute:
- N = total word count of Q 1 (no-tashkeel, basmala-counted).
- If N is odd, central index = (N+1)/2.
- Otherwise, central indices = {N/2, N/2+1}.
- Identify (verse_id, word_position_in_verse, word_text) at central index.

## 3. Success criterion

VINDICATED if central word is in verse 5.
NULL if central word is in any other verse.

## 4. Rules-tuple

- Tashkeel: no-tashkeel
- Token: orthographic-word
- Basmala counted as V1 of Q 1 (Hafs)
- Reading: Hafs-Kufan

## 5. Robustness check (additional)

Re-run with basmala NOT counted as a verse but words still counted: N=29 still, position-15 still v5? (Numerical answer expected unchanged because we count words globally, not verses; but report.)

Also re-run on min-tashkeel and full-tashkeel variants — confirm word-count invariance.

## 6. Pre-commit guardrails

Direction LOCKED. The test is mechanical and cannot be massaged.
