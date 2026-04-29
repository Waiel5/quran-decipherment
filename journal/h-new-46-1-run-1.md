---
journal_entry: h-new-46-1-run-1
date: 2026-04-15
agent: h-new-46-1-specialist
parent_finding: H-NEW-46
pre_reg: findings/phase-b-hypotheses/h-new-46-1-chronology-disentangle-prereg.md
script: scripts/h_new_46_1_chronology_disentangle.py
json: findings/phase-b-hypotheses/csv/h-new-46-1.json
findings: findings/phase-b-hypotheses/h-new-46-1-chronology-disentangle.md
seed: 20260416
n_perm: 100000
chronology_source: Tanzil Egyptian Standard (data/revelation-order.csv)
---

# Journal — H-NEW-46.1 run 1

## Origin

Tasked to disentangle H-NEW-46's STRONG-PASS finding (4/4 Bonferroni-4 length cells, p ≤ 1.6×10⁻⁴) from the dominant nuisance hypothesis: chronology. The H-NEW-46 paper itself listed "chronological correlate (most plausible)" as mechanism #1; this run is the locked test of that mechanism.

## Chronology source choice (LOCKED before computation)

Two candidate sources reviewed BEFORE any computation:

1. **Tanzil Egyptian Standard** (`data/revelation-order.csv`): already in repo; has both `period` (Meccan/Medinan) and `noldeke_order` columns. Period column uses the Egyptian-edition consensus 86/28 split.
2. **al-Suyūṭī al-Itqān fī ʿulūm al-Qurʾān, nawʿ 9** (`data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`): this is the canonical classical text on Meccan/Medinan classification.

Tanzil's `period` column matches al-Itqān nawʿ 9 standard split for nearly every surah; the small set of debated cases (Q 13, Q 47, Q 55, Q 76, Q 99 in some renderings) follow Tanzil/Egyptian-edition consensus. Since Tanzil is already the project's reference and aligns with al-Itqān, **locked: Tanzil's period field as the canonical chronology source**, with Q 13 = Medinan being the only borderline pre-disclosed for sensitivity analysis.

The chronology-source choice was locked into the pre-reg under §"Chronology source — locked" before the script was executed.

## Locked muqaṭṭaʿāt-by-period (pre-computation)

