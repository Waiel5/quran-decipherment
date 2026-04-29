---
finding_id: h-new-2-iltifat-catalog-rho
phase: B
status: REVERSE-SIGN (pre-registered direction REFUTED; strong opposite-sign correlation detected)
date: 2026-04-13
rules_tuple: (no-tashkeel, orthographic-token, pronoun-surface-match, within-surah-shuffle-null)
bonferroni_k: 5
pre_registration: directions locked BEFORE join in scripts/h_new_2_iltifat_rho.py lines 9-12
depends_on:
  - H-NEW-2 per-surah z-scores (scratch/team-discovery/result-pronoun-entropy.json)
  - findings/phase-b-hypotheses/classical-iltifat-catalog.md (46 surahs, 122 events; MEDIUM classical-synthesis rigor; catalog header B1/B2-fixed per audit-028 2026-04-13)
rigor_tag: classical-synthesis-anchored  # NOT Suyūṭī-direct
unblocks: audit-013 path #3
---

# [[h-new-2-iltifat-catalog-rho|H-NEW-2]] × classical iltifāt catalog — per-surah ρ

## Pre-registered verdict

**PRE-REGISTRATION REFUTED.** All three [[h-new-2-iltifat-catalog-rho|H-NEW-2]] signals correlate with the classical catalog
at p < 0.01 **but in the opposite sign from the classical prediction.**

| Signal | Pre-reg direction | Observed ρ (n=43) | Sign match | p (two-sided) |
|---|---|---|---|---|
| z_H (chain entropy) | ρ < 0 | **+0.4266** | FAIL | 0.00253 |
| z_MI (mutual info)  | ρ > 0 | **−0.4061** | FAIL | 0.00444 |
| z_shift (shift den) | ρ < 0 | **+0.4490** | FAIL | 0.00129 |

Under the strict pre-registered audit rule (sign must match to count as PASS), this is
**FAIL on path #3 of audit-013.** [[h-new-2-iltifat-catalog-rho|H-NEW-2]]'s per-surah signal is **not explained by** the
classical iltifāt catalog in the direction classical doctrine predicts.

But the null hypothesis of "no correlation" is strongly rejected. A substantive
**opposite-sign** structural relationship is present.

## Interpretation

All three signals agree on the reversal:
- Higher classical iltifāt density → *higher* (less negative) z_H (entropy closer to null)
- Higher classical iltifāt density → *lower* (less positive) z_MI (MI closer to null)
- Higher classical iltifāt density → *higher* (less negative) z_shift (shifts closer to null)

i.e., **surahs with more classically-flagged iltifāt events show WEAKER pronoun-chain
signature extremity in [[h-new-2-iltifat-catalog-rho|H-NEW-2]]**, not stronger.

Two candidate mechanisms (both publishable as [[h-new-2-iltifat-catalog-rho|H-NEW-2]]-EXT hypotheses, neither claimed
here as confirmed):

1. **Conspicuous-vs-diffuse iltifāt.** Classical scholars flag the *rhetorically conspicuous*
   iltifāt instances (narrative and legal peaks — person-shifts with commentator-quotable
   force). The [[h-new-2-iltifat-catalog-rho|H-NEW-2]] residual signal instead captures *diffuse systemic* pronoun-machinery
   distributed across all 73 surahs tested. The conspicuous events are a small subset of
   the total shift-machinery, so surahs with many *conspicuous* events don't have
   systematically more *total* pronoun-residual extremity.

2. **Short-surah saturation.** Catalog coverage skews to long Medinan surahs (density
   diluted by large N_verses), while [[h-new-2-iltifat-catalog-rho|H-NEW-2]]'s z-scores are power-law magnitude-dependent
   on n_pronouns. A longer surah with n=1800 pronouns gets a much larger |z| than a
   short surah with n=50, independently of iltifāt density. Residualizing on log(n_pronouns)
   before ρ would disentangle this.

Either mechanism would explain the clean sign reversal; distinguishing them requires a
follow-up computation.

## Numbers

### Primary (n=43 catalog ∩ [[h-new-2-iltifat-catalog-rho|H-NEW-2]] tested)

- ρ(density, z_H)     = +0.4266  (p₂ = 0.00253)
- ρ(density, z_MI)    = −0.4061  (p₂ = 0.00444)
- ρ(density, z_shift) = +0.4490  (p₂ = 0.00129)

None satisfy Bonferroni α = 0.01 / k=5 in the pre-registered direction (all sign-mismatched
→ one-sided p in pre-registered direction > 0.99, Bonferroni-corrected p = 1).

**Catalog surahs excluded (not in [[h-new-2-iltifat-catalog-rho|H-NEW-2]] tested set, n=3):** 5, 9, 13. ([[h-new-2-iltifat-catalog-rho|H-NEW-2]]
tested 73 surahs, the 41 short-late surahs with too few pronouns were dropped pre-registered
at the [[h-new-2-iltifat-catalog-rho|H-NEW-2]] level.)

