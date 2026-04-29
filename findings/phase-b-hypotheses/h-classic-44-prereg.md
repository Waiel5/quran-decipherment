---
finding_id: h-classic-44
phase: B
status: PRE-REGISTERED — computational-tester self-pre-reg per PRE-REG-STANDARD-04 + STANDARD-05
pre_registered_by: computational-tester (2026-04-14)
registration_date: 2026-04-14
parent_task: #95
spec_source: |
  findings/phase-b-hypotheses/h-classic-44-to-49-spec.md §H-CLASSIC-44 +
  task #95 description with meta-analyst local-vs-distant regime cut
  and transitive-prior confirmation (2026-04-13 update)
distinct_from: |
  task #21 / T-002 (adjacent-pair seam-Jaccard at d=1 only, z=+10.06) —
  H-CLASSIC-44 tests the **distance-decay** claim AND the regime-cut.
  Sub-test B (local-pairwise d=1) is a deliberate re-test of the T-002
  regime using a compound (J + gzip Δ) score; sub-test A (macro) tests
  the strictly stronger distance-gradient claim; sub-test C (regime-
  discrimination) explicitly measures the d=1 vs d=11+ contrast.
rules_tuple: (no-tashkeel, root-level via QAC, hafs-kufan, mashriqi)
seed: 20260414
sided_test: one-sided (all three sub-tests predict scores higher at low d / lower at high d)
direction_prereg_source: |
  al-Zarkashī Burhān, nawʿ munāsabāt al-suwar (nawʿ number PENDING
  physical verify); seconded by al-Biqāʿī Naẓm al-Durar fī tanāsub
  al-āyāt wa-l-suwar; further seconded by Nöldeke chronology implying
  adjacency = temporal clustering
regime_declaration: |
  H-CLASSIC-44 is a MACRO-ARCHITECTURAL test (between-surah, scope =
  whole canonical mushaf). It sits in the regime where al-Biqāʿī
  tradition has been REFUTED at z = −2.51 (H-META-1 convergence audit,
  macro-ring leg). A NULL on sub-test A would CONFIRM the regime cut;
  a POSITIVE on sub-test A would be a NOVEL finding — partial recovery
  of the macro-architectural regime against the prior null.
h_meta_1_prior: macro-regime-refuted-z-minus-2.51-local-pairwise-confirmed-z-plus-10.06
transitive_prior_status: |
  CONFIRMED-by-meta-analyst-2026-04-14-regime-level-not-author-level.
  H-CLASSIC-44 inherits the al-Biqāʿī macro-regime prior because the
  H-META-1 classifier learned a regime-level signature, not an
  author-level one. al-Zarkashī's munāsabāt al-suwar sits in the macro-
  architectural regime and inherits the prior regardless of attribution.
z_prior_source: "task #21 / task #50 al-Biqāʿī macro-ring direct test (NOT H-META-1 classifier score); z=−2.51 invariant to H-META-1 retrain"
bonferroni_k_wave: 6
bonferroni_family_wave: wave-1-3-six-families
bonferroni_k_outer: 6
bonferroni_family_outer: h-classic-44-49
bonferroni_k_inner: 3
bonferroni_family_inner: h-classic-44
parent_dispatch: 2026-04-14-wave-1-3-meta-analyst
families_in_dispatch: 6
alpha_unadjusted_dispatch: 0.05
alpha_after_wave_correction: 0.00833
alpha_after_family_correction: 0.001389
alpha_bon: 0.000463
alpha_bon_derivation: "0.05 / 6 (Wave 1-3 families) / 6 (H-CLASSIC-44-49 inner family) / 3 (A/B/C sub-tests) = 0.05/108 = 0.000463"
correction_origin: "team-lead approval message 2026-04-14 — triple-nested hierarchical Bonferroni per hypothesis-generator Wave 1-3 backfill"
internal_k: 3
null_publishable: true
positive_publishable: true
---

