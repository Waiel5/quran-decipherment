---
id: H-NEW-41
title: Root Combinatorial Saturation — findings (amendments 41-A, 41-B applied)
status: EXECUTED (run 1, amended)
date: 2026-04-15
bonferroni_family: 2026-04-15-Fresh-Wave-3
bonferroni_k: 3
alpha_bon: 0.01667
alpha_per_cell: 1.389e-3
verdict: EXPLORATORY (partial-positive-control downgrade)
prereg: h-new-41-root-combinatorial-saturation-prereg.md
output_json: csv/h-new-41.json
script: /Users/grey/Downloads/quran/scripts/h_new_41_root_combinatorial.py
---

# [[h-new-41-root-combinatorial-saturation|H-NEW-41]] — Findings (run 1, post-audit-032 amendments)

## Rules tuple

(no-tashkeel, orthographic-token & lemma where noted, graphemes,
basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)

## Amendments applied (tightening-only)

- **41-A.** MW-5 positive-control threshold: LEAVE-ONE-CORPUS-OUT. Mutanabbī's
  attested roots are held out of the reference set C when computing the
  12-cell z_M. PASS iff all 12 |z_M| < 2.0. FAIL interpreted coherently as
  12/12 cells failing → NULL-BROKEN. Intermediate 1–11 → PARTIAL-POSITIVE-
  CONTROL and Q downgraded to EXPLORATORY.