### Sensitivity: drop syn-only entries (n=25, retains Z+S / Z / S-flagged entries)

- ρ(density, z_H)     = +0.4901  (p₂ = 0.007)
- ρ(density, z_MI)    = −0.4774  (p₂ = 0.0092)
- ρ(density, z_shift) = +0.5309  (p₂ = 0.0027)

**The effect STRENGTHENS on the high-rigor subset.** This makes the "catalog-quality
artifact" explanation less plausible — dropping the shakiest 18 syn-only entries
increases |ρ|, not decreases it.

### Sensitivity: Z+S-strict both-sources-flagged (n=10)

- ρ = +0.406, −0.406, +0.491 (underpowered n=10; p₂ ≈ 0.1-0.2)

Directionally consistent but not significant. n too small.

## Pre-registered sign rule and garden-of-forking-paths

The direction was committed BEFORE looking at the join, in the script source at lines 9-12:

```
z_H      (chain entropy)  → ρ < 0
z_MI     (mutual info)    → ρ > 0
z_shift  (shift density)  → ρ < 0
```

The direction derivation: classical doctrine says iltifāt serves *tansheeṭ al-sāmiʿ*
(engaging the listener by rhetorical shift). If [[h-new-2-iltifat-catalog-rho|H-NEW-2]]'s signal measures the same
underlying phenomenon, per-surah magnitudes should track. [[h-new-2-iltifat-catalog-rho|H-NEW-2]] reports all three
signals' signs in its global finding: z_H<0 (entropy below null), z_MI>0 (MI above null),
z_shift<0 (shifts below null). So the sign rule is: per-surah catalog count should
correlate with the *direction-of-signature* in each signal, which means ρ(density, z_H)<0,
ρ(density, z_MI)>0, ρ(density, z_shift)<0.

No post-hoc switching: the sign-match test was run by the same script that produced the
numbers.

## Implication for [[h-new-2-iltifat-catalog-rho|H-NEW-2]]

[[h-new-2-iltifat-catalog-rho|H-NEW-2]] remains a strong Quran-wide pronoun-chain signature (|Stouffer z| ≈ 77-79
across three signals). What this test adjudicates is: **the per-surah distribution of
that signature is NOT explained by the classical iltifāt catalog in the direction
classical doctrine predicts.** Either (a) the catalog isn't the right ground truth
(conspicuous vs. diffuse), (b) the signal captures something orthogonal to iltifāt
that happens to be systemic at the Quran-wide level, or (c) both.

The test does **not** disconfirm [[h-new-2-iltifat-catalog-rho|H-NEW-2]]'s main finding. It disconfirms the narrow
classical-reduction claim that the per-surah pattern reflects flagged-iltifāt density.

## Caveats

- **Catalog rigor is MEDIUM**, not HIGH. See classical-iltifat-catalog.md retag memo:
  nawʿ numbers PENDING physical verification, `syn` tag entries are synthesis-inferred.
  Primary uses all 45 entries; drop-syn sensitivity confirms effect on Z+S+S+Z subset.
- **43 out of 45 catalog surahs** intersect [[h-new-2-iltifat-catalog-rho|H-NEW-2]]'s 73-surah tested set. 3 dropped
  (5, 9, 13).
- **[[h-new-2-iltifat-catalog-rho|H-NEW-2]] itself tested only 73 surahs** (not all 114); shorter surahs insufficient
  n_pronouns. This limits external validity for the full 114-surah catalog.
- **Classical catalog is surah-aggregated, not verse-aggregated.** A verse-level
  iltifāt-marker × pronoun-chain-residual correlation would be a stronger test; requires
  a per-verse catalog not currently available.
- **Density normalization by N_verses assumes uniform opportunity.** A surah with
  mostly short verses has more iltifāt opportunities per character than a surah with
  long verses — this may be partial confound.

## Reproducibility

- Script: scripts/h_new_2_iltifat_rho.py
- Output: findings/phase-b-hypotheses/csv/h-new-2-iltifat-rho.json
- Seed-dependent inputs: [[h-new-2-iltifat-catalog-rho|H-NEW-2]] used seed 20260413 (1000 within-surah permutations)
- Catalog frozen: findings/phase-b-hypotheses/classical-iltifat-catalog.md (2026-04-12 retag)

## Follow-ups queued (not claimed as findings here)

- **[[h-new-2-iltifat-catalog-rho|H-NEW-2]]-EXT-A:** log(n_pronouns) residualization before ρ — disentangle saturation confound
- **[[h-new-2-iltifat-catalog-rho|H-NEW-2]]-EXT-B:** verse-level catalog × verse-level pronoun-chain residual — stronger test
- **[[h-new-2-iltifat-catalog-rho|H-NEW-2]]-EXT-C:** conspicuous-vs-diffuse iltifāt classifier — test mechanism (1) explicitly
