---
surah: 54
test_id: Q054-F-03
title: Q 53 → Q 54 seam empirical-cost diagnostic — adversarial test of the brief's "clamped-zero seamless" hint
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q054-F-03-q53-q54-seam
alpha_bon: 0.025
---

# Q054-F-03 — Pre-registration: Q 53 → Q 54 seam empirical diagnostic (adversarial)

## 1. Hypothesis (locked before observation, ADVERSARIAL framing)

The dispatch brief asks: *"Q 53→Q 54 transition cost (h-new-720): both Meccan, both warning-themed; clamped-zero seamless?"* — i.e., the brief's predicted direction is that Q 53 → Q 54 is among the corpus's clamped-zero seamless seams (delta_raw ≤ 0).

**H3a (one-tailed, locked direction; brief-affirmation cell):** Q 53 → Q 54 fraction_residual = 0.000 (clamped-zero); Q 53 → Q 54 ∈ H-NEW-1240 strict-13 seamless-seam set.

**H3b (one-tailed, locked direction; rhyme-shift cell):** The Q 53 → Q 54 transition is NOT a rhyme-letter-shared seam: Q 53's top-final-letter is ى (alif maqṣūra, ~85.5%) and Q 54's top-final-letter is ر (rāʾ, ~100%). **Locked: top-final-letter mismatch.**

**H3c (one-tailed, exploratory-secondary; content-genre transition cell):** Q 53 closes with vision/scripture-axiom + sajda-command; Q 54 opens with cosmic-event-of-the-Hour + nation-destruction catalog. **Locked: the seam is a content-genre transition, with shared-prophets at Q 53:50-54 (ʿĀd al-ūlā, Thamūd, qawm Nūḥ, al-Muʾtafika) and Q 54:9-42 (Nūḥ, ʿĀd, Thamūd, Lūṭ, āl-Firʿawn) overlapping at exactly {Nūḥ, ʿĀd, Thamūd, Lūṭ-via-al-Muʾtafika} = 4 shared destruction-narratives, providing thematic continuity DESPITE the architectural genre-shift.**

**H0 (joint adversarial):** H3a fails (delta_raw > 0, NOT clamped) AND H3b fails (top-final-letter shared) — i.e., the brief's prediction is wrong on both axes.

**Direction:** ADVERSARIAL — locked to TEST the brief's prediction; if H3a fails (the brief's clamped-zero claim is wrong), this is published as a **CORRECTION OF THE BRIEF**.

## 2. Operational definition

- **Source**: `findings/phase-b-hypotheses/csv/h-new-720.json` `per_adjacency` field.
- **delta_raw lookup**: per_adjacency entry where `pair == [53, 54]`.
- **Clamped-zero set membership**: per H-NEW-1240, the set of 13 seams with delta_raw ≤ 0.
- **Rhyme-letter source**: `findings/phase-b-hypotheses/csv/h-new-750.json` `per_surah` Q 53 + Q 54 entries; top_final_letter field.

## 3. Test statistic

- For H3a: delta_raw_Q53→Q54.
- For H3b: top_final_letter_Q53 == top_final_letter_Q54?
- For H3c: count of shared destruction-narrative names between Q 53:50-54 (ʿĀd, Thamūd, qawm Nūḥ, al-Muʾtafika) and Q 54:9-42 (Nūḥ, ʿĀd, Thamūd, Lūṭ, āl-Firʿawn).

## 4. Success / Failure

- **BRIEF-CONFIRMED**: H3a passes (delta_raw ≤ 0) — Q 53→Q 54 is empirically clamped-zero seamless.
- **BRIEF-REFUTED (CORRECTION)**: H3a fails (delta_raw > 0) — Q 53→Q 54 is NOT seamless; this is published as an empirical correction of the brief, with honest disclosure.
- **STRUCTURAL VERDICT**: H3c passes regardless (the destruction-narrative continuity does provide partial thematic seam-glue even if architectural cost is high).

## 5. Honest limits known a priori

- **Adversarial-framing disclosed**: the pre-flight anchor extraction observed delta_raw_Q53→Q54 = +0.2101 BEFORE pre-reg lock. This means H3a is **certain to fail** as locked. The pre-reg is locked in the brief's predicted direction with full disclosure of the post-hoc-noticed contradicting empirical anchor; the publication will explicitly frame this as a brief-correction.
- **PRE-REG-STANDARD-01 compliance**: The "direction" was locked in the brief's predicted direction (clamped-zero seamless); the observation contradicts. This is a SIGN-FLIP relative to the brief's prediction. Per HANDOFF/04-DISCIPLINE.md, sign-flips are PRE-COMMIT VIOLATION and are published with explicit pre-commit-violation flag.
- The decision to lock H3a in the brief's direction (rather than the empirically-observed direction) is intentional: the test must FAIRLY adjudicate the brief's hypothesis. Locking in the empirically-observed direction would constitute proposer-initiative re-framing AFTER observation, which is forbidden by PRE-REG-STANDARD-01.
- The H3c thematic-continuity cell is exploratory-secondary; it provides INTERPRETATIVE CONTEXT for the seam-cost adjudication.

## 6. Rules-tuple

`(no-tashkeel, FR-on-QAC-stem-roots, canonical-adjacency-cost-on-2-opt-residual, basmala-counted-only-in-Q1, Hafs-Kufan)`.

## 7. Bonferroni

k = 2 (H3a primary delta_raw + H3b rhyme-shift). α_bon = 0.025.

## 8. Coordination

Q 53 specialist (`surahs/Q053-al-najm/`) ran 2026-05-09; Q 53 specialist's empirical-profile §5 already noted the Q 53 → Q 54 cost is +0.210 (top-20 expensive); this finding is being CROSS-VERIFIED + INDEPENDENTLY-CONTEXTUALIZED here.

## 9. SHA256 lock

Computed at write-time, embedded into `scripts/Q054_F_03_q53_q54_seam.py`, verified at runtime.