# H-CLASSIC-44 — al-Zarkashī canonical-distance-decay of inter-surah munāsaba (3-sub-test regime-cut)

## Pre-execution disclosure — pre-pilot single-test run preceded this pre-reg

A single-test version of this hypothesis (α=0.0083, not sub-test-split)
was authored, scripted, and run on 2026-04-14 BEFORE I discovered the
task #95 description had been updated with the regime-cut stratification
and PRE-REG-STANDARD-05 hierarchical Bonferroni. That pre-pilot result
is saved to `scratch/h_classic_44_pre_pilot/h-classic-44-pre-pilot-single-test.json`
for provenance and disclosed here:

- Single-test primary Spearman ρ = −1.0000, p_emp = 0.0062 (PASSED at
  obsolete single-test α=0.0083, would FAIL at hierarchical α=0.000463)
- Secondary-strong (d=1 vs d=11+ 99pct under permutation): PASSED
- Tertiary (muqaṭṭaʿāt-adj excluded): ρ = −0.700, p = 0.108 → FAILED
- Old-spec verdict: PARTIAL-MUQATTAAT-DRIVEN

The pre-pilot run is **NOT used** as the verdict. This pre-reg supersedes
it. The compliant 3-sub-test hierarchical-Bonferroni verdict run uses
the SAME seed (20260414) and the SAME scoring machinery (it is a
re-analysis of the same score matrix under the 3-sub-test decomposition,
not fresh data). I am disclosing the pre-pilot because:
1. It influences my priors (I expect the regime-cut to fire)
2. Skeptical-auditor will want to see that the compliant verdict run's
   parameters were not tuned from the pre-pilot
3. Garden-of-forking-paths transparency — the pre-pilot told me
   muqaṭṭaʿāt-adjacency dominates d=1; I did NOT change the locked
   muqaṭṭaʿāt set or any other pre-reg parameter in response.

The pre-pilot's muqaṭṭaʿāt-tertiary result informs my EXPECTED verdict
cell (PASS-LOCAL-ONLY with muqaṭṭaʿāt-exclusion caveat) but I have NOT
reshaped the acceptance matrix, score weights, or bucket edges post-hoc.

## Why this pre-registration exists

al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān* (nawʿ on *munāsabāt al-āyāt
wa-l-suwar*, likely nawʿ 13 — PENDING physical edition verify) argues
the canonical mushaf ordering is not arbitrary: adjacent surah-pairs
(d=1) exhibit greater thematic/lexical coherence than non-adjacent
pairs, with monotone decay as canonical distance grows.

Per the meta-analyst 2026-04-14 regime-cut analysis, the al-Biqāʿī
tradition shows a clean regime split:
- **Local-pairwise** (verse-pair / adjacent-surah seam): CONFIRMED at
  z = +10.06 (T-002)
- **Macro-ring / architectural** (full-mushaf geometry): REFUTED at
  z = −2.51

al-Zarkashī's munāsabāt al-suwar is the source that al-Biqāʿī later
systematized in *Naẓm al-Durar*; the transitive regime prior applies.
A single distance-decay test would be mis-scoped. The 3-sub-test split
explicitly separates the two regime sub-claims.

## Pre-registered hypotheses

### Sub-test A — Macro-architectural distance-decay (macro regime)

**H-CLASSIC-44-A (locked, one-sided):** Spearman ρ between canonical-
distance-bucket midpoint and mean per-bucket munāsaba score (across 5
buckets) is **NEGATIVE** at p_empirical < α_bon = 0.000463.

Buckets: d ∈ {1, 2, 3-5, 6-10, 11+} with midpoints {1, 2, 4, 8, 50}.
Null: 10,000 surah-permutations (seed 20260414), recomputed ρ.

**Prior expectation**: NULL, given the H-META-1 macro-regime refutation.

### Sub-test B — Local-pairwise d=1 seam coherence (local regime)

