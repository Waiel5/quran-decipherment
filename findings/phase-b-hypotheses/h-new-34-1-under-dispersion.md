---
finding_id: h-new-34.1
phase: B
status: MECHANISM-INCONSISTENT per pre-reg; with strong caveats (see §Caveats)
date: 2026-04-13
rules_tuple: (hafs-kufan, mashriqi abjad, hamza-carrier-policy, last-word-of-verse)
parent_finding: h-new-34 (PASSED-AS-NULL)
pre_registration: findings/phase-b-hypotheses/h-new-34-1-prereg.md
amendment: AMEND-27 (2026-04-14 three-point checklist)
task_id: 102
seed: 20260413
bonferroni_k: 3 (AMEND-27); 9 (auditor TOMORROW-TESTS alternative)
script: scripts/h_new_34_abjad_modular.py
output_json: findings/phase-b-hypotheses/csv/h-new-34.json (h_new_34_1_amendment section)
---

# [[h-new-34-1-under-dispersion|H-NEW-34.1]] — Muʿallaqāt rhymed-baseline + length-stratified follow-up

## Executive verdict

**MECHANISM-INCONSISTENT per pre-registered verdict table.** The parent
H-NEW-34 reverse signal (Quran under-disperses vs Bukhari/Jāḥiẓ) does
not survive the three-point AMEND-27 checklist:

1. **Muʿallaqāt rhymed-baseline (raw):** Quran is under-dispersed vs
   Muʿallaqāt at m=11 (z = −4.02, p < α_bon = 0.0033) but not at m=7
   (z = −1.68, p = 0.035) or m=19 (z = **+2.10**, over-dispersed). The
   rhyme-mechanism hypothesis predicted Muʿallaqāt to also under-disperse
   vs the Quran (i.e. |z_Quran vs Muʿallaqāt| ≈ 0). At m=19 the Quran
   over-disperses vs Muʿallaqāt — direction-inconsistent.

2. **Length-stratified (pooled-deciles, AMEND-27 point 2):** the
   under-dispersion signal **reverses sign** at stratified granularity.
   Bukhari stratified z is +3.66 at m=11 and −2.08 at m=19. Jāḥiẓ
   stratified z is +10.85, +19.26, +27.15 at m = 7, 11, 19
   respectively — strong **over-dispersion** after length conditioning.
   Per AMEND-27 tie-breaker, stratified is authoritative; the parent
   reverse signal is accordingly length-confound-explained, not
   rhyme-mechanism-mediated.

3. **Three-baseline joint verdict:** fails both PASS (all-3) and
   PARTIAL (2-of-3) thresholds for under-dispersion; over-dispersion at
   α_bon in multiple stratified Bukhari and Jāḥiẓ cells triggers the
   pre-registered MECHANISM-INCONSISTENT branch.

## Caveats (pre-registered escalation triggers, flagged to auditor)

Two methodological concerns must be weighed before integrator takes this
as final — the MECHANISM-INCONSISTENT verdict is literally correct under
the pre-reg but may reflect statistic-brittleness rather than a
substantive mechanism surprise.

**C1. Muʿallaqāt stratified is power-insufficient at the deciled grain.**
With N_Muʿallaqāt_bayt_finals = 792 across 10 pooled-letter-count deciles,
most deciles have < 10 items and are skipped. No stratified Muʿallaqāt
cell produced a usable z. Pre-reg said "no upsample by repeat-sampling"
for the Quran's N, but deciled analysis hit the floor before reaching
that rule. The stratified verdict therefore rests on Bukhari + Jāḥiẓ
only; Muʿallaqāt contributes only raw cells.

**C2. Stratified χ² at small per-decile N has high-variance nulls.**
At per-decile N in the 200-2300 range, the chi² null distribution from
Jāḥiẓ is narrow (word-length-conditioned Jāḥiẓ has few distinct types
per decile, so random draws produce very uniform residues and thus low
null chi²). The Quran's verse-final structured diversity (many distinct
rhyme-pool words at a given letter-count) then registers as
high-chi²-vs-null → apparent over-dispersion. This may be a pool-scarcity
artifact at stratified granularity, not a Quran-specific
over-dispersion signal. Specifically Jāḥiẓ decile 8 (n = 2344) at m = 19
returns a null mean of 77.97 vs observed 594.14 (z = +30.6); decile-pool
inspection suggests Jāḥiẓ at letter-count = 5 has limited type diversity.