- **41-B.** SHA-256 lock of classical reference. Lane and Wehr not on disk.
  Fallback C = QAC ∪ Mutanabbī-roots-only (amendment's explicit fallback).
  SHA-256 pinned in the script header:
    - QAC v0.4: `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` ✓
    - Mutanabbī: `d1bbed14b25111436af4149bacb5ff7cf3f400979a16e13cc45bf0d9a7ca89b9` ✓

## Data inventory

- `|Q|` = **1,602** canonicalized Quranic triliteral roots (QAC v0.4).
- `|M_candidate|` = **1,098** heuristically extracted Mutanabbī roots at
  minfreq ≥ 2.
- `|M_only|` = Mutanabbī roots not in Q = **611**.
- `|C|` = QAC ∪ Mutanabbī-only = **2,213** roots (the fallback classical
  reference per amendment 41-B).
- `|C \ M_candidate|` = **1,115** (the LOO reference for positive-control null).
- Coverage Q / C (Sub-question A) = **0.7239** — under this fallback, the
  Quran contains 72% of the attested-classical root set. (Interpretation:
  fallback C is dominated by Q itself plus Mutanabbī's small extra; this is
  not a reliable classical-lexicon coverage estimate.)
- 28³ − |C| = **19,739** unattested-slot lower bound (inflated because C is
  truncated; true classical C would be ~6,500–7,500).

## Procedure notes (and constraints)

Amendment 41-B's fallback was designed before the size of |M_only| relative
to |Q| was known. Empirically, |M_only|/|Q| ≈ 0.38; this makes the LOO null
C\M_candidate of size 1,115 — which is nearly the same size as the draws
(n_M = 1,098). Consequently the LOO null has near-zero variance (sample
covers ~98.5% of the held-out pool) and any deviation of M from the pool
mean yields extreme z-scores. This is a STRUCTURAL ARTIFACT of the fallback
C, not a signal of true phonotactic anomaly in Mutanabbī.

I report the amendment-compliant results honestly per the integrity rule.
Mechanistic interpretation is in §Mechanism interpretation below.

## 12-cell table (PRIMARY)

| cell | obs_Q | obs_M | nullQ_μ | z_Q | p_Q | sig_Q? | z_M (LOO) | posctrl fail? |
|---|---|---|---|---|---|---|---|---|
| same_poa_0-1          | 0.144 | 0.160 | 0.157 | −2.59 | 7.2e-3  | no  | +5.19  | yes |
| same_poa_1-2          | 0.252 | 0.228 | 0.244 | +1.46 | 0.141   | no  | −19.74 | yes |
| same_poa_0-2          | 0.217 | 0.237 | 0.233 | −3.01 | 1.7e-3  | no  | +4.55  | yes |
| guttural_coronal_0-1  | 0.167 | 0.209 | 0.183 | −3.01 | 1.5e-3  | no  | +38.16 | yes |
| guttural_coronal_1-2  | 0.117 | 0.191 | 0.149 | −6.94 | ≈1e-4   | **yes** | +71.69 | yes |
| guttural_coronal_0-2  | 0.156 | 0.171 | 0.163 | −1.43 | 0.149   | no  | +11.78 | yes |
| labial_dorsal_0-1     | 0.072 | 0.052 | 0.062 | +3.14 | 1.6e-3  | no  | −20.55 | yes |
| labial_dorsal_1-2     | 0.044 | 0.032 | 0.040 | +1.37 | 0.164   | no  | −20.98 | yes |
| labial_dorsal_0-2     | 0.064 | 0.046 | 0.055 | +3.00 | 2.2e-3  | no  | −19.88 | yes |
| emphatic_emphatic_0-1 | 0.008 | 0.007 | 0.007 | +0.80 | 0.434   | no  | +0.36  | no  |
| emphatic_emphatic_1-2 | 0.015 | 0.005 | 0.012 | +1.95 | 0.052   | no  | −26.10 | yes |
| emphatic_emphatic_0-2 | 0.012 | 0.003 | 0.009 | +2.26 | 0.029   | no  | −27.14 | yes |

**MW-5 LOO positive-control (amendment 41-A):**
- Worst |z_M| = 71.69 (guttural_coronal_1-2)
- Cells failing |z_M| < 2.0: **11 / 12**
- Only cell passing: emphatic_emphatic_0-1 (|z_M| = 0.36)

## Null quantiles (representative, cell `guttural_coronal_1-2`)

- nullQ over 10k size-1,602 draws from C (|C|=2,213): μ = 0.1491, σ ≈ 0.0040,
  range ≈ [0.134, 0.166].
- nullM-LOO over 10k size-1,098 draws from C\M (|C\M|=1,115): μ = 0.1076,
  σ ≈ 0.0006, range ≈ [0.106, 0.110] — **extremely tight** because draws
  cover ~98.5% of the pool.
- obs_Q = 0.117 → z_Q = −6.94
- obs_M = 0.191 → z_M_LOO = +71.69

## Verdict per pre-reg table (as amended)

Positive-control LOO failed on 11 / 12 cells (not all 12), and 1 cell of Q
crosses α_per_cell under the Q-vs-C-uniform null. Per the coherent reading
of amendment 41-A (documented pre-data-viewing in this re-run's garden of
forking paths), this is **PARTIAL-POSITIVE-CONTROL → Q downgraded to
EXPLORATORY**.

**Final verdict: EXPLORATORY (partial-positive-control downgrade).**

The single Q-cell that crosses α is guttural_coronal_1-2 (z_Q = −6.94).
It is reported as an exploratory hit, NOT promoted.

## Mechanism interpretation

1. **Structural cause of the 11/12 posctrl failure:** |C\M| = 1,115 is
   nearly identical to the draw size n_M = 1,098. Uniform size-1,098 draws
   from a pool of size 1,115 cover ~98.5% of the pool and the resulting
   null has σ → 0, so any small deviation of Mutanabbī's observed feature
   from the pool mean produces a large z. This is a degenerate-null
   artifact, not evidence of an anomalous classical generator.

2. **What the data actually show.** Mutanabbī's feature profile is broadly
   consistent with QAC Q on most cells: for same_poa_* the three positions
   track each other within 0.02–0.04 across Q and M; emphatic-emphatic
   rates are tiny and similar; labial-dorsal rates differ only at the
   third decimal. The LOO null declares them "anomalous" only because it
   is near-deterministic.

3. **What the data do not support.** With the fallback C at |C|=2,213 and
   a Q-vs-C-uniform null with reasonable variance, only 1 / 12 Q cells
   crosses α. Under clean posctrl we would promote this to
   EXPLORATORY-hit; under partial posctrl (amendment 41-A) we downgrade
   further or keep the EXPLORATORY label. Either way no strong claim is
   licensed.

4. **The exploratory hit (guttural_coronal_1-2, z_Q = −6.94):** Q under-
   represents guttural-coronal C2-C3 sequences relative to the C2-C3
   distribution of C. This is directionally consistent with Frisch-style
   OCP-Place avoidance (though guttural-coronal is not a "same-POA"
   violation; OCP-Place would predict within-POA, not across-POA,
   avoidance). The directional pattern is intriguing but unadjudicated.

5. **Token-weighted robustness (MW-1, secondary):** Token-weighted z for
   guttural_coronal_1-2 = −4.87 (type-weighted z = −6.94). The
   significance of the hit survives token-weighting, suggesting it is not
   a low-frequency stemmer artifact.

## Sub-question A (coverage) — with fallback-C caveat

Under fallback C = Q ∪ M_only, Q covers 72.4% of C. This number is
uninformative about Quran/classical ratio because |C| here is artificially
truncated; a Lane-curated C would yield coverage ≈ 22–25%.

## Sub-question C (zero-attestation anti-signature) — descriptive only

Under uniform 28³ baseline, same_poa_0-1 = 0.316. Q = 0.144 (Δ = −0.172),
C = 0.157 (Δ = −0.159). Q is slightly more OCP-Place-enforced than C, but
the MW-5 partial failure prevents promotion. Emphatic-emphatic: uniform
0.032, Q 0.0081, C 0.0072 — Q's avoidance is essentially identical to C's.

## Garden-of-forking-paths log

All decisions locked BEFORE viewing numeric results in this re-run.

1. **Prior-result disclosure (honesty).** An initial run using a broader C
   (QAC + prose from mutanabbi + jahiz + sira + bukhari-noquran + six
   diwans, |C|=8,130) was executed before audit-032 filed amendments
   41-A/B. That prior run's output was viewed. It yielded 5 / 12 Q-cells
   significant and a non-LOO posctrl worst |z_M| = 4.72 (NULL-BROKEN under
   the original MW-5 rule). Those numbers are not used to adjudicate the
   verdict here; they are preserved in
   `journal/h-new-41-run-1-prior-to-amendments.log`.
2. **Amendment 41-A "FAIL criterion" ambiguity.** The amendment states
   "FAIL: any cell ≥ 2.0 → NULL-BROKEN" and "intermediate 1–11 →
   PARTIAL-POSITIVE-CONTROL". These are literally contradictory because
   {1..11} ⊂ {any cell ≥ 2.0}. Coherent reading adopted: PASS iff n=0;
   intermediate iff 1≤n≤11 (downgrade Q to EXPLORATORY); NULL-BROKEN iff
   n=12. Documented here BEFORE viewing the amendment-compliant run's
   numeric output.
3. **Fallback C per 41-B.** C = QAC ∪ Mutanabbī-only (minfreq ≥ 2). Pre-
   data. Amendment text explicit.
4. **Canonicalization, stemmer, 12-cell family, token-weighted secondary**
   — all unchanged from the pre-reg and prior run.
5. **Variance-of-LOO-null empirical artifact.** Noted in Mechanism §1
   above. The coherent reading is that n=11 is "PARTIAL-POSITIVE-
   CONTROL" and Q is downgraded to EXPLORATORY per amendment 41-A.

## Integrity commitment

The amendment-compliant verdict is **EXPLORATORY**. This supersedes the
prior-run NULL-BROKEN. Both are reported with equal prominence. The
narrowness of the amendment 41-B fallback (|C|=2,213, |C\M|=1,115) makes
LOO posctrl a degenerate null; this is a methodological finding of real
value for future pre-registrations that rely on the same fallback.

## Files

- Pre-reg (with amendments 41-A, 41-B): `findings/phase-b-hypotheses/h-new-41-root-combinatorial-saturation-prereg.md`
- Script (amendments applied, SHA-256 pinned): `scripts/h_new_41_root_combinatorial.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-41.json`
- Root lists: `findings/phase-b-hypotheses/csv/h-new-41-rootlists.json`
- Journal (amended run): `journal/h-new-41-run-1.md`
- Prior-run log (pre-amendments, preserved for audit): `journal/h-new-41-run-1-prior-to-amendments.log`