**H-CLASSIC-44-B (locked, one-sided):** mean munāsaba score over
adjacent-surah pairs (d = 1, all 113 pairs) is **above** the 99th
percentile of the null distribution where pair identities are
randomized under surah-permutation (10,000 perms, seed 20260414+1).
Pass threshold: empirical one-sided p < α_bon = 0.000463.

**Prior expectation**: PASS, given T-002 z = +10.06.

### Sub-test C — Regime-discrimination diagnostic

**H-CLASSIC-44-C-primary (locked, one-sided):** the ratio R = (mean d=1
score) / (mean d=11+ score) is **above** the 99th percentile of the
null ratio distribution under 10,000 surah-permutations
(seed 20260414+2). Pass threshold: empirical one-sided p < α_bon = 0.000463.

**H-CLASSIC-44-C-secondary (locked, diagnostic — NOT verdict-entering):**
the absolute difference D = (mean d=1 score) − (mean d=11+ score) is
also computed and compared to its own permutation null. The difference
is reported alongside the ratio in the verdict JSON. If the ratio
FAILS but the difference PASSES at empirical p < α_bon, this is an
AMBIGUOUS-RATIO-NOISE-LIMIT cell and the primary-statistic verdict
stands as FAIL with a flag to skeptical-auditor. **No post-hoc
switching to difference-as-primary.**

**Prior expectation**: PASS on ratio (consistent with regime-cut
hypothesis).

## Pre-registered operationalization

### Munāsaba score (LOCKED; unchanged from pre-pilot)

For each unordered pair of surahs (A, B) with A ≠ B, the munāsaba
score M(A, B) is the mean of two locked components:

1. **Root-Jaccard component J(A, B)**: |R_A ∩ R_B| / |R_A ∪ R_B|,
   where R_S is the set of QAC STEM-only root strings appearing in
   surah S. Function-word roots are NOT removed.

2. **Length-residualized gzip pair-compression Δ(A, B)**:
   Δ_raw = |gzip(text_A)| + |gzip(text_B)| − |gzip(text_A + " " + text_B)|,
   normalized by (|text_A| + |text_B|) / 2, then residualized on
   log(|text_A| * |text_B|) via OLS.

**Locked combination**: M(A, B) = 0.5 * J_std(A, B) + 0.5 * Δ_std(A, B),
where J_std and Δ_std are z-scored across all 6441 unordered pairs.

Divine-name and proper-noun components from the spec are DROPPED from
the primary score (external annotation TSV not integrated).

### Muqaṭṭaʿāt confound reporting (LOCKED)

All three sub-tests are run TWICE:
- **With muqaṭṭaʿāt-adjacent pairs**: full 6441-pair corpus
- **Without muqaṭṭaʿāt-adjacent pairs**: exclude d=1 pairs where at
  least one surah is in MUQATTAAT = {2, 3, 7, 10, 11, 12, 13, 14, 15,
  19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45,
  46, 50, 68}