Computed by intersecting the 29-element muq set with Tanzil's period column:
- 26 muq are Meccan: {7, 10, 11, 12, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
- 3 muq are Medinan: {2, 3, 13}

This 26/3 split was visible from a 5-line python check before the test design. The pre-reg's 7-cell design accommodated the small Medinan-stratum n by including exact enumeration (B1, B2) rather than relying on permutation alone.

## Pipeline

1. Load verse counts via `analysis.tools.loader.load_quran('no-tashkeel')` and chronology via `data/revelation-order.csv`.
2. MW-7 internal-error gate: confirm muq-Meccan + muq-Medinan = 29; manually recompute means (85.15 and 176.33). PASS.
3. MW-5 positive controls:
   - PC-A1: plant 26 longest Meccan as fake-muq → A1 p = 1.0×10⁻⁴ (floor). PASS.
   - PC-B1: plant 3 longest Medinan as fake-muq → B1 p = 3.05×10⁻⁴ (= 1/C(28,3) combinatorial floor). PASS.
4. Run all 7 cells in sequence.
5. Compute verdict + write JSON.

Total runtime: ~3 seconds (10⁵ perms for cells A1/A2/C1-perm/C3; exact enum for B1/B2; analytic for C1, C2).

## Results

| Cell | Direction | Obs | Null mean | Null SD | p | sig at α_bon=0.00714 |
|---|---|---|---|---|---|---|
| A1 mecca-mean | upper | 85.15 | 53.67 | 7.81 | 4.0×10⁻⁵ | YES |
| A2 mecca-top26 | upper | 15/26 | 7.86 | 1.97 | 4.0×10⁻⁴ | YES |
| B1 medina-mean (exact) | upper | 176.33 | 57.96 | 37.21 | 4.9×10⁻³ | YES |
| B2 medina-top3 (exact) | upper | 2/3 | 0.32 | 0.52 | 2.3×10⁻² | NO |
| C1 stratified-MW (van Elteren) | two-sided | z=4.82 | — | — | 1.0×10⁻⁵ | YES |
| C2 OLS muq-coef (HC1) | n/a | β=+56.42 | — | — | 2.1×10⁻⁵ | YES |
| C3 period-residualized perm | upper | 40.50 | -0.02 | 8.55 | 1.0×10⁻⁵ | YES |

**n_sig = 6/7. VERDICT: STRONG-PASS.**

## Headline OLS

`verse_count = 25.74 + 44.46·I(Medinan) + 56.42·I(muqaṭṭaʿāt) + ε`, R² = 0.208.

The muqaṭṭaʿāt coefficient (+56.4 verses) is essentially identical to the unstratified gross gap (53.5 verses). Chronology absorbs ~0% of the muq-length signal.

Both classical-t (p < 10⁻⁶) and HC1-robust (p = 2.1×10⁻⁵) clear α_bon = 0.00714 by 100×–10⁴×. Headline (max conservative) = 2.1×10⁻⁵.

## Why B2 is the only failure

The B2 cell (Medinan top-3 count) has only 3 observations and 1 of them (Q 13 al-Raʿd, 43 verses) is much shorter than Q 2 and Q 3. Under exact enumeration of C(28,3) = 3276, observing 2-of-3 in the top-3 has p = 0.0232. This is significant at uncorrected α=0.05 but fails Bonferroni-7.

The B2 NULL is a tiny-n resolution problem, not a substantive contradiction. Companion cell B1 (Medinan mean, same data, continuous variable) gives p = 0.0049, well within α_bon. The combined cells C1, C2, C3 all clear α_bon by margins of 200× to 700×.

I publish B2 as NULL per the pre-reg's "publish PASS/NULL identically" rule, NOT as a downgrade. The final verdict 6/7 falls in the STRONG-PASS band (6-7 cells, OLS coef positive and significant).

## Q 13 sensitivity

Pre-disclosed sensitivity check: if Q 13 is reclassified as Meccan (Nöldeke's view) instead of Medinan (Tanzil/Egyptian-edition consensus):
- muq-Meccan becomes 27, muq-Medinan becomes 2
- muq-Meccan mean shifts from 85.15 → 83.59 (Q 13's 43 verses pulls mean down)
- muq-Medinan mean shifts from 176.33 → 243.00 (only Q 2 + Q 3 remain)
- Signal direction unchanged in both strata; OLS coefficient virtually unaffected

Locked answer remains Tanzil's classification. Sensitivity confirms robustness.

## Effect-size sanity

- Cell A1: z = (85.15 − 53.67) / 7.81 ≈ +4.03. ~4 SD above null mean within Meccan only.
- Cell C3: z ≈ 4.74. The within-period residual mean for muq is +40 verses, vs null SD of 8.5.
- Cell C2: t-statistic for muq coef under classical SE = 4.92, under HC1 = 4.43. Both extreme.
- The within-Meccan effect (+45 verses, muq mean − non-muq mean = 85.15 − 39.97) is the bulk of the signal; the 3-Medinan stratum amplifies it via two of the all-time longest surahs.

## Garden-of-forking-paths integrity check

- Chronology source choice was made BEFORE any per-cell computation. Documented in pre-reg.
- 7-cell test family declared in pre-reg before null ran. Bonferroni k=7 declared.
- Q 13 sensitivity disclosed in pre-reg, not as a verdict-altering rerun.
- B2 NULL is published transparently; not absorbed into a "we noticed it failed and dropped it" maneuver.
- The 6/7 verdict band was pre-defined; observing exactly 6 of 7 sig is not a post-hoc threshold tweak.

## Bonferroni accounting

- Family: **2026-04-16-Wave-Muqattaat-Extended-Disentangle**, separate from H-NEW-46's family to avoid double-counting.
- k = 7, α_bon = 0.05/7 ≈ 0.00714.
- 6 of 7 cell p-values clear α_bon, by margins of 1.4× (B1 cell, p = 4.9e-3 vs threshold 7.1e-3) up to 700× (C1, C3, p = 1×10⁻⁵).
- If we did combined family-wise tightening across H-NEW-44 + 45 + 46 + 46.1 (k = 6+8+4+7 = 25, α = 0.002), 5 of 7 cells would still pass (only B1 at p=4.9e-3 and B2 at p=2.3e-2 would fall out). Per project rule (feedback_bonferroni_tightening_vs_loosening), tightening is self-verifying. Headline finding is robust.

## Reproducibility

- Seed: 20260416 (matches H-NEW-45/46 wave for cross-comparability)
- N_PERM: 100,000 for permutation-based cells; exact for B1, B2
- Loader: `analysis.tools.loader.load_quran('no-tashkeel')`
- Chronology: `data/revelation-order.csv` (Tanzil Egyptian Standard)
- Pre-reg SHA-256 captured into JSON output as `prereg_sha256`
- Script: `scripts/h_new_46_1_chronology_disentangle.py` (~370 LOC, pure-Python; no numpy/scipy dependency)
- All output written to JSON before findings.md was drafted

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-46-1-chronology-disentangle-prereg.md`
- Findings: `findings/phase-b-hypotheses/h-new-46-1-chronology-disentangle.md`
- JSON: `findings/phase-b-hypotheses/csv/h-new-46-1.json`
- Script: `scripts/h_new_46_1_chronology_disentangle.py`

## Cross-finding context update

Four-axis muqaṭṭaʿāt structural finding cluster after this run:
- Axis 1 (subset algebra, H-NEW-44): rank-12, two Boolean decompositions
- Axis 2 (surah-position, H-NEW-45): gap-entropy clustering at p = 2×10⁻⁵
- Axis 3 (gross length, H-NEW-46): 4/4 cells STRONG-PASS at p ≤ 1.6×10⁻⁴
- Axis 4 (period-controlled length, H-NEW-46.1): 6/7 cells STRONG-PASS; OLS β_muq = +56.4 verses, p_HC1 = 2.1×10⁻⁵

The chronology disentanglement was the single most plausible nuisance hypothesis for axis 3. It is now ruled out. The classical traditions (al-Rāzī's 12 theories of muqaṭṭaʿāt, Welch 1986, Massey 1996, Nöldeke 1919) generally do not anticipate a length-dimension to muqaṭṭaʿāt assignment. This finding contributes a new structural axis that classical theory must accommodate.