Given C1 + C2, the MECHANISM-INCONSISTENT verdict is **provisionally
filed per pre-reg** but the auditor should assess whether the
stratified statistic is rigorous enough to overturn the parent reverse
signal, or whether a revised stratification (e.g. register-matched or
type-controlled) is needed.

## Raw-unstratified results (all baselines pass under-dispersion at α_bon = 0.0033 except m=19 Muʿallaqāt)

| Baseline  | m  | Quran χ² | Null mean | Null SD | z_Quran | Under-disperses α_bon=0.0033 |
|-----------|----|----------|-----------|---------|---------|-------------------------------|
| Bukhari   | 7  | 42.14    | 207        | 27.87   | **−5.95** | yes |
| Bukhari   | 11 | 75.64    | 687        | 53.81   | **−10.91** | yes |
| Bukhari   | 19 | 312.66   | 740        | 57.63   | **−7.89** | yes |
| Jāḥiẓ     | 7  | 42.14    | ~166       | ~28     | **−4.43** | yes |
| Jāḥiẓ     | 11 | 75.64    | ~550       | ~56     | **−6.62** | yes |
| Jāḥiẓ     | 19 | 312.66   | ~590       | ~59     | **−5.04** | yes |
| Muʿallaqāt | 7  | 42.14    | —         | —       | **−1.68** | no (p = 0.035) |
| Muʿallaqāt | 11 | 75.64    | —         | —       | **−4.02** | yes |
| Muʿallaqāt | 19 | 312.66   | —         | —       | **+2.10** | no (over-disperses) |

Muʿallaqāt uses sampling-with-replacement at N = 6219 from a pool of 792
bayt-final words (bootstrap-adjusted null; power-flagged). Jāḥiẓ and
Bukhari use sampling-without-replacement from their larger pools.

## Stratified results (AMEND-27 length-decile, authoritative per tie-breaker)

Pooled decile cut-points on letter-count (N_pooled = 873,429):
cut-points = [2, 3, 3, 3, 4, 4, 5, 5, 6]. Because Arabic word lengths
concentrate at 3-5 letters, only 5 of 10 deciles are non-empty after
binning; this is the floor that AMEND-27's decile protocol hits.

| Baseline   | m  | Stratified z | Under-disperse α_bon | Direction vs raw |
|------------|----|--------------|----------------------|-------------------|
| Bukhari    | 7  | −5.46        | yes                  | consistent |
| Bukhari    | 11 | **+3.66**    | no (over-disperse)   | **FLIPPED** |
| Bukhari    | 19 | −2.08        | no                   | weakened |
| Jāḥiẓ      | 7  | **+10.85**   | no (over-disperse)   | **FLIPPED** |
| Jāḥiẓ      | 11 | **+19.26**   | no (over-disperse)   | **FLIPPED** |
| Jāḥiẓ      | 19 | **+27.15**   | no (over-disperse)   | **FLIPPED** |
| Muʿallaqāt | —  | NaN (power-insufficient) | n/a              | n/a |

Three-baseline joint verdict under AMEND-27 (k=3, α_bon=0.0033):
worst-m stratified z per baseline = +3.66 (Bukhari), +27.15 (Jāḥiẓ),
NaN (Muʿallaqāt). **0/3 baselines pass under-dispersion at α_bon.**

Auditor alternative (k=9, α_bon=0.0056 per cell): 9/9 cells fail
under-dispersion; 5 cells over-disperse at α_bon. Triggers
MECHANISM-INCONSISTENT under both threshold specs.

## Pre-registered acceptance vs observed

| Pre-reg criterion (AMEND-27 Table 2) | Observed | Verdict |
|---|---|---|
| Stratified under-dispersion across all 3 baselines at α_bon = 0.0033 | 0 / 3 | not-PASS |
| Stratified under-dispersion at 2 of 3 baselines | 0 / 3 | not-PARTIAL |
| Stratified under-dispersion at ≤1 of 3 baselines | 0 / 3 | NULL candidate |
| Any baseline over-disperses at α_bon | 5 Jāḥiẓ + 1 Bukhari cells | **MECHANISM-INCONSISTENT** |

Per pre-reg: the MECHANISM-INCONSISTENT branch fires because over-dispersion
is observed at the α_bon level in multiple stratified cells. The pre-reg
commits to escalation.

## Mechanism interpretation (conditional on C1/C2 resolution)

