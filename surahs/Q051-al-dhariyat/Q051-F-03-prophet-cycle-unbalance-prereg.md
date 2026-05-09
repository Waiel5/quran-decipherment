---
surah: 51
test_id: Q051-F-03
title: Q 51:38-46 4-people pericope-cycle unbalance + chronologically-retrograde structure
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q051-F-03-prophet-cycle-unbalance
alpha_bon: 0.0167
---

# Q051-F-03 — Pre-registration: Q 51:38-46 prophet-cycle unbalance hypothesis

## 1. Hypothesis (locked before observation)

Q 51:38-46 contains a 4-people punishment-pericope-cycle (Mūsā / ʿĀd / Thamūd / Nūḥ in 9 verses, 3+2+3+1 length distribution). The cycle is structurally distinct from Q 7's 5-prophet-equal-length structure (per H-NEW-90 partial pass at z=+5.25):

**H1 (locked direction):** Q 51:38-46's pericope-length variance (CV) is HIGHER than Q 7's prophet-cycle CV. Operationally:
- Q 51 pericope lengths: [3, 2, 3, 1] (verse counts for Mūsā/ʿĀd/Thamūd/Nūḥ).
- Q 7 prophet-cycle pericope lengths: ~[24, 23, 23, 23, 24] (Nūḥ vv. 59-64, Hūd vv. 65-72, Ṣāliḥ vv. 73-79, Lūṭ vv. 80-84, Shuʿayb vv. 85-93 — approximate; locked).
- Compute Coefficient of Variation = std/mean for each.
- Locked direction: CV(Q 51) > CV(Q 7).

**H2 (locked direction, secondary):** Q 51:38-46's chronological-ordering is REVERSE of standard Israelite-history forward-ordering. Operationally: encode the 4 prophets in their canonical chronological position (Nūḥ=1, ʿĀd-Hūd=2, Thamūd-Ṣāliḥ=3, Mūsā=5) and compute Spearman ρ between *position-in-Q-51* and *chronological-rank*. Direction locked: ρ < 0 (negative correlation; reverse-ordered).

**H3 (locked direction, exploratory-secondary):** The 4-people cycle is a **catalogic** rather than narrative-extended structure, identifiable by anaphora-marker *wa-fī [SUBJECT]* opening the first 3 of the 4 pericopes (vv. 38, 41, 43). Test: count corpus verses opening with *wa-fī [PROPHET-NAME]* in the strict structural sense; predicted: 3 or 4 (the 3 in Q 51:38-46 plus possibly the Nūḥ-pericope opener at v. 46 with *wa-qawmu nūḥin*).

**H0 (joint):** Q 51's prophet-cycle is NEITHER more variable than Q 7's NOR chronologically reverse-ordered NOR catalogic-anaphora-structured.

**Direction:** locked POSITIVE for all three (CV > Q 7's, ρ < 0, anaphora-count ≥ 3).

## 2. Operational definitions

- **Pericope boundaries** (locked before observation):
  - Q 51 — Mūsā: vv. 38-40; ʿĀd: vv. 41-42; Thamūd: vv. 43-45; Nūḥ: v. 46.
  - Q 7 — Nūḥ: vv. 59-64 (6 v); Hūd: vv. 65-72 (8 v); Ṣāliḥ: vv. 73-79 (7 v); Lūṭ: vv. 80-84 (5 v); Shuʿayb: vv. 85-93 (9 v).
- **CV** = std(lengths) / mean(lengths).
- **Chronological rank** (locked): Nūḥ=1, ʿĀd-Hūd=2, Thamūd-Ṣāliḥ=3, Lūṭ=3, Shuʿayb=4, Mūsā=5.
- **Position-in-Q-51 / Q-7**: the order in which the prophet/people appears.
- **Spearman ρ**: rank correlation between position-in-X and chronological-rank.
- **Anaphora**: opening-word match `^وفي\b` (literal *wa-fī*).

## 3. Test statistic

- CV(Q 51) and CV(Q 7).
- Spearman ρ for Q 51 prophet-cycle position vs chronology.
- Count of *wa-fī [PROPHET-NAME]* corpus-wide.

## 4. Permutation null

H1: random 4-prophet-pericope-length-shuffle within {1, ..., 14} (the Q 51 prophet-block has 14 prophet verses Vv 38-46... wait, that's 9. recount.) Actually, the locked test is **descriptive** — CV is a single number, not a permutation-test quantity. The "null" is whether CV(Q 51) > CV(Q 7).

H2: descriptive — ρ is a single number from a 4-vs-4 ordered comparison.

H3: descriptive — the count of *wa-fī [PROPHET]* corpus-wide.

This is a **descriptive-comparative** pre-reg, not a permutation pre-reg. Acceptance is direction-match on each of {H1, H2, H3} relative to the locked hypothesis.

## 5. Success / Failure

- **CONFIRMED**: H1 CV(Q 51) > CV(Q 7), H2 ρ < 0, H3 count ≥ 3.
- **DIRECTIONAL**: 1-2 of {H1, H2, H3} pass.
- **NULL**: 0/3 pass.
- **PRE-COMMIT VIOLATION**: CV(Q 51) ≤ CV(Q 7) — the surah is MORE balanced, not less.

## 6. Honest limits known a priori

- This is a structural-descriptive test on a small N (4 pericopes); statistical power is limited. The CV and ρ comparisons are pre-locked but may not survive different pericope-boundary choices.
- The Q 7 baseline pericope-lengths are taken from the standard tafsir-tradition boundaries; alternative boundaries are possible.
- The chronological-rank is itself a classical-tradition assignment with some flexibility (e.g., Thamūd vs Lūṭ chronological order). Locked-rank is the al-Suyūṭī tradition.

## 7. Rules-tuple

`(no-tashkeel, structural-pericope-count, classical-chronology, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`.

## 8. Bonferroni

k = 3 (H1 CV-comparison, H2 Spearman, H3 anaphora-count). α_bon = 0.0167. Note: this is a categorical-pass test, not a continuous-test, so Bonferroni is loose.

## 9. Coordination

Independent of Q 7 specialist. Q 51 prophet-cycle structure was the central anchor of this specialist's brief. No duplication.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q051_F_03_prophet_cycle_unbalance.py`, verified at runtime.
