---
run: H-NEW-43 run-1 (amended by audit-032 amendments 43-A, 43-B)
date: 2026-04-15
seed: 20260415
outcome: NULL-BROKEN (AR(1) Ljung-Box lag-10 failed; positive control PASSED)
---

# H-NEW-43 Run-1 Journal (amendments applied)

## Timeline

- 14:00 — Read pre-reg. Locked specs before any spectral plot.
- 14:05 — Data inventory. bukhari-noquran.txt empty; used bukhari.txt. Muallaqat 792 verses → periodic-tile ×8 to reach 6,236.
- 14:10 — Decided periodic tiling for Muallaqat (recorded before run).
- 14:15 — Wrote scripts/h_new_43_verse_length_fft.py. AR(1) via Yule-Walker (OLS-equivalent); 10,000 surrogates; periodogram via rfft; k∈[55, 3118].
- 14:40 — Run-1 complete; initial verdict NULL (1 significant undirected peak at k=2563, 0 directed, does not meet EXPLORATORY-PASS threshold).
- 14:45 — audit-032 filed amendments 43-A (alpha_cell=1.28e-3, k=13) and 43-B (AR(1) Ljung-Box gate at lag 10, p>0.05). Both tightening-only, pre-committed before re-viewing results.
- 14:50 — Re-read pre-reg with amendments. Confirmed 43-A already the in-script value (no change). Implemented 43-B: added `ljung_box()` function, unpacked residuals from `fit_ar1`, gated verdict on LB p>0.05.
- 14:55 — Re-ran script.
- 14:58 — Final verdict: **NULL-BROKEN** (AR(1) LB p=1.35e-9, fails the gate).

## Garden-of-forking-paths log (committed BEFORE seeing results at each stage)

**Original run:**
- Per-surah demean for Quran: LOCKED in pre-reg.
- Global-mean demean for baselines (no surah structure): chosen at script-writing time. Recorded.
- Muallaqat: periodic tiling rather than zero-padding. Recorded before run.
- AR(1) null: LOCKED.
- Top-10 undirected peaks by local-maximum ranking: LOCKED.
- Directed-frequency search window ±10% of target-k (min ±3 bins): chosen at script-writing time; max-in-window null for proper search correction.

**Amendment application:**
- 43-A: was already the in-script value; no code change needed.
- 43-B: implemented exactly as specified (Ljung-Box lag 10, p>0.05 gate, no AR(2) rescue). Committed before re-running.

## Key numeric results

### Positive control (MW-5): PASS
- Injected f0=0.01, amp=0.2 sigma; detected z=33.90, p<1e-4 at alpha_cell=1.28e-3.
- Pipeline is implemented correctly.

### AR(1) fit, Quran
- phi = 0.1276, sigma_eps = 30.156.
- Ljung-Box lag-10: Q = 59.99 (df=9), **p = 1.35e-9**.
- **Fails pre-committed threshold p>0.05 → AR(1) null disqualified → NULL-BROKEN.**

### AR(1) fit, baselines (also all fail LB; expected for the tiled Muallaqat and the long prose corpora)
- Bukhari: phi=0.166, Q=1,149.83, p=8.19e-242
- Jahiz: phi=0.215, Q=693.63, p=1.62e-143
- Muallaqat (tiled): phi=0.720, Q=936.94, p=6.76e-196

### Peak tables (reported for transparency, not used for verdict)
- 0/5 directed frequencies significant at alpha_cell even under the disqualified AR(1) null.
- 1/10 top undirected peaks significant: k=2563 (period≈2.43 verses, z=7.52, p≈1e-4 under AR(1)). Not usable for verdict.
- Quran max peak amplitude 7,268 vs Bukhari max 107,186: Quran is smoother, not more periodic.

## Anomalies and choices

- Amendment 43-B is the controlling constraint. The Quran verse-length residuals carry serial correlation beyond a single lag. The decisive pre-commitment ("no post-hoc switch to AR(2)") converts what would have been a NULL verdict under AR(1) into NULL-BROKEN, reflecting that the null model itself is wrong for this signal.
- This is an honest NULL-BROKEN: the test cannot distinguish "verse-length is spectrally featureless beyond AR(1)" from "verse-length has structure but AR(1) over-rejects because residuals aren't white." A follow-up H-NEW-43.2 with a better null is the appropriate next step, separately pre-registered.
- The exploratory k=2563 peak at period≈2.43 verses is not usable under the current amended verdict. If investigated later, it requires its own pre-reg.
- No code or data from the unamended run influenced the amended analysis beyond the pre-committed LB gate addition. The script now produces deterministic results at seed=20260415 with both amendments in force.

## Files produced (final, amended)

- Script: /Users/grey/Downloads/quran/scripts/h_new_43_verse_length_fft.py
- JSON: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-43.json (now includes ljung_box_* fields, verdict_reason, amendments_applied)
- Periodogram CSV: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-43-periodogram.csv
- Findings: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-43-verse-length-fft.md

## Compliance

- MW-5 (positive control): PASS.
- MW-7 (publish NULL-BROKEN same as PASS): findings.md written with full detail.
- PRE-REG-STANDARD-04: seed, alpha_cell, alpha_bon, k_family all specified; amendments pre-committed before re-viewing.
- Bonferroni tightening vs loosening (2026-04-14 standard): amendment 43-A is self-verifying (1.28e-3 < 1.67e-3, tightening). Amendment 43-B adds a disqualification condition (tightening of what counts as a valid PASS). Both compliant.
- Ljung-Box amendment (43-B) was applied BEFORE re-inspecting the AR(1) residuals; residual values from the original run were not used to motivate any rule change.
