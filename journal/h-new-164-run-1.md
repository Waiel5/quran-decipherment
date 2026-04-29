---
id: h-new-164-run-1
date: 2026-04-17
hypothesis: h-new-164-fourier-verse-count
status: complete
---

# H-NEW-164 — Run 1 journal

## What I ran

DFT-based power-spectrum analysis of the 114 verse-count sequence in
canonical mushaf order. Pre-reg: α=0.05, Bonferroni k=1, seed=20260419,
n_perm=10,000 (random permutations of the same 114 integers as null).

- Primary: x = total_verses for each of 114 surahs.
- Secondary: cum[i] = cumulative sum x[0..i].
- MW-5: synthetic sinusoid length 114, f0=7, must peak at k=7.

## Key outputs

- MW-5: P_norm[7] = 1.000, argmax_k=7 → passed.
- Primary observed max peak: P_norm[1] = 0.332; null 99th = 0.139;
  null max = 0.231 across 10,000 perms → p = 9.999e-05.
- Secondary observed max peak: P_norm[1] = 0.579; null 99th = 0.143;
  null max = 0.258 → p = 9.999e-05.
- Primary top-5 (k, P_norm): (1,0.332), (2,0.099), (7,0.077),
  (3,0.061), (6,0.038).
- Secondary top-5: (1,0.579), (2,0.173), (3,0.064), (4,0.039), (5,0.025).

## Interpretation

Statistical null rejected at p < 1e-4 for both sequences, BUT the signal
is entirely in k=1 — the DC-adjacent low-frequency mode — which is the
Fourier footprint of the well-known descending-length ordering. This is
a **sanity-check level confirmation** that mushaf order is not a random
permutation, re-expressed in the frequency domain. No non-trivial
periodicity (e.g., k=7, k=19, etc.) exceeded null. The k=7 peak at 0.077
is below null 95th percentile (0.115) and **not significant**.

Honest posture: the descending-length convention is known; the "reject
null" verdict is uninteresting on its own. A genuinely novel follow-up
would require detrending (subtract monotone envelope) and testing
residual periodicity.

## Files

- `scripts/h_new_164_fourier_verse_count.py`
- `findings/phase-b-hypotheses/csv/h-new-164.json`
- `findings/phase-b-hypotheses/h-new-164-fourier-verse-count.md`
- `findings/phase-b-hypotheses/h-new-164-fourier-verse-count-prereg.md`

## Garden-of-forking-paths notes

Choices fixed in pre-reg before run:
- mean-detrend before DFT (removes DC).
- Normalize by sum over k=1..57 (Nyquist), not by total variance of x,
  so P_norm sums to 1 on the alternating-frequency band.
- Null: random permutation (no replacement) of the same 114 integers —
  preserves multiset, breaks position dependence.
- p = (k+1)/(N+1) style with N=10,000.

No post-hoc tuning. The qualitative result (k=1 dominance) is robust
and exactly what the ordering principle predicts.

## Verdict

Reject null (p < 1e-4) — descriptive / trivial-structure. Publish with
honest framing: not a novel periodicity discovery.
