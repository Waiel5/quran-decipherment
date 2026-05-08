---
finding_id: Q028-F-03
title: Qārūn-episode (Q 28:76-82) structural-isolation in Q 28
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q028-novel-findings
alpha_bon: 0.01
direction: ONE-SIDED-UPPER (block-distinctness)
status: PRE-REGISTERED
specialist: Q028-al-qasas-specialist
verdict: TBD
---

# Q028-F-03 — Qārūn-episode block isolation pre-reg

## 1. Hypothesis

Q 28:76-82 is a 7-verse self-contained Qārūn (Korah) narrative — the only extended Qārūn episode in the corpus. All other Qārūn mentions are passing references (Q 29:39, Q 40:24).

**H1 (locked, one-sided upper-tail)**: Of the 82 contiguous 7-verse windows in Q 28, the window 76-82 ranks **highest** by the metric:

`distinctness(window) = 1 − cos(TF(window), TF(Q28 \ window))`

i.e., it has the **least** vocabulary overlap with the rest of Q 28. Pre-committed rank ≤ 4 / 82 (top 5 %).

**H2 (locked)**: The Qārūn-window TF-vector is **anti-correlated** (cos < 0.10 on shared-root vocabulary, OR rank-bottom-5 of 82 windows by cosine-to-Madyan-window 22-28 vs all other window-pairs in Q 28).

**H3 (locked, deterministic)**: The orthographic token `قارون` (Qārūn) attestations corpus-wide ≥ 50 % in Q 28.

## 2. Direction-locking

H1 direction = Qārūn-window distinctness rank ≤ 4. Reverse = NULL.
H2 direction = Qārūn-Madyan cosine in bottom-5 % of pairwise window cosines. Reverse = NULL.
H3 direction = ≥ 50 % share. Lower = NULL.

## 3. Method

- TF-vector on orthographic-surface-tokens with prefix-stripping (و ف ل ب ال).
- Distinctness measured by cosine to surah-mean (excluding the window).
- For H2: compute pairwise cosines among all 82 contiguous 7-verse windows; rank `cos(W22-28, W76-82)` against the 82·81/2 = 3 321 pair distribution.
- For H3: substring search for `قارون` / `وقارون` etc. across 114 surahs.

## 4. Test family + Bonferroni

Family: Q028-novel-findings, k = 5. α_Bonferroni = 0.01.

## 5. Acceptance / failure

- **PASS** = H1 rank ≤ 4 AND H2 cosine in bottom 5 % AND H3 share ≥ 50 %.
- **DIRECTIONAL** = 1-2 of 3 pass.
- **NULL** = 0 / 3 pass.

## 6. MW protections

- MW-1: window-length matched (7 verses).
- MW-2: exhaustive enumeration of 82 windows + 3 321 pair-cosines.
- MW-3: TF vs TF-IDF sensitivity (secondary).
- MW-5: positive-control = same metric on a randomly-permuted Q 28 (verse-shuffled); the Qārūn-window rank should drop into mid-range.
- MW-6: instrument-control = Madyan-window 22-28 distinctness as a sister-test (one Madyan + one Qārūn = inner-Q28 control).
- MW-7: not invoked.

## 7. Honest framing

The block-boundary 76-82 is the universally-recognised Qārūn-episode boundary in the tafsir tradition (al-Ṭabarī, Ibn Kathīr, al-Qurṭubī all delimit the unit at v. 76 [بقد قال له قومه] through v. 82 [ويكأنه لا يفلح الكافرون]). This boundary was fixed BEFORE observation. The hypothesis is that the narrative-block-boundary recognised by classical scholarship coincides with a measurable lexical-distinctness signature.

This is structurally analogous to the al-Suyūṭī mufaṣṣal-tier discovery — i.e., classical narrative-segmentation finds an empirical correlate.

## 8. Pre-reg SHA

To be SHA-256-hashed at file-lock time and embedded in the runner script.