The **primary verdict uses the muqaṭṭaʿāt-included version** for all
three sub-tests (consistency with T-002's original scoring). The
muqaṭṭaʿāt-excluded rerun is a CONFOUND DIAGNOSTIC. If primary ≠
muqaṭṭaʿāt-excluded on ANY sub-test, the verdict cell is post-fixed
with MUQATTAAT-CONFOUND-FLAG.

### Null model (LOCKED)

For each sub-test, randomly permute the 114 surahs 10,000 times. Each
permutation re-assigns distances to the FIXED pair-score matrix
(scores unchanged; only the (A, B) → d mapping changes under the
permuted canonical order). Seeds:
- Sub-test A: 20260414
- Sub-test B: 20260415
- Sub-test C: 20260416

### Pass rules (LOCKED)

Each sub-test PASSES if its one-sided empirical p < α_bon = 0.000463.

## Pre-registered 6-cell verdict matrix

| Sub-test A | Sub-test B | Sub-test C | Verdict |
|---|---|---|---|
| PASS | PASS | PASS | **STRONG PASS** — both regimes survive |
| PASS | PASS | NULL | **PASS-FLAT** |
| NULL | PASS | PASS | **PASS-LOCAL-ONLY** — matches H-META-1 prior |
| PASS | NULL | NULL | **PASS-MACRO-ONLY** — surprise, escalate |
| NULL | NULL | any | **NULL** — al-Zarkashī refuted |
| any | any | REVERSE | **REVERSE** |
| any | any | AMBIGUOUS-RATIO-NOISE-LIMIT | **PARTIAL** |

**Expected cell**: PASS-LOCAL-ONLY.

**REVERSE cell**: Spearman ρ > 0 on sub-test A at p < α_bon, OR
sub-test C ratio R < 1 at p < α_bon (d=1 systematically LOWER than d=11+).

## No-fork protections

1. Munāsaba score LOCKED as 0.5 * J_std + 0.5 * Δ_std.
2. Distance buckets LOCKED to {1, 2, 3-5, 6-10, 11+} midpoints {1, 2, 4, 8, 50}.
3. Sub-test A statistic LOCKED as Spearman ρ across 5 bucket means.
4. Sub-test B statistic LOCKED as mean(d=1 score) vs permutation null.
5. Sub-test C primary statistic LOCKED as RATIO; secondary DIFFERENCE
   is diagnostic only.
6. Null seeds LOCKED (20260414, 20260415, 20260416), 10,000 perms each.
7. α_bon = 0.000463 (triple-nested hierarchical: wave k=6, family k=6, sub-test k=3 → 0.05/108).
8. Muqaṭṭaʿāt-adjacent: INCLUDED in primary, excluded version is a
   diagnostic flag. Muqaṭṭaʿāt set LOCKED to 29 traditional surahs.
9. Root extraction LOCKED to QAC v0.4 STEM-only.
10. 6-cell verdict matrix LOCKED per task #95 spec.

## Outputs

- JSON: `findings/phase-b-hypotheses/csv/h-classic-44.json`
- Narrative: `findings/phase-b-hypotheses/h-classic-44.md`
- Script: `scripts/h_classic_44_zarkashi_regime.py`
- Pre-pilot: `scratch/h_classic_44_pre_pilot/h-classic-44-pre-pilot-single-test.json`

## Pre-execution lock confirmation

This file is committed BEFORE the revised script is written. The
pre-pilot run is DISCLOSED, not used. Seed, score composition, buckets,
three-sub-test structure, 6-cell verdict matrix, triple-nested hierarchical
Bonferroni α = 0.000463, and MUQATTAAT set are LOCKED.

## Garden-of-forking-paths disclosure (mandatory per team-lead MW-5 discipline)

A non-compliant pre-pilot run (single distance-decay test at α=0.0083) was
completed on 2026-04-14 before the computational-tester noticed that the
task #95 description had been updated with the 3-sub-test hierarchical-
Bonferroni specification. The pre-pilot produced ρ = −1.0000 at the
non-compliant α, and its muqaṭṭaʿāt-adjacency stratification descriptively
showed that the d=1 bucket's monotone signal was partly driven by opener-
letter-cluster adjacency (39 of the d=1 pairs). This pre-pilot was saved
to scratch and NOT filed as verdict. The compliant 3-sub-test run under
this pre-registration reuses the same pair-score matrix; the analyst was
not blinded to the pre-pilot outcome at the time of compliant execution.
This disclosure is filed under MW-5 discipline; the finding's verdict-to-
pre-pilot relationship is explicit.

## Data reuse disclosure

- Reuses QAC loader from `scripts/h_classic_47_biqai_seam.py`.
- Reuses pair-score computation from the pre-pilot run
  (`scripts/h_classic_44_zarkashi_decay.py`, now scratch-only).
- Reuses `quran-text/quran-no-tashkeel.json` and QAC v0.4 morphology.
- Cross-refs: `findings/cross-finding/scholar-convergence-tracker.md`
  §2, §3, §5 MANDATORY in results header per task #95 spec.