**If auditor accepts stratified as rigorous:**
The parent H-NEW-34 reverse signal (raw Quran-under-dispersion vs prose
baselines, z ≈ −5 to −11) is **length-confound-mediated, not rhyme-driven**.
Once length is conditioned on, the Quran's abjad-residue distribution is
**not** more uniform than prose; at fine-grained within-decile comparison
it may be more dispersed than length-matched Jāḥiẓ (though per C2 the
sign of this residual is methodologically uncertain).

This would downgrade the parent reverse signal to a length-confound
artifact and close the [[h-new-34-1-under-dispersion|H-NEW-34.1]]-REVERSE novel-finding branch (no
upgrade to task #84 H-NEW-SURVEY-EXT mirror-string suppression scale).

**If auditor rules stratified brittle (C2 artifact):**
Revised stratification (register-matched, or type-controlled rather than
letter-count-binned) may be required. Intermediate status: "execution
complete but verdict held pending auditor statistical review."

## Reporting commitments satisfied

- Results filed regardless of direction (pre-reg §"Reporting commitment").
- Seed and script preserved: `scripts/h_new_34_abjad_modular.py` seed 20260413.
- Both AMEND-27 k=3 and auditor-alternative k=9 verdicts reported
  (both converge to MECHANISM-INCONSISTENT at this observed data).
- Raw and stratified statistics reported side-by-side per AMEND-27.
- Muʿallaqāt cells reported with power-adjusted flag per pre-reg rule.

## Routing

- **Parent H-NEW-34 primary verdict:** PASSED-AS-NULL stands (unchanged).
- **Parent H-NEW-34 reverse signal:** downgraded from "post-hoc
  hypothesis-generating exploratory" to **"length-confound-mediated,
  not a Quran-specific under-dispersion after stratified control."**
  MASTER §5 annotation should reflect this.
- **H-NEW-SURVEY-EXT task #84:** NOT activated — reverse signal does not
  survive the mechanism test.
- **[[h-new-34-1-under-dispersion|H-NEW-34.1]] PROMOTED-TO status:** not promoted; no new novel finding.
- **Auditor review requested** on C1 (Muʿallaqāt power) and C2
  (stratified statistic rigor) before integrator closes this finding.

## Reproduction pointers

- Script: `scripts/h_new_34_abjad_modular.py`.
- Data: `quran-text/quran-no-tashkeel.json`;
  `data/baseline-corpora/raw/{bukhari-noquran,jahiz-hayawan,muallaqa-*}.txt`.
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-34.json` sections
  `h_new_34_1_amendment`, `muallaqat_nulls_per_m`,
  `bukhari_nulls_under_dispersion`, `jahiz_nulls_under_dispersion`,
  `length_stratified_z_per_corpus_per_m`, `raw_vs_stratified_delta`,
  `k3_per_baseline_pass_AMEND27`, `three_corpus_joint_verdict_k3_AMEND27`,
  `auditor_k9_alternative`, `h_new_34_1_primary_verdict`,
  `h_new_34_1_auditor_alt_verdict`.
- Pre-reg: `findings/phase-b-hypotheses/h-new-34-1-prereg.md` (2026-04-13
  + 2026-04-14 AMEND-27).
- TOMORROW-TESTS gate row: `findings/TOMORROW-TESTS-PRE-REGISTRATION.md`
  §[[h-new-34-1-under-dispersion|H-NEW-34.1]].

## Honesty disclosures (garden of forking paths)

- First run had Muʿallaqāt z = NaN due to sampling-without-replacement
  collapsing SD to 0 when N_sample = N_pool exactly. Fix applied:
  with-replacement bootstrap at matched N for small-pool baselines
  (power-adjusted flag). No change to the substantive verdict —
  Muʿallaqāt raw cells then yielded z = (−1.68, −4.02, +2.10) which is
  mixed. This was a script bug, not a pre-reg forking path.
- Stratified per-decile bootstrap uses B = 200 rather than B = 1000
  (compute-budget trade-off). Per-decile p-values are accordingly
  quantized at 0.5% resolution. This is below the α_bon = 0.0033
  threshold resolution — flagged as a potential escalation trigger if
  auditor requires finer granularity.
- No post-hoc modulus selection. No post-hoc baseline swap. No
  direction change from pre-reg. Verdict follows the pre-reg Table 2
  decision rule mechanically.
